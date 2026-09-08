# Data Dictionary

| Field | Meaning |
|---|---|
| `incident_id` | Stable AAIO identifier |
| `title` | Neutral short description |
| `incident_date` | Earliest supported event/circulation date |
| `date_precision` | `day`, `month`, or `approximate_day` |
| `country` | Primary African country associated with the incident |
| `countries_affected` | Pipe-separated affected countries/regions |
| `region` | Broad African region |
| `sector` | Primary context/industry |
| `system_type` | Functional AI/synthetic-media class |
| `ai_system_or_tool` | Named model/tool where supported; otherwise `Unknown` |
| `incident_or_hazard` | Core release currently uses `incident`; reserved for future hazard work |
| `harm_types` | Pipe-separated harm descriptors |
| `affected_parties` | Pipe-separated affected groups/entities |
| `summary` | Source-calibrated factual synopsis |
| `reported_intent` | What evidence supports about intent; may be unknown |
| `response` | Public response/remediation reported |
| `regulatory_or_legal_outcome` | Known formal outcome or explicit statement that none was identified |
| `magnitude` | 0-4 project severity dimension |
| `scale` | 0-4 project severity dimension |
| `criticality` | 0-4 project severity dimension |
| `irreversibility` | 0-4 project severity dimension |
| `evidence_confidence` | A/B/C/D evidence grade |
| `qualification_basis` | Why the record satisfies or qualifies the inclusion standard |
| `source_1_*`, `source_2_*` | Provenance links and source type |
| `aiid_id` | AI Incident Database ID where applicable |
| `aiid_url` | AIID citation URL |
| `last_verified` | Last date a curator checked the record |
| `notes` | Important caveats |
| `curator` | Record curator |
| `severity_score` | Deterministic 0-100 project score |
| `severity_band` | Low/Limited/Moderate/High/Critical |
