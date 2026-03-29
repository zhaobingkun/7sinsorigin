#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EN_FILE="$ROOT/beginner-guide/equipment/index.html"
ZH_FILE="$ROOT/zh/beginner-guide/equipment/index.html"
OUT_DIR="$ROOT/assets/img/equipment"
mkdir -p "$OUT_DIR"

URLS="$(grep -Eho 'https://img\.game8\.co/[^"]+\.png/show' "$EN_FILE" "$ZH_FILE" | sort -u || true)"
if [[ -z "${URLS}" ]]; then
  echo "No game8 equipment image URLs found."
  exit 1
fi

failed=0
skipped=0
downloaded=0

while IFS= read -r url; do
  [[ -z "$url" ]] && continue
  trimmed="${url%/show}"
  id_part="$(echo "$trimmed" | awk -F'/' '{print $(NF-1)}')"
  file_part="$(basename "$trimmed")"
  local_name="equipment_${id_part}_${file_part}"
  target="$OUT_DIR/$local_name"

  if [[ ! -s "$target" ]]; then
    echo "Downloading: $url"
    if curl -fL --retry 3 --retry-delay 1 -A "Mozilla/5.0" "$url" -o "$target"; then
      downloaded=$((downloaded + 1))
    else
      echo "Failed: $url"
      failed=$((failed + 1))
      rm -f "$target"
      continue
    fi
  else
    echo "Skip existing: $local_name"
    skipped=$((skipped + 1))
  fi

  rel_path="/assets/img/equipment/$local_name"
  escaped_url="${url//\//\\/}"
  escaped_rel="${rel_path//\//\\/}"
  sed -i '' "s/${escaped_url}/${escaped_rel}/g" "$EN_FILE" "$ZH_FILE"
done <<< "$URLS"

echo "Done. Local equipment images saved under: $OUT_DIR"
echo "Downloaded: $downloaded | Existing reused: $skipped | Failed: $failed"
