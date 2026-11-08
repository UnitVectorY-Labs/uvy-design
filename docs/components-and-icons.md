# Components and icons

Use native HTML and a small set of consistent controls. The examples below are starting points to copy into an application and adapt to its content and workflows, not a required package. They share the CSS in the first example. Measurements use `rem` so they scale with the browser's default font size. See [typography and spacing](typography-and-spacing.md) for the wider layout scale and [color](color.md) for color roles.

## Shared styles

This example provides light and dark surfaces, visible focus, and wrapping for narrow screens. An application can set `data-theme="light"` or `data-theme="dark"` on its root element for an explicit choice; without one, the operating system preference applies. See [themes and navigation](themes-and-navigation.md) for persistence and toggle behavior.

```css
:root, :root[data-theme="light"] {
  color-scheme: light;
  --page: #f3f6fc;
  --surface: #fff;
  --text: #182b49;
  --muted: #50617c;
  --border: #cfdaeb;
  --blue: #1558ba;
  --orange: #a83e00;
  --orange-fill: #ff932e;
  --focus: #1558ba;
}
:root[data-theme="dark"] {
  color-scheme: dark;
  --page: #0c1729;
  --surface: #14243c;
  --text: #edf3ff;
  --muted: #b2c2da;
  --border: #354b6b;
  --blue: #8dbbff;
  --orange: #ffb16d;
  --orange-fill: #ff932e;
  --focus: #8dbbff;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) {
    color-scheme: dark;
    --page: #0c1729;
    --surface: #14243c;
    --text: #edf3ff;
    --muted: #b2c2da;
    --border: #354b6b;
    --blue: #8dbbff;
    --orange: #ffb16d;
    --orange-fill: #ff932e;
    --focus: #8dbbff;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--page);
  color: var(--text);
  font: 1rem/1.5 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
a { color: var(--blue); }
:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; }
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  min-height: 2.75rem;
  padding: .5rem 1rem;
  border: 1px solid var(--border);
  border-radius: .375rem;
  background: var(--surface);
  color: var(--text);
  font: inherit;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
}
.button:hover { border-color: var(--blue); }
.button:disabled { opacity: .6; cursor: not-allowed; }
.button--primary { background: var(--orange-fill); border-color: #a83e00; color: #182b49; }
.button--primary:hover { background: #ffad62; border-color: #873200; }
.button--icon { width: 2.75rem; padding: .5rem; color: var(--orange); }
.button svg { width: 1.25rem; height: 1.25rem; flex: none; }
.actions { display: flex; flex-wrap: wrap; gap: .5rem; }
.panel {
  padding: 1.25rem;
  border: 1px solid var(--border);
  border-radius: .5rem;
  background: var(--surface);
  box-shadow: 0 1px 3px rgb(0 0 0 / 8%);
}
.panel > :first-child { margin-top: 0; }
.panel > :last-child { margin-bottom: 0; }
.field { display: grid; gap: .375rem; }
.field label { font-weight: 600; }
.field input, .field select, .field textarea {
  width: 100%;
  min-height: 2.75rem;
  padding: .5rem .75rem;
  border: 1px solid var(--border);
  border-radius: .375rem;
  background: var(--surface);
  color: var(--text);
  font: inherit;
}
.hint { margin: 0; color: var(--muted); font-size: .875rem; }
.error { margin: 0; color: var(--text); font-size: .875rem; font-weight: 600; }
.field [aria-invalid="true"] { border: 2px solid var(--orange); }
.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; text-align: left; }
th, td { padding: .625rem .75rem; border-bottom: 1px solid var(--border); vertical-align: top; }
th { font-size: .875rem; }
.status { font-weight: 600; }
code { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; overflow-wrap: anywhere; }
```

## Actions and icons

Use one clear primary action per task. Use a button for an action and a link for navigation. The orange-filled primary button works with or without an icon; icon-only primary actions can use the orange icon treatment. Give every icon-only control an accessible name. Hide decorative icons from assistive technology.

```html
<div class="actions">
  <button class="button button--primary" type="submit" form="search-form">Search</button>
  <a class="button" href="/help">Search help</a>
  <button class="button button--icon" type="button" aria-label="Copy result">
    <svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="8" y="8" width="11" height="11" rx="2"></rect>
      <path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"></path>
    </svg>
  </button>
</div>
<p class="hint" role="status" aria-live="polite" id="copy-status"></p>
```

Connect the copy button to the application's copy behavior and update the status with “Copied” or a useful failure message. Use [Tabler Icons](https://tabler.io/icons) as the common icon family, with consistent outline size and stroke. Serve icons locally or inline them; keep meaningful data, provider marks and badges intact.

## Fields and validation

Labels remain visible after entry. Associate help and error messages with the input, set `aria-invalid` only when validation has failed, and explain how to correct the error. This example shows the error state; omit the error element and `aria-invalid` before validation.

```html
<form id="search-form" action="/search" method="get">
  <div class="field">
    <label for="domain">Domain</label>
    <input id="domain" name="domain" type="text" required
           value="example" aria-invalid="true" aria-describedby="domain-help domain-error">
    <p class="hint" id="domain-help">Enter a fully qualified domain name.</p>
    <p class="error" id="domain-error">Enter a domain such as example.com.</p>
  </div>
</form>
```

Use the same field styling for selects and textareas. Do not rely on placeholder text as a label. Put form actions near their fields in the actual layout and preserve normal keyboard submission.

## Panels, tables and feedback

Panels group related content with a neutral border and no colored line along the top or left. Keep ordinary content visible instead of adding tabs or disclosures for appearance alone. Tables can scroll within their own region on small screens without hiding columns.

```html
<section class="panel" aria-labelledby="results-title">
  <h2 id="results-title">Results</h2>
  <p class="hint">Most recent check for each domain.</p>
  <div class="table-wrap" tabindex="0" role="region" aria-label="Results table">
    <table>
      <thead><tr><th scope="col">Domain</th><th scope="col">Status</th></tr></thead>
      <tbody><tr><td><code>example.com</code></td><td><span class="status">Available</span></td></tr></tbody>
    </table>
  </div>
</section>
```

Provide useful loading, empty, error and success states in the content area. For example, use “No results. Try another domain” for an empty search and “Could not load results. Try again” with a retry action for a failure. Announce asynchronous updates with a `role="status"` region; use `role="alert"` for errors needing immediate attention. Identify status in text or with another non-color cue, not color alone. Preserve the meaning of application-specific data colors.
