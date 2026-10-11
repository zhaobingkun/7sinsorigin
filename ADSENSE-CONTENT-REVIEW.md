# AdSense 第二次低价值内容复查

复查日期：2026-10-11（Asia/Shanghai）。用户反馈仍因“低价值内容”未通过审核。

下方基线保留最初诊断的证据。用户随后授权全站整改；实施记录见本文件末尾。报告不是 Google 的逐页判定，未读取登录后的审核详情，未提交复审。

## 结论

9 月 26 日的整改主要补充编辑政策、来源说明，并排除 21 组薄页；核心攻略是否真正回答标题承诺的问题，仍未得到系统解决。不能把页面数量、字数、noindex 或技术 SEO 合格当作 AdSense 内容质量合格的替代证据。

## 可复核证据

1. `tier-list/index.html:54` 声称会给角色排名，但 S/A/B 三栏（72–74 行）只有等级定义，没有任何角色归属、版本测试条件或排名证据。主入口仍导向 6 月快照。线上 `/tier-list/` 也可见同样内容。
2. `beginner-guide/cooking/index.html:65` 解释的是“烹饪页面为什么有用”，正文没有列出可照做的配方、材料数量或效果。钓鱼页以及 5/6 月强度、平民配队、新手配队页也需要人工检查标题与交付是否匹配，不能只补长度。
3. `index.html:80`、`:199`、`:366` 公开展示了 `Current Search Intent`、`List Capacity: Top 15 (Expandable)`、`your provided screenshots` 等策划语句。首页当前入口混入大量旧内容，`:422` 仍以 Version 2.1/Khala 描述当前覆盖范围，与已经发布的 2.2 路由不一致。
4. `best-banner-to-pull/index.html` 与中文镜像仍是 `noindex`，但重新带有 AdSense loader。它们是上轮排除策略的回归，不代表 noindex 本身能解决审核问题，也不能据 loader 推断广告已经实际展示。
5. 官方 Netmarble `id 327` 的实时 API 正文确认：80 抽内 SSR、SSR 的 Pick Up 概率 50%、歪后下一 SSR 必定 Pick Up、SSR 计数和定向保证可继承，以及每池一次的 120 抽额外奖励（其进度不跨池，提前获得角色也不重置）。本地 Lancelot 新闻和抽卡决策页没有完整解释后两类进度差异。任何预算案例都必须同时考虑 120 抽奖励，不能简单把 80+80 当作唯一最坏预算。

官方公告：[Lancelot Pick Up & Exclusive Skin](https://7origin.netmarble.com/en/news/8/327)。本轮只核验该公告作为内容样本，没有执行完整的每日新公告检查，不能据此声称今天没有官方更新。

## 全站扫描基线

运行 `python3 scripts/audit_content_quality.py`：

- 446 个 HTML 页面，404 个未标注 noindex。
- 62 页匹配策划/搜索意图类词句，7 页链接文字占比偏高，2 页同时存在 noindex 与广告 loader。
- 这些是人工复核候选，不是 62 个违规页面。Hub 的链接密度可能合理；中文与英文的字符数也不可直接比较。脚本不评估 Google 审核结果，不修改网页。

## 原整改顺序（已获授权实施）

1. 清理首页当前入口、策划话术和陈旧版本表述；保留可达的新闻历史归档，不把旧攻略当作当前结论。
2. 强度榜如没有真实排名证据，改为诚实的养成决策指南；不要虚构角色排名或声称做过实测。
3. 对同一问题的多张抽卡/配队薄页逐页选择充实或合并。合并前明确规范 URL、EN/ZH 对应关系、内链和重定向；不批量删除历史新闻或仅按字数 noindex。
4. 优先重做少量真正可用的内容：官方规则支持的预算计算、活动剩余收益与截止时间、具体平台报错的排查分支。攻略需要实测时，收集版本、设备、阵容/装备和结果，缺资料就明确暂不提供结论。
5. 将人工排除清单和广告/索引检查加入发布流程，避免自动更新重新挂广告或恢复 sitemap；保留必要的网站所有权验证。
6. 完成内容整改后再验证 HTML、链接、SEO、索引/广告策略和线上发布，再决定是否申请复审。没有固定页数/字数可以保证通过。

## 官方政策依据

- [AdSense：网站尚未准备好展示广告](https://support.google.com/adsense/answer/12176698?hl=en)：要求有价值的独特内容、良好体验和导航，解决问题后再申请审核。
- [Google Publisher Policies：复制内容](https://support.google.com/publisherpolicies/answer/11190248?hl=en)：仅改写/转载，缺少额外评论、整理或价值，并不满足相应广告政策。引用官方公告本身不是问题，关键是本页是否提供了实质增量。

以上是最初诊断阶段的状态；后续实施如下。

## October 11, 2026 — substantive content remediation

User authorization: after reporting the repeated AdSense low-value rejection, the user requested “还有什么要改的，一次改好”, then “继续”. This supersedes the earlier diagnostic-only status. Google approval is not guaranteed; no AdSense re-review or account setting was submitted.

- Rebuilt EN/ZH home, beginner/character/system/issue hubs, codes and event/resource guides. Replaced unsupported tier placements with an explicitly non-ranking investment guide; team planning now documents failure diagnosis and upgrade stop conditions without invented team tests.
- Added complete current Pick Up rules and six worked budgets: SSR pity, featured guarantee and each banner's separate one-time 120th Draw Bonus. Corrected Elaine's October 8 event-name revision to Whispers of the Wind. No invented conversion prices, drop rates or comparative DPS claims.
- Reviewed manual policy: 18 route pairs merged, 42 incomplete draft pairs withdrawn, 29 historical/reference pairs preserved with archive warnings. All are noindex and excluded from sitemap; old news remains dated history. With existing utility exclusions, 446 HTML pages remain and 248 unique indexable sitemap URLs remain. This is manual editorial triage, not a character-count threshold.
- Official new fact: article 339, Regarding Knighthood Boss Battle Ranking Issues, published/modified 2026-10-10 09:37:29 UTC (1791625049549). Integrated into existing Knighthood EN/ZH pages and home/news/bugs discovery. Measures are under review; no reset, cancellation or compensation is confirmed. Timespace article 324 is a separate issue; rechecked its October 8 API revision (1791425178816) and retained the October 28 14:59 UTC mailbox deadline.
- Removed advertising runtime across the entire site; kept homepage AdSense ownership metadata and ads.txt. The local privacy panel controls Analytics only and is not a certified advertising CMP. Do not restore advertising before a separately reviewed consent setup.
- Added content-policy.json, read-only validation, a mechanical --apply enforcement option, Vercel permanent redirects, deployment-file exclusions and a GitHub quality workflow. Retired the three historical page generators to prevent overwriting reviewed content. Read agents.md and use sh scripts/release_check.sh before every publication.
- Static validation has passed all 446 pages: one H1, canonical/hreflang, OG/Twitter, JSON-LD, images, local targets/fragments, unique indexable titles/descriptions, exact sitemap inclusion and policy/redirect consistency. Diff check, XML check and JS syntax check pass. Desktop/mobile QA checked home/menu, events, budget tables and Chinese leaderboard layout; no viewport overflow at 390 px. Publication/live verification is a separate release step, not implied by these local results.
