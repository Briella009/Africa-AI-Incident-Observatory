# Interactive Dashboard

AAIO includes a Streamlit research dashboard in `app.py`.

## What the dashboard is for

The dashboard is designed for evidence exploration, not prevalence ranking. It provides:

- country, sector, year, severity and evidence-confidence filters;
- an Africa map showing where current seed records are documented;
- timelines and sector distributions;
- record-level source inspection;
- a separate evidence-quality view;
- a watchlist for cases excluded because AI attribution is not sufficiently established;
- CSV export of filtered records;
- links to methodology and source evidence.

A country with fewer records should never be interpreted as having fewer AI harms. The seed dataset reflects public visibility, source availability and curator coverage.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Connect a Streamlit Community Cloud account to GitHub.
2. Select the repository `Briella009/Africa-AI-Incident-Observatory`.
3. Use branch `main`.
4. Set the entrypoint to `app.py`.
5. Deploy publicly if the dashboard is intended for research/community use.

No secrets or external API keys are required for the seed dashboard.

## Visual design

The interface intentionally uses a restrained editorial palette and avoids decorative AI imagery. The goal is to resemble a research/public-interest data product rather than a generic AI demo.
