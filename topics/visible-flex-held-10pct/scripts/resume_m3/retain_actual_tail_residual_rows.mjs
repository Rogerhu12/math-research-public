// One original full-Jacobian replay. Retain every over-gate component and
// complete affected/upstream rows, so ties are not lost by a per-stage argmax.
// This read-only program changes no state and invokes no Newton solver.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,input,sourcePlan,output]=process.argv.slice(2);
if(!output||fs.existsSync(output))throw Error('Need a new complete-row output');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const record=JSON.parse(gunzipSync(fs.readFileSync(input)));
const cp=record.response.checkpoint,cfg=record.config;
if(!record.response.failed||!cp?.states||!cp?.cutHeight)throw Error('A retained actual failed state is required');
const manifest=JSON.parse(fs.readFileSync(sourcePlan));
const sources={...manifest.source_sha256};
for(const [name,digest] of Object.entries(record.source_sha256))sources[path.resolve(topic,'scripts',name)]=digest;
sources[path.resolve(process.argv[1])]=sha(process.argv[1]);
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Source changed: '+file);
const source=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,N=dn.tail.cells.length;
if(cp.states.length!==N+1||cp.states.some(row=>row.length!==K||row.some(v=>!Number.isFinite(v))))
 throw Error('The original complete finite grid is required');
const states=cp.states.map(v=>Float64Array.from(v)),radius=dn.tail.cells[0].profiles.at(-1)(1).r;
const target=Float64Array.from(cp.cutHeight,v=>v/radius**4),scales=new Float64Array(N+1);
scales[0]=Math.max(1e-250,...target.map(Math.abs));
for(let n=0;n<N;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
const begin=performance.now(),ev=dn.tail.evaluate(states,target,true,scales);
if(!Object.is(ev.norm,record.response.lastIteration.norm))throw Error('The full original stopping residual did not replay exactly');
const view=new DataView(new ArrayBuffer(8));
function neighbor(v,direction){
 if(v===0)return direction*Number.MIN_VALUE;
 view.setFloat64(0,v,false);const bits=view.getBigUint64(0,false);
 view.setBigUint64(0,(v>0)===(direction>0)?bits+1n:bits-1n,false);
 return view.getFloat64(0,false);
}
function component(n,j){
 const state=states[n][j],flow=ev.flows[n].out[j],residual=ev.residuals[n][j];
 const direction=Math.sign(residual),adjacent=direction?neighbor(state,direction):state;
 return {component:j,physicalMode:cfg.spacing*(j%M+1),kind:j<M?'height':'momentum',
  state,flow,signedResidual:residual,normalizationScale:scales[n],
  normalizedResidual:Math.abs(residual)/scales[n],direction,adjacentTowardFlow:adjacent,
  directedStep:adjacent-state,isExactlyOneDirectedNeighbor:direction!==0&&Object.is(adjacent,flow)};
}
const over=[],maxima=[];let otherMaximum=0;
for(let n=0;n<N;n++){
 let largest=0,largestComponent=0;
 for(let j=0;j<K;j++){
  const value=Math.abs(ev.residuals[n][j])/scales[n];
  if(value>largest){largest=value;largestComponent=j;}
  if(value>=cfg.solveTolerance)over.push({stage:n,...component(n,j)});
  else otherMaximum=Math.max(otherMaximum,value);
 }
 const cell=dn.tail.cells[n];
 maxima.push({stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
  rawLeft:cell.rawLeft,rawRight:cell.rawRight,component:largestComponent,
  normalizedResidual:largest,minA:ev.flows[n].minA,minD:ev.flows[n].minD});
}
const relevant=[...new Set(over.flatMap(r=>r.stage>0?[r.stage-1,r.stage]:[r.stage]))].sort((a,b)=>a-b);
const boundary={cut:Math.max(...target.map((v,j)=>Math.abs(states[0][j]-v)/scales[0])),
 deep:Math.max(...ev.end.map(v=>Math.abs(v)/scales[N]))};
const rows=relevant.map(n=>({...maxima[n],components:Array.from({length:K},(_,j)=>component(n,j))}));
const result={scope:'One original full-Jacobian evaluation of the same actual failed finite state. Every component at or above the original stopping gate is retained; full implicated and upstream rows are saved without recomputing their flows. No state change or solver call.',
 command:process.argv,input:{path:path.resolve(input),sha256:sha(input)},
 originalSourcePlan:{path:path.resolve(sourcePlan),sha256:sha(sourcePlan)},source_sha256:sources,
 modes:M,stages:N,quadrature:cfg.quadrature,shootingParts:cfg.shootingParts,
 originalGate:cfg.solveTolerance,originalFailure:record.response.failed,
 before:{norm:ev.norm,minA:ev.minA,minD:ev.minD,boundary},
 completeOverGateComponents:over,otherComponentMaximum:otherMaximum,
 fullAffectedAndUpstreamRows:rows,topStageMaxima:maxima.toSorted((a,b)=>b.normalizedResidual-a.normalizedResidual).slice(0,12),
 statesChanged:false,original_solver_invoked:false,seconds:(performance.now()-begin)/1000};
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Executed source changed: '+file);
fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({output,sha256:sha(output),norm:ev.norm,overGate:over,otherMaximum,boundary,seconds:result.seconds}));
