// Read-only local analytic Jacobians on an already fully replayed failed tail.
// No state, physical parameter, residual definition or solver gate is changed.
// The diagnostic is a finite derivative/ULP scale, not an interval error bound.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const [topic,input,locator,runSummary,output]=process.argv.slice(2);
if(!output)throw Error('Need source topic, native failed record, locator, run summary, output');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const record=JSON.parse(gunzipSync(fs.readFileSync(input)));
const located=JSON.parse(fs.readFileSync(locator));
const run=JSON.parse(fs.readFileSync(runSummary));
if(located.input_sha256!==sha(input)||located.inputAccepted||!record.response.failed)
 throw Error('Exact failed record and its completed full-Jacobian locator required');
if(located.replayNormalizedResidual!==record.response.lastIteration.norm||
 located.originalGate!==2e-9||record.config.solveTolerance!==2e-9)
 throw Error('Original stopping-state and gate mismatch');
const sources={...located.source_sha256};
for(const [name,digest] of Object.entries(record.source_sha256)){
 const p=path.resolve(topic,'scripts',name);sources[p]=digest;
}
for(const [name,digest] of Object.entries(run.periodic_engine_sha256)){
 const p=path.resolve(topic,'scripts/periodic-quadrature',name);sources[p]=digest;
}
for(const name of fs.readdirSync(path.join(topic,'scripts/periodic-quadrature'))){
 if(name.endsWith('.mjs')&&!sources[path.resolve(topic,'scripts/periodic-quadrature',name)])
  throw Error('Unbound periodic source: '+name);
}
for(const [p,digest] of Object.entries(sources))if(sha(p)!==digest)throw Error('Source changed: '+p);
sources[path.resolve(process.argv[1])]=sha(process.argv[1]);
const root=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=root;
process.env.CLOSING_TAIL_CACHE=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const cfg=record.config,cp=record.response.checkpoint;
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,N=dn.tail.cells.length;
if(cp.states.length!==N+1||cp.states.some(x=>x.length!==K))throw Error('Full original state shape required');
const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
const target=cp.cutHeight.map(v=>v/radius**4);
const scales=new Float64Array(N+1);
scales[0]=Math.max(1e-250,...target.map(Math.abs));
for(let n=0;n<N;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
const buffer=new ArrayBuffer(8),view=new DataView(buffer);
function ulpTowardPositive(value){
 if(!Number.isFinite(value))throw Error('Finite state required');
 if(value===0)return Number.MIN_VALUE;
 view.setFloat64(0,value,false);
 const bits=view.getBigUint64(0,false);
 view.setBigUint64(0,value>0?bits+1n:bits-1n,false);
 return view.getFloat64(0,false)-value;
}
const requests=new Map();
for(const row of located.largestResidual.slice(0,3)){
 for(const n of [row.stage,row.stage-1])if(n>=0&&n<N){
  const key=n+':'+row.component;
  if(!requests.has(key))requests.set(key,{stage:n,component:row.component});
 }
}
const rows=[],cache=new Map();
const began=performance.now();
for(const req of requests.values()){
 const n=req.stage,j=req.component,cell=dn.tail.cells[n];
 let f=cache.get(n);
 if(!f){
  const x=new Float64Array(K+2);x.set(cp.states[n+1]);
  f=cell.engine.flowStateWithJacobian(x,cell.profiles,{stepsPerSegment:cfg.steps});
  cache.set(n,f);
 }
 const out=Float64Array.from(f.state.slice(0,K),(v,i)=>v/(i<M?1:cell.portRatio));
 let rowNorm=0,peak=-1,columnMax=0,columnPeak=-1,rowAbsSum=0;
 const inputUlp=ulpTowardPositive(cp.states[n+1][j]);
 for(let i=0;i<K;i++){
  const r=Math.abs(out[i]-cp.states[n][i])/scales[n];
  if(r>rowNorm){rowNorm=r;peak=i;}
  const d=Math.abs(f.tangent[i*K+j]/(i<M?1:cell.portRatio));
  if(d>columnMax){columnMax=d;columnPeak=i;}
  rowAbsSum+=Math.abs(f.tangent[j*K+i]/(j<M?1:cell.portRatio));
 }
 const locatorRow=located.largestResidual.find(r=>r.stage===n);
 if(locatorRow&&rowNorm!==locatorRow.normalizedResidual)throw Error('Local full-Jac flow no longer matches locator');
 const diagonal=f.tangent[j*K+j]/(j<M?1:cell.portRatio);
 rows.push({stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
  rawLeft:cell.rawLeft,rawRight:cell.rawRight,component:j,
  physicalMode:(j%M+1)*cfg.spacing,componentKind:j<M?'height-variable':'momentum-variable',
  inputNode:n+1,inputValue:cp.states[n+1][j],inputUlpTowardPositive:inputUlp,
  outputRowNorm:rowNorm,outputPeakComponent:peak,
  diagonalAnalyticDerivative:diagonal,
  selectedOutputRowAbsSum:rowAbsSum,selectedInputColumnMax:columnMax,
  selectedInputColumnPeak:columnPeak,
  oneInputUlpLinearizedOutputMaxNormalized:columnMax*inputUlp/scales[n],
  oneInputUlpLinearizedOutputMaxOverOriginalGate:columnMax*inputUlp/scales[n]/cfg.solveTolerance,
  normalizationScale:scales[n],recordedFiniteLinearGain:dn.tail.gains[n][j%M],
  minA:f.minA,minD:f.minD});
}
const result={scope:'Read-only analytic local Jacobians at named rows of a complete failed state already replayed by the original full-Jacobian path. A one-ULP derivative estimate diagnoses sensitivity; it is not a nonlinear finite-difference guarantee, error enclosure, refinement certificate or accepted tail.',
 input_sha256:sha(input),locator_sha256:sha(locator),run_summary_sha256:sha(runSummary),
 source_sha256:sources,command:process.argv,
 originalGate:cfg.solveTolerance,fullStateStoppingResidual:located.replayNormalizedResidual,
 modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,parts:cfg.shootingParts,
 steps:cfg.steps,stages:N,selectedRows:rows,statesChanged:false,
 originalSolverInvoked:false,seconds:(performance.now()-began)/1000};
fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({output_sha256:sha(output),rows:rows.length,
 maximumInputUlpDerivativeOverGate:Math.max(...rows.map(r=>r.oneInputUlpLinearizedOutputMaxOverOriginalGate)),
 seconds:result.seconds}));
