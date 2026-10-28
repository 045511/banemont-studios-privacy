"""Check the static package's links, HTML structure and privacy constraints."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json

ROOT=Path(__file__).resolve().parent
checks=0
def check(ok,message):
    global checks
    checks+=1
    if not ok:raise AssertionError(message)

class Document(HTMLParser):
    def __init__(self,path):
        super().__init__(convert_charrefs=True)
        self.path=path;self.ids=set();self.links=[];self.elements=[];self.metas={};self.text=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);self.elements.append((tag,a))
        if 'id' in a:
            check(a['id'] not in self.ids,f'duplicate ID: {self.path}:{a["id"]}')
            self.ids.add(a['id'])
        for attr in ('href','src'):
            if attr in a:self.links.append(a[attr])
        if tag=='meta':self.metas[a.get('name',a.get('http-equiv',''))]=a.get('content','')
    def handle_data(self,data):self.text.append(data)

pages={}
for path in [ROOT/'index.html',ROOT/'games/astro-exit.html',ROOT/'delete-data.html']:
    doc=Document(path);doc.feed(path.read_text(encoding='utf-8'));pages[path]=doc
    check(sum(t=='h1' for t,a in doc.elements)==1,f'one H1: {path}')
    check(any(t=='html' and a.get('lang')=='en' for t,a in doc.elements),f'language: {path}')
    check('width=device-width' in doc.metas.get('viewport',''),f'responsive viewport: {path}')
    check(doc.metas.get('referrer')=='no-referrer',f'no referrer: {path}')
    check("default-src 'none'" in doc.metas.get('Content-Security-Policy',''),f'CSP: {path}')
    check(not any(t in ('script','form','iframe','input') for t,a in doc.elements),f'no collection widgets: {path}')
    text=' '.join(doc.text)
    check('BANEMONT' in text and 'info@banemont.org' in text,f'publisher/contact: {path}')
    check('28 October 2026' in text,f'revision date: {path}')
    check(not any(x in text for x in ['YOUR_PROJECT','YOUR_EMAIL','TODO','TBD','lorem ipsum']),f'no placeholder: {path}')
for path,doc in pages.items():
    for href in doc.links:
        part=urlsplit(href)
        if part.scheme:
            check(part.scheme in ('https','mailto'),f'only HTTPS/email outbound links: {href}')
            continue
        check(not part.netloc and not href.startswith('/'),f'project-relative link: {href}')
        target=(path.parent/unquote(part.path)).resolve() if part.path else path
        check(target.is_relative_to(ROOT) and target.is_file(),f'local target: {path}: {href}')
        if part.fragment:
            check(target in pages and unquote(part.fragment) in pages[target].ids,f'valid anchor: {href}')
check(not (ROOT/'_headers').exists(),'no unsupported host header file')
check((ROOT/'.nojekyll').exists(),'static Pages marker')
print(json.dumps({'checks':checks,'failures':0,'pages':len(pages),'scope':'Local static content and links; no live hosting or legal certification'},indent=2))
