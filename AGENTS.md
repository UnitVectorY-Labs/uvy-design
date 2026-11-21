# Repository guidance

This repository holds human-readable brand and design guidance for UnitVectorY-Labs projects, together with a single embeddable stylesheet (`site/uvy.css`) and shell script (`site/uvy.js`). Keep it unversioned and framework-independent. Write current guidance, not rollout plans, release records or generated assets.

The documentation site rendered from this repository is the flagship reference implementation of UnitVectorY-Labs Design and must strictly obey every rule in the guide itself. Never introduce guide-only styling that contradicts the guidance. Do not use the abbreviation "UVY" in page titles, headers, headings, or user-facing references — always write "UnitVectorY-Labs" (reserving `uvy-` strictly for code identifiers, filenames and the repository slug).

When applying this design language to another UnitVectorY-Labs application, copy/embed `site/uvy.css`, `site/uvy.js`, the official logo assets in `assets/` as needed, and only the Tabler outline icons needed. Each application owns its implementation; preserve its purpose, data semantics and workflows.
