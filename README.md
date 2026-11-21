# UVY Design

Current design guidance for Unit Vector Y Labs projects: quiet, precise engineering interfaces built on cool graphite surfaces, IBM Plex typography, a single 2px signal-orange accent rule, and first-class light and dark modes. This repository is an unversioned, human-readable reference. Each application owns its implementation; preserve its purpose, data semantics and workflows.

## Read the guide

- [Foundations](docs/foundations.md) — Aesthetic direction, restraint rules and adoption contract
- [Color](docs/color.md) — Graphite surfaces, signal orange, status, lifecycle, spectra and charts
- [Typography and spacing](docs/typography-and-spacing.md) — IBM Plex type scale, measure, numerals, geometry and motion
- [Header](docs/header.md) — Universal top bar, brand mark, active rule and theme switch
- [Themes and navigation](docs/themes-and-navigation.md) — Light/dark contract, sidebars, drawers, breadcrumbs, tabs and pagination
- [Icons](docs/icons.md) — Tabler outline icons, sizing, neutral-by-default coloring and labeling
- [Components](docs/components-and-icons.md) — Controls, panels, datasheets, status pills, tables, code viewers, alerts and charts
- [Footer](docs/footer.md) — Centered attribution, license, repository links and optional version line
- [Page archetypes](docs/page-archetypes.md) — Landings, catalogs, lookup tools, dashboards, admin apps and documentation
- [Review](docs/review.md) — Visual, responsive, accessibility and fallback audit checklist

## Explore the examples

Open the separate [examples index](examples/index.html). Each example is a focused, standalone page with no guide sidebar. Every HTML file embeds its own stylesheet and shell behavior so it opens directly in a browser without a server or build step.

## Apply to a project

Copy the semantic token block (`--uvy-*`) and the needed component patterns from [site/reference.css](site/reference.css), the inline Tabler sprite from [site/icons.inc](site/icons.inc), and the theme/drawer script from [site/theme.js](site/theme.js). Self-host the IBM Plex WOFF2 files in [site/fonts/](site/fonts/) with their SIL OFL license notice, or rely on system fallbacks when a project must stay single-file.

## Preview and publish

The GitHub Pages build renders the Markdown guides and copies the standalone examples into one static site. Generated output (`_site/`) is ignored; edit the Markdown, HTML and `site/` sources instead. After editing `site/reference.css` or `site/theme.js`, run `python3 scripts/sync_examples.py` to refresh the embedded copies in `examples/*.html`.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_site.py
.venv/bin/python scripts/check_site.py
.venv/bin/python -m http.server 8000 --directory _site
```

For browser regression checks, install `requirements-browser.txt`, run `.venv/bin/python -m playwright install --with-deps chromium`, and run `.venv/bin/python scripts/check_browser.py`. CI runs the same layout, contrast, keyboard, theme and interaction checks before publishing.

Open `http://localhost:8000`. All links stay relative so the site works under GitHub Pages repository subpaths and custom domains. Reading guides and navigating require no JavaScript; JavaScript enhances theme switching, drawers, tabs, copy buttons and example filters.

In repository **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. The published project URL is [unitvectory-labs.github.io/uvy-design](https://unitvectory-labs.github.io/uvy-design/).
