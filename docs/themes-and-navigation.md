# Themes and navigation

Every site supports light and dark modes. Without an explicit choice, follow the operating system preference, including changes made while the page is open. Manual selection overrides the system and persists where storage is available. Provide a System option to clear the override.

Use semantic variables for every component color. Set `color-scheme` so native controls match the theme. Apply stored preferences early to reduce flashes. Catch storage failures and keep the page functional without storage or JavaScript. Show theme controls only when their behavior is available.

Keep the [universal header](header.md) consistent across page archetypes. Use real links for destinations and buttons for actions. Selected navigation has a visible cue and `aria-current`. Documentation sidebars retain clear article labels and collapse naturally into a stacked layout on narrow screens.

Include a compact footer with the project's source and license. It must never cover content. Serve interface assets locally; font fallbacks keep text readable offline.

All [examples](../examples/components.html) contain their own CSS and theme behavior. Their shared preference key lets a choice carry across pages on the same origin; direct-file storage behavior depends on the browser.
