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
let worst=null;const localStages=[];
for(let stage=32;stage<=40;stage++){
 const oldFields=[];
 const before=walk(stage,oldCP.states[stage+1],v=>oldFields[v.fieldNo]={state:Float64Array.from(v.state),x:v.x});
 const after=walk(stage,current.states[stage+1],v=>{
  if(worst&&v.root.e.minA>=worst.current.minA)return;
  const oldField=oldFields[v.fieldNo];if(!oldField)return;
  const oldRoot=v.engine.root(oldField.state,v.profile,oldField.x),newRows=v.root.e.rows;
  let n=0;for(let j=1;j<N;j++)if(newRows[j].A<newRows[n].A)n=j;
  const oldRow=oldRoot.e.rows[n],newRow=newRows[n],g=v.root.g;
  worst={stage,x:v.x,phase:v.phase,fieldNo:v.fieldNo,current:scalarRoot(v.root),
   previousAtSameX:scalarRoot(oldRoot),sameTheta:{theta:2*Math.PI*n/N,previousA:oldRow.A,currentA:newRow.A,
    deltaL:newRow.L-oldRow.L,deltaWPt:g.w2*(newRow.Pt-oldRow.Pt),deltaA:newRow.A-oldRow.A},
   geometricM22:geometricProbe(v.engine,v.root,v.state,v.cell,v.profile,v.x,floor)};
 });
 localStages.push({stage,previous:before.summary,current:after.summary});
}
const nodalProbes=[];
for(const stage of [36,37]){
 const c=stages.cells[stage],p=c.profiles[0],e=engine(c),y=new Float64Array(K+2);y.set(current.states[stage+1]);
 const rt=e.root(y,p,0);nodalProbes.push({stage,root:scalarRoot(rt),geometricM22:geometricProbe(e,rt,y,c,p,0,floor)});
}
const trials=[];
for(const record of trialRecords){
 const stage=record.stage,c=stages.cells[stage],p=c.profiles[0],e=engine(c),run=walk(stage,record.inputState);
 const row={trial:record.trial,stage,originalLocalReplay:run.summary};
 if(!run.ok&&run.failure){
  const f=run.failure,loose=engine(c,M,looseFloor),guess=f.previousRoot?.L,
   seeded=guess?attempt(e,f.state,p,f.x,guess):{ok:false,summary:{error:'No previous local root'}},
   looseDefault=attempt(loose,f.state,p,f.x),looseSeeded=guess?attempt(loose,f.state,p,f.x,guess):{ok:false,summary:{error:'No previous local root'}};
  row.sameFailurePoint={x:f.x,r:e.geometry(p,f.x).r,originalFloor:floor,seededOriginalFloor:{ok:seeded.ok,...seeded.summary},
   looseFloor,looseDefault:{ok:looseDefault.ok,...looseDefault.summary},looseSeeded:{ok:looseSeeded.ok,...looseSeeded.summary}};
  const chosen=seeded.ok?{e,rt:seeded.rt,floor}:looseDefault.ok?{e:loose,rt:looseDefault.rt,floor:looseFloor}:looseSeeded.ok?{e:loose,rt:looseSeeded.rt,floor:looseFloor}:null;
  if(chosen)row.sameFailurePoint.geometricM22=geometricProbe(chosen.e,chosen.rt,f.state,c,p,f.x,chosen.floor);
 }
 trials.push(row);
}
const report={scope:'Local fixed-input branch/root diagnostics. Lower floor only in fixed-point diagnostic attempts, not a production acceptance or a new tail solution.',
 inputs:inputRecords,modes:M,quadrature:N,originalFloor:floor,iteration:snap.iteration,
 firstHeightFraction:current.cutHeight[0]/oldCP.cutHeight[0]-1,localStages,worst,nodalProbes,trials,elapsedSeconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,worst:{stage:worst.stage,x:worst.x,currentMinA:worst.current.minA,previousAAtSameTheta:worst.sameTheta.previousA,deltaL:worst.sameTheta.deltaL,deltaWPt:worst.sameTheta.deltaWPt,M22SamePointMinA:worst.geometricM22.defaultRoot?.minA},
 trialCount:trials.length,originalFailures:trials.filter(t=>!t.originalLocalReplay.ok).length,
 sameFloorSeedRecoveries:trials.filter(t=>t.sameFailurePoint?.seededOriginalFloor.ok).length,
 looseFloorRecoveries:trials.filter(t=>t.sameFailurePoint?.looseDefault.ok||t.sameFailurePoint?.looseSeeded.ok).length,
 elapsedSeconds:report.elapsedSeconds}));

