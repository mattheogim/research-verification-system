# Research Verification Manual v0.4 (final merged)

## Subtitle
A provenance-first, uncertainty-aware operating manual for paper discovery, counterevidence search, citation verification, equation handling, and claim-level auditing.

## Canonical version note
This file is the current **single source of truth** for the manual.
It supersedes earlier drafts (`v0.2`, `v0.2_complete`, `v0.3`, `v0.3.1 patched`, and exploratory `v0.4 draft`) by combining:
- the cleaner system-design spine,
- exact evidence and counterevidence tables,
- case-study grounding,
- concrete failure examples,
- and stronger governance / boundary statements.

This cleanup patch additionally fixes subsection numbering, removes stray internal-reference artifacts, merges abstract and concrete failure modes, and records the confirmed Baethge & Jergas evidence note.

---

# 0. Executive Summary

This project does **not** aim to make LLM outputs inherently trustworthy.

Its goal is to build a research workflow where:
- papers can be discovered without blindly trusting LLM outputs,
- citations can be checked for existence and metadata consistency,
- claims can be traced back to source spans, pages, and artifacts,
- contradictions can be evaluated at the **claim level**, not just the paper level,
- equations can be extracted when possible and flagged when uncertain,
- and every important step preserves uncertainty instead of hiding it.

The project therefore moves away from:
- “hallucination-free AI,”
- “hardcode everything,”
- and “human-in-the-loop solves it.”

It moves toward:
- **provenance-first design**,
- **layered trust**,
- **claim-level verification**,
- **version governance**,
- and **anti-overreliance review design**.

One-sentence summary:

> We are not trying to make scientific AI automatically trustworthy; we are building a system where research claims remain checkable, traceable, version-aware, and revisable even when every component can fail.

---

## 0.5 Case Study — Why this manual exists

A concrete motivating case already happened during this project.

An LLM-generated table of roughly 16 papers/sources about citation verification, PRISMA-style structure, automation bias, and research process risk was manually checked. The outcome was approximately:

- **11 confirmed** as substantially real/correct,
- **3 partially wrong** or weakly attributed,
- **2 clearly wrong** due to conflation or failed verification.

Representative error types included:

1. **Author/work conflation**  
   A "Storey + Ernst" entry merged two different works into one synthetic citation.

2. **Unverified numeric attribution**  
   A snowballing-related claim ("47 vs 38") could not be tied to the claimed author/year.

3. **Prototype overstretch**  
   Early-stage preprints were being used rhetorically as if they were settled standards.

This matters because it shows the exact failure mode this manual is designed to handle:

- not total nonsense,
- but **plausible-looking, partially grounded, confidence-inducing errors**.

That is more dangerous than obvious fabrication.

---

# 1. Problem Statement

## 1.1 Core questions

This project is built around three different questions:

1. How do we manage paper content and equations with minimal hallucination risk?
2. How do real researchers actually validate claims and citations in practice?
3. How do we trust an LLM that is asked to “find papers” or “find counterevidence” in the first place?

These are related but distinct problems. Mixing them leads to bad architecture.

## 1.2 What we are trying to solve

We are trying to build a workflow that can:
- discover candidate papers,
- verify whether cited papers actually exist,
- resolve paper manifestations and versions,
- map claims to evidence spans,
- classify support / partial support / contradiction / uncertainty,
- record structured verified notes,
- and surface where human review is truly needed.

## 1.3 What we are **not** trying to solve

We are **not** trying to:
- create a universal scientific truth engine,
- eliminate human reading,
- treat metadata checks as proof of semantic support,
- guarantee perfect equation extraction from arbitrary PDFs,
- or claim that grounded citations automatically equal verified claims.

---



## 1.4 Intended audience

This manual is primarily written for:
- individual researchers who are building or using AI-assisted literature workflows,
- small research teams or labs that want a repeatable verification process,
- tool builders designing citation/claim auditing pipelines,
- and advanced reviewers who want an explicit workflow for checking claims and counterevidence.

It is **not** primarily optimized for:
- fully manual traditional systematic-review teams with no automation component,
- journal policy language,
- or end-user-facing product copy.

This matters because review UX, governance, and acceptable workload depend on who the workflow is for.

# 2. Core Principles

## 2.1 Provenance-first

Every meaningful output should be tied back to a concrete artifact whenever possible:
- DOI / arXiv ID / PMID,
- PDF page,
- paragraph span,
- bounding box,
- equation crop,
- table crop,
- source TeX,
- manifestation / version metadata.

## 2.2 Uncertainty-aware

The system should preserve uncertainty instead of flattening it.

Examples:
- candidate clusters instead of forced single matches,
- support / partial / refute / uncertain instead of binary truth,
- parser disagreement instead of silent normalization,
- human override logs instead of invisible edits.

## 2.3 Layered trust

Not all evidence and not all operations deserve the same trust.

- Level 0: candidate generation
- Level 1: registry / metadata verification
- Level 2: source reading and evidence capture
- Level 3: cross-verification and contradiction handling

## 2.4 Human review is fallible

Humans are not perfect final judges.
They can overtrust AI framing, miss subtle mismatches, or rubber-stamp under workload.
Human review must therefore be designed as a subsystem, not assumed as a safety blanket.

## 2.5 Reader ≠ Auditor

A literature QA system and a verification system are not the same.

A strong **reader** can:
- search,
- gather evidence,
- summarize,
- answer with citations.

A strong **auditor** must additionally:
- verify manifestations and versions,
- inspect claim-support alignment,
- detect fake contradictions,
- track parser uncertainty,
- and govern corrections, retractions, and overrides.

---

# 3. Trust Layers

## 3.1 Level 0 — Candidate generation

Purpose:
- generate candidate papers,
- propose candidate counterevidence,
- suggest candidate claims,
- propose follow-up search directions.

Typical tools:
- LLM with web search,
- LLM over notes,
- brainstorming over seed papers.

Trust level:
- **lowest**.

Interpretation rule:
- this layer produces **suggestions**, not verified facts.

## 3.2 Level 1 — Registry / metadata verification

Purpose:
- verify paper existence,
- resolve identifiers,
- cluster manifestations,
- check metadata consistency.

Typical tools:
- Semantic Scholar,
- Crossref,
- arXiv,
- PubMed / PMC,
- local catalog scripts.

What this layer can do well:
- remove fake papers,
- catch missing identifiers,
- catch obvious metadata conflicts.

What it **cannot** do:
- prove that a specific claim is supported by a paper.

## 3.3 Level 2 — Source reading and evidence capture

Purpose:
- capture source spans,
- store page references,
- preserve literal evidence,
- save equation candidates and parser traces,
- write verified notes.

Typical artifacts:
- PDF,
- source TeX,
- XML / JATS,
- literal section text,
- visual crops.

Trust level:
- **high**, but still bounded by parser and reading errors.

## 3.4 Level 3 — Cross-verification

Purpose:
- identify strongest support,
- identify strongest contradiction or qualifier,
- classify conflict type,
- surface hidden assumptions,
- and filter fake contradictions.

Trust level:
- **highest available**, but not absolute.

---

# 4. Three-Tier Technical View

One of the biggest conceptual corrections from this project is that **“hardcoded vs LLM” is the wrong binary**.

A better technical view is:

## 4.1 Tier 1 — Deterministic registry / exact-ID operations
Examples:
- DOI checks,
- arXiv ID resolution,
- PubMed lookups,
- exact metadata comparisons.

## 4.2 Tier 2 — Specialized tools / narrow ML
Examples:
- GROBID,
- Nougat,
- Docling,
- Mathpix,
- layout analysis,
- heading classification,
- equation extraction.

These are neither pure rules nor open-ended LLM reasoning.
They are a distinct middle tier and must be treated explicitly.

## 4.3 Tier 3 — Open-ended LLM reasoning
Examples:
- query reformulation,
- claim normalization,
- support classification,
- contradiction explanation,
- uncertainty summaries.

The architecture gets much more realistic once this middle specialized-tools tier is explicit.

---

# 5. Reader vs Auditor

## 5.1 The role of `paper-qa`

`paper-qa` should be treated as a **strong reader/search baseline**.
It is useful for:
- ingest,
- indexing,
- metadata plumbing,
- grounded citation responses,
- agentic retrieval.

## 5.2 What can be reused from `paper-qa`

- document ingest flow,
- local indexing and search,
- retrieval patterns,
- citation-aware answer formatting,
- operational habits from docs/tests/examples.

## 5.3 What `paper-qa` should **not** be trusted to solve by itself

Not sufficient for:
- claim-level forensic verification,
- section provenance truth,
- equation truth,
- anti-overreliance review design,
- manifestation governance,
- attack-grade contradiction analysis.

## 5.4 Boundary statement

This is the strongest boundary version and should remain explicit:

- `paper-qa` should be **used** but not **trusted as final truth**.
- LaTeX conversion should be **used** but not **stored as truth by default**.
- Human review should be **used** but is **not a safety guarantee without blind / anti-overreliance design**.

---

# 6. Unit of Verification

> **The unit of verification is the claim, not the paper.**

Papers are containers.
Claims are what get supported, contradicted, overclaimed, distorted, or mis-scoped.

Without claim-level canonicalization, many “contradictions” are fake.
They may actually be:
- scope mismatch,
- metric mismatch,
- dataset mismatch,
- time-period mismatch,
- different definitions,
- or methodology mismatch.

## 6.1 Canonical claim schema

```json
{
  "claim_id": "C-001",
  "subject": "",
  "outcome": "",
  "metric": "",
  "dataset_or_population": "",
  "time_period": "",
  "definition_or_threshold": "",
  "claim_text_literal": "",
  "claim_text_normalized": "",
  "current_status": "candidate",
  "current_confidence": "low"
}
```

---

# 7. Evidence Model

## 7.1 Evidence bundle schema

```json
{
  "evidence_bundle_id": "E-001",
  "claim_id": "C-001",
  "source_paper_id": "P-014",
  "artifact_type": "pdf",
  "page_numbers": [4, 5],
  "spans": [
    {
      "page": 4,
      "literal_text": "",
      "bbox": [0, 0, 0, 0]
    }
  ],
  "equation_candidates": [],
  "tables_used": [],
  "figures_used": [],
  "parser_confidence": 0.0,
  "human_verified": false
}
```

## 7.2 Literal vs normalized fields

Every important extracted item should preserve both:
- **literal** = exactly what the source says,
- **normalized** = a model-friendly abstraction.

Examples:
- `heading_literal = "2.1 Model Architecture"`
- `heading_normalized = "METHODS"`

- `claim_text_literal = "The model achieved 91.7% on the PLOS set."`
- `claim_text_normalized = "The system reports ~92% accuracy on a specific dataset."`

This lets the system be useful **without letting normalization overwrite provenance**.

---

# 8. Verification Action Layer

## 8.1 `fetch_candidate_paper`

Purpose:
- verify that a candidate paper exists,
- resolve identifiers,
- create a candidate manifestation cluster.

Input:
- raw citation string,
- title,
- DOI,
- arXiv ID,
- author string.

Output:
- candidate cluster.

Failure modes:
- false merge,
- false split,
- noisy metadata,
- stale registry data.

## 8.2 `refresh_metadata_and_version`

Purpose:
- refresh preprint / conference / journal / corrected / retracted status.

Failure modes:
- incomplete links between versions,
- inconsistent registries,
- stale correction records.

## 8.3 `reread_source_span`

Purpose:
- reread a narrow evidence bundle,
- not the whole paper.

Input:
- page,
- bbox,
- literal span,
- paper ID.

Failure modes:
- bbox misalignment,
- parser corruption,
- ambiguous literal text.

## 8.4 `extract_equation_as_latex`

Purpose:
- create a structured equation candidate when math matters.

Input:
- source TeX or PDF region.

Output:
- LaTeX candidate + parser metadata.

Trust rule:
- higher if source TeX,
- lower if OCR / PDF-derived.

Failure modes:
- superscript/subscript confusion,
- symbol corruption,
- missing delimiters,
- parser disagreement.

Important rule:
- **do not store extracted LaTeX as truth by default**.

## 8.5 `fallback_to_visual_crop`

Purpose:
- expose parser failure instead of hiding it.

Output:
- crop,
- bbox,
- parser outputs,
- human review flag.

---

# 9. Algorithms

## 9.1 Retrieval-centered algorithms

### A. Seeded graph expansion
Purpose:
- expand from supportive and opposing seed papers.

Use when:
- you already have a few reliable seeds.

Main risk:
- graph echo chambers.

### B. Snowballing / citation chasing
Purpose:
- recover papers missed by keyword search.

Use when:
- recall matters.

Main risk:
- overfollowing one school or benchmark lineage.

### C. Active learning screening
Purpose:
- reduce screening workload by prioritizing likely-relevant papers.

Use when:
- the candidate pool is large.

Main risk:
- a weak stopping rule can hide relevant papers.

## 9.2 Verification-centered algorithms

### D. Claim extraction
Purpose:
- turn vague paper-level discussion into verifiable claim units.

### E. Evidence retrieval
Purpose:
- retrieve candidate spans that might support or challenge a claim.

### F. Support / partial / refute / uncertain classification
Purpose:
- classify claim-evidence alignment without forcing false certainty.

### G. Contradiction / context analysis
Purpose:
- distinguish real contradictions from fake contradictions caused by context mismatch.

### H. Independence clustering
Purpose:
- prevent one research line from being counted as multiple independent supports.

### I. Evidence quality scoring
Purpose:
- choose strongest support and strongest contradiction using explicit rules.

## 9.3 If forced to choose one retrieval-centered strategy

Choose a **SYMBALS-like combination**:
- seed recommendation,
- snowballing,
- active learning screening.

## 9.4 If forced to choose one contradiction-centered strategy

Choose:
- claim verification,
- contradiction typing,
- context-aware conflict analysis.

This separation matters.
Retrieval efficiency and contradiction validity are different problems.

---

# 10. Conflict Taxonomy

Each support/contradiction evaluation should classify conflict as one of:

- `direct_contradiction`
- `scope_mismatch`
- `metric_mismatch`
- `dataset_mismatch`
- `time_period_mismatch`
- `different_definition`
- `methodological_quality_mismatch`
- `annotation_or_label_mismatch`
- `non_independent_evidence_issue`
- `insufficient_information`

---

# 11. Evidence Scoring

The document should never say “strongest support” or “strongest contradiction” without a rule.

## 11.1 Suggested scoring dimensions

- `directness_to_claim`
- `independence`
- `study_type_weight`
- `replication_or_benchmark_bonus`
- `recency`
- `methodological_quality`
- `metric_alignment`
- `dataset_alignment`
- `definition_alignment`
- `time_alignment`
- `limitation_penalty`

## 11.2 Important note on weights

Any numerical weighting scheme in this document is a **heuristic draft only**.

It is **not** evidence-based yet and should **not** be treated as validated.
Weights must be calibrated by:
- domain,
- task,
- error cost,
- and validation corpus.

If calibration is absent, use scoring dimensions **without fixed weights**.

## 11.3 Optional illustrative formula

```text
evidence_score =
0.25 * directness_to_claim +
0.20 * independence +
0.15 * study_type_weight +
0.10 * replication_or_benchmark_bonus +
0.10 * methodological_quality +
0.10 * metric_alignment +
0.05 * dataset_alignment +
0.03 * definition_alignment +
0.02 * time_alignment
```

This is an **illustrative placeholder**, not a validated weighting scheme.

“Strongest” means:
- most directly relevant,
- sufficiently independent,
- methodologically credible,
- and aligned to the canonical claim.

It does **not** mean “most famous.”

# 12. Evidence Base

## 12.0 Evidence mapping rule

Every named source in this section must include:

- exact citation or persistent identifier,
- role tag,
- exact architecture claim supported,
- limitation,
- provenance quality (peer-reviewed / preprint / official doc / vendor doc).

## 12.1 Operational norms

| Source | Exact citation | Role tag | Supports which design claim | Limitation |
|---|---|---|---|---|
| PRISMA 2020 | Page MJ, McKenzie JE, Bossuyt PM, et al. *The PRISMA 2020 statement: an updated guideline for reporting systematic reviews*. **BMJ**. 2021;372:n71. DOI: 10.1136/bmj.n71 | `operational_norm` | Structured review/reporting workflows can be decomposed into explicit items and made machine-auditable | Reporting guidance, not claim-level citation verification |
| Cochrane Handbook Chapter 5 | Cochrane Training. *Chapter 5: Collecting data*. Official handbook chapter | `operational_norm` | Studies-not-reports mindset, structured extraction, independent extraction, multi-report handling | Handbook guidance, not an evaluated AI architecture |
| PRISMA-trAIce | Holst D, Moenck K, Koch J, Schmedemann O, Schüppstuhl T. *Transparent Reporting of AI in Systematic Literature Reviews: Development of the PRISMA-trAIce Checklist*. **JMIR AI**. 2025;4:e80247. DOI: 10.2196/80247 | `operational_norm`, `speculative_adoption` | AI-assisted evidence synthesis should disclose AI use, human-AI interaction, and evaluation | Foundational proposal, not yet a widely adopted formal standard |

## 12.2 Human failure evidence

| Source | Exact citation | Role tag | Supports which design claim | Limitation |
|---|---|---|---|---|
| Quotation inaccuracy meta-analysis | Baethge C, Jergas H. *Systematic review and meta-analysis of quotation inaccuracy in medicine*. **Research Integrity and Peer Review**. 2025;10:13. DOI: 10.1186/s41073-025-00173-z | `human_failure_evidence` | Humans already misquote and distort sources at meaningful rates; human review cannot be assumed perfect | Confirmed peer-reviewed medical-literature study; domain is medicine, not general AI verification |

## 12.3 Prototype verification systems

| Source | Exact citation | Role tag | Supports which design claim | Limitation |
|---|---|---|---|---|
| citecheck | Lee J. *citecheck: An MCP Server for Automated Bibliographic Verification and Repair in Scholarly Manuscripts*. arXiv:2603.17339, 2026 | `prototype_system`, `speculative_preprint` | Multi-source existence/metadata verification and structured repair are feasible as a tool layer | Preprint/prototype; not peer-reviewed standard |
| SemanticCite | Haan S. *SemanticCite: Citation Verification with AI-Powered Full-Text Analysis and Evidence-Based Reasoning*. arXiv:2511.16198, 2025. DOI: 10.48550/arXiv.2511.16198 | `prototype_system`, `speculative_preprint` | Four-way support taxonomy and full-text citation verification are feasible and useful | Preprint; cross-domain generalization not fully established |
| Citation Auditing | Janse van Rensburg LJ. *AI-Powered Citation Auditing: A Zero-Assumption Protocol for Systematic Reference Verification in Academic Research*. arXiv:2511.04683, 2025. DOI: 10.48550/arXiv.2511.04683 | `prototype_system`, `speculative_preprint` | Zero-assumption reference auditing can uncover fabricated, orphan, and retracted references | Validation corpus is limited; not a universal benchmark |

## 12.4 Baseline reader systems

| Source | Exact citation | Role tag | Supports which design claim | Limitation |
|---|---|---|---|---|
| PaperQA2 announcement / docs | Rodriques S. *PaperQA2: Superhuman scientific literature search*. FutureHouse, Sep 11 2024; plus `paper-qa` README | `baseline_reader` | A strong reader/search layer can exist independently from an auditor layer | Biology-heavy evaluation and vendor-authored evidence; not claim-level forensic verification |

## 12.5 Parser limitation evidence

| Source | Exact citation | Role tag | Supports which design claim | Limitation |
|---|---|---|---|---|
| Formula parser benchmark | *Benchmarking Document Parsers on Mathematical Formula Extraction from PDFs*. arXiv:2512.09874, 2025 | `parser_limit_evidence`, `equation_extraction_limit` | Equation parsing remains brittle; extracted LaTeX should not be treated as truth by default | Benchmark evidence still depends heavily on parser setup and benchmark design |

---

# 13. Counterevidence and Qualifying Evidence

## 13.1 Human review is not inherently safe

| Source | Exact citation | Role tag | Why it matters | Design implication |
|---|---|---|---|---|
| Automation bias paper | *Automation Bias in AI-Assisted Medical Decision-Making under Time Pressure in Computational Pathology*. arXiv:2411.00998, 2024 | `automation_risk_evidence` | Experts can reverse correct judgments after seeing wrong AI output | Blind-first review, label hiding, disagreement logging |
| Microsoft literature review | Passi S, Vorvoreanu M. *Overreliance on AI: Literature Review*. Microsoft Technical Report MSR-TR-2022-12, 2022 | `automation_risk_evidence` | Human oversight is weakened when users accept incorrect outputs | Human review must be designed, not assumed |
| Microsoft mitigation framework | Passi S, Vorvoreanu M, Kikin-Gil R. *Overreliance risk identification and mitigation framework*. MSR-TR-2025-26, 2025 | `automation_risk_evidence` | Overreliance mitigation is a product/UX design problem | Review layer requires explicit UX goals and evaluation |

## 13.2 Contradiction is often fake

| Source | Exact citation | Role tag | Why it matters | Design implication |
|---|---|---|---|---|
| Contradictory claims corpus | Alamri A, Stevenson M. *A corpus of potentially contradictory research claims from cardiovascular research abstracts*. **J Biomed Semantics**. 2016;7:36. DOI: 10.1186/s13326-016-0083-z | `contradiction_analysis_evidence` | Contradictions need explicit corpora and task structure | Claim-level contradiction handling needs dedicated resources |
| Context analysis paper | Rosemblat G, Fiszman M, Shin D, Kilicoglu H. *Towards a characterization of apparent contradictions in the biomedical literature using context analysis*. **J Biomed Inform**. 2019;98:103275. DOI: 10.1016/j.jbi.2019.103275 | `contradiction_analysis_evidence` | Many apparent contradictions disappear once context is analyzed | Conflict taxonomy and context analysis are mandatory |

## 13.3 LLM citation generation is low-trust

| Source | Exact citation | Role tag | Why it matters | Design implication |
|---|---|---|---|---|
| GhostCite | Xu Z, Qiu Y, Sun L, et al. *GhostCite: A Large-Scale Analysis of Citation Validity in the Age of Large Language Models*. arXiv:2602.06718, 2026 | `automation_risk_evidence`, `speculative_preprint` | LLMs generate invalid citations at non-trivial rates and humans often fail to verify them | Level 0 must remain low-trust |

---

# 14. Human Review Design

## 14.1 Human review is not a checkbox

Bad review design creates:
- rubber-stamping,
- anchoring on model labels,
- false confidence,
- and review fatigue.

## 14.2 Required features

- risk-based triage,
- blind-first mode for high-risk items,
- disagreement logging,
- override justification,
- escalation policy.

## 14.3 Minimum review outputs

Each review should store:
- support label,
- confidence,
- conflict type,
- whether contradiction is fake,
- whether stronger opposing evidence is still missing,
- reviewer note.

---

# 15. Governance

## 15.1 Status values

Suggested statuses:
- `candidate`
- `exists_verified`
- `metadata_verified`
- `source_read`
- `claim_linked`
- `cross_verified`
- `uncertain`
- `needs_review`
- `retracted`
- `superseded`
- `archived`

## 15.2 Independence policy

Evidence should not be counted twice just because it appears in multiple reports or papers.

Cluster by:
- same study,
- same dataset family,
- same benchmark family,
- same author group,
- same lab line where appropriate.

## 15.3 Version policy

For each cluster, record:
- preprint,
- conference,
- journal,
- correction / erratum,
- retraction,
- supplementary materials,
- which version each verified claim is attached to.

## 15.4 Verified note template

```markdown
# Verified Note

## Claim ID
C-001

## Paper ID
P-014

## Manifestation Used
journal_version_v2

## Source Location
Page 5, paragraph 2

## Literal Support
"..."

## Normalized Interpretation
The source reports X under condition Y using metric Z.

## Support Label
PARTIAL_SUPPORT

## Conflict Type
scope_mismatch

## Reviewer Note
The claim generalizes beyond the dataset actually tested.

## Follow-up Needed
Find stronger opposing paper from independent group.
```


## 15.5 Local verifier boundary

If a local verification script is used, its role should be stated explicitly:

> It is a **catalog hygiene + Level 1 verifier**, not a claim-truth engine.

It may verify:
- existence,
- identifier consistency,
- metadata mismatches,
- missing verified notes,
- obvious status drift.

It does **not** by itself verify:
- semantic claim support,
- contradiction validity,
- equation truth,
- or cross-version evidential equivalence.


---

# 16. Attack Matrix

The document becomes much stronger when opposition is structured.

## 16.1 Required columns

- `claim_id`
- `current_claim_text`
- `strongest_supporting_paper`
- `strongest_opposing_or_qualifying_paper`
- `conflict_type`
- `is_fake_contradiction`
- `hidden_assumption`
- `non_independent_evidence_flag`
- `missing_stronger_opposition_flag`
- `current_verdict`

## 16.2 Example

```text
claim_id: C-014
current_claim_text: "Human review is a reliable final safety layer."
strongest_supporting_paper: review_X
strongest_opposing_or_qualifying_paper: automation_bias_pathology_2024
conflict_type: direct_contradiction
is_fake_contradiction: false
hidden_assumption: humans remain independent after seeing AI output
non_independent_evidence_flag: false
missing_stronger_opposition_flag: false
current_verdict: Human review is necessary but not inherently reliable unless review UX is explicitly designed against overreliance.
```

---

# 17. Failure Modes

The system should explicitly admit how it breaks. Each failure mode should be paired with a concrete example or a recognizable failure pattern.

## 17.1 Parser corruption
What breaks:
- extracted structure or equation text is corrupted before downstream reasoning starts.

Concrete example:
- a parser turns `x^2` into `x_2`; a symbolic checker may still accept the result as formally valid.

Why it matters:
- formal validity is not source validity.

## 17.2 Manifestation ambiguity
What breaks:
- the system confuses preprint, conference, journal, corrected, or superseded versions.

Concrete example:
- a verified claim is attached to an early preprint while a later journal version changes the wording, metric, or caveat.

Why it matters:
- evidence may be “real” but tied to the wrong manifestation.

## 17.3 False determinism
What breaks:
- clean metadata is mistaken for semantic truth.

Concrete example:
- DOI, title, and authors all resolve correctly, but the cited paper still does not support the claim being made.

Why it matters:
- Level 1 verification can be overread as claim verification.

## 17.4 Fake contradiction
What breaks:
- an apparent contradiction is actually caused by scope, metric, dataset, time-period, or definition mismatch.

Concrete example:
- two papers look opposed, but one measures a different endpoint or uses a different population.

Why it matters:
- contradiction handling must be claim-centered and context-aware.

## 17.5 Human overreliance
What breaks:
- reviewers trust model framing, labels, or confidence too quickly.

Concrete example:
- a reviewer sees a pre-filled support label and anchors on it instead of independently checking the source span.

Why it matters:
- human review can silently become rubber-stamping.

## 17.6 Workflow theater
What breaks:
- the system appears rigorous because it has many boxes, labels, and checks, but little real source reading happens.

Concrete example:
- a claim passes through multiple metadata and UI stages without anyone confirming the exact supporting span.

Why it matters:
- procedural complexity can simulate rigor without producing it.

## 17.7 Evidence inflation
What breaks:
- multiple reports from the same study or research line are counted as independent support.

Concrete example:
- one benchmark family produces several papers and all of them are treated as independent evidence.

Why it matters:
- support can look stronger than it really is.

## 17.8 Schema rigidity
What breaks:
- the schema is frozen too early and cannot represent odd real-world documents, equations, supplements, or multimodal evidence.

Concrete example:
- a paper’s key evidence appears in a figure caption or supplement, but the schema assumes paragraph-based evidence only.

Why it matters:
- rigid structure can erase the very evidence the workflow is meant to preserve.

## 17.9 Early UI/UX failure
What breaks:
- review UX design pushes reviewers toward fast approval rather than careful judgment.

Concrete example:
- high-risk items are shown with pre-exposed model conclusions and no blind-first mode.

Why it matters:
- review design can manufacture overconfidence.

## 17.10 Missing ground-truth datasets
What breaks:
- calibration and evaluation are attempted without stable gold data.

Concrete example:
- support labels are tuned against ad hoc examples with no consistent benchmark.

Why it matters:
- the system cannot know whether it is improving or only sounding more systematic.


# 18. Maturity Map

## Mature enough to operationalize now
- registry existence checks,
- metadata gathering,
- catalog hygiene,
- basic grounded retrieval,
- verified notes,
- simple snowballing,
- active screening workflows.

## Plausible but not fully validated
- claim-support classification,
- contradiction typing across domains,
- manifestation clustering at scale,
- reviewer triage design.

## Still brittle / speculative
- equation truth from PDF parsing,
- universal section normalization,
- robust anti-overreliance UX,
- near-deterministic cross-domain claim auditing,
- stable shared schema across tools.

---

# 19. Open Questions and Second-Order Risks

## 19.1 Still-open questions

- What is the cost of a false negative vs a false positive?
- What is the legal limit of local caching and artifact storage?
- Where will ground-truth datasets come from?
- What empirical studies show how humans really verify claims in practice?
- Can a stable cross-tool schema emerge for sections, equations, tables, and evidence spans?
- How much review workload becomes bureaucratic overhead?
- Who maintains the living system after year 2?
- What incentive does a researcher have to correct or update the database?

## 19.2 Second-order risks

- Scale 10x: parser and reviewer bottlenecks may dominate.
- Scale 10x: storage, diffing, artifact versioning, and review queues may become the real bottleneck.
- Add more checks: workflow theater may replace real reading.
- Add stronger automation: overreliance risk may rise.
- Freeze schema too early: rigidity may block real-world document diversity.

---

# 20. Next Search Batches

These are the most important next literature bundles to search.

## A. Manifestation matching
Why it matters:
- without this, Level 1 stays noisier than it looks.

## B. Cross-domain claim alignment datasets
Why it matters:
- current evidence is too concentrated in specific domains.

## C. Anti-overreliance UX / blind review
Why it matters:
- human review can fail even when the architecture is otherwise sound.

## D. Real-world equation extraction benchmarks
Why it matters:
- synthetic PDF results do not guarantee field robustness.

## E. Copyright / licensing / caching policy
Why it matters:
- a system that cannot legally store or re-read artifacts will fail operationally.

## F. Retraction / correction / errata governance
Why it matters:
- a paper can exist and still be a bad or superseded source.

---

# 21. Prompt Pack for Other AIs

## Prompt 1 — Architecture audit

```text
I am designing a provenance-first paper verification system.

Please do not summarize my idea politely.
I want you to audit it.

System goal:
- Not hallucination-free generation
- But auditable outputs tied to source spans, page numbers, and artifacts

Current stack:
1. Identity/registry lookup (DOI, arXiv, PMID, Crossref, Semantic Scholar)
2. Parsing layer (GROBID, Nougat, Docling, Mathpix, source TeX when available)
3. Structure layer (sections, equations, tables, figures, literal vs normalized)
4. Claim-evidence alignment layer (supported / partial / unsupported / uncertain)
5. Human review layer
6. Version/retraction governance

Tasks:
1. Find primary-source papers or official docs that support this architecture.
2. Find primary-source papers that attack it.
3. Identify what parts are actually mature and what parts are still speculative.
4. Focus especially on:
   - manifestation/version matching
   - equation extraction reliability
   - human overreliance / automation bias
   - claim-citation alignment datasets
   - retraction/correction workflows
5. Use citations for every factual claim.
6. Distinguish peer-reviewed papers, preprints, official docs, vendor docs, and blog posts.

Output format:
- What is solid
- What is weak
- What is still missing
- What would break first in a real implementation
- 10 papers/docs I should read next
```

## Prompt 2 — Evidence for / against

```text
Search for papers and official documentation relevant to this question:

“How can we verify academic claims, citations, sections, and equations with minimal hallucination risk, while avoiding false confidence from human-in-the-loop review?”

I need two lists:
A. Evidence FOR a provenance-first layered verification system
B. Evidence AGAINST it / counterevidence / failure modes

Please prioritize:
- official docs
- peer-reviewed papers
- then recent arXiv preprints only if clearly labeled as preprints

Please search specifically for:
- systematic review data extraction norms
- quotation/citation error rates in human papers
- automation bias / overreliance in AI-assisted review
- PDF/equation parsing benchmarks
- citation verification systems
- manifestation-aware citation matching
- retraction/correction/version handling

For each item, return:
- citation
- what exact claim it supports
- why it matters to the architecture
- limitations
```

## Prompt 3 — `paper-qa` split review

```text
I am considering using Future House’s paper-qa / PaperQA2 as a reader/search baseline,
and building a separate verification layer on top.

Please evaluate whether this split makes sense:

reader baseline:
- ingest PDFs
- fetch metadata
- index text
- grounded citation answers
- agentic retrieval

verification layer on top:
- fetch_candidate_paper
- refresh_metadata_and_version
- reread_source_span
- extract_equation_as_latex
- fallback_to_visual_crop
- claim-support classification
- blind human review for high-risk items
- disagreement logging

Tasks:
1. Check what PaperQA2 actually supports in public docs and papers.
2. Identify which parts I can realistically reuse.
3. Identify what I must build myself.
4. Tell me where this plan is overambitious.
5. Suggest a smaller MVP that still produces real value.

Use primary sources and cite every factual claim.
Do not assume PaperQA2 already solves claim-level forensic verification unless the sources explicitly show that.
```

---

# 22. 5-Year-Old Explanation

There are many books.
A robot says,
“this book says this thing.”

But:
- the robot can be wrong,
- the machine reading the book can be wrong,
- and even the person checking can be wrong.

So we do this:
1. let the robot bring candidate books,
2. check whether the books are real,
3. open the real page,
4. check the important sentence,
5. and if it matters a lot, compare with another book too.

So the goal is **not**:
“trust the robot.”

The goal is:
**make it easy to go back and check what the robot said.**

---



# 22.5 Rough effort / cost framing

This manual is still weak on exact cost estimates, so the following should be treated as planning placeholders rather than commitments.

At minimum, a small MVP loop usually requires:
- manual source reading time for each high-value claim,
- registry/API calls for manifestation checking,
- storage for PDFs / crops / verified notes,
- and reviewer time for uncertain or high-risk items.

The exact cost will depend on:
- corpus size,
- average paper length,
- how often equations matter,
- whether source TeX is available,
- and how many items escalate to human review.

A future version should replace this section with measured numbers from a pilot run.

# 23. MVP

## Build now
- Level 0 candidate capture
- Level 1 registry verification
- claim schema
- verified note template
- `paper-qa` reader baseline
- `reread_source_span`
- simple attack matrix

## Defer
- equation truth engine
- heavy parser ensembles
- universal schema commitments
- high-complexity calibration systems

## Smallest useful loop
1. LLM proposes paper candidates
2. registry/API verifies existence
3. source span is manually captured
4. claim gets a support label
5. one strongest qualifier is attached
6. result is stored as a verified note

That loop already has real value.

---

# 24. Final Position

This project is best described as:

> A provenance-first, uncertainty-aware research verification workflow that treats LLMs, parsers, registries, and humans as fallible components and designs around that fallibility.

It is not:
- a pure RAG system,
- a pure parser project,
- a pure citation checker,
- or a pure human review system.

It is a layered workflow that combines:
- paper discovery,
- claim extraction,
- citation verification,
- contradiction handling,
- version governance,
- and review design.

