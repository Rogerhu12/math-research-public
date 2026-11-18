// Identify the actual residual component at a row already selected by the
// published full-map consistency probe. Its legacy `component` field labels
// map disagreement, and is not a residual-component label when the maps agree.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,input,comparison,runSummary,output]=process.argv.slice(2);
if(!output)throw Error('Need source topic, failed state, comparison, native run summary, output');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const rec=JSON.parse(gunzipSync(fs.readFileSync(input)));
const cmp=JSON.parse(fs.readFileSync(comparison)),run=JSON.parse(fs.readFileSync(runSummary));
if(cmp.input_sha256!==sha(input)||!rec.response.failed||
 cmp.normalized_variational_residual!==rec.response.lastIteration.norm)
 throw Error('A matching failed state and exact original full-Jacobian replay are required');
const sources={};
for(const [name,h] of Object.entries(rec.source_sha256))sources[path.resolve(topic,'scripts',name)]=h;
for(const [name,h] of Object.entries(run.periodic_engine_sha256))
 sources[path.resolve(topic,'scripts/periodic-quadrature',name)]=h;
for(const [p,h] of Object.entries(sources))if(sha(p)!==h)throw Error('Original source changed: '+p);
sources[path.resolve(process.argv[1])]=sha(process.argv[1]);
const root=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=root;
process.env.CLOSING_TAIL_CACHE=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const cfg=rec.config,cp=rec.response.checkpoint,M=cfg.modes,K=2*M;
if(cfg.solveTolerance!==2e-9||!cp.cutHeight.every((v,j)=>Object.is(v,rec.request.height[j])))
 throw Error('Original gate and unchanged physical target required');
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
if(cp.states.length!==dn.tail.cells.length+1)throw Error('Original complete shooting grid required');
const r=dn.tail.cells[0].profiles.at(-1)(1).r,target=cp.cutHeight.map(v=>v/r**4);
const scales=new Float64Array(cp.states.length);scales[0]=Math.max(1e-250,...target.map(Math.abs));
for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
const view=new DataView(new ArrayBuffer(8));
function ulp(x){
 x=Math.abs(x);if(x===0)return Number.MIN_VALUE;
 view.setFloat64(0,x,false);view.setBigUint64(0,view.getBigUint64(0,false)+1n,false);
 return view.getFloat64(0,false)-x;
}
const n0=cmp.worst_variational_residual.stage,rows=[];
const began=performance.now();
for(const n of [n0-1,n0]){
 if(n<0)continue;
 const cell=dn.tail.cells[n],x=new Float64Array(K+2);x.set(cp.states[n+1]);
 const f=cell.engine.flowStateWithJacobian(x,cell.profiles,{stepsPerSegment:cfg.steps});
 const out=Float64Array.from(f.state.slice(0,K),(v,j)=>v/(j<M?1:cell.portRatio));
 const res=Float64Array.from(out,(v,j)=>v-cp.states[n][j]);
 let k=0;for(let j=1;j<K;j++)if(Math.abs(res[j])>Math.abs(res[k]))k=j;
 const norm=Math.abs(res[k])/scales[n];
 if(n===n0&&norm!==cmp.normalized_variational_residual)throw Error('Named full-Jacobian row no longer matches');
 rows.push({stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
  rawLeft:cell.rawLeft,rawRight:cell.rawRight,residualComponent:k,
  physicalMode:cfg.spacing*(k%M+1),kind:k<M?'height-variable':'momentum-variable',
  stateValue:cp.states[n][k],flowValue:out[k],signedResidual:res[k],normalizedResidual:norm,
  scale:scales[n],componentUlp:ulp(cp.states[n][k]),
  absoluteResidualInUlps:Math.abs(res[k])/ulp(cp.states[n][k]),
  minA:f.minA,minD:f.minD});
}
const data={scope:'Only two named rows of an already fully replayed failed state are read. The actual residual component is identified independently of the old map-difference component field. No state, configuration or acceptance gate is changed; no solver is invoked.',
 input_sha256:sha(input),full_map_comparison_sha256:sha(comparison),run_summary_sha256:sha(runSummary),
 source_sha256:sources,command:process.argv,originalGate:cfg.solveTolerance,
 expectedFullResidual:cmp.normalized_variational_residual,selectedStage:n0,rows,
 seconds:(performance.now()-began)/1000,statesChanged:false,solverInvoked:false};
fs.writeFileSync(output,JSON.stringify(data,null,2)+'\n');
console.log(JSON.stringify({sha256:sha(output),selected:rows.at(-1),seconds:data.seconds}));
