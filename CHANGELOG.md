# Changelog

## 0.2.3 - 2026-09-16

### Added
- Verified Zenodo archive metadata for AAIO v0.2.0, including version DOI `10.5281/zenodo.22789832` and concept DOI `10.5281/zenodo.22789831`.
- `metadata/archived-releases.json` mapping the archived release to its exact source commit, GitHub release, Zenodo landing page and deposited ZIP checksums.
- DOI relationship checks in machine-readable metadata validation.

### Changed
- README, dataset card, `CITATION.cff`, Data Package metadata and Schema.org JSON-LD now distinguish the evolving repository from the exact DOI-backed v0.2.0 snapshot.
- `docs/impact.md` records the persistent archive separately from independent reuse or adoption evidence.

### Research significance
- v0.2.3 closes the provenance loop between the evolving AAIO repository and a stable, citable research-data snapshot without treating DOI minting as evidence of external adoption.

## 0.2.2 - 2026-09-16

### Added
- `scripts/check_source_health.py` for deduplicated monitoring of public evidence URLs across core, multilingual, operational and watchlist layers.
- Conservative link-health categories that distinguish `access_blocked`, `not_found`, server failures and network failures rather than treating every non-2xx response as a dead source.
- Weekly GitHub Actions source-health audit with JSON and Markdown reports uploaded as temporary workflow artifacts.
- `docs/source-resilience.md` documenting interpretation boundaries, request strategy, maintenance response and copyright-safe source replacement practices.
- Non-network tests for source inventory, provenance preservation, status classification and inventory-only reporting.

### Changed
- Dataset discovery metadata now records periodic public evidence link-health monitoring as a maintenance technique.
- README now surfaces source resilience as part of AAIO's provenance model.

### Research significance
- v0.2.2 extends provenance from recording *which evidence supports an incident* to monitoring *whether that evidence remains practically reviewable over time*. The audit is deliberately non-blocking because bot protection, rate limits and temporary outages do not determine evidence validity.

## 0.2.1 - 2026-09-16

### Added
- `datapackage.json` machine-readable descriptor for the core, multilingual, operational, watchlist and record-history resources.
- Schema.org `Dataset` JSON-LD metadata at `metadata/aaio-dataset.jsonld` for machine discovery.
- A comprehensive `docs/dataset-card.md` documenting motivation, composition, collection process, intended uses, limitations, ethics, maintenance and interoperability.
- `scripts/validate_metadata.py` to enforce version, license, resource-path and machine-readable metadata consistency.

### Changed
- Release validation now preserves historical promotion provenance across later patch releases instead of incorrectly requiring every promotion to occur in the current version.
- Release-integrity tests are version-aware and explicitly preserve the v0.2.0 origin of the two operational-to-core promotions.
- README navigation and research-data documentation now surface machine-readable metadata, the dataset card and the evidence pipeline more prominently.
- CI validates machine-readable research-data metadata alongside the existing incident, multilingual, operational, release and interoperability checks.

### Research significance
- v0.2.1 strengthens AAIO as a reusable research dataset rather than only a GitHub project. The new metadata layer improves machine discovery, documentation quality and downstream reuse while preserving the project's existing claim boundaries.

## 0.2.0 - 2026-09-15

### Added
- Two operational AI incidents promoted into the versioned core dataset, expanding coverage into Kenyan clinical decision support and South African professional legal research.
- Append-only `data/record_history.csv` for material record changes and promotion provenance.
- Explicit repository `VERSION` marker and release-consistency validation.
- Promotion traceability from `AAIO-OP-*` staging records to stable core incident IDs.
- Release and provenance policy covering semantic-style versioning, correction history, release gates and DOI archiving discipline.
- Public impact/adoption ledger and an AIID submission packet for original AAIO cases.
- Dashboard pipeline/provenance views and a direct incident-submission path.

### Changed
- Core dataset increased from 17 to 19 records while retaining 9 primary African countries.
- Operational evidence validation now checks promoted core IDs and release metadata.
- Dashboard version is read from the canonical `VERSION` file rather than hard-coded.
- CI now validates release metadata and material record history in addition to data, multilingual evidence, operational evidence, pytest and deterministic interoperability export generation.

### Research significance
- v0.2.0 moves AAIO beyond a synthetic-media-heavy seed by incorporating a peer-reviewed deployed-healthcare safety case and a direct judicial record of professional generative-AI failure.
- The release deliberately preserves the distinction between evidence strength, severity, candidate evidence and confirmed core incidents.

## 0.1.2 - 2026-09-09

### Added
- A source-led multilingual incident register with initial francophone, arabophone and lusophone African cases.
- Preservation of original-language source URLs and headlines alongside conservative English curator summaries.
- Explicit translation method, translation-uncertainty and AI-attribution-strength fields.
- A documented multilingual evidence and core-promotion protocol.
- Automated validation and tests requiring all three issue #2 language families, source provenance and translation calibration.

### Changed
- CI now validates multilingual evidence separately from the core incident dataset and interoperability export.

## 0.1.1 - 2026-09-09

### Added
- Versioned AIID/OECD semantic interoperability mapping covering all 29 OECD common-reporting criteria.
- Deterministic interoperability JSON export with embedded source/mapping SHA-256 hashes and a companion manifest.
- JSON Schema and tests for the interoperability export across all 17 v0.1.0 seed records.
- Explicit mapping-gap handling that preserves AAIO evidence confidence and source-calibration notes without fabricating external taxonomy values.

### Changed
- Expanded interoperability documentation with field-level mapping, limitations, provenance rules and non-equivalence safeguards.
- CI now smoke-tests interoperability export generation in addition to dataset validation and pytest.

## 0.1.0 - 2026-09-08

### Added
- 17 source-traceable seed incident records.
- Conservative watchlist for automated/algorithmic cases without sufficient AI attribution.
- Evidence-confidence and transparent severity rubrics.
- JSON Schema, deterministic validation and tests.
- Streamlit explorer and reproducible analysis script.
- Contributor, correction, ethics, security and interoperability documentation.
