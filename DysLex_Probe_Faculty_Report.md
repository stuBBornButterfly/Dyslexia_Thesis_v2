# DysLex-Probe: A Plain-Language Summary of Our Findings

**Faculty Findings Report**

| | |
|---|---|
| Supervisor | Dr. Farig Sadeque, Department of CSE, BRAC University |
| Date | June 2026 |
| Status | Final findings, ready for review |

---

## What the project is about

Dyslexia is a reading difficulty that affects how children learn to recognise words and the sounds in them. Doctors usually catch it with special sound-based tests. These tests exist for English, but they do not exist for most other languages, including Bangla. Bangla is spoken by more than 270 million people, and right now there is no good automatic screening tool for dyslexia in Bangla.

Big AI language models (called multilingual large language models, or LLMs) are trained on many languages at once. They might already understand a lot about how words and sounds work across languages. If that is true, then one AI model could help build screening tools for many languages at the same time, without needing a separate model for each language.

This project tested four well-known AI models to find out:

1. Which model is best at carrying useful knowledge from English to Bangla?
2. Does the knowledge actually live in the model, or is the model just using simple tricks?
3. Where inside the model does this knowledge sit?

---

## What we did

The whole study runs through a single pipeline (Figure 1): each of the four AI models gets the same 440 stimuli, we extract its internal representations, train a simple classifier, and check the results under strict sanity controls.

![Figure 1. End-to-end study pipeline.](FINAL%20YEAR%20THESIS%20Template_CSE400_Fall%202024%20ONWARDS/images/fig_pipeline.png)

We worked with four AI models that cover the main types of multilingual LLMs:

| Model | Type | Size | Bangla in training data? |
|---|---|---|---|
| XLM-RoBERTa large | Encoder-only | 0.56 billion parameters | Yes |
| Llama 3.1 8B | Decoder-only | 8 billion parameters | Very little |
| BLOOM 7B1 | Decoder-only | 7.1 billion parameters | Yes |
| mT5 XL | Encoder-decoder | 3.7 billion parameters | Yes |

The four architectures side by side are shown in Figure 2.

![Figure 2. Architectural comparison of the four probed multilingual LLMs.](FINAL%20YEAR%20THESIS%20Template_CSE400_Fall%202024%20ONWARDS/images/fig_models.png)

We built a test set of 440 items, half in English and half in Bangla, covering seven categories like minimal pairs (words that differ by one sound), pseudo-words, real words, multisyllabic words, rhymes, and short sentences. A native Bangla speaker checked all the Bangla items.

For each model, we passed every item through the model and looked at how the model represented it on the inside. Then we trained a very simple classifier on the English representations and asked: how well does it work on Bangla?

We also ran three honesty checks to make sure the model was really doing language work and not just using shortcuts like word length or the first letter of the word.

Finally, we did a test called causal ablation: we turned off small parts of the AI model on purpose and saw whether its Bangla performance dropped. This tells us where in the model the useful knowledge lives.

---

## What we found

### Finding 1: Most of the standard tests are not actually testing what we thought

Three of the four standard tests turned out to be solvable by cheap tricks.

- The voicing test (telling voiced sounds from voiceless ones) could be answered just by looking at the first letter of the Bangla word. The AI was not doing any sound work at all; it was just memorising letters.
- The spelling regularity test and the syllable counting test could be answered using basic features like word length, byte length, number of unique characters, and so on. The big AI models did not do any better than this simple shortcut.
- Only the test that asks the model to tell a real word from a made-up word survived our honesty checks, and only after we carefully matched the real and fake words to be the same length.

**This is the most important finding of the whole project.** It means a lot of past research about AI models understanding sounds across languages may have been measuring something simpler than they thought.

![Figure 3. Bangla voicing labels are recoverable from the first character alone (F1 0.78 to 0.94 across all four models). The probe is reading letter identity, not phonological voicing.](FINAL%20YEAR%20THESIS%20Template_CSE400_Fall%202024%20ONWARDS/images/plots_bn_voicing_sanity.png)

### Finding 2: Two of the four models actually work well; the other two fail

On the surviving real-vs-fake-word test, here is how each model did on Bangla:

| Model | Bangla accuracy (F1) | Gain over the simple shortcut | Verdict |
|---|---|---|---|
| BLOOM 7B1 | 0.92 | +0.30 | Works well |
| XLM-RoBERTa large | 0.86 | +0.24 | Works well |
| Llama 3.1 8B | 0.63 | +0.01 | Fails |
| mT5 XL | 0.60 | -0.02 | Fails |

Two things to note. First, the models that work well are the ones that have Bangla data in their training set. The one that does not (Llama) fails. Second, a small model (XLM-R, only 0.56 billion parameters) beats a much bigger model (Llama, 8 billion parameters) by a wide margin on Bangla. **Having Bangla in the training data matters much more than having a bigger model.**

![Figure 4. Cross-lingual transfer to Bangla on the length-matched real-vs-pseudo word task. BLOOM and XLM-R clearly beat the simple shortcut baseline; Llama and mT5 do not.](FINAL%20YEAR%20THESIS%20Template_CSE400_Fall%202024%20ONWARDS/images/plots_transfer_realword_matched.png)

![Figure 5. The same picture per layer for each model on every task. Only the bottom-row (length-matched realword) curves are honest measurements; the other rows reflect surface shortcuts.](FINAL%20YEAR%20THESIS%20Template_CSE400_Fall%202024%20ONWARDS/images/plots_four_models_transfer.png)

### Finding 3: One model (mT5) shows something rare and interesting

When we turn off small parts of mT5 on purpose, the Bangla performance drops by a clean amount. When we do the same to the other three models, the drop is either zero or random. This means mT5 has its cross-language knowledge stored in a small, specific set of locations inside the model, while the other models spread it out everywhere.

We then repeated this test at five different depths inside mT5, and the same pattern showed up at every depth. Two units in particular (numbered 782 and 1880) showed up again and again across most depths, like a kind of backbone.

This is interesting because no other model in our comparison has this property. mT5 is the only one where we can look inside and clearly see where the cross-language knowledge lives.

![Figure 6. Ablation across the four models. Turning off the top-ranked units only causes a clean Bangla drop in mT5; the others show no clear effect.](FINAL%20YEAR%20THESIS%20Template_CSE400_Fall%202024%20ONWARDS/images/plots_four_models_ablation.png)

![Figure 7. mT5 unit overlap across encoder depths. Two units (782 and 1880) keep appearing in the top-10 ranked set at most depths, forming a backbone.](FINAL%20YEAR%20THESIS%20Template_CSE400_Fall%202024%20ONWARDS/images/plots_mt5_unit_overlap.png)

### Finding 4: The four models are good at different things

There is no single best model. The right answer depends on what you want to do:

- If you want the **highest Bangla performance** for a real screening prototype: use **BLOOM 7B1**.
- If you want to **understand how the AI represents language**: use **mT5 XL**.
- If you have **limited hardware**: use **XLM-RoBERTa large** (small but strong).
- For Bangla cross-lingual work, **do not use Llama**. It collapses.

---

## What we recommend

1. **For a real working Bangla dyslexia screening tool**, start with BLOOM 7B1. It is the best at carrying knowledge from English to Bangla.
2. **For deeper research into how multilingual AI works**, use mT5 XL. It is the only model where we can actually find the parts that hold the cross-language knowledge.
3. **For low-budget or hardware-limited deployments**, use XLM-RoBERTa large. It is much smaller but almost as good.
4. **For any future research like this**, always run sanity checks first. Three out of four standard tests in this area were measuring shortcuts, not real language understanding. This is the most useful methodology lesson from the project.

---

## What this work cannot do

We want to be clear about what this project does and does not say.

- This is **not** a clinical diagnostic tool. A model with 0.92 accuracy on a research task cannot diagnose dyslexia in a child. Using it as if it could would harm children.
- The tests use a small number of items (50 matched word pairs per language). The numbers are point estimates, not guarantees.
- mT5 is the only encoder-decoder model we tested. The interesting backbone-units finding could be specific to mT5 or general to all encoder-decoder models. We cannot tell without testing more models.
- All Bangla voicing numbers in the early part of the work turned out to be unusable because the labels were guessable from the first letter. We honestly report this rather than hide it.

---

## In one sentence

The most useful single thing this project found is that three out of four standard tests in this area do not measure what people thought they measured, and once we fix the tests, BLOOM and XLM-R turn out to be the best multilingual AI models for low-resource Bangla lexical work, while mT5 is the most informative model for understanding how cross-language knowledge is stored inside an AI.

All numbers in this report come from real experiments. Full per-model and per-layer numbers are saved in the project files (`comparison_four_models.md`, `comparison_three_models.md`, and per-model CSVs). The full thesis manuscript contains the complete methodology, all tables, and all figures.
