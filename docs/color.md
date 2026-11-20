# Color

Use neutral surfaces and text with a restrained orange signature. Avoid large orange backgrounds, decorative heading underlines and colored panel edges.

| Semantic token | Light mode | Dark mode |
| --- | --- | --- |
| Page background | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#FAFAF8" aria-hidden="true"></span> `#FAFAF8` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#141619" aria-hidden="true"></span> `#141619` |
| Surface | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#FFFFFF" aria-hidden="true"></span> `#FFFFFF` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#202327" aria-hidden="true"></span> `#202327` |
| Primary text | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#22272B" aria-hidden="true"></span> `#22272B` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#F2F2F0" aria-hidden="true"></span> `#F2F2F0` |
| Secondary text | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#5E6671" aria-hidden="true"></span> `#5E6671` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#A7AFB8" aria-hidden="true"></span> `#A7AFB8` |
| Border | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#D8DBDE" aria-hidden="true"></span> `#D8DBDE` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#363B41" aria-hidden="true"></span> `#363B41` |
| Accent | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#F97316" aria-hidden="true"></span> `#F97316` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FB923C" aria-hidden="true"></span> `#FB923C` |
| Text link / selected text | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#9A3E00" aria-hidden="true"></span> `#9A3E00` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FDBA74" aria-hidden="true"></span> `#FDBA74` |
| Focus / control outline | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#9A3E00" aria-hidden="true"></span> `#9A3E00` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FB923C" aria-hidden="true"></span> `#FB923C` |
| Error text / outline | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#B42318" aria-hidden="true"></span> `#B42318` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#FDA29B" aria-hidden="true"></span> `#FDA29B` |
| Success text | <span class="palette-label" aria-hidden="true">Light</span> <span class="color-swatch" style="background:#21633B" aria-hidden="true"></span> `#21633B` | <span class="palette-label" aria-hidden="true">Dark</span> <span class="color-swatch" style="background:#86D9A0" aria-hidden="true"></span> `#86D9A0` |

## Interface contrast

Use accent for fills and indicators, not general small text. Orange primary buttons use dark <span class="color-swatch" style="background:#22272B" aria-hidden="true"></span> `#22272B` text and a contrast-appropriate outline. Links remain underlined. Selected navigation combines accessible accent-derived text, a visible indicator and `aria-current`.

Use stronger input boundaries (<span class="color-swatch" style="background:#7C838B" aria-hidden="true"></span> `#7C838B` light, <span class="color-swatch" style="background:#7D8792" aria-hidden="true"></span> `#7D8792` dark) than decorative separators. Check actual adjacent colors: normal text needs 4.5:1 contrast; large text, essential control boundaries and focus indicators need 3:1. Keep focus visible on both page and panel surfaces.

## Data and status

Brand accent, action feedback and application data have separate meanings. Red and green lifecycle tints may distinguish inactive and active records without implying error and success. Retain the application's mapping and explicit labels; exact shades may change to fit both themes.

Quantitative spectra retain their direction, scale, thresholds and units. Show numeric values and a legend; unknown or unavailable values remain distinct from zero. Use the same scale wherever values are compared. Do not replace a meaningful spectrum with brand orange.

Use semantic surface tokens for row tints and spectrum steps. Check every foreground against each tint, including links and secondary text; use primary text where needed. Never rely on color alone.

See [lifecycle highlighting](../examples/panels.html), [quantitative record highlighting](../examples/table-records.html) and [form feedback](../examples/forms.html).
