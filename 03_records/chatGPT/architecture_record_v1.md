# research_verification_record_and_qoc_v1

_Generated: 2026-04-16T01:39:54.676290+00:00_

## Purpose

This document is a **project record** and **QOC (Questions / Options / Criteria)** log for the research verification workflow project.

It preserves:
- what was discussed,
- what was decided,
- what was tested,
- why certain design directions were chosen,
- what evidence and counterevidence mattered,
- and what still remains open.

It is **not** the full operating manual.
It is the **decision-and-rationale companion** to the manual.

---

# 1. Project Snapshot

## Working project description

Build a **provenance-first, uncertainty-aware research verification workflow** for:
- paper discovery,
- counterevidence search,
- citation verification,
- equation handling,
- and claim-level auditing.

## Final framing reached so far

The goal is **not** “hallucination-free AI.”

The goal is:

> Make research claims auditable, traceable, version-aware, and revisable even when LLMs, parsers, registries, and humans can all fail.

## Core philosophical shifts

1. From **hallucination-free** → **auditable**
2. From **hardcoded vs LLM** → **3-tier architecture**
   - deterministic registry checks
   - specialized tools / narrow ML
   - open-ended LLM reasoning
3. From **human-in-the-loop is safe** → **human review must be designed**

---

# 2. Chronological Record

## Phase 1 — Problem decomposition

The original broad question was split into 3 different questions:

1. **How do we manage paper contents and equations with minimal hallucination risk?**
2. **How do real researchers actually validate claims and citations in practice?**
3. **How do we trust an LLM that is asked to “find papers” or “find counterevidence”?**

This decomposition separated:
- technical verification problems,
- human workflow problems,
- epistemic trust problems.

---

## Phase 2 — Rejected assumptions

The following assumptions were explicitly rejected.

### A. “If the LLM gets better, this problem mostly disappears.”
Rejected because:
- citation hallucination,
- source conflation,
- semantic overclaiming,
- and omission of uncertainty
remain structural issues.

### B. “If we hardcode enough, the problem mostly disappears.”
Rejected because:
- deterministic checks help with existence and metadata,
- but not with claim support,
- not with version drift,
- and not with parser corruption.

### C. “Human-in-the-loop makes it safe.”
Rejected because:
- humans can overtrust model framing,
- rubber-stamp under workload,
- and fail to detect subtle support mismatch.

### D. “If we can extract equations into LaTeX, we can verify the math.”
Rejected because:
- parser-safe does not mean source-true,
- symbolic validity does not mean provenance validity,
- and OCR/parser corruption can silently pass downstream.

---

## Phase 3 — Architecture consolidation

The project converged toward the following trust layers:

- **Level 0**: candidate generation
- **Level 1**: registry / metadata verification
- **Level 2**: source reading and evidence capture
- **Level 3**: cross-verification and contradiction handling

This trust structure became one of the main practical outputs of the discussion.

---

## Phase 4 — `paper-qa` boundary clarification

`paper-qa` / PaperQA2 was positioned as:

- a **strong reader/search baseline**
- **not** a claim-level forensic verification system
- useful for:
  - ingest
  - indexing
  - retrieval
  - grounded answer formatting
- not sufficient for:
  - claim-level support truth
  - section provenance truth
  - equation truth
  - anti-overreliance review design
  - manifestation governance

Boundary statement adopted:

- Use `paper-qa`
- Do **not** trust it as final truth

---

## Phase 5 — Algorithm layer clarification

The project identified a practical algorithm stack.

### Retrieval-centered
- seeded graph expansion
- snowballing
- active learning screening

### Verification-centered
- claim extraction
- evidence retrieval
- support / partial / refute / uncertain classification
- contradiction / context analysis
- independence clustering
- evidence quality scoring

Key insight:
- retrieval efficiency and contradiction validity are different problems.

---

## Phase 6 — Manual evolution

The manual evolved roughly like this:

- **v0.2**: stronger structure / system-design spine
- **v0.2_complete**: stronger evidence / counterevidence / prompt pack
- **v0.3 / v0.3.1**: merged structure + evidence
- **v0.4**: case study + exact evidence tables + named counterevidence + failure examples
- **v0.4.1 cleanup**: numbering cleanup, artifact removal, failure-mode integration, confirmed evidence note

---

## Phase 7 — Pilot run

A pilot run was executed using a **reconstructed 16-item test set**:
- original support/counterevidence table
- plus later gold-standard verification notes

Gold split:
- **11 exact**
- **3 partial**
- **2 error**

Main pilot finding:

> Level 1 is good at catching fake or conflated sources.  
> Level 2/3 are where semantic support, scope, overclaim, and contradiction actually get decided.

---

# 3. Main Decisions Log

## Decision 1
**Unit of verification = claim, not paper**

Reason:
- papers are containers
- claims are what get supported, contradicted, overclaimed, or mis-scoped

Consequence:
- contradiction analysis must be claim-level
- evidence bundles must attach to claims
- paper-level summaries are not enough

---

## Decision 2
**Use layered trust, not flat confidence**

Reason:
- candidate generation, metadata verification, source reading, and cross-verification are different operations
- they have different failure modes

Consequence:
- no single “verified” label is enough
- status values and phase distinctions matter

---

## Decision 3
**Reader ≠ Auditor**

Reason:
- systems that are good at literature QA are not automatically good at verification

Consequence:
- use reader baselines
- build verification as a separate layer

---

## Decision 4
**Preserve literal fields alongside normalized fields**

Reason:
- normalized abstractions are useful
- but they should never overwrite provenance

Consequence:
- every important extracted object should preserve:
  - literal
  - normalized

---

## Decision 5
**Treat extracted LaTeX as candidate evidence, not truth**

Reason:
- parser corruption can survive symbolic validation
- OCR and layout failures remain real

Consequence:
- visual fallback remains necessary

---

## Decision 6
**Human review must be designed**

Reason:
- humans are fallible
- model framing can influence decisions

Consequence:
- blind-first review
- disagreement logging
- override justification
- escalation policy

---

## Decision 7
**Evidence tables must include named sources with roles**

Reason:
- the manual should follow its own provenance-first principles

Consequence:
- exact evidence tables
- named counterevidence
- role tags
- limitations for each cited source

---

# 4. QOC (Questions / Options / Criteria)

## QOC-01 — What is the project goal?

### Question
What should the project optimize for?

### Options
- **O1**: hallucination-free AI
- **O2**: stronger hardcoded pipeline
- **O3**: provenance-first auditable workflow

### Criteria
- realism
- trustworthiness
- ability to survive parser/LLM/human failure
- operational usefulness

### Decision
**O3 selected**

### Why
O1 is unrealistic.  
O2 helps but cannot solve semantic support and version drift.  
O3 best matches the actual failure landscape.

---

## QOC-02 — What is the right architecture model?

### Question
How should the system be conceptualized?

### Options
- **O1**: hardcoded logic vs LLM
- **O2**: flat mixed pipeline
- **O3**: 3-tier architecture
  - deterministic registry
  - specialized tools / narrow ML
  - open-ended LLM reasoning

### Criteria
- conceptual clarity
- implementation realism
- parser placement realism
- trust-boundary clarity

### Decision
**O3 selected**

### Why
The middle tier was being ignored, and that made the architecture unrealistic.

---

## QOC-03 — What is the unit of verification?

### Question
Should verification happen at the paper level or claim level?

### Options
- **O1**: paper-level only
- **O2**: mixed paper/claim level
- **O3**: claim-level canonicalization

### Criteria
- contradiction quality
- support precision
- resistance to fake contradiction
- interpretability

### Decision
**O3 selected**

### Why
Most meaningful disagreement is claim-level, not paper-level.

---

## QOC-04 — What is `paper-qa` in this project?

### Question
How should `paper-qa` be positioned?

### Options
- **O1**: final truth system
- **O2**: retrieval component only
- **O3**: reader/search baseline with explicit boundary

### Criteria
- reuse value
- clarity
- overclaim avoidance
- compatibility with auditor layer

### Decision
**O3 selected**

### Why
It is strong enough to reuse, but not strong enough to absorb the entire verification problem.

---

## QOC-05 — How should paper discovery work?

### Question
What search strategy best fits the project?

### Options
- **O1**: keyword search only
- **O2**: citation chasing only
- **O3**: seeded graph expansion + snowballing + active screening

### Criteria
- recall
- efficiency
- counterevidence usefulness
- operational realism

### Decision
**O3 selected**

### Why
Search quality depends on both expansion and prioritization.

---

## QOC-06 — How should counterevidence search work?

### Question
How should “find opposing evidence” be done?

### Options
- **O1**: search for opposite keywords
- **O2**: paper-level contradiction detection
- **O3**: claim extraction + evidence retrieval + contradiction/context analysis

### Criteria
- real contradiction detection quality
- usefulness for attack matrix
- precision

### Decision
**O3 selected**

### Why
Naive contradiction search creates fake opposition due to context mismatch.

---

## QOC-07 — How should equations be handled?

### Question
What should the system do with equations?

### Options
- **O1**: trust parser output
- **O2**: normalize directly into symbolic form
- **O3**: treat extracted LaTeX as evidence candidate + keep visual fallback

### Criteria
- robustness
- provenance preservation
- parser failure resistance

### Decision
**O3 selected**

### Why
Equation truth cannot be assumed from parser output.

---

## QOC-08 — What should human review look like?

### Question
How should humans participate?

### Options
- **O1**: final checkbox reviewer
- **O2**: ad hoc manual reader
- **O3**: designed subsystem with blind-first review and disagreement logging

### Criteria
- anti-overreliance
- auditability
- review quality
- scalability

### Decision
**O3 selected**

### Why
Human review without design becomes rubber-stamping.

---

## QOC-09 — What is the role of the local verifier script?

### Question
How should the local verification script be framed?

### Options
- **O1**: claim-truth engine
- **O2**: metadata helper
- **O3**: catalog hygiene + Level 1 verifier

### Criteria
- honesty
- architectural clarity
- overclaim avoidance

### Decision
**O3 selected**

### Why
The script checks existence and metadata, not semantic truth.

---

## QOC-10 — What kind of document should preserve the work?

### Question
How should this project be recorded?

### Options
- **O1**: informal chat summaries only
- **O2**: one large manifesto only
- **O3**: manual + project record + QOC log + pilot results

### Criteria
- traceability
- future reuse
- clarity
- onboarding value

### Decision
**O3 selected**

### Why
A single manual is not enough to preserve design rationale.

---

# 5. Pilot Run Record

## Test set
- reconstructed 16-item set
- original support/counterevidence table + later gold notes

## Gold standard
- exact: 11
- partial: 3
- error: 2

## What Level 1 caught well
- fake or conflated sources
- misattributed source strings
- missing/underspecified source identity
- source-type mismatch

## What Level 2 caught
- scope mismatch
- overgeneralization
- conceptual source treated as empirical proof
- proposal/checklist treated as adopted standard

## What Level 3 caught
- overclaim from one source
- need for independent corroboration
- contradiction vs qualifier separation

## Main lesson
Level 1 is necessary but not enough.

---

# 6. Concrete Failure Examples

## Example 1 — Conflation
A source candidate combines multiple real names/ideas into one fake citation target.

Design lesson:
- Level 1 must reject conflated identity before semantic reasoning.

## Example 2 — Numeric provenance failure
A numeric comparison (e.g. “47 vs 38”) is repeated without a recoverable source chain.

Design lesson:
- exact numbers require exact provenance.

## Example 3 — Parser-safe but semantically wrong equation
`x^2` becomes `x_2`, yet downstream symbolic tools may still accept it.

Design lesson:
- parser-safe does not mean source-true.

---

# 7. What Evidence and Counterevidence Matter

## Named support classes
- PRISMA / Cochrane → operational norms
- quotation inaccuracy literature → human failure evidence
- citecheck / SemanticCite / citation auditing → prototype verification systems
- PaperQA2 → baseline reader
- parser benchmark papers → parser limitation evidence

## Named caution classes
- automation bias literature
- Microsoft overreliance literature
- contradiction/context papers
- citation hallucination evaluations
- parser limitation benchmarks

---

# 8. Open Risks

- false positive vs false negative tradeoff remains uncalibrated
- review workload can turn into bureaucracy
- legal caching and artifact storage remain unresolved
- cross-domain ground-truth datasets are still missing
- schema rigidity may appear too early
- human review UX remains under-validated
- pilot cost numbers are still sparse

---

# 9. Canonical Files

These are the most important project artifacts so far:

- `research_verification_manual_v0.4.1_cleanup_patch.md`
- `pilot_run_v0.4.1_report.md`
- `pilot_run_v0.4.1_results.csv`

Optional historical context:
- v0.2
- v0.2_complete
- v0.3 / v0.3.1
- v0.4 draft

---

# 10. Recommended Next Steps

## Immediate
- keep this QOC log with the manual
- use the pilot results as a permanent case study
- avoid splitting canonical versions again

## Next
- run a smaller 5-item end-to-end pilot with actual rereading time recorded
- add measured cost/time numbers
- expand exact evidence table rows
- attach stronger named counterevidence rows where still missing

## Later
- build a stable claim → evidence → contradiction dataset
- test blind review UX
- calibrate scoring only after real data exists

---

# 11. One-Paragraph 5-Year-Old Version

A robot helps find books, but robots can be wrong.
So the robot only brings **possible** books.
Then we check if the book is real, open the real page, read the important part, and compare it with another book if it matters a lot.
The point is not to trust the robot.
The point is to make it easy to check what the robot said.

---

# 12. One-Sentence Summary

> This project is about building a workflow that keeps research claims checkable even when LLMs, parsers, APIs, and humans can all fail.
