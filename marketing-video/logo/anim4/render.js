const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
const FPS = 30, D = 8, SUB = +process.env.SUB || 3, DSF = +process.env.DSF || 1.5;
(async () => {
  const [mode, a, b] = process.argv.slice(2);
  const br = await chromium.launch(); const p = await br.newPage({ viewport: { width: 1024, height: 1024 }, deviceScaleFactor: mode === 'stills' ? 1 : DSF });
  p.on('pageerror', e => console.log('PAGEERR', e.message));
  await p.goto('file://' + path.join(__dirname, 'anim.html')); await p.evaluate(() => window.prep());
  if (mode === 'stills') { for (const t of a.split(',').map(Number)) { await p.evaluate(t => window.seek(t), t); await p.screenshot({ path: path.join(__dirname, 'out', `s_${t}.jpg`), type: 'jpeg', quality: 85 }); } }
  else { const dir = path.join(__dirname, 'out', 'frames'); fs.mkdirSync(dir, { recursive: true });
    for (let f = +a; f < +b; f++) for (let k = 0; k < SUB; k++) { await p.evaluate(t => window.seek(t), (f + k / SUB * 0.6) / FPS);
      await p.screenshot({ path: path.join(dir, `f_${String(f * SUB + k).padStart(6, '0')}.jpg`), type: 'jpeg', quality: 96 }); } }
  await br.close();
})();
