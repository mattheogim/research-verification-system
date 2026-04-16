# L2 Codex Scaffold

이 디렉토리는 Codex L2 독립 실행 (Session C)을 위한 발판입니다.
/Users/matteokim/PaperResearchAgent/research-system/04_pilots/L2_codex_scaffold/README.md

## 사용법

1. Phase 1이 완료되면 `codex_L2_prompt_v1.md`의 placeholder를 채움
2. `L2_input.csv`를 이 디렉토리에 복사 (또는 symlink)
3. Rubric Freeze 후 Codex 세션에 prompt 전문을 전달
4. Codex 출력: `codex_L2_results.csv`

## 파일 목록

| 파일 | 상태 | 설명 |
|---|---|---|
| `codex_L2_prompt_v1.md` | Template (placeholder 미충전) | Codex에 줄 전체 prompt |
| `L2_input.csv` | 미생성 (Phase 5에서 생성) | Evaluation set input |
| `codex_L2_results.csv` | 미생성 (Codex가 생성) | Codex 출력 |
| `PREFLIGHT_CHECKLIST.md` | Ready | 실행 전 확인 사항 |

## 절대 금지

이 디렉토리에 아래 파일을 넣거나 Codex 세션에서 접근시키면 안 됨:
- pilot_L2_results.csv
- pilot_L2_report.md / pilot_L2_supplement.md
- gold_standard_*.md / gold_standard_*.csv
- L2_VALIDATION_PLAN_FULL.md
- claude_L2_independent.csv
- CODEX_L1_FEEDBACK.md
