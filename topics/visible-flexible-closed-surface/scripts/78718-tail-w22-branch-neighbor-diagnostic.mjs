// One saved W22 trial and the actual accepted neighboring iterate.
// Uses the same complete Fourier-root engine as the live worker, without a DN solve.
import fs from 'node:fs';import path from 'node:path';import zlib from 'node:zlib';import crypto from 'node:crypto';import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
import {createFourierRootSplitFluxEngine} from './78718-tail-fourier-root-split-engine.mjs';
const {integrationGrid}=await import(pathToFileURL(path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.config||!opt.accepted||!opt.trial||!opt.out||fs.existsSync(opt.out))throw Error('inputs and fresh output required');
const inputs=[];function read(p){const b=fs.readFileSync(p);inputs.push({path:path.resolve(p),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')});return JSON.parse(p.endsWith('.gz')?zlib.gunzipSync(b):b);}
const started=Date.now(),cfg=read(opt.config),accepted=read(opt.accepted),trial=read(opt.trial),M=cfg.modes,N=cfg.quadrature,K=2*M,
 floor=cfg.projectionFloor??accepted.checkpoint.parameters.projectionFloor??.05,looseFloor=1e-10,
 physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),stage=trial.stage,cell=stages.cells[stage],p=cell.profiles[0];
if(accepted.checkpoint.parameters.modes!==M||trial.inputState.length!==K)throw Error('W22 dimensions do not match');
const options={modes:M,spacing:cfg.spacing,quadrature:N,mu:cell.mu,orientation:cfg.orientation,projectionFloor:floor},
 e=createFourierRootSplitFluxEngine(options),loose=createFourierRootSplitFluxEngine({...options,projectionFloor:looseFloor});
function minIndex(rt){let i=0;for(let n=1;n<N;n++)if(rt.e.rows[n].A<rt.e.rows[i].A)i=n;return i;}
function summary(rt){const n=minIndex(rt),v=rt.e.rows[n];return {minA:rt.e.minA,minD:rt.e.minD,minS:rt.e.minS,iterations:rt.iterations,rootRelative:rt.err/rt.scale,r:rt.g.r,w:rt.g.w,theta:2*Math.PI*n/N,K:v.K,Pt:v.Pt};}
function attempt(engine,y,x,guess){try{const rt=engine.root(y,p,x,guess);return {ok:true,rt,report:summary(rt)};}catch(error){return {ok:false,report:{error:String(error)}};}}
function walk(initial){
 let state=new Float64Array(K+2);state.set(initial);const fields=[],grid=integrationGrid(cfg.steps,p.integrationBreakpoints??[]);let failure=null;
 function field(y,x,step,phase){
  const out=attempt(e,y,x);if(!out.ok){failure={state:Float64Array.from(y),x,step,phase,index:fields.length,error:out.report.error};throw Error(out.report.error);}
  fields.push({state:Float64Array.from(y),x,root:out.rt,step,phase});
  return e.rhs(y,p,x,false,out.rt);
 }
 try{
  for(let n=0;n<grid.length-1;n++){
   const x=grid[n],h=grid[n+1]-x,a=field(state,x,n,'a'),tmp=new Float64Array(K+2);
   for(let j=0;j<K+2;j++)tmp[j]=state[j]+h*a[j]/2;
   const b=field(tmp,x+h/2,n,'b');for(let j=0;j<K+2;j++)tmp[j]=state[j]+h*b[j]/2;
   const c=field(tmp,x+h/2,n,'c');for(let j=0;j<K+2;j++)tmp[j]=state[j]+h*c[j];
   const d=field(tmp,x+h,n,'d');state=Float64Array.from(state,(v,j)=>v+h*(a[j]+2*b[j]+2*c[j]+d[j])/6);
  }
  return {ok:true,fields,report:{fields:fields.length,minA:Math.min(...fields.map(v=>v.root.e.minA)),minD:Math.min(...fields.map(v=>v.root.e.minD))}};
 }catch(error){return {ok:false,fields,failure,report:{fields:fields.length,error:String(error),failure:failure?{x:failure.x,step:failure.step,phase:failure.phase}:null,minA:fields.length?Math.min(...fields.map(v=>v.root.e.minA)):null}};}
}
function pathRoots(engine,from,to,x){
 let a=attempt(engine,from,x);if(!a.ok)return {report:{ok:false,error:a.report.error}};
 let last=a.rt,lastState=Float64Array.from(from),alpha=0;
 for(let k=1;k<=32;k++){
  const t=k/32,y=Float64Array.from(from,(v,j)=>v+t*(to[j]-v)),b=attempt(engine,y,x,last.L);
  if(!b.ok)return {rt:last,state:lastState,report:{ok:false,lastAlpha:alpha,lastRoot:summary(last),failureAlpha:t,error:b.report.error}};
  last=b.rt;lastState=y;alpha=t;
 }
 return {rt:last,state:lastState,report:{ok:true,lastAlpha:1,root:summary(last)}};
}
function physicalDifference(reference,rt,y){
 const n=minIndex(rt),old=reference.root.e.rows[n],now=rt.e.rows[n],g=rt.g,theta=2*Math.PI*n/N;
 let low=0,high=0;const terms=[];
 for(let j=0;j<M;j++){
  const ell=cfg.spacing*(j+1),term=-g.E*ell*ell*g.r**3/g.w*(y[j]-reference.state[j])*Math.cos(ell*theta);
  if(j<15)low+=term;else high+=term;terms.push({mode:j+1,frequency:ell,E_delta_Pt:term});
 }
 terms.sort((a,b)=>Math.abs(b.E_delta_Pt)-Math.abs(a.E_delta_Pt));
 return {theta,referenceA:old.A,comparedA:now.A,deltaA:now.A-old.A,deltaK:now.K-old.K,
  E_delta_Pt:g.E*(now.Pt-old.Pt),resolvedM15Contribution:low,newW22Contribution:high,
  reconstructionGap:low+high-g.E*(now.Pt-old.Pt),largestTerms:terms.slice(0,6)};
}
const base=walk(accepted.checkpoint.states[stage+1]),bad=walk(trial.inputState);
if(!base.ok)throw Error('Actual accepted input failed local replay');
const report={scope:'Only one actual saved W22 trial stage and its accepted neighbor; low floor is fixed-point diagnosis, not a new solution or acceptance.',
 inputs,modes:M,quadrature:N,stage,rawCell:cell.rawCell,rawSegment:cell.rawSegment,originalFloor:floor,looseFloor,
 acceptedIteration:accepted.iteration,savedTrial:trial.trial,acceptedLocal:base.report,trialLocal:bad.report};
if(!bad.ok){
 const f=bad.failure,ref=base.fields[f.index];if(!ref||ref.x!==f.x)throw Error('Accepted field alignment mismatch');
 const seeded=attempt(e,f.state,f.x,ref.root.L),lowerDefault=attempt(loose,f.state,f.x),lowerSeed=attempt(loose,f.state,f.x,ref.root.L),
  normalPath=pathRoots(e,ref.state,f.state,f.x),loosePath=pathRoots(loose,ref.state,f.state,f.x);
 report.fixedFailurePoint={x:f.x,step:f.step,phase:f.phase,acceptedRoot:summary(ref.root),
  originalFloorAcceptedSeed:{ok:seeded.ok,...seeded.report},
  lowerFloorDefault:{ok:lowerDefault.ok,...lowerDefault.report},
  lowerFloorAcceptedSeed:{ok:lowerSeed.ok,...lowerSeed.report},
  originalFloorPath:normalPath.report,lowerFloorPath:loosePath.report};
 const sol=seeded.ok?{rt:seeded.rt,state:f.state}:lowerSeed.ok?{rt:lowerSeed.rt,state:f.state}:lowerDefault.ok?{rt:lowerDefault.rt,state:f.state}:loosePath.rt?loosePath:null;
 if(sol)report.physicalLeadingDifference={atFinalTrial:seeded.ok||lowerSeed.ok||lowerDefault.ok,...physicalDifference(ref,sol.rt,sol.state)};
}
report.sources={};for(const name of ['78718-tail-fourier-root-momentum.mjs','78718-tail-fourier-root-split-engine.mjs','78718-tail-fourier-product-flow.mjs','78718-tail-fourier-product-jacobian.mjs']){
 const b=fs.readFileSync(new URL(name,import.meta.url));report.sources[name]=crypto.createHash('sha256').update(b).digest('hex');
}
report.elapsedSeconds=(Date.now()-started)/1000;fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,acceptedLocal:report.acceptedLocal,trialLocal:report.trialLocal,
 fixedFailurePoint:report.fixedFailurePoint,physicalLeadingDifference:report.physicalLeadingDifference?{deltaA:report.physicalLeadingDifference.deltaA,deltaK:report.physicalLeadingDifference.deltaK,E_delta_Pt:report.physicalLeadingDifference.E_delta_Pt,resolvedM15Contribution:report.physicalLeadingDifference.resolvedM15Contribution,newW22Contribution:report.physicalLeadingDifference.newW22Contribution,atFinalTrial:report.physicalLeadingDifference.atFinalTrial}:null,
 elapsedSeconds:report.elapsedSeconds}));

