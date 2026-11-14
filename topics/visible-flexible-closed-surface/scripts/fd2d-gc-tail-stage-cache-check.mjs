// Actual small-stage arithmetic comparison and disk round trip, no BVP claim.
import fs from 'node:fs';
import crypto from 'node:crypto';
import v8 from 'node:v8';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {createSplitFluxCompactTailDN as original} from './fd2d-gc-tail-full160-split.mjs';
import {createSplitFluxCompactTailDN as cached} from './fd2d-gc-tail-full160-cached-split.mjs';
import {createSequentialStageCache} from './fd2d-gc-tail-sequential-stage-cache.mjs';
import {createFourierProductVariationalEngine} from './78718-tail-fourier-product-flow.mjs';
const [input,output,cacheRoot]=process.argv.slice(2);
if(!input||!output||!cacheRoot)throw Error('Usage: node check.mjs INPUT OUTPUT CACHE_DIRECTORY');
const start=Date.now(),config=JSON.parse(fs.readFileSync(input,'utf8'));
const cfg={...config,protectCell:20,valleyControls:config.valleyControls.slice(0,20),
  pulseCaps:config.pulseCaps?.slice(0,20),valleyCaps:config.valleyCaps?.slice(0,20),
  warpWeightLevels:config.warpWeightLevels?.slice(0,20),modes:2,spacing:2,depth:2,
  shootingParts:2,steps:8,quadrature:32,linearFar:8,linearSteps:16,
  projectionFloor:.05,fastJacobian:true,cuspAwareFlow:true};
const factory=createRecalibrationFactory(cfg);
boundTailPointCaches(factory,cfg,{pointsPerEntry:64});
const physical=factory.assemble();let disk=null;
const a=original({...cfg,tail:physical}),b=cached({...cfg,tail:physical,
  stageEvaluationCache:{begin:(states,withJac)=>disk?.begin(states,withJac)}});
for(const dn of [a,b]){
  const done=new Set();
  for(const c of dn.tail.cells){
    if(done.has(c.engine))continue;done.add(c.engine);
    const old={...c.engine},options={modes:cfg.modes,spacing:cfg.spacing,
      quadrature:cfg.quadrature,mu:c.mu,orientation:1,projectionFloor:.05,cuspAwareFlow:true};
    Object.assign(c.engine,createFourierProductVariationalEngine(options,old));
  }
}
const events=[],makeCache=()=>createSequentialStageCache({cacheRoot,entryURL:import.meta.url,
  tail:b.tail,backend:'fourier-product-moments-v1',
  dependencyBlobs:JSON.parse(fs.readFileSync(new URL('../notes/closing_tail_dependency_blobs.json',import.meta.url),'utf8')),
  diagnostic:row=>events.push(row)});
disk=makeCache();if(!disk)throw Error('The actual disk cache was not available');
const r=a.cutJets(new Float64Array(4)).radius,target=Float64Array.of(1e-12/r**4,0),
  states=a.tail.initial(target),scales=new Float64Array(states.length);
scales[0]=Math.max(1e-250,...target.map(Math.abs));
for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(a.tail.gains[n][0]);
function compare(x,y){
  let count=0,identical=0,maxDifference=0;
  function scalar(u,v){count++;if(Object.is(u,v))identical++;
    if(typeof u==='number'&&typeof v==='number'&&Number.isFinite(u)&&Number.isFinite(v))
      maxDifference=Math.max(maxDifference,Math.abs(u-v));
    else if(!Object.is(u,v))throw Error('Scalar kind changed');}
  for(const key of ['norm','minA','minD'])scalar(x[key],y[key]);
  for(let n=0;n<x.flows.length;n++){
    for(const key of ['out','J']){
      if(x.flows[n][key]===null){scalar(null,y.flows[n][key]);continue;}
      for(let j=0;j<x.flows[n][key].length;j++)scalar(x.flows[n][key][j],y.flows[n][key][j]);
    }
    for(const key of ['meanHeight','minA','minD'])scalar(x.flows[n][key],y.flows[n][key]);
    for(let j=0;j<x.residuals[n].length;j++)scalar(x.residuals[n][j],y.residuals[n][j]);
  }
  for(let j=0;j<x.end.length;j++)scalar(x.end[j],y.end[j]);
  if(count!==identical)throw Error('Actual scalar output changed');
  return {count,bitwise_identical:identical,maximum_absolute_difference:maxDifference};
}
const checks=[];
for(const withJac of [true,false]){
  const baseline=a.tail.evaluate(states,target,withJac,scales),
    first=b.tail.evaluate(states,target,withJac,scales);
  const firstCheck=compare(baseline,first);
  disk=makeCache();
  const replay=b.tail.evaluate(states,target,withJac,scales),replayCheck=compare(baseline,replay);
  checks.push({withJac,first:firstCheck,replayed_from_disk:replayCheck});
}
const sha=file=>crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const result={schema:'fd2d-serial-stage-cache-actual-equality-v1',completed:true,
  source_sha256:sha(new URL(import.meta.url)),input_sha256:sha(input),
  fixture:{protectCell:20,physicalDepth:2,modes:2,spacing:2,quadrature:32,parts:2,
    steps:8,linearFar:8,linearSteps:16,height:[1e-12,0]},
  scope:'Actual small derived fixture only. Original and cached equations/flows are compared; no nonlinear BVP convergence or full160 result is asserted.',
  checks,cache_metadata:disk.metadata,events,
  runtime:{seconds:(Date.now()-start)/1000,heap_size_limit:v8.getHeapStatistics().heap_size_limit,
    resources:process.resourceUsage(),memory:process.memoryUsage()}};
fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({output,checks,seconds:result.runtime.seconds,
  evaluations:events.filter(x=>x.event==='stage_cache_evaluation_complete'),peak_rss_kb:result.runtime.resources.maxRSS}));
