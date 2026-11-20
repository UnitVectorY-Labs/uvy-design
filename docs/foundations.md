# Foundations

Unit Vector Y Labs interfaces are minimal, precise, functional and visually consistent. Their character comes from modern engineering software and traditional technical publications: clear hierarchy, careful spacing and readable information.

- Use flat surfaces without decorative gradients.
- Reserve orange for primary actions, selected navigation and important interactive states.
- Prefer thin neutral borders to shadows; omit shadows by default.
- Use square or slightly rounded components.
- Prefer semantic HTML and native CSS. No shared JavaScript framework is required.
- Treat light and dark modes as equally important.

Each application leads with its own product identity and keeps its purpose, data semantics and workflows. Preserve fields, actions, navigation and meaningful visualization colors. Do not hide useful information behind new tabs or disclosures for appearance alone.

This repository is an unversioned, human-readable reference, not a distributed CSS package. Applications own their implementation and dependencies. Copy and adapt the example patterns; use semantic variables and namespaced classes such as `uvy-button`, `uvy-card` and `uvy-table--compact` where reusable variants help. Go templates, HTMX, Jekyll and static HTML can use the same visual rules. Project-specific styling should reuse the tokens wherever practical.

See [page archetypes](page-archetypes.md), the [component catalog](../examples/components.html) and the [review checklist](review.md).
