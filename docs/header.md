# Application header

Use this header as the common reference for UnitVectorY Labs application headers. Keep the application's own name, subtitle and navigation destinations. The [standalone header example](../examples/navigation.html) can be opened directly in a browser and contains the complete HTML, CSS and theme behavior.

- Use a full-width blue bar, with the content aligned to the same centered width and gutters as the page. Use a white, prominent application title and a short orange underline beneath it. A subtitle, when present, sits below the title in a light color with sufficient contrast.
- Place navigation and the theme control in the bar. Use links for destinations and identify the current page with `aria-current="page"` as well as a visible indicator. The theme control is a button with an accessible name that describes its action.
- On narrow screens, keep the title and theme control on the first row and put navigation on a separate row below them. Allow links and long titles to wrap; do not clip content or cause page-wide horizontal scrolling. A collapsible menu is appropriate when needed, provided its button has an accessible name and an accurate expanded state.
- Use visible focus indicators against blue. Navigation remains available without JavaScript. Start with the system color preference, remember an explicit choice when storage is available, and keep the interface usable when storage or JavaScript is unavailable.

A minimal structure follows; the example supplies the responsive styles and working theme toggle:

```html
<header class="site-header">
  <div class="header-inner">
    <div class="brand">
      <a href="/">Application name</a>
      <p>Optional subtitle</p>
    </div>
    <nav aria-label="Main navigation">
      <a href="/" aria-current="page">Home</a>
      <a href="/help">Help</a>
    </nav>
    <button type="button" class="theme-button" aria-label="Switch to dark theme">Theme</button>
  </div>
</header>
```

The example uses `#174b93` for the blue bar, white for the title and navigation, and `#ff932e` for the underline. Check contrast if adapting these colors. See [themes and navigation](themes-and-navigation.md) for broader behavior and [color](color.md) for other surface and text roles.
