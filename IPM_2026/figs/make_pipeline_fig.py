#!/usr/bin/env python
"""
Rebuild Fig. 1 (end-to-end pipeline).

The previous version was a draw.io export that was factually wrong after ByT5
was added as the fifth model: it showed only four model boxes, said "Four
architectures", gave the depth range as "24 - 32 layers" (ByT5 has 36), and
the footer read "4 architectures".

This rebuild keeps the original layout, palette and wording, and corrects all
four. Colours are the exact values lifted from the original diagram XML.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrow

# --- palette (verbatim from the original diagram) ---------------------------
CARD_EDGE = "#d8d4ca"
BODY      = "#4f5567"
MUTED     = "#8a8b91"
FAINT     = "#a6a8b0"
SECTIONS  = [
    # bar colour, heading colour, label
    ("#E8755C", "#C7553C", "01 · DATASET",        "440 Stimuli"),
    ("#3B4FAD", "#2B3B86", "02 · MODELS",         "Frozen multilingual LLM"),
    ("#1F8F8A", "#0F6E69", "03 · REPRESENTATION", "Per-layer hidden states"),
    ("#E0A53B", "#B6821D", "04 · METHOD",         "Linear probe"),
    ("#6B3F8E", "#4D2A6C", "05 · EVALUATION",     "Evaluation"),
]
SUBS = [
    "220 EN + 220 BN · matched bilingual pairs",
    "Five architectures, weights frozen",          # was "Four"
    "24 – 36 layers per model",                # was "24 - 32"
    "LogReg / Ridge · one per layer, per model",
    "Four-step validation suite",
]
NOTES = [
    "Matched bilingual probe items,\nbalanced by surface features.",
    "Encoder, decoder, and\nencoder–decoder families.",
    "Tapped from every transformer\nblock, no fine-tuning.",
    "Trained per layer × per model\n— frozen backbone.",
    "Each step rules out a weaker\nexplanation of the prior.",
]

fig, ax = plt.subplots(figsize=(15.31, 6.46))
ax.set_xlim(0, 1531); ax.set_ylim(0, 646); ax.invert_yaxis(); ax.axis("off")

def card(x, y, w, h, **kw):
    return FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=14",
                          linewidth=1.1, **kw)

def chip(x, y, w, h, fc, text, tc="#ffffff", fs=11, weight="bold", r=6):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle=f"round,pad=0,rounding_size={r}",
                 facecolor=fc, edgecolor="none"))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            color=tc, fontsize=fs, fontweight=weight, linespacing=1.35)

# --- header ------------------------------------------------------------------
ax.text(765, 38, "DysLex-Probe end-to-end pipeline", ha="center", va="center",
        fontsize=19, fontweight="bold", color="#000000")
ax.text(765, 72, "PROBING MULTILINGUAL LLMs · EN ⇋ BN", ha="center",
        va="center", fontsize=9.5, fontweight="bold", color="#000000")

# --- cards -------------------------------------------------------------------
X0, CW, GAP, TOP, CH = 12, 274, 36, 120, 460
for i, ((bar, head, kicker, title), sub, note) in enumerate(zip(SECTIONS, SUBS, NOTES)):
    x = X0 + i * (CW + GAP)
    ax.add_patch(Rectangle((x, TOP), CW, 7, facecolor=bar, edgecolor="none"))
    ax.add_patch(card(x, TOP + 11, CW, CH, facecolor="#ffffff", edgecolor=CARD_EDGE))
    ax.text(x + 18, TOP + 94, kicker, fontsize=7.6, color=MUTED, fontweight="bold")
    ax.text(x + 18, TOP + 124, title, fontsize=12.7, color=head, fontweight="bold")
    ax.text(x + 18, TOP + 152, sub, fontsize=7.9, color=BODY)
    ax.text(x + 18, TOP + CH - 36, note, fontsize=8.2, color=BODY,
            style="italic", linespacing=1.5, va="top")
    if i < 4:  # arrow to next card
        ax.add_patch(FancyArrow(x + CW + 8, TOP + 240, GAP - 16, 0,
                     width=1.6, head_width=9, head_length=9,
                     facecolor="#3a3f50", edgecolor="none", length_includes_head=True))

# 01 dataset ------------------------------------------------------------------
x = X0
chip(x + 18, TOP + 180, 112, 100, "#E8755C", "EN\n220\nEnglish", fs=12)
chip(x + 144, TOP + 180, 112, 100, "#C7553C", "BN\n220\nBangla", fs=12)

# 02 models -- now FIVE, ByT5 added -------------------------------------------
x = X0 + (CW + GAP)
BLUE, bw, bh = "#3B4FAD", 112, 46
for j, name in enumerate(["XLM-R", "Llama", "BLOOM", "mT5"]):
    chip(x + 18 + (j % 2) * 126, TOP + 180 + (j // 2) * 60, bw, bh, BLUE, name, fs=11.5)
chip(x + 81, TOP + 300, bw, bh, BLUE, "ByT5", fs=11.5)          # the fifth model

# 03 representation -----------------------------------------------------------
x = X0 + 2 * (CW + GAP)
for j in range(9):
    ax.add_patch(Rectangle((x + 18, TOP + 182 + j * 16), CW - 36, 11,
                 facecolor="#1F8F8A" if j in (2, 5, 8) else "#b8e0dc",
                 edgecolor="none"))
ax.text(x + 18, TOP + 352, "h⁽ℓ⁾ · one representation per layer",
        fontsize=8.2, color=BODY, style="italic")

# 04 method -------------------------------------------------------------------
x = X0 + 3 * (CW + GAP)
chip(x + 18, TOP + 180, 112, 78, "#E0A53B", "LOGREG\ndiscrete class", fs=9.5)
chip(x + 144, TOP + 180, 112, 78, "#B6821D", "RIDGE\ncontinuous fit", fs=9.5)

# 05 evaluation ---------------------------------------------------------------
x = X0 + 4 * (CW + GAP)
for j, lab in enumerate(["Surface-feature sanity", "Length-matched transfer",
                         "RSA", "Causal ablation"]):
    ax.add_patch(FancyBboxPatch((x + 18, TOP + 180 + j * 44), CW - 36, 34,
                 boxstyle="round,pad=0,rounding_size=6",
                 facecolor="#6B3F8E", edgecolor="#4D2A6C", linewidth=0.8))
    ax.text(x + 30, TOP + 197 + j * 44, "●  " + lab, ha="left", va="center",
            color="#ffffff", fontsize=8.8)

# --- legend + footer ---------------------------------------------------------
for i, (bar, _, _, _) in enumerate(SECTIONS):
    lx = 14 + i * 112
    ax.add_patch(Rectangle((lx, 619), 11, 11, facecolor=bar, edgecolor="none"))
    ax.text(lx + 18, 625, ["Dataset", "Models", "Representation", "Method",
                           "Evaluation"][i], fontsize=8, color=MUTED, va="center")
ax.text(1519, 625, "Frozen models · 440 stimuli · 5 architectures",   # was 4
        ha="right", va="center", fontsize=8, color=FAINT)

fig.subplots_adjust(0, 0, 1, 1)
fig.savefig("fig_pipeline.png", dpi=150, facecolor="white")
print("Saved fig_pipeline.png")
