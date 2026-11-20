# Page archetypes

All archetypes share the [universal header](header.md), [footer](footer.md), tokens and component treatment. Choose a layout based on the task; do not add a hero to every page.

| Archetype | Hero | Main layout | Reference |
| --- | --- | --- | --- |
| Project landing page | Compact | Centered, max 1200px | [Landing](../examples/landing.html) |
| Documentation landing page | None | Sidebar and article index | [Guide](foundations.md) |
| Documentation article | None | Sidebar, article, optional contents | [Article](../examples/documentation.html) |
| Static detail page | None | Readable summaries, panels and evidence tables | [Key details](../examples/panels.html) |
| Dynamic application | None | Task controls, current state and results | [Application workspace](../examples/application.html), [repository metrics](../examples/table-records.html) |
| Internal utility | None | Compact, task-focused | [Utility](../examples/utility.html) |
| Design system reference | None | Component catalog | [Examples index](../examples/index.html) |

A hero is reserved for a project landing page where it explains the product's purpose. Use a prominent H1, a short description and optionally one primary action. Decorative illustrations are unnecessary. Below it, show concrete capabilities and a clear route into the product or documentation.

Static articles and detail pages contain their meaningful content and links in the initial HTML. Search and theme controls may enhance them without making reading depend on JavaScript. Dynamic applications keep task controls close to changing results, show loading/empty/error states near the affected region, announce updates and preserve filter and focus state. Use dialogs for actual details, not to conceal ordinary article content. Utility pages keep input, action and output close together. Preserve meaningful existing layouts when adopting the visual rules.
