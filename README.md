# 7sinsorigin.com

SEO-oriented static site scaffold for **The Seven Deadly Sins: Origin** game information.

## Language structure

- English (default): `/`
- Chinese: `/zh/`

This structure is intentional for SEO:
- the root URL targets global/English search traffic
- Chinese content is grouped under `/zh/`
- pages include canonical and hreflang annotations

## Main keyword focus

- seven deadly sins origin
- the seven deadly sins origin
- the seven deadly sins: origin
- 7ds origin

## Current pages

The site has expanded far beyond the original scaffold.
Current `index.html` count: `288`

English:
- `/`
- `/seven-deadly-sins-origin/`
- `/release-date/`
- `/pre-register/`
- `/characters/`
- `/tier-list/`
- `/beginner-guide/`
- `/news/`
- `/news/2026/03/march-playlist-update/`
- `/about/`
- `/contact/`

Chinese:
- `/zh/`
- `/zh/seven-deadly-sins-origin/`
- `/zh/release-date/`
- `/zh/pre-register/`
- `/zh/characters/`
- `/zh/tier-list/`
- `/zh/beginner-guide/`
- `/zh/news/`
- `/zh/news/2026/03/march-playlist-update/`
- `/zh/about/`
- `/zh/contact/`

## External links included

- Download: `https://7origin.netmarble.com/game`
- Pre-register: `https://7origin.netmarble.com/preorder`
- Twitter/X: `https://x.com/netmarbleglobal`
- Facebook: `https://www.facebook.com/netmarbleglobal`
- Reddit: `https://www.reddit.com/r/SDSGrandCross/`

## SEO and crawl files

- `sitemap.xml`
- `robots.txt`
- `SEO-OPS.md` (weekly SEO operation checklist)

## Official image assets (optional local download)

Homepage uses PlayStation Blog public image URLs as fallback.
You can download them to local files with:

```bash
cd /Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin
./scripts/download_playstation_images.sh
```

Downloaded files are saved in `assets/img/official/`.


 open `https://7sinsorigin.com`.

## SEO baseline (implemented)

- all HTML pages now include:
  - `robots` with `max-image-preview:large`
  - `theme-color`
  - Open Graph tags (`og:*`)
  - Twitter card tags
  - JSON-LD (`WebPage` fallback on pages without existing schema)
- sitemap `lastmod` values refreshed to `2026-03-23`

## Recommended next actions

- submit sitemap in Google Search Console and Bing Webmaster Tools
- keep weekly publishing cadence (see `SEO-OPS.md`)


Post-launch expansion added on 2026-05-08: current tier list, current banner decision, diamond farming, beginner team, F2P team, post-launch mistakes, and three troubleshooting pages with zh mirrors.

May 2026 refresh added on 2026-05-24: Version 1.3 Part 1 and Part 2 news coverage, deeper pull-intent pages, and missing EN/ZH character language-entry fixes.

June 20 refresh added Developer Notes #14 / Version 1.6, the 100-day giveaway and livestream, and June 19 server-patch coverage with Chinese mirrors.

June 23 refresh added Version 1.6 maintenance-schedule coverage with Chinese mirror, updated current/upcoming banner routing, and refreshed homepage/news entries.

June 24 refresh added Version 1.6 update-details coverage, Elizabeth character pages, Elizabeth banner decision pages, corrected the maintenance change to June 25, and refreshed current/upcoming banner routing with Chinese mirrors.

June 25 refresh marked Version 1.6 maintenance as completed, moved Elizabeth from upcoming to current banner routing, and refreshed best-banner/current-banner decision pages without changing the page count.

June 26 refresh added Developer Notes #15, Version 1.6 Known Issues, Missing Potential Points compensation, and 100-Day Anniversary Survey coverage with Chinese mirrors; updated homepage, news hubs, bugs/errors hubs, sitemap, and raised the page count to 272.

June 30 refresh added Midsummer Day Surprise Giveaway coverage with Chinese mirror, refreshed homepage/news/event-schedule discovery paths, and raised the page count to 274.

July 1 refresh added Exciting Cube Unboxing and Leaderboard Regular Season 1 issue coverage with Chinese mirrors, updated the June 30 Version 1.6 Known Issues content, refreshed homepage/news/event-schedule/bugs-errors discovery paths, and raised the page count to 278.

July 2 refresh added Magic Pop and July 2 temporary-maintenance completed coverage with Chinese mirrors, updated Version 1.6 Known Issues and Version 1.6 Update Details to the July 2 official state, refreshed homepage/news/event-schedule/bugs-errors discovery paths, and raised the page count to 282.

July 6 refresh updated Version 1.6 Known Issues to the July 6 official state with Magic Pop party-entry, pet capture input-lock, and PS5 leaderboard reward mailbox entries; refreshed homepage/news/bugs-errors/leaderboard discovery paths and kept the page count at 282.

July 8 refresh updated Magic Pop - The Day of Mischief Begins to the July 8 official state with the mission-progress note that leaving before the game ends does not count knock-out or defeat objectives; refreshed homepage/news/event-schedule discovery paths and kept the page count at 282.

July 10 refresh added the official Version 1.7 Special Livestream Schedule coverage from the July 9 Netmarble notice, updated Version 1.6 Known Issues to the July 9 official state with Magic Pop room-state and Raid Pledge reward issues, refreshed homepage/news discovery paths, and raised the page count to 284.

July 13 refresh added official Developer Notes #16 and Twitch Drops Event coverage with Chinese mirrors, updated the Twitch Drops guide and event schedule, refreshed homepage/news discovery paths and sitemap, and raised the page count to 288.
