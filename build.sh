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
cp -r "$DOCS_SRC/integrations" "$SKILL_SRC/references/docs/"
cp "$DOCS_SRC/tutorials/build-form.md" "$SKILL_SRC/references/docs/"

# Release-note posts: how the system has changed over time. Merged into a
# single file — Claude Code rejects skill zips with more than 200 files.
python3 - "$REPO_ROOT/docs/_posts" "$SKILL_SRC/references/docs/changelog.md" <<'EOF'
import pathlib, re, sys

posts_dir, out_path = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
posts = []
for p in sorted(posts_dir.rglob("*.md")):
    m = re.match(r"(\d{4}-\d{2}-\d{2})-", p.name)
    if not m:
        continue
    text = p.read_text(encoding="utf-8")
    title, post_type, body = p.stem[11:], "", text
    fm = re.match(r"---\r?\n(.*?)\r?\n---\r?\n?(.*)", text, re.DOTALL)
    if fm:
        body = fm.group(2)
        for line in fm.group(1).splitlines():
            k, _, v = line.partition(":")
            if k.strip() == "title":
                title = v.strip().strip("\"'")
            elif k.strip() == "type":
                post_type = v.strip().strip("\"'")
    suffix = f" ({post_type})" if post_type else ""
    posts.append((m.group(1), f"## {m.group(1)} — {title}{suffix}\n\n{body.strip()}\n"))

posts.sort(key=lambda x: x[0], reverse=True)
header = ("# FormsByAir changelog\n\nDated release notes, newest first, "
          "merged from the documentation site's posts.\n\n")
out_path.write_text(header + "\n".join(entry for _, entry in posts), encoding="utf-8")
print(f"changelog.md: merged {len(posts)} posts")
EOF

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
if command -v zip > /dev/null; then
  (cd "$(dirname "$SKILL_SRC")" && zip -qr "$OUT" "$(basename "$SKILL_SRC")")
else
  # zip is missing on e.g. Git Bash for Windows; python3 is already required above
  (cd "$(dirname "$SKILL_SRC")" && python3 -m zipfile -c "$OUT" "$(basename "$SKILL_SRC")")
fi

echo "Built $OUT"
python3 -m zipfile -l "$OUT" | tail -1
