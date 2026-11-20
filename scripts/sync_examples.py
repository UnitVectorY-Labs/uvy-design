"""Refresh embedded reference CSS/behavior without making examples depend on assets."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
for path in (ROOT / 'examples').glob('*.html'):
    text = path.read_text()
    for tag, marker, asset in [('style', 'data-uvy-reference', 'reference.css'), ('script', 'data-uvy-shell', 'theme.js')]:
        content = (ROOT / 'site' / asset).read_text()
        text, count = re.subn(rf'<{tag} {marker}>(.*?)</{tag}>', lambda _: f'<{tag} {marker}>\n{content}</{tag}>', text, flags=re.S)
        assert count == 1, f'{path}: expected one {marker} block'
    path.write_text(text)
print('Updated embedded CSS and shell behavior in standalone examples')
