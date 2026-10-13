# Methodology (from Appendix B of the report, Version 1.4)

Seasonal factors, definitions, variance method and standards as published. The report is authoritative if this file and the report differ.

Appendix B
# Methodology, standards and revisions

## Definitions

- **White-collar.** People whose current or most recent job is in Census major occupation group 1 (management, business and financial) or 2 (professional and related): variable PRMJOCC1 = 1 or 2. Unemployed people with no prior job have no occupation and are excluded.

- **Labor force, unemployed.** Labor force = PEMLR 1–4; unemployed = PEMLR 3–4 (on layoff or looking). Estimates use the composite weight PWCMPWGT, the weight BLS uses for labor-force estimates.

- **Long-term.** Unemployed 27 weeks or more (PRUNEDUR ≥ 27). Durations are spells in progress, top-coded at 119 weeks.

- **Index.** White-collar long-term unemployed as a share of the white-collar labor force, seasonally adjusted, 3-month moving average, divided by its 2019 average and multiplied by 100. October 2025 was not collected; averages spanning it use the available months.

## Seasonal adjustment

The index is seasonally adjusted with monthly factors equal to each calendar month's average ratio to its year's mean, estimated over 2015–2019 and 2022–2025 (pandemic years 2020–2021 excluded) and normalized to average 1.0 (Jan 1.104, Feb 1.059, Mar 0.998, Apr 0.949, May 0.907, Jun 0.926, Jul 1.039, Aug 1.075, Sep 1.057, Oct 0.995, Nov 0.965, Dec 0.926). Factors are re-estimated once a year. This is simpler than the X-13ARIMA-SEATS method BLS uses, so each edition also reports the index under X-13, STL and an unadjusted 12-month average (Exhibit 3); conclusions do not depend on the method. All other microdata comparisons use the same months in each year (January–August) and are not seasonally adjusted.

## Margins of error

From Version 1.4, margins of error use the method the Bureau of Labor Statistics publishes for users of Current Population Survey estimates: generalized variance functions with the parameters in BLS's "Parameters and factors for calculating standard errors for estimates from the CPS" (methods document dated July 2026). For a level x, se = √((α + βN)(x − x²/N)), where N is the civilian noninstitutional population 16 and over; for a percentage p with base y, se = √(((α + βy)/y)·p(100 − p)). We use the published parameters for unemployed persons (overall and by major occupation group, tables PF-1 and PF-13), unemployed 27 weeks and over and their percentage of the unemployed (PF-12), and the civilian labor force (PF-1). BLS publishes factors for three- and twelve-month averages and their changes; for our eight-month (January–August) averages we interpolate linearly between those factors, and for year-apart changes we apply the published ratio of the change-in-yearly-average factor to the yearly-average factor. Comparisons with 2019 treat the periods as independent. Subgroup rates use the standard error of the numerator divided by the subgroup labor force, because BLS publishes rate parameters only for large groups. Margins are 1.645 standard errors (90% confidence). Duration bands and medians (Exhibits 13 and 14) keep our earlier approximation because BLS publishes no parameters for them. Census does not release replicate weights for the public-use monthly files, so generalized variance functions are the recommended public method; they can understate variance for small groups, which is one reason we suppress groups with fewer than about 100 unemployed respondents and mark those under 400 as small.

## Measures reported every month

To avoid reporting only the cells that moved, each edition reports this fixed list regardless of direction: the White-Collar Index; labor force participation for ages 55+ and 65+; long-term shares for white-collar workers 50+; recent-graduate (22–27, bachelor's+) and young high-school-graduate unemployment; blue-collar unemployment and long-term share; self-employment shares (all, white-collar, 55+); Census business applications; white-collar unemployment and long-term rates and shares; long-term duration bands for all and white-collar workers; long-term shares by occupation (Exhibit 11 groups), by white-collar industry (Exhibit 12 groups) and by white-collar age group; BLS headline indicators (Exhibit 6); JOLTS; Challenger cuts and AI attributions; the SEC Item 2.05 comparison; state payroll leaders and laggards; and unemployment-insurance exhaustion.

## Other NextChapter calculations

Year-to-date and over-the-year payroll changes are calculated from FRED levels as of October 2, 2026, and will change with revisions. Openings per unemployed person divides JOLTS openings by CPS unemployment. State percent changes use BLS levels. The SEC comparison counts distinct filings returned by EDGAR full-text search; see "SEC filing search and coding" below.

## Index name

From Version 1.8 the index is called the White-Collar Long-Search Index. It was called the White-Collar Long-Term Unemployment Index from Version 1.4 to 1.72, and before that the White-Collar Displacement Index. The measure, definition and values are unchanged. We renamed it because it counts everyone long-term unemployed whose last job was white-collar, including people who quit or are re-entering the labor force, and because it identifies long-term unemployment, not its cause. It should not be read as an estimate of AI-driven displacement. A companion measure limited to people who lost a job (excluding quits and re-entrants) is reported in Chapter 01.

## How the variance method changed the results

Until Version 1.3 we used a conservative rule of thumb (design effect 2.0; eight pooled months counted as 3.2 independent months). The BLS method gives margins about two-thirds as wide. The table compares them for key estimates. Every finding in the executive summary clears both; several smaller changes clear only the BLS-method margin and are flagged in the tables on that basis.

Exhibit 32
90% margins of error: earlier approximation versus BLS variance method

| Estimate (January–August, 2026 vs 2025) | Change | Earlier approximation | BLS method | Clears margin? |

| White-collar long-term unemployment rate | +0.18 pts | ±0.11 | ±0.08 | Both |

| White-collar unemployment rate | +0.18 pts | ±0.21 | ±0.15 | BLS method only |

| White-collar unemployed out 27+ weeks | +5.3 pts | ±3.6 | ±2.4 | Both |

| Computer and mathematical, out 27+ weeks | +13.4 pts | ±11.6 | ±7.5 | Both |

| Business and financial operations, out 27+ weeks | +7.4 pts | ±9.7 | ±6.3 | BLS method only |

| White-collar ages 55–64, out 27+ weeks | +12.9 pts | ±9.2 | ±6.3 | Both |

| White-collar ages 50+, out 27+ weeks | +7.6 pts | ±6.5 | ±4.5 | Both |

| Labor force participation, ages 55+ | −1.0 pt | ±0.5 | ±0.4 | Both |

| Unemployment, ages 22–27 with a bachelor's degree, vs 2019 | +1.5 pts | ±0.9 | ±0.7 | Both |

| Information industry (white-collar), out 27+ weeks | +9.0 pts | ±17.2 | ±11.0 | Neither |

NextChapter calculation from Census CPS public-use microdata (January–August 2025 and 2026; 2019 for the graduate row) using BLS parameters and factors. Computation scripts are in the replication materials.

## Seasonal adjustment: robustness

The headline comparison (0.75% vs 0.56%) compares the same months of each year without seasonal adjustment, so it does not depend on any adjustment method. The monthly index does. We recomputed it three other ways: with the Census Bureau's X-13ARIMA-SEATS program (log transform, automatic model, level shifts for April 2020 and July 2021; October 2025 interpolated for estimation and then dropped), with STL decomposition, and as an unadjusted 12-month moving average. Results are in Chapter 01 (Exhibit 3). X-13 diagnostics flag possible residual seasonality, a common issue in short series disrupted by the pandemic, which is why we show all four.

## Sample sizes, small cells and nonresponse

Every occupation and age table shows the unweighted number of unemployed respondents. Cells with fewer than 100 unemployed respondents are suppressed; cells with fewer than 400 are marked as small and should be read as indicative only (for example, architecture and engineering, 136 respondents). CPS response rates have fallen substantially over the past decade; if people who are unemployed for a long time respond at different rates than others, estimates could be biased in ways weights do not fully correct. We have not measured this bias.

## Occupation codes and historical comparability

CPS occupation codes changed in 2003, 2011 and 2020 (the last adopting the 2018 Census occupation classification). The index starts in 2015 and spans the 2020 change; the major groups used here were largely, but not entirely, preserved, and we treat January 2020 as a potential break. A planned extension back to 2003 will document each break and will be shortened rather than spliced if comparability cannot be shown. The 2019 baseline is a relatively normal pre-pandemic benchmark, not a historical minimum or equilibrium.

## Evidence standards

- **Number labels.** Source-reported (a figure published by the source); NextChapter calculation (computed by us from identified data, method stated); NextChapter estimate (involves an assumption or model); hypothesis (a claim we are testing, with no number).

- **Company AI evidence levels.** Level 1: management says AI will raise productivity or cut costs. Level 2: the statement plus an operating metric moving in the expected direction. Level 3: sufficient evidence that AI contributed to a measured change. We never treat Level 1 as Level 3, and nothing in this edition reaches Level 3.

- **Source hierarchy.** Tier 1: BLS, Census, DOL, SEC, Federal Reserve, BEA, NBER and peer-reviewed or university research. Tier 2: transparent industry data (Challenger, Indeed, LinkedIn, ADP via published research, staffing firms, recruiting-software vendors). Tier 3: media, used to find primary sources and cited directly only when no primary source is available.

- **Alternative explanations.** For any finding that might be read as an AI effect, we consider post-pandemic overhiring, the technology-sector correction, interest rates and the cost of capital, weaker venture funding, federal job cuts, outsourcing and offshoring, and remote work, and ask which observations are specifically consistent with AI rather than equally consistent with these.

## SEC filing search and coding (corrected in Version 1.4)

We use EDGAR full-text search for form 8-K, January 1–September 30, 2026, query "Item 2.05" (170 filings from 149 companies), and the same query combined separately with "artificial intelligence", "AI", "automation", "machine learning" and "generative AI". We read every match in full and code each by the role AI plays: operational in the restructuring section (AI changing work, or cutting to reinvest in AI), operational elsewhere in the filing, risk or forward-looking language only, or false match. Versions 1.0 and 1.1 omitted the "AI" query and therefore reported 2 rather than 16 filings citing AI in the restructuring section. Coding was done by one analyst; a second-coder reliability check is planned before the Operational AI Disclosure Index is published.

## Revenue per employee

Sample, sources and exclusions are stated in the note to the revenue-per-employee exhibit in the Q3 addendum. Headcounts are taken from each 10-K's human-capital section, read and verified by hand; revenue is from XBRL company facts for the same fiscal-year end. The sample will be fixed for future comparisons and updated annually.

## Replication materials and review

Replication materials are published at launchyournextchapter.com/reports/replication, which links to the public code repository. They include the Python scripts that pull and process Census CPS microdata, build the index and breakdowns, and compute margins of error; the BLS variance parameters used; the X-13 specification and seasonal-adjustment comparison; the SEC search queries and hand-coding sheet; the revenue-per-employee sample; derived data files; a variable dictionary; and a changelog. Census microdata are public and are not redistributed; the scripts download them directly. Results can be reproduced without contacting NextChapter. This edition has not been externally reviewed; when an outside methodological review takes place, we will name the reviewer and state its scope and date here.

## Revisions and corrections

Government data are revised. Each edition reflects data available on its "data through" date. Errors are corrected in the online edition with a dated note below, and the data files are updated to match. Send corrections to Justin Kulla, Founder and CEO, at jkulla@launchyournextchapter.com.

Version log

| Version | Date | Change |

| 1.4 | Oct 6, 2026 | Methods upgrade: margins of error recomputed with the BLS generalized variance method (published CPS parameters) instead of our earlier approximation; flags updated accordingly (more changes now clear the margin; all executive-summary findings clear both methods). Added seasonal-adjustment robustness checks (X-13ARIMA-SEATS, STL and a 12-month average), a job-losers-only companion measure, an evidence hierarchy, section labels separating our measurements from others' findings and interpretation, source links for headline figures, and published replication materials. No point estimates changed. |
| 1.3 | Oct 6, 2026 | Corrections: Greenhouse figures corrected (annual applications per recruiter 1,610 in 2022 to 4,890 in 2025, not 146 to 746; time to fill 59.7 days, not 57); data CSV index values aligned with the index file (161.6 and 128.2). Significance language made provisional ("beyond our approximate 90% margin of error") pending replicate-weight variance estimates; two sentences reworded so they do not claim more than the data show; table notes clarified; print layout of Exhibit 11 fixed. |
| 1.2 | Oct 6, 2026 | Correction: SEC restructuring filings citing AI in the restructuring section revised from 2 to 16 (search had omitted the abbreviation "AI"); Exhibit 10 and Chapter 03 text revised. Index renamed (measure unchanged). Added the Q3 2026 quarterly addendum (scorecard, expectations versus outcomes, SEC coding, revenue per employee, labor-market services, organizational redesign, reemployment), a chapter on independent research, two features, the Future Research Agenda, the "does not establish" box, expanded methodology and Appendix D (revision audit). No other previously published figures changed. |
| 1.1 | Oct 6, 2026 | Added chapters on older workers, jobs created and destroyed, and new businesses; expanded new graduates and blue-collar coverage and the mid-career skills gap; added contact details. No previously published figures changed. |
| 1.0 | Oct 5, 2026 | First publication. |

How to cite
Kulla, J. (2026, October 5). NextChapter Employment Report: September 2026 (Version 1.8; formerly the Displacement Report). NextChapter. https://launchyournextchapter.com/reports/displacement-report-september-2026
Copy citation
Data: report figures (CSV) · White-Collar Index history, 2015–2026 (CSV) · SEC restructuring filings coded for AI (CSV) · revenue per employee sample (CSV). Charts and data may be republished with attribution under CC BY 4.0. Index code is available on request.

