#!/usr/bin/env python3
from pathlib import Path
import csv, re, sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / 'data' / 'operational_incidents.csv'
REQUIRED = {
    'incident_id','title','incident_date','date_precision','country','sector',
    'system_type','ai_system_or_tool','incident_or_hazard','harm_types',
    'affected_parties','summary','response','evidence_confidence',
    'qualification_basis','source_1_name','source_1_url','source_1_type',
    'source_2_name','source_2_url','source_2_type','last_verified','notes',
    'curator','severity_score','severity_band','core_promotion_status'
}
ALLOWED_STATUS = {'eligible_for_core','hold','watchlist'}
ALLOWED_CONFIDENCE = {'A','B','C'}


def valid_url(value):
    parsed = urlparse(value)
    return parsed.scheme in {'http','https'} and bool(parsed.netloc)


def main():
    errors = []
    with CSV.open(encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = sorted(REQUIRED - fields)
        if missing:
            errors.append('Missing fields: ' + ', '.join(missing))
        rows = list(reader)

    ids = set()
    sectors = set()
    for index, row in enumerate(rows, 1):
        rid = row.get('incident_id', '')
        if not re.fullmatch(r'AAIO-OP-\d{4}', rid):
            errors.append(f'Record {index}: bad operational ID {rid}')
        if rid in ids:
            errors.append(f'Record {index}: duplicate ID {rid}')
        ids.add(rid)
        sectors.add(row.get('sector', ''))
        if row.get('incident_or_hazard') != 'incident':
            errors.append(f'{rid}: operational register requires realised incidents')
        if row.get('evidence_confidence') not in ALLOWED_CONFIDENCE:
            errors.append(f'{rid}: invalid confidence')
        if row.get('core_promotion_status') not in ALLOWED_STATUS:
            errors.append(f'{rid}: invalid promotion status')
        if row.get('core_promotion_status') == 'eligible_for_core' and row.get('evidence_confidence') not in {'A','B'}:
            errors.append(f'{rid}: core-eligible record must have A/B evidence')
        for field in ('source_1_url','source_2_url'):
            if not valid_url(row.get(field,'')):
                errors.append(f'{rid}: invalid {field}')
        if len(row.get('qualification_basis','').strip()) < 80:
            errors.append(f'{rid}: qualification basis is too thin')
        if len(row.get('notes','').strip()) < 80:
            errors.append(f'{rid}: calibration note is too thin')

    if len(rows) < 2:
        errors.append('Operational expansion must contain at least two independently sourced incidents')
    if not any('Healthcare' in sector for sector in sectors):
        errors.append('Operational expansion must include a healthcare deployment incident')

    if errors:
        print('\n'.join('ERROR: ' + error for error in errors))
        return 1
    print(f'OK: {len(rows)} operational incidents validated with explicit evidence and promotion status.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
