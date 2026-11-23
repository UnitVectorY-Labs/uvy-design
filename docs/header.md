# Universal header

Every UnitVectorY-Labs site shares the same crisp header anatomy: the isometric unit cube mark and monospace product title on the left, primary fixed-width navigation beside it with a bold 3px active rule, and a single sun/moon theme switch flush on the right.

## Anatomy and geometry

- **Surface and height.** `60px` (`3.75rem`) minimum desktop height, `--uvy-surface` background, `1px solid var(--uvy-border)` bottom rule, no shadow, aligned with either `.page` (`75rem`) or `.site-header--wide` (`100%`).
- **Logo mark and brand title.** The UnitVectorY-Labs mark is the transparent [isometric unit cube](logo.md) rendered at `28×28` (`1.75rem`) as an inline `.uvy-mark` SVG so its two-tone blue-slate faces adapt automatically between light and dark modes while the top face holds signal orange (`#F25C05`). **Never change the logo mark's color on hover.** Beside it sits the human-readable product title (for example, `Cert Observatory`, not a lowercase repository slug—reserve repository slugs for the footer's GitHub links) in semibold fixed-width monospace (`--uvy-font-mono`, `14–17px` responsive clamp). Applications keep their own product name and may keep their own product mark when one exists; when referencing the organization or design system in header titles, always spell out `UnitVectorY-Labs` rather than abbreviating to “UVY”.
- **Primary navigation.** Links use `13px` (`0.8125rem`) `--uvy-font-mono` spanning the full `60px` header height in `--uvy-text-muted` text, darkening to `--uvy-text` on hover. The active destination (`aria-current="page"`) displays in `--uvy-text` with a bold **`3px`** `--uvy-accent` bottom rule flush with the header border.
- **Direct theme switch.** A borderless `36px` square `.icon-button` (`44px` on coarse pointers) flush with the right edge. Show a Tabler moon in light mode and sun in dark mode, with an action-specific `aria-label` and `title` (“Switch to dark theme” / “Switch to light theme”). Do not add a separate “Use system theme” button or theme dropdown.

## Single-screen tools vs. multi-page titles

- **Multi-page sites and multi-view apps** display the site or product name in `.site-header` and use `.uvy-page-header` (`<h1>`) inside `<main>` for the distinct title of the active page, entity or view.
- **Single-screen tools and workspaces** already name the product in `.site-header`. **Do not repeat the product title in a `.uvy-page-header` directly below `.site-header`.** Instead, wrap the header `.brand` in `<h1>` inside `.header-identity` (`<h1><a class="brand" href="/">…</a></h1>`), open `<main>` directly with the primary controls or workspace so vertical space stays tight, and place any short orientation copy inside the primary panel or empty state where it guides the task.

## Mobile layout

At `768px` (`48rem`) and narrower:

- Keep the mobile menu button (when a sidebar exists) and brand identity on row 1 left, and pin the theme button to row 1 right.
- Wrap top-level navigation cleanly onto row 2 (`40px` height) with the same `3px` orange active indicator.
- The sidebar menu button uses a Tabler menu icon, `aria-label="Open navigation"`, `aria-controls="sidebar"` and accurate `aria-expanded`.

See [logo guidelines](logo.md), the [logo example](../examples/logo.html), [sidebar navigation](../examples/navigation.html), [top-bar navigation](../examples/topbar.html) and [landing page](../examples/landing.html).
