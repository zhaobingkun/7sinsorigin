# Project Experience

## Stable Architecture

- The site is a static bilingual topic-authority site with English at `/` and Chinese at `/zh/`.
- Important current pages should be reachable from the homepage or a hub within a few clicks.
- Archive pages remain historically accurate; current pages route users to the newest version-specific content.
- `README.md` and `PROJECT-MEMORY.md` track the current `index.html` page count.

## Official Source Workflow

- Netmarble's visible news page can return an SSR shell without showing the newest posts.
- The official forum list endpoint is:
  `https://7origin.netmarble.com/api/data-list?forumId=7dso_en&start=0&rows=20&parentMenuSeq=1`
- Individual official articles can be fetched with:
  `https://7origin.netmarble.com/api/data-article?forumId=7dso_en&id=<id>&menuSeq=<menu>`
- Confirm dates, event windows, rewards, character names, and update status from article data before publishing.
- Do not infer banner format, release date, rates, or pity from a livestream character preview.

## June 20, 2026 Refresh

- Added EN/ZH coverage for Developer Notes #14 and Version 1.6.
- Added EN/ZH coverage for the 100-day giveaway and June 23 livestream.
- Added EN/ZH coverage for the June 19 server patch.
- Updated homepage, news hubs, upcoming banners, event schedule, Escanor pages, sitemap, README, and project memory.
- Version 1.6 confirms an Escanor adjustment, but ranking changes should wait for the live implementation and testing.
- Current page count after this refresh: `256` HTML index pages.

## Validation Lessons

- Run `git diff --check` and `xmllint --noout sitemap.xml` before release.
- Check sitemap URL uniqueness and all local links after adding bilingual pages.
- Verify new pages include official source links and existing local assets.
- A local HTTP 200 response confirms resources are available, but visual browser QA is still useful for layout-sensitive changes.
