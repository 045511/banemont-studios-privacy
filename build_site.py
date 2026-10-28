"""Build the studio's static notices from reviewed content; no third-party packages."""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
import json

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'policy-content.json').read_text(encoding='utf-8'))

def render(page):
    depth=page['path'].count('/')
    prefix='../'*depth
    links=[('index.html','Privacy policy'),('games/astro-exit.html','Astro Exit'),('delete-data.html','Delete data')]
    navigation=''.join(f'<a href="{prefix+url}"'+(' aria-current="page"' if url==page['path'] else '')+f'>{name}</a>' for url,name in links)
    toc=''.join(f'<a href="#{s["id"]}">{escape(s["title"])}</a>' for s in page['sections'])
    sections=''.join(f'<section class="document-section" id="{s["id"]}" aria-labelledby="{s["id"]}-heading"><h2 id="{s["id"]}-heading">{escape(s["title"])}</h2>{s["body"]}</section>' for s in page['sections'])
    summary=''.join(f'<li>{item}</li>' for item in page['summary'])
    content=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; img-src 'self'; base-uri 'none'; form-action 'none'; object-src 'none'"><title>{escape(page['title'])} | BANEMONT STUDIOS</title><meta name="description" content="{escape(page['description'],quote=True)}"><meta name="color-scheme" content="light"><link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}site.css"></head>
<body><a class="skip" href="#main">Skip to content</a><header class="masthead"><div class="wrap"><a class="brand" href="{prefix}index.html" aria-label="BANEMONT STUDIOS privacy home">BANEMONT<span>STUDIOS</span></a><nav class="top-links" aria-label="Site navigation">{navigation}</nav></div></header>
<div class="hero"><div class="wrap"><p class="eyebrow">{escape(page['eyebrow'])}</p><h1>{escape(page['title'])}</h1><p class="lead">{page['intro']}</p><div class="meta"><span><strong>Last updated</strong> {DATA['updated']}</span><span><strong>Privacy contact</strong> <a href="mailto:info@banemont.org">info@banemont.org</a></span></div></div></div>
<main class="wrap layout" id="main"><aside class="contents"><div class="desktop-contents"><p class="contents-label">On this page</p><nav aria-label="Page contents">{toc}</nav></div><details class="mobile-contents"><summary>On this page</summary><nav aria-label="Page contents">{toc}</nav></details></aside><article><div class="summary-card"><h2>{escape(page['summary_title'])}</h2><ul>{summary}</ul></div>{sections}</article></main>
<footer><div class="wrap"><span>© 2026 BANEMONT STUDIOS · Published in app stores as BANEMONT</span><nav aria-label="Footer navigation">{navigation}<a href="mailto:info@banemont.org">Email support</a></nav></div></footer></body></html>
'''
    target=ROOT/page['path']
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(content,encoding='utf-8')

class TextCopy(HTMLParser):
    def __init__(self):super().__init__();self.parts=[]
    def handle_starttag(self,tag,attrs):
        if tag=='li':self.parts.append('\n- ')
        if tag in ('h2','h3'):self.parts.append('\n\n### ')
    def handle_endtag(self,tag):
        if tag in ('p','div','ul','ol','h2','h3'):self.parts.append('\n\n')
    def handle_data(self,text):self.parts.append(text)

review=['# BANEMONT STUDIOS — Privacy notices\n','Last updated: '+DATA['updated']+'\n',
        'Public privacy contact: info@banemont.org\n',
        'Review/export copy. The HTML pages include navigation and provider links.\n']
for page in DATA['pages']:
    render(page)
    review.append('\n---\n\n## '+page['title']+'\n')
    for section in page['sections']:
        parsed=TextCopy();parsed.feed(section['body'])
        review.append('\n### '+section['title']+'\n\n'+''.join(parsed.parts).strip()+'\n')
(ROOT/'PRIVACY_POLICY.md').write_text('\n'.join(review),encoding='utf-8')
print('Built '+str(len(DATA['pages']))+' static privacy pages.')
