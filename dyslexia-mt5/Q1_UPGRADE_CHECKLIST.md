# Q1 Upgrade Checklist -- Code to Add

Goal: keep the 4 models (XLM-R, mT5, BLOOM, Llama) as-is; add the analysis code
that moves the work from "good conference paper" to Q1-journal rigor.

Legend:
- [REUSE]  runs on data already on disk (no model re-run)
- [RE-EXTRACT]  needs activations re-saved for XLM-R / Llama / BLOOM (code already in main.ipynb)
- [NEW RUN]  needs new model(s) downloaded/run (optional axis)

Current state of saved data:
- representations/ has RAW activations for mT5 ONLY (45 MB x many files).
- All 4 models have only AGGREGATED per-layer numbers in results_*.csv
  (point estimates, single seed random_state=42, no variance, no CIs).

---

## 0. Plumbing that unlocks everything (do first)

- [ ] **0.1 Save all 4 models' activations** [RE-EXTRACT]
      Refactor the notebook extraction cells to dump per-item, per-layer reps for
      XLM-R, Llama, BLOOM into representations/ (same format as mt5_*_reps.npy),
      plus the matching id arrays. Without this, items 1.x and 3.x cannot get CIs
      for 3 of the 4 models.
- [ ] **0.2 Extract probing into a reusable module** (probing_lib.py)
      Functions: load_reps(model) -> probe(layer, seed) -> predictions.
      Turn the notebook cells into callable functions so every analysis below is a
      short script, not copy-pasted cells. Log seed + git hash + library versions.

## 1. Statistical rigor (highest value, lowest cost)

- [ ] **1.1 Bootstrap 95% CIs** on L0 / peak / gain accuracy and on transfer F1,
      per model x language. [REUSE for mT5, RE-EXTRACT for other 3]
      Replaces every point estimate in results_realword_length_matched.csv and
      results_transfer_realword_matched.csv with mean +/- CI.
- [ ] **1.2 Significance test: probe vs surface baseline** [REUSE/RE-EXTRACT]
      Paired bootstrap or permutation test that peak accuracy really exceeds the
      surface_EN / surface_BN columns. This is the core claim; it needs a p-value.
- [ ] **1.3 Significance test: transfer vs chance** [REUSE/RE-EXTRACT]
      Permutation test (shuffle labels) for bn_transfer_f1 above 0.5.
- [ ] **1.4 Model-vs-model comparison** with CIs (is Llama's gain really > XLM-R's?).
- [ ] **1.5 Multiple-comparison correction** (Holm-Bonferroni or FDR) across the
      many layer x task x model tests. Q1 reviewers will ask.
- [ ] **1.6 Effect sizes** (accuracy delta with CI / Cohen's d), not just p-values.

## 2. Probe validity controls (standard Q1 probing requirements)

- [ ] **2.1 Control-task selectivity** (Hewitt & Liang 2019) [RE-EXTRACT]
      Train the probe on random labels; report selectivity = real acc - control acc.
      Shows the probe reads structure, not just memorizes. Often a reviewer's #1 ask.
- [ ] **2.2 Random-embedding / untrained-layer baseline** -- probe random vectors to
      establish the floor.
- [ ] **2.3 Linear vs MLP probe** -- confirm a linear probe suffices (or report both),
      to rule out "the probe, not the model, learned the task."

## 3. Robustness / reproducibility

- [ ] **3.1 Multiple seeds** (>= 5) for probe training; report mean +/- SD across seeds.
      Currently single seed=42. [REUSE/RE-EXTRACT]
- [ ] **3.2 k-fold cross-validation** instead of one split, CIs across folds.
- [ ] **3.3 Sample-size / power analysis** for n=50; either justify it or expand stimuli.
- [ ] **3.4 requirements.txt + frozen seeds + a one-command reproduce script.**

## 4. Downstream / applied validation (turns the probe into a METHOD)

- [ ] **4.1 Screening classifier** [REUSE for mT5, RE-EXTRACT for others]
      Use probe features -> classify difficulty / error_type_targeted (columns already
      in dyslex_probe_stimuli_clean.csv). Report AUC / F1 with CIs.
- [ ] **4.2 Baseline comparison** -- probe-feature classifier vs surface-feature
      classifier vs random. Show the LLM representation beats the surface baseline.
- [ ] **4.3 Cross-lingual screening** -- train screening on EN probe features, test on
      BN (the low-resource payoff). This is the headline applied result.

## 5. Mechanism / generality (optional new-model axis)

- [ ] **5.1 Same-family scaling sweep** [NEW RUN]
      One family at 3-4 sizes (e.g. BLOOM 560M/1.1B/1.7B/3B or Pythia). Reuse the
      probing module from 0.2. Adds the "why/when does transfer emerge" mechanism
      claim WITHOUT replacing the 4 diverse models.
- [ ] **5.2 Emergence-vs-scale analysis** -- emergence layer / peak transfer as a
      function of model size across the sweep.

## 6. Causal ablation hardening (extend what already exists)

- [ ] **6.1 Add CIs + a proper random-ablation control distribution** to the existing
      specificity numbers (results_ablation_*.csv). [REUSE -- ablation reps already saved for mT5]
- [ ] **6.2 Extend ablation beyond mT5** if 0.1 is done for the other models. [RE-EXTRACT]

---

## Suggested order (value per effort)
1. Section 0 (plumbing)  ->  unlocks the rest
2. Section 1 (statistics)  ->  biggest credibility gain, mostly existing data
3. Section 2 (probe controls)  ->  closes the obvious reviewer objection
4. Section 4 (downstream)  ->  turns it into a method, biggest novelty lift
5. Section 3 (robustness)  ->  seeds + CV
6. Section 5 (scaling sweep)  ->  optional mechanism axis, only if GPU time allows
7. Section 6 (ablation CIs)  ->  quick polish

## Do NOT change
- The 4 models, the 440-item dataset, or any EXISTING reported number without sign-off.
  New analyses ADD columns (CIs, p-values, AUC); they do not overwrite the point
  estimates already in the thesis.
