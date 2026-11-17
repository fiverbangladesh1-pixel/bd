// Renders video.html frame by frame.
//   node render.js stills 2,6,12        -> out/still_<t>.png
//   node render.js frames <from> <to>   -> out/frames/f_00000.jpg ...
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const FPS = 30, DUR = 46;

(async () => {
  const [mode, a, b] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'video.html'));
  await page.evaluate(() => window.prep());
  if (mode === 'stills') {
    for (const t of a.split(',').map(Number)) {
      await page.evaluate(t => window.seek(t), t);
      await page.screenshot({ path: path.join(__dirname, 'out', `still_${t}.png`) });
    }
  } else {
    const dir = path.join(__dirname, 'out', 'frames');
    fs.mkdirSync(dir, { recursive: true });
    const from = +a || 0, to = +b || FPS * DUR;
    for (let f = from; f < to; f++) {
      await page.evaluate(t => window.seek(t), f / FPS);
      await page.screenshot({ path: path.join(dir, `f_${String(f).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 96 });
    }
  }
  await browser.close();
})();
