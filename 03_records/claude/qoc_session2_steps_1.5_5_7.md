# QOC Record: Session 2 — Steps 1.5, 5, 7

**Date:** 2026-04-15
**Session:** Clean re-run + Level 2 + Dataset C
**Model:** Claude Opus 4.6 (1M context)

---

## QOC-1: Title Abbreviation Threshold (Step 1.5)

**Question:** When a catalog title abbreviates the full paper title (e.g., "LMs" → "Language Models", subtitle omission), should this be EXACT or PARTIAL?

**Options:**
- O1: Strict — any title difference = PARTIAL
- O2: Lenient — standard bibliographic abbreviations = EXACT, substantive differences = PARTIAL
- O3: Binary — only check if paper is correctly identified

**Criteria:**
- Consistency with academic citation norms
- Sensitivity to genuine errors
- Reproducibility across verifiers

**Decision: O2 (Lenient)**
Standard abbreviations (LMs, LLMs, MAS), subtitle omission after colon, and missing articles ("a", "the") treated as EXACT. Substantive title differences (wrong words, different paper name) = PARTIAL. This matches standard bibliographic practice and gave 91.9% agreement vs the original run.

---

## QOC-2: NOT_VERIFIED → Verified Status (Step 1.5)

**Question:** When a paper was NOT_VERIFIED in the original run (paywall) but verified in the clean re-run (web search found metadata), how to count this in agreement?

**Options:**
- O1: Count as disagreement (different verdicts)
- O2: Exclude from agreement calculation (access-dependent)
- O3: Count as improvement (clean run is more thorough)

**Decision: O2 (Exclude)**
Report both metrics: strict agreement including NOT_VERIFIED (82.9%) and verifiable-only agreement (91.9%). The access difference is an environmental variable, not a process reliability issue.

---

## QOC-3: Level 2 SUPPORT vs PARTIAL Boundary (Step 5)

**Question:** When a cited paper contains relevant evidence but the citing document draws inferences beyond what the source explicitly states, is this SUPPORT or PARTIAL?

**Options:**
- O1: SUPPORT — the inference is reasonable
- O2: PARTIAL — the source doesn't explicitly make the claim
- O3: Case-by-case judgment

**Decision: O2 (PARTIAL)**
Applied consistently: if the citing document draws a design recommendation (e.g., "lazy loading") that the source paper doesn't mention, this is PARTIAL even if the inference is reasonable. The rationale: Level 2 measures claim-source alignment, not reasonableness of inference. Documented as "inferential overreach" pattern.

---

## QOC-4: Dataset C-1 Circularity (Step 7)

**Question:** Using the same LLM (Claude) to both generate and verify citations creates circularity. How to handle?

**Options:**
- O1: Disqualify C-1 entirely
- O2: Keep but flag as limitation
- O3: Use different model for verification (GPT)

**Decision: O2 (Keep + flag)**
The 100% error rate finding is too striking to discard. Circularity would bias toward *under*-detection (same model might reproduce same errors), yet verification still caught all 20 papers as erroneous. This actually strengthens the finding — even with circularity bias, errors are detectable. Flagged as limitation in report.

---

## QOC-5: C-3 Deliberately Planted Errors (Step 7)

**Question:** C-3 includes 2 deliberately planted wrong citations. Should these count in the error rate?

**Options:**
- O1: Include all (report 40% error rate)
- O2: Exclude planted errors (report 25% "natural" error rate)
- O3: Report both rates

**Decision: O3 (Report both)**
Total error rate: 4/10 = 40%. Natural error rate (excluding planted): 2/8 = 25%. Both are informative. The planted errors validate that the verification process catches deliberate errors; the natural errors show the unforced LLM citation error rate.
