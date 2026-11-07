# UVY Design

Design standards for the standalone UnitVectorY Labs website projects. Standardize colors, typography, spacing, icons and reusable elements while preserving each app's layout, navigation, workflow and meaningful data colors.

Version 0.1.0. Interface color is blue primary/orange accent with Tabler as the reference for modest rounding, subtle shadows and consistent controls; the existing green–yellow–red data spectrum remains intentional and independent. System fonts and standard/compact/spacious spacing are documented choices. Each app keeps its own identity, a top-right light/dark toggle and a standard project source/license footer.

## Consume

Copy the versioned files into the application's own asset directory. No network retrieval occurs at runtime. See [consuming](docs/consuming.md) for the full contract, including the required `UVY_DESIGN.md` adoption record and screenshot-backed PR evidence.

```html
<script src="assets/uvy-theme.js"></script>
<link rel="stylesheet" href="assets/uvy-tokens.css">
<link rel="stylesheet" href="assets/site.css">
```

| Path | Contents |
| --- | --- |
| `assets/uvy-tokens.css` | Light/dark color tokens |
| `assets/uvy-theme.js` | Cookie theme controller: OS preference first visit, top-right binary toggle |
| `assets/uvy-elements.css` | Optional element treatments |
| `icons/` | Official Tabler outline SVG sources (MIT), rendered inline |
| `vendor/htmx-4.0.0.min.js` | Pinned HTMX for applications that already use HTMX |

## Documents

- [Style guide](docs/style-guide.md): color tokens, type scale, spacing/densities, corners/shadows, icons, element treatments and mobile references.
- [Foundations](docs/foundations.md): scope, visual direction and the brand-versus-data color rule.
- [Component contracts](docs/components.md): style existing elements and preserve their behavior.
- [Theme and interaction contract](docs/theme-and-interaction-contract.md): theme cookie, static/HTMX output rules, shared states and controls.
- [Per-site audit checklist](docs/site-audit-checklist.md): actionable review items per application.
- [Consuming](docs/consuming.md): pinning, vendoring, theme button, adoption record and PR evidence requirements.

## Review specimens

The prototype stack demonstrates the standards against real application structures with bounded fixture data: UnreleasedCommits index/repository, JWKS explorer and service detail, and the CertSummary workbench.

Requires Go 1.26 or newer and any static HTTP server. There is no Go module dependency, frontend build step or runtime network dependency.

```sh
go run ./cmd/previewgen
python3 -m http.server 8765 --directory output --bind 127.0.0.1
```

Open <http://127.0.0.1:8765>. The review index is a navigation aid, not a portal to deploy. To compare spacing, open `table.html?density=compact` or `table.html?density=spacious`; omitting the parameter uses standard. Density is an implementation option, not a proposed extra application control.

HTMX 4.0.0 is shipped locally and exercised in the JWKS example. Selected Tabler outline SVGs are embedded inline by Go templates. Theme and app-specific review scripts are local; fonts use the system stack. No Tabler UI/Bootstrap runtime, CDN, webfont, icon font or icon JavaScript package is used. Snapshots are recorded from the real sites, with source URLs/times in [fixtures](prototypes/fixtures/); the examples intentionally bound their data and label it. [Asset manifest](prototypes/vendor/manifest.json) records origin commits and SHA-256 hashes; [third-party notices](THIRD_PARTY_NOTICES.txt) and full licenses accompany the source/generated output. [Optional browser review tools](tools/browser/README.md) support capture and QA runs.
