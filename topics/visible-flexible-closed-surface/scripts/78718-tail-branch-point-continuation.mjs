// Local branch diagnosis only; no shooting/BVP and no live source/config edits.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
const src=name=>pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',name));
const {createFastSplitFluxMomentumTailEngine}=await import(src('f6tail_fast_split_flux_engine.mjs'));
const {integrationGrid}=await import(src('f6tail_cusp_grid.mjs'));
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.packet||!opt.snapshot||!opt.trials||!opt.out||fs.existsSync(opt.out))throw Error('inputs and fresh out required');
const inputRecords=[];
function read(name){const bytes=fs.readFileSync(name);inputRecords.push({path:path.resolve(name),bytes:bytes.length,sha256:crypto.createHash('sha256').update(bytes).digest('hex')});return JSON.parse(name.endsWith('.gz')?zlib.gunzipSync(bytes):bytes);}
const started=Date.now(),packet=read(opt.packet),snap=read(opt.snapshot),trialRecords=opt.trials.split(',').map(read),
 oldCP=packet.response.checkpoint,current=snap.checkpoint,cfg=packet.config,
 M=cfg.modes,N=cfg.quadrature,K=2*M,floor=cfg.projectionFloor??.05,looseFloor=1e-10,
 physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),
 cache=new Map();
if(current.parameters.modes!==M||current.parameters.quadrature!==N||current.states.length!==oldCP.states.length)throw Error('comparison dimensions differ');
function engine(cell,modes=M,projectionFloor=floor){const key=cell.mu+':'+modes+':'+projectionFloor;
 if(!cache.has(key))cache.set(key,createFastSplitFluxMomentumTailEngine({modes,quadrature:N,spacing:cfg.spacing,mu:cell.mu,orientation:cfg.orientation,projectionFloor}));
 return cache.get(key);
}

const acceptedCache=new Map();
function referenceAt(stage,index){
 if(!acceptedCache.has(stage)){
  const fields=[];
  const run=walk(stage,current.states[stage+1],v=>fields[v.fieldNo]={state:Float64Array.from(v.state),rootL:Float64Array.from(v.root.L),x:v.x});
  if(!run.ok)throw Error('Saved accepted stage unexpectedly failed: '+run.summary.error);
  acceptedCache.set(stage,fields);
 }
 const v=acceptedCache.get(stage)[index];if(!v)throw Error('Missing accepted comparison field');return v;
}
function continuation(e,from,to,p,x,steps=32){
 let start=attempt(e,from,p,x);if(!start.ok)return {ok:false,stepsCompleted:0,error:start.summary.error};
 let last=start.rt,lastAlpha=0;
 for(let k=1;k<=steps;k++){
  const alpha=k/steps,y=Float64Array.from(from,(v,j)=>v+alpha*(to[j]-v)),next=attempt(e,y,p,x,last.L);
  if(!next.ok)return {ok:false,steps,stepsCompleted:k-1,lastAlpha,lastRoot:scalarRoot(last),failureAlpha:alpha,error:next.summary.error};
  last=next.rt;lastAlpha=alpha;
 }
 return {ok:true,steps,stepsCompleted:steps,lastAlpha,root:scalarRoot(last)};
}
const trials=[];
for(const record of trialRecords){
 const stage=record.stage,c=stages.cells[stage],p=c.profiles[0],e=engine(c),run=walk(stage,record.inputState),
  row={trial:record.trial,stage,originalLocalReplay:run.summary};
 if(!run.ok&&run.failure){
  const f=run.failure,ref=referenceAt(stage,f.fieldNo),loose=engine(c,M,looseFloor);
  if(ref.x!==f.x)throw Error('Radial field mismatch');
  const normalSeed=attempt(e,f.state,p,f.x,ref.rootL),looseSeed=attempt(loose,f.state,p,f.x,ref.rootL);
  row.actualAcceptedStateSeed={x:f.x,r:e.geometry(p,f.x).r,
   originalFloor:{ok:normalSeed.ok,...normalSeed.summary},
   looseFloor:{floor:looseFloor,ok:looseSeed.ok,...looseSeed.summary},
   normalContinuation:continuation(e,ref.state,f.state,p,f.x),
   looseContinuation:continuation(loose,ref.state,f.state,p,f.x)};
 }
 trials.push(row);
}
const report={scope:'Three fixed failure points: seed from actual accepted iterate and 32 local state homotopy roots, without DN/BVP. The 1e-10 floor is diagnostic only.',
 inputs:inputRecords,modes:M,quadrature:N,originalFloor:floor,looseFloor,iteration:snap.iteration,trials,
 scriptSHA256:crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex'),
 elapsedSeconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,
 originalFloorSeedRecoveries:trials.filter(t=>t.actualAcceptedStateSeed?.originalFloor.ok).length,
 looseFloorSeedRecoveries:trials.filter(t=>t.actualAcceptedStateSeed?.looseFloor.ok).length,
 normalPathCompletions:trials.filter(t=>t.actualAcceptedStateSeed?.normalContinuation.ok).length,
 loosePathCompletions:trials.filter(t=>t.actualAcceptedStateSeed?.looseContinuation.ok).length,
 elapsedSeconds:report.elapsedSeconds}));

function scalarRoot(rt){
 const rows=rt.e.rows;let at=0;for(let n=1;n<rows.length;n++)if(rows[n].A<rows[at].A)at=n;
 const v=rows[at];
 return {iterations:rt.iterations,relativeResidual:rt.err/rt.scale,minA:rt.e.minA,minD:rt.e.minD,minS:rt.e.minS,
  theta:2*Math.PI*at/N,r:rt.g.r,w:rt.g.w,atMinimumA:{onePlusL:1+v.L,WPt:rt.g.w2*v.Pt,P:v.P,Pt:v.Pt,K:v.K,D:v.D,S:v.S}};
}
function attempt(e,y,p,x,guess){try{const rt=e.root(y,p,x,guess);return {ok:true,rt,summary:scalarRoot(rt)};}catch(error){return {ok:false,summary:{error:String(error)}};}}
function geometricProbe(oldEngine,rt,y,cell,p,x,projectionFloor){
 const newM=22,newEngine=engine(cell,newM,projectionFloor),oldRaw=oldEngine.toRaw(y,p,x,rt).raw,raw=new Float64Array(2*newM);
 for(let j=0;j<M;j++){raw[j]=oldRaw[j];raw[newM+j]=oldRaw[M+j];}
 try{
  const init=newEngine.initializeFromRaw(raw,p,x),defaultAttempt=attempt(newEngine,init.state,p,x),
   seededAttempt=attempt(newEngine,init.state,p,x,init.L),chosen=defaultAttempt.ok?defaultAttempt:seededAttempt;
  let slopeCoefficientL1Gap=null,AAtCommonAnglesGap=null,extraPiRatio=null;
  if(chosen.ok){
   const other=chosen.rt,g=rt.g;
   slopeCoefficientL1Gap=Math.abs(g.w*(rt.L[0]-other.L[0]));
   for(let j=0;j<newM;j++){const f=cfg.spacing*(j+1),a=j<M?Math.sqrt(2)*g.w*rt.L[j+1]+f*f*g.r**3*y[j]:0,
    b=Math.sqrt(2)*g.w*other.L[j+1]+f*f*g.r**3*init.state[j];slopeCoefficientL1Gap+=Math.abs(a-b);}
   AAtCommonAnglesGap=Math.max(...rt.e.rows.map((v,n)=>Math.abs(v.A-other.e.rows[n].A)));
   extraPiRatio=Math.max(...Array.from(init.state.slice(newM+M,2*newM),Math.abs))/Math.max(1e-300,...Array.from(init.state.slice(newM,newM+M),Math.abs));
  }
  return {ok:true,modes:newM,floor:projectionFloor,defaultRoot:{ok:defaultAttempt.ok,...defaultAttempt.summary},
   geometricSeedRoot:{ok:seededAttempt.ok,...seededAttempt.summary},slopeCoefficientL1Gap,AAtCommonAnglesGap,extraPiRatio};
 }catch(error){return {ok:false,modes:newM,floor:projectionFloor,error:String(error)};}
}
function walk(stage,initial,onField=null){
 const cell=stages.cells[stage],e=engine(cell),p=cell.profiles[0],grid=integrationGrid(cfg.steps,p.integrationBreakpoints??[]),
  y=new Float64Array(K+2);y.set(initial);let state=y,lastRoot=null,fieldNo=0,currentFailure=null,minA=Infinity,minD=Infinity;
 function field(s,x,step,phase){
  let rt;
  try{rt=e.root(s,p,x);}catch(error){currentFailure={stage,x,step,phase,fieldNo,error:String(error),state:Float64Array.from(s),previousRoot:lastRoot};throw error;}
  minA=Math.min(minA,rt.e.minA);minD=Math.min(minD,rt.e.minD);
  onField?.({stage,x,step,phase,fieldNo,state:s,root:rt,engine:e,profile:p,cell});fieldNo++;lastRoot=rt;
  return e.rhs(s,p,x,false,rt);
 }
 try{
  for(let n=0;n<grid.length-1;n++){
   const x=grid[n],h=grid[n+1]-x,a=field(state,x,n,'a'),tmp=new Float64Array(K+2);
   for(let j=0;j<K+2;j++)tmp[j]=state[j]+h*a[j]/2;
   const b=field(tmp,x+h/2,n,'b');for(let j=0;j<K+2;j++)tmp[j]=state[j]+h*b[j]/2;
   const c=field(tmp,x+h/2,n,'c');for(let j=0;j<K+2;j++)tmp[j]=state[j]+h*c[j];
   const d=field(tmp,x+h,n,'d');
   state=Float64Array.from(state,(v,j)=>v+h*(a[j]+2*b[j]+2*c[j]+d[j])/6);
  }
  return {ok:true,summary:{stage,minA,minD,fields:fieldNo}};
 }catch(error){
  return {ok:false,summary:{stage,minA,minD,fields:fieldNo,error:String(error),failure:currentFailure?{x:currentFailure.x,step:currentFailure.step,phase:currentFailure.phase}:null},failure:currentFailure};
 }
}
