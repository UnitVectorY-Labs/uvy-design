# Themes and navigation

Follow the operating-system theme initially and respond to system changes while no override is set. The [header's sun/moon button](header.md) switches directly to the opposite theme and persists that choice where storage is available. “Use system theme” clears the override. Keep the page usable without storage or JavaScript; hide inactive controls.

The isolated [light](../examples/light.html) and [dark](../examples/dark.html) examples start in their named mode to make comparison predictable.

Use semantic color variables and `color-scheme` throughout. Apply saved preferences before painting where practical. Keep text, native controls, icons and focus indicators readable in both themes.

## Guide and example navigation

Keep documentation and examples in separate destinations. The guide sidebar contains only guide chapters in a stable conceptual order. Link from each chapter to the relevant full-page example; the Examples index lists isolated demonstrations. Examples do not inherit the guide sidebar. A sidebar inside a navigation or article example belongs only to that demonstration.

Avoid mixing guide chapters, sample pages and local anchors in one flat menu, reordering links between pages, or adding search/filter controls to a short menu. These patterns obscure where a link will take the reader.

## Application sidebars

Use a persistent left sidebar around 15rem wide on desktop. Keep search and task-relevant filters above an independently scrolling link list; do not invent filters for short menus. Keep the current destination marked when visible in the filtered list, using `aria-current` and an accent-derived indicator.

At widths of 768px or less, use a left drawer no wider than 18rem and leave a tappable backdrop visible. The header menu button opens it. Provide an explicit close button; close on Escape, backdrop click, destination selection and a change to desktop layout. Trap focus while open, keep the background inactive, and restore focus to the trigger on dismissal. Prevent background scrolling while allowing the drawer to scroll.

Use normal links and retain usable navigation without JavaScript. Preserve useful search, filter and scroll state when updating content. See the working [navigation](../examples/navigation.html) and [documentation](../examples/documentation.html) examples.

Use the shared [footer](footer.md) on static and dynamic pages. Serve assets locally. Standalone examples embed their styles and behavior; shared theme storage carries choices between pages on the same origin, subject to browser storage support.
