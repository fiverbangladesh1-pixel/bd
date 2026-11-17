const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 1600 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'colors.html') + '?rec=' + (process.argv[2] || 'navy-lime')); await p.evaluate(() => document.fonts.ready);
  await p.locator('#board').screenshot({ path: path.join(__dirname, 'colors', 'colour-variants.jpg'), type: 'jpeg', quality: 92 });
  for (const k of ['blue', 'navy-blue', 'white-blue', 'gradient', 'navy-lime', 'green', 'orange', 'black-gold']) await p.locator('#f_' + k).screenshot({ path: path.join(__dirname, 'colors', `profile-${k}.png`) });
  await b.close();
})();
