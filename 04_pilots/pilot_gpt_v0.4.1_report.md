# Pilot Run Report — GPT × Manual v0.4.1

_Date: 2026-04-15_
_AI: ChatGPT_
_Manual version: v0.4.1_
_Source: 03_records/claude/session_record_20260415.md, Phase 11_

---

## Design

- Test set: Same 16 sources (minus C-02)
- Method: Re-ran Level 1 on same set. Level 2/3 mapped against gold notes (did NOT read PDFs from scratch)
- Added "first issue layer" column

---

## Results Summary

- 2/2 hard failures caught at Level 1 (identical to Claude pilot)
- 2 partials flagged
- Most risk lives at Level 2 (per "first issue layer" column)

---

## Additional Confirmations

| Source | Status |
|---|---|
| Baethge & Jergas | Confirmed: Research Integrity and Peer Review 2025;10:13. 46 studies, ~32,000 quotations, 16.9% error, 8.0% major |
| Research Debt | Confirmed: Distill 2017, DOI 10.23915/distill.00005 |

---

## Limitations

- Level 2/3 mapped from gold notes, not fresh PDF reading
- No time measurement
- Excluded C-02 (SLR problems) from test set
- No new failure modes discovered

---

## Combined Pilot Conclusion (Claude + GPT)

- Level 1 hard failure detection: **reproduced across 2 independent runs**
- Level 2/3: still theoretical (gold-note mapping only)
- Time measurement: only Claude pilot estimated ~6 min/source
- Next step needed: 5-source PDF-reading pilot with wall-clock timing
