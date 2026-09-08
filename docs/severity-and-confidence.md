# Severity and Evidence Confidence

AAIO deliberately separates **how serious an event appears** from **how strong the evidence is**.

## Evidence confidence

### A - Strong
Use when at least one of the following is present:

- official/court/regulator finding directly supports the material fact;
- developer, deployer or affected institution publicly admits the relevant event;
- multiple credible independent sources materially agree;
- a high-quality fact-check has direct technical/documentary corroboration.

### B - Good
Use when credible independent reporting or fact-checking supports the AI linkage and event, but some attribution, intent or technical details remain unresolved.

### C - Limited but credible
Use when one credible source supports the case but meaningful uncertainty remains. The record must state that uncertainty clearly.

### D - Unverified/disputed
Not eligible for the core dataset. May be queued for further research.

## Severity rubric

Each dimension is scored from 0 to 4.

### Magnitude - 35%
- 0: no material harm established
- 1: minor or primarily informational effect
- 2: meaningful individual/institutional harm or credible risk of direct loss
- 3: severe harm to people, institutions or essential processes
- 4: catastrophic or life-threatening harm

### Scale - 25%
- 0: isolated/test event
- 1: very small audience or one directly affected person
- 2: local/limited multi-person exposure
- 3: national or large-platform exposure
- 4: mass, cross-border or sustained exposure

### Criticality - 25%
- 0: low-stakes context
- 1: ordinary consumer/content context
- 2: employment, reputation, routine public information
- 3: finance, sensitive personal data, major institutional trust
- 4: health/safety, elections, conflict, fundamental rights, critical public policy or national security

### Irreversibility - 15%
- 0: trivially reversible
- 1: quickly correctable with limited residue
- 2: correction possible but harm persists
- 3: difficult to reverse or wide downstream persistence
- 4: irreversible or permanent harm

## Formula

```text
score = round((35*magnitude + 25*scale + 25*criticality + 15*irreversibility) / 4)
```

Bands:

- 0-24 Low
- 25-49 Limited
- 50-69 Moderate
- 70-84 High
- 85-100 Critical

## Important limitation

The score is an **AAIO analytic aid**, not a legal finding, official AIID/OECD classification or probability estimate. Users should inspect the underlying dimensions and sources rather than treating a one-number score as ground truth.
