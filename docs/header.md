# Universal header

Every UnitVectorY-Labs site shares the same crisp header anatomy: the isometric unit cube mark and monospace product title on the left, primary fixed-width navigation beside it with a bold 3px active rule, and a single sun/moon theme switch flush on the right.

## Anatomy and geometry

- **Surface and height.** `60px` (`3.75rem`) minimum desktop height, `--uvy-surface` background, `1px solid var(--uvy-border)` bottom rule, no shadow, aligned with either `.page` (`75rem`) or `.site-header--wide` (`100%`).
- **Reveal on scroll up (not permanently frozen).** With `site/uvy.js`, `.site-header` scrolls naturally out of the way when moving down a long page (`.is-hidden`) and glides immediately back into view when the user scrolls up anywhere on the page, returns near the top, opens the mobile drawer, or moves keyboard focus into the header (`:focus-within`). Without JavaScript, on very short viewports (`max-height: 28rem`), or when printing, it remains a standard static top bar.
- **Logo mark and brand title.** The UnitVectorY-Labs mark is the transparent [isometric unit cube](logo.md) rendered at `28×28` (`1.75rem`) as an inline `.uvy-mark` SVG so its two-tone blue-slate faces adapt automatically between light and dark modes while the top face holds signal orange (`#F25C05`). **Never change the logo mark's color on hover.** Beside it sits the product title in semibold fixed-width monospace (`--uvy-font-mono`, `14–17px` responsive clamp). Applications keep their own product name and may keep their own product mark when one exists; when referencing the organization or design system in header titles, always spell out `UnitVectorY-Labs` rather than abbreviating to “UVY”.
- **Primary navigation (only when needed).** Use `<nav aria-label="Main navigation">` only when an application has genuinely distinct top-level sections (such as `Guide` and `Examples`, or top-bar app views). Links use `13px` (`0.8125rem`) `--uvy-font-mono` spanning the full `60px` header height in `--uvy-text-muted` text, darkening to `--uvy-text` on hover, with a bold **`3px`** `--uvy-accent` bottom rule on `aria-current="page"`. **Omit top-bar `<nav>` tabs on single-section documentation sites and sidebar-driven apps** — do not invent redundant tabs such as `Docs` or `GitHub` just to fill the header.
- **Right-side utility icons and theme switch (`.header-actions`).** Keep the borderless `36px` square `#theme` `.icon-button` (`44px` on coarse pointers) flush with the right edge (Tabler moon in light mode, sun in dark mode, with action-specific `aria-label` and `title`; never add a “Use system theme” button or dropdown). When a repository or utility link belongs in the header without warranting a navigation tab—such as linking to the project's GitHub repository on a documentation site—wrap it with `#theme` inside `.header-actions` as a matching borderless Tabler outline `<a class="icon-button">` (`brand-github`) placed immediately to the **left** of the theme switch.

## Mobile layout

At `768px` (`48rem`) and narrower:

- Keep the mobile menu button (when a sidebar exists) and brand identity on row 1 left, and pin `.header-actions` (including `#theme`) to row 1 right.
- Wrap top-level `<nav>` links cleanly onto row 2 (`40px` height) with the same `3px` orange active indicator; when a documentation site omits `<nav>`, the mobile header stays a single crisp row.
- The sidebar menu button uses a Tabler menu icon, `aria-label="Open navigation"`, `aria-controls="sidebar"` and accurate `aria-expanded`.

See [logo guidelines](logo.md), the [logo example](../examples/logo.html), [sidebar navigation](../examples/navigation.html), [top-bar navigation](../examples/topbar.html) and [landing page](../examples/landing.html).
