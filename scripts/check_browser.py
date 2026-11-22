"""Exercise standalone and published references with Chromium (optional QA dependency)."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import threading
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]


def check_layout(page):
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'Page overflow: {page.url}'
    assert page.locator('h1').count() == 1, page.url
    assert page.locator('.site-header .uvy-mark polygon').count() == 3, page.url
    assert page.locator('#theme svg:visible').count() == 1, page.url
    if page.viewport_size['width'] >= 768 and page.locator('#menu').count():
        assert page.locator('#menu').is_hidden(), f'#menu visible on desktop: {page.url}'
        assert page.locator('#menu-close').is_hidden(), f'#menu-close visible on desktop: {page.url}'
    assert page.locator('#theme-reset').count() == 0, f'Unexpected theme reset control: {page.url}'
    # Brand naming rule: never abbreviate UnitVectorY-Labs to UVY in titles or header brand.
    assert 'UVY' not in page.title(), f'Unexpected UVY in title: {page.title()} ({page.url})'
    brand_text = page.locator('.site-header .brand').inner_text()
    assert 'UVY' not in brand_text, f'Unexpected UVY in brand: {brand_text} ({page.url})'
    # The theme switch stays in the first header row at its right edge.
    assert page.evaluate("Math.abs(document.getElementById('theme').getBoundingClientRect().right-document.querySelector('.header-inner').getBoundingClientRect().right)<2"), page.url
    assert page.evaluate("document.getElementById('theme').getBoundingClientRect().top < document.querySelector('.header-inner').getBoundingClientRect().top+32"), page.url
    # Footer is always visible at the bottom of the viewport and compact.
    foot_rect = page.locator('.site-footer').evaluate("el => { const r = el.getBoundingClientRect(); return { top: r.top, bottom: r.bottom, height: r.height, vh: window.innerHeight }; }")
    assert foot_rect['top'] >= 0 and foot_rect['bottom'] <= foot_rect['vh'] + 2, f'Footer not visible in viewport: {foot_rect} ({page.url})'
    foot_text = page.locator('.site-footer').inner_text()
    assert 'UnitVectorY-Labs' in foot_text, page.url
    assert 'MIT License' in foot_text, page.url
    assert 'on GitHub' in foot_text, page.url
    assert 'Tabler' not in foot_text, page.url


def contrast_ratios(page, selector):
    return page.locator(selector).evaluate_all('''elements => {
      const ctx=document.createElement('canvas').getContext('2d');
      function rgb(color){ctx.clearRect(0,0,1,1);ctx.fillStyle=color;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data].slice(0,3);}
      function lum(color){return rgb(color).map(v=>v/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);}
      return elements.map(el=>{const style=getComputedStyle(el);const a=lum(style.color),b=lum(style.backgroundColor);return (Math.max(a,b)+.05)/(Math.min(a,b)+.05);});
    }''')


class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT / '_site'), **kwargs)

    def log_message(self, format, *args):
        pass


server = ThreadingHTTPServer(('127.0.0.1', 0), QuietHandler)
port = server.server_address[1]
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()

try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        errors = []
        layout_count = 0
        for theme in ['light', 'dark']:
            context = browser.new_context(color_scheme=theme)
            page = context.new_page()
            page.on('pageerror', lambda error: errors.append(str(error)))
            for folder in [ROOT / 'examples', ROOT / '_site/examples', ROOT / '_site/docs']:
                for file in folder.glob('*.html'):
                    for width in [320, 375, 1280]:
                        page.set_viewport_size({'width': width, 'height': 900})
                        page.goto(file.as_uri())
                        check_layout(page)
                        layout_count += 1
            page.goto((ROOT / 'examples/table-records.html').as_uri())
            assert min(contrast_ratios(page, 'td[data-value]:not([data-value=""]), .legend span')) >= 4.5
            page.goto((ROOT / 'examples/panels.html').as_uri())
            assert min(contrast_ratios(page, '.lifecycle-active .state, .lifecycle-inactive .state')) >= 4.5
            page.goto((ROOT / 'examples/components.html').as_uri())
            assert min(contrast_ratios(page, '.uvy-status, .uvy-button--primary')) >= 4.5
            context.close()

        # Verify cookie-based theme persistence over HTTP and forced light/dark examples.
        context = browser.new_context(viewport={'width': 1280, 'height': 900}, color_scheme='light')
        page = context.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        base = f'http://127.0.0.1:{port}'
        page.goto(f'{base}/index.html')
        page.locator('#theme').click()
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        cookies = {c['name']: c['value'] for c in context.cookies()}
        assert cookies.get('uvy-theme') == 'dark', cookies
        # Navigating to another doc page remembers dark mode via cookie.
        page.goto(f'{base}/docs/color.html')
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        # Visiting light.html forces light mode without overwriting the dark cookie.
        page.goto(f'{base}/examples/light.html')
        assert page.locator('html').get_attribute('data-theme') == 'light'
        page.goto(f'{base}/docs/icons.html')
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        # Switching back to light persists via cookie; dark.html still forces dark mode.
        page.locator('#theme').click()
        assert page.locator('html').get_attribute('data-theme') == 'light'
        assert {c['name']: c['value'] for c in context.cookies()}.get('uvy-theme') == 'light'
        page.goto(f'{base}/examples/dark.html')
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        page.goto(f'{base}/index.html')
        assert page.locator('html').get_attribute('data-theme') == 'light'

        # Verify reveal-on-scroll-up header behavior on a tall documentation page.
        page.goto(f'{base}/docs/color.html')
        page.evaluate("window.scrollTo(0, 600)")
        page.wait_for_timeout(250)
        assert 'is-hidden' in (page.locator('.site-header').get_attribute('class') or ''), 'Header should hide on scroll down'
        page.evaluate("window.scrollTo(0, 420)")
        page.wait_for_timeout(250)
        assert 'is-hidden' not in (page.locator('.site-header').get_attribute('class') or ''), 'Header should reveal on scroll up'
        assert page.locator('.site-header').evaluate("el => el.getBoundingClientRect().top") >= -1
        context.close()

        # Mobile drawer, forms, tables, topbar, tabs, copy, dialog, zoom.
        context = browser.new_context(viewport={'width': 375, 'height': 900}, color_scheme='light')
        page = context.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto((ROOT / 'examples/navigation.html').as_uri())
        page.locator('#menu').click()
        assert page.locator('#sidebar').get_attribute('aria-modal') == 'true'
        assert page.locator('#menu').get_attribute('aria-expanded') == 'true'
        page.locator('#menu-close').focus()
        page.keyboard.press('Shift+Tab')
        assert page.locator('#sidebar').evaluate('(el)=>el.contains(document.activeElement)')
        page.keyboard.press('Tab')
        assert page.locator('#menu-close').evaluate('(el)=>el===document.activeElement')
        page.keyboard.press('Escape')
        assert page.locator('#menu').evaluate('(el)=>el===document.activeElement')
        assert page.locator('#sidebar').evaluate('(el)=>el.inert')
        page.locator('#theme').click()
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        page.reload()
        assert page.locator('html').get_attribute('data-theme') == 'dark'
        page.locator('#theme').click()
        assert page.locator('html').get_attribute('data-theme') == 'light'
        page.locator('#menu').click()
        page.locator('#nav-search').fill('does-not-exist')
        assert page.locator('#nav-empty').is_visible()
        page.locator('#nav-search').fill('')
        page.locator('#nav-search').fill('Evidence')
        assert page.locator('#sidebar nav a:visible').count() == 1
        page.locator('#nav-search').fill('')
        page.locator('#menu-backdrop').click(position={'x': 350, 'y': 300})
        assert page.locator('#menu').get_attribute('aria-expanded') == 'false'
        page.locator('#menu').click()
        page.set_viewport_size({'width': 1280, 'height': 900})
        expect(page.locator('#menu-backdrop')).to_be_hidden()
        assert page.locator('#sidebar').evaluate('(el)=>!el.inert')
        assert page.locator('#theme').evaluate('(el)=>el===document.activeElement')
        page.set_viewport_size({'width': 375, 'height': 900})
        page.locator('#menu').click()
        page.locator('#sidebar nav a[href="#section-1"]').click()
        assert page.url.endswith('#section-1')
        assert page.locator('#sidebar').evaluate('(el)=>el.inert')

        # Top-bar navigation & search (no sidebar)
        page.goto((ROOT / 'examples/topbar.html').as_uri())
        assert page.locator('#sidebar').count() == 0
        page.locator('#topbar-search').fill('jwks')
        assert page.locator('#topbar-table tbody tr:visible').count() == 1
        page.locator('#topbar-clear').click()
        assert page.locator('#topbar-table tbody tr:visible').count() >= 4

        page.goto((ROOT / 'examples/forms.html').as_uri())
        page.locator('#domain').fill('invalid')
        page.get_by_role('button', name='Check domain').click()
        assert page.locator('#domain').get_attribute('aria-invalid') == 'true'
        page.locator('#domain').fill('example.com')
        page.get_by_role('button', name='Check domain').click()
        assert 'completed' in page.locator('#form-status').inner_text()
        page.get_by_role('button', name='Reset', exact=True).click()
        assert page.locator('#domain-error').is_hidden()

        page.goto((ROOT / 'examples/table.html').as_uri())
        assert page.locator('.table-wrap').first.evaluate('(el)=>el.scrollWidth>el.clientWidth')
        page.locator('#filter').fill('missing')
        assert page.locator('#empty').is_visible()
        page.locator('#clear').click()
        assert page.locator('[data-row]:visible').count() == 3
        page.locator('#density').select_option('compact')
        assert 'uvy-table--compact' in page.locator('#catalog').get_attribute('class')

        page.goto((ROOT / 'examples/table-records.html').as_uri())
        assert page.locator('[data-record]:visible').count() == 12
        assert page.locator('#records').get_attribute('role') == 'table'
        bounds = page.locator('[data-record]').first.evaluate('''row=>[...row.cells].map(cell=>{const r=cell.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width};})''')
        assert bounds[0]['width'] > bounds[2]['width'] * 2.8
        assert bounds[1]['width'] > bounds[2]['width'] * 2.8
        assert len({round(cell['y']) for cell in bounds[2:]}) == 1
        before = page.locator('[data-metric=age][data-value="240"]').get_attribute('style')
        page.locator('#sort').select_option('commits')
        page.locator('#direction').click()
        assert page.locator('[data-record]').first.locator('[data-metric=commits]').get_attribute('data-value') == '99'
        assert page.locator('[data-record]').last.locator('[data-metric=commits]').get_attribute('data-value') == ''
        page.locator('#repo-filter').fill('service-inventory')
        assert page.locator('[data-record]:visible').count() == 1
        assert page.locator('[data-metric=age][data-value="240"]').get_attribute('style') == before
        page.locator('#repo-filter').fill('missing')
        assert page.locator('#record-empty').is_visible()

        page.goto((ROOT / 'examples/utility.html').as_uri())
        page.get_by_role('button', name='Normalize', exact=True).click()
        assert page.locator('#result').inner_text() == 'catalog.example.com'
        copy_btn = page.get_by_role('button', name='Copy normalized identifier')
        copy_btn.click()
        expect(copy_btn).to_have_class(re.compile(r'\bis-copied\b'))

        page.goto((ROOT / 'examples/panels.html').as_uri())
        page.locator('#ev-tab-headers').focus()
        page.keyboard.press('ArrowRight')
        assert page.locator('#ev-tab-json').get_attribute('aria-selected') == 'true'
        assert page.locator('#ev-panel-json').is_visible()
        assert page.locator('#ev-panel-headers').is_hidden()

        page.goto((ROOT / 'examples/utility.html').as_uri())
        page.set_viewport_size({'width': 640, 'height': 900})
        page.evaluate("document.documentElement.style.fontSize='200%'")
        check_layout(page)

        page.goto((ROOT / '_site/docs/color.html').as_uri())
        assert page.locator('.color-swatch:visible').count() >= 22
        assert page.locator('.color-swatch').first.evaluate("el=>getComputedStyle(el).backgroundColor") != 'rgba(0, 0, 0, 0)'
        guide_links = page.locator('#sidebar nav a').evaluate_all('links=>links.map(link=>link.getAttribute("href"))')
        assert all('examples/' not in link for link in guide_links)
        page.goto((ROOT / '_site/docs/footer.html').as_uri())
        assert page.locator('#sidebar nav a').evaluate_all('links=>links.map(link=>link.getAttribute("href"))') == guide_links

        page.goto((ROOT / '_site/docs/logo.html').as_uri())
        assert page.locator('.logo-stage img').count() == 4
        assert all(page.locator('.logo-stage img').evaluate_all('imgs=>imgs.map(img=>img.complete && img.naturalWidth>0)'))

        page.goto((ROOT / 'examples/logo.html').as_uri())
        assert page.locator('.logo-stage img').count() == 4
        assert all(page.locator('.logo-stage img').evaluate_all('imgs=>imgs.map(img=>img.complete && img.naturalWidth>0)'))
        page.locator('#avatar-variant-light').click()
        assert 'uvy-avatar-light.svg' in page.locator('.logo-frames img').first.get_attribute('src')
        page.locator('#avatar-variant-dark').click()
        assert 'uvy-avatar-dark.svg' in page.locator('.logo-frames img').first.get_attribute('src')

        page.goto((ROOT / 'examples/index.html').as_uri())
        assert page.locator('#sidebar').count() == 0
        assert page.locator('.example-link').count() == 20

        # Hovering the header logo must never alter any polygon color.
        page.set_viewport_size({'width': 1280, 'height': 900})
        page.goto((ROOT / 'examples/landing.html').as_uri())
        def logo_colors():
            return page.evaluate("""() => [...document.querySelectorAll('.site-header .uvy-mark polygon')].map(el => {
              const s = getComputedStyle(el); return [s.fill, s.stroke];
            })""")
        before_hover = logo_colors()
        page.locator('.site-header .brand').hover()
        page.wait_for_timeout(150)
        assert logo_colors() == before_hover, f'Logo colors changed on hover: {before_hover} -> {logo_colors()}'

        # Fixed-width monospace voice on headings & buttons, sans on body paragraphs.
        h1_font = page.locator('h1').evaluate('el => getComputedStyle(el).fontFamily')
        p_font = page.locator('p.uvy-lead').evaluate('el => getComputedStyle(el).fontFamily')
        assert 'mono' in h1_font.lower() or 'menlo' in h1_font.lower() or 'consolas' in h1_font.lower() or 'courier' in h1_font.lower(), h1_font
        assert h1_font != p_font, (h1_font, p_font)

        # Dedicated footer variant pages and compact height.
        page.goto((ROOT / 'examples/footer.html').as_uri())
        assert page.locator('.site-footer .version').count() == 0
        assert page.locator('.site-footer .footer-meta').count() == 0
        assert page.locator('.site-footer').bounding_box()['height'] <= 52

        page.goto((ROOT / 'examples/footer-repositories.html').as_uri())
        assert 'jwks-catalog' in page.locator('.site-footer').inner_text()
        assert 'jwks-observer' in page.locator('.site-footer').inner_text()

        page.goto((ROOT / 'examples/footer-updated.html').as_uri())
        assert 'Last updated:' in page.locator('.site-footer .footer-meta').inner_text()
        assert page.locator('.site-footer .footer-meta time').count() == 1
        assert page.locator('.site-footer').bounding_box()['height'] <= 72

        page.goto((ROOT / 'examples/footer-version.html').as_uri())
        assert 'Version v1.4.2' in page.locator('.site-footer .version').inner_text()
        assert page.locator('.site-footer').bounding_box()['height'] <= 72

        page.set_viewport_size({'width': 375, 'height': 900})

        page.goto((ROOT / 'examples/application.html').as_uri())
        page.locator('#run-repository').select_option('observer')
        assert page.locator('.run-card').count() == 1
        page.locator('.run-card').click()
        assert page.locator('#run-detail').is_visible()
        page.keyboard.press('Escape')
        assert page.locator('#run-detail').is_hidden()
        page.locator('#run-refresh').click()
        expect(page.locator('#run-status')).to_have_text('Sample updated.')
        assert page.locator('#run-repository').input_value() == 'observer'
        context.close()

        # No-JS fallback
        context = browser.new_context(java_script_enabled=False, color_scheme='dark', viewport={'width': 320, 'height': 900})
        page = context.new_page()
        for file in [ROOT / '_site/index.html', *list((ROOT / 'examples').glob('*.html'))]:
            page.goto(file.as_uri())
            assert page.locator('h1').count() == 1
            assert page.locator('#theme').is_hidden()
            assert not page.evaluate('document.documentElement.scrollWidth>innerWidth'), file
            if page.locator('#sidebar').count():
                assert page.locator('#sidebar').is_visible()
                assert page.locator('#menu').is_hidden()
        context.close()

        # Storage-unavailable fallback
        context = browser.new_context()
        context.add_init_script("Storage.prototype.getItem=function(){throw Error('Storage unavailable')};Storage.prototype.setItem=function(){throw Error('Storage unavailable')};Storage.prototype.removeItem=function(){throw Error('Storage unavailable')};")
        page = context.new_page()
        page.goto((ROOT / 'examples/navigation.html').as_uri())
        page.locator('#theme').click()
        assert page.locator('html').get_attribute('data-theme') in ['light', 'dark']
        context.close()

        assert not errors, errors
        browser.close()
        print(f'Passed {layout_count} theme/viewport layouts; cookie themes, forced examples, topbar + sidebar search, icons, header/footer, drawer, forms, tables, contrast, zoom and fallbacks')
finally:
    server.shutdown()
