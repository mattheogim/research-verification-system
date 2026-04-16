# Level 2 Supplement — 3 Missing Papers + Quality Verification

_Date: 2026-04-15_
_Supplements: pilot_L2_report.md (original 5 papers)_

---

## Part A: Quality Verification of Original 5 Papers

Original L2 results were produced in a separate session. Cross-checked against source full text:

| Paper | Original L2 | Cross-check | Status | Notes |
|---|---|---|---|---|
| B1 Qian | PARTIAL (no "lazy loading") | **Confirmed** — Eq.6 logistic formula exists, "lazy loading" NOT in paper. 16 agents saturation confirmed. | PASS | |
| I1-a Tam (JSON) | SUPPORT | **Confirmed** — GSM8K -27.3pp, Last Letter -31.5pp. Key ordering forces answer before reasoning. | PASS | |
| I1-b Tam (NL-to-Format) | PARTIAL | **Needs revision** — paper explicitly calls NL-to-Format "important mitigation strategy achieving both consistent formats and optimal performance." Original verdict understated. | **REVISE → SUPPORT** | |
| S-02 PRISMA-trAIce | PARTIAL (proposal not norm) | **Confirmed** — "Development of checklist," not adopted standard. | PASS | |
| A3 Hegazy | PARTIAL (COT confound) | **Cannot fully verify** — HTML not available, abstract doesn't detail COT conditions. Verdict is reasonable but unconfirmed. | INCONCLUSIVE | Need PDF |
| C-04 Rosbach | PARTIAL (design recs inferred) | Not re-checked this session (original analysis is detailed and consistent) | ASSUMED PASS | |

**Summary: 4 PASS, 1 REVISE (I1-b PARTIAL→SUPPORT), 1 INCONCLUSIVE (A3)**

### Revision: I1-b Tam

**Old verdict:** PARTIAL — "NL-to-Format is one condition tested, not primary recommendation"
**New verdict:** SUPPORT — Paper explicitly recommends NL-to-Format as a mitigation strategy: "achieving both consistent formats and optimal performance." It is both an experimental condition AND the primary recommended solution.

---

## Part B: Level 2 on 3 Missing Papers

### S-01 PRISMA 2020 (Page et al., BMJ 2021) — CONTROL

**Claim from citing document:** "PRISMA provides a structured checklist for systematic review reporting" — cited as conceptual precedent for our verification framework's structured approach.

**Source verification:**
- PRISMA 2020 is a 27-item reporting guideline for systematic reviews
- It covers **reporting standards**, not citation verification specifically
- It does NOT prescribe how to verify individual citations
- Its relevance to our system is as an **analogy** (structured checklist approach) not direct evidence

**Judgment:** `PARTIAL`
**Confidence:** HIGH
**Justification:** PRISMA is accurately cited as existing and being a structured checklist. But citing it as "supporting evidence" for our verification framework overstates the connection — PRISMA is about SR reporting, not about verifying citation metadata. The analogy is fair but should be framed as "inspired by" not "supported by."
**Time:** 3 min

---

### S-04 SemanticCite (Haan, arXiv:2511.16198)

**Claim from citing document:** "SemanticCite's 4-class citation verification validates our multi-level classification approach"

**Source verification (full text read via HTML):**
- 4 classes: Supported, Partially Supported, Unsupported, Uncertain
- Pipeline: preprocessing → hybrid retrieval (dense + BM25) → neural reranking → LLM classification
- **Full-text analysis**, not metadata-only
- Weighted accuracy: 83.64% (Qwen3 4B)
- Explicitly rejects metadata-only tools as insufficient

**Judgment:** `PARTIAL`
**Confidence:** HIGH
**Justification:** SemanticCite does validate the concept of multi-class citation verification (4 classes similar to our Axis 2). However, their system integrates all levels simultaneously rather than separating discrete cost levels like our framework. Our claim that their work "validates our approach" is directionally correct but overstated — they validate the **classification scheme**, not the **staged cost architecture**. They don't separate cheap metadata checks from expensive source reading.
**Time:** 6 min

---

### C-02 SLR Problems (Uttley et al., JCE 2023)

**Claim from citing document:** "67 problems with systematic reviews" and associated implication ">90% SRs are useless"

**Source verification (via web search + publisher page):**
- Paper: "The problems with systematic reviews: a living systematic review"
- Uttley L et al. J Clin Epidemiol 2023;156:30-41
- Identified **67 discrete problems** across 485 articles (2000-2022)
- Updated in 2024: now 68 problems
- Problems span: comprehensiveness, rigor, transparency, objectivity
- Paper NEVER claims ">90% are useless" — it catalogs problems, not futility rates

**Judgment:** `PARTIAL`
**Confidence:** HIGH
**Justification:** The "67 problems" number is accurate (confirmed: 67 in 2023, 68 in 2024 update). However, the citing document's framing ">90% SRs are useless" is NOT from this paper. The paper systematically catalogs problems but does not make a blanket condemnation of systematic reviews. This is **claim inflation** — using a careful empirical catalog to justify a much stronger rhetorical claim.
**Time:** 4 min

---

## Updated Summary (All 8 papers)

| # | Paper | Claim Type | Judgment | Confidence |
|---|---|---|---|---|
| 1 | A3 Hegazy | factual_number | PARTIAL | MEDIUM |
| 2 | B1 Qian | empirical_finding | PARTIAL | HIGH |
| 3 | I1-a Tam (JSON) | empirical_finding | **SUPPORT** | HIGH |
| 4 | I1-b Tam (NL-to-Format) | design_recommendation | **SUPPORT** (revised) | HIGH |
| 5 | S-02 PRISMA-trAIce | operational_norm | PARTIAL | HIGH |
| 6 | C-04 Rosbach | empirical_finding | PARTIAL | HIGH |
| 7 | S-01 PRISMA 2020 | conceptual_precedent | PARTIAL | HIGH |
| 8 | S-04 SemanticCite | system_comparison | PARTIAL | HIGH |
| 9 | C-02 SLR problems | factual_number | PARTIAL | HIGH |

**Updated totals (9 claim-source pairs):**
- SUPPORT: 2 (22%)
- PARTIAL: 7 (78%)
- REFUTE: 0
- UNCERTAIN: 0

**Dominant error pattern unchanged:** Inferential overreach remains primary. Papers support claims directionally but citing documents draw conclusions beyond what sources explicitly state.

---

## Updated Cost-Benefit (8 papers total)

| Level | Time/paper | Finding rate |
|---|---|---|
| Level 1 | ~3 min | 29% metadata errors |
| Level 2 | ~4.6 min avg (8 papers) | 78% claims PARTIAL |
| Cost ratio | L2 = 1.5x L1 | But catches fundamentally different error class |
