# Typography and spacing

Use the following shared defaults when building an interface. Values are in `rem` so they respect the reader's browser font size. Adapt dense data displays where needed, but keep the hierarchy and target sizes recognizable.

```css
:root {
  --font-sans: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Consolas, monospace;
  --text-small: 0.875rem; /* 14px at the default browser size */
  --text-body: 1rem;
  --text-large: 1.25rem;
  --text-section: 1.5rem;
  --text-title: 2rem;
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --radius: 0.375rem;
  --content-width: 75rem;
}
body { font-family: var(--font-sans); font-size: var(--text-body); line-height: 1.5; }
code, pre, .technical-value { font-family: var(--font-mono); }
```

Use `--text-small` for supporting labels, `--text-body` for ordinary content, `--text-large` for prominent supporting text, `--text-section` for section headings and `--text-title` for the application title. Use weight 600 for headings and controls, and 400 for body text. Headings should have a line height around 1.2; avoid fixed heights that clip wrapped text. Make page and section titles blue with a restrained orange underline. In a blue application header, use a white title with the orange underline as shown in the [header reference](header.md). Align headings left on mobile.

Use 0.25–0.5rem between closely related label and value, 0.75–1rem between controls, 1rem between cards, and 2rem between sections. Start with 1rem card padding and 0.75rem by 1rem button padding. Use a centered content area with a maximum width of 75rem and 1rem side gutters; increase the gutters to 2rem on wider screens. Keep interactive targets at least 44 by 44 CSS pixels where practical, including icon-only actions.

```css
.page { width: min(100% - 2rem, var(--content-width)); margin-inline: auto; }
.stack > * + * { margin-block-start: var(--space-4); }
.section + .section { margin-block-start: var(--space-8); }
@media (min-width: 48rem) {
  .page { width: min(100% - 4rem, var(--content-width)); }
}
```

Allow long titles and technical values to wrap or scroll within their own region without causing page-wide horizontal overflow. Dense reference tables can be compact; forms and workspaces can have more room. Preserve useful existing responsive patterns: for example, Unreleased Commits retains its repository title and release followed by three side-by-side metric cells. Use the structure suited to each application's content.
