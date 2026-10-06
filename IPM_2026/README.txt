DysLex-Probe - Information Processing & Management submission
=============================================================

Main file : main.tex
Compiler  : XeLaTeX  (REQUIRED - pdfLaTeX will not work)
Bibliography: BibTeX (refs.bib + elsarticle-harv.bst), author-year

Ported from the ESWA submission. Body text is unchanged. Converted for IP&M:
  - author-year (Harvard/APA-style) citations via the elsarticle "authoryear"
    class option and natbib \citep
  - numbered thebibliography replaced by refs.bib + elsarticle-harv.bst
  - Elsevier highlights block added (5 items, each within the 85-char cap)
The abstract is still the ESWA one and is to be revised before submission.

Overleaf
--------
1. New Project > Upload Project > select this .zip
2. Menu > Compiler > XeLaTeX   (latexmkrc should set this automatically)
3. Menu > Main document > main.tex
Overleaf runs BibTeX automatically; no extra step needed.

Fonts
-----
fonts/ contains Noto Serif Bengali (Regular + Bold), bundled because it is a
system font and is NOT in a standard TeX Live install. Loaded by relative path.
Body font TeX Gyre Termes ships with TeX Live and is loaded by name.

Contents
--------
main.tex             full manuscript
refs.bib             40 references
elsarticle-harv.bst  Elsevier author-year bibliography style
latexmkrc            selects XeLaTeX
figs/                7 figures (Fig. 1-7)
fonts/               bundled Bengali font
