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
- Current `index.html` count: `312`
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

June 30 refresh added official Midsummer Day Surprise Giveaway coverage with EN/ZH mirrors, refreshed homepage/news/event-schedule discovery paths, and raised the page count to 274.

July 1 refresh added official Exciting Cube Unboxing and Leaderboard Regular Season 1 issue coverage with EN/ZH mirrors, updated Version 1.6 Known Issues to the June 30 official state, refreshed homepage/news/event-schedule/bugs-errors discovery paths, and raised the page count to 278.

July 2 refresh added official Magic Pop and July 2 temporary-maintenance completed coverage with EN/ZH mirrors, updated Version 1.6 Known Issues and Version 1.6 Update Details to the July 2 official state, refreshed homepage/news/event-schedule/bugs-errors discovery paths, and raised the page count to 282.

July 6 refresh updated official Version 1.6 Known Issues to the July 6 state with Magic Pop party-entry, pet capture input-lock, and PS5 leaderboard reward mailbox entries; refreshed homepage/news/bugs-errors/leaderboard discovery paths and kept the page count at 282.

July 8 refresh updated official Magic Pop - The Day of Mischief Begins to the July 8 state with the mission-progress note that leaving before the game ends does not count knock-out or defeat objectives; refreshed homepage/news/event-schedule discovery paths and kept the page count at 282.

July 10 refresh added official Version 1.7 Special Livestream Schedule coverage from the July 9 notice with EN/ZH mirrors, updated Version 1.6 Known Issues to the July 9 state with Magic Pop room-state and Raid Pledge reward entries, refreshed homepage/news discovery paths, and raised the page count to 284.

July 13 refresh added official Developer Notes #16 and Twitch Drops Event coverage with EN/ZH mirrors, updated Twitch Drops and event-schedule hubs, refreshed homepage/news discovery paths and sitemap, and raised the page count to 288.

July 14 refresh added official Version 1.7 Update Details, Gowther Pick Up and Exclusive Skin, and Version 1.7 Maintenance Schedule coverage with EN/ZH mirrors; refreshed homepage/news/event-schedule/current-banner/upcoming-banner discovery paths and sitemap, and raised the page count to 294.

July 15 refresh added official Version 1.7 Known Issues coverage with EN/ZH mirrors, marked Version 1.7 maintenance as completed, moved current banner and pull-decision routing to Gowther, refreshed homepage/news/event-schedule/bugs-errors discovery paths and sitemap, and raised the page count to 296.

July 16 refresh added official Europe Server Connection Instability [Resolved] coverage with EN/ZH mirrors, updated Version 1.7 Known Issues for the Armor Set display issue, updated Twitch Drops pages for the Small Cube Key Bundle distribution issue, refreshed homepage/news/event-schedule/bugs-errors/Twitch discovery paths and sitemap, and raised the page count to 298.

July 17 refresh added official July 16 Data Patch [Completed] coverage with EN/ZH mirrors, updated Version 1.7 Known Issues for the Durak Abyss Leaderboard clear-record issue, refreshed homepage/news/event-schedule/bugs-errors discovery paths and sitemap, and raised the page count to 300.

July 21 refresh added official July 22 Temporary Maintenance coverage with EN/ZH mirrors, covering Knighthood Boss Battle, Knighthood rankings/shop, Timespace Junction Sector 9, Confirmed! Twigo, Durak Abyss ranking reset, and bug fixes; refreshed homepage/news/event-schedule/bugs-errors discovery paths and sitemap, and raised the page count to 302.

July 22 refresh added official Confirmed! Twigo event coverage with EN/ZH mirrors, marked July 22 Temporary Maintenance as completed, updated Version 1.7 Known Issues and Version 1.7 Update Details to the July 22 official state, refreshed Knighthood/home/news/event-schedule/bugs-errors discovery paths plus sitemap/README/project memory, and raised the page count to 304.

July 24 refresh added official PlayStation 5 Connection Instability coverage with EN/ZH mirrors, updated Version 1.7 Known Issues to the July 24 state with the Potential wording resolved item, refreshed homepage/news/bugs-errors discovery paths plus sitemap/README/project memory, and raised the page count to 306.

July 25 refresh marked the official PlayStation 5 Connection Instability notice as resolved at 02:20 UTC, refreshed EN/ZH PS5 status pages plus homepage/news/bugs-errors discovery paths, updated sitemap/README/project memory, and kept the page count at 306.

July 27 refresh updated official Version 1.7 Known Issues to the July 27 state with a jump-action Invincibility window issue in several boss/dungeon battles and intermittent Confirmed Twigo daily-reset failures; noted that official Gowther details were modified at 04:49 UTC without a published change summary; refreshed EN/ZH known-issues, homepage/news/current-banner discovery paths and sitemap; page count remains 306.

July 29 refresh added official July 28 Server Patch coverage with EN/ZH mirrors after the notice appeared following the previous daily check. The patch completed at 05:32 UTC without maintenance and fixed intermittent Confirmed Twigo daily-reset failures; players must fully exit and reconnect. Version 1.7 Known Issues moved the Twigo item to resolved while the jump-action Invincibility issue remains active. Refreshed Twigo/home/news/event-schedule/bugs-errors paths, corrected upcoming-banner routing to no confirmed post-Gowther pickup, updated sitemap/README/project memory, and raised the page count to 308.

July 30 refresh found no new July 30 article, but the official July 28 Server Patch notice had been modified on July 29 at 09:33 UTC. Netmarble distributed 10 Confirmed Twigo Event Tickets per affected day at 09:00 UTC to players whose reward rearrange count did not reset. Updated EN/ZH patch and Twigo event pages, homepage/news/event-schedule discovery paths, sitemap/README/project memory, and kept the page count at 308.

July 31 refresh added official Developer Notes #17 and YouTube copyright-claims/content-creation coverage with EN/ZH mirrors. Version 1.8 is framed as groundwork for Half-Anniversary Version 2.0 and confirms a limited-time 15-player Hunting Event, Memory of Dimensions, information/retry QoL, renewed Path of the Hero and Challenge Missions, five weekly Regular Hero Draw Ticket x10 deliveries, appreciation rewards claimable after the update through August 26 14:59 UTC, Timespace Season I Sector 12/finale timing, tutorial skip, World Level 3 rewards, and Tag Skill targeting changes. The notes do not reveal the next pickup. Refreshed homepage/news/event-schedule/upcoming-banner paths, sitemap/README/project memory, and raised the page count to 312.

August 1 daily check found no new official article ID and no new August 1 post. Official `/en/update` still advertises 「An Unknown Threat」 Version 1.7 and Gowther, while the list/detail API shows Developer Notes #17 (`id 266`) was updated on July 31 at 08:45 UTC. The existing EN/ZH Developer Notes #17 pages already included the added Path of the Hero/Challenge Missions renewal, five weekly Regular Hero Draw Ticket x10 deliveries, and Version 1.8 appreciation reward details, so only the visible update timestamp, `NewsArticle.dateModified`, sitemap lastmod, and project records were refreshed. Page count remains 312.

August 2 daily check found no new official article ID, no new August 2 post, and no August 2 `modDate` on the tracked current notices. Confirmed detail timestamps: Developer Notes #17 (`id 266`) mod `2026-07-31 08:45 UTC`, creator notice (`id 269`) mod `2026-07-30 10:00 UTC`, July 28 server patch (`id 268`) mod `2026-07-29 09:34 UTC`, Version 1.7 Known Issues (`id 249`) mod `2026-07-28 05:36 UTC`, and Gowther details (`id 244`) mod `2026-07-27 04:50 UTC`. Official `/en/update` still presents Version 1.7/Gowther and does not show Version 1.8 as the update landing page. No public content page or sitemap entry changed. Page count remains 312.

August 7 maintenance check found no verifiable new official article or post after the August 5 banner boundary. Direct Netmarble API requests were blocked by local DNS and an escalated retry was unavailable; official web fetch still showed Version 1.7/Gowther on `/en/update` and an empty `/en/news` shell. Refreshed EN/ZH current and upcoming banner routes, pull-decision pages, event schedules, homepage planner copy, and sitemap so Gowther Pick Up and Confirmed! Twigo are historical/completed and no successor is presented as confirmed. Page count remains `312`.
