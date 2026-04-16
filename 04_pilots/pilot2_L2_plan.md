# Pilot 2 Plan — Level 2 Source Reading

_Created: 2026-04-15_
_Status: PLANNED (not yet executed)_
_Predecessor: Pilot 1 (Level 1, 16 sources) — see `pilot_claude_v0.4.1_report.md`_

---

## Context

Pilot 1 ran Level 1 (metadata verification) on 16 sources. Results: 80% error detection, 0 false positives. But Level 1 cannot catch **semantic errors** — cases where a paper exists but doesn't actually support the claimed argument.

Pilot 2's job: run Level 2 (source reading) for real and measure what it adds.

---

## Problems with the Original Plan (5 issues)

### 1. Level 2 checklist does not exist
v0.4.1 SS3.3 describes what Level 2 is (source span capture, page references, verified notes) but not step-by-step how. Pilot 1 had a clear procedure ("search registry, compare metadata"). Level 2 has "read the PDF and... do something."

**Fix:** Create checklist before running pilot (Step 0).

### 2. "Which claim to verify" is undefined
Pilot 1 = "does this paper exist?" (Yes/No). Level 2 = "does this paper support this claim?" — but the 16-source table never explicitly defines which specific claim each source backs. Only says "Supporting evidence."

**Fix:** Explicit claim mapping per source (Step 1).

### 3. No gold standard (circularity problem)
Pilot 1 gold standard: registry lookup (objective). Level 2 gold standard: "does paper support claim?" — judged by whom? If Claude judges, Claude validates Claude. This is the automation bias the project itself warns about.

**Fix:** Cannot fully solve, but mitigate: (a) require literal quotes, (b) output must be human-reviewable, (c) confidence ratings on every judgment.

### 4. PDF accessibility not confirmed
arXiv = free. BMJ/JMIR = mostly open access. JCE/JAMIA/Milbank Q = possible paywall. Selecting a paywalled paper kills the pilot.

**Fix:** Confirm access before selection; have fallbacks ready.

### 5. No success criteria
Pilot 1: "does Level 1 catch errors?" -> 80%. Pilot 2: "Level 2 finds something" is not a success criterion.

**Fix:** Define 4 specific questions (see Goals below).

---

## Goals (priority order)

| # | Question | Type |
|---|---|---|
| 1 | Can Level 2 be turned into a repeatable process? | Process |
| 2 | Does Level 2 find things Level 1 missed? | Value |
| 3 | How long does it take per source? | Cost |
| 4 | Where does Level 2 break down? | Limits |

---

## Steps

### Step 0 (pre-pilot): Create Level 2 Checklist

Extract from v0.4.1 SS3.3 + SS6.1 + SS7.1 + SS8.3:

1. Access source full text (PDF/TeX/HTML)
2. State the specific claim this source allegedly supports (claim schema)
3. Locate relevant section(s) in source
4. Record literal text span (page, paragraph)
5. Judge claim-span alignment: `SUPPORT` / `PARTIAL` / `REFUTE` / `UNCERTAIN`
6. Write 1-2 sentence justification for judgment
7. If equations/tables/figures are relevant, note separately
8. Write verified note

**Output:** `04_pilots/level2_checklist_v0.1.md`

### Step 1: Claim Mapping

For each of the 5 selected sources, explicitly define:
- The claim from our architecture document that cites this source
- The exact sentence or passage making the claim
- What the source is supposed to demonstrate

Uses v0.4.1 SS6.1 claim schema format.

### Step 2: Source Selection (5 sources)

**Selection criteria (revised):**
- Level 1 PASS but semantic question remains
- Open access only (no paywalls)
- Mix of verdict categories

| # | Source | L1 Result | Selection Reason | Access |
|---|---|---|---|---|
| 1 | S-01 PRISMA 2020 (BMJ) | EXACT | Control — fast check, time baseline | Open access |
| 2 | S-02 PRISMA-trAIce (JMIR) | EXACT | Does "AI+PRISMA" actually support our specific claim? | Open access |
| 3 | S-04 SemanticCite (arXiv) | EXACT | Does 4-class citation verification actually overlap our design? | arXiv (free) |
| 4 | C-02 SLR problems (JCE) | PARTIAL | "67 problems" vs "90% useless" — top candidate for verdict change | Access TBD |
| 5 | C-04 Automation Bias | PARTIAL | Goddard et al. JAMIA 2012 — verify 7% figure in original | Access TBD |

**Fallbacks (if C-02/C-04 paywalled):**
- C-05 Robotic Bureaucracy (Research Policy) — EXACT but claim alignment unchecked
- S-05 Citation Auditing (arXiv) — free access

### Step 3: Execute + Time

Per source:
- T0: Open full text
- T1: Find relevant section
- T2: Fill evidence bundle
- T3: Claim-evidence judgment

Record: where was it hard, where was confidence low.

### Step 4: Write Results

| Output | Path |
|---|---|
| Level 2 checklist | `04_pilots/level2_checklist_v0.1.md` |
| Pilot 2 report | `04_pilots/pilot_claude_v0.4.1_L2_report.md` |
| Pilot 2 results CSV | `04_pilots/pilot_claude_v0.4.1_L2_results.csv` |

---

## Explicit Limitations (what this pilot CANNOT answer)

- Scalability to 50+ sources (only testing 5)
- Inter-rater reliability (Claude only, no second AI)
- Level 3 (cross-verification) added value
- Performance on math/CS papers
- Whether the circularity problem is truly mitigated or just documented

---

## Execution Notes

- This plan was designed after reviewing v0.4.1 SS3.3, SS6.1, SS7.1, SS8.3
- Pilot 1 results: `pilot_claude_v0.4.1_report.md` + `pilot_claude_v0.4.1_results.csv`
- Full session context: `03_records/claude/session_record_20260415.md`
