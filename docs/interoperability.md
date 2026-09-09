# Interoperability

AAIO provides a **semantic interoperability layer** for two widely used AI-incident ecosystems:

- the [AI Incident Database (AIID)](https://incidentdatabase.ai/), including its editor-defined incident concepts and external incident identifiers; and
- the [OECD common reporting framework for AI incidents](https://www.oecd.org/en/publications/towards-a-common-reporting-framework-for-ai-incidents_f326d4ac-en.html), which defines 29 reporting criteria used to support interoperable incident reporting.

The export is intentionally conservative. It does **not** claim to be an official AIID submission schema, an OECD AIM ingestion format, a conformity assessment, or an endorsement by either organisation.

## Why semantic alignment instead of schema mimicry

AIID and OECD serve related but different purposes. AIID maintains incident records, supporting reports, manually populated entity roles, and multiple independent taxonomies. OECD's common reporting framework defines reporting criteria for cross-jurisdictional interoperability, while the OECD AI Incidents and Hazards Monitor (AIM) has its own evolving collection and enrichment pipeline.

AAIO therefore maps only what its source data actually supports. When two fields are related but not semantically equivalent, the export preserves the AAIO value as `raw_aaio_value` and marks the target field `approximate` or `unmapped` rather than inventing a normalized value.

## Alignment-status vocabulary

| Status | Meaning |
|---|---|
| `direct` | AAIO captures substantially the same concept and can transfer it without semantic inference. |
| `partial` | AAIO captures only part of the target concept or lacks target subfields. |
| `approximate` | AAIO has related information, but the target semantics or controlled vocabulary differ. |
| `unmapped` | AAIO does not currently capture the target concept in a defensible structured field. |
| `cross_reference_only` | AAIO stores an external identifier/URL but does not reproduce the external record schema. |

The machine-readable mapping is maintained in [`mapping/interoperability-map-v1.json`](../mapping/interoperability-map-v1.json).

## AIID core-concept alignment

AIID's Editor's Guide describes incident title/description, incident dates, and manually populated **developer**, **deployer**, and **harmed/nearly harmed** entity roles. AIID also supports multiple taxonomies rather than a single universal annotation scheme.

| AIID concept | AAIO field(s) | Status | Export behaviour |
|---|---|---|---|
| Existing incident number | `aiid_id`, `aiid_url` | `cross_reference_only` | Preserves the existing AIID link where AAIO has already matched the event. |
| Incident title | `title` | `direct` | Preserved without claiming AIID editor approval. |
| Description | `summary` | `direct` | Preserved as AAIO's source-calibrated synopsis. |
| Incident date | `incident_date`, `date_precision` | `partial` | Date and explicit precision are preserved. |
| Developer entities | none | `unmapped` | No entity is inferred from narrative text. |
| Deployer entities | none | `unmapped` | No entity is inferred from narrative text. |
| Harmed/nearly harmed parties | `affected_parties` | `approximate` | Exported as candidate labels only, not as normalized AIID entity tags. |
| Supporting reports | source fields | `partial` | Source name, URL and type are preserved, but AAIO does not construct full AIID report objects. |
| AIID taxonomy annotations | none | `unmapped` | AAIO does not fabricate CSET, GMF, MIT, or other AIID taxonomy labels. |

### Source-calibrated language

AAIO deliberately preserves wording such as `reported`, `purported`, `believed`, `alleged`, or `uncertain` when the source evidence requires it. This is compatible with AIID's editorial practice of using operational qualifiers where incident elements remain disputed or uncertain.

## OECD common reporting framework alignment

OECD's 2025 common reporting framework contains **29 criteria**. The mapping below covers every criterion. Seven are identified as mandatory in the framework: **1, 2, 3, 4, 7, 10 and 11**.

`strict_mandatory_mapping` in the export is an **AAIO internal quality signal only**. It reports whether those seven criteria are available as direct, non-null mappings. It must not be interpreted as an OECD submission-readiness or compliance determination.

| ID | OECD criterion | AAIO field(s) | Status | Key limitation |
|---:|---|---|---|---|
| 1 | Title | `title` | `direct` | — |
| 2 | Description of incident | `summary` | `direct` | — |
| 3 | How AI system relates to incident | none | `unmapped` | AAIO does not maintain a structured causal-role classification. |
| 4 | Submitter information | `curator` | `partial` | Curator name is not full submitter metadata. |
| 5 | Date of first known occurrence | `incident_date`, `date_precision` | `partial` | AAIO preserves explicit date precision. |
| 6 | Country(ies) where incident occurred | `country` | `partial` | `countries_affected` is not assumed to equal occurrence location. |
| 7 | Supporting materials | source fields | `direct` | Public source provenance is preserved. |
| 8 | AI system/product name and version | `ai_system_or_tool` | `partial` | Version is not separately captured. |
| 9 | Developer/deployer organisations | none | `unmapped` | No entity extraction is inferred. |
| 10 | Severity | AAIO severity fields | `unmapped` | AAIO's rubric is not OECD severity and is never auto-converted. |
| 11 | Harm type | `harm_types` | `approximate` | AAIO labels are not OECD controlled values. |
| 12 | Quantification of harm | none | `unmapped` | — |
| 13 | Unintended/wrongful use | `reported_intent` | `unmapped` | Intent is not equivalent to OECD's use-mode criterion. |
| 14 | Affected stakeholders | `affected_parties` | `approximate` | Raw labels are preserved without category conversion. |
| 15 | Human/fundamental-rights impacts | none | `unmapped` | — |
| 16 | Associated AI Principles | none | `unmapped` | — |
| 17 | Industries | `sector` | `approximate` | AAIO sectors are not ISIC-coded. |
| 18 | Business functions | none | `unmapped` | — |
| 19 | Critical functions/infrastructure | none | `unmapped` | — |
| 20 | Breadth of deployment | none | `unmapped` | AAIO `scale` measures impact exposure, not deployment breadth. |
| 21 | Link to training data | none | `unmapped` | — |
| 22 | Link to AI model | none | `unmapped` | — |
| 23 | Usage rights | none | `unmapped` | — |
| 24 | Multiple-AI-system interaction | none | `unmapped` | — |
| 25 | AI system tasks | `system_type` | `unmapped` | Descriptive system type is not converted to an OECD task taxonomy. |
| 26 | Maximum autonomy level | none | `unmapped` | — |
| 27 | Actions taken | `response` | `partial` | Free text is preserved; action categories are not inferred. |
| 28 | Steps to reproduce | none | `unmapped` | — |
| 29 | Additional information | several AAIO narrative fields | `partial` | Preserves context and qualification notes. |

### The severity rule is deliberately strict

AAIO's `severity_score`, `severity_band`, `magnitude`, `scale`, `criticality`, and `irreversibility` remain available in the exported AAIO provenance layer. They are **not** mapped into OECD criterion 10 because the vocabularies and scoring semantics are different. This prevents an apparently precise but unsupported conversion.

The same rule applies to AAIO `harm_types`, `affected_parties`, and `sector`: raw project values are preserved, but the exporter leaves the OECD canonical value `null` when a controlled-vocabulary conversion would require human judgment.

## Deterministic export contract

Generate the interoperability artefact with:

```bash
python scripts/export_interoperability.py
```

This writes:

- `exports/aaio-interoperability-v1.json`
- `exports/aaio-interoperability-v1.sha256`

The export is deterministic for the same input bytes and mapping version:

1. records are sorted by `incident_id`;
2. JSON object keys are sorted;
3. UTF-8 and a fixed pretty-print representation are used;
4. no runtime timestamp is embedded;
5. SHA-256 hashes of `data/incidents.csv` and the mapping file are embedded in the output; and
6. a SHA-256 manifest is written alongside the export.

This means two runs against unchanged inputs produce byte-identical JSON.

Generated export artefacts are intentionally **not committed**. `data/incidents.csv` and the mapping file remain the sources of truth; committing a second large derived dataset would create avoidable staleness risk. See [`exports/README.md`](../exports/README.md).

## Preserved AAIO provenance

Every exported record keeps the AAIO evidence layer even when an external field cannot be normalized:

- `evidence_confidence`
- `qualification_basis`
- `source_calibration_notes`
- `last_verified`
- `curator`
- primary and secondary source name, URL and source type
- AAIO severity dimensions, score and band, explicitly labelled as an AAIO project rubric

This makes the export auditable: a consumer can distinguish **what AAIO observed** from **what the interoperability layer could safely map**.

## Validation and tests

Run:

```bash
python scripts/validate.py
pytest -q
```

The interoperability tests verify that:

- all 29 OECD criteria and the seven mandatory criteria are represented;
- key AIID concepts are mapped or explicitly marked unmapped;
- the export is byte-deterministic;
- the SHA-256 manifest matches the generated file;
- all 17 v0.1.0 seed records are exported;
- evidence confidence and source-calibration fields survive unchanged;
- AIID developer/deployer/taxonomy fields are not fabricated;
- non-equivalent OECD fields remain `null` with explicit mapping status; and
- source/mapping SHA-256 values are embedded in the export.

## What this does not claim

AAIO interoperability output is **not**:

- an official AIID bulk-import or submission format;
- an OECD AIM ingestion schema;
- proof that an incident satisfies every OECD reporting criterion;
- an automatic AIID taxonomy classifier;
- an ISIC classifier;
- an OECD or AIID severity conversion; or
- evidence of endorsement, affiliation or certification.

## External references

- OECD (2025), *Towards a common reporting framework for AI incidents*: https://www.oecd.org/en/publications/towards-a-common-reporting-framework-for-ai-incidents_f326d4ac-en.html
- OECD AIM methodology: https://oecd.ai/en/incidents-methodology
- AI Incident Database Editor's Guide: https://incidentdatabase.ai/editors-guide/
- AI Incident Database taxonomies: https://incidentdatabase.ai/taxonomies/
- AI Incident Database research snapshots: https://incidentdatabase.ai/research/snapshots
