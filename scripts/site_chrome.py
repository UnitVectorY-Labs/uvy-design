"""Shared document chrome; examples embed it to remain standalone."""
from html import escape
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / 'site'
GUIDES = [
    ('foundations', 'Foundations'),
    ('color', 'Color'),
    ('typography-and-spacing', 'Typography and spacing'),
    ('header', 'Header'),
    ('themes-and-navigation', 'Themes and navigation'),
    ('icons', 'Icons'),
    ('components-and-icons', 'Components'),
    ('footer', 'Footer'),
    ('page-archetypes', 'Page archetypes'),
    ('review', 'Review'),
]
EXAMPLES = [
    ('light', 'Light mode', 'Cool graphite surfaces, dark ink, signal orange action and inputs.'),
    ('dark', 'Dark mode', 'The same tokens and controls in dark mode.'),
    ('typography', 'Typography', 'Type scale, measure, lists, inline code, timestamps and blockquotes.'),
    ('icons', 'Icons', 'Tabler outline sizing, neutral and status coloring, and copy actions.'),
    ('navigation', 'Header, sidebar and tabs', 'Persistent sidebar, mobile drawer, breadcrumbs and tabs.'),
    ('footer', 'Footer', 'Organization, license, repository links and optional version line.'),
    ('components', 'Components', 'Buttons, status pills, badges, alerts, empty states and loading.'),
    ('forms', 'Form', 'Labels, hints, inline validation, reset and status feedback.'),
    ('table', 'Comparison table', 'Toolbar filtering, compact density, pagination and local overflow.'),
    ('table-records', 'Mobile record table', 'Framed summary strip, quantitative spectra, sorting and mobile cards.'),
    ('panels', 'Detail panels', 'Key/value datasheet, lifecycle rows, payload tabs and copyable JSON.'),
    ('landing', 'Landing page', 'Typographic hero and rule-divided capabilities without card grids.'),
    ('documentation', 'Static article', 'Readable technical prose with local section navigation and code.'),
    ('application', 'Dynamic application', 'Live filters, status lanes using structured lists and a detail dialog.'),
    ('utility', 'Utility', 'Compact input, action, output and copy workflow.'),
]


def uvy_mark():
    return (
        '<svg class="uvy-mark" aria-hidden="true" width="24" height="24" viewBox="0 0 24 24">'
        '<rect class="uvy-mark__tile" width="24" height="24" rx="5"/>'
        '<circle class="uvy-mark__origin" cx="7.5" cy="16.5" r="1.75"/>'
        '<path class="uvy-mark__vector" d="M9.5 14.5L16.5 7.5M11.5 7.5H16.5V12.5"/>'
        '</svg>'
    )


def icon(name, mode='', cls='icon'):
    data = f' data-icon="{mode}"' if mode else ''
    return (
        f'<svg class="{cls}" aria-hidden="true"{data} width="20" height="20" viewBox="0 0 24 24" '
        f'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        f'<use href="#tabler-{name}"></use></svg>'
    )


def header(prefix='', identity='UVY Design', home='index.html', sidebar=True, current='guide', mark=True):
    icons = (SITE / 'icons.inc').read_text().strip()
    menu = (
        f'<button id="menu" class="icon-button menu-button" type="button" '
        f'aria-label="Open navigation" aria-controls="sidebar" aria-expanded="false" hidden>'
        f'{icon("menu")}</button>'
    ) if sidebar else ''
    reset = (
        '' if sidebar
        else '<button id="theme-reset" class="uvy-button--quiet uvy-button--small theme-reset" type="button" hidden>Use system theme</button>'
    )
    guide_current = ' aria-current="page"' if current == 'guide' else ''
    examples_current = ' aria-current="page"' if current == 'examples' else ''
    brand_mark = uvy_mark() if mark else ''
    return (
        f'<a class="skip" href="#main">Skip to content</a>\n'
        f'<header class="site-header"><div class="header-inner">{icons}'
        f'<div class="header-identity">{menu}'
        f'<a class="brand" href="{prefix}{home}">{brand_mark}<span>{escape(identity)}</span></a></div>'
        f'<nav aria-label="Main navigation">'
        f'<a href="{prefix}index.html"{guide_current}>Guide</a>'
        f'<a href="{prefix}examples/index.html"{examples_current}>Examples</a>'
        f'{reset}</nav>'
        f'<button id="theme" class="icon-button" type="button" aria-label="Switch color theme" hidden>'
        f'{icon("moon", "moon")}{icon("sun", "sun")}</button>'
        f'</div></header>'
    )


def navigation(links, title='Navigation', filters=False):
    search = (
        '<div class="nav-filters" hidden><div class="uvy-field">'
        '<label for="nav-search">Find a section</label>'
        '<input id="nav-search" type="search" autocomplete="off">'
        '</div></div>'
    ) if filters else ''
    return (
        f'<aside id="sidebar" class="sidebar" aria-label="{escape(title)}">'
        f'<div class="sidebar-tools"><div class="sidebar-heading">'
        f'<h2>{escape(title)}</h2>'
        f'<button id="menu-close" class="icon-button sidebar-close" type="button" aria-label="Close navigation" hidden>'
        f'{icon("x")}</button></div>{search}</div>'
        f'<nav aria-label="{escape(title)}">{links}</nav>'
        f'<p id="nav-empty" class="uvy-hint" hidden>No sections match. Clear the search.</p>'
        f'<div class="sidebar-footer">'
        f'<button id="theme-reset" class="uvy-button--quiet uvy-button--small theme-reset" type="button" hidden>Use system theme</button>'
        f'</div></aside>'
    )


def backdrop():
    return '<button id="menu-backdrop" class="menu-backdrop" type="button" aria-label="Close navigation" tabindex="-1" hidden></button>'


def footer(prefix='', repositories=None, version=None, show_version=False):
    """The server/build decides whether to render an application version at all."""
    repositories = repositories or [('uvy-design', 'https://github.com/UnitVectorY-Labs/uvy-design')]
    links = ' and '.join(
        f'<a href="{escape(url, quote=True)}"><strong>{escape(name)}</strong></a>'
        for name, url in repositories
    )
    version_line = f'<p class="version">Version {escape(version)}</p>' if show_version and version else ''
    return (
        f'<footer class="site-footer"><div class="footer-inner">'
        f'<p><a href="https://github.com/UnitVectorY-Labs">UnitVectorY-Labs</a>'
        f'<span class="footer-sep" aria-hidden="true">|</span>'
        f'<a href="{prefix}LICENSE">MIT License</a>'
        f'<span class="footer-sep" aria-hidden="true">|</span>'
        f'{links} on GitHub</p>{version_line}</div></footer>'
    )
