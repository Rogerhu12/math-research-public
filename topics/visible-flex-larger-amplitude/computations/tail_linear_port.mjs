// Same cusp-split physical RK4 transfer as the pinned 950f linear tool.
// Process all modes in one cell before proceeding to the next cell.  Once a
// cell is finished its private geometry-point closures are no longer needed
// and are released.  Each individual mode has exactly the original sequence
// of arithmetic operations; only independent modes are interleaved.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const [sourceTopic, configFile, outFile, modesText = '64', stepsText = '4096', farText = '48'] = process.argv.slice(2);
if (!sourceTopic || !configFile || !outFile)
  throw Error('Usage: node tail_linear_port.mjs SOURCE_TOPIC CONFIG.json OUTPUT.json [MODES STEPS FAR]');
const sourceRoot = path.join(sourceTopic, 'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT = sourceRoot;
process.env.CLOSING_TAIL_CACHE = path.join(sourceRoot, 'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory, idealModeGraph} = await import(pathToFileURL(path.join(sourceTopic, 'scripts/closing_weighted_tail.mjs')));
const {splitIntegrationInterval} = await import(pathToFileURL(path.join(sourceRoot, 'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));
const config = JSON.parse(fs.readFileSync(configFile, 'utf8'));
const modes = Number(modesText), steps = Number(stepsText), far = Number(farText);
if (![modes, steps, far].every(x => Number.isInteger(x) && x > 0)) throw Error('Positive integer discretization required');
const started = Date.now(), factory = createRecalibrationFactory(config), tail = factory.assemble();
if (far > tail.cells.length) throw Error('Requested far cell exceeds the frozen finite constructor');
const spacing = config.spacing ?? 3;
const cut = tail.cells[0].profiles.at(-1)(1), r = cut.r, w = Math.exp(cut.logw);
const ys = Array.from({length: modes}, (_, j) => [1,
  tail.parameters.orientation * idealModeGraph(spacing * (j + 1), tail.parameters.R, tail.parameters.a)]);
const logGains = new Float64Array(modes);
let lastMu = tail.cells[far - 1].mu, maximumHeapUsed = 0, maximumRSS = 0;

function physicalModeColumn(cell, mode, steps, initial) {
  let y = initial.slice();
  const logMu = Math.log(cell.mu), nu = mode * mode * (mode * mode - 1) / 12, root12 = Math.sqrt(12);
  function rhs(v, g) {
    const lr = Math.log(g.r), a = root12 * g.drdx * Math.exp(logMu - 8 * lr - g.logw),
      b = -nu * root12 * g.drdx * Math.exp(6 * lr + g.logw - logMu),
      d = (mode * mode - 4) * g.drdx / g.r;
    return [d * v[0] + a * v[1], b * v[0] - d * v[1]];
  }
  for (const profile of cell.profiles) for (let k = 0; k < steps; k++) {
    const pieces = splitIntegrationInterval(k / steps, (k + 1) / steps, profile.integrationBreakpoints ?? []);
    for (let j = 0; j < pieces.length - 1; j++) {
      const x = pieces[j], h = pieces[j + 1] - x,
        g0 = profile(x), gm = profile(x + h / 2), g1 = profile(x + h),
        a = rhs(y, g0), b = rhs([y[0] + h * a[0] / 2, y[1] + h * a[1] / 2], gm),
        c = rhs([y[0] + h * b[0] / 2, y[1] + h * b[1] / 2], gm),
        d = rhs([y[0] + h * c[0], y[1] + h * c[1]], g1);
      y = [y[0] + h * (a[0] + 2 * b[0] + 2 * c[0] + d[0]) / 6,
        y[1] + h * (a[1] + 2 * b[1] + 2 * c[1] + d[1]) / 6];
      if (!y.every(Number.isFinite)) throw Error('Nonfinite momentum mode ' + mode);
    }
  }
  return {column: y};
}

for (let n = far - 1; n >= 0; n--) {
  const cell = tail.cells[n];
  for (let j = 0; j < modes; j++) {
    ys[j][1] *= lastMu / cell.mu;
    const z = physicalModeColumn(cell, spacing * (j + 1), steps, ys[j]), norm = Math.hypot(...z.column);
    ys[j] = z.column.map(v => v / norm);
    logGains[j] += Math.log(norm);
  }
  lastMu = cell.mu;
  const usage = process.memoryUsage();
  maximumHeapUsed = Math.max(maximumHeapUsed, usage.heapUsed);
  maximumRSS = Math.max(maximumRSS, usage.rss);
  // These entries are private to this disposable factory.  Future cells and
  // the frozen source files are untouched.  No physical function is evaluated
  // again after its owning cell has completed all requested modes.
  for (const entry of factory.getEntries(n, config.valleyControls?.[n] ?? 0).entries)
    for (const name of ['point', 'profileSource', 'integrand', 'integrate']) entry[name] = null;
  if (n % 8 === 0) console.log(JSON.stringify({event: 'cell-complete', cell: n,
    modes, steps, seconds: (Date.now() - started) / 1000, heapUsed: usage.heapUsed}));
}
const rows = ys.map((y, j) => {
  const mode = spacing * (j + 1);
  return {mode,
    slope: mode * mode / r + Math.sqrt(12) * tail.cells[0].mu * y[1] / (r ** 8 * w * y[0]),
    logHeightGain: logGains[j] + Math.log(Math.abs(y[0])) + 4 * Math.log(r)};
});
const digest = data => crypto.createHash('sha256').update(data).digest('hex');
const result = {method: 'cusp-split RK4 momentum; cell-major scheduling',
  scope: 'Finite linear momentum transfer on the unchanged stored physical weighted metric. Existing modes may be preserved by the packaging helper; only genuinely integrated rows can be added. This is not a nonlinear response or an infinite-tail certificate.',
  source_sha256: digest(fs.readFileSync(new URL(import.meta.url))),
  reference_source: '950f-tail-linear-cusp.mjs',
  reference_source_sha256: digest(fs.readFileSync(path.join(sourceTopic, 'scripts/950f-tail-linear-cusp.mjs'))),
  source_revision: JSON.parse(fs.readFileSync(path.join(sourceTopic, 'source-origin.json'))).source_revision,
  configuration_note: 'Mode-by-mode transfer arithmetic is copied without reassociation from the pinned reference; only independent modes are interleaved cell by cell. Private completed-cell point-cache closures are released.',
  config, config_sha256: digest(fs.readFileSync(configFile)), stats: tail.stats,
  modes, spacing, steps, far,
  cut: {r, w, wr: w * cut.dlogwdx / cut.drdx, E: 1 + w * w,
    Ep: 2 * w * w * cut.dlogwdx / cut.drdx},
  rows, maximumHeapUsed, maximumRSS, seconds: (Date.now() - started) / 1000};
fs.writeFileSync(outFile, JSON.stringify(result, null, 2) + '\n', {flag: 'wx'});
console.log(JSON.stringify({event: 'done', output: outFile, modes, steps,
  seconds: result.seconds, maximumHeapUsed, maximumRSS}));
