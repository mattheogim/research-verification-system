# Human Gold Standard — 20 Papers Verification Template

_Annotator: Matteo Kim_
_Date: ____-__-___
_Instructions: 각 논문의 링크를 직접 열어서 실제 저자/제목/venue를 확인하세요._
_Claude/GPT 사용 금지 — 직접 눈으로 확인해야 합니다._

---

## 확인 방법

1. 아래 링크를 클릭해서 arXiv/DOI 페이지를 엽니다
2. 실제 title, authors, venue를 확인합니다
3. "Catalog" 열과 비교합니다
4. Human Verdict를 적습니다: `EXACT` / `PARTIAL` (뭐가 다른지) / `FAIL` (뭐가 틀린지)
5. 비고란에 근거를 적습니다

**소요 시간: 논문당 ~5분, 총 ~1.5-2시간**

---

## FAIL 예상 (2개) — 가장 중요

### 1. C2 — author_mismatch
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2510.01285 | |
| Title | LLM-Based Multi-Agent Blackboard System for Info Discovery in DS | 실제: _________________ |
| Authors | **Li et al.** | 실제 1저자: _________________ |
| Venue | arXiv | 실제: _________________ |
| **Claude verdict** | FAIL (author_wrong) | |
| **Human verdict** | __________ | |
| 비고 | | |

### 2. E7 — author_mismatch
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2505.18286 | |
| Title | Single-agent or Multi-agent Systems? Why Not Both? | 실제: _________________ |
| Authors | **Zhao et al.** | 실제 1저자: _________________ |
| Venue | arXiv | 실제: _________________ |
| **Claude verdict** | FAIL (author_wrong) | |
| **Human verdict** | __________ | |
| 비고 | | |

---

## PARTIAL 예상 (10개)

### 3. A3 — venue_drift
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2410.12853 | |
| Title | Diversity of Thought Elicits Stronger Reasoning... | 실제: _________________ |
| Authors | Hegazy | 실제: _________________ |
| Venue | **arXiv** | 실제: _________________ |
| **Claude verdict** | PARTIAL (venue_drift: published in JRAR) | |
| **Human verdict** | __________ | |
| 비고 | | |

### 4. B2 — venue_drift
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2402.05120 | |
| Title | More Agents Is All You Need | 실제: _________________ |
| Authors | Li et al. | 실제: _________________ |
| Venue | **arXiv** | 실제: _________________ |
| **Claude verdict** | PARTIAL (venue_drift: published in TMLR) | |
| **Human verdict** | __________ | |
| 비고 | | |

### 5. D3 — venue_missing (clean re-run에서 새로 발견)
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2308.10848 | |
| Title | AgentVerse: Facilitating Multi-Agent Collaboration | 실제: _________________ |
| Authors | Chen et al. | 실제: _________________ |
| Venue | **arXiv** | 실제: _________________ |
| **Claude verdict** | PARTIAL (venue_missing: ICLR 2024) | |
| **Human verdict** | __________ | |
| 비고 | | |

### 6. E6 — venue_inflation
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2509.05396 | |
| Title | Talk Isn't Always Cheap: Failure Modes in Multi-Agent Debate | 실제: _________________ |
| Authors | Wynn et al. | 실제: _________________ |
| Venue | **ICML 2025** | 실제: _________________ |
| **Claude verdict** | PARTIAL (venue_inflation: ICML MAS Workshop 2025) | |
| **Human verdict** | __________ | |
| 비고 | | |

### 7. G2 — title_wrong (clean re-run에서 새로 발견)
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2507.21028 | |
| Title | **MAJ-Eval: Multi-Agent-as-Judge** | 실제: _________________ |
| Authors | (unknown) | 실제: _________________ |
| Venue | arXiv | 실제: _________________ |
| **Claude verdict** | PARTIAL (title_wrong: actual title differs) | |
| **Human verdict** | __________ | |
| 비고 | | |

### 8. H1 — venue_year_wrong (clean re-run에서 새로 발견)
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2307.03172 | |
| Title | Lost in the Middle: How LMs Use Long Contexts | 실제: _________________ |
| Authors | Liu et al. | 실제: _________________ |
| Venue | **TACL 2024** | 실제: _________________ |
| **Claude verdict** | PARTIAL (venue_year: TACL 2023 not 2024) | |
| **Human verdict** | __________ | |
| 비고 | | |

### 9. H2 — title_wrong
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2505.18148 | |
| Title | **Lost in the Haystack** | 실제: _________________ |
| Authors | (unknown) | 실제: _________________ |
| Venue | arXiv | 실제: _________________ |
| **Claude verdict** | PARTIAL (title_wrong: "Hidden" not "Lost") | |
| **Human verdict** | __________ | |
| 비고 | | |

### 10. J8 — author_misleading (clean re-run에서 새로 발견)
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://www.infoq.com/news/2024/03/Evans-ddd-experiment-llm/ | |
| Title | LLM + DDD | 실제: _________________ |
| Authors | **Eric Evans** | 실제 글쓴이: _________________ |
| Venue | InfoQ | 실제: _________________ |
| **Claude verdict** | PARTIAL (author_misleading: article by Betts, not Evans) | |
| **Human verdict** | __________ | |
| 비고 | | |

### 11. J2 — venue_drift
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2403.13002 | |
| Title | AutoTRIZ | 실제: _________________ |
| Authors | (unknown) | 실제: _________________ |
| Venue | **arXiv** | 실제: _________________ |
| **Claude verdict** | PARTIAL (venue_drift: Adv. Eng. Informatics) | |
| **Human verdict** | __________ | |
| 비고 | | |

### 12. K1a — title_informal
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2505.04364 | |
| Title | **SwarmBench** | 실제: _________________ |
| Authors | (unknown) | 실제: _________________ |
| Venue | arXiv | 실제: _________________ |
| **Claude verdict** | PARTIAL (title_informal: not actual title) | |
| **Human verdict** | __________ | |
| 비고 | | |

---

## EXACT 예상 (8개) — control group

### 13. A1
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2305.14325 | |
| Title | Improving Factuality and Reasoning in LMs through Multiagent Debate | 실제: _________________ |
| Authors | Du et al. | 실제 1저자: _________________ |
| Venue | ICML 2024 | 실제: _________________ |
| **Claude verdict** | EXACT | |
| **Human verdict** | __________ | |

### 14. B1
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2406.07155 | |
| Title | Scaling LLM-based Multi-Agent Collaboration | 실제: _________________ |
| Authors | Qian et al. | 실제 1저자: _________________ |
| Venue | ICLR 2025 | 실제: _________________ |
| **Claude verdict** | EXACT | |
| **Human verdict** | __________ | |

### 15. D2
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2307.07924 | |
| Title | ChatDev: Communicative Agents for Software Development | 실제: _________________ |
| Authors | Qian et al. | 실제 1저자: _________________ |
| Venue | ACL 2024 | 실제: _________________ |
| **Claude verdict** | EXACT | |
| **Human verdict** | __________ | |

### 16. E5
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2311.17371 | |
| Title | Should we be going MAD? | 실제: _________________ |
| Authors | Smit et al. | 실제 1저자: _________________ |
| Venue | ICML 2024 | 실제: _________________ |
| **Claude verdict** | EXACT | |
| **Human verdict** | __________ | |

### 17. F1
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2310.13548 | |
| Title | Towards Understanding Sycophancy in Language Models | 실제: _________________ |
| Authors | Sharma et al. | 실제 1저자: _________________ |
| Venue | ICLR 2024 | 실제: _________________ |
| **Claude verdict** | EXACT | |
| **Human verdict** | __________ | |

### 18. I1
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2408.02442 | |
| Title | Let Me Speak Freely? Format Restrictions on LLM Performance | 실제: _________________ |
| Authors | Tam et al. | 실제 1저자: _________________ |
| Venue | arXiv | 실제: _________________ |
| **Claude verdict** | EXACT | |
| **Human verdict** | __________ | |

### 19. J9
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://www.nature.com/articles/s41467-026-70873-7 | |
| Title | Human Analogical Guidance Amplifies LLM Performance | 실제: _________________ |
| Authors | (unknown) | 실제: _________________ |
| Venue | Nature Comms | 실제: _________________ |
| **Claude verdict** | EXACT | |
| **Human verdict** | __________ | |

### 20. E9
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2603.04474 | |
| Title | From Spark to Fire: Error Cascades in LLM-Based MAS | 실제: _________________ |
| Authors | (unknown) | 실제: _________________ |
| Venue | arXiv | 실제: _________________ |
| **Claude verdict** | EXACT (but verify_papers.py said NOT FOUND) | |
| **Human verdict** | __________ | |
| 비고 | **특별 주의**: 두 시스템이 다른 답을 냄. 직접 확인 중요 | |

---

## 완료 후 할 것

1. 이 파일을 `05_evidence/gold_standard_20_completed.md`로 저장
2. Claude에게 전달 → precision/recall/F1 계산 (Step 6)
3. Human verdict vs Claude verdict 불일치 건 → disagreement analysis

## 요약 테이블 (완료 후 작성)

| Verdict | Claude | Human | 일치 | 불일치 |
|---|---|---|---|---|
| EXACT | 8 | ___ | ___ | ___ |
| PARTIAL | 10 | ___ | ___ | ___ |
| FAIL | 2 | ___ | ___ | ___ |
| **Total** | **20** | ___ | ___/20 | ___/20 |
