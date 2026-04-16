# Next Session Prompt — Dataset A Clean Re-run

Copy this into a new Claude session:

---

```
~/PaperResearchAgent/research-system 에서 작업 중.
GitHub: https://github.com/mattheogim/research-verification-system

남은 작업 1개: Dataset A (16개 소스) Level 1 clean re-run.

이전 결과를 절대 보지 마. 다음 CSV에서 논문 목록만 참고해:
04_pilots/pilot_claude_v0.4.1_results.csv

이 CSV의 id, source 컬럼만 보고, verdict/error_type 컬럼은 보지 마.
각 소스를 arXiv/DOI/웹에서 직접 확인해서 새 CSV를 만들어:
- 04_pilots/clean_rerun_L1_A_results.csv

포맷: ID,Source,Authors_Actual,Title_Actual,Venue_Actual,Verdict,Error_Type,Notes

끝나면:
1. 이전 결과(pilot_claude_v0.4.1_results.csv)와 일치율 계산
2. 04_pilots/clean_rerun_L1_A_comparison.md 에 비교 보고서 작성
3. 성공 기준: ≥90% 일치 = robust, 80-89% = acceptable, <80% = concern
4. git commit + push

meta-architect 원본 파일은 수정 금지.
```

---

## After this is done

All experiment matrix gaps will be filled:

```
                    research-system              meta-architect         HUMAN
                    L1(orig) L1(clean)  L2       verify_py(clean)       gold
Dataset A (16)     ✅        ✅ (TODO)  4/16     ✅                     10/20
Dataset B (42)     ✅        ✅ (91.9%) 4/42     ✅                     10/20
Dataset C (45)     ✅        -          -        partial                -
```

Remaining gaps (acceptable for paper):
- Dataset C clean re-run: not needed (C was already clean, first run)
- Dataset C verify_papers.py: partially done, can note as limitation
- Level 2 coverage 8/58: feasibility pilot, explicitly scoped
