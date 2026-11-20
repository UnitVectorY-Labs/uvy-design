# Color

Use neutral surfaces and text with a restrained orange signature. Avoid large orange backgrounds, decorative heading underlines and colored card edges.

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

The supplied accent is a fill or indicator, not a general small-text color. Use dark `#22272B` text on orange primary buttons and a contrast-appropriate outline to distinguish them from white surfaces. Links use the darker light-mode color above and remain underlined. Selected navigation combines accessible accent-derived text with an underline and `aria-current`.

Neutral separators are subtle and must not be the only way to identify an input. Inputs use a stronger outline (`#7C838B` in light mode, `#7D8792` in dark mode). Focus rings remain visible against both page and surface backgrounds. Check actual combinations: normal text needs 4.5:1 contrast; large text and essential control boundaries need 3:1. Disabled controls are visibly distinct and never the only explanation of an unavailable action.

Status colors communicate status, separately from the brand accent. Pair them with concise labels and useful messages. Preserve established application data colors, scales and directions, including green–yellow–red spectra.

Explore the [component catalog](../examples/components.html) and [form states](../examples/forms.html) in both themes.
