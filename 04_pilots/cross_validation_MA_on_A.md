# Cross-Validation: meta-architect verify_papers.py on Dataset A (16 sources → 13 papers)

_Date: 2026-04-15_
_System: meta-architect verify_papers.py (arXiv API + Semantic Scholar API)_
_Dataset: papers_clean_A.yaml (13 papers; 3 non-papers excluded: S-06 PyPI, S-07 API, S-09 platform)_
_Cache state: CLEAN (fresh YAML, no prior verification)_

---

## Execution Note

Dataset A sources were originally cataloged with abbreviated titles and minimal author info (e.g., "citecheck" instead of full arXiv title). Several WARNINGS below are **data preparation artifacts**, not verify_papers.py findings.

---

## Results Summary

| Category | Count | Papers |
|---|---|---|
| arXiv EXISTS | 5/5 with arXiv IDs | S-03, S-04, S-05, C-06, C-07 |
| S2 found (via DOI) | 4 | S-02, C-01, C-05, S-05 |
| S2 not found | 2 | S-01, S-08 |
| S2 rate-limited (429) | 4 | S-03, S-04, C-06, C-07 |
| **Skipped (no identifiers)** | **3** | **C-02, C-04, C-08** |
| ERRORS | 0 | - |

---

## Critical Finding: verify_papers.py Cannot Check the Most Problematic Papers

The 3 papers skipped by verify_papers.py (no arXiv ID, no DOI) are **exactly the papers with the worst errors**:

| Paper | verify_papers.py | research-system L1 | Error |
|---|---|---|---|
| **C-02** (SLR problems) | ⬜ SKIPPED | PARTIAL | claim_inflation — "90% useless" overstated |
| **C-04** (Automation Bias) | ⬜ SKIPPED | PARTIAL | metadata_error — wrong year (2016→2012) and venue |
| **C-08** (Budgen 2015) | ⬜ SKIPPED | ERROR | misattribution — authors are Wohlin/Badampudi, not Budgen |

Additionally:
| **C-06** (Cognitive Debt) | arXiv ✅ exists | ERROR | author_conflation — two different authors/papers merged |

verify_papers.py confirmed C-06's arXiv paper exists but **could not detect the author conflation** because:
1. The arXiv ID resolves to a real paper (Storey's paper)
2. The catalog merged TWO papers (Storey + Ernst) into one citation
3. verify_papers.py doesn't check if a citation represents one paper or multiple conflated ones

---

## Comparison: verify_papers.py vs research-system Level 1 on Dataset A

| Error | RS L1 | verify_papers.py | Who caught it? |
|---|---|---|---|
| C-08 misattribution | ERROR | SKIPPED (no ID) | **RS only** |
| C-06 author conflation | ERROR | Not detected (arXiv exists) | **RS only** |
| C-04 wrong year/venue | PARTIAL | SKIPPED (no ID) | **RS only** |
| C-02 claim inflation | PARTIAL | SKIPPED (no ID) | **RS only** |
| S-08 procedural gap | UNVERIFIED | S2 not found | Both flagged |

### Score (Dataset A)

| Metric | research-system L1 | verify_papers.py |
|---|---|---|
| True errors detected | 4 | 0 |
| Papers checkable | 13/13 (manual) | 10/13 (API-based) |
| Papers skipped | 0 | 3 (no identifiers) |
| Time | ~90 min (manual) | ~3 min (automated) |

---

## Key Insight: API Coverage Gap

verify_papers.py's fundamental limitation on Dataset A: **it can only check papers with arXiv IDs or DOIs.** Non-CS papers (medical journals without arXiv, policy memos, Distill articles) fall through.

Dataset A has 5 arXiv papers, 4 DOI-only papers, 1 web article, 3 non-papers. The **error-rich papers** (C-02 JCE, C-04 JAMIA, C-08 no valid citation) are exactly in the DOI-only/no-identifier category where API-based tools are weakest.

This directly supports the **failure regime separation** argument:
- **API tools work well** for arXiv-heavy datasets (Dataset B = CS/AI papers)
- **Manual/LLM verification is necessary** for cross-domain datasets with mixed source types
- **Neither alone is sufficient** for real-world research workflows that cite across disciplines

---

## Comparison with Dataset B Results

| Metric | Dataset A (mixed) | Dataset B (CS/AI) |
|---|---|---|
| verify_papers.py coverage | 77% (10/13) | 88% (37/42) |
| verify_papers.py unique finds | 0 | 1 (E9) |
| RS L1 unique finds | 4 | 8 |
| Papers with no identifiers | 3 (23%) | 5 (12%) |

**Pattern:** As datasets become more cross-domain, API-based tools lose coverage and manual verification becomes more critical.
