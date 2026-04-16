# Research Workflow / Verification Project Log + QOC

## 문서 목적

이 문서는 지금까지 진행한 **research verification / workflow design** 논의를 기록으로 남기기 위한 통합 문서다.

이 문서는 다음을 동시에 수행한다.

* 지금까지의 설계 변화 기록
* 버전별 차이 정리
* 핵심 decision와 rationale 보존
* 남은 open question 정리
* QOC(Questions / Options / Criteria) 형태로 의사결정 구조 기록

---

# 1. Project Snapshot

## 현재 한 줄 정의

이 프로젝트는 **LLM, parser, registry, human reviewer 모두를 fallible component로 보고**, scientific claim / citation / contradiction / version risk를 **provenance-first**하게 관리하는 workflow를 설계하는 것이다.

## 현재까지 갈라진 두 축

### 축 A — Verification Architecture

대표 문서: **v0.4.1**

핵심 질문:

* 무엇을 trust하고 무엇을 trust하지 말아야 하는가?
* claim verification system을 어떤 architecture로 설계해야 하는가?
* registry, parser, reader, human review, version governance를 어떻게 구분할 것인가?

핵심 성격:

* 설계 문서
* evidence-grounded manual
* provenance / uncertainty / trust boundary 중심

### 축 B — Research Operations Protocol

대표 문서: **v1.2**

핵심 질문:

* 여러 AI를 실제 연구 workflow 안에서 어떻게 운영할 것인가?
* 질문 난이도와 위험도에 따라 어떤 tier를 쓸 것인가?
* 언제 멈추고, 언제 escalation 하고, 어떤 claim을 먼저 공격할 것인가?

핵심 성격:

* 운영 매뉴얼
* execution protocol
* step-by-step workflow 중심

## 현재의 핵심 인식

이 둘은 경쟁 관계가 아니라 **상보적**이다.

* **v0.4.1** = spine / architecture / trust design
* **v1.2** = workflow engine / operational protocol

즉,

> **근거 있는 설계 + 실행 가능한 운영**
> 을 합쳐야 다음 버전이 강해진다.

---

# 2. Timeline / Version Evolution

## Phase 0 — 막연한 multi-AI cross-check 아이디어

초기 상태에서는 여러 AI에게 서로의 답을 계속 보여주면서 검토시키는 방식이 강하게 고려되었다.

예시:

* A가 답함
* B에게 “A가 이렇게 말했어”
* C에게 “A와 B가 이렇게 말했어”
* D에게 “누가 맞아?”

### 이 방식의 문제로 드러난 것

* dialogue contamination
* anchoring / framing drift
* correlated error
* agent debate overhead
* source provenance loss

### 교정된 핵심 인식

문단 vs 문단 비교가 아니라,

> **claim vs evidence** 구조로 내려가야 한다.

---

## Phase 1 — CAVI / claim-centered workflow 등장

핵심 흐름:

* Question Lock
* Independent Search
* Claim Matrix
* Contradiction Pass
* Blind Attack
* Judge
* Final Memo

### 장점

* 문단 레벨 오염을 줄임
* claim unit으로 검증 단위를 고정
* contradiction를 강제적으로 찾게 만듦

### 한계

* strongest paper를 찾는 기준이 약함
* evidence strength가 명시되지 않음
* context mismatch와 fake contradiction 분리가 약함
* stopping rule이 없음
* retrieval algorithm 자체가 약함

---

## Phase 2 — 강화 피드백 반영

추가된 핵심 요소:

* claim canonicalization
* evidence scoring
* independence clustering
* retrieval algorithm explicitness
* stopping rule
* context-aware contradiction analysis

### 이때의 핵심 개선 포인트

1. 논문 단위가 아니라 claim 단위 검증
2. strongest paper 선정 전에 evidence strength 비교
3. support / contradiction를 context-aware하게 분리
4. retrieval strategy 자체를 명시
5. 언제 멈추는지 규칙 추가

---

## Phase 3 — v1.0 / v1.1 / v1.2로 이어지는 운영 매뉴얼 강화

### v1.0

* 좋은 아이디어 / 좋은 구조
* 하지만 execution layer가 아직 약함

### v1.1

추가:

* Evaluation Layer
* Reviewer Calibration Layer
* Coverage Risk Check

핵심 의미:

* 이제 단순한 절차 문서가 아니라 **검증 가능한 프로토콜**로 진화

### v1.2

추가:

* Execution Tiers
* Escalation Triggers
* Coverage-aware Stopping Rule
* Claim Triage
* Blind Attack raw-evidence-linked mode
* Evidence scoring anchors + rationale + confidence
* tier별 evaluation intensity
* Artifact / Manifestation Governance

핵심 의미:

> **좋은 프로토콜**에서
> **실제로 굴릴 수 있는 운영 매뉴얼**로 발전

---

# 3. Current Comparative View

## v0.4.1 vs v1.2

| 항목       | v0.4.1                                                                | v1.2                                                                            |
| -------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 중심 질문    | 검증 시스템을 어떻게 설계할 것인가                                                   | 여러 AI를 써서 연구를 어떻게 운영할 것인가                                                       |
| 강점       | evidence base, case study, parser 한계, reader/auditor 구분, trust layers | execution tiers, escalation, stopping, triage, prompt library, workflow clarity |
| 약점       | 실제 운영 순서와 tiering이 약함                                                 | 구조는 강하지만 실증 evidence와 case study가 약함                                            |
| 잘하는 것    | architecture / trust boundary / governance 철학                         | practical workflow / step-by-step operation                                     |
| 합치면 얻는 것 | 근거 있는 설계 + 실행 가능한 운영                                                  | 근거 있는 설계 + 실행 가능한 운영                                                            |

## 현재 판단

* v0.4.1은 **더 grounded**하다.
* v1.2는 **더 operational**하다.
* 다음 버전은 둘을 merge해야 한다.

---

# 4. Key Decisions So Far

## D1. Unit of verification = paper가 아니라 claim

### 이유

* paper-level contradiction은 가짜일 수 있음
* 실제 충돌은 metric / dataset / definition / time / scope mismatch에서 많이 생김

### 결과

* claim canonicalization 도입
* claim matrix를 핵심 구조로 채택

---

## D2. Reader와 Auditor는 분리해야 한다

### 이유

* strong reader는 retrieval / summarization / citation answer를 잘할 수 있음
* 하지만 manifestation governance, contradiction audit, parser uncertainty, anti-overreliance review는 reader만으로 해결 안 됨

### 결과

* `paper-qa` 같은 시스템은 reader/search baseline으로 정의
* auditor layer는 별도로 설계

---

## D3. Human review는 safety blanket가 아니다

### 이유

* humans can overtrust AI
* calibration 없는 review는 drift 가능
* reviewer agreement가 높아도 다 같이 틀릴 수 있음

### 결과

* reviewer calibration
* adjudication rule
* borderline casebook
* blind-first review 설계 필요

---

## D4. Search는 하나의 pass로 끝나지 않는다

### 이유

* keyword search alone은 recall 한계
* citation chasing alone은 echo chamber 위험
* active screening alone은 stopping 문제가 있음

### 결과

* seed expansion
* snowballing
* terminology variation
* venue variation
* coverage-aware stopping rule

---

## D5. “더 안 나온다” ≠ “충분히 찾았다”

### 이유

* coverage illusion 가능
* strongest opposition miss risk가 남을 수 있음
* terminology variation / venue diversity가 부족할 수 있음

### 결과

* coverage-aware stopping rule 채택
* stop only if coverage gate 통과

---

## D6. 숫자 점수는 truth가 아니라 structured judgment다

### 이유

* score만 있으면 fake precision 발생
* 사람마다 1 vs 2를 다르게 줄 수 있음

### 결과

* score + rationale + confidence 저장
* 특히 directness / independence / claim specificity / methodological quality에 confidence 필수

---

## D7. workflow governance만으론 부족하고 artifact governance도 필요하다

### 이유

* preprint / conference / journal / corrected / retracted / superseded 관리 필요
* 예전 verdict를 잘못된 manifestation에 묶어둘 위험

### 결과

* work_id / manifestation_id / verdict_id 분리
* revalidation trigger 명시

---

# 5. Current Open Problems

## O1. Independent Search A + B가 진짜 independent retrieval인가?

현재 상태에서는 Search A와 Search B가 실행은 독립적이지만, retrieval strategy까지 강제적으로 분리되어 있진 않다.

문제:

* 같은 질문을 두면 seed overlap이 크게 날 수 있음
* 역할 분리와 retrieval diversity는 다름

남은 과제:

* Searcher A / B에 retrieval policy를 명시적으로 부여
* 예: A = high-precision seed search, B = citation chasing + terminology variation

---

## O2. v1.2의 scoring과 v0.4.1의 scoring을 어떻게 통합할까?

현재 관찰:

* v0.4.1 = 더 epistemically cautious
* v1.2 = 더 operationally usable

남은 과제:

* 형식은 v1.2 채택
* warning / humility 문구는 v0.4.1 채택

---

## O3. 실제 claim당 비용은 얼마인가?

지금까지 많이 논의됐지만, 실제 운영 cost는 아직 pilot로 측정되지 않았다.

필요 측정값:

* time per resolved claim
* time per tier
* strongest opposition miss rate
* reviewer fatigue point
* skipped-step frequency

---

## O4. external gold truth 문제는 얼마나 현실적으로 해결 가능한가?

문서상으론 gold set, held-out set, external audit가 있지만,
현실적으로는 비용이 크다.

남은 과제:

* sentinel claim set
* small gold adjudicated set
* partial benchmark strategy

---

## O5. pairwise judge는 어디까지 믿을 수 있는가?

현재는 close call에만 쓰고 swap-order 2회를 넣지만,
여전히 model-specific bias, rubric wording sensitivity 문제가 남는다.

---

# 6. QOC

---

## QOC 1 — 검증 단위를 무엇으로 둘 것인가?

### Question

검증 단위를 paper로 둘 것인가, claim으로 둘 것인가?

### Options

* **O1. Paper-level verification**
* **O2. Claim-level verification**
* **O3. Hybrid: paper-level screening 후 claim-level audit**

### Criteria

* fake contradiction 감소
* support/contradiction의 정확도
* provenance traceability
* auditability
* 운영 복잡도

### Discussion

* Paper-level verification은 빠르지만, scope mismatch나 metric mismatch를 잘못 contradiction로 보는 문제가 크다.
* Claim-level verification은 더 정확하지만 비용이 증가한다.
* Hybrid는 screening cost와 audit precision 사이의 절충안이다.

### Current Decision

**O3 (Hybrid)** 채택.

* paper-level은 candidate generation / screening 용
* claim-level은 실제 support/contradiction audit 용

### Status

Accepted

---

## QOC 2 — Reader와 Auditor를 통합할 것인가 분리할 것인가?

### Question

literature QA / search system과 verification / audit system을 하나로 볼 것인가?

### Options

* **O1. Single unified system**
* **O2. Reader baseline + separate auditor layer**
* **O3. Reader 중심, auditor는 human-only 보완**

### Criteria

* modularity
* trust boundary clarity
* implementation feasibility
* audit rigor
* long-term maintainability

### Discussion

* unified system은 편하지만 boundary가 흐려질 수 있다.
* reader와 auditor를 분리하면 trust model이 더 명확해진다.
* human-only auditor는 scale이 약하다.

### Current Decision

**O2** 채택.

### Status

Accepted

---

## QOC 3 — 검색을 한 번만 할 것인가 다단계로 할 것인가?

### Question

retrieval을 single-pass로 할 것인가, multi-pass로 할 것인가?

### Options

* **O1. single keyword search**
* **O2. keyword + review-first expansion**
* **O3. seeded graph expansion + snowballing + terminology variation + active screening**

### Criteria

* recall
* strongest opposition 발견 가능성
* time cost
* echo chamber risk
* stopping clarity

### Discussion

* single search는 빠르지만 miss risk가 큼.
* multi-pass는 recall이 좋지만 비용이 크다.
* coverage-aware stopping 없으면 multi-pass도 무한히 늘어난다.

### Current Decision

**O3**를 high-stakes 이상 기본 전략으로 채택.
Tier A에서는 O2 또는 축소된 O3 허용.

### Status

Accepted with tier sensitivity

---

## QOC 4 — Evidence strength를 숫자로 표현할 것인가?

### Question

evidence strength를 scoring으로 표현할 것인가, qualitative note로만 남길 것인가?

### Options

* **O1. no scoring, qualitative note only**
* **O2. weighted scoring formula**
* **O3. anchored scoring + rationale + confidence**

### Criteria

* repeatability
* calibration 가능성
* false precision 위험
* operational usability
* reviewer burden

### Discussion

* no scoring은 유연하지만 반복 사용시 비교가 어렵다.
* weighted formula는 과학적으로 validated되지 않으면 위험하다.
* anchored scoring + rationale + confidence는 fake precision을 줄이면서 operational하게 쓸 수 있다.

### Current Decision

**O3** 채택.
단, “structured judgment이지 measurement instrument는 아니다” 문구를 유지.

### Status

Accepted

---

## QOC 5 — Human review를 어떻게 설계할 것인가?

### Question

human review를 단순 final check로 둘 것인가, calibration/adjudication subsystem으로 둘 것인가?

### Options

* **O1. final sanity check only**
* **O2. calibrated adjudication subsystem**
* **O3. full blind dual review on all claims**

### Criteria

* reviewer reliability
* cost
* scalability
* bias mitigation
* suitability for high-stakes use

### Discussion

* sanity check only는 overreliance / drift 위험이 큼.
* calibrated adjudication은 강하지만 cost가 든다.
* full blind dual review on all claims은 너무 비쌀 수 있다.

### Current Decision

**O2** 채택.
Tier C 이상에서 mandatory.

### Status

Accepted

---

## QOC 6 — 언제 검색을 멈출 것인가?

### Question

stop decision을 어떻게 정의할 것인가?

### Options

* **O1. 더 이상 새 논문이 안 나오면 stop**
* **O2. core claim coverage만 충족하면 stop**
* **O3. coverage-aware stopping rule**

### Criteria

* missed strongest opposition 방지
* operational clarity
* false stop risk
* cost control

### Discussion

* 새 논문이 안 나오는 건 search exhaustion일 뿐 coverage 보장은 아니다.
* core claim coverage만으로도 echo chamber를 놓칠 수 있다.
* coverage-aware stopping은 더 엄격하지만 현실적이다.

### Current Decision

**O3** 채택.

### Status

Accepted

---

## QOC 7 — tier 구조가 필요한가?

### Question

모든 질문에 full protocol을 적용할 것인가, tiered execution을 둘 것인가?

### Options

* **O1. one protocol for all**
* **O2. tiered execution (Fast / Standard / High-stakes / Publication-grade)**

### Criteria

* adoption cost
* repeatability
* high-stakes safety
* practicality

### Discussion

* one protocol for all은 명확하지만 실제론 너무 무거워진다.
* tiered execution은 adoption 가능성을 높인다.

### Current Decision

**O2** 채택.

### Status

Accepted

---

## QOC 8 — version governance를 workflow에 포함할 것인가?

### Question

preprint / journal / correction / retraction lifecycle을 protocol 안에 넣을 것인가?

### Options

* **O1. metadata 수준에서만 처리**
* **O2. manifestation-aware governance를 protocol 핵심에 포함**

### Criteria

* long-term correctness
* revalidation ability
* archive safety
* implementation complexity

### Discussion

* metadata-only는 가볍지만 superseded verdict 위험이 남는다.
* manifestation-aware governance는 복잡하지만 운영 시스템으로 가려면 필요하다.

### Current Decision

**O2** 채택.

### Status

Accepted

---

## QOC 9 — v0.4.1과 v1.2의 관계를 어떻게 정의할 것인가?

### Question

두 문서를 대체 관계로 볼 것인가, 병합 가능한 상보적 관계로 볼 것인가?

### Options

* **O1. v1.2가 더 최신이므로 v0.4.1 대체**
* **O2. v0.4.1이 더 grounded하므로 v1.2 폐기**
* **O3. 역할 분리 후 통합**

### Criteria

* evidence grounding
* operational clarity
* maintainability
* future extensibility

### Discussion

* v1.2는 execution이 강함
* v0.4.1은 evidence / architecture가 강함
* 둘은 서로 비워진 부분을 채운다.

### Current Decision

**O3** 채택.

### Status

Accepted

---

# 7. What To Merge Next

## v1.2 → v0.4.1로 가져올 것

1. Execution Tiers
2. Escalation Triggers
3. Coverage-aware Stopping Rule
4. Claim Triage
5. Expanded prompt library
6. Role interfaces (Searcher / Attacker / Judge 등)

## v0.4.1 → v1.2로 가져올 것

1. evidence base table
2. concrete case study
3. failure examples
4. three-tier technical view
5. reader ≠ auditor boundary
6. automation bias / overreliance warning
7. explicit “heuristic draft only” language where needed

---

# 8. Immediate Next Step

현재 단계에서 가장 중요한 건 더 많은 이론 섹션 추가가 아니라 **pilot**다.

## pilot 목적

* time per resolved claim 측정
* tier별 실제 사용성 측정
* strongest opposition miss rate 측정
* reviewer fatigue point 확인
* skipped-step frequency 기록
* search A/B overlap 측정

## 추천 pilot 질문 수

* 3개에서 5개

## 각 pilot에서 남길 로그

* chosen tier
* escalation 발생 여부
* claim 수
* triage shortlist 수
* time per claim
* time per run
* strongest opposition miss 여부
* coverage stop rationale
* reviewer disagreement 여부
* artifact conflict 여부

---

# 9. Current Final Position

현재까지의 최종 인식은 다음과 같다.

1. 단순 multi-AI cross-check는 오염과 correlated error를 키울 수 있다.
2. 검증 단위는 claim이어야 한다.
3. retrieval, contradiction analysis, scoring, governance를 분리해서 설계해야 한다.
4. human review는 calibrated subsystem이어야 한다.
5. v0.4.1과 v1.2는 경쟁이 아니라 상보적이다.
6. 다음 단계는 설계 철학 추가가 아니라 **pilot validation**이다.

---

# 10. One-line Summary

> 우리는 단순히 “AI가 논문을 잘 찾게” 하려는 것이 아니라,
> **claim가 source span, contradiction context, evidence strength, version state까지 추적 가능한 research verification + operations system**을 만들고 있다.
