#!/usr/bin/env bash

echo "[Setup Checkpoints] Starting..."

CKPT_DIR="$PIXI_PROJECT_ROOT/checkpoints/sam-3d-body-dinov3"

if [ ! -f "$CKPT_DIR/model.ckpt" ]; then
    echo "[Setup Checkpoints] Downloading sam-3d-body-dinov3 from HuggingFace..."
    python -c "
from huggingface_hub import snapshot_download
snapshot_download(repo_id='facebook/sam-3d-body-dinov3', local_dir='$CKPT_DIR')
"
else
    echo "[Setup Checkpoints] Checkpoints already present, skipping."
fi

echo "[Setup Checkpoints] Done."
