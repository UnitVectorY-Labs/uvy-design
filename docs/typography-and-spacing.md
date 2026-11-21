# Typography and spacing

Set interfaces in **IBM Plex Sans** and technical values in **IBM Plex Mono**. Self-host WOFF2 font files (400, 400 italic, 500, 600 for Sans; 400, 500 for Mono) alongside their SIL OFL license notice, keeping system sans-serif and monospace fallbacks so pages render cleanly offline or in single-file utilities.

## Type scale

| Role | Size | Weight | Line-height | Tracking |
| --- | --- | --- | --- | --- |
| Landing display | 36–48px (`clamp(2.25rem, 1.5rem + 3vw, 3rem)`) | 600 | 1.05 | `-0.03em` |
| H1 page title | 30–36px (`clamp(1.875rem, 1.5rem + 1.25vw, 2.25rem)`) | 600 | 1.15 | `-0.02em` |
| H2 section heading | 24px / `1.5rem` | 600 | 1.25 | `-0.01em` |
| H3 subheading | 18px / `1.125rem` | 600 | 1.35 | `0` |
| H4 / panel heading | 16px / `1rem` | 600 | 1.4 | `0` |
| Body text | 16px / `1rem` | 400 | 1.6 | `0` |
| UI text, controls, tables | 14px / `0.875rem` | 400 / 500 | 1.45 | `0` |
| Labels, table headers, captions | 12px / `0.75rem` | 500 | 1.4 | `0.01em` |

<div class="type-preview"><span><small>Display</small><strong style="font-size:2.5rem;line-height:1.05;letter-spacing:-0.03em;font-weight:600">Inspect every certificate</strong></span><span><small>H1 · 36px</small><strong style="font-size:2.25rem;line-height:1.15;letter-spacing:-0.02em;font-weight:600">Service key details</strong></span><span><small>H2 · 24px</small><strong style="font-size:1.5rem;line-height:1.25;letter-spacing:-0.01em;font-weight:600">Key observations</strong></span><span><small>H3 · 18px</small><strong style="font-size:1.125rem;line-height:1.35;font-weight:600">Provider evidence</strong></span><span><small>Body · 16px</small><span>Neutral graphite surfaces and clear hierarchy keep dense technical data scannable.</span></span><span><small>UI · 14px</small><span style="font-size:0.875rem;color:var(--uvy-text-muted)">Secondary text, table cells, form labels and helper hints.</span></span><span><small>Label · 12px</small><span style="font-size:0.75rem;font-weight:500;color:var(--uvy-text-muted)">Sentence-case label or table column header</span></span></div>

## Typographic craft

- **Sentence case everywhere.** Headings, buttons, tabs, table headers and sidebar group labels use sentence case. Never set labels in tracked-out ALL CAPS.
- **No decorative eyebrows or word highlights.** Do not stack unnecessary category eyebrows above headings, and do not italicize or recolor a single word inside a headline for drama.
- **Selective monospace.** Use `IBM Plex Mono` for identifiers, domains, URLs, commit SHAs, versions, algorithms, permissions, timestamps and code blocks — not for prose UI labels or decorative headings.
- **Tabular numerals.** Apply `font-variant-numeric: tabular-nums` on tables, stat strips, counts and `<time>` elements so columns align vertically. Right-align numeric table columns (`.num`).
- **Timestamps.** Format operational timestamps consistently in ISO-like UTC (`2026-11-20 08:00 UTC`) with `<time datetime="...">`. If relative time (“3h ago”) helps scanning, include the exact UTC timestamp in the `title` attribute or detail view.
- **Measure and wrapping.** Keep prose paragraphs and list items within `70ch`. Use `text-wrap: balance` on headings and `overflow-wrap: anywhere` on long identifiers and URLs so nothing pushes the viewport horizontally.

## Spacing scale

Use the 8-step scale **4, 8, 12, 16, 24, 32, 48, 64px** (`--uvy-space-1` through `--uvy-space-8`). Center page content within `75rem` (1200px) with responsive side gutters (`clamp(1rem, 3vw, 2rem)`). Start with 24px desktop panel padding (16px on mobile), 8–12px control gaps, 24px between stacked panels and 48px above major sections.

<div class="spacing-preview"><div><i style="width:0.25rem" aria-hidden="true"></i><span>4px</span></div><div><i style="width:0.5rem" aria-hidden="true"></i><span>8px</span></div><div><i style="width:0.75rem" aria-hidden="true"></i><span>12px</span></div><div><i style="width:1rem" aria-hidden="true"></i><span>16px</span></div><div><i style="width:1.5rem" aria-hidden="true"></i><span>24px</span></div><div><i style="width:2rem" aria-hidden="true"></i><span>32px</span></div><div><i style="width:3rem" aria-hidden="true"></i><span>48px</span></div><div><i style="width:4rem" aria-hidden="true"></i><span>64px</span></div></div>

## Geometry, borders and motion

Corner radii encode hierarchy instead of using one radius everywhere:

| Element | Radius | Border / elevation |
| --- | --- | --- |
| Tags, badges, inline code, `<kbd>` | `3px` (`--uvy-radius-tag`) | `1px solid --uvy-border` (badges) |
| Buttons, inputs, sidebar links | `4px` (`--uvy-radius-control`) | `1px solid --uvy-border-emphasis` / `--uvy-border-input` |
| Panels, alerts, code blocks, stat strips | `6px` (`--uvy-radius-panel`) | `1px solid --uvy-border`, no shadow |
| Dialogs and drawers | `8px` (`--uvy-radius-overlay`) | `1px solid --uvy-border` + `--uvy-shadow-overlay` |
| Status pills | `999px` (capsule) | Tinted fill with dot, no heavy border |

Buttons and inputs default to `36px` (`2.25rem`) minimum height, expanding to `44px` (`2.75rem`) on `@media (pointer: coarse)`. Textareas grow with content (`field-sizing: content`).

State transitions (hover fills, border shifts, underline opacity) run for `120ms` (`--uvy-duration`) with `cubic-bezier(0.2, 0, 0, 1)`; drawer slides run for `180ms`. Disable all transitions and animations under `@media (prefers-reduced-motion: reduce)`.

See the [typography example](../examples/typography.html).
