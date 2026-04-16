# Pilot 2: Level 2 Source Reading Report

**Date:** 2026-04-15
**Model:** Claude Opus 4.6 (1M context)
**Papers read:** 5 (2 research-system sources + 3 meta-architect sources)
**Total time:** ~28 minutes wall-clock

---

## Summary

| Paper | Claim Type | Judgment | Key Issue |
|-------|-----------|----------|-----------|
| A3 Hegazy | Factual number | **PARTIAL** | Numbers accurate but comparison not controlled (COT confound) |
| B1 Qian | Empirical finding | **PARTIAL** | Scaling law exists but "lazy loading" inference unsupported |
| I1 Tam (degradation) | Empirical finding | **SUPPORT** | Strong, direct evidence for JSON reasoning penalty |
| I1 Tam (hybrid pattern) | Design recommendation | **PARTIAL** | NL-to-Format is one condition tested, not primary recommendation |
| S-02 PRISMA-trAIce | Operational norm | **PARTIAL** | Proposal not adopted standard; "speculative_adoption" more accurate |
| C-04 Rosbach | Empirical finding | **PARTIAL** | 7% figure correct; design recommendations are citing doc's inference |

**Overall: 1 SUPPORT, 5 PARTIAL, 0 REFUTE, 0 UNCERTAIN** (out of 6 claim-source pairs from 5 papers)

---

## Goal 1: Can Level 2 be turned into a repeatable process?

**Answer: Yes, with caveats.**

The Level 2 checklist (see `level2_checklist_v0.1.md`) worked for all 5 papers. The key steps — claim identification, source span location, alignment judgment — were consistently applicable. However:
- Judgment subjectivity remains (SUPPORT vs PARTIAL boundary is fuzzy)
- Mathematical/statistical verification depth is limited
- Time varies significantly by paper complexity (4-8 min per paper)

---

## Goal 2: Does Level 2 find things Level 1 missed?

**Answer: Yes. 5 of 6 claims had issues invisible to Level 1.**

Level 1 confirmed these papers exist with correct metadata. Level 2 found:

| Paper | L1 Verdict | L2 Finding | What L1 Missed |
|-------|-----------|------------|----------------|
| A3 | PARTIAL (venue) | PARTIAL (numbers not controlled) | COT confound in the key comparison |
| B1 | EXACT | PARTIAL (no lazy loading) | "Lazy loading" not mentioned in source |
| I1 | EXACT | SUPPORT + PARTIAL | Degradation confirmed; hybrid pattern overstated |
| S-02 | EXACT | PARTIAL (not a norm) | Proposal vs adopted standard distinction |
| C-04 | N/A (L1 different paper) | PARTIAL (design recs inferred) | Citing doc infers design patterns not in source |

**Key insight:** The most common Level 2 error pattern is **inferential overreach** — the cited paper contains relevant evidence, but the citing document draws design conclusions or recommendations that go beyond what the source explicitly states. 4 of 5 PARTIAL judgments follow this pattern.

---

## Goal 3: How long does it take per source?

| Paper | Time (min) | Complexity |
|-------|-----------|------------|
| A3 Hegazy | 8 | Medium — needed to check specific numbers in tables |
| B1 Qian | 4 | Low — formula is clearly presented in one section |
| I1 Tam | 6 | Medium — two claims to verify, multiple experiments |
| S-02 PRISMA-trAIce | 5 | Medium — checklist items to map to claim pillars |
| C-04 Rosbach | 5 | Medium — needed to distinguish methodology from recommendations |

**Average: 5.6 min/paper** (vs Level 1 ~3 min/paper)
**Cost ratio: ~1.9x** Level 1

---

## Goal 4: Where does Level 2 break down?

1. **Judgment subjectivity:** The SUPPORT/PARTIAL boundary depends on how strictly you interpret "the claim matches the source." A lenient reading would give A3 and S-02 SUPPORT verdicts; a strict reading gives PARTIAL.

2. **Inferential claims are hardest:** When the citing document infers a design principle from empirical findings (B1 → lazy loading, C-04 → blind-first review), Level 2 must judge whether the inference is "reasonable" — this requires domain expertise.

3. **No cross-verification:** Level 2 cannot tell you if a *better* source exists for the claim, only whether the cited source supports it.

4. **Circularity:** Claude verifying claims that a system (partially designed with LLM assistance) generated. Mitigated by requiring literal source spans and human-reviewable output.

---

## Downstream Impact Analysis

### Case 1: A3 Hegazy — Diversity Premium Overstated

**Original claim:** "+9pp diversity improvement (91% vs 82%)" → justifies multi-model assignment in meta-architect.

**Level 2 finding:** The 82% homogeneous baseline uses COT prompting while the 91% diverse result's COT status is unclear. Without COT, homogeneous only reaches 80%, making the gap +11pp. With COT controlled, the gap might be smaller. No statistical robustness reported.

**Impact on design decision:** The multi-model assignment strategy in meta-architect relies on this diversity premium as empirical justification. The premium likely exists (the trend is clear) but its exact magnitude is uncertain. The design decision is probably sound but the quantitative justification should include the caveat that the cited comparison is not fully controlled.

**Recommendation:** Add caveat in architecture document; consider citing additional diversity studies for triangulation.

### Case 2: B1 Qian — Lazy Loading Lacks Source Support

**Original claim:** "Logistic growth formula" → justifies scaling + lazy loading design.

**Level 2 finding:** The paper presents a sigmoid scaling law showing quality saturation around 16 agents. This supports the scaling design. But "lazy loading" is never mentioned — the inference that saturation implies lazy instantiation is the citing document's design decision, not the source paper's recommendation.

**Impact on design decision:** The lazy loading pattern in `router.py` and `lazy_loader.py` cannot trace its justification to B1. The scaling saturation finding is valid, but the architectural response (lazy loading) needs its own justification — either from a different source or as an engineering decision documented separately.

**Recommendation:** Separate the citation: cite B1 for scaling saturation evidence, add a separate note that lazy loading is a design inference not sourced from B1.

### Case 3: C-04 Rosbach — Design Recommendations Are Inferred

**Original claim:** Automation bias → justifies blind-first review, label hiding, disagreement logging.

**Level 2 finding:** The 7% automation bias rate is accurately cited. But "blind-first review, label hiding, disagreement logging" are the citing document's design responses — the source paper used blind-first as experimental methodology but did not prescribe it as a system design feature.

**Impact on design decision:** The design features are well-motivated by the empirical findings, but the traceability chain has a gap. The paper provides the *problem evidence* (automation bias exists at ~7%), not the *solution prescription* (blind-first review).

**Recommendation:** Reframe the citation: "Motivated by Rosbach et al.'s finding of 7% commission error rate, we implement blind-first review as a mitigation strategy" (clearly attributing the design to our inference, not the source's recommendation).

---

## Cost-Benefit Summary

| Level | Time/paper | Errors found | Error type |
|-------|-----------|-------------|------------|
| Level 1 | ~3 min | 12/41 (29%) | Metadata: wrong authors, wrong venue, wrong title |
| Level 2 | ~5.6 min | 5/6 claims (83%) | Semantic: inferential overreach, uncontrolled comparisons, overstated normative authority |

**Level 2 cost is 1.9x Level 1, but catches a fundamentally different error class.** Level 1 errors are about whether the paper exists correctly. Level 2 errors are about whether the citation actually supports the claim — a more subtle and arguably more impactful problem.

The inferential overreach pattern (4/5 PARTIAL cases) suggests this is the dominant Level 2 error mode: authors cite real papers with real findings, but draw design conclusions that go beyond what the source explicitly states.

---

## Limitations

1. **N=5 is small** — cannot generalize error rates
2. **Single verifier** — no inter-rater reliability for Level 2 judgments
3. **LLM circularity** — Claude verifying LLM-assisted citations
4. **No Level 3** — cross-verification (do multiple sources agree?) not tested
5. **Selection bias** — papers were chosen because they had open semantic questions, not randomly sampled
