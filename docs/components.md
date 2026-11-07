# Style and component contracts — v0.1.0

These contracts preserve every application's layout, navigation, content order, workflows and data presentations. This is a styleguide and visual-polish effort. It does not authorize a replacement shell, a new information architecture, hidden filters, redesigned mobile records or replacement heatmaps.

Tabler is visual inspiration for restrained surfaces, typography, controls and spacing, not a runtime dependency. Use system fonts, blue as primary and orange as accent, and official Tabler SVGs embedded inline. Serve pinned HTMX locally where an application already uses it. Plain CSS and minimal JavaScript remain appropriate; static sorting, local filtering and certificate parsing need no new framework or remote endpoint.

## Foundations

| Contract | Application |
| --- | --- |
| Color tokens | Named light/dark surface, text, border, focus, blue action and orange accent values; preserve meaningful semantic colors and visualization scales. |
| Typography | System-font stack; consistent heading/body/label scale; monospace only for technical values. Preserve existing hierarchy and content order. |
| Spacing and density | Shared spacing scale with comfortable and compact treatments. Dense reference data remains dense; tune padding and line height before changing markup. |
| Surfaces | Restrained borders, radii and shadows inspired by Tabler. Polish current cards/panels rather than imposing new ones. |
| Icons | Inline official Tabler SVG, consistent size/stroke and currentColor; decorative icons aria-hidden, icon-only actions retain accessible names. Retain third-party provider marks and actual badges. |
| Local assets | Vendor/version CSS, small scripts, HTMX and any icon source notices. No required remote font or runtime stylesheet. |

## Components in their existing locations

| Component | Polish contract | Verification |
| --- | --- | --- |
| Existing header/navigation | Keep placement, links, labels and desktop/mobile interaction. Harmonize colors, type and active/focus states; project identity stays standalone. | Long name, keyboard, active route, narrow width, deep link. |
| Existing heading/section | Tune type, spacing and blue/orange accents without moving sections or adding promotional copy. | Long technical names, hierarchy, 200% text zoom. |
| Theme toggle | Binary light/dark button at top right; first visit follows OS until explicit choice persists in a host-only cookie. Initialize before paint; keep state outside HTMX swap region. | Reload, OS change before explicit choice, unavailable cookies, swaps and accessible action name. |
| Input/filter/control | Consistent border, radius, padding and focus; add necessary labels/associations with minimal markup. Preserve existing filter visibility, semantics and order. | Empty, typing, disabled, invalid, keyboard, no-match and reset when already present. |
| Existing list/table | Keep columns, fields, grouping, actions and responsive behavior; polish row padding, separators, identifiers and status text. | Real long URLs, KIDs, repository names, narrow viewport; no omitted data. |
| Metrics | Use the existing UnreleasedCommits compact mobile pattern as reference: three metrics side by side. Keep concise labels and readable values; do not mandate large cards or stack these three by default. | Three values at 390px, long/zero/unavailable values and enlarged text. |
| Status/feedback | Pair meaning with text where necessary; style existing success/warning/error/unknown states. Brand orange remains distinct from warnings. | Dark/light contrast, screen-reader feedback for existing async changes. |
| Numeric colors/heatmaps | Preserve intentional green–yellow–red spectrum, value mapping, heatmap structure and legends. Adjust theme contrast only; do not substitute badges, bars or a monochrome scale. | Range extremes, missing values, unchanged numerical interpretation. |
| Metadata/code/copy | Preserve placement and content; tune monospace, wrapping and buttons; add specific accessible names and copy feedback where needed. | Long values, selection, clipboard failure, no page overflow. |
| Footer | Bottom project GitHub/actual-license links, consistent typography and theme styling; nonfixed, never overlays content. | Short/long pages and narrow widths. |

Minimal accessibility repairs are within the audit inventory: labels, language, focus visibility, accessible names, expanded state and appropriate semantics where needed. They are not a reason to change navigation or redesign a workflow. Any larger interaction issue should be recorded separately for review.

## Per-application boundaries

- DNS CAA and JWKS keep their sidebar/detail layout and existing mobile navigation. Observer remains a data source with no new UI.
- GCP IAM retains role/permission browse, comparison and include/exclude search. GCP Service retains its horizontal navigation and list/detail pages.
- CertSummary retains its certificate input/result workbench and actual parsing behavior.
- BadgeIndexer retains repository/badge views, previews and visible filters.
- UnreleasedCommits retains its repository presentation, green–yellow–red information encoding and compact three-metric mobile summary.
- Cert Observatory retains its existing live application structure, navigation, Tailwind build and Go embedding.

## Delivery and review

Begin with versioned vendorable CSS tokens/component treatments, a small theme script and examples that adapt current markup. A shared Go module is deferred until real reuse demonstrates a need. CertSummary must consume assets without a Go migration. Current HTMX 4 uses colon-separated event names; preserve version-correct handlers and verify against each pinned version rather than treating those names as defects.

Review actual application-based desktop/mobile light/dark screenshots. Check token contrast, type, density, icon consistency, controls, footer and local assets against the [site audit checklist](site-audit-checklist.md). Application adoption happens through per-application pull requests; nothing here authorizes merging or deployment.
