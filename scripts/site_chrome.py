"""HTML shell for the published guide; examples embed the same patterns."""
from html import escape
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / 'site'


def header(prefix='', identity='UVY Design', home='index.html', sidebar=True):
    icons = (SITE / 'icons.inc').read_text()
    menu = f'''<button id="menu" class="icon-button menu-button" type="button" aria-label="Open navigation" aria-controls="sidebar" aria-expanded="false" hidden>{icon('menu')}</button>''' if sidebar else ''
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner">{icons}
<button id="theme" class="icon-button" type="button" aria-label="Switch color theme" hidden>{icon('moon', 'moon')}{icon('sun', 'sun')}</button>
<a class="brand" href="{prefix}{home}">{escape(identity)}</a>
<nav aria-label="Main navigation"><a href="{prefix}index.html">Guide</a><a href="{prefix}examples/components.html">Examples</a></nav>{menu}</div></header>'''


def icon(name, mode=''):
    data = f' data-icon="{mode}"' if mode else ''
    return f'<svg class="icon" aria-hidden="true"{data} width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-{name}"></use></svg>'


def navigation(links, title='Navigation'):
    return f'''<aside id="sidebar" class="sidebar" aria-label="{title}"><div class="sidebar-tools"><div class="sidebar-heading"><h2>{title}</h2><button id="menu-close" class="icon-button sidebar-close" type="button" aria-label="Close navigation" hidden>{icon('x')}</button></div><div class="nav-filters" hidden><div class="field"><label for="nav-search">Find a page</label><input id="nav-search" type="search" autocomplete="off"></div><div class="field"><label for="nav-group">Show</label><select id="nav-group"><option value="all">All pages</option><option value="guide">Guidance</option><option value="example">Examples</option></select></div></div></div><nav aria-label="{title}">{links}</nav><p id="nav-empty" class="hint" hidden>No pages match. Clear the search or change the filter.</p><div class="sidebar-footer"><button id="theme-reset" type="button" hidden>Use system theme</button></div></aside>'''


def backdrop():
    return '<button id="menu-backdrop" class="menu-backdrop" type="button" aria-label="Close navigation" tabindex="-1" hidden></button>'
