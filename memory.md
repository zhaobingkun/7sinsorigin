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

## Daily Check Log

- 2026-06-21: attempted to check the official Netmarble news API, official pages, search, and the in-app browser. The official domain could not be reached from the available network paths, so no current-content claim was treated as verified and no site content was changed.
- 2026-06-22: repeated the official API, official-site search, direct network, public-DNS, YouTube, and X checks, including a later retry. External DNS resolution remained unavailable, so today's official update status could not be verified and no site content was changed.
- 2026-06-23: official Netmarble API returned a new `Version 1.6 Maintenance Schedule` notice. Added EN/ZH news pages, updated homepage/news hubs, refreshed current/upcoming banner wording for the original June 24 maintenance boundary, updated sitemap, and raised the page count to `258`.
- 2026-06-24: official Netmarble API returned `Version 1.6 Update Details`, Elizabeth details, and the changed maintenance notice. Added EN/ZH Version 1.6 update-details pages, Elizabeth character pages, and Elizabeth banner decision pages; corrected current/upcoming banner wording to show Merlin/Daisy as ending before the June 25 maintenance and Elizabeth as after-maintenance; raised the page count to `264`.
- 2026-06-25: official Netmarble API showed `Version 1.6 Update Details` updated at 08:13 UTC and `Version 1.6 Maintenance Schedule [Completed]`. Refreshed EN/ZH current-banner, upcoming-banner, best-banner, Elizabeth, and maintenance/update pages so Elizabeth/Radiant Summer Memories is treated as the current banner after maintenance; page count remains `264`.
- 2026-06-26: official Netmarble API returned new `Developer Notes #15`, new/updated `Version 1.6 Known Issues`, `Notice Regarding Missing Potential Points`, and `100-Day Anniversary Survey`. Added EN/ZH pages for all four, updated homepage/news hubs and bugs-errors hubs, updated sitemap, and raised the page count to `272`. The Developer Notes page should be treated as roadmap/QoL coverage, not a banner confirmation.
