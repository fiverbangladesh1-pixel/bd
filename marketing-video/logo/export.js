const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 1400 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'logo.html')); await p.evaluate(() => document.fonts.ready);
  const shot = async (id, name, transparent) => { if (transparent) await p.evaluate(() => document.body.style.background = 'transparent');
    await p.locator(id).screenshot({ path: path.join(__dirname, 'export', name), omitBackground: !!transparent }); };
  await shot('#sheet', 'logo-sheet.png'); await shot('#av_black', 'avatar-black-1024.png'); await shot('#av_grad', 'avatar-gradient-1024.png'); await shot('#av_dark', 'avatar-dark-1024.png');
  await shot('#lk_white', 'lockup-white-transparent.png', true); await shot('#lk_grad', 'lockup-gradient-transparent.png', true); await shot('#lk_dark', 'lockup-dark-transparent.png', true);
  await shot('#icon_white', 'icon-white-transparent.png', true); await shot('#icon_grad', 'icon-gradient-transparent.png', true);
  await b.close();
})();
