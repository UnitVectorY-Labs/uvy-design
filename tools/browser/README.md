# Optional browser review tools

These development-only tools require Node.js, Playwright Chromium and its platform libraries. They are not included in the generated website and are not consumer dependencies.

From this directory:

```sh
npm ci
npx playwright install --with-deps chromium
```

The browser dependency installer may require system privileges. On the research host, missing Linux libraries and DejaVu/Noto Emoji fonts were instead downloaded/extracted into `/tmp` without modifying system packages. That host-specific setup is not a product dependency.

From the repository root, generate and serve the specimens as documented in README. Then, from this directory:

```sh
npm run check
```

This refreshes `research/prototype-qa.json` and specimen screenshots, so inspect the diff. It checks selected behavior, source-derived three-cell mobile metrics and original heat colors, top-right binary theme toggle, footer links and token contrast; it is not a complete accessibility or HTMX test suite. `npm run capture` visits the public live sites, refreshes current screenshots and capture manifests, and should only be run when a new baseline is wanted. Record a capture date with each run.

## Release asset checks

Run `python3 scripts/package-release.py` from the repo root, serve the repository root on localhost:8766, then run `node tools/browser/release-check.cjs`. The checker creates an ignored output fixture and tests the actual distributable controller/tokens, including delegated post-swap toggles and package hashes.
