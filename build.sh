#!/usr/bin/env bash
# Build the FormsByAir form-authoring Claude skill.
#
# Usage:
#   ./build.sh                 # version defaults to today's date (e.g. 2026.7.10)
#   ./build.sh 2026.8.2        # explicit version
#
# Expected layout (adjust SKILL_SRC / DOCS_SRC if yours differs):
#   <repo root>/
#   ├── docs/_docs/            # the Documentation repo's markdown sources
#   └── skill/formsbyair-form-authoring/   # this skill's source
#
# Output: dist/formsbyair-form-authoring-<version>.zip
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
SKILL_SRC="$REPO_ROOT/skill/formsbyair-form-authoring"
DOCS_SRC="$REPO_ROOT/docs/_docs"
DIST="$REPO_ROOT/dist"

VERSION="${1:-$(date +%Y).$(date +%-m).$(date +%-d)}"

[ -f "$SKILL_SRC/SKILL.md" ] || { echo "ERROR: no SKILL.md at $SKILL_SRC"; exit 1; }
[ -d "$DOCS_SRC" ] || { echo "ERROR: no docs at $DOCS_SRC"; exit 1; }

echo "Building formsbyair-form-authoring $VERSION"

# 1. Refresh the bundled docs snapshot (authoring-relevant sections only)
rm -rf "$SKILL_SRC/references/docs"
mkdir -p "$SKILL_SRC/references/docs"
cp -r "$DOCS_SRC/questions" "$SKILL_SRC/references/docs/"
cp -r "$DOCS_SRC/tags"      "$SKILL_SRC/references/docs/"
cp -r "$DOCS_SRC/forms"     "$SKILL_SRC/references/docs/"
cp "$DOCS_SRC/tutorials/build-form.md" "$SKILL_SRC/references/docs/"

# 2. Stamp the version (frontmatter line and body footer)
sed -i.bak -E "s/^version: .*/version: $VERSION/" "$SKILL_SRC/SKILL.md"
sed -i.bak -E "s/^Skill version: [^ ]*/Skill version: $VERSION/" "$SKILL_SRC/SKILL.md"
rm -f "$SKILL_SRC/SKILL.md.bak"

# 3. Sanity checks: validator runs clean on the bundled example
python3 "$SKILL_SRC/scripts/validate.py" "$SKILL_SRC"/assets/*.xsd > /dev/null \
  || { echo "ERROR: validate.py failed on bundled example"; exit 1; }

# 4. Package
mkdir -p "$DIST"
OUT="$DIST/formsbyair-form-authoring-$VERSION.zip"
rm -f "$OUT"
(cd "$(dirname "$SKILL_SRC")" && zip -qr "$OUT" "$(basename "$SKILL_SRC")")

echo "Built $OUT"
unzip -l "$OUT" | tail -1
