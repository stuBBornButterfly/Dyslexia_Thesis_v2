#!/usr/bin/env python3
"""Reconstruct 'Pretraining recipes on one grid' with a 5th ByT5 card (matches drawio design)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle

W, H = 1600, 1350
fig = plt.figure(figsize=(W/150, H/150), dpi=150)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(H, 0)
ax.axis("off")

BG = "#FCFBF8"
ax.add_patch(Rectangle((0, 0), W, H, facecolor=BG, edgecolor="none", zorder=0))
PURPLE = "#8A5CB0"; DARK = "#1b1b1b"; GRAY = "#4a4a4a"; FOOT = "#2c2c2c"
CHK = "#2f7d3a"; CROSS = "#b3382f"

def blend(hexc, alpha, base=(0.988, 0.984, 0.972)):
    hexc = hexc.lstrip("#")
    r, g, b = (int(hexc[i:i+2], 16)/255 for i in (0, 2, 4))
    return tuple(alpha*c + (1-alpha)*bc for c, bc in zip((r, g, b), base))

def rrect(x, y, w, h, fc, ec="none", lw=0, rad=10, z=1, alpha=1):
    ax.add_patch(FancyBboxPatch((x+rad, y+rad), w-2*rad, h-2*rad,
                boxstyle=f"round,pad={rad},rounding_size={rad}",
                facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z, alpha=alpha, mutation_aspect=1))

def txt(x, y, s, size, color=DARK, weight="normal", ha="left", va="center", style="normal", z=5, family="DejaVu Sans"):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va,
            style=style, zorder=z, family=family)

def layer_stack(cx, top, color, grayed=False, w=140, seg_h=11, gap=5):
    edge = "#9a9a9a" if grayed else color
    fill = "#e6e4e0" if grayed else blend(color, 0.16)
    y = top
    for _ in range(3):
        rrect(cx-w/2, y, w, seg_h, fill, ec=edge, lw=1.0, rad=2.5, z=3); y += seg_h+gap
    txt(cx, y+6, "⋮", 12, color=edge, ha="center"); y += 18
    for _ in range(3):
        rrect(cx-w/2, y, w, seg_h, fill, ec=edge, lw=1.0, rad=2.5, z=3); y += seg_h+gap
    return top, y-gap

def attention(cx, cy, color, causal=True, n=4, r=12, span=180):
    xs = [cx-span/2 + i*span/(n-1) for i in range(n)]
    for x in xs:
        ax.add_patch(Circle((x, cy), r, facecolor=color, edgecolor="none", zorder=4))
    pairs = [(0, 1), (1, 2), (2, 3), (0, 2), (1, 3)] if causal else [(0, 1), (1, 2), (2, 3), (0, 3)]
    for a, b in pairs:
        rad = -0.55 if (b-a) == 1 else -0.9
        style = "-|>" if causal else "<|-|>"
        ax.add_patch(FancyArrowPatch((xs[a], cy-r), (xs[b], cy-r),
                     connectionstyle=f"arc3,rad={rad}", arrowstyle=style,
                     mutation_scale=8, lw=1.3, color=color, zorder=5))

def card(x, y, w, h, color, name, kind_sub, bangla_ok, footer, arch):
    body = blend(color, 0.10)
    rrect(x, y, w, h, body, ec=blend(color, 0.30), lw=1.2, rad=14, z=1)
    hh = 58
    rrect(x, y, w, hh+14, color, rad=14, z=2)
    ax.add_patch(Rectangle((x, y+hh), w, 14, facecolor=body, edgecolor="none", zorder=2))
    txt(x+20, y+22, name, 15, color="white", weight="bold")
    txt(x+20, y+43, kind_sub, 8.5, color="white", weight="bold")
    pw, ph = 132, 28
    px, py = x+w-pw-16, y+hh/2-ph/2
    rrect(px, py, pw, ph, "white", rad=14, z=3)
    txt(px+pw/2, py+ph/2, "✓ Bangla" if bangla_ok else "✗ Bangla", 10.5,
        color=(CHK if bangla_ok else CROSS), weight="bold", ha="center")
    by = y+hh+14
    footer_y = y+h-18
    if arch in ("enc", "dec"):
        scx = x+118; top = by+28
        _, bot = layer_stack(scx, top, color, w=140)
        txt(scx, top-14, "▲ OUTPUT", 8, color=GRAY, ha="center", weight="bold")
        txt(scx, bot+15, "▲ INPUT", 8, color=GRAY, ha="center", weight="bold")
        txt(scx, bot+34, "Encoder-only" if arch == "enc" else "Decoder-only", 10, color=color, ha="center", weight="bold")
        acx = x+w*0.66; acy = by+70
        attention(acx, acy, color, causal=(arch == "dec"))
        if arch == "enc":
            txt(acx, acy+58, "↔ Bidirectional", 11, color=color, ha="center", weight="bold")
            txt(acx, acy+78, "every token sees all others", 9, color=GRAY, ha="center")
        else:
            txt(acx, acy+58, "→ Causal", 11, color=color, ha="center", weight="bold")
            txt(acx, acy+78, "each token sees only the past", 9, color=GRAY, ha="center")
    else:
        ecx = x+w*0.30; dcx = x+w*0.72; top = by+34
        _, bot = layer_stack(ecx, top, color, w=130)
        layer_stack(dcx, top, color, grayed=True, w=130)
        txt(ecx, top-14, "ENCODER", 8.5, color=DARK, ha="center", weight="bold")
        txt(dcx, top-14, "DECODER", 8.5, color=GRAY, ha="center", weight="bold")
        midy = (top+bot)/2
        ax.add_patch(FancyArrowPatch((ecx+74, midy), (dcx-74, midy), arrowstyle="-|>",
                     mutation_scale=12, lw=1.5, color=color, zorder=5))
        txt((ecx+dcx)/2, midy-11, "cross-attn", 8.5, color=color, ha="center", weight="bold")
        txt(ecx, bot+14, "probed ✓", 9, color=CHK, ha="center", weight="bold")
        txt(dcx, bot+14, "unused", 9, color=GRAY, ha="center")
        note = "byte-level input (UTF-8), no subword vocabulary" if arch == "encdec_byte" else "decoder unused, only the encoder is probed"
        txt(x+w/2, bot+34, note, 9, color=GRAY, ha="center", style="italic")
    ax.add_patch(Rectangle((x+16, footer_y-16), w-32, 1, facecolor=blend(color, 0.30), edgecolor="none", zorder=3))
    txt(x+20, footer_y, footer, 10, color=FOOT, weight="bold")

# header
txt(50, 46, "FIGURE · BACKBONES", 11, color=PURPLE, weight="bold")
txt(48, 84, "Five pretraining recipes on one grid", 23, color=DARK, weight="bold")
txt(50, 122, "The five probed backbones, one card each, spanning objective, coverage and tokenization.", 12, color=GRAY, weight="bold")

CW, CH = 720, 336
GX, GY = 40, 28
X0, Y0 = 48, 168
col = [X0, X0+CW+GX]
row = [Y0, Y0+CH+GY, Y0+2*(CH+GY)]

card(col[0], row[0], CW, CH, "#2F6FA6", "XLM-R large", "ENCODER-ONLY · MASKED LM", True,
     "0.56B · 24L · 1024h · SentencePiece · Bangla ✓", "enc")
card(col[1], row[0], CW, CH, "#C33F3C", "Llama 3.1 8B", "DECODER-ONLY · CAUSAL LM", False,
     "8B · 32L · 4096h · BPE · Bangla minimal", "dec")
card(col[0], row[1], CW, CH, "#3A9A55", "BLOOM 7B1", "DECODER-ONLY · CAUSAL LM", True,
     "7.1B · 30L · 4096h · BPE · Bangla ✓ (ROOTS)", "dec")
card(col[1], row[1], CW, CH, "#8A5CB0", "mT5 XL", "ENCODER-DECODER · SPAN CORRUPTION", True,
     "3.7B · 24 enc-L · 2048h · SentencePiece", "encdec")
card(col[0], row[2], CW, CH, "#E07B00", "ByT5 XL", "ENCODER-DECODER · SPAN CORRUPTION", True,
     "3.7B · 36 enc-L · 2560h · byte-level", "encdec_byte")

# ---- tokenization-control callout (redesigned) ----
SLATE = "#37474F"
tx, ty = col[1], row[2]
rrect(tx, ty, CW, CH, "#FFFFFF", ec="#dad6cd", lw=1.3, rad=14, z=1)
# accent tag pill (auto-sized to text via bbox)
ax.text(tx+26, ty+32, "TOKENIZATION CONTROL", fontsize=9.5, color="white", weight="bold",
        ha="left", va="center", zorder=3, family="DejaVu Sans",
        bbox=dict(boxstyle="round,pad=0.45", facecolor=SLATE, edgecolor="none"))
# headline + subtext
txt(tx+24, ty+68, "ByT5 is mT5's byte-level twin", 15.5, color=DARK, weight="bold")
txt(tx+24, ty+92, "Same architecture, objective and corpus; only the tokenizer changes.", 9.5, color=GRAY)

# two comparison mini-cards
mcw, mch = 288, 120
mcy = ty+112
def minicard(mx, color, name, tok_bold, tok_sub, chips, mono=False):
    body = blend(color, 0.09)
    rrect(mx, mcy, mcw, mch, body, ec=blend(color, 0.45), lw=1.2, rad=11, z=3)
    rrect(mx, mcy, mcw, 32, color, rad=11, z=4)
    ax.add_patch(Rectangle((mx, mcy+21), mcw, 11, facecolor=body, edgecolor="none", zorder=4))
    txt(mx+mcw/2, mcy+16, name, 13, color="white", weight="bold", ha="center")
    txt(mx+mcw/2, mcy+52, tok_bold, 12.5, color=color, weight="bold", ha="center")
    txt(mx+mcw/2, mcy+72, tok_sub, 9.5, color=GRAY, ha="center")
    n = len(chips); chw = 26 if mono else 46; gap = 6
    total = n*chw+(n-1)*gap; x0 = mx+mcw/2-total/2
    for i, ch in enumerate(chips):
        cx = x0+i*(chw+gap)
        rrect(cx, mcy+90, chw, 20, "white", ec=blend(color, 0.55), lw=1.0, rad=5, z=5)
        txt(cx+chw/2, mcy+100.5, ch, 8.5 if mono else 9.5, color=DARK, ha="center",
            family="DejaVu Sans Mono" if mono else "DejaVu Sans")
minicard(tx+24, "#8A5CB0", "mT5", "SentencePiece", "subword vocabulary", ["wa", "ter"])
minicard(tx+CW-24-mcw, "#E07B00", "ByT5", "UTF-8 bytes", "no vocabulary",
         ["77", "61", "74", "65", "72"], mono=True)
# center swap badge + arrow
amid = (tx+24+mcw + tx+CW-24-mcw)/2
aymid = mcy+mch/2-6
ax.add_patch(FancyArrowPatch((tx+24+mcw+4, aymid), (tx+CW-24-mcw-4, aymid), arrowstyle="-|>",
             mutation_scale=13, lw=2.2, color=SLATE, zorder=5))
ax.add_patch(Circle((amid, aymid), 15, facecolor=SLATE, edgecolor="white", lw=1.5, zorder=6))
txt(amid, aymid, "≠", 15, color="white", weight="bold", ha="center", z=7)
txt(amid, aymid+30, "only this", 8.5, color=SLATE, weight="bold", ha="center")
txt(amid, aymid+42, "changes", 8.5, color=SLATE, weight="bold", ha="center")
# bottom takeaway strip
sy = ty+CH-44
rrect(tx+22, sy, CW-44, 32, blend(SLATE, 0.10), ec=blend(SLATE, 0.32), lw=1.0, rad=9, z=3)
ax.add_patch(Circle((tx+42, sy+16), 5, facecolor=SLATE, edgecolor="none", zorder=5))
txt(tx+58, sy+16, "Isolates tokenization from architecture and objective", 11, color="#2b373d", weight="bold", va="center")

# design-space banner
bx, by_, bw, bh = 48, row[2]+CH+22, CW*2+GX, 60
rrect(bx, by_, bw, bh, "#F3F1EC", ec="#d9d5cc", lw=1.2, rad=12)
txt(bx+26, by_+bh/2, "DESIGN SPACE", 11, color="#7a6f5c", weight="bold", va="center")
label_end = bx+200
txt(label_end + (bx+bw-24-label_end)/2, by_+bh/2,
    "{enc-only, dec-only, enc-decoder} × {multilingual, English-heavy} × {subword, byte}",
    11, color=DARK, weight="bold", ha="center", va="center")

import sys
out = sys.argv[1] if len(sys.argv) > 1 else "fig_models_v2.png"
fig.savefig(out, dpi=220, facecolor=BG)
print("saved", out)
