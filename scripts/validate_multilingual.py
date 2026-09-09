#!/usr/bin/env python3
"""Validate AAIO's multilingual incident-evidence register."""
from pathlib import Path
import csv
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "multilingual_incidents.csv"

REQUIRED_FIELDS = {
    "record_id", "country", "region", "source_language", "language_family",
    "incident_date", "date_precision", "incident_title_en", "english_curator_summary",
    "system_type", "harm_types", "source_name", "source_title_original", "source_url",
    "source_published_date", "source_type", "ai_attribution_strength", "translation_method",
    "translation_uncertainty", "translation_uncertainty_note", "core_status",
    "last_verified", "curator",
}
REQUIRED_FAMILIES = {"francophone", "arabophone", "lusophone"}
LANGUAGE_FOR_FAMILY = {
    "francophone": "French",
    "arabophone": "Arabic",
    "lusophone": "Portuguese",
}
ALLOWED_UNCERTAINTY = {"low", "medium", "high"}
ALLOWED_ATTRIBUTION = {"confirmed", "probable", "reported", "uncertain"}
ALLOWED_STATUS = {"candidate_for_core", "promoted_to_core", "watchlist", "excluded"}


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    errors = []
    with DATA.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = sorted(REQUIRED_FIELDS - fields)
        if missing:
            errors.append("Missing columns: " + ", ".join(missing))
        rows = list(reader)

    ids = set()
    families = set()
    for index, row in enumerate(rows, 1):
        rid = row.get("record_id", "")
        if not re.fullmatch(r"AAIO-ML-\d{4}", rid):
            errors.append(f"Record {index}: invalid record_id {rid!r}")
        if rid in ids:
            errors.append(f"Record {index}: duplicate record_id {rid}")
        ids.add(rid)

        family = row.get("language_family", "")
        families.add(family)
        if family not in REQUIRED_FAMILIES:
            errors.append(f"{rid}: unsupported initial language_family {family!r}")
        expected_language = LANGUAGE_FOR_FAMILY.get(family)
        if expected_language and row.get("source_language") != expected_language:
            errors.append(f"{rid}: {family} must use source_language={expected_language}")

        if not valid_url(row.get("source_url", "")):
            errors.append(f"{rid}: invalid source_url")
        if not row.get("source_title_original", "").strip():
            errors.append(f"{rid}: original-language title is required")
        if not row.get("english_curator_summary", "").strip():
            errors.append(f"{rid}: English curator summary is required")
        if len(row.get("english_curator_summary", "").split()) < 25:
            errors.append(f"{rid}: English curator summary is too short for calibrated context")

        uncertainty = row.get("translation_uncertainty")
        if uncertainty not in ALLOWED_UNCERTAINTY:
            errors.append(f"{rid}: invalid translation_uncertainty {uncertainty!r}")
        if not row.get("translation_uncertainty_note", "").strip():
            errors.append(f"{rid}: translation uncertainty requires an explanatory note")
        if not row.get("translation_method", "").strip():
            errors.append(f"{rid}: translation method is required")

        attribution = row.get("ai_attribution_strength")
        if attribution not in ALLOWED_ATTRIBUTION:
            errors.append(f"{rid}: invalid ai_attribution_strength {attribution!r}")
        status = row.get("core_status")
        if status not in ALLOWED_STATUS:
            errors.append(f"{rid}: invalid core_status {status!r}")

    missing_families = sorted(REQUIRED_FAMILIES - families)
    if missing_families:
        errors.append("Missing required language families: " + ", ".join(missing_families))

    if len(rows) < 3:
        errors.append("Multilingual register must contain at least one record per target language family")

    if errors:
        print("\n".join("ERROR: " + error for error in errors))
        return 1
    print(
        f"OK: {len(rows)} multilingual records validated across "
        f"{', '.join(sorted(families))}; original links, summaries and translation uncertainty are present."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
