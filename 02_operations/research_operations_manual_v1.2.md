# Research Workflow Manual v1.2

## 목적
이 문서는 **여러 AI가 서로의 긴 요약문을 끝없이 평가하는 구조**를 피하고, **같은 원자료를 독립적으로 읽고, claim 단위로 검증하고, 반증·누락·버전 리스크까지 관리하는 구조**를 운영하기 위한 실전 매뉴얼이다.

이 버전은 v1.1의 뼈대 위에 다음을 추가·수정했다.
- `Execution Tiers`
- `Escalation Triggers`
- `Coverage-aware Stopping Rule`
- `Blind Attack`의 raw-evidence-linked mode
- `Evidence Scoring`의 0/1/2 anchor + rationale + confidence
- `Claim Triage`
- tier별 `Evaluation Layer`
- `Artifact / Manifestation Governance`

---

# 목차

0. Execution Tiers
1. Escalation Triggers
2. 운영 원칙
3. 전체 파이프라인 개요
4. 준비물
5. Step 0 — Question Lock
6. Step 1 — Raw Evidence Packet 만들기
7. Step 2 — Independent Search A
8. Step 3 — Independent Search B
9. Step 4 — Evidence Pool Expansion
10. Step 5 — De-dup + Independence Clustering
11. Step 6 — Claim Canonicalization
12. Step 7 — Claim Matrix 작성
13. Step 8 — Evidence Scoring
14. Step 9 — Contradiction / Context Analysis
15. Step 10 — Coverage-aware Stopping Rule
16. Step 11 — Claim Triage
17. Step 12 — Blind Attack
18. Step 13 — Pointwise Verification
19. Step 14 — Reviewer Calibration / Adjudication
20. Step 15 — Pairwise Judge for Close Calls Only
21. Step 16 — Evaluation Layer
22. Step 17 — Final Decision Memo
23. Step 18 — Archive / Artifact Governance
24. 절대 하지 말아야 할 것
25. 초압축 버전
26. 프롬프트 라이브러리

---

# 0. Execution Tiers

이 매뉴얼은 모든 질문에 full protocol을 강제하지 않는다.
질문의 중요도, 비용, 실패 리스크에 따라 먼저 실행 등급을 고른다.

## Tier A — Fast
### 대상
- 빠른 탐색
- 저위험 질문
- 초기 아이디어 정리
- 내부 메모 초안

### 필수 단계
- Step 0 — Question Lock
- Step 2 — Independent Search A
- Step 3 — Independent Search B 또는 생략
- Step 6 — Claim Canonicalization
- Step 7 — Claim Matrix
- Step 11 — Claim Triage
- Step 12 — Blind Attack
- Step 17 — Final Decision Memo

### 생략 가능
- Evidence Scoring
- Reviewer Calibration
- Pairwise Judge
- Full Archive
- External evaluation

### 산출물
- 짧은 claim matrix
- 주요 반증 후보
- 가벼운 final memo

---

## Tier B — Standard
### 대상
- 일반 연구 질문
- related work 비교
- 반증 탐색이 중요한 경우
- 팀 내부 공유용 분석

### 필수 단계
- Tier A 전부
- Step 8 — Evidence Scoring
- Step 9 — Contradiction / Context Analysis
- Step 10 — Coverage-aware Stopping Rule
- Step 13 — Pointwise Verification
- Step 16 — Lightweight Evaluation

### 산출물
- score가 붙은 claim matrix
- contradiction/context 분석
- lightweight evaluation log

---

## Tier C — High-stakes
### 대상
- 중요한 의사결정
- 민감한 연구 결론
- 외부 공유 가능성이 있는 문서
- 팀 정책/전략에 영향이 있는 경우

### 필수 단계
- Tier B 전부
- Step 14 — Reviewer Calibration / Adjudication
- Step 15 — Pairwise Judge for close calls only
- Step 18 — Archive / Artifact Governance
- Step 16 — Structured Evaluation

### 산출물
- calibration log
- adjudication log
- structured evaluation
- version-aware archive

---

## Tier D — Publication-grade
### 대상
- 외부 제출물
- 논문/보고서/장기 보존 프로젝트
- 프로토콜 자체 성능 비교 실험
- high-consequence governance

### 필수 단계
- Tier C 전부
- Step 16 — Full Evaluation
- external gold set
- held-out challenge set
- baseline comparison
- pre-registered success thresholds
- post-hoc external audit

### 산출물
- external evaluation report
- benchmark comparison
- full governance manifest

---

# 1. Escalation Triggers

아래 중 하나라도 발생하면 상위 tier로 승격한다.

## 기본 승격 트리거
- direct contradiction 발견
- strongest opposition missing 가능성 높음
- reviewer disagreement가 지속됨
- coverage risk가 medium 이상
- artifact version conflict 발생
- external sharing 예정
- 팀 의사결정에 직접 사용 예정
- legal / medical / financial implication 존재

## 승격 규칙
- Tier A에서 trigger 발생 → 최소 Tier B로 승격
- Tier B에서 trigger 발생 → 최소 Tier C로 승격
- Tier C에서 trigger 발생 → Tier D 여부 검토

## Tier D 승격 조건
- 외부 제출물
- formal benchmarking 필요
- external gold evaluation 필요
- retraction/correction/version conflict가 중요함

---

# 2. 운영 원칙

## 원칙 1: 원자료는 그대로 둔다
논문 PDF, abstract, figure, 표, 발췌문, note, DOI/URL, venue 정보는 **원문 그대로** 유지한다.
모든 자료를 같은 문서 포맷으로 재작성할 필요는 없다.

## 원칙 2: 비교는 얇은 공통 스키마에서만 한다
같게 만들어야 하는 건 논문 원문이 아니라 **추출 레이어**다.
즉, 각 source에서 아래 정보만 공통 스키마로 맞춘다.

```text
Source ID
Title
Year
DOI / URL
Study type
Population / dataset
Metric
Claim snippet
Evidence snippet
Limitation snippet
```

## 원칙 3: AI끼리 긴 문단을 전달하지 않는다
금지:
`A가 이렇게 말했어 → B 너 생각은?`

허용:
- 같은 raw evidence packet을 서로 다른 AI에 독립적으로 입력
- 결과는 나중에 claim matrix에서만 합침

## 원칙 4: judge는 마지막 close call에만 쓴다
judge를 초반에 쓰면 style bias, order bias, framing bias를 더 많이 탈 수 있다.
먼저 claim을 자르고, evidence를 붙이고, 반증을 찾고, 점검한 뒤에만 judge를 쓴다.

## 원칙 5: 절차가 많다고 성능이 좋아진 것은 아니다
프로토콜의 정교함과 프로토콜의 효율은 다르다.
따라서 tier, evaluation, escalation, stopping이 반드시 필요하다.

## 원칙 6: version을 관리하지 않으면 정교한 오류를 보관하게 된다
preprint, conference, journal, corrected, erratum, retracted, superseded를 구분하지 않으면,
좋은 workflow가 오래된 verdict를 정교하게 보존하는 시스템이 될 수 있다.

---

# 3. 전체 파이프라인 개요

```text
Execution Tier 선택
→ Escalation Trigger 확인
→ Question Lock
→ Raw Evidence Packet
→ Independent Search A
→ Independent Search B
→ Evidence Pool Expansion
→ De-dup / Independence Clustering
→ Claim Canonicalization
→ Claim Matrix
→ Evidence Scoring
→ Contradiction / Context Analysis
→ Coverage-aware Stopping Rule
→ Claim Triage
→ Blind Attack
→ Pointwise Verification
→ Reviewer Calibration / Adjudication
→ Pairwise Judge for close calls only
→ Evaluation Layer
→ Final Decision Memo
→ Archive / Artifact Governance
```

---

# 4. 준비물

## 4-1. 필수 역할 인터페이스

- **Searcher A**: 빠른 academic retrieval 가능 도구
- **Searcher B**: deep research / long-form synthesis 가능 도구
- **Normalizer**: claim matrix 생성 가능 도구
- **Attacker**: raw evidence 대조형 비판이 가능한 도구
- **Judge**: blind pairwise / pointwise 판정이 가능한 도구
- **Closed-corpus verifier**: 업로드 논문 묶음 안에서 근거 추적 가능한 도구

## 4-2. 현재 예시 조합
- Searcher A: Perplexity Ask/Search
- Searcher B: Perplexity Research 또는 ChatGPT Deep Research
- Normalizer: ChatGPT 또는 Claude
- Attacker: Claude
- Judge: ChatGPT 또는 Gemini
- Closed-corpus verifier: PaperQA

## 4-3. 권장 폴더 구조

```text
/project-name/
  00_question_lock.md
  01_raw_sources/
  02_seed_papers/
  03_evidence_pool/
  04_claim_packets/
  05_claim_matrix/
  06_scores/
  07_attacks/
  08_verification/
  09_evaluation/
  10_final_memo/
  11_archive/
  12_manifest/
```

## 4-4. 권장 데이터 객체
- `question_lock`
- `raw_evidence_packet`
- `claim_packet`
- `claim_matrix`
- `score_sheet`
- `attack_log`
- `verification_log`
- `evaluation_log`
- `artifact_manifest`

---

# 5. Step 0 — Question Lock

## 목적
AI마다 질문을 다르게 해석하는 걸 막는다.

## 입력
- 실제 연구 질문 1개

## 출력
- 고정된 질문 정의서 1장

## 반드시 고정할 것
1. one-sentence question
2. inclusion criteria
3. exclusion criteria
4. what counts as contradiction
5. what counts as only a scope difference
6. final deliverable format

## 실패 신호
- 질문 문장이 2개 이상으로 갈라짐
- contradiction 정의가 없음
- scope difference 정의가 없음
- deliverable이 불명확함

---

# 6. Step 1 — Raw Evidence Packet 만들기

## 목적
각 AI에게 같은 원자료를 주기 위한 공통 입력 packet을 만든다.

## 입력
- 논문 PDF
- abstract
- figure/table screenshot
- DOI / arXiv / venue 링크
- 네 메모
- correction / erratum / retraction 정보가 있으면 함께 포함

## 출력
- evidence packet 묶음

## packet 스키마
```text
Packet ID:
Source type: paper / review / benchmark / rebuttal / replication / note
Title:
Year:
Authors:
Venue:
DOI / URL:
Artifact status: preprint / conference / journal / corrected / erratum / retracted / superseded
Abstract:
Key figure/table note:
Claim snippet:
Evidence snippet:
Known limitation snippet:
Manifestation ID:
Prior manifestation ID:
Snapshot date:
```

## 규칙
- 원자료는 수정하지 않는다.
- snippet은 추출 레이어일 뿐 canonical artifact가 아니다.
- artifact status를 반드시 적는다.

---

# 7. Step 2 — Independent Search A

## 목적
빠르게 seed paper를 잡는다.

## 도구
- Searcher A

## 출력
- primary papers 5–8개
- review/survey 2–4개
- rebuttal / replication / benchmark 2–4개
- weakening / qualifying papers 2–4개

## 규칙
- 여기선 수집만 한다.
- supportive literature만 모이면 실패다.
- review / rebuttal / replication이 없으면 추가 검색 필요.

---

# 8. Step 3 — Independent Search B

## 목적
한 번 깊게 파서 landscape를 만든다.

## 도구
- Searcher B

## 출력
- supporting cluster
- contradicting cluster
- qualifying cluster
- unresolved disputes list

## 규칙
- 너무 많은 synthesis tool을 초반부터 중첩하지 않는다.
- provenance가 흐려지지 않게 raw source link를 유지한다.

---

# 9. Step 4 — Evidence Pool Expansion

## 목적
처음 찾은 seed papers 주변을 체계적으로 확장한다.

## 확장 방식
1. seed papers
2. positive seed expansion
3. negative seed expansion
4. backward snowballing
5. forward snowballing
6. review / benchmark / replication 우선 확장
7. terminology variation search
8. venue variation search

## 규칙
- citation count만 보고 강한 논문으로 간주하지 않는다.
- jargon variation이 큰 주제는 terminology variation search를 반드시 수행한다.
- review/rebuttal/replication/benchmark가 evidence pool에 충분히 들어와야 한다.

---

# 10. Step 5 — De-dup + Independence Clustering

## 목적
같은 연구 라인 논문 여러 편을 독립 증거처럼 두 번 세지 않게 한다.

## 클러스터 기준
- same author group
- same lab / collaboration line
- same benchmark family
- same dataset family
- same study reported in multiple papers
- same work, different manifestation

## 출력
- independence cluster가 표시된 evidence pool

## 규칙
- strong evidence는 cluster 단위로 센다.
- 같은 study의 multiple reports는 한 묶음으로 다룬다.
- work-level 중복과 manifestation-level 중복을 구분한다.

---

# 11. Step 6 — Claim Canonicalization

## 목적
“논문 단위 충돌”이 아니라 “claim 단위 충돌”로 바꾼다.

## canonical fields
1. subject
2. outcome
3. metric
4. dataset / population
5. time period
6. definition / threshold

## 규칙
- UNKNOWN을 허용한다.
- 무리한 추론으로 빈칸을 채우지 않는다.
- canonical claim은 최대한 비교 가능해야 한다.

## 출력
```text
Claim ID:
subject:
outcome:
metric:
dataset/population:
time period:
definition/threshold:
```

---

# 12. Step 7 — Claim Matrix 작성

## 목적
자유서술을 비교 가능한 검증 단위로 바꾼다.

## 출력 형식
```text
Claim ID:
Canonical claim:
Type: factual / interpretation / methodological
Support status: supported / contradicted / qualified / unclear
Supporting sources:
Contradicting sources:
Scope conditions:
Evidence gaps:
What would change the verdict:
```

## 규칙
- atomic claim만 허용
- source 없는 claim 금지
- scope 조건 없는 contradiction 금지
- interpretation claim과 factual claim을 섞지 말 것

---

# 13. Step 8 — Evidence Scoring

## 목적
“가장 유명한 논문”이 아니라 **현재 claim에 가장 직접적이고 독립적인 증거**를 고른다.

## scoring output 형식
각 핵심 축은 아래 3개를 함께 저장한다.

```text
metric_name_score:
metric_name_rationale:
metric_name_confidence:
```

예:
```text
directness_score: 1
directness_rationale: proxy outcome only, not exact target metric
directness_confidence: medium
```

## 필수 점수축
1. directness
2. independence
3. study type strength
4. replication / benchmark / review value
5. recency
6. claim specificity
7. methodological quality
8. limitations transparency

## scoring anchors

### 1. directness
- 0 = claim을 직접 다루지 않음
- 1 = 관련은 있으나 proxy outcome 또는 부분 조건만 다룸
- 2 = 동일 subject/outcome/metric/population을 직접 검증함

### 2. independence
- 0 = 같은 study 또는 같은 evidence family의 반복 보고
- 1 = 부분적으로만 독립
- 2 = 저자군, 데이터셋 family, benchmark line이 실질적으로 독립

### 3. study type strength
- 0 = 의견성 글, 비체계적 서술, 약한 실험
- 1 = 단일 실험 논문
- 2 = systematic review / benchmark / replication / rebuttal / meta-analysis

### 4. replication / benchmark / review value
- 0 = 해당 없음
- 1 = 간접적으로 관련
- 2 = claim 판단에 직접적으로 중요한 replication / benchmark / review

### 5. recency
- 0 = 최신 evidence를 반영하지 못할 가능성이 큼
- 1 = 중간
- 2 = 현재 claim 기준 충분히 최신

### 6. claim specificity
- 0 = broad topic relevance만 있음
- 1 = claim 일부만 맞음
- 2 = canonical claim과 정확히 일치

### 7. methodological quality
- 0 = 설계/평가/통제의 약점이 큼
- 1 = 보통
- 2 = 설계와 한계 보고가 강함

### 8. limitations transparency
- 0 = 한계 언급 거의 없음
- 1 = 한계 일부 언급
- 2 = 한계와 failure mode를 명시적으로 보고

## 규칙
- 모든 score에 rationale을 붙인다.
- 핵심 4개 축은 confidence도 필수다:
  - directness
  - independence
  - claim specificity
  - methodological quality
- 숫자를 진실처럼 다루지 않는다.
- score는 정리된 판단이지, 측정 장치가 아니다.

---

# 14. Step 9 — Contradiction / Context Analysis

## 목적
“진짜 반증”과 “가짜 반증”을 구분한다.

## conflict taxonomy
- direct contradiction
- scope mismatch
- metric mismatch
- dataset mismatch
- time-period mismatch
- different definition
- annotation / labeling mismatch
- methodological quality mismatch

## 산출물
각 claim마다 아래를 남긴다.
```text
Conflict type:
Real contradiction or only apparent:
Differing context variables:
Hidden assumption in current matrix:
Would conclusion change if context were aligned?:
One-sentence verdict:
```

## 규칙
- contradiction처럼 보이는 것의 상당수는 context mismatch일 수 있다.
- score가 높다고 contradiction이 자동으로 “진짜”가 되는 건 아니다.
- context variables를 먼저 맞춘 뒤 판단한다.

---

# 15. Step 10 — Coverage-aware Stopping Rule

## 목적
끝없이 더 찾지 않되, 단순히 “더 못 찾는 상태”를 “충분히 찾은 상태”로 착각하지 않게 한다.

## stop only if
1. 최근 2라운드 확장에서 새 독립 cluster가 거의 안 나옴
2. 핵심 claim별로 support 1개 + contradiction/qualification 1개 확보
3. 새로 추가되는 논문이 결론을 바꾸지 않고 same-family evidence만 더함
4. terminology variation coverage가 low가 아님
5. review / rebuttal / replication coverage가 존재함
6. strongest opposition miss risk가 low임
7. same-family echo chamber ratio가 허용 범위 내임

## coverage gate indicators
- seed family diversity: low / medium / high
- venue diversity: low / medium / high
- terminology variation coverage: low / medium / high
- rebuttal/replication presence: yes / no
- review coverage: yes / no
- same-family echo chamber ratio: %
- strongest opposition miss risk: low / medium / high

## stop 금지 조건
아래 중 하나라도 true면 stop 금지:
- terminology variation coverage = low
- review or rebuttal or replication 없음
- strongest opposition miss risk = medium 이상
- same-family echo chamber ratio 높음
- artifact version conflict unresolved

---

# 16. Step 11 — Claim Triage

## 목적
Blind Attack 전에 어떤 claim을 우선 공격할지 고른다.

## 왜 필요한가
모든 claim을 동일 강도로 공격하면 attacker overload가 생길 수 있다.

## triage ranking factors
- uncertainty
- impact
- disagreement
- coverage risk
- verdict fragility
- missing strongest opposition risk
- version conflict risk

## 운영 규칙
- high-impact claim은 shortlist에 무조건 포함
- unclear claim은 우선순위 상승
- same-family evidence만 있는 claim은 우선순위 상승
- 일반적으로 상위 3~7개 claim만 Blind Attack 대상으로 삼음
- high-stakes 이상에서는 shortlist 선정 이유를 기록

## 출력
```text
Triage shortlist:
- Claim ID
- priority reason
- attack priority: high / medium / low
```

---

# 17. Step 12 — Blind Attack

## 목적
현재 matrix의 과장, 숨은 가정, 누락된 반증, citation distortion을 공격한다.

## 입력
- current claim matrix
- linked raw evidence packets
- exact cited spans
- strongest support / strongest opposition candidates
- triage shortlist

## 규칙
- 공격은 1라운드만
- 예쁜 요약 금지
- claim matrix만 보고 citation distortion을 단정하지 말 것
- 반드시 raw evidence packet 또는 cited span을 근거로 삼을 것
- shortlist 없는 전체 무차별 공격 금지

## 출력 형식
```text
Attack ID:
Target Claim ID:
Raw packet ID:
Cited span used:
Attack type:
Why the matrix is wrong or fragile:
Estimated verdict impact: low / medium / high
Suggested next check:
```

## 필수 공격 종류
- overclaim
- hidden assumption
- duplicated non-independent evidence
- citation distortion
- fake contradiction caused by context mismatch
- stronger missing opposition

---

# 18. Step 13 — Pointwise Verification

## 목적
judge에 가기 전에 claim 하나씩 개별 검증한다.

## 입력
- Claim ID
- canonical claim
- supporting evidence
- opposing evidence
- context variables
- evidence scores
- relevant attacks

## 출력
```text
Current verdict:
Strongest reason for the verdict:
Main uncertainty:
Evidence that could flip the verdict:
Reviewer note:
```

## 규칙
- pairwise 전에 pointwise를 먼저 한다.
- unclear이면 이유를 명시한다.
- evidence가 mixed면 mixed라고 적는다.

---

# 19. Step 14 — Reviewer Calibration / Adjudication

## 목적
human review의 drift와 inconsistency를 줄인다.

## 필수 산출물
- gold-set claims 10개 이상
- borderline casebook
- adjudication rule
- calibration log

## gold-set 구성
각 claim은 최소 아래 라벨 중 하나를 포함한다.
- supported
- contradicted
- qualified
- unclear

## calibration 절차
1. reviewer가 gold-set을 독립 판정
2. disagreement 패턴 기록
3. taxonomy 오해 교정
4. borderline examples를 casebook에 추가
5. threshold agreement 도달 전 실제 review 금지

## 운영 규칙
- Tier C 이상에서는 calibration 없이 human adjudication 금지
- disagreement는 자유 토론으로만 풀지 말고, rulebook + adjudication form으로 푼다
- calibration examples와 실제 평가셋이 지나치게 겹치지 않게 한다

## adjudication form 최소 항목
```text
Claim ID:
Initial reviewer labels:
Why disagreement happened:
Rule applied:
Final adjudicated label:
Need to update casebook?: yes / no
```

---

# 20. Step 15 — Pairwise Judge for Close Calls Only

## 목적
정말 애매한 claim만 A/B 두 버전 중 어느 쪽이 더 나은지 본다.

## 사용 조건
- pointwise verdict가 unclear
- attack 이후도 결론이 안 선다
- two candidate summaries 둘 다 plausible

## 규칙
- close call에만 사용
- swap-order 2회는 기본
- 결과가 갈리면 Tie
- Tie면 pointwise verdict와 adjudication note를 우선

## 출력
```text
Winner: A / B / Tie
Reason:
Biggest weakness in A:
Biggest weakness in B:
```

---

# 21. Step 16 — Evaluation Layer

## 목적
이 프로토콜이 baseline보다 실제로 더 나은지 확인한다.

## 16A. Tier별 evaluation 강도

### Tier B — Lightweight Evaluation
필수 지표:
- strongest opposing paper miss risk
- fake contradiction count
- time per resolved claim

### Tier C — Structured Evaluation
필수 지표:
- Tier B 전부
- reviewer agreement
- verdict stability across reruns
- baseline 하나와 비교

### Tier D — Full Evaluation
필수 지표:
- Tier C 전부
- gold-set accuracy
- held-out claim accuracy
- post-hoc external audit pass rate
- baseline comparison multiple variants
- pre-registered thresholds

## 16B. baseline 후보
- simple search + summary
- search + claim matrix only
- search + contradiction pass only
- search + matrix + pointwise only

## 16C. primary metrics
- strongest opposing paper miss rate
- fake contradiction rate
- verdict stability across reruns
- reviewer agreement
- time per resolved claim
- same-family echo chamber ratio

## 16D. external metrics
- gold-set accuracy
- held-out claim accuracy
- outside-the-protocol benchmark performance
- external reviewer audit

## 16E. success criteria
프로젝트 시작 전에 고정:
- baseline 대비 miss rate 감소 목표
- fake contradiction 감소 목표
- stability 유지 또는 개선
- time cost upper bound

## 16F. External Gold Evaluation Policy
반드시 아래 중 최소 2개를 사용:
- gold adjudicated claim set
- blind held-out claims
- outside-the-protocol benchmark set
- external reviewer audit

## 금지
아래만으로 protocol superiority를 결론내지 말 것:
- same taxonomy
- same calibration examples
- same reviewers
- same source bundle
- same internal adjudication logic

## 규칙
- internal agreement만으로 성공 선언 금지
- Tier D에서는 pre-registered thresholds 없이 superiority 선언 금지

---

# 22. Step 17 — Final Decision Memo

## 목적
길고 혼란스러운 대화를 끝내고, 결론을 한 장으로 잠근다.

## 출력 구조
```text
## Final answer
## Strongest supporting evidence
## Strongest contradicting or qualifying evidence
## What is actually settled
## What is still uncertain
## Coverage risk
## Calibration status
## Artifact/version status
## What would most likely change the conclusion
## Confidence: Low / Medium / High
```

## 규칙
- do not invent certainty
- if evidence is mixed, say mixed
- do not hide contradictions
- state whether calibration was performed
- state whether active verdict is tied to latest manifestation
- under 500 words

---

# 23. Step 18 — Archive / Artifact Governance

## 목적
문서 객체의 lifecycle을 추적하고 superseded verdict를 관리한다.

## 핵심 개념
- `work_id`: 같은 intellectual work를 묶는 ID
- `manifestation_id`: preprint / conference / journal / corrected / retracted 등 개별 버전 ID
- `verdict_id`: 특정 manifestation에 대해 내려진 판정 ID

## 상태값
- preprint
- conference
- journal
- corrected
- erratum
- retracted
- superseded

## 필수 기록
- artifact hash
- source snapshot date
- parser version
- manifestation type
- linked prior manifestation
- whether current verdict is superseded

## revalidation triggers
아래 중 하나면 재검증:
- newer manifestation 등장
- correction / erratum 공지
- retraction 발생
- parser change로 cited span 재구성 필요
- stronger opposing paper 발견
- DOI merge / metadata conflict 발생

## 규칙
- strongest evidence는 manifestation 기준으로 연결할 것
- superseded manifestation의 verdict는 active verdict로 쓰지 말 것
- work-level claim과 manifestation-level verdict를 구분할 것

## archive output 예시
```text
work_id:
manifestation_id:
verdict_id:
artifact_status:
source_snapshot:
artifact_hash:
linked_prior_manifestation:
active_or_superseded:
revalidation_required: yes / no
```

---

# 24. 절대 하지 말아야 할 것

1. AI가 쓴 긴 요약문을 다른 AI에게 그대로 넘기기
2. supportive literature만 모으기
3. citation count 큰 논문을 strongest evidence로 착각하기
4. 같은 author/dataset family 논문을 독립 증거처럼 세기
5. judge를 맨 앞에 쓰기
6. 토론 라운드를 길게 늘리기
7. stopping rule 없이 끝없이 확장하기
8. raw evidence 없이 citation distortion을 판정하기
9. score만 저장하고 rationale/confidence를 생략하기
10. preprint verdict를 최신 journal/correction 등장 후에도 그대로 active verdict로 쓰기

---

# 25. 초압축 버전

1. Tier 선택
2. Escalation trigger 확인
3. Question Lock
4. Search A/B
5. Claim Canonicalization
6. Claim Matrix
7. Evidence Scoring
8. Coverage-aware Stopping
9. Claim Triage
10. Blind Attack
11. Pointwise Verification
12. 필요시 Calibration / Pairwise Judge
13. Tier별 Evaluation
14. Final Memo
15. Archive / Artifact Governance

---

# 26. 프롬프트 라이브러리

## A. Question Lock
```text
I want a strict research question lock.

Research question:
{질문}

Output exactly:
1. One-sentence question
2. Inclusion criteria
3. Exclusion criteria
4. What counts as contradiction
5. What counts as only a scope difference
6. Final deliverable format

Do not answer the question yet.
```

## B. Seed Search
```text
Search only. Do not synthesize yet.

Question:
{질문}

Find:
- 5 to 8 primary papers
- 2 to 4 review/survey papers
- 2 to 4 rebuttals, replication studies, or benchmark papers
- 2 to 4 papers that weaken or qualify the main claim

For each item give:
- title
- year
- why it matters
- type
- direct link
```

## C. Deep Research
```text
Do a deep research pass on this question.

Question:
{질문}

Requirements:
- separate support vs contradiction vs qualification
- identify review / benchmark / rebuttal / replication
- state weak or missing evidence
- do not collapse into one conclusion too early
- end with unresolved disputes
```

## D. Claim Canonicalization
```text
Canonicalize each target claim into:
- subject
- outcome
- metric
- dataset/population
- time period
- definition/threshold

If a field is missing, write UNKNOWN.
Do not infer aggressively.
```

## E. Claim Matrix
```text
Convert the materials into a claim matrix.

Rules:
- atomic claims only
- merge duplicates
- separate factual vs interpretation claims
- attach exact sources
- use QUALIFIED instead of CONTRADICTED when only context differs

Schema:
Claim ID:
Canonical claim:
Type:
Status:
Supporting sources:
Contradicting sources:
Scope conditions:
Evidence gaps:
What would change the verdict:
```

## F. Evidence Scoring
```text
Score each evidence source on:
- directness
- independence
- study type strength
- replication/benchmark/review value
- recency
- claim specificity
- methodological quality
- limitations transparency

For each score return:
- score
- rationale
- confidence

Then rank the evidence for this claim.
```

## G. Contradiction Analysis
```text
For each claim, compare the strongest support and strongest opposition.

Return:
- conflict type
- whether contradiction is real or only apparent
- which context variables differ
- whether the current matrix overclaims
- one-sentence verdict
```

## H. Coverage-aware Stopping
```text
Assess whether this claim set is ready to stop.

Check:
- new independent cluster yield
- support/contradiction coverage per core claim
- terminology variation coverage
- review/rebuttal/replication presence
- strongest opposition miss risk
- same-family echo chamber ratio
- artifact/version conflicts

Return:
- stop / continue
- stop rationale
- unresolved coverage risks
```

## I. Claim Triage
```text
Rank claims for attack priority.

Use these factors:
- uncertainty
- impact
- disagreement
- coverage risk
- verdict fragility
- strongest opposition miss risk
- version conflict risk

Return top 3 to 7 claims with reasons.
```

## J. Blind Attack
```text
You are not allowed to rewrite nicely.
You are auditing the claim matrix against the linked raw evidence.

Question:
{질문}

Current claim matrix:
{CLAIM_MATRIX}

Linked raw evidence packets:
{RAW_EVIDENCE_PACKETS}

Exact cited spans:
{CITED_SPANS}

Attack shortlist:
{TRIAGE_SHORTLIST}

Tasks:
- find overclaims
- find hidden assumptions
- find duplicated non-independent evidence
- find citation distortion by comparing matrix claims against cited raw spans
- find fake contradictions caused by context mismatch
- find stronger missing opposition

Output only:
- Attack 1
- Attack 2
- Attack 3

Each attack must include:
- target Claim ID
- raw packet ID
- cited span used
- why the matrix is wrong or fragile
- estimated verdict impact: low / medium / high
- suggested next check
```

## K. Pointwise Verification
```text
Evaluate this single claim pointwise.

Return:
- current verdict
- strongest reason for the verdict
- main uncertainty
- evidence that could flip the verdict
- reviewer note
```

## L. Reviewer Calibration
```text
Use this gold-set to calibrate reviewers.

For each claim:
- assign label
- explain why
- note which rule was hard to apply

Then summarize:
- disagreement patterns
- taxonomy confusions
- borderline cases to add to casebook
```

## M. Pairwise Judge
```text
You are a blind judge.

Rubric:
- factual support
- contradictory evidence handling
- scope control
- methodological caution
- citation reliability

Candidate A:
{A}

Candidate B:
{B}

Return exactly:
Winner: A / B / Tie
Reason:
Biggest weakness in A:
Biggest weakness in B:
```

## N. Evaluation Layer
```text
Compare this protocol run against the baseline.

Return:
- strongest opposing paper miss rate
- fake contradiction rate
- verdict stability
- reviewer agreement
- time per resolved claim
- same-family echo chamber ratio
- gold-set accuracy if available
- held-out accuracy if available
- whether success thresholds were met
```

## O. Final Memo
```text
Write a final decision memo.

Use exactly:
## Final answer
## Strongest supporting evidence
## Strongest contradicting or qualifying evidence
## What is actually settled
## What is still uncertain
## Coverage risk
## Calibration status
## Artifact/version status
## What would most likely change the conclusion
## Confidence: Low / Medium / High

Rules:
- do not invent certainty
- if mixed, say mixed
- do not hide contradictions
- state whether calibration was performed
- state whether active verdict is tied to latest manifestation
- under 500 words
```

---

# 한 줄 요약

**같은 원자료를 독립적으로 읽게 하고, claim을 canonical form으로 자르고, evidence를 점수화하되 rationale과 confidence를 남기고, coverage-aware stopping과 claim triage를 거친 뒤, raw-evidence-linked attack과 pointwise verification을 수행하고, calibration·evaluation·artifact governance를 상황에 맞게 계층적으로 적용하는 것.**
