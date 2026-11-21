"""Render the UVY Design guide site following its own style guide strictly."""
from pathlib import Path
from html import escape
import re
import shutil
import markdown
from site_chrome import header, navigation, backdrop, footer, icon, GUIDES

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


def apply_uvy_components(html, stem, title, prefix):
    """Apply UVY page-header, panel, code-block and directory patterns to rendered Markdown."""
    # 1. Opening H1 + lead paragraph -> .uvy-page-header with optional breadcrumb.
    crumb = ''
    if stem != 'README':
        crumb = (
            f'<nav class="uvy-breadcrumbs" aria-label="Breadcrumb"><ol>'
            f'<li><a href="{prefix}index.html">Guide</a></li>'
            f'<li aria-current="page">{escape(title)}</li>'
            f'</ol></nav>'
        )
    html = re.sub(
        r'(<h1[^>]*>.*?</h1>)\s*<p>(.*?)</p>',
        lambda m: (
            f'{crumb}<div class="uvy-page-header"><div>'
            f'{m.group(1)}<p class="uvy-lead">{m.group(2)}</p>'
            f'</div></div>'
        ),
        html,
        count=1,
        flags=re.S,
    )

    # 2. Wrap Markdown tables inside a flush .uvy-panel > .table-wrap.
    html = (
        html.replace(
            '<table>',
            '<div class="uvy-panel"><div class="table-wrap" role="region" aria-label="Reference table" tabindex="0"><table>',
        )
        .replace('</table>', '</table></div></div>')
    )
    if stem == 'color':
        html = (
            html.replace('<table>', '<table class="palette-table" role="table">')
            .replace('<thead>', '<thead role="rowgroup">')
            .replace('<tbody>', '<tbody role="rowgroup">')
            .replace('<tr>', '<tr role="row">')
            .replace('<th>', '<th scope="col" role="columnheader">')
            .replace('<td>', '<td role="cell">')
        )

    # 3. Wrap fenced code blocks in .uvy-code with a copy button.
    code_idx = 0

    def wrap_code(match):
        nonlocal code_idx
        code_idx += 1
        lang = match.group(1) or 'snippet'
        body = match.group(2)
        cid = f'doc-code-{code_idx}'
        copy_svg = icon('copy', cls='icon icon-small')
        check_svg = icon('check', cls='icon icon-small')
        return (
            f'<div class="uvy-code">'
            f'<div class="uvy-code__bar"><span>{escape(lang)}</span>'
            f'<button type="button" class="uvy-button--quiet uvy-button--small uvy-copy" '
            f'data-copy-target="{cid}" data-enable-with-js disabled aria-label="Copy {escape(lang)} snippet">'
            f'<span data-copy class="with-icon">{copy_svg}Copy</span>'
            f'<span data-copied class="with-icon">{check_svg}Copied</span>'
            f'</button></div>'
            f'<pre tabindex="0" aria-label="{escape(lang)} example"><code id="{cid}">{body}</code></pre>'
            f'</div>'
        )

    html = re.sub(
        r'<pre><code(?: class="language-([^"]+)")?>(.*?)</code></pre>',
        wrap_code,
        html,
        flags=re.S,
    )

    # 4. On README (home), render the chapter directory as a clean .uvy-index.
    if stem == 'README':
        def convert_index(match):
            items = re.findall(
                r'<li>\s*<a href="([^"]+)">([^<]+)</a>\s*[—–-]\s*(.*?)\s*</li>',
                match.group(1),
                flags=re.S,
            )
            if not items:
                return match.group(0)
            rows = ''.join(
                f'<li><a href="{href}"><strong>{label}</strong><span>{desc}</span></a></li>'
                for href, label, desc in items
            )
            return f'<ul class="uvy-index">{rows}</ul>'

        html = re.sub(r'<ul>(.*?)</ul>', convert_index, html, count=1, flags=re.S)

    return html


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / 'assets', OUT / 'assets')
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
        article = apply_uvy_components(article, source.stem, title, prefix)
        links = ''.join(
            f'<a href="{prefix}docs/{slug}.html"'
            + (' aria-current="page"' if source.stem == slug else '')
            + f'>{escape(label)}</a>'
            for slug, label in GUIDES
        )
        dest.write_text(
            f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{escape(title)} — Unit Vector Y Labs</title>
    <link rel="icon" type="image/svg+xml" href="{prefix}assets/uvy-standalone-mark-light.svg" media="(prefers-color-scheme: light)" />
    <link rel="icon" type="image/svg+xml" href="{prefix}assets/uvy-standalone-mark-dark.svg" media="(prefers-color-scheme: dark)" />
    <link rel="stylesheet" href="{prefix}site/uvy.css" />
    <script src="{prefix}site/uvy.js"></script>
  </head>
  <body>
    {header(prefix)}
    <main class="page layout" id="main">
      {navigation(links, 'Design guide')}
      <div class="workspace">
        <article class="article">
          {article}
          <p class="uvy-source-note"><a href="{prefix}{rel.as_posix()}">Standalone Markdown source</a></p>
        </article>
      </div>
    </main>
    {backdrop()}
    {footer(prefix)}
  </body>
</html>
'''
        )
        shutil.copy(source, OUT / rel)
    print(f'Built {len(DOCS) + 1} guide pages and {len(list((OUT / "examples").glob("*.html")))} examples in {OUT}')


if __name__ == '__main__':
    build()
