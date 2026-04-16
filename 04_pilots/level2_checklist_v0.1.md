# Level 2 Verification Checklist v0.1

_Created: 2026-04-15_
_Derived from: v0.4.1 SS3.3, SS6.1, SS7.1, SS8.3_

---

## Purpose

Level 2 verification determines whether a cited source **actually supports the claim** made in the citing document. Level 1 checks "does this paper exist with correct metadata?" Level 2 checks "does this paper say what you claim it says?"

---

## Procedure (per source)

### Step 1: Claim Identification
- [ ] State the **exact claim** in the citing document that references this source
- [ ] Identify the **claim type**: factual number, design recommendation, conceptual framework, empirical finding
- [ ] Record the **citing passage** (file, line number, exact text)

### Step 2: Source Access
- [ ] Obtain full text (PDF/HTML/TeX)
- [ ] Confirm access (no paywall; fallback if needed)
- [ ] Note source format and length

### Step 3: Relevant Section Location
- [ ] Identify section(s) most likely to contain supporting evidence
- [ ] Read those sections fully (not just abstract)
- [ ] Record **source span**: exact text, section reference, page/paragraph

### Step 4: Claim-Evidence Alignment Judgment
- [ ] Assign judgment:
  - `SUPPORT` — source directly and accurately supports the claim
  - `PARTIAL` — source partially supports but claim overstates, omits caveats, or makes unsupported inferences
  - `REFUTE` — source contradicts the claim
  - `UNCERTAIN` — evidence is ambiguous or insufficient to judge
- [ ] Write 1-2 sentence justification
- [ ] Record confidence: HIGH / MEDIUM / LOW

### Step 5: Caveat Documentation
- [ ] List caveats the citing claim omits (conditions, limitations, scope restrictions)
- [ ] Note if the claim makes inferences beyond what the source states
- [ ] Flag any numerical inaccuracies

### Step 6: Time Recording
- [ ] Record wall-clock time for this source (start → finish)

### Step 7: Output
- [ ] Fill CSV row
- [ ] Write evidence bundle (claim, span, judgment, justification, caveats)

---

## Judgment Criteria

| Judgment | Definition |
|----------|------------|
| SUPPORT | The source contains a passage that directly and accurately supports the claim as stated. No material omissions in the citing claim. |
| PARTIAL | The source contains relevant evidence, but the citing claim (a) overstates the finding, (b) omits important caveats/conditions, (c) infers beyond what the source states, or (d) uses the source for a purpose it wasn't designed for. |
| REFUTE | The source contains evidence that contradicts or undermines the claim. |
| UNCERTAIN | The source is ambiguous, the relevant section is unclear, or the evidence is insufficient to judge alignment. |

---

## Known Limitations

1. **Circularity**: When an LLM verifies claims that an LLM generated, the verifier may share biases with the generator
2. **Interpretation subjectivity**: Claim-evidence alignment requires judgment; reasonable people may disagree
3. **Scope**: Only checks cited claims, not whether better sources exist
4. **Depth**: Cannot verify mathematical proofs, replicate experiments, or assess statistical validity in depth
