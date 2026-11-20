"""Render guidance for Pages; original Markdown and standalone HTML stay usable."""
from pathlib import Path
from html import escape
import re
import shutil
import markdown

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'
DOCS = sorted((ROOT / 'docs').glob('*.md'))


def web_links(html):
    # Only rewrite local Markdown destinations in rendered HTML, never code samples.
    def replace(match):
        target = match[1]
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
            return match[0]
        target = re.sub(r'\.md(?=$|[#?])', '.html', target)
        target = re.sub(r'(^|/)README\.html(?=$|[#?])', r'\1index.html', target)
        return 'href="' + target + '"'
    return re.sub(r'href="([^"]+)"', replace, html)


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / 'site', OUT / 'site')
    shutil.copytree(ROOT / 'examples', OUT / 'examples')
    shutil.copy(ROOT / 'LICENSE', OUT / 'LICENSE')
    (OUT / '.nojekyll').touch()
    for example in (OUT / 'examples').glob('*.html'):
        example.write_text(web_links(example.read_text()))
    for source in [ROOT / 'README.md', *DOCS]:
        rel = source.relative_to(ROOT)
        dest = OUT / ('index.html' if source.name == 'README.md' else str(rel.with_suffix('.html')))
        dest.parent.mkdir(exist_ok=True)
        prefix = '../' if rel.parent != Path('.') else ''
        text = source.read_text()
        title = text.splitlines()[0].lstrip('# ')
        article = web_links(markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc']))
        # Wide prose tables scroll within a named, keyboard-accessible region.
        article = article.replace('<table>', '<div class="table-wrap" role="region" aria-label="Reference table" tabindex="0"><table>').replace('</table>', '</table></div>')
        links = ''.join(f'<a href="{prefix}docs/{doc.stem}.html"'+(' aria-current="page"' if doc == source else '')+f'>{escape(doc.read_text().splitlines()[0].lstrip("# "))}</a>' for doc in DOCS)
        dest.write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)} — Unit Vector Y Labs</title><link rel="stylesheet" href="{prefix}site/reference.css"><script src="{prefix}site/theme.js"></script></head><body><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="header-inner"><a class="brand" href="{prefix}index.html"><span class="mark" aria-hidden="true">Y</span>UVY Design</a><nav aria-label="Main navigation"><a href="{prefix}index.html">Guide</a><a href="{prefix}examples/components.html">Examples</a></nav><label class="theme" hidden>Theme <select id="theme"><option value="system">System</option><option value="light">Light</option><option value="dark">Dark</option></select></label></div></header><main class="page layout" id="main"><aside class="sidebar"><nav aria-label="Guide articles">{links}</nav></aside><article class="article">{article}<p class="guide-note"><a href="{prefix}{rel.as_posix()}">Standalone Markdown source</a></p></article></main><footer><div class="footer-inner"><a href="https://github.com/UnitVectorY-Labs/uvy-design">Source</a> · <a href="{prefix}LICENSE">License</a></div></footer></body></html>''')
        shutil.copy(source, OUT / rel)
    print(f'Built {len(DOCS) + 1} guide pages and {len(list((OUT / "examples").glob("*.html")))} examples in {OUT}')


if __name__ == '__main__':
    build()
