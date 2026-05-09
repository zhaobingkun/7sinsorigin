# Google API SEO Setup

## 先说结论
- 不建议只给普通 `API key`
- 这类站点数据更稳的是 `service account`
- 真正分析流量最重要的是：
  - `searchconsole.googleapis.com`
  - `analyticsdata.googleapis.com`
- `analyticsadmin.googleapis.com` 主要用来确认属性和数据流配置，不是主分析来源

## 你需要准备什么
1. 一个 Google Cloud `service account`
2. 下载这个 service account 的 JSON 凭据文件
3. 把这个 service account 邮箱加入：
   - Search Console 站点资源，至少 `Restricted` 或更高权限
   - GA4 属性，至少 `Viewer` 权限

## 本项目里已经放好的文件
- 脚本：
  - [scripts/google_seo_audit.py](/Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin/scripts/google_seo_audit.py)
- 本地配置文件：
  - [scripts/google_api_config.json](/Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin/scripts/google_api_config.json)
- 环境变量示例：
  - [scripts/.env.google.example](/Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin/scripts/.env.google.example)

## 安装依赖
```bash
pip install google-api-python-client google-auth google-auth-httplib2
```

## 你需要填的 4 个值
默认直接改这个文件：

```json
{
  "GOOGLE_APPLICATION_CREDENTIALS": "/absolute/path/to/google-service-account.json",
  "GSC_SITE_URL": "https://7sinsorigin.com/",
  "GA4_PROPERTY_ID": "123456789",
  "SEO_AUDIT_DAYS": 90,
  "RUN_GSC": true,
  "RUN_GA4": false,
  "GSC_ROW_LIMIT": 5000,
  "HTTP_TIMEOUT_SECS": 120,
  "RUN_GA4_ADMIN": false
}
```

脚本会优先读 `scripts/google_api_config.json`。  
如果你以后想临时覆盖，也还能继续用环境变量。

## 怎么跑
```bash
cd /Users/zhaobingkun/dev/7sinsorigin.com/7sinsorigin
python3 scripts/google_seo_audit.py
```

如果你第一次跑就遇到超时，先保持：
- `RUN_GSC: true`
- `RUN_GA4: false`
- `RUN_GA4_ADMIN: false`
- `GSC_ROW_LIMIT: 5000`
- `HTTP_TIMEOUT_SECS: 120`

先只跑 Search Console。  
等基础数据跑通后，再把 `RUN_GA4` 改成 `true`，最后再决定要不要打开更重的 Admin 调用。

## 跑完会输出什么
会写到：
- `reports/gsc-query-page.csv`
- `reports/gsc-pages.csv`
- `reports/gsc-queries.csv`
- `reports/ga4-pages.csv`
- `reports/ga4-sources.csv`
- `reports/ga4-admin.json`
- `reports/seo-audit-summary.md`

## 我最想先看的字段

### Search Console
- `query`
- `page`
- `clicks`
- `impressions`
- `ctr`
- `position`

### GA4
- `pagePath`
- `deviceCategory`
- `sessions`
- `screenPageViews`
- `engagementRate`
- `averageSessionDuration`

## 拿到数据后怎么用
1. `impressions` 高但 `ctr` 低：
   - 改 `title`
   - 改 `meta description`
   - 看 SERP 意图是否跑偏

2. `position` 在 `8-20`：
   - 补内容
   - 补内链
   - 从新闻页反链到 evergreen 页

3. 有流量但 `engagementRate` 低：
   - 改首屏
   - 改目录结构
   - 把答案提前

4. 新页没展示：
   - 查收录
   - 查 sitemap
   - 查主题是否太薄

## 如果你不想直接给我密钥
最稳的做法是：
1. 你自己本地填好 `scripts/google_api_config.json`
2. 你自己跑脚本
3. 把 `reports/` 目录里的 CSV / MD 发我
4. 我根据真实数据继续给你改站

## 如果你想直接让我分析
你可以给我这几种东西之一：
- `reports/seo-audit-summary.md`
- `reports/gsc-query-page.csv`
- `reports/ga4-pages.csv`
- 或者整个 `reports/` 目录
