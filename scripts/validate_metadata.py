#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
PACKAGE = ROOT / "datapackage.json"
JSONLD = ROOT / "metadata" / "aaio-dataset.jsonld"
ARCHIVES = ROOT / "metadata" / "archived-releases.json"
CITATION = ROOT / "CITATION.cff"
DOI_RE = re.compile(r"^10\.5281/zenodo\.\d+$")


def main() -> int:
    errors: list[str] = []

    try:
        package = json.loads(PACKAGE.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: could not parse datapackage.json: {exc}")
        return 1

    try:
        jsonld = json.loads(JSONLD.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: could not parse metadata/aaio-dataset.jsonld: {exc}")
        return 1

    try:
        archives = json.loads(ARCHIVES.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: could not parse metadata/archived-releases.json: {exc}")
        return 1

    if package.get("name") != "africa-ai-incident-observatory":
        errors.append("datapackage name must be africa-ai-incident-observatory")
    if package.get("version") != VERSION:
        errors.append(f"datapackage version {package.get('version')} != VERSION {VERSION}")
    if package.get("profile") != "data-package":
        errors.append("datapackage profile must be data-package")

    licenses = package.get("licenses", [])
    if not any(item.get("name") == "CC-BY-4.0" for item in licenses if isinstance(item, dict)):
        errors.append("datapackage must declare CC-BY-4.0 data license")

    resources = package.get("resources", [])
    if not resources:
        errors.append("datapackage must contain resources")
    resource_names: set[str] = set()
    for resource in resources:
        if not isinstance(resource, dict):
            errors.append("datapackage resource must be an object")
            continue
        name = str(resource.get("name", "")).strip()
        path = str(resource.get("path", "")).strip()
        if not name:
            errors.append("datapackage resource missing name")
        if name in resource_names:
            errors.append(f"duplicate datapackage resource name: {name}")
        resource_names.add(name)
        if resource.get("profile") != "tabular-data-resource":
            errors.append(f"resource {name or '<unnamed>'} must use tabular-data-resource profile")
        if not path:
            errors.append(f"resource {name or '<unnamed>'} missing path")
        elif not (ROOT / path).exists():
            errors.append(f"resource path does not exist: {path}")
        schema = resource.get("schema")
        if schema:
            schema_path = ROOT / str(schema)
            if not schema_path.exists():
                errors.append(f"resource schema path does not exist: {schema}")
            else:
                try:
                    json.loads(schema_path.read_text(encoding="utf-8"))
                except Exception as exc:
                    errors.append(f"resource schema is not valid JSON: {schema}: {exc}")

    expected_resources = {
        "core-incidents",
        "multilingual-evidence",
        "operational-evidence",
        "watchlist",
        "record-history",
    }
    if not expected_resources <= resource_names:
        errors.append(
            "datapackage missing expected resources: "
            + ", ".join(sorted(expected_resources - resource_names))
        )

    core = next((r for r in resources if isinstance(r, dict) and r.get("name") == "core-incidents"), None)
    if not core or core.get("schema") != "schema/core-table-schema.json":
        errors.append("core-incidents must reference schema/core-table-schema.json")

    if jsonld.get("@context") != "https://schema.org":
        errors.append("JSON-LD @context must be https://schema.org")
    if jsonld.get("@type") != "Dataset":
        errors.append("JSON-LD @type must be Dataset")
    if jsonld.get("version") != VERSION:
        errors.append(f"JSON-LD version {jsonld.get('version')} != VERSION {VERSION}")
    if jsonld.get("license") != "https://creativecommons.org/licenses/by/4.0/":
        errors.append("JSON-LD must declare the CC BY 4.0 license URL")
    if not jsonld.get("description"):
        errors.append("JSON-LD description is required")
    if not jsonld.get("creator", {}).get("name"):
        errors.append("JSON-LD creator name is required")
    if not jsonld.get("distribution"):
        errors.append("JSON-LD must describe at least one distribution")

    concept_doi = str(archives.get("concept_doi", "")).strip()
    if not DOI_RE.fullmatch(concept_doi):
        errors.append("archive registry concept_doi must be a Zenodo DOI")
    if archives.get("concept_doi_url") != f"https://doi.org/{concept_doi}":
        errors.append("archive registry concept DOI URL does not match concept_doi")

    archived_releases = archives.get("releases", [])
    if not isinstance(archived_releases, list) or not archived_releases:
        errors.append("archive registry must contain at least one release")
    else:
        versions: set[str] = set()
        for release in archived_releases:
            if not isinstance(release, dict):
                errors.append("archive release entry must be an object")
                continue
            version = str(release.get("version", "")).strip()
            version_doi = str(release.get("version_doi", "")).strip()
            source_commit = str(release.get("source_commit", "")).strip()
            if not version:
                errors.append("archive release missing version")
            elif version in versions:
                errors.append(f"duplicate archived release version: {version}")
            versions.add(version)
            if not DOI_RE.fullmatch(version_doi):
                errors.append(f"archived release {version or '<unknown>'} has invalid version DOI")
            if version_doi == concept_doi:
                errors.append(f"archived release {version or '<unknown>'} must not reuse concept DOI as version DOI")
            if release.get("version_doi_url") != f"https://doi.org/{version_doi}":
                errors.append(f"archived release {version or '<unknown>'} DOI URL mismatch")
            if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
                errors.append(f"archived release {version or '<unknown>'} must record a 40-character source commit")
            if not str(release.get("github_release", "")).startswith("https://github.com/"):
                errors.append(f"archived release {version or '<unknown>'} missing GitHub release URL")
            if not str(release.get("zenodo_record", "")).startswith("https://zenodo.org/records/"):
                errors.append(f"archived release {version or '<unknown>'} missing Zenodo record URL")
            if not re.fullmatch(r"[0-9a-f]{32}", str(release.get("archive_md5", ""))):
                errors.append(f"archived release {version or '<unknown>'} missing valid archive MD5")
            if not re.fullmatch(r"[0-9a-f]{64}", str(release.get("archive_sha256", ""))):
                errors.append(f"archived release {version or '<unknown>'} missing valid archive SHA-256")

    package_aaio = package.get("_aaio", {})
    if package_aaio.get("archived_releases") != "metadata/archived-releases.json":
        errors.append("datapackage must point to metadata/archived-releases.json")
    if package_aaio.get("concept_doi") != concept_doi:
        errors.append("datapackage concept DOI must match archive registry")

    jsonld_identifier = jsonld.get("identifier", {})
    if not isinstance(jsonld_identifier, dict) or jsonld_identifier.get("value") != concept_doi:
        errors.append("JSON-LD identifier must use the archive concept DOI")

    citation_text = CITATION.read_text(encoding="utf-8")
    if f'version: "{VERSION}"' not in citation_text:
        errors.append("CITATION.cff version does not match VERSION")
    if concept_doi not in citation_text:
        errors.append("CITATION.cff must include the concept DOI")
    for release in archived_releases if isinstance(archived_releases, list) else []:
        if isinstance(release, dict):
            version_doi = str(release.get("version_doi", "")).strip()
            if version_doi and version_doi not in citation_text:
                errors.append(f"CITATION.cff missing archived version DOI {version_doi}")

    if errors:
        print("\n".join("ERROR: " + error for error in errors))
        return 1

    print(
        f"OK: machine-readable metadata validated for AAIO v{VERSION}; "
        f"{len(resources)} packaged resources and {len(archived_releases)} archived release(s) are present."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
