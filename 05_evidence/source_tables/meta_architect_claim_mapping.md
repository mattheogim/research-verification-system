# Meta Architect — Claim Mapping (Level 2 Context)

_Extracted from: `paper-feature-map.json` + Phase 0 execution plan_
_Extracted on: 2026-04-15_
_Purpose: Maps each design decision to the paper(s) that justify it — needed for Level 2 verification_

> This file is a READ-ONLY snapshot. Sources: `~/meta-architect/research/paper-feature-map.json` + Phase 0 plan.

---

## A. Code Feature → Paper (from paper-feature-map.json)

| Feature | Source Files | Required Papers | What to verify in Level 2 |
|---|---|---|---|
| **Debate protocol** (Phase 4 adversarial challenge) | phase4.py, critic agents | A1 §2 Method, A2 §1 DoT + §2 MAD, E6 §4 failure modes | Does A1's debate protocol match our Phase 4 design? Does E6's failure taxonomy cover our cases? |
| **Multi-model assignment** | model_assignment.py | A3 §4.2 Diversity of Thought, E3 (Self-MoA counter) | Does A3's +9%p diversity premium apply to architecture tasks? Does E3 invalidate this? |
| **Blackboard implementation** | blackboard/ | C1 §3 + §3.2 Blackboard Cycle, E1 §3 criticisms | Does C1's 5-role cycle map to our slot structure? |
| **Scaling + Lazy Loading** | router.py, lazy_loader.py | B1 §2 MacNet + §3.3 Scaling Law, E2 §4.3 Scaling Principles | Is B1's logistic growth formula applicable? Does E2's T=2.72(n+0.5)^1.724 match? |
| **Peer review system** | state_transition.py, review_authority.py | G2 §3 MAJ-Eval, F1 sycophancy, G1 §3 bias + §5 mitigation | Does MAJ-Eval's framework match our review authority design? |
| **Structured output** | base_agent.py, entry.py | I1 §3 experiments + §4 mitigation | Does I1 actually show reasoning degradation with JSON forcing? |
| **Agent prompts** | agents/prompts/ | E4 (personas don't help) | Does E4 show personas hurt? Do we need structural role separation instead? |
| **Convergence** | state_assessor.py, deadlock_resolver.py | E5 §4 convergence analysis | Does E5's hyperparameter sensitivity apply to our Phase structure? |
| **Context management** | views.py | H1 §3 experiments | Is the 30%+ middle-position accuracy drop real? |

## B. Design Decision → Paper (from Phase 0 plan)

| Phase 0 Item | Decision | Paper Justification | Level 2 Question |
|---|---|---|---|
| Item 2: Review rubric | CoT-forced review with randomized order | G2 MAJ-Eval, G1 LLM-as-Judge survey | Does G2 propose exactly this mechanism? |
| Item 4: Convergence rules | 10 rounds/phase + 3 consecutive <5% change + 200 call safety net | deep-4 (from E5 analysis) | Is the 10-round + 5% threshold from the paper or invented? |
| Item 5: Precedent Researcher | Remove RAG, use web_search + LLM | deep-6 | What evidence supports removing RAG? |
| Item 6: No Rubber-Stamping | Phase 4 agents must propose 1 alternative + 1 risk | A2 DoT problem, E6 failure modes | Does DoT problem + debate failures justify this specific rule? |
| Item 7: Success criteria tiers | code_verifiable / simulation_possible / manual_only | deep-1 | Is this 3-tier from the literature or invented? |
| Item 8: Phase transition reasoning | State Assessor generates 200-token summary | A4 Collaborativeness | Does A4's finding justify transition summaries? |
| Item 9: Think NL, Write Schema | reasoning=NL / contribution=Pydantic | I1 | Does I1 propose this exact hybrid pattern? |
| Item 11: Roadmap update | Phase 0→0.5→1→2→3→4 | MASTER-PLAN | Internal decision, no paper verification needed |

## C. Key Numbers Needing Original Text Confirmation

| Number | Claimed Source | Where Used | Priority |
|---|---|---|---|
| +7~16pp debate improvement | A1 Du et al. | Phase 4 justification | HIGH — already VERIFIED |
| 91% GSM-8K (diverse) vs 82% (homogeneous) | A3 Hegazy | Multi-model assignment | HIGH — already VERIFIED |
| T=2.72(n+0.5)^1.724 coordination cost | E2 DeepMind | Lazy Loading justification | HIGH — already VERIFIED |
| Effective team size ~3-4 | E2 DeepMind | Agent count justification | HIGH — already VERIFIED |
| 30%+ middle-position accuracy drop | H1 Liu et al. | Context management | MEDIUM |
| JSON forcing reasoning penalty | I1 Tam et al. | Structured output design | MEDIUM |
| 30%p persona performance drop | E4 Basil et al. | Agent prompt design | MEDIUM |
| Logistic growth pattern for agent scaling | B1 Qian et al. | Scaling design | HIGH — formula UNVERIFIED |
| SOTA + fewer tokens (Blackboard) | C1 Han & Zhang | Blackboard choice | HIGH — numbers UNVERIFIED |
