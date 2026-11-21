# Review

Review every adapted application in **light and dark modes** at **1280px**, **375px** and **320px**, plus **200% zoom**. Compare against the original application to confirm its purpose, data semantics and workflows remain intact.

## Visual craft and restraint

- Light mode uses crisp cool surfaces (`#F5F7FA` / `#FFFFFF`); dark mode uses deep midnight blue-slate (`#090D16` / `#111827`) paired with bright signal orange (`#F25C05` / `#FF7A1A`).
- `3px` signal-orange rules appear consistently on active header nav links, active sidebar links, active tabs, blockquotes, alerts and `.uvy-output` wells. No decorative gradients or ambient card shadows.
- Universally supported `system-ui` sans handles prose and forms; fixed-width `ui-monospace` handles the header brand, breadcrumbs, table headers, stat figures, badges, status pills, counts, timestamps and code/output wells.
- No nested `.uvy-panel` boxes, no uniform SaaS card grids where a hairline directory or table fits better, no ALL-CAPS eyebrows and no trailing arrows on buttons.
- Copy uses sentence case, active verbs and direct, non-apologetic error and empty states.

## Shell, cookie themes and footer

- Header is `60px` desktop with the `28×28` isometric unit cube mark (transparent standalone geometry adapting to light and dark surfaces) + `18px` monospace title left, full-height nav links with `3px` orange active bar, and a single borderless sun/moon toggle flush right on row 1 at every width. No “Use system theme” clutter button.
- Brand logo assets use the official square-canvas SVGs from `assets/` (standalone marks for transparent headers, favicons and READMEs; avatar marks with `11px` optical margin for profile images and rounded/circular crops controlled in CSS).
- Clicking the theme toggle switches immediately and persists via the `uvy-theme` cookie across pages (while forced specimen pages like `light.html` / `dark.html` keep their mode without overwriting the cookie). Content and navigation stay usable without JavaScript or cookies.
- Sticky sidebar layouts scroll naturally with the page and convert to an accessible focus-trapped mobile drawer below `768px`. Top-bar layouts without a sidebar keep search and filters clear in `.uvy-toolbar`.
- Footer has generous `32px` vertical padding on `--uvy-surface`, well-spaced `|` separators, calm muted links, monospace bold repository name(s), and omits the optional `.version` line completely from HTML when disabled.

## Contrast, data and accessibility

- Normal text meets **4.5:1** contrast on every surface, including lifecycle rows, status pills, alerts and quantitative spectrum cells. Essential borders, focus rings, `3px` indicators and meaningful icons (including colored Tabler icons) meet **3:1**. Primary orange buttons use dark `--uvy-on-accent` ink.
- Any Tabler outline icon used preserves its 24×24 viewBox, 2px stroke and accessible labeling (or `aria-hidden="true"` when paired with text).
- Lifecycle tints remain distinct from operational health verdicts; quantitative spectra retain direction, per-column scaling, units, legend and distinct unknown values; charts read `--uvy-chart-1..6`.
- Comparison tables scroll inside keyboard-focusable `.table-wrap` regions; mobile record tables reflow cleanly; zero horizontal page overflow occurs at 320px or 200% zoom; `prefers-reduced-motion: reduce` disables transitions and spinner rotation.

Run `scripts/check_site.py` and `scripts/check_browser.py`, then inspect rendered screenshots in both light and dark modes before shipping.
