# Icons

Use [Tabler Icons](https://tabler.io/icons) in the outline style. Inline an SVG sprite or serve local SVG files; no icon font or external CDN is required. Keep Tabler's MIT license comment inside the sprite source rather than adding attribution to the application footer.

## Sizing and stroke

Preserve the original `24 × 24` viewBox, `stroke-width="2"`, `stroke-linecap="round"`, `stroke-linejoin="round"`, `fill="none"` and `stroke="currentColor"`.

| Size | Class | Context |
| --- | --- | --- |
| `16px` (`1rem`) | `.icon-small` | Inline with 14px metadata, validation errors, compact buttons, code bar actions |
| `20px` (`1.25rem`) | `.icon` | Default interface icons: header controls, buttons, alerts |
| `24px` (`1.5rem`) | `.icon-large` | Sparse standalone section or empty-state symbol |

<div class="icon-preview"><span class="with-icon"><svg class="icon icon-small" aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-file-text"></use></svg> 16px</span><span class="with-icon"><svg class="icon" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-file-text"></use></svg> 20px</span><span class="with-icon"><svg class="icon icon-large" aria-hidden="true" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-file-text"></use></svg> 24px</span></div>

Keep the icon's rendered size separate from its clickable target: icon buttons remain `36px` square (`44px` on coarse pointers) regardless of whether the inner glyph is 16px or 20px.

## Color and restraint

Keep icons neutral by default so signal orange remains meaningful:

- **Header and chrome controls** (theme toggle, menu trigger, close button): `--uvy-text-muted`, transitioning to `--uvy-text` on `--uvy-hover`.
- **Primary buttons**: inherit `--uvy-on-accent` (`#1A1E23`).
- **Secondary and quiet buttons**: inherit button text color.
- **Status alerts and copy confirmation**: inherit the matching semantic token (`--uvy-ok`, `--uvy-warn`, `--uvy-danger`, `--uvy-info`).
- **Provider marks and badges**: preserve meaningful third-party provider logos and repository status badges rather than replacing them with generic outline icons.

Essential icons need at least **3:1** contrast against their adjacent background.

## Accessibility

- Use `<button>` for actions and `<a href>` for navigation.
- Icon-only buttons require an action-specific `aria-label` and matching `title` (for example, “Switch to dark theme” or “Copy endpoint URL”).
- Mark decorative icons and icons paired with visible text `aria-hidden="true"`.
- Never rely on an icon alone to convey an error, status or unfamiliar action.

See [icons](../examples/icons.html) and [header controls](../examples/navigation.html).
