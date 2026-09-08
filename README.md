# Africa AI Incident Observatory

**A source-traceable, open dataset for documenting AI incidents affecting African people, institutions and information environments.**

[![Validate data](https://github.com/Briella009/Africa-AI-Incident-Observatory/actions/workflows/validate-data.yml/badge.svg)](https://github.com/Briella009/Africa-AI-Incident-Observatory/actions/workflows/validate-data.yml)
![Records](https://img.shields.io/badge/verified%20seed%20records-17-0f766e)
![License](https://img.shields.io/badge/code-MIT-blue)
![Data](https://img.shields.io/badge/data-CC%20BY%204.0-green)

**Seed release:** v0.1.0 · 17 curated records · 9 primary African countries · locally validated 8 September 2026

## Why this exists

AI failures become useful public evidence only when they are documented consistently enough to compare, audit and learn from.

In August 2026, the AI Incident Database reported that, from February 2020 through July 2026, African incidents represented roughly **1.3% of records in the OECD AI Incidents and Hazards Monitor and 4.2% of records in AIID**. AIID argued that this reflects a structural visibility and reporting problem rather than evidence that Africa experiences unusually few AI harms.

The **Africa AI Incident Observatory (AAIO)** is an independent, open-data response to that gap. It turns scattered public reports into structured incident records while preserving uncertainty and links back to the evidence.

> **This is not an official AIID, OECD, African Union or government project.** AAIO is an independent research and public-interest technology project. It links to those resources where relevant and does not claim their endorsement.

## Research foundation

- [AI Incident Database: Strengthening AI Incident Monitoring and Reporting in Africa for Global AI Safety](https://incidentdatabase.ai/blog/strengthening-ai-incident-monitoring-and-reporting-in-africa-for-global-ai-safety/)
- [OECD AI Incidents and Hazards Monitor methodology](https://oecd.ai/en/incidents-methodology)
- [NIST AI Risk Management Framework 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
- [African Union Continental Artificial Intelligence Strategy](https://au.int/en/documents/20240809/continental-artificial-intelligence-strategy)

## What is in the repository

- `data/incidents.csv` — curated core records that meet the inclusion threshold
- `scripts/export_json.py` — deterministic JSON export for downstream research workflows
- `data/watchlist.csv` — important automated/algorithmic cases excluded from the core dataset because AI causation is not sufficiently established
- `schema/incident.schema.json` — machine-readable record schema
- `docs/methodology.md` — inclusion, exclusion and verification methodology
- `docs/severity-and-confidence.md` — transparent severity and evidence-confidence rubric
- `docs/data-dictionary.md` — field definitions
- `docs/interoperability.md` — mapping notes for AIID/OECD/NIST-style workflows
- `docs/ethics.md` — safeguards against overclaiming, retraumatisation and unsafe publication
- `docs/publication-brief.md` — public-facing research framing, findings and claim limits
- `scripts/validate.py` — deterministic dataset validator
- `scripts/analyze.py` — reproducible summary statistics
- `app.py` — interactive Streamlit explorer
- `.github/ISSUE_TEMPLATE/incident_submission.yml` — structured community submission template

## Seed release

The seed release contains **17 source-traceable records** spanning misinformation, influence operations, health misinformation, financial scams, conflict information, model behaviour and government-policy integrity.

It is intentionally **not comprehensive**. The absence of a record for a country does **not** mean that no incident occurred. It means only that no qualifying record has yet been included in this release.

### Countries represented in the seed release

Nigeria, Zambia, Kenya, Ghana, Tanzania, Rwanda, Burkina Faso, South Africa and Sudan. Some incidents have cross-border effects.

## Inclusion rule

A core record must satisfy all of the following:

1. **AI linkage** — a credible source connects the event to an AI system, model, AI-generated content, or AI-enabled deployment.
2. **Realised event** — the record documents an incident, not only a hypothetical risk.
3. **African nexus** — the event materially affects an African country, population, institution or information environment.
4. **Traceable evidence** — at least one credible, publicly reviewable source is available.
5. **Calibrated language** — uncertain claims remain labelled as alleged, purported, reported, believed or unverified where appropriate.

Cases that are relevant to automated decision-making but fail the AI-linkage threshold are held in the **watchlist**, not silently promoted to AI incidents.

## Evidence confidence

| Grade | Meaning |
|---|---|
| A | Strong evidence: primary/official evidence, direct admission, court record, or strong independent corroboration |
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

The score is a **research aid, not an official risk rating**. See `docs/severity-and-confidence.md`.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/validate.py
python scripts/export_json.py  # optional machine-readable JSON export
streamlit run app.py
```

## Contribute an incident

Open an **Incident submission** issue and provide the source links and evidence requested by the template. Submissions are reviewed against the same inclusion criteria as existing records.

Please do **not** submit:

- private personal data
- leaked credentials or access tokens
- graphic abuse material
- operational instructions that enable wrongdoing
- allegations without evidence

## Relationship to existing incident work

AAIO is designed to complement, not duplicate, global incident infrastructure. The methodology draws on concepts used by the **OECD AI Incidents and Hazards Monitor**, the **AI Incident Database**, and operational risk-management practices such as the **NIST AI Risk Management Framework**.

Where a seed record is already indexed by AIID, its AIID identifier is preserved for traceability.

## Citation

Please cite the repository using `CITATION.cff`.

## Author

**Blessing Ezeobioha**  
Cybersecurity practitioner and AI researcher working on threat intelligence, AI governance and responsible technology in African contexts.

- GitHub: [@Briella009](https://github.com/Briella009)
- ORCID: [0009-0005-9972-9380](https://orcid.org/0009-0005-9972-9380)
- LinkedIn: [Blessing Ezeobioha](https://www.linkedin.com/in/blessing-ezeobioha-)

## Status

**Seed release / research prototype.** The dataset will change as sources are corrected, incidents are added, or classifications are re-evaluated. Every correction should be documented in the changelog.
