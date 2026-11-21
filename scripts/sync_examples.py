"""Refresh embedded uvy.css and uvy.js so standalone examples remain self-contained."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
css = (ROOT / 'site' / 'uvy.css').read_text()
js = (ROOT / 'site' / 'uvy.js').read_text()

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
