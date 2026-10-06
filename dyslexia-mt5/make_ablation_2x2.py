#!/usr/bin/env python
"""
Regenerate the RQ3 BN-side ablation figure as a 2x2 grid.

The original (main.ipynb, cell 11, "Plot 3") used plt.subplots(1, 4, figsize=(20, 4.5)),
which renders ~1.1 in tall in the paper and is unreadable. Same data, same colours,
same panel order -- only the layout and typography change.

Data source: comparison_four_models.xlsx, sheet "ablation_bn" (exported by that cell),
so the numbers are the notebook's, not re-derived here.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
XLSX = os.path.join(HERE, "comparison_four_models.xlsx")

MODELS = ["xlmr", "llama", "bloom", "mt5"]
DISPLAY = {"xlmr": "XLM-R", "llama": "Llama", "bloom": "BLOOM", "mt5": "mT5"}
TASKS = ["voicing", "realword", "ortho", "syllable"]

# Identical to the notebook's Plot 3
COND = [
    ("base_BN",   "baseline", "#888888", 1.0),
    ("top20_BN",  "top20",    "#d62728", 1.0),
    ("rand10_BN", "rand10",   "#1f77b4", 0.7),
]

df = pd.read_excel(XLSX, sheet_name="ablation_bn")
for col, *_ in COND:                      # "—" marks tasks that were never run
    df[col] = pd.to_numeric(df[col], errors="coerce")

plt.rcParams.update({
    "font.size": 11, "axes.titlesize": 14, "axes.labelsize": 12,
    "xtick.labelsize": 11, "ytick.labelsize": 10, "legend.fontsize": 11,
})

fig, axes = plt.subplots(2, 2, figsize=(11, 8))
x = np.arange(len(MODELS))
w = 0.27

for ax, task in zip(axes.ravel(), TASKS):
    sub = df[df.task == task].set_index("model")
    for off, (col, label, colour, alpha) in zip((-w, 0.0, w), COND):
        vals = [sub.loc[m, col] if m in sub.index else np.nan for m in MODELS]
        ax.bar(x + off, vals, w, label=label, color=colour, alpha=alpha)

    # An empty slot means "never measured", not "scored zero" -- say so, because the
    # syllable panel has genuine negative bars and a gap could be misread. One note
    # centred over the empty run, so it cannot collide with the y-axis tick labels.
    missing = [i for i, m in enumerate(MODELS)
               if m not in sub.index or pd.isna(sub.loc[m, "base_BN"])]
    if missing:
        ax.text(float(np.mean(missing)), 0.5, "not measured", ha="center", va="center",
                fontsize=11, style="italic", color="#aaaaaa",
                transform=ax.get_xaxis_transform())

    ax.set_title(task)
    ax.set_xticks(x)
    ax.set_xticklabels([DISPLAY[m] for m in MODELS])
    ax.grid(alpha=0.3, axis="y")
    ax.set_axisbelow(True)
    ax.axhline(0, color="black", lw=0.8)

for ax in axes[:, 0]:
    ax.set_ylabel("BN score")

# One figure-level legend instead of four identical per-panel ones.
fig.legend(handles=[Patch(facecolor=c, alpha=a, label=l) for _, l, c, a in COND],
           loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(0.5, -0.005))
fig.suptitle("RQ3: BN-side ablation (frozen probe) — 4 models", fontsize=15)
fig.tight_layout(rect=[0, 0.045, 1, 0.97])

out = os.path.join(HERE, "plots_four_models_ablation_2x2.png")
fig.savefig(out, dpi=200, bbox_inches="tight")
plt.close(fig)
print(f"Saved {out}")
