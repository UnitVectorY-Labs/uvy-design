# Themes and navigation

## Light and dark themes

Follow the operating system preference initially via `color-scheme: light dark` and `light-dark()` tokens, and react immediately to OS changes while no user override is set.

- Store explicit choices in `localStorage` under the shared key `uvy-theme` (`"light"` or `"dark"`) and mirror them onto `<html data-theme="light|dark">`.
- Run the small theme bootstrap script synchronously in `<head>` so saved choices apply before first paint without a flash of the wrong theme.
- The header sun/moon button switches directly to the opposite theme; “Use system theme” deletes `data-theme` and removes `uvy-theme`.
- Keep all pages readable and navigable when JavaScript or `localStorage` is unavailable; hide JS-only controls with `hidden` until enhanced.
- Listen to `window`'s `storage` event so open tabs on the same origin stay synchronized.

The isolated [light](../examples/light.html) and [dark](../examples/dark.html) examples lock their initial mode with `data-example-theme` so side-by-side comparison stays predictable.

## Guide and example separation

Keep documentation chapters and full-page examples in separate destinations. A documentation sidebar lists chapters in one stable conceptual order without mixing local anchors, examples or unnecessary search boxes into a short menu.

## Application sidebars and drawers

Use a persistent `15rem` left sidebar on desktop separated by a `1px` vertical border. Inside the sidebar:

- Keep section search or domain filters sticky above an independently scrolling link list; omit filters when a sidebar has fewer than ~12 links.
- Mark the active destination with `aria-current="page"` (or `"location"` for in-page sections), `--uvy-hover` fill, `--uvy-text` ink and a `2px` `--uvy-accent` left bar — the vertical counterpart of the header's 2px bottom bar.
- At `768px` or narrower, collapse the sidebar into a left slide-over drawer (`max-width: 18rem`, leaving a visible tappable backdrop). Provide an explicit close button; dismiss on `Escape`, backdrop click, link activation or resize back to desktop. Set `role="dialog"`, `aria-modal="true"`, trap keyboard Tab focus, mark background landmarks `inert`, lock body scroll and restore focus to the menu button on close.
- Without JavaScript, render the sidebar inline above the content so every link remains reachable.

## Breadcrumbs, tabs and pagination

- **Breadcrumbs** (`.uvy-breadcrumbs`): Use on nested entity detail pages, metadata browsers and documentation hierarchies (`Catalog / Service / Key`). Separate items with a quiet `/` and mark the final item `aria-current="page"`.
- **Tabs** (`.uvy-tabs`): Use `role="tablist"` and `role="tab"` to switch between closely related views of the same entity (for example, formatted claims vs. raw JSON payload). The selected tab (`aria-selected="true"`) carries the same `2px` `--uvy-accent` bottom rule as header navigation. Support `ArrowLeft`, `ArrowRight`, `Home` and `End` keys. Never hide primary content behind tabs purely to shorten a page.
- **Pagination** (`.uvy-pagination`): Show the current visible range in tabular numerals on the left and quiet Previous / Next links or buttons on the right.

See [header, sidebar and tabs](../examples/navigation.html), [detail panels](../examples/panels.html) and [static article](../examples/documentation.html).
