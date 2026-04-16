# Claude L2 Preflight Checklist

Claude L2 실행 (Session B) 전에 **모든 항목** 확인.
하나라도 미완료면 실행 금지.

---

## Phase 1 산출물 확인

- [ ] `level2_checklist_v1.0.md` 존재 (decision tree 확정)
- [ ] `edge_case_bank_L2.md` 존재 (8개+ 사례)
- [ ] Calibration 완료: 기존 9개 pair를 decision tree로 재판정, 결과 기록
- [ ] Calibration log: `calibration_log_L2.md` 존재 (verdict 변경 사유)

## Rubric Freeze 확인

- [ ] git tag `rubric-freeze-v1` 존재
  ```bash
  git tag -l 'rubric-freeze-v1'
  ```
- [ ] Tag에 포함된 파일:
  - [ ] `level2_checklist_v1.0.md`
  - [ ] `edge_case_bank_L2.md`
  - [ ] `claude_L2_prompt_v1.md` (placeholder 채워진 버전)
  - [ ] `claude_L2_prompt_v1.md` (placeholder 채워진 버전)
  - [ ] `L2_input.csv`

## Prompt 완성 확인

- [ ] `claude_L2_prompt_v1.md`에 `PLACEHOLDER` 문자열이 **0개**
  ```bash
  grep -c 'PLACEHOLDER' L2_claude_scaffold/claude_L2_prompt_v1.md
  # 결과가 0이어야 함
  ```
- [ ] `[BEGIN DECISION_TREE_V1]`과 `[END DECISION_TREE_V1]` 사이에 내용 있음
- [ ] `[BEGIN MATERIALITY_TEST_V1]`과 `[END MATERIALITY_TEST_V1]` 사이에 내용 있음
- [ ] `[BEGIN EDGE_CASE_BANK_V1]`과 `[END EDGE_CASE_BANK_V1]` 사이에 내용 있음

## Input 확인

- [ ] `L2_input.csv` 존재
- [ ] Evaluation set만 포함 (calibration 9개 제외)
- [ ] 최소 12행
- [ ] 컬럼: ID, Paper_Title, ArXiv_URL, Claim_Text, Claim_Type, Citing_Location
- [ ] 이전 judgment 컬럼 없음 (verdict leak 방지)

## Prompt Parity 확인

- [ ] Claude prompt와 Codex prompt가 output 파일명 외 동일
  ```bash
  diff <(sed 's/claude_L2_independent/OUTPUT/g' L2_claude_scaffold/claude_L2_prompt_v1.md) \
       <(sed 's/claude_L2_independent/OUTPUT/g' L2_claude_scaffold/claude_L2_prompt_v1.md)
  # 차이 없어야 함
  ```

## Session Isolation 확인

- [ ] Codex 세션에 이 프로젝트의 다른 파일 접근 불가 확인
- [ ] 특히 금지 파일 목록 (prompt에 명시됨):
  - pilot_L2_results.csv
  - pilot_L2_report.md / pilot_L2_supplement.md
  - gold_standard_*.md
  - L2_VALIDATION_PLAN_FULL.md
  - error_taxonomy.md
  - claude_L2_independent.csv
  - CODEX_L1_FEEDBACK.md

## 실행 순서 확인

- [ ] Human gold standard (Phase 2) 실행 완료 또는 병렬 진행 중
- [ ] Claude L2 (Session B) 실행 완료 또는 병렬 진행 중
- [ ] Session B와 Session B가 서로의 결과를 모름

---

## 실행

모든 항목 확인 후:
1. 새 Codex 세션 열기
2. `claude_L2_prompt_v1.md` 전문을 프롬프트로 전달
3. `L2_input.csv`를 세션에 제공
4. Codex가 `claude_L2_independent.csv` 생성하면 이 디렉토리에 저장
5. Session D (비교 분석)에서 사용
