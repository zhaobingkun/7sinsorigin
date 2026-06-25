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
Current `index.html` count: `264`

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
