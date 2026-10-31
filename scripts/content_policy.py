#!/usr/bin/env python3
"""Enforce manually reviewed publication decisions; never score content by length.

Default is read-only. --apply performs mechanical metadata/navigation cleanup,
withdraws explicitly listed drafts, and creates redirect fallbacks. Source edits
and new editorial decisions belong in reviewed patches, not this utility.
"""
import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://7sinsorigin.com'
POLICY = json.loads((ROOT / 'content-policy.json').read_text())
GENERATED_DIRS = {'.git', 'dist'}
DATE = POLICY['reviewed']
AD_RE = re.compile(r'<script\b[^>]*src=["\'][^"\']*(?:adsbygoogle|pagead2\.googlesyndication)[^"\']*["\'][^>]*>.*?</script>', re.I | re.S)
ANCHOR_RE = re.compile(r'<a\b(?P<before>[^>]*?)href=["\'](?P<href>[^"\']+)["\'](?P<after>[^>]*)>(?P<label>.*?)</a>', re.I | re.S)


def path_info(path):
    route = '/' + path.parent.relative_to(ROOT).as_posix().strip('.') + '/'
    route = route.replace('//', '/')
    zh = route.startswith('/zh/')
    base = route[4:] if zh else route[1:]
    return route, base.strip('/'), zh


def meta(text, key, value, attr='name'):
    tag = f'<meta {attr}="{key}" content="{html.escape(value, quote=True)}">'
    pattern = rf'<meta\b(?=[^>]*\b{attr}=["\']{re.escape(key)}["\'])[^>]*>'
    if re.search(pattern, text, re.I):
        return re.sub(pattern, lambda _: tag, text, flags=re.I)
    return text.replace('</head>', tag + '\n</head>', 1)


def title_of(text):
    match = re.search(r'<title>(.*?)</title>', text, re.S | re.I)
    return html.unescape(match[1]) if match else '7DS Origin'


def update_identity(text, title, description):
    text = re.sub(r'<title>.*?</title>', lambda _: '<title>' + html.escape(title) + '</title>', text, count=1, flags=re.S | re.I)
    for key, value, attr in [('description', description, 'name'), ('og:title', title, 'property'), ('og:description', description, 'property'), ('twitter:title', title, 'name'), ('twitter:description', description, 'name')]:
        text = meta(text, key, value, attr)
    def schema(match):
        data = json.loads(match[1])
        nodes = data if isinstance(data, list) else [data]
        for node in nodes:
            if not isinstance(node, dict):
                continue
            node['name' if 'name' in node else 'headline'] = title
            node['description'] = description
            node['dateModified'] = DATE
        return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'
    return re.sub(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', schema, text, flags=re.S | re.I)


def nav(zh, route):
    prefix = '/zh/' if zh else '/'
    pairs = [('', '首页', 'Home'), ('banners/current/', '当前卡池', 'Banners'), ('tier-list/', '养成决策', 'Investment'), ('beginner-guide/', '攻略', 'Guides'), ('events-schedule/', '活动', 'Events'), ('news/', '公告', 'News')]
    links = ''.join(f'<a href="{prefix}{slug}">{cn if zh else en}</a>' for slug, cn, en in pairs)
    other = route[3:] if zh else '/zh' + route
    links += f'<a href="{other}" lang="{"en" if zh else "zh"}">{"English" if zh else "中文"}</a>'
    return '<nav class="nav-links">' + links + '</nav>'


def transform(path, text):
    route, base, zh = path_info(path)
    prefix = '/zh/' if zh else '/'
    # Changed privacy/layout code must not be hidden by an older browser cache.
    version = DATE.replace('-', '')
    text = re.sub(r'(/assets/(?:js/site\.js|css/site\.css))(?:\?v=[^"\']*)?', lambda m: m[1] + '?v=' + version, text)
    text = AD_RE.sub('', text) if not POLICY['ads_enabled'] else text
    # Remove launch-era and other-game destinations from shared footers.
    text = text.replace('https://x.com/netmarbleglobal', 'https://x.com/7DSO_EN')
    text = re.sub(r'<a\b[^>]*href=["\']https://7origin\.netmarble\.com/preorder["\'][^>]*>.*?</a>', '', text, flags=re.S | re.I)
    text = re.sub(r'<a\b[^>]*href=["\']https://(?:www\.)?reddit\.com/r/SDSGrandCross/?["\'][^>]*>.*?</a>', '', text, flags=re.S | re.I)
    if base in POLICY['merged']:
        target = prefix + POLICY['merged'][base].strip('/')
        target = target.rstrip('/') + '/' if target != '/' else target
        title = ('页面已合并：' if zh else 'Page merged: ') + base
        label = '前往完整指南' if zh else 'Open the consolidated guide'
        return f'''<!doctype html>
<html lang="{'zh-CN' if zh else 'en'}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)}</title><meta name="description" content="{label}"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="{ORIGIN}{target}"><link rel="alternate" hreflang="en" href="{ORIGIN}/{'%s/' % POLICY['merged'][base] if POLICY['merged'][base] else ''}"><link rel="alternate" hreflang="zh" href="{ORIGIN}/zh/{'%s/' % POLICY['merged'][base] if POLICY['merged'][base] else ''}"><link rel="alternate" hreflang="x-default" href="{ORIGIN}/{'%s/' % POLICY['merged'][base] if POLICY['merged'][base] else ''}"><meta property="og:title" content="{html.escape(title, quote=True)}"><meta property="og:description" content="{label}"><meta property="og:url" content="{ORIGIN}{target}"><meta property="og:image" content="{ORIGIN}/assets/img/brand/logo-mark.png"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{html.escape(title, quote=True)}"><meta name="twitter:description" content="{label}"><meta name="twitter:image" content="{ORIGIN}/assets/img/brand/logo-mark.png"><link rel="stylesheet" href="/assets/css/site.css"><link rel="icon" href="/assets/img/brand/favicon-32.png"><script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@type':'WebPage','name':title,'url':ORIGIN+target},ensure_ascii=False)}</script></head><body><main><section class="page-head"><div class="container"><h1>{html.escape(title)}</h1><p><a href="{target}">{label}</a></p></div></section></main></body></html>
'''
    if base in POLICY['withdrawn']:
        # These are undated incomplete drafts, not official historical notices.
        original = re.sub(r'^(Withdrawn draft: |已撤下草稿：)', '', title_of(text))
        title = ('已撤下草稿：' if zh else 'Withdrawn draft: ') + original
        description = ('旧草稿缺少可验证的具体步骤或实测依据，已撤下，不作为当前攻略。' if zh else 'This incomplete draft has been withdrawn because the promised instructions were not verified. It is not a current guide.')
        reason = ('旧稿未能提供与标题相符的可验证步骤、数据或测试条件。本站不再把它作为当前攻略，也不会补写没有证据的配方、位置、阵容或账号操作。' if zh else POLICY['withdrawn'][base])
        main = f'<main><section class="page-head"><div class="container"><h1>{html.escape(title)}</h1><p>{description}</p><p>{html.escape(reason)}</p><p>{"2026 年 10 月 11 日编辑复核：确认资料完整后才会重新发布。旧稿可从项目版本历史恢复。" if zh else "Editorial review, October 11, 2026: republication requires substantive evidence. The previous draft remains recoverable in project version history."}</p><p><a href="{prefix}beginner-guide/">{"已复核指南" if zh else "Reviewed guides"}</a> · <a href="{prefix}news/">{"官方公告资料" if zh else "Official-source news archive"}</a> · <a href="{prefix}contact/">{"提供更正资料" if zh else "Send a correction"}</a></p></div></section></main>'
        text = re.sub(r'<main\b[^>]*>.*?</main>', lambda _: main, text, count=1, flags=re.S | re.I)
        text = update_identity(text, title, description)
        text = meta(text, 'robots', 'noindex,follow,max-image-preview:large')
        if 'application/ld+json' not in text:
            data = {'@context': 'https://schema.org', '@type': 'WebPage', 'name': title, 'description': description, 'url': ORIGIN + route, 'dateModified': DATE}
            text = text.replace('</head>', '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>\n</head>', 1)
    elif base in POLICY['archives']:
        original = re.sub(r'^(Archive: |历史存档：)', '', title_of(text))
        title = ('历史存档：' if zh else 'Archive: ') + original
        description = ('历史资料，不代表当前版本强度、数值或可用性。请先查看当前公告和已复核指南。' if zh else 'Historical reference, not a verified current-version ranking, value, or availability guide. Check current official notices before using it.')
        text = update_identity(text, title, description)
        text = meta(text, 'robots', 'noindex,follow,max-image-preview:large')
        if 'data-editorial-archive' not in text:
            note = ('<strong>历史存档，不是当前攻略。</strong> 本页保留旧版本资料；未记录的实测条件或截图版本不能作为当前角色强度、配方或装备数值的证据。' if zh else '<strong>Historical archive, not a current guide.</strong> Original patch/reference material is retained below. Missing test conditions or screenshot build dates mean it is not evidence for current rankings, recipes, or equipment values.')
            text = re.sub(r'(<main\b[^>]*>)', lambda m: m[1] + f'<section class="section" data-editorial-archive><div class="container"><p>{note}</p><p><a href="{prefix}beginner-guide/">{"当前已复核入口" if zh else "Reviewed current guides"}</a></p></div></section>', text, count=1, flags=re.I)
    elif base in POLICY.get('reinstated', []):
        text = meta(text, 'robots', 'index,follow,max-image-preview:large')
    # Keep archived bodies intact; only public navigation/ad plumbing is shared.
    text = re.sub(r'<nav\b[^>]*class=["\']nav-links["\'][^>]*>.*?</nav>', lambda _: nav(zh, route), text, count=1, flags=re.S | re.I)
    if 'data-menu-btn' not in text and '<nav class="nav-links">' in text:
        button = '<button class="menu-btn" type="button" data-menu-btn>' + ('菜单' if zh else 'Menu') + '</button>'
        text = text.replace('<nav class="nav-links">', button + '<nav class="nav-links">', 1)
    if route in ('/', '/zh/'):
        text = meta(text, 'google-adsense-account', POLICY['publisher'])
    if 'data-privacy-settings' not in text and '</footer>' in text:
        text = text.replace('</footer>', '<p class="container small"><button class="privacy-link-button" type="button" data-privacy-settings>' + ('隐私选择' if zh else 'Privacy choices') + '</button></p></footer>', 1)
    labels = {'tier-list': ('养成优先级', 'Investment priorities'), 'beginner-guide/best-team-comps': ('配队规划', 'Team planning'), 'currency-guide': ('资源预算', 'Currency budget'), 'daily-checklist': ('日常与周常检查清单', 'Daily and weekly checklist'), 'current-banner-worth-it': ('抽卡预算与选择', 'Pull budget and decisions'), 'systems/raid-rewards-and-weekly-prep': ('Raid 奖励与准备', 'Raid rewards and preparation'), 'characters': ('官方角色资料入口', 'Official hero announcements'), '': ('首页', 'Home')}
    def links(match):
        href = html.unescape(match['href'])
        local = href[len(ORIGIN):] if href.startswith(ORIGIN + '/') else href
        if not local.startswith('/') or local.startswith('//'):
            return match[0]
        bare = local.split('#')[0].split('?')[0]
        lzh = bare.startswith('/zh/')
        slug = bare[4:].strip('/') if lzh else bare.strip('/')
        if slug in POLICY['merged']:
            dest = POLICY['merged'][slug]
            new = ('/zh/' if lzh else '/') + (dest + '/' if dest else '')
            suffix = local[len(bare):]
            label = labels.get(dest, ('完整指南', 'Consolidated guide'))[0 if lzh else 1]
            return '<a' + match['before'] + 'href="' + new + suffix + '"' + match['after'] + '>' + label + '</a>'
        if slug == 'tier-list':
            return '<a' + match['before'] + 'href="' + href + '"' + match['after'] + '>' + labels[slug][0 if lzh else 1] + '</a>'
        if base not in POLICY['archives'] and base not in POLICY['withdrawn'] and not base.startswith('news/2026/') and (slug in POLICY['withdrawn'] or slug in POLICY['archives']):
            return '<span class="small">' + match['label'] + ('（未复核存档）' if zh else ' (unverified archive)') + '</span>'
        return match[0]
    return re.sub(r'[ \t]+$', '', ANCHOR_RE.sub(links, text), flags=re.M)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    changed = []
    for path in sorted(ROOT.rglob('index.html')):
        if any(part in GENERATED_DIRS for part in path.parts):
            continue
        original = path.read_text()
        updated = transform(path, original)
        if original != updated:
            changed.append(path.relative_to(ROOT).as_posix())
            if args.apply:
                path.write_text(updated)
    print(('Applied' if args.apply else 'Policy drift in'), len(changed), 'HTML pages')
    if not args.apply and changed:
        print('\n'.join(changed[:25]))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
