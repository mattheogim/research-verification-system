# 연구 워크플로우 기록 + QOC

## 목적

이 문서는 지금까지 진행한 논의, 버전 변화, 핵심 판단, 남은 리스크를 **기록용**으로 남기기 위한 문서다.

특히 아래 두 문서를 어떻게 볼지, 무엇을 흡수할지, 다음에 무엇을 검증해야 할지를 명확히 남긴다.

* **v0.4.1** = 검증 아키텍처 / provenance-first verification spine
* **v1.2** = 운영 프로토콜 / multi-AI research operations manual

---

# 1. 현재 한 줄 상태

> **지금 상태는 “좋은 아이디어” 단계를 넘었고, “운영 가능한 강한 매뉴얼” 단계까지 왔다.**
> 다만 아직 남은 핵심 문제는 설계 자체보다 **운영 비용, scoring의 주관성, external gold truth, retrieval 독립성** 쪽에 있다.

---

# 2. 지금까지의 흐름 요약

## 2.1 초반 핵심 문제의식

처음 문제는 단순히 “어떤 AI가 논문조사에 더 좋냐”가 아니었다.
실제 핵심은 아래였다.

1. 여러 AI를 같이 쓰면 정말 더 좋아지는가
2. 서로의 답을 다시 다른 AI에게 넘기는 방식이 괜찮은가
3. 논문 탐색, 반증 찾기, claim 검증, human review를 어떻게 설계해야 하는가
4. 결국 믿을 수 있는 건 무엇이고, 무엇은 끝까지 의심해야 하는가

이 과정에서 다음 결론이 형성됐다.

* AI끼리 긴 문단을 전달하는 루프는 오염을 누적시킬 수 있다.
* 따라서 **같은 원자료를 독립적으로 읽게 하고**, 결과는 나중에 **claim 단위**로만 합치는 쪽이 더 낫다.
* “논문 단위 충돌”이 아니라 **claim 단위 충돌**을 봐야 한다.
* 검색, 반증, 판정, 버전 관리, human review drift는 서로 다른 문제다.

---

## 2.2 운영 매뉴얼 라인의 진화

### v1.0

초기 운영 매뉴얼은 좋은 구조를 가졌지만, 다음이 약했다.

* evaluation layer 부족
* reviewer calibration 부족
* coverage risk 부족
* stopping rule 약함
* 버전/manifestation 관리 부족

### v1.1

v1.1에서는 아래가 추가되며 크게 강화됐다.

* Evaluation Layer
* Reviewer Calibration Layer
* Coverage Risk Check
* baseline comparison 관점
* human inconsistency에 대한 대응

즉 “좋은 절차”에서 “검증 가능한 절차”로 이동했다.

### v1.2

v1.2에서는 운영성 중심 패치가 들어갔다.

* **Execution Tiers**
* **Escalation Triggers**
* **Coverage-aware Stopping Rule**
* **Claim Triage**
* **Evidence Scoring anchors + rationale + confidence**
* **raw-evidence-linked Blind Attack**
* **Artifact / Manifestation Governance**
* **tier별 Evaluation Layer**

결과적으로 v1.2는 “실제로 굴릴 수 있는 매뉴얼”에 가까워졌다.

---

## 2.3 v0.4.1 라인의 위치

v0.4.1은 운영 매뉴얼이라기보다, **검증 아키텍처의 spine** 역할을 한다.

강점은 다음과 같다.

* provenance-first 설계
* layered trust
* reader ≠ auditor 구분
* deterministic / specialized ML / open LLM의 3-tier 기술 구조
* case study 기반 실제 오류 예시
* evidence tables
* automation bias와 human overreliance 경고
* parser limitation을 명시적으로 인정
* unit of verification = claim

즉 v0.4.1은 “왜 이런 시스템이어야 하는가”를 강하게 설명하는 문서다.

---

# 3. 현재 최종 판단

## 3.1 v0.4.1과 v1.2의 관계

> **둘은 경쟁이 아니라 짝이다.**

더 정확히 쓰면:

* **v0.4.1** = provenance-first **verification architecture**
* **v1.2** = multi-AI assisted **research operations protocol**

즉,

* v0.4.1은 **spine**
* v1.2는 **workflow engine**

이라고 볼 수 있다.

### v1.2가 우리에게 주는 것

* Execution Tiers
* Escalation Triggers
* Coverage-aware Stopping Rule
* Claim Triage
* 확장된 Prompt Library
* Searcher / Normalizer / Attacker / Judge 역할 분리

### v0.4.1이 v1.2보다 강한 것

* 실제 오류 사례
* evidence table
* parser limitation recognition
* reader vs auditor boundary
* automation bias 명시
* three-tier technical structure
* stronger anti-overtrust stance

---

## 3.2 현재 전체 상태에 대한 압축 평가

### v0.4.1

* 좋은 설계 문서
* 근거가 강함
* 실제 실패 예시가 있음
* 운영 단계와 tiering은 약함

### v1.2

* 운영 가능성이 높음
* 절차가 강함
* tier / escalation / stopping / governance가 좋음
* retrieval 독립성, 비용, scoring 주관성, external gold truth 문제는 남음

### 통합 시 기대 모습

> **근거 있는 설계 + 실행 가능한 운영**

이 조합이 다음 버전의 핵심 방향이다.

---

# 4. 아직 남은 핵심 리스크

## 4.1 retrieval independence 문제

현재 v1.2의 Searcher A/B는 역할은 분리돼 있지만, 검색 전략의 독립성이 아직 약하다.
즉 실제론 같은 논문을 많이 찾아올 가능성이 있다.

필요한 수정:

* Searcher A = high-precision seed retrieval
* Searcher B = citation chasing / negative seed expansion / terminology variation / venue variation
* overlap이 높으면 strategy diversification

---

## 4.2 scoring은 usable하지만 measurement는 아님

v1.2의 scoring은 v0.4.1보다 운영적으로 낫다.
하지만 여전히 **structured judgment**이지, 진짜 measurement instrument는 아니다.

따라서 문서에 명확히 남겨야 할 문장:

> 이 점수는 calibrated measurement가 아니라 structured judgment다.

---

## 4.3 운영 비용 문제

18단계 전체 파이프라인은 강하지만 무겁다.
Tiering으로 완화했어도 실제로는 아래 문제가 남는다.

* Standard 이상부터 claim당 비용 증가
* calibration / evaluation / archive 생략 위험
* 사람이 실제로 다 안 돌릴 가능성

따라서 다음 단계는 실제 질문 3~5개에 pilot를 돌려서,
어디서 제일 많이 삐걱거리는지 보는 것이다.

---

## 4.4 external gold truth 문제

Evaluation Layer가 생겼지만,
여전히 “정답을 누가 고정하느냐” 문제는 완전히 해결되지 않는다.

따라서 Tier D에서 필요한 것:

* gold adjudicated claim set
* held-out challenge set
* baseline comparison
* external reviewer audit
* pre-registered success thresholds

---

## 4.5 pairwise judge는 남는 한계

close call 전용 + swap-order 2회는 맞는 방향이지만,
여전히 model-specific bias / rubric wording sensitivity는 남는다.
이건 구조적 결함이라기보다 잔여 리스크로 본다.

---

# 5. 현재까지의 핵심 의사결정 로그

## Decision 1

**문단 vs 문단 비교를 버리고 claim vs evidence 비교로 간다.**

이유:

* 긴 요약문 전달은 오염 누적 위험이 크다.
* contradiction는 논문 단위보다 claim 단위에서 더 정확하게 판단된다.

결과:

* claim canonicalization 필수
* claim matrix 필수
* contradiction/context analysis 필수

---

## Decision 2

**원자료를 그대로 유지하고, 얇은 공통 스키마만 맞춘다.**

이유:

* 논문 원문 전체를 동일 포맷으로 재작성할 필요는 없다.
* 중요한 건 raw evidence 보존과 비교 레이어 정규화다.

결과:

* raw evidence packet
* claim packet
* evidence snippet
* literal vs normalized 구분

---

## Decision 3

**judge는 마지막 close call에만 쓴다.**

이유:

* 초반 judge는 bias 위험이 크다.
* 먼저 pointwise verification과 contradiction/context analysis를 해야 한다.

결과:

* pointwise first
* pairwise later
* swap-order 2회
* tie 허용

---

## Decision 4

**Tier 기반 운영으로 간다.**

이유:

* 모든 질문에 full protocol을 강제하면 adoption cost가 너무 크다.
* 가벼운 질문과 고위험 질문을 같은 비용으로 다룰 필요가 없다.

결과:

* Tier A Fast
* Tier B Standard
* Tier C High-stakes
* Tier D Publication-grade

---

## Decision 5

**Stopping은 coverage-aware 해야 한다.**

이유:

* “더 못 찾음”과 “충분히 찾음”은 다르다.
* stopping rule만 있고 coverage gate가 없으면 coverage illusion이 생긴다.

결과:

* terminology variation coverage
* rebuttal/replication presence
* strongest opposition miss risk
* echo chamber ratio
* artifact version conflict
  를 함께 본다.

---

## Decision 6

**Artifact / Manifestation Governance를 별도 층으로 둔다.**

이유:

* preprint / journal / corrected / retracted를 같은 것으로 다루면 안 된다.
* 좋은 workflow도 오래된 verdict를 정교하게 보관하는 시스템이 될 수 있다.

결과:

* work_id
* manifestation_id
* verdict_id
* superseded status
* revalidation trigger

---

# 6. QOC (Question / Options / Criteria)

아래는 앞으로 계속 확장할 수 있는 QOC 기록이다.

---

## QOC 1 — v0.4.1과 v1.2의 관계를 어떻게 정의할 것인가

### Question

v0.4.1과 v1.2는 경쟁 문서인가, 보완 문서인가?

### Options

1. 둘 중 하나를 버리고 하나만 canonical로 삼는다.
2. v1.2를 상위 문서로 두고 v0.4.1을 appendix로 내린다.
3. v0.4.1을 설계 spine, v1.2를 운영 manual로 두고 상보적으로 운용한다.

### Criteria

* evidence richness
* operational usefulness
* long-term maintainability
* conceptual clarity

### Decision

**Option 3 채택**

### Why

* v0.4.1은 evidence와 boundary가 강하다.
* v1.2는 실행 절차와 tiering이 강하다.
* 둘을 합치는 것이 가장 합리적이다.

### Consequences

* 다음 버전은 통합 문서가 될 가능성이 높다.
* 중복 섹션 정리 필요
* 역할 충돌 정리 필요

---

## QOC 2 — verification unit은 paper인가 claim인가

### Question

검증의 기본 단위를 논문 전체로 볼 것인가, claim으로 볼 것인가?

### Options

1. paper-level verification
2. claim-level verification
3. paper-level + claim-level hybrid

### Criteria

* contradiction precision
* provenance traceability
* reviewer usability
* false contradiction 방지

### Decision

**Option 2를 기본으로, 필요 시 Option 3 보조**

### Why

* contradiction는 대부분 claim level에서 판단해야 정확하다.
* paper-level은 container이고, claim이 실제 unit이다.

### Consequences

* claim canonicalization 필수
* claim matrix 필수
* stronger support/opposition도 claim 기준

---

## QOC 3 — 여러 AI의 검색을 어떻게 독립적으로 만들 것인가

### Question

Independent Search A + B는 단순히 다른 AI를 쓰는 것으로 충분한가?

### Options

1. 다른 AI면 충분하다.
2. 같은 AI라도 검색 전략이 다르면 충분하다.
3. AI뿐 아니라 retrieval policy까지 다르게 설계해야 한다.

### Criteria

* overlap reduction
* recall diversity
* opposition discovery
* 운영 복잡도

### Decision

**Option 3 채택 예정**

### Why

* 다른 AI라도 실제로 같은 seed 논문을 많이 가져올 수 있다.
* 독립성은 모델이 아니라 retrieval policy 차이에서 더 많이 나온다.

### Consequences

* Searcher A/B 정의를 policy level로 수정해야 함
* overlap threshold / diversification trigger 추가 필요

---

## QOC 4 — evidence scoring은 어떤 성격으로 둘 것인가

### Question

Evidence scoring을 measurement처럼 다룰 것인가, structured judgment로 다룰 것인가?

### Options

1. numeric scoring = quasi-measurement
2. numeric scoring = heuristic only
3. anchor + rationale + confidence를 가진 structured judgment

### Criteria

* usability
* honesty about uncertainty
* calibration potential
* reviewer consistency

### Decision

**Option 3 채택**

### Why

* 숫자만 두면 가짜 정밀함이 생긴다.
* rationale/confidence를 같이 저장하면 더 정직하다.

### Consequences

* 모든 핵심 score에 rationale 필수
* 일부 핵심 score에 confidence 필수
* 문서에 “measurement 아님” 명시 필요

---

## QOC 5 — stopping은 어떻게 할 것인가

### Question

언제 논문 탐색을 멈출 것인가?

### Options

1. 새 논문이 안 나오면 멈춘다.
2. 핵심 claim마다 support/opposition 한 쌍이 생기면 멈춘다.
3. coverage-aware stopping gate를 통과했을 때만 멈춘다.

### Criteria

* missed opposition risk
* reviewer cost
* coverage illusion 방지
* practical usability

### Decision

**Option 3 채택**

### Why

* 단순 stop rule은 coverage illusion을 막지 못한다.
* terminology coverage, review/rebuttal presence, version conflict까지 봐야 한다.

### Consequences

* stop decision이 더 보수적이 됨
* 운영 비용 증가 가능
* Tier A/B에선 완화 규칙 필요

---

## QOC 6 — human review를 어떻게 볼 것인가

### Question

인간 최종 검토를 safety blanket로 볼 것인가, 별도 설계가 필요한 subsystem으로 볼 것인가?

### Options

1. human-in-the-loop면 충분하다.
2. reviewer calibration 없이도 괜찮다.
3. calibration, adjudication, drift control이 필요한 subsystem으로 본다.

### Criteria

* automation bias 방지
* reviewer consistency
* auditability
* realism

### Decision

**Option 3 채택**

### Why

* human review는 fallible하다.
* calibration / adjudication rule 없이는 drift가 생길 수 있다.

### Consequences

* Tier C 이상 calibration 필요
* adjudication form 필요
* gold-set / borderline casebook 필요

---

## QOC 7 — artifact version을 어떻게 관리할 것인가

### Question

preprint / journal / corrected / retracted를 같은 것으로 볼 것인가?

### Options

1. 동일 work면 하나로 본다.
2. manifestation을 분리하되 verdict는 공유한다.
3. work와 manifestation을 분리하고 verdict도 manifestation 단위로 연결한다.

### Criteria

* version safety
* provenance precision
* correction handling
* archive clarity

### Decision

**Option 3 채택**

### Why

* 같은 intellectual work라도 manifestation에 따라 claim wording, metric, caveat가 바뀔 수 있다.

### Consequences

* work_id / manifestation_id / verdict_id 필요
* revalidation trigger 필요
* superseded verdict 상태 필요

---

# 7. 다음 단계

## 바로 해야 할 것

1. v0.4.1에 다음을 흡수

   * Execution Tiers
   * Escalation Triggers
   * Coverage-aware Stopping Rule
   * Claim Triage
   * Prompt Library 확장

2. v1.2에 다음을 흡수

   * evidence tables
   * concrete failure cases
   * automation bias warnings
   * reader ≠ auditor boundary
   * parser limitation evidence

3. pilot 설계

   * 실제 질문 3~5개 선정
   * Tier A/B/C 각각 최소 1회 이상 실행
   * time per resolved claim 기록
   * miss rate / fake contradiction / reviewer fatigue 기록

---

## 중기 과제

* Search A/B retrieval policy 분리
* scoring measurement claim 방지 문구 강화
* external gold-set 운영 현실성 검토
* pairwise judge residual bias 로그 설계

---

# 8. 최종 메모

지금까지의 결론을 가장 짧게 적으면 이거다.

> **우리는 “논문조사를 잘하는 AI”를 만드는 쪽에서 출발했지만, 지금은 “실패 가능한 구성요소들 위에서 연구 검증을 어떻게 안전하게 운영할 것인가”를 설계하는 단계까지 왔다.**

그리고 현재 가장 중요한 판단은 아래 두 문장이다.

> **v0.4.1은 verification spine이다.**
> **v1.2는 operations engine이다.**

둘을 합치면 다음 버전은 단순 patch가 아니라,
**근거 있는 설계 + 운영 가능한 워크플로우 + 버전 안전한 검증 시스템**으로 갈 수 있다.
