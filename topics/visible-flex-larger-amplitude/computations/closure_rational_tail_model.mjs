// A separately named fixed metric with an exact rational deep definition.
// The existing factory and every saved old-g artifact remain unchanged.
// This module retains all shallow cell objects and their global warp alpha.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {installBoundedPointCache} from './closure_bounded_point_cache.mjs';

const SQRT12=Math.sqrt(12);
const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const adapterSHA256=sha256(fs.readFileSync(new URL(import.meta.url)));
const boundedPointCacheSHA256=sha256(fs.readFileSync(new URL('./closure_bounded_point_cache.mjs',import.meta.url)));

export async function createRationalDeepTail(config,options={}) {
  const sourceTopic=path.resolve(options.sourceTopic??process.env.VISIBLE_FLEX_SOURCE_TOPIC??'');
  if(!fs.existsSync(path.join(sourceTopic,'source-origin.json')))
    throw Error('Pinned sourceTopic with source-origin.json is required');
  const sourceRoot=path.join(sourceTopic,'repro/source-root');
  const weightedPath=path.join(sourceTopic,'scripts/closing_weighted_tail.mjs');
  const sourcePath=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/general_root_smooth_tail_cells.cjs');
  process.env.CLOSING_TAIL_CACHE=path.dirname(sourcePath);
  const weighted=await import(pathToFileURL(weightedPath).href);
  const {default:oldCells}=await import(pathToFileURL(sourcePath).href);
  const p={...config};
  if(p.rejoinR20At!==undefined&&p.rejoinR20At!==null)
    throw Error('This adapter is for the original delta0=.006 source, not the rejoin source');
  const factory=weighted.createRecalibrationFactory(p);
  // A supplied alpha is an explicit fixed binary datum.  Otherwise retain the
  // original factory's result; constructing deep cells never recomputes it.
  const head=factory.assemble(p.valleyControls??[],options.frozenWarpAlpha??null);
  const q=head.source.parameters;
  if(q.R!==64||q.a!==2.75||q.delta0!==.006||q.etaPower!==1.5||q.etaRatioAtN0!==.05)
    throw Error('R15 currently defines only R64, a=11/4, delta0=.006, etaPower=3/2, etaRatio=.05');
  if(q.orientation!==1)throw Error('This first adapter implements the current outward source orientation');
  const start=p.protectCell??factory.parameters.protectCell;
  if(start!==head.cells.length)throw Error('The rational replacement must begin after every warped head cell');
  const alpha=65/64,A=q.a*Math.log(2),cache=new Map();
  const after=n=>3*q.delta0*2**(-n)+
    6*q.etaRatioAtN0*q.delta0*2**(-q.etaPower*(n+1))/(1-2**(-q.etaPower));
  function deepCell(n) {
    if(!Number.isInteger(n)||n<start)throw Error('Deep cell index must be an integer >= protectCell');
    if(cache.has(n))return cache.get(n);
    const delta=q.delta0*2**(-n),c=q.etaRatioAtN0*2**(-n*(q.etaPower-1));
    const mu=q.epsilonScale*delta**q.a;
    if(!(delta>0&&mu>0&&Number.isFinite(mu)))
      throw Error('This floating evaluator has reached underflow; the exact deep definition remains (1.1) of R15');
    const rInner=q.rCuff*Math.exp(after(n)/SQRT12),logBase=Math.log(mu);
    let offset=0;
    const profiles=oldCells.cellSegments(delta,64,alpha,A,c).map(seg=>{
      const len=seg.lengthRatio*delta,s0=offset;offset+=len;
      return x=>{
        const s=seg.transition?oldCells.cellSmooth(x):0;
        const ds=seg.transition?oldCells.cellSmoothDerivative(x):0;
        const logRadius=Math.log(rInner)+(s0+len*x)/SQRT12;
        const r=Math.exp(logRadius);
        return {r,drdx:len*r/SQRT12,
          logw:logBase+seg.lo+(seg.hi-seg.lo)*s-Math.log(delta)-7*logRadius,
          dlogwdx:(seg.hi-seg.lo)*ds-7*len/SQRT12};
      };
    });
    const cell={n,physicalIndex:n,delta,c,R:64,alpha,mu,profiles,
      calibrationDefinition:'exact rational 65/64; not a zero of T21',
      length:delta*(3+6*c),rOuter:rInner};
    cache.set(n,cell);return cell;
  }
  function cell(n){return n<start?head.cells[n]:deepCell(n);}
  function headFingerprint() {
    const hash=crypto.createHash('sha256');
    for(const c of head.cells)for(const profile of c.profiles)
      for(const x of [0,.25,.5,.75,1]) {
        const z=profile(x);
        hash.update(JSON.stringify([z.r,z.drdx,z.logw,z.dlogwdx])+'\n');
      }
    return hash.digest('hex');
  }
  const initialFingerprint=headFingerprint(),frozenWarpAlpha=head.stats.alpha;
  // The original profile point map retains every quadrature point forever.
  // A 192-cell linear trace otherwise accumulates millions of cached objects.
  // Reuse its exact point formula with a bounded per-segment cache; this is
  // arithmetic storage only and is checked against the original fingerprint.
  const pointCacheLimit=options.pointCacheLimit??96;
  if(pointCacheLimit>0)installBoundedPointCache(factory,
    {count:start,controls:p.valleyControls??[],limit:pointCacheLimit});
  if(headFingerprint()!==initialFingerprint)throw Error('Bounded point cache changed the shallow source values');
  const shallow=head.cells.at(-1).profiles[0](0),deep=deepCell(start).profiles.at(-1)(1);
  const endpointCheck={
    shallowIndex:start-1,deepIndex:start,
    radiusDifference:deep.r-shallow.r,
    logSlopeDifference:deep.logw-shallow.logw,
    relativeSlopeDifference:Math.expm1(deep.logw-shallow.logw),
    logarithmicPhysicalDerivativeDifference:deep.dlogwdx/deep.drdx-shallow.dlogwdx/shallow.drdx,
    scope:'Floating evaluation diagnostic; exact endpoint two-jet compatibility follows from the symbolic source definition.'
  };
  const manifest={
    definition:'visible-larger-rational-deep-alpha-v1',
    sourceRevision:JSON.parse(fs.readFileSync(path.join(sourceTopic,'source-origin.json'),'utf8')).source_revision,
    sourceTopic,start,deepAlpha:'65/64',
    exactSourceConstants:{delta0:'3458764513820541/576460752303423488',
      etaRatioAtN0:'3602879701896397/72057594037927936',
      convention:'Fixed dyadic input constants with exact real profile functions; floating evaluations are approximations.'},
    physicalParameters:head.parameters,frozenWarpAlpha,pointCacheLimit,
    headFingerprint:initialFingerprint,
    headFingerprintDefinition:'SHA256 of unchanged head (r,drdx,logw,dlogwdx) at fractions 0,.25,.5,.75,1 in each segment',
    sourceHashes:{weighted:sha256(fs.readFileSync(weightedPath)),cells:sha256(fs.readFileSync(sourcePath)),
                  adapter:adapterSHA256,boundedPointCache:boundedPointCacheSHA256},
    endpointCheck,
    semanticBoundary:'New metric beyond protectCell. The old stored metric is not relabeled, and no exact infinite nonlinear DN is supplied.'
  };
  function assertFrozenHead(){
    if(head.stats.alpha!==frozenWarpAlpha||headFingerprint()!==initialFingerprint)
      throw Error('Shallow metric changed while constructing the rational deep extension');
    return true;
  }
  return {head,factory,cell,deepCell,start,manifest,assertFrozenHead,
          physicalModeColumn:weighted.physicalModeColumn,
          idealModeGraph:weighted.idealModeGraph};
}
