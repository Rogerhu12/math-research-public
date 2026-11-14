// Reuse the pinned binary calibration table without changing stored geometry.
// All 160 head cells and the original auxiliary far graphs remain present.
import fs from 'node:fs';
import crypto from 'node:crypto';
import {createFrozenCalibrationFactory,profileFingerprint} from './strong_frozen_calibration_factory.mjs';
import {installBoundedPointCache} from './closure_bounded_point_cache.mjs';
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const fractions=[0,.125,.25,.5,.75,.875,1];

export async function createStoredPhysical(config) {
  const sourceTopic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
  const ledgerReadyFile=process.env.VISIBLE_FLEX_FROZEN_LEDGER_READY;
  const storedReadyFile=process.env.VISIBLE_FLEX_FROZEN_STORED_READY;
  if(!sourceTopic||!ledgerReadyFile||!storedReadyFile)
    throw Error('Frozen stored geometry requires the pinned source and both saved ready references');
  const limit=Number(process.env.VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT??8);
  if(!Number.isInteger(limit)||limit<1||limit>96)
    throw Error('Point cache limit must be an integer in [1,96]');
  const adapted=await createFrozenCalibrationFactory(config,
    {sourceTopic,ledgerReadyFile,storedReadyFiles:[storedReadyFile]});
  const physical=adapted.factory.assemble();
  const before=profileFingerprint(physical,fractions),alpha=physical.stats.alpha;
  installBoundedPointCache(adapted.factory,
    {count:physical.cells.length,controls:config.valleyControls??[],limit});
  const after=profileFingerprint(physical,fractions);
  if(before!==after||!Object.is(physical.stats.alpha,alpha))
    throw Error('Frozen stored geometry changed under bounded point memoization');
  adapted.verify(physical);
  const memoryBefore=process.memoryUsage();
  if(typeof globalThis.gc==='function')globalThis.gc();
  const memoryAfter=process.memoryUsage();
  const manifest={
    name:'tail-original-stored-metric-bounded-points-v1',
    sourceRevision:adapted.manifest.sourceRevision,
    physicalParameters:physical.parameters,frozenWarpAlpha:alpha,
    cellCount:physical.cells.length,pointCacheLimit:limit,
    profileFingerprintBefore:before,profileFingerprintAfter:after,
    fingerprintFields:['r','drdx','logw','dlogwdx'],fingerprintFractions:fractions,
    sourceSHA256:{weighted:adapted.manifest.sourceSHA256.weighted,
      adapter:sha(fs.readFileSync(new URL(import.meta.url))),
      boundedPointCache:sha(fs.readFileSync(new URL('./closure_bounded_point_cache.mjs',import.meta.url)))},
    frozenCalibrationAdapter:adapted.manifest,
    compactStorageAdapter:{
      name:'original-g-smaller-point-cache-and-explicit-gc-v1',pointCacheLimit:limit,
      fingerprintBefore:before,fingerprintAfter:after,
      explicitGcAvailable:typeof globalThis.gc==='function',memoryBefore,memoryAfter},
    scope:'The saved original binary alpha_n and global warp alpha are reused through a source-hash-locked lookup. All original physical formulas, arithmetic order, 160 cells and auxiliary far transfers remain; five- and seven-fraction historical fingerprints are checked. No rational deep replacement or physical recalibration.'
  };
  return {physical,factory:adapted.factory,manifest};
}
