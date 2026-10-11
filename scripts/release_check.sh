#!/bin/sh
# Run before staging, committing or pushing. Does not modify files or publish.
set -eu
cd "$(dirname "$0")/.."
git diff --check
xmllint --noout sitemap.xml
python3 scripts/content_policy.py
python3 scripts/validate_site.py
find . -name index.html -type f | wc -l
git status --short
