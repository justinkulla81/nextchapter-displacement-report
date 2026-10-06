# NextChapter Displacement Report — replication materials

Code, parameters and derived data behind the **NextChapter Displacement Report** (September 2026 edition, Version 1.6), a monthly report on white-collar job loss, long job searches, AI and career transitions.

Report: https://launchyournextchapter.com/reports/displacement-report-september-2026
Corrections and questions: Justin Kulla, jkulla@launchyournextchapter.com

## What you can reproduce

| Output in the report | How |
|---|---|
| White-Collar Long-Term Unemployment Index (Exhibit 1), monthly 2015–2026 | `code/01_wc_index_monthly.py` → `data/wc-index.csv` (seasonal factors in `methodology/methodology.md`) |
| Breakdowns by occupation, industry, age; older workers; graduates; blue-collar | `code/02_cps_breakdowns.py` and `code/03_cps_aggregates.py` → `data/cps_aggregates_jan_aug_2019_2025_2026.json` |
| 90% margins of error (BLS generalized variance method) | `code/04_margins_of_error.py` with `data/bls_gvf_parameters.json` → `data/margins_of_error_results.json` |
| Seasonal-adjustment robustness (fixed factors, X-13ARIMA-SEATS, STL, 12-month average) | `code/05_seasonal_sensitivity.py`, `code/x13_wcltu.spc` → `data/index_sensitivity.csv` |
| AI in SEC restructuring filings (Form 8-K, Item 2.05) | `methodology/sec_item205_search.md` (queries and coding rules) and `data/sec-item205-ai-coding-2026.csv` |
| Hires per job opening, 2001–2026 | `data/hires_per_opening.csv` (BLS JOLTS via FRED; annual averages) |
| Revenue per employee, 27 large white-collar employers | `data/displacement-report-2026-q3-revenue-per-employee.csv` (sources and rules in `methodology/methodology.md`) |
| Senior openings tracker (pilot, Appendix A) | `code/07_openings_tracker_pilot.py` (requires the NextChapter jobs database; not reproducible externally; pilot only) |
| Nativity breakdown; age-sex standardized 55+ participation (v1.6) | `code/09_nativity_and_age_standardization.py` |
| Industry productivity vs long searches (Q3 feature) | `code/08_industry_productivity.py`, `data/industry_productivity_vs_long_searches.csv` |

## Data sources

- **Census Bureau, Current Population Survey basic monthly public-use microdata**, via api.census.gov (free key: https://api.census.gov/data/key_signup.html). Microdata are not redistributed here; the scripts download them.
- **BLS, "Parameters and factors for calculating standard errors for estimates from the CPS"** (methods dated July 2026): https://www.bls.gov/cps/documentation.htm#reliability
- **SEC EDGAR full-text search** (https://efts.sec.gov/LATEST/search-index) and filing archives.
- Third-party figures cited in the report (BLS releases, Challenger, Federal Reserve surveys and others) are listed with links in the report's Appendix C.

## Run it

```bash
pip install pandas numpy statsmodels x13binary
export CENSUS_API_KEY="<your-free-key>"
cd code
python3 01_wc_index_monthly.py --start 2015-01 --end 2026-08 --out ../data/wc_index_raw.csv
python3 03_cps_aggregates.py --years 2019 2025 2026 --through 8 --out ../data/cps_aggregates_jan_aug_2019_2025_2026.json
python3 04_margins_of_error.py
python3 05_seasonal_sensitivity.py
```

## Known limitations

- Margins of error use BLS generalized variance functions because Census does not publish replicate weights for the public-use monthly files; GVFs can understate variance for small groups. Eight-month average factors are interpolated between published 3- and 12-month factors.
- CPS occupation codes changed in 2020; the index treats January 2020 as a potential break.
- The SEC coding was done by one analyst; no second-coder reliability check yet.
- The revenue-per-employee sample is limited to companies whose 10-Ks state comparable total headcount; figures are nominal; acquisitions are flagged, not adjusted.

## License

Code: MIT License. Data files and documentation: CC BY 4.0 (attribute "NextChapter Displacement Report").
