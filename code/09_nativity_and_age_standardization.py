#!/usr/bin/env python3
"""Version 1.6 additions.
(a) White-collar long-term unemployment by nativity (PRCITSHP: 1-3 U.S.-born, 4 naturalized, 5 noncitizen).
(b) Ages 55+ participation standardized to the 2025 mix of 5-year age groups x sex.
Pulls CPS basic monthly files from the Census API (Jan-Aug) and writes the two JSON files in ../data.
Group arrays: [labor force, unemployed, unemployed 27+ wks (thousands, monthly avg), unweighted unemployed respondents, job losers, job losers 27+].
Usage: export CENSUS_API_KEY="<your-free-key>"; python3 09_nativity_and_age_standardization.py
"""
import json, os, urllib.parse, urllib.request
MON = ["jan","feb","mar","apr","may","jun","jul","aug"]
def fetch(y, m, v, key):
    q = urllib.parse.urlencode({"get": v, "key": key})
    with urllib.request.urlopen(f"https://api.census.gov/data/{y}/cps/basic/{m}?{q}", timeout=180) as r:
        return json.loads(r.read().decode())
def nativity(key, years=("2019","2025","2026")):
    out = {}
    for y in years:
        A = {}
        for m in MON:
            d = fetch(y, m, "PWCMPWGT,PEMLR,PRUNEDUR,PRMJOCC1,PRCITSHP,PRTAGE,PRUNTYPE", key); ix = {n: i for i, n in enumerate(d[0])}
            for R in d[1:]:
                w, l = float(R[ix["PWCMPWGT"]]), int(R[ix["PEMLR"]])
                if w <= 0 or l < 1: continue
                c = int(R[ix["PRCITSHP"]]); nat = "nb" if c <= 3 else "nz" if c == 4 else "nc"
                inlf = l <= 4; age = int(R[ix["PRTAGE"]]); occ = int(R[ix["PRMJOCC1"]])
                p = A.setdefault("pop_" + nat, [0.0, 0.0]); p[0] += w; p[1] += w if inlf else 0
                if not inlf: continue
                un = l >= 3; dur = int(R[ix["PRUNEDUR"]]); jl = 1 <= int(R[ix["PRUNTYPE"]]) <= 3
                gs = ["all_" + nat] + (["wc_" + nat] + (["wcu35_" + nat] if age < 35 else []) if occ in (1, 2) else [])
                for k in gs:
                    a = A.setdefault(k, [0.0] * 6); a[0] += w
                    if un:
                        a[1] += w; a[3] += 1
                        if dur >= 27: a[2] += w
                        if jl:
                            a[4] += w
                            if dur >= 27: a[5] += w
        out[y] = {k: [round(x / 8 / 1e3) if i != 3 else x for i, x in enumerate(v)] for k, v in A.items()}
    return out
def age_sex(key, years=("2025","2026")):
    out = {}
    for y in years:
        A = {}
        for m in MON:
            d = fetch(y, m, "PWCMPWGT,PEMLR,PRTAGE,PESEX", key)
            for R in d[1:]:
                w, l, a, s = float(R[0]), int(R[1]), int(R[2]), R[3]
                if w <= 0 or l < 1 or a < 55: continue
                b = "55" if a < 60 else "60" if a < 65 else "65" if a < 70 else "70" if a < 75 else "75"
                p = A.setdefault(f"{b}_{s}", [0.0, 0.0]); p[0] += w; p[1] += w if l <= 4 else 0
        out[y] = {k: [round(v[0] / 8 / 1e3), round(v[1] / 8 / 1e3)] for k, v in A.items()}
    return out
def standardize(d):
    P = sum(v[0] for v in d["2025"].values())
    raw = {y: 100 * sum(v[1] for v in d[y].values()) / sum(v[0] for v in d[y].values()) for y in d}
    std = 100 * sum(d["2025"][k][0] / P * d["2026"][k][1] / d["2026"][k][0] for k in d["2025"])
    return raw, std
if __name__ == "__main__":
    key = os.environ["CENSUS_API_KEY"]
    json.dump(nativity(key), open("../data/cps_nativity_jan_aug_2019_2025_2026.json", "w"))
    d = age_sex(key); json.dump(d, open("../data/cps_55plus_age_sex_cells_2025_2026.json", "w"))
    raw, std = standardize(d); print("55+ participation", raw, "2026 at 2025 mix:", round(std, 2))
