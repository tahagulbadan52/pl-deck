#!/usr/bin/env bash
# Assemble all blocks into gallery.html and screenshot each to scripts/_shots/.
# Visual QA for the block library. Run from the skill root.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"
python3 scripts/build_gallery.py
[ -d /tmp/node_modules/puppeteer ] || (cd /tmp && npm install puppeteer --silent)
node scripts/shoot.js
echo "Open gallery.html or scripts/_shots/ to review."
