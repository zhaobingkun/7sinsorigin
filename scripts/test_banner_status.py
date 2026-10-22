"""Read-only bilingual banner-status regression; optional review-scope baseline."""
import json
import os
import re
import subprocess
import unittest
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path

from validate_site import Page

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ['banners/upcoming/index.html', 'zh/banners/upcoming/index.html']
BASELINE = os.environ.get('SEO_REVIEW_BASELINE')

def old(name):
    return subprocess.check_output(['git', 'show', f'{BASELINE}:{name}'], cwd=ROOT)

def map_urls(text):
    return {node.find('{*}loc').text: node.findtext('{*}lastmod') for node in ET.fromstring(text)}

class BannerStatusTests(unittest.TestCase):
    def test_bilingual_identity_and_review_date(self):
        for name in TARGETS:
            with self.subTest(name=name):
                text = (ROOT / name).read_text()
                page = Page(text)
                self.assertEqual(page.h1, 1)
                self.assertNotIn('noindex', page.meta['robots'])
                self.assertEqual(page.canonical, ['https://7sinsorigin.com/' + name.replace('index.html', '')])
                self.assertEqual(page.alternates['en'], 'https://7sinsorigin.com/banners/upcoming/')
                self.assertEqual(page.alternates['zh'], 'https://7sinsorigin.com/zh/banners/upcoming/')
                date = re.search(r'<time datetime="([^"]+)"', text)[1]
                article = next(x for x in self.schemas(text) if x['@type'] == 'Article')
                self.assertEqual(article['dateModified'], date)

    @staticmethod
    def schemas(text):
        return [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)]

    def test_visible_faq_and_schema_match(self):
        for name in TARGETS:
            text = (ROOT / name).read_text()
            visible = [(unescape(q), unescape(a)) for q, a in re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', text, re.S)]
            schema = next(x for x in self.schemas(text) if x['@type'] == 'FAQPage')
            expected = [(x['name'], x['acceptedAnswer']['text']) for x in schema['mainEntity']]
            self.assertEqual(visible, expected, name)
            self.assertGreaterEqual(len(visible), 1, name)

    def test_status_rows_and_parallel_next_checks(self):
        routes = []
        for name in TARGETS:
            text = (ROOT / name).read_text()
            status = text.split('id="next-banner-status"')[1].split('</tbody>')[0]
            values = re.findall(r'data-status="([^"]+)"', status)
            self.assertEqual(len(values), 4, name)
            self.assertTrue(all(x in ['confirmed', 'unannounced'] for x in values), name)
            checks = re.search(r'<ul id="next-checks">(.*?)</ul>', text, re.S)[1]
            links = re.findall(r'href="([^"]+)"', checks)
            self.assertEqual(len(links), 4, name)
            prefix = '/zh/' if name.startswith('zh/') else '/'
            self.assertTrue(all(x.startswith(prefix) for x in links), name)
            routes.append([x[len(prefix):] for x in links])
        self.assertEqual(routes[0], routes[1])

    @unittest.skipUnless(BASELINE, 'Set SEO_REVIEW_BASELINE for this release scope check')
    def test_only_selected_html_and_sitemap_dates_changed(self):
        names = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', BASELINE], cwd=ROOT).decode().splitlines()
        for name in names:
            if (name.endswith('.html') and name not in TARGETS) or name in ['content-policy.json', 'vercel.json', '_redirects', 'robots.txt', 'ads.txt', 'assets/js/site.js', 'assets/css/site.css']:
                self.assertEqual((ROOT / name).read_bytes(), old(name), name)
        before, after = map_urls(old('sitemap.xml')), map_urls((ROOT / 'sitemap.xml').read_text())
        self.assertEqual(set(before), set(after))
        for url in before:
            if url.endswith('/banners/upcoming/'):
                self.assertEqual(after[url], '2026-10-22')
            else:
                self.assertEqual(after[url], before[url], url)
        for name in TARGETS:
            before_page, after_page = Page(old(name).decode()), Page((ROOT / name).read_text())
            self.assertEqual(before_page.title, after_page.title, name)
            self.assertEqual(before_page.meta['robots'], after_page.meta['robots'], name)
            self.assertEqual(before_page.canonical, after_page.canonical, name)

if __name__ == '__main__':
    unittest.main(verbosity=2)
