# L1 Normalization Rules — v1.0

_Created: 2026-04-16 (Phase 1, parallel task)_
_Purpose: Claude vs Codex L1 결과 재채점을 위한 정규화 규칙 고정_

---

## Rules

### N1: 약어 확장 (Abbreviation Expansion)

**규칙:** CS 분야에서 자명한 약어 확장/축약은 EXACT.

| 예시 | 판정 |
|---|---|
| "LLMs" ↔ "Large Language Models" | EXACT |
| "MAS" ↔ "Multi-Agent Systems" | EXACT |
| "NLP" ↔ "Natural Language Processing" | EXACT |
| "CoT" ↔ "Chain of Thought" | EXACT |
| "SwarmBench" vs "Benchmarking LLMs' Swarm Intelligence" | PARTIAL — 비공식 약칭, 자명하지 않음 |

**기준:** 해당 분야 연구자가 추가 설명 없이 같은 논문으로 인식하면 EXACT.

### N2: Subtitle 생략 (Subtitle Omission)

**규칙:** 콜론 이후 부분(subtitle) 생략은 **조건부 EXACT**.

| 조건 | 판정 |
|---|---|
| Main title이 unique (동명 논문 없음) | EXACT |
| 동명 논문 존재 가능 | PARTIAL — subtitle이 disambiguation에 필요 |
| Subtitle만 다르고 main title 동일한 다른 논문이 실재 | PARTIAL |

**기준:** subtitle 없이도 정확히 하나의 논문으로 식별 가능하면 EXACT.

### N3: Venue Alias (Venue 별칭)

**규칙:** 공식 약어/별칭은 EXACT. 비공식이거나 다른 venue면 PARTIAL/FAIL.

| 예시 | 판정 |
|---|---|
| "TACL" ↔ "Transactions of the ACL" | EXACT |
| "ICML 2024" ↔ "International Conference on Machine Learning, 2024" | EXACT |
| "NeurIPS" ↔ "NeurIPS 2025" (연도만 추가) | EXACT |
| "arXiv" → "TMLR" (preprint → journal 게재) | PARTIAL (venue_drift) |
| "ICML Workshop" → "ICML" (workshop → main) | PARTIAL (venue_inflation) |
| "ScienceDirect" (플랫폼) → actual journal name | PARTIAL (venue 불명확) |

### N4: 저자 비교 (Author Comparison)

**규칙:**
- "(unknown)" 또는 "(survey)" 등 catalog placeholder는 **에러가 아님** — metadata gap
- 실제 저자가 다른 사람이면 **에러** (PARTIAL 또는 FAIL)
- "et al." 사용은 EXACT (first author + et al. 관행)

| 예시 | 판정 |
|---|---|
| "Li et al." (catalog) vs "Li, Wang, Zhang" (actual) | EXACT — et al. 관행 |
| "(unknown)" (catalog) vs "Smith et al." (actual) | **NOT AN ERROR** — metadata gap, 별도 표기 |
| "Zhao et al." (catalog) vs "Gao et al." (actual) | **FAIL** — 다른 사람 |
| "Li et al." (catalog) vs "Salemi et al." (actual) | **FAIL** — 다른 사람 |

---

## 적용 절차

1. 각 논문에 대해 N1-N4 적용
2. 모든 규칙 적용 후 나머지 차이가 있으면 PARTIAL
3. 차이 없으면 EXACT
4. 다른 논문으로 매핑되면 FAIL

## 재채점 대상

`pilot_meta_architect_L1_results.csv` (Claude, 42개) + `codex_L1_results.csv` (Codex, 41개)를
이 규칙으로 재채점 → `cross_model_L1_rescored.csv`
