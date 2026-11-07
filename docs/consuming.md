# Consuming v0.1.0

Application pull requests implement these standards. PRs require review; adoption guidance here does not authorize merging or deployment.

## Pin and vendor

Pin the version in `VERSION` and the source commit you copied from, and record checksums. Copy `assets/uvy-tokens.css` and `assets/uvy-theme.js` into the consumer's local/embedded asset directory. `uvy-elements.css` is optional opt-in styling; map existing selectors to tokens instead of replacing layouts. Include the MIT license. Copy only needed SVGs from `icons/`, retain their MIT notice and render the paths inline in templates/HTML. Existing HTMX consumers may use `vendor/htmx-4.0.0.min.js`; retain its license and do not switch major versions casually. Do not add HTMX to vanilla-JS apps for consistency alone.

Load the theme script synchronously in head before local CSS. Then load tokens, optional treatments, and the app's CSS. No network retrieval from this repository occurs at runtime. Static generators copy files into their output; live Go apps embed them as required by their source architecture. Other required libraries, graphs and preview artwork must also be served locally; retain appropriate notices.

```html
<script src="assets/uvy-theme.js"></script>
<link rel="stylesheet" href="assets/uvy-tokens.css">
<link rel="stylesheet" href="assets/site.css">
```

## Theme button

Keep the native button at the header's top right, outside HTMX swap regions. Add `data-uvy-theme-toggle`, `hidden`, and an initial action name. Insert the official inline moon/sun SVGs with `aria-hidden="true" focusable="false"` in `.uvy-theme-dark-icon` / `.uvy-theme-light-icon` spans. Use `uvy-elements.css` or equivalent local adapter styles. The controller reveals and updates it. No System/reset UI is required. Do not keep an older localStorage theme handler active alongside it.

## Record adoption

Each consumer adds `UVY_DESIGN.md` (or the equivalent docs location) recording the design repository, version, source commit, copied file paths/checksums/licenses, adapter selectors/density, approved exceptions, verification and update procedure. Source assets are copied verbatim; put app-specific changes in adapter CSS. Future updates are reviewed diffs, never automatic runtime fetches.

Follow [style guide](style-guide.md), [component contracts](components.md) and [site audit checklist](site-audit-checklist.md). Preserve all fields, navigation, URLs, data computations and intentional green–yellow–red visualizations. A necessary responsive repair may wrap existing content; it must not hide fields or replace established workflows.

## PR evidence is mandatory

Each app gets its own branch, agent and PR. Identify major routes/page types and important states before editing. Capture before and after from identical local data whenever possible. Each major page needs eight screenshots: before/after × desktop/mobile × light/dark. Use 1440×1000 and 390×844, with full-page captures or supplemental images where content extends below the viewport. Verify 320px separately. If baseline lacks a theme, emulate both OS preferences and explicitly label its unchanged appearance; do not invent a dark baseline.

Use Playwright to capture browser screenshots. Preserve route/state/data/viewport/OS/resolved-theme/source-SHA provenance in a manifest. Put screenshot images in a dedicated evidence branch of the design repo, not application source trees; pin raw-image links to the evidence commit. Embed before/after comparison tables in each PR, grouped by page and theme. Include all requested images, with no local paths or inaccessible links. A small evidence index links full screenshots and verification. Follow stricter application screenshot rules where the available tools support them; record tool limitations explicitly.

## Validation

Run application tests/builds; exercise main workflows, sorting/filtering, copying, parse/error states, direct links and existing HTMX history/title/focus as applicable. Check cookie persistence, OS initial preference, both themes, mobile data preservation, keyboard/focus, long values and no external runtime requests. Verify source-data/licensing behavior separately. Document any actual limitations rather than claiming complete accessibility from screenshots.
