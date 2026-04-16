# L2 Calibration Log

_Date: 2026-04-16_
_Purpose: Decision tree v1.0으로 기존 9개 claim-source pair 재판정. v0.1 판정과 비교._
_기존 9개는 calibration set. 이후 evaluation에 사용하지 않음._

---

## Calibration Results

| ID | Paper | v0.1 Verdict | v1.0 Verdict | v1.0 Sub | 일치? | 변경 사유 |
|---|---|---|---|---|---|---|
| A3 | Hegazy | PARTIAL | PARTIAL | MINOR | ✓ (parent) | 숫자는 정확하지만 COT 조건 누락 = 조건 과장. 원문에 "diversity premium" 개념은 있음 → overstatement |
| B1 | Qian | PARTIAL | PARTIAL | **MAJOR** | ✓ (parent) | "lazy loading"이 원문에 없음 = attribution gap. scaling law 자체는 있지만 아키텍처 처방은 귀속 |
| I1-a | Tam (JSON) | SUPPORT | SUPPORT | — | ✓ | Step 2 YES: 27pp drop 수치, 메커니즘, task dependency 모두 보존됨 |
| I1-b | Tam (NL-to-Format) | PARTIAL → SUPPORT* | **SUPPORT** | — | ✓ | Step 2 YES: supplement에서 수정됨. 원문이 NL-to-Format을 "important mitigation strategy" 명시적 추천 |
| S-02 | PRISMA-trAIce | PARTIAL | PARTIAL | MINOR | ✓ (parent) | disclosure 3 pillars는 원문에 있음. "proposal" → "norm" 지위 격상 = overstatement |
| C-04 | Rosbach (AB) | PARTIAL | PARTIAL | **MAJOR** | ✓ (parent) | "blind-first review" 추천이 원문에 없음 = attribution gap. 7% AB 수치는 정확하지만 설계 처방은 citing doc 추론 |
| S-01 | PRISMA 2020 | PARTIAL | **UNCERTAIN** | — | **✗** | 원문(SR 보고 가이드라인)이 citation verification과 접선적 관련만 있음. Step 1에서 "관련 내용 있음"보다 "다른 도메인" 판단이 적절. 비유적 관련 ≠ evidence. Edge case E9 참조 |
| S-04 | SemanticCite | PARTIAL | PARTIAL | MINOR | ✓ (parent) | 4-class 분류는 원문에 있음. "validates our approach" 과장 = overstatement. staged cost architecture는 원문에 없지만 claim의 핵심은 "multi-class validation" |
| C-02 | SLR Problems | PARTIAL | PARTIAL | **MAJOR** | ✓ (parent) | "67 problems" 숫자는 정확. 하지만 ">90% SRs are useless"는 원문에 없음 = attribution gap (claim inflation) |

## Summary

| Metric | 결과 |
|---|---|
| Parent-class 일치 | **8/9** (89%) |
| Parent-class 불일치 | **1/9** (S-01: PARTIAL → UNCERTAIN) |
| Sub-type 분류 결과 | 2 SUPPORT, 3 PARTIAL-MAJOR, 2 PARTIAL-MINOR, 1 UNCERTAIN |
| v0.1에 없던 구분 | MAJOR vs MINOR 세분화가 error 심각도를 분리 (B1, C-04, C-02 = MAJOR; A3, S-02, S-04 = MINOR) |

## 불일치 분석: S-01 (PARTIAL → UNCERTAIN)

**v0.1 판정:** PARTIAL — "PRISMA is accurately cited as existing and being a structured checklist. But citing it as 'supporting evidence' for our verification framework overstates the connection."

**v1.0 판정:** UNCERTAIN — Decision tree Step 1에서 "원문에 claim과 관련된 내용이 있는가?"에 대해:
- PRISMA는 systematic review **보고** 가이드라인
- Citing document의 claim은 citation **검증** 프레임워크의 근거
- 이 두 도메인은 "구조화된 체크리스트"라는 형식적 유사성만 공유
- v1.0 edge case E9 (tangentially related)과 정확히 일치

**판단:** v1.0이 더 정확. v0.1은 "관련 있지만 과장"으로 봤으나, 실제로는 "다른 도메인의 비유적 참조". UNCERTAIN이 PARTIAL보다 적절.

**Tree 수정 필요?** 아니오. Tree는 정상 작동. v0.1이 Step 1에서 너무 관대했을 뿐.

## Calibration 합격 기준 확인

플랜 기준: "8/9 이상 일치 또는 불일치 case에서 Tree가 더 나은 판정을 내림"
- Parent-class 일치: 8/9 ✓
- 불일치 1건(S-01): Tree가 더 정확한 판정 ✓
- **PASS**

## 분포 변화

| Category | v0.1 | v1.0 |
|---|---|---|
| SUPPORT | 2 (22%) | 2 (22%) |
| PARTIAL | 7 (78%) | 5 (56%) — 3 MAJOR + 2 MINOR |
| UNCERTAIN | 0 (0%) | 1 (11%) |
| REFUTE | 0 (0%) | 0 (0%) |

PARTIAL 비율이 78% → 56%로 감소. MAJOR/MINOR 세분화 + S-01 재분류 효과.

---

## v1.0 이후 수정 사항

현재 없음. Calibration PASS로 decision tree v1.0 유지.
