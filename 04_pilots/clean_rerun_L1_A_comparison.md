# Dataset A Clean Re-run: Level 1 Comparison Report

**Date:** 2026-04-16
**Original run:** `pilot_claude_v0.4.1_results.csv` (research-system L1)
**Clean re-run:** `clean_rerun_L1_A_results.csv` (independent verification)
**Dataset:** A (17 sources: S-01 to S-09, C-01 to C-08)

## Summary

| Metric | Value |
|--------|-------|
| Total sources | 17 |
| Exact verdict match | 16/17 (94.1%) |
| Substantive agreement | 17/17 (100%) |
| Assessment | **ROBUST** (>=90%) |

## Per-Source Comparison

| ID | Original Verdict | Clean Re-run Verdict | Match | Notes |
|----|-----------------|---------------------|-------|-------|
| S-01 | EXACT | EXACT | Y | |
| S-02 | EXACT | EXACT | Y | |
| S-03 | EXACT | EXACT | Y | |
| S-04 | EXACT | EXACT | Y | |
| S-05 | EXACT | EXACT | Y | |
| S-06 | EXACT | EXACT | Y | |
| S-07 | EXACT | EXACT | Y | |
| S-08 | UNVERIFIED | EXACT | N* | Improvement: original had procedural gap |
| S-09 | EXACT | EXACT | Y | |
| C-01 | EXACT | EXACT | Y | |
| C-02 | PARTIAL | PARTIAL | Y | Both found claim_inflation |
| C-03 | EXACT | EXACT | Y | |
| C-04 | PARTIAL | PARTIAL | Y | Both found metadata_error |
| C-05 | EXACT | EXACT | Y | |
| C-06 | ERROR | ERROR | Y | Both found author_conflation |
| C-07 | EXACT | EXACT | Y | |
| C-08 | ERROR | ERROR | Y | Both found misattribution |

## Disagreement Analysis

### S-08: UNVERIFIED -> EXACT (Improvement)

The only disagreement is S-08 (Research Debt by Olah, Distill 2017). The original run marked this UNVERIFIED with error type `procedural_gap` - it was not searched during the initial verification session. The clean re-run successfully verified this source:

- **Authors:** Chris Olah and Shan Carter
- **Title:** "Research Debt"
- **Venue:** Distill, 2017
- **DOI:** 10.23915/distill.00005
- **URL:** https://distill.pub/2017/research-debt/

This is a **methodological improvement**, not a substantive disagreement. The original run acknowledged this gap in its notes ("Later confirmed DOI 10.23915/distill.00005").

## Verdict Distribution

| Verdict | Original | Clean Re-run |
|---------|----------|-------------|
| EXACT | 13 | 14 |
| PARTIAL | 2 | 2 |
| ERROR | 2 | 2 |
| UNVERIFIED | 1 | 0 |

The clean re-run resolved 1 UNVERIFIED source to EXACT, matching the distribution expected from full coverage.

## Error Detection Consistency

All errors detected in the original run were independently confirmed:

1. **C-02 (claim_inflation):** Both runs identified that Uttley et al. (2023) found 67 discrete problems, not "90% of SLRs are useless."
2. **C-04 (metadata_error):** Both runs identified that the automation bias reference has wrong year/venue. Actual sources: Goddard et al. JAMIA 2012 or Lyell & Coiera JAMIA 2017.
3. **C-06 (author_conflation):** Both runs identified that Storey authored cognitive debt alone (arXiv:2603.22106, 2026), Ernst is on a different paper. Two authors/papers were merged with wrong year.
4. **C-08 (misattribution):** Both runs found no "Budgen (2015)" paper with numbers 47 vs 38. The numbers are unverifiable.

## Robustness Assessment

**Result: ROBUST (94.1% exact match, 100% substantive agreement)**

- >= 90% agreement: ROBUST
- 80-89% agreement: acceptable
- < 80% agreement: concern

The single disagreement (S-08) is a procedural improvement, not a substantive contradiction. When excluding procedural gaps, the agreement is 100%.

## Cross-Dataset Comparison

| Dataset | Agreement Rate | Assessment |
|---------|---------------|------------|
| Dataset A (this run) | 94.1% (16/17) | ROBUST |
| Dataset B (prior run) | 91.9% (34/37) | ROBUST |

Both datasets show robust reproducibility above the 90% threshold.

## Methodology Notes

- Each source was independently verified via arXiv, DOI lookups, and web search
- 4 parallel verification agents were used to cover all 17 sources
- No reference was made to original verdicts during verification
- Original CSV was used only for source IDs and names
