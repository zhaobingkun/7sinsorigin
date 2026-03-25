#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EN_FILE="$ROOT/beginner-guide/pets/index.html"
ZH_FILE="$ROOT/zh/beginner-guide/pets/index.html"
OUT_DIR="$ROOT/assets/img/pets"
mkdir -p "$OUT_DIR"

URLS="$(grep -Eho 'https://img\.game8\.co/[^"]+\.png/show' "$EN_FILE" "$ZH_FILE" | sort -u || true)"
if [[ -z "${URLS}" ]]; then
  echo "No game8 pet image URLs found."
  exit 1
fi

while IFS= read -r url; do
  [[ -z "$url" ]] && continue
  trimmed="${url%/show}"
  id_part="$(echo "$trimmed" | awk -F'/' '{print $(NF-1)}')"
  file_part="$(basename "$trimmed")"
  local_name="pet_${id_part}_${file_part}"
  target="$OUT_DIR/$local_name"

  if [[ ! -s "$target" ]]; then
    echo "Downloading: $url"
    curl -fL --retry 3 --retry-delay 1 -A "Mozilla/5.0" "$url" -o "$target"
  else
    echo "Skip existing: $local_name"
  fi

  rel_path="/assets/img/pets/$local_name"
  escaped_url="${url//\//\\/}"
  escaped_rel="${rel_path//\//\\/}"
  sed -i '' "s/${escaped_url}/${escaped_rel}/g" "$EN_FILE" "$ZH_FILE"
done <<< "$URLS"

echo "Done. Local pet images saved under: $OUT_DIR"
