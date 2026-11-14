// Compare two complete, same-g responses at their actual common radial nodes.
// No radial ODE/DN is repeated. This is finite pointwise evidence, not a C2 bound.
import fs from 'node:fs';
import zlib from 'node:zlib';
import {createHash} from 'node:crypto';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {subdividePhysical} from './fd2d-gc-tail-stage-graphs.mjs';
import {createDeepSplitMomentumEngine} from './fd2d-gc-tail-deep-engine.mjs';
import {createMomentumPhysicalJetEvaluator} from './fd2d-metric-deep-momentum-physical-jets.mjs';

const [configFile,coarseFile,fineFile,coarseMeansFile,fineMeansFile,out]=process.argv.slice(2),
 hash=b=>createHash('sha256').update(b).digest('hex'),started=Date.now();
function read(file){const bytes=fs.readFileSync(file);return {bytes,sha256:hash(bytes),value:JSON.parse(file.endsWith('.gz')?zlib.gunzipSync(bytes):bytes)};}
const config=read(configFile),input=[read(coarseFile),read(fineFile)],
 responses=input.map(d=>d.value),prior=responses.map(d=>d.checkpoint),
 meansInput=[read(coarseMeansFile),read(fineMeansFile)],means=meansInput.map(d=>d.value);
if(responses.some(r=>!r.converged))throw Error('Both inputs must be complete converged finite responses');
const p=prior.map(c=>c.parameters),ignore=new Set(['modes','quadrature']),
 identity=p.map(v=>JSON.stringify(Object.fromEntries(Object.entries(v).filter(([key])=>!ignore.has(key)))));
if(identity[0]!==identity[1])throw Error('Physical or radial finite identity differs');
if(JSON.stringify(prior[0].rawNode)!==JSON.stringify(prior[1].rawNode))throw Error('Radial index maps differ');
if(prior[0].states.length!==prior[1].states.length)throw Error('Node counts differ');
for(let j=0;j<2;j++)if(means[j].source_response_sha256!==input[j].sha256||means[j].mean_heights.length+1!==prior[j].states.length)
 throw Error('Retained mean data is not bound to the response');
const cfg=config.value,factory=createRecalibrationFactory(cfg),
 cache=boundTailPointCaches(factory,cfg,{pointsPerEntry:8}),physical=factory.assemble(),
 stages=subdividePhysical(physical,p[0].physicalDepth,p[0].shootingParts),count=stages.cells.length+1;
if(count!==prior[0].states.length)throw Error('Rebuilt nodes differ');
const meanDifference=new Float64Array(count);
for(let i=count-2;i>=0;i--)meanDifference[i]=meanDifference[i+1]+(means[1].mean_heights[i]-means[0].mean_heights[i]);
const engineCaches=[new Map(),new Map()],jetCaches=[new Map(),new Map()],keys=['height','ur','ut','urr','urt','utt'],
 maxima=Object.fromEntries(keys.map(key=>[key,{absolute:0,node:null,angle:null}]));
let maximumNormalizedLChange=0,maximumQChange=0,maximumMeanHeightDifference=0,
 minimumLeading=Infinity,minimumProjectionD=Infinity,sampledPoints=0;
const selected=[],selectedNodes=new Set([0,8,18,28,36,2640,2880,...[8,12,16,24,32,64,128,160].map(i=>stages.rawNode[i])]);
for(let node=0;node<count;node++){
 const cell=stages.cells[node===0?0:node-1],profile=node===0?cell.profiles.at(-1):cell.profiles[0],x=node===0?1:0,
  ratio=node===0?cell.portRatio:1,values=[],roots=[];
 for(let j=0;j<2;j++){
  const M=p[j].modes,N=p[j].quadrature;
  if(!engineCaches[j].has(cell.mu)){
   const engine=createDeepSplitMomentumEngine({modes:M,spacing:p[j].spacing,quadrature:N,
    mu:cell.mu,orientation:p[j].orientation,projectionFloor:p[j].projectionFloor});
   engineCaches[j].set(cell.mu,engine);jetCaches[j].set(cell.mu,createMomentumPhysicalJetEvaluator(engine,{spacing:p[j].spacing}));
  }
  const engine=engineCaches[j].get(cell.mu),state=new Float64Array(2*M+2);state.set(prior[j].states[node]);
  for(let k=0;k<M;k++)state[M+k]*=ratio;
  if(j===1)state[2*M]=meanDifference[node];
  const root=engine.root(state,profile,x),jets=jetCaches[j].get(cell.mu)(state,profile,x);
  roots.push(root);values.push(jets);minimumLeading=Math.min(minimumLeading,jets.minA);minimumProjectionD=Math.min(minimumProjectionD,jets.minD);
 }
 for(let k=0;k<p[0].modes;k++)maximumQChange=Math.max(maximumQChange,Math.abs(prior[1].states[node][k]-prior[0].states[node][k]));
 for(let k=0;k<roots[1].L.length;k++)maximumNormalizedLChange=Math.max(maximumNormalizedLChange,Math.abs(roots[1].L[k]-(roots[0].L[k]??0)));
 maximumMeanHeightDifference=Math.max(maximumMeanHeightDifference,Math.abs(meanDifference[node]));
 const N=p[0].quadrature,scale=p[1].quadrature/N;
 if(!Number.isInteger(scale))throw Error('Fine angular grid must contain the coarse grid');
 const local=Object.fromEntries(keys.map(key=>[key,0])),absolutePerturbation=Array.from({length:2},()=>({nonmeanHeight:0,ur:0,ut:0,urr:0,urt:0,utt:0}));
 for(let angle=0;angle<N;angle++){
  if(selectedNodes.has(node))for(let j=0;j<2;j++){
   const sample=values[j].perAngle[j===0?angle:scale*angle],g=roots[j].g,
    wr=g.dlogwdx===0?0:Math.sign(g.drdx)*Math.sign(g.dlogwdx)*Math.exp(g.logw-Math.log(Math.abs(g.drdx))+Math.log(Math.abs(g.dlogwdx)));
   let nonmean=0;for(let k=0;k<p[j].modes;k++)nonmean+=g.r**4*prior[j].states[node][k]*Math.cos(p[j].spacing*(k+1)*2*Math.PI*angle/N);
   const q=absolutePerturbation[j];q.nonmeanHeight=Math.max(q.nonmeanHeight,Math.abs(nonmean));
   for(const key of ['ur','ut','urr','urt','utt'])q[key]=Math.max(q[key],Math.abs(sample[key]-(key==='ur'?g.w:key==='urr'?wr:0)));
  }
  for(const key of keys){const delta=Math.abs(values[1].perAngle[scale*angle][key]-values[0].perAngle[angle][key]);
   if(!Number.isFinite(delta))throw Error('Nonfinite physical-jet difference');local[key]=Math.max(local[key],delta);
   if(delta>maxima[key].absolute)maxima[key]={absolute:delta,node,rawCell:cell.rawCell,rawSegment:cell.rawSegment,angle,theta:2*Math.PI*angle/N};
  }sampledPoints++;
 }
 if(selectedNodes.has(node))selected.push({node,rawCell:cell.rawCell,rawSegment:cell.rawSegment,r:roots[0].g.r,logw:roots[0].g.logw,meanDifference:meanDifference[node],maximumDifferences:local,absolutePerturbation,absolutePerturbationScope:'Actual finite angular samples; nonmean height and derivatives relative to the rotational profile. Floating differences are not rigorous bounds.'});
}
const report={schema:'fd2d-same-g-actual-node-mode-refinement-v1',
 source:{path:import.meta.filename,sha256:hash(fs.readFileSync(import.meta.filename))},
 config:{path:configFile,sha256:config.sha256},
 responses:input.map((r,j)=>({path:[coarseFile,fineFile][j],sha256:r.sha256,modes:p[j].modes,quadrature:p[j].quadrature,residual:responses[j].residual,audit:responses[j].audit})),
 retainedMeans:meansInput.map((r,j)=>({path:[coarseMeansFile,fineMeansFile][j],sha256:r.sha256,inputHash:means[j].inputHash})),
 radial_nodes:count,common_angles:p[0].quadrature,sampledPoints,maxima,maximumNormalizedLChange,maximumQChange,
 maximumMeanHeightDifference,cutMeanDifference:meanDifference[0],minimumLeading,minimumProjectionD,selected,
 pointCache:cache,seconds:(Date.now()-started)/1000,
 scope:'Actual complete same-g finite responses, compared at common nodes and common angular samples; finite mean anchor at node160. No radial re-integration, continuous enclosure, infinite-tail proof, or successful strong surface is asserted.'};
fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({out,seconds:report.seconds,maxima,maximumNormalizedLChange,maximumMeanHeightDifference,sampledPoints}));
