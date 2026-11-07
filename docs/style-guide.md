# Style guide — v0.1.0

Apply these styles to existing application elements. This guide does not authorize a new layout, navigation system, section hierarchy, tab or disclosure. Application changes land through per-application pull request review.

## Application boundary

Keep the existing page structure and workflows. Style the existing masthead, headings, controls, records and footer. Use JWKS explorer, UnreleasedCommits index/detail and CertSummary workspace as the first examples. Do not turn the explorer into a flat generic catalog, turn a workspace into marketing panels or move normal data behind tabs. Keep standalone project identity, without organization branding or decorative labels.

## Color tokens

These v0.1.0 values are the normative reference. The `--uvy-` prefix namespaces CSS tokens; it is not visible branding. Adapt a consumer's existing variable names or map them explicitly rather than forcing markup changes. Blue/orange branding and data/status colors have separate roles.

| Token | Light | Dark | Usage |
| --- | --- | --- | --- |
| `--uvy-page` | `#f3f6fc` | `#0c1729` | Existing page background |
| `--uvy-surface` | `#ffffff` | `#14243c` | Cards, input/output areas |
| `--uvy-text` | `#182b49` | `#edf3ff` | Body text and headings |
| `--uvy-muted` | `#50617c` | `#b2c2da` | Supporting labels and metadata |
| `--uvy-divider` | `#cfdaeb` | `#354b6b` | Quiet structural lines |
| `--uvy-control` | `#7285a1` | `#8096b7` | Input/button boundaries |
| `--uvy-link` | `#1558ba` | `#8dbbff` | Links and selected text |
| `--uvy-blue-soft` | `#e9f1ff` | `#1b3559` | Selected/hover surface |
| `--uvy-masthead` | `#1558ba` | `#104ca7` | Existing project header |
| `--uvy-on-masthead` | `#ffffff` | `#ffffff` | Header title/navigation |
| `--uvy-section` | `#e3edff` | `#203f6a` | Blue-tinted table/section header |
| `--uvy-accent` | `#a83e00` | `#ffb16d` | Orange text and focus accent |
| `--uvy-accent-fill` | `#ff932e` | `#ff932e` | Orange masthead bottom rule |
| `--uvy-accent-ink` | `#34200b` | `#34200b` | Text on orange fill |
| `--uvy-accent-soft` | `#fff0df` | `#392719` | Orange-tinted note surface |
| `--uvy-focus` | `#1558ba` | `#ffb16d` | Focus on neutral surfaces |
| `--uvy-success` | `#166338` | `#91dfb4` | Explicit success text |
| `--uvy-success-soft` | `#e6f5ed` | `#193d31` | Success surface |
| `--uvy-warning` | `#805600` | `#f8d778` | Explicit warning text |
| `--uvy-warning-soft` | `#fff4cc` | `#3b321b` | Warning surface |
| `--uvy-danger` | `#a32232` | `#ffabb5` | Explicit error text |
| `--uvy-danger-soft` | `#fdecef` | `#45212c` | Error surface |

White text pairs with masthead blue. Dark `accent-ink` pairs with orange fill. Ordinary links use the theme's link token; a filled blue action may pair pale dark-mode blue with dark surface-colored text, or use masthead blue with white text, provided its chosen pair is contrast-checked. Do not put white small text on a light orange surface.

The section token is a blue tint; an existing strong blue header may use masthead/on-masthead instead. Select the treatment for an existing element, consistently, rather than adding a new header band to every group.

The palette is a visual contract, not a blanket contrast certification. Measure actual text, hover, focus and control pairs. Use `control` for interactive edges rather than the fainter `divider`. Header focus uses white so it remains visible on blue.

## Preserve data color mappings

UnreleasedCommits already computes green–yellow–red backgrounds and corresponding foregrounds for three metrics. Preserve the computation, thresholds, interpolation, direction and data values. Do not replace it with blue/orange branding or a generic status badge. Its three metrics remain individually labeled and numeric; do not turn the whole repository card red because one cell is red.

Theme adaptations may change a cell's luminance/foreground to remain readable while preserving its green/yellow/red relationship and meaning. Check low, middle and high values for each metric against the source application. Add no new severity interpretation. If a future legend is needed, propose it separately rather than inventing thresholds in the shared CSS.

## Typography

```css
--uvy-font: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
--uvy-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
```

System fonts intentionally avoid downloads, third-party requests and font-loading shifts. Use monospace for code, URLs/keys where exact characters matter and raw output; do not apply it to every label. Numeric metrics use `font-variant-numeric: tabular-nums`.

| Role | Size / line-height | Weight |
| --- | --- | --- |
| Project title | 26px / 1.25 | 700 |
| Existing page H1 | 28px / 1.25 | 700 |
| Section heading | 18px / 1.35 | 650 |
| Group heading | 16px / 1.4 | 600 |
| Body / controls | 16px / 1.5 | 400 / 600 for action labels |
| Data / code | 14px / 1.5–1.6 | 400 |
| Supporting label | 13px / 1.4 | 400–600 |
| Mobile metric label | 12px / 1.35 | 500 |
| Mobile metric value | 18px / 1.3 | 650 |

These roles style existing hierarchy; they do not require adding headings. Do not shrink essential values below 14px. A small mobile metric label supports a nearby prominent value and must remain readable and wrap naturally. Use sentence case. No decorative uppercase eyebrow, subtitle or slogan.

## Spacing and density

Spacing tokens are 4, 8, 12, 16, 24, 32 and 48px. Keep existing layout widths and column proportions unless responsive fit requires a separately reviewed correction. Density is selected per application or existing region; it does not require a new UI control or persist another preference.

| Measurement | Compact | Standard | Spacious |
| --- | --- | --- | --- |
| Page section gap | 16px | 24px | 32px |
| Existing card/panel padding | 12px | 16px | 24px |
| Table cell vertical padding | 8px | 12px | 16px |
| Table cell horizontal padding | 12px | 16px | 20px |
| Related field gap | 8px | 12px | 16px |
| Separate control-group gap | 12px | 16px | 24px |
| Button horizontal padding | 12px | 16px | 20px |
| Minimum primary touch target | 44px | 44px | 44px |

Compact changes whitespace, not type legibility, content, actions or keyboard targets. Keep all three metrics in the mobile UnreleasedCommits card at every density. Increase spacing for a workspace when useful without rebuilding its columns. Do not use arbitrary per-page spacing values when a token fits.

Example mapping to existing selectors:

```css
:root { --uvy-panel-pad: 16px; --uvy-row-y: 12px; --uvy-group-gap: 16px; }
[data-density="compact"] { --uvy-panel-pad: 12px; --uvy-row-y: 8px; --uvy-group-gap: 12px; }
[data-density="spacious"] { --uvy-panel-pad: 24px; --uvy-row-y: 16px; --uvy-group-gap: 24px; }
/* Map existing application selectors to these tokens; retain their layout. */
```

## Corners, borders and shadows

Use 1px dividers and control edges, 4px radius for small badges/code regions, 6px for controls and 8px for existing cards/panels. The orange masthead rule is 4px. Use slight rounding consistently rather than alternating pills and sharp rectangles without purpose.

A subtle shadow on existing elevated cards is allowed and desired as part of the Tabler-inspired direction: light `0 1px 3px rgb(24 43 73 / 8%)`, dark `0 1px 3px rgb(0 0 0 / 24%)`. Borders still define the edge. Do not add nested panels or lift every table cell. Hover can change color/border without translating or scaling a record.

## Icons

Use [Tabler outline icons](https://docs.tabler.io/icons) as inline SVG with a 24×24 viewBox, `fill="none"`, `stroke="currentColor"`, consistent stroke width 2 and rounded line caps/joins. Default displayed size is 20px; 16px for inline metadata and 24px for a prominent action. Align icons with their accompanying label with an 8px gap.

Select icons that identify actual actions: sun/moon for theme, search for search, copy for copy and an external-link mark only when needed. Do not add an icon to every heading. Decorative icons get `aria-hidden="true"` and `focusable="false"`; icon-only buttons receive a direct accessible action name. Preserve the icon source/version and MIT notice when copying SVG paths. Do not use icon fonts, remotely fetched SVG, emoji or a JavaScript icon package.

Tabler UI is a [visual reference](https://docs.tabler.io/ui), not a required dependency. Its broad component catalog does not justify adding those components to an application.

## Reusable element treatments

| Existing element | Style guidance | Preserve |
| --- | --- | --- |
| Masthead | Blue, white project title, orange bottom rule, top-right binary theme toggle | Project identity and current navigation |
| Navigation | Consistent spacing, visible active state and focus | Existing destinations, labels and order |
| Search/filter | Visible label, control boundary, 6px corners | Existing behavior, options and URL state |
| Table | Blue-led header, aligned values, row spacing by density | Columns, sorting and meaningful color mappings |
| Existing card | 8px corners, subtle border/shadow | Its content groups and actions |
| Technical output | Local monospace, wrap or local overflow, readable size | Exact value and existing copy/download |
| Status | Word/value plus semantic colors | Existing domain meaning |
| Footer | Project GitHub and MIT license links, compact spacing | Correct current-project destinations |

Do not introduce new tabs/disclosures or hide normal data to make the visual specimen look cleaner. Existing specialized interaction semantics still need accessibility checks, but changing information architecture is not part of adopting these styles.

## Mobile examples

For UnreleasedCommits index, preserve its established pattern: repository title and latest release above a single row of three side-by-side metric cells. Small labels identify unreleased commits, days behind and days since release. Keep the original heat colors per cell, links and mobile sort control. Labels can wrap; values stay prominent. Use `minmax(0, 1fr)` for the three equal cells and permit long repository names to wrap. At 320px, do not remove a metric or replace the row with a tall definition list.

JWKS explorer retains its existing explorer navigation/content relationship and available controls. UnreleasedCommits repository detail retains its sections and commit information. CertSummary retains input/output workspace structure and existing conversion behavior, stacking established workspace regions only as appropriate to its current mobile model. A shared style is not a universal mobile card template.

## Footer and theme

The footer links to the standalone project's own repository and MIT license. `body` uses a full-height flex column; `main` grows; footer is normal flow. No fixed footer or overlay. Theme behavior follows [the interaction contract](theme-and-interaction-contract.md): first visit OS preference, top-right binary toggle, explicit host-only cookie, no System selector or extra reset UI.

## Delivery and review checklist

All runtime files ship with the application: local pinned HTMX, local CSS/JS, system fonts and inline Tabler SVG. Static output copies assets; live Go apps embed them. No CDN, remote font, icon font or Tabler/Bootstrap runtime is introduced. Preserve existing dependencies only where separately reviewed; a new shared element must not add a remote runtime requirement.

For each application PR, compare actual-layout before/after screenshots in light/dark and standard/compact/spacious densities. Confirm all fields/navigation remain present; UnreleasedCommits metrics and spectrum match; mobile title/release/three-cell layout fits; JWKS explorer and CertSummary workspace remain recognizable; keyboard focus/contrast and 200% zoom work; and short/long pages place the footer correctly. Check network requests to confirm self-contained asset delivery. Record any structural change as a separate proposal rather than disguising it as a token update.

## Specimen token mapping

The examples currently retain short CSS names from their review stylesheet. The table below is the explicit mapping to the namespaced guide; it does not require consumers to rename their existing selectors.

| Guide role | Specimen variable |
| --- | --- |
| page / surface / text / muted | `--bg` / `--surface` / `--text` / `--muted` |
| divider / control | `--line` / `--control` |
| link / blue-soft / masthead / section | `--blue` / `--blue-soft` / `--masthead` / `--section` |
| accent / accent-fill / accent-ink / accent-soft | `--orange` / `--orange-fill` / `--orange-ink` / `--orange-soft` |
| focus / success / success-soft | `--focus` / `--success` / `--success-soft` |
| panel padding / row vertical / row horizontal | `--pad` / `--row-y` / `--row-x` |
| section / related field / control-group gap | `--gap` / `--field-gap` / `--group-gap` |
| button horizontal padding / shadow | `--button-x` / `--shadow` |

On-masthead is white in both modes. Warning/danger roles are specified for future state examples but are not exercised by these bounded screenshots. Check source-linked values and selected contrast results rather than treating a token table as a complete accessibility pass.

## Implementation source and version

Use the [v0.1.0 consuming instructions](consuming.md). Canonical shared tokens are in `assets/uvy-tokens.css`; `assets/uvy-theme.js` implements the cookie contract; `assets/uvy-elements.css` is opt-in. Inline official source SVGs from `icons/`. Map existing selectors rather than copying the prototype layout stylesheet. Each consumer pins the version and records provenance. All major pages require desktop/mobile and light/dark before/after evidence embedded in its PR.
