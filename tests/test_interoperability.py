from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "incidents.csv"
MAPPING = ROOT / "mapping" / "interoperability-map-v1.json"
SCHEMA = ROOT / "schema" / "interoperability-export.schema.json"
SCRIPT = ROOT / "scripts" / "export_interoperability.py"


def source_rows():
    with SOURCE.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def run_export(tmp_path: Path, stem: str = "interop"):
    output = tmp_path / f"{stem}.json"
    sha_output = tmp_path / f"{stem}.sha256"
    subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--source",
            str(SOURCE),
            "--mapping",
            str(MAPPING),
            "--output",
            str(output),
            "--sha-output",
            str(sha_output),
        ],
        check=True,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return output, sha_output


def test_mapping_covers_all_oecd_criteria_and_aiid_core_concepts():
    mapping = json.loads(MAPPING.read_text(encoding="utf-8"))
    oecd = mapping["oecd_common_reporting_framework"]
    assert [item["id"] for item in oecd] == list(range(1, 30))
    assert [item["id"] for item in oecd if item["mandatory"]] == [1, 2, 3, 4, 7, 10, 11]

    aiid_concepts = {item["concept"] for item in mapping["aiid_core"]}
    assert {
        "incident_number",
        "incident_title",
        "description",
        "incident_date",
        "developer_entities",
        "deployer_entities",
        "harmed_or_nearly_harmed_parties",
        "supporting_reports",
        "taxonomy_annotations",
    } <= aiid_concepts


def test_export_is_byte_deterministic_and_hash_matches(tmp_path):
    first, first_sha = run_export(tmp_path, "first")
    second, second_sha = run_export(tmp_path, "second")

    assert first.read_bytes() == second.read_bytes()
    digest = hashlib.sha256(first.read_bytes()).hexdigest()
    assert first_sha.read_text(encoding="utf-8").strip() == f"{digest}  first.json"
    assert second_sha.read_text(encoding="utf-8").strip() == f"{digest}  second.json"


def test_export_validates_against_schema_and_covers_seed(tmp_path):
    output, _ = run_export(tmp_path)
    payload = json.loads(output.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(payload)

    rows = sorted(source_rows(), key=lambda row: row["incident_id"])
    assert payload["source_dataset"]["record_count"] == len(rows) == 17
    assert [record["aaio"]["incident_id"] for record in payload["records"]] == [
        row["incident_id"] for row in rows
    ]


def test_export_preserves_evidence_confidence_and_source_calibration(tmp_path):
    output, _ = run_export(tmp_path)
    payload = json.loads(output.read_text(encoding="utf-8"))
    rows = {row["incident_id"]: row for row in source_rows()}

    for record in payload["records"]:
        source = rows[record["aaio"]["incident_id"]]
        provenance = record["aaio"]["provenance"]
        assert provenance["evidence_confidence"] == source["evidence_confidence"]
        assert provenance["qualification_basis"] == source["qualification_basis"]
        assert provenance["source_calibration_notes"] == source["notes"]
        assert provenance["last_verified"] == source["last_verified"]
        assert provenance["curator"] == source["curator"]
        assert provenance["sources"][0]["url"] == source["source_1_url"]
        assert provenance["sources"][1]["url"] == source["source_2_url"]


def test_aiid_alignment_is_explicitly_non_inventive(tmp_path):
    output, _ = run_export(tmp_path)
    payload = json.loads(output.read_text(encoding="utf-8"))
    rows = {row["incident_id"]: row for row in source_rows()}

    for record in payload["records"]:
        incident_id = record["aaio"]["incident_id"]
        source = rows[incident_id]
        aiid = record["alignments"]["aiid_core"]
        assert aiid["existing_incident"]["incident_id"] == int(source["aiid_id"])
        assert aiid["existing_incident"]["url"] == source["aiid_url"]
        assert aiid["existing_incident"]["status"] == "cross_reference_only"
        assert aiid["entities"]["developer"] == {"value": None, "status": "unmapped"}
        assert aiid["entities"]["deployer"] == {"value": None, "status": "unmapped"}
        assert aiid["taxonomy_annotations"]["value"] is None
        assert aiid["taxonomy_annotations"]["status"] == "unmapped"


def test_oecd_alignment_flags_non_equivalent_fields_instead_of_guessing(tmp_path):
    output, _ = run_export(tmp_path)
    payload = json.loads(output.read_text(encoding="utf-8"))

    for record in payload["records"]:
        oecd = record["alignments"]["oecd_common_reporting_framework"]
        criteria = oecd["criteria"]
        assert sorted(map(int, criteria.keys())) == list(range(1, 30))
        assert criteria["1"]["status"] == "direct" and criteria["1"]["value"]
        assert criteria["2"]["status"] == "direct" and criteria["2"]["value"]
        assert criteria["3"]["status"] == "unmapped" and criteria["3"]["value"] is None
        assert criteria["9"]["status"] == "unmapped" and criteria["9"]["value"] is None
        assert criteria["10"]["status"] == "unmapped" and criteria["10"]["value"] is None
        assert criteria["10"]["raw_aaio_value"]["score"] == record["aaio"]["severity"]["score"]
        assert criteria["11"]["status"] == "approximate" and criteria["11"]["value"] is None
        assert criteria["11"]["raw_aaio_value"] == record["aaio"]["harm_types"]
        assert criteria["14"]["status"] == "approximate" and criteria["14"]["value"] is None
        assert criteria["17"]["status"] == "approximate" and criteria["17"]["value"] is None
        assert criteria["20"]["value"] is None
        assert criteria["25"]["value"] is None
        assert oecd["strict_mandatory_mapping"]["complete"] is False
        assert oecd["strict_mandatory_mapping"]["missing_or_non_direct"] == [3, 4, 10, 11]


def test_source_and_mapping_hashes_are_embedded(tmp_path):
    output, _ = run_export(tmp_path)
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["source_dataset"]["sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    assert payload["mapping"]["sha256"] == hashlib.sha256(MAPPING.read_bytes()).hexdigest()
