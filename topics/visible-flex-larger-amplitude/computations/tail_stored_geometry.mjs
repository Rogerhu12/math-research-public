// The original stored metric with a bounded point memoization policy.
// No rational deep replacement, calibration change, or new warp is performed.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {installBoundedPointCache} from './closure_bounded_point_cache.mjs';

const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const fractions=[0,.125,.25,.5,.75,.875,1];

export async function createStoredPhysical(config) {
  const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
  if(!topic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC is required');
  const weightedPath=path.join(topic,'scripts/closing_weighted_tail.mjs');
  const {createRecalibrationFactory}=await import(pathToFileURL(weightedPath).href);
  // Match the immutable worker's constructor invocation exactly.
  const factory=createRecalibrationFactory(config),physical=factory.assemble();
  if(physical.parameters.orientation!==1)
    throw Error('The shared stable-graph adapter has only been checked for orientation +1');
  const fingerprint=()=>{
    const hash=crypto.createHash('sha256');
    for(const cell of physical.cells)for(const profile of cell.profiles)
      for(const x of fractions){
        const z=profile(x);
        hash.update(JSON.stringify([z.r,z.drdx,z.logw,z.dlogwdx])+'\n');
      }
    return hash.digest('hex');
  };
  const before=fingerprint(),alpha=physical.stats.alpha,limit=96;
  installBoundedPointCache(factory,
    {count:physical.cells.length,controls:config.valleyControls??[],limit});
  const after=fingerprint();
  if(before!==after||physical.stats.alpha!==alpha)
    throw Error('A storage-policy change altered the original physical geometry');
  const manifest={
    name:'tail-original-stored-metric-bounded-points-v1',
    sourceRevision:JSON.parse(fs.readFileSync(path.join(topic,'source-origin.json'),'utf8')).source_revision,
    physicalParameters:physical.parameters,frozenWarpAlpha:alpha,
    cellCount:physical.cells.length,pointCacheLimit:limit,
    profileFingerprintBefore:before,profileFingerprintAfter:after,
    fingerprintFields:['r','drdx','logw','dlogwdx'],fingerprintFractions:fractions,
    sourceSHA256:{weighted:sha256(fs.readFileSync(weightedPath)),
      adapter:sha256(fs.readFileSync(new URL(import.meta.url))),
      boundedPointCache:sha256(fs.readFileSync(new URL('./closure_bounded_point_cache.mjs',import.meta.url)))},
    scope:'Original createRecalibrationFactory(config).assemble() and every original cell retained. Only private point memoization is bounded. No rational deep metric is imported or constructed.'
  };
  return {physical,factory,manifest};
}
