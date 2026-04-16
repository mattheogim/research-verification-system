# Codex L2 Prompt — v1 Template
# STATUS: READY — Phase 1 산출물 삽입 완료 (2026-04-16)
# 이 파일을 Codex 세션에 전문 복붙으로 전달

---

You are performing a blinded Level 2 claim-evidence verification task.

## Isolation Rules (CRITICAL)
This is an isolated evaluation run. Use ONLY:
1. This prompt
2. The input file specified below
3. Direct fetches to paper URLs (arXiv, ar5iv, publisher pages)

Do NOT use or rely on:
- Memory, saved memories, chat history, project context
- Previous runs, prior outputs, prior analyses
- Gold labels, human judgments, prior Claude/Codex outputs
- Comparison tables, experiment plans, session notes
- Any other local project files

If required information is unavailable from allowed materials, say so. Do not fill gaps from memory.

## Task
For each row in `04_pilots/L2_input.csv`, verify whether the cited source's full text
supports the stated claim.

## Full-Text Requirement
You MUST read the full text of the source before assigning a verdict.
Abstract-only reading is NOT sufficient.
ar5iv HTML preferred: https://ar5iv.labs.arxiv.org/html/{arxiv_id}
If only abstract is available, mark Access_Status = abstract_only.

## Official Definition Block (sole authority for verdict assignment)

[BEGIN DECISION_TREE_V1]

Step 1. Does the source full text contain content related to the claim?
  - Source inaccessible → UNCERTAIN (Access_Status = inaccessible)
  - Source does not address the claim topic at all:
      - Does the source contradict the claim? YES → REFUTE, NO → UNCERTAIN
  - Source contains related content → proceed to Step 2

Step 2. Does the claim accurately reflect the source's key content?
  - YES: scope, conditions, qualifiers, numbers, causation all preserved → SUPPORT
  - NO: one or more differences exist → proceed to Step 3

Step 3. Does the difference change the claim's core assertion? (Apply Materiality Test)
  - NO: cosmetic difference → SUPPORT
    Examples: "~90%" → "90%", "LLMs" → "Large Language Models"
  - YES: material difference → proceed to Step 4

Step 4. Does the source explicitly address the claim's key concept?
  - NO: the concept does not appear in the source, but the citing document attributes it
    → PARTIAL-MAJOR (attribution gap)
    Example: source never mentions "lazy loading" but claim says "this paper justifies lazy loading"
  - YES: source addresses it but claim overstates scope/status/causation
    → PARTIAL-MINOR (overstatement)
    Example: source says "proposed framework" but claim says "established standard"

Principles:
1. Source text only: base verdicts on what is actually written, not background knowledge
2. Strongest passage: judge against the passage that most strongly supports the claim
3. Tentative language: if source uses "may/suggests/could" but claim uses "shows/demonstrates/proves", that is material
4. Scope preservation: if source limits to specific conditions/domains but claim generalizes, that is material
5. Single strongest claim: if multiple sub-claims exist, judge the most central one

[END DECISION_TREE_V1]

[BEGIN MATERIALITY_TEST_V1]

Use this table at Step 3 to determine if a difference is cosmetic or material:

| Difference Type | SUPPORT (cosmetic) | PARTIAL (material) | Rule |
|---|---|---|---|
| Numbers | "~90%" → "90%" | "82% with COT" → "82% baseline" (condition dropped) | Dropping conditions = material |
| Scope | "in LLMs" → "in GPT-4" (subset OK) | "in pathology" → "generally" (overgeneralization) | Expanding to superset = material |
| Causation | "A correlates with B" → "A relates to B" | "A correlates with B" → "A causes B" | Correlation→causation = always material |
| Prescription | "X is one approach" → "X is an approach" | "X is one approach" → "X is recommended" | Description→prescription = material |
| Status | "proposed methodology" → "proposed framework" | "proposed framework" → "established standard" | Status elevation = material |
| Abbreviation | "LMs" → "Language Models" | "Lost in the Haystack" → "Hidden in the Haystack" | Meaning change possible = material |
| Attribution | "paper studies X" → "paper covers X" | "one experimental condition" → "paper recommends X" | Elevating minor contribution to main = material |

Boundary principle: when in doubt, classify as material (conservative).
Test: "Would a reader who read the source get a different impression from this claim?" If YES = material.

[END MATERIALITY_TEST_V1]

[BEGIN EDGE_CASE_BANK_V1]

E1 (SUPPORT boundary): Abbreviation expansion
- Claim: "Large Language Models show emergent capabilities"
- Source: "LLMs show emergent capabilities"
- Verdict: SUPPORT — obvious abbreviation, no meaning change

E2 (SUPPORT boundary): Subset specification
- Claim: "This was observed in GPT-4"
- Source: "This was observed across multiple LLMs including GPT-4"
- Verdict: SUPPORT — claim narrows scope (subset), does not overstate

E3 (PARTIAL-MINOR): Status elevation
- Claim: "PRISMA-trAIce establishes the norm for AI disclosure"
- Source: "We propose a checklist for AI-assisted systematic review reporting"
- Verdict: PARTIAL-MINOR — source addresses AI disclosure (concept present) but "propose" ≠ "establishes the norm"

E4 (PARTIAL-MINOR): Scope overgeneralization
- Claim: "Experts are biased by AI output"
- Source: "In pathology TCP estimation, 28 experts showed 7% automation bias rate"
- Verdict: PARTIAL-MINOR — automation bias concept is present, but domain (pathology) and scale (n=28) are dropped

E5 (PARTIAL-MAJOR): Attribution gap
- Claim: "This paper's scaling law justifies lazy loading architecture"
- Source: sigmoid scaling law showing quality saturates at ~16 agents. "lazy loading" never mentioned.
- Verdict: PARTIAL-MAJOR — scaling law exists but "lazy loading" is not in the source at all

E6 (PARTIAL-MAJOR): Description→prescription leap
- Claim: "The paper recommends blind-first review"
- Source: reports automation bias exists (7% AB rate) but makes no design recommendations
- Verdict: PARTIAL-MAJOR — "blind-first review" as a specific design is not addressed in the source

E7 (REFUTE - synthetic): Direct contradiction
- Claim: "This technique improves performance"
- Source: "We found this technique significantly degraded performance across all benchmarks"
- Verdict: REFUTE — source explicitly states the opposite

E8 (REFUTE - synthetic): Statistical reversal
- Claim: "Multi-agent systems consistently outperform single agents"
- Source: "No statistically significant difference between multi-agent and single-agent (p=0.42)"
- Verdict: REFUTE — "no significant difference" contradicts "consistently outperform"

E9 (UNCERTAIN): Tangentially related
- Claim: "This paper supports our verification framework's structured approach"
- Source: PRISMA 2020 — systematic review reporting guideline. No content about citation verification.
- Verdict: UNCERTAIN — formal similarity (both use checklists) but different domains entirely

E10 (UNCERTAIN): Access failure
- Claim: any claim
- Source: behind paywall, only abstract accessible. Abstract does not address claim.
- Verdict: UNCERTAIN (Access_Status = abstract_only) — cannot assign substantive verdict

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
7. **THEN apply** decision tree + materiality test to assign Verdict
8. Write one CSV row
9. Repeat for all rows

## Quality Rules
- Do NOT normalize away meaningful differences unless the Definition Block says to
- Do NOT upgrade tentative language ("may", "suggests") into strong claims
- Do NOT treat implied plausibility as textual support
- Do NOT use background knowledge to repair missing evidence
- Do NOT infer author intent beyond what the source text states
- If using a search engine to locate a paper: do NOT base verdict on search snippets (navigation only)

## Output Schema
Save to `04_pilots/codex_L2_results.csv` with exactly these columns (order matters):

```
ID,Evidence_Section,Evidence_Quote,Evidence_Strength,Why_Not_Stronger,Why_Not_Weaker,Verdict,Verdict_Sub,Confidence,Justification,Source_URL,Verification_Basis,Access_Status,Time_Min
```

Column definitions (evidence columns BEFORE verdict columns):
- ID: copy from input
- Evidence_Section: section name in source (e.g. "Section 3.2", "Table 2")
- Evidence_Quote: most relevant verbatim quote from source (max 20 words)
- Evidence_Strength: strong / moderate / weak / none
- Why_Not_Stronger: 1 sentence — why not a stronger support level
- Why_Not_Weaker: 1 sentence — why not a weaker support level
- Verdict: SUPPORT / PARTIAL / REFUTE / UNCERTAIN
- Verdict_Sub: MAJOR / MINOR (only if Verdict=PARTIAL, else blank)
- Confidence: HIGH / MEDIUM / LOW
- Justification: 1-2 sentence verdict rationale
- Source_URL: exact URL actually accessed for this paper
- Verification_Basis: full_text_direct_fetch / abstract_only / search_only / access_failure
- Access_Status: full_text_accessed / abstract_only / inaccessible
- Time_Min: minutes spent on this pair

## Substantive-Verdict Constraint
If Access_Status is NOT full_text_accessed, do NOT assign SUPPORT / PARTIAL / REFUTE.
Use UNCERTAIN with Justification = "full text not accessed".

## Evidence Rules
- Base judgment on the most relevant source passage, not on title, abstract, or assumed contribution
- If the claim overstates the source, explain exactly what is overstated
- If the source does not mention the claim's key concept, state that explicitly
- If the source supports only a weaker version of the claim, record that as such

## Final Checklist
Before saving, verify every row has:
- [ ] Source_URL filled
- [ ] Verification_Basis filled
- [ ] Evidence_Section filled
- [ ] Evidence_Quote filled
- [ ] Access_Status filled
- [ ] Input order preserved
- [ ] No reliance on prior sessions or unattached files

## Constraints
- Read ONLY `04_pilots/L2_input.csv` from this project
- Do NOT read any other project files
- Specifically FORBIDDEN: pilot_L2_results.csv, pilot_L2_report.md, pilot_L2_supplement.md,
  gold_standard_*.md, L2_VALIDATION_PLAN_FULL.md, error_taxonomy.md,
  claude_L2_independent.csv, CODEX_L1_FEEDBACK.md
- You MUST fetch and read the actual paper. Do not rely on memory.

Save only the CSV to `04_pilots/codex_L2_results.csv`.
Do not read or write any other project files.
