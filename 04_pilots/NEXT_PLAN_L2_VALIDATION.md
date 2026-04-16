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

## Codex L1 Cross-Model Experiment (추가)

_Identified: 2026-04-16_

### 목적
Claude L1 결과와 Codex L1 결과를 같은 데이터(42개)에서 비교.
Claude recall = 73.3% (human gold 기준). Codex는?

### 입력
`04_pilots/codex_L1_input.csv` — 정답 컬럼 제거된 clean 입력 (6개 컬럼만)

### 출력
`04_pilots/codex_L1_results.csv`

### 결과 해석 프레임

| 결과 | 의미 | 논문 contribution |
|---|---|---|
| Codex = Claude (같은 에러 잡고, 같은 것 놓침) | LLM 공통 약점 | "모델 교체로 해결 불가, 인간 검증 또는 API 자동화 필요" |
| Codex가 Claude 놓친 4개(E5,I1,J9,E9) 잡음 | Multi-model 가치 증명 | "Claude+Codex 조합이 단일 모델보다 recall 높음" |
| Codex가 Claude보다 많이 놓침 | 모델 선택 중요 | "모든 LLM이 동등하지 않다 — task별 모델 선택 근거" |

### 캐시 주의
- `codex_L1_input.csv`만 읽게 할 것
- 프로젝트 내 다른 파일(experiment_master_plan.md 등)에 정답이 있으므로 접근 금지
- 프롬프트에 "다른 파일 접근 금지" 명시 완료

---

## 판단 필요

- full validation으로 갈지 (conference 수준)
- "L2는 feasibility pilot" scoping으로 갈지 (workshop 수준)
- venue threshold 결과(PASS)와의 관계
- Codex 결과에 따라 multi-model 실험 확대 여부
