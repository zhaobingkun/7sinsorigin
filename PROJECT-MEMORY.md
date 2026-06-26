# Project Memory

## Project Identity
- Path: `/Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin`
- Live domain: `https://7sinsorigin.com`
- Repo state: this directory is a git repository
- Site type: bilingual static SEO site for **The Seven Deadly Sins: Origin**

## Language Structure
- English default site: `/`
- Chinese mirror site: `/zh/`
- Canonical and `hreflang` are part of the core site structure
- Preferred multilingual pattern:
  - English on root
  - Chinese in subdirectory

## Current Scale
- Current `index.html` count: `272`
- This is no longer a small scaffold; it is a fairly large bilingual topic site

## Core Keyword Focus
- `seven deadly sins origin`
- `the seven deadly sins origin`
- `the seven deadly sins: origin`
- `7ds origin`

## Main Site Sections
- Core hubs:
  - `/`
  - `/seven-deadly-sins-origin/`
  - `/release-date/`
  - `/pre-register/`
  - `/characters/`
  - `/tier-list/`
  - `/beginner-guide/`
  - `/systems/`
  - `/banners/`
  - `/news/`
- Chinese mirrors exist for the main hubs under `/zh/`

## Important Content Lines Already Expanded
- Utility / event / progression pages:
  - `/codes/`
  - `/twitch-drops/`
  - `/all-achievements/`
  - `/events-schedule/`
  - `/daily-checklist/`
  - `/weekly-checklist/`
  - `/currency-guide/`
  - `/how-to-get-stronger/`
  - `/how-to-link-accounts/`
  - `/server-reset-times/`
  - `/upcoming-characters/`
- Beginner guide subtree includes pages such as:
  - `cooking`
  - `fishing`
  - `leveling-fast`
  - `material-farming`
  - `weapon-upgrade`
  - `story-progression`
  - `free-rewards`
  - `best-team-comps`
  - `equipment`
  - `armor`
  - `pets`
- Systems subtree includes pages such as:
  - `elements`
  - `knighthood`
  - `open-world-exploration`
  - `co-op-and-party-play`
  - `mounts-and-fast-travel`
  - `day-night-and-weather`
  - `progression-and-upgrades`
  - `combat`
  - `controller-support`
  - `gacha-pity`
- Banner / pull intent line:
  - `/banners/`
  - `/banners/current/`
  - `/banners/upcoming/`
  - `/best-banner-to-pull/`
- Troubleshooting / support line:
  - `/bugs-errors/`
  - `/login-failed/`
  - `/install-failed/`
  - `/update-failed/`
  - `/is-there-controller-support/`
  - `/best-settings/`
  - `/reroll-or-not/`

## Character Coverage
- Character hub:
  - `/characters/`
- Existing specific character pages include:
  - `meliodas`
  - `elaine`
  - `king`
  - `diane`
  - `tristan`
  - `tioreh`
  - `clotho`
  - `elizabeth`
- Chinese mirrors exist for the character line as well

## Technical / SEO Baseline
- Important files:
  - `sitemap.xml`
  - `robots.txt`
  - `SEO-OPS.md`
  - `assets/css/site.css`
  - `assets/js/site.js`
- Baseline already in place:
  - `canonical`
  - `hreflang`
  - Open Graph tags
  - Twitter card tags
  - JSON-LD on pages
  - bilingual mirrored structure
- This project is intentionally SEO-first and should stay static-rendered / HTML-visible

## Scripts And Asset Helpers
- Page / content generation:
  - `scripts/generate_growth_and_system_pages.py`
- Image download helpers:
  - `scripts/download_playstation_images.sh`
  - `scripts/download_equipment_images.sh`
  - `scripts/download_armor_images.sh`
  - `scripts/download_pet_images.sh`
  - `scripts/download_team_comp_images.sh`
  - `scripts/team_comp_image_sources.txt`

## Known Direction From Previous Work
- English homepage and Chinese homepage were both strengthened around clearer main-intent targeting
- We previously expanded:
  - first batch of 10 pages on the English side
  - matching `/zh/` mirrors
  - another English batch around exploration / progression / co-op
  - matching `/zh/` mirrors
- We also strengthened hub pages and some title/meta/OG wording for better main-keyword alignment

## Content Strategy Notes
- Treat this as a topic authority site, not a one-shot keyword landing page
- Priority page types:
  - release-date / pre-register / official-news intent
  - evergreen guide hubs
  - character pages
  - systems pages
  - banner / pull-decision pages
  - troubleshooting pages
- For future GEO / AI-answer optimization:
  - answer-first intros
  - clear confirmed vs speculative wording
  - stronger internal linking from news to evergreen pages

## Maintenance Notes
- When returning to this project, check these first:
  1. `README.md`
  2. `SEO-OPS.md`
  3. `sitemap.xml`
  4. homepage `index.html`
  5. Chinese homepage `zh/index.html`
  6. `systems/`, `beginner-guide/`, `banners/`, and `news/` hubs
- If new English pages are added, mirror them under `/zh/` whenever practical
- Keep `hreflang` pairs aligned
- Keep sitemap `lastmod` fresh when adding or thickening key pages

## Suggested Next Focus
- Continue thickening highest-value evergreen pages instead of only adding thin directories
- Prioritize:
  - banner / pull pages
  - character pages
  - troubleshooting pages
  - systems pages tied to real query intent
- Preserve the current bilingual hub-and-child architecture; it is one of the strongest parts of this project


Post-launch expansion added on 2026-05-08: current tier list, current banner decision, diamond farming, beginner team, F2P team, post-launch mistakes, and three troubleshooting pages with zh mirrors.

May refresh added on 2026-05-24: two Version 1.3 news pages with zh mirrors, deeper pull-intent coverage, and missing language-switch entry fixes on five character detail pages.

June 20 refresh added Developer Notes #14 / Version 1.6, the 100-day giveaway and livestream, and June 19 server-patch coverage with zh mirrors.

June 23 refresh added official Version 1.6 maintenance-schedule coverage with zh mirror, updated homepage/news hubs, refreshed current/upcoming banner wording around the original June 24 maintenance, and raised the page count to 258.

June 24 refresh added official Version 1.6 update-details coverage, Elizabeth EN/ZH character pages, Elizabeth EN/ZH banner decision pages, corrected the maintenance change to June 25 02:00-09:00 UTC, and raised the page count to 264.

June 25 refresh marked official Version 1.6 maintenance as completed, moved Elizabeth/Radiant Summer Memories from upcoming to current banner routing, refreshed best-banner/current-banner decision pages, and kept the page count at 264.

June 26 refresh added official Developer Notes #15, Version 1.6 Known Issues, Missing Potential Points compensation, and 100-Day Anniversary Survey coverage with EN/ZH mirrors; refreshed homepage/news/bugs-errors discovery paths and raised the page count to 272.
