// Locate finite-tail source metric error without another shooting solve.
// Optional higher-M results are local zero-padded-state diagnostics only.
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
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.packet||!opt.out||fs.existsSync(opt.out))throw Error('fresh --out and --packet required');
const started=Date.now(),buf=fs.readFileSync(opt.packet),packet=JSON.parse(zlib.gunzipSync(buf)),cfg=packet.config,cp=packet.response.checkpoint;
const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),oldM=cfg.modes,N=cfg.quadrature,K=2*oldM,steps=Number(opt.steps??cfg.steps),rawCell=Number(opt.cell??0);
if(cp.states.length!==stages.cells.length+1)throw Error('stage mismatch');
const cache=new Map();
function evaluator(c,M,N){const key=[c.rawCell,M,N].join(':');if(cache.has(key))return cache.get(key);let engine=createFastSplitFluxMomentumTailEngine({modes:M,spacing:cfg.spacing,quadrature:N,mu:c.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05});if(cfg.cuspAwareFlow)engine=withCuspAwareRK(engine);const obj={engine,jets:createMomentumPhysicalJetEvaluator(engine,{spacing:cfg.spacing})};cache.set(key,obj);return obj;}
function metricNorm(g,v,w){const A=(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])/g.E-1,B=(v[0]*w[0]+v[1]*w[1]+v[2]*w[2])/(g.r*Math.sqrt(g.E)),C=(w[0]*w[0]+w[1]*w[1]+w[2]*w[2])/(g.r*g.r)-1;return Math.max(Math.abs((A+C+Math.hypot(A-C,2*B))/2),Math.abs((A+C-Math.hypot(A-C,2*B))/2));}
function evaluate(stage,x,y,M=oldM,n=N,coordinates=false){const c=stages.cells[stage],p=c.profiles[0],{engine,jets}=evaluator(c,M,n),g=engine.geometry(p,x),j=jets(y,p,x),m=actualMetricFromDarbouxJets(g,j.perAngle,{returnCoordinates:coordinates});return {g,j,m,row:{stage,rawCell:c.rawCell,rawSegment:c.rawSegment,part:c.part,x,r:g.r,modes:M,quadrature:n,metric:m.actualMetricRelativeOperatorError,rr:m.actualMetricRelativeRR,rt:m.actualMetricRelativeRT,tt:m.actualMetricRelativeTT,curl:m.maximumRadialCurlCorrection,darboux:j.maxDarboux,rootResidual:j.rootRelativeResidual}};}
const perStage=[];let worst=null,worstState=null;
for(let stage=0;stage<stages.cells.length;stage++){
 const c=stages.cells[stage];if(c.rawCell!==rawCell)continue;
 let y=new Float64Array(K+2);y.set(cp.states[stage+1]);let best=null;const {engine}=evaluator(c,oldM,N),p=c.profiles[0];
 for(let k=0;k<=steps;k++){const ev=evaluate(stage,k/steps,y);if(!best||ev.row.metric>best.metric)best=ev.row;if(!worst||ev.row.metric>worst.metric){worst=ev.row;worstState=Float64Array.from(y);}if(k<steps)y=engine.rk4(y,p,k/steps,1/steps);}
 perStage.push(best);if(perStage.length%12===0)console.log(JSON.stringify({phase:'scan',stages:perStage.length,maximum:worst.metric,elapsedSeconds:(Date.now()-started)/1000}));
}
if(!worst)throw Error('no selected stages');
const base=evaluate(worst.stage,worst.x,worstState,oldM,N,true),angular=[];
for(const q of [N,1024,2048].filter((v,i,a)=>a.indexOf(v)===i)){
 const e=evaluate(worst.stage,worst.x,worstState,oldM,q,true),factor=q/N;if(!Number.isInteger(factor))throw Error('nested grid required');let sharedMax=0,sharedJetGap=0,sharedRadialGap=0;
 for(let j=0;j<N;j++){const h=j*factor;sharedMax=Math.max(sharedMax,metricNorm(e.g,e.m.radialDerivatives[h],e.m.angularDerivatives[h]));for(const key of ['ur','ut','urr','urt','utt'])sharedJetGap=Math.max(sharedJetGap,Math.abs(e.j.perAngle[h][key]-base.j.perAngle[j][key]));for(let k=0;k<3;k++)sharedRadialGap=Math.max(sharedRadialGap,Math.abs(e.m.radialDerivatives[h][k]-base.m.radialDerivatives[j][k]));}
 angular.push({...e.row,metricAtOriginalAngles:sharedMax,sharedJetGap,sharedRadialGap});
}
const high=evaluate(worst.stage,worst.x,worstState,oldM,2048),omega=high.j.perAngle.map(v=>{const S=high.g.r**2-v.ut**2,D=high.g.E*S-high.g.r**2*v.ur**2;return v.darboux*high.g.E**2*high.g.r**4/(D*Math.sqrt(D));});
const spectrum=[];for(let f=0;f<=180;f++){let c=0,s=0;for(let j=0;j<omega.length;j++){const t=2*Math.PI*f*j/omega.length;c+=omega[j]*Math.cos(t)/omega.length;s+=omega[j]*Math.sin(t)/omega.length;}spectrum.push({frequency:f,amplitude:Math.hypot(c,s)*(f?2:1)});}spectrum.sort((a,b)=>b.amplitude-a.amplitude);
const enlarged=[];
for(const m of [oldM,oldM+1,oldM+2,18,22,26].filter((v,i,a)=>v>=oldM&&a.indexOf(v)===i)){
 const y=new Float64Array(2*m+2);for(let j=0;j<oldM;j++){y[j]=worstState[j];y[m+j]=worstState[oldM+j];}y[2*m]=worstState[2*oldM];y[2*m+1]=worstState[2*oldM+1];
 const e=evaluate(worst.stage,worst.x,y,m,2048);let radialSlopeChange=0;for(let j=0;j<2048;j++)radialSlopeChange=Math.max(radialSlopeChange,Math.abs(e.j.perAngle[j].ur-high.j.perAngle[j].ur));enlarged.push({...e.row,radialHeightSlopeChange:radialSlopeChange});
}
const report={scope:'Floating source-jet diagnosis, not a new solved tail or a continuous certificate. Higher-M rows change local root/ODE derivatives on the zero-padded saved state.',packet:{path:path.resolve(opt.packet),bytes:buf.length,sha256:crypto.createHash('sha256').update(buf).digest('hex')},program:{path:path.resolve(process.argv[1]),sha256:crypto.createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex')},modes:oldM,quadrature:N,rawCell,steps,savedAudit:packet.response.audit,points:perStage.length*(steps+1),worst,perStage,angular,omegaSpectrumLargest:spectrum.slice(0,12),omegaRetainedMaximum:Math.max(...spectrum.filter(v=>v.frequency<=cfg.spacing*oldM).map(v=>v.amplitude)),omegaOmittedMaximum:Math.max(...spectrum.filter(v=>v.frequency>cfg.spacing*oldM).map(v=>v.amplitude)),enlarged,elapsedSeconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,maximum:worst.metric,stage:worst.stage,x:worst.x,elapsedSeconds:report.elapsedSeconds}));
