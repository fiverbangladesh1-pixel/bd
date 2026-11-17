// node render.js stills 2,6,12 | node render.js frames <from> <to>   (SUB sub-frames per frame for motion blur)
const { chromium } = require('playwright');const path = require('path');const fs = require('fs');
const FPS = 30, SUB = +process.env.SUB || 4;
(async () => {
  const [mode, a, b] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  page.on('pageerror', e => console.log('PAGEERR', e.message));
  await page.goto('file://' + path.join(__dirname, 'video.html'));
  await page.evaluate(() => window.prep());
  if (mode === 'stills') {
    for (const t of a.split(',').map(Number)) { await page.evaluate(t => window.seek(t), t);
      await page.screenshot({ path: path.join(__dirname, 'out', `s_${t}.jpg`), type: 'jpeg', quality: 88 }); }
  } else {
    const dir = path.join(__dirname, 'out', 'frames'); fs.mkdirSync(dir, { recursive: true });
    for (let f = +a; f < +b; f++) for (let k = 0; k < SUB; k++) {
      await page.evaluate(t => window.seek(t), (f + k / SUB * 0.6) / FPS);
      await page.screenshot({ path: path.join(dir, `f_${String(f * SUB + k).padStart(6, '0')}.jpg`), type: 'jpeg', quality: 95 }); }
  }
  await browser.close();
})();
