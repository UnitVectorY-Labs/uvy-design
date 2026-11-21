# Components

Build with semantic HTML first and reach for namespaced `uvy-*` classes when a shared visual pattern helps. Applications own their markup and templates; copy the patterns from `site/reference.css` and the standalone examples.

| Component | Classes | Role |
| --- | --- | --- |
| Buttons | `.uvy-button`, `--primary`, `--quiet`, `--danger`, `--small`, `.icon-button` | One primary orange action per task; neutral secondary and borderless quiet actions |
| Toolbars | `.uvy-toolbar`, `.uvy-count` | Search inputs, selects, actions and live result counts aligned on one baseline |
| Panels | `.uvy-panel`, `__header`, `__footer` | Flat `--uvy-surface` containers with 6px corners and hairline borders; never nested |
| Datasheets | `.uvy-kv` | Two-column key/value metadata lists separated by hairlines |
| Summary strip | `.uvy-stats` | Single framed horizontal strip of headline metrics with 1px inner rules |
| Structured lists | `.uvy-list`, `__item`, `__primary`, `__meta` | Hairline-divided interactive rows inside a panel instead of nested cards |
| Status pills | `.uvy-status`, `--ok`, `--warn`, `--danger`, `--info`, `--active`, `--inactive`, `--critical`, `--running` | Changing operational or lifecycle state: colored dot + text inside a subtle capsule |
| Badges | `.uvy-badge` | Fixed technical attributes (algorithm, region, role type, protocol) in monospace |
| Tables | `.table-wrap`, `.uvy-table--compact`, `--comparison`, `--interactive`, `.num` | Subtle header row, horizontal dividers, tabular numerals, no zebra striping |
| Code viewers | `.uvy-code`, `__bar`, `--wrap`, `.uvy-copy` | Sunken monospace well with caption bar, copy button and optional wrapping |
| Alerts & empty | `.uvy-alert`, `--ok`, `--warn`, `--danger`, `.uvy-empty` | Restrained tinted alerts with icon + next step; dashed empty states with action |
| Loading & dialogs | `.uvy-spinner`, `[aria-busy="true"]`, `<dialog>` | Inline spinner or muted region during HTMX/async updates; structured native dialogs |

## Buttons, toolbars and forms

- Use one `.uvy-button--primary` per task or screen. Use active verbs (“Check domain”, “Save changes”, “Normalize”), never generic “Submit” or trailing arrows.
- Destructive actions (delete client, revoke key) use `.uvy-button--danger` and confirm inside a native `<dialog>` whose button names the destructive verb.
- Keep form labels visible above fields inside `.uvy-field`. Connect helper text and errors via `aria-describedby`. On validation failure, set `aria-invalid="true"`, explain how to fix the value in `.uvy-field-error`, focus the first invalid field, and preserve user input.
- Align filters, sort selects, density toggles and live item counts in `.uvy-toolbar` directly above the table or list they govern.

## Panels, datasheets and summary strips

- Use `.uvy-panel` to group cohesive content (an evidence table, a configuration form, a detail section). Do not nest panels inside panels: use `.uvy-list` for clickable rows inside a panel, and let `.table-wrap` bleed edge-to-edge inside a panel so table borders align cleanly with `.uvy-panel__header`.
- Use `.uvy-kv` (backed by `<dl>`) for entity metadata such as endpoints, issuers, timestamps, subjects and permissions. Pair copyable values with a compact `.uvy-copy` button.
- Use `.uvy-stats` (a single bordered `<dl>` strip) for 2–4 summary counts at the top of a catalog or dashboard rather than separate floating KPI cards.

## Status pills vs. attribute badges

Distinguish **mutable states** from **static properties**:

- **Status pills (`.uvy-status`)** carry a 6px circular dot and sentence-case text for states that reflect health, execution or lifecycle:
  - Operational: `--ok` (Passed, Valid, Completed), `--warn` (Expiring, Degraded), `--danger` (Failed, Invalid, High), `--info` (Queued, Running; add `--running` for a subtle halo), `--critical` (solid high-contrast danger fill for KEV / critical security findings).
  - Lifecycle: `--active` and `--inactive` map to `--uvy-active` / `--uvy-inactive` so key/record lifecycle remains distinct from error/success verdicts.
- **Attribute badges (`.uvy-badge`)** are bordered 3px-radius neutral monospace chips for fixed values such as `RS256`, `us-central1`, `Custom role`, or `v1.10.0`. Do not color-code every entity type with competing rainbow accents.

## Tables, spectra and mobile reflow

- Always include `<caption>` (visible or `.sr-only`), `<th scope="col">`, units in column headers, and `.num` right-alignment with `tabular-nums` for numbers.
- **Comparison tables** (`.uvy-table--comparison`) stay tabular at all widths inside a keyboard-focusable `.table-wrap` (`role="region" tabindex="0"`). Never silently drop columns on mobile.
- **Long record tables** (`.record-table`) may reflow below `768px` into labeled record cards where identity and release span full width above three equal, labeled metric cells.
- **Lifecycle rows** (`.lifecycle-active`, `.lifecycle-inactive`) and **quantitative spectra** (`.scale-low`, `.scale-mid`, `.scale-high`, `.scale-unknown`) always pair color with explicit text, a legend and numeric values. Keep unknown values distinct from zero.

## Code, JSON, tokens and copy actions

- Wrap multi-line JSON payloads, certificates, configs and commands in `.uvy-code` with a `.uvy-code__bar` caption and `.uvy-copy` button. Add `.uvy-code--wrap` for long unbroken strings such as JWTs, PEM blocks or SHA-256 digests so they never trap horizontal scroll.
- `.uvy-copy` confirms inline by swapping its icon/label to “Copied” in `--uvy-ok` for ~1.8 seconds and announcing the copy in a polite `role="status"` region when appropriate.

## Loading, HTMX updates, empty states and dialogs

- Keep loading indicators close to the region being updated: pair `.uvy-spinner` with descriptive text (“Checking certificate chain…”) or mark the updating container `aria-busy="true"`. In HTMX apps, reveal `.htmx-indicator` inline inside the toolbar or button without blocking unrelated controls.
- Empty states (`.uvy-empty`) explain why nothing is shown and provide a clear recovery action (“Clear filters”, “Inspect a domain”).
- Native `<dialog>` overlays use `.uvy-dialog__header`, `.uvy-dialog__body` and `.uvy-dialog__footer` with `--uvy-shadow-overlay`, an explicit close button, and Escape dismissal.

## Charts and diagrams

For uPlot, Chart.js and Mermaid diagrams:

- Read `--uvy-chart-1` through `--uvy-chart-6`, `--uvy-chart-grid`, `--uvy-chart-axis`, `--uvy-surface` and `--uvy-text` via `getComputedStyle(document.documentElement)` at render time and re-apply them when `data-theme` or `prefers-color-scheme` changes.
- Keep chart backgrounds flat (`--uvy-surface`), gridlines hairline (`--uvy-chart-grid`), axes in `--uvy-text-muted`, and numbers in `IBM Plex Mono` / tabular numerals.
- Reserve brand orange for interactive crosshairs or highlighted selections rather than making every series orange.

See [components](../examples/components.html), [forms](../examples/forms.html), [comparison table](../examples/table.html), [record table](../examples/table-records.html) and [detail panels](../examples/panels.html).
