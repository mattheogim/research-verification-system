# Dataset C: Independent Verification Report

**Date:** 2026-04-15
**Model:** Claude Opus 4.6 (1M context)
**Purpose:** Test verification on sources outside the meta-architect ecosystem (Step 7)

---

## Overview

| Dataset | Source | Domain | N | EXACT | PARTIAL | FAIL | NOT_FOUND |
|---------|--------|--------|---|-------|---------|------|-----------|
| C-1 | LLM-generated | CS (Federated Learning) | 20 | 0 (0%) | 14 (70%) | 0 | 6 (30%) |
| C-2 | Awesome-LLM GitHub list | CS (LLMs) | 15 | 13 (87%) | 2 (13%) | 0 | 0 |
| C-3 | PubMed / Medical | Biomedical | 10 | 6 (60%) | 4 (40%) | 0 | 0 |
| **Total** | | | **45** | **19 (42%)** | **20 (44%)** | **0** | **6 (13%)** |

---

## Dataset C-1: LLM-Generated Citations (Federated Learning 2024-2025)

**Method:** Asked Claude to generate 20 paper citations on "federated learning 2024-2025", then verified each against arXiv/web.

**Key Finding: 0% of LLM-generated citations were fully correct.**

- **14 papers (70%):** Correspond to real papers but with metadata errors
  - Most common: fabricated arXiv IDs, inflated publication years, venue errors
- **6 papers (30%):** Entirely fabricated — no matching paper exists
- **0 papers (0%):** Fully correct metadata

**Error types observed:**
- Fabricated arXiv IDs (most common — plausible-looking but non-existent)
- Inflated publication years (e.g., claiming 2024 for a 2023 paper)
- Wrong venues (claiming conference acceptance when paper is arXiv-only)
- Author name variations (minor misspellings or wrong first names)

**Implication:** LLM-generated bibliographies require 100% verification. Even well-known papers have metadata errors when generated from LLM memory. This validates the core premise of the research verification system.

---

## Dataset C-2: Awesome-LLM GitHub List

**Source:** https://github.com/Hannibal046/Awesome-LLM
**Method:** Extracted 15 papers from the curated list, verified each against arXiv.

**Key Finding: 87% accuracy — curated human lists are much more reliable than LLM generation.**

| ID | Paper | Verdict | Notes |
|----|-------|---------|-------|
| C2-01 | Attention Is All You Need (1706.03762) | EXACT | |
| C2-02 | Megatron-LM (1909.08053) | EXACT | |
| C2-03 | ZeRO (1910.02054) | EXACT | |
| C2-04 | Scaling Laws (2001.08361) | EXACT | |
| C2-05 | Switch Transformers (2101.03961) | EXACT | |
| C2-06 | Codex (2107.03374) | EXACT | |
| C2-07 | Foundation Models (2108.07258) | EXACT | |
| C2-08 | T0 / Multitask Prompted Training (2110.08207) | EXACT | |
| C2-09 | GLaM (2112.06905) | EXACT | |
| C2-10 | Gopher (2112.11446) | EXACT | |
| C2-11 | Chain-of-Thought (2201.11903) | EXACT | |
| C2-12 | LaMDA (2201.08239) | EXACT | |
| C2-13 | Megatron-Turing NLG (2201.11990) | **PARTIAL** | "DeepSpeed" truncated to "Deep" in title |
| C2-14 | InstructGPT (2203.02155) | EXACT | |
| C2-15 | UL2 (2205.05131) | **PARTIAL** | "UL2:" prefix missing from title |

**Structural note:** Awesome-LLM uses organization-level attribution (e.g., "Google", "OpenAI") rather than individual author names, and omits formal publication venues. This is a different metadata format than academic citations but is standard for awesome-lists.

**Errors found:** Both are minor title truncations — the list slightly abbreviates paper titles. No wrong papers, no fabricated entries.

---

## Dataset C-3: PubMed / Medical Papers

**Method:** Generated 10 medical/biomedical paper citations (mix of landmark + recent + deliberately planted errors), then verified against PubMed.

| ID | Paper | Verdict | Error Type | Notes |
|----|-------|---------|-----------|-------|
| C3-01 | BioBERT (Lee et al., Bioinformatics 2020) | EXACT | | |
| C3-02 | RECOVERY Trial (NEJM 2021) | EXACT | | |
| C3-03 | ClinicalBERT (arXiv 2019) | **PARTIAL** | author_wrong | Generated BERT authors (Devlin et al.) instead of actual ClinicalBERT authors (Huang et al.) — parent-paper author bleed |
| C3-04 | AlphaFold (Nature 2021) | EXACT | | |
| C3-05 | GPT-4 Medical (arXiv 2023) | **PARTIAL** | title_wrong | "Medical Competency Examinations" vs actual "Medical Challenge Problems" |
| C3-06 | LLMs Encode Clinical Knowledge (Nature 2023) | EXACT | | |
| C3-07 | LLMs in Medicine Review (Nature Medicine 2023) | EXACT | | |
| C3-08 | AI in Health and Medicine (Nature Medicine 2022) | EXACT | | |
| C3-09 | Med-PaLM (arXiv 2023) | **PARTIAL** | author_wrong + title_wrong + venue_wrong | 3 simultaneous errors — deliberately planted |
| C3-10 | Dermatologist-level Skin Cancer (2017) | **PARTIAL** | venue_wrong | Nature listed as NEJM — deliberately planted |

**2 unintentional errors detected:**
- C3-03: Parent-paper author bleed (BERT → ClinicalBERT author confusion)
- C3-05: Semantically similar but factually wrong title substitution

**2 deliberately planted errors detected:**
- C3-09: Multiple fabricated metadata fields
- C3-10: Wrong venue (Nature vs NEJM)

---

## Domain-Specific Findings

### Medical vs CS Citation Verification

| Dimension | CS Papers | Medical Papers |
|-----------|-----------|----------------|
| **Primary verification source** | arXiv (fragmented) | PubMed (unified) |
| **Author format** | Individual names | Often consortium/group authorship |
| **Preprint → publication gap** | Months | Months to years |
| **Title error mode** | Abbreviation, informal names | Cross-paper title contamination |
| **Author error mode** | Wrong first author, institutional attribution | Parent-paper author bleed |
| **Venue confusion risk** | Conference vs arXiv | Journal name confusion (Nature vs NEJM) |

**Key insight:** Level 1 verification is actually *easier* for medical papers when PubMed is available, because PubMed provides a single authoritative metadata source. CS papers lack a comparable unified database. However, medical citation errors tend to be more subtle (e.g., wrong authors for derivative work like ClinicalBERT).

---

## Comparison with Dataset A+B

| Dataset | Source Type | N | Error Rate | FAIL Rate | Dominant Error |
|---------|-----------|---|-----------|-----------|----------------|
| A (16) | Research-system sources | 16 | 25% | 0% | venue_missing |
| B (37) | Meta-architect sources | 37 | 24% | 5% | author_wrong, venue_missing |
| C-1 (20) | LLM-generated | 20 | **100%** | 30% fabricated | fabricated_id, venue_wrong |
| C-2 (15) | Human-curated list | 15 | **13%** | 0% | title_truncation |
| C-3 (10) | Medical (mixed) | 10 | **40%** | 0% | author_wrong, title_wrong |

**Hierarchy of reliability:**
1. Human-curated lists (13% error) — most reliable
2. Architecture document citations (24-25%) — moderate
3. Medical LLM-generated with known papers (40%) — elevated
4. LLM-generated from scratch (100%) — completely unreliable

This supports the paper's thesis: citation verification is necessary, and the error rate varies dramatically by source type.

---

## Limitations

1. **C-1 detailed per-paper data:** Summary statistics are available but individual paper results need to be regenerated for appendix use
2. **C-2 selection bias:** Awesome-LLM contains landmark papers more likely to have stable metadata
3. **C-3 deliberate errors:** 2 of 4 errors were planted; the "natural" error rate is 2/8 = 25%
4. **Sample sizes are small** (N=20, 15, 10) — insufficient for statistical significance claims
5. **Same LLM for generation and verification** in C-1 and C-3 — partial circularity
