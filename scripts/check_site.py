"""Dependency-free checks for a static portfolio and project-relative links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parent.parent

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.h1 = 0
        self.main = 0
        self.title = False
        self.description = False
        self.viewport = False
        self.language = False
        self.errors = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        for key in ('href', 'src'):
            if key in a:
                self.links.append(a[key])
        if tag == 'img':
            for key in ('alt', 'width', 'height'):
                if not a.get(key):
                    self.errors.append(f"Image lacks {key}: {a.get('src')}")
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        if tag == 'title': self.title = True
        if tag == 'html': self.language = bool(a.get('lang'))
        if tag == 'meta' and a.get('name') == 'description': self.description = bool(a.get('content'))
        if tag == 'meta' and a.get('name') == 'viewport': self.viewport = True
        if a.get('target') == '_blank' and 'noopener' not in a.get('rel', ''):
            self.errors.append('New-tab link missing noopener')

p = Page()
p.feed((ROOT / 'index.html').read_text())
assert p.h1 == 1 and p.main == 1, 'Use one main heading and main landmark'
assert p.title and p.description and p.viewport and p.language, 'Missing page metadata'
assert len(p.ids) == len(set(p.ids)), 'Duplicate IDs'
for link in p.links:
    u = urlsplit(link)
    if u.scheme or u.netloc:
        continue
    if not u.path and u.fragment:
        assert u.fragment in p.ids, f'Broken anchor: {link}'
    if u.path:
        assert not u.path.startswith('/'), f'Root-relative link breaks project Pages: {link}'
        assert (ROOT / unquote(u.path)).is_file(), f'Missing file: {link}'
assert not p.errors, '\n'.join(p.errors)
print(f'PASS: {len(p.links)} asset/link references; page metadata, image attributes, landmarks, and IDs.')
