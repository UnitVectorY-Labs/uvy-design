"""Check built local destinations and fragment IDs, including project subpaths."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1] / '_site'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate ID: {attrs["id"]}'
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

pages = {path: Page(path) for path in ROOT.rglob('*.html')}
assert pages, 'Build the site before checking it'
errors = []
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        if url.path.startswith('/'):
            errors.append(f'{path}: root-relative link breaks project hosting: {link}')
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if not target.is_relative_to(ROOT):
            errors.append(f'{path}: link escapes site: {link}')
        elif not target.exists():
            errors.append(f'{path}: missing destination: {link}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{path}: missing fragment: {link}')
assert not errors, '\n'.join(errors)
print(f'Checked local links, assets, IDs and fragments in {len(pages)} pages')
