#!/usr/bin/env bash
# Watch the upstream Platinumlist design system for brand-token changes.
# Mirrors pl-design-system/scripts/check-updates.sh: compares the latest commit
# SHA of the design-system repo against a stored value. When it differs, the
# brand palette/type may have changed -> review and update tokens.css.
#
# Usage: bash scripts/check-tokens.sh
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STORE="$SCRIPT_DIR/../tokens.version"
REPO="rustambiazarti/pl_designsystem"   # upstream brand source of truth

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI not found — skipping token check."; exit 0
fi

LATEST="$(gh api "repos/$REPO/commits/main" --jq '.sha' 2>/dev/null || echo "")"
[ -z "$LATEST" ] && { echo "Could not reach $REPO — skipping."; exit 0; }
STORED="$(cat "$STORE" 2>/dev/null || echo "none")"

if [ "$LATEST" = "$STORED" ]; then
  echo "UP_TO_DATE  tokens.css matches design system @ ${LATEST:0:8}"
else
  echo "UPDATE_AVAILABLE  design system moved: ${STORED:0:8} -> ${LATEST:0:8}"
  echo "Review brand token changes upstream, update tokens.css, then run:"
  echo "  echo $LATEST > tokens.version"
  exit 1
fi
