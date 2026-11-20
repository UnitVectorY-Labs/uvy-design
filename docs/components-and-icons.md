# Components and icons

Use semantic HTML and a small set of namespaced variants. Each application owns its styles; the [component catalog](../examples/components.html) provides inspectable, standalone patterns.

| Component | Default treatment |
| --- | --- |
| Buttons | 36px minimum height, 4px corners; orange primary or neutral secondary |
| Tables | Subtle header surface, horizontal dividers, no decorative zebra striping |
| Lists | Native bullets or numbering, consistent indentation |
| Panels | Surface background, thin neutral border, 6px corners |
| Inputs | Strong neutral boundary, visible accent-derived focus ring |
| Alerts | Restrained status color, concise label and next step |
| Code blocks | Monospace, muted surface, thin border, local overflow |
| Links | Underlined, accessible accent-derived text; visible hover and focus |
| Badges | Compact text, subdued surface, minimal rounding |

## Actions and icons

Use one primary action per task. Links navigate; buttons perform actions. Explain unavailable actions. Use **Tabler Icons** outline icons, normally 20px with a 2-unit stroke in their 24px view box, served locally or inline. Give icon-only controls accessible names and hide decorative icons from assistive technology. Preserve meaningful provider marks and data badges.

## Panels and summaries

Group related information under a clear heading. Place compact label/value summaries above their related tables; keep technical identifiers monospace and allow long values to wrap. Keep evidence, its source and qualifying notes together. Start with 24px panel padding and stacked-panel gaps; compact grids use 16px gaps. Reduce panel padding to 16px on mobile.

See [detail panels and lifecycle tables](../examples/panels.html).

## Fields and validation

Keep labels visible; connect help and errors with `aria-describedby`. Set `aria-invalid` after validation fails, explain the correction, focus the first invalid field on submission and retain entered values. Use native constraints where possible; real applications also validate on the server. Announce asynchronous success with `role="status"` and urgent errors with `role="alert"`.

See the [working form](../examples/forms.html).

## Tables and feedback

Use captions, scoped headers and visible units. Density changes spacing without removing data. Lifecycle row tints retain the application's meaning: active/inactive is distinct from success/error. Pair color with section headings or explicit status text.

On mobile, records may reflow into labeled cards when every value and action retains its context. Keep comparison tables tabular; contain unavoidable horizontal scrolling in a named, keyboard-accessible region. Do not hide columns to make a table fit. Empty states explain the absence and a next action; loading and errors stay near the affected content.

See [comparison tables](../examples/panels.html) and the [long record table](../examples/table-records.html).
