#!/usr/bin/env python3
"""Export a self-contained reading HTML to a public, portable interactive edition.

Usage: python3 scripts/import-reading.py --html /path/to/reviewed.html
       --slug commanding-heights --source-url https://example.com/
       --pdf-url https://example.com/report.pdf --published-at YYYY-MM-DD

Exports only the selected HTML, extracted inline images and a provenance manifest.
It does not upload original PDFs, full translations or files from the input folder.
"""
import argparse
from datetime import date
import base64
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlparse


def export(args):
    date.fromisoformat(args.published_at)
    root = Path(__file__).resolve().parents[1]
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.slug):
        raise ValueError('Use a lowercase, hyphenated slug.')
    for url in [args.source_url, args.pdf_url, args.site_url]:
        if urlparse(url).scheme != 'https' or not urlparse(url).netloc:
            raise ValueError('Public source and site URLs must use HTTPS.')
    source_path = Path(args.html)
    raw = source_path.read_text()
    text = raw
    article = f'/reading/{args.slug}/'
    output = root / 'static' / 'reading' / args.slug / 'explore'
    media = output / 'media'
    media.mkdir(parents=True, exist_ok=True)
    images = {}

    def image(match):
        mime, encoded = match.groups()
        payload = base64.b64decode(encoded)
        digest = hashlib.sha256(payload).hexdigest()[:16]
        filename = f'{digest}.{"jpg" if mime == "jpeg" else mime}'
        (media / filename).write_bytes(payload)
        images[filename] = hashlib.sha256(payload).hexdigest()
        return f'src="media/{filename}"'

    text = re.sub(r'src="data:image/(jpeg|png|webp);base64,([A-Za-z0-9+/=]+)"', image, text)

    class Links(HTMLParser):
        def __init__(self):
            super().__init__()
            self.hrefs = set()

        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                self.hrefs.add(dict(attrs).get('href', ''))

    links = Links()
    links.feed(text)
    for href in links.hrefs:
        if href.startswith(('#', 'https://', 'http://', 'mailto:')):
            continue
        if href.split('#', 1)[0].endswith('.pdf'):
            destination = args.pdf_url + (('#' + href.split('#', 1)[1]) if '#' in href else '')
        elif href.endswith('.md'):
            name = unquote(href)
            destination = article + '#evidence-audit' if '核对' in name else (args.source_url if '英文' in name else article + '#bilingual-reading')
        else:
            raise ValueError(f'Unmapped local link: {href}')
        text = text.replace(f'href="{href}"', f'href="{destination}"')

    text = text.replace('class="wordmark" href="#top"', f'class="wordmark" href="{article}"')
    text = re.sub(r'<strong>[^<]+</strong><span>原文深读</span>', '<strong>精读</strong><span>返回文章</span>', text, count=1)
    text = text.replace('你提供的英文 PDF', '英文原版 PDF').replace('你提供的 PDF', '英文原版 PDF').replace('已提供的 PDF', '英文原版 PDF')
    text = text.replace('基于用户提供的英文 PDF 制作；未以中文编译文章为分析依据。', f'依据英文原作独立解读；公开版整理于 {args.published_at}。')
    text = text.replace('英文摘自已提供的', '英文摘自')
    text = text.replace('完整英文 Markdown ↗', '英文原作网页 ↗').replace('完整中文初译 ↗', '返回精读文章 ↗')
    text = text.replace('核对记录.md', article + '#evidence-audit')
    text = text.replace('查看完整核对记录 ↗', '查看文章核对说明 ↗')
    canonical = f'{args.site_url.rstrip("/")}{article}explore/'
    text = text.replace('<head>', f'<head><link rel="canonical" href="{canonical}">', 1)
    if re.search(r'/Users/|file://|obsidian://|base64,', text):
        raise ValueError('Private path or unextracted inline asset remains.')
    (output / 'index.html').write_text(text)
    (output / 'provenance.json').write_text(json.dumps({
        'original_source': args.source_url,
        'original_pdf': args.pdf_url,
        'public_edition_date': args.published_at,
        'reviewed_html_sha256': hashlib.sha256(raw.encode()).hexdigest(),
        'public_html_sha256': hashlib.sha256(text.encode()).hexdigest(),
        'images': images,
        'note': 'Public edition: local companion links replaced by public sources and reading-page anchors.'
    }, ensure_ascii=False, indent=2) + '\n')
    print(f'Exported {output.relative_to(root)}/index.html; {len(images)} unique images.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', required=True)
    parser.add_argument('--slug', required=True)
    parser.add_argument('--source-url', required=True)
    parser.add_argument('--pdf-url', required=True)
    parser.add_argument('--site-url', default='https://sunqi.site')
    parser.add_argument('--published-at', required=True, help='Public edition date, YYYY-MM-DD.')
    export(parser.parse_args())
