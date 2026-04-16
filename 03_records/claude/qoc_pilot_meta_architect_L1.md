# QOC Record — Pilot: Meta Architect Level 1 Verification

_Date: 2026-04-15_
_Session: Claude Opus 4.6_

---

## Question 1: research-system Level 1 vs meta-architect's own verification — which catches more?

### Options Considered

| Option | Pros | Cons |
|---|---|---|
| A. Trust meta-architect's VERIFIED tags | Fast, already done | LLM verified LLM — circularity |
| B. Run research-system Level 1 on all 37 | Independent check, catches metadata errors | Takes ~1 session |
| C. Skip Level 1, go straight to Level 2 | Tests deeper claims | Misses basic errors, expensive |

### Criteria
- Independence from original LLM verification
- Error detection rate
- Cost (time)
- Scientific rigor

### Decision: B (run Level 1 on all 37)

### Outcome
- 9 errors found in 37 papers (24% error rate)
- 2 FAIL (wrong authors), 7 PARTIAL (venue/title discrepancies)
- Meta-architect VERIFIED tags: 5/6 correct, 1/6 missed venue update
- Level 1 proved its value on first real-world test

---

## Question 2: What order to verify? Level 1 first or Level 2 first?

### Options Considered

| Option | Pros | Cons |
|---|---|---|
| A. Level 2 first on 5 selected papers | Tests deeper claims immediately | Expensive, selection is guesswork |
| B. Level 1 first on all, then Level 2 on selected | Data-driven selection for Level 2 | Takes longer overall |

### Decision: B

### Rationale
- Level 1 is cheap and broad — covers all 37 papers in one pass
- Level 1 results inform Level 2 selection (not guessing)
- Phase 1 alone already answers "does research-system add value over meta-architect's system?"

---

## Question 3: How to handle the circularity problem?

### Context
Meta-architect's VERIFIED tags were applied by an LLM. Running Level 1 with another LLM doesn't fully solve circularity — but it does add:
1. Independent second opinion
2. Live web verification (not memory-based)
3. Structured comparison against source of record (arXiv pages)

### Decision: Accept partial mitigation
- Level 1 uses live web data (not LLM memory) → reduces circularity
- Record all evidence (URLs, actual metadata) for human review
- Flag remaining uncertainty explicitly

---

## Question 4: Should claim mapping context be prepared before Level 2?

### Options
| Option | Pros | Cons |
|---|---|---|
| A. Prepare claim mapping now | Level 2 agent has full context | Extra work before Level 2 starts |
| B. Do claim mapping during Level 2 | Simpler | Level 2 agents lack context, user flagged this |

### Decision: A — prepare now
User correctly identified that verification without context is meaningless for Level 2.
Extracted claim mapping from `paper-feature-map.json` + Phase 0 plan → saved to `05_evidence/source_tables/meta_architect_claim_mapping.md`.

---

## Key Facts Established

1. LLM-generated paper catalogs: **76% metadata-accurate** (28/37 exact, excluding NOT VERIFIED)
2. Error pattern: conflation (mixing metadata between papers), not fabrication
3. Author attribution errors: 2/37 (5%) — most dangerous type
4. Venue inflation: 1/37 — workshop cited as main conference
5. Meta-architect VERIFIED tag reliability: 83% (5/6)
6. Level 1 verification cost: ~1 session for 37 papers
7. Level 1 value: catches errors that meta-architect's own system missed
