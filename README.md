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
Current `index.html` count: `372`

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

July 14 refresh added official Version 1.7 Update Details, Gowther Pick Up and Exclusive Skin, and Version 1.7 Maintenance Schedule coverage with Chinese mirrors; refreshed homepage/news/event-schedule/current-banner/upcoming-banner discovery paths and sitemap, and raised the page count to 294.

July 15 refresh added official Version 1.7 Known Issues coverage with Chinese mirror, marked Version 1.7 maintenance as completed, moved current banner and pull-decision routing to Gowther, refreshed homepage/news/event-schedule/bugs-errors discovery paths and sitemap, and raised the page count to 296.

July 16 refresh added official Europe Server Connection Instability [Resolved] coverage with Chinese mirror, updated Version 1.7 Known Issues for the Armor Set display entry, updated Twitch Drops pages for the Small Cube Key Bundle distribution issue, refreshed homepage/news/event-schedule/bugs-errors/Twitch discovery paths and sitemap, and raised the page count to 298.

July 17 refresh added official July 16 Data Patch [Completed] coverage with Chinese mirror, updated Version 1.7 Known Issues for the Durak Abyss Leaderboard clear-record entry, refreshed homepage/news/event-schedule/bugs-errors discovery paths and sitemap, and raised the page count to 300.

July 21 refresh added official July 22 Temporary Maintenance coverage with Chinese mirror, updated homepage/news/event-schedule/bugs-errors discovery paths and sitemap, and raised the page count to 302.

July 22 refresh added official Confirmed! Twigo coverage with Chinese mirror, marked July 22 Temporary Maintenance as completed, updated Version 1.7 Known Issues and Update Details to the July 22 official state, refreshed Knighthood/home/news/event-schedule/bugs-errors discovery paths and sitemap, and raised the page count to 304.

July 24 refresh added official PlayStation 5 Connection Instability coverage with Chinese mirror, updated Version 1.7 Known Issues to the July 24 official state, refreshed homepage/news/bugs-errors discovery paths and sitemap, and raised the page count to 306.

July 25 refresh marked the official PlayStation 5 Connection Instability notice as resolved at 02:20 UTC, refreshed homepage/news/bugs-errors discovery paths and sitemap, and kept the page count at 306.

July 27 refresh updated the EN/ZH Version 1.7 Known Issues coverage with the new jump-action Invincibility timing and Confirmed Twigo daily-reset issues, noted the official Gowther detail-page refresh without inferring an undocumented skill change, refreshed homepage/news/current-banner discovery paths and sitemap, and kept the page count at 306.

July 29 refresh added EN/ZH coverage of the official July 28 server patch that fixed Confirmed Twigo daily resets, moved the issue to resolved in Version 1.7 Known Issues, refreshed the Twigo event/home/news/event-schedule/bugs-errors paths, corrected the upcoming-banner page to show no confirmed successor to Gowther, updated the sitemap, and raised the page count to 308.

July 30 refresh found no new July 30 article, but captured the July 29 09:33 UTC update to the official server-patch notice: affected players received 10 Confirmed Twigo Event Tickets per impacted day at 09:00 UTC. Updated the EN/ZH patch and event pages, homepage/news/event-schedule discovery paths, and sitemap; page count remains 308.

July 31 refresh added EN/ZH coverage of Developer Notes #17 and the official YouTube copyright-claims/content-creation notice. The 1.8 preview confirms a 15-player Hunting Event, Memory of Dimensions, QoL and mission renewals, five weekly Regular Hero Draw Ticket x10 deliveries, appreciation rewards, and the Timespace Season I finale, while confirming no next pickup. Refreshed homepage/news/event-schedule/upcoming-banner paths and sitemap, and raised the page count to 312.

August 1 daily check found no new official article ID and no new August 1 post. Netmarble had updated Developer Notes #17 on July 31 at 08:45 UTC; the existing EN/ZH pages already covered the added mission reward and support reward details, so only the visible official update time, article `dateModified`, sitemap lastmod, and project notes were refreshed. Page count remains 312.

August 2 daily check found no new official article ID, no new August 2 post, and no August 2 `modDate` on the tracked current notices. The official update page still advertises 「An Unknown Threat」 Version 1.7 / Gowther, and Developer Notes #17 remains the latest list item with its July 31 08:45 UTC update. No public content page or sitemap entry changed. Page count remains 312.

August 7 maintenance check found no verifiable new official article ID or post after the August 5 banner boundary. Direct Netmarble API requests were blocked by local DNS and the escalation retry was unavailable; official web fetch still showed Version 1.7/Gowther on `/en/update` and an empty `/en/news` shell. Updated EN/ZH current and upcoming banner routes, pull-decision pages, event schedules, homepage planner copy, and sitemap so Gowther Pick Up and Confirmed! Twigo are historical/completed and no successor is presented as confirmed. Page count remains 312.

August 10 refresh found official Version 1.8 records after the August 7 boundary: Version 1.8 Update Details (`id 267`, updated August 5 08:50 UTC), Derieri hero details (`id 259`), Derieri Pick Up and Exclusive Skin (`id 260`, updated August 4 11:36 UTC), Version 1.8 Known Issues (`id 265`, updated August 5 09:58 UTC), August 5 and August 7 completed server patches (`ids 270` and `271`), Hawk Pass Season IV, and Leaderboard Regular Season 3 Issues (`id 275`). Added six EN/ZH official-source news pages plus a bilingual Leaderboard Guide, moved current banner routing to confirmed Derieri Pick Up, refreshed homepage/news/events/bugs/banner decision pages, updated sitemap and project records, and raised the page count to `326`.

August 11 refresh added EN/ZH coverage of the official Partner Creator Program Season 2 announcement (`id 272`, published August 10 09:30 UTC). The pages record the 1,000-follower/subscriber threshold, monthly video or livestream options, program benefits, application form, and policy caveats; refreshed homepage/news discovery and sitemap, and raised the page count to `328`.

August 12 refresh added EN/ZH coverage of the official Half Anniversary Eve check-in (`id 273`), Chaos That Devours the Desert Hunting Event (`id 274`), and completed August 12 maintenance (`id 276`). Updated Version 1.8 Update Details (`id 267`) and Known Issues (`id 265`) to their August 12 timestamps and current issue/resolution state, refreshed homepage/news/events/bugs discovery, updated sitemap, and raised the page count to `334`.

August 14 maintenance refresh captured the official `id 265` Version 1.8 Known Issues modification titled `Updated on August 12 11:35 UTC`, added the resolved intermittent server-connection issue to the EN/ZH pages, synchronized exact update timestamps and sitemap lastmods, and kept the page count at `334`. No newer official article ID or banner change was found.

August 16 refresh found official `id 265` Version 1.8 Known Issues updated on August 14 at 10:00 UTC with a new Swiftest Showdown Day 4 retry-registration issue, and `id 276` August 12 maintenance updated on August 14 at 09:37 UTC with the same unresolved issue note. Added EN/ZH coverage for the previously uncovered official `id 263` Rewinding Fate - Into the Memory of Dimensions article, refreshed the known-issues and maintenance pages, homepage/news/events/bugs discovery paths, sitemap, and project records, and raised the page count to `336`.

August 18 refresh added EN/ZH coverage of official `id 277` Half-Anniversary Festival Special Livestream Schedule & Details and `id 279` Developer Notes #18. The pages cover the August 21 11:00 UTC livestream, Version 2.0/2.1 roadmap, Raid [Hard], Transcendence Refinement, Maze, the six-hero rerun vote, planned Meliodas distribution, and Half-Anniversary rewards while keeping Ban and later banners unconfirmed. Refreshed homepage/news/events/upcoming-banner discovery paths and sitemap; page count is `340`.

August 19 maintenance refresh found no new official article IDs after `id 279`. The official API shows `id 276` was refreshed on August 18 at 06:20 UTC; its current body is already covered, but the maintenance page was corrected so it no longer states an 08:00 completion after the notice's current 03:00-07:40 UTC window. Updated EN/ZH article timestamps, JSON-LD, sitemap lastmods, and project records; page count remains `340`. No banner change or successor was confirmed.

August 22 refresh added EN/ZH coverage of official `id 280` Official Discord AMA Season 3, including the August 21 11:00 UTC to September 2 06:59 UTC question window, Discord channel, topic categories, and participation caveats. The official `id 278` Half Anniversary Festival Livestream notice was also incorporated into the existing livestream page as the August 21 replay state. Refreshed homepage/news/events discovery paths and sitemap; page count is `342`. No new banner, rate, pity, or release-date claim was inferred.

August 25 refresh added EN/ZH coverage of official article `id 289`, 「The Traitor's Street」 Version 2.0 Maintenance Schedule, for August 26 UTC. The notice confirms Ban, the Ravens region, Indura Monspeet, Transcendence Engravement/Refinement, Raid [Nightmare], Ranking Season 4, ending Version 1.8 content, and Star Fragment x300 compensation through September 9 14:59 UTC. Kept Derieri current until maintenance completion and moved Ban into confirmed-upcoming routing without inventing banner rates, pity, or maintenance hours. Refreshed homepage/news/events/bugs/banner decision paths and sitemap; page count is `344`.

August 26 refresh added EN/ZH coverage of official Version 2.0 Update Details (`id 290`), Hero Ban Details (`id 288`), Ban Pick Up & Exclusive Skin (`id 282`), and Poll Draw Survey (`id 286`). The notices confirm the post-maintenance Ban pickup window, Hero Pick Up Draw Tickets, six rerun candidates, Ravens, Labyrinth, Raid Nightmare, Transcendence systems, and new events. Updated the maintenance page with the confirmed 02:00-09:00 UTC window, refreshed homepage/news/events/bugs/banner routing, sitemap, and project records, and raised the page count to `352`. Kept Derieri current until official maintenance completion is verified; no numeric Ban rate, pity carryover, or rerun banner was inferred.

August 27 refresh verified official articles `id 292` Twitch Drops Event and `id 291` Version 2.0 Known Issues, plus material updates to `id 289` maintenance, `id 290` Version 2.0 details, `id 288` Ban details, `id 282` Ban Pick Up, `id 265` Version 1.8 Known Issues, and `id 267`/`id 258` event-extension details. Added EN/ZH Twitch Drops and Version 2.0 Known Issues pages, marked maintenance completed with the final 02:00-10:00 UTC window and two Star Fragment x300 compensations, moved current banner routing to Ban, extended Chaos That Devours the Desert to the September 2 maintenance, and refreshed homepage/news/events/bugs/sitemap routes. Page count is `356`; no successor banner or unconfirmed meta/rate claim was added.

August 28 refresh added EN/ZH coverage of official `id 112`, August 27 Server Patch [Completed]. The patch ran from 10:20 to 10:32 UTC and fixed higher-grade equipment consumption during Engraved Equipment Refinement, missing Transcendence Essence drops in the Indura Monspeet Boss Challenge, and balance/HP handling in two Act 16 quests. Refreshed homepage/news/events/bugs discovery paths and sitemap; page count is `358`.

September 1 refresh verified official `id 164`, August 31 Recommended Update, and a material August 31 update to `id 291`, Version 2.0 Known Issues. The recommended update required no maintenance and fixed intermittent Physical-attribute damage-number display plus incorrect download-screen logo language. The known-issues notice added the Ban-owned Protein Bug Skewer region-quest issue and marked those two display issues resolved. Added EN/ZH recommended-update pages, refreshed EN/ZH known-issues coverage, homepage/news/events/bugs discovery paths, corrected the stale Chinese current-banner route to live Ban, updated the sitemap, and refreshed project records. Page count is `360`.

September 4 refresh verified official `id 293`, September 3 Temporary Maintenance [Completed], and the September 3 update to `id 291`, Version 2.0 Known Issues. The maintenance completed at 08:20 UTC, opened Event Boss - Her Return, Holy Knights and Thieves, and Timespace Junction Season 2 Sector 1, and excluded Labyrinth pending further review. Added EN/ZH maintenance pages, updated Known Issues with five resolved items and six remaining issues, refreshed homepage/news/events/bugs discovery and sitemap, and raised the page count to `362`.

September 5 refresh captured official event notices `ids 294`, `295`, and `296` for Her Return, Holy Knights and Thieves, and Timespace Junction Season 2. Added EN/ZH event pages, refreshed homepage/news/events discovery and sitemap, and corrected the official September 3 maintenance window to 03:00–08:20 UTC plus the September 4 09:02 UTC update. The page count is `368`; Ban remains the confirmed current pickup.

September 7 refresh added official `id 297`, September 7 Server Patch [Completed]. The patch completed at 06:08 UTC and fixed intermittent access to the Holy Knights and Thieves minigame. Added EN/ZH patch pages, refreshed news discovery and sitemap, and raised the page count to `370`. No banner, reward, rate, or Labyrinth release claim was inferred.

September 8 refresh captured material updates to official `id 293` and `id 291`, both titled as updated at 03:04 UTC (API modification timestamps 03:04:25 and 03:06:16 UTC). The maintenance notice now says the Oasis Village NPC minimap-icon issue needs a later fix, and the Version 2.0 Known Issues page lists it as current instead of resolved; refreshed EN/ZH pages, bugs/errors discovery, homepage/news labels, sitemap lastmods, and project records. Page count remains `370`.

September 10 refresh added EN/ZH coverage of official article `id 298`, the completed server patch that fixed Boss Challenge restart/party-record bugs and Field Boss reward issues, closed the two affected Transcendence leaderboards, and replaced ranking rewards with clear-based apology compensation. Refreshed homepage/news/events/bugs/leaderboard discovery paths and sitemap; Ban remains the confirmed current pickup and the page count is `372`.

September 11 daily refresh found no new official article ID or banner change. Official `id 293` and `id 297` showed September 10 API modification timestamps, but their current content was already fully covered; refreshed EN/ZH visible recheck timestamps, JSON-LD `dateModified`, homepage/news discovery parity, sitemap lastmods, and project records. Page count remains `372`.
