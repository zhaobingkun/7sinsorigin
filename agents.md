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
10. Read `content-policy.json` before publishing: merged, withdrawn and archive routes must not return to the sitemap or current-guide navigation without substantive evidence and explicit editorial review. Do not use word counts as the publication decision.
11. The three `generate_*` scripts are retired historical generators. Do not bypass their stop guard or regenerate over reviewed pages. `content_policy.py --apply` is only mechanical policy/navigation enforcement; it is not a content writer.
12. Advertising runtime is disabled by policy. Keep ownership metadata and `ads.txt`, but do not add ad loaders or treat the Analytics-only privacy panel as a certified advertising CMP. Future advertising requires separate consent configuration/review.
13. For a short official notice, update an existing useful guide when it answers the same intent; do not automatically create another thin news page. Distinguish confirmed official facts, rule-derived calculations, and untested gameplay advice.

## Release Checks

Run at minimum:

```bash
sh scripts/release_check.sh
git diff --check
xmllint --noout sitemap.xml
find . -name index.html -type f | wc -l
git status --short
```

Also verify new internal-link targets exist, EN/ZH pairs are present, sitemap URLs are unique, and edited pages contain the required SEO metadata.

The release script is read-only and validates every page, publication policy and redirect config. The GitHub workflow runs the same policy/HTML checks, but does not itself gate an independent hosting deployment. After pushing to `origin/main`, verify live 200 responses, permanent redirects and updated HTML markers. Never equate local validation or noindex with AdSense approval, and do not submit a re-review without the user's request.
