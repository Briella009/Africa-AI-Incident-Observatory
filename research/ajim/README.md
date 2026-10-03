# AAIO/AJIM reproducibility package

This directory contains the frozen analysis package for the AJIM study on multilingual discovery, provenance and semantic loss in African AI incident reporting.

## Frozen inputs

The analysis uses repository state anchored to commit `90db01070243f3da23ea472578d2f4d2df79d964` and dataset version `0.2.3`.

Input Git blobs are recorded in `freeze-metadata.json`:

- `data/incidents.csv` — 19 core incidents
- `data/watchlist.csv` — 3 excluded/watchlist records
- `mapping/interoperability-map-v1.json` — AIID/OECD semantic mapping
- `research/ajim/frozen/multilingual-analysis.csv` — 9 multilingual discovery candidates

The multilingual analysis file contains only the variables required for the statistical comparison. The detailed source-verification notes remain in the project evidence work; all nine rows remain `candidate_for_core`.

## Reproduce the statistics

From the repository root:

```bash
python research/ajim/analyse_frozen.py
```

The script validates the frozen row counts, unique incident identifiers, severity mathematics, language balance, candidate/core separation and OECD mapping cardinality before writing `research/ajim/results/results-summary.json`.

The committed tables provide the publication-facing breakdowns:

- `table1-dataset-layers.csv`
- `table2-core-geography.csv`
- `table3-language-coverage.csv`
- `table4-evidence-confidence.csv`
- `table5-source-patterns.csv`
- `table6-taxonomy-loss.csv`
- `table7-oecd-mandatory-criteria.csv`

## Figures

The `figures/` directory contains vector SVG figures suitable for journal production or later conversion to PDF/EPS:

1. core-country distribution;
2. multilingual discovery effect;
3. evidence-confidence distribution;
4. OECD taxonomy/interoperability loss.

Every plotted value is present in the committed CSV tables or `results-summary.json`; the SVGs contain no additional analytical values.

## Independent verification

On 27 September 2026, 15 headline metrics were independently recomputed directly from the frozen inputs and compared with `results-summary.json`. All 15 checks passed. The checked metrics and distributions are recorded in `results/verification.json`.

## Interpretation boundary

The corpus is purposive and documentation-based. Country counts must not be used as national incident-rate rankings. The multilingual sample was intentionally balanced across French, Arabic and Portuguese, so language-level counts are design features rather than prevalence estimates. OECD mapping status measures semantic transferability, not compliance or endorsement.

## Post-freeze upstream note

AAIO issue #9 later identified an existing AIID incident corresponding to AAIO-0019. The frozen core still has a null AIID field for that record because the repository workflow requires a verified upstream acceptance/merge outcome before changing the core dataset. This preserves reproducibility of the frozen 17/19 populated-cross-reference statistic.


## Completion status

Frozen numerical outputs were rechecked on 3 October 2026 against the committed inputs and remain internally consistent. The data collection and descriptive analysis are complete for the current study design.
