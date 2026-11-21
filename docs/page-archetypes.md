# Page archetypes

All archetypes share `site/uvy.css`, `site/uvy.js`, the [universal header](header.md) and the [footer](footer.md). Choose centered (`.page`, `75rem` max) or full-width (`.page--wide`), and choose sidebar or top-bar navigation based on the application's workload.

| Archetype | Width & navigation | Core patterns | Examples / portfolio fit |
| --- | --- | --- | --- |
| Project landing | `.page`, top-bar | Compact display `.hero`, `.uvy-features` divided by hairlines | [Landing](../examples/landing.html) |
| Catalog with sidebar | `.page`, sticky sidebar + search | Sidebar filter, mobile drawer, `.uvy-kv` datasheet, evidence panels | [Sidebar nav](../examples/navigation.html), [Detail panels](../examples/panels.html) — DNS CAA, JWKS, GCP IAM/Service Catalogs |
| Wide catalog / top-bar search | `.page--wide`, top-bar (no sidebar) | Header links, `.uvy-tabs`, `.uvy-toolbar` search + wide table | [Top-bar nav](../examples/topbar.html), [Record table](../examples/table-records.html) — Unreleased Commits, Badge Indexer, GH Scan Scope |
| Lookup & inspection tool | `.page`, top-bar | Compact query form, `.uvy-output` terminal well, `.uvy-code` + `.uvy-copy` | [Utility](../examples/utility.html), [Forms](../examples/forms.html) — Cert Observatory, OCI Supply Chain Observatory, GCP Metadata Explorer, Lockbox KMS |
| Operational dashboard | `.page` or `.page--wide`, top-bar | `.uvy-stats`, `.uvy-toolbar`, `.uvy-list` lanes, charts, `<dialog>` | [Application](../examples/application.html) — GHA Dashboard, GCP Spot Observatory |
| Documentation site | `.page`, sticky sidebar | Breadcrumbs, `.uvy-page-header`, `70ch` prose, `.uvy-panel` tables, `.uvy-code` | [Static article](../examples/documentation.html), [this guide](foundations.md) |

## Width and navigation guidelines

- **Centered `.page` (`75rem`)** prevents reading lines and form controls from sprawling across ultrawide monitors. Use it by default for docs, landings, detail pages and lookup utilities.
- **Fluid `.page--wide`** unlocks full viewport width for wide dashboards, multi-column lane boards, repo×badge matrices and top-bar search indexes. Keep `.site-header--wide` and `.site-footer--wide` aligned, and keep prose paragraphs inside capped at `70ch`.
- **Sidebar vs. top-bar**: Use a sticky left sidebar when users jump frequently across dozens of named sections or entities. Use top-bar navigation plus an inline `.uvy-toolbar` search when the entire app revolves around one searchable workspace or a handful of top-level views.

## Theming Jekyll documentation (`just-the-docs` and `minima`)

Sites built on `just-the-docs` or Jekyll `minima` can match UVY Design cleanly through their custom stylesheet (`_sass/custom/custom.scss` or `assets/css/style.scss`):

- Map canvas, surface, border, text, muted text, link, code well and focus variables directly to the light (`#F5F7FA` / `#FFFFFF` / `#F25C05`) and midnight-slate dark (`#090D16` / `#111827` / `#FF7A1A`) tokens in [Color](color.md).
- Set body font to `--uvy-font-sans` and brand/code/table headers to `--uvy-font-mono`.
- Use the `3px` orange active bar on sidebar links and keep the centered UnitVectorY-Labs footer and sun/moon cookie toggle where the layout allows.
