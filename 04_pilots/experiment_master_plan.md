# Plan: Research Verification System — Full Experiment + Paper Preparation

## Context

연구 검증 시스템(research-system)의 논문화를 위해 실험을 완성해야 한다. 현재 상태:

**Done:**
- Level 1 수동 검증: Dataset A (16개) + Dataset B (37개) = 53개
- 에러 발견: 9/37 (24%), 4/16 (25%)
- Pilot 1 GPT replication

**Missing (리뷰어 reject 사유):**
1. Human gold standard 없음 → precision/recall 계산 불가
2. CiteAudit (arXiv:2602.23452) 대비 novelty 불명확
3. N=53, 통계적 검정력 부족
4. 교차 검증 안 됨 (두 시스템 × 두 데이터셋)
5. Level 2 미실행 (4-level 중 2개만 테스트)

**새로 발견된 사실:**
- meta-architect에 `verify_papers.py`가 이미 있음 (arXiv API + Semantic Scholar API 자동 검증)
- CiteAudit: 9,442 citations, 97% accuracy, 100% recall, multi-agent pipeline

---

## Cache Elimination Protocol

공정한 비교를 위해 모든 실험에서 캐시를 제거해야 함:

### 1. meta-architect verify_papers.py 실행 시
- `papers.yaml`의 `status` 필드를 전부 `unverified`로 리셋한 **복사본** 사용
- `research/verified/` 디렉토리 비우기 (원본은 건드리지 않음 — 복사본에서)
- `verified_date`, `citation_count`, `semantic_scholar_id` 등 auto-fill 필드 제거
- **실행 방법:** research-system 내에 `temp_clean_run/` 디렉토리 만들어서 격리 실행
- 원본 meta-architect 파일 절대 수정 금지

### 2. research-system Level 1 재실행 시
- **새 세션**에서 실행 (이전 대화 컨텍스트 없는 상태)
- 이전 pilot 결과 파일을 참조하지 않는 프롬프트 사용
- WebFetch 결과는 캐시 없음 (매번 live fetch)

### 3. LLM 메모리 캐시
- Claude/GPT의 학습 데이터에 논문 정보가 있을 수 있음 (pre-training cache)
- 이건 제거 불가능 — **한계로 명시**
- 완화: API-based verification (verify_papers.py)은 LLM 메모리와 무관하게 arXiv API 결과만 사용

### 4. 실험 기록 시 명시할 것
- 각 실험의 캐시 상태 (clean/cached)
- 사용한 API 엔드포인트 + 응답 시간
- LLM 모델 버전 (Claude Opus 4.6 등)
- 세션 격리 여부

---

## Execution Plan (8 Steps)

### Step 1: CiteAudit 논문 정독 + 차별화 확정
**왜:** Reject 2 방어. 가장 직접적 경쟁자 — 읽지 않고 논문 쓸 수 없음.
**할 일:**
- `WebFetch`로 https://arxiv.org/abs/2602.23452 HTML 전문 읽기
- 차별점 정리 (우리 = 비용 기반 단계적 방법론, CiteAudit = 자동 탐지 도구)
- `05_evidence/source_tables/competitor_analysis.md`에 기록
**산출물:** competitor_analysis.md
**시간:** ~30분

### Step 1.5: research-system Level 1 clean re-run (Dataset A + B)
**왜:** 현재 Pilot 1과 MA-L1 결과는 이 대화 세션에서 나옴 — 이전 논의 컨텍스트가 cache로 작동. 공정 비교를 위해 새 세션에서 재실행 필요.
**할 일:**
- **새 Claude 세션** 열기 (이 대화 컨텍스트 없이)
- 프롬프트: "이 CSV의 논문 목록을 arXiv/웹에서 Level 1 검증해줘" (방법론만 제공, 이전 결과 안 줌)
- Dataset A (16개) 재실행
- Dataset B (37개) 재실행
- 이전 결과와 일치율 계산 (재현성 지표)
**산출물:** `04_pilots/clean_rerun_L1_A.csv`, `04_pilots/clean_rerun_L1_B.csv`, 일치율 보고
**시간:** ~2시간
**사전 성공 기준:**
- ≥90% 일치: robust (프로세스 신뢰 가능)
- 80-89% 일치: acceptable, 차이 원인 분석 + limitation 기록
- <80% 일치: context dependency 문제 → limitation으로 보고, 실험 설계 재검토
**의미:** 만약 clean run 결과가 이전과 동일하면 → 프로세스가 robust. 다르면 → 컨텍스트 의존성 문제 발견.

### Step 2: meta-architect verify_papers.py를 Dataset A(16개)에 실행
**왜:** 교차 검증 매트릭스 빈 칸 채우기. meta-architect 시스템의 성능을 다른 데이터셋에서 측정.
**할 일:**
- research-system의 16개 소스를 papers.yaml 형식으로 변환
- **캐시 제거:** 새 papers.yaml에 status=unverified, auto-fill 필드 비움
- `temp_clean_run/` 디렉토리에서 격리 실행
- `verify_papers.py` 실행 (arXiv API + Semantic Scholar)
- 결과를 research-system Level 1 결과와 비교
**산출물:** `04_pilots/cross_validation_MA_on_A.md` + CSV
**시간:** ~1시간
**주의:** meta-architect 원본 코드/데이터 수정 금지 — 복사본에서 실행

### Step 3: meta-architect verify_papers.py를 Dataset B(37개)에 clean run
**왜:** 기존 VERIFIED 태그 = cache. 태그 무시하고 처음부터 실행해야 공정 비교.
**할 일:**
- `verify_papers.py --summary` 현재 상태 기록 (before snapshot)
- **캐시 제거:** papers.yaml 복사 → 모든 status를 unverified로, verified_date/citation_count/semantic_scholar_id 제거
- `research/verified/` 빈 디렉토리로 복사
- `temp_clean_run/` 에서 격리 실행
- `verify_papers.py` 전체 실행 (arXiv API + Semantic Scholar — fresh API calls)
- 결과를 research-system Level 1 결과와 비교
- **핵심 질문:** research-system이 잡은 9개 에러를 verify_papers.py도 잡는지?
  - C2 저자 오류 (Li → Salemi): verify_papers.py의 author matching이 잡나?
  - E7 저자 오류 (Zhao → Gao): 같은 질문
  - E6 venue 인플레이션: verify_papers.py는 venue를 체크하나?
**산출물:** `04_pilots/cross_validation_MA_on_B.md` + CSV
**시간:** ~1시간

### Step 2.5: Baseline Script 비교 (핵심 — 아키텍처 정당화)
**왜:** "arXiv API 5줄이면 되는 거 아니냐?" 반론 방어. 이것 없이는 시스템 존재 이유 없음.
**할 일:**
- **Baseline 1 (ID match):** DOI / arXiv ID exact match만으로 존재 확인 → 가장 단순
- **Baseline 2 (metadata match):** title + first author + year exact/near-exact → 구조적이지만 단순
- **Baseline 3 (fuzzy match):** title Jaccard similarity only → title 유사도만으로 판단
- **System A (research-system L1):** 구조적 검증 (title + author + venue + year + arXiv ID 전체 대조 + LLM 판단)
- **System B (meta-architect verify_papers.py):** arXiv API + Semantic Scholar API 자동 검증
- **5개를 Dataset A + B에 전부 돌려서 비교**
- 측정: 각 시스템별 에러 탐지 수, FP, FN, 시간
- **핵심 분석: "failure regime" 분리** — 어떤 에러는 baseline으로 충분하고, 어떤 에러만 staged system이 필요한지
**산출물:** `04_pilots/baseline_comparison.md` + CSV + failure regime 분석
**시간:** ~2시간 (baseline 스크립트 작성 + 실행)
**Contribution framing:** "항상 더 좋다"가 아니라 "cheap baseline이 커버하는 영역 vs architecture가 필요한 failure regime을 분리했다"

### Step 2.6: Error Taxonomy Formalization
**왜:** EXACT/PARTIAL/FAIL은 너무 거침. 세분화 없이는 CiteAudit과 차별화 불가.
**할 일:**
- 기존 결과를 새 taxonomy로 재분류:
- **축 1: Metadata Correctness**
  - `fabricated_reference` — 존재하지 않는 논문
  - `author_mismatch` — 저자 완전 오류 (다른 사람)
  - `title_mismatch` — 제목이 다른 논문과 혼동됨
  - `venue_inflation` — citation reports a stronger venue/status than justified by the verified record
  - `venue_drift` — paper is real, but catalog not updated after later publication state change
  - `identifier_mismatch` — DOI, arXiv ID, year, volume, pages 오류
- **축 2: Claim Support Correctness** (Level 2에서 측정)
  - `semantic_support` — 논문이 claim을 실제로 뒷받침함
  - `partial_support` — 부분적으로만 뒷받침
  - `semantic_mis_support` — 논문은 맞지만 claim을 뒷받침 안 함
  - `contradicts` — 논문이 claim을 반박함
- **각 유형에 operational definition 문장으로 고정**
- Dataset A + B 전체 재분류
- CiteAudit taxonomy와 비교 테이블
**산출물:** `04_pilots/error_taxonomy.md` + 재분류된 CSV
**시간:** ~1시간

### Step 4: Human Gold Standard 구축 (20개)
**왜:** Reject 1 방어. 이것 없으면 논문 불가.
**할 일:**
- 53개 중 20개 선별 (EXACT 8개 + PARTIAL 7개 + FAIL 2개 + NOT_VERIFIED 3개 — 분포 반영, PARTIAL 충분히 확보)
- 각 논문의 arXiv 페이지를 직접 열어 확인 (사람이)
- ground truth 라벨: 새 error taxonomy 기준 + 근거
- **삼자 비교:** Human label vs Claude verdict vs GPT verdict → Fleiss' Kappa
- research-system L1, meta-architect verify_papers.py, baseline script 각각의 precision/recall/F1 계산
- **verifier error rate** 명시적 계산 (Claude가 틀린 건수)
**산출물:** `05_evidence/gold_standard_10.md` + `04_pilots/precision_recall_report.md`
**시간:** ~2시간 (사람 작업)
**중요:** 사용��가 직접 arXiv 페이지에서 확인 (LLM 순환 방지)
**확정:** 사용자가 10개 직접 검증하기로 결���

### Step 5: Level 2 실행 (5개 — dogfooding 포함)
**왜:** 4-level 프레임워크에서 Level 2 가치 증명. CiteAudit와의 차별점.
**할 일:**
- `pilot2_L2_plan.md`의 Step 0: Level 2 checklist 확정
- 5개 선별 (research-system 자체 소스 2개 + meta-architect 논문 3개)
  - 자체: S-02 PRISMA-trAIce, C-04 Automation Bias
  - MA: A3 Hegazy (VERIFIED인데 venue PARTIAL), B1 Qian (⚠️ 수식 미확인), I1 Tam (key claim)
- 각 논문 원문(arXiv HTML) 읽기 → claim-evidence alignment
- 시간 측정 (wall-clock per paper)
- **Downstream impact analysis:** 발견된 에러 중 2-3개에 대해 "이 citation error 때문에 어떤 design claim이 약화되었고, 어떤 system choice가 재검토되었는지" 구체적 사례 제시
  - 예: E7 "Zhao et al." 저자 오류 → meta-architect 설계서에서 이 논문을 인용한 결정의 traceability가 깨짐
  - 예: E6 venue inflation → Phase 4 설계의 근거 신뢰도가 달라짐
**산출물:** `04_pilots/pilot_L2_report.md` + CSV + `04_pilots/level2_checklist_v0.1.md` + downstream impact 섹션
**시간:** ~3시간

### Step 6: 통계 분석
**왜:** Reject 3 부분 방어. N=53은 작지만 effect size가 크면 유의.
**할 일:**
- 95% CI 계산 (error rate)
- Cohen's Kappa: research-system L1 vs meta-architect verify_papers.py 일치도
- Cohen's Kappa: Claude vs GPT (Pilot 1 데이터)
- McNemar's test: 두 시스템 간 에러 탐지 차이 유의성
- Fisher's exact test: VERIFIED vs UNVERIFIED 에러율 차이
**산출물:** `04_pilots/statistical_analysis.md`
**시간:** ~1시간

### Step 7: 추가 데이터셋 확보 (독립 프로젝트)
**왜:** Reject 3 강화. 같은 생태계(meta-architect)에서만 테스트하면 편향.
**할 일:**
- **Dataset C-1:** LLM에게 CS 주제(예: "federated learning 2024-2025")로 20개 논문 목록 생성시키고 검증
- **Dataset C-2:** 공개된 awesome-list (github)에서 논문 목록 가져와 검증
- **Dataset C-3:** 비-CS 도메인 (PubMed 의학 논문 5-10개) — 도메인 편향 통제
- 전부 실행 (사용자 확정)
- 비-CS 도메인에서 Level 1 적용 한계가 발견되면 그 자체가 finding
- Level 1 실행 → 기존 결과와 에러율 비교
**산출물:** `05_evidence/source_tables/dataset_C_*.md` + pilot report
**시간:** ~2시간

### Step 8: 최종 결과 통합 + 논문 뼈대
**왜:** 모든 실험 결과를 하나로.
**할 일:**
- 전체 교차 검증 매트릭스 완성:
  ```
                      research-system    meta-architect    HUMAN
                      L1      L2         verify_papers.py  gold
  Dataset A (16)      ✅      ✅(2개)     ✅                ✅(5개)
  Dataset B (37)      ✅      ✅(3개)     ✅                ✅(5개)
  Dataset C (20+)     ✅      -          ✅                -
  ```
- README 업데이트 (결과 반영)
- 논문 뼈대: Abstract, Introduction, Method, Experiments, Results, Discussion, Limitations
- GitHub push
**산출물:** Updated README + `04_pilots/paper_outline.md`
**시간:** ~1시간

---

## 우선순위 체크리스트

### 논문 필수 (없으면 reject)
- [Step 4] Human gold standard → precision/recall
- [Step 1] CiteAudit 차별화
- [Step 6] 통계 분석 (최소 CI + Kappa)

### 실험 완성 (없으면 약함)
- [Step 2+3] 교차 검증 (두 시스템 × 두 데이터셋)
- [Step 5] Level 2 실행 (프레임워크 완성)
- [Step 7] 독립 데이터셋 (N 확대)

### 패키징 (없으면 비전문적)
- [Step 8] 통합 보고서 + 논문 뼈대

---

## 실행 순서 (의존성 기반)

```
Step 1   (CiteAudit) ──────────────────────────────────────┐
Step 1.5 (RS clean re-run A+B) ──┐                          │
Step 2   (MA on A) ──────────────┤                          │
Step 3   (MA on B) ──────────────┤── Step 6 (통계) ──┐      │
Step 4   (Gold 10개) ────────────┘                    │      │
Step 5   (Level 2, 5개) ───────────────────────────── ┤      │
Step 7   (Dataset C) ─── Step 6 ──────────────────── ┤      │
                                                      └── Step 8 (통합) ◄──┘
```

**병렬 가능:** Step 1, 1.5, 2, 3, 7 (독립)
**의존 (강제 순서):**
- Step 2.6 (Taxonomy) → Step 4 (Gold Standard) — taxonomy 확정 후 labeling
- Step 2.5 (Baseline) → Step 6 (통계) — baseline 결과 필요
- Step 4 (Gold) → Step 6 (통계) — human label 필요
- Step 6 → Step 8 (통합)
- Step 1 (CiteAudit) → Step 8 (포지셔닝 반영)

### 완성된 교차 매트릭스

```
                    research-system             meta-architect system      HUMAN
                    L1(cached) L1(clean) L2     verify_papers.py(clean)    gold
Dataset A (16)     ✅ Pilot1  Step 1.5   Step5  Step 2                     Step 4 (5개)
Dataset B (37)     ✅ MA-L1   Step 1.5   Step5  Step 3                     Step 4 (5개)
Dataset C (40+)    -          Step 7     -      Step 7                     -
```

**빈 칸: 0.** 모든 조합이 커버됨.

---

## 2차 체크에서 추가로 발견된 누락 사항

### A. Error Severity Taxonomy (누락)
현재 모든 에러를 동등하게 취급하고 있음. 분류 필요:
- **Critical:** 존재하지 않는 논문 (fabrication) → 0건
- **High:** 저자 완전 오류 (misattribution) → 2건
- **Medium:** venue 인플레이션 (workshop→conference) → 1건
- **Low:** venue 미업데이트, 제목 약간 다름 → 6건

→ Step 8에서 에러 심각도별 분석 추가. "24% 에러"보다 "5% high-severity 에러"가 더 정확한 보고.

### B. Cost-Benefit Analysis (누락)
Level 1: 3분/논문 → 9개 에러 발견
Level 2: 30-60분/논문 → ? 추가 발견
이 비율을 정량화해야 함 → Step 5 결과에서 계산.
"Level 1이 전체 에러의 X%를 발견하고, Level 2가 추가 Y%를 잡는다. 비용은 10배인데 추가 발견은 Z%"

### C. 재현성 (Reproducibility) 문제
- research-system Level 1 = 수동 → 다른 사람이 재현 어려움
- meta-architect verify_papers.py = 코드 → 재현 가능
- 최소한 Level 1 실행 절차를 step-by-step으로 문서화 필요
→ Step 8에서 재현 프로토콜 문서 포함

### D. 두 시스템 아키텍처 비교 문서 (누락)
"meta-architect는 이렇게 짜놨고, research-system은 이렇게 한다"를 나란히 보여주는 문서가 없음.
→ Step 1 이후 `05_evidence/system_comparison.md` 생성

### E. 논문 타겟 venue — 데이터 먼저, venue 나중 (확정)
**전략:** Workshop 기준으로 Step 1-6 완료 → 결과 보고 venue 결정.
**사전 threshold (HARKing 방지):**
- Staged system이 baseline 대비 에러 탐지율 **≥20% 높으면** → conference 제출
- Gold standard에서 precision **≥ 0.85**이면 → conference 제출
- 둘 다 미달이면 → workshop / short paper
**확대 시:** Step 7 Dataset C를 20개→50개로 증가 (conference 기준 N=100+ 달성)

---

## 빠뜨린 것 없는지 체크

| 리뷰어 우려 | 대응 Step | 충분? |
|---|---|---|
| Gold standard 없음 | Step 4 | 10개면 최소. 20개면 좋음 |
| CiteAudit novelty | Step 1 | 정독 후 판단 |
| N 부족 | Step 7 | 73+로 확대. 200+은 후속 연구 |
| 교차 검증 안 됨 | Step 2+3 | 완전한 2×2 매트릭스 |
| Level 2 미실행 | Step 5 | 5개 pilot — feasibility 수준 |
| 순환 문제 | Step 4 | Human gold로 부분 해결 |
| 자동화 없음 | Step 2+3 | MA 시스템 활용으로 자동화 측면 포함 |
| inter-rater reliability | Step 6 | Claude vs GPT (Pilot 1) + 두 시스템 비교 |
| 에러 심각도 미정의 | Step 5+8 | Level 2에서 "실제 해로운 에러" 구분 |
| verifier error rate | Step 4 | Gold 대비 false positive/negative 측정 |
| 에러 심각도 분류 | Step 8 | critical/high/medium/low taxonomy |
| cost-benefit 정량화 | Step 5+8 | Level 1 vs Level 2 비용 대비 추가 발견 |
| 재현성 문서 | Step 8 | step-by-step 재현 프로토콜 |
| 시스템 아키텍처 비교 | Step 1 이후 | meta-architect vs research-system 나란히 |

---

## Files to Create/Modify

## 최종 체크박스 (피드백 반영)

- [ ] Dataset construction rule: 왜 이 53개가 선택되었는지 명시 (Step 8)
- [ ] Baseline failure regime analysis: 어떤 오류는 script로 충분하고 어떤 오류만 staged system이 필요한지 (Step 2.5)
- [ ] Downstream impact examples: citation correction이 실제 design decision을 어떻게 바꿨는지 2-3개 사례 (Step 5)
- [ ] "independently" → "separately prompted" 표현 사용 (작성 시)
- [ ] Sample selection bias 명시 (Step 8)
- [ ] Gold 결과를 "calibration evidence"로 프레이밍 (작성 시)

---

**Create (research-system):**
- `05_evidence/source_tables/competitor_analysis.md`
- `04_pilots/cross_validation_MA_on_A.md` + CSV
- `04_pilots/cross_validation_MA_on_B.md` + CSV
- `05_evidence/gold_standard_10.md`
- `04_pilots/precision_recall_report.md`
- `04_pilots/pilot_L2_report.md` + CSV
- `04_pilots/level2_checklist_v0.1.md`
- `04_pilots/statistical_analysis.md`
- `05_evidence/source_tables/dataset_C_*.md`
- `04_pilots/paper_outline.md`

**Modify:**
- `00_master/README.md` (index update)
- `README.md` (results update)

**Read-only (meta-architect — 수정 금지):**
- `research/verify_papers.py` (실행만)
- `research/papers.yaml` (읽기만)
- `research/papers_schema.py` (참고만)

---

## Verification

각 Step 완료 시:
1. 산출물 파일 존재 확인
2. CSV 데이터 무결성 (빈 셀 없음)
3. QOC 기록 작성 (주요 결정마다)
4. README 인덱스 업데이트
5. git commit + push
