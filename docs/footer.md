# Footer

Every page ends with a compact, centered footer: **UnitVectorY-Labs | license | named GitHub repository link(s)**. Link the organization to its GitHub profile, name the actual license, and link each contributing repository by name. Join multiple repositories with “and” followed by “on GitHub.” Keep unrelated credits out of the footer.

Use a neutral top border, 16px vertical padding and 14px text. Allow links to wrap naturally into centered lines on mobile. The footer stays outside the scrolling workspace and never overlays content. Static documentation and dynamic applications use the same structure.

Container applications may show a second, muted monospace line with their supplied build/version identifier. Render it only when the identifier exists and the application's version-display setting is enabled. An environment variable must be able to disable it; preserve an existing switch where present, and document the variable and its default in the application. Omit the whole line when disabled, including the identifier in the HTML. Read this configuration on the server, or at build time for static output; browser JavaScript cannot read container environment variables. A version is optional application metadata, not a version for this guide.

See the [isolated footer with repository and version controls](../examples/footer.html). The [static article](../examples/documentation.html) and [application workspace](../examples/application.html) show the same footer in context.
