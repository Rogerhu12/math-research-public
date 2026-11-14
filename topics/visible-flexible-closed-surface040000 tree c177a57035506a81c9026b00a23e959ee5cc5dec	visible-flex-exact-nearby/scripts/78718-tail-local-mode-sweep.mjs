// Coarse high-mode local diagnostics along an unchanged saved-tail trajectory.
// This deliberately does not solve a high-mode tail or a coupled BVP.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
const srcRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
const src=name=>pathToFileURL(path.join(srcRoot,'topics/large-amplitude-twist-flex/scripts',name));
const {createFastSplitFluxMomentumTailEngine}=await import(src('f6tail_fast_split_flux_engine.mjs'));
const {createMomentumPhysicalJetEvaluator}=await import(src('f6tail_momentum_physical_jets.mjs'));
const {actualMetricFromDarbouxJets}=await import(src('f6tail_actual_metric.mjs'));
const {withCuspAwareRK}=await import(src('f6tail_cusp_grid.mjs'));
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.packet||!opt.locations||!opt.out||fs.existsSync(opt.out))throw Error('fresh output and two inputs required');
const started=Date.now(),pb=fs.readFileSync(opt.packet),packet=JSON.parse(zlib.gunzipSync(pb)),cfg=packet.config,cp=packet.response.checkpoint;
const lb=fs.readFileSync(opt.locations),locations=JSON.parse(lb),oldM=cfg.modes,N=cfg.quadrature,steps=cfg.steps;
if(locations.packet.sha256!==crypto.createHash('sha256').update(pb).digest('hex'))throw Error('location input mismatch');
const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),rawCell=Number(opt.cell??0),stride=Number(opt.stride??4);
const modes=[oldM,...String(opt.modes??'18,22').split(',').map(Number)].filter((v,i,a)=>v>=oldM&&a.indexOf(v)===i),cache=new Map();
function evFor(c,M){const key=[c.rawCell,M].join(':');if(cache.has(key))return cache.get(key);let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:cfg.spacing,quadrature:N,mu:c.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05});if(cfg.cuspAwareFlow)engine=withCuspAwareRK(engine);const o={engine,jets:createMomentumPhysicalJetEvaluator(engine,{spacing:cfg.spacing})};cache.set(key,o);return o;}
function resize(y,M){if(M===oldM)return y;const z=new Float64Array(2*M+2);for(let j=0;j<oldM;j++){z[j]=y[j];z[M+j]=y[oldM+j];}z[2*M]=y[2*oldM];z[2*M+1]=y[2*oldM+1];return z;}
const maxByM=new Map(),perStage=[],minLeading=new Map(),minD=new Map();let points=0;
for(let n=0;n<stages.cells.length;n++){
 const c=stages.cells[n];if(c.rawCell!==rawCell)continue;
 const original=evFor(c,oldM),p=c.profiles[0],loc=locations.perStage.find(q=>q.stage===n),peak=loc?Math.round(loc.x*steps):-1;
 let y=new Float64Array(2*oldM+2);y.set(cp.states[n+1]);const local=new Map();
 for(let k=0;k<=steps;k++){
  if(k%stride===0||k===steps||k===peak){
   const x=k/steps;points++;
   for(const M of modes){const {engine,jets}=evFor(c,M),z=resize(y,M),g=engine.geometry(p,x),j=jets(z,p,x),metric=actualMetricFromDarbouxJets(g,j.perAngle),row={modes:M,stage:n,rawSegment:c.rawSegment,part:c.part,x,r:g.r,metric:metric.actualMetricRelativeOperatorError,rr:metric.actualMetricRelativeRR,rt:metric.actualMetricRelativeRT,tt:metric.actualMetricRelativeTT,darboux:j.maxDarboux,minLeading:j.minA,minD:j.minD};if(!local.has(M)||row.metric>local.get(M).metric)local.set(M,row);if(!maxByM.has(M)||row.metric>maxByM.get(M).metric)maxByM.set(M,row);minLeading.set(M,Math.min(minLeading.get(M)??Infinity,j.minA));minD.set(M,Math.min(minD.get(M)??Infinity,j.minD));}
  }
  if(k<steps)y=original.engine.rk4(y,p,k/steps,1/steps);
 }
 perStage.push({stage:n,maxima:[...local.values()]});if(perStage.length%12===0)console.log(JSON.stringify({stages:perStage.length,points,maxima:[...maxByM.values()].map(v=>({modes:v.modes,metric:v.metric})),elapsedSeconds:(Date.now()-started)/1000}));
}
const report={scope:'Floating coarse local zero-padding diagnosis along the unchanged original finite-M trajectory. It is not a high-M trajectory, solved tail, or continuous bound.',packet:{path:path.resolve(opt.packet),bytes:pb.length,sha256:crypto.createHash('sha256').update(pb).digest('hex')},locationReport:{path:path.resolve(opt.locations),sha256:crypto.createHash('sha256').update(lb).digest('hex')},program:{path:path.resolve(process.argv[1]),sha256:crypto.createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex')},originalModes:oldM,quadrature:N,originalSteps:steps,rawCell,stride,points,modeCount:modes.length,maxima:[...maxByM.values()],guardMinima:modes.map(m=>({modes:m,minLeading:minLeading.get(m),minD:minD.get(m)})),perStage,elapsedSeconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,points,maxima:report.maxima.map(v=>({modes:v.modes,metric:v.metric,stage:v.stage,x:v.x})),elapsedSeconds:report.elapsedSeconds}));
