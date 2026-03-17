#!/usr/bin/env bash

echo "[Setup Detectron2] Starting..."

SITE_PACKAGES=$(python -c "import site; print(site.getsitepackages()[0])")

if [ ! -d "$SITE_PACKAGES/detectron2" ]; then
    echo "[Setup Detectron2] Installing detectron2 (this may take a few minutes)..."
    CUDA_HOME=$CONDA_PREFIX python -m pip install --no-build-isolation --no-deps \
        'git+https://github.com/facebookresearch/detectron2.git@a1ce2f9'
else
    echo "[Setup Detectron2] Already installed, skipping."
fi

echo "[Setup Detectron2] Done."
