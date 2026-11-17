const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 2400, height: 1400 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'logo2.html')); await p.evaluate(() => document.fonts.ready);
  const shot = async (id, name, tr) => { await p.evaluate(t => document.body.style.background = t ? 'transparent' : '#555', !!tr);
    await p.locator(id).screenshot({ path: path.join(__dirname, 'export2', name), omitBackground: !!tr }); };
  await shot('#sheet', 'brand-sheet.png'); await shot('#avA', 'avatar-signature-1024.png'); await shot('#avB', 'avatar-midnight-1024.png'); await shot('#avC', 'avatar-light-1024.png');
  await shot('#lkW', 'lockup-white-transparent.png', 1); await shot('#lkG', 'lockup-gradient-transparent.png', 1); await shot('#lkD', 'lockup-dark-transparent.png', 1);
  await shot('#icG', 'icon-gradient-transparent.png', 1); await shot('#icW', 'icon-white-transparent.png', 1);
  await b.close();
})();
