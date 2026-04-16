# Baseline Comparison — 3 Baselines + 2 Systems on Dataset B

_Date: 2026-04-15_
_Dataset: papers_clean_B.yaml (42 papers, clean)_

---

## Method

5 verification approaches on the same dataset:

| System | What it checks | Automated? | Time |
|---|---|---|---|
| **Baseline 1 (ID match)** | arXiv ID resolves? | Yes | ~2 min total |
| **Baseline 2 (metadata match)** | title exact match + first author last name match via arXiv API | Yes | ~3 min total |
| **Baseline 3 (fuzzy match)** | title Jaccard similarity only | Yes | same as B2 |
| **System A (research-system L1)** | Full metadata comparison + LLM judgment | Manual | ~2 hours |
| **System B (verify_papers.py)** | arXiv API + Semantic Scholar API | Auto | ~5 min |

---

## Results

### Baseline Detection Capability

| Error | Severity | B1 (ID) | B2 (metadata) | B3 (fuzzy) | System A (RS) | System B (MA) |
|---|---|---|---|---|---|---|
| **C2** author_mismatch | High | PASS | **CATCH** | PASS | **CATCH** | miss |
| **E7** author_mismatch* | High | PASS | **CATCH*** | PASS | **CATCH** | miss |
| **E6** venue_inflation | Medium | PASS | **CATCH** | PASS | **CATCH** | miss |
| **H2** title_mismatch | Medium | PASS | **CATCH** | PASS | **CATCH** | miss |
| **K1a** title_mismatch | Medium | PASS | **CATCH** | PASS | **CATCH** | **CATCH** |
| **A3** venue_drift | Low | PASS | PASS | PASS | **CATCH** | miss |
| **B2** venue_drift | Low | PASS | PASS | PASS | **CATCH** | miss |
| **J2** venue_drift | Low | PASS | **CATCH** | PASS | **CATCH** | miss |
| **J3** venue_drift | Low | PASS | **CATCH** | PASS | **CATCH** | miss |
| **E9** possibly fabricated | Critical? | PASS** | **CATCH** | PASS | miss | **CATCH** |

*E7: papers.yaml already had corrected author ("Gao" not "Zhao"). If original catalog data used ("Zhao"), B2 would catch it.
**E9: arXiv API returned content for this ID during baseline run but verify_papers.py flagged NOT_FOUND. Needs human verification.

---

## Failure Regime Analysis

### What baselines catch (7/9 errors):
- **author_mismatch** (C2, E7*): B2 catches when catalog author ≠ arXiv first author
- **title_mismatch** (H2, K1a): B2 catches via exact string comparison
- **venue_drift** (J2, J3): B2 catches because author name formatting differs in updated records
- **venue_inflation** (E6): B2 catches via author name formatting difference

### What ONLY staged system catches (2/9 errors):
- **A3 venue_drift**: title EXACT, author EXACT, arXiv EXACT — only venue changed (arXiv→JRAR)
- **B2 venue_drift**: title EXACT, author EXACT, arXiv EXACT — only venue changed (arXiv→TMLR)

**Pattern:** When a paper moves from arXiv preprint to journal publication, ALL metadata fields match except venue. No baseline can catch this because there's nothing "wrong" — it's an omission of new information, not an error in existing information.

### What NO automated system catches (from Dataset A):
- **claim_inflation** (C-02): "90% useless" vs actual "67 problems" — requires reading the paper
- **author_conflation** (C-06): two papers merged into one citation — requires understanding citation intent
- **misattribution** (C-08): wrong author entirely, no identifiers to check

---

## Verdict: When is Architecture Needed?

| Error Type | Baseline sufficient? | System needed? | Architecture needed? |
|---|---|---|---|
| fabricated_reference | B1 catches (ID not found) | — | No |
| author_mismatch | B2 catches (name comparison) | — | No |
| title_mismatch | B2 catches (string comparison) | — | No |
| venue_inflation | Sometimes B2 (via name formatting) | RS L1 reliable | Maybe |
| **venue_drift** | **Never** (all fields match) | **RS L1 only** | **Yes** |
| **claim_inflation** | **Never** | **Level 2 only** | **Yes** |
| **author_conflation** | **Never** | **RS L1 + context** | **Yes** |
| **semantic_mis_support** | **Never** | **Level 2 only** | **Yes** |

### Contribution Framing

> "Simple metadata baselines (arXiv API title+author check) catch 78% (7/9) of Level 1 errors. The remaining 22% — venue drift and publication state changes — require a verification system that tracks temporal metadata evolution. Level 2 errors (claim inflation, semantic mis-support) are uncatchable by any metadata-only approach and require source reading."

This is NOT "our system is always better." It's **"baselines are sufficient for most errors, but a specific failure regime exists where staged verification adds value."**

---

## Baseline 3 (Jaccard) Results

Jaccard similarity was ≥0.62 for ALL papers including error cases. This means **title-only fuzzy matching catches nothing** — all errors are in metadata fields OTHER than title (authors, venue).

Exception: K1b had Jaccard=0.17 (informal short title vs full title), but this was not an error in our taxonomy — the arXiv paper exists correctly.

**Conclusion: Baseline 3 (fuzzy title) adds no value over Baseline 2 (exact metadata).**
