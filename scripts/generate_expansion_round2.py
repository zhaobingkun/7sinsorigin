#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-05-05"


PAGES = [
    {
        "slug": "pre-register-rewards",
        "og_type": "article",
        "en": {
            "title": "Pre-Register Rewards Guide | Seven Deadly Sins Origin",
            "description": "Pre-register rewards guide for Seven Deadly Sins Origin covering what to watch, what is usually confirmed first, and how to verify launch reward delivery.",
            "h1": "Seven Deadly Sins Origin Pre-Register Rewards Guide",
            "intro": "Reward-search traffic is usually high intent. Players are not looking for vague hype here. They want to know what rewards are confirmed, what may still change, and what they should save as proof before launch.",
            "cards": [
                ("What to Verify First", "<ul class=\"list-clean\"><li>Which rewards are explicitly confirmed on official pages</li><li>Whether rewards are tied to registration, launch login, or campaign milestones</li><li>Whether region or platform can affect timing</li></ul>"),
                ("What Usually Changes Later", "<p>Reward wording often becomes clearer closer to launch. Milestone totals, delivery timing, and account-bound conditions are the parts most likely to be clarified after the first promo push.</p>"),
                ("Best Use Case", "<p>Open this page when the main question is not how to pre-register, but what you are actually likely to receive and how to make sure the reward claim path stays safe.</p>"),
                ("Related Pages", "<p><a href=\"/pre-register/\">Pre-Register</a> · <a href=\"/release-date/\">Release Date</a> · <a href=\"/launch-day-checklist/\">Launch Day Checklist</a> · <a href=\"/news/\">News</a></p>"),
            ],
        },
        "zh": {
            "title": "预注册奖励指南 | 七大罪 Origin",
            "description": "七大罪 Origin 预注册奖励指南，整理哪些奖励已经明确、哪些细节还可能变化，以及上线前该如何留存确认信息。",
            "h1": "七大罪 Origin 预注册奖励指南",
            "intro": "奖励类搜索通常都很高意图。用户不是来看宣传词，而是想确认奖励到底有没有、什么时候发、以及怎样避免上线后因为账号或区服问题错过发放。",
            "cards": [
                ("先确认什么", "<ul class=\"list-clean\"><li>哪些奖励是官方页面已经明确写出的</li><li>奖励到底绑定预注册、上线登录还是里程碑活动</li><li>区服或平台会不会影响发放节奏</li></ul>"),
                ("后面最容易变的地方", "<p>离上线越近，奖励文案通常会更清楚。最容易继续被补充的通常是里程碑条件、发放时间和账号绑定规则。</p>"),
                ("适合什么时候看", "<p>当你关心的重点不是“怎么预注册”，而是“到底能拿到什么，以及怎么确保领得到”，就应该先看这一页。</p>"),
                ("相关页面", "<p><a href=\"/zh/pre-register/\">预注册</a> · <a href=\"/zh/release-date/\">发售时间</a> · <a href=\"/zh/launch-day-checklist/\">上线日清单</a> · <a href=\"/zh/news/\">新闻</a></p>"),
            ],
        },
    },
    {
        "slug": "launch-day-checklist",
        "og_type": "article",
        "en": {
            "title": "Launch Day Checklist | Seven Deadly Sins Origin",
            "description": "Launch day checklist for Seven Deadly Sins Origin covering account prep, install checks, reward claims, and the first pages to open after servers go live.",
            "h1": "Seven Deadly Sins Origin Launch Day Checklist",
            "intro": "Launch-day pages work when they reduce chaos. Players usually need one clean checklist: account ready, install ready, server timing clear, and a short reading path for the first hour after launch.",
            "cards": [
                ("Before Servers Open", "<ul class=\"list-clean\"><li>Confirm which account method you will actually keep</li><li>Bookmark the official game and news pages</li><li>Check install size, platform, and region timing ahead of time</li></ul>"),
                ("First Hour Priorities", "<ul class=\"list-clean\"><li>Log in with the correct account flow first</li><li>Check whether rewards and milestone mail arrive as expected</li><li>Avoid wasting early currency before roster needs are clearer</li></ul>"),
                ("Best Reading Order", "<p>Start with <a href=\"/current-characters/\">Current Characters</a>, then <a href=\"/best-beginner-team/\">Best Beginner Team</a>, then <a href=\"/daily-checklist/\">Daily Checklist</a> so your first session has direction.</p>"),
                ("Related Pages", "<p><a href=\"/pre-register/\">Pre-Register</a> · <a href=\"/pre-register-rewards/\">Pre-Register Rewards</a> · <a href=\"/how-to-link-accounts/\">How to Link Accounts</a> · <a href=\"/daily-checklist/\">Daily Checklist</a></p>"),
            ],
        },
        "zh": {
            "title": "上线日清单 | 七大罪 Origin",
            "description": "七大罪 Origin 上线日清单，整理账号准备、安装检查、奖励确认和开服后第一小时最该看的页面。",
            "h1": "七大罪 Origin 上线日清单",
            "intro": "上线日页面真正有价值的地方，是帮玩家减少混乱。最有用的不是长篇空话，而是一份干净的清单：账号准备好没有、安装准备好没有、开服时间清楚没有、第一小时该先看哪几页。",
            "cards": [
                ("开服前先做什么", "<ul class=\"list-clean\"><li>确认你最终要保留的账号登录方式</li><li>提前收藏官方游戏页和新闻页</li><li>提前确认安装包、平台和区服开放时间</li></ul>"),
                ("开服后一小时重点", "<ul class=\"list-clean\"><li>先用正确的账号方式登录</li><li>先确认预注册和里程碑奖励是否正常到帐</li><li>不要太早乱花前期资源</li></ul>"),
                ("推荐阅读顺序", "<p>先看 <a href=\"/zh/current-characters/\">当前角色</a>，再看 <a href=\"/zh/best-beginner-team/\">最佳开荒队伍</a>，然后看 <a href=\"/zh/daily-checklist/\">日常清单</a>，这样开服第一小时更有方向。</p>"),
                ("相关页面", "<p><a href=\"/zh/pre-register/\">预注册</a> · <a href=\"/zh/pre-register-rewards/\">预注册奖励</a> · <a href=\"/zh/how-to-link-accounts/\">账号绑定</a> · <a href=\"/zh/daily-checklist/\">日常清单</a></p>"),
            ],
        },
    },
    {
        "slug": "guest-account-vs-linked-account",
        "og_type": "article",
        "en": {
            "title": "Guest Account vs Linked Account | Seven Deadly Sins Origin",
            "description": "Guest account vs linked account guide for Seven Deadly Sins Origin with what each path risks and when to bind before progress becomes dangerous to lose.",
            "h1": "Guest Account vs Linked Account in Seven Deadly Sins Origin",
            "intro": "This page targets a very common setup mistake. Players want to know whether starting as guest is safe, when to bind, and what account path creates the lowest chance of losing progress.",
            "cards": [
                ("Guest Account Risk", "<p>Guest flows are attractive because they are fast, but the tradeoff is obvious: they become dangerous once real progress, rewards, or purchases start piling up without a confirmed bind.</p>"),
                ("Linked Account Value", "<p>A linked account usually gives better recovery, better device switching, and less launch-day confusion. The cost is just deciding your long-term login method early.</p>"),
                ("Best Use Case", "<p>Open this page before heavy play begins, not after. The safest moment to choose the better account path is before the account starts carrying real value.</p>"),
                ("Related Pages", "<p><a href=\"/how-to-link-accounts/\">How to Link Accounts</a> · <a href=\"/cross-save-and-cross-progression/\">Cross-Save and Cross-Progression</a> · <a href=\"/unlink-account/\">Unlink Account</a> · <a href=\"/login-failed/\">Login Failed</a></p>"),
            ],
        },
        "zh": {
            "title": "游客账号和绑定账号怎么选 | 七大罪 Origin",
            "description": "七大罪 Origin 游客账号和绑定账号选择指南，整理两种路径的风险点，以及什么时候必须尽快完成绑定。",
            "h1": "七大罪 Origin 游客账号和绑定账号怎么选",
            "intro": "这是非常典型的启动期问题。玩家真正想知道的，是游客开局到底安不安全、什么时候必须绑定，以及哪种账号路径更不容易把进度弄丢。",
            "cards": [
                ("游客账号的风险", "<p>游客开局的优势只是快，但风险也很直接：一旦开始有真实进度、奖励甚至充值，没绑定的游客号就会越来越危险。</p>"),
                ("绑定账号的价值", "<p>绑定账号通常意味着更好的找回能力、更顺的换设备体验，以及更少的开服期账号混乱。代价只是你需要更早决定长期使用的登录方式。</p>"),
                ("适合什么时候看", "<p>这页最该在你正式深玩前打开，而不是等进度很多以后再补救。越早决定账号路径，越安全。</p>"),
                ("相关页面", "<p><a href=\"/zh/how-to-link-accounts/\">账号绑定</a> · <a href=\"/zh/cross-save-and-cross-progression/\">跨平台存档</a> · <a href=\"/zh/unlink-account/\">解除绑定</a> · <a href=\"/zh/login-failed/\">登录失败</a></p>"),
            ],
        },
    },
    {
        "slug": "cross-save-and-cross-progression",
        "og_type": "article",
        "en": {
            "title": "Cross-Save and Cross-Progression Guide | Seven Deadly Sins Origin",
            "description": "Cross-save and cross-progression guide for Seven Deadly Sins Origin with what to verify between devices, accounts, and platform assumptions before launch.",
            "h1": "Seven Deadly Sins Origin Cross-Save and Cross-Progression Guide",
            "intro": "Cross-save questions attract strong traffic because they affect where players start and whether they trust the account path at all. The right page should clarify what to verify first instead of assuming every platform setup works the same way.",
            "cards": [
                ("What to Check First", "<ul class=\"list-clean\"><li>Whether progress is tied to a publisher account, platform account, or both</li><li>Whether switching devices requires account binding first</li><li>Whether region or store version affects progression visibility</li></ul>"),
                ("What Players Usually Assume Wrong", "<p>The biggest mistake is assuming that installing the game on another device automatically means the same progress is ready there. Cross-progression only feels simple when the account layer is already correct.</p>"),
                ("Best Use Case", "<p>Use this page when choosing your main device, testing early device switching, or deciding how much trust to place in a guest-account start.</p>"),
                ("Related Pages", "<p><a href=\"/how-to-link-accounts/\">How to Link Accounts</a> · <a href=\"/guest-account-vs-linked-account/\">Guest vs Linked Account</a> · <a href=\"/unlink-account/\">Unlink Account</a> · <a href=\"/systems/controller-support/\">Controller Support</a></p>"),
            ],
        },
        "zh": {
            "title": "跨平台存档与进度共享指南 | 七大罪 Origin",
            "description": "七大罪 Origin 跨平台存档与进度共享指南，整理设备切换前该确认什么，以及账号层最容易误判的地方。",
            "h1": "七大罪 Origin 跨平台存档与进度共享指南",
            "intro": "跨平台存档相关问题的搜索意图很强，因为它直接决定玩家在哪个设备开局，以及敢不敢放心投入时间。真正有用的页面，不是空泛地说“支持或不支持”，而是先讲清楚该验证什么。",
            "cards": [
                ("先看什么", "<ul class=\"list-clean\"><li>进度到底绑定发行商账号、平台账号，还是两者都要</li><li>换设备前是否必须先完成绑定</li><li>区服或商店版本会不会影响进度显示</li></ul>"),
                ("最常见的误判", "<p>最常见的错误，就是以为换台设备安装后进度会自动出现。跨平台体验看起来简单，前提其实是账号层本来就做对了。</p>"),
                ("适合什么时候看", "<p>当你在决定主力设备、准备测试设备切换，或者怀疑游客开局以后不好转正时，这页最值得先开。</p>"),
                ("相关页面", "<p><a href=\"/zh/how-to-link-accounts/\">账号绑定</a> · <a href=\"/zh/guest-account-vs-linked-account/\">游客号和绑定号怎么选</a> · <a href=\"/zh/unlink-account/\">解除绑定</a> · <a href=\"/zh/systems/controller-support/\">手柄支持</a></p>"),
            ],
        },
    },
    {
        "slug": "unlink-account",
        "og_type": "article",
        "en": {
            "title": "Unlink Account Guide | Seven Deadly Sins Origin",
            "description": "Unlink account guide for Seven Deadly Sins Origin with what to check before trying to detach a login method or move account ownership safely.",
            "h1": "Seven Deadly Sins Origin Unlink Account Guide",
            "intro": "Unlink-account traffic is usually high stress traffic. Players arrive here when they are already worried about being stuck with the wrong login path, so the page should stay conservative and focus on safety checks rather than promising easy reversals.",
            "cards": [
                ("Safety First", "<ul class=\"list-clean\"><li>Verify you still have a safe recovery method before changing anything</li><li>Check whether publisher and platform links are treated differently</li><li>Do not assume unlinking is reversible without support involvement</li></ul>"),
                ("Why This Page Matters", "<p>Account changes become dangerous once a real roster, launch rewards, or purchases are attached. That is why unlink pages should prioritize risk control over speed.</p>"),
                ("Best Use Case", "<p>Use this page before filing support, before switching devices permanently, or before trying to clean up an early guest-account mistake.</p>"),
                ("Related Pages", "<p><a href=\"/how-to-link-accounts/\">How to Link Accounts</a> · <a href=\"/guest-account-vs-linked-account/\">Guest vs Linked Account</a> · <a href=\"/cross-save-and-cross-progression/\">Cross-Save</a> · <a href=\"/bugs-errors/\">Bugs and Errors</a></p>"),
            ],
        },
        "zh": {
            "title": "解除账号绑定指南 | 七大罪 Origin",
            "description": "七大罪 Origin 解除账号绑定指南，整理在更换登录方式或处理早期错误绑定前必须先确认的安全点。",
            "h1": "七大罪 Origin 解除账号绑定指南",
            "intro": "解除绑定类搜索通常都带着压力，因为用户往往已经开始担心自己绑错了号。真正有用的页面，不该承诺简单撤销，而是先讲清楚怎么降低风险。",
            "cards": [
                ("先把安全放第一位", "<ul class=\"list-clean\"><li>先确认还有可用的找回方式</li><li>先确认发行商账号和平台账号是不是不同层级</li><li>不要默认解除绑定一定能轻松恢复</li></ul>"),
                ("为什么这页重要", "<p>一旦账号上已经挂了真实角色、上线奖励或者充值记录，账号变更就会变得更危险，所以这类页面最重要的是风险控制。</p>"),
                ("适合什么时候看", "<p>准备提交客服单、准备永久换设备，或者想修正早期游客号错误时，都应该先看这一页。</p>"),
                ("相关页面", "<p><a href=\"/zh/how-to-link-accounts/\">账号绑定</a> · <a href=\"/zh/guest-account-vs-linked-account/\">游客号和绑定号</a> · <a href=\"/zh/cross-save-and-cross-progression/\">跨平台存档</a> · <a href=\"/zh/bugs-errors/\">错误与问题</a></p>"),
            ],
        },
    },
    {
        "slug": "pity-carry-over",
        "og_type": "article",
        "en": {
            "title": "Does Pity Carry Over? | Seven Deadly Sins Origin",
            "description": "Pity carry-over guide for Seven Deadly Sins Origin with the exact questions players need answered before treating banner progress as transferable.",
            "h1": "Does Pity Carry Over in Seven Deadly Sins Origin?",
            "intro": "This is one of the highest-intent gacha questions because it directly changes whether players pull now or save. The page should frame the exact carry-over question and separate confirmed rules from assumptions.",
            "cards": [
                ("What Carry-Over Usually Means", "<p>Players usually mean one of two things: whether pity progress survives after a banner ends, or whether it transfers between banner types. Those are not automatically the same rule.</p>"),
                ("What to Verify Before Pulling", "<ul class=\"list-clean\"><li>Whether pity is banner-specific or shared</li><li>Whether pity resets when the featured unit changes</li><li>Whether official wording distinguishes event banners from standard banners</li></ul>"),
                ("Why This Changes Pull Decisions", "<p>If pity does not carry over, partial progress becomes much riskier. If it does carry over in limited ways, saving and planning become more flexible.</p>"),
                ("Related Pages", "<p><a href=\"/systems/gacha-pity/\">Gacha and Pity</a> · <a href=\"/banners/current/\">Current Banners</a> · <a href=\"/save-summons-or-pull-now/\">Save Summons or Pull Now</a> · <a href=\"/best-banner-to-pull/\">Best Banner to Pull</a></p>"),
            ],
        },
        "zh": {
            "title": "保底会继承吗？ | 七大罪 Origin",
            "description": "七大罪 Origin 保底继承问题整理，帮助玩家在抽卡前先分清不同保底继承含义和最关键的验证点。",
            "h1": "七大罪 Origin 保底会继承吗？",
            "intro": "这是最典型的高意图抽卡问题之一，因为它会直接改变玩家现在抽还是继续存。真正该做的，不是空想保底规则，而是把“继承”到底指什么先拆清楚。",
            "cards": [
                ("玩家说的继承通常是哪两种", "<p>大多数玩家说“保底继承”，其实可能指两件不同的事：池子结束后保底进度还在不在，以及不同池子之间会不会互通。这两件事不能默认一样。</p>"),
                ("抽之前先确认什么", "<ul class=\"list-clean\"><li>保底是单池独立还是多池共通</li><li>换 featured 角色后保底会不会重置</li><li>官方文案有没有区分活动池和常驻池</li></ul>"),
                ("为什么这会改变抽卡决策", "<p>如果保底不继承，半途抽进去的风险会明显更高；如果部分继承成立，抽卡规划就会灵活得多。</p>"),
                ("相关页面", "<p><a href=\"/zh/systems/gacha-pity/\">抽卡与保底系统</a> · <a href=\"/zh/banners/current/\">当前卡池</a> · <a href=\"/zh/save-summons-or-pull-now/\">现在该抽还是继续存</a> · <a href=\"/zh/best-banner-to-pull/\">最值得抽哪个池</a></p>"),
            ],
        },
    },
    {
        "slug": "how-to-get-more-diamonds",
        "og_type": "article",
        "en": {
            "title": "How to Get More Diamonds | Seven Deadly Sins Origin",
            "description": "How to get more diamonds in Seven Deadly Sins Origin with a priority-based view of where premium pull currency is most likely to come from.",
            "h1": "How to Get More Diamonds in Seven Deadly Sins Origin",
            "intro": "Currency-search traffic is usually practical traffic. Players do not just want a big list. They want to know which diamond sources are worth checking first and which sources are too slow to build a real banner plan around.",
            "cards": [
                ("Most Valuable Early Sources", "<ul class=\"list-clean\"><li>Launch rewards, milestone rewards, and official campaigns</li><li>Story and progression milestones that unlock naturally</li><li>Daily and weekly loops that can be sustained without destroying account efficiency</li></ul>"),
                ("What Not to Overrate", "<p>The slowest sources are often not useless, but they should not become the center of your banner plan if they arrive too late or cost too much time.</p>"),
                ("Best Use Case", "<p>Open this page when the real question is whether your account can realistically afford another banner target without breaking progression.</p>"),
                ("Related Pages", "<p><a href=\"/currency-guide/\">Currency Guide</a> · <a href=\"/best-use-of-diamonds/\">Best Use of Diamonds</a> · <a href=\"/daily-checklist/\">Daily Checklist</a> · <a href=\"/save-summons-or-pull-now/\">Save Summons or Pull Now</a></p>"),
            ],
        },
        "zh": {
            "title": "怎么获得更多钻石 | 七大罪 Origin",
            "description": "七大罪 Origin 获取更多钻石的优先级指南，帮助玩家分清哪些来源最值得先看，哪些来源不适合当核心抽卡计划。",
            "h1": "七大罪 Origin 怎么获得更多钻石",
            "intro": "货币类搜索通常都很实用。玩家真正关心的不是一张长清单，而是哪些钻石来源最值得先看，哪些来源虽然存在，但不适合拿来支撑真实抽卡计划。",
            "cards": [
                ("前期最有价值的来源", "<ul class=\"list-clean\"><li>上线奖励、里程碑奖励和官方活动</li><li>自然推进主线与成长时会解锁的奖励</li><li>不会严重拖慢账号效率的日常和周常来源</li></ul>"),
                ("不要高估什么", "<p>最慢的钻石来源不一定没用，但如果回收太晚、耗时太高，就不适合拿来当你的主要抽卡计划基础。</p>"),
                ("适合什么时候看", "<p>如果你真正想知道的是：我的账号还能不能负担下一个目标池，而不是“哪里都能拿一点钻石”，那就该先看这页。</p>"),
                ("相关页面", "<p><a href=\"/zh/currency-guide/\">货币指南</a> · <a href=\"/zh/best-use-of-diamonds/\">钻石最值得花在哪</a> · <a href=\"/zh/daily-checklist/\">日常清单</a> · <a href=\"/zh/save-summons-or-pull-now/\">现在该抽还是继续存</a></p>"),
            ],
        },
    },
    {
        "slug": "best-use-of-diamonds",
        "og_type": "article",
        "en": {
            "title": "Best Use of Diamonds | Seven Deadly Sins Origin",
            "description": "Best use of diamonds guide for Seven Deadly Sins Origin with spending priorities, banner logic, and how to avoid wasting premium currency early.",
            "h1": "Best Use of Diamonds in Seven Deadly Sins Origin",
            "intro": "The highest-value diamond page is not just a spending list. It is a decision page that explains when banner spending is justified, when account growth needs should come first, and which convenience purchases deserve caution.",
            "cards": [
                ("Best Spending Priority", "<ul class=\"list-clean\"><li>Protect premium pull value first</li><li>Use diamonds where they support meaningful roster or progression gains</li><li>Be skeptical of convenience spending if it delays a better banner decision later</li></ul>"),
                ("What Usually Goes Wrong", "<p>Early accounts often waste premium currency on short-term comfort, then arrive at a stronger banner without enough resources left to act.</p>"),
                ("Best Use Case", "<p>Use this page when the question is not how to get more diamonds, but whether the diamonds you already have are about to be spent in the right place.</p>"),
                ("Related Pages", "<p><a href=\"/how-to-get-more-diamonds/\">How to Get More Diamonds</a> · <a href=\"/currency-guide/\">Currency Guide</a> · <a href=\"/best-banner-to-pull/\">Best Banner to Pull</a> · <a href=\"/what-to-buy-in-shop/\">What to Buy in Shop</a></p>"),
            ],
        },
        "zh": {
            "title": "钻石最值得花在哪 | 七大罪 Origin",
            "description": "七大罪 Origin 钻石使用优先级指南，整理哪些投入更值，哪些前期便利消费最容易让后续抽卡变得被动。",
            "h1": "七大罪 Origin 钻石最值得花在哪",
            "intro": "最有价值的钻石页，不该只是支出清单，而应该是一张决策页：什么时候抽卡投入合理，什么时候该先保留资源，以及哪些便利消费最值得警惕。",
            "cards": [
                ("最好的使用优先级", "<ul class=\"list-clean\"><li>先保护高价值的抽卡资源</li><li>把钻石花在真正会改变阵容或成长效率的地方</li><li>对会拖慢后续强池计划的便利消费保持怀疑</li></ul>"),
                ("最容易出错的地方", "<p>很多前期账号都会把钻石花在短期舒服上，结果真正更强的池子来了时，资源已经不够用了。</p>"),
                ("适合什么时候看", "<p>当你的问题已经不是“怎么拿更多钻石”，而是“手里的钻石要不要现在就花掉”，这页就最有价值。</p>"),
                ("相关页面", "<p><a href=\"/zh/how-to-get-more-diamonds/\">怎么获得更多钻石</a> · <a href=\"/zh/currency-guide/\">货币指南</a> · <a href=\"/zh/best-banner-to-pull/\">最值得抽哪个池</a> · <a href=\"/zh/what-to-buy-in-shop/\">商店里最值得买什么</a></p>"),
            ],
        },
    },
    {
        "slug": "what-to-buy-in-shop",
        "og_type": "article",
        "en": {
            "title": "What to Buy in Shop | Seven Deadly Sins Origin",
            "description": "Shop-buying guide for Seven Deadly Sins Origin with what items usually deserve resources first and which shop traps can slow account growth.",
            "h1": "What to Buy in Shop in Seven Deadly Sins Origin",
            "intro": "Shop pages matter because new accounts rarely lose power through one terrible pull. They lose value through repeated small purchases that look harmless but quietly eat the same resources needed for banners and upgrades.",
            "cards": [
                ("What Usually Deserves Priority", "<ul class=\"list-clean\"><li>Items that remove real progression bottlenecks</li><li>Currency-efficient upgrades tied to your active team plan</li><li>Limited items that are harder to replace later</li></ul>"),
                ("What Often Becomes a Trap", "<p>Low-value convenience items and scattered impulse buys often feel cheap in isolation, but together they can delay real banner or upgrade goals.</p>"),
                ("Best Use Case", "<p>Open this page before spending premium or semi-premium resources in shop menus that look harmless but can reshape your first-week resource curve.</p>"),
                ("Related Pages", "<p><a href=\"/currency-guide/\">Currency Guide</a> · <a href=\"/best-use-of-diamonds/\">Best Use of Diamonds</a> · <a href=\"/daily-checklist/\">Daily Checklist</a> · <a href=\"/how-to-get-stronger/\">How to Get Stronger</a></p>"),
            ],
        },
        "zh": {
            "title": "商店里最值得买什么 | 七大罪 Origin",
            "description": "七大罪 Origin 商店购买优先级指南，整理哪些资源最值得优先换，哪些看似便宜的东西最容易拖慢账号成长。",
            "h1": "七大罪 Origin 商店里最值得买什么",
            "intro": "商店类页面很重要，因为很多新号并不是输在一次抽卡，而是输在一连串看起来无伤大雅的小消费上，最后把本该留给卡池和强化的资源一点点吃掉。",
            "cards": [
                ("通常值得优先考虑什么", "<ul class=\"list-clean\"><li>能直接解决成长瓶颈的道具</li><li>和当前主力队伍计划高度相关的高效率投入</li><li>以后更难补回来的限量资源</li></ul>"),
                ("最常见的陷阱", "<p>低价值便利道具和随手冲动消费，单看一次好像不贵，但累计起来往往会拖慢真正重要的抽卡或强化目标。</p>"),
                ("适合什么时候看", "<p>在你准备把高级资源或半高级资源花进商店之前，这页最值得先开一次，因为很多隐形损失都是在这里开始的。</p>"),
                ("相关页面", "<p><a href=\"/zh/currency-guide/\">货币指南</a> · <a href=\"/zh/best-use-of-diamonds/\">钻石最值得花在哪</a> · <a href=\"/zh/daily-checklist/\">日常清单</a> · <a href=\"/zh/how-to-get-stronger/\">如何快速变强</a></p>"),
            ],
        },
    },
    {
        "slug": "f2p-beginner-guide",
        "og_type": "article",
        "en": {
            "title": "F2P Beginner Guide | Seven Deadly Sins Origin",
            "description": "Free-to-play beginner guide for Seven Deadly Sins Origin with early resource discipline, roster expectations, and where F2P accounts should stay conservative.",
            "h1": "Seven Deadly Sins Origin F2P Beginner Guide",
            "intro": "F2P pages work when they set expectations correctly. The useful version is not just “you can play for free.” It explains where free accounts gain ground, where they should stay conservative, and what mistakes create avoidable pressure.",
            "cards": [
                ("What F2P Accounts Need Most", "<ul class=\"list-clean\"><li>Cleaner resource discipline than spenders can get away with</li><li>A narrower roster plan focused on account function</li><li>Patience around banners that are strong but not essential</li></ul>"),
                ("Where F2P Mistakes Start", "<p>Most F2P pressure starts when the account tries to mimic spender flexibility too early. The fix is usually not grinding harder, but making fewer unnecessary pivots.</p>"),
                ("Best Use Case", "<p>Open this page when you want your first-week and first-month decisions to stay realistic for a free account instead of borrowing paid-account assumptions.</p>"),
                ("Related Pages", "<p><a href=\"/best-beginner-team/\">Best Beginner Team</a> · <a href=\"/currency-guide/\">Currency Guide</a> · <a href=\"/save-summons-or-pull-now/\">Save Summons or Pull Now</a> · <a href=\"/beginner-mistakes/\">Beginner Mistakes</a></p>"),
            ],
        },
        "zh": {
            "title": "零氪新手指南 | 七大罪 Origin",
            "description": "七大罪 Origin 零氪新手指南，整理免费账号该如何控资源、设预期，以及最应该避免的前期误区。",
            "h1": "七大罪 Origin 零氪新手指南",
            "intro": "零氪页真正有价值的地方，不是告诉你“免费也能玩”，而是把预期讲清楚：哪些地方零氪能稳住，哪些地方要更保守，以及哪些错误会让压力变成不必要的损耗。",
            "cards": [
                ("零氪账号最需要什么", "<ul class=\"list-clean\"><li>比氪金号更干净的资源纪律</li><li>更窄、更明确的阵容规划</li><li>面对强但不刚需的卡池时更稳的忍耐力</li></ul>"),
                ("零氪最容易从哪里开始崩", "<p>很多零氪压力，不是因为资源太少，而是因为太早模仿氪金号的灵活度。真正的修正通常是少转向，而不是更拼命刷。</p>"),
                ("适合什么时候看", "<p>如果你希望第一周和第一个月的决策，真正建立在免费账号逻辑上，而不是借用了付费账号思路，这页就很重要。</p>"),
                ("相关页面", "<p><a href=\"/zh/best-beginner-team/\">最佳开荒队伍</a> · <a href=\"/zh/currency-guide/\">货币指南</a> · <a href=\"/zh/save-summons-or-pull-now/\">现在该抽还是继续存</a> · <a href=\"/zh/beginner-mistakes/\">新手常见错误</a></p>"),
            ],
        },
    },
    {
        "slug": "beginner-mistakes",
        "og_type": "article",
        "en": {
            "title": "Beginner Mistakes Guide | Seven Deadly Sins Origin",
            "description": "Beginner mistakes guide for Seven Deadly Sins Origin with the early decisions that most often slow growth, waste resources, or make banner plans harder.",
            "h1": "Seven Deadly Sins Origin Beginner Mistakes Guide",
            "intro": "Mistake pages attract strong search intent because players rarely know the exact mistake before they feel its cost. The best version of this page points to patterns that quietly slow growth instead of waiting for obvious failure.",
            "cards": [
                ("Most Common Early Mistakes", "<ul class=\"list-clean\"><li>Spreading upgrades across too many units too early</li><li>Spending premium currency without a real banner plan</li><li>Treating every side activity as equally urgent</li></ul>"),
                ("Why These Mistakes Hurt So Much", "<p>Early losses compound. A weak currency decision or upgrade split can distort the next several days of progression, not just the next ten minutes.</p>"),
                ("Best Use Case", "<p>Open this page when your account feels active but not efficient, or when you want a short mistake filter before making another round of spending or upgrade choices.</p>"),
                ("Related Pages", "<p><a href=\"/f2p-beginner-guide/\">F2P Beginner Guide</a> · <a href=\"/currency-guide/\">Currency Guide</a> · <a href=\"/best-beginner-team/\">Best Beginner Team</a> · <a href=\"/how-to-get-stronger/\">How to Get Stronger</a></p>"),
            ],
        },
        "zh": {
            "title": "新手常见错误指南 | 七大罪 Origin",
            "description": "七大罪 Origin 新手常见错误指南，整理最容易拖慢成长、浪费资源、破坏抽卡计划的前期决策。",
            "h1": "七大罪 Origin 新手常见错误指南",
            "intro": "错误类页面的搜索意图通常很强，因为玩家往往在意识到“有代价”之后，才开始找自己到底错在哪。最有价值的版本，应该提前指出那些会悄悄拖慢成长的模式。",
            "cards": [
                ("最常见的前期错误", "<ul class=\"list-clean\"><li>太早把资源分散到太多角色身上</li><li>没有抽卡计划就先花掉高级资源</li><li>把所有支线内容都当成同样急</li></ul>"),
                ("为什么这些错误代价这么高", "<p>前期损失会叠加。一次升级分散或者一次货币误用，影响的通常不只是十分钟，而是接下来好几天的成长节奏。</p>"),
                ("适合什么时候看", "<p>如果你的账号看起来一直很忙，但始终不够顺，或者你想在下一轮投入资源前先过滤一遍最常见错误，这页就很合适。</p>"),
                ("相关页面", "<p><a href=\"/zh/f2p-beginner-guide/\">零氪新手指南</a> · <a href=\"/zh/currency-guide/\">货币指南</a> · <a href=\"/zh/best-beginner-team/\">最佳开荒队伍</a> · <a href=\"/zh/how-to-get-stronger/\">如何快速变强</a></p>"),
            ],
        },
    },
    {
        "slug": "save-summons-or-pull-now",
        "og_type": "article",
        "en": {
            "title": "Save Summons or Pull Now? | Seven Deadly Sins Origin",
            "description": "Save summons or pull now guide for Seven Deadly Sins Origin with the key questions that decide whether immediate pulling is justified or patience is stronger.",
            "h1": "Should You Save Summons or Pull Now in Seven Deadly Sins Origin?",
            "intro": "This is a classic high-intent banner question. Players rarely need motivation here. They need a decision framework for whether a live banner solves a real account problem or just tempts them away from a better future target.",
            "cards": [
                ("Pull Now If", "<ul class=\"list-clean\"><li>The banner solves a missing core role your account actually lacks</li><li>The unit improves more than one real team path</li><li>You understand the pity and carry-over risk well enough</li></ul>"),
                ("Save If", "<ul class=\"list-clean\"><li>The banner is strong but non-essential</li><li>Upcoming banner risk looks higher-value for your account</li><li>Your resource curve becomes too fragile after one bad pull run</li></ul>"),
                ("Why This Page Matters", "<p>Many accounts do not fail because they pulled once. They fail because they kept making short-horizon decisions with no roster plan behind them.</p>"),
                ("Related Pages", "<p><a href=\"/best-banner-to-pull/\">Best Banner to Pull</a> · <a href=\"/banners/current/\">Current Banners</a> · <a href=\"/banners/upcoming/\">Upcoming Banners</a> · <a href=\"/pity-carry-over/\">Does Pity Carry Over?</a></p>"),
            ],
        },
        "zh": {
            "title": "现在该抽还是继续存？ | 七大罪 Origin",
            "description": "七大罪 Origin 现在该抽还是继续存的判断页，整理哪些情况适合立刻抽，哪些情况更该保留资源等待后续池。",
            "h1": "七大罪 Origin 现在该抽还是继续存？",
            "intro": "这是最典型的高意图卡池问题之一。玩家真正需要的不是鼓励，而是一套判断框架：当前池到底是在补真实缺口，还是只是在把你从更好的后续目标里拽走。",
            "cards": [
                ("什么时候现在抽更合理", "<ul class=\"list-clean\"><li>这个池真的补到了你账号缺的核心功能位</li><li>该角色能同时服务多条真实队伍路线</li><li>你已经理解保底和继承风险</li></ul>"),
                ("什么时候更该继续存", "<ul class=\"list-clean\"><li>当前池虽然强，但不是刚需</li><li>后续池对你的账号价值可能更高</li><li>一轮抽卡失败后，你的资源曲线会变得太脆弱</li></ul>"),
                ("为什么这页重要", "<p>很多账号不是毁在“一次抽卡”，而是毁在一连串只看眼前、没有阵容规划支撑的短视决策上。</p>"),
                ("相关页面", "<p><a href=\"/zh/best-banner-to-pull/\">最值得抽哪个池</a> · <a href=\"/zh/banners/current/\">当前卡池</a> · <a href=\"/zh/banners/upcoming/\">后续卡池</a> · <a href=\"/zh/pity-carry-over/\">保底会继承吗</a></p>"),
            ],
        },
    },
]


def render_page(lang: str, slug: str, page: dict) -> str:
    is_zh = lang == "zh"
    locale = "zh_CN" if is_zh else "en_US"
    language = "zh-CN" if is_zh else "en"
    title = page["title"]
    desc = page["description"]
    h1 = page["h1"]
    intro = page["intro"]
    cards = page["cards"]
    og_type = page.get("og_type", "article")
    base = "https://7sinsorigin.com"
    path = f"/zh/{slug}/" if is_zh else f"/{slug}/"
    canonical = f"{base}{path}"
    alt_en = f"{base}/{slug}/"
    alt_zh = f"{base}/zh/{slug}/"
    home_href = "/zh/" if is_zh else "/"
    home_label = "首页" if is_zh else "Home"
    lang_switch = f"/{slug}/" if is_zh else f"/zh/{slug}/"
    lang_label = "English" if is_zh else "中文"
    menu_label = "菜单" if is_zh else "Menu"
    nav = (
        '<a href="/zh/">首页</a><a href="/zh/seven-deadly-sins-origin/">Origin 总览</a><a href="/zh/release-date/">发售时间</a>'
        '<a href="/zh/pre-register/">预注册</a><a href="/zh/characters/">角色</a><a href="/zh/tier-list/">强度榜</a>'
        '<a href="/zh/beginner-guide/">新手攻略</a><a href="/zh/news/">新闻</a>'
        if is_zh
        else '<a href="/">Home</a><a href="/seven-deadly-sins-origin/">Origin Hub</a><a href="/release-date/">Release Date</a>'
        '<a href="/pre-register/">Pre-Register</a><a href="/characters/">Characters</a><a href="/tier-list/">Tier List</a>'
        '<a href="/beginner-guide/">Beginner Guide</a><a href="/news/">News</a>'
    )
    breadcrumb = f'<p class="breadcrumb"><a href="{home_href}">{home_label}</a> / {h1}</p>'
    cards_html = "".join(f'<article class="card"><h2>{heading}</h2>{body}</article>' for heading, body in cards)
    schema_type = "Article"
    return f"""<!doctype html>
<html lang="{language}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0d3f2b">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{alt_en}">
  <link rel="alternate" hreflang="zh" href="{alt_zh}">
  <link rel="alternate" hreflang="x-default" href="{alt_en}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="{locale}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="7sinsorigin.com">
  <meta property="og:image" content="https://7sinsorigin.com/assets/img/brand/logo-mark.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://7sinsorigin.com/assets/img/brand/logo-mark.png">
  <link rel="stylesheet" href="/assets/css/site.css">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/brand/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/img/brand/favicon-16.png">
  <link rel="apple-touch-icon" href="/assets/img/brand/apple-touch-icon.png">
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"{schema_type}","headline":"{title}","description":"{desc}","url":"{canonical}","inLanguage":"{language}","mainEntityOfPage":"{canonical}"}}</script>
</head>
<body>
<header class="site-header"><div class="container nav"><a class="brand" href="{home_href}"><img class="brand-logo" src="/assets/img/brand/logo-nav.jpg" alt="7sinsorigin.com logo"><span>7sinsorigin.com</span></a><button class="menu-btn" type="button" data-menu-btn>{menu_label}</button><nav class="nav-links">{nav}<a href="{lang_switch}" lang="{'en' if is_zh else 'zh'}">{lang_label}</a></nav></div></header>
<main>
  <section class="page-head"><div class="container">{breadcrumb}<h1>{h1}</h1><p>{intro}</p></div></section>
  <section class="section"><div class="container grid">{cards_html}</div></section>
</main>
<footer class="footer"><div class="container"><p class="small"><a href="{'/zh/about/' if is_zh else '/about/'}">{'关于' if is_zh else 'About'}</a> | <a href="{'/zh/contact/' if is_zh else '/contact/'}">{'联系' if is_zh else 'Contact'}</a></p><p class="small">Copyright <span data-year></span> 7sinsorigin.com</p></div></footer>
<script src="/assets/js/site.js"></script>
</body>
</html>
"""


def write_pages() -> None:
    for page in PAGES:
        slug = page["slug"]
        for lang in ("en", "zh"):
            page_data = page[lang]
            rel = Path("zh") / slug / "index.html" if lang == "zh" else Path(slug) / "index.html"
            out = ROOT / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            page_data = {**page_data, "og_type": page["og_type"]}
            out.write_text(render_page(lang, slug, page_data), encoding="utf-8")


def update_text(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text and new not in text:
        text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


def update_hubs() -> None:
    update_text(
        ROOT / "pre-register/index.html",
        '<p><a href="/release-date/">Release Date</a> · <a href="/banners/current/">Current Banners</a> · <a href="/best-banner-to-pull/">Best Banner to Pull On</a> · <a href="/how-to-link-accounts/">How to Link Accounts</a> · <a href="/systems/controller-support/">Controller Support</a> · <a href="/beginner-guide/">Beginner Guide</a> · <a href="https://7origin.netmarble.com/game" target="_blank" rel="noopener">Official Game Page</a></p>',
        '<p><a href="/release-date/">Release Date</a> · <a href="/pre-register-rewards/">Pre-Register Rewards</a> · <a href="/launch-day-checklist/">Launch Day Checklist</a> · <a href="/best-banner-to-pull/">Best Banner to Pull On</a> · <a href="/how-to-link-accounts/">How to Link Accounts</a> · <a href="/systems/controller-support/">Controller Support</a> · <a href="/beginner-guide/">Beginner Guide</a> · <a href="https://7origin.netmarble.com/game" target="_blank" rel="noopener">Official Game Page</a></p>',
    )
    update_text(
        ROOT / "zh/pre-register/index.html",
        '<p><a href="/zh/release-date/">发售时间</a> · <a href="/zh/banners/current/">当前卡池</a> · <a href="/zh/best-banner-to-pull/">现在最值得抽哪个卡池</a> · <a href="/zh/how-to-link-accounts/">账号绑定</a> · <a href="/zh/systems/controller-support/">手柄支持</a> · <a href="/zh/beginner-guide/">新手攻略</a> · <a href="https://7origin.netmarble.com/game" target="_blank" rel="noopener">官方游戏页</a></p>',
        '<p><a href="/zh/release-date/">发售时间</a> · <a href="/zh/pre-register-rewards/">预注册奖励</a> · <a href="/zh/launch-day-checklist/">上线日清单</a> · <a href="/zh/best-banner-to-pull/">现在最值得抽哪个卡池</a> · <a href="/zh/how-to-link-accounts/">账号绑定</a> · <a href="/zh/systems/controller-support/">手柄支持</a> · <a href="/zh/beginner-guide/">新手攻略</a> · <a href="https://7origin.netmarble.com/game" target="_blank" rel="noopener">官方游戏页</a></p>',
    )
    update_text(
        ROOT / "how-to-link-accounts/index.html",
        '<p><a href="/pre-register/">Pre-Register</a> · <a href="/systems/controller-support/">Controller Support</a> · <a href="/release-date/">Release Date</a> · <a href="/bugs-errors/">Bugs and Errors</a></p>',
        '<p><a href="/guest-account-vs-linked-account/">Guest vs Linked Account</a> · <a href="/cross-save-and-cross-progression/">Cross-Save</a> · <a href="/unlink-account/">Unlink Account</a> · <a href="/release-date/">Release Date</a> · <a href="/bugs-errors/">Bugs and Errors</a></p>',
    )
    update_text(
        ROOT / "zh/how-to-link-accounts/index.html",
        '<p><a href="/zh/pre-register/">预注册</a> · <a href="/zh/systems/controller-support/">手柄支持</a> · <a href="/zh/release-date/">发售时间</a> · <a href="/zh/bugs-errors/">错误与问题</a></p>',
        '<p><a href="/zh/guest-account-vs-linked-account/">游客号和绑定号</a> · <a href="/zh/cross-save-and-cross-progression/">跨平台存档</a> · <a href="/zh/unlink-account/">解除绑定</a> · <a href="/zh/release-date/">发售时间</a> · <a href="/zh/bugs-errors/">错误与问题</a></p>',
    )
    update_text(
        ROOT / "systems/gacha-pity/index.html",
        '<p><a href="/systems/">Systems Hub</a> · <a href="/banners/current/">Current Banners</a> · <a href="/banners/upcoming/">Upcoming Banners</a> · <a href="/news/">News</a> · <a href="/tier-list/">Tier List</a></p>',
        '<p><a href="/systems/">Systems Hub</a> · <a href="/pity-carry-over/">Does Pity Carry Over?</a> · <a href="/save-summons-or-pull-now/">Save Summons or Pull Now</a> · <a href="/banners/current/">Current Banners</a> · <a href="/tier-list/">Tier List</a></p>',
    )
    update_text(
        ROOT / "zh/systems/gacha-pity/index.html",
        '<p><a href="/zh/systems/">系统总览</a> · <a href="/zh/banners/current/">当前卡池</a> · <a href="/zh/banners/upcoming/">后续卡池</a> · <a href="/zh/news/">新闻</a> · <a href="/zh/tier-list/">强度榜</a></p>',
        '<p><a href="/zh/systems/">系统总览</a> · <a href="/zh/pity-carry-over/">保底会继承吗</a> · <a href="/zh/save-summons-or-pull-now/">现在该抽还是继续存</a> · <a href="/zh/banners/current/">当前卡池</a> · <a href="/zh/tier-list/">强度榜</a></p>',
    )
    update_text(
        ROOT / "currency-guide/index.html",
        '<p><a href="/best-banner-to-pull/">Best Banner to Pull On</a> · <a href="/best-beginner-team/">Best Beginner Team</a> · <a href="/how-to-get-stronger/">How to Get Stronger</a> · <a href="/beginner-guide/">Beginner Guide</a></p>',
        '<p><a href="/how-to-get-more-diamonds/">How to Get More Diamonds</a> · <a href="/best-use-of-diamonds/">Best Use of Diamonds</a> · <a href="/what-to-buy-in-shop/">What to Buy in Shop</a> · <a href="/best-banner-to-pull/">Best Banner to Pull On</a> · <a href="/beginner-guide/">Beginner Guide</a></p>',
    )
    update_text(
        ROOT / "zh/currency-guide/index.html",
        '<p><a href="/zh/best-banner-to-pull/">现在最值得抽哪个卡池</a> · <a href="/zh/best-beginner-team/">最佳开荒队伍</a> · <a href="/zh/how-to-get-stronger/">如何快速变强</a> · <a href="/zh/beginner-guide/">新手攻略</a></p>',
        '<p><a href="/zh/how-to-get-more-diamonds/">怎么获得更多钻石</a> · <a href="/zh/best-use-of-diamonds/">钻石最值得花在哪</a> · <a href="/zh/what-to-buy-in-shop/">商店里最值得买什么</a> · <a href="/zh/best-banner-to-pull/">现在最值得抽哪个卡池</a> · <a href="/zh/beginner-guide/">新手攻略</a></p>',
    )
    update_text(
        ROOT / "banners/index.html",
        '<li><a href="/best-banner-to-pull/">Best Banner to Pull On</a></li>',
        '<li><a href="/best-banner-to-pull/">Best Banner to Pull On</a></li><li><a href="/save-summons-or-pull-now/">Save Summons or Pull Now</a></li>',
    )
    update_text(
        ROOT / "zh/banners/index.html",
        '<li><a href="/zh/best-banner-to-pull/">现在最值得抽哪个卡池</a></li>',
        '<li><a href="/zh/best-banner-to-pull/">现在最值得抽哪个卡池</a></li><li><a href="/zh/save-summons-or-pull-now/">现在该抽还是继续存</a></li>',
    )
    update_text(
        ROOT / "beginner-guide/index.html",
        '<p><a href="/beginner-guide/all-characters-unlock/">All Characters List and How to Unlock (Launch Planning)</a></p>',
        '<p><a href="/f2p-beginner-guide/">F2P Beginner Guide</a></p><p><a href="/beginner-mistakes/">Beginner Mistakes Guide</a></p><p><a href="/launch-day-checklist/">Launch Day Checklist</a></p><p><a href="/beginner-guide/all-characters-unlock/">All Characters List and How to Unlock (Launch Planning)</a></p>',
    )
    update_text(
        ROOT / "zh/beginner-guide/index.html",
        '<p><a href="/zh/beginner-guide/all-characters-unlock/">全角色列表与解锁方式（开服规划）</a></p>',
        '<p><a href="/zh/f2p-beginner-guide/">零氪新手指南</a></p><p><a href="/zh/beginner-mistakes/">新手常见错误指南</a></p><p><a href="/zh/launch-day-checklist/">上线日清单</a></p><p><a href="/zh/beginner-guide/all-characters-unlock/">全角色列表与解锁方式（开服规划）</a></p>',
    )


def update_sitemap() -> None:
    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    additions = []
    for page in PAGES:
        for loc in (f"https://7sinsorigin.com/{page['slug']}/", f"https://7sinsorigin.com/zh/{page['slug']}/"):
            if loc not in text:
                additions.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>")
    if additions:
        text = text.replace("</urlset>", "\n" + "\n".join(additions) + "\n</urlset>")
    for hub in [
        "https://7sinsorigin.com/pre-register/",
        "https://7sinsorigin.com/how-to-link-accounts/",
        "https://7sinsorigin.com/systems/gacha-pity/",
        "https://7sinsorigin.com/currency-guide/",
        "https://7sinsorigin.com/beginner-guide/",
        "https://7sinsorigin.com/banners/",
        "https://7sinsorigin.com/zh/pre-register/",
        "https://7sinsorigin.com/zh/how-to-link-accounts/",
        "https://7sinsorigin.com/zh/systems/gacha-pity/",
        "https://7sinsorigin.com/zh/currency-guide/",
        "https://7sinsorigin.com/zh/beginner-guide/",
        "https://7sinsorigin.com/zh/banners/",
    ]:
        import re
        text = re.sub(
            rf"(<loc>{re.escape(hub)}</loc><lastmod>)([^<]+)(</lastmod>)",
            rf"\g<1>{TODAY}\g<3>",
            text,
        )
    sitemap.write_text(text, encoding="utf-8")


def main() -> int:
    write_pages()
    update_hubs()
    update_sitemap()
    print(f"Generated {len(PAGES) * 2} new mirrored pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
