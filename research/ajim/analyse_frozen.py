#!/usr/bin/env python3
import csv,json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"research"/"ajim"/"results"
OUT.mkdir(parents=True,exist_ok=True)

def rows(path):
    with open(path,encoding="utf-8",newline="") as f:
        return list(csv.DictReader(f))
def pct(n,d): return round(100*n/d,1) if d else 0.0
def counts(rs,key): return Counter(r[key] for r in rs)

core=rows(ROOT/"data"/"incidents.csv")
watch=rows(ROOT/"data"/"watchlist.csv")
multi=rows(ROOT/"research"/"ajim"/"frozen"/"multilingual-analysis.csv")
mapping=json.load(open(ROOT/"mapping"/"interoperability-map-v1.json",encoding="utf-8"))

assert len(core)==19 and len({r["incident_id"] for r in core})==19
assert len(watch)==3 and len(multi)==9
assert counts(multi,"source_language")==Counter({"French":3,"Arabic":3,"Portuguese":3})
assert all(r["core_status"]=="candidate_for_core" for r in multi)
assert len(mapping["oecd_common_reporting_framework"])==29
assert len([x for x in mapping["oecd_common_reporting_framework"] if x["mandatory"]])==7
for r in core:
    s=round((35*int(r["magnitude"])+25*int(r["scale"])+25*int(r["criticality"])+15*int(r["irreversibility"]))/4)
    b="Low" if s<25 else "Limited" if s<50 else "Moderate" if s<70 else "High" if s<85 else "Critical"
    assert s==int(r["severity_score"]) and b==r["severity_band"]

cc=counts(core,"country"); rc=counts(core,"region")
cconf=counts(core,"evidence_confidence"); mconf=counts(multi,"evidence_confidence")
core_c=set(cc); multi_c={r["country"] for r in multi}; new=sorted(multi_c-core_c)
oecd=Counter(x["status"] for x in mapping["oecd_common_reporting_framework"])
mandatory=[x for x in mapping["oecd_common_reporting_framework"] if x["mandatory"]]
mand=Counter(x["status"] for x in mandatory)
aiidmap=Counter(x["status"] for x in mapping["aiid_core"])
aiid=sum(bool(r["aiid_id"].strip()) for r in core)
org=counts(multi,"source_name")

result={
 "freeze_base_commit":"90db01070243f3da23ea472578d2f4d2df79d964",
 "core_records":19,"watchlist_records":3,"multilingual_candidates":9,
 "core_unique_countries":len(core_c),"core_country_counts":dict(cc),
 "core_region_counts":dict(rc),"top3_country_share_pct":pct(sum(v for _,v in cc.most_common(3)),19),
 "new_countries":new,"new_country_count":len(new),
 "records_in_new_countries":sum(r["country"] in new for r in multi),
 "records_in_new_countries_pct":pct(sum(r["country"] in new for r in multi),9),
 "cumulative_unique_countries":len(core_c|multi_c),
 "country_coverage_increase_pct":pct(len(new),len(core_c)),
 "core_confidence":dict(cconf),"multilingual_confidence":dict(mconf),
 "multilingual_translation_uncertainty":dict(counts(multi,"translation_uncertainty")),
 "multilingual_ai_attribution":dict(counts(multi,"ai_attribution_strength")),
 "multilingual_source_orgs":dict(org),
 "aiid_cross_references":aiid,"aiid_cross_reference_pct":pct(aiid,19),
 "oecd_status":dict(oecd),"oecd_unmapped_pct":pct(oecd["unmapped"],29),
 "oecd_direct_pct":pct(oecd["direct"],29),
 "mandatory_status":dict(mand),"mandatory_direct_pct":pct(mand["direct"],7),
 "strict_direct_mandatory_complete_records":0,
 "aiid_mapping_status":dict(aiidmap)
}
(OUT/"results-summary.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"status":"OK","core":19,"multi":9,"new_countries":len(new),"oecd_unmapped":oecd["unmapped"]},sort_keys=True))
