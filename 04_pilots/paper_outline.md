# Paper Outline — Cost-Aware Staged Verification of LLM-Generated Citations

_Target: Conference short/full paper_
_Pre-registered thresholds: BOTH PASSED (improvement ≥20%, precision ≥0.85)_

---

## Title Options

1. "Metadata Conflation in LLM-Generated Research Catalogs: A Cost-Aware Staged Verification Framework"
2. "Beyond Fabrication: Detecting Citation Conflation in AI-Assisted Research Workflows"
3. "When Baselines Are Enough and When They're Not: Failure Regimes in LLM Citation Verification"

---

## Abstract (~250 words)

**Problem:** LLMs generate plausible-looking paper catalogs, but metadata accuracy is unreliable. Prior work (CiteAudit, SemanticCite) focuses on fabricated citations — papers that don't exist. We address a different error regime: **metadata conflation** — papers that exist but have wrong authors, inflated venues, or unsupported claims.

**Method:** We present a cost-aware staged verification framework with four levels (L0-L3) and evaluate it on 98 papers across 5 datasets. We compare against 3 baselines and 1 automated verification system (verify_papers.py), with 20-paper human gold standard.

**Results:**
- LLM-curated catalogs contain 28-31% metadata errors; pure LLM generation reaches 100%
- Simple metadata baselines catch 78% of Level 1 errors; venue drift (22%) requires staged verification
- Level 1 precision: 91.7%, recall: 73.3% (F1=0.815) against human gold
- Two verification systems are complementary, not competing: research-system finds 8 unique errors, automated system finds 1
- Level 2 source reading reveals 83% of citations have inferential overreach — a category absent from existing taxonomies
- Clean re-run agreement: 91.9% (process is robust)

**Contribution:** We identify failure regimes where cheap baselines are sufficient vs. where staged architecture is needed, provide a 2-axis error taxonomy (metadata correctness + claim support), and show that citation errors in curated catalogs differ fundamentally from fabricated citations.

---

## 1. Introduction

- LLMs increasingly used to build literature reviews, evidence tables, paper catalogs
- Known problem: hallucinated citations (CiteAudit 2026, SemanticCite 2025)
- Less studied problem: metadata conflation in papers that DO exist
  - Wrong author (5%): "Zhao et al." → actual author is Gao
  - Venue inflation (3%): workshop paper cited as main conference
  - Venue drift (11%): preprint→journal not updated
  - Inferential overreach: paper supports claim partially but is cited as full support
- These errors are different from fabrication: they pass existence checks
- Research question: What verification architecture is cost-effective for which error types?

---

## 2. Related Work

### 2.1 Citation Fabrication Detection
- CiteAudit (2026): multi-agent pipeline, 9,442 citations, 97% accuracy, 100% recall on fabricated refs
- RefChecker: Semantic Scholar + LLM web search
- hallucinated-citations (ETH Zurich): statistical analysis of arXiv
- **Gap:** These detect fabricated citations. Our error regime (conflation) passes their checks.

### 2.2 Citation Support Verification
- SemanticCite (2025): 4-class (support/contradict/irrelevant/uncertain)
- PaperQA2: superhuman on biology QA, not forensic verification
- **Gap:** SemanticCite classifies support but doesn't measure cost or identify when simple baselines suffice.

### 2.3 Human Citation Errors
- Baethge & Jergas (2025): 16.9% human quotation error rate
- Walters & Wilder (2023): LLM fabricated citations in academic writing
- **Our contribution:** LLM errors differ in KIND from human errors (author conflation vs. typos)

---

## 3. Method

### 3.1 Staged Verification Framework (v0.4.1)
- Level 0: Structural integrity (format, schema)
- Level 1: Metadata verification (arXiv/S2/Crossref API + LLM comparison)
- Level 2: Source reading (claim-evidence alignment)
- Level 3: Cross-verification (inter-source consistency)
- Cost escalation: L1 ~3 min/paper, L2 ~5.6 min/paper

### 3.2 Error Taxonomy (2-axis)
- Axis 1: Metadata correctness (fabricated, author_mismatch, title_mismatch, venue_inflation, venue_drift, identifier_mismatch)
- Axis 2: Claim support correctness (full, partial, no_support, contradicts)
- Operational definitions for each type (not interpretive)

### 3.3 Experimental Design
- 5 datasets (A: 16, B: 42, C-1: 20, C-2: 15, C-3: 10)
- 5 verification approaches (3 baselines + 2 systems)
- Human gold standard (n=20, 1 human annotator + 2 LLM separately prompted)
- Cache elimination protocol (clean re-runs, fresh sessions)
- Pre-registered venue thresholds

---

## 4. Results

### 4.1 Error Rates Across Datasets
- Table: error rates + 95% Wilson CI for each dataset
- Key finding: curation process matters more than LLM involvement (100% vs 13%)

### 4.2 Baseline Sufficiency Analysis (Failure Regimes)
- Table: which baselines catch which error types
- Key finding: Baseline 2 catches 78%; venue_drift requires staged system
- Figure: failure regime diagram

### 4.3 Cross-System Complementarity
- Table: detection by system (RS vs MA vs baselines)
- Key finding: neither alone catches everything; combined = 10 vs 9 or 2

### 4.4 Human-Aligned Evaluation
- Confusion matrix, P/R/F1
- Disagreement analysis (5 cases)
- Systematic blind spot: arXiv metadata gaps

### 4.5 Level 2: Inferential Overreach
- 5/6 claims PARTIAL — dominant error is overreach
- This is NOT in CiteAudit's taxonomy
- Downstream impact: 2-3 design decisions affected

---

## 5. Discussion

### 5.1 When Baselines Are Enough
- fabricated_reference: ID match sufficient
- author_mismatch: metadata match sufficient
- title_mismatch: metadata match sufficient

### 5.2 When Architecture Is Needed
- venue_drift: all metadata fields match, only venue state changed
- inferential_overreach: paper exists and is "about" the topic but doesn't support the specific claim
- author_conflation: two papers merged into one citation

### 5.3 Practical Recommendations
1. Always run ID + metadata baseline first (free, catches 78%)
2. Use staged system for cross-domain catalogs (non-arXiv coverage gap)
3. Level 2 is expensive but reveals qualitatively different errors

---

## 6. Limitations

- n=98 total, CI still wide (±10% on combined)
- Human gold: 1 annotator (not 3), Kappa moderate (0.444)
- LLM pre-training cache cannot be eliminated
- Domain bias: primarily CS/AI papers (PubMed subset small)
- Level 2 is feasibility pilot (n=5), not comprehensive
- LLM verifying LLM (partial circularity, mitigated but not solved)
- Subtitle truncation boundary: EXACT vs PARTIAL is judgment call

---

## 7. Conclusion

We show that LLM citation errors in curated catalogs are fundamentally different from fabricated citations: they are metadata conflation in real papers, not invention. Simple baselines catch most errors, but a specific failure regime (venue drift, inferential overreach) requires staged verification. Two independently designed systems are complementary, not competitive — neither alone catches everything.
