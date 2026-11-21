# Color

Use cool technical graphite surfaces and dark charcoal ink with a calibrated signal-orange accent. Avoid large orange backgrounds, colored panel edges, decorative heading underlines and warm cream tints.

## Core semantic tokens

Define colors with `color-scheme: light dark` and `light-dark()` so both themes share one token block.

| Token | Role | Light mode | Dark mode |
| --- | --- | --- | --- |
| `--uvy-bg` | Page canvas | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#F6F7F8" aria-hidden="true"></span> `#F6F7F8` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#121418" aria-hidden="true"></span> `#121418` |
| `--uvy-surface` | Panels, header, inputs | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#FFFFFF" aria-hidden="true"></span> `#FFFFFF` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#1A1D22" aria-hidden="true"></span> `#1A1D22` |
| `--uvy-sunken` | Code wells, inline code | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#F0F2F4" aria-hidden="true"></span> `#F0F2F4` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#0E1013" aria-hidden="true"></span> `#0E1013` |
| `--uvy-hover` | Subtle interactive fill | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#ECEEF1" aria-hidden="true"></span> `#ECEEF1` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#23272D" aria-hidden="true"></span> `#23272D` |
| `--uvy-border` | Hairline dividers, panels | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#DFE2E6" aria-hidden="true"></span> `#DFE2E6` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#2C3138" aria-hidden="true"></span> `#2C3138` |
| `--uvy-border-emphasis` | Table header rules, secondary buttons | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#C9CED5" aria-hidden="true"></span> `#C9CED5` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#3D434B" aria-hidden="true"></span> `#3D434B` |
| `--uvy-border-input` | Essential input boundaries (≥ 3:1) | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#858C95" aria-hidden="true"></span> `#858C95` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#6C7580" aria-hidden="true"></span> `#6C7580` |
| `--uvy-text` | Primary text and headings | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#1A1E23" aria-hidden="true"></span> `#1A1E23` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#ECEEF1" aria-hidden="true"></span> `#ECEEF1` |
| `--uvy-text-muted` | Secondary text, labels, metadata | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#59616B" aria-hidden="true"></span> `#59616B` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#9AA3AE" aria-hidden="true"></span> `#9AA3AE` |
| `--uvy-text-faint` | Placeholders, version footers | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#7D858F" aria-hidden="true"></span> `#7D858F` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#78818C" aria-hidden="true"></span> `#78818C` |
| `--uvy-accent` | Primary button fill, active 2px bar | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#EE6418" aria-hidden="true"></span> `#EE6418` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FF8A3D" aria-hidden="true"></span> `#FF8A3D` |
| `--uvy-accent-hover` | Primary button hover | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#E25C14" aria-hidden="true"></span> `#E25C14` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FF9D5C" aria-hidden="true"></span> `#FF9D5C` |
| `--uvy-on-accent` | Text on primary orange fill | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#1A1E23" aria-hidden="true"></span> `#1A1E23` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#1A1E23" aria-hidden="true"></span> `#1A1E23` |
| `--uvy-link` | Prose and action links | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#A8430A" aria-hidden="true"></span> `#A8430A` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FFB07A" aria-hidden="true"></span> `#FFB07A` |
| `--uvy-focus` | Keyboard focus ring | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#C24E0C" aria-hidden="true"></span> `#C24E0C` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FF9A55" aria-hidden="true"></span> `#FF9A55` |

## Feedback status tokens

Status colors communicate operational feedback and never substitute for brand orange. Pair every status tint with explicit text and a dot or icon.

| Token | Role | Light mode | Dark mode |
| --- | --- | --- | --- |
| `--uvy-ok` / `--uvy-ok-bg` | Success, healthy, passed | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#1F6B3D" aria-hidden="true"></span> `#1F6B3D` / <span class="color-swatch" style="background:#E6F4EA" aria-hidden="true"></span> `#E6F4EA` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#7FD69B" aria-hidden="true"></span> `#7FD69B` / <span class="color-swatch" style="background:#14301F" aria-hidden="true"></span> `#14301F` |
| `--uvy-warn` / `--uvy-warn-bg` | Warning, degraded, expiring | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#7F5300" aria-hidden="true"></span> `#7F5300` / <span class="color-swatch" style="background:#FBF1D9" aria-hidden="true"></span> `#FBF1D9` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#EDC167" aria-hidden="true"></span> `#EDC167` / <span class="color-swatch" style="background:#352A12" aria-hidden="true"></span> `#352A12` |
| `--uvy-danger` / `--uvy-danger-bg` | Error, failed, high severity | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#B42318" aria-hidden="true"></span> `#B42318` / <span class="color-swatch" style="background:#FCEBEA" aria-hidden="true"></span> `#FCEBEA` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FF9C94" aria-hidden="true"></span> `#FF9C94` / <span class="color-swatch" style="background:#3B1E20" aria-hidden="true"></span> `#3B1E20` |
| `--uvy-info` / `--uvy-info-bg` | Running, informational | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#1E5AA8" aria-hidden="true"></span> `#1E5AA8` / <span class="color-swatch" style="background:#E8F0FB" aria-hidden="true"></span> `#E8F0FB` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#8CB8F0" aria-hidden="true"></span> `#8CB8F0` / <span class="color-swatch" style="background:#16253A" aria-hidden="true"></span> `#16253A` |

## Application data, spectra and charts

Brand accent, operational feedback and domain data stay semantically distinct:

- **Lifecycle states.** Green (`--uvy-active-bg` `#E9F5EC` / `#16301F`) and red (`--uvy-inactive-bg` `#FCEDEC` / `#3A1F21`) row tints may distinguish active and inactive records (such as observed signing keys) without implying health or error. Retain explicit labels.
- **Quantitative spectra.** Use `--uvy-scale-low` (`#DCEFE2` / `#1F3F2A`), `--uvy-scale-mid` (`#F6E8BF` / `#43381A`) and `--uvy-scale-high` (`#F6D4D0` / `#4B2629`) or continuous blends between them. Keep direction, per-column normalization, thresholds and units intact. Unknown or unavailable values stay neutral (`--uvy-surface`) and distinct from zero. Never replace a quantitative scale with brand orange.
- **Categorical charts.** Use `--uvy-chart-1` through `--uvy-chart-6` for multi-series plots (uPlot, Chart.js, Mermaid) so series remain legible and distinct from brand orange:

| Series | Light mode | Dark mode |
| --- | --- | --- |
| `--uvy-chart-1` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#2F6FBA" aria-hidden="true"></span> `#2F6FBA` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#6FA3E8" aria-hidden="true"></span> `#6FA3E8` |
| `--uvy-chart-2` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#1F8A84" aria-hidden="true"></span> `#1F8A84` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#4CC2B9" aria-hidden="true"></span> `#4CC2B9` |
| `--uvy-chart-3` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#B07A06" aria-hidden="true"></span> `#B07A06` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#E6B04A" aria-hidden="true"></span> `#E6B04A` |
| `--uvy-chart-4` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#7A5BC7" aria-hidden="true"></span> `#7A5BC7` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#A58BEA" aria-hidden="true"></span> `#A58BEA` |
| `--uvy-chart-5` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#C44E73" aria-hidden="true"></span> `#C44E73` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#E57FA0" aria-hidden="true"></span> `#E57FA0` |
| `--uvy-chart-6` | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#5B6573" aria-hidden="true"></span> `#5B6573` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#9AA3AE" aria-hidden="true"></span> `#9AA3AE` |

## Interface contrast

- Normal text requires **4.5:1** contrast against its actual rendered background, including links and secondary text on tinted rows or spectrum cells.
- Large text, essential input boundaries (`--uvy-border-input`), focus rings (`--uvy-focus`), active 2px indicators (`--uvy-accent`) and meaningful icons require **3:1**.
- Primary orange buttons always use dark `--uvy-on-accent` (`#1A1E23`) ink (≥ 5.1:1 in light mode, ≥ 7.1:1 in dark mode), never white text.
- Prose links use `--uvy-link` with a subtle 1px underline that strengthens to full opacity on hover.

See [light mode](../examples/light.html), [dark mode](../examples/dark.html), [lifecycle highlighting](../examples/panels.html) and [quantitative spectra](../examples/table-records.html).
