const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 3200, height: 1600 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'lockups.html') + '?m=1&c=gradient'); await p.evaluate(() => document.fonts.ready);
  const o = n => path.join(__dirname, 'lockups', n);
  await p.locator('#board').screenshot({ path: o('logo-colours.jpg'), type: 'jpeg', quality: 92 });
  for (let i = 1; i <= 4; i++) for (const k of ['white-blue', 'blue', 'gradient', 'navy-blue', 'navy-lime', 'green', 'orange', 'black-gold'])
    await p.locator(`#f_${i}_${k}`).screenshot({ path: o(`logo${i}-${k}.png`) });
  await p.locator('#sq').screenshot({ path: o('recommended-logo-square.png') });
  await p.locator('#ic').screenshot({ path: o('recommended-profile.png') });
  await b.close();
})();
