# Theme and interaction contract — v0.1.0

This contract standardizes theme and interaction behavior across applications: existing application structure and navigation are preserved, normal data stays visible, runtime assets are self-contained, and the theme/footer behavior below is normative. Application compliance is verified through per-application pull request review.

This contract standardizes behavior within existing layouts. It does not authorize new tabs, disclosures, navigation, sections or workflows. Keep existing sorting, filters, URLs and field relationships.

## Appearance preference

Provide a simple binary light/dark button at the top right of the project masthead. There is no System selector or additional reset control. Give the button an accessible name that describes its action, such as “Switch to dark mode” or “Switch to light mode”, and a clear visible focus state. Any sun/moon icon is supplemental to that name.

On first visit, with no valid saved override, use the system preference. CSS `prefers-color-scheme` provides the no-JavaScript baseline. An early small script reads a valid light/dark cookie, otherwise resolves the current system preference, and sets `data-theme="light"` or `data-theme="dark"` on the document root before styles paint. Track system changes while no explicit override exists. Templates and data are shared between modes.

The first toggle chooses the opposite of the currently displayed appearance and saves an explicit preference. Further toggles alternate light/dark. Store the preference in a host-only cookie named `uvy-theme`, with value `light` or `dark`, `Path=/`, `SameSite=Lax`, `Max-Age=31536000`, and `Secure` on HTTPS. Omit Domain. Do not refresh persistence merely because someone visits. Ignore invalid values and handle unavailable cookie storage without breaking the page; the current-page toggle can still work.

Resetting to system behavior means clearing this site's `uvy-theme` cookie and reloading. Document that behavior for maintainers; do not add a reset option to the site UI. Once an explicit preference exists, later OS changes do not override it. Without JavaScript the static page follows CSS system preference and hides the inactive toggle; it cannot inspect its cookie without script.

A host-only cookie applies to the current site. The projects span `unitvectorylabs.com` and `unitvectory-labs.net`; one cookie cannot cover those unrelated registrable domains. Each standalone project remembers its own choice. Do not introduce cross-site preference synchronization.

Keep root appearance outside HTMX swap targets and set `color-scheme` for native controls. Honor `prefers-reduced-motion`; do not animate the whole document during theme changes.

## Static output and Go templates

A static catalog emits a complete document for every canonical route. The same Go template partial renders the content inside that page and the corresponding HTML fragment. A fragment is an alternate representation, never the only way to reach the content. Link href values point to full pages. HTMX attributes may request a generated fragment and push the canonical full-page URL.

A shared base provides document metadata, assets, masthead and footer. Content partials own the page-specific heading and data. Fragment boundaries and stable IDs are documented; nested duplicate IDs are not permitted. Keep template escaping enabled, including technical values supplied by data sources.

Versioned plain CSS, a small appearance script and documented HTML/Go-template examples are sufficient for a first distribution. All runtime assets are self-contained. Ship pinned HTMX locally, alongside local CSS and behavior scripts; embed assets in Go-served applications and include them in generated static output. Use system fonts and selected Tabler icons as inline SVG only. No CDN scripts/styles, remote fonts, icon fonts, emoji stand-ins or required Tabler/Bootstrap runtime. Avoid a mandatory JavaScript component runtime or a new backend. An optional Go embed package can be considered after the shared patterns prove useful.

## Enhancement and navigation

Ordinary links must open correct pages with JavaScript disabled, support new-tab/open-link actions and expose canonical URLs. A live Go form provides a normal method/action and can render a complete response. HTMX supplies fragment updates, never a second implementation of content or validation.

For a static catalog, a search/filter that needs browser-side data must be described honestly. Prefer a small client-side index where appropriate, with usable browse pages and explicit no-script guidance; HTMX cannot invent a server search endpoint on a static host. If a GET route is supported, keep query/filter/pagination state in its URL. Do not imply a static form works without JS when no generated or server route handles it.

After a navigation swap, update the document title, place focus on the new page heading or main region as appropriate, and make the result understandable to a screen reader. Back/forward must restore the content and URL consistently. Do not reset appearance or attach duplicate listeners after swaps. Use event names and event-detail shapes documented for the pinned HTMX version: v2 examples use `htmx:beforeRequest`/`htmx:afterSwap`, while the audited HTMX 4 bundle emits names including `htmx:before:request`/`htmx:after:swap`. Do not treat these as interchangeable or change hooks based only on v2 documentation. Verify the pinned version and scope initialization to the inserted content; prefer event delegation where practical.

## Shared states and controls

Every input needs a persistent label; placeholder is an example, not its accessible name. Help and validation text are associated with the field. Buttons retain an accessible name when responsive layouts hide visible text. Use native links, buttons and selects rather than clickable div elements. Preserve each application’s navigation and filters on mobile. Adjust spacing and wrapping within its existing structure; do not invent replacement navigation.

Identify the updating region as busy during a request; expose a concise loading status. Preserve useful existing content while an update is pending unless clearing it is necessary to prevent a misleading result. Announce completion or result count through a restrained polite status region. Errors explain what failed and give a specific retry or correction; they must remain visible without relying on color.

Use one owner for each loading/error state. Disable duplicate submission only while needed, then restore it after success, HTTP error, network failure or cancellation. A failed enhancement must leave a normal canonical link or retry available.

Keep ordinary fields and content visible. Native details/summary is allowed only when the task warrants hiding secondary content and that specific use is reviewed separately. Do not add a disclosure or tab as part of style-guide adoption. Existing specialized tabs require the complete keyboard and ARIA pattern: tablist, labeled tabpanels, controls/label relationships, selected state, roving tabindex and arrow/Home/End navigation. Do not add tab roles to plain independent buttons.

Copy actions report success and failure accessibly. Preserve exact copied values while permitting a display format. Long code, URLs and identifiers must not create page-wide horizontal scrolling; use local overflow, wrapping or a clearly labeled expanded view.

## Acceptance checks for a pilot

- First visit follows OS light and OS dark with no stored override; the no-JS CSS baseline also follows the OS.
- The top-right binary toggle switches the resolved appearance and saves Light or Dark after the first interaction; it persists after reload, canonical navigation and HTMX swaps. No System selector or reset UI appears.
- Without an override, later OS changes apply. With an explicit override they do not. Clearing the host cookie and reloading restores first-visit system behavior.
- Invalid/blocked cookies leave a functional page. Inspect cookie scope/attributes on HTTPS; no cross-domain synchronization is assumed.
- Direct detail URLs, browser back/forward and open-in-new-tab work; the title and focus reflect the current view.
- Full page and fragment show the same content. Static search behavior and its no-JS fallback are tested as implemented.
- Loading, zero results, validation, network error, server error and retry are understandable with keyboard and screen reader.
- Tab, Shift+Tab, Enter and Space work for controls; specialized tabs also support their documented navigation keys.
- At 320px width and 200% zoom, existing navigation, filters and all fields remain available without page-wide overflow. UnreleasedCommits follows its existing title/release card plus three side-by-side metric cells with small labels; preserve its sorting and green–yellow–red mapping. Other applications retain their own established responsive structure.
- Ordinary content remains visible. No new tabs, disclosures or rearranged application sections appear. JWKS explorer, UnreleasedCommits index/detail and CertSummary workspace retain their source layouts.
- Standard, compact and spacious densities change spacing only; no density hides fields, actions or navigation. Subtle shadows and modest corners do not replace existing structure.
- UnreleasedCommits metric values, thresholds and green–yellow–red direction match the original application, with readable foregrounds in both themes.
- The standalone project masthead has no UnitVectorY-Labs branding, decorative subtitle or eyebrow. The compact footer links to that project GitHub repository and MIT license, reaches the bottom through flex layout, and never overlays content.
- Text, control boundaries, status and focus meet contrast requirements in both themes. Reduced motion is respected.
- Disable external network access after loading the local application: its local CSS, scripts, pinned HTMX, system fonts and inline Tabler SVG still render and work. No new client framework or remote runtime asset is introduced.
