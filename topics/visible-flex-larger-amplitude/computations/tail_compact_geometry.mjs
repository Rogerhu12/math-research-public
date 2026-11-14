// A stricter memoization bound on the unchanged original stored geometry.
// Both original and compact fingerprints are retained. No physical parameter,
// calibration, quadrature, slope or operation order is changed.
import fs from 'node:fs';
import crypto from 'node:crypto';
import {createStoredPhysical as createOriginal} from './tail_stored_geometry.mjs';
import {installBoundedPointCache} from './closure_bounded_point_cache.mjs';
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');

export async function createStoredPhysical(config) {
  const answer=await createOriginal(config);
  const limit=Number(process.env.VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT??16);
  if(!Number.isInteger(limit)||limit<1||limit>96)
    throw Error('Compact point cache limit must be an integer in [1,96]');
  const original=answer.manifest;
  const fingerprint=()=>{
    const hash=crypto.createHash('sha256');
    for(const cell of answer.physical.cells)for(const profile of cell.profiles)
      for(const x of original.fingerprintFractions){
        const z=profile(x);hash.update(JSON.stringify([z.r,z.drdx,z.logw,z.dlogwdx])+'\n');
      }
    return hash.digest('hex');
  };
  const before=fingerprint(),alpha=answer.physical.stats.alpha;
  installBoundedPointCache(answer.factory,
    {count:answer.physical.cells.length,controls:config.valleyControls??[],limit});
  const after=fingerprint();
  if(before!==original.profileFingerprintAfter||before!==after||answer.physical.stats.alpha!==alpha)
    throw Error('Compact storage changed the original geometry');
  const memoryBefore=process.memoryUsage();
  if(typeof globalThis.gc==='function')globalThis.gc();
  const memoryAfter=process.memoryUsage();
  answer.manifest={...original,pointCacheLimit:limit,compactStorageAdapter:{
    name:'original-g-smaller-point-cache-and-explicit-gc-v1',
    previousPointCacheLimit:original.pointCacheLimit,pointCacheLimit:limit,
    fingerprintBefore:before,fingerprintAfter:after,
    explicitGcAvailable:typeof globalThis.gc==='function',memoryBefore,memoryAfter,
    sourceSHA256:{compact:sha(fs.readFileSync(new URL(import.meta.url))),
      original:sha(fs.readFileSync(new URL('./tail_stored_geometry.mjs',import.meta.url))),
      cache:sha(fs.readFileSync(new URL('./closure_bounded_point_cache.mjs',import.meta.url)))},
    scope:'Storage and garbage collection only. Original head, calibration, profile formulas and numerical integrals are retained.'
  }};
  return answer;
}
