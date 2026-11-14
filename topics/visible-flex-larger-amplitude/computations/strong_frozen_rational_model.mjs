// Same rational 65/64 deep definition, with checked reuse of the old 160 alphas.
// No original source module, worker, runner, or metric parameter is edited.
import fs from 'node:fs';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const sha = data => crypto.createHash('sha256').update(data).digest('hex');
const ORIGINAL_SHA = '12e6ae86a49b5282e00b56e78993190b5818373ffaecfc096b66e7d7a48a53a8';
const FACTORY_SHA = '77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247';
const SELF_SHA = sha(fs.readFileSync(new URL(import.meta.url)));
const originalURL = new URL('./closure_rational_tail_model.mjs', import.meta.url);
const factoryURL = new URL('./strong_frozen_calibration_factory.mjs', import.meta.url);
const pointCacheURL = new URL('./closure_bounded_point_cache.mjs', import.meta.url);
const original = fs.readFileSync(originalURL, 'utf8');
if (sha(original) !== ORIGINAL_SHA)
  throw Error('The rational model source changed; review the single-call transform');
if (sha(fs.readFileSync(factoryURL)) !== FACTORY_SHA)
  throw Error('The geometry-checked frozen calibration factory changed');

const transforms = [];
function replace(source, before, after, count = 1) {
  const actual = source.split(before).length - 1;
  if (actual !== count)
    throw Error('Frozen rational source anchor count differs: ' + actual);
  transforms.push({before, after, count});
  return source.replaceAll(before, after);
}

let transformed = original;
// Retain the true original adapter identity and resolve its filesystem reads.
transformed = replace(transformed, 'import.meta.url', JSON.stringify(originalURL.href), 2);
transformed = replace(transformed, "'./closure_bounded_point_cache.mjs'",
  JSON.stringify(pointCacheURL.href), 2);
const replacement = `
  const __frozenReuse = await __createFrozenCalibrationFactory(p, {
    sourceTopic,
    ledgerReadyFile: process.env.CLOSURE_FROZEN_CALIBRATION_READY,
    storedReadyFiles: JSON.parse(process.env.CLOSURE_FROZEN_STORED_READY_FILES ?? '[]')
  });
  if (!Object.is(options.frozenWarpAlpha, __frozenReuse.reference.frozenWarpAlpha))
    throw Error('Rational head requires the same explicit saved global warp alpha');
  const factory = __frozenReuse.factory;`;
transformed = replace(transformed,
  '  const factory=weighted.createRecalibrationFactory(p);', replacement);
transformed = replace(transformed, '  function assertFrozenHead(){',
  '  manifest.frozenCalibrationReuse = __frozenReuse.manifest;\n' +
  '  function assertFrozenHead(){');
const helperImport = 'import {createFrozenCalibrationFactory as __createFrozenCalibrationFactory} from ' +
  JSON.stringify(factoryURL.href) + ';\n';
transformed = helperImport + transformed;
const transformedSHA256 = sha(transformed);
const transformedURL = 'data:text/javascript;base64,' + Buffer.from(transformed).toString('base64');

export async function createRationalDeepTail(config, options = {}) {
  if (!Number.isFinite(options.frozenWarpAlpha))
    throw Error('Frozen rational reuse requires an explicit non-null finite frozenWarpAlpha');
  if (!process.env.CLOSURE_FROZEN_CALIBRATION_READY)
    throw Error('CLOSURE_FROZEN_CALIBRATION_READY must name the checked full160 ledger');
  const stored = JSON.parse(process.env.CLOSURE_FROZEN_STORED_READY_FILES ?? '[]');
  if (!Array.isArray(stored) || !stored.every(value => typeof value === 'string'))
    throw Error('CLOSURE_FROZEN_STORED_READY_FILES must encode an array of file names');
  const module = await import(transformedURL);
  const result = await module.createRationalDeepTail(config, options);
  if (result.manifest.sourceHashes.adapter !== ORIGINAL_SHA)
    throw Error('Original rational adapter hash was not retained');
  if (result.manifest.deepAlpha !== '65/64' || result.start !== 160)
    throw Error('Unexpected rational metric definition or head length');
  if (!result.manifest.frozenCalibrationReuse)
    throw Error('The factory reuse manifest was not retained');
  result.manifest.frozenCalibrationSourceTransform = {
    name: 'same-rational-model-frozen-finite-head-calibration-v1',
    adapterFile: fileURLToPath(import.meta.url),
    adapterSHA256: SELF_SHA,
    originalAdapterFile: fileURLToPath(originalURL),
    originalAdapterSHA256: ORIGINAL_SHA,
    transformedAdapterSHA256: transformedSHA256,
    frozenFactoryFile: fileURLToPath(factoryURL),
    frozenFactorySHA256: FACTORY_SHA,
    helperImport,
    transforms,
    mathematicalCallReplacements: 1,
    deepMetricDefinitionChanged: false,
    originalSourceHashesAdapterRetained: true,
    scope: 'Only the old n<160 binary calibration alpha lookup is replaced. Original rational65/64 deep definition, all head cells, global warp alpha, source formulas and physical integration order are retained. This is neither a nonlinear solve nor an infinite-tail existence certificate.'
  };
  result.assertFrozenHead();
  return result;
}
