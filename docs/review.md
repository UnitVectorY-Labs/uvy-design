# Review

Review every adapted application in **light and dark modes** at **1280px**, **375px** and **320px**, plus **200% zoom**. Compare against the original application to verify its purpose, data semantics and workflows remain intact.

## Visual restraint and craft

- Cool graphite surfaces (`#F6F7F8` / `#121418` canvas, `#FFFFFF` / `#1A1D22` surface), no warm-cream tint, no decorative gradients, and shadows limited strictly to dialogs and drawers.
- Signal orange appears only on primary actions, keyboard focus, prose links (accessible `--uvy-link`) and the 2px active indicator in header nav, sidebar and tabs. Icons, headings and footers stay neutral.
- No nested panels inside panels, no uniform SaaS card grids where a table or index list fits better, no ALL-CAPS labels or decorative eyebrows, and no arrow glyphs appended to buttons.
- IBM Plex Sans renders for UI/prose and IBM Plex Mono appears only for actual technical identifiers, timestamps and code. Tables and stat strips use `tabular-nums` with right-aligned numbers.
- Copy uses sentence case, active verbs, and direct non-apologetic error and empty states.

## Shell, navigation and themes

- Header height is `56px` desktop, with product identity left, full-height nav links with 2px active bar, and borderless theme toggle flush right on the first row at every width.
- Theme toggle switches immediately between light and dark, persists to `localStorage["uvy-theme"]`, updates its `aria-label` and `title` to the next action, syncs across tabs, and falls back gracefully when storage or JavaScript is unavailable. “Use system theme” clears the override.
- Mobile drawer (`≤ 768px`) opens from the header menu button, traps focus, sets `aria-modal="true"` and background `inert`, closes via close button, Escape, backdrop click, link activation or resize to desktop, and restores focus cleanly.
- Centered footer shows `UnitVectorY-Labs | actual license | named GitHub repository link(s)` in quiet muted text, with optional monospace version line omitted completely from HTML when disabled.

## Contrast, data and accessibility

- Normal text meets **4.5:1** contrast on every surface, including tinted lifecycle rows, status pills, alerts and quantitative spectrum cells. Input borders, focus rings, 2px active rules and essential icons meet **3:1**. Primary buttons use `#1A1E23` dark ink.
- Status pills combine dot + explicit label; lifecycle states remain distinct from error/success verdicts; quantitative spectra keep direction, per-column normalization, units, legend and distinct unknown values.
- Charts and diagrams use `--uvy-chart-1..6` and update cleanly when the theme switches.
- Forms keep visible labels, `aria-describedby` hints/errors, `aria-invalid="true"` on failure, focus on first invalid field and `role="status"` / `role="alert"` announcements.
- Comparison tables scroll inside keyboard-focusable `.table-wrap` regions; mobile record tables reflow cleanly with all values and links preserved.
- Long identifiers and URLs wrap cleanly with zero page-level horizontal overflow at 320px and 200% zoom, and `prefers-reduced-motion: reduce` disables transitions and spinner rotation.

Automated checks (`scripts/check_site.py`, `scripts/check_browser.py`) supplement hands-on visual inspection; always inspect rendered pages in both themes before shipping.
