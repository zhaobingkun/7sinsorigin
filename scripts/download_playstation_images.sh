#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$ROOT_DIR/assets/img/official"
mkdir -p "$OUT_DIR"

urls=(
  "https://blog.playstation.com/tachyon/2006/12/5c9e27e4c17f094f719fd93a54821816f790239f.jpg?crop_strategy=smart&resize=1088%2C612"
  "https://blog.playstation.com/tachyon/2006/12/7f0de083b72fcc5bd95a132f4a42b56037a4ea21.jpg?fit=1024%2C1024"
  "https://blog.playstation.com/tachyon/2006/12/8ede614024edbaed8bac938915a2489b4b64c828.jpg?fit=1024%2C1024"
  "https://blog.playstation.com/tachyon/2006/12/89e7ab808e20a16f62c8f1dfe15aa34081994648.jpg?fit=1024%2C1024"
)

names=(
  "ps-origin-keyart.jpg"
  "ps-origin-combat-1.jpg"
  "ps-origin-combat-2.jpg"
  "ps-origin-characters.jpg"
)

for i in "${!urls[@]}"; do
  echo "Downloading ${names[$i]}"
  curl -L --fail --retry 3 --retry-delay 1 -o "$OUT_DIR/${names[$i]}" "${urls[$i]}"
done

cat > "$OUT_DIR/SOURCE.txt" <<'SRC'
Image source: PlayStation Blog (public media URLs)
Page: https://blog.playstation.com/2025/12/11/the-seven-deadly-sins-origin-unveils-cooperative-raid-battles/

Files:
- ps-origin-keyart.jpg
- ps-origin-combat-1.jpg
- ps-origin-combat-2.jpg
- ps-origin-characters.jpg
SRC

echo "Done. Images saved to: $OUT_DIR"
