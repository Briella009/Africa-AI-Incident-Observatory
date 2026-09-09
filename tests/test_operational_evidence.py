from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'data' / 'operational_incidents.csv'


def rows():
    with PATH.open(encoding='utf-8', newline='') as handle:
        return list(csv.DictReader(handle))


def test_operational_register_has_multiple_sectors():
    data = rows()
    assert len(data) >= 2
    assert len({row['sector'] for row in data}) >= 2


def test_healthcare_case_preserves_patient_harm_boundary():
    case = next(row for row in rows() if row['incident_id'] == 'AAIO-OP-0001')
    assert '115' in case['summary']
    assert '67' in case['summary']
    assert 'does not infer patient injury' in case['summary']
    assert case['evidence_confidence'] == 'A'
    assert 'nature.com' in case['source_1_url']
    assert 'pubmed.ncbi.nlm.nih.gov' in case['source_2_url']


def test_legal_case_has_direct_ai_linkage_and_primary_sources():
    case = next(row for row in rows() if row['incident_id'] == 'AAIO-OP-0002')
    assert case['ai_system_or_tool'] == 'ChatGPT'
    assert case['evidence_confidence'] == 'A'
    assert 'lawlibrary.org.za' in case['source_1_url']
    assert 'saflii.org' in case['source_2_url']


def test_core_eligible_records_are_high_confidence_and_source_traceable():
    for row in rows():
        if row['core_promotion_status'] == 'eligible_for_core':
            assert row['evidence_confidence'] in {'A', 'B'}
            assert row['source_1_url'].startswith('https://')
            assert row['source_2_url'].startswith('https://')
            assert len(row['qualification_basis']) >= 80
            assert len(row['notes']) >= 80


def test_operational_ids_do_not_collide_with_versioned_core_ids():
    core = ROOT / 'data' / 'incidents.csv'
    with core.open(encoding='utf-8', newline='') as handle:
        core_ids = {row['incident_id'] for row in csv.DictReader(handle)}
    operational_ids = {row['incident_id'] for row in rows()}
    assert core_ids.isdisjoint(operational_ids)
