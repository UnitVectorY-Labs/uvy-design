"""Shared document chrome; examples embed it to remain standalone."""
from html import escape
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / 'site'
GUIDES = [
    ('foundations', 'Foundations'),
    ('logo', 'Logo'),
    ('color', 'Color'),
    ('typography-and-spacing', 'Typography and spacing'),
    ('header', 'Header'),
    ('themes-and-navigation', 'Themes and navigation'),
    ('icons', 'Icons'),
    ('components-and-icons', 'Components'),
    ('charts', 'Charts and graphs'),
    ('footer', 'Footer'),
    ('page-archetypes', 'Page archetypes'),
    ('review', 'Review'),
]
EXAMPLES = [
    ('light', 'Light mode', 'Crisp cool light surfaces, dark ink, signal orange and controls.'),
    ('dark', 'Dark mode', 'Deep midnight blue-slate surfaces paired with bright signal orange.'),
    ('logo', 'Logo', 'Official isometric unit cube variants, theme-adaptive header mark and CSS avatar framing.'),
    ('typography', 'Typography', 'Fixed-width monospace terminal headings and controls paired with system UI sans prose.'),
    ('icons', 'Icons', 'Any Tabler outline icon, size tiers, semantic color usage and copy actions.'),
    ('navigation', 'Sidebar navigation & search', 'Sticky left sidebar with search filter, mobile drawer, breadcrumbs and tabs.'),
    ('topbar', 'Top-bar navigation & search', 'No-sidebar wide layout with header links, inline search toolbar and category tabs.'),
    ('footer', 'Footer — Standard', 'Compact always-visible sticky footer with license and single repository link.'),
    ('footer-repositories', 'Footer — Multiple repositories', 'Compact always-visible sticky footer citing multiple contributing repositories.'),
    ('footer-updated', 'Footer — Last updated', 'Compact always-visible sticky footer with an ISO-8601 UTC Last updated line.'),
    ('footer-version', 'Footer — Application version', 'Compact always-visible sticky footer with a server-configured build version line.'),
    ('components', 'Components', 'Buttons, status pills, badges, alerts, empty states and loading indicators.'),
    ('forms', 'Form', 'Labels, hints, inline validation, reset and status feedback.'),
    ('table', 'Comparison table', 'Toolbar filtering, compact density, pagination and local horizontal scroll.'),
    ('table-records', 'Mobile record table', 'Framed stat strip, quantitative spectra, sorting and mobile record cards.'),
    ('panels', 'Detail panels', 'Key/value datasheet, lifecycle rows, payload tabs and copyable JSON.'),
    ('charts', 'Charts and graphs', 'Theme-reactive trend panels, paired KPI metrics, dashed percentiles and aligned breakdown sparklines.'),
    ('landing', 'Landing page', 'Typographic hero and rule-divided capabilities without card grids.'),
    ('documentation', 'Static article', 'Readable technical prose with sticky local navigation and code blocks.'),
    ('application', 'Dynamic application', 'Live filters, status lanes using structured lists and a detail dialog.'),
    ('utility', 'Utility', 'Compact input, action, terminal-style output well and copy workflow.'),
]


def uvy_mark():
    """UnitVectorY-Labs geometric isometric unit cube mark (transparent standalone geometry)."""
    return (
        '<svg class="uvy-mark" aria-hidden="true" width="28" height="28" viewBox="0 0 100 100">'
        '<g stroke-width="4" stroke-linejoin="round">'
        '<polygon class="uvy-mark__top" points="50,8 82.5,26.75 50,45.5 17.5,26.75"/>'
        '<polygon class="uvy-mark__left" points="12.3,35.75 44.8,54.5 44.8,92 12.3,73.25"/>'
        '<polygon class="uvy-mark__right" points="55.2,54.5 87.7,35.75 87.7,73.25 55.2,92"/>'
        '</g>'
        '</svg>'
    )


def icon(name, mode='', cls='icon'):
    data = f' data-icon="{mode}"' if mode else ''
    return (
        f'<svg class="{cls}" aria-hidden="true"{data} width="20" height="20" viewBox="0 0 24 24" '
        f'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        f'<use href="#tabler-{name}"></use></svg>'
    )


def header(prefix='', identity='UnitVectorY-Labs Design Guide', home='index.html', sidebar=True, current='guide', mark=True, wide=False):
    icons = (SITE / 'icons.inc').read_text().strip()
    menu = (
        f'<button id="menu" class="icon-button menu-button" type="button" '
        f'aria-label="Open navigation" aria-controls="sidebar" aria-expanded="false" hidden>'
        f'{icon("menu")}</button>'
    ) if sidebar else ''
    guide_current = ' aria-current="page"' if current == 'guide' else ''
    examples_current = ' aria-current="page"' if current == 'examples' else ''
    brand_mark = uvy_mark() if mark else ''
    hdr_cls = 'site-header site-header--wide' if wide else 'site-header'
    return (
        f'<a class="skip" href="#main">Skip to content</a>\n'
        f'<header class="{hdr_cls}"><div class="header-inner">{icons}'
        f'<div class="header-identity">{menu}'
        f'<a class="brand" href="{prefix}{home}">{brand_mark}<span>{escape(identity)}</span></a></div>'
        f'<nav aria-label="Main navigation">'
        f'<a href="{prefix}index.html"{guide_current}>Guide</a>'
        f'<a href="{prefix}examples/index.html"{examples_current}>Examples</a>'
        f'</nav>'
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
        f'</aside>'
    )


def backdrop():
    return '<button id="menu-backdrop" class="menu-backdrop" type="button" aria-label="Close navigation" tabindex="-1" hidden></button>'


def footer(prefix='', repositories=None, updated=None, version=None, show_version=False, wide=False):
    """The server/build decides whether to render an updated timestamp or application version."""
    repositories = repositories or [('uvy-design', 'https://github.com/UnitVectorY-Labs/uvy-design')]
    links = ' and '.join(
        f'<a href="{escape(url, quote=True)}"><strong>{escape(name)}</strong></a>'
        for name, url in repositories
    )
    meta_lines = []
    if updated:
        meta_lines.append(
            f'<p class="footer-meta">Last updated: <time datetime="{escape(updated, quote=True)}">{escape(updated)}</time></p>'
        )
    if show_version and version:
        meta_lines.append(f'<p class="version">Version {escape(version)}</p>')
    ftr_cls = 'site-footer site-footer--wide' if wide else 'site-footer'
    return (
        f'<footer class="{ftr_cls}"><div class="footer-inner">'
        f'<p><a href="https://github.com/UnitVectorY-Labs">UnitVectorY-Labs</a>'
        f'<span class="footer-sep" aria-hidden="true">|</span>'
        f'<a href="{prefix}LICENSE">MIT License</a>'
        f'<span class="footer-sep" aria-hidden="true">|</span>'
        f'{links} on GitHub</p>{"".join(meta_lines)}</div></footer>'
    )
