# CO-PO Mapping vs. Thesis: Gap Analysis

**Source rubric:** `co_po_mapping.xlsx` (CSE400 final-year thesis rubric, BRAC University).
**Thesis under review:** DysLex-Probe thesis at `FINAL YEAR THESIS Template_CSE400_Fall 2024 ONWARDS/`.
**Date of comparison:** 2026-06-05.

This document walks through each Course Outcome (CO1 through CO14) row in the rubric, checks whether the thesis content matches the rubric's expected chapter and section, and lists every weakness or mismatch that should be fixed before the panel review.

---

## Chapter-to-file mapping in the current thesis

| TOC chapter (rendered) | File on disk | Status |
|---|---|---|
| Chapter 1 Introduction | `chapters/chapter_1.tex` | OK |
| Chapter 2 Literature Review | `chapters/chapter_2.tex` | OK |
| Chapter 3 Requirements, Impacts and Constraints | `chapters/chapter_3.tex` | OK |
| **Chapter 4 Proposed Methodology** | `chapters/chapter_5.tex` | OK in TOC; rubric also calls it Chapter 4 |
| **Chapter 5 Result Analysis** | `chapters/chapter_6.tex` | OK in TOC; rubric also calls it Chapter 5 |
| Chapter 6 Conclusion | `chapters/chapter_9.tex` | OK |

Numbering in the rendered PDF matches what the rubric expects at chapter level. The mismatches below are all at the **section** level inside Chapter 1 and Chapter 5.

---

## CO-by-CO gap analysis

### CO1 (PO2): Formulate a complex engineering problem — Chapter 1

Rubric expects: `1.1 Background`, `1.2 Rational[e]`, `1.2 Problem Statement` (the duplicate `1.2` is the rubric's own typo, second item should read `1.3`), `1.3 Objective`, `1.4 Methodology in Brief`, `1.5 Scopes and Challenges`.

Thesis has, in order:

1. Background
2. Rationale of the Study or Motivation
3. Problem Statement
4. **Research Questions  (NEW, not in rubric)**
5. Objective
6. Methodology in Brief
7. Scopes and Challenges

**Weakness 1 (medium).** The newly added "Research Questions" section in Chapter 1 shifts the numbering: in the rubric, "Objective" should be `1.3`, "Methodology in Brief" should be `1.4`, and "Scopes and Challenges" should be `1.5`. In the current thesis they are `1.4`, `1.5`, `1.6` after the new section is inserted. The panel CO-PO checker will need to be told that the rubric's section numbers have shifted by one. Two fix options:

- Keep the RQ section and add a one-line note on the cover sheet that says "Research Questions section added between Problem Statement and Objective; subsequent 1.x numbering shifts by one".
- Or move the RQ content into a final paragraph at the end of "Problem Statement" so the rubric numbering is preserved.

---

### CO2 (PO3): Final specifications and requirements — Chapter 3 §3.1

Rubric expects: `Chapter 3: 3.1 Final Specifications and Requirements`.

Thesis: §3.1 Final Specifications and Requirements is present and covers data, model, software, hardware and reproducibility requirements.

**Status: OK.** No weakness.

---

### CO3 (PO6): Societal, health, safety, legal, cultural impact — Chapter 3 §3.2

Rubric expects: `Chapter 3: 3.2 Societal Impact`.

Thesis: §3.2 Societal Impact is present and covers clinical-gap framing and bounded-claim discipline.

**Weakness 2 (low).** The rubric language mentions "health, safety, legal and cultural" but our current §3.2 emphasises societal and clinical impact and only briefly touches legal (license use in §3.4) and does not explicitly discuss health-and-safety implications of misuse (e.g., harm to children from false-positive screening) or cultural context (e.g., why Bangla-script orthography matters culturally). Recommend adding two short paragraphs to §3.2: one explicit "Health and safety implications" paragraph (already partially there but not headed) and one explicit "Legal and cultural context" paragraph.

---

### CO4 (PO7): Sustainability and environmental impact — Chapter 3 §3.3

Rubric expects: `Chapter 3: 3.3 Environmental Impact`.

Thesis: §3.3 Environmental Impact is present and discusses compute footprint, frozen vs. fine-tuned amortisation, and the sanity-check methodology contribution.

**Status: OK.** No weakness.

---

### CO5 (PO3): Design multiple solutions and verify — Chapter 4 §4.1, §4.2

Rubric expects: `Chapter 4: 4.1 Design Process or Methodology Overview` and `Chapter 4: 4.2 Preliminary Design or Design (Model) Specification`.

Thesis: both sections are present at the top of `chapter_5.tex` with the exact rubric titles. Three design alternatives (A: fine-tune, B: single-layer, C: per-layer probing with sanity controls; C selected) are described as required.

**Status: OK.** No weakness at the section-title level.

---

### CO6 (PO4): Analyse and assess alternative designs — Chapter 5 §5.1, §5.2, Final Design Adjustment, §5.3, §5.4, §5.6

Rubric expects the following sections in Chapter 5:

- `5.1 Performance Evaluation`
- `5.2 Analysis of Design Solutions`
- `Final Design Adjustment`
- `5.3 Statistical Analysis`
- `5.4 Comparisons and Relationships`
- `5.6 Discussion`

Thesis (current) has, after my refactor of `chapter_6.tex`:

1. Evaluation Criteria and Reporting Conventions
2. RQ1: In-Language English Probing across the Four Models
3. Surface-Feature Sanity Checks Invalidate Three of Four Tasks
4. RQ2: Length-Matched Cross-Lingual Transfer
5. Representational Similarity Analysis Corroborates the Transfer Split
6. RQ3: Causal Forward-Hook Ablation on Length-Matched Realword
7. mT5 Localisation across Encoder Depth (RQ3 extension)
8. Final Design Adjustments
9. Statistical Analysis
10. RQ4: Cross-Model Comparison and Model Selection
11. Discussion
12. Limitations

**Weakness 3 (HIGH, this is the biggest single gap).** None of the rubric-expected section titles for Chapter 5 are present verbatim. The CO6 evaluator panel and the supervisor will be checking the rubric strings against the table of contents, and the current TOC does not match. Specifically:

| Rubric section | Present in current thesis? | Where |
|---|---|---|
| 5.1 Performance Evaluation | NOT named that | renamed to "Evaluation Criteria and Reporting Conventions" (5.1) |
| 5.2 Analysis of Design Solutions | NOT present as a section | split into RQ1, sanity checks, RQ2, RSA, RQ3, mT5 sections (5.2–5.7) |
| Final Design Adjustment | present | §5.8 (rubric implies it should be §5.2 or §5.x with that label) |
| 5.3 Statistical Analysis | present | §5.9 in current TOC, not §5.3 |
| 5.4 Comparisons and Relationships | NOT named that | renamed to "RQ4: Cross-Model Comparison and Model Selection" (§5.10) |
| 5.6 Discussion | present | §5.11 in current TOC, not §5.6 |

Two fix options:

- **Option A (recommended for rubric alignment): re-add the rubric-named umbrella sections.** Keep all my deeper RQ-tagged subsections, but wrap them under the rubric's section names. Specifically:
  - §5.1 Performance Evaluation [umbrella] → contains RQ1 + sanity-checks + RQ2 + RSA as subsections
  - §5.2 Analysis of Design Solutions [umbrella] → contains RQ3 + mT5 localisation as subsections
  - §5.3 Final Design Adjustments
  - §5.4 Statistical Analysis
  - §5.5 Comparisons and Relationships → contains RQ4 cross-model comparison + relationship to prior work
  - §5.6 Discussion → contains interpretation, implications, limitations
- **Option B: rename my section headings to exactly match the rubric** without restructuring. Simpler but loses the RQ-traceability that makes the chapter readable.

Going with Option A is the right move because it preserves both rubric compliance and the deeper analytical structure. Net effect: about six new umbrella section headers added; all current content stays in place as subsections.

---

### CO7 (PO3): Complete the final design with adjustments — Chapter 5 (rubric says §5.2 Final Design Adjustments)

Rubric expects: `Chapter 5: 5.2 Final Design Adjustments`.

Thesis: a "Final Design Adjustments" section is present as §5.8 (not §5.2 as the rubric mapping cell suggests). The content is correct (two adjustments: pruning to length-matched realword, depth-scan extension).

**Weakness 4 (low, resolved by fixing Weakness 3 Option A above).** Section number mismatch; will be resolved by the umbrella restructure.

---

### CO8 (PO5): Use modern engineering/IT tools — Presentation + report

Rubric expects: "Selection of appropriate tools" and "Usage of tools" demonstrated, with assessment via "Final Thesis Report Presentation and Demo".

Thesis: Appendix A (Software, Hardware, Reproducibility) lists the full tool stack (PyTorch, transformers, scikit-learn, Unsloth, bitsandbytes, etc.) and the per-model environment files.

**Weakness 5 (low).** Appendix A satisfies the rubric content, but the appendix is not titled or framed as "Tools Used"; the CO-PO panel may miss it. Recommend:

- Add a short cross-reference paragraph at the end of Chapter 4 §4.4 (Implementation of Selected Design) saying "The full software and hardware stack used in this study is enumerated in Appendix A: Software, Hardware and Reproducibility."
- Optionally rename Appendix A to "Appendix A: Tools, Software, Hardware and Reproducibility" so the rubric keyword "tools" appears in the appendix title.

The 5 marks from Defense Panel for CO8 are scored on the presentation itself; that is a separate deliverable.

---

### CO9 (PO12): Literature survey — Chapter 2 §2.1, §2.2, §2.3

Rubric expects: `Chapter 2: 2.1 Preliminaries`, `2.2 Review of Existing Research`, `2.3 Summary of Key Findings`.

Thesis: §2.1 Preliminaries, §2.2 Review of Existing Research, §2.3 Summary of Key Findings are all present with the exact rubric titles and substantial content.

**Status: OK.** No weakness.

---

### CO10 (PO11): Resource management — Chapter 3 §3.6, §3.7

Rubric expects: `Chapter 3: 3.6 Project Management Plan` and `Chapter 3: 3.7 Risk Management`.

Thesis: both sections present with rubric-matching titles. §3.6 has five phases and resources; §3.7 has five identified risks with mitigations.

**Status: OK.** No weakness.

---

### CO11 (PO11): Economic analysis — Chapter 3 §3.8

Rubric expects: `Chapter 3: 3.8 Economic Analysis`.

Thesis: §3.8 Economic Analysis is present (~one paragraph on amortisation and frozen-vs-fine-tune cost).

**Weakness 6 (medium).** The current §3.8 is short (about 120 words) and reads more like a justification paragraph than an economic analysis. The rubric explicitly asks for "cost-benefit estimation". Recommend extending §3.8 to include:

- A small table with order-of-magnitude cost estimates (GPU-hours used, electricity cost in BDT or USD, cloud-API equivalent cost if BLOOM were called via Hugging Face inference endpoints, etc.).
- A one-paragraph cost-benefit discussion: estimated cost of building one Bangla screening prototype on top of BLOOM vs. estimated cost of training a per-language model from scratch.
- Possibly a paragraph on deployment cost (consumer-GPU vs. cloud) for a clinical pilot.

---

### CO12 (PO8): Ethical considerations — Chapter 3 §3.4

Rubric expects: `Chapter 3: 3.4 Ethical Issues`.

Thesis: §3.4 Ethical Issues is present and covers four ethical considerations (no human participants, model-weight licensing, clinical-claim discipline, honest negative-result reporting).

**Status: OK.** No weakness.

---

### CO13 (PO9): Team work — supervisor / co-supervisor marks

Rubric expects: Peer evaluation and instructor observation, "Supervisor and Co-Supervisor's marks".

Thesis: this study has a single student and a single supervisor (Dr. Farig Sadeque). No co-supervisor is named. Author placeholders are still empty.

**Weakness 7 (low, administrative).** Three things to fix on the administrative pages:

- Fill the `Student ID` placeholder in `core/declaration.tex:19` and `core/approval.tex:5`.
- Decide whether a co-supervisor is being assigned. If yes, add their name to `core/approval.tex`. If no, the current single-supervisor approval block is fine.
- Confirm with the program coordinator whether single-author CSE400 theses are still evaluated against CO13 at the rubric weight of 5 marks. If yes, the supervisor's mark is the only input.

---

### CO14 (PO10): Effective written and oral communication — Final Report + IEEE Journal version

Rubric expects: "Final Report, IEEE Journal version" and a poster presentation, with 20 marks split across P2 poster (5), Defense Panel final report (10), Supervisor (5).

Thesis: the full thesis manuscript is present. **There is no separate IEEE-style journal paper.**

**Weakness 8 (HIGH).** The rubric explicitly lists "IEEE Journal version" alongside the final report. The current deliverable set does not include a journal-style condensed paper. This is worth 5 to 10 marks at the panel and should be produced. Recommend:

- Produce a 6-to-8-page IEEE conference-format paper that condenses the thesis: Abstract, 1 Introduction, 2 Related Work, 3 Methodology, 4 Results, 5 Discussion, 6 Conclusion, References. The abstract we already have (250-word academic version) and the per-finding tables in Chapter 5 are reusable verbatim.
- The IEEE template (`IEEEtran.cls`) is standard and the existing `references.bib` already uses IEEE numeric style, so this is mostly a packaging exercise rather than a writing exercise.

---

## Summary of weaknesses (ranked by severity)

| # | Severity | Where | What |
|---|---|---|---|
| 3 | **HIGH** | Chapter 5 (results) | Rubric section names (5.1 Performance Evaluation, 5.2 Analysis of Design Solutions, 5.3 Statistical Analysis, 5.4 Comparisons and Relationships, 5.6 Discussion) are not present as section titles after my RQ-tagged refactor. Fix by adding umbrella sections that contain the RQ-tagged subsections. |
| 8 | **HIGH** | Deliverable set | No IEEE-style journal-format paper produced. Rubric CO14 explicitly lists "IEEE Journal version" alongside the final report. Worth up to 10 panel marks. |
| 1 | Medium | Chapter 1 | New Research Questions section shifts the 1.x numbering by one relative to the rubric. Either flag on cover sheet or merge the RQ content into the end of Problem Statement. |
| 6 | Medium | Chapter 3 §3.8 | Economic Analysis is short; rubric asks for cost-benefit estimation. Add a small table of GPU-hour and cloud-API equivalent costs and a one-paragraph cost-benefit discussion. |
| 2 | Low | Chapter 3 §3.2 | Societal Impact does not explicitly head a "Health and safety" paragraph or a "Legal and cultural" paragraph. Add both. |
| 5 | Low | Appendix A | Tools satisfied by Appendix A; cross-reference from Chapter 4 §4.4 and optionally rename appendix to include the keyword "Tools" so the panel does not miss it. |
| 4 | Low | Chapter 5 | Final Design Adjustments not at the rubric-expected §5.2 numbering; resolved automatically by fixing Weakness 3 Option A. |
| 7 | Low (admin) | `core/declaration.tex`, `core/approval.tex` | Fill `Student ID`. Decide on co-supervisor. |

---

## Suggested action order

1. **Fix Weakness 3 first** (rubric section names in Chapter 5). One large edit pass to `chapters/chapter_6.tex`. This is the highest-impact, lowest-effort fix.
2. **Address Weakness 1** (Chapter 1 numbering): either inline-merge the RQ content into Problem Statement, or add a cover-sheet note.
3. **Extend Weakness 6** (Economic Analysis): add a small cost table and one cost-benefit paragraph to `chapters/chapter_3.tex` §3.8.
4. **Address Weakness 2** (Societal Impact): add two short paragraphs to `chapters/chapter_3.tex` §3.2.
5. **Address Weakness 5** (Tools cross-reference): one-line addition to `chapters/chapter_5.tex` §4.4 plus optional appendix retitle.
6. **Address Weakness 7** (admin): fill `Student ID`, decide co-supervisor presence.
7. **Address Weakness 8 (IEEE Journal version):** produce a separate 6-8 page IEEE conference-style paper using `IEEEtran.cls`. This is a separate document, not an edit to the thesis.

All eight weaknesses are fixable in one to two days of focused work. None requires re-running experiments or re-collecting data.
