# Scope

This repository is the versioned design standards source for standalone UnitVectorY-Labs website projects. It holds standards, vendorable assets and review specimens — not application code, decision logs or rollout tracking. Consumer applications adopt the standards through their own pull requests; do not merge or deploy them without explicit instruction. All guidance and examples preserve app layout/navigation/workflows/data semantics.

Keep the prototype stack Go standard-library static generation, plain CSS and minimal JavaScript. Preserve framework-independent assets for sites that do not use Go or HTMX. Do not add a frontend runtime framework or required remote assets.

Write documentation as current standards, not history: state rules and contracts, not approval narratives, revision logs or rollout tracking. Label fixture data and incomplete behavior honestly. Do not claim accessibility compliance based only on screenshots or automated checks.

Run `go run ./cmd/previewgen` after prototype edits. Use the documented browser review tooling when changing interactive behavior. Do not deploy specimens. Consumer PRs carry their own before/after desktop/mobile light/dark major-page evidence; screenshots attach to the consumer pull request and are never committed to a source tree.
