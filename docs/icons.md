# Icons

Use [Tabler Icons](https://tabler.io/icons), outline style. Inline the SVGs or serve them locally; no icon font or JavaScript framework is required. Keep the upstream MIT license notice with copied assets or embedded SVG source, rather than adding attribution to the application footer.

## Size and color

Use the original 24 × 24 view box, a 2-unit stroke and `currentColor`. Render ordinary interface icons at 20px; use 16px beside small metadata or 24px for a standalone section symbol. The icon's size is separate from its button's 36px target, increasing to 44px for coarse pointers.

| Context | Treatment |
| --- | --- |
| Theme and navigation controls | Accessible accent-derived color; visible focus; sun/moon changes with the next action |
| Primary action | Inherit the button's contrast-safe foreground, including dark text on orange |
| Secondary action or metadata | Inherit neutral text or secondary text; avoid decorative orange on every icon |
| Status | Use the matching semantic status color and an explicit text label |
| Heading or summary | Optional, sparse; align with the text baseline without replacing the heading |

<div class="icon-preview"><span class="with-icon"><svg class="icon icon-small" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-file-text"></use></svg> 16px</span><span class="with-icon"><svg class="icon " aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-file-text"></use></svg> 20px</span><span class="with-icon"><svg class="icon icon-large" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><use href="#tabler-file-text"></use></svg> 24px</span></div>

Essential icons need 3:1 contrast against adjacent surfaces. Keep shape, size and stroke consistent within a row. Preserve provider logos and meaningful data symbols rather than replacing them with generic icons.

## Behavior and labeling

Use a button for an action and a link for a destination. Icon-only controls need an accessible name and a helpful title; name the action, such as “Switch to dark theme.” Hide decorative SVGs with `aria-hidden="true"`. When text labels the control, the accompanying icon is decorative. Do not use icons alone to explain errors, status or unfamiliar actions.

See the [working icon scenarios](../examples/icons.html) and the [header controls](../examples/navigation.html).
