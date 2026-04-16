# Research Verification System

> LLM-generated paper catalogs contain **~24% metadata errors**. This system catches them.

A cost-efficient, multi-level verification framework for auditing academic paper citations produced by Large Language Models. Designed for researchers who use AI to build literature reviews, evidence tables, or paper catalogs — and need to know which citations are real.

---

## Key Results

Tested on **53 papers** across two independent datasets:

| Metric | Dataset 1 (16 sources) | Dataset 2 (37 papers) |
|:---|:---:|:---:|
| **Metadata accuracy** | 69% | 76% |
| **Errors found by Level 1** | 4/5 known (80%) | 9/37 (24%) |
| **False positives** | 0 | 0 |
| **Time per paper** | ~6 min | ~3 min |
| **Critical errors (FAIL)** | 2 | 2 |

### Error Types Discovered

```
Author misattribution  ██████████████  5% ← most dangerous (completely wrong author)
Venue inflation        ███████         3% ← workshop cited as main conference
Missing venue update   ████████████████████  11% ← arXiv → journal, not updated
Title confusion        ███████         3% ← similar papers mixed up
Metadata exact match   ████████████████████████████████████████████████████████  76%
```

### LLM Self-Verification Audit

When an LLM marks its own citations as `[VERIFIED]`:

```
Correct verifications:  ████████████████████████  83% (5/6)
Missed errors:          ████                     17% (1/6)
```

---

## How It Works

The system uses **cost-based staged verification** — cheap checks filter before expensive ones:

```
                          ┌─────────────────────────────────┐
                          │  Level 0: Structural Integrity  │
                          │  (format, schema, completeness) │
                          │  Cost: ~0 min/paper             │
                          └──────────────┬──────────────────┘
                                         │
                          ┌──────────────▼──────────────────┐
                          │  Level 1: Metadata Verification │
                          │  (arXiv, Crossref, Semantic S.) │
                          │  Cost: ~3-6 min/paper           │
                          │  ✓ Catches: wrong author, title │
                          │    venue, year, arXiv ID        │
                          └──────────────┬──────────────────┘
                                         │
                          ┌──────────────▼──────────────────┐
                          │  Level 2: Source Reading         │
                          │  (PDF/HTML, claim-evidence map)  │
                          │  Cost: ~30-60 min/paper         │
                          │  ✓ Catches: overclaim, scope    │
                          │    mismatch, misinterpretation   │
                          └──────────────┬──────────────────┘
                                         │
                          ┌──────────────▼──────────────────┐
                          │  Level 3: Cross-Verification    │
                          │  (inter-source consistency)     │
                          │  Cost: varies                   │
                          └─────────────────────────────────┘
```

Level 1 alone catches **80% of detectable errors** at **3 minutes per paper**.

---

## Repository Structure

```
research-verification-system/
├── 00_master/
│   └── README.md                          ← Project index (internal)
├── 01_architecture/
│   └── research_verification_architecture_v0.4.1.md  ← Verification framework
├── 02_operations/
│   └── research_operations_manual_v1.2.md ← Operational procedures
├── 03_records/
│   ├── chatGPT/                           ← QOC decision records
│   └── claude/                            ← Session records + QOC
├── 04_pilots/
│   ├── pilot_claude_v0.4.1_report.md      ← Pilot 1: 16 sources
│   ├── pilot_meta_architect_L1_report.md  ← Pilot 2: 37 papers
│   ├── pilot_meta_architect_L1_results.csv
│   ├── pilot_gpt_v0.4.1_report.md         ← GPT replication
│   ├── pilot2_L2_plan.md                  ← Level 2 plan
│   └── analysis_L1_system_evaluation.md   ← System evaluation
└── 05_evidence/
    ├── case_studies/
    └── source_tables/                     ← Paper catalogs + claim mappings
```

---

## Findings

### 1. LLM errors are conflation, not fabrication

LLMs don't invent papers. They mix up metadata between real, similar papers. A paper about "multi-agent debate" gets attributed to the wrong "et al." from a related paper. The arXiv ID resolves — but the authors are wrong.

### 2. Author misattribution is the most dangerous error

Two papers (5%) had **completely wrong first authors** — not misspellings, but different people entirely. These would pass cursory review ("the paper exists, the title matches") but corrupt citation records.

### 3. Venue inflation misrepresents evidence quality

One paper published at an **ICML workshop** was cited as an **ICML main conference** paper. Workshop and main conference papers have very different peer review standards — this inflates the credibility of the evidence.

### 4. LLM self-verification is incomplete

When an LLM tags its own citations as `[VERIFIED]`, it catches major errors but misses venue updates (papers that moved from arXiv preprint to journal publication). **83% reliable, 17% gap.**

### 5. Level 1 is high-ROI

At ~3 minutes per paper with zero false positives, Level 1 metadata verification is the single most cost-effective quality check for LLM-generated literature reviews.

---

## Pilot Summary

| Pilot | Dataset | Papers | Errors Found | Key Insight |
|:---|:---|:---:|:---:|:---|
| **Pilot 1** | Original evidence table | 16 | 4 FAIL, 1 PARTIAL | 80% error detection rate |
| **GPT Replication** | Same 16 sources | 16 | 2 FAIL | Hard failures caught by both LLMs |
| **Meta-Architect L1** | External project catalog | 37 | 2 FAIL, 7 PARTIAL | 24% raw error rate, 0 false positives |

---

## Related Work

| Project | Approach | Difference |
|:---|:---|:---|
| [Citation-Hallucination-Detection](https://github.com/Vikranth3140/Citation-Hallucination-Detection) | 3-stage pipeline (lookup → fuzzy → LLM) | Focuses on existence checking; we add claim-evidence alignment |
| [RefChecker](https://github.com/markrussinovich/refchecker) | Semantic Scholar + LLM web search | Automated tool; we provide a methodology framework |
| [hallucinated-citations](https://github.com/ethz-spylab/hallucinated-citations) | arXiv hallucination detection | Statistical analysis; we do per-paper forensic verification |
| [SemanticCite](https://arxiv.org/abs/2511.16198) | 4-class citation verification | ML classifier; we use structured manual + LLM hybrid |

This project is **methodology-first** — it provides a reproducible verification framework rather than a tool. The architecture (v0.4.1) and pilots serve as evidence for a research paper on LLM citation reliability.

---

## Status

- [x] Level 0-1 verification architecture (v0.4.1)
- [x] Pilot 1: 16 sources (Claude + GPT replication)
- [x] Pilot 2: 37 papers from external project
- [x] Claim mapping for Level 2 context
- [ ] Level 2 checklist finalization
- [ ] Level 2 pilot (5 papers, PDF reading)
- [ ] Automated Level 1 script (arXiv API)
- [ ] Cross-domain testing (medical, legal, physics)

---

## License

This project is part of ongoing research. Citation information will be added upon publication.
