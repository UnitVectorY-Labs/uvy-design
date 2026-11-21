# Footer

Every page ends with a calm, generously spaced, centered footer:

**UnitVectorY-Labs | license | named GitHub repository link(s)**

- Link `UnitVectorY-Labs` to `https://github.com/UnitVectorY-Labs`.
- Name and link the project's actual license (such as `MIT License` or `Apache-2.0 License`).
- Link each contributing repository by name in `<strong>` (rendered in fixed-width monospace primary ink), joined with “and” when multiple repositories apply, followed by “on GitHub.”
- Keep third-party asset notices (such as Tabler Icons) with their source assets rather than crowding the footer.

## Visual treatment and spacing

- Give the footer real breathing room: `32px` (`2rem`) vertical padding (`padding-block: var(--uvy-space-6)`), `--uvy-surface` background and a crisp `1px solid var(--uvy-border)` top border.
- Space the `|` separators generously (`margin-inline: 0.75rem`) in `--uvy-border-emphasis` so items never feel crowded.
- Keep footer links calm (`--uvy-text-muted`, no heavy default underlines), brightening to `--uvy-text` with a crisp underline on hover.
- Because sidebar layouts use sticky positioning and natural document scrolling, the footer always rests cleanly at the bottom of the document — never slicing scrolled text above it.
- On wide layouts (`.page--wide`), add `.site-footer--wide` so the footer container aligns with the header and workspace gutters.

## Optional application version line

Containerized or deployed applications may render a second centered line in `--uvy-text-faint` monospace (`12px`, `.version`) showing their build/version identifier:

- Render it only when the identifier exists and the application's version-display setting is enabled.
- Provide an environment variable to disable it (preserving any existing variable name in the application and documenting its default).
- When disabled or unset, omit the element and identifier completely from the server-rendered or built HTML.

See the [footer example](../examples/footer.html), [static article](../examples/documentation.html) and [dynamic application](../examples/application.html).
