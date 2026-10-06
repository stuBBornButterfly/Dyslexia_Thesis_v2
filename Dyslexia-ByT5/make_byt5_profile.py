#!/usr/bin/env python3
"""ByT5 byte-level probing profile: (a) in-language English per-task emergence;
(b) length-matched real/pseudoword Bangla zero-shot transfer vs encoder depth."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

D = "/home/accesx-denied/Ayesha/Dyslexia/Dyslexia-ByT5/"
en = pd.read_csv(D+"results_english_probing_byt5.csv")
mt = pd.read_csv(D+"results_transfer_realword_matched_byt5.csv")

ORANGE = "#E07B00"; RED = "#C33F3C"; BLUE = "#2F6FA6"; GRAY = "#7a7a7a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "axes.edgecolor": "#666", "axes.linewidth": 1.0})

fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.4, 4.5))

# ---- panel (a): English in-language per-task (F1) ----
tasks = [("voicing", RED, "Voicing", "-"),
         ("realword", ORANGE, "Real / pseudoword", "-"),
         ("ortho", BLUE, "Orthographic", "-")]
for t, c, lab, ls in tasks:
    s = en[en.task == t].sort_values("layer")
    lw = 2.8 if t == "realword" else 2.0
    axA.plot(s.layer, s.score, ls, color=c, lw=lw, label=lab, zorder=3,
             marker="o", ms=3, mec="none")
# voicing L1 spike annotation
axA.scatter([1], [0.966], s=70, facecolor="none", edgecolor=RED, lw=1.8, zorder=5)
axA.annotate("L1 peak 0.97\n(first-byte access to\nthe initial character)",
             xy=(1, 0.966), xytext=(6, 0.80), fontsize=9.5, color=RED,
             ha="left", va="center",
             arrowprops=dict(arrowstyle="->", color=RED, lw=1.3))
axA.set_title("(a)  ByT5 in-language English probing", fontsize=12.5, fontweight="bold", loc="left")
axA.set_xlabel("Encoder layer (0 = embedding, 36 = top)")
axA.set_ylabel("Probe macro-F1")
axA.set_ylim(0.45, 1.02); axA.set_xlim(-1, 37)
axA.legend(loc="lower right", frameon=True, fontsize=10, framealpha=0.95)
axA.grid(True, alpha=0.25, lw=0.7)

# ---- panel (b): matched real/pseudoword Bangla transfer vs depth ----
s = mt.sort_values("layer")
axB.plot(s.layer, s.bn_transfer_f1, "-", color=ORANGE, lw=2.8, zorder=3,
         marker="o", ms=3, mec="none", label="ByT5 Bangla transfer")
axB.axhline(0.6232, ls="--", color=GRAY, lw=1.6, zorder=2)
axB.text(0.5, 0.6232+0.012, "surface baseline 0.62", fontsize=9.5, color=GRAY, va="bottom")
axB.scatter([29], [0.920], s=80, color=ORANGE, edgecolor="white", lw=1.4, zorder=6)
axB.annotate("peak L29 = 0.92", xy=(29, 0.920), xytext=(15, 0.965),
             fontsize=10, color=ORANGE, fontweight="bold", ha="center",
             arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.3))
axB.set_title("(b)  ByT5 length-matched real/pseudoword transfer (EN$\\rightarrow$BN)",
              fontsize=12.5, fontweight="bold", loc="left")
axB.set_xlabel("Encoder layer (0 = embedding, 36 = top)")
axB.set_ylabel("Zero-shot Bangla macro-F1")
axB.set_ylim(0.28, 1.0); axB.set_xlim(-1, 37)
axB.grid(True, alpha=0.25, lw=0.7)

for a in (axA, axB):
    a.spines["top"].set_visible(False); a.spines["right"].set_visible(False)

fig.tight_layout()
import sys
out = sys.argv[1] if len(sys.argv) > 1 else "byt5_profile.png"
fig.savefig(out, dpi=200, facecolor="white", bbox_inches="tight")
if out.endswith(".png"):
    fig.savefig(out[:-4]+".pdf", facecolor="white", bbox_inches="tight")
print("saved", out)
