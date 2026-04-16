# Next Plan: Level 2 Full Validation

_Identified: 2026-04-16_
_Status: PLANNING NEEDED (separate session)_

---

## Problem

L1에는 적용한 검증 체계를 L2에는 적용하지 않았음:

| 검증 요소 | L1 | L2 |
|---|---|---|
| Gold standard (human) | ✅ 20개 | ❌ 없음 |
| Inter-rater agreement | ✅ Claude vs GPT + Human | ❌ 없음 |
| Operational definition | ✅ error_taxonomy.md | ⚠️ checklist 있지만 SUPPORT/PARTIAL 경계 모호 |
| Clean re-run | ✅ A=94.1%, B=91.9% | ❌ 없음 |
| Baseline comparison | ✅ 5개 시스템 비교 | ❌ 없음 |
| N | 98개 | 8개 (8%) |

## 필요한 것

1. L2 gold standard — 사람이 같은 8개 논문 읽고 claim-evidence alignment 독립 판정
2. L2 inter-rater — 2명+ 독립 판정, 최소 pairwise agreement
3. SUPPORT vs PARTIAL operational definition 강화 — "inferential overreach" 기준 문장화
4. L2 clean re-run — 새 세션에서 같은 8개 재실행
5. L2 baseline — "논문 abstract만 읽고 판정" vs "전문 읽고 판정" 비교

## 판단 필요

- full validation으로 갈지 (conference 수준)
- "L2는 feasibility pilot" scoping으로 갈지 (workshop 수준)
- venue threshold 결과(PASS)와의 관계
