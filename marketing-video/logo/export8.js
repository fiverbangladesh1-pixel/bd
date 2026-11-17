const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const rec = process.argv[2] || 'yellow-black', note = process.argv[3] || '';
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 3000 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'pop.html') + '?rec=' + rec); await p.evaluate(() => document.fonts.ready); await p.waitForLoadState('networkidle');
  await p.evaluate(n => { const e = document.getElementById('note'); if (n) e.innerHTML = n; else e.remove(); }, note);
  await p.locator('#board').screenshot({ path: path.join(__dirname, 'pop', 'attention-test.jpg'), type: 'jpeg', quality: 92 });
  if (process.argv[4]) for (const k of ['yellow-black', 'orange', 'blue-yellow', 'black-yellow', 'red', 'lime-navy', 'blue-white', 'white-orange']) {
    await p.setViewportSize({ width: 2400, height: 2200 }); await p.locator('#f_' + k).scrollIntoViewIfNeeded();
    await p.locator('#f_' + k).screenshot({ path: path.join(__dirname, 'pop', `profile-${k}.png`) }); }
  await b.close();
})();
