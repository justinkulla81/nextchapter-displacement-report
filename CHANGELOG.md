# Changelog

## 1.6 — 2026-10-06
- Correction: ages 55+ participation decline (38.1% → 37.1%) is compositional; standardized to the 2025 age-sex mix the change is −0.05 pt (code/09_nativity_and_age_standardization.py; data/cps_55plus_age_sex_cells_2025_2026.json). Removed from the report summary.
- Added white-collar long-term unemployment by nativity (data/cps_nativity_jan_aug_2019_2025_2026.json).

## 1.5 — 2026-10-06
- Added annual Q3 feature: industry productivity (BLS TFP 2019–24) versus white-collar long-term share by industry (code/08_industry_productivity.py; data/industry_productivity_vs_long_searches.csv).
- Report adds career-ladder, employer-training, college AI program and WIOA retraining sections (sourced from published data; no new microdata processing). Point estimates unchanged.

## 1.4 — 2026-10-06
- Margins of error recomputed with the BLS generalized variance method (published CPS parameters); flags updated. Point estimates unchanged.
- Added seasonal-adjustment robustness (X-13ARIMA-SEATS, STL, 12-month average) and a job-losers-only companion measure.
- Added hires-per-opening series (data/hires_per_opening.csv) and an illustrative net-productivity ledger.
- Published this repository.

## 1.3 — 2026-10-06
- Corrected Greenhouse figures (annual applications per recruiter 1,610 → 4,890; time to fill 59.7 days). Data CSV index values aligned (161.6; 128.2). Significance wording made provisional; two sentences reworded.

## 1.2 — 2026-10-06
- Correction: SEC restructuring filings citing AI in the restructuring section revised from 2 to 16 of 170 (search had omitted the abbreviation "AI"). Index renamed White-Collar Long-Term Unemployment Index. Added Q3 2026 quarterly addendum.

## 1.1 — 2026-10-06
- Added chapters on older workers, jobs created and destroyed, new businesses; expanded graduates and blue-collar.

## 1.0 — 2026-10-05
- First publication.
