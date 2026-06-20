# Project Instructions

## Project

- Site: `https://7sinsorigin.com`
- Type: bilingual static SEO site for The Seven Deadly Sins: Origin
- English routes live at `/`; Chinese mirrors live under `/zh/`
- Core content must remain visible in the original HTML without JavaScript

## Goals And Boundaries

- Publish useful, official-source-first game news, guides, banner advice, and troubleshooting content.
- Prefer clear long-tail search intent and evergreen topic coverage over speculative or short-lived content.
- Do not present leaks, predictions, or inferred banner details as confirmed facts.
- Preserve historical archive pages; update current routing pages instead of rewriting old records.

## Working Rules

1. Read `agents.md`, `memory.md`, `README.md`, and `PROJECT-MEMORY.md` before project work.
2. Inspect `git status --short` first and never overwrite unrelated user changes.
3. For daily content checks, follow the `seven-sins-origin-daily` skill and verify time-sensitive facts against official sources.
4. Add English and Chinese mirrors together whenever practical. Keep canonical and `hreflang` pairs aligned.
5. Update homepage routes, relevant hubs, internal links, and `sitemap.xml` when publishing important pages.
6. Keep each page answer-first, focused on one search intent, and materially different from nearby pages.
7. Maintain unique title, meta description, H1, canonical, Open Graph, Twitter, structured data, and image alt text.
8. Use `nofollow` or `sponsored` for untrusted or paid external links and `noopener` for new-window links.
9. Record reusable decisions, failures, and validation lessons in `memory.md` after meaningful work.

## Release Checks

Run at minimum:

```bash
git diff --check
xmllint --noout sitemap.xml
find . -name index.html -type f | wc -l
git status --short
```

Also verify new internal-link targets exist, EN/ZH pairs are present, sitemap URLs are unique, and edited pages contain the required SEO metadata.
