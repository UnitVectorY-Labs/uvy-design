# Universal header

Every Unit Vector Y Labs site shares the same quiet header anatomy: product identity on the left, primary navigation beside it, and the theme switch flush on the far right.

## Anatomy and geometry

- **Surface and rule.** `56px` (`3.5rem`) minimum desktop height, `--uvy-surface` background, `1px solid var(--uvy-border)` bottom divider, no shadow, aligned to the same `75rem` page gutters as main content.
- **Brand identity.** Lead with the application's own product name (and optional mark). UnitVectorY-Labs properties may use the 24×24 geometric vector mark (`uvy-mark`) showing an orange unit vector rising from its origin dot on an ink tile. Keep long product names readable and allowed to wrap.
- **Primary navigation.** Links span the full `56px` header height in quiet `--uvy-text-muted` text, darkening to `--uvy-text` on hover. The active destination (`aria-current="page"`) renders in `--uvy-text` with a flush `2px` `--uvy-accent` bottom rule sitting directly on the header divider.
- **Theme switch.** A borderless `36px` square `.icon-button` (`44px` on coarse pointers) flush with the right gutter. Display a Tabler moon in light mode and sun in dark mode, using neutral `--uvy-text-muted` ink that brightens on `--uvy-hover`. Name the next action in both `aria-label` and `title` (for example, “Switch to dark theme”).
- **System theme reset.** Offer “Use system theme” as a quiet secondary button in the sidebar footer, or beside header navigation when no sidebar exists, shown only while a manual override is active. Never replace the direct toggle with a dropdown.

## Mobile layout

At `768px` (`48rem`) and narrower:

- Keep the mobile menu trigger (when a sidebar exists) and product identity on the first row left, and keep the theme switch pinned at the top-right corner of the first row.
- Wrap header navigation onto a second full-width row (`40px` height) with the same 2px active indicator.
- The sidebar trigger uses a Tabler menu icon, an explicit accessible name (“Open navigation”), `aria-controls="sidebar"` and accurate `aria-expanded`.

See [header and sidebar](../examples/navigation.html), [static article](../examples/documentation.html) and [landing page](../examples/landing.html).
