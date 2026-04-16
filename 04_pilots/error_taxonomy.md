# Error Taxonomy — Formalized 2-Axis Classification

_Date: 2026-04-15_
_Applies to: Dataset A (16 sources) + Dataset B (37 papers)_

---

## Axis 1: Metadata Correctness

Each error type has an **operational definition** (fixed, not interpretive):

| Code | Name | Operational Definition | Severity |
|---|---|---|---|
| `fabricated_reference` | Fabricated reference | No scholarly record exists matching any combination of title + authors + identifiers. The paper was invented. | Critical |
| `author_mismatch` | Author mismatch | The catalog attributes the paper to author(s) who do not appear in the actual author list of the verified record. Not a spelling variation — a different person entirely. | High |
| `title_mismatch` | Title mismatch | The catalog title differs from the verified record in a way that could refer to a different paper (not just abbreviation or minor wording). | Medium |
| `venue_inflation` | Venue inflation | The citation reports a stronger venue or status than justified by the verified record. Example: workshop paper cited as main conference paper. | Medium |
| `venue_drift` | Venue drift | The paper is real, but the catalog was not updated after a later publication state change. Example: arXiv preprint that was later published in a journal, but catalog still says "arXiv". | Low |
| `identifier_mismatch` | Identifier mismatch | DOI, arXiv ID, year, volume, or page numbers are incorrect in the catalog. | Low |
| `exact_match` | No error | All verifiable metadata fields match the authoritative record. | None |
| `not_verified` | Not verified | Cannot access authoritative record (paywall, no identifier, web article). | N/A |

### Decision rules for edge cases

- **Abbreviated vs wrong title:** "Improving Factuality... through Multiagent Debate" vs "Improving Factuality and Reasoning in Language Models through Multiagent Debate" → `exact_match` (abbreviation, same paper)
- **"Lost in the Haystack" vs "Hidden in the Haystack":** → `title_mismatch` (different word, could confuse with "Lost in the Middle")
- **"SwarmBench" vs "Benchmarking LLMs' Swarm intelligence":** → `title_mismatch` (informal name, not actual title)
- **venue not listed vs venue wrong:** "arXiv" when actually "TMLR" → `venue_drift` (paper moved from preprint to journal). "ICML 2025" when actually "ICML Workshop 2025" → `venue_inflation` (inflated status)

---

## Axis 2: Claim Support Correctness (Level 2 — measured separately)

| Code | Name | Operational Definition |
|---|---|---|
| `full_support` | Full support | The cited section of the paper contains evidence that directly supports the specific claim made in the citing document. |
| `partial_support` | Partial support | The paper addresses the topic but the specific claim overstates, narrows, or extends what the paper actually shows. |
| `no_support` | No support (mis-citation) | The paper does not address the claim at all, or addresses a different aspect. The citation is misplaced. |
| `contradicts` | Contradicts | The paper's findings directly contradict the claim being made. The citation is counter-evidence being cited as support. |
| `not_assessed` | Not assessed | Level 2 was not performed on this paper. |

---

## Dataset B (37 papers) — Reclassified

| ID | Old Verdict | Old Error_Type | New Axis 1 Code | Severity | Notes |
|---|---|---|---|---|---|
| A1 | EXACT | - | exact_match | None | |
| A2 | EXACT | - | exact_match | None | |
| A3 | PARTIAL | venue_missing | venue_drift | Low | arXiv → JRAR (published after cataloging) |
| A4 | EXACT | - | exact_match | None | |
| B1 | EXACT | - | exact_match | None | |
| B2 | PARTIAL | venue_missing | venue_drift | Low | arXiv → TMLR |
| C1 | EXACT | - | exact_match | None | |
| **C2** | **FAIL** | **author_wrong** | **author_mismatch** | **High** | Catalog: "Li et al." → Actual: Salemi et al. |
| D1 | EXACT | - | exact_match | None | |
| D2 | EXACT | - | exact_match | None | |
| D3 | EXACT | - | exact_match | None | |
| E1 | EXACT | - | exact_match | None | |
| E2 | EXACT | - | exact_match | None | |
| E3 | EXACT | - | exact_match | None | |
| E4 | EXACT | - | exact_match | None | |
| E5 | EXACT | - | exact_match | None | |
| **E6** | **PARTIAL** | **venue_inflated** | **venue_inflation** | **Medium** | ICML Workshop → cited as ICML main |
| **E7** | **FAIL** | **author_wrong** | **author_mismatch** | **High** | Catalog: "Zhao et al." → Actual: Gao et al. |
| E8 | EXACT | - | exact_match | None | |
| E9 | EXACT | - | exact_match | None | |
| E10 | EXACT | - | exact_match | None | |
| F1 | EXACT | - | exact_match | None | |
| G1 | EXACT | - | exact_match | None | |
| G2 | EXACT | - | exact_match | None | |
| H1 | EXACT | - | exact_match | None | |
| **H2** | **PARTIAL** | **title_wrong** | **title_mismatch** | **Medium** | "Lost" → "Hidden" |
| I1 | EXACT | - | exact_match | None | |
| J1 | EXACT | - | exact_match | None | |
| J2 | PARTIAL | venue_missing | venue_drift | Low | arXiv → Adv. Eng. Informatics |
| J3 | PARTIAL | venue_missing | venue_drift | Low | arXiv → ICAART 2025 |
| J4 | - | - | not_verified | N/A | paywall |
| J5 | - | - | not_verified | N/A | paywall |
| J6 | EXACT | - | exact_match | None | |
| J7 | - | - | not_verified | N/A | paywall |
| J8 | - | - | not_verified | N/A | web article |
| J9 | EXACT | - | exact_match | None | |
| **K1a** | **PARTIAL** | **title_informal** | **title_mismatch** | **Medium** | "SwarmBench" ≠ actual title |
| K1b | EXACT | - | exact_match | None | |
| K4 | EXACT | - | exact_match | None | |
| K5 | EXACT | - | exact_match | None | |
| K6 | EXACT | - | exact_match | None | |

---

## Summary by Severity (Dataset B, N=37)

| Severity | Count | % | Papers |
|---|---|---|---|
| **Critical** (fabricated) | 0 | 0% | - |
| **High** (author mismatch) | 2 | 5.4% | C2, E7 |
| **Medium** (title/venue inflation) | 3 | 8.1% | E6, H2, K1a |
| **Low** (venue drift) | 4 | 10.8% | A3, B2, J2, J3 |
| **None** (exact match) | 24 | 64.9% | (24 papers) |
| **N/A** (not verified) | 4 | 10.8% | J4, J5, J7, J8 |

### Headline reframing

- Old: "24% error rate" (9/37)
- New: "5.4% high-severity + 8.1% medium-severity metadata errors; additionally 10.8% venue drift (low severity, not strictly errors)"
- Even more precise: **"13.5% actionable errors" (high + medium)**, 10.8% informational (venue drift)

---

## Comparison with CiteAudit Taxonomy

| Our Category | CiteAudit Equivalent | Overlap |
|---|---|---|
| fabricated_reference | Title-level / Author-level hallucination | Direct overlap (but we found 0 cases) |
| author_mismatch | Author-level: addition/deletion/perturbation | Partial — CiteAudit includes spelling variants, we only count different people |
| title_mismatch | Title-level: keyword substitution | Partial — CiteAudit focuses on fabricated titles, we include confusion |
| venue_inflation | Metadata-level: venue mismatch | **Not distinguished in CiteAudit** — they don't separate drift from inflation |
| venue_drift | Metadata-level: venue mismatch | **Not distinguished in CiteAudit** |
| identifier_mismatch | Metadata-level: DOI/year fabrication | Direct overlap |
| full/partial/no_support | Not covered | **Our unique contribution** (Axis 2) |
| contradicts | Not covered | **Our unique contribution** (Axis 2) |
