# Contributing

Thank you for improving African AI incident visibility.

## Before submitting

Check that the event:

- has a material African nexus;
- has a credible AI linkage;
- actually occurred;
- has at least one credible public source;
- is not already represented by an existing AAIO record.

Use the **Incident submission** issue template. Do not open a pull request containing a new incident until the evidence review is complete.

## Evidence rules

Prefer primary/official evidence and independent reporting. If sources disagree, describe the disagreement. Never strengthen `reported` into `confirmed` without stronger evidence.

## Corrections

Use the **Data correction** template for factual errors, broken links, date changes, new regulatory outcomes or classification disputes.

## Pull requests

All changes must pass:

```bash
python scripts/validate.py
pytest -q
```

A data change should also update `CHANGELOG.md`.
