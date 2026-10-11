#!/usr/bin/env python3
"""Read-only content triage. Flags require editorial review; counts are not Google rules."""
import argparse
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDITORIAL_PATTERNS = (
    r"high.intent", r"search intent", r"search traffic", r"pages? work because",
    r"this page matters", r"why this page", r"traffic is", r"search volume",
    r"这页.*搜索", r"高意图", r"搜索流量", r"搜索意图", r"这类页面.*价值",
)


class Body(HTMLParser):
    def __init__(self):
        super().__init__()
        self.main = False
        self.hidden = 0
        self.anchor = 0
        self.text = []
        self.link_text = []
        self.paragraphs = []
        self.in_p = False
        self.current_p = []
        self.links = []
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta':
            self.meta[attrs.get('name', attrs.get('property', ''))] = attrs.get('content', '')
        if tag == 'main': self.main = True
        if tag in ('script', 'style'): self.hidden += 1
        if self.main and tag == 'a':
            self.anchor += 1
            self.links.append(attrs.get('href', ''))
        if self.main and tag == 'p': self.in_p, self.current_p = True, []

    def handle_endtag(self, tag):
        if tag == 'main': self.main = False
        if tag in ('script', 'style'): self.hidden = max(0, self.hidden - 1)
        if tag == 'a': self.anchor = max(0, self.anchor - 1)
        if tag == 'p' and self.in_p:
            self.paragraphs.append(' '.join(self.current_p))
            self.in_p = False

    def handle_data(self, value):
        if self.main and not self.hidden:
            value = ' '.join(value.split())
            if value:
                self.text.append(value)
                if self.anchor: self.link_text.append(value)
                if self.in_p: self.current_p.append(value)


def inventory():
    records = []
    for path in sorted(ROOT.rglob('index.html')):
        if '.git' in path.parts: continue
        html = path.read_text()
        body = Body()
        body.feed(html)
        text = ' '.join(body.text)
        noindex = 'noindex' in body.meta.get('robots', '')
        ads = 'pagead/js/adsbygoogle.js' in html
        flags = []
        if noindex and ads: flags.append('noindex-with-ad-loader')
        if any(re.search(pattern, text, re.I) for pattern in EDITORIAL_PATTERNS):
            flags.append('publisher-planning-copy')
        ratio = len(' '.join(body.link_text)) / max(1, len(text))
        if ratio > .45: flags.append('navigation-heavy')
        route = '/' + str(path.relative_to(ROOT).parent).strip('.') + '/'
        route = route.replace('//', '/')
        records.append(dict(route=route, chars=len(text), words=len(text.split()),
                            noindex=noindex, ads=ads, flags=flags,
                            paragraphs=body.paragraphs, links=body.links))
    return records


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    records = inventory()
    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
    else:
        print(f"HTML pages: {len(records)}; indexable: {sum(not r['noindex'] for r in records)}")
        print('Flags (triage signals, not policy verdicts):', dict(Counter(f for r in records for f in r['flags'])))
        for row in records:
            if row['flags']:
                print(row['route'], row['chars'], ', '.join(row['flags']))
