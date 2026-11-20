# Color

Use neutral surfaces and text with a restrained orange signature. Avoid large orange backgrounds, decorative heading underlines and colored panel edges.

| Semantic token | Light mode | Dark mode |
| --- | --- | --- |
| Page background | `#FAFAF8` | `#141619` |
| Surface | `#FFFFFF` | `#202327` |
| Primary text | `#22272B` | `#F2F2F0` |
| Secondary text | `#5E6671` | `#A7AFB8` |
| Border | `#D8DBDE` | `#363B41` |
| Accent | `#F97316` | `#FB923C` |
| Text link / selected text | `#9A3E00` | `#FDBA74` |
| Focus / control outline | `#9A3E00` | `#FB923C` |
| Error text / outline | `#B42318` | `#FDA29B` |
| Success text | `#21633B` | `#86D9A0` |

## Interface contrast

Use accent for fills and indicators, not general small text. Orange primary buttons use dark `#22272B` text and a contrast-appropriate outline. Links remain underlined. Selected navigation combines accessible accent-derived text, a visible indicator and `aria-current`.

Use stronger input boundaries (`#7C838B` light, `#7D8792` dark) than decorative separators. Check actual adjacent colors: normal text needs 4.5:1 contrast; large text, essential control boundaries and focus indicators need 3:1. Keep focus visible on both page and panel surfaces.

## Data and status

Brand accent, action feedback and application data have separate meanings. Red and green lifecycle tints may distinguish inactive and active records without implying error and success. Retain the application's mapping and explicit labels; exact shades may change to fit both themes.

Quantitative spectra retain their direction, scale, thresholds and units. Show numeric values and a legend; unknown or unavailable values remain distinct from zero. Use the same scale wherever values are compared. Do not replace a meaningful spectrum with brand orange.

Use semantic surface tokens for row tints and spectrum steps. Check every foreground against each tint, including links and secondary text; use primary text where needed. Never rely on color alone.

See [lifecycle highlighting](../examples/panels.html), [quantitative record highlighting](../examples/table-records.html) and [form feedback](../examples/forms.html).
