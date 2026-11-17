const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 1400 }, deviceScaleFactor: 1 });
  for (const t of ['teal', 'green']) {
    const u = 'file://' + path.join(__dirname, 'set.html') + '?t=' + t; const o = n => path.join(__dirname, 'sets', `${t}-${n}`);
    await p.goto(u); await p.evaluate(() => document.fonts.ready); await p.waitForLoadState('networkidle');
    await p.locator('#cover').screenshot({ path: o('facebook-cover.png') });
    await p.locator('#lockup').screenshot({ path: o('logo-horizontal.png') });
    await p.locator('#square').screenshot({ path: o('logo-with-name.png') });
    await p.goto(u); await p.waitForLoadState('networkidle');
    await p.locator('#mock').screenshot({ path: o('preview.jpg'), type: 'jpeg', quality: 88 });
    fs.copyFileSync(path.join(__dirname, 'gen2', `up_${t}_0.png`), o('profile-2048.png'));
  }
  await b.close();
})();
