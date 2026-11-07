const path = require('path');
const root = path.resolve(__dirname, '../..');
const { chromium } = require('playwright');
const fs = require('fs');
const luminance = hex => {
  let raw = hex.trim().slice(1);
  if (raw.length === 3) raw = raw.split('').map(x => x+x).join('');
  const [r,g,b] = raw.match(/../g).map(x => parseInt(x,16)/255).map(x => x <= .04045 ? x/12.92 : ((x+.055)/1.055)**2.4);
  return .2126*r + .7152*g + .0722*b;
};
const contrast = (a,b) => (Math.max(luminance(a),luminance(b))+.05)/(Math.min(luminance(a),luminance(b))+.05);
const hex = rgb => '#'+rgb.match(/\d+/g).slice(0,3).map(n => Number(n).toString(16).padStart(2,'0')).join('');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('http://127.0.0.1:8765/table.html');
  const report=[];
  for (const theme of ['light','dark']) {
    if (await page.locator('html').getAttribute('data-theme') !== theme) await page.click('#theme-toggle');
    const tokens = await page.evaluate(() => {
      const s = getComputedStyle(document.documentElement);
      return Object.fromEntries(['bg','surface','text','muted','blue','orange','orange-soft','focus','control','success','success-soft','masthead','orange-fill','orange-ink','section'].map(k => [k,s.getPropertyValue('--'+k).trim()]));
    });
    tokens.white='#ffffff';
    for (const [fg,bg,min] of [['text','bg',4.5],['text','surface',4.5],['muted','bg',4.5],['muted','surface',4.5],['blue','surface',4.5],['surface','blue',4.5],['orange','orange-soft',4.5],['success','success-soft',4.5],['focus','bg',3],['focus','surface',3],['control','surface',3],['text','section',4.5],['white','masthead',4.5],['orange-ink','orange-fill',4.5]]) {
      const ratio=contrast(tokens[fg],tokens[bg]);
      report.push({theme,foreground:fg,background:bg,ratio:Math.round(ratio*100)/100,min,pass:ratio>=min});
    }
    const cells=await page.locator('.metric-cell').evaluateAll(cells=>cells.map(cell=>({foreground:getComputedStyle(cell).color,background:getComputedStyle(cell).backgroundColor,value:cell.dataset.sortValue})));
    cells.forEach((cell,index)=>{
      const ratio=contrast(hex(cell.foreground),hex(cell.background));
      report.push({theme,context:'original metric spectrum',index,value:cell.value,foreground:hex(cell.foreground),background:hex(cell.background),ratio:Math.round(ratio*100)/100,min:4.5,pass:ratio>=4.5});
    });
  }
  fs.writeFileSync(path.join(root,'research/contrast-checks.json'),JSON.stringify(report,null,2)+'\n');
  console.log(`${report.filter(r=>r.pass).length}/${report.length} selected token and original metric-cell contrast checks pass`);
  await browser.close();
  if(report.some(r=>!r.pass))process.exit(1);
})();
