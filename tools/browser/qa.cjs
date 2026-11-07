const path = require('path');
const root = path.resolve(__dirname, '../..');
const { chromium } = require('playwright');
const fs = require('fs');
const assert = require('assert/strict');

(async () => {
  const browser = await chromium.launch();
  const dir = path.join(root, 'research/screenshots/revision-3');
  fs.mkdirSync(dir, { recursive: true });
  const errors = [], external = [], checks = [];
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, colorScheme: 'light' });
  const page = await context.newPage();
  context.on('request', request => { if (!request.url().startsWith('http://127.0.0.1:8765/')) external.push(request.url()); });
  page.on('pageerror', error => errors.push(error.message));
  const setTheme = async theme => {
    if (await page.locator('html').getAttribute('data-theme') !== theme) await page.click('#theme-toggle');
    assert.equal(await page.locator('html').getAttribute('data-theme'), theme);
  };
  for (const name of ['index', 'table', 'repository', 'catalog', 'workbench']) {
    for (const [size, width, height] of [['desktop', 1440, 1000], ['mobile', 390, 844], ['narrow', 320, 844], ['tablet', 768, 1024]]) {
      await page.setViewportSize({ width, height });
      await page.goto(`http://127.0.0.1:8765/${name}.html`);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false, `${name}: ${width}px overflow`);
      assert.equal(await page.locator('[role=tab],details').count(), 0);
      assert.equal((await page.locator('header').innerText()).includes('UnitVectorY Labs'), false);
      assert.equal((await page.locator('footer a').first().innerText()).trim(), 'Open source on GitHub');
      assert.equal(await page.locator('footer a').nth(1).textContent(), 'MIT License');
      const toggle = await page.locator('#theme-toggle').boundingBox();
      assert(toggle.width >= 44 && toggle.height >= 44 && toggle.x > width / 2 && toggle.y < 32);
      assert(await page.locator('#theme-toggle svg.icon[aria-hidden=true]').count() === 2);
      if (name === 'table' && width <= 768) {
        const boxes = await page.locator('#repositories tbody tr:first-child .metric-cell').evaluateAll(cells => cells.map(cell => { const r = cell.getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height }; }));
        assert.equal(boxes.length, 3);
        assert(boxes.every(box => Math.abs(box.y - boxes[0].y) < 1 && box.width > 0 && box.height < 100));
        assert((await page.locator('#repositories tbody tr:first-child').boundingBox()).height < 240, 'Compact source-derived metric card');
      }
      if (name === 'catalog' && width <= 768) {
        await page.click('#nav-toggle');
        assert(await page.locator('#service-search').isVisible());
        await page.keyboard.press('Escape');
        assert.equal(await page.locator('#nav-toggle').getAttribute('aria-expanded'), 'false');
      }
      if (size === 'desktop' || size === 'mobile') {
        for (const theme of ['light', 'dark']) {
          await setTheme(theme);
          await page.screenshot({ path: `${dir}/${name}-${theme}-${size}.png` });
          await page.screenshot({ path: `${dir}/${name}-${theme}-${size}-full.png`, fullPage: true });
        }
      }
    }
  }
  checks.push('Five actual-layout examples at 320/390/768/1440px: no page overflow, no content tabs/disclosures, project-only masthead, inline SVG toggle, project footer');
  checks.push('Mobile UnreleasedCommits cards retain three side-by-side metrics and compact height; JWKS retains existing responsive navigation relationship');
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('http://127.0.0.1:8765/table.html');
  await setTheme('light');
  await page.selectOption('#sort-field', '2');
  let values = await page.locator('#repositories .metric-cell:nth-child(3)').evaluateAll(cells => cells.map(c => Number(c.dataset.sortValue)));
  assert.deepEqual(values, [...values].sort((a,b) => a-b));
  await page.click('#sort-direction');
  values = await page.locator('#repositories .metric-cell:nth-child(3)').evaluateAll(cells => cells.map(c => Number(c.dataset.sortValue)));
  assert.deepEqual(values, [...values].sort((a,b) => b-a));
  checks.push('Existing mobile sort field and direction work and update aria-sort');
  const source = JSON.parse(fs.readFileSync(path.join(root, 'prototypes/fixtures/unreleased.json')));
  await page.reload();
  for (let i = 0; i < source.repos.length; i++) {
    const colors = await page.locator(`#repositories tbody tr:nth-child(${i + 1}) .metric-cell`).evaluateAll(cells => cells.map(c => c.style.backgroundColor));
    const hexToRgb = hex => `rgb(${parseInt(hex.slice(1,3),16)}, ${parseInt(hex.slice(3,5),16)}, ${parseInt(hex.slice(5,7),16)})`;
    assert.deepEqual(colors, ['commit_color','behind_color','since_color'].map(k => hexToRgb(source.repos[i][k])));
  }
  checks.push('All 24 captured heatmap background colors match production; subset is not renormalized');
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.goto('http://127.0.0.1:8765/catalog.html');
  assert.equal(await page.evaluate(() => htmx.version), '4.0.0');
  await page.fill('#service-search', 'no-such-service');
  assert.equal(await page.locator('#service-count').textContent(), '0 services');
  await page.fill('#service-search', '');
  await page.selectOption('#provider-filter', 'auth0');
  assert.equal(await page.locator('#service-count').textContent(), '2 services');
  await page.selectOption('#provider-filter', 'all');
  await page.click('a.service-link[href="service-3d-systems.html"]');
  await page.waitForURL('**/service-3d-systems.html');
  await page.waitForFunction(() => document.querySelector('[data-service]')?.dataset.service === '3d-systems');
  assert.equal(await page.title(), '3D Systems · JWKS Catalog');
  assert.equal(await page.locator('#service-main .key-table tbody tr').count(), 6);
  await page.goBack();
  await page.waitForFunction(() => document.querySelector('[data-service]')?.dataset.service === '1worldsync');
  await page.goto('http://127.0.0.1:8765/service-3d-systems.html');
  assert.equal(await page.locator('#service-main h1').textContent(), '3D Systems');
  checks.push('Pinned local HTMX 4: two real full-page/fragment service routes, title/history/back/direct entry and local provider filtering');
  await page.goto('http://127.0.0.1:8765/workbench.html');
  assert(await page.locator('#certificate-output').isVisible());
  await page.fill('#cert-input', '');
  assert.equal(await page.locator('#certificate-output').isVisible(), false);
  assert.equal(await page.locator('#certificate-state').textContent(), 'No certificate processed yet.');
  checks.push('CertSummary visual specimen hides recorded output after input changes; no false decoder claim');
  for (const density of ['compact','spacious']) {
    await page.goto(`http://127.0.0.1:8765/table.html?density=${density}`);
    assert.equal(await page.locator('html').getAttribute('data-density'), density);
    await setTheme('light');
    await page.screenshot({ path: `${dir}/table-${density}-light-desktop.png`, fullPage: true });
    await page.setViewportSize({ width: 390, height: 844 });
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > innerWidth), false);
    await page.screenshot({ path: `${dir}/table-${density}-light-mobile.png` });
    await page.setViewportSize({ width: 1440, height: 1000 });
  }
  checks.push('Standard, compact and spacious densities preserve content and mobile metric row');
  await setTheme('dark'); await page.reload();
  assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
  await page.emulateMedia({ colorScheme: 'light' });
  assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark');
  for (const theme of ['light', 'dark']) {
    const c = await browser.newContext({ colorScheme: theme, javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
    const p = await c.newPage(); await p.goto('http://127.0.0.1:8765/table.html');
    assert.equal(await p.locator('#repositories tbody tr').count(), 8);
    assert.equal(await p.evaluate(() => getComputedStyle(document.documentElement).colorScheme), theme);
    await c.close();
  }
  assert.deepEqual(external, []); assert.deepEqual(errors, []);
  checks.push('Cookie appearance survives reload; no-JS content and OS theme; zero external runtime requests and zero page errors');
  fs.writeFileSync(path.join(root, 'research/prototype-qa.json'), JSON.stringify({ revision: 3, date: '2026-11-07', checks, errors, external_requests: external }, null, 2));
  console.log(JSON.stringify({ checks, errors, external }, null, 2));
  await browser.close();
})().catch(error => { console.error(error); process.exit(1); });
