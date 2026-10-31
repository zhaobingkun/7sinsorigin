# Project Memory

## October 31, 2026 — October 30 data patch refresh

- Official Netmarble article `id 360` confirms the October 30 08:00–08:15 UTC data patch. It fixed the Mighty Freaky Circus event-map entrance interaction issue after leaving the maze, improved targeting detection for chess pieces in Taranis's Sanctuary, and significantly reduced their HP.
- Updated the existing bilingual Version 2.3 issue coverage, bugs/errors hubs, Raid rewards guide, events schedule, homepage/news discovery and sitemap. Keep the 2.3 maze item resolved after the patch; the separate Weekly Reward, UI-label, Steam, party-movement and falling-beneath-ground items remain listed. Do not turn the HP change into a universal clear-time, tier or team claim.
- The direct shell request to `7origin.netmarble.com` failed DNS, but the required official list/detail API was verified through the official API response in Chrome. No separate thin data-patch page or banner/rate/pity inference was added.
- The first release check exposed that ignored Cloudflare `dist/` output was being scanned as source; excluding generated `.git`/`dist` paths from the policy and HTML validators restored the intended source-only check without changing deployment output.
- Release validation passed at 464 tracked HTML pages and 266 unique sitemap URLs; the shell `find` count remains 928 because it includes the ignored 464-page `dist/` mirror.
- Live browser verification caught residual wording in the Raid examples that treated the 500-Star-Fragment Abyss bonus as active; all EN/ZH references now mark it as historical and ended with Version 2.3.

## October 30, 2026 — Version 2.3 known issues and event refresh

- Official article `id 358` is updated October 29 at 05:28 UTC. It adds the Mighty Freaky Circus event-map entrance issue after leaving the maze, plus Weekly Reward recharge-screen, Estia Growth Mission Bundle label, locked Timespace ranking-label, Steam, party-movement, and falling-beneath-ground issues. The maze entrance issue is scheduled for the November 4 maintenance; only the Steam update and reconnect steps are stated workarounds.
- Official data patch `id 359` confirms the October 28 14:30–14:50 UTC patch added a Leave button below the Mighty Freaky Circus minimap and resumes from the explored maze's starting point after re-entry. Official `id 357` is the Version 2.3 details notice updated October 28 at 01:50 UTC.
- Added bilingual Version 2.3 Known Issues pages and refreshed the bilingual Version 2.3 update, bugs/errors, homepage, news indexes, events schedule, sitemap and project records. No separate thin data-patch page, successor banner, numeric rate, or tier claim was inferred.
- Current scale after validation is 464 HTML pages and 266 unique sitemap URLs. Direct official API access succeeded; live production verification remains a post-push step.

## October 29, 2026 — Version 2.3 official update and banner refresh

- Official Version 2.3 details confirm Estia and Clotho Pick Up announcements after the October 28 maintenance through the November 18 maintenance, plus Halloween content, Taranis [Transcendence], Star Map, World Level 5 and related systems. Added bilingual pages for the update and Estia; no numeric rates, tier rankings or successor banner were inferred.
- Refreshed bilingual home/news/current-banner/pull-budget/events discovery, updated the Partner Creator Season 2 page with the October 26 mid-season notice, and added four URLs to the sitemap. Lancelot/Elaine remain historical Version 2.2 pages.
- The required official API hostname did not resolve during this run; official localized Netmarble articles and web search were used as fallback evidence. Recheck live URLs after publishing.
- Validated scale after this release: 462 HTML pages and 264 unique sitemap URLs.

## October 23, 2026 — Version 2.3 Developer Notes and reset schedule

- Official Netmarble article `id 346`, `Developer Notes #21`, was published and modified at `2026-10-23T09:30:21.025Z`. It confirms Version 2.3 Bonus Locks, World Level 5, Corruption Frenzy, account-wide Star Map progression, a second Memory of Dimensions story, Taranis [Transcendence], Greed Incarnate rewards, and a Knighthood Boss Battle Season 2 revamp. Its Version 2.4 and 2027 items remain plans, not current release facts.
- Official article `id 351`, `Regarding Upcoming Raid and Knighthood Boss Battle Changes`, was published and modified at `2026-10-23T10:12:06.711Z`. It confirms Mystic Keys, Chaos Keys, and weekly Raid reward claim counts reset during the October 28 maintenance; post-update replenishment matches the amount used before the update. Knighthood Boss Battle is unavailable after the October 26 07:00 UTC weekly reset and the new season begins after October 28 maintenance.
- Added bilingual pages for both notices, refreshed homepage/news/events/Raid/Knighthood discovery, sitemap, README, and project memory. Current banner routes remain Lancelot/Elaine through October 28; no successor, rate, pity, or 2.4/2027 launch claim was inferred. Current scale is 458 HTML pages and 260 unique indexable sitemap URLs.

## October 20, 2026 — server patch and Version 2.2 issue refresh

- Official Netmarble article `id 345`, `October 20 (Tue) Server Patch [Completed]`, was published and modified at `2026-10-20T10:16:03.669Z`. It confirms the completed 09:40–10:14 UTC patch added the `Relentless Challenger` title to the Timespace Junction: Extra Season 1 Sector 12 first-clear reward; prior claimants receive the title during the October 28 maintenance. It also lists server-stability improvements.
- Official article `id 335` was materially updated at `2026-10-19T02:05:06.554Z` and adds a Chaos That Devours the Desert Event Mission V counting issue for SSR Equipment obtained from the Draco King Drake Boss Challenge. Updated the bilingual Known Issues pages and bugs/errors hub; no workaround or fix was invented.
- Added bilingual patch pages, refreshed homepage/news discovery, sitemap, README, and project records. Current scale is 454 HTML pages and 256 unique indexable sitemap URLs. No banner successor or unrelated Version 2.3 claim was inferred.

## October 19, 2026 — Version 2.3 equipment bonus-lock notice

- Official Netmarble article `id 344`, `Regarding Changes to Enchantment and Engraved Equipment Bonuses`, was published and modified at `2026-10-19T08:30:04.342Z`. It confirms that the Version 2.3 update during the October 28 maintenance will add selectable Bonus Locks for Enchantment and Engraved Equipment rerolls. Engraved Equipment can lock up to two bonuses; Enchantment can lock any number provided at least one remains unlocked; no additional resources are required and reroll cost remains unchanged.
- Added bilingual article pages at `/news/2026/10/enchantment-bonus-locks/` and `/zh/news/2026/10/enchantment-bonus-locks/`, refreshed homepage/news and systems discovery, and added both URLs to the sitemap. Do not infer new stat priorities, rates, a complete Version 2.3 feature list, or a banner successor after October 28.
- Current scale is 452 HTML pages and 254 unique sitemap URLs.

## October 14, 2026 — current Hunting Event and Version 2.2 refresh

- Official Netmarble article `id 342`, `Hunting Event - Chaos That Devours the Desert`, was published at `2026-10-14T07:01:23.327Z`. It confirms the October 14 07:00–November 4 06:59:59 UTC window, sequential Day 1–5 event quests through NPC Ensia, the Beings of Deep Darkness unlock, the 10–15-player Abyss dungeon The Hermit Beneath the Sand, up to two daily Desert Keeper’s Keys, first-clear Lichdragon’s Roar Weapon Selection Chest, the listed quest/mission rewards, and Golden Sand Token shop rules. Unused tokens reset after the event.
- Official article `id 335` was updated at `2026-10-14T09:25:00Z` and adds the PS5 `[Party Introduction] → [Enter Manually]` issue while `Set to Searchable` is active. Article `id 333` has the same update timestamp and marks the mobile Merlin Wand Special Attack `Electromagnetic Field` animation interruption resolved on October 8.
- Added EN/ZH current-event pages at `/news/2026/10/chaos-that-devours-desert/` and `/zh/news/2026/10/chaos-that-devours-desert/`; refreshed the Version 2.2 update/known-issues pages, homepage/news/events/bugs hubs, README, sitemap, and project records. Preserve the August event page as historical archive; do not infer a post-October-28 banner.
- Page count is 450 and sitemap count is 252 before the October 19 release; current scale is recorded above.

## October 13, 2026 — additional Knighthood maintenance and current issue update

- Official article `id 341`, `October 13 (Tue) Additional Temporary Maintenance [Completed]`, was modified at `2026-10-13T09:12:39Z`. It confirms an 08:30–09:10 UTC follow-up because Knighthood Boss Battle attempts and individual cumulative-score rewards did not reset after the first October 13 maintenance; the follow-up reset rankings and resumed sequential reward distribution, and lists Star Fragment ×300 maintenance compensation claimable through October 27 14:59 UTC.
- Official article `id 335`, Version 2.2 Known Issues, was modified at `2026-10-13T10:30:50Z` and adds the Draco King Drake higher-difficulty lower-quality `Tyrant Dragon's Black Heart Top` issue and the iOS controller Timespace Junction: Extra selection issue. It marks the Knighthood attempt-reset issue resolved on October 13; the existing controller, Hawk Pass XP, Steam, party movement, and falling-beneath-ground issues remain current.
- Updated existing bilingual maintenance and known-issues pages rather than creating a thin second news route. Refreshed homepage/news, bugs/errors, events schedule, Knighthood, sitemap, and metadata/project records. Page count remains `448`; sitemap remains `250` unique indexable URLs. No banner successor after October 28 was inferred.

## October 12, 2026 — official Knighthood maintenance follow-up

- Official Netmarble article `id 340`, `October 13 (Tue) Temporary Maintenance & Knighthood Boss Battle Ranking Notice`, was published and modified at `2026-10-12T09:32:36Z`. It confirms that Lancelot’s Gauntlets Special Attack `Anchor Shot` can stack across party members, schedules October 13 05:00–07:00 UTC maintenance, removes affected current-leaderboard records, postpones and equalizes ranking rewards, and lists Star Fragment ×300, Knighthood Coins ×50 for the stated participants, plus up to 15 individual cumulative-score coins under its conditions.
- Added bilingual article coverage and refreshed homepage/news, Knighthood, leaderboard, known-issues, events-schedule, sitemap, README, and project memory. Article 339 remains the initial investigation; no successor banner after October 28 was inferred. Current scale is 448 HTML pages and 250 unique sitemap URLs.

## October 11, 2026 — substantive content remediation

User authorization: after reporting the repeated AdSense low-value rejection, the user requested “还有什么要改的，一次改好”, then “继续”. This supersedes the earlier diagnostic-only status. Google approval is not guaranteed; no AdSense re-review or account setting was submitted.

- Rebuilt EN/ZH home, beginner/character/system/issue hubs, codes and event/resource guides. Replaced unsupported tier placements with an explicitly non-ranking investment guide; team planning now documents failure diagnosis and upgrade stop conditions without invented team tests.
- Added complete current Pick Up rules and six worked budgets: SSR pity, featured guarantee and each banner's separate one-time 120th Draw Bonus. Corrected Elaine's October 8 event-name revision to Whispers of the Wind. No invented conversion prices, drop rates or comparative DPS claims.
- Reviewed manual policy: 18 route pairs merged, 42 incomplete draft pairs withdrawn, 29 historical/reference pairs preserved with archive warnings. All are noindex and excluded from sitemap; old news remains dated history. With existing utility exclusions, 446 HTML pages remain and 248 unique indexable sitemap URLs remain. This is manual editorial triage, not a character-count threshold.
- Official new fact: article 339, Regarding Knighthood Boss Battle Ranking Issues, published/modified 2026-10-10 09:37:29 UTC (1791625049549). Integrated into existing Knighthood EN/ZH pages and home/news/bugs discovery. Measures are under review; no reset, cancellation or compensation is confirmed. Timespace article 324 is a separate issue; rechecked its October 8 API revision (1791425178816) and retained the October 28 14:59 UTC mailbox deadline.
- Removed advertising runtime across the entire site; kept homepage AdSense ownership metadata and ads.txt. The local privacy panel controls Analytics only and is not a certified advertising CMP. Do not restore advertising before a separately reviewed consent setup.
- Added content-policy.json, read-only validation, a mechanical --apply enforcement option, Vercel permanent redirects, deployment-file exclusions and a GitHub quality workflow. Retired the three historical page generators to prevent overwriting reviewed content. Read agents.md and use sh scripts/release_check.sh before every publication.
- Static validation has passed all 446 pages: one H1, canonical/hreflang, OG/Twitter, JSON-LD, images, local targets/fragments, unique indexable titles/descriptions, exact sitemap inclusion and policy/redirect consistency. Diff check, XML check and JS syntax check pass. Desktop/mobile QA checked home/menu, events, budget tables and Chinese leaderboard layout; no viewport overflow at 390 px. Publication/live verification is a separate release step, not implied by these local results.


- October 10 daily maintenance found no new Netmarble article ID or material modification after the October 8 records; the official API still ends at `id 338`. Corrected stale current-entry copy in the bilingual banner hubs, homepage known-issues cards, and EN/ZH events schedule so Lancelot and Elaine are current, Version 2.2 is the active issue route, and ended Version 2.0/2.1 activities are labeled as archives. Page count remains `446` with `404` indexable sitemap URLs. No successor after October 28 is confirmed.

- October 9 official-source maintenance verified new Netmarble articles `id 335` Version 2.2 Known Issues, `id 337` October 8 Server Patch, and `id 338` October 8 Server Patch [Completed]. It confirms the current 2.2 controller, Hawk Pass XP, Steam, party movement, and falling-under-ground issues; marks the Act 17 tutorial popup and Knighthood Headquarters entry as resolved; and adds the Ferzen Mines Raid Tag Skill fix. Article `id 312` was updated to October 8 10:00 UTC and now marks the 2.1 Khala, Hero Tag, Skip input, and controller cursor issues resolved. Added bilingual issue and patch pages, refreshed homepage/news/events/bugs discovery and current/upcoming/best-banner routing, and raised the page count to `446` with `404` indexable sitemap URLs. Do not infer a successor banner after October 28.

October 8 official-source maintenance verified that Version 2.2 is live after the scheduled maintenance. The official API added articles `id 322`, `326`, `327`, `328`, `329`, `330`, `331`, and updated full details as `id 333` (`modDate` `2026-10-08T00:49:10Z`). Added EN/ZH coverage for the livestream replay, Version 2.2 update details, Lancelot skills, Lancelot and Elaine Pick Up banners, Update Celebration Check-In, Draw Bingo, and Exciting Cube Unboxing. Current routing now points to Lancelot and Elaine through the October 28 maintenance; no successor after that window is confirmed. Page count is `442` with `400` indexable sitemap URLs. Do not infer a post-October-28 banner or universal meta ranking.

October 7 official-source maintenance verified new Netmarble article `id 323`, the Version 2.2 Maintenance Schedule, with API timestamp `2026-10-07T02:00:00Z`. It confirms the October 8 02:00–09:00 UTC maintenance, Lancelot, Guardian's Resolve, Main Quest Act 17, Cordin Village, Elaine Pick Up, Draco King Drake difficulties, Ranking Season 6, Timespace Extra Sectors 1–12, new events, and compensation. Added EN/ZH article pages, refreshed homepage/news/events/banner discovery, sitemap, README, and project records; page count is `426` with `384` indexable sitemap URLs. Keep Elaine's detailed rates, pity rules, and duration unconfirmed.

October 6 official-source maintenance verified new Netmarble article `id 332`, Regarding Changes to Raid Entry Currency, with API timestamp `2026-10-06T10:14:54Z`. It confirms Chaos Keys for Raid [Nightmare] and [Hell], two Weekly Reward claims per week across Chaos Keys and Mystic Keys, up to 1,000 Weekly Reward Star Fragments, a temporary 500-Star-Fragment Abyss reward through Version 2.3, and the recommendation to use existing Mystic Keys before Version 2.2. Added EN/ZH coverage and refreshed Raid rewards, events, homepage, and banner planning routes.

October 6 official-source maintenance verified material modification of article `id 321`, Version 2.2 Special Livestream Schedule & Details, with API `modDate` `2026-10-06T08:26:52Z`. Updated the existing EN/ZH pages' visible timestamp, JSON-LD `dateModified`, and Global guest note; no Lancelot banner, release date, rates, pity, or unrelated gameplay claim was inferred.

October 2 official-source maintenance verified new Netmarble article `id 324`, Regarding Leaderboard Regular Season 5 Issues, with API timestamp `2026-10-02T11:30:07Z`. The notice says an unintended use of certain heroes may affect Timespace Junction records, cancels Season 5 final-ranking rewards, grants participants the listed Star Fragment and Sector 3/4 Laurel of Glory compensation after the October 8 maintenance, and changes Regular Season 6 to equal rewards without ranking-based Titles or reward differences. Added EN/ZH article pages, refreshed homepage/news/events/bugs discovery, sitemap, README, and project memory; page count is `422` with `380` indexable sitemap URLs. Do not name a specific hero or method, and do not infer a banner or broader gameplay change.

October 2 official-source maintenance verified new Netmarble article `id 321`, Version 2.2 Special Livestream Schedule & Details, with API timestamp `2026-10-01T10:00:16Z`. The notice confirms an October 7, 11:00 UTC simultaneous Korean/Japanese/Global livestream, Lancelot skills and gameplay, a new main story, new content, and a replay link. Added EN/ZH article pages, refreshed homepage/news/events discovery and sitemap, and raised the page count to `420` with `378` indexable sitemap URLs. Keep Lancelot banner timing, release date, rates, pity, and the Version 2.2 maintenance window unconfirmed.

September 30 official-source maintenance verified the material `modDate` change for official article `id 312`, Version 2.1 Known Issues: the API timestamp is `2026-09-29T05:37:05Z`, while the official title says updated September 29 at 05:36 UTC. The added issue is the Khala Dual Swords Ultimate Move `Mirror Arsenal` additional effect `Normal Attack: Shaper - Mirage Blade` activating under the same fewer-than-three-Shaper condition as Copycat. Updated EN/ZH issue pages, homepage/news/bugs/events discovery, sitemap lastmods, and project records; page count remains `418` and the sitemap has `376` URLs. No banner, reward, rate, pity, or roadmap change was inferred.

September 29 official-source maintenance added bilingual coverage of article `id 320`, September 28 AOS Recommended Update. The notice confirms a no-maintenance Android update scheduled for 09:46 UTC that fixes intermittent repeat shader compilation when reconnecting. Updated homepage/news/bugs discovery, sitemap, README, and project records; page count is `418` and the sitemap has `376` indexable URLs. No banner, reward, rate, pity, or roadmap change was inferred.

September 26 AdSense content-quality pass added bilingual `/editorial-policy/` pages, expanded About/news/homepage source disclosures, removed generic homepage video placeholders, and marked 21 thin/utility EN/ZH page pairs `noindex,follow` while removing them from the sitemap and AdSense inventory. The pages remain accessible for users. The total `index.html` count is `416`; the sitemap has `374` indexable URLs. Historical policy, superseded October 11: use the manual content-policy.json decisions and substantive evidence before reinstatement, not a character-count gate.

September 24 official-source maintenance added bilingual coverage of official articles `id 319`, `315`, `316`, and `317`: Developer Notes #20, Update Eve Check-In, Koo and the Two Fools, and Swiftest Showdown. The new pages cover confirmed September 23–October 8 event windows, requirements, rewards, and roadmap plans while keeping Version 2.2–2.5 timing and future features explicitly unconfirmed. Page count was `414` before the editorial-policy pair was added.

September 26 official-source maintenance found no article after `id 319`, but `id 310` Developer Notes #19.5 had a material API modification at September 23 11:29 UTC. Refreshed its EN/ZH pages with the exact Raid Pledge same-Attribute/five-player easing and weekly Raid Shop quantities, updated visible timestamps and `NewsArticle.dateModified`, marked both news index cards as updated September 23, and advanced sitemap lastmods. The rest of the roadmap remains explicitly planned rather than confirmed; no banner change was inferred.

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
- Current `index.html` count: `454`
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

August 10 refresh found official Version 1.8 records after the August 7 boundary: Version 1.8 Update Details (`id 267`, updated August 5 08:50 UTC), Derieri hero details (`id 259`), Derieri Pick Up and Exclusive Skin (`id 260`, updated August 4 11:36 UTC), Version 1.8 Known Issues (`id 265`, updated August 5 09:58 UTC), August 5 and August 7 completed server patches (`ids 270` and `271`), Hawk Pass Season IV, and Leaderboard Regular Season 3 Issues (`id 275`). Added six EN/ZH official-source news pages plus a bilingual Leaderboard Guide, moved current banner routing to confirmed Derieri Pick Up, refreshed homepage/news/events/bugs/banner decision pages, updated sitemap and project records, and raised the page count to `326`.

August 11 refresh added EN/ZH coverage of the official Partner Creator Program Season 2 announcement (`id 272`, published August 10 09:30 UTC). The notice confirms recruitment until further notice, the 1,000-follower/subscriber eligibility threshold, three alternative monthly activity requirements, listed creator benefits, and the official application form. Refreshed homepage/news discovery and sitemap; no banner or gameplay claims were inferred; page count is `328`.

August 12 refresh added EN/ZH coverage of official Half Anniversary Eve Check-In (`id 273`), Chaos That Devours the Desert Hunting Event (`id 274`), and completed August 12 Temporary Maintenance (`id 276`). The new event pages record the August 12 to August 26 window, 14-day check-in rewards, Kalbash Hunting Event requirements/rewards, Timespace Sector 11 opening, maintenance compensation and fixes. Updated Version 1.8 Update Details (`id 267`) to August 12 07:14 UTC and Version 1.8 Known Issues (`id 265`) to August 12 07:43 UTC, including the new event-dungeon display issue and four resolved issues. Refreshed homepage/news/events/bugs discovery, sitemap, and page count to `334`.

August 14 maintenance refresh captured the later official `id 265` Version 1.8 Known Issues modification, titled `Updated on August 12 11:35 UTC` with API `modDate` at 11:37 UTC. Added the resolved intermittent server-connection issue to the EN/ZH coverage, synchronized exact visible and JSON-LD timestamps plus sitemap lastmods, and kept the page count at `334`; no new article ID or banner change was confirmed.

August 16 refresh found official `id 265` Version 1.8 Known Issues updated on August 14 at 10:00 UTC with a new Swiftest Showdown Day 4 retry-registration issue, and `id 276` August 12 maintenance updated on August 14 at 09:37 UTC with the same unresolved issue note. Article `id 263` Rewinding Fate - Into the Memory of Dimensions was present in the official feed but had no local page; added EN/ZH coverage with its Holy Knight Marmas requirement, Book of Stars entry path, single-player rules, saved progress, and no fixed end date. Refreshed EN/ZH known-issues and maintenance pages, homepage/news/events/bugs discovery paths, sitemap, and raised the page count to `336`.

August 18 refresh added EN/ZH coverage for official `id 277` Half-Anniversary Festival Special Livestream Schedule & Details and `id 279` Developer Notes #18. The livestream is scheduled for August 21 at 11:00 UTC and previews Version 2.0, Ban skills/gameplay, a new main quest, and new content. Developer Notes #18 outlines Version 2.0/2.1 systems including Raid [Hard], Transcendence Refinement, Maze, Boss Challenge [Transcendence], a six-hero rerun vote, planned Meliodas distribution, and Half-Anniversary rewards. Refreshed homepage/news/events/upcoming-banner discovery paths and sitemap; page count is `340`. No Ban or successor banner was treated as confirmed.

August 19 maintenance refresh found no new official article IDs after `id 279`. The official API shows `id 276` was refreshed on August 18 at 06:20 UTC; its current body is already covered, but the EN/ZH maintenance pages were corrected so they no longer state an 08:00 completion after the notice's current 03:00-07:40 UTC window. Updated article timestamps, JSON-LD, sitemap lastmods, and project records; page count remains `340`. No banner change or successor was confirmed.

August 22 refresh added EN/ZH coverage of official `id 280` Official Discord AMA Season 3. The pages record the August 21 11:00 UTC to September 2 06:59 UTC question window, official Discord channel, five question categories, sequential-answer caveat, and channel moderation notes. Official `id 278` Half Anniversary Festival Livestream was a material follow-up to `id 277`; the existing EN/ZH livestream pages now describe the August 21 replay state and cite both official notices. Refreshed homepage/news/events discovery paths and sitemap; page count is `342`. No new banner, rate, pity, or release-date claim was inferred.

August 25 refresh added EN/ZH coverage of official `id 289`, 「The Traitor's Street」 Version 2.0 Maintenance Schedule, for August 26 UTC. The notice confirms Ban, Ravens, Indura Monspeet, Transcendence Engravement/Refinement, Raid [Nightmare], Ranking Season 4, ending Version 1.8 content, and Star Fragment x300 compensation through September 9 14:59 UTC. Kept Derieri current until maintenance completion and moved Ban into confirmed-upcoming routing without inventing banner rates, pity, or maintenance hours. Refreshed homepage/news/events/bugs/banner decision paths and sitemap; page count is `344`.

August 26 refresh added EN/ZH coverage of official Version 2.0 Update Details (`id 290`), Hero Ban Details (`id 288`), Ban Pick Up & Exclusive Skin (`id 282`), and Poll Draw Survey (`id 286`). The notices confirm the post-maintenance Ban pickup window, Hero Pick Up Draw Tickets, six rerun candidates, Ravens, Labyrinth, Raid Nightmare, Transcendence systems, and new events. Updated the maintenance page with the confirmed 02:00-09:00 UTC window, refreshed homepage/news/events/bugs/banner routing, sitemap, and project records, and raised the page count to `352`. Kept Derieri current until official maintenance completion is verified; no numeric Ban rate, pity carryover, or rerun banner was inferred.

August 27 refresh verified official `id 292` Twitch Drops Event and `id 291` Version 2.0 Known Issues, plus material modifications to `id 289` maintenance, `id 290` Version 2.0 details, `id 288` Ban details, `id 282` Ban Pick Up, `id 265` Version 1.8 Known Issues, and `id 267`/`id 258` event-extension details. Added EN/ZH Twitch Drops and Version 2.0 Known Issues pages, marked the August 26 maintenance completed with the final 02:00-10:00 UTC window and two Star Fragment x300 compensations, moved current banner routing to Ban, extended Chaos That Devours the Desert through the September 2 maintenance, refreshed homepage/news/events/bugs/sitemap routes, and raised the page count to `356`. No successor banner or unsupported rate, pity, leak, or meta claim was inferred.

August 28 refresh added EN/ZH coverage of official `id 112`, August 27 Server Patch [Completed]. The patch ran from 10:20 to 10:32 UTC and fixed higher-grade equipment consumption during Engraved Equipment Refinement, missing Transcendence Essence drops in the Indura Monspeet Boss Challenge, and balance/HP handling in two Act 16 quests. Refreshed homepage/news/events/bugs discovery paths and sitemap; page count is `358`.

August 30 daily check found no new official Netmarble article IDs and no article modifications after the August 27 changes already covered on the site. Official `/en/update` now visibly confirms Ban has arrived, matching the existing Ban current-banner routes. Corrected the English homepage planner's stale Derieri default copy and kept the project page count synchronized at `358`; no new news page was created.

September 1 refresh verified official `id 164`, August 31 Recommended Update, and a material August 31 update to `id 291`, Version 2.0 Known Issues. The recommended update was applied without maintenance at 02:00 UTC and fixed intermittent Physical-attribute damage-number display plus incorrect download-screen logo language. The known-issues notice added the Ban-owned Protein Bug Skewer region-quest issue and marked those two display issues resolved. Added EN/ZH recommended-update pages, refreshed EN/ZH known-issues coverage, homepage/news/events/bugs discovery paths, corrected the stale Chinese current-banner route to live Ban, updated the sitemap, and refreshed project records; page count is `360`. No banner, rate, pity, leak, or unsupported meta claim was inferred.

September 4 refresh verified official `id 293`, September 3 Temporary Maintenance [Completed], and the September 3 update to `id 291`, Version 2.0 Known Issues. The final maintenance window was 03:00–08:20 UTC; it opened Event Boss - Her Return, Holy Knights and Thieves, and Timespace Season 2 Sector 1, while Labyrinth was excluded pending further review. Added EN/ZH maintenance coverage, updated Known Issues to list five September 3 resolutions and six remaining issues, refreshed homepage/news/events/bugs discovery and sitemap, and raised the page count to `362`. Ban remains the confirmed current pickup; no successor, rate, pity, leak, or unsupported meta claim was inferred.

September 7 refresh verified official `id 297`, September 7 Server Patch [Completed]. The patch completed at 06:08 UTC and fixed intermittent inability to play the Holy Knights and Thieves minigame under certain conditions. Added EN/ZH patch coverage and sitemap entries; page count is `370`. No banner, reward, rate, or Labyrinth release claim was inferred.

September 8 refresh verified material updates to official `id 293` and `id 291`, both titled as updated at 03:04 UTC (API modification timestamps 03:04:25 and 03:06:16 UTC). The maintenance notice moved the Oasis Village NPC minimap-icon issue out of the September 3 resolved fixes and into a later-fix state; the Version 2.0 Known Issues EN/ZH pages now list it as current, with four September 3 resolutions. Refreshed maintenance/known-issues pages, bugs/errors and homepage/news discovery, sitemap lastmods, and project records; page count remains `370`.

September 10 refresh added EN/ZH coverage of official `id 298`, September 10 Server Patch & Regarding Leaderboard Regular Season 4 [Completed]. The patch completed at 02:31 UTC, fixed Boss Challenge restart/party-record bugs and Field Boss reward issues, closed the Indura Monspeet and Her Return Transcendence leaderboards, and set clear-based apology compensation plus equal rewards for future Transcendence time attacks until system improvements are complete. Refreshed homepage/news/events/bugs/leaderboard discovery paths and sitemap; page count is `372`. Ban remains the confirmed current pickup and no successor banner was inferred.

September 10 SEO opportunity refresh used the supplied traffic report as a prioritization input. The report's claim that no codes page existed was incorrect: `/codes/` and `/zh/codes/` were already present. Updated those pages to answer current-code status directly, added homepage codes discovery, refreshed tier-list/banner hubs for operational search intent, corrected stale Merlin Version 1.5 current-banner wording to an official-survey/rerun-watch state, and synchronized Clotho/upcoming-characters watchlist language. All EN/ZH pairs and sitemap lastmods were updated; page count remains `372`. Survey candidates and watchlist names must not be presented as confirmed banners.

September 11 daily refresh found no new official article ID or banner change. Official `id 293` and `id 297` had September 10 API modification timestamps, but their current maintenance and patch facts were already covered. Refreshed EN/ZH visible recheck timestamps, JSON-LD `dateModified`, homepage/news discovery parity, and sitemap lastmods; page count remains `372`. Ban remains the confirmed current pickup.

September 5 refresh captured official event notices `ids 294`, `295`, and `296` for Her Return, Holy Knights and Thieves, and Timespace Junction Season 2. Added EN/ZH event pages, refreshed homepage/news/events discovery and sitemap, corrected the maintenance record to the official 03:00–08:20 UTC window and September 4 09:02 UTC update, and raised the page count to `368`. Ban remains the confirmed current pickup; no successor, rate, pity, leak, or unsupported meta claim was inferred.

September 12 refresh verified official article `id 299`, Developer Notes #19 - Discord AMA Season 3 Answers, published and modified September 11 at 11:00 UTC. Added EN/ZH coverage of the Labyrinth removal explanation, Version 2.1 plans, Ferzen Mines, Knighthood Headquarters, Poll Draw rerun format, future content, Daily Mission revamp, and AMA answers; refreshed homepage/news/events/upcoming-banner discovery and sitemap. Page count is `374`. No 2.1 date, Poll Draw hero names, new banner rate, or Labyrinth return date was inferred.
