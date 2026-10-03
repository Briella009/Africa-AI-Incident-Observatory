# AAIO/AJIM study protocol

## Study title

**Working title:** Documenting AI harms in under-represented information ecosystems: multilingual discovery, provenance and semantic loss in African AI incident reporting.

**Target venue:** Aslib Journal of Information Management special issue, *AI Empowered Information Science for Sustainable Futures*.

## Study objective

The study examines AI-incident documentation as an information-science problem: what becomes discoverable, how provenance and uncertainty affect qualification, and what information is lost when locally curated evidence is aligned with global incident-reporting structures.

The study does not estimate national AI-incident prevalence and does not rank countries by safety or harm.

## Research questions

**RQ1 — Visibility and language.** What unique incidents, countries and source organisations become visible when French-, Arabic- and Portuguese-language discovery is added to AAIO's English-dominant core?

**RQ2 — Evidence and qualification.** What evidence-confidence, source and qualification patterns distinguish the frozen core, multilingual candidates and excluded watchlist cases?

**RQ3 — Interoperability and semantic loss.** What information is directly preserved, partially preserved, approximated or left unmapped when AAIO fields are aligned with AIID concepts and the OECD common reporting framework?

## Design

This is a descriptive observational information audit built on a curated public-evidence dataset and a design-science artefact. The analysis uses three intentionally separate evidence layers:

1. the 19-record AAIO core;
2. nine multilingual discovery candidates; and
3. three watchlist records excluded because AI linkage or causation was not sufficiently established.

The interoperability analysis uses the versioned AAIO mapping for nine AIID core concepts and all 29 OECD common reporting-framework criteria.

## Frozen analytical scope

- Frozen data base commit: `90db01070243f3da23ea472578d2f4d2df79d964`
- Dataset version at freeze: `0.2.3`
- Core incidents: 19
- Multilingual candidates: 9
- Watchlist records: 3
- OECD criteria: 29
- Target discovery languages: French, Arabic and Portuguese, three candidates per language
- Primary geography: African countries with a material nexus to the documented event

Input Git blob identifiers are recorded in `freeze-metadata.json`.

## Inclusion rule for the core

A core record requires all of the following:

1. a credible connection to an AI system, AI-generated output, AI-enabled manipulation, deployment, misuse or malfunction;
2. a realised event rather than a hypothetical hazard;
3. a material African nexus;
4. at least one credible, publicly reviewable source;
5. wording calibrated to the strength of the evidence;
6. deduplication at the underlying-event level; and
7. evidence confidence A, B or C.

A detector score by itself is insufficient evidence of AI generation.

## Exclusion and staging

Cases remain outside the core when AI involvement is not established, the event is hypothetical, the evidence is an uncorroborated allegation, the record duplicates an existing underlying event, the source is not safely reviewable, or the evidence cannot support the claimed African nexus.

Multilingual candidates remain analytically separate from the core. Their discovery is evidence of additional documentation visibility, not automatic promotion.

## Evidence and translation coding

Evidence confidence follows AAIO's A-D rubric, with D excluded from the core. Multilingual candidates additionally preserve:

- source language and language family;
- original source organisation and URL;
- AI-attribution strength: confirmed, probable, reported or uncertain;
- translation uncertainty: low, medium or high; and
- explicit evidence basis and verification date in the companion provenance file.

Machine-assisted English synthesis does not replace the original-language source.

## Analysis plan

### RQ1

Calculate unique primary countries, country counts, discovery-language counts, new countries added relative to the core, and the proportion of multilingual candidates from countries absent from the core. Report these as documentation-coverage effects only.

### RQ2

Report evidence-confidence distributions, AIID cross-reference coverage, primary and secondary source-type distributions, multilingual source-organisation concentration, translation uncertainty and watchlist exclusions. The corpus is too small and purposive for prevalence inference.

### RQ3

Count mapping status across OECD and AIID concepts using the controlled statuses `direct`, `partial`, `approximate`, `unmapped` and, for AIID cross-reference fields, `cross_reference_only`. Do not convert AAIO severity, harm, sector or stakeholder labels into external controlled vocabularies without a human-reviewed semantic mapping.

## Reliability and audit trail

The repository provides deterministic structural validation, stable identifiers, severity-math checks, frozen Git object identifiers, source provenance, reproducible summary statistics, publication tables and figure-data traceability.

The study is presently a **single-curator coding audit**. No second independent human coder or inter-rater reliability statistic has been completed for the AAIO coding. The manuscript must not claim inter-rater validation. This is reported as a limitation rather than silently implied away.

## Ethics and claim boundaries

AAIO uses publicly reviewable evidence and does not collect new participant data for this study. It avoids unnecessary personal information and does not infer creator identity, motive, model identity, victim injury or culpability beyond what sources support.

The study must not claim that countries with more rows have more AI incidents, that countries absent from the corpus are safer, or that AAIO is endorsed by AIID, OECD, NIST or the African Union.

## Reproducibility

Run:

```bash
python research/ajim/analyse_frozen.py
```

The committed result tables and vector figures are linked to the frozen inputs through `results-summary.json`, `verification.json` and `freeze-metadata.json`. Source-level provenance for the nine multilingual candidates is retained in `frozen/multilingual-provenance.csv`.
