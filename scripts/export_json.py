#!/usr/bin/env python3
from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'data' / 'incidents.csv'
OUT = ROOT / 'data' / 'incidents.generated.json'
NUMERIC = {'magnitude', 'scale', 'criticality', 'irreversibility', 'severity_score'}

with SRC.open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
for row in rows:
    for key in NUMERIC:
        row[key] = int(row[key])
OUT.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(f'Wrote {len(rows)} records to {OUT.relative_to(ROOT)}')
