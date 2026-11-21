# Foundations

Unit Vector Y Labs software is made for engineers inspecting infrastructure, security posture, certificates, signing keys and repositories. Interfaces take their cues from precision measuring instruments and technical datasheets: quiet graphite surfaces, crisp typography, disciplined spacing and clear information hierarchy.

## Core principles

- **Flat, cool graphite surfaces.** Let contrast between page canvas, elevated surface and sunken code wells organize the screen. Omit decorative gradients, glassmorphism and ambient shadows; reserve shadows strictly for overlays such as dialogs and mobile drawers.
- **One disciplined accent.** Signal orange marks primary actions, keyboard focus and a crisp 2px active-location rule in navigation and tabs. Keep chrome, icons, headings and footers neutral so orange retains its signal value.
- **Structure encodes meaning.** Use hairline borders, tables, key/value datasheets and grouped panels only where they clarify hierarchy. Do not wrap every paragraph or link in identical rounded cards, do not nest panels inside panels, and do not add numbered markers unless the content is an ordered sequence.
- **Restrained typography.** Set interfaces in IBM Plex Sans and reserve IBM Plex Mono for actual technical values (identifiers, domains, SHAs, versions, endpoints and code). Avoid tracked-out all-caps eyebrow labels, decorative single-word color accents in headings, and arrow glyphs appended to button labels.
- **Purposeful motion.** Motion answers a direct user action (opening a drawer, confirming a copy, hovering a control) in 120–180ms. Avoid scroll-triggered section entrances, floating hover lifts and ambient animations. Always honor `prefers-reduced-motion`.
- **Direct writing.** Write in sentence case and active voice from the user's perspective. Name buttons for what they do (“Check domain”, “Save changes”, not “Submit”). Errors explain what failed and how to recover without apologizing. Empty states state what is absent and offer the next step.
- **First-class light and dark modes.** Follow the operating system by default, allow an instant toggle, and verify contrast in both modes.

## Adopting this guide in an application

This repository is an unversioned, human-readable reference rather than a distributed CSS framework. Go `html/template` apps, HTMX servers, Jekyll sites and static catalogs all share the same visual contract while owning their own markup and build pipelines:

1. **Preserve the application.** Keep the application's product name, purpose, navigation structure, data semantics, workflows and meaningful visualization colors. Do not hide useful columns or fields behind extra clicks for appearance alone.
2. **Use the semantic token contract.** Copy the `--uvy-*` custom properties and `color-scheme: light dark` / `light-dark()` definitions from `site/reference.css`. Project-specific CSS should reference those tokens instead of hardcoding colors or spacing.
3. **Standardize theme storage.** Store explicit theme overrides under the `uvy-theme` key (`"light"` or `"dark"`) on `localStorage`, reflect them on `<html data-theme="...">`, and keep the theme switch button at the top right of the header.
4. **Reuse namespaced primitives.** Use semantic HTML first, then adopt `uvy-*` classes (`uvy-panel`, `uvy-kv`, `uvy-stats`, `uvy-status`, `uvy-badge`, `uvy-toolbar`, `uvy-code`, `uvy-alert`, `uvy-empty`, `uvy-tabs`, `uvy-list`) where shared patterns apply.
5. **Preserve proven application layouts.** Retain the [DNS CAA Catalog](https://dns-caa-catalog.unitvectorylabs.com/) sidebar/drawer, [Cert Observatory](https://cert-observatory.unitvectory-labs.net/) direct icon theme switch, [JWKS Catalog](https://jwks-catalog.unitvectorylabs.com/service-3d-systems.html) grouped detail and lifecycle labels, and [Unreleased Commits](https://unreleasedcommits.unitvectorylabs.com/) mobile record layout and metric semantics, styled with this guide's palette, type and geometry.

See [color](color.md), [components](components-and-icons.md), [page archetypes](page-archetypes.md), the [examples index](../examples/index.html) and the [review checklist](review.md).
