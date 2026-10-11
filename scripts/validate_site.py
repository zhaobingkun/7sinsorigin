#!/usr/bin/env python3
"""Read-only static release gate. Technical checks are not an AdSense verdict."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from content_policy import POLICY, ROOT, ORIGIN, path_info, transform


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.h1 = 0
        self.meta = {}
        self.canonical = []
        self.alternates = {}
        self.refs = []
        self.images = []
        self.title = ''
        self.in_title = False
        self.ids = set()
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self.in_title = True
        if tag == 'meta': self.meta[a.get('name', a.get('property', ''))] = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical.append(a.get('href'))
        if tag == 'link' and a.get('rel') == 'alternate': self.alternates[a.get('hreflang')] = a.get('href')
        if tag in ('a', 'link') and a.get('href'): self.refs.append(a['href'])
        if tag in ('img', 'script') and a.get('src'): self.refs.append(a['src'])
        if tag == 'img': self.images.append(a)

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False

    def handle_data(self, data):
        if self.in_title: self.title += data


def local_target(href, source):
    url = urlsplit(href)
    if url.scheme not in ('', 'http', 'https') or (url.netloc and url.netloc != '7sinsorigin.com'):
        return None
    pathname = unquote(url.path)
    target = ROOT / pathname.lstrip('/') if pathname.startswith('/') else source.parent / pathname
    if not pathname: target = source
    elif target.is_dir(): target /= 'index.html'
    return target, unquote(url.fragment)


def validate():
    errors = []
    pages = {}
    titles, descriptions = defaultdict(list), defaultdict(list)
    sources = {}
    for path in sorted(ROOT.rglob('index.html')):
        if '.git' in path.parts: continue
        source = path.read_text()
        pages[path] = Page(source)
        sources[path] = source
    sitemap = ET.parse(ROOT / 'sitemap.xml')
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [item.text for item in sitemap.findall('s:url/s:loc', ns)]
    if len(urls) != len(set(urls)): errors.append('Duplicate sitemap URLs')
    for url in urls:
        target = local_target(url, ROOT / 'index.html')
        if not target or target[0] not in pages: errors.append('Missing sitemap target: ' + url)
        elif 'noindex' in pages[target[0]].meta.get('robots', ''): errors.append('Noindex URL in sitemap: ' + url)
    for path, page in pages.items():
        route, base, zh = path_info(path)
        label = path.relative_to(ROOT).as_posix()
        noindex = 'noindex' in page.meta.get('robots', '')
        merged = base in POLICY['merged']
        expected = ORIGIN + route
        if merged:
            dest = POLICY['merged'][base]
            expected = ORIGIN + ('/zh/' if zh else '/') + (dest + '/' if dest else '')
        if page.h1 != 1: errors.append(f'{label}: H1 count {page.h1}')
        if page.canonical != [expected]: errors.append(f'{label}: canonical {page.canonical}, expected {expected}')
        mirror = ROOT / (base + '/index.html' if base else 'index.html') if zh else ROOT / 'zh' / (base + '/index.html' if base else 'index.html')
        if mirror not in pages: errors.append(f'{label}: missing language mirror')
        en_base = POLICY['merged'][base] if merged else base
        en = ORIGIN + '/' + (en_base + '/' if en_base else '')
        cn = ORIGIN + '/zh/' + (en_base + '/' if en_base else '')
        for lang, target in [('en', en), ('zh', cn), ('x-default', en)]:
            if page.alternates.get(lang) != target: errors.append(f'{label}: incorrect hreflang {lang}')
        for tag in ('description', 'viewport', 'robots', 'og:title', 'og:description', 'og:url', 'og:image', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image'):
            if not page.meta.get(tag): errors.append(f'{label}: missing {tag}')
        if page.meta.get('og:url') != expected: errors.append(f'{label}: OG URL does not match canonical')
        schemas = re.findall(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', sources[path], re.I | re.S)
        if not schemas: errors.append(f'{label}: no JSON-LD')
        for schema in schemas:
            try: json.loads(schema)
            except json.JSONDecodeError as exc: errors.append(f'{label}: invalid JSON-LD {exc}')
        if any('alt' not in img for img in page.images): errors.append(f'{label}: image missing alt')
        if transform(path, sources[path]) != sources[path]: errors.append(f'{label}: content-policy drift')
        if not noindex:
            titles[page.title.strip()].append(label)
            descriptions[page.meta.get('description', '').strip()].append(label)
            if ORIGIN + route not in urls: errors.append(f'{label}: indexable URL missing from sitemap')
        for ref in page.refs:
            local = local_target(ref, path)
            if not local: continue
            target, fragment = local
            if not target.exists(): errors.append(f'{label}: missing local reference {ref}')
            elif fragment and target in pages and fragment not in pages[target].ids:
                errors.append(f'{label}: missing fragment {ref}')
    for kind, values in [('title', titles), ('description', descriptions)]:
        for value, paths in values.items():
            if len(paths) > 1: errors.append(f'Duplicate indexable {kind}: {paths}')
    runtime_sources = list(sources.values()) + [p.read_text() for p in (ROOT / 'assets/js').glob('*.js')]
    if any('adsbygoogle' in src or 'pagead2.googlesyndication' in src for src in runtime_sources) and not POLICY['ads_enabled']:
        errors.append('Ad runtime is disabled by policy but a loader/request remains')
    for path in [ROOT / 'index.html', ROOT / 'zh/index.html']:
        if pages[path].meta.get('google-adsense-account') != POLICY['publisher']:
            errors.append(f'{path.name}: ownership verification missing')
    if 'pub-6428701926694635' not in (ROOT / 'ads.txt').read_text(): errors.append('ads.txt publisher mismatch')
    config = json.loads((ROOT / 'vercel.json').read_text())
    redirects = config.get('redirects', [])
    expected_redirects = set()
    for base, dest in POLICY['merged'].items():
        if dest in POLICY['merged']: errors.append(f'Redirect chain in policy: {base} -> {dest}')
        for prefix in ('/', '/zh/'):
            expected_redirects.add((prefix + base + '/:path*', prefix + (dest + '/' if dest else ''), True))
    actual_redirects = {(r.get('source'), r.get('destination'), r.get('permanent')) for r in redirects}
    if len(redirects) != len(actual_redirects) or actual_redirects != expected_redirects:
        errors.append('Vercel redirects differ from reviewed content-policy routes')
    for path, page in pages.items():
        _, base, _ = path_info(path)
        if base not in POLICY['merged']:
            if 'data-menu-btn' not in sources[path]: errors.append(f'{path}: missing mobile menu button')
            if 'data-privacy-settings' not in sources[path]: errors.append(f'{path}: missing privacy settings entry')
    print(f'Checked {len(pages)} HTML pages; {len(urls)} unique sitemap URLs; {len(errors)} errors')
    for error in errors[:100]: print(error)
    return errors


if __name__ == '__main__':
    sys.exit(bool(validate()))
