# Methodology

## 1. Purpose

AAIO is a public-interest evidence layer for AI incidents with an African nexus. It is designed to make cases comparable without overstating what the sources prove.

The project follows a conservative rule: **when AI involvement is unclear, exclude the case from the core dataset and document it in the watchlist instead.**

## 2. Conceptual basis

The methodology is informed by:

- OECD AI Incidents and Hazards Monitor definitions and taxonomy work
- AI Incident Database incident records and research on collective incident memory
- NIST AI Risk Management Framework incident-response and documentation practices

AAIO does not reproduce or claim ownership of those taxonomies. It keeps its schema small enough for journalists, researchers, civil-society organisations and practitioners to use without specialist tooling.

## 3. Core incident definition

For AAIO, a core incident is a publicly documented event in which the development, deployment, use, misuse or malfunction of an AI system is credibly linked to realised harm or a material adverse effect affecting an African person, community, institution, market, public service, information environment or country.

A case is included only when all five criteria below are satisfied.

### 3.1 AI linkage
A source must establish a credible connection to an AI system or AI-generated output. Marketing language or speculation is insufficient.

### 3.2 Realised event
There must be an event that actually occurred. Purely hypothetical hazards belong in future hazard research, not the core incident table.

### 3.3 African nexus
At least one African country, population, institution or information environment must be materially affected.

### 3.4 Traceable evidence
At least one source must be publicly reviewable and credible. A single social-media allegation without corroboration is insufficient.

### 3.5 Calibrated wording
The record may not state as fact what the source states only as allegation. Terms such as `reported`, `purported`, `believed`, `alleged` and `uncertain` are preserved when required.

## 4. Exclusions

AAIO excludes from the core table:

- ordinary software or automated decision failures where AI involvement is not established
- hypothetical risks with no realised event
- unattributed social-media claims that lack credible verification
- duplicated reports of the same underlying event
- claims whose only support is an AI-content detector score with no corroborating evidence
- private or non-public information that cannot be safely reviewed

Important excluded cases may be placed in `data/watchlist.csv` with an explicit reason.

## 5. Source hierarchy

Preferred evidence order:

1. court judgments, regulator findings, official incident notices, direct developer/company admissions
2. independent investigative journalism and specialist fact-checking
3. peer-reviewed or methodologically transparent research
4. reputable incident databases that preserve source provenance
5. other credible public reporting

A source is never treated as infallible. Conflicts are recorded and the wording is narrowed to the strongest shared claim.

## 6. Deduplication

Records are deduplicated by the underlying event, not by article URL. Multiple reports about the same event remain sources on one record unless materially distinct harms or deployments justify separate incidents.

## 7. Dates

`incident_date` represents the earliest reasonably supported date of occurrence or circulation, not necessarily the publication date of a fact-check. `date_precision` indicates whether the date is exact, month-level or approximate.

## 8. Updates and corrections

Every material correction should:

1. update the source-backed record;
2. update `last_verified`;
3. add a note to `CHANGELOG.md`;
4. preserve uncertainty rather than silently resolving disputed facts.

## 9. What absence means

Country-level absence is **not evidence of safety**. It can reflect monitoring gaps, language coverage, media access, reporting incentives, database coverage or curator capacity.
