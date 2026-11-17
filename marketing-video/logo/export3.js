const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 1400 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'premium.html')); await p.evaluate(() => document.fonts.ready); await p.waitForLoadState('networkidle');
  for (const k of ['glass', 'gold', 'soft', 'chrome']) await p.locator('#bn_' + k).screenshot({ path: path.join(__dirname, 'premium', `banner-${k}.png`) });
  await p.locator('#sheet').screenshot({ path: path.join(__dirname, 'premium', 'premium-sheet.jpg'), type: 'jpeg', quality: 92 });
  await b.close();
})();
