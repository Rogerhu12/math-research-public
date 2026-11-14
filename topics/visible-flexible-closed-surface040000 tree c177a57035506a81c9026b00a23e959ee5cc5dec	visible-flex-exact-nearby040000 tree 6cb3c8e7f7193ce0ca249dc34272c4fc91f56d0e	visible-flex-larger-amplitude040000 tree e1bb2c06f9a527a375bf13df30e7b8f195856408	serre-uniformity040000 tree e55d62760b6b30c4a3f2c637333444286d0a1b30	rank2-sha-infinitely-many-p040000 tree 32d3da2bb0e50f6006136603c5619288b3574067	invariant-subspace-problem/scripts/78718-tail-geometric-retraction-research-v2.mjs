// v2 uses the same mean equation with its base-plus-differential mean guess.
// Fixed-node R95 study on the actual failed W22 trial8 and accepted trial9.
// It reconstructs only two warm nodes, takes no RK/ODE/shooting/DN steps,
// and does not change the live worker or any saved candidate.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
import {createFourierRootSplitFluxEngine} from './78718-tail-fourier-root-split-engine.mjs';
import {prepareGeometricNodeRetraction} from './78718-tail-geometric-newton-retraction-v2.mjs';

const args=process.argv.slice(2),opt={};
for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.config||!opt.accepted||!opt.trial||!opt.out||fs.existsSync(opt.out))throw Error('Inputs and fresh output required');
const bindings=[];
function read(p){const b=fs.readFileSync(p);bindings.push({path:path.resolve(p),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});return JSON.parse(p.endsWith('.gz')?zlib.gunzipSync(b):b);}
function identity(p){if(p instanceof URL)p=fileURLToPath(p);const b=fs.readFileSync(p);return {path:path.resolve(p),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};}
function maxabs(a){return Math.max(...Array.from(a,Math.abs));}
function difference(a,b){return maxabs(Float64Array.from(a,(v,j)=>v-b[j]));}

const started=Date.now(),cfg=read(opt.config),accepted=read(opt.accepted),trial=read(opt.trial),
 priorReport=read(cfg.initialCheckpoint),prior=priorReport.response.checkpoint,
 physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),
 M=cfg.modes,K=2*M,N=cfg.quadrature,spacing=cfg.spacing,
 floor=cfg.projectionFloor??accepted.checkpoint.parameters.projectionFloor??.05,
 lambda=trial.trial.step,stage=trial.stage,node=stage+1;
if(!(lambda>0)||trial.trial.iteration!==0)throw Error('The intended initial Newton trial is required');

function context(i,projectionFloor=floor){
 const cell=stages.cells[i===0?0:i-1],profile=i===0?cell.profiles.at(-1):cell.profiles[0],x=i===0?1:0,ratio=i===0?cell.portRatio:1,
  options={modes:M,spacing,quadrature:N,mu:cell.mu,orientation:cfg.orientation,projectionFloor};
 return {cell,profile,x,ratio,engine:createFourierRootSplitFluxEngine(options),options};
}
function initialNode(i,ctx){
 const oldM=prior.parameters.modes,oldN=prior.parameters.quadrature,
  old=createFourierRootSplitFluxEngine({...ctx.options,modes:oldM,quadrature:oldN,projectionFloor:prior.parameters.projectionFloor??.05}),
  y=new Float64Array(2*oldM+2),oldStored=prior.states[i];
 for(let j=0;j<oldM;j++){y[j]=oldStored[j];y[oldM+j]=oldStored[oldM+j]*ctx.ratio;}
 const root=old.root(y,ctx.profile,ctx.x),raw=old.toRaw(y,ctx.profile,ctx.x,root).raw,extended=new Float64Array(K);
 for(let j=0;j<oldM;j++){extended[j]=raw[j];extended[M+j]=raw[oldM+j];}
 const initialized=ctx.engine.initializeFromRaw(extended,ctx.profile,ctx.x),stored=new Float64Array(K);
 for(let j=0;j<M;j++){stored[j]=initialized.state[j];stored[M+j]=initialized.state[M+j]/ctx.ratio;}
 return stored;
}
function rootSummary(ctx,stored){
 const y=new Float64Array(K+2);for(let j=0;j<M;j++){y[j]=stored[j];y[M+j]=stored[M+j]*ctx.ratio;}
 try{const r=ctx.engine.root(y,ctx.profile,ctx.x);return {ok:true,minA:r.e.minA,minD:r.e.minD,minS:r.e.minS,relativeResidual:r.err/r.scale};}
 catch(error){return {ok:false,error:String(error)};}
}

const ctx=context(node),base=initialNode(node,ctx),bad=Float64Array.from(trial.inputState),good=accepted.checkpoint.states[node],
 delta=Float64Array.from(base,(v,j)=>(bad[j]-v)/lambda),
 reconstructedHalf=Float64Array.from(base,(v,j)=>v+lambda*delta[j]/2),
 halfDifference=difference(reconstructedHalf,good);
if(halfDifference>2e-12*Math.max(1,maxabs(good)))throw Error('Reconstructed original direction does not recover actual accepted half-step');
const prepared=prepareGeometricNodeRetraction({engine:ctx.engine,profile:ctx.profile,x:ctx.x,state:base,delta,spacing,portRatio:ctx.ratio}),
 loose=context(node,1e-10),loosePrepared=prepareGeometricNodeRetraction({engine:loose.engine,profile:loose.profile,x:loose.x,state:base,delta,spacing,portRatio:loose.ratio});
const rows=[];
for(const factor of [1/64,1/32,1/16,1/8,1/4,1/2,1,2]){
 const step=lambda*factor,linear=Float64Array.from(base,(v,j)=>v+step*delta[j]),
  row={factor,step,linearOriginalFloor:rootSummary(ctx,linear),linearLooseFloor:rootSummary(loose,linear)};
 for(const [name,prep,c] of [['retractedOriginalFloor',prepared,ctx],['retractedLooseFloor',loosePrepared,loose]]){
  try{
   const result=prep.step(step,{detail:true}),error=difference(result.state,linear);
   row[name]={ok:true,...result.diagnostics,canonicalDifference:error,
    canonicalDifferenceOverStepSquared:error/step**2,root:rootSummary(c,result.state)};
  }catch(error){row[name]={ok:false,error:String(error)};}
 }
 rows.push(row);
}

// Node0's actual normalization can be checked without a new solve. The
// direction comes from the same accepted half-step relative to the warm.
const zero=context(0),base0=initialNode(0,zero),good0=accepted.checkpoint.states[0],
 delta0=Float64Array.from(base0,(v,j)=>(good0[j]-v)/(lambda/2)),
 stored0=prepareGeometricNodeRetraction({engine:zero.engine,profile:zero.profile,x:zero.x,state:base0,delta:delta0,spacing,portRatio:zero.ratio}),
 engineState=Float64Array.from(base0,(v,j)=>j>=M?v*zero.ratio:v),
 engineDelta=Float64Array.from(delta0,(v,j)=>j>=M?v*zero.ratio:v),
 engine0=prepareGeometricNodeRetraction({engine:zero.engine,profile:zero.profile,x:zero.x,state:engineState,delta:engineDelta,spacing,portRatio:1}),
 cutStep=lambda/16,a0=stored0.step(cutStep).state,b0=engine0.step(cutStep).state,
 cutNormalizationGap=maxabs(Float64Array.from(a0,(v,j)=>(j>=M?v*zero.ratio:v)-b0[j]));
const report={scope:'Actual W22 fixed-node retraction study only; no whole shooting residual or accepted nonlinear solution is computed.',
 inputs:bindings,helper:identity(new URL('78718-tail-geometric-newton-retraction-v2.mjs',import.meta.url)),
 script:identity(new URL('78718-tail-geometric-retraction-research-v2.mjs',import.meta.url)),
 M,N,spacing,stage,node,originalFloor:floor,looseFloor:1e-10,originalTrialStep:lambda,
 recoveredHalfStepMaxDifference:halfDifference,baseRoot:rootSummary(ctx,base),
 prepared:prepared.diagnostics,rows,
 node0:{portRatio:zero.ratio,step:cutStep,normalizationGap:cutNormalizationGap},
 BVP_calls:0,DN_calls:0,RK_steps:0,shooting_residual_evaluations:0,
 production_changed:false,seconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({output:identity(opt.out),stage,node,halfDifference,base:report.baseRoot,
 targetStep:rows.find(x=>x.factor===1),node0:report.node0,seconds:report.seconds}));
