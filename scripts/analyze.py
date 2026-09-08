#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data'/'incidents.csv')
print('Africa AI Incident Observatory - seed summary')
print(f'Records: {len(df)}')
print(f'Primary countries: {df.country.nunique()}')
print(f'Date range: {df.incident_date.min()} to {df.incident_date.max()}')
print('\nBy country:')
print(df.country.value_counts().to_string())
print('\nBy sector:')
print(df.sector.value_counts().to_string())
print('\nEvidence confidence:')
print(df.evidence_confidence.value_counts().sort_index().to_string())
print('\nSeverity bands:')
print(df.severity_band.value_counts().to_string())
