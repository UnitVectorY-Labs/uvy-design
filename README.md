# UVY Design

Current design guidance for Unit Vector Y Labs projects: crisp cool-light and deep midnight-slate dark interfaces, universally supported system typography with subtle fixed-width terminal instrumentation, a bold 3px signal-orange accent rule, and a single embeddable stylesheet (`site/uvy.css`).

## Read the guide

- [Foundations](docs/foundations.md) — Aesthetic direction, restraint rules and single-CSS adoption contract
- [Logo](docs/logo.md) — Isometric unit cube mark, standalone and avatar SVGs, and brand usage guidelines
- [Color](docs/color.md) — Cool light surfaces, midnight blue-slate dark mode, signal orange, status, spectra and charts
- [Typography and spacing](docs/typography-and-spacing.md) — System UI sans, fixed-width terminal touches, scale, width flexibility and motion
- [Header](docs/header.md) — Universal top bar, isometric unit cube mark, 3px active rule and theme toggle
- [Themes and navigation](docs/themes-and-navigation.md) — Cookie-persisted themes, sticky sidebars, top-bar search, drawers, breadcrumbs and tabs
- [Icons](docs/icons.md) — Any Tabler outline icon, sizing, semantic color usage and accessible labeling
- [Components](docs/components-and-icons.md) — Controls, panels, datasheets, status pills, tables, code/output wells, alerts and charts
- [Footer](docs/footer.md) — Generously spaced centered attribution, license, repository links and optional version line
- [Page archetypes](docs/page-archetypes.md) — Landings, catalogs, lookup tools, dashboards, admin apps and documentation
- [Review](docs/review.md) — Visual, responsive, accessibility and fallback audit checklist

## Apply to a project

UVY Design ships a single zero-dependency stylesheet ([site/uvy.css](site/uvy.css)) and optional shell script ([site/uvy.js](site/uvy.js)) so an engineer or AI agent can embed them directly into any Go `html/template`, HTMX, static HTML, Jekyll or SPA project:

1. Embed or link `site/uvy.css` (and `site/uvy.js` for the cookie-backed theme toggle, mobile drawer, tabs and copy buttons).
2. Use the inline `.uvy-mark` isometric cube SVG in `.site-header` and the square-canvas logo assets in [assets/](docs/logo.md) for favicons, READMEs and external avatars.
3. Inline only the [Tabler Icons](https://tabler.io/icons) outline SVGs your application uses (a starter subset lives in [site/icons.inc](site/icons.inc)).
4. Preserve the application's purpose, workflows, fields and domain data semantics while applying the `--uvy-*` tokens and `uvy-*` patterns.

## Explore the examples

Open the separate [examples index](examples/index.html) for 17 standalone HTML pages covering light and dark themes, official logo variants, typography, colored icons, both sidebar and top-bar navigation/search, tables, panels, forms and full page archetypes. Every example embeds `site/uvy.css` and `site/uvy.js` so it opens directly in a browser with no server or build step.

## Preview and publish

The documentation site built from this repository follows its own style guide using `site/uvy.css` and `site/uvy.js`. Generated output (`_site/`) is ignored; edit Markdown, HTML and `site/` sources instead. After editing `site/uvy.css` or `site/uvy.js`, run `python3 scripts/sync_examples.py` to refresh the standalone examples.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_site.py
.venv/bin/python scripts/check_site.py
.venv/bin/python -m http.server 8000 --directory _site
```

For browser regression checks, install `requirements-browser.txt`, run `.venv/bin/python -m playwright install --with-deps chromium`, and run `.venv/bin/python scripts/check_browser.py`. CI runs the same layout, cookie-theme, contrast, keyboard and interaction checks before publishing to [unitvectory-labs.github.io/uvy-design](https://unitvectory-labs.github.io/uvy-design/).
