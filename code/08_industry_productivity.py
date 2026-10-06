#!/usr/bin/env python3
"""Q3 annual feature: white-collar long-term share by industry (2019 vs 2026) with BLS-GVF margins.
TFP values are hand-entered from BLS 'Total Factor Productivity for Major Industries, 2024', Table 3
(accessed 2026-10-06; data revised 2026-03-19). Run from the code/ folder: python3 08_industry_productivity.py"""
import types
moe = types.ModuleType("moe")
src = open("04_margins_of_error.py").read().split("rows=[]")[0]
exec(src, moe.__dict__)
for k, lbl in [("wc_ind_7","Information"),("wc_ind_9","Professional & business services"),("wc_ind_8","Financial activities"),("wc_ind_4","Manufacturing"),("wc_ind_10","Education & health"),("wc","All white-collar")]:
    p1, p0, d, m = moe.ltu_share_change(k, "2026", "2019")
    print(f"{lbl:34} 2019 {p0:5.1f}  2026 {p1:5.1f}  change {d:+5.1f} ±{m:.1f}")
