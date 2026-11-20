"""Shared document chrome; examples embed it to remain standalone."""
from html import escape
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / 'site'
GUIDES = [
    ('foundations', 'Foundations'), ('color', 'Color'),
    ('typography-and-spacing', 'Typography and spacing'), ('header', 'Header'),
    ('themes-and-navigation', 'Themes and navigation'), ('icons', 'Icons'),
    ('components-and-icons', 'Components'), ('footer', 'Footer'),
    ('page-archetypes', 'Page archetypes'), ('review', 'Review'),
]
EXAMPLES = [
    ('light', 'Light mode', 'Light surfaces, text, accent and controls.'),
    ('dark', 'Dark mode', 'The same components in dark mode.'),
    ('typography', 'Typography', 'Headings, prose, lists and technical content.'),
    ('icons', 'Icons', 'Size, color and accessible icon controls.'),
    ('navigation', 'Sidebar and header', 'Persistent navigation and a mobile drawer.'),
    ('footer', 'Footer', 'Organization, license, repositories and optional version.'),
    ('components', 'Buttons', 'Primary, secondary and disabled actions.'),
    ('forms', 'Form', 'Labels, validation, reset and feedback.'),
    ('table', 'Comparison table', 'Density, filtering and local overflow.'),
    ('table-records', 'Mobile record table', 'Record cards, sorting and numeric spectra.'),
    ('panels', 'Detail panels', 'Endpoint summaries, lifecycle states and evidence.'),
    ('landing', 'Landing page', 'A compact product introduction.'),
    ('documentation', 'Static article', 'Readable content with local article navigation.'),
    ('application', 'Dynamic application', 'Filters, updates and run details.'),
    ('utility', 'Utility', 'A compact input/action/output workflow.'),
]


def icon(name, mode=''):
    data = f' data-icon="{mode}"' if mode else ''
    return f'<svg class="icon" aria-hidden="true"{data} width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-{name}"></use></svg>'


def header(prefix='', identity='UVY Design', home='index.html', sidebar=True, current='guide'):
    icons = (SITE / 'icons.inc').read_text()
    menu = f'<button id="menu" class="icon-button menu-button" type="button" aria-label="Open navigation" aria-controls="sidebar" aria-expanded="false" hidden>{icon("menu")}</button>' if sidebar else ''
    reset = '' if sidebar else '<button id="theme-reset" class="theme-reset" type="button" hidden>Use system theme</button>'
    guide_current = ' aria-current="page"' if current == 'guide' else ''
    examples_current = ' aria-current="page"' if current == 'examples' else ''
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner">{icons}<div class="header-identity">{menu}<a class="brand" href="{prefix}{home}">{escape(identity)}</a></div><nav aria-label="Main navigation"><a href="{prefix}index.html"{guide_current}>Guide</a><a href="{prefix}examples/index.html"{examples_current}>Examples</a>{reset}</nav><button id="theme" class="icon-button" type="button" aria-label="Switch color theme" hidden>{icon('moon', 'moon')}{icon('sun', 'sun')}</button></div></header>'''


def navigation(links, title='Navigation', filters=False):
    search = '''<div class="nav-filters" hidden><div class="field"><label for="nav-search">Find a section</label><input id="nav-search" type="search" autocomplete="off"></div></div>''' if filters else ''
    return f'''<aside id="sidebar" class="sidebar" aria-label="{title}"><div class="sidebar-tools"><div class="sidebar-heading"><h2>{title}</h2><button id="menu-close" class="icon-button sidebar-close" type="button" aria-label="Close navigation" hidden>{icon('x')}</button></div>{search}</div><nav aria-label="{title}">{links}</nav><p id="nav-empty" class="hint" hidden>No sections match. Clear the search.</p><div class="sidebar-footer"><button id="theme-reset" type="button" hidden>Use system theme</button></div></aside>'''


def backdrop():
    return '<button id="menu-backdrop" class="menu-backdrop" type="button" aria-label="Close navigation" tabindex="-1" hidden></button>'


def footer(prefix='', repositories=None, version=None, show_version=False):
    """The server/build decides whether to render an application version at all."""
    repositories = repositories or [('uvy-design', 'https://github.com/UnitVectorY-Labs/uvy-design')]
    links = ' and '.join(f'<a href="{escape(url, quote=True)}"><strong>{escape(name)}</strong></a>' for name, url in repositories)
    version_line = f'<p class="version">Version {escape(version)}</p>' if show_version and version else ''
    return f'''<footer class="site-footer"><div class="footer-inner"><p><a href="https://github.com/UnitVectorY-Labs">UnitVectorY-Labs</a> <span aria-hidden="true">|</span> <a href="{prefix}LICENSE">MIT License</a> <span aria-hidden="true">|</span> {links} on GitHub</p>{version_line}</div></footer>'''
