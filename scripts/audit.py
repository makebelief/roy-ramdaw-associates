#!/usr/bin/env python3
"""Dependency-free pre-deployment audit. Run: python3 scripts/audit.py"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
from xml.etree import ElementTree
import json, re, sys

root=Path(__file__).resolve().parents[1]/'public'
domain='https://royramdaw.co.za'
indexable={'/','/about/','/practice-areas/','/managing-partner/','/insights/','/contact/'}
errors=[]
warnings=[]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.items=[];self.headings=[];self.ids=set();self.scripts=[];self.in_script=False;self.in_title=False;self.title=''
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);self.items.append((tag,a))
        if tag=='h1':self.headings.append(a)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='script' and a.get('type')=='application/ld+json':self.in_script=True;self.scripts.append('')
        if tag=='title':self.in_title=True
    def handle_endtag(self,tag):
        if tag=='script':self.in_script=False
        if tag=='title':self.in_title=False
    def handle_data(self,data):
        if self.in_script:self.scripts[-1]+=data
        if self.in_title:self.title+=data

def issue(msg):errors.append(msg)
pages={}
for f in sorted(root.rglob('*.html')):
    rel=f.relative_to(root).as_posix()
    url='/' if rel=='index.html' else '/'+rel if rel=='404.html' else '/'+rel[:-len('index.html')]
    p=Page()
    try:p.feed(f.read_text(encoding='utf-8'))
    except Exception as exc:issue(f'{rel}: invalid HTML: {exc}')
    pages[url]=p
    if len(p.headings)!=1:issue(f'{url}: expected one h1, found {len(p.headings)}')
    if not 16<len(p.title)<95:issue(f'{url}: invalid title length {len(p.title)}')
    for tag,a in p.items:
        if tag=='img' and not a.get('alt'):issue(f'{url}: image without alt')
        if tag in ('script','link') and a.get('src','').startswith('http'):
            warnings.append(f'{url}: external script')
    metas={a.get('name') or a.get('property'):a.get('content') for tag,a in p.items if tag=='meta'}
    if len(metas.get('description',''))<70:issue(f'{url}: missing/short description')
    if 'noindex' in metas.get('robots','') and url in indexable:issue(f'{url}: indexing blocked')
    if 'noindex' not in metas.get('robots','') and url not in indexable:issue(f'{url}: expected noindex')
    canonicals=[a.get('href') for tag,a in p.items if tag=='link' and 'canonical' in a.get('rel','').split()]
    if canonicals!=[domain+url]:issue(f'{url}: canonical {canonicals} != {domain+url}')
    if metas.get('og:url')!=domain+url:issue(f'{url}: og:url does not match canonical')
    if not metas.get('og:image','').startswith(domain+'/assets/'):issue(f'{url}: missing first-party OG image')
    for entry in p.scripts:
        try: json.loads(entry)
        except Exception as exc:issue(f'{url}: JSON-LD malformed: {exc}')
    if 'roy-ramdaw-associates.vercel.app' in f.read_text():issue(f'{url}: stale Vercel URL')

for url,p in pages.items():
    for tag,a in p.items:
        for name in ['src','href']:
            v=a.get(name,'')
            if not v or v.startswith(('mailto:','tel:','javascript:','data:')):continue
            parsed=urlparse(v)
            if parsed.scheme and parsed.scheme not in ('http','https'): continue
            if parsed.scheme and parsed.netloc not in ('royramdaw.co.za','www.royramdaw.co.za'):continue
            if v.startswith('//'):continue
            if parsed.path.startswith('/'):
                path=unquote(parsed.path)
            elif parsed.path:
                path=str(Path(url).parent / parsed.path)
            else:
                path=url
            if '..' in Path(path).parts:issue(f'{url}: path traversal {v}');continue
            target=root/path.lstrip('/')
            if target.is_dir():target=target/'index.html'
            if path=='/':target=root/'index.html'
            if not target.exists():issue(f'{url}: missing asset/link {v} (from {tag})');continue
            if parsed.fragment and target.suffix=='.html':
                related='/' if target==root/'index.html' else '/'+target.relative_to(root).as_posix()
                if related.endswith('index.html') and related!='/':related=related[:-len('index.html')]
                if related in pages and unquote(parsed.fragment) not in pages[related].ids:
                    issue(f'{url}: nonexistent anchor {v}')

try:
    s=ElementTree.parse(root/'sitemap.xml')
    urls={x.text for x in s.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
    expected={domain+p for p in indexable}
    if urls!=expected:issue(f'sitemap URLs differ. missing={expected-urls}, extra={urls-expected}')
except Exception as exc:issue(f'sitemap invalid: {exc}')
robots=(root/'robots.txt').read_text()
if f'Sitemap: {domain}/sitemap.xml' not in robots:issue('robots.txt sitemap incorrect')
headers=(root/'_headers').read_text()
for header in ('Content-Security-Policy:','Strict-Transport-Security:','X-Content-Type-Options:','X-Robots-Tag: noindex'):
    if header not in headers:issue(f'missing security/header rule: {header}')
if re.search(r'(?m)^/\*\s*\n\s+X-Robots-Tag:', headers):issue('global X-Robots-Tag noindex detected')
print(f'Checked {len(pages)} HTML pages; {len(indexable)} indexable; {len(list(root.rglob("*")))} deployed entries')
print(f'Production assets: {sum(f.stat().st_size for f in root.rglob("*") if f.is_file())/1024:.0f} KiB (before compression/CDN)')
for msg in warnings:print('WARNING:',msg)
for msg in errors:print('ERROR:',msg)
print('AUDIT:', 'PASS' if not errors else f'FAIL ({len(errors)} issues)')
sys.exit(0 if not errors else 1)
