#!/usr/bin/env python3
from pathlib import Path
import csv, json, re, sys
from urllib.parse import urlparse
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
CSV=ROOT/'data'/'incidents.csv'
SCHEMA=ROOT/'schema'/'incident.schema.json'
NUMERIC={'magnitude','scale','criticality','irreversibility','severity_score'}


def severity(d):
    score=round((35*int(d['magnitude'])+25*int(d['scale'])+25*int(d['criticality'])+15*int(d['irreversibility']))/4)
    band='Low' if score<25 else 'Limited' if score<50 else 'Moderate' if score<70 else 'High' if score<85 else 'Critical'
    return score, band


def valid_url(s):
    p=urlparse(s)
    return p.scheme in {'http','https'} and bool(p.netloc)


def typed(row):
    out=dict(row)
    for key in NUMERIC:
        out[key]=int(out[key])
    return out


def main():
    errors=[]
    schema=json.load(open(SCHEMA,encoding='utf-8'))
    validator=Draft202012Validator(schema)
    with open(CSV,encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    ids=set()
    for i,raw in enumerate(rows,1):
        try:
            r=typed(raw)
        except Exception as exc:
            errors.append(f'CSV record {i}: numeric conversion failed: {exc}')
            continue
        for err in validator.iter_errors(r):
            errors.append(f'CSV record {i}: {err.message}')
        if not re.fullmatch(r'AAIO-\d{4}',r.get('incident_id','')):
            errors.append(f"Bad ID: {r.get('incident_id')}")
        if r.get('incident_id') in ids:
            errors.append(f"Duplicate ID: {r['incident_id']}")
        ids.add(r.get('incident_id'))
        if r.get('evidence_confidence')=='D':
            errors.append(f"Core record may not have D confidence: {r['incident_id']}")
        if r.get('incident_or_hazard')!='incident':
            errors.append(f"Seed core must be realised incident: {r['incident_id']}")
        for k in ('source_1_url','source_2_url'):
            if not valid_url(r.get(k,'')):
                errors.append(f"Invalid URL {k}: {r['incident_id']}")
        aiid_id=r.get('aiid_id','').strip()
        aiid_url=r.get('aiid_url','').strip()
        if bool(aiid_id) != bool(aiid_url):
            errors.append(f"AIID ID/URL must both be present or both blank: {r['incident_id']}")
        if aiid_url and not valid_url(aiid_url):
            errors.append(f"Invalid URL aiid_url: {r['incident_id']}")
        score,band=severity(r)
        if r['severity_score']!=score:
            errors.append(f"Severity score mismatch {r['incident_id']}: {r['severity_score']} != {score}")
        if r['severity_band']!=band:
            errors.append(f"Severity band mismatch {r['incident_id']}: {r['severity_band']} != {band}")
    if len(rows)<15:
        errors.append('Seed release unexpectedly small')
    if errors:
        print('\n'.join('ERROR: '+e for e in errors)); return 1
    print(f'OK: {len(rows)} core records validated; schema, IDs, URLs and severity math are consistent.')
    return 0

if __name__=='__main__': sys.exit(main())
