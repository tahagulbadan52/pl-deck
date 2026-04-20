#!/usr/bin/env bash
# pl-deck skill installer
# Usage: curl -fsSL https://raw.githubusercontent.com/YOUR-USERNAME/pl-deck/main/install.sh | bash
set -e

SKILL_DIR="$HOME/.claude/skills/pl-deck"
REPO_URL="${PL_DECK_REPO:-https://github.com/YOUR-USERNAME/pl-deck.git}"

echo "→ Installing pl-deck skill to $SKILL_DIR"

# Make sure ~/.claude/skills exists
mkdir -p "$HOME/.claude/skills"

if [ -d "$SKILL_DIR/.git" ]; then
  echo "→ Skill already installed — updating instead"
  cd "$SKILL_DIR"
  git pull --ff-only
else
  if [ -d "$SKILL_DIR" ]; then
    echo "✗ $SKILL_DIR exists but is not a git repo."
    echo "  Back it up and remove it, then re-run this installer."
    exit 1
  fi
  git clone --depth 1 "$REPO_URL" "$SKILL_DIR"
fi

echo ""
echo "✓ pl-deck skill installed."
echo ""
echo "Next steps:"
echo "  1. Open Claude Code in any folder"
echo "  2. Run:  /pl-deck"
echo ""
echo "For PDF export, Node.js 18+ is required (Puppeteer auto-installs on first export)."
