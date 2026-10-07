#!/usr/bin/env python3
"""Version 1.7: 'beyond unemployment' check for employed white-collar workers (PRMJOCC1 1-2), Jan-Aug.
Shares of employed (PEMLR 1-2): part time for economic reasons (PRWKSTAT 3 or 6), multiple jobholders (PEMJOT=1),
self-employed incorporated or unincorporated (PEIO1COW 6-7); mean actual hours, all jobs (PEHRACTT>0, at work PEMLR=1).
Weight: PWCMPWGT. Writes ../data/cps_hidden_displacement_wc_jan_aug_2019_2025_2026.json
Usage: export CENSUS_API_KEY="<your-free-key>"; python3 10_hidden_displacement.py
Margins of error in the report are approximate (CPS total-unemployment GVF parameters); BLS characteristic-specific parameters to be adopted from the October 2026 edition."""
import json, os, urllib.parse, urllib.request
MON = ["jan","feb","mar","apr","may","jun","jul","aug"]
V = "PWCMPWGT,PEMLR,PRWKSTAT,PEMJOT,PEIO1COW,PEHRACTT,PRMJOCC1"
def fetch(y, m, key):
    q = urllib.parse.urlencode({"get": V, "key": key})
    with urllib.request.urlopen(f"https://api.census.gov/data/{y}/cps/basic/{m}?{q}", timeout=180) as r:
        return json.loads(r.read().decode())
def run(key, years=("2019","2025","2026")):
    out = {}
    for y in years:
        A = {}
        for m in MON:
            d = fetch(y, m, key); ix = {n: i for i, n in enumerate(d[0])}
            for R in d[1:]:
                w, l = float(R[ix["PWCMPWGT"]]), int(R[ix["PEMLR"]])
                if w <= 0 or l not in (1, 2): continue
                occ = int(R[ix["PRMJOCC1"]]); gs = ["all"] + (["wc"] if occ in (1, 2) else []) + (["mbf"] if occ == 1 else []) + (["prof"] if occ == 2 else [])
                ws = int(R[ix["PRWKSTAT"]]); pte = ws in (3, 6); mj = int(R[ix["PEMJOT"]]) == 1
                cow = int(R[ix["PEIO1COW"]]); se = cow in (6, 7); seu = cow == 7; h = int(R[ix["PEHRACTT"]])
                for g in gs:
                    a = A.setdefault(g, [0.0] * 10); a[0] += w; a[8] += 1
                    if pte: a[1] += w; a[9] += 1
                    if mj: a[2] += w
                    if se: a[3] += w
                    if seu: a[4] += w
                    if l == 1 and h > 0: a[5] += w * h; a[6] += w
        out[y] = {g: {"E": round(a[0] / 8 / 1e3), "pte": round(100 * a[1] / a[0], 2), "mj": round(100 * a[2] / a[0], 2), "se": round(100 * a[3] / a[0], 2),
                      "seu": round(100 * a[4] / a[0], 2), "hrs": round(a[5] / a[6], 2), "n": int(a[8]), "npte": int(a[9])} for g, a in A.items()}
    return out
if __name__ == "__main__":
    json.dump(run(os.environ["CENSUS_API_KEY"]), open("../data/cps_hidden_displacement_wc_jan_aug_2019_2025_2026.json", "w"), indent=1)
