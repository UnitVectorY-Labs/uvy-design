"""Refresh embedded uvy.css, uvy.js and header brand mark in standalone examples."""
from pathlib import Path
import re
from site_chrome import uvy_mark

ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / 'site' / 'uvy.css').read_text()
js = (ROOT / 'site' / 'uvy.js').read_text()
mark = uvy_mark()

for path in sorted((ROOT / 'examples').glob('*.html')):
    text = path.read_text()
    for tag, marker, content in [
        ('style', 'data-uvy-reference', css),
        ('script', 'data-uvy-shell', js),
    ]:
        text, count = re.subn(
            rf'<{tag} {marker}>(.*?)</{tag}>',
            lambda _, t=tag, m=marker, c=content: f'<{tag} {marker}>\n{c}</{tag}>',
            text,
            flags=re.S,
        )
        assert count == 1, f'{path}: expected one {marker} block'
    text, mark_count = re.subn(
        r'(<a class="brand" href="[^"]+">)<svg class="uvy-mark".*?</svg>',
        lambda m: f'{m.group(1)}{mark}',
        text,
        count=1,
        flags=re.S,
    )
    assert mark_count == 1, f'{path}: expected header .brand .uvy-mark'
    favicon_block = (
        '    <link rel="icon" type="image/svg+xml" href="../assets/uvy-standalone-mark-light.svg" media="(prefers-color-scheme: light)" />\n'
        '    <link rel="icon" type="image/svg+xml" href="../assets/uvy-standalone-mark-dark.svg" media="(prefers-color-scheme: dark)" />'
    )
    if 'rel="icon"' not in text:
        text, icon_count = re.subn(
            r'(<title>.*?</title>)',
            lambda m: f'{m.group(1)}\n{favicon_block}',
            text,
            count=1,
        )
        assert icon_count == 1, f'{path}: expected <title>'
    path.write_text(text)
print('Updated embedded CSS, shell behavior, favicons and header mark in standalone examples')
