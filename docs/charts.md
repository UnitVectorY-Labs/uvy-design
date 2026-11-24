# Charts and graphs

Present time-series telemetry and operational breakdowns in flat `.uvy-panel` containers using fixed-width monospace axes and legends, hairline gridlines, crisp 2px strokes and paired summary figures. Keep plots calm, high-contrast and free of decorative gradients or overlapping spaghetti lines.

## Chart panel anatomy

Frame each graph inside a flat `.uvy-panel` so metrics, units and plotted trends scan as one cohesive unit:

- **Top header (`.uvy-chart-panel__top`).** Pair the monospace panel title (`15px`, semibold) on the left with a quiet, right-aligned monospace unit label (`.uvy-chart-unit`, `12px`, `--uvy-text-faint`) such as `Jobs`, `Seconds`, `Minutes` or `Percent`.
- **Headline KPI strip (`.uvy-chart-metrics`).** Place the period's headline figures directly above the plot in bold tabular monospace (`--uvy-font-mono`, `font-variant-numeric: tabular-nums`). When a panel plots two related series (such as `Job runs` with `Failed jobs`, or `Average` with `P95`), display both KPIs side by side with slim horizontal line swatches (`.uvy-swatch`, solid or `.uvy-swatch--dashed`) connecting each figure to its plotted line.
- **Plot region.** Render crisp `2px` lines over `1px` `--uvy-chart-grid` hairlines with `--uvy-chart-axis` monospace ticks (`11px`). Omit decorative area gradients, drop shadows and 3D effects.
- **Compact legend.** Use `12px` tabular monospace with slim horizontal bar markers (`12px × 3px` solid, or `2px` dashed for dashed series) rather than large square blocks. Omit placeholder colons and dashes (such as `Job runs: —`) when the pointer is not hovering a data point; display the series value cleanly on hover only. Keep hover crosshairs subtle (`1px dashed var(--uvy-border-emphasis)`).

## Color selection and contrast

Choose series colors by meaning first, then category:

| Series role | Recommended token | Stroke | Notes |
| --- | --- | --- | --- |
| Primary volume / neutral count | `--uvy-chart-1` | Solid (`2px`) | High contrast on light (`#2563EB`) and dark (`#60A5FA`) panels |
| Failures, errors, failure rate | `--uvy-danger` | Solid (`2px`) | Semantic error meaning; never use brand orange for errors |
| Execution duration, healthy throughput | `--uvy-ok` | Solid (`2px`) | Semantic healthy/duration series (`≥ 7:1` light and dark) |
| Queue wait, degraded latency | `--uvy-warn` | Solid (`2px`) | Semantic caution/wait series (`≥ 6.6:1` light and dark) |
| Secondary percentile / companion (P95) | `--uvy-chart-4` | Dashed (`[5, 3]`) | Pair color with a dashed stroke so it stays distinct without color |
| Additional categorical series | `--uvy-chart-2`, `--uvy-chart-5`, `--uvy-chart-6` | Solid or dashed | Reserve brand orange (`--uvy-accent`) for UI chrome, not chart palettes |

- **Never rely on color alone.** Pair companion statistical series (such as P95 alongside Average) with a dashed stroke (`[5, 3]` in canvas, `stroke-dasharray: 5 3` in SVG), explicit text labels and matching dashed swatches in both KPI headers and legends.
- **Verify KPI text contrast (`≥ 4.5:1`).** `--uvy-chart-1`, `--uvy-chart-4`, `--uvy-ok`, `--uvy-warn` and `--uvy-danger` all meet `≥ 4.5:1` contrast against `--uvy-surface` (`#FFFFFF` light / `#111827` dark) and may color headline KPI numerals directly. When using lighter categorical tokens (such as `--uvy-chart-2` or `--uvy-chart-3` in light mode), render the KPI numeral in `--uvy-text` and reserve the series color for the swatch and plotted line.

## Resolving `light-dark()` tokens for Canvas 2D

Canvas libraries (uPlot, Chart.js) cannot parse CSS `light-dark(...)` expressions directly, and `getComputedStyle(document.documentElement).getPropertyValue('--uvy-chart-1')` returns the literal `light-dark(...)` string rather than an `rgb(...)` color. Resolve tokens through a hidden probe element so the browser evaluates `color-scheme` and `data-theme` automatically:

```js
const probe = document.createElement("span");
probe.className = "sr-only";
probe.setAttribute("aria-hidden", "true");
document.body.append(probe);

function resolveColor(token) {
  probe.style.color = `var(${token})`;
  return getComputedStyle(probe).color;
}
```

Re-render canvas plots whenever the active theme or container width changes:

```js
new MutationObserver(renderCharts).observe(document.documentElement, {
  attributes: true,
  attributeFilter: ["data-theme"],
});
matchMedia("(prefers-color-scheme: dark)").addEventListener("change", renderCharts);
new ResizeObserver(renderCharts).observe(chartContainer);
```

Set canvas axis tick fonts from `--uvy-font-mono` (`11px ${monoFont}`) so plotted numbers match the fixed-width terminal chrome.

## Aggregate trends with aligned breakdown sparklines

When summarizing dozens or hundreds of repositories, workflows or runner types, **never plot every entity as an overlapping line on one chart**. Instead:

1. **Summarize at the top.** Render 2-column aggregate trend panels covering all matching records independently of breakdown search or pagination.
2. **Break down in a hairline list.** Place per-entity rows inside a single flat `.uvy-panel` separated by `1px solid var(--uvy-border)` hairlines, paired with search, sort and `.uvy-pagination` controls.
3. **Align compact inline SVG sparklines (`.uvy-sparkline`).** Give each entity row aligned metric columns showing the same series colors, dash patterns and bucket boundaries as the main charts:
   - Use a shared Y-axis scale per metric across all rows so magnitudes compare honestly by eye.
   - Align sparkline baselines across every column using a quiet `1px` `--uvy-border` rule (`.uvy-sparkline__baseline`).
   - Set `preserveAspectRatio="none"` and `vector-effect="non-scaling-stroke"` on `<polyline>` elements (`stroke-width="1.75"`, `stroke-linecap="round"`, `stroke-linejoin="round"`).
   - Keep zero-filled buckets and missing-sample gaps honest and consistent between aggregate graphs and mini sparklines.

## Accessibility and no-JS fallback

- Give every chart container and SVG sparkline `role="img"` with a concise, descriptive `aria-label` (for example, `aria-label="Queue time over time"`).
- Render headline KPI values and per-entity breakdown figures in server-rendered semantic HTML so all numeric summaries remain readable without JavaScript.
- Include a brief `<noscript>` hint beneath canvas chart grids explaining that trend charts require JavaScript while summary figures, filters and breakdowns remain available.

See the interactive [charts and graphs example](../examples/charts.html) for live theme-reactive canvas plots and aligned SVG breakdown sparklines.
