# Research Verification System

> LLM-generated paper catalogs contain **29-31% metadata errors**. Simple baselines catch 78% — but **venue drift and inferential overreach require staged verification.**

A cost-aware, multi-level verification framework for auditing academic paper citations in AI-assisted research workflows. Tested on 98 papers across 5 datasets, with human gold standard validation.

---

## Key Results

| Metric | Value |
|:---|:---|
| **Total papers verified** | 98 (5 datasets) |
| **Level 1 precision** | 91.7% (human gold standard, n=20) |
| **Level 1 recall** | 73.3% |
| **F1 score** | 0.815 |
| **Clean re-run agreement** | 91.9% (robust) |
| **False positive rate** | 0 across all datasets |

### Error Rates by Dataset

```
LLM-generated (no review)     ████████████████████████████████████████  100%  (20/20)
PubMed medical                ████████████████                          40%   (4/10)
LLM-curated (A)               ████████████                              31%   (5/16)
LLM-curated (B)               ███████████                               29%   (12/42)
Human-curated (awesome-list)  █████                                     13%   (2/15)
```

### What Baselines Catch vs What Architecture Catches

```
                Baseline 2    Staged System    Level 2 Only
                (metadata)    (RS Level 1)     (source reading)
                ──────────    ────────────     ─────────────
author_mismatch    ✓              ✓
title_mismatch     ✓              ✓
venue_inflation    ✓              ✓
venue_drift        ✗              ✓              
inferential        ✗              ✗               ✓
  overreach
                ──────────    ────────────     ─────────────
Coverage:         78%            100%           +83% claims
                                                 partial
```

**Baselines are enough for 78% of errors.** Staged verification adds value only for venue drift (where all metadata fields match) and inferential overreach (where the paper exists but doesn't support the specific claim).

---

## Two Systems Are Complementary

Cross-validation of two independently designed verification systems on the same datasets:

| | research-system L1 found | Missed |
|---|---|---|
| **verify_papers.py found** | 1 (title) | 1 (E9 existence) |
| **Missed** | 8 (authors, venues) | — |

Neither system alone catches everything.

---

## Error Taxonomy (2-Axis)

**Axis 1 — Metadata Correctness:**

| Type | Definition | Frequency |
|---|---|---|
| `fabricated_reference` | Paper doesn't exist | 0% (in curated catalogs) |
| `author_mismatch` | Completely wrong author attribution | 5% |
| `venue_inflation` | Stronger venue reported than actual | 3% |
| `venue_drift` | Publication state change not tracked | 14% |
| `title_mismatch` | Confused with similar paper | 5% |

**Axis 2 — Claim Support (Level 2):**

| Type | Frequency (n=5) |
|---|---|
| Full support | 17% |
| Partial (inferential overreach) | 83% |

---

## How It Works

```
Level 0  ──→  Level 1  ──→  Level 2  ──→  Level 3
(schema)     (metadata)    (source)     (cross-ref)
~0 min       ~3 min        ~5.6 min     varies
             ↓              ↓
         catches 78%    catches overreach
         of all errors  (83% partial)
```

Cost-based escalation: cheap checks filter before expensive ones.

---

## Experiments Completed

| Step | What | Result |
|:---|:---|:---|
| Pilot 1 | L1 on 16 sources (Claude + GPT) | 80% detection, 0 FP |
| Pilot 2 | L1 on 42 papers (meta-architect) | 29% error rate, 0 FP |
| Clean re-run | Same 42 papers, fresh session | 91.9% agreement |
| Cross-validation | RS vs verify_papers.py on both datasets | Complementary (8+1 unique) |
| Baseline comparison | 3 baselines + 2 systems | 78% baseline-catchable |
| Human gold | 20 papers, human-verified | P=91.7%, R=73.3% |
| Level 2 | 5 papers, source reading | 83% partial support |
| Dataset C | 45 papers (CS + medical + curated) | 100% / 40% / 13% rates |

---

## Repository Structure

```
research-verification-system/
├── 00_master/README.md              ← Internal project index
├── 01_architecture/                 ← v0.4.1 verification framework
├── 02_operations/                   ← v1.2 operations manual
├── 03_records/                      ← QOC decisions + session logs
├── 04_pilots/                       ← All experiment reports + CSVs
│   ├── experiment_master_plan.md    ← 10-step experiment design
│   ├── error_taxonomy.md            ← 2-axis formalized taxonomy
│   ├── baseline_comparison.md       ← 5-system comparison
│   ├── statistical_analysis.md      ← CI, Kappa, P/R/F1
│   ├── paper_outline.md             ← Conference paper draft structure
│   └── (12 more pilot reports + CSVs)
├── 05_evidence/
│   ├── gold_standard_20_*.md        ← Human verification results
│   └── source_tables/               ← Paper catalogs + claim mappings
└── temp_clean_run/                  ← Isolated experiment scripts
```

---

## Related Work

| Project | Focus | Our Difference |
|:---|:---|:---|
| [CiteAudit](https://arxiv.org/abs/2602.23452) (2026) | Fabricated citation detection (9,442 citations) | We address **conflation**, not fabrication |
| [SemanticCite](https://arxiv.org/abs/2511.16198) | 4-class citation support verification | We add **cost-aware staged escalation** |
| [RefChecker](https://github.com/markrussinovich/refchecker) | Automated checking tool | We provide **methodology + failure regime analysis** |

Our contribution is not a better tool — it's identifying **where baselines are sufficient and where architecture is needed.**

---

## Status

- [x] Verification architecture (v0.4.1) + operations manual (v1.2)
- [x] 98 papers verified across 5 datasets
- [x] 3 baselines + 2 systems compared
- [x] Human gold standard (n=20)
- [x] Level 2 pilot (n=5)
- [x] Error taxonomy formalized (2-axis)
- [x] Statistical analysis (CI, Kappa, P/R/F1)
- [x] Paper outline drafted
- [ ] Paper writing
- [ ] Scale to n=200+ for tighter CI

---

## License

This project is part of ongoing research. Citation information will be added upon publication.
