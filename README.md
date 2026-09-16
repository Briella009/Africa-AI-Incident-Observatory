# Africa AI Incident Observatory

**A source-traceable, open research dataset for documenting AI incidents affecting African people, institutions and information environments.**

[![Live Dashboard](https://img.shields.io/badge/Live%20Dashboard-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://aaio-africa.streamlit.app/)
[![Validate data](https://github.com/Briella009/Africa-AI-Incident-Observatory/actions/workflows/validate-data.yml/badge.svg)](https://github.com/Briella009/Africa-AI-Incident-Observatory/actions/workflows/validate-data.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22789831.svg)](https://doi.org/10.5281/zenodo.22789831)
![Records](https://img.shields.io/badge/verified%20core%20records-19-0f766e)
![Version](https://img.shields.io/badge/dataset-v0.2.3-516b78)
![License](https://img.shields.io/badge/code-MIT-blue)
![Data](https://img.shields.io/badge/data-CC%20BY%204.0-green)

**Dashboard:** https://aaio-africa.streamlit.app/

**Current dataset:** v0.2.3 · 19 curated core records · 9 primary African countries · 3 multilingual source families · operational evidence provenance · AIID/OECD semantic interoperability · scheduled public-source resilience monitoring · DOI-backed v0.2.0 archive

**Quick links:** [Explore data](data/incidents.csv) · [Dashboard](https://aaio-africa.streamlit.app/) · [Methodology](docs/methodology.md) · [Dataset card](docs/dataset-card.md) · [Data dictionary](docs/data-dictionary.md) · [Interoperability](docs/interoperability.md) · [Source resilience](docs/source-resilience.md) · [Archived releases](metadata/archived-releases.json) · [Contribute](https://github.com/Briella009/Africa-AI-Incident-Observatory/issues/new?template=incident_submission.yml) · [Citation](CITATION.cff)

## Why this exists

AI failures become useful public evidence only when they are documented consistently enough to compare, audit and learn from.

In August 2026, the AI Incident Database reported that, from February 2020 through July 2026, African incidents represented roughly **1.3% of records in the OECD AI Incidents and Hazards Monitor and 4.2% of records in AIID**. AIID argued that this reflects a structural visibility and reporting problem rather than evidence that Africa experiences unusually few AI harms.

The **Africa AI Incident Observatory (AAIO)** is an independent, open-data response to that gap. It turns scattered public reports into structured incident records while preserving source provenance, uncertainty, evidence quality and the path by which a candidate becomes a core record.

> **AAIO is not an official AIID, OECD, NIST, African Union or government project.** It links to those resources where relevant and does not claim their endorsement.

## What makes AAIO different

| Design choice | Why it matters |
|---|---|
| **Evidence confidence is separate from severity** | A serious allegation does not become a high-confidence fact simply because the potential harm is large. |
| **Watchlist instead of forced classification** | Automated, biometric or algorithmic cases remain visible without being mislabeled as AI incidents when AI linkage is weak. |
| **Multilingual discovery keeps translation uncertainty** | French-, Arabic- and Portuguese-language evidence can be reviewed without presenting translated summaries as original-source text. |
| **Operational staging keeps promotion history** | Deployed-healthcare and professional-use cases retain staging IDs and release provenance after promotion into the core dataset. |
| **Interoperability does not fabricate equivalence** | Non-equivalent OECD/AIID fields remain partial, approximate or unmapped rather than receiving invented normalized values. |
| **Material changes are auditable** | Core-record promotions and substantive corrections are tracked in an append-only history ledger. |
| **Machine-readable research metadata** | Data Package metadata, a tabular schema, Schema.org JSON-LD and `CITATION.cff` make the dataset easier to inspect and reuse programmatically. |
| **Persistent release provenance** | DOI-backed snapshots are mapped to exact source commits, release URLs and deposited-file checksums rather than being treated as interchangeable with the evolving branch. |
| **Public evidence links are monitored over time** | A weekly audit identifies broken, blocked or unstable evidence URLs without confusing temporary web failures with evidence invalidity. |

## v0.2.3 — DOI-backed research archive

The **19 core incidents remain unchanged**. v0.2.3 connects the evolving repository to AAIO's first verified persistent research-data archive.

AAIO v0.2.0 is archived on Zenodo as a Dataset with version DOI **`10.5281/zenodo.22789832`**. The concept DOI **`10.5281/zenodo.22789831`** represents the AAIO archive across versions. The archive is tied to source commit `e5826b33fd8f4b9926a39707870e9ec93d739d4d`; machine-readable provenance is recorded in [`metadata/archived-releases.json`](metadata/archived-releases.json).

DOI minting is treated as persistent research infrastructure, not as evidence of independent adoption, citation or institutional use.

## v0.2.2 — source resilience

The **19 core incidents remain unchanged**. v0.2.2 strengthens the evidence infrastructure around them.

AAIO now maintains a deduplicated inventory of public evidence URLs and can audit their practical reachability across the core, multilingual, operational and watchlist layers. The audit distinguishes `not_found` from access blocking, rate limiting, server failures and network errors. It is deliberately **not a release gate** because bot protection and temporary outages do not determine whether an incident is valid.

A scheduled GitHub Actions workflow produces temporary JSON and Markdown reports, preserving the connection between each public URL and the AAIO records that rely on it. See [source resilience and link-health monitoring](docs/source-resilience.md).

## v0.2.1 — research-data readiness

v0.2.1 made AAIO easier to discover, understand, validate and reuse without changing the 19 core records established in v0.2.0. It added:

- `datapackage.json` describing the core and evidence-layer resources;
- `schema/core-table-schema.json` for typed, machine-readable structure of the core CSV;
- `metadata/aaio-dataset.jsonld` using Schema.org `Dataset` metadata;
- a comprehensive [dataset card](docs/dataset-card.md) covering motivation, composition, collection, intended uses, limitations, ethics and maintenance;
- automated metadata validation in CI; and
- version-aware release-integrity checks that preserve historical promotion provenance.

These additions are **FAIR-oriented**, not a claim of formal FAIR certification.

## Dataset snapshot

The current core dataset contains **19 source-traceable incidents** across **9 primary African countries**. It spans synthetic media, influence operations, health misinformation, financial scams, conflict information, model behaviour, government-policy integrity, clinical decision support and professional legal research.

The project also maintains:

- a multilingual discovery layer covering **francophone, arabophone and lusophone** source families;
- an operational evidence layer with promotion traceability;
- a conservative watchlist for relevant cases that do not yet meet the AI-linkage threshold;
- an append-only history ledger for material record changes; and
- a non-blocking source-resilience audit for public evidence links.

The dataset is intentionally **not comprehensive or prevalence-weighted**. Missing records do not imply missing harm, and country counts must not be interpreted as national AI-safety rankings.

### Primary countries currently represented

Nigeria, Zambia, Kenya, Ghana, Tanzania, Rwanda, Burkina Faso, South Africa and Sudan. Some incidents have cross-border effects.

## Evidence pipeline

AAIO keeps evidence review visible rather than collapsing everything into one table.

```text
Public source discovery
        ↓
Evidence review + AI-linkage check
        ↓
┌───────────────────────────────┐
│ Multilingual / operational    │
│ staging or conservative       │
│ watchlist                     │
└───────────────────────────────┘
        ↓ when threshold is met
Core incident record
        ↓
Versioned release + history ledger
        ↓
Interoperability export / upstream submission
        ↓
Ongoing public-source resilience monitoring
```

Promotion into the core dataset requires a credible AI linkage, a realised event, a material African nexus, traceable public evidence and wording calibrated to what the evidence actually establishes.

## Repository structure

### Core research data

- `data/incidents.csv` — versioned core incidents
- `data/multilingual_incidents.csv` — source-led multilingual evidence candidates
- `data/operational_incidents.csv` — operational evidence review and promotion records
- `data/watchlist.csv` — deliberately non-core technology-governance cases
- `data/record_history.csv` — append-only material-change ledger

### Schemas and machine-readable metadata

- `schema/incident.schema.json` — JSON Schema used by the core validator
- `schema/core-table-schema.json` — tabular schema for downstream CSV tooling
- `datapackage.json` — machine-readable resource descriptor
- `metadata/aaio-dataset.jsonld` — Schema.org dataset metadata
- `metadata/archived-releases.json` — DOI archive/version/commit/checksum registry
- `CITATION.cff` — citation metadata

### Methods and research documentation

- `docs/methodology.md` — inclusion, exclusion and verification methodology
- `docs/dataset-card.md` — dataset motivation, composition, intended uses, limitations and maintenance
- `docs/data-dictionary.md` — core field definitions
- `docs/severity-and-confidence.md` — severity and evidence-confidence rubric
- `docs/multilingual-evidence.md` — multilingual discovery and translation-calibration protocol
- `docs/operational-coverage.md` — operational expansion and negative-result discipline
- `docs/interoperability.md` — AIID/OECD semantic mapping and non-equivalence safeguards
- `docs/source-resilience.md` — public evidence link-health interpretation and maintenance protocol
- `docs/release-policy.md` — versioning, corrections, provenance and DOI discipline
- `docs/impact.md` — externally verifiable adoption, reuse and citation ledger
- `docs/aiid-submission-packet.md` — prepared upstream submission notes for original AAIO operational cases

### Validation and reproducibility

- `scripts/validate.py` — core schema, IDs, URLs and severity math
- `scripts/validate_multilingual.py` — multilingual provenance validation
- `scripts/validate_operational.py` — operational evidence and promotion validation
- `scripts/validate_release.py` — version, citation, promotion and history consistency
- `scripts/validate_metadata.py` — machine-readable metadata, archive DOI and resource consistency
- `scripts/export_interoperability.py` — deterministic AIID/OECD semantic export
- `scripts/check_source_health.py` — public evidence inventory and non-blocking link-health audit
- `app.py` — interactive Streamlit explorer

## Inclusion rule

A core record must satisfy all of the following:

1. **AI linkage** — a credible source connects the event to an AI system, model, AI-generated content or AI-enabled deployment.
2. **Realised event** — the record documents an event that occurred, not only a hypothetical risk.
3. **African nexus** — the event materially affects an African country, population, institution or information environment.
4. **Traceable evidence** — at least one credible, publicly reviewable source is available.
5. **Calibrated language** — uncertain claims remain labelled as alleged, purported, reported, believed or unverified where appropriate.

Cases relevant to automated decision-making but failing the AI-linkage threshold remain in the **watchlist**, not silently promoted to AI incidents.

## Evidence confidence

| Grade | Meaning |
|---|---|
| A | Strong evidence: primary/official evidence, direct admission, court record, peer-reviewed deployment evidence, or strong independent corroboration |
| B | Good evidence: credible independent reporting/fact-checking with direct technical or documentary support |
| C | Limited but credible: one strong source or material attribution uncertainty; wording must preserve uncertainty |
| D | Unverified/disputed: excluded from the core dataset |

Confidence measures **evidence quality**, not incident severity.

## Severity

AAIO uses a transparent project rubric based on four dimensions scored 0-4:

- magnitude of harm — 35%
- scale of exposure/affected population — 25%
- criticality (health, safety, rights, democracy, critical services) — 25%
- difficulty of reversal/remediation — 15%

The score is a **research aid, not an official legal or regulatory rating**. See [severity and confidence](docs/severity-and-confidence.md).

## Interoperability

AAIO provides a deterministic semantic alignment layer for AIID concepts and **all 29 criteria in the OECD common reporting framework**.

The exporter preserves AAIO evidence confidence, provenance and severity dimensions while refusing unsupported conversions. For example, AAIO severity is not silently converted into OECD severity, and AAIO affected-party labels are not presented as normalized AIID entities without review.

See [interoperability documentation](docs/interoperability.md).

## Reproducibility

Run the full structural validation path locally:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/validate.py
python scripts/validate_multilingual.py
python scripts/validate_operational.py
python scripts/validate_release.py
python scripts/validate_metadata.py
pytest -q
python scripts/export_interoperability.py \
  --output /tmp/aaio-interoperability-v1.json \
  --sha-output /tmp/aaio-interoperability-v1.sha256
python scripts/check_source_health.py --inventory-only
streamlit run app.py
```

A live source audit is intentionally separate because it depends on third-party web availability:

```bash
python scripts/check_source_health.py \
  --output /tmp/aaio-source-health.json \
  --markdown-output /tmp/aaio-source-health.md
```

Passing CI verifies AAIO's declared structural and consistency controls; it does not certify external source permanence or remove legitimate interpretive uncertainty.

## Explore the dashboard

The [live dashboard](https://aaio-africa.streamlit.app/) lets users:

- filter the core dataset by country, year, sector, severity and evidence confidence;
- inspect individual incident sources and caveats;
- compare evidence quality separately from severity;
- review multilingual and operational evidence pipelines;
- inspect material record history;
- review the conservative watchlist; and
- download filtered data.

## Contribute or challenge a record

Use the [structured Incident submission form](https://github.com/Briella009/Africa-AI-Incident-Observatory/issues/new?template=incident_submission.yml) for new evidence. Corrections and evidence-backed challenges are welcome; the goal is to make records more defensible over time, not simply more numerous.

Please do **not** submit private personal data, leaked credentials, graphic abuse material, operational instructions that enable wrongdoing, or unsupported allegations.

## Research foundation

- [AI Incident Database: Strengthening AI Incident Monitoring and Reporting in Africa for Global AI Safety](https://incidentdatabase.ai/blog/strengthening-ai-incident-monitoring-and-reporting-in-africa-for-global-ai-safety/)
- [OECD: Towards a common reporting framework for AI incidents](https://www.oecd.org/en/publications/towards-a-common-reporting-framework-for-ai-incidents_f326d4ac-en.html)
- [OECD AI Incidents and Hazards Monitor methodology](https://oecd.ai/en/incidents-methodology)
- [NIST AI Risk Management Framework / AIRC](https://airc.nist.gov/airmf-resources/airmf/)
- [African Union Continental Artificial Intelligence Strategy](https://au.int/en/documents/20240809/continental-artificial-intelligence-strategy)

## Citation and archiving

For analysis that depends on the exact archived dataset, cite **AAIO v0.2.0**:

> Ezeobioha, B. (2026). *Africa AI Incident Observatory (AAIO) v0.2.0* (Version 0.2.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.22789832

- **Version DOI — v0.2.0:** https://doi.org/10.5281/zenodo.22789832
- **Concept DOI — all archived AAIO versions:** https://doi.org/10.5281/zenodo.22789831
- **Zenodo record:** https://zenodo.org/records/22789832
- **Exact source commit:** `e5826b33fd8f4b9926a39707870e9ec93d739d4d`

Use the **version DOI** when exact reproducibility matters. Use the **concept DOI** when referring to AAIO as an evolving archived research resource. The current `main` branch may be newer than the latest archived snapshot, so the two should not be treated as byte-identical.

See [`CITATION.cff`](CITATION.cff) and [`metadata/archived-releases.json`](metadata/archived-releases.json) for machine-readable citation and archive provenance.

## Author

**Blessing Ezeobioha**  
Cybersecurity practitioner and AI researcher working across threat intelligence, AI governance and responsible technology in African contexts.

- GitHub: [@Briella009](https://github.com/Briella009)
- ORCID: [0009-0005-9972-9380](https://orcid.org/0009-0005-9972-9380)
