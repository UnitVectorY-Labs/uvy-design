# Typography and spacing

Use universally supported system fonts so `site/uvy.css` embeds cleanly into any application with zero external font files or network requests. Pair readable `system-ui` sans-serif prose with fixed-width `ui-monospace` instrumentation for subtle retro-terminal clarity.

## Font stacks

- **Sans (`--uvy-font-sans`)**: `system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif` — body copy, page headings, form controls, navigation links.
- **Monospace (`--uvy-font-mono`)**: `ui-monospace, "Cascadia Mono", "SFMono-Regular", Menlo, Consolas, "Liberation Mono", "DejaVu Sans Mono", monospace` — header brand title, breadcrumbs, table headers, stat values, counts, status pills, badges, timestamps, identifiers, versions and code/output wells.

## Type scale

| Role | Font | Size | Weight | Line-height |
| --- | --- | --- | --- | --- |
| Landing display | Sans | 36–52px (`clamp(2.25rem, 1.5rem + 3vw, 3.25rem)`) | 600 | 1.05 |
| H1 page title | Sans | 32–40px (`clamp(2rem, 1.65rem + 1.4vw, 2.5rem)`) | 600 | 1.12 |
| H2 section heading | Sans | 24px / `1.5rem` | 600 | 1.25 |
| H3 subheading | Sans | 18px / `1.125rem` | 600 | 1.35 |
| Header brand | Mono | 18px / `1.125rem` | 600 | 1.2 |
| Body text | Sans | 16px / `1rem` | 400 | 1.65 |
| UI controls, tables | Sans | 14px / `0.875rem` | 400 / 500 | 1.5 |
| Labels, headers, badges | Mono | 12px / `0.75rem` | 500 | 1.45 |

<div class="uvy-specimen type-preview"><span><small>Display</small><strong style="font-size:2.5rem;line-height:1.05;letter-spacing:-0.03em;font-weight:600">Inspect every certificate</strong></span><span><small>H1 · 40px</small><strong style="font-size:2.25rem;line-height:1.12;letter-spacing:-0.025em;font-weight:600">Service key details</strong></span><span><small>H2 · 24px</small><strong style="font-size:1.5rem;line-height:1.25;letter-spacing:-0.015em;font-weight:600">Key observations</strong></span><span><small>Brand · 18px</small><strong style="font-family:var(--uvy-font-mono);font-size:1.125rem;font-weight:600">UnitVectorY-Labs</strong></span><span><small>Body · 16px</small><span>Readable system sans keeps documentation and explanations effortless to scan.</span></span><span><small>Mono · 12px</small><span style="font-family:var(--uvy-font-mono);font-size:0.75rem;color:var(--uvy-text-muted)">2026-11-20 08:00 UTC · RS256 · sha256:9f86d081</span></span></div>

## Subtle terminal restraint

- **Keep prose in sans-serif.** Fixed-width type brings crisp technical character when reserved for structural labels, metrics, paths, timestamps and code. Do not set long paragraphs in monospace.
- **Sentence case everywhere.** Headings, buttons, tabs, table headers and sidebar labels use sentence case — never tracked-out ALL CAPS.
- **Tabular numerals & UTC timestamps.** Apply `tabular-nums` to all tables, stat strips, counts and `<time>` elements (`2026-11-20 08:00 UTC`). Right-align numeric table columns (`.num`).
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
