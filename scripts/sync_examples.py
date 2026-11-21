"""Refresh embedded reference CSS/behavior without making examples depend on assets."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / 'site' / 'reference.css').read_text().replace('url("fonts/', 'url("../site/fonts/')
js = (ROOT / 'site' / 'theme.js').read_text()

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
    path.write_text(text)
print('Updated embedded CSS and shell behavior in standalone examples')
