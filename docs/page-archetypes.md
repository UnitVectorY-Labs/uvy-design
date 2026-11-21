# Page archetypes

All archetypes share the [universal header](header.md), [footer](footer.md), `--uvy-*` tokens and component grammar. Choose a layout for the task at hand; reserve a hero strictly for project landing pages.

| Archetype | Hero | Layout structure | Examples / portfolio fit |
| --- | --- | --- | --- |
| Project landing | Compact | Typographic hero + rule-divided capabilities (`75rem` max) | [Landing](../examples/landing.html) |
| Catalog index & detail | None | Sidebar or search toolbar, stat strip, tables, `.uvy-kv` datasheet, evidence panels | [Panels](../examples/panels.html), [Record table](../examples/table-records.html) — DNS CAA, JWKS, GCP IAM/Service Catalogs, Unreleased Commits |
| Lookup & inspection tool | None | Focused query form/toolbar directly above structured results, tabs and JSON/token viewer | [Utility](../examples/utility.html), [Forms](../examples/forms.html) — Cert Observatory, OCI Supply Chain Observatory, GCP Metadata Explorer, Lockbox KMS |
| Operational dashboard | None | Filter toolbar, `.uvy-stats`, status lanes (`.uvy-list`), charts and detail `<dialog>` | [Application](../examples/application.html) — GHA Dashboard, GCP Spot Observatory, GH Scan Scope |
| CRUD / admin workspace | None | Breadcrumbs, resource table, create/edit forms, confirmation dialogs | [Table](../examples/table.html), [Forms](../examples/forms.html) — Worktree Foundry, Service Auth Central |
| Documentation site | None | Persistent `15rem` sidebar, `70ch` prose column, code blocks | [Static article](../examples/documentation.html), [Guide](foundations.md) |

## Archetype notes

- **Project landing pages** open with a clear display headline (`clamp(2.25rem, 1.5rem + 3vw, 3rem)`), a plain one-sentence explanation (`.uvy-lead`), and at most one primary orange action plus a secondary documentation link. Follow with `.uvy-features` divided by a hairline rule rather than a grid of decorative cards. Skip illustrations and tracked-out eyebrows.
- **Catalogs and static detail pages** render complete, readable content and normal links in the initial HTML. Group entity metadata in `.uvy-kv`, show evidence tables edge-to-edge inside `.uvy-panel`, and preserve domain-specific row colors (lifecycle, severity, quantitative spectra) alongside explicit labels.
- **Lookup and inspection utilities** keep input, action and output tight in one view. Show raw payloads (certificates, JWT claims, JSON responses) in `.uvy-code` with `.uvy-copy` buttons and `.uvy-tabs` when multiple views exist.
- **Dynamic dashboards** keep filters, refresh controls and live status text (`role="status"`) adjacent to the results they update. Preserve filter state and focus across HTMX swaps or polling refreshes. Use `<dialog>` for detail views and destructive confirmations, not to hide primary page content.

## Theming Jekyll documentation (`just-the-docs` and `minima`)

Projects published with `just-the-docs` or Jekyll `minima` can adopt the UVY aesthetic without rewriting their templates:

- Override the theme's Sass variables or custom stylesheet (`_sass/custom/custom.scss` or `assets/css/style.scss`) to map background, surface, border, body text, muted text, link, code well and focus colors directly to the `--uvy-*` light and dark hex values in [Color](color.md).
- Set body and heading fonts to IBM Plex Sans (`--uvy-font-sans`) and code to IBM Plex Mono (`--uvy-font-mono`).
- Replace default purple/blue sidebar active states and link accents with `--uvy-accent` (2px indicator) and `--uvy-link`.
- Keep the shared centered UnitVectorY-Labs footer structure and direct sun/moon theme toggle where the layout allows.
