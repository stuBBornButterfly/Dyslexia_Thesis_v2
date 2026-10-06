#!/usr/bin/env bash
# copy_plots.sh — copy generated plots from per-model dirs into images/
# Run from inside the thesis template directory (next to main.tex).
set -e

DEST="images"
SRC_ROOT=".."

mkdir -p "$DEST"

cp "$SRC_ROOT/Dyslexia-XLM-R/plots_ablation_degradation.png"     "$DEST/"
cp "$SRC_ROOT/Dyslexia-XLM-R/plots_ablation_final.png"           "$DEST/"
cp "$SRC_ROOT/Dyslexia-XLM-R/plots_english_probing.png"          "$DEST/"
cp "$SRC_ROOT/Dyslexia-XLM-R/plots_rsa.png"                      "$DEST/"
cp "$SRC_ROOT/Dyslexia-XLM-R/plots_transfer.png"                 "$DEST/"
cp "$SRC_ROOT/Dyslexia-XLM-R/plots_transfer_ratio.png"           "$DEST/"

cp "$SRC_ROOT/dyslexia-LLM/plots_ablation_doseresponse_llama.png" "$DEST/"
cp "$SRC_ROOT/dyslexia-LLM/plots_ablation_llama_final.png"        "$DEST/"
cp "$SRC_ROOT/dyslexia-LLM/plots_rsa_llama.png"                   "$DEST/"

cp "$SRC_ROOT/dyslexia-bloom/plots_ablation_bloom_final.png"     "$DEST/"
cp "$SRC_ROOT/dyslexia-bloom/plots_ablation_llama_vs_bloom.png"  "$DEST/"
cp "$SRC_ROOT/dyslexia-bloom/plots_rsa_bloom.png"                "$DEST/"

cp "$SRC_ROOT/dyslexia-mt5/plots_bn_voicing_sanity.png"          "$DEST/"
cp "$SRC_ROOT/dyslexia-mt5/plots_four_models_ablation.png"       "$DEST/"
cp "$SRC_ROOT/dyslexia-mt5/plots_four_models_english.png"        "$DEST/"
cp "$SRC_ROOT/dyslexia-mt5/plots_four_models_transfer.png"       "$DEST/"
cp "$SRC_ROOT/dyslexia-mt5/plots_layer_emergence_all_models.png" "$DEST/"
cp "$SRC_ROOT/dyslexia-mt5/plots_mt5_unit_overlap.png"           "$DEST/"
cp "$SRC_ROOT/dyslexia-mt5/plots_thesis_summary.png"             "$DEST/"
cp "$SRC_ROOT/dyslexia-mt5/plots_transfer_realword_matched.png"  "$DEST/"

echo "Copied $(ls "$DEST" | wc -l) image files into $DEST/"
