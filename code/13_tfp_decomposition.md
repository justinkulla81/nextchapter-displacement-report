# TFP decomposition (Version 1.72)
Source: Federal Reserve Bank of San Francisco quarterly TFP file (https://www.frbsf.org/wp-content/uploads/quarterly_tfp.xlsx), sheet "annual" (and "quarterly" summary rows), updated 2026-09-03, data through 2026 Q2.
Columns used: dLP (output per hour), dtfp, dtfp_util, dk (capital services), dhours, dLQ (labor composition), alpha (capital share).
Contributions: capital deepening = alpha*(dk - dhours); labor quality = (1-alpha)*dLQ; dLP = capital deepening + labor quality + dtfp (within rounding).
Output: data/sf_fed_tfp_decomposition.csv. Update quarterly when the SF Fed posts a new vintage (about five weeks after each GDP release); record the vintage date in CHANGELOG.
