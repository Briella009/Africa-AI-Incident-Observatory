import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "multilingual_incidents.csv"


def rows():
    with DATA.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_validator_passes():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_multilingual.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_all_issue_2_language_families_are_represented():
    by_family = {row["language_family"] for row in rows()}
    assert {"francophone", "arabophone", "lusophone"} <= by_family


def test_original_language_evidence_is_preserved():
    for row in rows():
        assert row["source_url"].startswith(("http://", "https://"))
        assert row["source_title_original"].strip()
        assert row["source_language"] in {"French", "Arabic", "Portuguese"}


def test_english_summary_does_not_replace_translation_metadata():
    for row in rows():
        assert len(row["english_curator_summary"].split()) >= 25
        assert row["translation_method"].strip()
        assert row["translation_uncertainty"] in {"low", "medium", "high"}
        assert row["translation_uncertainty_note"].strip()


def test_ai_attribution_is_calibrated():
    indexed = {row["record_id"]: row for row in rows()}
    # AFP's Burkina Faso source is probabilistic about AI involvement.
    assert indexed["AAIO-ML-0001"]["ai_attribution_strength"] == "probable"
    assert "very probably" in indexed["AAIO-ML-0001"]["english_curator_summary"].lower()
    # The Arabic and Portuguese fact-checks directly identify AI generation/manipulation.
    assert indexed["AAIO-ML-0002"]["ai_attribution_strength"] == "confirmed"
    assert indexed["AAIO-ML-0003"]["ai_attribution_strength"] == "confirmed"


def test_discovery_does_not_silently_promote_records_to_core():
    assert all(row["core_status"] == "candidate_for_core" for row in rows())
