# SEC Form 8-K Item 2.05 search and AI coding

**Population.** Form 8-K filings, January 1–September 30, 2026, returned by EDGAR full-text search (https://efts.sec.gov/LATEST/search-index) for the phrase `"Item 2.05"`: 170 distinct filings (accession numbers) from 149 companies. Q1 53, Q2 57, Q3 60.

**AI queries.** The same search combined separately with each of: `"artificial intelligence"`, `"AI"`, `automation`, `"machine learning"`, `"generative AI"`. Union: 26 filings. (Versions 1.0–1.1 omitted `"AI"` and undercounted.)

**Coding.** Every matching document was read in full. Each filing gets one category, by the strongest use of AI:

- **C1:** operational, in the Item 2.05 (restructuring) section, with AI changing how work is done (e.g., "AI-first operating model").
- **C2:** operational, in the Item 2.05 section, with costs cut to reinvest in AI.
- **C3:** operational AI or automation language elsewhere in the same filing (e.g., Item 8.01).
- **B:** AI only in risk-factor or forward-looking-statement language.
- **X:** false match (company or investee name only).

**Result.** C1 10 filings / 8 companies; C2 6 / 6; C3 2 / 2; B 6 / 6; X 2 / 2; no AI mention 144 filings. Coded file: `data/sec-item205-ai-coding-2026.csv`.

**Limits.**

- Single coder.
- Item 2.05 requires disclosure of the decision and costs, not reasons, so silence is not evidence AI played no role.
- Challenger counts workers in announced cuts; these counts are filings. The units differ.
