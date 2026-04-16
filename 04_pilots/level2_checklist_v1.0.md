# Level 2 Decision Rules — v1.0

_Created: 2026-04-16 (Phase 1)_
_Status: DRAFT — calibration 후 freeze_

---

## 1. Decision Tree

입력: (claim text, source full text)
출력: SUPPORT / PARTIAL-MAJOR / PARTIAL-MINOR / REFUTE / UNCERTAIN

```
Step 1. 원문에 claim과 관련된 내용이 있는가?
  │
  ├── 원문 접근 불가 → UNCERTAIN (Access_Status = inaccessible)
  │
  ├── 원문에 claim 주제와 관련 내용 없음
  │     └── claim이 원문의 finding을 반박하는가?
  │           ├── YES → REFUTE
  │           └── NO → UNCERTAIN ("source does not address this claim")
  │
  └── 원문에 관련 내용 있음 →
      │
      Step 2. claim이 원문의 핵심 내용을 정확히 반영하는가?
        │
        ├── YES: 범위, 조건, 한정어, 수치, 인과 관계 모두 보존
        │     └── SUPPORT
        │
        └── NO: 하나 이상 차이 있음 →
            │
            Step 3. 그 차이가 claim의 핵심 주장을 바꾸는가? (Materiality Test 적용)
              │
              ├── NO: cosmetic difference
              │     └── SUPPORT
              │     예: "약 90%" → "90%", "LLMs" → "Large Language Models"
              │
              └── YES: material difference →
                  │
                  Step 4. 원문이 claim의 핵심 개념을 명시적으로 다루는가?
                    │
                    ├── NO: 원문에 해당 개념이 없는데 citing document가 귀속함
                    │     └── PARTIAL-MAJOR (attribution gap)
                    │     예: 원문에 "lazy loading" 언급 없는데 citing doc이
                    │         "이 논문이 lazy loading을 정당화한다"고 주장
                    │
                    └── YES: 원문이 다루긴 하지만 claim이 과장/확대
                          └── PARTIAL-MINOR (overstatement)
                          예: 원문 "제안된 프레임워크" → claim "확립된 표준"
                              원문 "pathology에서" → claim "일반적으로"
```

### 판정 원칙

1. **Source text only:** 판정은 원문에 실제로 적힌 내용에만 기반. 배경 지식으로 빈칸을 채우지 않음.
2. **Strongest passage:** 원문에서 claim을 가장 강하게 지지하는 구절을 기준으로 판정. 약한 구절로 PARTIAL을 만들지 않음.
3. **Tentative language rule:** 원문이 "may", "suggests", "could" 등 잠정적 표현을 쓰면, claim이 이를 단정적("shows", "demonstrates", "proves")으로 바꿨는지 확인. 바꿨으면 Step 3에서 material.
4. **Scope preservation:** 원문이 특정 조건/도메인/모델에 한정했는데 claim이 일반화하면 material.
5. **Single strongest claim:** 한 pair에 여러 sub-claim이 있으면 가장 핵심적인 것 하나만 판정.

---

## 2. Materiality Test

Step 3 "핵심 주장을 바꾸는가?"를 판단하는 기준.

| 차이 유형 | SUPPORT (cosmetic, non-material) | PARTIAL (material) | 판단 기준 |
|---|---|---|---|
| **수치** | "약 90%" → "90%" | "82% with COT" → "82% baseline" (조건 누락) | 조건/맥락이 빠지면 material |
| **범위** | "LLMs에서" → "GPT-4에서" (하위집합 OK) | "pathology에서" → "일반적으로" (과잉 일반화) | 상위집합으로 확대하면 material |
| **인과** | "A와 B 상관" → "A와 B 관련" | "A와 B 상관" → "A가 B를 일으킴" | 상관→인과 전환은 항상 material |
| **추천/처방** | "X가 한 가지 방법" → "X가 한 접근" | "X가 한 가지 방법" → "X를 추천" | 서술→처방 전환은 material |
| **지위** | "제안된 방법론" → "제안된 프레임워크" | "제안된 프레임워크" → "확립된 표준" | 지위 격상은 material |
| **약어/표현** | "LMs" → "Language Models" | "Lost in the Haystack" → "Hidden in the Haystack" | 의미 변경 가능하면 material |
| **기여 귀속** | "논문이 X를 연구함" → "논문이 X를 다룸" | "논문의 한 실험 조건" → "논문이 X를 추천" | 부수적 기여를 주 기여로 격상하면 material |

### Materiality 경계 원칙

- **의심스러우면 material 쪽으로 판정** (보수적 접근)
- 차이가 "독자가 원문을 읽었을 때 다른 인상을 받을 수 있는가?"에 YES면 material
- 복수 cosmetic 차이가 누적되면 전체적으로 material일 수 있음 — 개별이 아닌 총체적 판단

---

## 3. Edge Case Bank

### 3.1 SUPPORT 경계 사례

**Case E1: 약어 확장**
- Claim: "Large Language Models show emergent capabilities"
- Source: "LLMs show emergent capabilities"
- Verdict: **SUPPORT** — 자명한 약어 확장은 cosmetic
- 근거: 약어와 원문이 동일 의미, 독자 혼동 없음

**Case E2: 하위집합 지정**
- Claim: "GPT-4에서 이 현상이 관찰되었다"
- Source: "여러 LLM에서 이 현상이 관찰되었다 (GPT-4 포함)"
- Verdict: **SUPPORT** — claim이 source 범위의 하위집합. 과장이 아님.
- 근거: 범위 축소(일반→구체)는 material하지 않음, 범위 확대(구체→일반)만 material

### 3.2 PARTIAL-MINOR 경계 사례

**Case E3: 지위 격상 (proposal → norm)**
- Claim: "PRISMA-trAIce establishes the norm for AI disclosure in systematic reviews"
- Source: "We propose a checklist for AI-assisted systematic review reporting"
- Verdict: **PARTIAL-MINOR** — 원문이 disclosure를 다루긴 하지만, "propose" ≠ "establishes the norm"
- 근거: 핵심 개념(AI disclosure checklist)은 원문에 있음. 지위만 격상.

**Case E4: 범위 확대 (domain-specific → general)**
- Claim: "전문가도 AI 출력에 편향된다"
- Source: "pathology TCP 추정에서 28명의 전문가가 AI 오류 출력에 편향되었다 (7% AB rate)"
- Verdict: **PARTIAL-MINOR** — 원문이 automation bias를 다루지만, 도메인(pathology)과 규모(n=28) 한정.
- 근거: 핵심 개념(expert automation bias)은 있음. 범위만 과장.

### 3.3 PARTIAL-MAJOR 경계 사례

**Case E5: Attribution gap (원문에 없는 개념 귀속)**
- Claim: "이 논문의 scaling law가 lazy loading 아키텍처를 정당화한다"
- Source: sigmoid collaborative scaling law (quality saturates at ~16 agents). "lazy loading" 언급 없음.
- Verdict: **PARTIAL-MAJOR** — scaling law는 있지만, "lazy loading"은 원문에 존재하지 않는 개념.
- 근거: citing document가 원문에 없는 아키텍처 패턴을 귀속함.

**Case E6: 처방적 전환 (description → recommendation)**
- Claim: "논문이 blind-first review를 추천한다"
- Source: automation bias를 보고하지만, blind-first review를 명시적으로 추천하지 않음. design recommendation은 citing document의 추론.
- Verdict: **PARTIAL-MAJOR** — 원문이 "blind-first review"라는 구체적 설계를 다루지 않음.
- 근거: 경험적 발견(AB exists)에서 구체적 설계(blind-first)로의 leap.

### 3.4 REFUTE 사례 (합성)

**Case E7: 직접 모순**
- Claim: "이 기법은 성능을 향상시킨다"
- Source: "We found that this technique significantly degraded performance across all benchmarks (Table 3)"
- Verdict: **REFUTE** — 원문이 claim의 정반대를 명시적으로 진술.
- 근거: 원문에 "degraded performance" 명시.

**Case E8: 결론 역전**
- Claim: "Multi-agent systems consistently outperform single agents"
- Source: "Our results show no statistically significant difference between multi-agent and single-agent configurations (p=0.42)"
- Verdict: **REFUTE** — 원문이 "no significant difference"를 보고하는데 claim이 "consistently outperform"으로 역전.
- 근거: 통계적으로 유의하지 않은 차이를 일관된 우위로 전환.

### 3.5 UNCERTAIN 사례 (합성)

**Case E9: 접선적 관련 (tangentially related)**
- Claim: "이 논문이 우리 검증 프레임워크의 구조화된 접근을 뒷받침한다"
- Source: PRISMA 2020 — systematic review 보고 가이드라인. Citation verification에 대한 내용 없음.
- Verdict: **UNCERTAIN** — 원문이 구조화된 체크리스트 접근을 사용하지만, citation verification과는 다른 도메인.
- 근거: 비유적 관련은 있지만 직접적 evidence가 아님. SUPPORT도 REFUTE도 아님.

**Case E10: 접근 불가**
- Claim: 임의의 claim
- Source: paywall 뒤, abstract만 접근 가능. Abstract에 claim 관련 언급 없음.
- Verdict: **UNCERTAIN** (Access_Status = abstract_only)
- 근거: 본문에 evidence가 있을 수 있지만 확인 불가. Substantive verdict 불가.

---

## 4. PARTIAL Sub-type 정의

| Sub-type | 정의 | 핵심 질문 | 예시 |
|---|---|---|---|
| **PARTIAL-MAJOR** | 원문이 claim의 핵심 개념을 **명시적으로 다루지 않음**. Citing document가 원문에 없는 것을 귀속. | "원문에서 이 개념/용어/추천을 직접 찾을 수 있는가?" → NO | B1 "lazy loading", C-04 "blind-first review 추천" |
| **PARTIAL-MINOR** | 원문이 핵심 개념을 **다루긴 하지만** claim이 범위/조건/지위/인과를 과장. | "원문에서 이 개념을 찾을 수 있지만, claim이 원문보다 강한가?" → YES | S-02 proposal→norm, A3 조건 누락 |

**경계 판단:** "원문에서 claim의 핵심 키워드/개념을 ctrl+F로 찾을 수 있는가?"
- 찾을 수 있으면 → PARTIAL-MINOR (overstatement) 방향
- 찾을 수 없으면 → PARTIAL-MAJOR (attribution gap) 방향
- 이 heuristic은 시작점이지 절대 규칙은 아님 — 맥락 판단 필요
