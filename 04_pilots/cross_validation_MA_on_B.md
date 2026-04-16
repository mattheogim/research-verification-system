# Cross-Validation: meta-architect verify_papers.py on Dataset B (37→42 papers)

_Date: 2026-04-15_
_System: meta-architect verify_papers.py (arXiv API + Semantic Scholar API)_
_Dataset: papers_clean_B.yaml (42 papers, all status=unverified, cache stripped)_
_Cache state: CLEAN (all verified_date, citation_count, semantic_scholar_id removed)_
_Note: Dataset B originally counted as 37 in papers-catalog.md; papers.yaml contains 42 entries (5 additional: E4 SSRN-only, J4/J5/J7/J8 no arXiv)_

---

## Execution Environment

- verify_papers.py copied to temp_clean_run/ (read-only from meta-architect)
- papers_clean_B.yaml: all 42 papers set to status=unverified
- verified/ directory: empty
- Semantic Scholar API: rate-limited (429 errors on ~60% of requests)
- arXiv API: all requests succeeded

---

## Results Summary

| Category | Count | Papers |
|---|---|---|
| arXiv EXISTS | 36/37 with arXiv IDs | All except E9 |
| arXiv NOT FOUND | **1** | **E9 (2603.04474)** |
| S2 found | 10 | C1,D3,E2,E6,E10,H2,I1,J3,J4,K5 |
| S2 rate-limited (429) | ~25 | Most papers |
| S2 not found | 1 | J1 |
| Skipped (no identifiers) | 5 | E4,J5,J7,J8,K2 |

---

## Critical Finding: E9 Does Not Exist on arXiv

verify_papers.py flagged **E9 (arXiv:2603.04474)** as "DOES NOT EXIST".

**Our Level 1 (WebFetch-based) said EXACT** — we found a page at arxiv.org/abs/2603.04474 and it returned content about error cascades in multi-agent systems.

**Possible explanations:**
1. arXiv API vs web page discrepancy (API may have different availability window)
2. The paper was temporarily available and then removed
3. Our WebFetch hit a cached/redirect page that appeared valid
4. **Our Level 1 made a false negative (missed a real error)**

**This needs human gold standard verification (Step 4).**

---

## Comparison: verify_papers.py vs research-system Level 1

| Error | research-system L1 | verify_papers.py | Who caught it? |
|---|---|---|---|
| **C2 author_mismatch** | FAIL | Not detected (✅ exists) | **RS only** |
| **E7 author_mismatch** | FAIL | Not detected (✅ exists) | **RS only** |
| **E6 venue_inflation** | PARTIAL | Not detected (S2 found, no venue check) | **RS only** |
| **H2 title_mismatch** | PARTIAL | INFO only (similarity=0.62, not flagged as warning) | **RS only** |
| **E9 possibly fabricated** | EXACT (false negative?) | ❌ DOES NOT EXIST | **MA only** |
| **A3 venue_drift** | PARTIAL | Not detected (S2 429 error) | **RS only** |
| **B2 venue_drift** | PARTIAL | Not detected (S2 429 error) | **RS only** |
| **J2 venue_drift** | PARTIAL | Not detected (S2 429 error) | **RS only** |
| **J3 venue_drift** | PARTIAL | Not detected (S2 found, venue not checked) | **RS only** |
| **K1a title_mismatch** | PARTIAL | ⚠️ WARNING (similarity=0.17) | **Both** |

### Score

| Metric | research-system L1 | verify_papers.py |
|---|---|---|
| True errors detected | 9 (possibly 8 if E9 is wrong) | 2 (E9 + K1a) |
| Unique finds | 8 | 1 (E9) |
| False positives | 0 (pending gold) | ~12 (false "author mismatch" warnings for "et al." formatting) |
| Time | ~2 hours (manual) | ~5 minutes (automated) |

---

## Why verify_papers.py Misses Author Errors

The script checks: `first_author_last_name(catalog) == first_author_last_name(arXiv)`

For C2: catalog says "Li et al." → script extracts "Li" → arXiv first author is "Alireza Salemi" → script extracts "Salemi" → **should trigger mismatch**.

But looking at the output, C2 got **no warning**. This suggests:
1. The S2 check for C2 was rate-limited (429 error)
2. The arXiv title check passed (correct title)
3. The author check uses arXiv API which returns "Alireza Salemi" but the name extraction/comparison failed silently

**This is a bug or limitation in verify_papers.py's author matching logic** — it catches "formatting mismatches" (et al. vs full name) but misses **completely wrong first authors** when the catalog uses an abbreviated form like "Li et al." and the extraction doesn't match against the full author list.

---

## Key Insight for Paper

**The two systems are complementary, not competing:**

| Error type | Best caught by | Why |
|---|---|---|
| fabricated_reference (paper doesn't exist) | **verify_papers.py** | API existence check is definitive |
| author_mismatch (wrong person) | **research-system L1** | Requires full author list comparison, not just first-author-last-name |
| venue_inflation (workshop→conference) | **research-system L1** | Requires understanding venue hierarchy |
| venue_drift (preprint→journal) | **research-system L1** | Requires checking current publication status |
| title_mismatch (similar titles confused) | **Both** (different sensitivity) | verify_papers.py uses Jaccard, RS uses semantic comparison |

**Neither system alone catches everything. The staged combination catches more than either alone.**

This directly supports the "cost-aware staged verification" framing:
1. Run verify_papers.py first (5 min, automated, catches existence failures)
2. Run research-system L1 on the rest (3 min/paper, catches metadata quality issues)
3. Escalate to Level 2 for claim-evidence alignment
