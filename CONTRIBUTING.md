# Contributing

Thank you for improving African AI incident visibility.

## Before submitting

Check that the event:

- has a material African nexus;
- has a credible AI linkage rather than only automation, digitisation or biometrics;
- actually occurred or produced a material adverse effect;
- has at least one credible public source;
- is not already represented by an existing AAIO core, staging or watchlist record.

Use the **Incident submission** issue template. Do not open a pull request containing a new incident until the evidence review is complete.

## Evidence rules

Prefer primary/official evidence, peer-reviewed deployment studies and independent reporting. If sources disagree, describe the disagreement. Never strengthen `reported`, `purported`, `believed` or `probable` into `confirmed` without stronger evidence.

Do not convert:

- an unsafe model recommendation into a patient-injury claim unless the source establishes injury;
- an automated-system failure into an AI incident unless AI involvement is evidenced;
- a benchmark or hypothetical risk into a realised incident;
- a complaint or allegation into a confirmed discriminatory outcome without supporting evidence.

## Multilingual evidence

Original-language sources are welcome. Preserve the original-language URL and headline, describe the translation method, and record translation uncertainty. Machine-assisted translation should not be presented as certified or native-speaker review.

See `docs/multilingual-evidence.md`.

## Operational evidence

Operational cases may enter `data/operational_incidents.csv` before core promotion. A staging record that is later promoted keeps its `AAIO-OP-*` ID and records the stable core ID and release version so the review trail remains auditable.

See `docs/operational-coverage.md`.

## Corrections

Use the **Data correction** template for factual errors, broken links, date changes, new regulatory outcomes or classification disputes.

Material changes to a core incident should also add an entry to `data/record_history.csv`. Typographical changes that do not alter meaning do not require a history entry.

## Starter pull requests

New incident records should continue through the evidence-review workflow first, but contributors can make useful direct PRs such as:

- add or improve a validator test for an existing schema rule;
- improve source-resilience tooling or tests;
- improve dataset-card, data-dictionary, interoperability, or methodology documentation;
- add a reproducible analysis notebook that reads the public dataset without modifying core records;
- improve accessibility or dashboard documentation;
- add a test for multilingual/provenance edge cases using public or synthetic fixtures.

Keep first contributions narrow and independently reviewable.

## Pull requests

Run the full validation path:

```bash
python scripts/validate.py
python scripts/validate_multilingual.py
python scripts/validate_operational.py
python scripts/validate_release.py
pytest -q
```

Data or release changes should update `CHANGELOG.md`. Versioned releases must keep `VERSION`, `CITATION.cff`, `README.md` and the changelog synchronized.

## External recognition and reuse

If you use AAIO in research, journalism, policy analysis or another public project, please cite the dataset and share a public link. Independently verifiable reuse can be recorded in `docs/impact.md`; AAIO does not count self-authored promotion as external adoption.
