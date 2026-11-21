# Themes and navigation

## Cookie-persisted light and dark themes

Follow the operating system theme initially via `color-scheme: light dark` and `light-dark()`. When the user clicks the header sun/moon button, switch immediately and remember the choice across every page on the site:

- Save the choice in a first-party cookie: `uvy-theme=light|dark; path=/; max-age=31536000; SameSite=Lax` (mirroring to `localStorage` as a fallback when opening standalone HTML files over `file://`).
- Apply the saved cookie synchronously in `<head>` via `site/uvy.js` before first paint so pages never flash the wrong theme.
- Keep the control simple: one direct sun/moon toggle in the header. Do not add a “Use system theme” reset button or multi-option dropdown.
- The isolated [light](../examples/light.html) and [dark](../examples/dark.html) specimen pages set `data-example-theme="light|dark"` on `<html>` to force their respective modes without overwriting the user's `uvy-theme` cookie.
- All content and links remain usable when JavaScript, cookies or storage are unavailable; hide `#theme` until enhanced.

## Two navigation & search models

Applications across Unit Vector Y Labs use two primary navigation patterns — choose the one that fits the site's information architecture:

### 1. Persistent sticky sidebar + search

Best for multi-chapter documentation, large domain catalogs and entity trees (`dns-caa-catalog`, `jwks-catalog`, this design guide):

- A `15.5rem` sticky left sidebar (`position: sticky; top: 0; max-height: 100dvh; overflow-y: auto`) beside a naturally scrolling main column — never trap the whole viewport in `height: 100dvh; overflow: hidden`, which clips content above the footer.
- Keep search inputs sticky inside `.sidebar-tools` for long lists; omit search on short menus.
- Mark the current destination with `aria-current="page"` (or `"location"`), `--uvy-hover` fill and a bold `3px` `--uvy-accent` left bar.
- At `768px` or narrower, convert the sidebar into an accessible left drawer (`max-width: 18rem`) with close button, `Escape` and backdrop dismissal, Tab focus trapping, `inert` background and focus restoration. Without JavaScript, the sidebar renders inline above content.

See [sidebar navigation & search](../examples/navigation.html).

### 2. Top-bar navigation + inline search (no sidebar)

Best for single-workspace observatories, repository dashboards, lookup tools and wide tables (`unreleasedcommits`, `cert-observatory`, `ghadashboard`, `ghscanscope`):

- Omit the sidebar completely and optionally use `.page--wide` (with `.site-header--wide` and `.site-footer--wide`) so tables and boards can breathe across wide monitors.
- Put top-level destinations in the header nav (with the `3px` orange bottom rule) and place search, category tabs and filters directly above the results in a `.uvy-toolbar`.

See [top-bar navigation & search](../examples/topbar.html).

## Breadcrumbs, tabs and pagination

- **Breadcrumbs** (`.uvy-breadcrumbs`): Monospace path segments separated by `/` (`guide / color` or `examples / catalog / identity.example.com`) with `aria-current="page"` on the current item.
- **Tabs** (`.uvy-tabs`): `role="tablist"` with the same `3px` `--uvy-accent` bottom rule on `aria-selected="true"`, supporting `ArrowLeft`, `ArrowRight`, `Home` and `End`.
- **Pagination** (`.uvy-pagination`): Tabular visible range on the left and compact Previous / Next controls on the right.
