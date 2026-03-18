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

## Official image assets (optional local download)

Homepage uses PlayStation Blog public image URLs as fallback.
You can download them to local files with:

```bash
cd /Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin
./scripts/download_playstation_images.sh
```

Downloaded files are saved in `assets/img/official/`.

## Local preview

You can preview with any static server, for example:

```bash
cd /Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Next recommended tasks

- connect domain DNS and hosting
- submit sitemap to Google Search Console and Bing Webmaster Tools
- add structured data (FAQ/Article/Breadcrumb)
- publish recurring update posts to build long-tail keyword traffic
