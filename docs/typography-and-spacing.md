# Typography and spacing

Use IBM Plex Sans for body and headings, and IBM Plex Mono for code, technical labels and occasional title treatments. Self-host licensed font files in applications that use them; retain system sans-serif and monospace fallbacks. The standalone references use these stacks without external font requests and display installed Plex fonts when available.

| Element | Size | Weight |
| --- | --- | --- |
| H1 | 32px / 2rem | 600 |
| H2 | 24px / 1.5rem | 600 |
| H3 | 20px / 1.25rem | 600 |
| H4 | 16px / 1rem | 600 |
| Body | 16px / 1rem | 400 |
| Small text | 14px / .875rem | 400 |
| Technical label | 12px / .75rem | 500 |

Body line-height is 1.6; headings use approximately 1.25. Keep headings in primary text color. Use monospace selectively, without turning the interface into a terminal. Technical labels are brief secondary metadata, not essential instructions.

Use the spacing scale **4, 8, 12, 16, 24, 32, 48, 64px**, expressed in rem. Start with 16–24px panel padding, 8–12px control gaps and 32px between sections. Center page content within 1200px, with at least 16px side gutters. Articles should generally stay near 70 characters per line.

Interactive elements have 4px corners, panels 6px corners and borders are 1px solid. Omit shadows by default. Buttons and inputs are 36px high by default, using minimum heights so text can grow. Increase touch targets toward 44px on coarse pointers or add space between targets. Textareas grow with content.

At narrow widths, stack columns, wrap navigation and long titles, and scroll wide tables or code within their own regions. Preserve information and workflow. Check zoom at 200% and a 320px viewport.

See the [typography reference](../examples/typography.html).
