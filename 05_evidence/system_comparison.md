# System Comparison: research-system vs meta-architect verification

_Date: 2026-04-16_
_Purpose: Side-by-side architecture comparison for paper Section 3_

---

## research-system (this project)

**Type:** Manual methodology framework
**Verification levels:** 4 (L0 structural → L1 metadata → L2 source reading → L3 cross-verification)
**Automation:** None — human/LLM executes checklist manually via WebFetch
**Error detection:** LLM reads arXiv page, compares all metadata fields, makes judgment
**Author check:** Full author list comparison (catches completely wrong authors)
**Venue check:** Compares catalog venue against current publication status (catches inflation + drift)
**Claim support:** Level 2 reads full paper text, judges claim-evidence alignment
**Output:** Markdown reports + CSV per pilot
**Hook/CI:** None
**Reproducibility:** Process documented (level2_checklist_v0.1.md), but manual execution varies by operator

## meta-architect verify_papers.py

**Type:** Automated Python script
**Verification levels:** 3 (L0 catalog → L1 API check → L2 manual reading)
**Automation:** L1 fully automated (arXiv API + Semantic Scholar API)
**Error detection:** API query → existence check + title similarity (Jaccard) + first author last name match
**Author check:** First author last name only (misses completely wrong authors when catalog uses "et al.")
**Venue check:** Via Semantic Scholar (but rate-limited, ~60% 429 errors in testing)
**Claim support:** Manual (read paper → create verified/{id}.md)
**Output:** Terminal report (errors/warnings/info) + papers.yaml status update
**Hook/CI:** PreToolUse hook (`check_paper_deps.py`) warns before coding without reading paper
**Reproducibility:** Fully reproducible (same script, same API calls → same results)

---

## Head-to-Head Results (Dataset B, 42 papers)

| Capability | research-system L1 | verify_papers.py |
|---|---|---|
| Papers checkable | 42/42 (100%) | 37/42 (88%) |
| Errors detected | 9 | 2 |
| **Unique finds** | **8** | **1** (E9 existence) |
| False positives | 0 | ~12 format warnings |
| Time | ~2 hours (manual) | ~5 minutes (auto) |
| author_mismatch (C2, E7) | ✅ caught | ❌ missed |
| venue_inflation (E6) | ✅ caught | ❌ missed |
| venue_drift (A3, B2, J2, J3) | ✅ caught | ❌ missed (S2 rate-limited) |
| title_mismatch (H2, K1a) | ✅ caught | ⚠️ K1a only |
| fabricated? (E9) | ❌ missed | ✅ caught |

## Head-to-Head Results (Dataset A, 16 sources)

| Capability | research-system L1 | verify_papers.py |
|---|---|---|
| Papers checkable | 16/16 (100%) | 10/13 (77%) |
| Errors detected | 4 | 0 |
| Skipped (no identifiers) | 0 | 3 (C-02, C-04, C-08) |
| Key finding | Catches all error types | Cannot check papers without arXiv/DOI |

---

## Why Neither Alone Is Sufficient

| Error regime | Best system | Why |
|---|---|---|
| Paper doesn't exist (fabricated) | verify_papers.py | API existence check is definitive |
| Wrong author (conflation) | research-system L1 | Requires full author list comparison |
| Wrong venue (inflation) | research-system L1 | Requires understanding venue hierarchy |
| Venue outdated (drift) | research-system L1 | Requires checking current publication state |
| No identifiers (non-arXiv) | research-system L1 | Manual search can find papers without IDs |
| Claim doesn't match source | research-system L2 | Requires reading paper content |
| Scale (100+ papers) | verify_papers.py | Automated, 5 minutes |

**Optimal workflow:**
1. verify_papers.py first (5 min, catches existence failures)
2. research-system L1 on remaining (3 min/paper, catches metadata quality)
3. research-system L2 on high-priority claims (5 min/paper, catches semantic errors)
