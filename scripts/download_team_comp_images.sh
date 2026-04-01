#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="$ROOT/assets/img/team-comps"
MAP_FILE="$ROOT/scripts/team_comp_image_sources.txt"
EN_FILE="$ROOT/beginner-guide/best-team-comps/index.html"
ZH_FILE="$ROOT/zh/beginner-guide/best-team-comps/index.html"

FORCE=0
DRY_RUN=0

usage() {
  cat <<'USAGE'
Usage:
  ./scripts/download_team_comp_images.sh [--force] [--dry-run]

Options:
  --force    Redownload even if local PNG already exists.
  --dry-run  Print actions only, do not download or edit files.
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --force) FORCE=1 ;;
    --dry-run) DRY_RUN=1 ;;
    -h|--help) usage; exit 0 ;;
    *)
      echo "Unknown option: $1"
      usage
      exit 1
      ;;
  esac
  shift
done

if [[ ! -f "$MAP_FILE" ]]; then
  echo "Missing mapping file: $MAP_FILE"
  exit 1
fi

mkdir -p "$OUT_DIR"

downloaded=0
skipped=0
failed=0
switched_refs=0
processed=0

while IFS='|' read -r key url label; do
  [[ -z "${key:-}" ]] && continue
  [[ "${key:0:1}" == "#" ]] && continue
  [[ -z "${url:-}" ]] && continue

  processed=$((processed + 1))
  png_path="$OUT_DIR/$key.png"
  svg_ref="/assets/img/team-comps/$key.svg"
  png_ref="/assets/img/team-comps/$key.png"

  need_download=1
  if [[ -s "$png_path" && "$FORCE" -ne 1 ]]; then
    need_download=0
  fi

  if [[ "$need_download" -eq 1 ]]; then
    if [[ "$DRY_RUN" -eq 1 ]]; then
      echo "[dry-run] download $key -> $png_path"
      downloaded=$((downloaded + 1))
    else
      echo "Downloading: $label"
      if curl -fL --retry 3 --retry-delay 1 -A "Mozilla/5.0" "$url" -o "$png_path"; then
        downloaded=$((downloaded + 1))
      else
        echo "Failed: $url"
        failed=$((failed + 1))
      fi
    fi
  else
    echo "Skip existing: $key.png"
    skipped=$((skipped + 1))
  fi

  # If PNG exists, replace SVG refs in both team pages.
  if [[ "$DRY_RUN" -eq 1 ]]; then
    if grep -q "$svg_ref" "$EN_FILE" "$ZH_FILE"; then
      echo "[dry-run] replace refs: $svg_ref -> $png_ref"
    fi
  else
    if [[ -s "$png_path" ]]; then
      before_count="$( (grep -o "$svg_ref" "$EN_FILE" "$ZH_FILE" 2>/dev/null || true) | wc -l | tr -d ' ' )"
      if [[ "${before_count:-0}" -gt 0 ]]; then
        escaped_svg="${svg_ref//\//\\/}"
        escaped_png="${png_ref//\//\\/}"
        sed -i '' "s/${escaped_svg}/${escaped_png}/g" "$EN_FILE" "$ZH_FILE"
        switched_refs=$((switched_refs + before_count))
      fi
    fi
  fi
done < "$MAP_FILE"

echo "Processed roles: $processed"
echo "Downloaded: $downloaded | Existing reused: $skipped | Failed: $failed"
if [[ "$DRY_RUN" -eq 0 ]]; then
  echo "Reference replacements (.svg -> .png): $switched_refs"
  echo "Done. Team images directory: $OUT_DIR"
fi
