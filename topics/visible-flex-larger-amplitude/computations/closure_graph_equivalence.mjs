// Small reproducibility check for the memory-saving linear/cache adapters.
// No root, Fourier model, tolerance or source profile is changed.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {buildRationalStableStageGraphs} from './closure_linear_stage_graphs.mjs';
import {installBoundedPointCache} from './closure_bounded_point_cache.mjs';

const [sourceTopic,portPath,outPath]=process.argv.slice(2);
if(!sourceTopic||!portPath||!outPath)throw Error('SOURCE_TOPIC PORT_JSON OUT_JSON required');
const root=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=root;
process.env.CLOSING_TAIL_CACHE=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const inputs=['closure_graph_equivalence.mjs','closure_linear_stage_graphs.mjs','closure_bounded_point_cache.mjs'];
const entrypointHashes=Object.fromEntries(inputs.map(n=>[n,sha256(fs.readFileSync(new URL('./'+n,import.meta.url)))]));
const weightedPath=path.join(sourceTopic,'scripts/closing_weighted_tail.mjs');
const stagePath=path.join(sourceTopic,'scripts/950f-tail-subdivision.mjs');
const {createRecalibrationFactory}=await import(pathToFileURL(weightedPath));
const {subdividePhysical,buildStableStageGraphs}=await import(pathToFileURL(stagePath));
const packet=JSON.parse(fs.readFileSync(portPath,'utf8'));
const config=packet.config??packet.parameters??packet;
const t0=Date.now(),factory=createRecalibrationFactory(config),physical=factory.assemble();
function fingerprint(){
  const h=crypto.createHash('sha256');
  for(const c of physical.cells)for(const p of c.profiles)for(const x of [0,.1,.25,.5,.75,.9,1]){
    const z=p(x);h.update(JSON.stringify([z.r,z.drdx,z.logw,z.dlogwdx])+'\n');
  }
  return h.digest('hex');
}
const before=fingerprint();
const options={modes:3,spacing:2,linearFar:12,linearSteps:64};
const stages=subdividePhysical(physical,4,4);
const reference=buildStableStageGraphs(physical,stages,options);
installBoundedPointCache(factory,{count:physical.cells.length,controls:config.valleyControls??[],limit:96});
const after=fingerprint(),actual=buildRationalStableStageGraphs(physical,stages,options);
const counts={graphs:0,gains:0},mismatches=[];
let maxAbsolute=0,maxRelative=0;
for(const field of ['graphs','gains'])for(let n=0;n<reference[field].length;n++)for(let j=0;j<options.modes;j++){
  const a=reference[field][n][j],b=actual[field][n][j];counts[field]++;
  const absolute=Math.abs(a-b),relative=absolute/Math.max(1,Math.abs(a));
  maxAbsolute=Math.max(maxAbsolute,absolute);maxRelative=Math.max(maxRelative,relative);
  if(!Object.is(a,b)&&mismatches.length<12)mismatches.push({field,n,j,reference:a,actual:b,absolute,relative});
}
const report={status:before===after&&maxAbsolute===0?'PASS':'FAIL',
  assertion:'All graph and gain values are bitwise equal; sampled physical profiles unchanged.',
  options,rawDepth:4,shootingParts:4,counts,maxAbsolute,maxRelative,mismatches,
  headFingerprintBefore:before,headFingerprintAfter:after,
  entrypointHashes,sourceHashes:{weighted:sha256(fs.readFileSync(weightedPath)),stages:sha256(fs.readFileSync(stagePath))},
  portPath,portSHA256:sha256(fs.readFileSync(portPath)),
  elapsedSeconds:(Date.now()-t0)/1000,peakRSSKiB:process.resourceUsage().maxRSS,
  scope:'Finite floating equivalence check for this configuration, not an interval proof or infinite-tail result.'};
fs.writeFileSync(outPath,JSON.stringify(report,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify(report));
if(report.status!=='PASS')process.exitCode=1;
