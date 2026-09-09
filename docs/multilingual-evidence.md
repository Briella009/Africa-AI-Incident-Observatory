# Multilingual evidence protocol

AAIO's v0.1.0 seed is heavily English-language. That is a visibility limitation, not evidence that AI incidents are rarer in African information environments where French, Arabic, Portuguese or other languages dominate public reporting.

This document defines a deliberately separate multilingual evidence layer. It is **not** part of the AIID/OECD interoperability work and does not alter or imitate either external schema.

## What is in `data/multilingual_incidents.csv`

The register contains source-traceable incident candidates discovered through non-English reporting. Each row preserves:

- the original-language source URL;
- the source's original headline in its original script/language;
- source language and language family;
- a conservative English curator summary;
- the source's level of AI attribution;
- translation method and explicit translation uncertainty;
- a `core_status` field so discovery is not confused with promotion to AAIO's core incident dataset.

The first release deliberately includes one documented source-led case for each language family named in issue #2:

| Record | Country | Source language | Family | Source | Status |
|---|---|---|---|---|---|
| AAIO-ML-0001 | Burkina Faso | French | francophone | AFP Factuel | candidate_for_core |
| AAIO-ML-0002 | Morocco | Arabic | arabophone | Misbar | candidate_for_core |
| AAIO-ML-0003 | Angola | Portuguese | lusophone | Verifica.ao | candidate_for_core |

This is a minimum viable correction to the discovery bias, not a claim of representative continental coverage.

## Translation policy

AAIO distinguishes **translation** from **fact verification**.

1. The original-language URL and headline are retained. The English text never replaces them.
2. English summaries are curator syntheses, not purported verbatim translations.
3. Translation method is recorded. The initial records use machine-assisted curator translation/synthesis; they are not labelled as certified or native-speaker translations.
4. Translation uncertainty is one of `low`, `medium`, or `high` and must include a note explaining the rating.
5. Where the source itself uses probabilistic language about AI attribution, the English summary must preserve that uncertainty. For example, `très probablement` must not become `confirmed`.
6. Ambiguous technical terms are not normalised merely to make an English taxonomy cleaner.
7. Proper names, organisations, dates and locations should be checked independently where feasible; uncertainty must remain visible when not resolved.

### Translation-uncertainty rubric

**Low** — the source's central finding and event details are unambiguous, and the curator summary avoids contested nuance. This does not mean the translation is professionally certified.

**Medium** — the central finding is recoverable, but linguistic nuance, idiom, legal terminology, attribution language or source context could materially affect a more detailed translation. The English summary should be correspondingly narrow.

**High** — translation or contextual ambiguity could change the incident interpretation. A high-uncertainty record should not be promoted to the core dataset without additional review or corroboration.

## AI-attribution strength

The multilingual register separates what happened from how strongly the source establishes AI involvement:

- `confirmed`: the reviewed source directly concludes that AI generation/manipulation was involved and describes its verification basis;
- `probable`: the source presents AI involvement as likely/probable rather than proven;
- `reported`: the source reports an AI attribution made by another identifiable party without independently establishing it;
- `uncertain`: available evidence does not support stronger attribution.

These labels describe the **reviewed source evidence**, not technical certainty about a model, vendor or creator.

## Core promotion rule

A multilingual discovery record is not automatically a core AAIO record. Promotion should require the same evidentiary discipline used elsewhere in AAIO: realised event, African nexus, traceable evidence, calibrated AI linkage and sufficient source quality. Where only one source has been reviewed, the record may remain `candidate_for_core` until corroboration or deeper source review is available.

This separation prevents a coverage-expansion goal from lowering the core dataset's evidentiary threshold.

## Current limitations

Three records do not make AAIO multilingual or representative. They establish a reproducible mechanism for expanding beyond English-language discovery. Future work should add more locally produced reporting, especially from francophone West/Central Africa, Arabic-speaking North Africa and Sudan, and lusophone Angola, Mozambique, Cabo Verde, Guinea-Bissau and Sao Tome and Principe.

Search-language coverage should itself be measured in future releases. Absence from this register must never be interpreted as absence of incidents.
