// Read-only numerical diagnostics of already closed trial-stage inputs.
// Original RK4, angular root, RHS arithmetic, floor and equations are retained.
// This file does not alter or call the active shooting worker.
import fs from 'node:fs';
import path from 'node:path';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';
import {fileURLToPath,pathToFileURL} from 'node:url';

const {values:v}=parseArgs({options:{
  'source-root':{type:'string'},config:{type:'string'},
  inputs:{type:'string',multiple:true},out:{type:'string'}
}});
for(const key of ['source-root','config','out'])
  if(!v[key])throw Error('Missing --'+key);
if(!v.inputs?.length)throw Error('At least one --inputs is required');
if(fs.existsSync(v.out))throw Error('Refusing to overwrite a diagnostic');
const here=path.dirname(fileURLToPath(import.meta.url));
const sourceRoot=path.resolve(v['source-root']);
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const sourcePath=name=>path.join(process.env.CLOSING_TAIL_CACHE,name);
const sourceURL=name=>pathToFileURL(sourcePath(name));
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const shaText=s=>createHash('sha256').update(s).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(sourceURL('f6tail_fast_split_flux_engine.mjs'));
const {withCuspAwareRK}=await import(sourceURL('f6tail_cusp_grid.mjs'));
const rootSource=fs.readFileSync(sourcePath('general_root_tail_momentum.mjs'),'utf8');
const splitSource=fs.readFileSync(sourcePath('f6tail_momentum_split_flux.mjs'),'utf8');
function extract(text,start,end){
  const first=text.indexOf(start),last=text.indexOf(end,first);
  if(first<0||last<=first||text.indexOf(start,first+1)>=0)throw Error('Source extraction marker is not unique');
  return text.slice(first,last);
}
const rootBody=extract(rootSource,' function solveSPD(',' function initializeFromRaw(');
const rkBody=extract(splitSource,'  function rk4(','  return {...base,rhs,rk4,statistics};');
const config=read(v.config),started=performance.now();
const physical=createRecalibrationFactory(config).assemble();
const cases=[];
const equalBytes=(a,b)=>Buffer.from(a.buffer,a.byteOffset,a.byteLength)
  .equals(Buffer.from(b.buffer,b.byteOffset,b.byteLength));

for(const input of v.inputs){
  const record=read(input),p=record.parameters,M=p.modes,N=p.quadrature,J=M+1,K=2*M;
  if(p.projectionFloor!==.05||p.rhsEvaluation!=='split-linear-flux-v1')
    throw Error('This replay requires the original .05 floor and split RHS');
  for(const key of ['modes','spacing','quadrature','steps','shootingParts'])
    if(config[key]!==p[key])throw Error('Config/record mismatch '+key);
  if(config.depth!==p.physicalDepth||record.inputState.length!==K)
    throw Error('Stage shape/depth mismatch');
  const staged=subdividePhysical(physical,p.physicalDepth,p.shootingParts);
  const cell=staged.cells[record.stage];
  if(cell.rawCell!==record.rawCell||cell.rawSegment!==record.rawSegment)
    throw Error('Raw stage identity mismatch');
  const base=createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,
    mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});
  const original=withCuspAwareRK(base);
  const sq2=Math.sqrt(2),sq12=Math.sqrt(12),floor=p.projectionFloor;
  const frequencies=Float64Array.from({length:M},(_,j)=>(j+1)*p.spacing);
  const cs=Array.from({length:N},(_,n)=>{
    const theta=2*Math.PI*n/N;
    return Float64Array.from({length:J},(_,j)=>j?sq2*Math.cos(frequencies[j-1]*theta):1);
  });
  const sn=Array.from({length:N},(_,n)=>{
    const theta=2*Math.PI*n/N;
    return Float64Array.from(frequencies,m=>sq2*Math.sin(m*theta));
  });
  function data(state,g){
    const Q=state.slice(0,M),pc=new Float64Array(M),pt=new Float64Array(J);
    for(let j=0;j<M;j++){pc[j]=-frequencies[j]*g.r**3*Q[j]/(sq2*g.w);pt[j+1]=frequencies[j]*pc[j];}
    const factor=p.orientation*sq12*cell.mu/(sq2*g.r**4*g.w2),target=new Float64Array(J);
    for(let j=0;j<M;j++)target[j+1]=factor*state[M+j];
    return {Q,pc,pt,target};
  }
  function margins(L,state,g){
    const d=data(state,g);
    let minA=Infinity,minD=Infinity,minS=Infinity,firstBad=null,atMinA=null;
    const points=[];
    for(let n=0;n<N;n++){
      let P=0,Pt=0,Lv=L[0];
      for(let j=0;j<M;j++){P+=d.pc[j]*sn[n][j];Pt+=d.pt[j+1]*cs[n][j+1];Lv+=L[j+1]*cs[n][j+1];}
      const k=Lv-Pt,T=2*k+k*k+g.E*P*P,D=1-g.w2*T,S=1-g.w2*P*P,A=1+Lv+g.w2*Pt;
      const row={node:n,theta:2*Math.PI*n/N,P,Pt,L:Lv,K:k,D,S,A};
      points.push(row);
      if(A<minA){minA=A;atMinA=row;}
      minD=Math.min(minD,D);minS=Math.min(minS,S);
      if(!firstBad&&!(D>floor&&S>floor&&A>floor))
        firstBad={...row,failed:['D','S','A'].filter(key=>!(row[key]>floor))};
    }
    return {minA,minD,minS,passesOriginalGuard:firstBad===null,firstBad,atMinA,points};
  }
  const shortMargin=m=>({minA:m.minA,minD:m.minD,minS:m.minS,passesOriginalGuard:m.passesOriginalGuard,
    firstBad:m.firstBad,atMinA:m.atMinA});
  function tracedRoot(state,profile,x,guess=null){
    const trace=[],g=base.geometry(profile,x),target=data(state,g).target;
    let iteration=-1,backtrack=0,lastL=null;
    const evaluator=(L,Q,geometry,needJac=true)=>{
      if(needJac){iteration++;backtrack=0;lastL=Float64Array.from(L);}
      const margin=margins(L,state,geometry);
      const row={iteration,kind:needJac?'accepted-iterate':'line-search-candidate',
        backtrack:needJac?null:backtrack,step:needJac?null:2**(-backtrack),...shortMargin(margin)};
      if(!needJac)backtrack++;
      if(needJac)row.coefficients=Array.from(L);
      try{
        const e=base.evaluateL(L,Q,geometry,needJac);
        if(e.minA!==margin.minA||e.minD!==margin.minD||e.minS!==margin.minS)
          throw Error('Independent margin arithmetic differs from frozen engine');
        row.residual=Math.max(...Array.from(e.moments,(z,j)=>Math.abs(z-target[j])));
        row.scale=Math.max(1e-300,e.maxQuad,...Array.from(target,Math.abs));
        trace.push(row);return e;
      }catch(error){row.error=String(error);trace.push(row);throw error;}
    };
    const root=new Function('M','J','sq2','sq12','mu','orientation','geometry','evaluateL',
      rootBody+'\nreturn root;')(M,J,sq2,sq12,cell.mu,p.orientation,base.geometry,evaluator);
    try{
      const result=root(state,profile,x,guess);
      return {success:true,trace,lastL:Array.from(result.L),root:{
        iterations:result.iterations,residual:result.err,scale:result.scale,
        relativeResidual:result.err/result.scale,roundoffFallback:result.roundoffFallback??false,
        minA:result.e.minA,minD:result.e.minD,minS:result.e.minS},result};
    }catch(error){
      return {success:false,error:String(error),trace,lastL:lastL?Array.from(lastL):null};
    }
  }
  let lastRoot=null,location=null,firstFailure=null,rhsCalls=0,successfulSteps=0,
    successfulStepByteChecks=0,rootTraceEqualityChecked=false;
  const rhsHistory=[];
  const observedRhs=(state,profile,x)=>{
    rhsCalls++;
    const where={...location,rhsCall:rhsCalls,substage:(location.localRhs++%4),
      sourceX:x,rawSourceX:cell.rawLeft+(cell.rawRight-cell.rawLeft)*x};
    try{
      const root=base.root(state,profile,x);
      if(!rootTraceEqualityChecked){
        const traced=tracedRoot(state,profile,x);
        if(!traced.success||!equalBytes(traced.result.L,root.L)||traced.root.residual!==root.err||
          traced.root.scale!==root.scale||traced.root.iterations!==root.iterations)
          throw Error('Extracted diagnostic root is not identical at the first successful point');
        rootTraceEqualityChecked=true;
      }
      rhsHistory.push({...where,success:true,radius:root.g.r,minA:root.e.minA,minD:root.e.minD,
        minS:root.e.minS,rootIterations:root.iterations,rootRelativeResidual:root.err/root.scale});
      lastRoot=root;
      return base.rhs(state,profile,x,false,root);
    }catch(error){
      if(firstFailure)throw error;
      const g=base.geometry(profile,x),d=data(state,g),diagnostic=tracedRoot(state,profile,x);
      if(diagnostic.success||diagnostic.error!==String(error))
        throw Error('Extracted root did not reproduce the frozen root failure');
      delete diagnostic.result;
      const initial=margins(d.target,state,g);
      const seeds=[];
      const unitA=new Float64Array(J);
      for(let j=0;j<M;j++)unitA[j+1]=-g.w2*d.pt[j+1];
      seeds.push({name:'unit-A-seed-c0',guess:unitA});
      if(lastRoot)seeds.push({name:'last-successful-RK-root',guess:Float64Array.from(lastRoot.L)});
      let lo=-Infinity,hi=Infinity;
      for(const point of initial.points){
        if(!(point.S>floor&&g.E*point.S>floor)){lo=Infinity;hi=-Infinity;break;}
        const radius=Math.sqrt(g.E*point.S-floor)/g.w;
        lo=Math.max(lo,point.Pt-1-radius-point.L,floor-1-g.w2*point.Pt-point.L);
        hi=Math.min(hi,point.Pt-1+radius-point.L);
      }
      if(lo<hi){
        const margin=Math.min((hi-lo)/4,.01),guess=Float64Array.from(d.target);
        guess[0]=Math.min(Math.max(0,lo+margin),hi-margin);
        seeds.push({name:'mean-only-feasible-target-seed',guess,meanIntervalApprox:[lo,hi]});
      }
      const alternatives=[];
      for(const candidate of seeds){
        const before=margins(candidate.guess,state,g),row={name:candidate.name,
          initialCoefficients:Array.from(candidate.guess),initial:shortMargin(before)};
        if(candidate.meanIntervalApprox)row.meanIntervalApprox=candidate.meanIntervalApprox;
        if(before.passesOriginalGuard){
          const tested=tracedRoot(state,profile,x,candidate.guess);
          delete tested.result;row.originalRootWithSeed=tested;
        }else row.originalRootWithSeed={success:false,notCalledBecauseInitialGuardFailed:true};
        alternatives.push(row);
      }
      firstFailure={...where,error:String(error),state:Array.from(state),geometry:{
        r:g.r,logw:g.logw,w:g.w,w2:g.w2,E:g.E,drdx:g.drdx,dlogwdx:g.dlogwdx},
        target:Array.from(d.target),defaultInitial:shortMargin(initial),rootTrace:diagnostic,
        alternatives,meanOnlyTargetSliceNonempty:lo<hi,meanOnlyTargetIntervalApprox:[lo,hi]};
      rhsHistory.push({...where,success:false,error:String(error),radius:g.r});
      throw error;
    }
  };
  const plainObservedRK=new Function('rhs','size',rkBody+'\nreturn rk4;')(observedRhs,base.size);
  const observed=withCuspAwareRK({...base,rk4:plainObservedRK});
  let state=new Float64Array(K+2);state.set(record.inputState);
  outer:for(let profileIndex=0;profileIndex<cell.profiles.length;profileIndex++){
    const profile=cell.profiles[profileIndex];
    for(let k=0;k<p.steps;k++){
      location={profileIndex,ordinaryStep:k,ordinaryStart:k/p.steps,ordinaryH:1/p.steps,localRhs:0};
      const incoming=state;
      let actualError=null,expectedError=null,candidate=null,reference=null;
      try{candidate=observed.rk4(incoming,profile,k/p.steps,1/p.steps);}catch(error){actualError=String(error);}
      try{reference=original.rk4(incoming,profile,k/p.steps,1/p.steps);}catch(error){expectedError=String(error);}
      if(actualError!==expectedError)throw Error('Diagnostic RK failure differs from original: '+actualError+' versus '+expectedError);
      if(actualError){
        if(!firstFailure||actualError!==record.trial.error)throw Error('Saved stage failure was not reproduced');
        firstFailure.originalUninstrumentedRKError=expectedError;
        break outer;
      }
      if(!equalBytes(candidate,reference))throw Error('Diagnostic RK state differs from frozen original');
      successfulStepByteChecks++;successfulSteps++;state=candidate;
    }
  }
  if(!firstFailure)throw Error('The saved stage unexpectedly succeeded');
  cases.push({input:path.resolve(input),inputSHA256:sha(input),inputScope:record.scope,
    trial:record.trial,stage:record.stage,rawCell:record.rawCell,rawSegment:record.rawSegment,
    rawLeft:cell.rawLeft,rawRight:cell.rawRight,steps:p.steps,modes:M,quadrature:N,floor,
    profileBreakpoints:cell.profiles.map(profile=>profile.integrationBreakpoints??[]),
    successfulSteps,successfulStepByteChecks,rootTraceEqualityChecked,rhsCalls,rhsHistory,firstFailure});
}
const sources=[
  'general_root_tail_momentum.mjs','f6tail_momentum_split_flux.mjs','f6tail_fast_split_flux_engine.mjs',
  'f6tail_fast_momentum.mjs','f6tail_cusp_grid.mjs'
].map(sourcePath).concat(['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs',
  '950f-tail-subdivision.mjs','db6f-prefix-tail-trial-core.mjs','db6f-prefix-tail-trial-split.mjs'].map(n=>path.join(here,n)));
const report={status:'closed-stage-first-RK-failure-diagnostic-not-a-solved-tail-or-proof',
  scope:'Read-only replay of the saved failed stage only. Original .05 guard, target, root/RK arithmetic and split RHS are unchanged. Every successful whole RK step is byte-compared to the original. Alternate seeds are evaluated only at the failed point, never fed into a shooting solve. Sampled margins and residuals are not rigorous enclosures or a nonexistence theorem.',
  scriptSHA256:sha(fileURLToPath(import.meta.url)),config:{file:path.resolve(v.config),sha256:sha(v.config)},
  sourceSHA256:Object.fromEntries(sources.map(s=>[s,sha(s)])),
  extractedRootSHA256:shaText(rootBody),extractedRK4SHA256:shaText(rkBody),
  cases,seconds:(performance.now()-started)/1000};
fs.writeFileSync(v.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({finished:true,seconds:report.seconds,cases:cases.map(c=>({
  trial:c.trial.trial,step:c.trial.step,stage:c.stage,rk:c.firstFailure.ordinaryStep,
  substage:c.firstFailure.substage,x:c.firstFailure.sourceX,defaultA:c.firstFailure.defaultInitial.minA,
  defaultD:c.firstFailure.defaultInitial.minD,defaultS:c.firstFailure.defaultInitial.minS,
  error:c.firstFailure.error,rootIterations:c.firstFailure.rootTrace.trace.filter(t=>t.kind==='accepted-iterate').length,
  alternateSuccesses:c.firstFailure.alternatives.filter(a=>a.originalRootWithSeed.success).map(a=>a.name)
}))}));
