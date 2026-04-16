# Pilot Run Report — Claude × Manual v0.4.1

_Date: 2026-04-15_
_AI: Claude Opus 4.6_
_Manual version: v0.4.1_
_Source: 03_records/claude/session_record_20260415.md, Phase 8_

---

## Design

- Test set: 16 sources from original evidence table
- Gold standard: verification results from Phase 2 (web search verification)
- Workflow: Manual v0.4.1, Levels 0→1→2
- Question: Does the workflow catch known errors?

---

## Results Summary

| Verdict | Count |
|---|---|
| PASS | 10 |
| PARTIAL | 2 |
| FAIL | 2 |
| UNVERIFIED | 1 |

### Key Metrics

| Metric | Value |
|---|---|
| Level 1 detection rate | 4/5 known errors = **80%** |
| False positives | **0** |
| Pre-workflow accuracy | ~69% (11/16) |
| Post-Level-1 accuracy | ~92% (11/12) |
| Time per source | ~6 minutes |
| Total pilot time | ~90-110 minutes (16 sources) |

---

## Error Types vs Level 1 Detection

| Error type | Example | Caught at L1? |
|---|---|---|
| Author conflation | C-06: Storey+Ernst merged | Yes |
| Wrong year/venue | C-04: "PubMed, 2016" → JAMIA 2012 | Yes |
| Claim inflation | C-02: "90% useless" overstated | Yes |
| Unverifiable numbers | C-08: "47 vs 38" no source | Yes |
| Procedural gap (not searched) | S-08: Research Debt skipped | No |

---

## What Level 1 Cannot Catch

- "Does this paper actually support this claim?" → needs Level 2
- Exact numeric claims within papers → needs Level 2
- Scope mismatch / overclaim → needs Level 2/3

---

## Conclusion

Level 1 (registry/metadata check) is effective for catching hard failures (wrong author, wrong year, fabricated citations). It does NOT replace semantic verification (Level 2/3).
