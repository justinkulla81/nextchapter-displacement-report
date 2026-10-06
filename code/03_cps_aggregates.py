#!/usr/bin/env python3
"""Pool January-August CPS microdata into the group totals used for the report's
breakdowns and margins of error (data/cps_aggregates_jan_aug_2019_2025_2026.json).

For each group and year: monthly-average labor force (thousands), unemployed
(thousands), unemployed 27+ weeks (thousands), unweighted unemployed respondents
(summed over months), unemployed job losers (thousands) and job losers 27+ weeks
(thousands); plus population and labor force for ages 16+, 55+ and 65+.

Usage:  export CENSUS_API_KEY=...   (free at api.census.gov/data/key_signup.html)
        python3 03_cps_aggregates.py --years 2019 2025 2026 --through 8 --out ../data/cps_aggregates.json
"""
import argparse, json, os, urllib.parse, urllib.request
MON = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
VARS = "PWCMPWGT,PEMLR,PRUNEDUR,PRMJOCC1,PRDTOCC1,PRMJIND1,PRTAGE,PRUNTYPE,PEEDUCA"

def fetch(y, m, key):
    q = urllib.parse.urlencode({"get": VARS, "key": key})
    with urllib.request.urlopen(f"https://api.census.gov/data/{y}/cps/basic/{MON[m-1]}?{q}", timeout=180) as r:
        return json.loads(r.read().decode())

def groups(age, occ, docc, ind, edu):
    ab = "16_24" if age < 25 else "25_34" if age < 35 else "35_44" if age < 45 else "45_54" if age < 55 else "55_64" if age < 65 else "65p"
    ks = ["all", "age_" + ab]
    if 7 <= occ <= 10: ks.append("blue")
    if 22 <= age <= 27 and edu >= 43: ks.append("grad_ba")      # bachelor's or higher
    if 22 <= age <= 27 and edu == 39: ks.append("hs2227")       # high school diploma only
    if docc > 0: ks.append(f"occ_{docc}")
    if occ in (1, 2):                                            # white-collar
        ks += ["wc", "wc_age_" + ("u35" if age < 35 else "35_44" if age < 45 else "45_54" if age < 55 else "55_64" if age < 65 else "65p")]
        if age >= 50: ks.append("wc_50p")
        if ind > 0: ks.append(f"wc_ind_{ind}")
    return ks

def accumulate(rows, A, P):
    ix = {n: i for i, n in enumerate(rows[0])}
    for r in rows[1:]:
        w = float(r[ix["PWCMPWGT"]]); l = int(r[ix["PEMLR"]])
        if w <= 0 or l < 1: continue
        age = int(r[ix["PRTAGE"]]); inlf = l <= 4
        for k, ok in (("pop16", True), ("pop55", age >= 55), ("pop65", age >= 65)):
            if ok:
                p = P.setdefault(k, [0.0, 0.0]); p[0] += w
                if inlf: p[1] += w
        if not inlf: continue
        un = l >= 3; dur = int(r[ix["PRUNEDUR"]]); ut = int(r[ix["PRUNTYPE"]]); jl = 1 <= ut <= 3
        for k in groups(age, int(r[ix["PRMJOCC1"]]), int(r[ix["PRDTOCC1"]]), int(r[ix["PRMJIND1"]]), int(r[ix["PEEDUCA"]])):
            a = A.setdefault(k, [0.0] * 6); a[0] += w
            if un:
                a[1] += w; a[3] += 1
                if dur >= 27: a[2] += w
                if jl:
                    a[4] += w
                    if dur >= 27: a[5] += w

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--years", nargs="+", required=True); ap.add_argument("--through", type=int, default=8); ap.add_argument("--out", default="cps_aggregates.json")
    a = ap.parse_args(); key = os.environ["CENSUS_API_KEY"]; out = {}
    for y in a.years:
        A, P = {}, {}
        for m in range(1, a.through + 1): accumulate(fetch(y, m, key), A, P)
        n = a.through
        G = {k: [round(v[0]/n/1e3), round(v[1]/n/1e3, 1), round(v[2]/n/1e3, 1), v[3], round(v[4]/n/1e3, 1), round(v[5]/n/1e3, 1)] for k, v in A.items()}
        out[str(y)] = {"G": G, "P": {k: [round(v[0]/n/1e3), round(v[1]/n/1e3)] for k, v in P.items()}}
    json.dump(out, open(a.out, "w")); print("wrote", a.out)
