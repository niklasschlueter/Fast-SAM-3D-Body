#!/usr/bin/env bash

echo "[Setup Chumpy] Starting..."

SITE_PACKAGES=$(python -c "import site; print(site.getsitepackages()[0])")

if [ ! -d "$SITE_PACKAGES/chumpy" ]; then
    echo "[Setup Chumpy] Installing chumpy from GitHub..."
    python -m pip install git+https://github.com/mattloper/chumpy.git
else
    echo "[Setup Chumpy] Already installed, skipping."
fi

echo "[Setup Chumpy] Done."
