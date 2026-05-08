from __future__ import annotations

import re
from pathlib import Path


ROOT = Path("/Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin")
TODAY = "2026-05-08"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def replace_required(text: str, old: str, new: str) -> str:
    if new in text:
        return text
    return text.replace(old, new) if old in text else text


def sub_required(pattern: str, repl: str, text: str) -> str:
    new_text, count = re.subn(pattern, repl, text, flags=re.S)
    return new_text if count else text


def update_homepage(path: Path, zh: bool = False) -> None:
    text = read(path)
    if not zh:
        text = replace_required(
            text,
            "<title>The Seven Deadly Sins: Origin Guide, News, Release Date</title>",
            "<title>The Seven Deadly Sins: Origin Guide, Current Banner, Tier List & News</title>",
        )
        text = replace_required(
            text,
            'content="The Seven Deadly Sins: Origin guide hub with release date updates, pre-register steps, character guides, tier list, systems, and latest official news."',
            'content="The Seven Deadly Sins: Origin guide hub with current banner advice, tier list updates, beginner teams, diamond farming paths, fixes, and latest official news."',
        )
        text = replace_required(
            text,
            'content="Guide hub for The Seven Deadly Sins: Origin with release date tracking, pre-register steps, characters, tier list, systems, and news."',
            'content="Guide hub for The Seven Deadly Sins: Origin with current banner advice, tier list updates, beginner teams, currency planning, and live-service news."',
        )
        text = replace_required(
            text,
            "<h1>The Seven Deadly Sins: Origin Guide, News, and Release Date Hub</h1>",
            "<h1>The Seven Deadly Sins: Origin Guide Hub for Current Banner, Tier List, and Best Teams</h1>",
        )
        text = replace_required(
            text,
            """<p class="lead">
            The Seven Deadly Sins: Origin is an anime-inspired open-world RPG set in Britannia. This homepage is built to track the game in one place:
            release date updates, pre-register steps, official news, characters, tier list changes, beginner systems, and launch-week checklists without making you dig through scattered trailers and posts.
          </p>""",
            """<p class="lead">
            The Seven Deadly Sins: Origin is now in its live-service phase, so the homepage needs to answer current-player questions first:
            what banner is worth it now, who to build first, how to farm diamonds faster, which beginner teams are safest after launch, and which fixes to open when crashes, controller problems, or mobile performance issues get in the way.
          </p>""",
        )
        text = replace_required(
            text,
            '<div class="status-item"><span>Core Search Intent</span><strong>The Seven Deadly Sins: Origin release date, news, characters, and beginner guides</strong></div>',
            '<div class="status-item"><span>Current Search Intent</span><strong>Current banner, current tier list, best team, diamonds, and post-launch fixes</strong></div>',
        )
        text = replace_required(
            text,
            '<div class="status-item"><span>World Focus</span><strong>Britannia, open-world exploration, team setup, and launch progression</strong></div>',
            '<div class="status-item"><span>Live-Service Focus</span><strong>Patch notes, roster decisions, routine progression, and account efficiency</strong></div>',
        )
        text = replace_required(
            text,
            '<div class="status-item"><span>Use Case</span><strong>Quick answers before launch and patch-day checklists after updates</strong></div>',
            '<div class="status-item"><span>Best Use Case</span><strong>Quick answers for active players who need a banner decision, team route, or fix page right now</strong></div>',
        )
        text = replace_required(
            text,
            """<div class="container status-strip" data-reveal style="--delay: .04s;">
        <a class="status-card" href="/release-date/"><span>Release Date</span><strong>Timeline Tracker</strong></a>
        <a class="status-card" href="/pre-register/"><span>Pre-Register</span><strong>Steps and Rewards</strong></a>
        <a class="status-card" href="/characters/"><span>Characters</span><strong>Roles and Builds</strong></a>
        <a class="status-card" href="/events-schedule/"><span>Event Flow</span><strong>Schedule and Rewards</strong></a>
      </div>""",
            """<div class="container status-strip" data-reveal style="--delay: .04s;">
        <a class="status-card" href="/banners/current/"><span>Current Banner</span><strong>Pull Decision</strong></a>
        <a class="status-card" href="/tier-list/"><span>Current Tier List</span><strong>Build Priority</strong></a>
        <a class="status-card" href="/how-to-farm-diamonds-fast/"><span>Diamond Farming</span><strong>Fastest Sources</strong></a>
        <a class="status-card" href="/news/2026/04/patchnotes-1-1-here/"><span>Patch Notes</span><strong>Version 1.1</strong></a>
      </div>""",
        )
        text = replace_required(text, "<h2>Recommended Paths</h2>", "<h2>Recommended Post-Launch Routes</h2>")
        text = replace_required(
            text,
            "<p>Follow the route that matches the problem you are actually trying to solve. Each cluster below is meant to send you to a small set of pages with a clear next action.</p>",
            "<p>Follow the route that matches the problem you are actually trying to solve after launch. These clusters are built around current-player searches, not countdown traffic.</p>",
        )
        text = sub_required(
            r'<div class="route-grid">.*?</div>\s*</div>\s*</section>',
            """<div class="route-grid">
          <article class="card route-card" data-reveal style="--delay: .05s;">
            <h3>Current Meta Route</h3>
            <p>Use this route if the real question is who to build now and which pages reflect the live account meta.</p>
            <ul class="route-links">
              <li><a href="/current-tier-list-may-2026/">Current Tier List (May 2026)</a></li>
              <li><a href="/best-team-for-beginners-may-2026/">Best Team for Beginners</a></li>
              <li><a href="/best-f2p-team-may-2026/">Best F2P Team</a></li>
              <li><a href="/tier-list/">Tier List Hub</a></li>
              <li><a href="/characters/">Characters</a></li>
            </ul>
            <p class="route-note">Best for players deciding where limited materials should go after launch.</p>
          </article>
          <article class="card route-card" data-reveal style="--delay: .1s;">
            <h3>Banner and Diamonds Route</h3>
            <p>Use this route when the real issue is whether to pull, save, farm diamonds, or wait for the next cycle.</p>
            <ul class="route-links">
              <li><a href="/current-banner-worth-it/">Is the Current Banner Worth It?</a></li>
              <li><a href="/next-banner-should-you-save/">Next Banner: Should You Save?</a></li>
              <li><a href="/how-to-farm-diamonds-fast/">How to Farm Diamonds Fast</a></li>
              <li><a href="/best-use-of-diamonds/">Best Use of Diamonds</a></li>
              <li><a href="/currency-guide/">Currency Guide</a></li>
            </ul>
            <p class="route-note">Best for players trying to avoid short-horizon pulls and weak spending decisions.</p>
          </article>
          <article class="card route-card" data-reveal style="--delay: .15s;">
            <h3>Routine Growth Route</h3>
            <p>Use this route when your account is active but your growth loop still feels messy.</p>
            <ul class="route-links">
              <li><a href="/daily-checklist/">Daily Checklist</a></li>
              <li><a href="/weekly-checklist/">Weekly Checklist</a></li>
              <li><a href="/launch-day-checklist/">Launch Day Checklist</a></li>
              <li><a href="/top-10-beginner-mistakes-after-launch/">Top 10 Beginner Mistakes After Launch</a></li>
              <li><a href="/beginner-guide/">Beginner Guide</a></li>
            </ul>
            <p class="route-note">Best for players who need a cleaner first-week and first-month routine.</p>
          </article>
          <article class="card route-card" data-reveal style="--delay: .2s;">
            <h3>Fix and Performance Route</h3>
            <p>Use this route when the game runs badly, crashes, or control support is blocking play.</p>
            <ul class="route-links">
              <li><a href="/crash-on-launch-fix/">Crash on Launch Fix</a></li>
              <li><a href="/mobile-performance-settings/">Mobile Performance Settings</a></li>
              <li><a href="/steam-controller-not-working/">Steam Controller Not Working</a></li>
              <li><a href="/best-settings/">Best Settings</a></li>
              <li><a href="/bugs-errors/">Bugs and Errors Hub</a></li>
            </ul>
            <p class="route-note">Best for players trying to fix launch friction before they even judge the roster or banner meta.</p>
          </article>
        </div>
      </div>
    </section>""",
            text,
        )
        text = replace_required(
            text,
            "<h2>New Reward Pages</h2>",
            "<h2>Current Decision Pages</h2>",
        )
        text = replace_required(
            text,
            '<p><a href="/codes/">Codes Tracker</a> · <a href="/twitch-drops/">Twitch Drops</a> · <a href="/events-schedule/">Events Schedule</a></p>',
            '<p><a href="/current-banner-worth-it/">Current Banner Worth It?</a> · <a href="/next-banner-should-you-save/">Next Banner: Should You Save?</a> · <a href="/save-summons-or-pull-now/">Save Summons or Pull Now?</a></p>',
        )
        text = replace_required(
            text,
            "<p class=\"small\">These pages target launch-week reward intent instead of broad guide intent, which gives the site more long-tail entry points.</p>",
            "<p class=\"small\">These pages target active banner and resource searches instead of countdown traffic, which is where the live-service volume now sits.</p>",
        )
        text = replace_required(text, "<h2>New Routine Pages</h2>", "<h2>Growth and Routine Pages</h2>")
        text = replace_required(
            text,
            '<p><a href="/daily-checklist/">Daily Checklist</a> · <a href="/weekly-checklist/">Weekly Checklist</a> · <a href="/all-achievements/">All Achievements</a></p>',
            '<p><a href="/daily-checklist/">Daily Checklist</a> · <a href="/weekly-checklist/">Weekly Checklist</a> · <a href="/top-10-beginner-mistakes-after-launch/">Top 10 Beginner Mistakes After Launch</a></p>',
        )
        text = replace_required(
            text,
            "<p class=\"small\">Routine pages age well because players revisit them after each reset and update cycle.</p>",
            "<p class=\"small\">Routine and mistake pages age well because players revisit them after resets, patch changes, and banner cycles.</p>",
        )
        text = replace_required(text, "<h2>New Exploration and Growth Pages</h2>", "<h2>Performance and Build Pages</h2>")
        text = replace_required(
            text,
            '<p><a href="/systems/open-world-exploration/">Open World Exploration</a> · <a href="/systems/co-op-and-party-play/">Co-Op and Party Play</a> · <a href="/systems/mounts-and-fast-travel/">Mounts and Fast Travel</a> · <a href="/systems/day-night-and-weather/">Day Night and Weather</a> · <a href="/systems/progression-and-upgrades/">Progression and Upgrades</a> · <a href="/beginner-guide/leveling-fast/">How to Level Fast</a></p>',
            '<p><a href="/mobile-performance-settings/">Mobile Performance Settings</a> · <a href="/steam-controller-not-working/">Steam Controller Not Working</a> · <a href="/crash-on-launch-fix/">Crash on Launch Fix</a> · <a href="/best-team-for-beginners-may-2026/">Best Team for Beginners</a> · <a href="/best-f2p-team-may-2026/">Best F2P Team</a></p>',
        )
        text = replace_required(
            text,
            "<p class=\"small\">These pages give the site stronger evergreen coverage around exploration, multiplayer, travel, and account-growth intent.</p>",
            "<p class=\"small\">These pages push the site toward current-player searches: settings, controller friction, crashes, and roster decisions after launch.</p>",
        )
    else:
        text = replace_required(
            text,
            "<title>七大罪：Origin 攻略、新闻、发售时间中文站</title>",
            "<title>七大罪：Origin 攻略站：当前卡池、强度榜、配队与新闻</title>",
        )
        text = replace_required(
            text,
            'content="七大罪：Origin 中文站，整理发售时间、预注册、角色、强度榜、系统说明与官方新闻更新。"',
            'content="七大罪：Origin 中文站，整理当前卡池、强度榜、最佳配队、钻石获取、排错与官方新闻更新。"',
        )
        text = replace_required(
            text,
            "<h1>七大罪：Origin 攻略、新闻与发售时间导航</h1>",
            "<h1>七大罪：Origin 当前卡池、强度榜、配队与新闻导航</h1>",
        )
        text = replace_required(
            text,
            """<p class="lead">
            <strong>七大罪：Origin</strong> 是以不列颠尼亚为舞台的开放世界 RPG。本站围绕发售时间、预注册、官方新闻、角色定位、强度榜变化、
            新手系统与开服准备路线整理内容，方便你快速找到真正需要的页面，而不是在零散资讯里反复查找。
          </p>""",
            """<p class="lead">
            <strong>七大罪：Origin</strong> 现在已经进入上线后阶段，所以首页更应该先解决现役玩家问题：
            当前卡池值不值得抽、现在该养谁、怎么更快攒钻石、上线后最容易犯哪些错，以及遇到闪退、移动端卡顿、手柄支持异常时该先开哪一页。
          </p>""",
        )
        text = replace_required(
            text,
            """<div class="container status-strip" data-reveal style="--delay: .04s;">
        <a class="status-card" href="/zh/release-date/"><span>发售时间</span><strong>窗口追踪</strong></a>
        <a class="status-card" href="/zh/pre-register/"><span>预注册</span><strong>流程与奖励</strong></a>
        <a class="status-card" href="/zh/characters/"><span>角色定位</span><strong>配队参考</strong></a>
        <a class="status-card" href="/zh/events-schedule/"><span>活动节奏</span><strong>时间与奖励</strong></a>
      </div>""",
            """<div class="container status-strip" data-reveal style="--delay: .04s;">
        <a class="status-card" href="/zh/banners/current/"><span>当前卡池</span><strong>抽卡判断</strong></a>
        <a class="status-card" href="/zh/tier-list/"><span>当前强度榜</span><strong>培养优先级</strong></a>
        <a class="status-card" href="/zh/how-to-farm-diamonds-fast/"><span>快速攒钻石</span><strong>高价值来源</strong></a>
        <a class="status-card" href="/zh/news/2026/04/patchnotes-1-1-here/"><span>补丁说明</span><strong>1.1 版本</strong></a>
      </div>""",
        )
        text = replace_required(text, "<h2>推荐入口分区</h2>", "<h2>上线后推荐入口分区</h2>")
        text = replace_required(
            text,
            "<p>不要把所有内容混成一串链接。按问题分区后，用户和爬虫都更容易理解这个站每块内容的职责。</p>",
            "<p>不要再把首页主要精力放在预热词上。按“当前卡池、当前强度、成长循环、排错设置”分区后，更符合上线后的真实搜索需求。</p>",
        )
        text = sub_required(
            r'<div class="route-grid">.*?</div>\s*</div>\s*</section>',
            """<div class="route-grid">
          <article class="card route-card" data-reveal style="--delay: .05s;">
            <h3>当前 Meta 路线</h3>
            <p>如果你真正想知道的是现在该养谁、哪些角色最稳，就先走这组。</p>
            <ul class="route-links">
              <li><a href="/zh/current-tier-list-may-2026/">当前强度榜（2026 年 5 月）</a></li>
              <li><a href="/zh/best-team-for-beginners-may-2026/">当前最佳开荒队伍</a></li>
              <li><a href="/zh/best-f2p-team-may-2026/">当前最佳 F2P 队伍</a></li>
              <li><a href="/zh/tier-list/">强度榜入口</a></li>
              <li><a href="/zh/characters/">角色总览</a></li>
            </ul>
            <p class="route-note">适合在资源有限时决定先养谁的人。</p>
          </article>
          <article class="card route-card" data-reveal style="--delay: .1s;">
            <h3>卡池与钻石路线</h3>
            <p>如果核心问题是“现在值不值得抽”“要不要继续存石”，先看这里。</p>
            <ul class="route-links">
              <li><a href="/zh/current-banner-worth-it/">当前卡池值不值得抽</a></li>
              <li><a href="/zh/next-banner-should-you-save/">下个卡池该不该存</a></li>
              <li><a href="/zh/how-to-farm-diamonds-fast/">快速攒钻石</a></li>
              <li><a href="/zh/best-use-of-diamonds/">钻石最值得花在哪</a></li>
              <li><a href="/zh/currency-guide/">货币与资源指南</a></li>
            </ul>
            <p class="route-note">适合想保住资源、避免短视抽卡的人。</p>
          </article>
          <article class="card route-card" data-reveal style="--delay: .15s;">
            <h3>成长循环路线</h3>
            <p>如果账号一直在动，但节奏总感觉乱，就先看这组。</p>
            <ul class="route-links">
              <li><a href="/zh/daily-checklist/">日常清单</a></li>
              <li><a href="/zh/weekly-checklist/">周常清单</a></li>
              <li><a href="/zh/launch-day-checklist/">上线日清单</a></li>
              <li><a href="/zh/top-10-beginner-mistakes-after-launch/">上线后最常见 10 个新手错误</a></li>
              <li><a href="/zh/beginner-guide/">新手攻略</a></li>
            </ul>
            <p class="route-note">适合想把第一周和第一个月路线走顺的人。</p>
          </article>
          <article class="card route-card" data-reveal style="--delay: .2s;">
            <h3>排错与设置路线</h3>
            <p>如果游戏运行不稳、手柄异常、手机发热或闪退，就先开这些页。</p>
            <ul class="route-links">
              <li><a href="/zh/crash-on-launch-fix/">启动闪退怎么修</a></li>
              <li><a href="/zh/mobile-performance-settings/">手机端性能设置</a></li>
              <li><a href="/zh/steam-controller-not-working/">Steam 手柄不工作怎么办</a></li>
              <li><a href="/zh/best-settings/">最佳设置</a></li>
              <li><a href="/zh/bugs-errors/">Bugs 与报错总览</a></li>
            </ul>
            <p class="route-note">适合先把运行问题解决，再谈卡池和配队的人。</p>
          </article>
        </div>
      </div>
    </section>""",
            text,
        )
        text = replace_required(text, "<h2>新增奖励页</h2>", "<h2>当前决策页面</h2>")
        text = replace_required(
            text,
            '<p><a href="/zh/codes/">兑换码追踪</a> · <a href="/zh/twitch-drops/">Twitch Drops</a> · <a href="/zh/events-schedule/">活动日程</a></p>',
            '<p><a href="/zh/current-banner-worth-it/">当前卡池值不值得抽</a> · <a href="/zh/next-banner-should-you-save/">下个卡池该不该存</a> · <a href="/zh/save-summons-or-pull-now/">现在该抽还是继续存</a></p>',
        )
        text = replace_required(
            text,
            "<p class=\"small\">这组页面更偏上线周和活动周奖励意图，能补足中文侧的奖励相关搜索词。</p>",
            "<p class=\"small\">这些页面承接的是上线后真实存在的抽卡与资源决策搜索，而不是已经开始衰减的预热词。</p>",
        )
        text = replace_required(text, "<h2>新增日程页</h2>", "<h2>成长与循环页面</h2>")
        text = replace_required(
            text,
            '<p><a href="/zh/daily-checklist/">日常清单</a> · <a href="/zh/weekly-checklist/">周常清单</a> · <a href="/zh/all-achievements/">成就总览</a></p>',
            '<p><a href="/zh/daily-checklist/">日常清单</a> · <a href="/zh/weekly-checklist/">周常清单</a> · <a href="/zh/top-10-beginner-mistakes-after-launch/">上线后最常见 10 个新手错误</a></p>',
        )
        text = replace_required(
            text,
            "<p class=\"small\">日周常页更适合承接重复搜索和长期回访流量。</p>",
            "<p class=\"small\">日常、周常和错误页更耐用，因为玩家会在每次重置、版本更新和资源紧张时反复回来查。</p>",
        )
        text = replace_required(text, "<h2>新增探索与成长页</h2>", "<h2>性能与配队页面</h2>")
        text = replace_required(
            text,
            '<p><a href="/zh/systems/open-world-exploration/">开放世界探索</a> · <a href="/zh/systems/co-op-and-party-play/">联机与队伍协作</a> · <a href="/zh/systems/mounts-and-fast-travel/">坐骑与快速移动</a> · <a href="/zh/systems/day-night-and-weather/">昼夜与天气</a> · <a href="/zh/systems/progression-and-upgrades/">成长与强化系统</a> · <a href="/zh/beginner-guide/leveling-fast/">快速升级路线</a></p>',
            '<p><a href="/zh/mobile-performance-settings/">手机端性能设置</a> · <a href="/zh/steam-controller-not-working/">Steam 手柄不工作怎么办</a> · <a href="/zh/crash-on-launch-fix/">启动闪退怎么修</a> · <a href="/zh/best-team-for-beginners-may-2026/">当前最佳开荒队伍</a> · <a href="/zh/best-f2p-team-may-2026/">当前最佳 F2P 队伍</a></p>',
        )
        text = replace_required(
            text,
            "<p class=\"small\">这组页面补上探索、联机、成长三条主线，让中文侧的中层搜索词更完整。</p>",
            "<p class=\"small\">这些页面更贴近上线后的真实搜索：性能、手柄、闪退，以及当前配队与成长决策。</p>",
        )
    write(path, text)


def update_hub_pages() -> None:
    # EN
    path = ROOT / "tier-list/index.html"
    text = read(path)
    text = replace_required(text, "<title>Seven Deadly Sins Origin Tier List (Early Meta)</title>", "<title>Current Tier List and Build Priorities | Seven Deadly Sins Origin</title>")
    text = replace_required(text, 'content="Early meta tier list for Seven Deadly Sins Origin with practical role tiers and pull-priority notes."', 'content="Current tier list and build priorities for Seven Deadly Sins Origin with who to build first, who is slipping, and what changes after launch."')
    text = replace_required(text, "<h1>7DS Origin Tier List (Early Build)</h1>", "<h1>7DS Origin Current Tier List and Build Priorities</h1>")
    text = replace_required(text, "Use this page as a launch-prep tier list, not a final balance verdict. The goal is to explain how we sort carries, supports, and utility picks before the live meta fully settles.", "Use this page as the current-build hub, not a frozen launch snapshot. The goal is to explain who deserves scarce materials first, which roles are safest after launch, and which pages to open when a banner or patch changes your short list.")
    text = replace_required(text, "This page is built for launch planning. We rank characters by account value, role flexibility, setup cost, and how safely they fit into early teams. A strong pick is not just damage; it is also consistency, support value, and how easy it is to build around.", "This page is built for the current live-account phase. We rank characters by account value, role flexibility, setup cost, and how safely they fit into actual post-launch teams. A strong pick is not just damage; it is also consistency, support value, and how easy it is to finish the team around them.")
    text = replace_required(text, "Last reviewed: April 9, 2026.", "Last reviewed: May 8, 2026.")
    text = replace_required(text, '<a class="status-card" href="/news/"><span>Meta Changes</span><strong>Patch News</strong></a>', '<a class="status-card" href="/current-tier-list-may-2026/"><span>Current Snapshot</span><strong>May 2026 Tier View</strong></a>')
    text = replace_required(text, '<p><a href="/characters/">Characters</a> · <a href="/characters/diane/">Diane Guide</a> · <a href="/characters/king/">King Guide</a> · <a href="/characters/tristan/">Tristan Guide</a> · <a href="/characters/elaine/">Elaine Guide</a> · <a href="/characters/meliodas/">Meliodas Guide</a> · <a href="/beginner-guide/best-team-comps/">Best Team Comps</a> · <a href="/beginner-guide/party-setup-tips/">Party Setup Tips</a> · <a href="/beginner-guide/equipment/">SSR Equipment Guide</a> · <a href="/news/">News</a></p>', '<p><a href="/current-tier-list-may-2026/">Current Tier List (May 2026)</a> · <a href="/best-team-for-beginners-may-2026/">Best Team for Beginners</a> · <a href="/best-f2p-team-may-2026/">Best F2P Team</a> · <a href="/characters/">Characters</a> · <a href="/beginner-guide/best-team-comps/">Best Team Comps</a> · <a href="/news/2026/04/patchnotes-1-1-here/">Patch 1.1 Notes</a></p>')
    write(path, text)

    path = ROOT / "banners/current/index.html"
    text = read(path)
    text = replace_required(text, "<h1>Current Banners</h1>", "<h1>Current Banner Tracker and Pull Decision Guide</h1>")
    text = replace_required(text, "This page should answer one thing fast: what banner is active right now, what type of player benefits from it, and what page you should open next before committing pulls.", "This page should answer the live-service question fast: what banner is active right now, who actually benefits, whether it is worth spending on, and which page should settle the decision before you commit pulls.")
    text = replace_required(text, "At the moment, treat current-banner coverage as a live tracker page. When a banner is confirmed, this page should summarize the featured unit, who benefits, and whether the account value is immediate or conditional.", "Treat current-banner coverage as a decision page, not just a tracker. When a banner is confirmed, this page should summarize the featured unit, who benefits, whether the value is immediate or conditional, and when saving is the stronger move.")
    text = replace_required(text, '<p><a href="/banners/">Banners Hub</a> · <a href="/banners/upcoming/">Upcoming Banners</a> · <a href="/tier-list/">Tier List</a> · <a href="/characters/elaine/">Elaine Guide</a> · <a href="/characters/meliodas/">Meliodas Guide</a></p>', '<p><a href="/current-banner-worth-it/">Is the Current Banner Worth It?</a> · <a href="/next-banner-should-you-save/">Next Banner: Should You Save?</a> · <a href="/save-summons-or-pull-now/">Save Summons or Pull Now?</a> · <a href="/tier-list/">Tier List</a> · <a href="/how-to-farm-diamonds-fast/">How to Farm Diamonds Fast</a></p>')
    write(path, text)

    path = ROOT / "currency-guide/index.html"
    text = read(path)
    text = replace_required(text, "<h1>Currency Guide</h1>", "<h1>Current Currency Guide and Spending Priorities</h1>")
    text = replace_required(text, "Currency pages matter because most early account mistakes are spending mistakes. The useful version of this page separates scarce pull currency from progression currency and reminds players that not every resource shortage should be fixed the same way.", "Currency pages matter because most post-launch account mistakes are spending mistakes. The useful version of this page separates scarce pull currency from progression currency and points players toward the fastest realistic diamond and shop decisions.")
    text = replace_required(text, '<p><a href="/how-to-get-more-diamonds/">How to Get More Diamonds</a> · <a href="/best-use-of-diamonds/">Best Use of Diamonds</a> · <a href="/what-to-buy-in-shop/">What to Buy in Shop</a> · <a href="/best-banner-to-pull/">Best Banner to Pull On</a> · <a href="/beginner-guide/">Beginner Guide</a></p>', '<p><a href="/how-to-farm-diamonds-fast/">How to Farm Diamonds Fast</a> · <a href="/how-to-get-more-diamonds/">How to Get More Diamonds</a> · <a href="/best-use-of-diamonds/">Best Use of Diamonds</a> · <a href="/what-to-buy-in-shop/">What to Buy in Shop</a> · <a href="/current-banner-worth-it/">Current Banner Worth It?</a></p>')
    write(path, text)

    path = ROOT / "beginner-guide/index.html"
    text = read(path)
    text = replace_required(text, '<a class="status-card" href="/pre-register/"><span>Before Launch</span><strong>Pre-Register Checklist</strong></a>', '<a class="status-card" href="/launch-day-checklist/"><span>Current Launch Loop</span><strong>Launch Day Checklist</strong></a>')
    text = replace_required(text, '<li><a href="/pre-register/">Pre-Register</a></li>', '<li><a href="/launch-day-checklist/">Launch Day Checklist</a></li>')
    text = replace_required(text, '<p><a href="/f2p-beginner-guide/">F2P Beginner Guide</a></p>', '<p><a href="/best-team-for-beginners-may-2026/">Best Team for Beginners (May 2026)</a></p><p><a href="/best-f2p-team-may-2026/">Best F2P Team (May 2026)</a></p><p><a href="/f2p-beginner-guide/">F2P Beginner Guide</a></p>')
    text = replace_required(text, '<p><a href="/beginner-mistakes/">Beginner Mistakes Guide</a></p>', '<p><a href="/top-10-beginner-mistakes-after-launch/">Top 10 Beginner Mistakes After Launch</a></p><p><a href="/beginner-mistakes/">Beginner Mistakes Guide</a></p>')
    text = replace_required(text, '<p><a href="/currency-guide/">Currency Guide</a></p><p><a href="/how-to-get-stronger/">How to Get Stronger</a></p><p><a href="/best-beginner-team/">Best Beginner Team</a></p>', '<p><a href="/currency-guide/">Currency Guide</a></p><p><a href="/how-to-get-stronger/">How to Get Stronger</a></p><p><a href="/best-beginner-team/">Best Beginner Team</a></p><p><a href="/how-to-farm-diamonds-fast/">How to Farm Diamonds Fast</a></p>')
    text = replace_required(text, '<p><a href="/tier-list/">Tier List</a> · <a href="/characters/">Characters</a> · <a href="/current-characters/">Current Characters</a> · <a href="/upcoming-characters/">Upcoming Characters</a> · <a href="/best-beginner-team/">Best Beginner Team</a> · <a href="/best-team-by-element/">Best Team by Element</a> · <a href="/currency-guide/">Currency Guide</a> · <a href="/how-to-get-stronger/">How to Get Stronger</a> · <a href="/beginner-guide/leveling-fast/">How to Level Fast</a> · <a href="/beginner-guide/material-farming/">Material Farming</a> · <a href="/beginner-guide/weapon-upgrade/">Weapon Upgrade</a> · <a href="/beginner-guide/story-progression/">Story Progression</a> · <a href="/beginner-guide/free-rewards/">Free Rewards</a> · <a href="/daily-checklist/">Daily Checklist</a> · <a href="/weekly-checklist/">Weekly Checklist</a> · <a href="/beginner-guide/cooking/">Cooking Guide</a> · <a href="/beginner-guide/fishing/">Fishing Guide</a> · <a href="/reroll-or-not/">Reroll or Not?</a> · <a href="/news/">News</a> · <a href="/beginner-guide/best-team-comps/">Best Team Comps</a></p>', '<p><a href="/current-tier-list-may-2026/">Current Tier List (May 2026)</a> · <a href="/best-team-for-beginners-may-2026/">Best Team for Beginners</a> · <a href="/best-f2p-team-may-2026/">Best F2P Team</a> · <a href="/top-10-beginner-mistakes-after-launch/">Top 10 Beginner Mistakes After Launch</a> · <a href="/how-to-farm-diamonds-fast/">How to Farm Diamonds Fast</a> · <a href="/daily-checklist/">Daily Checklist</a> · <a href="/weekly-checklist/">Weekly Checklist</a> · <a href="/currency-guide/">Currency Guide</a> · <a href="/news/">News</a></p>')
    write(path, text)

    path = ROOT / "bugs-errors/index.html"
    text = read(path)
    text = replace_required(text, '<p><a href="/systems/controller-support/">Controller Support</a> · <a href="/is-there-controller-support/">Is There Controller Support?</a> · <a href="/how-to-link-accounts/">How to Link Accounts</a> · <a href="/install-failed/">Install Failed</a> · <a href="/login-failed/">Login Failed</a> · <a href="/update-failed/">Update Failed</a></p>', '<p><a href="/crash-on-launch-fix/">Crash on Launch Fix</a> · <a href="/mobile-performance-settings/">Mobile Performance Settings</a> · <a href="/steam-controller-not-working/">Steam Controller Not Working</a> · <a href="/systems/controller-support/">Controller Support</a> · <a href="/install-failed/">Install Failed</a> · <a href="/update-failed/">Update Failed</a></p>')
    text = replace_required(text, '<p><a href="/systems/controller-support/">Controller Support</a> · <a href="/how-to-link-accounts/">How to Link Accounts</a> · <a href="/pre-register/">Pre-Register</a> · <a href="/release-date/">Release Date</a></p>', '<p><a href="/crash-on-launch-fix/">Crash on Launch Fix</a> · <a href="/mobile-performance-settings/">Mobile Performance Settings</a> · <a href="/steam-controller-not-working/">Steam Controller Not Working</a> · <a href="/systems/controller-support/">Controller Support</a></p>')
    write(path, text)

    # ZH
    path = ROOT / "zh/tier-list/index.html"
    text = read(path)
    text = replace_required(text, "<title>七大罪 Origin 强度榜（前期参考）</title>", "<title>七大罪 Origin 当前强度榜与培养优先级</title>")
    text = replace_required(text, "七大罪 Origin 开服前期强度榜，结合账号价值、队伍适配面与资源优先级做参考。", "七大罪 Origin 当前强度榜与培养优先级，帮助你判断上线后现在最值得先养谁、哪些角色可以后放。")
    text = replace_required(text, "<h1>七大罪 Origin 强度榜（前期参考）</h1>", "<h1>七大罪 Origin 当前强度榜与培养优先级</h1>")
    text = replace_required(text, "这页更适合拿来做开服前的资源优先级判断，而不是给每个角色下最终判决。重点是看谁适合先投、谁更依赖体系、谁更值得和配队页联动一起看。", "这页现在更适合当成当前版本入口，而不是停留在开服前判断。重点是看上线后资源应该先投给谁、哪些角色更适合现阶段账号、哪些需要和卡池页一起联动看。")
    text = replace_required(text, "<p>我们优先看账号价值、队伍适配面、培养成本和前期稳定性。高位角色不只是输出强，还要能在资源紧张时更容易兑现价值。</p>", "<p>我们优先看账号价值、队伍适配面、培养成本和上线后稳定性。高位角色不只是输出强，还要在资源紧张时更容易兑现价值。</p>")
    text = replace_required(text, "<p>2026 年 4 月 9 日。等更多版本调整和实战数据公开后，这页会继续补厚。</p>", "<p>2026 年 5 月 8 日。现在优先看当前角色、当前配队和补丁变化，而不是沿用开服前判断。</p>")
    text = replace_required(text, '<a class="status-card" href="/zh/news/"><span>版本变化</span><strong>新闻</strong></a>', '<a class="status-card" href="/zh/current-tier-list-may-2026/"><span>当前快照</span><strong>2026 年 5 月版</strong></a>')
    text = replace_required(text, '<p><a href="/zh/characters/">角色总览</a> · <a href="/zh/characters/diane/">Diane 指南</a> · <a href="/zh/characters/king/">King 指南</a> · <a href="/zh/characters/tristan/">Tristan 指南</a> · <a href="/zh/characters/elaine/">Elaine 指南</a> · <a href="/zh/characters/meliodas/">Meliodas 指南</a> · <a href="/zh/beginner-guide/best-team-comps/">最佳团队配置</a></p>', '<p><a href="/zh/current-tier-list-may-2026/">当前强度榜（2026 年 5 月）</a> · <a href="/zh/best-team-for-beginners-may-2026/">当前最佳开荒队伍</a> · <a href="/zh/best-f2p-team-may-2026/">当前最佳 F2P 队伍</a> · <a href="/zh/characters/">角色总览</a> · <a href="/zh/beginner-guide/best-team-comps/">最佳团队配置</a> · <a href="/zh/news/2026/04/patchnotes-1-1-here/">1.1 补丁说明</a></p>')
    write(path, text)

    path = ROOT / "zh/banners/current/index.html"
    text = read(path)
    text = replace_required(text, "<h1>当前卡池</h1>", "<h1>当前卡池追踪与抽卡判断</h1>")
    text = replace_required(text, "这页要解决的核心问题很简单：现在开的池子是什么，适合谁抽，抽之前还应该先看哪些页面。", "这页要解决的不是“现在开什么池”这么简单，而是：现在这个池值不值得抽、适合什么账号、抽之前还要先看哪些页才能避免短视决策。")
    text = replace_required(text, "在正式卡池细节完全落地前，这页更适合作为实时追踪页。等官方确认后，应第一时间补充角色定位、适用账号和要不要立刻抽的判断。", "把当前卡池页当成决策页，而不只是追踪页。等官方确认后，应第一时间补角色定位、适用账号、是否能立刻补洞，以及什么时候存石更稳。")
    text = replace_required(text, '<p><a href="/zh/banners/">卡池总览</a> · <a href="/zh/banners/upcoming/">后续卡池</a> · <a href="/zh/tier-list/">强度榜</a> · <a href="/zh/characters/elaine/">Elaine 指南</a> · <a href="/zh/characters/meliodas/">Meliodas 指南</a></p>', '<p><a href="/zh/current-banner-worth-it/">当前卡池值不值得抽</a> · <a href="/zh/next-banner-should-you-save/">下个卡池该不该存</a> · <a href="/zh/save-summons-or-pull-now/">现在该抽还是继续存</a> · <a href="/zh/tier-list/">强度榜</a> · <a href="/zh/how-to-farm-diamonds-fast/">快速攒钻石</a></p>')
    write(path, text)

    path = ROOT / "zh/currency-guide/index.html"
    text = read(path)
    text = replace_required(text, "<h1>货币与资源指南</h1>", "<h1>当前货币与资源使用优先级</h1>")
    text = replace_required(text, "货币页最重要的价值，是帮玩家避免前期因为乱花资源把账号节奏打散。真正要分清的是：哪些资源会影响抽卡弹性，哪些资源会影响主力成长，哪些又是短缺但能补回来的。", "货币页现在最重要的价值，是帮玩家避免上线后因为乱花资源把账号节奏打散。真正要分清的是：哪些资源会影响抽卡弹性，哪些资源会影响当前成长，哪些又应该先用快方法补。")
    text = replace_required(text, '<p><a href="/zh/how-to-get-more-diamonds/">怎么获得更多钻石</a> · <a href="/zh/best-use-of-diamonds/">钻石最值得花在哪</a> · <a href="/zh/what-to-buy-in-shop/">商店里最值得买什么</a> · <a href="/zh/best-banner-to-pull/">现在最值得抽哪个卡池</a> · <a href="/zh/beginner-guide/">新手攻略</a></p>', '<p><a href="/zh/how-to-farm-diamonds-fast/">快速攒钻石</a> · <a href="/zh/how-to-get-more-diamonds/">怎么获得更多钻石</a> · <a href="/zh/best-use-of-diamonds/">钻石最值得花在哪</a> · <a href="/zh/what-to-buy-in-shop/">商店里最值得买什么</a> · <a href="/zh/current-banner-worth-it/">当前卡池值不值得抽</a></p>')
    write(path, text)

    path = ROOT / "zh/beginner-guide/index.html"
    text = read(path)
    text = replace_required(text, '<a class="status-card" href="/zh/pre-register/"><span>开服前</span><strong>预注册清单</strong></a>', '<a class="status-card" href="/zh/launch-day-checklist/"><span>上线后</span><strong>上线日清单</strong></a>')
    text = replace_required(text, '<li><a href="/zh/pre-register/">预注册</a></li>', '<li><a href="/zh/launch-day-checklist/">上线日清单</a></li>')
    text = replace_required(text, '<p><a href="/zh/f2p-beginner-guide/">F2P 新手攻略</a></p>', '<p><a href="/zh/best-team-for-beginners-may-2026/">当前最佳开荒队伍</a></p><p><a href="/zh/best-f2p-team-may-2026/">当前最佳 F2P 队伍</a></p><p><a href="/zh/f2p-beginner-guide/">F2P 新手攻略</a></p>')
    text = replace_required(text, '<p><a href="/zh/beginner-mistakes/">新手常见错误</a></p>', '<p><a href="/zh/top-10-beginner-mistakes-after-launch/">上线后最常见 10 个新手错误</a></p><p><a href="/zh/beginner-mistakes/">新手常见错误</a></p>')
    text = replace_required(text, '<p><a href="/zh/currency-guide/">货币与资源指南</a></p><p><a href="/zh/how-to-get-stronger/">如何快速变强</a></p><p><a href="/zh/best-beginner-team/">最佳开荒队伍</a></p>', '<p><a href="/zh/currency-guide/">货币与资源指南</a></p><p><a href="/zh/how-to-get-stronger/">如何快速变强</a></p><p><a href="/zh/best-beginner-team/">最佳开荒队伍</a></p><p><a href="/zh/how-to-farm-diamonds-fast/">快速攒钻石</a></p>')
    text = replace_required(text, '<p><a href="/zh/tier-list/">强度榜</a> · <a href="/zh/characters/">角色总览</a> · <a href="/zh/current-characters/">当前角色</a> · <a href="/zh/upcoming-characters/">后续角色</a> · <a href="/zh/best-beginner-team/">最佳开荒队伍</a> · <a href="/zh/best-team-by-element/">按属性选最佳队伍</a> · <a href="/zh/currency-guide/">货币与资源指南</a> · <a href="/zh/how-to-get-stronger/">如何快速变强</a> · <a href="/zh/beginner-guide/leveling-fast/">如何快速升级</a> · <a href="/zh/beginner-guide/material-farming/">素材刷取指南</a> · <a href="/zh/beginner-guide/weapon-upgrade/">武器强化指南</a> · <a href="/zh/beginner-guide/story-progression/">主线推进指南</a> · <a href="/zh/beginner-guide/free-rewards/">免费奖励指南</a> · <a href="/zh/daily-checklist/">日常清单</a> · <a href="/zh/weekly-checklist/">周常清单</a> · <a href="/zh/beginner-guide/cooking/">烹饪指南</a> · <a href="/zh/beginner-guide/fishing/">钓鱼指南</a> · <a href="/zh/reroll-or-not/">要不要刷初始</a> · <a href="/zh/news/">新闻</a> · <a href="/zh/beginner-guide/best-team-comps/">最佳团队配置</a></p>', '<p><a href="/zh/current-tier-list-may-2026/">当前强度榜（2026 年 5 月）</a> · <a href="/zh/best-team-for-beginners-may-2026/">当前最佳开荒队伍</a> · <a href="/zh/best-f2p-team-may-2026/">当前最佳 F2P 队伍</a> · <a href="/zh/top-10-beginner-mistakes-after-launch/">上线后最常见 10 个新手错误</a> · <a href="/zh/how-to-farm-diamonds-fast/">快速攒钻石</a> · <a href="/zh/daily-checklist/">日常清单</a> · <a href="/zh/weekly-checklist/">周常清单</a> · <a href="/zh/currency-guide/">货币与资源指南</a> · <a href="/zh/news/">新闻</a></p>')
    write(path, text)

    path = ROOT / "zh/bugs-errors/index.html"
    text = read(path)
    text = replace_required(text, '<p><a href="/zh/systems/controller-support/">手柄支持</a> · <a href="/zh/is-there-controller-support/">有没有手柄支持</a> · <a href="/zh/how-to-link-accounts/">如何绑定账号</a> · <a href="/zh/install-failed/">安装失败</a> · <a href="/zh/login-failed/">登录失败</a> · <a href="/zh/update-failed/">更新失败</a></p>', '<p><a href="/zh/crash-on-launch-fix/">启动闪退怎么修</a> · <a href="/zh/mobile-performance-settings/">手机端性能设置</a> · <a href="/zh/steam-controller-not-working/">Steam 手柄不工作怎么办</a> · <a href="/zh/systems/controller-support/">手柄支持</a> · <a href="/zh/install-failed/">安装失败</a> · <a href="/zh/update-failed/">更新失败</a></p>')
    text = replace_required(text, '<p><a href="/zh/systems/controller-support/">手柄支持</a> · <a href="/zh/how-to-link-accounts/">如何绑定账号</a> · <a href="/zh/pre-register/">预注册</a> · <a href="/zh/release-date/">发售时间</a></p>', '<p><a href="/zh/crash-on-launch-fix/">启动闪退怎么修</a> · <a href="/zh/mobile-performance-settings/">手机端性能设置</a> · <a href="/zh/steam-controller-not-working/">Steam 手柄不工作怎么办</a> · <a href="/zh/systems/controller-support/">手柄支持</a></p>')
    write(path, text)


PAGE_DATA = [
    {
        "slug": "current-tier-list-may-2026",
        "title_en": "Current Tier List May 2026",
        "desc_en": "Current tier list for Seven Deadly Sins Origin in May 2026 with who to build first, who is slipping, and which roles are safest after launch.",
        "h1_en": "Seven Deadly Sins Origin Current Tier List for May 2026",
        "intro_en": "If you need a fast current read, start here: build the units that solve multiple teams, protect scarce upgrades, and stay useful even if the next patch moves numbers slightly.",
        "c1_en": ("Build First", ["Flexible core carries", "Supports that fit more than one real lineup", "Units that are already good before perfect gear"]),
        "c2_en": ("What Can Wait", "High-upside picks that need rare partners, heavy gear, or a more stable roster can usually wait until your first account lane is secure."),
        "c3_en": ("Best Companion Pages", "Open /tier-list/, /best-team-for-beginners-may-2026/, /best-f2p-team-may-2026/, and /news/2026/04/patchnotes-1-1-here/ together when you want the safest current build path."),
        "related_en": [("/tier-list/", "Tier List Hub"), ("/best-team-for-beginners-may-2026/", "Best Team for Beginners"), ("/best-f2p-team-may-2026/", "Best F2P Team"), ("/characters/", "Characters"), ("/news/2026/04/patchnotes-1-1-here/", "Patch 1.1 Notes")],
        "title_zh": "当前强度榜 2026 年 5 月",
        "desc_zh": "七大罪 Origin 2026 年 5 月当前强度榜，帮助你判断现在最该先养谁、哪些角色可以后放。",
        "h1_zh": "七大罪 Origin 当前强度榜（2026 年 5 月）",
        "intro_zh": "如果你需要一个更贴近当前版本的快速判断，这页就是入口：优先养能覆盖多队伍、能保护稀缺资源、就算下个补丁微调也不容易立刻掉队的角色。",
        "c1_zh": ("最该先养谁", ["能覆盖多个队伍路线的核心位", "能进入多套实战阵容的功能辅助", "不用等到完美装备也能兑现价值的角色"]),
        "c2_zh": ("哪些可以后放", "那些需要稀有搭档、重装备投入或更完整 roster 才会发力的高上限角色，通常可以等账号主线稳定后再回头补。"),
        "c3_zh": ("最适合一起看的页面", "想快速形成当前培养路线时，建议把 /zh/tier-list/、/zh/best-team-for-beginners-may-2026/、/zh/best-f2p-team-may-2026/ 和 /zh/news/2026/04/patchnotes-1-1-here/ 一起打开。"),
        "related_zh": [("/zh/tier-list/", "强度榜入口"), ("/zh/best-team-for-beginners-may-2026/", "当前最佳开荒队伍"), ("/zh/best-f2p-team-may-2026/", "当前最佳 F2P 队伍"), ("/zh/characters/", "角色总览"), ("/zh/news/2026/04/patchnotes-1-1-here/", "1.1 补丁说明")],
    },
    {
        "slug": "best-team-for-beginners-may-2026",
        "title_en": "Best Team for Beginners May 2026",
        "desc_en": "Best team for beginners in Seven Deadly Sins Origin for May 2026 with safe first-lineup logic after launch.",
        "h1_en": "Best Team for Beginners in Seven Deadly Sins Origin (May 2026)",
        "intro_en": "The safest beginner team after launch is usually the one you can actually finish, pilot, and keep upgrading without splitting materials across too many experiments.",
        "c1_en": ("What a Safe Starter Team Needs", ["One clear carry path", "Two support slots that are realistic to finish", "Enough stability that mistakes do not instantly end a run"]),
        "c2_en": ("When to Reroute", "If the team you want depends on banner luck, rare pairings, or expensive gear before it feels playable, choose the safer route first and revisit the flashy comp later."),
        "c3_en": ("Best Companion Pages", "Pair this page with /best-beginner-team/, /best-team-by-element/, /current-tier-list-may-2026/, and /currency-guide/ so your first team plan also matches your resource reality."),
        "related_en": [("/best-beginner-team/", "Best Beginner Team"), ("/best-team-by-element/", "Best Team by Element"), ("/currency-guide/", "Currency Guide"), ("/current-tier-list-may-2026/", "Current Tier List")],
        "title_zh": "当前最佳开荒队伍 2026 年 5 月",
        "desc_zh": "七大罪 Origin 2026 年 5 月当前最佳开荒队伍，帮助新手按上线后版本判断最稳的第一队。",
        "h1_zh": "七大罪 Origin 当前最佳开荒队伍（2026 年 5 月）",
        "intro_zh": "上线后最稳的开荒队伍，通常不是纸面最华丽的那一队，而是你真的能成型、能顺手操作、又不会把材料分散到太多实验里的那一队。",
        "c1_zh": ("安全开荒队需要什么", ["明确的一条主 C 路线", "两个现实可成型的辅助位", "足够稳定，失误时不会马上断节奏"]),
        "c2_zh": ("什么时候该换路线", "如果你想走的队伍太依赖卡池运气、稀有搭配或昂贵装备，建议先走更稳的队，再回头补高上限阵容。"),
        "c3_zh": ("最适合一起看的页面", "建议和 /zh/best-beginner-team/、/zh/best-team-by-element/、/zh/current-tier-list-may-2026/、/zh/currency-guide/ 一起看，这样队伍判断才不会脱离资源现实。"),
        "related_zh": [("/zh/best-beginner-team/", "最佳开荒队伍"), ("/zh/best-team-by-element/", "按属性选最佳队伍"), ("/zh/currency-guide/", "货币与资源指南"), ("/zh/current-tier-list-may-2026/", "当前强度榜")],
    },
    {
        "slug": "best-f2p-team-may-2026",
        "title_en": "Best F2P Team May 2026",
        "desc_en": "Best F2P team for Seven Deadly Sins Origin in May 2026 with low-risk build logic after launch.",
        "h1_en": "Best F2P Team in Seven Deadly Sins Origin (May 2026)",
        "intro_en": "A good F2P team is not just cheap. It should survive banner volatility, avoid heavy duplicate pressure, and keep your account flexible for the next big resource decision.",
        "c1_en": ("F2P Team Rules", ["Avoid teams that demand too many banner-exclusive pieces", "Prioritize utility that remains useful across multiple farms and events", "Keep your first team compatible with daily and weekly routines"]),
        "c2_en": ("What Usually Fails", "The weakest F2P plans are the ones that copy whale-level assumptions while lacking the banner depth or gear budget to support them."),
        "c3_en": ("Best Companion Pages", "Use /f2p-beginner-guide/, /how-to-farm-diamonds-fast/, /best-use-of-diamonds/, and /save-summons-or-pull-now/ with this page when your goal is an efficient free-to-play route."),
        "related_en": [("/f2p-beginner-guide/", "F2P Beginner Guide"), ("/how-to-farm-diamonds-fast/", "How to Farm Diamonds Fast"), ("/best-use-of-diamonds/", "Best Use of Diamonds"), ("/save-summons-or-pull-now/", "Save Summons or Pull Now")],
        "title_zh": "当前最佳 F2P 队伍 2026 年 5 月",
        "desc_zh": "七大罪 Origin 2026 年 5 月当前最佳 F2P 队伍，帮助你按上线后版本走更稳的平民路线。",
        "h1_zh": "七大罪 Origin 当前最佳 F2P 队伍（2026 年 5 月）",
        "intro_zh": "好的 F2P 队伍不只是便宜，而是要能扛住卡池波动、不太依赖重复角色，并且让账号在下一次资源决策前仍保有弹性。",
        "c1_zh": ("F2P 队伍的判断规则", ["尽量避免过度依赖限定卡池拼图", "优先考虑在多种 farm 和活动里都能工作的功能位", "保证第一队能兼容日常与周常循环"]),
        "c2_zh": ("最常失败的地方", "很多 F2P 路线会失败，不是因为角色弱，而是因为拿着重氪假设去规划平民账号，结果卡在卡池深度和装备预算上。"),
        "c3_zh": ("最适合一起看的页面", "如果目标是把平民路线走稳，建议和 /zh/f2p-beginner-guide/、/zh/how-to-farm-diamonds-fast/、/zh/best-use-of-diamonds/、/zh/save-summons-or-pull-now/ 一起看。"),
        "related_zh": [("/zh/f2p-beginner-guide/", "F2P 新手攻略"), ("/zh/how-to-farm-diamonds-fast/", "快速攒钻石"), ("/zh/best-use-of-diamonds/", "钻石最值得花在哪"), ("/zh/save-summons-or-pull-now/", "现在该抽还是继续存")],
    },
    {
        "slug": "how-to-farm-diamonds-fast",
        "title_en": "How to Farm Diamonds Fast",
        "desc_en": "How to farm diamonds fast in Seven Deadly Sins Origin with the fastest realistic sources after launch.",
        "h1_en": "How to Farm Diamonds Fast in Seven Deadly Sins Origin",
        "intro_en": "Players searching this phrase usually do not want every possible source. They want the fastest realistic loop that helps them reach the next banner or pity checkpoint without wasting time on low-return tasks.",
        "c1_en": ("Fastest Realistic Sources", ["Launch rewards and time-limited campaigns", "Daily and weekly loops with strong repeat value", "Progression milestones that unlock naturally while making the account stronger"]),
        "c2_en": ("What Is Too Slow", "A source can still be valid and still be too slow to anchor your banner plan. The useful view is speed plus account value, not just whether diamonds technically exist there."),
        "c3_en": ("Best Companion Pages", "Use this with /how-to-get-more-diamonds/, /best-use-of-diamonds/, /current-banner-worth-it/, and /next-banner-should-you-save/ when you want a faster and cleaner pull route."),
        "related_en": [("/how-to-get-more-diamonds/", "How to Get More Diamonds"), ("/best-use-of-diamonds/", "Best Use of Diamonds"), ("/current-banner-worth-it/", "Current Banner Worth It?"), ("/next-banner-should-you-save/", "Next Banner: Should You Save?")],
        "title_zh": "快速攒钻石",
        "desc_zh": "七大罪 Origin 快速攒钻石指南，帮助你判断上线后哪些来源最快、最值得做。",
        "h1_zh": "七大罪 Origin 怎么快速攒钻石",
        "intro_zh": "搜这个词的玩家通常并不想看所有可能来源，而是想知道：在上线后版本里，什么路线最快、最现实，能尽快把你送到下一个抽卡节点或保底节点。",
        "c1_zh": ("最快也最现实的来源", ["上线奖励和限时活动", "高重复价值的日常与周常", "一边推进一边自然解锁的成长节点"]),
        "c2_zh": ("哪些来源太慢", "一个来源即使有效，也可能慢到不适合做你主要抽卡计划的支点。真正有用的判断标准是速度加账号价值，而不是“那里也能拿一点”。"),
        "c3_zh": ("最适合一起看的页面", "想把抽卡路线走得更快更稳，建议和 /zh/how-to-get-more-diamonds/、/zh/best-use-of-diamonds/、/zh/current-banner-worth-it/、/zh/next-banner-should-you-save/ 一起看。"),
        "related_zh": [("/zh/how-to-get-more-diamonds/", "怎么获得更多钻石"), ("/zh/best-use-of-diamonds/", "钻石最值得花在哪"), ("/zh/current-banner-worth-it/", "当前卡池值不值得抽"), ("/zh/next-banner-should-you-save/", "下个卡池该不该存")],
    },
    {
        "slug": "current-banner-worth-it",
        "title_en": "Is the Current Banner Worth It?",
        "desc_en": "Current banner worth it guide for Seven Deadly Sins Origin with a clearer pull-or-save decision path.",
        "h1_en": "Is the Current Banner Worth It in Seven Deadly Sins Origin?",
        "intro_en": "This page exists for the real live-service question: should you spend on the current banner now, or is the smarter move to protect pity, diamonds, and roster flexibility for the next cycle?",
        "c1_en": ("Pull If", ["The unit solves a real role gap", "The account gets immediate value in more than one mode", "Your next banner risk looks lower than your current need"]),
        "c2_en": ("Save If", "If the banner is merely strong on paper, but your account does not urgently need it, saving is often the better play—especially when diamonds and pity are both under pressure."),
        "c3_en": ("Best Companion Pages", "Use /banners/current/, /save-summons-or-pull-now/, /next-banner-should-you-save/, and /currency-guide/ before making a final banner decision."),
        "related_en": [("/banners/current/", "Current Banners"), ("/save-summons-or-pull-now/", "Save Summons or Pull Now"), ("/next-banner-should-you-save/", "Next Banner: Should You Save?"), ("/currency-guide/", "Currency Guide")],
        "title_zh": "当前卡池值不值得抽",
        "desc_zh": "七大罪 Origin 当前卡池值不值得抽的判断页，帮助你分清现在该抽还是更该继续存。",
        "h1_zh": "七大罪 Origin 当前卡池值不值得抽？",
        "intro_zh": "这页就是为真实的 live-service 问题准备的：现在这个池子到底该不该抽，还是应该保护保底、钻石和 roster 弹性，等下一个周期再决定。",
        "c1_zh": ("什么情况可以抽", ["这个角色确实补到了你的队伍缺口", "它能在多个模式里立刻给账号带来价值", "相比当前需求，下个卡池的不确定性更低"]),
        "c2_zh": ("什么情况更该存", "如果这个池子只是纸面上很强，但你的账号现在并不急需，那通常更值得继续存，尤其是当钻石和保底都很吃紧时。"),
        "c3_zh": ("最适合一起看的页面", "在做最终抽卡判断前，建议把 /zh/banners/current/、/zh/save-summons-or-pull-now/、/zh/next-banner-should-you-save/、/zh/currency-guide/ 一起打开。"),
        "related_zh": [("/zh/banners/current/", "当前卡池"), ("/zh/save-summons-or-pull-now/", "现在该抽还是继续存"), ("/zh/next-banner-should-you-save/", "下个卡池该不该存"), ("/zh/currency-guide/", "货币与资源指南")],
    },
    {
        "slug": "next-banner-should-you-save",
        "title_en": "Next Banner: Should You Save?",
        "desc_en": "Next banner should you save guide for Seven Deadly Sins Origin with a practical hold-or-spend framework.",
        "h1_en": "Should You Save for the Next Banner in Seven Deadly Sins Origin?",
        "intro_en": "Saving is only smart when it protects a better target. This page is for players trying to decide whether the next banner is important enough to delay current spending and progression plans.",
        "c1_en": ("Save For the Next Banner If", ["Your current roster already clears your near-term content", "The next unit may solve a more important account weakness", "Your pity and diamond curve become too fragile after one more live pull cycle"]),
        "c2_en": ("Do Not Overwait", "Over-saving can also hurt. If waiting keeps your account weak for too long, you may lose more progression value than you gain from perfect future timing."),
        "c3_en": ("Best Companion Pages", "Use /banners/upcoming/, /current-banner-worth-it/, /save-summons-or-pull-now/, and /how-to-farm-diamonds-fast/ together when you need a realistic save plan."),
        "related_en": [("/banners/upcoming/", "Upcoming Banners"), ("/current-banner-worth-it/", "Current Banner Worth It?"), ("/save-summons-or-pull-now/", "Save Summons or Pull Now"), ("/how-to-farm-diamonds-fast/", "How to Farm Diamonds Fast")],
        "title_zh": "下个卡池该不该存",
        "desc_zh": "七大罪 Origin 下个卡池该不该存的判断页，帮助你平衡当前抽卡和后续资源安排。",
        "h1_zh": "七大罪 Origin 下个卡池该不该提前存？",
        "intro_zh": "存石只有在它保护了更值得的目标时才有意义。这页适合那些正在权衡：为了下个池子，现在是否应该暂缓当前抽卡和成长节奏的人。",
        "c1_zh": ("什么情况该为下个卡池存", ["当前 roster 已经够你打完近期内容", "下个角色更可能补上真正重要的弱点", "再经历一次当前抽卡周期后，保底和钻石会变得太脆弱"]),
        "c2_zh": ("也别过度等待", "一味等下去也会伤账号。如果等待让你太长时间都处在弱势状态，损失的成长价值可能比你理想中的未来 timing 还大。"),
        "c3_zh": ("最适合一起看的页面", "如果你要做更现实的存石计划，建议把 /zh/banners/upcoming/、/zh/current-banner-worth-it/、/zh/save-summons-or-pull-now/、/zh/how-to-farm-diamonds-fast/ 一起看。"),
        "related_zh": [("/zh/banners/upcoming/", "后续卡池"), ("/zh/current-banner-worth-it/", "当前卡池值不值得抽"), ("/zh/save-summons-or-pull-now/", "现在该抽还是继续存"), ("/zh/how-to-farm-diamonds-fast/", "快速攒钻石")],
    },
    {
        "slug": "top-10-beginner-mistakes-after-launch",
        "title_en": "Top 10 Beginner Mistakes After Launch",
        "desc_en": "Top 10 beginner mistakes after launch in Seven Deadly Sins Origin with the errors that hurt growth, pulls, and team progress most.",
        "h1_en": "Top 10 Beginner Mistakes After Launch in Seven Deadly Sins Origin",
        "intro_en": "Post-launch mistakes are usually not dramatic. They are small repeated decisions—bad spending, weak lineup planning, ignored routines—that quietly cut your account efficiency for days.",
        "c1_en": ("Mistakes That Hurt Most", ["Spreading upgrades across too many experiments", "Chasing a current banner without a team plan", "Ignoring daily and weekly loops until resources suddenly feel impossible"]),
        "c2_en": ("How to Recover", "Fix the route, not just the symptom. Most beginner recoveries come from narrowing the account plan, rebuilding the first stable team, and protecting diamonds from panic pulls."),
        "c3_en": ("Best Companion Pages", "Use /beginner-mistakes/, /daily-checklist/, /weekly-checklist/, and /best-team-for-beginners-may-2026/ when you want a cleaner post-launch reset."),
        "related_en": [("/beginner-mistakes/", "Beginner Mistakes Guide"), ("/daily-checklist/", "Daily Checklist"), ("/weekly-checklist/", "Weekly Checklist"), ("/best-team-for-beginners-may-2026/", "Best Team for Beginners")],
        "title_zh": "上线后最常见的 10 个新手错误",
        "desc_zh": "七大罪 Origin 上线后最常见的 10 个新手错误，帮助你识别哪些问题最容易拖慢成长、浪费资源和抽卡计划。",
        "h1_zh": "七大罪 Origin 上线后最常见的 10 个新手错误",
        "intro_zh": "上线后的错误往往不戏剧化，而是一连串重复的小决策：乱花资源、队伍路线模糊、忽视日常循环，最后让账号效率被慢慢磨掉。",
        "c1_zh": ("最伤账号的错误", ["把强化材料分散给太多试验角色", "没有队伍计划就追当前卡池", "忽视日常和周常，直到资源突然断层"]),
        "c2_zh": ("怎么把节奏拉回来", "恢复账号节奏最重要的不是头痛医头，而是重新收窄路线：先把第一队稳定下来，再保护好钻石，避免继续恐慌式抽卡。"),
        "c3_zh": ("最适合一起看的页面", "如果你想把上线后的节奏重新拉顺，建议和 /zh/beginner-mistakes/、/zh/daily-checklist/、/zh/weekly-checklist/、/zh/best-team-for-beginners-may-2026/ 一起看。"),
        "related_zh": [("/zh/beginner-mistakes/", "新手常见错误"), ("/zh/daily-checklist/", "日常清单"), ("/zh/weekly-checklist/", "周常清单"), ("/zh/best-team-for-beginners-may-2026/", "当前最佳开荒队伍")],
    },
    {
        "slug": "crash-on-launch-fix",
        "title_en": "Crash on Launch Fix",
        "desc_en": "Crash on launch fix guide for Seven Deadly Sins Origin with the first checks to run before deeper troubleshooting.",
        "h1_en": "How to Fix Seven Deadly Sins Origin Crash on Launch",
        "intro_en": "Crash-on-launch traffic is high-intent because the player cannot even start. The best version of this page cuts straight to the first checks that remove environment, install, and cache problems before deeper diagnosis.",
        "c1_en": ("First Checks", ["Restart the client and the device before changing account settings", "Confirm install integrity and storage space", "Check whether the issue started after a patch, hotfix, or asset download"]),
        "c2_en": ("What to Avoid", "Do not change too many variables at once. A useful crash fix path isolates install issues, device issues, and account issues instead of mixing all three together."),
        "c3_en": ("Best Companion Pages", "Use /install-failed/, /update-failed/, /mobile-performance-settings/, and /bugs-errors/ if the crash starts after installation, an update, or a device heat problem."),
        "related_en": [("/install-failed/", "Install Failed"), ("/update-failed/", "Update Failed"), ("/mobile-performance-settings/", "Mobile Performance Settings"), ("/bugs-errors/", "Bugs and Errors Hub")],
        "title_zh": "启动闪退怎么修",
        "desc_zh": "七大罪 Origin 启动闪退修复指南，帮助你先排掉最常见的安装、缓存和设备问题。",
        "h1_zh": "七大罪 Origin 启动闪退怎么修",
        "intro_zh": "启动闪退这类搜索的意图非常强，因为玩家连游戏都进不去。最有用的做法，是先把安装、缓存和设备环境问题按顺序排掉，而不是一口气乱改很多项。",
        "c1_zh": ("第一轮先检查什么", ["先重启客户端和设备，再考虑改账号层设置", "确认安装完整性和剩余存储空间", "先判断问题是不是从补丁、热更新或资源下载后开始的"]),
        "c2_zh": ("最该避免什么", "不要一次改太多变量。真正有效的排错，是把安装问题、设备问题和账号问题分开，而不是混在一起改。"),
        "c3_zh": ("最适合一起看的页面", "如果闪退发生在安装、更新或设备过热之后，建议把 /zh/install-failed/、/zh/update-failed/、/zh/mobile-performance-settings/、/zh/bugs-errors/ 一起看。"),
        "related_zh": [("/zh/install-failed/", "安装失败"), ("/zh/update-failed/", "更新失败"), ("/zh/mobile-performance-settings/", "手机端性能设置"), ("/zh/bugs-errors/", "Bugs 与报错总览")],
    },
    {
        "slug": "mobile-performance-settings",
        "title_en": "Mobile Performance Settings",
        "desc_en": "Mobile performance settings for Seven Deadly Sins Origin with what to lower first for heat, battery, and smoother sessions.",
        "h1_en": "Best Mobile Performance Settings for Seven Deadly Sins Origin",
        "intro_en": "Mobile performance pages work because players want a practical compromise: enough frame stability to play well, without turning the device into a heat source or draining battery in one short session.",
        "c1_en": ("What to Lower First", ["Visual quality before control clarity", "Background load and unnecessary effects before core visibility", "Settings that reduce heat spikes during long sessions"]),
        "c2_en": ("Who Should Open This Page", "This page is for mobile-first players, players hitting device heat limits, and anyone whose account routine is being slowed by unstable sessions instead of weak teams."),
        "c3_en": ("Best Companion Pages", "Use /best-settings/, /crash-on-launch-fix/, /steam-controller-not-working/, and /bugs-errors/ if the real issue mixes performance, input, and stability together."),
        "related_en": [("/best-settings/", "Best Settings Guide"), ("/crash-on-launch-fix/", "Crash on Launch Fix"), ("/steam-controller-not-working/", "Steam Controller Not Working"), ("/bugs-errors/", "Bugs and Errors Hub")],
        "title_zh": "手机端性能设置",
        "desc_zh": "七大罪 Origin 手机端性能设置指南，帮助你判断为了发热、续航和稳定性，应该先降哪些选项。",
        "h1_zh": "七大罪 Origin 手机端最佳性能设置",
        "intro_zh": "移动端性能页最有价值的地方，在于帮玩家找到一个现实折中：既有足够稳定的帧数和操作感，又不会把设备很快推到发热和掉电的极限。",
        "c1_zh": ("先降什么最值", ["先降画质，不先牺牲操作清晰度", "先关背景负载和非必要特效", "优先压住长时间游玩时最容易引发热尖峰的设置"]),
        "c2_zh": ("适合谁先看", "这页适合手机端为主的玩家、设备容易发热的玩家，以及那些账号节奏并不是卡在队伍，而是卡在游戏不稳上的人。"),
        "c3_zh": ("最适合一起看的页面", "如果你的问题同时混着性能、输入和稳定性，建议把 /zh/best-settings/、/zh/crash-on-launch-fix/、/zh/steam-controller-not-working/、/zh/bugs-errors/ 一起看。"),
        "related_zh": [("/zh/best-settings/", "最佳设置"), ("/zh/crash-on-launch-fix/", "启动闪退怎么修"), ("/zh/steam-controller-not-working/", "Steam 手柄不工作怎么办"), ("/zh/bugs-errors/", "Bugs 与报错总览")],
    },
    {
        "slug": "steam-controller-not-working",
        "title_en": "Steam Controller Not Working",
        "desc_en": "Steam controller not working fix for Seven Deadly Sins Origin with the first checks that separate support, mapping, and device issues.",
        "h1_en": "Seven Deadly Sins Origin Steam Controller Not Working Fix",
        "intro_en": "Controller-search traffic is practical traffic. Players want to know whether the problem is game support, Steam input mapping, device detection, or an update that changed control behavior.",
        "c1_en": ("First Things to Check", ["Confirm whether the current build supports the controller path you are using", "Check Steam input and mapping conflicts before assuming the game is broken", "Test whether the issue is limited to one device profile or all controller input"]),
        "c2_en": ("Where Players Get Stuck", "The most common mistake is mixing support questions with mapping questions. If the game sees the pad but the layout feels wrong, the fix path is different from a full no-detection failure."),
        "c3_en": ("Best Companion Pages", "Use /systems/controller-support/, /is-there-controller-support/, /best-settings/, and /bugs-errors/ when you want the fastest route from controller confusion to a stable setup."),
        "related_en": [("/systems/controller-support/", "Controller Support"), ("/is-there-controller-support/", "Is There Controller Support?"), ("/best-settings/", "Best Settings Guide"), ("/bugs-errors/", "Bugs and Errors Hub")],
        "title_zh": "Steam 手柄不工作怎么办",
        "desc_zh": "七大罪 Origin Steam 手柄不工作修复指南，帮助你先分清是支持问题、映射问题还是设备识别问题。",
        "h1_zh": "七大罪 Origin Steam 手柄不工作怎么办",
        "intro_zh": "手柄相关搜索都很实用。玩家真正想分清的是：到底是游戏支持问题、Steam Input 映射问题、设备识别问题，还是更新后控制行为变了。",
        "c1_zh": ("第一轮先检查什么", ["先确认当前版本是否支持你现在使用的手柄路径", "先排 Steam Input 和映射冲突，再判断是不是游戏本身有问题", "先测试问题是单一设备 profile 触发，还是所有手柄输入都异常"]),
        "c2_zh": ("最容易卡住的地方", "最常见的错误，是把“支不支持”和“映射不对”混成一个问题。如果游戏能识别手柄但按键布局不对，修法和完全识别不到是不同的。"),
        "c3_zh": ("最适合一起看的页面", "想最快从手柄混乱走到稳定设置，建议把 /zh/systems/controller-support/、/zh/is-there-controller-support/、/zh/best-settings/、/zh/bugs-errors/ 一起看。"),
        "related_zh": [("/zh/systems/controller-support/", "手柄支持"), ("/zh/is-there-controller-support/", "有没有手柄支持"), ("/zh/best-settings/", "最佳设置"), ("/zh/bugs-errors/", "Bugs 与报错总览")],
    },
]


def build_page(lang: str, data: dict) -> str:
    zh = lang == "zh"
    prefix = "/zh" if zh else ""
    home = "/zh/" if zh else "/"
    nav = (
        '<a href="/zh/">首页</a><a href="/zh/seven-deadly-sins-origin/">Origin 总览</a><a href="/zh/release-date/">发售时间</a><a href="/zh/pre-register/">预注册</a><a href="/zh/characters/">角色</a><a href="/zh/tier-list/">强度榜</a><a href="/zh/beginner-guide/">新手攻略</a><a href="/zh/news/">新闻</a><a href="/{slug}/" lang="en">English</a>'
        if zh else
        '<a href="/">Home</a><a href="/seven-deadly-sins-origin/">Origin Hub</a><a href="/release-date/">Release Date</a><a href="/pre-register/">Pre-Register</a><a href="/characters/">Characters</a><a href="/tier-list/">Tier List</a><a href="/beginner-guide/">Beginner Guide</a><a href="/news/">News</a><a href="/zh/{slug}/" lang="zh">中文</a>'
    ).format(slug=data["slug"])
    title = data["title_zh"] if zh else data["title_en"]
    desc = data["desc_zh"] if zh else data["desc_en"]
    h1 = data["h1_zh"] if zh else data["h1_en"]
    intro = data["intro_zh"] if zh else data["intro_en"]
    c1_title, c1_items = data["c1_zh"] if zh else data["c1_en"]
    c2_title, c2_body = data["c2_zh"] if zh else data["c2_en"]
    c3_title, c3_body = data["c3_zh"] if zh else data["c3_en"]
    related = data["related_zh"] if zh else data["related_en"]
    locale = "zh_CN" if zh else "en_US"
    in_lang = "zh-CN" if zh else "en"
    alt_href = f"https://7sinsorigin.com/{data['slug']}/" if zh else f"https://7sinsorigin.com/zh/{data['slug']}/"
    canon = f"https://7sinsorigin.com{prefix}/{data['slug']}/"
    breadcrumb = " / ".join(
        [f'<a href="{home}">{"首页" if zh else "Home"}</a>', h1]
    )
    list_items = "".join(f"<li>{item}</li>" for item in c1_items)
    related_html = " · ".join(f'<a href="{href}">{label}</a>' for href, label in related)
    about_label = "关于" if zh else "About"
    contact_label = "联系" if zh else "Contact"
    menu_label = "菜单" if zh else "Menu"
    small_note = "Current-version page, rewritten for post-launch search intent. Last reviewed: May 8, 2026." if not zh else "当前版本页，按上线后搜索意图重写。最后复核：2026 年 5 月 8 日。"
    return f"""<!doctype html>
<html lang="{in_lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d3f2b">
  <title>{title} | {'七大罪 Origin' if zh else 'Seven Deadly Sins Origin'}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{canon}">
  <link rel="alternate" hreflang="en" href="https://7sinsorigin.com/{data['slug']}/">
  <link rel="alternate" hreflang="zh" href="https://7sinsorigin.com/zh/{data['slug']}/">
  <link rel="alternate" hreflang="x-default" href="https://7sinsorigin.com/{data['slug']}/">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="{locale}">
  <meta property="og:title" content="{title} | {'七大罪 Origin' if zh else 'Seven Deadly Sins Origin'}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon}">
  <meta property="og:site_name" content="7sinsorigin.com">
  <meta property="og:image" content="https://7sinsorigin.com/assets/img/brand/logo-mark.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} | {'七大罪 Origin' if zh else 'Seven Deadly Sins Origin'}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://7sinsorigin.com/assets/img/brand/logo-mark.png">
  <link rel="stylesheet" href="/assets/css/site.css">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/brand/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/img/brand/favicon-16.png">
  <link rel="apple-touch-icon" href="/assets/img/brand/apple-touch-icon.png">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{title} | {'七大罪 Origin' if zh else 'Seven Deadly Sins Origin'}","description":"{desc}","url":"{canon}","inLanguage":"{in_lang}","mainEntityOfPage":"{canon}"}}</script>
</head>
<body>
<header class="site-header"><div class="container nav"><a class="brand" href="{home}"><img class="brand-logo" src="/assets/img/brand/logo-nav.jpg" alt="7sinsorigin.com logo"><span>7sinsorigin.com</span></a><button class="menu-btn" type="button" data-menu-btn>{menu_label}</button><nav class="nav-links">{nav}</nav></div></header>
<main>
  <section class="page-head"><div class="container"><p class="breadcrumb">{breadcrumb}</p><h1>{h1}</h1><p>{intro}</p></div></section>
  <section class="section"><div class="container grid">
    <article class="card"><h2>{c1_title}</h2><ul class="list-clean">{list_items}</ul></article>
    <article class="card"><h2>{c2_title}</h2><p>{c2_body}</p></article>
    <article class="card"><h2>{c3_title}</h2><p>{c3_body}</p><p class="small">{small_note}</p></article>
    <article class="card"><h2>{'相关页面' if zh else 'Related Pages'}</h2><p>{related_html}</p></article>
  </div></section>
</main>
<footer class="footer"><div class="container"><p class="small"><a href="{prefix}/about/">{about_label}</a> | <a href="{prefix}/contact/">{contact_label}</a></p><p class="small">Copyright <span data-year></span> 7sinsorigin.com</p></div></footer>
<script src="/assets/js/site.js"></script>
</body>
</html>
"""


def create_pages() -> None:
    for item in PAGE_DATA:
        write(ROOT / item["slug"] / "index.html", build_page("en", item))
        write(ROOT / "zh" / item["slug"] / "index.html", build_page("zh", item))


def update_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = read(path)
    for item in PAGE_DATA:
        for loc in (
            f"https://7sinsorigin.com/{item['slug']}/",
            f"https://7sinsorigin.com/zh/{item['slug']}/",
        ):
            if loc in text:
                continue
            text = text.replace(
                "</urlset>",
                f'  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>\n</urlset>',
            )
    write(path, text)


def update_memory() -> None:
    for name in ("README.md", "PROJECT-MEMORY.md"):
        path = ROOT / name
        if not path.exists():
            continue
        text = read(path)
        text = re.sub(r"Current page count: \d+", "Current page count: 194", text)
        if "current-tier-list-may-2026" not in text and "post-launch" not in text.lower():
            text += "\n\nPost-launch expansion added on 2026-05-08: current tier list, current banner decision, diamond farming, beginner team, F2P team, post-launch mistakes, and three troubleshooting pages with zh mirrors.\n"
        write(path, text)


def main() -> None:
    update_homepage(ROOT / "index.html", zh=False)
    update_homepage(ROOT / "zh/index.html", zh=True)
    update_hub_pages()
    create_pages()
    update_sitemap()
    update_memory()


if __name__ == "__main__":
    main()
