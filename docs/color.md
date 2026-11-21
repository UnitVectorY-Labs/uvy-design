# Color

Pair crisp cool-light surfaces and deep midnight blue-slate dark surfaces with bright signal orange. The cool blue undertone in dark mode complements orange cleanly while keeping dense tables, code blocks and status indicators calm and legible.

## Core semantic tokens

Define colors with `color-scheme: light dark` and `light-dark()` so light and dark modes share one token block in `site/uvy.css`.

| Token | Role | Light mode | Dark mode |
| --- | --- | --- | --- |
| `--uvy-bg` | Page canvas | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#F5F7FA" aria-hidden="true"></span> `#F5F7FA` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#090D16" aria-hidden="true"></span> `#090D16` |
| `--uvy-surface` | Panels, header, footer, inputs | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#FFFFFF" aria-hidden="true"></span> `#FFFFFF` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#111827" aria-hidden="true"></span> `#111827` |
| `--uvy-sunken` | Code wells, table headers, inline code | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#ECEFF4" aria-hidden="true"></span> `#ECEFF4` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#060911" aria-hidden="true"></span> `#060911` |
| `--uvy-hover` | Subtle interactive fill | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#E6EAF0" aria-hidden="true"></span> `#E6EAF0` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#1B2538" aria-hidden="true"></span> `#1B2538` |
| `--uvy-border` | Hairline dividers, panels | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#D8DFE8" aria-hidden="true"></span> `#D8DFE8` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#1F2B40" aria-hidden="true"></span> `#1F2B40` |
| `--uvy-border-emphasis` | Table header rules, secondary buttons | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#BFC8D6" aria-hidden="true"></span> `#BFC8D6` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#2E3F5C" aria-hidden="true"></span> `#2E3F5C` |
| `--uvy-border-input` | Input boundaries (≥ 3:1) | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#7A8596" aria-hidden="true"></span> `#7A8596` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#6B7D99" aria-hidden="true"></span> `#6B7D99` |
| `--uvy-text` | Primary text and headings | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#111827" aria-hidden="true"></span> `#111827` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#F0F4FA" aria-hidden="true"></span> `#F0F4FA` |
| `--uvy-text-muted` | Secondary text, metadata, labels | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#4B5565" aria-hidden="true"></span> `#4B5565` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#9AA8BF" aria-hidden="true"></span> `#9AA8BF` |
| `--uvy-text-faint` | Placeholders, version footers | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#697486" aria-hidden="true"></span> `#697486` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#77869E" aria-hidden="true"></span> `#77869E` |
| `--uvy-accent` | Primary fill, j-hat tile, 3px active rule | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#F25C05" aria-hidden="true"></span> `#F25C05` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FF7A1A" aria-hidden="true"></span> `#FF7A1A` |
| `--uvy-accent-hover` | Primary button hover | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#DB4F00" aria-hidden="true"></span> `#DB4F00` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FF9140" aria-hidden="true"></span> `#FF9140` |
| `--uvy-on-accent` | Dark ink on signal orange | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#111622" aria-hidden="true"></span> `#111622` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#0B0F19" aria-hidden="true"></span> `#0B0F19` |
| `--uvy-link` | Prose and action links | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#B84200" aria-hidden="true"></span> `#B84200` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FF9A4D" aria-hidden="true"></span> `#FF9A4D` |
| `--uvy-focus` | Keyboard focus ring | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#D94E00" aria-hidden="true"></span> `#D94E00` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FF8A33" aria-hidden="true"></span> `#FF8A33` |

## Semantic status tokens

Status colors communicate operational outcomes and never substitute for brand orange. Pair every status color with explicit text and a dot or icon.

| Token | Role | Light mode | Dark mode |
| --- | --- | --- | --- |
| `--uvy-ok`<br>`--uvy-ok-bg` | Passed, healthy, verified | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#166534" aria-hidden="true"></span> `#166534` / <span class="color-swatch" style="background:#E7F6EC" aria-hidden="true"></span> `#E7F6EC` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#6EE798" aria-hidden="true"></span> `#6EE798` / <span class="color-swatch" style="background:#0E2A1C" aria-hidden="true"></span> `#0E2A1C` |
| `--uvy-warn`<br>`--uvy-warn-bg` | Expiring, degraded, caution | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#854D0E" aria-hidden="true"></span> `#854D0E` / <span class="color-swatch" style="background:#FEF5D8" aria-hidden="true"></span> `#FEF5D8` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FACC55" aria-hidden="true"></span> `#FACC55` / <span class="color-swatch" style="background:#2D230B" aria-hidden="true"></span> `#2D230B` |
| `--uvy-danger`<br>`--uvy-danger-bg` | Failed, error, high severity | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#B91C1C" aria-hidden="true"></span> `#B91C1C` / <span class="color-swatch" style="background:#FDECEC" aria-hidden="true"></span> `#FDECEC` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FF8A8A" aria-hidden="true"></span> `#FF8A8A` / <span class="color-swatch" style="background:#34151B" aria-hidden="true"></span> `#34151B` |
| `--uvy-info`<br>`--uvy-info-bg` | Running, informational | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#1D4ED8" aria-hidden="true"></span> `#1D4ED8` / <span class="color-swatch" style="background:#E8F0FE" aria-hidden="true"></span> `#E8F0FE` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#7BB2FF" aria-hidden="true"></span> `#7BB2FF` / <span class="color-swatch" style="background:#102342" aria-hidden="true"></span> `#102342` |

## Domain data, spectra and charts

- **Lifecycle rows.** `--uvy-active-bg` (`#E9F6ED` / `#0F2B1D`) and `--uvy-inactive-bg` (`#FDEEEE` / `#34161D`) distinguish active and recently deactivated records without implying error or health.
- **Quantitative spectra.** `--uvy-scale-low` (`#D9F0E1` / `#143624`), `--uvy-scale-mid` (`#F7E9BC` / `#3B3012`) and `--uvy-scale-high` (`#F7D2CE` / `#471D25`) retain direction, per-column scaling, units and legends. Unknown values remain neutral (`--uvy-surface`) and distinct from zero. Never substitute brand orange for a quantitative scale.
- **Categorical charts.** Use `--uvy-chart-1` through `--uvy-chart-6` for uPlot, Chart.js and Mermaid series:

| Series | Light mode | Dark mode |
| --- | --- | --- |
| `--uvy-chart-1` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#2563EB" aria-hidden="true"></span> `#2563EB` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#60A5FA" aria-hidden="true"></span> `#60A5FA` |
| `--uvy-chart-2` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#0D9488" aria-hidden="true"></span> `#0D9488` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#2DD4BF" aria-hidden="true"></span> `#2DD4BF` |
| `--uvy-chart-3` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#CA8A04" aria-hidden="true"></span> `#CA8A04` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FACC15" aria-hidden="true"></span> `#FACC15` |
| `--uvy-chart-4` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#7C3AED" aria-hidden="true"></span> `#7C3AED` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#A78BFA" aria-hidden="true"></span> `#A78BFA` |
| `--uvy-chart-5` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#DB2777" aria-hidden="true"></span> `#DB2777` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#F472B6" aria-hidden="true"></span> `#F472B6` |
| `--uvy-chart-6` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#475569" aria-hidden="true"></span> `#475569` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#94A3B8" aria-hidden="true"></span> `#94A3B8` |

## Contrast rules

- Normal text meets **4.5:1** contrast against its actual rendered background, including text and links on lifecycle rows, status pills, alerts and spectrum cells.
- Input boundaries (`--uvy-border-input`), focus rings (`--uvy-focus`), 3px active indicators (`--uvy-accent`) and meaningful icons meet **3:1**.
- Primary signal-orange buttons and the j-hat brand tile always pair with dark `--uvy-on-accent` ink (`≥ 5.3:1` light, `≥ 7.3:1` dark), never white text.

See [light mode](../examples/light.html), [dark mode](../examples/dark.html), [lifecycle highlighting](../examples/panels.html) and [quantitative spectra](../examples/table-records.html).
