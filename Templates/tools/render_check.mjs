// Render LiaScript files in headless Chrome with the official LiaScript viewer and check every slide:
// which components rendered (quizzes, surveys, scripts, code, diagrams, media), raw syntax that leaked
// into the visible text, JavaScript errors and failed requests.
//
// Setup (once):  cd tools && npm install
// Usage:         node tools/render_check.mjs [--shots DIR] FILE.md ...   (paths relative to the current folder)
// Chrome:        macOS default path, or set CHROME_PATH.
import puppeteer from 'puppeteer-core';
import http from 'http';
import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const VIEWER = path.dirname(require.resolve('@liascript/editor/dist/index.html'));
const ROOT = process.cwd();
const CHROME = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = 3124;
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.md': 'text/markdown',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json', '.wasm': 'application/wasm' };

const COMPONENTS = {
  quiz: '.lia-quiz', survey: '.lia-survey', hint: '.lia-quiz__hints', slider: 'input[type=range]', script: '.lia-script',
  code: '.lia-code', run: 'button[title=Execute]', mermaid: 'svg[aria-roledescription]', iframe: 'iframe',
  image: '.lia-figure', table: 'table', alert: '[class*=lia-quote__alert]', details: 'details',
};
const LEAKS = [/\[\[/, /\]\]/, /\[\(/, /\{\{/, /\}\}/, /\*\*\*/, /```/, /<details/, /<script/, /@input/, /@Pyodide/,
  /@mermaid/, /-->/, /<!--/, /<!–/, /⟶/, /\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)/, /<section/, /<div/];

// Static server: viewer under /liascript/, course files from the current folder, slides shown in Textbook mode
const server = http.createServer((req, res) => {
  let url;
  try { url = decodeURIComponent(req.url.split('?')[0]); } catch { res.writeHead(404); return res.end(); }  // e.g. unfilled %%IMAGE-PATH%%
  const file = url.startsWith('/liascript/') ? path.join(VIEWER, url.slice(11) || 'index.html') : path.join(ROOT, url);
  fs.readFile(file, (err, data) => {
    if (err) { res.writeHead(404); return res.end(); }
    if (file.endsWith('.md')) data = data.toString().replace(/^mode:\s+Presentation/m, 'mode:     Textbook');
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream', 'Access-Control-Allow-Origin': '*' });
    res.end(data);
  });
}).listen(PORT);

const args = process.argv.slice(2);
const shotsAt = args.indexOf('--shots');
const shots = shotsAt >= 0 ? args.splice(shotsAt, 2)[1] : null;
if (shots) fs.mkdirSync(shots, { recursive: true });
if (!args.length) { console.log('usage: node tools/render_check.mjs [--shots DIR] FILE.md ...'); process.exit(2); }

const browser = await puppeteer.launch({ executablePath: CHROME, headless: true });
let failed = 0;
for (const rel of args) {
  const src = fs.readFileSync(path.join(ROOT, rel), 'utf8');
  let inCode = false;
  const heads = src.split('\n').filter(line => (/^\s*```/.test(line) ? (inCode = !inCode, false) : !inCode && /^#{1,2} /.test(line)));
  console.log(`\n=== ${rel} (${heads.length} slides)`);
  for (let i = 1; i <= heads.length; i++) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 1000 });
    const problems = [];
    page.on('pageerror', e => { if (!/fetchError/.test(e.message)) problems.push('JS error: ' + e.message.slice(0, 160)) });
    page.on('response', r => { if (r.status() >= 400 && !r.url().includes('%25%25')) problems.push(`warning: HTTP ${r.status()} ${r.url().slice(0, 110)}`) });
    await page.goto(`http://localhost:${PORT}/liascript/index.html?http://localhost:${PORT}/${rel}#${i}`, { waitUntil: 'networkidle2', timeout: 90000 });
    try {
      await page.waitForFunction(() => !document.body.innerText.includes('Loading scripts') && document.querySelector('.lia-slide__content'), { timeout: 120000 });
    } catch { problems.push('JS error: course did not finish loading (dead import URL?)'); }
    await new Promise(r => setTimeout(r, 2500));
    const res = await page.evaluate((COMPONENTS, LEAKS) => {
      const root = document.querySelector('.lia-slide__content') || document.body;
      const counts = Object.entries(COMPONENTS).map(([k, sel]) => [k, root.querySelectorAll(sel).length]).filter(([, n]) => n);
      const clone = root.cloneNode(true);
      clone.querySelectorAll('pre, code, .lia-code, svg, style, script').forEach(e => e.remove());
      const text = clone.innerText;
      const leaks = LEAKS.map(([s, f]) => new RegExp(s, f)).filter(r => r.test(text)).map(r => r.source);
      if (/%%/.test(text.replace(/%%[A-Z0-9-]+%%/g, ''))) leaks.push('broken %%placeholder%%');
      return { counts, leaks };
    }, COMPONENTS, LEAKS.map(r => [r.source, r.flags]));
    const bad = res.leaks.length || problems.some(p => p.startsWith('JS'));
    failed += bad;
    console.log(`${bad ? 'ERR' : 'OK '} [${i}] ${heads[i - 1].replace(/^#+ /, '').slice(0, 60)}  ` + res.counts.map(([k, n]) => `${k}:${n}`).join(' '));
    if (res.leaks.length) console.log('      raw syntax visible: ' + res.leaks.join('  '));
    for (const p of [...new Set(problems)]) console.log('      ' + p);
    if (shots) await page.screenshot({ path: path.join(shots, `${path.basename(rel, '.md')}_${i}.png`), fullPage: true });
    await page.close();
  }
}
await browser.close();
server.close();
console.log(`\n${failed ? failed + ' slide(s) with problems' : 'all slides OK'}`);
process.exit(failed ? 1 : 0);
