from pathlib import Path
import csv, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]

def test_seed_has_multiple_countries_and_sources():
    rows=list(csv.DictReader(open(ROOT/'data'/'incidents.csv',encoding='utf-8')))
    assert len(rows)>=15
    assert len({r['country'] for r in rows})>=8
    assert all(r['source_1_url'].startswith('https://') for r in rows)
    assert all(r['last_verified']=='2026-09-08' for r in rows)

def test_watchlist_is_separate():
    core={r['incident_id'] for r in csv.DictReader(open(ROOT/'data'/'incidents.csv',encoding='utf-8'))}
    watch=list(csv.DictReader(open(ROOT/'data'/'watchlist.csv',encoding='utf-8')))
    assert watch
    assert all(w['watch_id'] not in core for w in watch)

def test_json_export_matches_csv_ids(tmp_path):
    subprocess.run([sys.executable, str(ROOT/'scripts'/'export_json.py')], check=True, cwd=ROOT)
    rows=list(csv.DictReader(open(ROOT/'data'/'incidents.csv',encoding='utf-8')))
    data=json.load(open(ROOT/'data'/'incidents.generated.json',encoding='utf-8'))
    assert [r['incident_id'] for r in rows] == [r['incident_id'] for r in data]
    (ROOT/'data'/'incidents.generated.json').unlink()
