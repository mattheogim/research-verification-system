# L2 Full Validation Plan — Rigorous Execution Spec

_Created: 2026-04-15_
_Updated: 2026-04-16 — Codex L1 결과 반영 + Codex peer review 반영_
_Status: DRAFT v3 — Codex review 피드백 통합 완료_
_Reviewed by: Codex (독립 세션, 2026-04-16)_
_Supersedes: NEXT_PLAN_L2_VALIDATION.md (too high-level)_

---

## 0. Why This Plan Exists

L1 검증은 6개 축 모두 충족 (gold standard, inter-rater, operational def, clean re-run, baseline, N=98).
L2 검증은 6개 축 중 **0개 충족**. 현재 L2는 N=8, gold standard 없음, inter-rater 없음.

이대로 논문에 넣으면 reviewer가 "L2는 anecdotal pilot" 한 줄로 끝낼 수 있음.
이 플랜의 목표: **L2를 conference-defensible 수준으로 올리거나, workshop-level scoping을 명시적으로 선택하는 근거를 만들기.**

---

## 1. Scope Decision (Phase 0 — 가장 먼저 결정)

실행 전에 반드시 결정해야 할 것:

| 경로 | L2 목표 | 필요 N | 검증 수준 | 논문 positioning |
|---|---|---|---|---|
| **A: Full validation** | L2도 conference-level | 최소 20 claim-source pairs | Gold + Inter-rater + Re-run + Baseline | "We validate both L1 and L2" |
| **B: Feasibility pilot** | L2는 "promising direction" | 현재 8~12면 충분 | Gold + Re-run만 (inter-rater 생략 가능) | "L2 is feasibility; full validation is future work" |

**추천: 경로 B로 시작하되, Phase 2 결과에 따라 A로 확장 결정.**
이유: N=8에서 inter-rater kappa는 CI가 너무 넓어서 의미 없음. 먼저 operational definition을 단단하게 잡고, gold standard로 LLM 정확도를 측정한 뒤, 그 결과가 promising하면 N 확장.

---

## 2. Phase 1: Operational Definition Hardening

**목적:** SUPPORT vs PARTIAL 경계를 누가 읽어도 같은 판정을 내릴 수 있게 만들기.
**선행조건:** 없음 (가장 먼저 실행)
**산출물:** `level2_checklist_v1.0.md` (v0.1 대체)

### 2.1 현재 문제

v0.1 체크리스트의 PARTIAL 정의:
> "source contains relevant evidence, but the citing claim (a) overstates the finding, (b) omits important caveats/conditions, (c) infers beyond what the source states, or (d) uses the source for a purpose it wasn't designed for."

문제점:
- (a)~(d) 각각의 **정도**가 불명확. 얼마나 overstate해야 PARTIAL인가?
- "important caveats" — 누가 important를 판단하나?
- "infers beyond" — 어디까지가 합리적 추론이고 어디부터가 overreach인가?

### 2.2 해결: Decision Tree + Boundary Examples

**Decision Tree:**

```
1. 원문에 claim과 관련된 내용이 있는가?
   ├── NO → REFUTE (원문이 claim을 반박) 또는 UNCERTAIN (관련 없거나 모호)
   └── YES →
       2. claim이 원문의 범위/조건/한정어를 보존하는가?
          ├── YES → SUPPORT
          └── NO →
              3. 차이가 claim의 핵심 주장을 바꾸는가?
                 ├── NO → SUPPORT (cosmetic difference)
                 └── YES →
                     3b. 원문이 claim의 핵심 개념을 명시적으로 다루는가?
                         ├── NO → PARTIAL-MAJOR (attribution gap: 원문이 안 다루는 걸 귀속)
                         └── YES → PARTIAL-MINOR (overstatement: 다루지만 과장/확대)
```

**PARTIAL 세분화 근거 (Gap 5):**
- PARTIAL-MAJOR: 원문에 해당 개념이 없는데 있다고 귀속 (예: B1 "lazy loading" — 원문에 없음)
- PARTIAL-MINOR: 원문이 다루긴 하지만 범위/지위/인과를 과장 (예: S-02 proposal→norm)

**"핵심 주장을 바꾸는가" 기준 (Materiality Test):**

| 차이 유형 | SUPPORT (cosmetic) | PARTIAL (material) |
|---|---|---|
| 숫자 | 원문 "약 90%" → claim "90%" | 원문 "82% with COT" → claim "82% baseline" (조건 누락) |
| 범위 | 원문 "LLMs에서" → claim "GPT-4에서" (하위집합) | 원문 "pathology에서" → claim "일반적으로" (과잉 일반화) |
| 인과 | 원문 "A와 B 상관" → claim "A와 B 관련" | 원문 "A와 B 상관" → claim "A가 B를 일으킴" (인과 추론) |
| 추천 | 원문 "X가 한 가지 방법" → claim "X가 한 접근" | 원문 "X가 한 가지 방법" → claim "X를 추천" (처방적 전환) |
| 지위 | 원문 "제안된 프레임워크" → claim "제안된 방법론" | 원문 "제안된 프레임워크" → claim "확립된 표준" (지위 부풀림) |

### 2.3 L1 정규화 규칙 (Codex 결과에서 파생 — 병렬 작업)

Codex L1 실험이 증명한 것: **정규화 규칙 없이 모델 간 비교는 무의미.**
L2 decision tree와 동시에 L1 정규화 규칙도 고정해야 함.

**확정해야 할 4개 규칙:**

| # | 규칙 | 옵션 A (Claude 현행) | 옵션 B (Codex 현행) | 추천 |
|---|---|---|---|---|
| N1 | 약어 확장 | LLMs = Large Language Models → EXACT | 다르면 PARTIAL | **A** — CS 관행상 자명한 약어 허용 |
| N2 | Subtitle 생략 | 콜론 이후 생략 → EXACT | 다르면 PARTIAL | **조건부** — main title이 unique하면 EXACT, 동명 논문 존재 시 PARTIAL |
| N3 | Venue alias | TACL = Transactions of ACL → EXACT | 다르면 PARTIAL | **A** — 공식 약어 허용 |
| N4 | 저자 비교 | first author 중심 | full list + (unknown) 에러 | **절충** — catalog에 "(unknown)"은 metadata gap이지 error 아님. 실제 저자 불일치만 에러 |

**산출물:** `normalization_rules_L1.md`
**이 규칙으로 Claude + Codex 42개 결과 재채점 → `cross_model_L1_rescored.csv`**

**L2와의 연결:** N2(subtitle)의 "unique 여부" 판단 로직이 L2의 "materiality test"와 동형.
정규화 규칙 설계 경험이 L2 decision tree 설계에 직접 도움됨.

### 2.4 기존 8개로 Calibration (번호 수정)

기존 9개 claim-source pair를 Decision Tree로 재판정하여 v0.1 판정과 비교:

| ID | v0.1 Judgment | Decision Tree 재판정 | 일치? | 불일치 시 Tree 수정 필요? |
|---|---|---|---|---|
| A3 | PARTIAL | ? | | |
| B1 | PARTIAL | ? | | |
| I1-a | SUPPORT | ? | | |
| I1-b | PARTIAL | ? | | |
| S-02 | PARTIAL | ? | | |
| C-04 | PARTIAL | ? | | |
| S-01 | PARTIAL | ? | | |
| S-04 | PARTIAL | ? | | |

**합격 기준:** 8/9 이상 일치 또는 불일치 case에서 Tree가 더 나은 판정을 내림.
**불합격 시:** Tree 수정 → 재판정 → 반복 (최대 3회).

### 2.5 Edge Case Bank

각 (a)~(d) 유형별로 최소 2개씩, 총 8개 이상의 경계 사례 문서화:
- 각 사례: claim text, source text, SUPPORT/PARTIAL 판정, 1문장 근거
- REFUTE/UNCERTAIN 합성 사례 각 2개 포함 (Gap 4)
- 이 bank가 cross-model calibration의 교재가 됨

### 2.6 Calibration / Evaluation Split (Codex review 반영)

> **⚠️ Codex 지적:** 기존 9개 pair로 decision tree를 다듬고, 같은 9개로 T1/T2를 평가하면 test set leakage.

**규칙:**
- **Calibration set:** 기존 9개 claim-source pairs (A3, B1, I1-a, I1-b, S-02, C-04, S-01, S-04 + 1)
  - Phase 1 decision tree 튜닝에 사용
  - T1/T2/T3/T5 평가에 **사용 금지**
  - 논문에 "calibration set (N=9)"으로 보고
- **Evaluation set:** Phase 2에서 새로 선정하는 papers (최소 8개 pairs, 목표 12+)
  - Phase 1 산출물(frozen decision tree)로만 판정
  - T1/T2/T3/T5 평가에 사용
  - 논문에 "evaluation set (N=12+)"으로 보고

**Evaluation set 선정 기준:**
1. Calibration set과 겹치지 않는 논문
2. Open access (arXiv 우선)
3. Claim type 다양성 (calibration set에 없는 conceptual_framework, system_comparison 포함)
4. SUPPORT 기대 비율 40%+ (calibration set의 78% PARTIAL skew 보정)
5. Dataset A, B, C에서 골고루

**이게 Phase 5 (Sample Expansion)를 사실상 필수로 만듦** — calibration 9개 + evaluation 12+ = 최소 21개 pairs.

### 2.7 Rubric Freeze Gate (Codex review 반영)

> **⚠️ Codex 지적:** Phase 2-3 병렬은 freeze protocol 없으면 위험. 하나라도 바뀌면 moving target.

**Phase 1 종료 시 아래를 모두 잠금 (이후 수정 금지):**

| 항목 | 파일 | freeze 방법 |
|---|---|---|
| Decision tree v1.0 | `level2_checklist_v1.0.md` | git tag `rubric-freeze-v1` |
| Edge case bank | `edge_case_bank_L2.md` | 같은 tag |
| Claude L2 prompt | `claude_L2_prompt_v1.md` | 같은 tag |
| Codex L2 prompt | `codex_L2_prompt_v1.md` | 같은 tag |
| L2_input.csv | `L2_input.csv` | 같은 tag |
| Tool policy | 아래 명시 | 같은 tag |
| Source archive | `L2_source_archive/` | snapshot date 기록 |
| Model version | prompt 내 명시 | — |

**Tool policy (frozen):**
- Claude: WebFetch로 arXiv HTML 접근. ar5iv 우선.
- Codex: 동일한 방식으로 arXiv HTML 접근. ar5iv 우선.
- 둘 다: abstract-only 판정 금지. Verification_Basis 컬럼 필수.
- 둘 다: 프로젝트 내 다른 파일 접근 금지.

**Freeze 이후 수정이 필요한 경우:**
- Decision tree 변경 → `rubric-freeze-v2` 새 tag → **Phase 2-3 전부 재실행**
- Prompt 변경 → 해당 모델만 재실행
- Source archive 변경 → 전부 재실행
- **어떤 수정이든 변경 사유를 `rubric_change_log.md`에 기록**

---

## 3. Phase 2: Human Gold Standard

**목적:** 사람이 독립적으로 **evaluation set** claim-source pair를 판정하여 LLM 정확도 측정.
**선행조건:** Phase 1 완료 + Rubric Freeze (Section 2.7)
**산출물:** `gold_standard_L2.md`, `gold_standard_L2.csv`

### 3.1 Protocol

1. **Rater:** 본인 (논문 저자). 이상적으로는 외부인이지만, 1인 연구에서는 아래 절차로 보완.
2. **Blinding:** LLM 판정 결과를 보지 않은 상태에서 판정.
   - Evaluation set만 사용 (calibration set 9개는 이미 봤으므로 제외)
   - L2_input.csv의 Claim_Text + ArXiv_URL만 보고 원문 접근 → 독립 판정
3. **판정 기준:** Frozen decision tree + edge case bank (Section 2.7 freeze 이후 버전)

4. **Evidence-First Protocol (Codex review 반영):**
   > ⚠️ Codex 지적: rubric을 만들고, edge case를 보고, threshold를 고민한 뒤 blinded self-rating해도
   > 완전한 독립 gold가 아님. Memory leakage가 남음.

   **순서를 강제하여 편향 최소화:**
   - Step 1: 원문에서 claim 관련 섹션 찾기 → **Evidence_Section, Evidence_Quote 먼저 기록**
   - Step 2: "이 evidence가 claim을 얼마나 지지하는가?" → **Evidence_Strength (strong/moderate/weak/none) 기록**
   - Step 3: Evidence_Strength를 decision tree에 대입 → **Verdict 기록**
   - **Step 1-2를 전부 마친 후에만 Step 3 진행** (한 pair씩이 아니라 전체 evidence 수집 후 verdict 일괄)

   이렇게 하면:
   - Evidence 수집이 verdict에 영향받지 않음
   - Verdict는 evidence에 기반 (사후 합리화 방지)
   - Audit trail: evidence → strength → verdict 경로가 추적 가능

5. **기록 형식:** 각 pair별로:
   - Evidence_Section: 원문 섹션명 (예: "Section 3.2, Table 2")
   - Evidence_Quote: 가장 관련 있는 원문 문장 1개
   - Evidence_Strength: strong / moderate / weak / none
   - Why_Not_Stronger: 왜 더 강한 support가 아닌지 1문장
   - Why_Not_Weaker: 왜 더 약한 support가 아닌지 1문장
   - Human_Judgment: SUPPORT / PARTIAL-MAJOR / PARTIAL-MINOR / REFUTE / UNCERTAIN
   - Confidence: HIGH / MEDIUM / LOW
   - Time_Min: 소요 시간

6. **한계 명시 (논문에 반드시 포함):**
   > "The gold standard was created by the same researcher who designed the decision tree.
   > While we mitigated bias through evidence-first protocol and rubric freezing,
   > full independence requires an external rater, which was not feasible for this study."

### 3.2 Sample

**최소:** 현재 8개 논문 (9 claim-source pairs) 전수 — N이 작으니 sampling 하면 안 됨.
**권장:** 4~6개 추가하여 총 13~15 pairs. 추가 기준:
- Dataset C에서 2~3개 (domain diversity)
- SUPPORT가 나올 것으로 예상되는 것 2~3개 (현재 SUPPORT 비율 22%로 skewed)
  - SUPPORT 사례가 너무 적으면 precision 계산 불가

### 3.3 Metrics

| Metric | 계산법 | L1 참고값 | L2 목표 |
|---|---|---|---|
| Agreement rate | (일치 수 / 전체) | 75% (15/20) | ≥70% |
| Cohen's Kappa | κ = (po - pe) / (1 - pe) | 0.444 | ≥0.40 (moderate) |
| PARTIAL precision | TP_partial / (TP_partial + FP_partial) | N/A | 보고만 (threshold 없음) |
| SUPPORT precision | TP_support / (TP_support + FP_support) | N/A | 보고만 |

**주의:** N=9에서 kappa의 95% CI는 매우 넓음 (±0.3 이상 가능). 따라서:
- Kappa는 보고하되 "N 한계로 해석 주의" 명시
- Agreement rate를 주 metric으로 사용
- 불일치 case의 정성 분석이 핵심 (왜 달랐는가?)

### 3.4 불일치 분석 Protocol

모든 Human ≠ LLM case에 대해:
1. 불일치 방향: LLM이 더 관대(SUPPORT) vs 더 엄격(PARTIAL)?
2. 원인 분류:
   - (a) 원문 해석 차이 (합리적 불일치)
   - (b) LLM이 원문을 못 읽음 (access/hallucination)
   - (c) Decision tree 경계 모호 (definition 문제)
   - (d) Human 실수
3. 각 원인별 대응:
   - (a) → 논문에 "interpretation variability" 보고
   - (b) → LLM limitation 보고 + 해당 case 재검증
   - (c) → Phase 1 decision tree 수정 → 전체 재판정
   - (d) → 수정 후 재집계

---

## 4. Phase 3: Claude + Codex 독립 L2 실행 (Cross-Model Reproducibility)

**목적:** 같은 operational definition으로 두 모델을 독립 실행하여:
1. **재현성** — Claude clean re-run (기존 Phase 3 기능)
2. **Cross-model reproducibility** — Claude vs Codex (재현성 보충 신호, inter-rater 대체 **아님**)
3. **Definition quality test** — 정의가 충분히 명확한지 (두 모델이 수렴하면 명확)

> **⚠️ Codex review 지적:** Claude와 Codex는 shared pretraining, 유사한 검색 습관, 같은 prompt로 인해
> 같은 방향으로 틀릴 수 있음 (correlated errors). T5는 **재현성 proxy**이지 **타당도 증거 아님.**
> 논문에서 "inter-rater replacement"가 아닌 "supplementary reproducibility signal"로 표현할 것.

**선행조건:** Phase 1 완료 + L2 input file 생성
**산출물:** `claude_L2_independent.csv`, `codex_L2_independent.csv`, `L2_inter_model_comparison.md`

### 4.0 L1 교훈 적용

L1에서 배운 것: 정규화 규칙 없이 비교 → EXACT 57% vs 12% (무의미한 차이).
L2에서 반복하지 않기 위해:
- **같은 operational definition** (decision tree + materiality test + edge cases)을 prompt에 inline 포함
- **같은 input file** (논문 ID + URL + claim text)
- **같은 output format** (verdict + 근거 + provenance)
- 이렇게 Layer 3(verdict mapping)를 고정하면, 차이가 나면 그건 진짜 Layer 1-2(능력) 차이

### 4.1 Session Isolation Protocol

```
Session A: Phase 1 실행 (definition + input file 생성)
  ├── 산출물: level2_checklist_v1.0.md, L2_input.csv
  │   이 세션은 L2 판정을 직접 하지 않음 (사전 판단 오염 방지)
  │
  ├──→ Session B: Claude L2 실행 (새 세션)
  │     ├── 입력: L2_input.csv + operational definition (prompt에 inline)
  │     ├── 출력: claude_L2_independent.csv
  │     └── 접근 금지: pilot_L2_results.csv, 이 플랜, gold standard
  │
  ├──→ Session C: Codex L2 실행 (별도)
  │     ├── 입력: L2_input.csv + operational definition (prompt에 inline)
  │     ├── 출력: codex_L2_independent.csv
  │     └── 접근 금지: 위와 동일 + claude_L2_independent.csv
  │
  └──→ Session D: 비교 분석 (제3 세션)
        ├── 입력: claude_L2_*.csv + codex_L2_*.csv + gold_standard_L2.csv
        └── 출력: L2_inter_model_comparison.md
```

**Session B와 C는 병렬 실행 가능** — 서로의 결과를 모름.

### 4.2 공통 Input File 설계

`L2_input.csv` — Phase 1 완료 후 생성:

```csv
ID,Paper_Title,ArXiv_URL,Claim_Text,Claim_Type,Citing_Location
A3,"Hegazy - Diversity of Thought",https://arxiv.org/abs/2410.12853,"91% GSM-8K (diverse) vs 82% (homogeneous) = +9pp diversity premium",factual_number,"[citing doc file:line]"
B1,"Qian et al. - Scaling MAS",https://arxiv.org/abs/2406.07155,"Logistic growth formula for agent scaling; justifies lazy loading",empirical_finding,"[citing doc file:line]"
...
```

**포함:** ID, 논문 제목, arXiv URL, claim 원문, claim type, 인용 위치
**미포함:** 이전 judgment, confidence, key finding, downstream impact

### 4.3 Unified L2 Prompt Template (Claude + Codex 공통)

> **Phase 1 완료 후 placeholder를 채워서 최종 확정.**
> Claude와 Codex 양쪽에 **동일한 텍스트**로 사용. OUTPUT_FILE만 다름.
> 우리 template + Codex 자체 설계 prompt를 merge하여 강화.

```markdown
You are performing a blinded Level 2 claim-evidence verification task.

## Isolation Rules (CRITICAL)
This is an isolated evaluation run. Use ONLY:
1. This prompt
2. {{INPUT_FILE}} (the input CSV)
3. Direct fetches to paper URLs (arXiv, ar5iv, publisher pages)

Do NOT use or rely on:
- Memory, saved memories, chat history, project context
- Previous runs, prior outputs, prior analyses
- Gold labels, human judgments, prior Claude/Codex outputs
- Comparison tables, experiment plans, session notes
- Any other local project files

If required information is unavailable from allowed materials, say so. Do not fill gaps from memory.

## Task
For each row in {{INPUT_FILE}}, verify whether the cited source's full text
supports the stated claim.

## Full-Text Requirement
You MUST read the full text of the source before assigning a verdict.
Abstract-only reading is NOT sufficient.
ar5iv HTML preferred: https://ar5iv.labs.arxiv.org/html/{arxiv_id}
If only abstract is available, mark Access_Status = abstract_only.

## Official Definition Block (sole authority for verdict assignment)

[BEGIN DECISION_TREE_V1]
{{DECISION_TREE_V1 — Phase 1에서 확정, inline 전문}}
[END DECISION_TREE_V1]

[BEGIN MATERIALITY_TEST_V1]
{{MATERIALITY_TEST_V1 — Phase 1에서 확정, inline 전문}}
[END MATERIALITY_TEST_V1]

[BEGIN EDGE_CASE_BANK_V1]
{{EDGE_CASE_BANK_V1 — Phase 1에서 확정, inline 전문}}
[END EDGE_CASE_BANK_V1]

### PARTIAL Sub-types
- PARTIAL-MAJOR: source does not address the claim's key concept (attribution gap)
- PARTIAL-MINOR: source addresses it but claim overstates scope/status/causation (overstatement)

## Procedure (EVIDENCE-FIRST — order matters)
1. Read input row (claim text + source URL)
2. Fetch source full text from official URL
3. Read enough full text to evaluate the exact claim
4. Identify the strongest relevant passage
5. **Record evidence FIRST:** Evidence_Section, Evidence_Quote, Evidence_Strength
6. **Record Why_Not:** Why_Not_Stronger, Why_Not_Weaker
7. **THEN apply** decision tree + materiality test → Verdict
8. Write one CSV row
9. Repeat for all rows

## Quality Rules
- Do NOT normalize away meaningful differences unless the Definition Block says to
- Do NOT upgrade tentative language ("may", "suggests") into strong claims
- Do NOT treat implied plausibility as textual support
- Do NOT use background knowledge to repair missing evidence
- Do NOT infer author intent beyond what the source text states
- If using a search engine to locate a paper: do NOT base verdict on search snippets

## Output Schema
Save to {{OUTPUT_FILE}} with exactly these columns (order matters):

ID,Evidence_Section,Evidence_Quote,Evidence_Strength,Why_Not_Stronger,Why_Not_Weaker,Verdict,Verdict_Sub,Confidence,Justification,Source_URL,Verification_Basis,Access_Status,Time_Min
```

Column definitions (evidence columns before verdict columns):
- ID: copy from input
- Evidence_Section: section name in source (e.g. "Section 3.2", "Table 2")
- Evidence_Quote: most relevant verbatim quote from source (≤20 words)
- Evidence_Strength: strong / moderate / weak / none
- Why_Not_Stronger: 1 sentence — why not a stronger support level
- Why_Not_Weaker: 1 sentence — why not a weaker support level
- Verdict: SUPPORT / PARTIAL / REFUTE / UNCERTAIN
- Verdict_Sub: MAJOR / MINOR (only if Verdict=PARTIAL, else blank)
- Confidence: HIGH / MEDIUM / LOW
- Justification: 1-2 sentence verdict rationale
- Source_URL: exact URL actually accessed
- Verification_Basis: full_text_direct_fetch / abstract_only / search_only / access_failure
- Access_Status: full_text_accessed / abstract_only / inaccessible
- Time_Min: minutes spent on this pair

## Substantive-Verdict Constraint
If Access_Status ≠ full_text_accessed, do NOT assign SUPPORT / PARTIAL / REFUTE.
Use UNCERTAIN with Justification = "full text not accessed".

## Final Checklist
Before saving, verify every row has:
- [ ] Source_URL filled
- [ ] Verification_Basis filled
- [ ] Evidence_Section filled
- [ ] Evidence_Quote filled
- [ ] Access_Status filled
- [ ] Input order preserved
- [ ] No reliance on prior sessions or unattached files

Save only the CSV to {{OUTPUT_FILE}}.
Do not read or write any other project files.
```

**Claude용:** `{{INPUT_FILE}}` = `04_pilots/L2_input.csv`, `{{OUTPUT_FILE}}` = `04_pilots/claude_L2_independent.csv`
**Codex용:** `{{INPUT_FILE}}` = `04_pilots/L2_input.csv`, `{{OUTPUT_FILE}}` = `04_pilots/codex_L2_results.csv`
**Definition Block, Quality Rules, Output Schema — 한 글자도 다르면 안 됨.**

### 4.4.1 Prompt/Tool Parity Requirements (Codex review 반영)

> ⚠️ Codex 지적: Claude vs Codex 비교는 모델 비교가 아니라 **모델+도구+프롬프트 패키지** 비교.
> 도구 차이가 있으면 T5 해석이 깨짐.

**Parity checklist (freeze 시 확인):**

| 항목 | Claude | Codex | 동일 여부 |
|---|---|---|---|
| Operational definition text | 복붙 | 복붙 | 반드시 동일 |
| Input file | L2_input.csv | L2_input.csv | 동일 |
| Output schema | 13 컬럼 | 13 컬럼 | 동일 |
| Evidence-first 절차 | 7 steps | 7 steps | 동일 |
| Web access method | WebFetch | 웹 검색 도구 | **다름 — 논문에 명시** |
| arXiv access | ar5iv HTML 권장 | ar5iv HTML 권장 | 동일 권장이지만 강제 불가 |
| Source archive 사용 | 로컬 복사본 사용 가능 | 로컬 복사본 접근 가능? | **확인 필요** |
| 다른 파일 접근 | 금지 명시 | 금지 명시 | 동일 |

**도구 차이가 있는 부분은 논문에 명시:**
> "Both models received identical prompts and operational definitions.
> Claude used WebFetch and Codex used its web browsing tool for source access.
> This means our comparison tests model+tool packages, not pure model capability."

**완화책:** 두 모델 모두 Source_URL + Verification_Basis를 기록하므로, access 차이로 인한 verdict 차이를 사후 식별 가능.

### 4.5 Metrics (3-way 비교)

**PARTIAL subtype 처리 규칙 (Codex review 반영):**
- **Parent-class agreement:** PARTIAL-MAJOR vs PARTIAL-MINOR = **일치** (둘 다 PARTIAL)
- **Subtype agreement:** PARTIAL-MAJOR vs PARTIAL-MINOR = **불일치** (subtype mismatch)
- T1/T2/T5는 **parent-class 기준**으로 계산
- Subtype mismatch는 별도 보고 (정보 손실 방지)

| Metric | 비교 쌍 | 의미 | 기준 |
|---|---|---|---|
| Agreement (parent-class) | Human vs Claude | **PRIMARY endpoint** (T1) | ≥ 아래 참조 |
| Agreement (parent-class) | Human vs Codex | Secondary | 보고만 |
| Agreement (parent-class) | Claude vs Codex | Cross-model reproducibility (T5) | ≥ 아래 참조 |
| Subtype agreement | 각 쌍 | PARTIAL 내 세분화 일치도 | 보고만 (threshold 없음) |
| Cohen's Kappa | Claude vs Codex | 기준 고정 후 모델 간 일치도 + 95% CI | 보고만 (N 작아서 CI 넓음) |
| 방향성 일치 | 3-way | SUPPORT↔REFUTE 역전 | 0건 (T4) |

### 4.6 3-way 불일치 분석

**Step 1: Evidence_Quote 비교 (verdict 보기 전에)**

각 불일치 case에서 먼저 확인: 세 rater가 **같은 구절을 참조했는가?**

| Evidence 패턴 | 의미 | 이것이 결정하는 것 |
|---|---|---|
| 같은 구절 → 다른 verdict | **Definition 문제** — 같은 evidence를 다르게 해석 | → Phase 1 decision tree 수정 |
| 다른 구절 → 다른 verdict | **Source access/검색 능력 차이** — 관련 구절을 찾는 능력이 다름 | → Tool parity 또는 모델 능력 문제 |
| 다른 구절 → 같은 verdict | 우연의 일치 가능 — evidence는 다르지만 결론은 같음 | → 주의 필요, audit에서 확인 |

**Step 2: Verdict 패턴 분석 (Step 1 결과와 함께)**

| Verdict 패턴 | 의미 | 대응 |
|---|---|---|
| Human=Claude≠Codex | Codex 능력 한계 또는 source access 문제 | Codex의 Verification_Basis + Evidence_Quote 확인 |
| Human=Codex≠Claude | Claude 능력 한계 (이전 세션 bias?) | Claude의 Evidence_Quote 확인 |
| Human≠Claude=Codex | 두 모델 공통 맹점 (L1의 E5처럼) | **가장 중요한 발견** — LLM 공통 한계. Evidence_Quote로 같은 구절인지 확인 |
| Human≠Claude≠Codex (3-way 불일치) | Definition 문제 | Phase 1 decision tree 모호 → 수정 |

### 4.7 기존 Phase 3 기능 (재현성) 보존

Claude 독립 실행이 기존 clean re-run을 대체:
- Claude pilot (기존 8개) vs Claude independent (같은 8개, 새 세션)
- 이 비교가 재현성 metric
- 추가로 Codex 비교가 inter-model metric

### 4.8 불일치 대응 (업데이트)

- **1~2건 경미 차이 (PARTIAL ↔ SUPPORT):** 허용, 논문에 보고
- **3건 이상 Claude≠Codex:** definition 문제 가능 → Phase 1 decision tree 재검토
- **SUPPORT ↔ REFUTE 역전:** 해당 case 원인 분석 필수 (T4)
- **Codex Verification_Basis ≠ full_text_fetch:** 해당 case를 별도 집계 (provenance 문제)
- **3-way 불일치 3건+:** Phase 1로 돌아가 decision tree 수정 → 전체 재실행

---

## 5. Phase 4: Baseline Comparison

**목적:** "LLM이 전문을 읽어야 하는가?" — 더 싼 방법과 비교.
**선행조건:** Phase 2 (gold standard) 완료
**산출물:** `baseline_comparison_L2.md`

### 5.1 Baselines

| Baseline | 방법 | 비용 | 기대 |
|---|---|---|---|
| **B0: Random** | base rate로 랜덤 판정 (현재 78% PARTIAL) | 0 min | 하한선 |
| **B1: Abstract-only** | abstract만 읽고 claim-evidence alignment 판정 | ~1 min/pair | 대부분 SUPPORT로 나올 것 (abstract은 긍정적) |
| **B2: Keyword overlap** | claim과 source abstract의 keyword overlap score → threshold로 SUPPORT/PARTIAL 분류 | ~0.5 min/pair | Recall 낮을 것 (semantic gap) |
| **B3: LLM abstract-only** | Claude에게 abstract만 주고 판정시키기 | ~1 min/pair | Full-text보다 SUPPORT 비율 높을 것 |

### 5.2 비교 프레임

Human gold standard을 ground truth로 사용:
- 각 baseline의 Agreement with gold
- 각 baseline이 놓치는 PARTIAL case 분석
- **핵심 질문:** "Full-text reading이 abstract-only 대비 PARTIAL을 얼마나 더 잡는가?"

### 5.3 Pre-registered Threshold

> **L2 baseline threshold:** Full-text LLM 판정이 best baseline 대비 agreement +15% 이상이면 "L2 reading adds value" 주장 가능.

근거: L1에서 staged system이 baseline 대비 +28.6% (9/9 vs 7/9). L2는 task가 더 어렵고 N이 작으므로 threshold를 낮춤.

---

## 6. Phase 5: Evaluation Set Construction (필수 — calibration/evaluation split으로 인해)

**상태 변경:** calibration/evaluation split (Section 2.6)으로 인해 Phase 5는 더 이상 "조건부"가 아님.
Evaluation set 최소 12개 pairs가 없으면 T1~T5를 계산할 수 없음.
**선행조건:** Phase 1 완료 + Rubric Freeze
**산출물:** `L2_input.csv` (evaluation set), evaluation set 선정 근거 문서

### 6.1 목표 N

| 경로 | Evaluation set | 총 N (cal+eval) | 근거 |
|---|---|---|---|
| Workshop | 12 pairs | 21 (9+12) | 최소 통계 의미 |
| Conference | 20 pairs | 29 (9+20) | Kappa CI 의미 있는 수준 |

### 6.2 Sampling Frame + Selection Rule (Codex review 반영)

> ⚠️ Codex 지적: "SUPPORT 비율 40%+ 목표로 paper 추가"는 optional stopping 위험.
> 분포가 원하는 쪽으로 맞춰질 때까지 더 뽑는 구조가 됨.

**사전 고정된 sampling frame:**
1. **Pool:** Dataset A (16) + Dataset B (42) + Dataset C (45) = 103개 논문 중 calibration 8개 제외 = **95개 후보**
2. **접근성 필터:** arXiv ID 있고 full-text 접근 가능한 것만 (paywall 제외)
3. **Claim 추출:** 각 후보 논문에 대해, citing document에서 가장 핵심적인 claim 1개만 추출
4. **추출 규칙:** claim이 가장 구체적인 것 우선 (숫자, 실험 결과, 인과 주장 > 일반적 언급)

**Selection rule (사전 고정):**
1. 접근 가능한 후보 중에서
2. Claim type별 최소 2개 확보 (stratified): factual, empirical, design, conceptual, comparison
3. 각 type 내에서 **무작위** 선정 (random.sample, seed 고정)
4. **총 12개** (workshop 기준). Conference로 확장 시 같은 규칙으로 8개 추가.

**Stopping rule:**
- 12개 도달하면 멈춤. 결과를 보고 더 뽑지 않음.
- 접근 불가(paywall, URL 다운)로 탈락 시 같은 type에서 다음 무작위 후보로 교체.
- **SUPPORT/PARTIAL 비율은 조작하지 않음.** 나온 대로 보고.

### 6.3 Task Definition: Live vs Archived Verification (Codex review 반영)

> ⚠️ Codex 지적: 로컬 복사본 사용하면 "live web verification"이 아니라 "archived-source verification".
> 혼용하면 안 됨.

**규칙:**
- **Phase 2 (Human gold):** Live access (실시간 arXiv 접근) — 이것이 "gold" 조건
- **Phase 3 (Claude + Codex):** Live access — 모델이 직접 fetch
- **Phase 4 (Baseline B3):** Live access — abstract-only이지만 같은 접근 조건
- **Source archive:** 결과 비교 시 "접근한 URL이 같은 페이지인가?" 검증용으로만 사용
  - 만약 Phase 3에서 논문 URL이 다운되어 Claude/Codex가 접근 못 하면 → 해당 pair NOT_VERIFIED 처리, N에서 제외
  - Archive를 대체 source로 주지 않음 (live access parity 유지)

**논문에 명시:**
> "All verifications used live web access at the time of execution.
> Source URLs were archived for audit purposes but not used as input to any verification step."

---

## 7. Phase 6: Cross-Model Experiment — 결과 확정 (2026-04-16)

**상태: Codex L1 실행 완료. 분석 완료. 정규화 작업 미완료.**

### 7.0 결과 요약

| | Claude | Codex | Human Gold (20개) |
|---|---|---|---|
| EXACT | 24/42 (57%) | 5/41 (12%) | 15/20 (75%) |
| PARTIAL | 9/42 (21%) | 34/41 (83%) | 4/20 (20%) |
| FAIL | 2/42 (5%) | 2/41 (5%) | 0/20 (0%) |
| NOT_VERIFIED | 7/42 (17%) | 0/41 (0%) | 1/20 (5%) |

**Session 3 해석: 능력은 동등, 기준이 다름.**
**⚠️ 주의: 이것은 가설이지 검증된 결론이 아님.**

Codex의 3-layer 분석:

| Layer | 내용 | Session 3 판단 | 실제 확인 수준 |
|---|---|---|---|
| Layer 1: Paper identification | 같은 논문을 찾았는가? | 동등 | **미검증** — Codex가 실제 fetch했는지 학습 데이터 기억인지 구분 불가 (provenance 부재) |
| Layer 2: Field verification | 어떤 필드가 다른지 발견 | 동등 | **부분 검증** — FAIL 2건(C2, E7)은 둘 다 잡았지만 severity 다름. 나머지는 정규화 후 재채점 필요 |
| Layer 3: Verdict mapping | EXACT/PARTIAL/FAIL 분류 | 완전히 다름 | **확인됨** — EXACT 57% vs 12%는 명확한 기준 차이 |

**능력 동등성을 확인하려면:**
1. L1 정규화 규칙 고정 후 재채점 → 재채점 결과에서 verdict가 수렴하면 Layer 1-2 동등 추정 강화
2. 재채점 후에도 diverge하는 case → 그게 진짜 능력 차이
3. Codex provenance 문제는 해결 불가 (재실행하면 캐시 오염) → **논문에 한계로 명시**

### 7.1 Claude 놓친 4개에 대한 Codex 결과

| 논문 | Human Gold | Claude | Codex | Codex가 잡았나? | 같은 이유? |
|---|---|---|---|---|---|
| E5 (subtitle drop) | PARTIAL | EXACT (놓침) | EXACT (놓침) | **둘 다 놓침** | — |
| I1 (EMNLP venue) | PARTIAL (venue) | EXACT (놓침) | PARTIAL (title) | 잡았지만 **다른 이유** | 아니오 |
| J9 (subtitle drop) | PARTIAL (subtitle) | EXACT (놓침) | PARTIAL (author) | 잡았지만 **다른 이유** | 아니오 |
| E9 (title phrase) | PARTIAL (title) | EXACT (놓침) | PARTIAL (author) | 잡았지만 **다른 이유** | 아니오 |
| H1 (Claude FP) | EXACT | PARTIAL (오검출) | EXACT | Codex가 맞음 | — |

**결론:** Codex가 human gold와 **같은 에러를 같은 이유로 잡은 건 0건**.
I1/J9/E9는 AUTHOR_PLACEHOLDER("(unknown)" 표기)로 잡은 것이지, venue missing이나 subtitle 누락을 잡은 게 아님.

### 7.2 NEXT_PLAN의 3가지 시나리오 → 실제 결과 매핑

| 사전 시나리오 | 실제? | 설명 |
|---|---|---|
| "Codex ≈ Claude (같은 에러, 같은 놓침)" | **부분 해당** | Layer 1-2는 동등하지만 Layer 3 기준이 달라서 verdict 분포가 극단적으로 다름 |
| "Codex가 Claude 놓친 것 잡음 → multi-model 가치" | **기각** | 잡긴 했지만 다른 이유. Human gold와 일치하는 추가 detection = 0건 |
| "Codex가 더 못함 → 모델 선택 중요" | **기각** | 능력은 동등. 기준이 다를 뿐 |

**사전 시나리오에 없던 결과:** "능력 동등 + 기준 상이" — 이것 자체가 contribution.

### 7.3 논문 contribution (조건부)

> **Cross-model comparison reveals that verdict assignment diverges dramatically without shared normalization rules (EXACT 57% vs 12%), even when both models identify the same papers and detect the same field differences. Whether this reflects pure policy divergence or underlying capability gaps requires normalization and rescoring to determine.**

확정 가능한 contribution: **정규화 규칙 없이 cross-model 비교는 무의미하다는 것 자체.**
조건부 contribution: **능력 동등성은 정규화 후 재채점 결과에 달림.**

이 발견이 L2 Phase 1 (Operational Definition Hardening)의 **존재 이유를 실증적으로 정당화**함.

### 7.4 미완료 작업: L1 정규화 규칙 고정 + 재채점

Codex가 제안한 정규화 규칙 (합리적, 채택 검토):

| 규칙 | 내용 | 현재 Claude 적용 | 현재 Codex 적용 |
|---|---|---|---|
| 약어 확장 | LLMs = Large Language Models 허용 | 허용 (EXACT) | 불허 (PARTIAL) |
| Subtitle 생략 | 콜론 이후 부분 생략 허용 | 허용 (EXACT) | 불허 (PARTIAL) |
| Venue alias | TACL vs full journal name | 허용 (EXACT) | 불허 (PARTIAL) |
| 저자 비교 | first author만 vs full list | first author 중심 | full list + (unknown) 에러 처리 |

**이 작업은 L2 Phase 1과 병렬로 실행해야 함:**
1. L1 정규화 규칙 확정
2. Claude + Codex 결과를 같은 규칙으로 재채점
3. 재채점된 결과로 P/R/F1 재계산
4. `cross_model_L1_analysis.md` 최종 작성

### 7.5 Codex 결과 → L2 Scope Decision 연결 (업데이트)

| Codex L1 발견 | 확실도 | L2 영향 |
|---|---|---|
| **기준 상이 (Layer 3)** | 확인됨 | → L2 Phase 1(정의 고정)이 최우선. 정의 없이 어떤 실험도 무의미 |
| **능력 동등 (Layer 1-2)** | **미검증 가설** | → 정규화 후 재채점까지는 multi-model 효과 판단 보류 |
| **E5 공통 약점 (subtitle drop)** | 확인됨 | → L2에서도 비슷한 "공통 맹점" 존재 가능 → gold standard에서 발견해야 함 |
| **정규화 없이 비교 무의미** | 확인됨 | → L1/L2 모두 정규화 규칙 선행 필수 |
| **AUTHOR_PLACEHOLDER 에러** | 확인됨 | → L2에서도 "catalog artifact vs real error" 구분 필요 |
| **Codex provenance 불명** | 해결 불가 | → 논문에 한계 명시. 능력 비교 주장 약화 |

**Scope decision 업데이트:** 경로 B(feasibility) 여전히 추천하지만, 근거가 "multi-model 효과 없음"에서 **"정규화 전이라 판단 불가, 보수적으로 B"**로 변경.

### 7.6 Contamination 사후 검증 결과

- [x] Codex에 `codex_L1_input.csv`만 제공
- [x] 프롬프트에 "다른 파일 접근 금지" 명시
- [x] **사후 검증:** Codex가 I1/J9/E9를 잡은 이유가 human gold와 다름 → contamination 증거 없음
- [x] Codex 스스로 provenance 문제 인정 (live fetch vs 학습 데이터 구분 불가)
- **Provenance 한계:** Codex 결과에 Source_URL/Verification_Basis 컬럼 없음. 재실행 시 추가하면 캐시 오염. → **논문에 한계로 명시**

---

## 8. Execution Order & Dependencies

```
[완료] Phase 6: Codex L1 ──→ 결론: 기준 상이 확인, 능력 동등은 미검증
  │
Phase 1: Operational Definition Hardening (Session A) ← **최우선**
  ├── L2 decision tree + edge case bank + PARTIAL-MAJOR/MINOR
  ├── L1 정규화 규칙 (병렬)
  ├── L2_input.csv 생성
  ├── Claude L2 prompt 확정
  ├── Codex L2 prompt 확정 (definition 부분 동일해야 함)
  │
  ├──→ Phase 2: Human Gold Standard (Phase 1 필수, Session A에서 가능)
  │     ├── 산출물: gold_standard_L2.csv
  │     │
  │     ├──→ Phase 3: Claude + Codex 독립 L2 실행 (Phase 1 필수)
  │     │     ├── Session B: Claude L2 (새 세션, input만)
  │     │     ├── Session C: Codex L2 (별도, input만) ← **B와 병렬**
  │     │     ├── Session D: 3-way 비교 분석
  │     │     │
  │     │     └──→ Phase 4: Baseline Comparison (Phase 2 필수)
  │     │           └──→ Phase 5: Sample Expansion (조건부)
  │     │
  │     └── [3-way 불일치 3건+ → Phase 1로 돌아감]
  │
  └──→ L1 재채점 → cross_model_L1_analysis.md
```

**Critical path:** Phase 1 → Phase 2 + Phase 3(병렬) → Phase 4
**핵심 변경 (2026-04-16):**
- Phase 3이 단순 clean re-run에서 **Claude+Codex 독립 실행 + 3-way 비교**로 확장
- Inter-model agreement를 cross-model reproducibility check으로 사용 (inter-rater 대체가 아닌 보충 신호) (1인 연구의 현실적 해법)
- Session isolation protocol 추가 (A→B/C→D)
- 새 threshold T5 추가 (Claude vs Codex ≥75%)
- Phase 2(gold)와 Phase 3(독립 실행)은 **병렬 가능** — gold는 Session A에서, 독립 실행은 B/C에서

### Master Plan (experiment_master_plan.md) 연결

| Master Plan Step | 상태 | 이 플랜과의 관계 |
|---|---|---|
| Step 1 (CiteAudit) | ✅ Done | 직접 관련 없음 |
| Step 1.5 (L1 clean re-run) | ✅ Done (91.9%) | L2 Phase 3의 protocol 참고 |
| Step 2-3 (cross validation) | ✅ Done | L2 baseline 설계 참고 |
| Step 2.5 (baseline comparison) | ✅ Done | L2 Phase 4의 baseline 프레임 참고 |
| Step 2.6 (error taxonomy) | ✅ Done | L2 Phase 1의 decision tree 기반 |
| Step 4 (L1 gold standard) | ✅ Done (20개) | L2 Phase 2의 protocol 복제 |
| Step 5 (L2 execution) | ✅ Done (8개) | **이 플랜의 검증 대상** |
| Step 6 (statistics) | ✅ Done | L2 metrics 설계 참고 |
| Step 7 (Dataset C) | ✅ Done | L2 Phase 5 확장 시 paper pool |
| Step 8 (integration) | Partial | L2 검증 결과가 여기로 합류 |
| **Codex L1 cross-model** | ✅ 실행 완료, 정규화 미완 | Phase 6 결과 확정: 능력 동등, 기준 상이. L1 정규화 + 재채점 필요 |

---

## 9. Pre-registered Thresholds (사전 등록) — Codex review 반영

### 9.1 Primary vs Secondary Endpoints (Codex review 반영)

> ⚠️ Codex 지적: 5개 threshold를 모두 동등하게 취급하면 multiple comparison 문제.
> Primary endpoint 1개를 지정하고, 나머지는 secondary로 내려야 함.

**PRIMARY:** T1 (Gold standard agreement) — 이것만 논문 본문의 success/fail을 결정
**SECONDARY:** T2, T3, T5 — 추가 정보, threshold FAIL해도 논문에서 L2 제거하지 않음
**SAFETY:** T4 — 심각 불일치 감시, FAIL 시 해당 case 원인 분석 필수

### 9.2 Count-based + CI 병기 (Codex review 반영)

> ⚠️ Codex 지적: N=12에서 한 케이스가 agreement를 8%p 흔듦. % threshold만으로는 불안정.

**모든 threshold를 % 기준 + count 기준 + 95% CI로 3중 보고:**

| # | Type | Metric | % Threshold | Count Threshold (N=12 기준) | 95% CI 보고 | PASS 시 | FAIL 시 |
|---|---|---|---|---|---|---|---|
| T1 | **PRIMARY** | Human vs Claude agreement (parent-class) | ≥70% | ≥9/12 일치 | Wilson interval 필수 | L2 credible | L2 = "feasibility only" |
| T2 | Secondary | Claude re-run agreement | ≥80% | ≥10/12 일치 | Wilson interval | Process reproducible | Decision tree 재설계 |
| T3 | Secondary | Full-text vs abstract-only: gold 기준 paired accuracy improvement | — | Full-text가 gold와 **2건+ 더 일치** | McNemar's test p-value | "L2 reading adds value" | "Abstract-only may suffice" |
| T4 | Safety | SUPPORT↔REFUTE 역전 | 0건 | 0건 | — | OK | 원인 분석 필수 |
| T5 | Secondary | Claude vs Codex agreement (parent-class) | ≥70% | ≥9/12 일치 | Wilson interval | "Cross-model reproducible" | "Definition still ambiguous" |

**T3 수정 근거 (Codex review):**
- 이전 T3 "PARTIAL detection +2건"은 PARTIAL 남발로 gaming 가능
- 새 T3: **gold standard 대비 paired accuracy** — full-text Claude vs abstract-only Claude, 각각 gold와 비교
- McNemar's test로 유의성 검정 (paired data이므로)
- N=12에서 McNemar's power가 낮지만, 방향 + effect size 보고

**T5 하향 조정:** 75% → 70%. Codex 지적 반영 — cross-model agreement는 inter-rater 대체가 아니라 보충 신호. L1과의 일관성보다 현실적 기대치가 중요.

### 9.3 실패 대응 매트릭스 (T1 중심)

| T1 (PRIMARY) | T2 | T5 | 의미 | 대응 |
|---|---|---|---|---|
| ✓ | ✓ | ✓ | 완전 성공 | 논문에 L2 포함, Phase 5 확장 고려 |
| ✓ | ✓ | ✗ | Gold 일치 + 재현 가능, 모델 간 차이 | 성공. "model-specific interpretation exists" 부기 |
| ✓ | ✗ | ✓ | Gold 일치 + 모델 간 일치, 재현 불안정 | 성공이나 "session context dependency" 부기 |
| **✗** | ✓ | ✓ | 모델끼리 일치하지만 Human과 불일치 | **PRIMARY FAIL**이지만 **가장 흥미로운 결과** — LLM 공통 맹점. L2 포함하되 "LLM common blind spot" framing |
| **✗** | ✗ | ✗ | 전면 실패 | **PRIMARY FAIL** — L2를 "exploratory pilot"로 격하 |
| ✓ | ✗ | ✗ | Gold만 일치 | 성공이나 Decision tree 모호 → 강화 필요 부기 |

**PRIMARY FAIL (T1 ✗) 대응 원칙:**
- T1 FAIL = L2가 논문 본문의 **주장(claim)**에서 제외됨
- 단, L2 데이터 자체는 보고 (Results에서 Discussion으로 이동)
- T1 FAIL + T5 PASS = 특수 case: LLM 공통 한계 자체가 finding

---

## 10. 논문 Positioning 시나리오

검증 결과에 따른 논문 서술 전략:

### 시나리오 A: 모든 threshold PASS
> "We validate both metadata verification (L1, N=98) and claim-evidence alignment (L2, N=15+) with pre-registered thresholds. L2 adds value over abstract-only baselines."

### 시나리오 B: T1+T2 PASS, T3 FAIL
> "L2 process is reproducible and agrees with human judgment, but abstract-only analysis may suffice for this sample. Full-text reading's value requires larger-scale validation."

### 시나리오 C: T1 FAIL
> "L2 claim-evidence alignment remains an open challenge. Our pilot identifies inferential overreach as the dominant error type, but LLM-based detection does not yet match human judgment reliably."

### 시나리오 D: 전면 실패
> "We demonstrate that L1 metadata verification is reliable (N=98, P=91.7%), while L2 semantic verification is premature for automation. This boundary itself is a contribution."

### 시나리오 E: L2 완전 삭제 (Gap 8)
> **조건:** T1+T2+T3 전부 FAIL + Phase 1 calibration에서 기존 verdict 3개+ 변경
> L2를 논문 본문에서 제거. Discussion의 "Future Work" 1문단으로 축소.
> "We attempted L2 claim-evidence verification but found the task too subjective for reliable automation at this scale."
> L2 pilot 데이터는 supplementary material로 공개 (투명성).

**핵심:** 어떤 결과가 나와도 논문에 쓸 수 있도록 framing을 미리 준비.

---

## 11. Checklist Before Execution

### 즉시 (Phase 1 시작 전)
- [ ] Phase 1 decision tree 초안 작성
- [ ] Phase 1 calibration (기존 9개 claim-source pair를 decision tree로 재판정)
- [ ] Edge case bank 8개 이상 작성
- [ ] Pre-registered thresholds (T1~T4) 최종 확인 + 날짜 기록 (HARKing 방지)

### Codex 결과 (완료 — 잔여 작업)
- [x] ~~Codex input 파일 격리~~ (codex_L1_input.csv로 이미 격리 완료)
- [x] `codex_L1_results.csv` 형식 검증 (41행)
- [x] Contamination check — 통과 (human gold와 같은 이유로 잡은 건 0건)
- [x] Claude L1 결과와 비교표 생성 (Session 3에서 완료)
- [ ] **L1 정규화 규칙 확정** (`normalization_rules_L1.md`) ← Phase 1과 병렬
- [ ] 정규화 후 Claude + Codex 재채점 (`cross_model_L1_rescored.csv`)
- [ ] 재채점 기준 P/R/F1 재계산
- [ ] `cross_model_L1_analysis.md` 최종 작성

### Phase 0 결정 시 (Phase 1 + Codex 결과 이후)
- [ ] Scope decision (경로 A vs B) 확정 + 근거 문서화
- [ ] Phase 2 blinded input 파일 생성 (judgment/Key_Finding 컬럼 제거)
- [ ] Phase 2 추가 paper 후보 리스트 작성 (경로 A면 필요)
- [ ] 각 Phase 산출물 파일명 확정

---

## 12. Known Gaps & Fixes (자체 검토)

이 플랜을 다시 검토하면서 발견한 빈틈들.

### Gap 1: PARTIAL 압도적 편향 (78%)

현재 9개 중 7개가 PARTIAL. 이 상태에서:
- "항상 PARTIAL이라고 답해라" baseline이 78% agreement를 달성
- Phase 4의 B0(Random) baseline이 사실상 trivial하지 않음 — 이미 높음
- SUPPORT precision은 N=2로 의미 없음

**Fix:**
- Phase 4의 B0 baseline을 "majority class baseline (항상 PARTIAL)"로 명시 변경
- T3 threshold 재검토: full-text가 majority baseline 대비 +15%p면 93% 이상이어야 함 — 비현실적
- **T3 수정 제안:** "Full-text가 abstract-only(B3) 대비 PARTIAL detection에서 +2건 이상 추가 발견" (absolute count 기반)
- Phase 5에서 SUPPORT 비율을 40%+ 목표로 paper 추가 (class balance)

### Gap 2: I1-a와 I1-b 독립성 문제

같은 논문(Tam et al.)에서 2개 claim. 독립 관측이 아님.
- 같은 source를 읽었으므로 access/hallucination 에러가 correlated
- I1-b의 Time_Min=0 (I1-a 읽으면서 동시 판정)

**Fix:**
- 통계 보고 시 "9 claim-source pairs from 8 unique papers" 명시
- Within-paper pairs는 sensitivity analysis에서 1개로 묶어 재계산 (N=8 기준)
- Phase 5 확장 시 1 paper = 1 claim 원칙 (multi-claim은 가장 중요한 것 1개만)

### Gap 3: Clean Re-run의 Claim Identification 일관성

Phase 3에서 새 세션이 같은 논문을 읽되, **다른 claim을 추출**할 수 있음.
- 예: B1에서 "scaling law" 대신 "collaborative efficiency" claim을 잡으면 — 이건 불일치인가?

**Fix:**
- Phase 3 input에 **claim text도 포함** (논문 ID + claim text). 새 세션은 claim을 추출하는 게 아니라, 주어진 claim에 대해 판정만 하게 함
- 이렇게 하면 claim identification reproducibility와 judgment reproducibility를 분리할 수 있음
- Claim identification 일관성은 별도 실험이 필요 (이 플랜 scope 밖 — future work)

### Gap 4: REFUTE/UNCERTAIN 빈 카테고리

Decision tree에 4개 branch가 있지만 REFUTE 0건, UNCERTAIN 0건.
- Calibration 불가 — tree가 이 경우에 작동하는지 알 수 없음

**Fix:**
- Phase 1 edge case bank에 **합성 REFUTE/UNCERTAIN 사례 2개씩** 추가
  - REFUTE 예: "source says X decreases performance" but claim says "X improves performance"
  - UNCERTAIN 예: source is tangentially related, neither supports nor refutes
- 이들은 실제 데이터가 아니라 calibration용 — 논문 N에는 포함하지 않음
- 논문에 "our sample contained no REFUTE/UNCERTAIN cases; this limits generalizability to these categories" 명시

### Gap 5: PARTIAL 내 심각도 미분류

B1의 PARTIAL(lazy loading을 원문이 언급조차 안 함 = **fabricated attribution**)과
S-02의 PARTIAL(proposal을 norm으로 격상 = **status inflation**)은 심각도가 다름.

**Fix:**
- PARTIAL을 2단계로 세분화:
  - `PARTIAL-MAJOR`: 원문이 claim의 핵심을 지지하지 않음 (B1: lazy loading 언급 없음)
  - `PARTIAL-MINOR`: 원문이 claim을 지지하되 범위/조건/지위를 과장 (S-02: proposal→norm)
- Decision tree Step 3 이후에 Step 3b 추가:
  ```
  3b. 원문이 claim의 핵심 개념을 명시적으로 다루는가?
      ├── NO → PARTIAL-MAJOR (attribution gap)
      └── YES but overstated → PARTIAL-MINOR (overstatement)
  ```
- 논문 기여: "PARTIAL is not monolithic — we distinguish attribution gaps from overstatements"

### Gap 6: Phase 1 calibration이 verdict를 바꿀 경우

Decision tree로 재판정 시 기존 verdict가 바뀌면 (예: I1-b PARTIAL → SUPPORT):
- PARTIAL 비율이 변함 → B0 baseline 변함 → T3 threshold 변함
- 기존 결과와 새 결과 중 어떤 것이 "official"인지 불명확

**Fix:**
- **Phase 1 calibration 결과가 official version.** v0.1 판정은 "pre-calibration"으로 기록
- Verdict 변경 시: old verdict, new verdict, 변경 이유를 `calibration_log_L2.md`에 기록
- Pre-registered threshold는 calibration 이후의 분포 기준으로 계산
- **중요: threshold는 calibration 전에 설정, calibration 후 분포로 다시 확인. 둘이 충돌하면 더 보수적인 쪽 채택**

### Gap 7: Source Access Failure 대응

Re-run 시 논문 URL이 다운되거나 paywall 생길 수 있음.

**Fix:**
- Phase 2 시작 전에 8개 논문 전체의 **PDF/HTML 로컬 복사본** 보관
- Phase 3 re-run에서도 같은 복사본 사용 (URL 접근 차이로 인한 불일치 제거)
- 논문에 "all sources were accessed on [date] and archived locally" 명시

### Gap 9: Codex "능력 동등" 가설 미검증 (2026-04-16 추가)

Session 3가 "Layer 1-2 동등"이라고 결론냈지만:
- Codex의 provenance 불명 (실제 fetch vs 학습 데이터 기억)
- 정규화 전이라 verdict 차이가 기준 차이인지 능력 차이인지 분리 안 됨
- FAIL 2건(C2, E7)에서 둘 다 잡았지만 severity 판정이 다름 → 이것도 기준인지 능력인지 불명

**Fix:**
- 플랜 전체에서 "능력 동등"을 사실이 아닌 **가설**로 표기
- L1 정규화 후 재채점 → 수렴 여부로 가설 검증
- 재채점 후에도 diverge하는 case가 3건+ 이면 "능력 차이 존재" 보고
- Codex provenance는 해결 불가 → 논문에 한계 명시 ("we cannot verify whether Codex performed live verification or relied on pre-training knowledge")

### Gap 10: L1 정규화 작업이 플랜에 없었음 (2026-04-16 추가)

Codex 결과 전에는 L1 정규화가 필요 없었음. 이제 필수.
Phase 1에 Section 2.3으로 추가 완료. 병렬 산출물로 `normalization_rules_L1.md` + `cross_model_L1_rescored.csv`.

### Gap 8: L2 섹션 완전 삭제 시나리오 없음

시나리오 D("L2는 premature")는 있지만, "L2를 논문에서 완전히 빼는" 옵션이 없음.

**Fix:**
- 시나리오 E 추가:
  > **T1 FAIL + Phase 1 calibration에서 기존 verdict 3개+ 변경:**
  > L2를 논문 본문에서 제거. Discussion의 "Future Work" 1문단으로 축소.
  > "We attempted L2 claim-evidence verification but found the task too subjective for reliable automation at this scale."
- 이 시나리오에서도 L2 pilot 데이터 자체는 supplementary material로 공개 (투명성)

---

### Codex Peer Review에서 추가된 Gaps (2026-04-16)

### Gap 11: Inter-model agreement ≠ inter-rater agreement

Claude와 Codex는 shared pretraining, 유사한 검색 습관으로 correlated errors 가능.
**Fix:** 플랜 전체에서 "inter-rater replacement" → "cross-model reproducibility check"로 변경. 완료.

### Gap 12: Calibration/evaluation set 미분리

기존 9개로 tree 다듬고, 같은 9개로 평가하면 test set leakage.
**Fix:** Section 2.6에서 분리. 기존 9개 = calibration only, evaluation = 새 12+ pairs. 완료.

### Gap 13: Gold standard pseudo-independence

같은 사람이 rubric 만들고 gold rating. Memory leakage.
**Fix:** Evidence-first protocol (Section 3.1 Step 4). 한계 명시 필수. 완료.

### Gap 14: Tiny N으로 % threshold 불안정

N=12에서 1건 = 8%p. 70% vs 75% threshold 구분이 무의미할 수 있음.
**Fix:** Count + % + 95% CI 3중 보고 (Section 9.2). 완료.

### Gap 15: T3 gaming 가능

PARTIAL 남발하면 T3 PASS. 검출 능력이 아니라 기준 관대함을 측정하게 됨.
**Fix:** T3를 gold 기준 paired accuracy improvement로 변경 (Section 9.2). 완료.

### Gap 16: Rubric drift during parallel execution

Phase 2-3 병렬 중 decision tree, prompt, tool policy 중 하나라도 바뀌면 moving target.
**Fix:** Rubric Freeze Gate (Section 2.7). git tag + change log. 완료.

### Gap 17: Prompt/tool parity 부재

Claude와 Codex는 모델 비교가 아니라 모델+도구+프롬프트 패키지 비교.
**Fix:** Section 4.4.1 parity checklist. 도구 차이 논문 명시. 완료.

### Gap 18: Optional stopping in Phase 5

"SUPPORT 40% 목표"는 결과 보면서 더 뽑는 구조가 됨.
**Fix:** Section 6.2에 sampling frame + selection rule + stopping rule 사전 고정. 완료.

### Gap 19: T4 = 0 reversals가 공허

REFUTE 사례가 없으면 자동 PASS.
**Status:** 부분 해결. Synthetic calibration case는 있지만 evaluation set에 reversal 가능 case가 있을지는 sampling 결과에 달림. 논문에 "T4 was trivially satisfied due to absence of REFUTE cases in our sample" 명시 필요.

### Gap 20: Archived copy vs live access 혼동

로컬 복사본 = "archived-source verification" ≠ "live web verification".
**Fix:** Section 6.3에서 task definition 분리. Archive는 audit용만. 완료.

---

## 13. 현재 NEXT_PLAN과의 차이

| NEXT_PLAN 항목 | 이 플랜에서 |
|---|---|
| "사람이 같은 8개 논문 읽고 판정" | Phase 2: blinding protocol + 기록 형식 + 불일치 분석 protocol 구체화 |
| "2명+ 독립 판정" | 1인 연구 현실 반영 → blinded self-rating + clean re-run으로 대체. Inter-rater는 N≥20일 때만 의미 있음 |
| "inferential overreach 기준 문장화" | Phase 1: decision tree + materiality test + edge case bank + calibration |
| "새 세션에서 재실행" | Phase 3: 구체적 protocol + 불일치 허용 기준 + 대응 절차 |
| "abstract만 읽고 판정 비교" | Phase 4: 4개 baseline + pre-registered threshold |
| "full validation으로 갈지 판단" | Phase 0: 경로 A/B + 시나리오별 논문 positioning |
| Codex 실험 | Phase 6: 별도 트랙, contamination control 강화 |
| (없었음) | Pre-registered thresholds 4개 + 실패 대응 매트릭스 |
| (없었음) | 실행 순서 + 의존관계 그래프 |
| (없었음) | 논문 positioning 시나리오 4개 |
