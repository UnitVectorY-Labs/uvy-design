# Footer

Every page keeps a compact, calm, centered footer **always visible at the bottom of the viewport**:

**UnitVectorY-Labs | license | named GitHub repository link(s)**

- Link `UnitVectorY-Labs` to `https://github.com/UnitVectorY-Labs`.
- Name and link the project's actual license (such as `MIT License` or `Apache-2.0 License`).
- Link each contributing repository by name in `<strong>` (rendered in fixed-width monospace primary ink), joined with “and” when multiple repositories apply, followed by “on GitHub”.
- Keep third-party asset notices (such as Tabler Icons) with their source assets rather than crowding the footer.

## Always-visible layout and compact sizing

- **Always shown at the bottom of the viewport.** `.site-footer` uses `position: sticky; bottom: 0; z-index: 3;` with `margin-top: auto` on the flex `<body>`. On short pages it sits flush at the bottom of the window; on tall pages it remains anchored to the bottom of the viewport while scrolling and docks cleanly beneath `<main>` at the end of the document without clipping or obscuring the final lines of content.
- **Compact vertical footprint.** Keep the footer slim so it never crowds the workspace: `10px` (`0.625rem`) vertical padding, `13px` (`0.8125rem`) primary text, `12px` (`0.75rem`) secondary metadata, `4px` (`var(--uvy-space-1)`) gap between lines, `--uvy-surface` background and a crisp `1px solid var(--uvy-border)` top border.
- **Calm styling and clear separation.** Space `|` separators cleanly (`margin-inline: var(--uvy-space-2)`) in `--uvy-border-emphasis`. Keep footer links in `--uvy-text-muted` without default underlines, brightening to `--uvy-text` with an underline on hover.
- **Scroll clearance and print.** `html` sets `scroll-padding-bottom: 4.5rem` so keyboard focus and `#anchor` jumps clear the sticky footer, desktop `.sidebar` limits its height cleanly above it, and `@media print` / very short viewports (`max-height: 28rem`) release sticky positioning automatically.
- **Wide alignment.** On wide layouts (`.page--wide`), add `.site-footer--wide` so the footer container aligns with the header and workspace gutters.

## Footer variants

Choose the variant that matches the application's publishing model. Each variant has its own standalone example page:

| Variant | Secondary line | When to use | Example |
| --- | --- | --- | --- |
| **Standard** | *(none)* | Single-repository static sites, documentation guides and utilities | [Footer — Standard](../examples/footer.html) |
| **Multiple repositories** | *(none)* | Sites combining a catalog and observer/generator repo (joined with “and”) | [Footer — Multiple repositories](../examples/footer-repositories.html) |
| **Last updated** | `Last updated: <time>…</time>` (`.footer-meta`) | Scheduled crawlers and generated static catalogs (`dns-caa-catalog`, `jwks-catalog`, `gcp-iam-catalog`) | [Footer — Last updated](../examples/footer-updated.html) |
| **Application version** | `Version …` (`.version`) | Deployed or containerized web apps when version display is enabled | [Footer — Application version](../examples/footer-version.html) |

### 1. Standard (single repository)

```html
<footer class="site-footer">
  <div class="footer-inner">
    <p>
      <a href="https://github.com/UnitVectorY-Labs">UnitVectorY-Labs</a>
      <span class="footer-sep" aria-hidden="true">|</span>
      <a href="LICENSE">MIT License</a>
      <span class="footer-sep" aria-hidden="true">|</span>
      <a href="https://github.com/UnitVectorY-Labs/uvy-design"><strong>uvy-design</strong></a> on GitHub
    </p>
  </div>
</footer>
```

### 2. Multiple contributing repositories

```html
<footer class="site-footer">
  <div class="footer-inner">
    <p>
      <a href="https://github.com/UnitVectorY-Labs">UnitVectorY-Labs</a>
      <span class="footer-sep" aria-hidden="true">|</span>
      <a href="LICENSE">MIT License</a>
      <span class="footer-sep" aria-hidden="true">|</span>
      <a href="https://github.com/UnitVectorY-Labs/jwks-catalog"><strong>jwks-catalog</strong></a>
      and
      <a href="https://github.com/UnitVectorY-Labs/jwks-observer"><strong>jwks-observer</strong></a>
      on GitHub
    </p>
  </div>
</footer>
```

### 3. Static catalog with `Last updated` UTC timestamp

Generated catalogs and scheduled crawlers render a second centered line in compact `--uvy-text-faint` monospace (`12px`, `.footer-meta`) with an ISO-8601 UTC `<time>` timestamp:

```html
<footer class="site-footer">
  <div class="footer-inner">
    <p>
      <a href="https://github.com/UnitVectorY-Labs">UnitVectorY-Labs</a>
      <span class="footer-sep" aria-hidden="true">|</span>
      <a href="LICENSE">MIT License</a>
      <span class="footer-sep" aria-hidden="true">|</span>
      <a href="https://github.com/UnitVectorY-Labs/dns-caa-catalog"><strong>dns-caa-catalog</strong></a> on GitHub
    </p>
    <p class="footer-meta">Last updated: <time datetime="2026-11-21T16:05:05Z">2026-11-21T16:05:05Z</time></p>
  </div>
</footer>
```

### 4. Deployed application with optional version line

Containerized or deployed applications may render a second centered line in `--uvy-text-faint` monospace (`12px`, `.version`) showing their build/version identifier:

```html
<footer class="site-footer">
  <div class="footer-inner">
    <p>
      <a href="https://github.com/UnitVectorY-Labs">UnitVectorY-Labs</a>
      <span class="footer-sep" aria-hidden="true">|</span>
      <a href="LICENSE">MIT License</a>
      <span class="footer-sep" aria-hidden="true">|</span>
      <a href="https://github.com/UnitVectorY-Labs/cert-observatory"><strong>cert-observatory</strong></a> on GitHub
    </p>
    <p class="version">Version v1.4.2</p>
  </div>
</footer>
```

- Render `.version` only when the identifier exists and the application's version-display setting is enabled.
- Provide an environment variable to disable it (preserving any existing variable name in the application and documenting its default).
- When disabled or unset, omit the element and identifier completely from the server-rendered or built HTML.
