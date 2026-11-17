const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1640, height: 1000 }, deviceScaleFactor: 1 });
  const u = 'file://' + path.join(__dirname, 'cover.html');
  await p.goto(u); await p.evaluate(() => document.fonts.ready); await p.waitForLoadState('networkidle');
  await p.locator('#cover').screenshot({ path: path.join(__dirname, 'cover', 'facebook-cover.png') });
  await p.goto(u); await p.waitForLoadState('networkidle');
  await p.locator('#mock').screenshot({ path: path.join(__dirname, 'cover', 'preview-mobile.jpg'), type: 'jpeg', quality: 88 });
  await b.close();
})();
