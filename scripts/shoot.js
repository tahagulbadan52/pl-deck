// Screenshot every .slide in gallery.html to scripts/_shots/slide-NN.png
const puppeteer = require('/tmp/node_modules/puppeteer');
const path = require('path');
const fs = require('fs');
(async () => {
  const root = path.resolve(__dirname, '..');
  const outDir = path.join(__dirname, '_shots');
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(root, 'gallery.html'), { waitUntil: 'networkidle0', timeout: 60000 });
  await new Promise(r => setTimeout(r, 1500));
  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(outDir, `slide-${String(i+1).padStart(2,'0')}.png`) });
  }
  console.log('shot', slides.length, 'slides ->', outDir);
  await browser.close();
})();
