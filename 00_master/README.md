# Research Verification System — Project Index

> We are not trying to make scientific AI automatically trustworthy; we are building a system where research claims remain checkable, traceable, version-aware, and revisable even when every component can fail.

---

## Documents

### Core (paired — do not merge)

| Doc | Role | Path |
|---|---|---|
| **v0.4.1** | Verification Architecture (spine) | `01_architecture/research_verification_architecture_v0.4.1.md` |
| **v1.2** | Research Operations Manual (muscles) | `02_operations/research_operations_manual_v1.2.md` |

### Records

| File | Content | Path |
|---|---|---|
| QOC Master | Decision log + rationale (KO) | `03_records/chatGPT/qoc_master.md` |
| QOC Summary | Project summary (KO) | `03_records/chatGPT/qoc_summary_ko.md` |
| Architecture Record | Architecture evaluation (EN) | `03_records/chatGPT/architecture_record_v1.md` |
| Claude Session 1 | Full session record Phase 1-11 (EN) | `03_records/claude/session_record_20260415.md` |
| QOC Session 1 | MA L1 pilot decisions | `03_records/claude/qoc_pilot_meta_architect_L1.md` |
| QOC Session 2 | Steps 1.5+5+7 decisions | `03_records/claude/qoc_session2_steps_1.5_5_7.md` |
| QOC Session 3 | Steps 4+6+8+L2, **error log included** | `03_records/claude/qoc_session3_steps_4_6_8_L2.md` |

### Pilots

| File | Content | Path |
|---|---|---|
| Pilot 1 Report | Level 1 on 16 sources | `04_pilots/pilot_claude_v0.4.1_report.md` |
| Pilot 1 Results | Source-by-source CSV | `04_pilots/pilot_claude_v0.4.1_results.csv` |
| GPT Pilot Report | Replication run (16 sources) | `04_pilots/pilot_gpt_v0.4.1_report.md` |
| Pilot 2 Plan | Level 2 plan — **COMPLETED** | `04_pilots/pilot2_L2_plan.md` |
| MA L1 Report | Level 1 on 42 meta-architect papers | `04_pilots/pilot_meta_architect_L1_report.md` |
| MA L1 Results | 42-row CSV | `04_pilots/pilot_meta_architect_L1_results.csv` |
| Clean Re-run B | 42 papers, fresh session (91.9%) | `04_pilots/clean_rerun_L1_results.csv` + `comparison.md` |
| Clean Re-run A | 17 sources, fresh session (94.1%) | `04_pilots/clean_rerun_L1_A_results.csv` + `comparison.md` |
| Cross-val MA→A | verify_papers.py on Dataset A | `04_pilots/cross_validation_MA_on_A.md` |
| Cross-val MA→B | verify_papers.py on Dataset B | `04_pilots/cross_validation_MA_on_B.md` |
| Baseline Comparison | 3 baselines + 2 systems, failure regime | `04_pilots/baseline_comparison.md` |
| Error Taxonomy | 2-axis formalization + operational definitions | `04_pilots/error_taxonomy.md` |
| L2 Report | 5 papers source reading | `04_pilots/pilot_L2_report.md` + `results.csv` |
| L2 Supplement | 3 additional papers + quality verification | `04_pilots/pilot_L2_supplement.md` |
| L2 Checklist | Step-by-step Level 2 procedure | `04_pilots/level2_checklist_v0.1.md` |
| Dataset C Report | 45 papers (CS + medical + curated) | `04_pilots/dataset_C_report.md` + `results.csv` |
| Statistical Analysis | CI, Kappa, P/R/F1, venue threshold | `04_pilots/statistical_analysis.md` |
| System Evaluation | Strengths, weaknesses, improvements | `04_pilots/analysis_L1_system_evaluation.md` |
| Paper Outline | Conference paper draft structure | `04_pilots/paper_outline.md` |
| Experiment Plan | 10-step master plan + cache protocol | `04_pilots/experiment_master_plan.md` |

### Evidence

| File | Purpose | Path |
|---|---|---|
| Gold Standard Template | 20-paper verification template | `05_evidence/gold_standard_20_template.md` |
| Gold Standard Completed | Human-verified 20 papers (P=91.7% R=73.3%) | `05_evidence/gold_standard_20_completed.md` |
| System Comparison | RS vs MA side-by-side architecture | `05_evidence/system_comparison.md` |
| Dataset Construction | Construction rules + known biases | `05_evidence/dataset_construction_and_bias.md` |
| MA Papers Snapshot | 42 papers from meta-architect | `05_evidence/source_tables/meta_architect_papers.md` |
| Claim Mapping | Design decision → paper mapping (L2 context) | `05_evidence/source_tables/meta_architect_claim_mapping.md` |
| Competitor Analysis | CiteAudit detailed analysis + differentiation | `05_evidence/source_tables/competitor_analysis.md` |
| Legalize Sources | No academic papers (legislative data only) | `05_evidence/source_tables/legalize_sources.md` |

---

## Key Results (final)

1. **Error rates:** LLM-curated catalogs 29-31%, pure LLM generation 100%, human-curated 13%
2. **Error types:** conflation, not fabrication (0 fabricated in curated catalogs)
3. **Author mismatch:** 5% (most dangerous — completely wrong person)
4. **Venue drift:** 14% (baseline-uncatchable — only staged system finds)
5. **Level 1 precision:** 91.7%, recall 73.3%, F1 0.815 (human gold, n=20)
6. **Clean re-run:** A=94.1%, B=91.9% (both ROBUST)
7. **Baseline coverage:** 78% of L1 errors catchable by simple metadata match
8. **Two systems complementary:** RS finds 8 unique, MA finds 1 unique
9. **Level 2:** 78% of claims PARTIAL (inferential overreach dominant)
10. **Venue threshold:** Both PASS → conference eligible

## Answered Hypotheses

1. ~~Level 2 catches scope/overclaim~~ → **YES** (78% PARTIAL, inferential overreach)
2. ~~RS vs MA verification~~ → **Complementary** (neither alone sufficient)
3. ~~Baseline sufficient?~~ → **78% yes, 22% no** (venue_drift = architecture needed)

## Remaining

1. Paper writing (outline ready: `04_pilots/paper_outline.md`)
2. Scale to n=200+ for tighter CI (후속 연구)
3. Reproducibility protocol documentation
4. Test on additional domains (legal, physics)
