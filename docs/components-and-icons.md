# Components and icons

Use semantic HTML with consistent base styling and a small set of namespaced variants. Each application owns its styles. The [standalone component catalog](../examples/components.html) contains inspectable CSS and HTML; no shared package or framework is required.

| Component | Default treatment |
| --- | --- |
| Buttons | 36px minimum height, 4px corners; orange primary or neutral secondary |
| Tables | Subtle header surface, horizontal dividers, no zebra striping |
| Lists | Native bullets or numbering with consistent indentation |
| Cards | Surface background, thin neutral border, 6px corners |
| Inputs | Strong neutral boundary, visible accent-derived focus ring |
| Alerts | Restrained status text and border, concise label and next step |
| Code blocks | Monospace, muted surface, thin border, local overflow |
| Navigation | Neutral text, accessible accent-derived selected text |
| Dividers | 1px neutral border |
| Links | Underlined, accessible accent-derived text; visible hover and focus |
| Badges | Compact text, subdued surface, minimal rounding |

## Actions and icons

Use one primary action per task. Links navigate; buttons perform actions. Disabled actions need an explanation. Prefer short visible labels; icon-only controls need accessible names. Use consistent Tabler outline icons when icons help, served locally or inline. Hide decorative icons from assistive technology. Preserve meaningful provider marks and data badges.

## Fields and validation

Keep labels visible and connect help/error text with `aria-describedby`. Set `aria-invalid` only after validation fails. Explain how to correct the value, focus the first invalid field after submission, and retain entered values. Use native constraints where possible and validate again on the server in real applications. Announce asynchronous success with `role="status"`; urgent errors can use `role="alert"`.

Try the [form example](../examples/forms.html) for validation, reset, selects, textareas, buttons and alerts.

## Tables and feedback

Use captions, scoped headers and visible units. Density changes spacing without removing columns or changing data. Make wide tables scroll in a keyboard-accessible region. Empty states explain the absence and a useful next action. Loading and error states belong near the affected content; identify status through words as well as color.

Try [table densities and empty results](../examples/panels.html) and the [compact utility](../examples/utility.html).
