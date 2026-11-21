# Icons

Use **[Tabler Icons](https://tabler.io/icons)** in the outline style. **Any outline icon from the full Tabler Icons library is allowed** — the compact sprite in `site/icons.inc` is only a starter subset for this guide. Copy only the Tabler SVG symbols an application actually uses and keep Tabler's MIT license comment alongside the SVG source (note that Go `html/template` strips HTML comments at render time, so keeping the notice in the source template or static asset file is sufficient) rather than in the application footer. For multi-thousand-row indexes, prefer lightweight CSS semantic dots over repeating thousands of `<svg><use>` instances.

## Sizing and stroke

Preserve Tabler's original `24 × 24` viewBox, `stroke-width="2"`, `stroke-linecap="round"`, `stroke-linejoin="round"`, `fill="none"` and `stroke="currentColor"`.

| Size | Class | Context |
| --- | --- | --- |
| `16px` (`1rem`) | `.icon-small` | Inline with 14px metadata, validation errors, compact buttons, code bar actions |
| `20px` (`1.25rem`) | `.icon` | Default interface icons: header controls, buttons, alerts |
| `24px` (`1.5rem`) | `.icon-large` | Sparse standalone section or empty-state symbol |

<div class="uvy-specimen icon-preview"><span class="with-icon"><svg class="icon icon-small" aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-file-text"></use></svg> 16px</span><span class="with-icon"><svg class="icon" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-file-text"></use></svg> 20px</span><span class="with-icon"><svg class="icon icon-large" aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-file-text"></use></svg> 24px</span></div>

Keep an icon's visual size separate from its button hit area: icon-only buttons stay `36px` square (`44px` on coarse pointers).

## Using icons in different colors

Icons inherit `currentColor` by default so they follow surrounding text automatically. When an icon communicates meaning — status, emphasis or category — pair it with one of the semantic color classes in `site/uvy.css` (all calibrated for ≥ 3:1 contrast in both light and dark modes):

| Class | Token | When to use |
| --- | --- | --- |
| *(default)* | `currentColor` (`--uvy-text`) | Standard buttons, navigation links, primary actions (dark ink on orange) |
| `.icon-muted` | `--uvy-text-muted` | Quiet chrome (theme toggle, menu button), metadata, secondary hints |
| `.icon-accent` | `--uvy-accent` | Highlighted terminal cues, active feature callouts, selected indicators |
| `.icon-ok` | `--uvy-ok` | Passed checks, verified signatures, copy confirmation |
| `.icon-warn` | `--uvy-warn` | Expiring certificates, degraded services, cautions |
| `.icon-danger` | `--uvy-danger` | Failed checks, invalid fields, critical alerts |
| `.icon-info` | `--uvy-info` | Running jobs, informational notices, scheduled metadata |

<div class="uvy-specimen icon-preview"><span class="with-icon"><svg class="icon" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-terminal-2"></use></svg> Default</span><span class="with-icon"><svg class="icon icon-muted" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-search"></use></svg> Muted</span><span class="with-icon"><svg class="icon icon-accent" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-key"></use></svg> Accent</span><span class="with-icon"><svg class="icon icon-ok" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-shield-check"></use></svg> Ok</span><span class="with-icon"><svg class="icon icon-warn" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-alert-triangle"></use></svg> Warn</span><span class="with-icon"><svg class="icon icon-danger" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-alert-circle"></use></svg> Danger</span><span class="with-icon"><svg class="icon icon-info" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-info-circle"></use></svg> Info</span></div>

Preserve third-party provider logos and repository status badges rather than replacing them with generic icons.

## Accessibility

- Use `<button>` for actions and `<a href>` for destinations.
- Icon-only buttons need an action-specific `aria-label` and matching `title` (such as “Switch to dark theme” or “Copy endpoint URL”).
- Mark decorative icons and icons paired with visible text `aria-hidden="true"`. Never rely on an icon or color alone to explain an error or status.

See the [icons example](../examples/icons.html) for interactive colored icon scenarios.
