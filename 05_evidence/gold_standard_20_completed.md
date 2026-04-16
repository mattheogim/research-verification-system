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
| Title | LLM-Based Multi-Agent Blackboard System for Info Discovery in DS | 실제: LLM-Based Multi-Agent Blackboard System for Information Discovery in Data Science |
| Authors | **Li et al.** | 실제 1저자: Alireza Salemi (UMass Amherst) |
| Venue | arXiv | 실제: arXiv (no journal ref, v1 2025-09-30, v2 2026-01-31) |
| **Claude verdict** | FAIL (author_wrong) | |
| **Human verdict** | FAIL (author_wrong) | |
| 비고 | | 1저자 Salemi, 공저자 Parmar/Goyal/Song/Yoon/Zamani/Pfister/Palangi. 저자진에 "Li" 없음 → Catalog의 "Li et al."은 명백한 오류. Title은 축약형이라 문제 없고 venue도 arXiv 일치. Author 단일 오류로 FAIL. |

### 2. E7 — author_mismatch
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2505.18286 | |
| Title | Single-agent or Multi-agent Systems? Why Not Both? | 실제: Single-agent or Multi-agent Systems? Why Not Both? (일치) |
| Authors | **Zhao et al.** | 실제 1저자: Mingyan Gao |
| Venue | arXiv | 실제: arXiv (no journal ref, submitted 2025-05-23) |
| **Claude verdict** | FAIL (author_wrong) | |
| **Human verdict** | FAIL (author_wrong) | |
| 비고 | | 1저자 Gao, 공저자 Li/Liu/Yu/Wang/Lin/Lai. 저자진 7명 중 "Zhao" 성 없음 → Catalog "Zhao et al."은 명백한 오류. Title/venue는 일치. Author 단일 오류로 FAIL. |

## PARTIAL 예상 (10개)

### 3. A3 — venue_drift
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2410.12853 | |
| Title | Diversity of Thought Elicits Stronger Reasoning... | 실제: Diversity of Thought Elicits Stronger Reasoning Capabilities in Multi-Agent Debate Frameworks (일치) |
| Authors | Hegazy | 실제: Mahmood Hegazy (single author, 일치) |
| Venue | **arXiv** | 실제: Journal of Robotics and Automation Research (JRAR), Vol. 5 Issue 3, Oct 2024 |
| **Claude verdict** | PARTIAL (venue_drift: published in JRAR) | |
| **Human verdict** | PARTIAL (venue_drift) | |
| 비고 | | arXiv Journal ref 필드에 JRAR publication 명시 (DOI: 10.33140/JRAR). Title/author 일치. Catalog가 arXiv preprint로 기록했지만 실제로는 JRAR 2024에 published → venue_drift 확정. |JRAR은 low-tier venue지만 verification 관점에서는 arXiv ≠ JRAR이므로 venue_drift 확정.

### 4. B2 — venue_drift
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2402.05120 | |
| Title | More Agents Is All You Need | 실제: More Agents Is All You Need (일치) |
| Authors | Li et al. | 실제 1저자: Junyou Li (Zhang/Yu/Fu/Ye) — 일치 |
| Venue | **arXiv** | 실제: Published at Transactions on Machine Learning Research (TMLR) |
| **Claude verdict** | PARTIAL (venue_drift: published in TMLR) | |
| **Human verdict** | PARTIAL (venue_drift) | |
| 비고 | | arXiv Comments 필드에 "Published at TMLR" 명시. Title/author 일치. Catalog가 arXiv로 기록했지만 실제로는 TMLR publication → venue_drift 확정. TMLR은 high-reputation venue (A3의 JRAR과 달리 학계 인정). |

### 5. D3 — venue_missing
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2308.10848 | |
| Title | AgentVerse: Facilitating Multi-Agent Collaboration | 실제: AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors (Catalog는 subtitle 생략했지만 main title 일치) |
| Authors | Chen et al. | 실제 1저자: Weize Chen (Tsinghua, 16 authors) — 일치 |
| Venue | **arXiv** | 실제: ICLR 2024 (Poster) |
| **Claude verdict** | PARTIAL (venue_missing: ICLR 2024) | |
| **Human verdict** | PARTIAL (venue_missing) | |
| 비고 | | arXiv abstract 페이지는 v3(2023-10) 기준 "Under review"로 stale — 저자들이 publication metadata 업데이트 안 함. 하지만 ICLR 2024 공식 proceedings (iclr.cc/virtual/2024/poster/19109), GitHub repo 공지(2024-01-17), Semantic Scholar, 저자 개인 사이트 모두에서 ICLR 2024 acceptance 확인. Catalog가 arXiv preprint로만 기록 → venue_missing 확정. |
💡 중요한 methodological note
D3는 arXiv만으로는 검증 불가능한 케이스입니다. 이건 gold standard 만들 때 기록해둘 만한 lesson:

"arXiv Journal ref/Comments 필드만 의존하면 false negative 발생 가능. 학회 publication을 arXiv에 업데이트 안 하는 저자들 많음 (특히 ICLR처럼 OpenReview에서 published되는 경우). 따라서 venue verification은 OpenReview, 학회 공식 proceedings, 저자 개인 사이트, GitHub repo를 교차 확인해야 함."

나중에 disagreement analysis 할 때 이런 케이스가 생기면 이 methodology 근거로 설명할 수 있습니다.


### 6. E6 — venue_inflation
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2509.05396 | |
| Title | Talk Isn't Always Cheap: Failure Modes in Multi-Agent Debate | 실제: Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate ("Understanding" 누락) |
| Authors | Wynn et al. | 실제 1저자: Andrea Wynn (Satija, Hadfield) — 일치 |
| Venue | **ICML 2025** | 실제: ICML MAS Workshop 2025 |
| **Claude verdict** | PARTIAL (venue_inflation: ICML MAS Workshop 2025) | |
| **Human verdict** | PARTIAL (venue_inflation) | |
| 비고 | | arXiv Comments에 "ICML MAS Workshop 2025" 명시. Catalog가 "ICML 2025"로만 적어 메인 컨퍼런스처럼 보이게 함 → venue_inflation 확정 (workshop ≠ main conference). 참고: Title에서도 "Understanding" 단어 누락되어 있으나 이건 minor truncation이라 primary verdict는 venue_inflation으로 유지. |Workshop vs main conference 구분은 학계 평판에 큰 영향을 미치므로 venue_inflation은 특히 중요한 카테고리입니다. ICML main conference는 acceptance rate ~27%인 반면 workshop은 훨씬 관대 → Catalog가 "ICML 2025"로만 표기하면 독자가 메인 proceedings 논문으로 오해할 수 있음. 이건 Claude가 잘 잡아낸 케이스.

### 7. G2 — title_wrong
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2507.21028 | |
| Title | **MAJ-Eval: Multi-Agent-as-Judge** | 실제: Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation |
| Authors | (unknown) | 실제 1저자: Jiaju Chen (Lu, Wang, Zeng, Huang, Gesi, Xu, Yao, Wang) |
| Venue | arXiv | 실제: arXiv (no journal ref, submitted 2025-07-28) |
| **Claude verdict** | PARTIAL (title_wrong: actual title differs) | |
| **Human verdict** | PARTIAL (title_wrong) | |
| 비고 | | Catalog는 프레임워크 약어 "MAJ-Eval"을 title prefix로 잘못 배치. 실제 title에서 "Multi-Agent-as-Judge"는 main title, "MAJ-EVAL"은 abstract 내부의 framework naming일 뿐. Subtitle ("Aligning LLM-Agent-Based...") 전체 누락. Title 구조 자체를 오해한 오류. Author도 Catalog에서는 unknown이지만 실제 Jiaju Chen 등 확인 — 이건 missing이지 wrong은 아니므로 primary verdict는 title_wrong으로 유지. |

### 8. H1 — venue_year_wrong (clean re-run에서 새로 발견)
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2307.03172 | |
| Title | Lost in the Middle: How LMs Use Long Contexts | 실제: Lost in the Middle: How Language Models Use Long Contexts (Catalog는 "LMs" 축약) |
| Authors | Liu et al. | 실제 1저자: Nelson F. Liu — 일치 |
| Venue | **TACL 2024** | 실제: TACL 2024, Vol. 12, pp. 157-173 (Published Feb 2024) |
| **Claude verdict** | PARTIAL (venue_year: TACL 2023 not 2024) | |
| **Human verdict** | **EXACT** (Claude error — Catalog is correct) | |
| 비고 | | ⚠️ **DISAGREEMENT 케이스**: Claude verdict가 틀렸음. arXiv Comments는 "TACL 2023"이라 적혀있지만 이는 acceptance year. 실제 publication: TACL Volume 12, pp. 157-173, Published Feb 2024. 확인 소스: ACL Anthology (aclanthology.org/2024.tacl-1.9), MIT Press direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638, 논문 PDF 자체 ("Submission batch: 8/2023; Revision batch: 10/2023; Published 2/2024"), researchr.org. 학계 표준 인용 = TACL 2024. Catalog는 정확함. Claude가 arXiv Comments의 acceptance year를 publication year로 오인한 오류. |

### 9. H2 — title_wrong
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2505.18148 | |
| Title | **Lost in the Haystack** | 실제: Hidden in the Haystack: Smaller Needles are More Difficult for LLMs to Find |
| Authors | (unknown) | 실제 1저자: Owen Bianchi (Koretsky, Willey, Alvarado, Nayak, Asija, Kuznetsov, Nalls, Faghri, Khashabi) |
| Venue | arXiv | 실제: arXiv (Comments: "Under Review", v1 2025-05-23, v2 2025-12-16) |
| **Claude verdict** | PARTIAL (title_wrong: "Hidden" not "Lost") | |
| **Human verdict** | PARTIAL (title_wrong) | |
| 비고 | | Catalog가 첫 단어 "Hidden"을 "Lost"로 잘못 기록. H1 "Lost in the Middle"과의 혼동으로 추정됨 (둘 다 long-context LLM 논문). Subtitle 전체도 누락. Author는 unknown으로 비어있지만 실제 Bianchi et al. 10명 확인. Primary verdict는 title_wrong으로 유지. |

### 10. J8 — author_misleading (clean re-run에서 새로 발견)
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://www.infoq.com/news/2024/03/Evans-ddd-experiment-llm/ | |
| Title | LLM + DDD | 실제: Eric Evans Encourages DDD Practitioners to Experiment with LLMs |
| Authors | **Eric Evans** | 실제 글쓴이: Thomas Betts (Senior Laureate Application Architect, Blackbaud) |
| Venue | InfoQ | 실제: InfoQ News, 2024-03-18 (일치) |
| **Claude verdict** | PARTIAL (author_misleading: article by Betts, not Evans) | |
| **Human verdict** | PARTIAL (author_misleading) | |
| 비고 | | Thomas Betts가 기사 글쓴이, Eric Evans는 기사 주제(DDD 창시자, Explore DDD 기조연설자). Catalog는 기사의 subject를 author로 오인 — 뉴스 기사에서 흔한 cataloging 오류 패턴. Title도 "LLM + DDD"는 topic summary 수준으로 축약되어 실제 제목과 차이 크지만, primary verdict는 author_misleading으로 유지. Venue는 InfoQ로 일치. |

### 11. J2 — venue_drift
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2403.13002 | |
| Title | AutoTRIZ | 실제: AutoTRIZ: Automating Engineering Innovation with TRIZ and Large Language Models (Catalog는 subtitle 전체 누락, main title만 기록) |
| Authors | (unknown) | 실제 1저자: Shuo Jiang (Li, Qian, Zhang, Luo) |
| Venue | **arXiv** | 실제: Advanced Engineering Informatics, Vol. 65 (2025), article 103312 |
| **Claude verdict** | PARTIAL (venue_drift: Adv. Eng. Informatics) | |
| **Human verdict** | PARTIAL (venue_drift) | |
| 비고 | | arXiv Journal ref 필드에 "Advanced Engineering Informatics 65 (2025): 103312" 명시 (DOI: 10.1016/j.aei.2025.103312). Catalog가 arXiv preprint로만 기록 → venue_drift 확정. Advanced Engineering Informatics는 Elsevier 저널(impact factor ~7+), high-reputation venue. Catalog는 title도 subtitle 누락하고 author도 unknown으로 비어있지만 primary verdict는 venue_drift로 유지. |

### 12. K1a — title_informal
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2505.04364 | |
| Title | **SwarmBench** | 실제: Benchmarking LLMs' Swarm intelligence |
| Authors | (unknown) | 실제 1저자: Kai Ruan (Huang, Wen, Sun) |
| Venue | arXiv | 실제: arXiv (no journal ref, v1 2025-05-07, v4 2025-10-15) |
| **Claude verdict** | PARTIAL (title_informal: not actual title) | |
| **Human verdict** | PARTIAL (title_informal) | |
| 비고 | | "SwarmBench"는 논문이 소개하는 benchmark toolkit 이름 (abstract: "we introduce SwarmBench, a novel benchmark..."). 실제 title은 "Benchmarking LLMs' Swarm intelligence". G2 (MAJ-Eval) 과 동일한 cataloging 패턴: framework/tool 이름을 논문 title로 잘못 기록. Author도 unknown으로 비어있지만 primary verdict는 title_informal로 유지. |

---

## EXACT 예상 (8개) — control group

### 13. A1
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2305.14325 | |
| Title | Improving Factuality and Reasoning in LMs through Multiagent Debate | 실제: Improving Factuality and Reasoning in Language Models through Multiagent Debate ("LMs" 축약, 내용 일치) |
| Authors | Du et al. | 실제 1저자: Yilun Du (Li, Torralba, Tenenbaum, Mordatch) — 일치 |
| Venue | ICML 2024 | 실제: ICML 2024, PMLR 235, pp. 11733-11763 (확인 완료) |
| **Claude verdict** | EXACT | |
| **Human verdict** | EXACT | |
| 비고 | | arXiv 페이지에는 Journal ref 없지만 ICML 2024 publication은 GitHub 저장소 설명, ICML 공식 페이지(icml.cc/virtual/2024/poster/32620), dblp, 논문 PDF의 "PMLR 235, 2024"로 확인. "LMs" 축약은 consistent shorthand로 허용 (C2 "Info/DS" 패턴과 동일). EXACT 확정. |

### 14. B1
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2406.07155 | |
| Title | Scaling LLM-based Multi-Agent Collaboration | 실제: Scaling Large Language Model-based Multi-Agent Collaboration ("LLM" 축약, 내용 일치) |
| Authors | Qian et al. | 실제 1저자: Chen Qian (Xie, Wang, Liu, Zhu, Xia, Dang, Du, Chen, Yang, Liu, Sun) — 일치 |
| Venue | ICLR 2025 | 실제: ICLR 2025 (arXiv Comments: "Accepted to ICLR-2025") |
| **Claude verdict** | EXACT | |
| **Human verdict** | EXACT | |
| 비고 | | arXiv Comments 필드에 "Accepted to ICLR-2025" 명시. Title "LLM" 축약은 consistent shorthand. 모든 필드 일치 → EXACT 확정. |

### 15. D2
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2307.07924 | |
| Title | ChatDev: Communicative Agents for Software Development | 실제: ChatDev: Communicative Agents for Software Development (완전 일치) |
| Authors | Qian et al. | 실제 1저자: Chen Qian (Liu, Liu, Chen, Dang, Li, Yang, Chen, Su, Cong, Xu, Li, Liu, Sun) — 일치 |
| Venue | ACL 2024 | 실제: ACL 2024 (arXiv Comments: "Accepted to ACL 2024") |
| **Claude verdict** | EXACT | |
| **Human verdict** | EXACT | |
| 비고 | | arXiv Comments 필드에 "Accepted to ACL 2024" 명시. Title/author/venue 모두 완전 일치 → EXACT 확정. B1과 같은 1저자(Chen Qian)이지만 다른 논문 (ChatDev vs MacNet). |

### 16. E5
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2311.17371 | |
| Title | Should we be going MAD? | 실제: Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs (main title는 동일, subtitle drop — acceptable shorthand) |
| Authors | Smit et al. | 실제 1저자: Andries Smit (Duckworth, Grinsztajn, Barrett, Pretorius) — 일치 |
| Venue | ICML 2024 | 실제: ICML 2024, PMLR 235, pp. 45883-45905 (확인 완료) |
| **Claude verdict** | EXACT | |
| **Human verdict** | PARTIAL (title_incomplete) | |
| 비고 | | arXiv 페이지에는 venue 정보 없지만 ICML 2024 publication은 PMLR 공식 proceedings, ICML 가상 페이지(icml.cc/virtual/2024/poster/34657), OpenReview, ACM DL에서 확인. 모든 저자 InstaDeep 소속. Subtitle drop은 J2 (AutoTRIZ) 와 같은 acceptable shorthand 패턴 (catchy main title까지만 기록). EXACT 확정. |

### 17. F1
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2310.13548 | |
| Title | Towards Understanding Sycophancy in Language Models | 실제: Towards Understanding Sycophancy in Language Models (완전 일치) |
| Authors | Sharma et al. | 실제 1저자: Mrinank Sharma (19명 공저, Anthropic 주도) — 일치 |
| Venue | ICLR 2024 | 실제: ICLR 2024 (Poster) |
| **Claude verdict** | EXACT | |
| **Human verdict** | exact | |
| 비고 | | arXiv 페이지에는 venue 정보 없지만 ICLR 2024 publication은 ICLR 공식 proceedings PDF ("Published as a conference paper at ICLR 2024"), iclr.cc/virtual/2024/poster/17593, OpenReview에서 확인. Title/author/venue 모두 catalog와 일치. |

### 18. I1 — venue_missing (Claude error 발견)
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2408.02442 | |
| Title | Let Me Speak Freely? Format Restrictions on LLM Performance | 실제: Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models (main title 동일, subtitle paraphrased) |
| Authors | Tam et al. | 실제 1저자: Zhi Rui Tam (Wu, Tsai, Lin, Lee, Chen — Appier AI Research & NTU) — 일치 |
| Venue | **arXiv** | 실제: EMNLP 2024 Industry Track, pp. 1218-1236, Miami, November 2024 |
| **Claude verdict** | EXACT | |
| **Human verdict** | PARTIAL (venue_missing: EMNLP 2024 Industry Track) | |
| 비고 | | ⚠️ **DISAGREEMENT 케이스 (Claude error)**: Claude가 EXACT로 잘못 판정. arXiv Comments는 "18 pages"만 있어 venue 정보 없지만 실제로는 EMNLP 2024 Industry Track에 published (ACL Anthology: aclanthology.org/2024.emnlp-industry.91, DOI: 10.18653/v1/2024.emnlp-industry.91). Catalog도 arXiv로만 기록해서 EMNLP publication 누락 → venue_missing. D3(AgentVerse/ICLR 2024)와 같은 패턴: arXiv metadata에 publication 정보 없으면 놓치는 경우. Title subtitle도 paraphrased 형태라 minor issue 있으나 primary는 venue_missing. |

### 19. J9
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://www.nature.com/articles/s41467-026-70873-7 | |
| Title | Human Analogical Guidance Amplifies LLM Performance | 실제: Human analogical guidance amplifies LLM performance through cross-domain knowledge activation (main title 동일, subtitle drop — E5와 같은 acceptable shorthand) |
| Authors | (unknown) | 실제 저자: R. Larraz & A. Corma (2 authors) |
| Venue | Nature Comms | 실제: Nature Communications, Published 03 April 2026 (Open Access, unedited AOP version) |
| **Claude verdict** | EXACT | |
| **Human verdict** | PARTIAL (title_incomplete) | |
| 비고 | | Subtitle "through cross-domain knowledge activation"이 Catalog에서 drop됐지만 E5(Should we be going MAD?) 패턴과 동일 acceptable shorthand. Venue "Nature Comms" = Nature Communications shorthand. 논문은 현재 AOP(advance online publication) unedited version 상태이지만 2026-04-03 정식 published로 DOI 할당됨. Author 정보가 Catalog에 unknown이지만 이건 secondary issue (이전 G2/K1a/J2/K1a 등과 동일 패턴). EXACT 확정. |
### 20. E9
| Field | Catalog | 확인란 |
|---|---|---|
| **Link** | https://arxiv.org/abs/2603.04474 | |
| Title | From Spark to Fire: Error Cascades in LLM-Based MAS | 실제: From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration |
| Authors | (unknown) | 실제 1저자: Yizhe Xie (Zhu, Zhang, Zhu, Ye, Qi, Chen, Zhou — 8명) |
| Venue | arXiv | 실제: arXiv (2026-03-04 submit, v1, no journal ref) |
| **Claude verdict** | EXACT (but verify_papers.py said NOT FOUND) | |
| **Human verdict** | PARTIAL (title_incomplete) | |
| 비고 | | **특별 주의 케이스**: verify_papers.py가 "NOT FOUND"라고 했지만 실제로 논문 존재 (2026-03-04 arXiv submit). verify_papers.py의 오류 — catalog 링크는 valid. 하지만 title은 PARTIAL: (1) 실제 title의 중간 phrase "Modeling and Mitigating" 완전 누락 (논문 main contribution), (2) "MAS"(Multi-Agent Systems 약어)로 적혀있지만 실제는 "Multi-Agent Collaboration" (다른 단어). C 기준에서 단순 약어 치환 넘어 단어 자체가 다르므로 title_incomplete 판정. Author unknown은 secondary issue. Venue arXiv 일치. |

---

## 완료 후 할 것

1. 이 파일을 `05_evidence/gold_standard_20_completed.md`로 저장
2. Claude에게 전달 → precision/recall/F1 계산 (Step 6)
3. Human verdict vs Claude verdict 불일치 건 → disagreement analysis

## 요약 테이블 (완료 후 작성)
🎯 최종 요약 (C 기준 적용)
전체 20건 판정 결과
#항목Catalog 오류 유형Claude verdictHuman verdict일치?1C2author_wrongFAILFAIL✅2E7author_wrongFAILFAIL✅3A3venue_drift (JRAR)PARTIALPARTIAL✅4B2venue_drift (TMLR)PARTIALPARTIAL✅5D3venue_missing (ICLR 2024)PARTIALPARTIAL✅6E6venue_inflation (Workshop)PARTIALPARTIAL✅7G2title_wrongPARTIALPARTIAL✅8H1(실제 오류 없음)PARTIALEXACT❌9H2title_wrongPARTIALPARTIAL✅10J8author_misleadingPARTIALPARTIAL✅11J2venue_drift (AEI)PARTIALPARTIAL✅12K1atitle_informalPARTIALPARTIAL✅13A1(오류 없음)EXACTEXACT✅14B1(오류 없음)EXACTEXACT✅15D2(오류 없음)EXACTEXACT✅16E5title_incompleteEXACTPARTIAL❌17F1(오류 없음)EXACTEXACT✅18I1venue_missing (EMNLP 2024)EXACTPARTIAL❌19J9title_incompleteEXACTPARTIAL❌20E9title_incompleteEXACTPARTIAL❌
Agreement: 15/20 = 75%

📊 Verdict 분포
VerdictClaudeHuman일치불일치EXACT8444 (모두 Claude false EXACT)PARTIAL1014104FAIL2220Total2020155

🔍 Disagreement 분석 (5건)
Claude false EXACT (Claude가 오류 놓침) — 4건:

E5 (Should we be going MAD?): Subtitle drop 놓침 → C 기준으로 PARTIAL
I1 (Let Me Speak Freely?): EMNLP 2024 Industry Track 놓침 → venue_missing PARTIAL
J9 (Human Analogical Guidance): Subtitle drop 놓침 → C 기준으로 PARTIAL
E9 (From Spark to Fire): "Modeling and Mitigating" phrase 누락 놓침 → title_incomplete PARTIAL

Claude false PARTIAL (Claude가 과잉 검출) — 1건:

H1 (Lost in the Middle): TACL acceptance year(2023)와 publication year(2024) 혼동. Catalog의 TACL 2024는 실제 publication year로 정확.


📈 Precision & Recall (Claude's error detection)
Claude가 "오류 있음"(PARTIAL+FAIL)으로 판정한 건: 12건 (10 PARTIAL + 2 FAIL)

True Positive (실제 오류): 11건
False Positive (실제 오류 없음): 1건 (H1)

실제 오류 있는 건 (Human verdict 기준): 16건 (14 PARTIAL + 2 FAIL)

Claude가 찾은 오류: 11건
Claude가 놓친 오류: 5건 (E5, I1, J9, E9, H1 보정 후)

잠깐, 수정:

H1은 실제 오류 없음(EXACT). Claude가 PARTIAL로 오검출.
나머지 15건은 실제 오류 있음.

계산:

Precision = TP / (TP + FP) = 11 / 12 = 91.7%
Recall = TP / (TP + FN) = 11 / 15 = 73.3%
F1 = 2 × (P × R) / (P + R) = 2 × (0.917 × 0.733) / (0.917 + 0.733) = 0.815


💡 Key Findings

Claude의 체계적 blind spot: arXiv에 Journal ref 없으면 학회 publication 놓치는 경향 (D3는 잡았지만 I1은 놓침). EMNLP Industry Track처럼 mainstream이 아닌 venue는 특히 취약.
Title truncation 과소 검출: E5, J9처럼 subtitle drop된 케이스들을 Claude가 "shorthand OK"로 과하게 관대하게 처리. C 기준(strict subtitle preservation)에서는 PARTIAL이 맞음.
Year disambiguation 오류: H1에서 Claude가 acceptance year(2023)를 publication year(2024)로 혼동. TACL 같은 journal의 rolling publication 특성을 고려하지 못함.
Cataloging의 체계적 bias 관찰 (Matteo님의 수작업 검증으로만 발견 가능한 것):

Framework name을 title로 오기록 (G2, K1a)
뉴스 기사 subject를 author로 오기록 (J8)
유사 논문 간 cross-contamination (H1-H2)


Recall 73.3%가 Gold standard의 핵심 가치: 나머지 26.7% = Claude가 혼자 못 잡는 오류 = Human verification이 필수임을 실증.
