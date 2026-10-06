#!/usr/bin/env python3
"""Seasonal-adjustment robustness for the White-Collar Long-Term Unemployment Index.
Compares: (1) published index (fixed monthly factors, 3-month average); (2) Census X-13ARIMA-SEATS
(spec: x13_wcltu.spc; requires `pip install x13binary statsmodels`); (3) STL; (4) unadjusted
12-month moving average. Each is rebased to its own 2019 average = 100.
Run from code/:  python3 05_seasonal_sensitivity.py
"""
import subprocess, shutil, pandas as pd, numpy as np
from statsmodels.tsa.seasonal import STL
d = pd.read_csv('../data/wc-index.csv'); d['month'] = pd.PeriodIndex(d.month, freq='M'); d = d.set_index('month')
nsa = d['wc_ltu_rate_pct_nsa']; full = pd.period_range(nsa.index.min(), nsa.index.max(), freq='M'); nsa = nsa.reindex(full)
missing = list(nsa[nsa.isna()].index)                     # October 2025 was not collected
filled = nsa.interpolate()
def rebase(s):
    m3 = s.rolling(3, min_periods=2).mean(); return 100 * m3 / s[s.index.year == 2019].mean()
# X-13
exe = shutil.which('x13as') or shutil.which('x13as_html')
vals = [f'{v:.4f}' for v in filled.values]; lines = '\n'.join(' '.join(vals[i:i+12]) for i in range(0, len(vals), 12))
spec = open('x13_wcltu.spc').read(); start = spec.index('data=('); end = spec.index(')', start)
open('x13_run.spc', 'w').write(spec[:start] + 'data=(\n' + lines + '\n ' + spec[end:])
subprocess.run([exe, 'x13_run'], check=True, capture_output=True)
x = pd.read_csv('x13_run.d11', sep='\t', skiprows=2, header=None, names=['date', 'v'])
x.index = pd.PeriodIndex(x.date.astype(str).str[:4] + '-' + x.date.astype(str).str[4:], freq='M'); x13 = x['v'].astype(float)
stl = STL(filled.to_timestamp(), period=12, robust=True).fit()
stlsa = pd.Series((filled.to_timestamp() - stl.seasonal).values, index=filled.index)
for s in (x13, stlsa): s[s.index.isin(missing)] = np.nan
out = pd.DataFrame({'published': d['wc_index_2019_100'], 'x13': rebase(x13), 'stl': rebase(stlsa),
                    'nsa_12mo': 100 * nsa.rolling(12, min_periods=11).mean() / nsa[nsa.index.year == 2019].mean()})
out.round(2).to_csv('../data/index_sensitivity.csv'); print(out.tail(15).round(1))
