// Explicitly authorized read-only probes of one closed failed entry state.
// The moment equation, metric, state and target are unchanged. Only the
// positive numerical guard is varied in these isolated diagnostic calls.
import fs from 'node:fs';
import path from 'node:path';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';
import {pathToFileURL,fileURLToPath} from 'node:url';

const {values:v}=parseArgs({options:Object.fromEntries(
  ['source-root','config','stage-input','control-checkpoint','out'].map(k=>[k,{type:'string'}]))});
for(const key of ['source-root','config','stage-input','control-checkpoint','out'])
  if(!v[key])throw Error('Missing --'+key);
if(fs.existsSync(v.out))throw Error('Refusing to overwrite an output');
const here=path.dirname(fileURLToPath(import.meta.url)),sourceRoot=path.resolve(v['source-root']);
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const source=name=>path.join(process.env.CLOSING_TAIL_CACHE,name);
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const {createMomentumTailEngine}=await import(pathToFileURL(source('general_root_tail_momentum.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(source('f6tail_fast_split_flux_engine.mjs')));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const config=read(v.config),input=read(v['stage-input']),p=input.parameters,M=p.modes,K=2*M,J=M+1,
  sq2=Math.sqrt(2),sq12=Math.sqrt(12),start=performance.now();
if(input.stage!==35||input.rawCell!==0||input.rawSegment!==4||input.trial.step!==.0625||
  p.projectionFloor!==.05||p.modes!==15||p.quadrature!==256)
  throw Error('This probe is restricted to the saved lambda=1/16 M15 entry');
const physical=createRecalibrationFactory(config).assemble(),
  staged=subdividePhysical(physical,p.physicalDepth,p.shootingParts),cell=staged.cells[input.stage],
  profile=cell.profiles[0],x=0,state=new Float64Array(K+2),freq=Float64Array.from({length:M},(_,j)=>(j+1)*p.spacing);
state.set(input.inputState);
const engine=(N,floor)=>createMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,
  mu:cell.mu,orientation:p.orientation,projectionFloor:floor});
const base=engine(256,.05),g=base.geometry(profile,x),target=new Float64Array(J),unitA=new Float64Array(J);
const factor=p.orientation*sq12*cell.mu/(sq2*g.r**4*g.w2);
for(let j=0;j<M;j++){
  target[j+1]=factor*state[M+j];
  const pc=-freq[j]*g.r**3*state[j]/(sq2*g.w);
  unitA[j+1]=-g.w2*freq[j]*pc;
}
const rootSource=fs.readFileSync(source('general_root_tail_momentum.mjs'),'utf8'),
  begin=rootSource.indexOf(' function solveSPD('),end=rootSource.indexOf(' function initializeFromRaw(',begin);
if(begin<0||end<=begin)throw Error('Root extraction failed');
const body=rootSource.slice(begin,end),equal=(a,b)=>Buffer.from(a.buffer,a.byteOffset,a.byteLength)
  .equals(Buffer.from(b.buffer,b.byteOffset,b.byteLength));
const records=[];
function solve(N,floor,seed,name){
  const e=engine(N,floor),accepted=[],summary={N,floor,seed:name},knownTarget=target;
  let rejected=0;
  const evaluate=(L,Q,geometry,needJac=true)=>{
    try{
      const r=e.evaluateL(L,Q,geometry,needJac);
      if(needJac)accepted.push({iteration:accepted.length,minA:r.minA,minD:r.minD,minS:r.minS,
        residual:Math.max(...Array.from(r.moments,(a,j)=>Math.abs(a-knownTarget[j]))),
        scale:Math.max(1e-300,r.maxQuad,...Array.from(knownTarget,Math.abs))});
      return r;
    }catch(error){if(!needJac)rejected++;throw error;}
  };
  const traced=new Function('M','J','sq2','sq12','mu','orientation','geometry','evaluateL',
    body+'\nreturn root;')(M,J,sq2,sq12,cell.mu,p.orientation,e.geometry,evaluate);
  let one=null,two=null,errorOne=null,errorTwo=null;
  try{one=traced(state,profile,x,seed);}catch(error){errorOne=String(error);}
  try{two=e.root(state,profile,x,seed);}catch(error){errorTwo=String(error);}
  if(errorOne!==errorTwo||Boolean(one)!==Boolean(two)||
    (one&&(!equal(one.L,two.L)||one.err!==two.err||one.scale!==two.scale)))
    throw Error('Recorded root differs from uninstrumented original');
  Object.assign(summary,{success:!!one,originalFunctionExactlyReproduced:true,
    error:errorOne,accepted,rejectedLineSearchEvaluations:rejected});
  if(one)Object.assign(summary,{L:Array.from(one.L),iterations:one.iterations,residual:one.err,
    scale:one.scale,relativeResidual:one.err/one.scale,minA:one.e.minA,minD:one.e.minD,minS:one.e.minS});
  records.push(summary);
  return one;
}
// A successful base-state control from the separately closed iteration file.
const control=read(v['control-checkpoint']),cp=control.checkpoint??control.response?.checkpoint??control,
  controlState=new Float64Array(K+2);
if(cp.parameters.modes!==M||cp.parameters.quadrature!==256||
  cp.states[input.stage+1].length!==K)throw Error('Wrong control checkpoint');
controlState.set(cp.states[input.stage+1]);
const controlRoot=base.root(controlState,profile,0);
const controlExtracted=new Function('M','J','sq2','sq12','mu','orientation','geometry','evaluateL',
  body+'\nreturn root;')(M,J,sq2,sq12,cell.mu,p.orientation,base.geometry,base.evaluateL)(controlState,profile,0);
if(!equal(controlRoot.L,controlExtracted.L)||controlRoot.err!==controlExtracted.err)
  throw Error('Successful base root extraction control failed');
const split=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:256,
  mu:cell.mu,orientation:p.orientation,projectionFloor:.05});
const splitText=fs.readFileSync(source('f6tail_momentum_split_flux.mjs'),'utf8'),
  rkStart=splitText.indexOf('  function rk4('),rkEnd=splitText.indexOf('  return {...base,rhs,rk4,statistics};',rkStart),
  rkBody=splitText.slice(rkStart,rkEnd);
const withKnown=(s,pr,xx)=>split.rhs(s,pr,xx,false,split.root(s,pr,xx));
const extractedRK=new Function('rhs','size',rkBody+'\nreturn rk4;')(withKnown,split.size);
const a=extractedRK(controlState,profile,0,1/p.steps),b=split.rk4(controlState,profile,0,1/p.steps);
if(!equal(a,b))throw Error('Successful control RK byte comparison failed');
const controlResult={input:path.resolve(v['control-checkpoint']),sha256:sha(v['control-checkpoint']),
  iteration:control.iteration,stage:input.stage,rootCoefficientsByteIdentical:true,
  firstRKStepByteIdentical:true,root:{minA:controlRoot.e.minA,minD:controlRoot.e.minD,
    minS:controlRoot.e.minS,residual:controlRoot.err,scale:controlRoot.scale}};

const successful=[];
for(const floor of [.05,.025,.01,.001]){
  for(const [name,seed]of [['default-target',null],['unit-A-c0',unitA]]){
    const r=solve(256,floor,seed,name);
    if(r)successful.push({floor,seed:name,root:r});
  }
}
const refinements=[];
for(const entry of successful){
  const row={floor:entry.floor,seed:entry.seed,levels:[]};
  let previous=entry.root;
  for(const N of [512,1024]){
    const next=solve(N,entry.floor,previous.L,'continuation-from-lower-angular-count');
    row.levels.push({N,success:!!next,
      rootCoefficientDifference:next?Math.max(...Array.from(next.L,(a,j)=>Math.abs(a-previous.L[j]))):null});
    if(!next){previous=null;break;}previous=next;
  }
  if(previous){
    try{
      const dense=engine(8192,entry.floor).evaluateL(previous.L,state.slice(0,M),g,true);
      row.denseOriginalEquation={N:8192,passesOriginalPositiveFloor:true,minA:dense.minA,minD:dense.minD,
        minS:dense.minS,residual:Math.max(...Array.from(dense.moments,(a,j)=>Math.abs(a-target[j])))};
    }catch(error){row.denseOriginalEquation={N:8192,passesOriginalPositiveFloor:false,error:String(error)};}
  }
  refinements.push(row);
}
const sourcePaths=['general_root_tail_momentum.mjs','f6tail_momentum_split_flux.mjs',
  'f6tail_fast_split_flux_engine.mjs','f6tail_fast_momentum.mjs'].map(source).concat(
  ['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs','950f-tail-subdivision.mjs'].map(s=>path.join(here,s)));
const report={status:'isolated-positive-floor-probe-not-a-stage-or-coupled-solution',
  authorizationScope:'Root explicitly authorized .025/.01/.001 numerical positive-floor probes at the saved lambda=1/16 entry. No active worker, old checkpoint, metric or equation is changed.',
  mathematicalScope:'All roots here concern one fixed finite moment target. Positive angular sampling is not a rigorous all-angle bound. Failure is not nonexistence. Successful local roots would still not solve any complete stage or prefix-tail joint system.',
  scriptSHA256:sha(fileURLToPath(import.meta.url)),inputs:Object.fromEntries(
    ['config','stage-input','control-checkpoint'].map(k=>[k,{file:path.resolve(v[k]),sha256:sha(v[k])}])),
  sourceSHA256:Object.fromEntries(sourcePaths.map(s=>[s,sha(s)])),stage:input.stage,
  rawCell:cell.rawCell,rawSegment:cell.rawSegment,rawX:cell.rawLeft,x,
  originalFloor:.05,geometry:{r:g.r,w:g.w,w2:g.w2,E:g.E,drdx:g.drdx},
  controlResult,records,refinements,seconds:(performance.now()-start)/1000};
const encoded=JSON.stringify(report,null,2)+'\n';
if(Buffer.byteLength(encoded)>1_000_000)throw Error('Diagnostic unexpectedly requires gzip');
fs.writeFileSync(v.out,encoded);
console.log(JSON.stringify({finished:true,seconds:report.seconds,
  controlRootAndRKByteIdentical:true,records:records.map(r=>({N:r.N,floor:r.floor,seed:r.seed,
    success:r.success,minA:r.minA,residual:r.residual,error:r.error,
    last:r.accepted.at(-1)})),refinements}));
