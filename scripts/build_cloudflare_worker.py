#!/usr/bin/env python3
"""Build the public-only static asset bundle used by Cloudflare Workers."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_HOST = "7sinsorigin.com"
WORKER_NAME = "seven-sins-origin"
EXCLUDED_PARTS = {
    ".git",
    ".github",
    ".vercel",
    "__pycache__",
    "dist",
    "reports",
    "scripts",
}
ROOT_PUBLIC_FILES = {
    "index.html",
    "404.html",
    "ads.txt",
    "robots.txt",
    "sitemap.xml",
    "favicon.ico",
    "favicon.svg",
    "site.webmanifest",
}
VERIFICATION_FILE = re.compile(r"^[0-9a-f]{32}\.txt$")


def should_copy(relative: Path) -> bool:
    if any(part in EXCLUDED_PARTS or part.startswith(".") for part in relative.parts):
        return False
    if len(relative.parts) == 1:
        return relative.name in ROOT_PUBLIC_FILES or bool(VERIFICATION_FILE.fullmatch(relative.name))
    if relative.parts[0] == "assets":
        return True
    return relative.suffix.lower() == ".html"


def copy_public_files(output: Path) -> int:
    count = 0
    for source in ROOT.rglob("*"):
        if not source.is_file():
            continue
        relative = source.relative_to(ROOT)
        if not should_copy(relative):
            continue
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        count += 1
    return count


def write_redirects(output: Path) -> None:
    rules: list[str] = []
    config_path = ROOT / "vercel.json"
    if config_path.exists():
        config = json.loads(config_path.read_text(encoding="utf-8"))
        for rule in config.get("redirects", []):
            status = 308 if rule.get("permanent") else 302
            rules.append(f"{rule['source']} {rule['destination']} {status}")
    if rules:
        (output / "_redirects").write_text("\n".join(rules) + "\n", encoding="utf-8")


def write_headers(output: Path) -> None:
    content = f"""/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

https://:worker.bingkun-zhao.workers.dev/*
  X-Robots-Tag: noindex
"""
    (output / "_headers").write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    output = args.output.resolve()
    if output == ROOT or ROOT in output.parents and output.name in {"assets", "scripts"}:
        raise SystemExit(f"Refusing unsafe output directory: {output}")
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    count = copy_public_files(output)
    write_redirects(output)
    write_headers(output)
    required = [output / "index.html", output / "robots.txt", output / "sitemap.xml"]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("Missing required public files: " + ", ".join(missing))
    print(f"Built {count} public files for https://{CANONICAL_HOST} in {output}")


if __name__ == "__main__":
    main()
