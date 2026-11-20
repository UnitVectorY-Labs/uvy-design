# Universal header

Use the same anatomy across sites: a theme icon at the far left, compact product identity beside it, and contextual navigation on the right. Applications retain their own name, mark and destinations.

- Use a 56px minimum desktop height, page-aligned gutters, surface background and 1px neutral bottom border. Omit shadows.
- Make the theme button 36px square, increasing to 44px for coarse pointers. Use a Tabler moon in light mode and sun in dark mode, with an action-specific accessible name and title such as “Switch to dark mode.”
- Keep identity readable as names wrap. On narrow screens, retain the theme icon and identity on the first row; put the sidebar menu trigger at the right and allow other navigation to wrap.
- Selected destinations use accessible accent-derived text, a visible indicator and `aria-current="page"`.
- The sidebar trigger uses a Tabler menu icon, a clear accessible name, `aria-controls` and accurate `aria-expanded`.

The theme button switches directly between light and dark. Offer a separate “Use system theme” action in the sidebar footer or page footer; do not replace the button with a theme dropdown.

See the working [header and sidebar reference](../examples/navigation.html), [documentation layout](../examples/documentation.html) and [landing page](../examples/landing.html).
