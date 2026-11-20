# UVY Design

Current design guidance for Unit Vector Y Labs projects: minimal, precise engineering interfaces with neutral surfaces, restrained orange accents and first-class light and dark modes. This is an unversioned, human-readable reference. Each application owns its implementation; preserve its purpose, data semantics and workflows.

## Read the guide

- [Foundations](docs/foundations.md): principles and implementation approach.
- [Color](docs/color.md): semantic palette, contrast and status colors.
- [Typography and spacing](docs/typography-and-spacing.md): fonts, hierarchy and geometry.
- [Universal header](docs/header.md): shared anatomy and responsive behavior.
- [Page archetypes](docs/page-archetypes.md): layouts and hero policy.
- [Components and icons](docs/components-and-icons.md): controls, tables and feedback.
- [Themes and navigation](docs/themes-and-navigation.md): system preference and manual overrides.
- [Review](docs/review.md): practical checks across themes and screen sizes.

## Explore the examples

Open any HTML file directly in a browser. Each contains its own styles and scripts, with no server, build step or external assets required. The font stacks prefer locally installed IBM Plex fonts and fall back to system fonts.

| Example | What to inspect |
| --- | --- |
| [Landing page](examples/landing.html) | Compact hero, capabilities and one primary action |
| [Documentation article](examples/documentation.html) | Sidebar, readable article and code |
| [Compact utility](examples/utility.html) | Local input, action and output |
| [Forms and actions](examples/forms.html) | Validation, reset, inputs, select, textarea and alerts |
| [Key detail panels](examples/panels.html) | Endpoint summaries, lifecycle row tints, comparison tables and empty states |
| [Repository metrics](examples/table-records.html) | Long table, mobile record cards, sorting and independent metric spectra |
| [Typography and content](examples/typography.html) | Headings, lists, links and code |
| [Universal header](examples/navigation.html) | Top-left Tabler theme icon, searchable left navigation and mobile drawer |
| [Component catalog](examples/components.html) | Common components and routes to complete examples |

Related-guide links in the examples point to Markdown when opened locally. The web build converts these links to rendered guide pages. Original Markdown is also available from every rendered article.

## Preview and publish

The GitHub Pages build renders the Markdown and copies the standalone examples into one static site. Generated output is ignored; edit the Markdown, HTML and presentation sources instead. `site/reference.css` and `site/theme.js` style the published guide; the examples deliberately embed their own copies so each HTML file remains portable. After changing common CSS or shell behavior, run `python3 scripts/sync_examples.py` to refresh the embedded copies. Page content remains authored HTML.

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_site.py
.venv/bin/python scripts/check_site.py
.venv/bin/python -m http.server 8000 --directory _site
```

For browser regression checks, install `requirements-browser.txt`, run `python -m playwright install --with-deps chromium`, then `python scripts/check_browser.py` in the virtual environment. CI runs the same layout, keyboard, theme, data-contrast and interaction checks before publishing.

Open `http://localhost:8000`. Relative links also work under GitHub Pages repository subpaths and custom domains. The site needs no runtime JavaScript to read guides or navigate; JavaScript enables appearance controls and example interactions.

In repository **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. The included workflow checks pull requests and publishes pushes to `main`, or manual workflow runs. GitHub environment protection rules may require deployment approval. See [GitHub's custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

The published project URL is [unitvectory-labs.github.io/uvy-design](https://unitvectory-labs.github.io/uvy-design/); availability depends on the repository's Pages configuration and a successful workflow run.
