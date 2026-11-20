"""Exercise standalone and published references with Chromium (optional QA dependency)."""
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]


def check_layout(page):
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), f'Page overflow: {page.url}'
    assert page.locator('h1').count() == 1, page.url
    assert page.locator('#theme svg:visible').count() == 1, page.url
    # Theme switch must precede the independent identity link.
    assert page.evaluate("document.getElementById('theme').getBoundingClientRect().right <= document.querySelector('.brand').getBoundingClientRect().left"), page.url


def contrast_ratios(page, selector):
    return page.locator(selector).evaluate_all('''elements => {
      const ctx=document.createElement('canvas').getContext('2d');
      function rgb(color){ctx.clearRect(0,0,1,1);ctx.fillStyle=color;ctx.fillRect(0,0,1,1);return [...ctx.getImageData(0,0,1,1).data].slice(0,3);}
      function lum(color){return rgb(color).map(v=>v/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4).reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);}
      return elements.map(el=>{const style=getComputedStyle(el);const a=lum(style.color),b=lum(style.backgroundColor);return (Math.max(a,b)+.05)/(Math.min(a,b)+.05);});
    }''')


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
        context.close()

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
    page.locator('#menu').click()
    page.locator('#theme-reset').click()
    assert page.locator('html').get_attribute('data-theme') is None
    assert page.locator('#sidebar').get_attribute('data-open') is None
    assert page.locator('#theme').evaluate('(el)=>el===document.activeElement')
    page.emulate_media(color_scheme='dark')
    expect(page.locator('#theme')).to_have_attribute('aria-label', 'Switch to light theme')
    page.locator('#menu').click()
    page.locator('#nav-search').fill('does-not-exist')
    assert page.locator('#nav-empty').is_visible()
    page.locator('#nav-search').fill('')
    page.locator('#nav-group').select_option('guide')
    assert page.locator('#sidebar nav a:visible').count() == 2
    page.locator('#nav-group').select_option('all')
    page.locator('#menu-backdrop').click(position={'x': 350, 'y': 300})
    assert page.locator('#menu').get_attribute('aria-expanded') == 'false'
    page.locator('#menu').click()
    page.set_viewport_size({'width': 1280, 'height': 900})
    expect(page.locator('#menu-backdrop')).to_be_hidden()
    assert page.locator('#sidebar').evaluate('(el)=>!el.inert')
    assert page.locator('#theme').evaluate('(el)=>el===document.activeElement')
    page.set_viewport_size({'width': 375, 'height': 900})
    page.locator('#menu').click()
    page.locator('#sidebar nav a[href="forms.html"]').click()
    assert page.url.endswith('forms.html')
    assert page.locator('#sidebar').evaluate('(el)=>el.inert')
    page.locator('#domain').fill('invalid')
    page.get_by_role('button', name='Check domain').click()
    assert page.locator('#domain').get_attribute('aria-invalid') == 'true'
    page.locator('#domain').fill('example.com')
    page.get_by_role('button', name='Check domain').click()
    assert 'completed' in page.locator('#form-status').inner_text()
    page.get_by_role('button', name='Reset', exact=True).click()
    assert page.locator('#domain-error').is_hidden()
    page.goto((ROOT / 'examples/panels.html').as_uri())
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
    page.get_by_role('button', name='Normalize').click()
    assert page.locator('#result').inner_text() == 'catalog.example.com'
    page.set_viewport_size({'width': 640, 'height': 900})
    page.evaluate("document.documentElement.style.fontSize='200%'")
    check_layout(page)
    context.close()

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

    context = browser.new_context()
    context.add_init_script("Storage.prototype.getItem=function(){throw Error('Storage unavailable')};Storage.prototype.setItem=function(){throw Error('Storage unavailable')};Storage.prototype.removeItem=function(){throw Error('Storage unavailable')};")
    page = context.new_page()
    page.goto((ROOT / 'examples/navigation.html').as_uri())
    page.locator('#theme').click()
    assert page.locator('html').get_attribute('data-theme') in ['light', 'dark']
    context.close()
    assert not errors, errors
    browser.close()
    print(f'Passed {layout_count} theme/viewport layouts; drawer, keyboard, themes, forms, tables, sorting, contrast, zoom, no-JS and blocked-storage checks')
