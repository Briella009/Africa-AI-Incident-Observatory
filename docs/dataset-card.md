# AAIO Dataset Card

## Dataset summary

The **Africa AI Incident Observatory (AAIO)** is an open, source-traceable research dataset for documenting publicly evidenced AI incidents with a material African nexus. It is designed for researchers, journalists, civil-society organisations, policymakers, security practitioners and other users who need inspectable evidence rather than unqualified incident counts.

AAIO separates four things that are often collapsed in incident catalogues:

1. whether an event qualifies as a realised AI incident;
2. how strong the public evidence is;
3. how severe the incident appears under AAIO's project rubric; and
4. where a record sits in the evidence-review pipeline.

The current release is intentionally conservative. It is **not a census of African AI harm and must not be used to rank countries by incident prevalence**.

## Motivation

Public evidence about AI failures affecting African people and institutions is fragmented across court judgments, regulator statements, fact-checks, peer-reviewed studies, company notices, local-language reporting and global incident databases. This makes systematic comparison difficult and can create a misleading impression that missing records mean missing harm.

AAIO was created to make that evidence easier to inspect, challenge, reuse and submit into broader incident-learning ecosystems while preserving uncertainty.

## Version

- Dataset version: `0.2.3`
- Release line: `0.2.x`
- Canonical version marker: `VERSION`
- Core data: `data/incidents.csv`
- Data license: CC BY 4.0
- Code license: MIT
- Concept DOI: `10.5281/zenodo.22789831`
- Archived v0.2.0 DOI: `10.5281/zenodo.22789832`

AAIO uses semantic-style dataset versioning. See `docs/release-policy.md`. The DOI-backed v0.2.0 snapshot is preserved separately from the evolving `main` branch; archive provenance is recorded in `metadata/archived-releases.json`.

## Composition

The repository contains several intentionally distinct evidence layers.

### Core incidents

`data/incidents.csv` contains records that meet AAIO's core inclusion threshold: credible AI linkage, realised event, African nexus, traceable public evidence and calibrated wording.

The current core release contains **19 records across 9 primary African countries**. The records span synthetic media, information operations, health misinformation, financial scams, conflict information, model behaviour, government-policy integrity, clinical decision support and professional legal research.

### Multilingual discovery layer

`data/multilingual_incidents.csv` preserves source-led discovery from French-, Arabic- and Portuguese-language reporting. It stores original-language source information, translation method, translation uncertainty and AI-attribution strength. A multilingual discovery record is not automatically a core incident.

### Operational evidence layer

`data/operational_incidents.csv` is a review layer for incidents in deployed or professional settings. It preserves staging identifiers and promotion metadata so that movement into the core dataset is auditable.

### Watchlist

`data/watchlist.csv` contains technology-governance cases that are important to track but do not currently meet AAIO's AI-linkage threshold. The watchlist exists to prevent pressure to mislabel automation, biometrics or algorithmic decision-making as AI without sufficient evidence.

### Record history

`data/record_history.csv` is an append-only ledger for material record changes, promotions and corrections.

## Collection process

AAIO uses public evidence only. Candidate incidents are identified through incident databases, court and government materials, peer-reviewed literature, fact-checkers, investigative journalism, company statements and multilingual source discovery.

A candidate is reviewed against the five core inclusion rules in `docs/methodology.md`. When evidence is incomplete, disputed or does not establish AI involvement, the record is narrowed, staged or excluded rather than strengthened by inference.

AAIO does not use an AI-content detector score by itself as proof that content is AI-generated.

## Evidence hierarchy

Preferred evidence, in approximate order, is:

1. court judgments, regulator findings, official incident notices and direct developer/company admissions;
2. independent investigative journalism and specialist fact-checking;
3. peer-reviewed or methodologically transparent research;
4. reputable incident databases preserving source provenance; and
5. other credible public reporting.

The hierarchy is not absolute. Sources can conflict, and an official source can still be incomplete. Record wording is calibrated to the strongest claim the evidence supports.

## Labels and annotations

### Evidence confidence

AAIO uses grades A-D to describe the strength of public evidence. Confidence is separate from severity.

- **A:** strong primary, official, judicial, peer-reviewed deployment or strongly corroborated evidence;
- **B:** good independent reporting/fact-checking with direct technical or documentary support;
- **C:** limited but credible evidence with material uncertainty preserved;
- **D:** unverified/disputed and excluded from the core dataset.

### Severity

Severity is a project research aid computed from four 0-4 dimensions: magnitude, scale, criticality and irreversibility. It is **not** an OECD, AIID, legal or regulatory severity classification.

## Preprocessing and transformations

AAIO performs curator-led normalization rather than automated fact generation. This includes:

- neutral incident titles;
- standardized date precision;
- pipe-separated labels for harms and affected parties;
- source-type labelling;
- evidence-confidence grading;
- deterministic severity scoring;
- explicit qualification and caveat notes; and
- deterministic interoperability export generation.

Multilingual records preserve translation method and uncertainty rather than presenting machine-assisted English summaries as original-source text.

## Quality controls

The repository CI validates:

- core JSON Schema conformance;
- stable IDs and duplicate prevention;
- source URL structure;
- severity mathematics;
- multilingual provenance fields;
- operational promotion links;
- release/version consistency;
- material history requirements;
- machine-readable dataset metadata and archive DOI relationships; and
- deterministic AIID/OECD interoperability export generation.

Passing CI means the repository satisfies its declared structural and consistency checks. It does **not** certify that every external source is permanently available or that every incident interpretation is beyond dispute.

## Source persistence monitoring

AAIO v0.2.2 added a separate maintenance control for public evidence URLs. `scripts/check_source_health.py` builds a deduplicated inventory of source links used across the core, multilingual, operational and watchlist layers and can test whether those URLs are practically reachable from a GitHub runner.

The audit distinguishes missing pages from rate limits, bot blocks, server failures and network errors. It is deliberately **non-blocking**: HTTP reachability is not evidence validity, and a temporary 403, 429 or timeout must not automatically change a record's confidence or inclusion status.

See `docs/source-resilience.md`.

## Intended uses

AAIO is suitable for:

- qualitative incident analysis;
- governance and policy research;
- source-led case comparison;
- studying evidence and reporting gaps;
- incident-response and AI-risk education;
- multilingual incident-discovery research;
- preparing defensible upstream incident submissions; and
- reproducible analysis where users retain the stated coverage limitations.

## Uses that require caution or are not supported

AAIO should not be used to:

- estimate national AI-incident rates from raw row counts;
- rank African countries by AI safety or harm prevalence;
- infer that countries absent from the dataset have no AI incidents;
- treat an AAIO severity score as a legal or regulatory determination;
- infer causation beyond the cited evidence;
- infer state sponsorship, malicious intent or individual culpability when sources do not establish it; or
- train a model to predict "unsafe countries" or similarly stigmatizing labels from this non-representative sample.

## Known limitations and biases

AAIO is affected by public-reporting visibility, language coverage, internet accessibility, source permanence, media capacity, litigation/publication delays and curator capacity. Public-facing synthetic-media incidents are generally easier to observe than failures inside hospitals, lenders, employers, schools and government systems.

The v0.2.x line has begun to address this by adding operational incidents, a multilingual evidence layer and source-persistence monitoring, but those changes do not make the dataset comprehensive or statistically representative.

Some incidents have cross-border effects while still requiring one primary country field for analysis. Users should inspect `countries_affected` and source context rather than treating `country` as the only geography.

## Ethical considerations

AAIO minimizes unnecessary personal information, avoids republishing harmful media where a source citation is sufficient, preserves uncertainty and avoids inferring victim injury, motive or culpability beyond the evidence. See `docs/ethics.md`.

## Maintenance and corrections

Material corrections should update the core record, `last_verified`, `data/record_history.csv` and the changelog. Staged evidence retains its original staging identifier after promotion. Public-source link failures are reviewed under `docs/source-resilience.md` and do not trigger automatic evidence downgrades. See `docs/release-policy.md`.

## Interoperability

AAIO provides a deterministic semantic alignment layer for AIID concepts and all 29 criteria in the OECD common reporting framework. Non-equivalent fields remain explicitly partial, approximate or unmapped rather than being silently normalized.

See `docs/interoperability.md` and `mapping/interoperability-map-v1.json`.

## Machine-readable metadata

- `datapackage.json` describes repository data resources in a Data Package-style descriptor.
- `metadata/aaio-dataset.jsonld` exposes Schema.org `Dataset` metadata for machine discovery.
- `metadata/archived-releases.json` maps archived versions to exact source commits, GitHub releases, Zenodo records, DOI relationships and deposited-file checksums.
- `CITATION.cff` contains current-project citation metadata and references the archived v0.2.0 dataset.

AAIO's first verified DOI-backed archive is v0.2.0. The version DOI is `10.5281/zenodo.22789832`; the concept DOI for all archived AAIO versions is `10.5281/zenodo.22789831`.

## Citation

For work that depends on the exact archived v0.2.0 dataset, cite:

> Ezeobioha, B. (2026). *Africa AI Incident Observatory (AAIO) v0.2.0* (Version 0.2.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.22789832

Use the concept DOI `10.5281/zenodo.22789831` when referring to AAIO as an evolving archived research resource rather than a specific dataset snapshot. `CITATION.cff` remains the repository-level citation metadata for the current branch.

## Maintainer

**Blessing Ezeobioha**  
ORCID: https://orcid.org/0009-0005-9972-9380  
GitHub: https://github.com/Briella009

## Feedback

Corrections, source challenges and new incident evidence are welcome through the repository issue templates. Evidence-backed disagreement is part of the project design; records should become more defensible over time, not merely more numerous.
