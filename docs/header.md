# Universal header

Use the same anatomy across sites: product identity on the left, contextual navigation beside it, and the theme icon at the far right. Applications retain their own name, mark and destinations.

- Use a 56px minimum desktop height, page-aligned gutters, surface background and 1px neutral bottom border. Omit shadows.
- Make the theme button 36px square, increasing to 44px for coarse pointers. Use a Tabler moon in light mode and sun in dark mode, with an action-specific accessible name and title such as “Switch to dark mode.”
- Keep identity readable as names wrap. On narrow screens, keep the theme button in the top-right corner of the first row, with the menu trigger and identity on the left. Other navigation may wrap below.
- Selected destinations use accessible accent-derived text, a visible indicator and `aria-current="page"`.
- The sidebar trigger uses a Tabler menu icon, a clear accessible name, `aria-controls` and accurate `aria-expanded`.

The theme button switches directly between light and dark. Offer a separate “Use system theme” action as a secondary action in the sidebar footer, or in header navigation when there is no sidebar; do not replace the button with a theme dropdown.

See the working [header and sidebar reference](../examples/navigation.html), [documentation layout](../examples/documentation.html) and [landing page](../examples/landing.html).
