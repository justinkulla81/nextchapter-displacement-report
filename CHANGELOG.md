# Changelog

## 1.72 — 2026-10-07
| Change | Type | Previous | Current | Reason | Historical impact |
|---|---|---|---|---|---|
| TFP decomposition from SF Fed quarterly series (code/13_tfp_decomposition.md; data/sf_fed_tfp_decomposition.csv) | Section addition; new data source | Labor productivity only (BLS) | Adds TFP, utilization-adjusted TFP, capital deepening, labor quality | Distinguish technology-driven productivity from capital deepening and utilization | None (new series); illustrative productivity scenario gains a caveat, figures unchanged |
| Check of Apollo (Slok) Oct 5, 2026 note | Interpretation | None | Cited, labeled post-reference-period | Reconcile outside commentary with the data | None |

## 1.71 — 2026-10-06
| Change | Type | Previous | Current | Reason | Historical impact |
|---|---|---|---|---|---|
| AI exposure vs outcomes across 22 occupation groups (code/11) | Section addition; new measure | None | Eloundou et al. (2024) exposure, OEWS May 2022 weights; 2019 and 2022 baselines | Defensible cross-sectional test of capability vs labor outcomes | None (new series) |
| Conversational-threshold postulate; customer service vs receptionists | Interpretation (stated hypothesis); new measure | None | CPS occupation codes 5240, 5400 | Test whether remote-conversation jobs change first | None |
| Education and potential-experience breakdowns (code/12) | Section addition; new measure | White-collar defined by occupation only | Adds ages 22+ by PEEDUCA and potential experience | Track the degree-holding core | None; white-collar definition unchanged |
| Higher-education cost, completion, payback and debt section | Section addition (secondary sources) | None | Chapter 09 | Context for degree-holding core | None |

## 1.7 — 2026-10-06
| Change | Type | Previous | Current | Reason | Historical impact |
|---|---|---|---|---|---|
| "Beyond unemployment" white-collar panel (code/10_hidden_displacement.py) | Section addition; new measure | None | Involuntary part-time, multiple jobs, self-employment, hours; Jan–Aug 2019/2025/2026 | Test whether displacement hides inside jobs | None (new series) |
| Rewiring-constraint feature and three-speed scorecard | Section addition; interpretation | None | Feature with evidence scorecard | Frame data without overclaiming | None |
| Change-record standard (methodology/change_record_standard.md) | Methodology documentation | Version log only | Standing requirement from Oct 2026 | Longitudinal transparency | None |
| Cover "data available through" date | Measurement documentation | Reference period and publication date | Adds source-data date | Distinguish periods | None |

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
