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
| Claude Session | Full session record Phase 1-11 (EN) | `03_records/claude/session_record_20260415.md` |
| **QOC Pilot MA L1** | Decision log for meta-architect Level 1 pilot | `03_records/claude/qoc_pilot_meta_architect_L1.md` |

### Pilots

| File | Content | Path |
|---|---|---|
| Claude Pilot Report | Level 1 test on 16 sources | `04_pilots/pilot_claude_v0.4.1_report.md` |
| Claude Pilot Results | Source-by-source CSV | `04_pilots/pilot_claude_v0.4.1_results.csv` |
| GPT Pilot Report | Replication run | `04_pilots/pilot_gpt_v0.4.1_report.md` |
| **Pilot 2 Plan** | Level 2 source reading plan (5 sources) | `04_pilots/pilot2_L2_plan.md` |
| **MA L1 Report** | Level 1 on 37 meta-architect papers (9 errors found) | `04_pilots/pilot_meta_architect_L1_report.md` |
| **MA L1 Results** | Source-by-source CSV (37 rows) | `04_pilots/pilot_meta_architect_L1_results.csv` |

### Evidence

| Dir / File | Purpose |
|---|---|
| `05_evidence/case_studies/` | New case studies (existing tables stay in v0.4.1 §12-13) |
| `05_evidence/source_tables/` | Standalone source tables for future pilots |
| `05_evidence/source_tables/meta_architect_papers.md` | **37 papers** from meta-architect (snapshot) |
| `05_evidence/source_tables/meta_architect_claim_mapping.md` | Claim-to-paper mapping for Level 2 context |
| `05_evidence/source_tables/legalize_sources.md` | Legalize note (no academic papers — legislative data only) |

---

## Key Facts (established)

1. LLM-generated paper lists: ~70% accurate (16 sources, independently confirmed)
2. **LLM-generated paper catalogs: 76% metadata-accurate** (28/37 exact, meta-architect pilot)
3. Error types: conflation, not fabrication (confirmed across both datasets)
4. **Author attribution errors: 5%** (2/37, most dangerous type — complete wrong author)
5. Level 1 catches hard failures: 2/2 in both pilots
6. Level 1 does NOT catch semantic errors
7. **Meta-architect VERIFIED tag reliability: 83%** (5/6 correct, 1 missed venue)
5. PaperQA2: superhuman on biology QA, not a forensic verifier
6. Automation bias: 7% expert reversal rate
7. Human quotation errors: 16.9% total, 8.0% major (Baethge & Jergas 2025)

## Open Hypotheses

1. Level 2 catches scope/overclaim errors in fresh sources
2. Full workflow improves accuracy beyond Level 1
3. 18-step pipeline cost-feasibility
4. System works on math/CS papers
5. ~~research-system Level 1/2 vs meta-architect's own verification~~ → **ANSWERED (Phase 1)**: Level 1 found 9 errors in 37 papers; meta-architect's VERIFIED missed 1/6. Level 1 adds clear value.
6. **Level 2 on meta-architect papers** — do UNVERIFIED key numbers (B1 scaling formula, C1 token savings) hold up against original text?

## Next Steps

1. **Pilot 2 — Level 2 실행** (plan ready: `04_pilots/pilot2_L2_plan.md`)
   - Step 0: Level 2 checklist 작성
   - Step 1: Claim mapping (5 sources)
   - Step 2: PDF 접근성 확인 + fallback
   - Step 3: 실행 + wall-clock timing
2. Merge v1.2 operational elements into v0.4.1
3. Replace scoring with 0/1/2 anchor format
4. Test on completely new topic
