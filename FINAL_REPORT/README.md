# DysLex-Probe Thesis (BRAC University CSE400)

**Title:** Probing Cross-Lingual Lexical Representations in Multilingual LLMs for Low-Resource Dyslexia Screening

**Supervisor:** Dr. Farig Sadeque

## Build

Requires **XeLaTeX** (not pdfLaTeX) because Bangla characters use `fontspec` + `polyglossia` + `FreeSerif` (Bengali script).

```bash
# 1. (Optional) Re-copy plots from the per-model dirs into images/
bash copy_plots.sh

# 2. Compile (three xelatex passes + biber)
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

If `FreeSerif` is unavailable, replace `\newfontfamily\banglafont[Script=Bengali]{FreeSerif}` in `main.tex` with `Noto Serif Bengali` or any installed Bengali-script font.

## Layout

```
.
├── main.tex                # entry point; XeLaTeX
├── README.md               # this file
├── copy_plots.sh           # copies 20 plots from ../<model>/ into images/
├── core/                   # titlepage, declaration, approval, ethics, abstract, dedication, acknowledgement
├── chapters/               # 1 Intro, 2 LitReview, 3 Reqs/Impacts, 5 Methodology, 6 Results, 9 Conclusion
├── appendix/               # Appendix A reproducibility, Appendix B stimuli
├── bibliography/           # references.bib (IEEE numeric)
└── images/                 # populated by copy_plots.sh
```

## Notes

- Author placeholders (`Student ID`, `Program Coordinator`, `Head of Department`) in `core/declaration.tex` and `core/approval.tex` still need filling.
- 11 of the 20 copied plots are referenced in `chapters/chapter_6.tex`; the remainder are available for the discussion if needed.
- All result numbers in Chapter 6 trace to `comparison_four_models.md` in `../dyslexia-mt5/` and `comparison_three_models.md` in `../dyslexia-bloom/`.
