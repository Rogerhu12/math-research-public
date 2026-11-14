// Fixed saved-tail diagnostics. No shooting solve, BVP, change of physical g,
// or replacement of the saved shooting state occurs in this script.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const src=name=>pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',name));
const {createFastSplitFluxMomentumTailEngine}=await import(src('f6tail_fast_split_flux_engine.mjs'));
const {createMomentumPhysicalJetEvaluator}=await import(src('f6tail_momentum_physical_jets.mjs'));
const {actualMetricFromDarbouxJets}=await import(src('f6tail_actual_metric.mjs'));
const {withCuspAwareRK}=await import(src('f6tail_cusp_grid.mjs'));
const argv=process.argv.slice(2),opt={};
for(let k=0;k<argv.length;k+=2){if(!argv[k].startsWith('--')||!argv[k+1])throw Error('key/value arguments required');opt[argv[k].slice(2)]=argv[k+1];}
if(!opt.packet||!opt.out)throw Error('--packet FILE --out FILE required');
if(fs.existsSync(opt.out))throw Error('output exists');
const started=Date.now(),buf=fs.readFileSync(opt.packet),packet=JSON.parse(zlib.gunzipSync(buf)),cfg=packet.config;
const cp=packet.response.checkpoint,M=cfg.modes,K=2*M,spacing=cfg.spacing;
const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts);
if(cp.states.length!==stages.cells.length+1||cp.states.some(s=>s.length!==K))throw Error('saved stage dimensions');
const cache=new Map();
function evaluator(c,N){
 const key=[c.rawCell,N].join(':');if(cache.has(key))return cache.get(key);
 let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing,quadrature:N,mu:c.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05});
 if(cfg.cuspAwareFlow)engine=withCuspAwareRK(engine);
 const obj={engine,jets:createMomentumPhysicalJetEvaluator(engine,{spacing})};cache.set(key,obj);return obj;
}
function stateAtNative(stage,x){const c=stages.cells[stage],y=new Float64Array(K+2);y.set(cp.states[stage+(x===0?1:0)]);if(x===1)for(let j=M;j<K;j++)y[j]*=c.portRatio;return y;}
function point(stage,x,y,N){
 const c=stages.cells[stage],p=c.profiles[0],{engine,jets}=evaluator(c,N),g=engine.geometry(p,x),j=jets(y,p,x),m=actualMetricFromDarbouxJets(g,j.perAngle);
 return {stage,rawCell:c.rawCell,rawSegment:c.rawSegment,part:c.part,x,r:g.r,quadrature:N,
  metric:m.actualMetricRelativeOperatorError,rr:m.actualMetricRelativeRR,rt:m.actualMetricRelativeRT,tt:m.actualMetricRelativeTT,
  radialCurlCorrection:m.maximumRadialCurlCorrection,darboux:j.maxDarboux,holonomy:m.angularHolonomyResidual,translationPeriod:m.translationPeriod,rootResidual:j.rootRelativeResidual};
}
const candidates=[],perCell=[];let max=null;
const count=Number(opt['raw-cells']??cfg.depth),N=cfg.quadrature;
for(let n=0;n<stages.cells.length;n++){
 const c=stages.cells[n];if(c.rawCell>=count)break;
 for(const x of [0,1]){const row=point(n,x,stateAtNative(n,x),N);if(!max||row.metric>max.metric)max=row;candidates.push(row);}
 if(n===stages.cells.length-1||stages.cells[n+1].rawCell!==c.rawCell){const rows=candidates.filter(q=>q.rawCell===c.rawCell),best=rows.reduce((a,b)=>a.metric>b.metric?a:b);perCell.push(best);console.log(JSON.stringify({phase:'native-cell',cell:c.rawCell,maximum:best.metric,elapsedSeconds:(Date.now()-started)/1000}));}
}
candidates.sort((a,b)=>b.metric-a.metric);
const selected=[];for(const row of candidates){if(!selected.some(q=>q.stage===row.stage)){selected.push(row);if(selected.length===Number(opt['selected-stages']??8))break;}}
const angular=[];for(const row of selected){const y=stateAtNative(row.stage,row.x);angular.push({native:row,refined:[1024,2048].filter(n=>n>N).map(n=>point(row.stage,row.x,y,n))});}
const radial=[];
for(const selectedRow of selected.slice(0,Number(opt['radial-stages']??4))){
 const stage=selectedRow.stage,c=stages.cells[stage],p=c.profiles[0],{engine}=evaluator(c,N),runs=[];
 for(const steps of [32,64,128]){
  let y=stateAtNative(stage,0),best=point(stage,0,y,N),endpoint=null;
  for(let k=0;k<steps;k++){y=engine.rk4(y,p,k/steps,1/steps);const row=point(stage,(k+1)/steps,y,N);if(row.metric>best.metric)best=row;if(k+1===steps)endpoint=row;}
  const target=stateAtNative(stage,1);let stateGap=0,stateScale=0;for(let j=0;j<K;j++){stateGap=Math.max(stateGap,Math.abs(y[j]-target[j]));stateScale=Math.max(stateScale,Math.abs(target[j]));}
  runs.push({steps,maximum:best,endpoint,relativeNativeStateGap:stateGap/Math.max(1e-300,stateScale)});
 }
 radial.push({stage,runs});console.log(JSON.stringify({phase:'radial-stage',stage,maxima:runs.map(r=>({steps:r.steps,metric:r.maximum.metric})),elapsedSeconds:(Date.now()-started)/1000}));
}
const report={scope:'Floating diagnosis on one fixed saved finite tail, no new shooting solve; native endpoints plus selected local IVPs. It is not a whole-domain bound or a new coupled solution.',
 packet:{path:path.resolve(opt.packet),bytes:buf.length,sha256:crypto.createHash('sha256').update(buf).digest('hex')},
 program:{path:path.resolve(process.argv[1]),sha256:crypto.createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex')},
 modes:M,spacing,physicalDepth:cfg.depth,shootingParts:cfg.shootingParts,originalSteps:cfg.steps,originalQuadrature:N,savedAudit:packet.response.audit,
 nativePoints:candidates.length,nativeMaximum:max,perCell,angular,radial,elapsedSeconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,nativeMaximum:max.metric,elapsedSeconds:report.elapsedSeconds}));
