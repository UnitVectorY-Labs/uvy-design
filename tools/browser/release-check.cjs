const {chromium}=require('playwright');
const fs=require('fs');const path=require('path');const assert=require('assert/strict');
const root=path.resolve(__dirname,'../..');
fs.mkdirSync(path.join(root,'output'),{recursive:true});
fs.writeFileSync(path.join(root,'output/asset-check.html'),'<!doctype html><html><head><script src="/assets/uvy-theme.js"></script><link rel="stylesheet" href="/assets/uvy-tokens.css"><link rel="stylesheet" href="/assets/uvy-elements.css"></head><body><button data-uvy-theme-toggle hidden>Theme</button><main></main></body></html>');
(async()=>{
 const browser=await chromium.launch();
 const context=await browser.newContext({colorScheme:'light'});
 const page=await context.newPage();
 await page.goto('http://127.0.0.1:8766/output/asset-check.html');
 assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
 assert.equal(await page.locator('[data-uvy-theme-toggle]').isVisible(),true);
 await page.emulateMedia({colorScheme:'dark'});await page.waitForFunction(()=>document.documentElement.dataset.theme==='dark');
 await page.click('[data-uvy-theme-toggle]');assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
 await page.reload();assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
 await page.evaluate(()=>{document.querySelector('main').innerHTML='<button data-uvy-theme-toggle>added after swap</button>';document.dispatchEvent(new Event('htmx:after:swap'));});
 await page.locator('main button').click();assert.equal(await page.locator('html').getAttribute('data-theme'),'dark');
 const cookie=(await context.cookies()).find(x=>x.name==='uvy-theme');assert.equal(cookie.sameSite,'Lax');assert.equal(cookie.path,'/');
 for(const theme of ['light','dark']){
  const c=await browser.newContext({javaScriptEnabled:false,colorScheme:theme});const p=await c.newPage();await p.goto('http://127.0.0.1:8766/output/asset-check.html');assert.equal(await p.evaluate(()=>getComputedStyle(document.documentElement).colorScheme),theme);await c.close();
 }
 await context.addCookies([{name:'uvy-theme',value:'invalid',url:'http://127.0.0.1:8766'}]);await page.emulateMedia({colorScheme:'light'});await page.reload();assert.equal(await page.locator('html').getAttribute('data-theme'),'light');
 const manifest=JSON.parse(fs.readFileSync(path.join(root,'dist/asset-manifest.json')));const crypto=require('crypto');for(const file of manifest.files){assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(root,file.path))).digest('hex'),file.sha256);}
 console.log('Release assets: OS defaults, override persistence, delegated post-swap toggle, invalid-cookie fallback, no-JS themes and package hashes pass');
 await browser.close();
})();
