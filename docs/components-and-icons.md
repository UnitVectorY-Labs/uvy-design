# Components

Build with semantic HTML first and apply the namespaced `uvy-*` patterns from `site/uvy.css`. Copy the stylesheet verbatim so every UnitVectorY-Labs project shares identical controls, spacing and states.

| Component | Classes | Role |
| --- | --- | --- |
| Buttons | `.uvy-button`, `--primary`, `--quiet`, `--danger`, `--small`, `.icon-button` | One bright orange primary action per task; neutral secondary and quiet actions |
| Toolbars | `.uvy-toolbar`, `.uvy-count` | Search, selects, actions and monospace result counts aligned on one baseline |
| Panels | `.uvy-panel`, `__header`, `__footer` | Flat `--uvy-surface` containers with 5px corners and hairline borders; never nested |
| Datasheets | `.uvy-kv` | Two-column key/value metadata lists divided by hairlines |
| Summary strip | `.uvy-stats` | Single framed strip of monospace tabular headline metrics |
| Structured lists | `.uvy-list`, `__item`, `__primary`, `__meta` | Hairline-divided interactive rows inside a panel instead of nested cards |
| Status pills | `.uvy-status`, `--ok`, `--warn`, `--danger`, `--info`, `--active`, `--inactive`, `--critical`, `--running` | Changing operational or lifecycle state: colored dot + monospace text |
| Badges | `.uvy-badge` | Fixed technical properties (algorithm, region, version, role type) in monospace |
| Tables | `.table-wrap`, `.uvy-table--compact`, `--comparison`, `--interactive`, `.num` | Sunken monospace column headers, hairline rows, tabular numerals, no zebra striping |
| Code & output | `.uvy-code`, `__bar`, `--wrap`, `.uvy-output`, `.uvy-copy` | Sunken code blocks with copy bar, plus 3px-accented terminal output wells |
| Alerts & empty | `.uvy-alert`, `--ok`, `--warn`, `--danger`, `.uvy-empty` | 3px left-accented status alerts with icons; dashed empty states with recovery action |
| Loading & dialogs | `.uvy-spinner`, `[aria-busy="true"]`, `<dialog>` | Inline spinner or muted container during HTMX/async updates; structured native dialogs |

## Buttons, toolbars and forms

- Use one `.uvy-button--primary` per task or screen. Name buttons with plain active verbs (“Check domain”, “Save changes”, “Normalize”), never generic “Submit” or trailing arrows.
- Destructive actions use `.uvy-button--danger` and confirm inside a native `<dialog>` whose action repeats the destructive verb.
- Keep visible `<label>` elements above inputs in `.uvy-field` (rendered in fixed-width monospace). Add `.uvy-input--mono` to inputs that hold technical identifiers such as domains, endpoints, hashes or search filters. Connect hints and inline errors via `aria-describedby`. On validation failure, set `aria-invalid="true"`, show `.uvy-field-error` with a Tabler `alert-circle` icon, focus the first invalid field and retain entered values.
- Place search inputs, selects, sort controls and `.uvy-count` inside `.uvy-toolbar` directly above the results they filter.

## Panels, datasheets and summary strips

- Never nest `.uvy-panel` inside `.uvy-panel`. Use `.uvy-list` for clickable rows inside a panel, and place `.table-wrap` directly inside `.uvy-panel` so tables bleed cleanly edge-to-edge under `.uvy-panel__header`.
- Use `.uvy-kv` (`<dl>`) for entity metadata (endpoints, issuers, timestamps, subjects, permissions) with compact `.uvy-copy` buttons beside copyable values.
- Use `.uvy-stats` (a single bordered `<dl>` strip) for 2–4 headline metrics rather than disconnected floating cards.

## Status pills vs. attribute badges

- **Status pills (`.uvy-status`)** carry a colored dot and concise text for states that change: `--ok`, `--warn`, `--danger`, `--info` (`--running` adds a subtle pulse halo), `--critical` (solid danger fill for KEV / critical findings), and lifecycle `--active` / `--inactive`.
- **Attribute badges (`.uvy-badge`)** tag static technical properties (`RS256`, `us-central1`, `v1.10.0`, `Custom role`) in neutral monospace without competing entity colors.

## Tables, spectra and mobile reflow

- Include `<caption>` (visible or `.sr-only`), `<th scope="col">`, explicit units, and right-aligned `.num` columns.
- **Comparison tables** (`.uvy-table--comparison`) remain tabular inside a keyboard-focusable `.table-wrap` (`role="region" tabindex="0"`). Never silently drop columns on mobile.
- **Record tables** (`.record-table`) reflow below `768px` into labeled mobile cards preserving every value, link and sort option.
- **Lifecycle rows** and **quantitative spectra** pair color with explicit text, units and a legend, keeping unknown values neutral and distinct from zero.

## Code blocks, terminal output and copy actions

- Wrap JSON payloads, YAML, certificates and commands in `.uvy-code` with `.uvy-code__bar` and `.uvy-copy`. Add `.uvy-code--wrap` for long JWTs, PEM blocks or digests.
- For single-value utility outputs, use `.uvy-output` (sunken well, 3px orange left bar, subtle `>` prompt glyph and copy button) to reinforce the terminal utility character without clutter.

## Loading, HTMX updates, empty states and dialogs

- Keep `.uvy-spinner` or `aria-busy="true"` next to the region being updated; reveal `.htmx-indicator` inline without blocking unrelated controls.
- `site/uvy.js` delegates `.uvy-copy` (`[data-copy-target]`, `[data-copy-text]`) and `[role="tablist"]` interactions at the `document` level and re-enhances `[data-enable-with-js]` / `[data-requires-js]` automatically on `htmx:afterSwap` and `htmx:after:swap` (and exposes `window.uvyEnhance(root)` for client-rendered fragments).
- `.uvy-empty` explains why nothing is shown and offers a direct next action.
- Native `<dialog>` overlays use `.uvy-dialog__header`, `.uvy-dialog__body` and `.uvy-dialog__footer` with `--uvy-shadow-overlay`, an explicit close button and Escape dismissal.

## Charts and diagrams

- For time-series plots, paired KPI cards and breakdown sparklines, follow the [charts and graphs](charts.md) guide.
- For canvas libraries (uPlot, Chart.js), resolve `--uvy-chart-1..6`, semantic status tokens (`--uvy-ok`, `--uvy-warn`, `--uvy-danger`), `--uvy-chart-grid`, `--uvy-chart-axis`, `--uvy-surface` and `--uvy-text` to computed `rgb(...)` values through a hidden probe element (because `getPropertyValue` returns literal `light-dark(...)` strings) and re-render whenever `data-theme` or `prefers-color-scheme` changes.
- For SVG diagrams (including Mermaid), bind node fills, strokes, edges and cluster borders directly to `--uvy-*` CSS custom properties (`light-dark()`) so theme toggles recolor the diagram immediately without re-rendering.

See [components](../examples/components.html), [forms](../examples/forms.html), [comparison table](../examples/table.html), [record table](../examples/table-records.html), [detail panels](../examples/panels.html), [charts and graphs](../examples/charts.html) and [utility](../examples/utility.html).
