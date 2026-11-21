# Foundations

UnitVectorY-Labs builds software for engineers inspecting infrastructure, certificates, signing keys, policies and repositories. Interfaces combine the clarity of technical documentation with fixed-width retro-terminal precision: cool light surfaces, deep midnight blue-slate dark mode, crisp hairlines, an always-visible compact footer and a bold 3px signal-orange accent rule.

## Core principles

- **Flat surfaces, deep contrast.** Light mode uses crisp cool paper (`#F5F7FA` canvas, `#FFFFFF` panels); dark mode uses a deep midnight blue-slate (`#090D16` canvas, `#111827` panels) whose cool blue undertone naturally complements bright signal orange. Omit decorative gradients and ambient shadows; reserve shadows strictly for overlays such as dialogs and drawers.
- **One unmistakable orange signature.** Bright signal orange (`#F25C05` light / `#FF7A1A` dark) crowns the top face of the [isometric unit cube mark](logo.md) (`#F25C05`), primary actions, keyboard focus, and a bold `3px` active rule on header navigation, sidebars, tabs, callouts and terminal output wells.
- **Retro-terminal chrome, readable prose.** Pair fixed-width `ui-monospace` across structural surfaces—page headings (`H1`–`H4`), header brand titles, navigation links, tabs, buttons, form labels, datasheet keys, table headers, directory titles, stat figures, badges, timestamps, technical inputs and code/output wells—with universally supported `system-ui` sans-serif for paragraphs, lead text, hints and narrative explanations. Never set long prose paragraphs in monospace, and never bury monospace only in tiny footnotes.
- **Structure encodes meaning.** Group related controls and tables in flat `.uvy-panel` containers without nesting panels inside panels. Avoid uniform SaaS card grids where a hairline directory or table scans faster. Avoid tracked-out ALL-CAPS eyebrows and trailing arrows on buttons.
- **Always-visible compact footer.** Pin a slim, calm `.site-footer` to the bottom of the viewport (`position: sticky; bottom: 0`) so project attribution, license, repository links and optional metadata (`Last updated` or `Version`) remain in view without pushing off the bottom of tall pages or crowding the workspace.
- **Purposeful motion.** Transitions answer direct interaction (120ms hover/focus, 180ms drawer slide) and stop cleanly under `prefers-reduced-motion`. Never recolor or animate the logo mark on hover.
- **Direct writing.** Write in sentence case and active voice (“Check domain”, “Save changes”, not “Submit”). Errors explain what failed and how to recover without apologizing. Empty states state what is absent and provide the next action.

## Brand naming

- **Always spell out `UnitVectorY-Labs`.** Never abbreviate `UnitVectorY-Labs` to “UVY” in page `<title>` elements, header brand titles, headings, links, documentation prose or user-facing references. Write **UnitVectorY-Labs Design Guide** and **UnitVectorY-Labs Design Examples**, not “UVY Guide” or “UVY Examples”.
- **Reserve `uvy-` strictly for code identifiers.** The short `uvy-` prefix belongs only in machine-facing technical identifiers: CSS custom properties (`--uvy-*`), CSS classes (`.uvy-*`), filenames (`site/uvy.css`, `site/uvy.js`, `assets/uvy-*.svg`), the theme cookie (`uvy-theme`) and repository slugs (`uvy-design`).

## Single-CSS adoption contract

`site/uvy.css` is designed as **one self-contained, zero-dependency stylesheet** that any UnitVectorY-Labs application can embed directly (for example via Go `//go:embed`, a static `<link>`, or an inline `<style>`):

1. **Copy `site/uvy.css` and `site/uvy.js` verbatim.** Because they rely on universally supported system font stacks and inline SVG icons, they require no external CDNs, build pipelines or bundled font directories.
2. **Keep every application's identity and semantics.** Retain the product's own title, workflows, navigation model (sidebar or top-bar), fields and meaningful visualization colors.
3. **Standardize cookie theme persistence.** Use the single sun/moon toggle in the header and store the choice in the `uvy-theme` cookie (`light` or `dark`), mirrored on `<html data-theme="...">`.
4. **Choose container width to fit the app.** Use the default centered `.page` (`75rem` max) for reading, forms and detail pages, or add `.page--wide` (with `.site-header--wide` and `.site-footer--wide`) for dense full-width dashboards and matrices.
5. **The guide follows itself.** The rendered documentation site in this repository is built directly on `site/uvy.css` and `site/uvy.js` as the flagship reference implementation.

See [logo](logo.md), [color](color.md), [typography and spacing](typography-and-spacing.md), [components](components-and-icons.md), [footer](footer.md), [page archetypes](page-archetypes.md), [UnitVectorY-Labs Design Examples](../examples/index.html) and the [review checklist](review.md).
