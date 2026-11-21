# Typography and spacing

Use universally supported system fonts so `site/uvy.css` embeds cleanly into any application with zero external font files or network requests. Establish an unmistakable retro-terminal engineering voice by setting **structural chrome, headings and instrumentation in fixed-width `ui-monospace`**, while keeping **body prose and descriptions in crisp `system-ui` sans-serif**.

## Two-voice font system

- **Monospace (`--uvy-font-mono`)**: `ui-monospace, "Cascadia Mono", "SFMono-Regular", Menlo, Consolas, "Liberation Mono", "DejaVu Sans Mono", monospace` — landing display, `H1`–`H4` headings, header brand title, header & sidebar navigation, tabs, buttons, form labels and legends, panel & dialog titles, datasheet keys (`.uvy-kv dt`), directory titles (`.uvy-index strong`), table column headers, record row identifiers, stat strips, counts, status pills, badges, timestamps, technical inputs (`.uvy-input--mono`), versions and code/output wells.
- **Sans (`--uvy-font-sans`)**: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif` — body paragraphs, lead text (`.uvy-lead`), hints (`.uvy-hint`), list descriptions, alert copy, prose table cells and multiline prose textareas.

## Type scale

| Role | Font | Size | Weight | Line-height |
| --- | --- | --- | --- | --- |
| Landing display | Mono | 28–44px (`clamp(1.75rem, 1.3rem + 2.1vw, 2.75rem)`) | 700 | 1.12 |
| H1 page title | Mono | 24–34px (`clamp(1.5rem, 1.25rem + 1.1vw, 2.125rem)`) | 700 | 1.18 |
| H2 section heading | Mono | 21px / `1.3125rem` | 600 | 1.28 |
| H3 subheading | Mono | 17px / `1.0625rem` | 600 | 1.35 |
| Header brand | Mono | 14–17px (`clamp(0.875rem, 0.8rem + 0.35vw, 1.0625rem)`) | 600 | 1.2 |
| Panel title / H4 | Mono | 15px / `0.9375rem` | 600 | 1.4 |
| Nav, tabs, buttons, labels, keys | Mono | 13px / `0.8125rem` | 500 | 1.4 |
| Body prose | Sans | 16px / `1rem` | 400 | 1.65 |
| Descriptions, hints, prose cells | Sans | 14px / `0.875rem` | 400 | 1.55 |
| Table headers, badges, meta | Mono | 12px / `0.75rem` | 500 | 1.45 |

<div class="uvy-specimen type-preview"><span><small>Display · Mono</small><strong style="font-family:var(--uvy-font-mono);font-size:2rem;line-height:1.12;letter-spacing:-0.03em;font-weight:700">Inspect every certificate</strong></span><span><small>H1 · Mono</small><strong style="font-family:var(--uvy-font-mono);font-size:1.75rem;line-height:1.18;letter-spacing:-0.025em;font-weight:700">Service key details</strong></span><span><small>H2 · Mono</small><strong style="font-family:var(--uvy-font-mono);font-size:1.3125rem;line-height:1.28;letter-spacing:-0.02em;font-weight:600">Key observations</strong></span><span><small>Chrome · Mono</small><strong style="font-family:var(--uvy-font-mono);font-size:0.875rem;font-weight:600">UnitVectorY-Labs · Check domain · RS256</strong></span><span><small>Body · Sans</small><span>Readable system sans keeps documentation, explanations and alert copy effortless to scan alongside fixed-width terminal headings and controls.</span></span><span><small>Meta · Mono</small><span style="font-family:var(--uvy-font-mono);font-size:0.75rem;color:var(--uvy-text-muted)">2026-11-21T16:05:05Z · sha256:9f86d081 · 12 records</span></span></div>

## Terminal clarity without fatigue

- **Let monospace lead structure, keep prose in sans.** Giving headings, navigation, buttons, labels, keys and metrics a consistent fixed-width voice creates an immediate retro-terminal engineering feel across every page, while system sans preserves reading speed on multi-sentence prose.
- **Use `.uvy-input--mono` for technical inputs.** Apply `.uvy-input--mono` to inputs expecting domains, hostnames, identifiers, hashes, endpoints or search queries (`example.com`, `catalog.example.com`) so typed values match the terminal aesthetic.
- **Sentence case everywhere.** Headings, buttons, tabs, table headers and sidebar labels use sentence case — never tracked-out ALL CAPS.
- **Tabular numerals & UTC timestamps.** Apply `tabular-nums` to all tables, stat strips, counts and `<time>` elements (`2026-11-21 16:05 UTC` or ISO-8601 `2026-11-21T16:05:05Z`). Right-align numeric table columns (`.num`).
- **Measure.** Keep prose paragraphs and list items within `70ch` even inside full-width layouts.

## Spacing & flexible page width

Use the 8-step spacing scale **4, 8, 12, 16, 24, 32, 48, 64px** (`--uvy-space-1` through `--uvy-space-8`):

<div class="uvy-specimen spacing-preview"><div><i style="width:0.25rem" aria-hidden="true"></i><span>4px</span></div><div><i style="width:0.5rem" aria-hidden="true"></i><span>8px</span></div><div><i style="width:0.75rem" aria-hidden="true"></i><span>12px</span></div><div><i style="width:1rem" aria-hidden="true"></i><span>16px</span></div><div><i style="width:1.5rem" aria-hidden="true"></i><span>24px</span></div><div><i style="width:2rem" aria-hidden="true"></i><span>32px</span></div><div><i style="width:3rem" aria-hidden="true"></i><span>48px</span></div><div><i style="width:4rem" aria-hidden="true"></i><span>64px</span></div></div>

- **Default container (`.page`)**: Centered within `75rem` (`1200px`) with responsive side gutters (`clamp(1rem, 3vw, 2rem)`). Ideal for documentation, landing pages, forms and detail pages.
- **Full-width container (`.page--wide`)**: Expands fluidly to `100%` of the viewport (preserving the same side gutters). Pair with `.site-header--wide` and `.site-footer--wide` for dense operational dashboards, badge matrices and wide top-bar search tools.

## Geometry, 3px stroke & motion

- **Corners**: `3px` tags/badges/inline code, `4px` buttons/inputs/sidebar links, `5px` panels/code blocks/alerts, `6px` dialogs and drawers, `999px` status pills.
- **3px accent rule (`--uvy-stroke: 3px`)**: Used consistently on active header nav links, active sidebar items, active tabs, blockquotes, alerts and terminal output wells.
- **Targets & motion**: `36px` minimum control height (`44px` on coarse pointers); `120ms` state transitions and `180ms` drawer slides; disabled completely under `prefers-reduced-motion: reduce`.

See [typography](../examples/typography.html) and [top-bar wide layout](../examples/topbar.html).
