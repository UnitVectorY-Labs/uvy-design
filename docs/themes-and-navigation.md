# Themes and navigation

Follow the operating-system theme initially and respond to system changes while no override is set. The [header's sun/moon button](header.md) switches directly to the opposite theme and persists that choice where storage is available. “Use system theme” clears the override. Keep the page usable without storage or JavaScript; hide inactive controls.

Use semantic color variables and `color-scheme` throughout. Apply saved preferences before painting where practical. Keep text, native controls, icons and focus indicators readable in both themes.

## Sidebar navigation

Use a persistent left sidebar around 15rem wide on desktop. Keep search and task-relevant filters above an independently scrolling link list; do not invent filters for short menus. Keep the current destination marked when visible in the filtered list, using `aria-current` and an accent-derived indicator.

At widths of 768px or less, use a left drawer no wider than 18rem and leave a tappable backdrop visible. The header menu button opens it. Provide an explicit close button; close on Escape, backdrop click, destination selection and a change to desktop layout. Trap focus while open, keep the background inactive, and restore focus to the trigger on dismissal. Prevent background scrolling while allowing the drawer to scroll.

Use normal links and retain usable navigation without JavaScript. Preserve useful search, filter and scroll state when updating content. See the working [navigation](../examples/navigation.html) and [documentation](../examples/documentation.html) examples.

Include a compact footer linking to the project's source and license without covering content. Serve assets locally. Standalone examples embed their styles and behavior; shared theme storage carries choices between pages on the same origin, subject to browser storage support.
