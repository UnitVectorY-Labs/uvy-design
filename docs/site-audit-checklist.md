# Per-site visual audit and future migration checklist

Per-site audit items for adopting v0.1.0. Use this checklist with the mandatory screenshot matrix in [consuming](consuming.md). No merge/deployment is implied.

## Invariants for every site

- Preserve layout, navigation location/links/behavior, section order, filters, fields, workflows and actual data.
- Preserve existing visualizations and intentional green–yellow–red scales; no replacement heatmaps, new dashboard architecture or standardized sidebar.
- Preserve each application's technology and rendering model; no framework migration, required remote runtime assets or unnecessary HTMX adoption.
- Restrict markup changes to styling hooks and necessary accessibility: language, labels, accessible names, focus, status associations, expanded state and semantics. Record larger interaction defects separately.
- Preserve the UnreleasedCommits compact three-metric mobile row; use it as reference where three existing metrics are comparable, without inventing metrics elsewhere.

## Shared evidence pass

For each site capture route, date, viewport, theme and representative state. Review desktop and 390px light/dark with real long values. Check system fonts, token contrast, type hierarchy, spacing/density, official inline Tabler icon size/stroke, controls, theme persistence, bottom GitHub/license footer and locally served assets. Test keyboard, 200% text zoom, deep links and no-JS baseline where applicable. Confirm no structural change through before/after comparison. Screenshots do not certify accessibility.

Use these mapping keys in an adoption record: **T** color tokens; **Y** typography; **S** spacing/density; **I** icons; **C** controls/minimal accessibility; **H** theme; **F** footer; **L** local assets.

## DNS CAA Catalog

Preserve sidebar/detail, mobile navigation, domain/provider pages, summary arrangement and checkbox combinations.

- [ ] T/H: map blue/orange, surfaces, record absence/error/status to light/dark tokens without changing meaning.
- [ ] Y/S: align headings, dense navigation, record tables and summary padding; check sticky filter offsets at zoom.
- [ ] I: replace decorative interface emoji with official inline Tabler SVG where appropriate; retain meaningful record labels.
- [ ] C: label search; verify filter labels, visible focus, menu name/expanded state; record larger navigation issues separately.
- [ ] F/L: consistent project/license footer; vendor HTMX and shared assets locally with versions/notices.
- [ ] Evidence: home, domain with/without records, provider, filtered nav and mobile open/closed navigation; direct full page plus existing HTMX path.

## JWKS Catalog / JWKS Observer

Preserve sidebar/detail, provider filter/marks, endpoint sections, key history and observer provenance. Observer remains data-only.

- [ ] T/H: theme endpoint/history/provider-evidence surfaces; retain explicit active/history/unknown meanings.
- [ ] Y/S: tune dense services, endpoint labels and monospace URLs/KIDs; test wrapping without losing selectable values.
- [ ] I: official inline UI icons; keep provider marks and their screen-reader naming.
- [ ] C: label search; check focus, mobile expanded state and nested-link close behavior as minimal repairs; preserve provider filtering.
- [ ] F/L: footer references correct catalog/observer sources; serve pinned HTMX locally; preserve version-correct colon-separated HTMX 4 events.
- [ ] Evidence: home, provider-filtered list, service endpoints, active/history keys, long IDs, mobile navigation and full/fragment parity.

## GCP IAM Catalog

Preserve horizontal navigation, browse/detail, comparisons, include/exclude search, saved state and URL sharing.

- [ ] T/H: map action/accent/surfaces and semantic states; preserve information encoded by existing status colors.
- [ ] Y/S: align system type, dense list rows, compare panels and form padding without moving sections.
- [ ] I: official inline UI icons at consistent scale; retain accessible action names.
- [ ] C: language, labels, focus and accessible copy/status feedback. Inventory div-table/autocomplete semantics as scoped repairs; no replacement workflow without review.
- [ ] F/L: correct footer and local assets; do not add HTMX to vanilla-JS filtering or comparisons solely for consistency.
- [ ] Evidence: home, role/permission list/detail, compare two items, include/exclude results, empty/error and saved/shared state at both widths/themes.

## GCP Service Catalog

Preserve horizontal navigation and services/domain/API list/detail hierarchy and columns.

- [ ] T/H: tokenize surfaces/actions; distinguish non-preferred API lifecycle with readable text plus existing semantics.
- [ ] Y/S: consistent type, table density and long API/service identifier wrapping.
- [ ] I/C: official inline search/UI icons; labels, html language, focus and native control consistency. Keep existing search behavior unless a specific small repair is reviewed.
- [ ] F/L: bottom project/license footer and versioned local CSS/JS; no new HTMX requirement.
- [ ] Evidence: home, services, domains, APIs and detail; long descriptions, mobile navbar/table and no-match state. Preserve data while correcting accidental overflow.

## CertSummary

Preserve existing input/result workbench, certificate parsing, examples and actions; do not migrate its stack.

- [ ] T/H: theme workbench, validation and certificate-value surfaces with blue/orange and meaningful error states.
- [ ] Y/S: align system type, textarea/code values and compact result spacing without reorganizing panels.
- [ ] I/C: inline official icons; named buttons, input/error association, focus and copy feedback using minimal markup.
- [ ] F/L: bottom project/license footer; local assets; no remote parse endpoint or new Go/HTMX requirement.
- [ ] Evidence: empty, valid PEM, malformed PEM, example, long subject/SAN/fingerprint and clipboard failure; mobile current layout.

## BadgeIndexer

Preserve repository/badge views, preview rendering, visible filters, count/data grouping and current navigation.

- [ ] T/H: tokenize panels, action/accent and filter states; keep badge artwork intact.
- [ ] Y/S: align counts, rows, preview spacing and technical repository identifiers with appropriate density.
- [ ] I/C: official inline interface icons; retain actual badges; labels, focus, selected-filter distinction and feedback.
- [ ] F/L: consistent footer; local pinned HTMX/CSS/scripts; retain badge artwork and audit image delivery separately so the self-contained implementation can snapshot/cache badge assets at build time rather than silently adding browser dependencies.
- [ ] Evidence: dashboard, active/cleared filters, no-match, repository detail, badge detail and narrow preview-heavy screen.

## UnreleasedCommits

Preserve repository/release/commit presentation, sorting/filtering, history and intentional green–yellow–red spectrum.

- [ ] T/H: retain heatmap/spectrum mapping and legends; improve light/dark legibility without replacing visualization.
- [ ] Y/S: preserve compact three-metric side-by-side mobile treatment; tune font sizes, gaps and labels for real counts.
- [ ] I/C: official inline UI icons; retain data indicators, accessible action names/focus and current controls.
- [ ] F/L: bottom GitHub/license footer and pinned local assets; preserve existing HTMX/static behavior.
- [ ] Evidence: overview with low/mid/high values, three metrics at 390px, repository/commit detail, no release/no commits distinctions and long names/SHAs.

## Cert Observatory

Preserve live Go architecture, existing navigation/layout, domain/certificate views and all charts/heatmaps/scales.

- [ ] T/H: map shared tokens into current Tailwind source/compiled output; keep meaningful semantic and visualization colors.
- [ ] Y/S: align type/density, current panels, dense certificate tables and long values; no shell replacement.
- [ ] I/C: standardize official inline Tabler SVG usage; labels, focus, lookup validation and async feedback with minimal changes.
- [ ] F/L: footer alignment, local pinned HTMX and embedded assets; retain required compiled CSS and Go embed workflow.
- [ ] Evidence: domain lookup, domain/certificate detail, list/history/visualization, loading/error and narrow existing navigation in both themes. Follow this repo's screenshot rules during any future implementation.

## Adoption record

For each later site record reviewed baseline/prototype links, approved asset version, T/Y/S/I/C/H/F/L results, minimal markup repairs, unchanged layout/navigation/scale confirmation, outstanding separately reviewed behavior issues and actual verification limits. Do not mark a site migrated from screenshot review alone.
