# UVY Design

Current design guidance for Unit Vector Y Labs projects: minimal, precise engineering interfaces with neutral surfaces, restrained orange accents and first-class light and dark modes. This is an unversioned, human-readable reference. Each application owns its implementation; preserve its purpose, data semantics and workflows.

## Read the guide

- [Foundations](docs/foundations.md)
- [Color](docs/color.md)
- [Typography and spacing](docs/typography-and-spacing.md)
- [Header](docs/header.md)
- [Themes and navigation](docs/themes-and-navigation.md)
- [Icons](docs/icons.md)
- [Components](docs/components-and-icons.md)
- [Footer](docs/footer.md)
- [Page archetypes](docs/page-archetypes.md)
- [Review](docs/review.md)

## Explore the examples

Open the separate [examples index](examples/index.html). Each page is a full-page implementation focused on one concept, with no guide sidebar. The [light](examples/light.html), [dark](examples/dark.html), [footer](examples/footer.html), [icons](examples/icons.html) and [table](examples/table.html) references are intentionally small. Complete static and dynamic layouts are available separately.

Every HTML example contains its own styles and behavior and can be opened directly in a browser. No server, build step or external assets are required. Font stacks prefer locally installed IBM Plex and fall back to system fonts. The web build renders Markdown guide pages and adapts links; the Markdown remains readable on its own.

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
