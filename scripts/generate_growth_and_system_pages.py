#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


PAGES = [
    {
        "en_path": "systems/open-world-exploration/index.html",
        "zh_path": "zh/systems/open-world-exploration/index.html",
        "og_type": "website",
        "en": {
            "crumb_href": "/systems/",
            "crumb_label": "Systems",
            "title": "Open World Exploration Guide | The Seven Deadly Sins: Origin",
            "description": "Open world exploration guide for The Seven Deadly Sins: Origin with map-reading priorities, route planning, gathering logic, and exploration support pages.",
            "h1": "The Seven Deadly Sins: Origin Open World Exploration Guide",
            "intro": "Exploration pages work when they reduce wasted movement. Instead of treating the open world as a sightseeing checklist, the useful approach is to connect routes, gathering, fast travel, story progress, and combat readiness.",
            "cards": [
                ("Why Exploration Matters", "<p>Open-world pages matter because players rarely search them for lore alone. They search them because progression slows down when exploration, gathering, quest order, and travel efficiency stop lining up.</p>"),
                ("Best Early Exploration Loop", "<ul class=\"list-clean\"><li>Open map nodes and route anchors before drifting into side detours</li><li>Pair story pushes with gathering and material collection</li><li>Use region clears to support upgrades instead of treating them as separate chores</li></ul>"),
                ("Best Companion Pages", "<p>Use this page with <a href=\"/systems/mounts-and-fast-travel/\">Mounts and Fast Travel</a>, <a href=\"/beginner-guide/story-progression/\">Story Progression Guide</a>, and <a href=\"/beginner-guide/material-farming/\">Material Farming Guide</a> so exploration supports account growth instead of slowing it down.</p>"),
                ("Related Pages", "<p><a href=\"/systems/mounts-and-fast-travel/\">Mounts and Fast Travel</a> · <a href=\"/systems/day-night-and-weather/\">Day Night and Weather</a> · <a href=\"/beginner-guide/material-farming/\">Material Farming</a> · <a href=\"/beginner-guide/story-progression/\">Story Progression</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/systems/",
            "crumb_label": "系统说明",
            "title": "开放世界探索指南 | 七大罪：Origin 系统说明",
            "description": "七大罪：Origin 开放世界探索指南，整理地图阅读、跑图路线、采集逻辑与探索相关支撑页面。",
            "h1": "七大罪：Origin 开放世界探索指南",
            "intro": "探索页的价值在于减少无效跑图。不要把开放世界只当风景清单，更重要的是把路线、采集、快速旅行、主线推进和战斗准备连成一条可执行的成长路线。",
            "cards": [
                ("为什么探索重要", "<p>大多数玩家搜索探索页，并不是为了看设定说明，而是因为成长速度会被跑图效率、采集路线、任务顺序和移动成本直接拖慢。</p>"),
                ("前期探索路线", "<ul class=\"list-clean\"><li>先开图节点和关键路线锚点，再去做支线绕路</li><li>把主线推进和采集、材料收集绑在一起做</li><li>区域清理要服务升级目标，而不是变成独立杂务</li></ul>"),
                ("适合搭配的页面", "<p>建议和 <a href=\"/zh/systems/mounts-and-fast-travel/\">坐骑与快速旅行</a>、<a href=\"/zh/beginner-guide/story-progression/\">主线推进指南</a>、<a href=\"/zh/beginner-guide/material-farming/\">材料刷取指南</a> 一起看，让探索直接服务账号成长。</p>"),
                ("相关页面", "<p><a href=\"/zh/systems/mounts-and-fast-travel/\">坐骑与快速旅行</a> · <a href=\"/zh/systems/day-night-and-weather/\">昼夜与天气系统</a> · <a href=\"/zh/beginner-guide/material-farming/\">材料刷取</a> · <a href=\"/zh/beginner-guide/story-progression/\">主线推进</a></p>"),
            ],
        },
    },
    {
        "en_path": "systems/co-op-and-party-play/index.html",
        "zh_path": "zh/systems/co-op-and-party-play/index.html",
        "og_type": "website",
        "en": {
            "crumb_href": "/systems/",
            "crumb_label": "Systems",
            "title": "Co-Op and Party Play Guide | The Seven Deadly Sins: Origin",
            "description": "Co-op and party play guide for The Seven Deadly Sins: Origin covering role prep, raid readiness, shared progression expectations, and team support pages.",
            "h1": "The Seven Deadly Sins: Origin Co-Op and Party Play Guide",
            "intro": "Co-op pages matter because multiplayer questions are rarely about one button or one menu. Players want to know what to prepare before joining, which roles translate well into group play, and how to avoid dragging a team run down.",
            "cards": [
                ("What Co-Op Usually Changes", "<ul class=\"list-clean\"><li>Role clarity matters more because weak utility becomes obvious in group content</li><li>Team safety and positioning usually matter more than solo burst habits</li><li>Preparation pages become more important because one underbuilt slot affects the whole party</li></ul>"),
                ("Best Use Case", "<p>Open this page when the question is not whether the game has multiplayer, but what kind of account prep makes co-op feel smoother on day one and during raid-style content.</p>"),
                ("Best Companion Pages", "<p>Pair this guide with <a href=\"/systems/combat/\">Combat System</a>, <a href=\"/beginner-guide/weapon-upgrade/\">Weapon Upgrade Guide</a>, and <a href=\"/beginner-guide/leveling-fast/\">Leveling Fast Guide</a> so team-play expectations stay connected to build readiness.</p>"),
                ("Related Pages", "<p><a href=\"/systems/combat/\">Combat System</a> · <a href=\"/best-beginner-team/\">Best Beginner Team</a> · <a href=\"/beginner-guide/weapon-upgrade/\">Weapon Upgrade</a> · <a href=\"/beginner-guide/leveling-fast/\">Leveling Fast</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/systems/",
            "crumb_label": "系统说明",
            "title": "联机与组队玩法指南 | 七大罪：Origin 系统说明",
            "description": "七大罪：Origin 联机与组队玩法指南，整理角色准备、Raid 适配、多人协作预期与相关队伍页面。",
            "h1": "七大罪：Origin 联机与组队玩法指南",
            "intro": "联机页的重点不是单个按钮怎么点，而是进组前该准备什么、哪些角色定位更适合多人环境，以及怎样避免因为养成不足拖慢整队体验。",
            "cards": [
                ("联机会改变什么", "<ul class=\"list-clean\"><li>角色定位会更重要，因为功能不足在多人内容里更容易暴露</li><li>队伍安全性和站位通常比单人爆发习惯更关键</li><li>准备页的重要性更高，因为一个未养成的位置就会影响整队</li></ul>"),
                ("适合什么时候看", "<p>当你真正关心的是“联机前该准备什么”，而不是“这游戏有没有多人模式”时，就该先看这一页。</p>"),
                ("适合搭配的页面", "<p>建议和 <a href=\"/zh/systems/combat/\">战斗系统</a>、<a href=\"/zh/beginner-guide/weapon-upgrade/\">武器强化指南</a>、<a href=\"/zh/beginner-guide/leveling-fast/\">快速升级指南</a> 一起看，让联机准备和养成节奏保持一致。</p>"),
                ("相关页面", "<p><a href=\"/zh/systems/combat/\">战斗系统</a> · <a href=\"/zh/best-beginner-team/\">最佳开荒队伍</a> · <a href=\"/zh/beginner-guide/weapon-upgrade/\">武器强化</a> · <a href=\"/zh/beginner-guide/leveling-fast/\">快速升级</a></p>"),
            ],
        },
    },
    {
        "en_path": "systems/mounts-and-fast-travel/index.html",
        "zh_path": "zh/systems/mounts-and-fast-travel/index.html",
        "og_type": "website",
        "en": {
            "crumb_href": "/systems/",
            "crumb_label": "Systems",
            "title": "Mounts and Fast Travel Guide | The Seven Deadly Sins: Origin",
            "description": "Mounts and fast travel guide for The Seven Deadly Sins: Origin with travel efficiency priorities, route planning, and how movement systems support exploration and farming.",
            "h1": "The Seven Deadly Sins: Origin Mounts and Fast Travel Guide",
            "intro": "Travel pages matter because movement efficiency decides how much real progress fits into a session. A good mounts and fast travel plan cuts wasted backtracking, supports material routes, and keeps story progress from feeling slower than it should.",
            "cards": [
                ("What Good Travel Planning Solves", "<ul class=\"list-clean\"><li>Less wasted time between quests, gathering loops, and event tasks</li><li>Cleaner exploration routes with fewer repeated detours</li><li>Better pairing between world movement and farming efficiency</li></ul>"),
                ("Best Early Priorities", "<p>Unlock dependable travel anchors early, learn which routes are worth repeating, and avoid over-optimizing scenic loops before the account actually needs high-volume farming.</p>"),
                ("Best Companion Pages", "<p>This page works best with <a href=\"/systems/open-world-exploration/\">Open World Exploration</a>, <a href=\"/beginner-guide/material-farming/\">Material Farming</a>, and <a href=\"/daily-checklist/\">Daily Checklist</a> because movement systems are really about making progression loops shorter.</p>"),
                ("Related Pages", "<p><a href=\"/systems/open-world-exploration/\">Open World Exploration</a> · <a href=\"/beginner-guide/material-farming/\">Material Farming</a> · <a href=\"/daily-checklist/\">Daily Checklist</a> · <a href=\"/beginner-guide/story-progression/\">Story Progression</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/systems/",
            "crumb_label": "系统说明",
            "title": "坐骑与快速旅行指南 | 七大罪：Origin 系统说明",
            "description": "七大罪：Origin 坐骑与快速旅行指南，整理移动效率、路线规划，以及跑图系统如何服务探索与刷图。",
            "h1": "七大罪：Origin 坐骑与快速旅行指南",
            "intro": "移动系统会直接决定一局游戏能推进多少真实进度。好的坐骑和快速旅行规划，可以减少回头路、支撑材料路线，并让主线推进不至于被跑路拖慢。",
            "cards": [
                ("好的移动规划能解决什么", "<ul class=\"list-clean\"><li>减少任务、采集和活动之间的无效移动时间</li><li>让探索路线更干净，少走重复回头路</li><li>让世界移动和刷材料路线更容易配合</li></ul>"),
                ("前期优先级", "<p>先解锁稳定的传送点和关键移动节点，搞清楚哪些路线值得重复，再考虑更细的跑图优化。</p>"),
                ("适合搭配的页面", "<p>建议与 <a href=\"/zh/systems/open-world-exploration/\">开放世界探索</a>、<a href=\"/zh/beginner-guide/material-farming/\">材料刷取指南</a>、<a href=\"/zh/daily-checklist/\">日常清单</a> 一起看，因为移动系统本质上是在缩短成长循环。</p>"),
                ("相关页面", "<p><a href=\"/zh/systems/open-world-exploration/\">开放世界探索</a> · <a href=\"/zh/beginner-guide/material-farming/\">材料刷取</a> · <a href=\"/zh/daily-checklist/\">日常清单</a> · <a href=\"/zh/beginner-guide/story-progression/\">主线推进</a></p>"),
            ],
        },
    },
    {
        "en_path": "systems/day-night-and-weather/index.html",
        "zh_path": "zh/systems/day-night-and-weather/index.html",
        "og_type": "website",
        "en": {
            "crumb_href": "/systems/",
            "crumb_label": "Systems",
            "title": "Day Night and Weather Guide | The Seven Deadly Sins: Origin",
            "description": "Day night and weather guide for The Seven Deadly Sins: Origin with how environment timing can affect exploration rhythm, gathering expectations, and route planning.",
            "h1": "The Seven Deadly Sins: Origin Day Night and Weather Guide",
            "intro": "Environment-system pages matter because timing can change how players read exploration and progression. Even when the effect is indirect, day-night and weather systems shape route choices, gathering comfort, and when some tasks feel more efficient to run.",
            "cards": [
                ("Why This System Matters", "<p>Players search this topic because they are trying to understand whether the world state is cosmetic, practical, or worth planning around. A useful page clarifies how to think about that question without overcomplicating the answer.</p>"),
                ("Best Use Case", "<ul class=\"list-clean\"><li>Pair time-of-day awareness with exploration and gathering runs</li><li>Use world-state changes to improve route reading instead of forcing awkward detours</li><li>Keep environment planning secondary to core progression goals</li></ul>"),
                ("Best Companion Pages", "<p>Open this page together with <a href=\"/systems/open-world-exploration/\">Open World Exploration</a>, <a href=\"/systems/mounts-and-fast-travel/\">Mounts and Fast Travel</a>, and <a href=\"/beginner-guide/material-farming/\">Material Farming</a> to keep environmental timing tied to practical routes.</p>"),
                ("Related Pages", "<p><a href=\"/systems/open-world-exploration/\">Open World Exploration</a> · <a href=\"/systems/mounts-and-fast-travel/\">Mounts and Fast Travel</a> · <a href=\"/beginner-guide/material-farming/\">Material Farming</a> · <a href=\"/events-schedule/\">Events Schedule</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/systems/",
            "crumb_label": "系统说明",
            "title": "昼夜与天气系统指南 | 七大罪：Origin 系统说明",
            "description": "七大罪：Origin 昼夜与天气系统指南，整理环境时间如何影响探索节奏、采集体验与跑图规划。",
            "h1": "七大罪：Origin 昼夜与天气系统指南",
            "intro": "环境系统页的意义在于解释“时间变化和天气变化到底值不值得规划”。即使影响不是硬性门槛，它也会改变探索舒适度、采集体验和路线选择。",
            "cards": [
                ("为什么值得了解", "<p>玩家搜索这个主题，通常是想判断世界状态到底只是外观变化，还是会实际影响探索与成长节奏。实用页应该把这个问题讲清楚，而不是堆设定。</p>"),
                ("适合怎么用", "<ul class=\"list-clean\"><li>把时间变化和探索、采集路线放在一起考虑</li><li>利用环境变化优化路线，而不是强行绕远</li><li>环境规划始终放在主成长目标之后</li></ul>"),
                ("适合搭配的页面", "<p>建议和 <a href=\"/zh/systems/open-world-exploration/\">开放世界探索</a>、<a href=\"/zh/systems/mounts-and-fast-travel/\">坐骑与快速旅行</a>、<a href=\"/zh/beginner-guide/material-farming/\">材料刷取指南</a> 一起看，让环境变化服务实际路线。</p>"),
                ("相关页面", "<p><a href=\"/zh/systems/open-world-exploration/\">开放世界探索</a> · <a href=\"/zh/systems/mounts-and-fast-travel/\">坐骑与快速旅行</a> · <a href=\"/zh/beginner-guide/material-farming/\">材料刷取</a> · <a href=\"/zh/events-schedule/\">活动日程</a></p>"),
            ],
        },
    },
    {
        "en_path": "systems/progression-and-upgrades/index.html",
        "zh_path": "zh/systems/progression-and-upgrades/index.html",
        "og_type": "website",
        "en": {
            "crumb_href": "/systems/",
            "crumb_label": "Systems",
            "title": "Progression and Upgrades Guide | The Seven Deadly Sins: Origin",
            "description": "Progression and upgrades guide for The Seven Deadly Sins: Origin covering account-growth order, upgrade pacing, and how systems pages connect to daily progression.",
            "h1": "The Seven Deadly Sins: Origin Progression and Upgrades Guide",
            "intro": "Progression pages matter because weak accounts usually do not fail from one bad choice. They fail from scattered upgrades. This guide is about upgrade order, system pacing, and keeping roster, gear, and routine decisions pointed in the same direction.",
            "cards": [
                ("What Strong Progression Looks Like", "<ul class=\"list-clean\"><li>One clear account goal at a time instead of many half-built lanes</li><li>Upgrade order that matches current content pressure</li><li>Daily and weekly loops that support long-term roster growth</li></ul>"),
                ("Best Use Case", "<p>Open this page when the account is active but not efficient. If progress feels slow even after playing regularly, the real issue is often upgrade direction rather than playtime.</p>"),
                ("Best Companion Pages", "<p>This guide fits best with <a href=\"/beginner-guide/leveling-fast/\">Leveling Fast</a>, <a href=\"/beginner-guide/weapon-upgrade/\">Weapon Upgrade</a>, <a href=\"/daily-checklist/\">Daily Checklist</a>, and <a href=\"/weekly-checklist/\">Weekly Checklist</a>.</p>"),
                ("Related Pages", "<p><a href=\"/beginner-guide/leveling-fast/\">Leveling Fast</a> · <a href=\"/beginner-guide/weapon-upgrade/\">Weapon Upgrade</a> · <a href=\"/how-to-get-stronger/\">How to Get Stronger</a> · <a href=\"/daily-checklist/\">Daily Checklist</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/systems/",
            "crumb_label": "系统说明",
            "title": "成长与养成系统指南 | 七大罪：Origin 系统说明",
            "description": "七大罪：Origin 成长与养成系统指南，整理账号成长顺序、养成节奏，以及系统页如何连接日常推进。",
            "h1": "七大罪：Origin 成长与养成系统指南",
            "intro": "成长页的重点从来不是某一个错误选择，而是养成方向太分散。这个页面要解决的是升级顺序、系统节奏，以及角色、装备和日常路线如何朝同一个目标推进。",
            "cards": [
                ("什么叫好的成长路线", "<ul class=\"list-clean\"><li>一次只推进一个明确目标，而不是多条半成型路线同时养</li><li>升级顺序要贴合当前内容压力</li><li>日常和周常循环要服务长期养成目标</li></ul>"),
                ("适合什么时候看", "<p>如果账号一直在线但成长效率不高，就该回来看这页。问题通常不在于玩得不够久，而在于养成方向不够集中。</p>"),
                ("适合搭配的页面", "<p>建议和 <a href=\"/zh/beginner-guide/leveling-fast/\">快速升级指南</a>、<a href=\"/zh/beginner-guide/weapon-upgrade/\">武器强化指南</a>、<a href=\"/zh/daily-checklist/\">日常清单</a>、<a href=\"/zh/weekly-checklist/\">周常清单</a> 一起看。</p>"),
                ("相关页面", "<p><a href=\"/zh/beginner-guide/leveling-fast/\">快速升级</a> · <a href=\"/zh/beginner-guide/weapon-upgrade/\">武器强化</a> · <a href=\"/zh/how-to-get-stronger/\">如何快速变强</a> · <a href=\"/zh/daily-checklist/\">日常清单</a></p>"),
            ],
        },
    },
    {
        "en_path": "beginner-guide/leveling-fast/index.html",
        "zh_path": "zh/beginner-guide/leveling-fast/index.html",
        "og_type": "article",
        "en": {
            "crumb_href": "/beginner-guide/",
            "crumb_label": "Beginner Guide",
            "title": "How to Level Fast | The Seven Deadly Sins: Origin Beginner Guide",
            "description": "Leveling fast guide for The Seven Deadly Sins: Origin with early progression order, efficiency priorities, and pages to pair with your leveling route.",
            "h1": "How to Level Fast in The Seven Deadly Sins: Origin",
            "intro": "Leveling pages work best when they stop promising magic shortcuts and start clarifying order of operations. Fast leveling usually comes from better route design, stronger upgrade timing, and fewer wasted side pushes, not from one hidden trick.",
            "cards": [
                ("Best Fast-Leveling Priorities", "<ol class=\"list-clean\"><li>Push the main progression lane before drifting into low-yield side content</li><li>Upgrade one functional team instead of splitting materials</li><li>Use daily and weekly loops to support the same growth target</li></ol>"),
                ("What Slows Leveling Down", "<p>Accounts fall behind when story progress, gear upgrades, and farming routes all point in different directions. The fix is usually not more grind, but a cleaner order of operations.</p>"),
                ("Best Companion Pages", "<p>Use this guide with <a href=\"/beginner-guide/story-progression/\">Story Progression Guide</a>, <a href=\"/systems/progression-and-upgrades/\">Progression and Upgrades</a>, and <a href=\"/daily-checklist/\">Daily Checklist</a> so your leveling path stays efficient after each reset.</p>"),
                ("Related Pages", "<p><a href=\"/beginner-guide/story-progression/\">Story Progression</a> · <a href=\"/systems/progression-and-upgrades/\">Progression and Upgrades</a> · <a href=\"/daily-checklist/\">Daily Checklist</a> · <a href=\"/how-to-get-stronger/\">How to Get Stronger</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/beginner-guide/",
            "crumb_label": "新手攻略",
            "title": "快速升级指南 | 七大罪：Origin 新手攻略",
            "description": "七大罪：Origin 快速升级指南，整理前期推进顺序、效率优先级，以及和升级路线最适合搭配的页面。",
            "h1": "七大罪：Origin 快速升级指南",
            "intro": "升级页真正有用的地方，不是承诺神秘捷径，而是讲清楚顺序。大多数快速升级都来自更合理的路线、更准确的强化时机，以及更少的无效支线消耗。",
            "cards": [
                ("快速升级优先级", "<ol class=\"list-clean\"><li>先推主成长路线，再考虑低收益支线内容</li><li>先养一套能稳定推进的队伍，不要过早分散材料</li><li>让日常和周常都服务同一个成长目标</li></ol>"),
                ("为什么会升级变慢", "<p>主线推进、装备强化和刷图路线如果各走各的，等级成长自然会慢下来。真正要修的是顺序，不一定是强度不够。</p>"),
                ("适合搭配的页面", "<p>建议和 <a href=\"/zh/beginner-guide/story-progression/\">主线推进指南</a>、<a href=\"/zh/systems/progression-and-upgrades/\">成长与养成系统</a>、<a href=\"/zh/daily-checklist/\">日常清单</a> 一起看，让升级路线在每次重置后都保持效率。</p>"),
                ("相关页面", "<p><a href=\"/zh/beginner-guide/story-progression/\">主线推进</a> · <a href=\"/zh/systems/progression-and-upgrades/\">成长与养成系统</a> · <a href=\"/zh/daily-checklist/\">日常清单</a> · <a href=\"/zh/how-to-get-stronger/\">如何快速变强</a></p>"),
            ],
        },
    },
    {
        "en_path": "beginner-guide/material-farming/index.html",
        "zh_path": "zh/beginner-guide/material-farming/index.html",
        "og_type": "article",
        "en": {
            "crumb_href": "/beginner-guide/",
            "crumb_label": "Beginner Guide",
            "title": "Material Farming Guide | The Seven Deadly Sins: Origin Beginner Guide",
            "description": "Material farming guide for The Seven Deadly Sins: Origin with route planning, gathering priorities, and how to connect farming to upgrades instead of wasting runs.",
            "h1": "The Seven Deadly Sins: Origin Material Farming Guide",
            "intro": "Material-farming pages matter because players rarely need more farming in general. They need cleaner routes, better priorities, and a reason to stop farming one thing and move on to the next upgrade target.",
            "cards": [
                ("Best Farming Mindset", "<ul class=\"list-clean\"><li>Farm for the next upgrade breakpoint, not for vague future inventory goals</li><li>Pair world movement with farming instead of doing travel-only sessions</li><li>Keep gathering routes tied to the team or weapon plan you are actively building</li></ul>"),
                ("What This Page Solves", "<p>This page is for players who feel active but still run short on useful materials. The answer is usually route quality, target clarity, and knowing when to stop an inefficient loop.</p>"),
                ("Best Companion Pages", "<p>Pair material farming with <a href=\"/beginner-guide/weapon-upgrade/\">Weapon Upgrade</a>, <a href=\"/systems/mounts-and-fast-travel/\">Mounts and Fast Travel</a>, and <a href=\"/systems/open-world-exploration/\">Open World Exploration</a> to keep gathering connected to real upgrades.</p>"),
                ("Related Pages", "<p><a href=\"/beginner-guide/weapon-upgrade/\">Weapon Upgrade</a> · <a href=\"/systems/mounts-and-fast-travel/\">Mounts and Fast Travel</a> · <a href=\"/systems/open-world-exploration/\">Open World Exploration</a> · <a href=\"/daily-checklist/\">Daily Checklist</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/beginner-guide/",
            "crumb_label": "新手攻略",
            "title": "材料刷取指南 | 七大罪：Origin 新手攻略",
            "description": "七大罪：Origin 材料刷取指南，整理跑图路线、采集优先级，以及如何让刷材料直接服务强化目标。",
            "h1": "七大罪：Origin 材料刷取指南",
            "intro": "材料页真正要解决的问题，不是让你“多刷一点”，而是告诉你该刷什么、刷到什么程度该停，以及怎样让每一轮采集都服务当前的强化目标。",
            "cards": [
                ("刷材料的正确思路", "<ul class=\"list-clean\"><li>围绕下一个强化节点刷，不要为了模糊的未来库存无上限堆材料</li><li>把跑图移动和采集绑在一起做，减少纯跑路局</li><li>材料路线要服务当前正在养的队伍或武器</li></ul>"),
                ("这页解决什么", "<p>如果你已经很勤快，但关键材料还是总缺，问题通常不在于刷得少，而在于路线不干净、目标不清楚，以及停手时机不对。</p>"),
                ("适合搭配的页面", "<p>建议和 <a href=\"/zh/beginner-guide/weapon-upgrade/\">武器强化指南</a>、<a href=\"/zh/systems/mounts-and-fast-travel/\">坐骑与快速旅行</a>、<a href=\"/zh/systems/open-world-exploration/\">开放世界探索</a> 一起看，让采集路线直接服务强化结果。</p>"),
                ("相关页面", "<p><a href=\"/zh/beginner-guide/weapon-upgrade/\">武器强化</a> · <a href=\"/zh/systems/mounts-and-fast-travel/\">坐骑与快速旅行</a> · <a href=\"/zh/systems/open-world-exploration/\">开放世界探索</a> · <a href=\"/zh/daily-checklist/\">日常清单</a></p>"),
            ],
        },
    },
    {
        "en_path": "beginner-guide/weapon-upgrade/index.html",
        "zh_path": "zh/beginner-guide/weapon-upgrade/index.html",
        "og_type": "article",
        "en": {
            "crumb_href": "/beginner-guide/",
            "crumb_label": "Beginner Guide",
            "title": "Weapon Upgrade Guide | The Seven Deadly Sins: Origin Beginner Guide",
            "description": "Weapon upgrade guide for The Seven Deadly Sins: Origin with early upgrade order, material discipline, and how weapon decisions connect to team progression.",
            "h1": "The Seven Deadly Sins: Origin Weapon Upgrade Guide",
            "intro": "Weapon-upgrade pages matter because weapon choices shape damage pacing, material drain, and team stability. A useful guide is not just a chart of upgrades; it explains when to commit and when to hold resources for a better breakpoint.",
            "cards": [
                ("Best Upgrade Logic", "<ul class=\"list-clean\"><li>Prioritize upgrades that support your main carry or core utility role</li><li>Avoid spreading high-value materials across too many experiments</li><li>Check whether the next upgrade meaningfully changes current content performance</li></ul>"),
                ("Common Early Mistake", "<p>The biggest mistake is treating every promising weapon like an immediate investment. Upgrade timing matters more than upgrade excitement when resources are still tight.</p>"),
                ("Best Companion Pages", "<p>This guide works best with <a href=\"/beginner-guide/material-farming/\">Material Farming</a>, <a href=\"/systems/progression-and-upgrades/\">Progression and Upgrades</a>, and <a href=\"/beginner-guide/leveling-fast/\">How to Level Fast</a>.</p>"),
                ("Related Pages", "<p><a href=\"/beginner-guide/material-farming/\">Material Farming</a> · <a href=\"/systems/progression-and-upgrades/\">Progression and Upgrades</a> · <a href=\"/beginner-guide/ssr-weapon-ocr/\">SSR Weapon Guide</a> · <a href=\"/best-team-by-element/\">Best Team by Element</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/beginner-guide/",
            "crumb_label": "新手攻略",
            "title": "武器强化指南 | 七大罪：Origin 新手攻略",
            "description": "七大罪：Origin 武器强化指南，整理前期强化顺序、材料分配纪律，以及武器选择如何影响队伍成长。",
            "h1": "七大罪：Origin 武器强化指南",
            "intro": "武器强化页的意义在于解释“什么时候该强化，什么时候该留”。武器选择会直接影响输出节奏、材料消耗和队伍稳定度，所以不能只看面板，而要看时机。",
            "cards": [
                ("强化逻辑", "<ul class=\"list-clean\"><li>优先强化主力输出或核心功能位要用的武器</li><li>高价值材料不要同时摊给太多试验路线</li><li>先判断下一档强化是否真的能改善当前内容体验</li></ul>"),
                ("常见前期错误", "<p>最常见的错误，是看到有潜力的武器就立刻投入。前期材料紧的时候，强化时机往往比“看起来不错”更重要。</p>"),
                ("适合搭配的页面", "<p>建议和 <a href=\"/zh/beginner-guide/material-farming/\">材料刷取指南</a>、<a href=\"/zh/systems/progression-and-upgrades/\">成长与养成系统</a>、<a href=\"/zh/beginner-guide/leveling-fast/\">快速升级指南</a> 一起看。</p>"),
                ("相关页面", "<p><a href=\"/zh/beginner-guide/material-farming/\">材料刷取</a> · <a href=\"/zh/systems/progression-and-upgrades/\">成长与养成系统</a> · <a href=\"/zh/beginner-guide/ssr-weapon-ocr/\">SSR 武器攻略</a> · <a href=\"/zh/best-team-by-element/\">按属性选最佳队伍</a></p>"),
            ],
        },
    },
    {
        "en_path": "beginner-guide/story-progression/index.html",
        "zh_path": "zh/beginner-guide/story-progression/index.html",
        "og_type": "article",
        "en": {
            "crumb_href": "/beginner-guide/",
            "crumb_label": "Beginner Guide",
            "title": "Story Progression Guide | The Seven Deadly Sins: Origin Beginner Guide",
            "description": "Story progression guide for The Seven Deadly Sins: Origin with early route planning, when to pause for upgrades, and how to keep story progress tied to account growth.",
            "h1": "The Seven Deadly Sins: Origin Story Progression Guide",
            "intro": "Story-progression pages matter because many early accounts lose momentum by stopping at the wrong time. A clean story route should tell you when to keep pushing, when to branch into upgrades, and how to avoid wandering away from the strongest progression lane.",
            "cards": [
                ("Best Story Route Mindset", "<ul class=\"list-clean\"><li>Push story when it still unlocks systems, currencies, or travel benefits</li><li>Pause only when the account has a real combat or upgrade wall</li><li>Use side content to support the next story push, not to replace it</li></ul>"),
                ("What This Page Solves", "<p>This guide is for players who feel busy in the world but are not sure whether they are actually moving the account forward. Good story routing fixes that confusion fast.</p>"),
                ("Best Companion Pages", "<p>Use this page together with <a href=\"/beginner-guide/leveling-fast/\">How to Level Fast</a>, <a href=\"/systems/open-world-exploration/\">Open World Exploration</a>, and <a href=\"/systems/progression-and-upgrades/\">Progression and Upgrades</a>.</p>"),
                ("Related Pages", "<p><a href=\"/beginner-guide/leveling-fast/\">How to Level Fast</a> · <a href=\"/systems/open-world-exploration/\">Open World Exploration</a> · <a href=\"/systems/progression-and-upgrades/\">Progression and Upgrades</a> · <a href=\"/daily-checklist/\">Daily Checklist</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/beginner-guide/",
            "crumb_label": "新手攻略",
            "title": "主线推进指南 | 七大罪：Origin 新手攻略",
            "description": "七大罪：Origin 主线推进指南，整理前期路线安排、什么时候停下来补养成，以及如何让主线推进和账号成长保持一致。",
            "h1": "七大罪：Origin 主线推进指南",
            "intro": "很多前期账号会卡住，不是因为强度不够，而是主线停错了时间。好的主线路线要告诉你什么时候继续推、什么时候该转去补养成，以及怎样避免脱离最强成长主线。",
            "cards": [
                ("主线推进思路", "<ul class=\"list-clean\"><li>当主线还能解锁系统、资源或传送收益时，就继续推</li><li>只有在出现真正的战斗墙或养成墙时才停下来补强</li><li>支线和探索应该服务下一次主线推进，而不是替代主线</li></ul>"),
                ("这页解决什么", "<p>如果你总觉得事情很多，却不确定账号是否真的在前进，这一页就是用来把主线节奏重新整理清楚的。</p>"),
                ("适合搭配的页面", "<p>建议和 <a href=\"/zh/beginner-guide/leveling-fast/\">快速升级指南</a>、<a href=\"/zh/systems/open-world-exploration/\">开放世界探索</a>、<a href=\"/zh/systems/progression-and-upgrades/\">成长与养成系统</a> 一起看。</p>"),
                ("相关页面", "<p><a href=\"/zh/beginner-guide/leveling-fast/\">快速升级</a> · <a href=\"/zh/systems/open-world-exploration/\">开放世界探索</a> · <a href=\"/zh/systems/progression-and-upgrades/\">成长与养成系统</a> · <a href=\"/zh/daily-checklist/\">日常清单</a></p>"),
            ],
        },
    },
    {
        "en_path": "beginner-guide/free-rewards/index.html",
        "zh_path": "zh/beginner-guide/free-rewards/index.html",
        "og_type": "article",
        "en": {
            "crumb_href": "/beginner-guide/",
            "crumb_label": "Beginner Guide",
            "title": "Free Rewards Guide | The Seven Deadly Sins: Origin Beginner Guide",
            "description": "Free rewards guide for The Seven Deadly Sins: Origin with launch-week claims, login checks, event reward logic, and the best pages to pair with reward tracking.",
            "h1": "The Seven Deadly Sins: Origin Free Rewards Guide",
            "intro": "Free-reward pages matter because players do not want a vague promise of freebies. They want a stable way to track login rewards, event claims, codes, drops, and pre-register value without missing easy account progress.",
            "cards": [
                ("What Usually Counts as Free Rewards", "<ul class=\"list-clean\"><li>Pre-register bonuses and launch-week claim windows</li><li>Login rewards, events, and patch-time compensation</li><li>Codes, drops, and other official reward channels worth checking regularly</li></ul>"),
                ("Best Use Case", "<p>Open this guide when the question is not whether rewards exist, but how to keep free rewards tied to a real progression plan instead of treating them like disconnected one-off claims.</p>"),
                ("Best Companion Pages", "<p>This page works best with <a href=\"/codes/\">Codes Tracker</a>, <a href=\"/twitch-drops/\">Twitch Drops</a>, <a href=\"/events-schedule/\">Events Schedule</a>, and <a href=\"/pre-register/\">Pre-Register Guide</a>.</p>"),
                ("Related Pages", "<p><a href=\"/codes/\">Codes Tracker</a> · <a href=\"/twitch-drops/\">Twitch Drops</a> · <a href=\"/events-schedule/\">Events Schedule</a> · <a href=\"/pre-register/\">Pre-Register Guide</a></p>"),
            ],
        },
        "zh": {
            "crumb_href": "/zh/beginner-guide/",
            "crumb_label": "新手攻略",
            "title": "免费奖励指南 | 七大罪：Origin 新手攻略",
            "description": "七大罪：Origin 免费奖励指南，整理开服奖励、登录奖励、活动奖励以及适合搭配的追踪页面。",
            "h1": "七大罪：Origin 免费奖励指南",
            "intro": "免费奖励页要解决的不是“有没有福利”，而是怎样稳定追踪登录奖励、活动奖励、兑换码、Drops 和预注册收益，不漏掉最容易拿到的账号成长资源。",
            "cards": [
                ("哪些算免费奖励", "<ul class=\"list-clean\"><li>预注册奖励和开服领取窗口</li><li>登录奖励、活动奖励与补偿奖励</li><li>兑换码、Drops 和其他值得定期检查的官方福利渠道</li></ul>"),
                ("适合什么时候看", "<p>当你真正关心的是“怎样把免费奖励和账号成长绑在一起”时，就该先看这页，而不是零散去翻不同活动入口。</p>"),
                ("适合搭配的页面", "<p>建议和 <a href=\"/zh/codes/\">兑换码追踪</a>、<a href=\"/zh/twitch-drops/\">Twitch Drops</a>、<a href=\"/zh/events-schedule/\">活动日程</a>、<a href=\"/zh/pre-register/\">预注册指南</a> 一起看。</p>"),
                ("相关页面", "<p><a href=\"/zh/codes/\">兑换码追踪</a> · <a href=\"/zh/twitch-drops/\">Twitch Drops</a> · <a href=\"/zh/events-schedule/\">活动日程</a> · <a href=\"/zh/pre-register/\">预注册指南</a></p>"),
            ],
        },
    },
]


def page_url(path: str) -> str:
    return f"https://7sinsorigin.com/{path.replace('index.html', '')}"


def render_page(page: dict, lang: str) -> str:
    data = page[lang]
    is_zh = lang == "zh"
    current_path = page["zh_path"] if is_zh else page["en_path"]
    current_url = page_url(current_path)
    en_url = page_url(page["en_path"])
    zh_url = page_url(page["zh_path"])
    og_locale = "zh_CN" if is_zh else "en_US"
    html_lang = "zh-CN" if is_zh else "en"
    home_href = "/zh/" if is_zh else "/"
    home_label = "首页" if is_zh else "Home"
    hub_href = "/zh/seven-deadly-sins-origin/" if is_zh else "/seven-deadly-sins-origin/"
    hub_label = "Origin 总览" if is_zh else "Origin Hub"
    release_href = "/zh/release-date/" if is_zh else "/release-date/"
    release_label = "发售时间" if is_zh else "Release Date"
    prereg_href = "/zh/pre-register/" if is_zh else "/pre-register/"
    prereg_label = "预注册" if is_zh else "Pre-Register"
    chars_href = "/zh/characters/" if is_zh else "/characters/"
    chars_label = "角色" if is_zh else "Characters"
    tier_href = "/zh/tier-list/" if is_zh else "/tier-list/"
    tier_label = "强度榜" if is_zh else "Tier List"
    beginner_href = "/zh/beginner-guide/" if is_zh else "/beginner-guide/"
    beginner_label = "新手攻略" if is_zh else "Beginner Guide"
    news_href = "/zh/news/" if is_zh else "/news/"
    news_label = "新闻" if is_zh else "News"
    lang_switch_href = page["en_path"].replace("index.html", "/") if is_zh else page["zh_path"].replace("index.html", "/")
    lang_switch_href = "/" + lang_switch_href.lstrip("/")
    lang_switch_label = "English" if is_zh else "中文"
    about_href = "/zh/about/" if is_zh else "/about/"
    about_label = "关于" if is_zh else "About"
    contact_href = "/zh/contact/" if is_zh else "/contact/"
    contact_label = "联系" if is_zh else "Contact"
    cards_html = "".join(
        f"<article class=\"card\"><h2>{title}</h2>{body}</article>" for title, body in data["cards"]
    )
    return f"""<!doctype html>
<html lang="{html_lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d3f2b">
  <title>{data["title"]}</title>
  <meta name="description" content="{data["description"]}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{current_url}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="zh" href="{zh_url}">
  <link rel="alternate" hreflang="x-default" href="{en_url}">
  <meta property="og:type" content="{page["og_type"]}">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:title" content="{data["title"]}">
  <meta property="og:description" content="{data["description"]}">
  <meta property="og:url" content="{current_url}">
  <meta property="og:site_name" content="7sinsorigin.com">
  <meta property="og:image" content="https://7sinsorigin.com/assets/img/worldview/kingdom-of-liones-home.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{data["title"]}">
  <meta name="twitter:description" content="{data["description"]}">
  <meta name="twitter:image" content="https://7sinsorigin.com/assets/img/worldview/kingdom-of-liones-home.jpg">
  <link rel="stylesheet" href="/assets/css/site.css">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/brand/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/img/brand/favicon-16.png">
  <link rel="apple-touch-icon" href="/assets/img/brand/apple-touch-icon.png">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{data["title"]}",
    "description": "{data["description"]}",
    "url": "{current_url}",
    "inLanguage": "{html_lang}"
  }}
  </script>
</head>
<body>
<header class="site-header"><div class="container nav"><a class="brand" href="{home_href}"><img class="brand-logo" src="/assets/img/brand/logo-nav.jpg" alt="7sinsorigin.com logo"><span>7sinsorigin.com</span></a><button class="menu-btn" type="button" data-menu-btn>{"菜单" if is_zh else "Menu"}</button><nav class="nav-links"><a href="{home_href}">{home_label}</a><a href="{hub_href}">{hub_label}</a><a href="{release_href}">{release_label}</a><a href="{prereg_href}">{prereg_label}</a><a href="{chars_href}">{chars_label}</a><a href="{tier_href}">{tier_label}</a><a href="{beginner_href}">{beginner_label}</a><a href="{news_href}">{news_label}</a><a href="{lang_switch_href}"{" lang=\"zh\"" if not is_zh else ""}>{lang_switch_label}</a></nav></div></header>
<main>
  <section class="page-head"><div class="container"><p class="breadcrumb"><a href="{home_href}">{home_label}</a> / <a href="{data["crumb_href"]}">{data["crumb_label"]}</a> / {data["h1"]}</p><h1>{data["h1"]}</h1><p>{data["intro"]}</p></div></section>
  <section class="section"><div class="container grid">{cards_html}</div></section>
</main>
<footer class="footer"><div class="container"><p class="small"><a href="{about_href}">{about_label}</a> | <a href="{contact_href}">{contact_label}</a></p><p class="small">Copyright <span data-year></span> 7sinsorigin.com</p></div></footer>
<script src="/assets/js/site.js"></script>
</body>
</html>
"""


def main() -> None:
    for page in PAGES:
        for lang in ("en", "zh"):
            path = page["en_path"] if lang == "en" else page["zh_path"]
            target = ROOT / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(render_page(page, lang))
            print(f"Wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
