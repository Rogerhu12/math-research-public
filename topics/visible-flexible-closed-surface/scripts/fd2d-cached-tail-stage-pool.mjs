// Optional parallel evaluation of independent shooting maps. No shooting solve
// or stable graph is constructed here. All residual reductions remain serial.
import {Worker, MessageChannel, receiveMessageOnPort, isMainThread, workerData} from 'node:worker_threads';
import {performance} from 'node:perf_hooks';
import v8 from 'node:v8';
import {createStageMapCache} from './fd2d-stage-map-cache.mjs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createFourierRootSplitFluxEngine} from './78718-tail-fourier-root-split-engine.mjs';

const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const {splitIntegrationInterval,integrationGrid}=await import(pathToFileURL(path.join(
 sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));
const KIND='visible-flex-independent-stage-pool-v4-resumable';
const C={generation:0,next:1,done:2,firstFailure:3,lock:4,stop:5,withJac:6,ready:7,fatal:8,progress:9};

function infrastructure(message){const e=new Error(message);e.code='TAIL_STAGE_POOL_INFRASTRUCTURE';return e;}
function lock(a){while(Atomics.compareExchange(a,C.lock,0,1)!==0)Atomics.wait(a,C.lock,1,1000);}
function unlock(a){Atomics.store(a,C.lock,0);Atomics.notify(a,C.lock);}

// While Atomics.wait blocks the main event loop, Worker error/exit callbacks
// cannot run. A shared progress counter therefore bounds an unreported native
// worker death as well as an actual hang. This is an infrastructure timeout,
// never a relaxation of a numerical residual or a mathematical rejection.
export function waitForSharedCompletion({control,doneIndex,doneCount,progressIndex,
 noProgressMilliseconds,checkFatal=()=>{},observeProgress=()=>{}}){
 let progress=Atomics.load(control,progressIndex),lastProgress=performance.now();
 while(Atomics.load(control,doneIndex)!==doneCount){
  checkFatal();observeProgress();
  const now=performance.now(),current=Atomics.load(control,progressIndex);
  if(current!==progress){progress=current;lastProgress=now;}
  const remaining=noProgressMilliseconds-(now-lastProgress);
  if(remaining<=0)throw infrastructure('Stage worker made no shared progress for '+noProgressMilliseconds+' ms');
  const done=Atomics.load(control,doneIndex);
  if(done!==doneCount)Atomics.wait(control,doneIndex,done,Math.min(1000,remaining));
 }
 checkFatal();observeProgress();
}

async function resolvesWithin(promise,milliseconds){
 let timer;
 const answer=await Promise.race([promise.then(()=>true),
  new Promise(resolve=>{timer=setTimeout(()=>resolve(false),milliseconds);})]);
 clearTimeout(timer);return answer;
}

// The caller first publishes its normal stop flag. If a worker cannot reach
// that flag, terminate it rather than waiting indefinitely for a JS finally.
export async function closeStageWorkers(threads,exitPromises,{closeGraceMilliseconds=2000,
 terminateGraceMilliseconds=5000}={}){
 const all=Promise.all(exitPromises);
 if(await resolvesWithin(all,closeGraceMilliseconds))return {forcedTermination:false,allExited:true};
 for(const worker of threads)worker.terminate().catch(()=>{});
 if(await resolvesWithin(all,terminateGraceMilliseconds))return {forcedTermination:true,allExited:true};
 for(const worker of threads)worker.unref();
 throw infrastructure('Stage worker termination did not finish within '+terminateGraceMilliseconds+' ms');
}

// This is the original cellFlow arithmetic, including the original independent
// zero mean-height variables and the row-only port momentum normalization.
export function serialStageFlow(cell,input,{withJac,stepsPerSegment}){
 const M=cell.engine.M,K=2*M,s=new Float64Array(K+2);s.set(input);
 let f;
 if(withJac)f=cell.engine.flowStateWithJacobian(s,cell.profiles,{stepsPerSegment});
 else{
  let state=s;
  for(const profile of cell.profiles)for(let k=0;k<stepsPerSegment;k++)
   state=cell.engine.rk4(state,profile,k/stepsPerSegment,1/stepsPerSegment);
  f={state};
 }
 const out=Float64Array.from(f.state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio);
 let J=null;
 if(withJac){J=new Float64Array(K*K);for(let i=0;i<K;i++)for(let j=0;j<K;j++)
  J[i*K+j]=f.tangent[i*K+j]/(i<M?1:cell.portRatio);}
 return {out,J,meanHeight:f.state[K]+f.state[K+1],minA:f.minA,minD:f.minD};
}

// Transfer exact evaluations of each ORIGINAL profile at the finite collection
// of floating-point arguments used by BOTH original RK loops. This is neither
// interpolation nor a change of the analytic physical profile. Lookup misses
// are infrastructure errors; they never fall back to approximate values.
function tabulateProfile(profile,steps,cuspAwareFlow){
 const points=new Set(),cuts=Array.from(profile.integrationBreakpoints??[]);
 const addRK=(x,h)=>{points.add(x);points.add(x+h/2);points.add(x+h);};
 for(let k=0;k<steps;k++){
  const x=k/steps,h=1/steps;
  const grid=cuspAwareFlow?splitIntegrationInterval(x,x+h,cuts):[x,x+h];
  if(grid.length===2)addRK(x,h);
  else for(let j=0;j<grid.length-1;j++)addRK(grid[j],grid[j+1]-grid[j]);
 }
 const grid=cuts.length?integrationGrid(steps,cuts):null,ordinaryH=1/steps;
 for(let k=0;k<(grid?grid.length-1:steps);k++)
  addRK(grid?grid[k]:k*ordinaryH,grid?grid[k+1]-grid[k]:ordinaryH);
 const xs=Float64Array.from(points),first=profile(xs[0]),keys=Object.keys(first);
 const values=new Float64Array(xs.length*keys.length);
 for(let i=0;i<xs.length;i++){
  const g=i===0?first:profile(xs[i]);
  if(JSON.stringify(Object.keys(g))!==JSON.stringify(keys))
   throw infrastructure('Original profile field layout changes on its RK nodes');
  for(let j=0;j<keys.length;j++){
   const value=g[keys[j]];
   if(typeof value!=='number'||!Number.isFinite(value))
    throw infrastructure('Original profile has a nonfinite or nonnumeric field '+keys[j]);
   values[i*keys.length+j]=value;
  }
 }
 return {xs,keys,values,cuts};
}

function restoreProfile(table){
 const map=new Map();
 for(let i=0;i<table.xs.length;i++){
  const g={};for(let j=0;j<table.keys.length;j++)g[table.keys[j]]=table.values[i*table.keys.length+j];
  map.set(table.xs[i],g);
 }
 const profile=x=>{
  const g=map.get(x);
  if(g===undefined)throw infrastructure('RK profile lookup argument was not tabulated: '+x);
  return g;
 };
 profile.integrationBreakpoints=table.cuts;
 return profile;
}

function workerLoop(data){
 const {buffers,port,options,tables,id,stepsPerSegment}=data;
 const control=new Int32Array(buffers.control),status=new Int32Array(buffers.status),
  input=new Float64Array(buffers.input),output=new Float64Array(buffers.output),
  jacobian=new Float64Array(buffers.jacobian),scalar=new Float64Array(buffers.scalar),
  statistics=new Float64Array(buffers.statistics),K=2*options.modes;
 const cache=new Map();
 try{
  const cells=tables.map(t=>{
   if(!cache.has(t.mu))cache.set(t.mu,createFourierRootSplitFluxEngine({...options,mu:t.mu}));
   return {engine:cache.get(t.mu),profiles:t.profiles.map(restoreProfile),portRatio:t.portRatio};
  });
  port.postMessage({kind:'ready',worker:id,heapSizeLimit:v8.getHeapStatistics().heap_size_limit});
  Atomics.add(control,C.ready,1);Atomics.notify(control,C.ready);
  let generation=0;
  while(!Atomics.load(control,C.stop)){
   const nextGeneration=Atomics.load(control,C.generation);
   if(nextGeneration===generation){Atomics.wait(control,C.generation,generation);continue;}
   generation=nextGeneration;
   if(Atomics.load(control,C.stop))break;
   const withJac=Atomics.load(control,C.withJac)===1;
   for(;;){
    lock(control);
    const position=Atomics.load(control,C.next),failure=Atomics.load(control,C.firstFailure);
    if(position>=cells.length||position>=failure||Atomics.load(control,C.stop)){
     unlock(control);break;
    }
    Atomics.store(control,C.next,position+1);Atomics.add(control,C.progress,1);unlock(control);
    // A status-1 entry was restored from this exact evaluation's actual
    // output cache. It has already completed the same independent map.
    if(Atomics.load(status,position)===1)continue;
    try{
     const f=serialStageFlow(cells[position],input.subarray(position*K,(position+1)*K),
      {withJac,stepsPerSegment});
     output.set(f.out,position*K);if(withJac)jacobian.set(f.J,position*K*K);
     scalar[3*position]=f.meanHeight;
     scalar[3*position+1]=withJac?f.minA:NaN;scalar[3*position+2]=withJac?f.minD:NaN;
     Atomics.store(status,position,1);
    }catch(error){
     // The claim and failure publication use the same lock. No stage above
     // this observed failure can subsequently be dispatched. Lower already
     // running stages finish, so the original minimum failure is recovered.
     lock(control);
     Atomics.store(control,C.firstFailure,Math.min(position,Atomics.load(control,C.firstFailure)));
     unlock(control);
     port.postMessage({kind:'stage-error',generation,position,index:tables[position].index,
      error:{name:error.name??'Error',message:String(error.message??error),code:error.code??null}});
     Atomics.store(status,position,-1);
    }
    Atomics.add(control,C.progress,1);
   }
   let evaluations=0,roundoffFallbacks=0,maximumRootRelativeResidual=0;
   for(const engine of cache.values()){
    const q=engine.statistics;if(!q)continue;
    evaluations+=q.evaluations;roundoffFallbacks+=q.roundoffFallbacks;
    maximumRootRelativeResidual=Math.max(maximumRootRelativeResidual,q.maximumRootRelativeResidual);
   }
   statistics[3*id]=evaluations;statistics[3*id+1]=roundoffFallbacks;
   statistics[3*id+2]=maximumRootRelativeResidual;
   Atomics.add(control,C.done,1);Atomics.notify(control,C.done);
  }
 }catch(error){
  port.postMessage({kind:'fatal',worker:id,error:{name:error.name??'Error',message:String(error.message??error)}});
  Atomics.store(control,C.fatal,1);Atomics.notify(control,C.done);Atomics.notify(control,C.ready);
 }finally{port.close();}
}

/** Independent finite stage maps; evaluate is synchronous to retain the
 * existing synchronous Newton/Riccati implementation. Only stage maps run
 * concurrently; outputs are copied and reduced in the original index order.
 * close must be awaited before publishing each complete DN response.
 */
export async function createStagePool({stages,modes,quadrature,spacing,orientation,
 projectionFloor,stepsPerSegment,workers=2,cuspAwareFlow=false,
 noProgressMilliseconds=120000,closeGraceMilliseconds=2000,terminateGraceMilliseconds=5000,
 cacheRoot=null,cacheDiagnostic=()=>{}}){
 if(![2,4].includes(workers))throw infrastructure('This optional backend uses two or four workers');
 if(!Array.isArray(stages)||!stages.length||!Number.isInteger(stepsPerSegment)||stepsPerSegment<1)
  throw infrastructure('Nonempty stages and positive integral RK steps required');
 for(const value of [noProgressMilliseconds,closeGraceMilliseconds,terminateGraceMilliseconds])
  if(!Number.isFinite(value)||value<=0)throw infrastructure('Positive finite infrastructure time limits required');
 for(let i=0;i<stages.length;i++){
  if(!Number.isInteger(stages[i].index)||stages[i].index<0||(i&&stages[i].index<=stages[i-1].index))
   throw infrastructure('Stage indices must be distinct and increasing');
  if(stages[i].cell.engine.M!==modes)throw infrastructure('Stage engine order differs from pool order');
 }
 const options={modes,quadrature,spacing,orientation,projectionFloor,cuspAwareFlow};
 const began=performance.now();
 let tables=stages.map(({index,cell})=>({index,mu:cell.mu,portRatio:cell.portRatio,
  profiles:cell.profiles.map(p=>tabulateProfile(p,stepsPerSegment,cuspAwareFlow))}));
 const profileTableMilliseconds=performance.now()-began;
 const count=stages.length,K=2*modes,make=(length,size)=>new SharedArrayBuffer(length*size);
 const stageCache=createStageMapCache({cacheRoot,entryURL:import.meta.url,tables,options,
  stepsPerSegment,count,K,diagnostic:cacheDiagnostic});
 let buffers={control:make(16,4),status:make(count,4),input:make(count*K,8),
  output:make(count*K,8),jacobian:make(count*K*K,8),scalar:make(3*count,8),statistics:make(3*workers,8)};
 let control=new Int32Array(buffers.control),status=new Int32Array(buffers.status),
  input=new Float64Array(buffers.input),output=new Float64Array(buffers.output),
  jacobian=new Float64Array(buffers.jacobian),scalar=new Float64Array(buffers.scalar),
  statistics=new Float64Array(buffers.statistics);
 const metadata={implementation:KIND,workers,stageCount:count,modes,quadrature,stepsPerSegment,
  cuspAwareFlow,profileTableMilliseconds,
  profileCount:tables.reduce((s,t)=>s+t.profiles.length,0),
  exactProfilePoints:tables.reduce((s,t)=>s+t.profiles.reduce((u,p)=>u+p.xs.length,0),0),
  profileTableValueBytes:tables.reduce((s,t)=>s+t.profiles.reduce((u,p)=>u+p.xs.byteLength+p.values.byteLength,0),0),
  sharedBufferBytes:Object.values(buffers).reduce((s,b)=>s+b.byteLength,0),
  policy:'ascending dynamic claims; stop dispatch above first observed failure; minimum failed stage; serial ordered reduction',
  resourceLimits:{maxOldGenerationSizeMb:128,maxYoungGenerationSizeMb:16,stackSizeMb:4},
  noProgressMilliseconds,closeGraceMilliseconds,terminateGraceMilliseconds,
  workerHeapSizeLimitBytes:[],closeBeforeDNResponse:true,stageMapCache:stageCache?.metadata??null};
 const threads=[],ports=[],exits=[],failures=[],messages=[];
 let closed=false,active=false,generation=0;
 const drain=()=>{
  for(const port of ports){let row;while((row=receiveMessageOnPort(port))!==undefined)messages.push(row.message);}
 };
 const fatal=()=>{
  drain();const row=messages.find(m=>m.kind==='fatal');
  if(failures.length||row||Atomics.load(control,C.fatal))
   throw infrastructure('Stage worker failed: '+(failures[0]?.message??row?.error?.message??'worker fatal flag'));
 };
 async function close(){
  if(closed)return;closed=true;
  if(control){Atomics.store(control,C.stop,1);Atomics.add(control,C.generation,1);Atomics.notify(control,C.generation);}
  try{return await closeStageWorkers(threads,exits,{closeGraceMilliseconds,terminateGraceMilliseconds});}
  finally{
   for(const port of ports)port.close();
   tables=null;buffers=null;control=null;status=null;input=null;output=null;jacobian=null;scalar=null;statistics=null;
  }
 }
 try{
  for(let id=0;id<workers;id++){
   const {port1,port2}=new MessageChannel();ports.push(port1);
   const worker=new Worker(new URL(import.meta.url),{workerData:{kind:KIND,id,port:port2,buffers,tables,options,stepsPerSegment},
    transferList:[port2],execArgv:[],resourceLimits:metadata.resourceLimits});
   worker.on('error',e=>failures.push(e));
   exits.push(new Promise(resolve=>worker.once('exit',code=>{
    if(!closed)failures.push(new Error('Stage worker exited unexpectedly with code '+code));resolve(code);
   })));
   threads.push(worker);
  }
  let ready=0,lastReady=performance.now();
  while(Atomics.load(control,C.ready)!==workers){
   fatal();const current=Atomics.load(control,C.ready);
   if(current!==ready){ready=current;lastReady=performance.now();}
   if(performance.now()-lastReady>=noProgressMilliseconds)
    throw infrastructure('Stage worker startup made no shared progress for '+noProgressMilliseconds+' ms');
   await new Promise(r=>setTimeout(r,10));
  }
  drain();
  metadata.workerHeapSizeLimitBytes=messages.filter(m=>m.kind==='ready').sort((a,b)=>a.worker-b.worker).map(m=>m.heapSizeLimit);
  messages.length=0;tables=null;
 }catch(error){await close();throw error;}
 function cumulativeStatistics(){
  if(closed)return null;
  let evaluations=0,roundoffFallbacks=0,maximumRootRelativeResidual=0;
  for(let i=0;i<workers;i++){
   evaluations+=statistics[3*i];roundoffFallbacks+=statistics[3*i+1];
   maximumRootRelativeResidual=Math.max(maximumRootRelativeResidual,statistics[3*i+2]);
  }
  return {evaluations,roundoffFallbacks,maximumRootRelativeResidual,
   scope:'Actual cumulative work in this request pool, including already dispatched later stages after an earlier failure.'};
 }
 function evaluate(inputs,withJac){
  if(closed||active)throw infrastructure('Stage pool is closed or already evaluating');
  if(!Array.isArray(inputs)||inputs.length!==count||typeof withJac!=='boolean')
   throw infrastructure('Stage input count or Jacobian flag differs');
  active=true;
  try{
   fatal();messages.length=0;
   for(let i=0;i<count;i++){
    if(inputs[i].length!==K)throw infrastructure('Stage input dimension differs');
    input.set(inputs[i],i*K);
   }
   status.fill(0);
   const retained=stageCache?.begin(input,withJac,{status,output,jacobian,scalar})??null;
   Atomics.store(control,C.next,0);Atomics.store(control,C.done,0);
   Atomics.store(control,C.firstFailure,count);Atomics.store(control,C.withJac,withJac?1:0);
   generation++;Atomics.store(control,C.generation,generation);Atomics.notify(control,C.generation);
   waitForSharedCompletion({control,doneIndex:C.done,doneCount:workers,progressIndex:C.progress,
    noProgressMilliseconds,checkFatal:fatal,observeProgress:()=>retained?.flush()});
   retained?.finish();fatal();
   const firstFailure=Atomics.load(control,C.firstFailure),results=new Array(count);
   for(let i=0;i<Math.min(count,firstFailure+1);i++){
    if(Atomics.load(status,i)===-1){
     drain();const row=messages.find(m=>m.kind==='stage-error'&&m.generation===generation&&m.position===i);
     if(!row)throw infrastructure('Stage error message was absent after completion barrier');
     const error=new Error(row.error.message);error.name=row.error.name;
     if(row.error.code)error.code=row.error.code;
     results[i]={error};break;
    }
    if(Atomics.load(status,i)!==1)throw infrastructure('A lower stage was not completed before the barrier');
    results[i]={out:output.slice(i*K,(i+1)*K),J:withJac?jacobian.slice(i*K*K,(i+1)*K*K):null,
     meanHeight:scalar[3*i],minA:withJac?scalar[3*i+1]:undefined,minD:withJac?scalar[3*i+2]:undefined};
   }
   return results;
  }finally{active=false;}
 }
 return {evaluate,close,metadata,cumulativeStatistics};
}

if(!isMainThread&&workerData?.kind===KIND)workerLoop(workerData);
