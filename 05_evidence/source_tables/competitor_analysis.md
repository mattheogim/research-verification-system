# Competitor Analysis — CiteAudit vs Research Verification System

_Date: 2026-04-15_
_Source: CiteAudit (arXiv:2602.23452, Feb 2026)_

---

## CiteAudit Summary

Multi-agent verification pipeline for detecting **fabricated citations** (hallucinated references that don't exist).

**Pipeline:** 4 stages — OCR extraction → memory lookup (cosine τ=0.92) → web search (Google, top-5 full text) → Scholar verification (canonical records)

**Dataset:** 9,442 citations (6,475 real + 2,967 hallucinated), generated + real-world

**Performance:** 97.3% accuracy, 93.8% precision, 100% recall on generated; 97.2% accuracy, 82.3% precision, 100% recall on real-world

**Cost:** $0 (local Qwen3-VL-235B) vs $70/M tokens (GPTZero)

---

## Key Differentiation

| Dimension | CiteAudit | Our System |
|---|---|---|
| **Error type** | Fabricated citations (don't exist) | Metadata conflation (exist but mixed up) |
| **Product** | Detection tool (auto pipeline) | Verification methodology (staged framework) |
| **Taxonomy** | fabricated / verified (binary + subtypes) | 2-axis: metadata correctness + claim support |
| **Scale** | 9,442 citations | 53 papers (pilot), extensible |
| **Level 2 (claim support)** | Not addressed | Core differentiator — does paper support claim? |
| **Cost model** | Full pipeline every time | Staged escalation — L1 filters before L2 |
| **Downstream impact** | Not measured | Measures how errors affect design decisions |
| **Cross-system comparison** | Single system benchmarked | Two systems × two datasets, clean runs |

---

## Where CiteAudit Is Stronger

1. **Scale:** 9,442 vs 53 — not comparable
2. **Automation:** Fully automated pipeline vs manual process
3. **Dataset construction:** Controlled perturbations + real-world, chi-squared validated
4. **Performance reporting:** Full P/R/F1 across multiple models and subsets
5. **Ablation study:** Each module's contribution measured (Scholar removal → recall 100%→68.4%)

## Where We Are Stronger (our claim space)

1. **Different error regime:** Our papers all EXIST — the errors are metadata mixing, not fabrication. CiteAudit's 100% recall means nothing for our error type since the papers resolve correctly.

2. **Claim-evidence alignment (Level 2):** CiteAudit verifies "does this paper exist?" We go further: "does this paper actually support the claim it's cited for?" This is a fundamentally harder problem.

3. **Cost-based escalation:** CiteAudit runs full pipeline. We show that 80% of errors are catchable at Level 1 (3 min/paper), and only the hard cases need Level 2 (30-60 min/paper). This cost framework is our methodological contribution.

4. **Failure regime separation:** We identify WHERE baselines are sufficient vs WHERE architecture is needed. CiteAudit benchmarks ONE system; we compare multiple systems and identify their complementary strengths.

5. **Downstream impact:** We show that citation errors actually changed design decisions in a real project. CiteAudit doesn't measure practical consequences of errors.

---

## What CiteAudit DOESN'T Catch (our gap)

CiteAudit's Judge Agent uses "Strict Consistency Criterion" — exact field matching. This means:
- **venue_drift** (arXiv → journal update): CiteAudit would flag this as mismatch, but it's not an error — it's legitimate progression. Our taxonomy distinguishes drift from inflation.
- **venue_inflation** (workshop → main conference): CiteAudit can't distinguish workshop from main conference — both would match as "venue exists."
- **semantic_mis_support**: CiteAudit doesn't read the paper's content to check claim alignment.

---

## Positioning Strategy

**DO NOT claim:** "We present a citation verification system" (direct competition with CiteAudit)

**DO claim:** "We present a cost-aware staged verification framework for LLM-assisted research workflows, focusing on metadata conflation and claim-evidence alignment — error types that existing fabrication-detection tools do not address."

**Relationship to CiteAudit:** Complementary, not competitive. CiteAudit = Level 0-1 at scale (does paper exist?). Our system = Level 1-2 in depth (is the citation trustworthy for its purpose?).

---

## CiteAudit Limitations We Can Exploit

1. **No inter-annotator agreement reported** — author-team-only annotation, no Kappa. We plan human + LLM comparison.
2. **No cross-domain testing** — their dataset is CS-heavy. We test on non-CS (PubMed).
3. **No cost framework** — they report $0 inference cost but not human review time saved or escalation decisions.
4. **Fabrication ≠ real-world problem in curated catalogs** — when researchers build paper catalogs, fabrication is rare (we found 0). The real problems are subtler: wrong authors, wrong venues, claims not supported.

---

## Numbers We Must Cite

- "CiteAudit achieves 97.3% accuracy with 100% recall on fabricated citations"
- "Their benchmark contains 9,442 citations across generated and real-world sources"
- "Ablation shows Scholar Agent removal drops recall from 100% to 68.4%"
- Our counter: "In our datasets of LLM-curated research catalogs, 0% of errors were fabricated citations — 100% were metadata conflation in real papers"
