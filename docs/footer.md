# Footer

Every page ends with a compact, centered footer:

**UnitVectorY-Labs | license | named GitHub repository link(s)**

- Link `UnitVectorY-Labs` to `https://github.com/UnitVectorY-Labs`.
- Name and link the project's actual license (for example, `MIT License` or `Apache-2.0 License`).
- Link each contributing repository by name in `<strong>`, joined with “and” when multiple repositories apply, followed by “on GitHub.”
- Keep unrelated credits (such as icon or font attributions) out of the footer; place third-party license notices alongside their source assets.

## Visual treatment

- `1px solid var(--uvy-border)` top divider, `16px` (`1rem`) vertical padding and `14px` text in `--uvy-text-muted`.
- Footer links inherit `--uvy-text-muted` with subtle underlines and darken to `--uvy-text` on hover — never loud orange link blocks at the bottom of the page.
- Separate items with `<span class="footer-sep" aria-hidden="true">|</span>` in `--uvy-border-emphasis`. Allow links to wrap cleanly into centered lines on narrow screens.
- Keep the footer outside the scrolling `.workspace` pane so it never overlays content.

## Optional application version line

Containerized or deployed applications may render a second centered line in `--uvy-text-faint` monospace (`12px`, `.version`) showing their build/version identifier:

- Render the line only when a version identifier is supplied and the application's version-display toggle is enabled.
- Provide an environment variable to disable it (preserving any existing variable name in the application and documenting its default).
- When disabled or unset, omit the element and identifier completely from the server-rendered or built HTML. Never rely on client JavaScript to hide it.

See the [footer example](../examples/footer.html), [static article](../examples/documentation.html) and [dynamic application](../examples/application.html).
