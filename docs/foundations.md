# Foundations — v0.1.0

## Scope: style existing applications

This repository establishes colors, fonts, spacing, icons, density and reusable visual elements. It does not authorize structural redesign. Preserve each application's layout, navigation, workflows, visible fields, sorting and filtering. Do not add tabs, move existing content behind disclosures, substitute a generic catalog shell or invent a new information hierarchy as part of adopting the guide. Any later structural proposal needs its own review.

Each application stands alone under its project name. Do not add UnitVectorY-Labs branding, cross-project portal navigation, decorative subtitles or eyebrow labels. Useful existing task descriptions remain where they help people use the application.

## Visual direction

Use blue and orange visibly and consistently: project blue masthead with white title, orange bottom rule, blue-led section/table styling and light/dark neutral content surfaces. Adapt those treatments to the application's existing header and sections. Do not manufacture new panels or navigation solely to exhibit tokens.

Use [Tabler UI](https://docs.tabler.io/ui) as a visual reference for readable technical interfaces, modest rounding and subtle shadows. This does not adopt its Bootstrap-based UI framework, layouts or JavaScript. System fonts are an intentional portability and performance choice. Use only selected [Tabler Icons](https://docs.tabler.io/icons) as inline SVG; no emoji substitutes, icon fonts or remotely loaded icon assets.

Detailed scales, color pairs and examples are in [style-guide.md](style-guide.md). Standard, compact and spacious densities are all supported. Density changes spacing, not which content exists; an application may select a density without adding a new user-facing selector.

## Brand and data colors are distinct

Blue/orange identifies the interface. The existing UnreleasedCommits green–yellow–red metric spectrum conveys meaningful relative values and must be preserved independently of branding. Preserve the application's numeric thresholds, interpolation, direction and values; do not reinterpret age or volume as a new severity system. Keep numeric values and labels visible, with readable foregrounds in both themes. A palette adjustment must not silently change data semantics.

## Existing mobile patterns are references

Use the existing UnreleasedCommits mobile record pattern: repository title and latest release, followed by three side-by-side metric cells with small readable labels. Preserve every field, sorting affordance and link. Avoid converting those metrics into a tall field-by-field list or hiding them to shorten a card. Fit long names and labels without page-wide overflow.

Do not impose that card on every application. JWKS explorer retains its explorer structure and navigation. CertSummary retains its input/output workspace; its mobile arrangement must keep both parts and normal results available. UnreleasedCommits repository detail retains its existing sections. Improve style and responsive fit within each established layout.

## Shared behavior and delivery

Use a top-right binary light/dark toggle, initialize from OS preference and remember explicit choices in a host-only cookie. There is no System selector or extra reset UI. Each application's footer links to its own GitHub repository and MIT license and sits at the bottom via a growing main region, never fixed over content. See [the behavior contract](theme-and-interaction-contract.md).

All runtime assets must be self-contained: local pinned HTMX, local CSS and small scripts, system fonts and inline Tabler SVG. Static generated output contains its assets; Go-served applications embed theirs. Do not add CDN dependencies or an additional client framework. The guide's examples do not require Tabler CSS or Bootstrap.

## Review gate

Review actual-layout specimens: JWKS explorer, UnreleasedCommits index and repository detail, and CertSummary workspace, in both themes and relevant mobile widths. Compare each to its source application's layout to catch unintended structural changes.

Check standard/compact/spacious spacing, real long values, keyboard focus, first-visit theme, persistence, footer placement and existing data colors. Keep normal data visible; do not add tabs or disclosures. Test 320px width, 200% zoom and reduced motion. Target [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/), including text/control contrast and target sizing. Visual review alone does not certify accessibility.

[Impeccable](https://github.com/pbakaus/impeccable) and [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) informed research and critique. User requirements govern the result; neither tool is a runtime dependency or an industry standard.
