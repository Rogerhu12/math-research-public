// R531 persistent coordinator and dedicated complete-cell worker entry.
// The worker branch imports the real R523-loaded factory only. It never
// imports tail_frozen_worker.mjs or any stdin protocol loop.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {serialize,deserialize} from 'node:v8';
import {Worker,isMainThread,parentPort,workerData,threadId} from 'node:worker_threads';
import {fileURLToPath,pathToFileURL} from 'node:url';

const SCHEMA='R531-complete576-current-cellflow-worker-pool-v1';
const self=fileURLToPath(import.meta.url),here=path.dirname(self);
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const mono=()=>Number(process.hrtime.bigint())/1e9;
const requireValue=(ok,text)=>{if(!ok)throw Error(text);};
function proc(pid){
 try{
  const s=fs.readFileSync('/proc/'+pid+'/stat','utf8'),a=s.slice(s.lastIndexOf(')')+2).split(' ');
  return {pid:Number(s.slice(0,s.indexOf(' '))),state:a[0],ppid:Number(a[1]),pgid:Number(a[2]),
   sid:Number(a[3]),start_ticks:a[19]};
 }catch(e){if(e?.code==='ENOENT'||e?.code==='ESRCH')return null;throw e;}
}
function originalNumber(v){
 const b=Buffer.allocUnsafe(8);b.writeDoubleLE(v);
 return {value:Number.isFinite(v)?v:null,float64le_hex:b.toString('hex'),
  classification:Number.isNaN(v)?'NaN':v===Infinity?'positive-infinity':
   v===-Infinity?'negative-infinity':Object.is(v,-0)?'negative-zero':'finite'};
}
function encode(v){return JSON.stringify(v,(_k,x)=>typeof x==='number'&&
 (!Number.isFinite(x)||Object.is(x,-0))?{R531_original_binary64_number:originalNumber(x)}:x)+'\n';}
function identity(file,base=null){
 const b=fs.readFileSync(file);return {file:base?path.relative(base,file):path.resolve(file),bytes:b.length,sha256:sha(b)};
}
function atomic(file,raw){
 fs.writeFileSync(file+'.writing',raw,{flag:'wx'});fs.renameSync(file+'.writing',file);
}
function writeJSON(file,v){atomic(file,Buffer.from(encode(v)));return identity(file);}
function readJSON(file){return JSON.parse(fs.readFileSync(file,'utf8'));}
function checked(row){
 const b=fs.readFileSync(row.file);requireValue(b.length===row.bytes&&sha(b)===row.sha256,
  'R531 actual payload/source identity differs: '+row.file);return b;
}
function errorRecord(e){
 return {name:e?.name??'Error',message:e?.message??String(e),
  stack:String(e?.stack??e).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<original-data-url-source>'),
  properties:Object.fromEntries(Object.keys(e??{}).map(k=>[k,e[k]]))};
}
function errorSummary(e){
 const tr=e?.finiteRootTrace;
 return {name:e?.name??'Error',message:e?.message??String(e),
  stack:String(e?.stack??e).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<original-data-url-source>'),
  finite_trace_variation:e?.finiteTraceVariation??null,
  original_root_trace:tr?{schema:tr.schema,root_evaluations:tr.root_evaluations,
   line_trials:tr.line_trials,iterations:tr.iterations,return_reason:tr.return_reason,
   accepted_updates:tr.accepted_updates.map(p=>({iteration:p.iteration,backtrack:p.backtrack,alpha:p.alpha})),
   line_decisions:tr.line_decisions}:null};
}
// These five literal guards are thrown by the bound original root source.
// Allocation/transport errors, even when raised during flow, are not given
// mathematical-error priority or a serial-resource-frontier claim.
const originalRootNumericMessages=new Set([
 'momentum profile out of float range','momentum branch D/S/A rejected',
 'momentum Newton matrix not SPD','momentum Newton line search failed',
 'momentum Newton iteration limit']);
function originalNumericError(e){
 return e?.name==='Error'&&originalRootNumericMessages.has(e.message);
}
function requireActions(){
 requireValue(process.env.GITHUB_ACTIONS==='true'&&
  (process.env.GITHUB_REPOSITORY??'').toLowerCase()==='rogerhu12/math-research-public',
  'R531 complete parallel execution belongs only to public Actions');
}
function commonSources(launch){
 for(const row of launch.source_files)checked(row);
 requireValue(launch.source_files.some(r=>path.resolve(r.file)===self),
  'R531 actual pool module must be one of the complete bound sources');
}

async function runWorker(){
 requireActions();
 const {launch,worker_index,directory}=workerData;
 commonSources(launch);
 const factoryPath=path.join(launch.source_topic,'scripts/78718-tail-fourier-root-split-engine.mjs');
 const {createFourierRootSplitFluxEngine}=await import(pathToFileURL(factoryPath).href);
 const traceFile=process.env.VISIBLE_FINITE_TRACE_SOURCE_RECORD,
  capacityFile=process.env.VISIBLE_FLEX_TAIL_CAPACITY_RECORD;
 const trace=readJSON(traceFile),capacity=readJSON(capacityFile);
 requireValue(trace.loaded_root===true&&trace.loaded_split===true&&
  trace.original_root_and_rhs_primal_arithmetic_recovered===true,
  'R531 worker must actually load the original capacity/root/trace/flow factory');
 requireValue(capacity.requestedCapacity===112&&capacity.capacity===112,
  'R531 worker keeps actual full112 capacity');
 const engines=new Map(),engineMetadata=new Map(),engineOptions=new Map();let current=null,busy=false;
 function allEngines(){
  return [...engines].map(([engine_index,e])=>({...engineMetadata.get(engine_index),
   counters:e.finiteTraceStatistics,
   actual_split_RHS_statistics:e.statistics,
   worker_index,thread_id:threadId,
   counts_are_actual_calls_not_unique_state_points:true,
   snapshot_position:current}));
 }
 const sources={trace:identity(traceFile,directory),capacity:identity(capacityFile,directory),
  actual_factory_file:identity(factoryPath),actual_pool_source:identity(self),
  loaded_trace_schema:trace.schema,actual_backend:'original64-noJ-primal-zero-flux-input-support-finite-root-variation-v1'};
 parentPort.postMessage({event:'ready',worker_index,thread_id:threadId,sources});
 parentPort.on('message',message=>{
  if(message.kind==='close'){parentPort.close();return;}
  requireValue(message.kind==='stage'&&!busy,'R531 worker accepts one original stage at a time');
  busy=true;
  const {stage,engine_spec,evaluation_sequence,result_directory,steps}=message;
  const n=stage.stage;
  current={evaluation_sequence,stage:n,rawCell:stage.rawCell,rawSegment:stage.rawSegment,
   phase:'stage-start',profile_index:null,field_index:null};
  parentPort.postMessage({event:'started',worker_index,thread_id:threadId,evaluation_sequence,
   stage:n,rawCell:stage.rawCell,rawSegment:stage.rawSegment});
  let executionPhase='worker-source-and-engine-binding';
  try{
   requireValue(stage.worker_index===worker_index&&engine_spec.worker_index===worker_index,
    'R531 stage uses its original engine fixed worker assignment');
   let engine=engines.get(stage.engine_index);
   if(engine){
    const old=engineOptions.get(stage.engine_index),now=engine_spec.options;
    requireValue(Object.keys(old).length===Object.keys(now).length&&
     Object.keys(old).every(k=>Object.hasOwn(now,k)&&Object.is(old[k],now[k])),
     'R531 keeps the exact actual options of each persistent original engine');
   }
   if(!engine){
    engine=createFourierRootSplitFluxEngine(engine_spec.options);
    requireValue(engine.M===112&&engine.N===2048&&engine.size===226,
     'R531 actual engine has the complete original dimensions');
    requireValue(sha(engine.flowStateWithJacobian.toString())===engine_spec.original_stage_variation_source_sha256&&
     sha(engine.rhsWithJacobian.toString())===engine_spec.original_local_field_source_sha256&&
     sha(engine.rk4.toString())===engine_spec.original_noJ_RK_source_sha256,
     'R531 worker calls the same actually loaded stage/field/noJ methods');
    engines.set(stage.engine_index,engine);engineOptions.set(stage.engine_index,{...engine_spec.options});
    engineMetadata.set(stage.engine_index,{engine_index:stage.engine_index,
     first_stage:engine_spec.original_first_stage,
     original_stage_addresses:engine_spec.stage_addresses,
     stage_count:engine_spec.stage_addresses.length,
     implementation:engine.variationalEvaluation,
     local_field_source_sha256:sha(engine.rhsWithJacobian.toString()),
     stage_variation_source_sha256:sha(engine.flowStateWithJacobian.toString()),
     original_noJ_RK_source_sha256:sha(engine.rk4.toString())});
   }
   const positions=[];
   const profiles=stage.profiles.map((packet,profile_index)=>{
    const position={used:0,total:packet.rows.length};positions.push(position);
    function profile(x){
     const row=packet.rows[position.used];
     if(!(row!==undefined&&Object.is(row.x,x))){
      const e=Error('R531 actual original RK/profile address changed');
      e.parallelCellflowBinding=true;throw e;
     }
     current={evaluation_sequence,stage:n,rawCell:stage.rawCell,rawSegment:stage.rawSegment,
      phase:'captured-original-profile-returned-to-original-root',
      profile_index,field_index:position.used,ordinary_index:row.ordinary_index,
      sub_index:row.sub_index,RK_field_index:row.field_index,x:originalNumber(x)};
     position.used++;
     parentPort.postMessage({event:'position',worker_index,thread_id:threadId,
      evaluation_sequence,stage:n,position:current});
     // The fixed root immediately reads the ordinary original value record;
     // the known-root RHS and captured tangent never call profile again.
     return row.geometry;
    }
    profile.integrationBreakpoints=packet.integrationBreakpoints;
    return profile;
   });
   requireValue(stage.initial instanceof Float64Array&&stage.initial.length===226,
    'R531 sends every original stage state word, including both initialized means');
   executionPhase='original-complete-cell-flow';
   const f=engine.flowStateWithJacobian(stage.initial,profiles,{stepsPerSegment:steps});
   executionPhase='complete-result-transport';
   requireValue(positions.every(p=>p.used===p.total),'R531 complete original profile-call tape was not consumed');
   current={evaluation_sequence,stage:n,rawCell:stage.rawCell,rawSegment:stage.rawSegment,
    phase:'full226-state-and226x224-tangent-returned',profile_positions:positions};
   const file=path.join(result_directory,'stage-'+String(n).padStart(4,'0')+'.v8'),
    raw=serialize(f);
   fs.writeFileSync(file,raw,{flag:'wx'});
   parentPort.postMessage({event:'completed',worker_index,thread_id:threadId,
    evaluation_sequence,stage:n,file:path.basename(file),bytes:raw.length,sha256:sha(raw),
    full_state_entries:226,full_tangent_rows:226,shape_columns:224,
    original_root_calls:f.originalRootCalls,original_RHS_calls:f.originalRhsCalls,
    captured_J_calls:f.capturedJacobianCalls,
    exact_current_engine_snapshots:allEngines(),position:current});
  }catch(error){
   current={...current,phase:'original-stage-or-transport-error-returned'};
   const file=path.join(result_directory,'error-stage-'+String(n).padStart(4,'0')+'.v8'),
    raw=serialize(errorRecord(error));
   fs.writeFileSync(file,raw,{flag:'wx'});
   parentPort.postMessage({event:'stage_error',worker_index,thread_id:threadId,evaluation_sequence,
    stage:n,rawCell:stage.rawCell,rawSegment:stage.rawSegment,
    error:errorSummary(error),stage_execution_phase:executionPhase,
    original_stage_failure:executionPhase==='original-complete-cell-flow'&&
     error?.parallelCellflowBinding!==true&&error?.finiteTraceVariation?.resource_budget!==true&&
     originalNumericError(error),
    unclassified_original_flow_error:executionPhase==='original-complete-cell-flow'&&!originalNumericError(error),
    error_payload:{file:path.basename(file),bytes:raw.length,sha256:sha(raw)},
    resource_budget:error?.finiteTraceVariation?.resource_budget===true,
    exact_current_engine_snapshots:allEngines(),position:current});
  }finally{busy=false;}
 });
}

async function runCoordinator(){
 requireActions();
 const args=process.argv.slice(2);
 requireValue(args.length===4&&args[0]==='--pool-directory'&&args[2]==='--launch-sha256',
  'R531 explicit pool directory and actual launch SHA required');
 const base=path.resolve(args[1]),launchPath=path.join(base,'launch.json'),launchRaw=fs.readFileSync(launchPath);
 requireValue(sha(launchRaw)===args[3],'R531 original parent launch changed');
 const launch=JSON.parse(launchRaw);
 requireValue(launch.schema===SCHEMA&&launch.computations===here&&launch.coordinator===self,
  'R531 binds the actual source directory and independent entry');
 commonSources(launch);
 const own=proc(process.pid),parent=proc(launch.main_owner.pid);
 requireValue(own.ppid===launch.main_owner.pid&&parent&&
  parent.start_ticks===launch.main_owner.start_ticks&&own.pgid===parent.pgid&&own.sid===parent.sid,
  'R531 coordinator stays in the actual original owner group');
 requireValue(Number(process.env.VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC)===launch.deadline_monotonic,
  'R531 must not reset the original scientific clock');
 writeJSON(path.join(base,'pool-owner.json'),{schema:SCHEMA+'-actual-owner',actual:own,
  parent:launch.main_owner,source:identity(self),same_original_pgid_and_sid:true});
 const workers=[],evaluations=[];let active=null,lastSequence=-1,closing=false,
  readyCount=0,finishStarted=false,poll=null,watchdog=null;
 const eventFile=path.join(base,'events.jsonl'),eventHash=crypto.createHash('sha256');
 let eventBytes=0,eventRows=0,lastProgressRows=-1;
 fs.writeFileSync(eventFile,'',{flag:'wx'});
 function event(row){
  const raw=Buffer.from(encode({utc:new Date().toISOString(),...row}));
  fs.appendFileSync(eventFile,raw);eventHash.update(raw);eventBytes+=raw.length;eventRows++;
 }
 function eventIdentity(){return {file:path.relative(base,eventFile),bytes:eventBytes,
  rows:eventRows,sha256:eventHash.copy().digest('hex'),complete_successfully_written_prefix:true};}
 function stageAddress(s){return [s.stage,s.rawCell,s.rawSegment,s.engine_index,s.worker_index];}
 function currentSummary(){
  if(!active)return null;
  const statuses={unvisited:[],assigned_not_started:[],started_without_completed_return:[],
   completed:[],stage_error:[],interrupted_without_completed_return:[]};
  for(let n=0;n<active.rows.length;n++)statuses[active.rows[n].status].push(n);
  return {evaluation_sequence:active.input.evaluation_sequence,context:active.input.context,
   input:active.input_identity,stage_address_columns:['stage','rawCell','rawSegment','engine_index','worker_index'],
   stage_addresses:active.input.stages.map(stageAddress),
   actual_stage_status_indices:statuses,first_reported_error_stage:active.errorLimit,
   errors:active.errors,stop_reason:active.stopReason,
   completion_not_inferred_from_counts_or_worker_readiness:true};
 }
 function progress(){
  lastProgressRows=eventRows;
  writeJSON(path.join(base,'progress.json'),{schema:SCHEMA+'-actual-progress',
   original_owner:launch.main_owner,actual_coordinator:own,original_deadline_monotonic:launch.deadline_monotonic,
   worker_count:workers.length,closing,current_evaluation:currentSummary(),completed_evaluations:evaluations,
   workers:workers.map(w=>({worker_index:w.index,thread_id:w.threadId,
    ready:w.ready,online:w.online,exit_event:w.exit,uncaught_error:w.error,
    current_stage:w.current,latest_position:w.position,sources:w.sources,
    statistics:w.statistics,statistics_are_exact_at_last_reported_position:w.statisticsPosition,
    current_incomplete_stage_has_no_fabricated_statistics:w.current!==null,
    worker_JS_resource_limits:w.limits})),
   events:eventIdentity(),no_source_or_scientific_result_uploaded:true});
 }
 function workerSnapshot(w,message){
  if(message.exact_current_engine_snapshots){
   w.statistics=message.exact_current_engine_snapshots;w.statisticsPosition=message.position;
  }
  if(message.position)w.position=message.position;
 }
 function startNext(w){
  if(!active||closing||w.current!==null||!w.ready)return;
  const n=w.queue.find(n=>active.rows[n].status==='unvisited'&&
   (active.errorLimit===null||n<active.errorLimit));
  if(n===undefined)return;
  const row=active.rows[n],stage=active.input.stages[n];
  row.status='assigned_not_started';w.current=n;
  event({event:'assigned',evaluation_sequence:active.input.evaluation_sequence,
   stage:n,worker_index:w.index,thread_id:w.threadId});
  w.worker.postMessage({kind:'stage',stage,engine_spec:active.input.engines[stage.engine_index],
   evaluation_sequence:active.input.evaluation_sequence,
   result_directory:active.directory,steps:active.input.steps});
 }
 function finishEvaluation(){
  if(!active)return;
  const a=active,input=a.input,
   complete=a.rows.every(r=>r.status==='completed'),
   errorStages=a.errors.map(e=>e.stage).filter(Number.isInteger).sort((x,y)=>x-y),
   first=errorStages.length?errorStages[0]:null,
   priority=first!==null&&a.rows.slice(0,first).every(r=>r.status==='completed'),
   selected=priority?a.errors.find(e=>e.stage===first&&e.original_stage_failure===true):null;
  const actual=currentSummary();
  const result={schema:SCHEMA+'-evaluation-result',evaluation_sequence:input.evaluation_sequence,
   input:a.input_identity,context:input.context,complete,resource_budget:a.resourceBudget,
   stop_reason:complete?null:a.stopReason??'original-stage-error',
   original_first_stage_error_priority_proved:priority&&selected!==null,
   original_stage_error:selected?{...selected.error_payload,stage:selected.stage,
    rawCell:input.stages[selected.stage].rawCell,rawSegment:input.stages[selected.stage].rawSegment}:null,
   all_original_reported_errors:a.errors,actual_status:actual,
   completed:a.rows.flatMap((r,n)=>r.status==='completed'?[{stage:n,...r.output}]:[]),
   complete_results_in_original_n_order:true,worker_numeric_order_not_global_order:true,
   changed_resource_frontier_not_original_serial_partial_equivalence:true,
   task_completed:false};
  const file=path.join(a.directory,'result.json');
  writeJSON(file,result);
  evaluations.push({evaluation_sequence:input.evaluation_sequence,context:input.context,
   input:a.input_identity,result:identity(file,base),complete,
   actual_status:actual,resource_budget:a.resourceBudget,
   original_first_stage_error_priority_proved:priority&&selected!==null,
   completed_stage_count:result.completed.length});
  event({event:'evaluation_return',evaluation_sequence:input.evaluation_sequence,complete,
   result:identity(file,base),first_original_error_stage:priority&&selected!==null?first:null});
  active=null;for(const w of workers){w.current=null;w.queue=[];}
  progress();
 }
 function maybeFinish(){
  if(!active||closing)return;
  for(const w of workers)startNext(w);
  if(workers.every(w=>w.current===null))finishEvaluation();
 }
 async function shutdown(reason,{resource=false}={}){
  if(finishStarted)return;finishStarted=true;closing=true;
  if(poll)clearInterval(poll);if(watchdog)clearInterval(watchdog);
  if(active){active.stopReason=reason;active.resourceBudget=resource;}
  const retentionErrors=[];
  const retain=fn=>{try{fn();}catch(e){retentionErrors.push(errorSummary(e));}};
  retain(()=>event({event:'pool_shutdown_requested',reason,resource_budget:resource}));
  retain(progress);
  // Actual thread termination must still be attempted when a metadata write,
  // including ENOSPC, fails. Such failure never creates a successful receipt.
  await Promise.allSettled(workers.map(async w=>{
   if(w.exit!==null)return;
   w.termination_requested=true;
   try{await w.worker.terminate();}catch(e){w.termination_error=errorSummary(e);}
  }));
  // exit handlers run before terminate() promises fulfill.
  if(active){
   for(const w of workers)if(w.current!==null&&
    !['completed','stage_error'].includes(active.rows[w.current].status))
     active.rows[w.current].status='interrupted_without_completed_return';
   retain(finishEvaluation);
  }
  retain(progress);
  retain(()=>writeJSON(path.join(base,'pool-closed.json'),{schema:SCHEMA+'-actual-closed',
   reason,resource_budget:resource,actual_coordinator:own,original_owner:launch.main_owner,
   all_worker_exit_events_observed:workers.every(w=>w.exit!==null),
   workers:workers.map(w=>({worker_index:w.index,thread_id:w.threadId,exit_event:w.exit,
    termination_requested:w.termination_requested===true,
    termination_error:w.termination_error??null,uncaught_error:w.error,
    statistics:w.statistics,statistics_position:w.statisticsPosition,last_position:w.position,
    sources:w.sources})),evaluations,retention_errors:retentionErrors,
   last_progress:fs.existsSync(path.join(base,'progress.json'))?
    identity(path.join(base,'progress.json'),base):null,events:eventIdentity(),
   no_acceptance_inferred_from_complete_worker_exit:true}));
  process.exitCode=resource?124:reason==='requested-close'&&retentionErrors.length===0?0:1;
  if(workers.some(w=>w.exit===null)){
   // If thread exit itself remains unknown, ending this real coordinator
   // ends its threads. The parent/outer owner must then report that boundary.
   process.stderr.write('R531 worker exit event unavailable; terminating coordinator\n');
   process.kill(process.pid,'SIGKILL');
  }
 }
 try{
 for(let i=0;i<launch.worker_count;i++){
  const directory=path.join(base,'worker-'+String(i).padStart(2,'0'));fs.mkdirSync(directory);
  const env={...process.env,NODE_OPTIONS:'',
   VISIBLE_FINITE_TRACE_SOURCE_RECORD:path.join(directory,'finite-trace-source.json'),
   VISIBLE_FLEX_TAIL_CAPACITY_RECORD:path.join(directory,'capacity-source.json')};
  const limits={maxOldGenerationSizeMb:launch.worker_heap_mb,maxYoungGenerationSizeMb:4,stackSizeMb:4};
  const worker=new Worker(new URL(import.meta.url),{workerData:{launch,worker_index:i,directory},
   env,execArgv:['--import',path.join(here,'exact_20261114_tail_capacity_loader.mjs'),
    '--import',path.join(here,'geometry_20261116_original64_input_support_contracted_finite_trace_loader.mjs')],
   resourceLimits:limits,stdin:false,stdout:true,stderr:true,trackUnmanagedFds:true});
  const w={index:i,worker,threadId:worker.threadId,ready:false,online:false,exit:null,error:null,
   current:null,position:null,statistics:[],statisticsPosition:null,sources:null,limits,queue:[]};
  workers.push(w);
  const out=fs.createWriteStream(path.join(directory,'stdout.log'),{flags:'wx'}),
   err=fs.createWriteStream(path.join(directory,'stderr.log'),{flags:'wx'});
  worker.stdout.pipe(out);worker.stderr.pipe(err);
  worker.on('online',()=>{w.online=true;event({event:'worker_online',worker_index:i,thread_id:w.threadId});});
  worker.on('message',message=>{
   try{
    requireValue(message.worker_index===i&&message.thread_id===w.threadId,
     'R531 actual worker message owner differs');
    if(message.event==='ready'){
     requireValue(!w.ready,'R531 worker may become ready only once');w.ready=true;w.sources=message.sources;readyCount++;
     event({event:'worker_ready',worker_index:i,thread_id:w.threadId,sources:w.sources});
     if(readyCount===launch.worker_count)writeJSON(path.join(base,'pool-ready.json'),{
      schema:SCHEMA+'-actually-ready',actual_coordinator:own,
      worker_count:workers.length,actual_worker_ids:workers.map(v=>[v.index,v.threadId]),
      real_original_factory_loaded_in_every_worker:true});
     progress();return;
    }
    requireValue(active&&message.evaluation_sequence===active.input.evaluation_sequence&&
     message.stage===w.current,'R531 actual worker stage address differs');
    const row=active.rows[message.stage];
    if(message.event==='started'){
     requireValue(row.status==='assigned_not_started','R531 stage starts once');
     row.status='started_without_completed_return';event(message);return;
    }
    if(message.event==='position'){w.position=message.position;event(message);return;}
    workerSnapshot(w,message);
    if(message.event==='completed'){
     requireValue(row.status==='started_without_completed_return','R531 completion follows a real start');
     row.status='completed';row.output={file:message.file,bytes:message.bytes,sha256:message.sha256};
     event({event:'completed',evaluation_sequence:message.evaluation_sequence,stage:message.stage,
      worker_index:i,thread_id:w.threadId,output:row.output});
     w.current=null;progress();maybeFinish();return;
    }
    if(message.event==='stage_error'){
     row.status='stage_error';active.errors.push({stage:message.stage,worker_index:i,thread_id:w.threadId,
      error:message.error,error_payload:message.error_payload,resource_budget:message.resource_budget,
      stage_execution_phase:message.stage_execution_phase,original_stage_failure:message.original_stage_failure,
      unclassified_original_flow_error:message.unclassified_original_flow_error,
      position:message.position});
     active.errorLimit=active.errorLimit===null?message.stage:Math.min(active.errorLimit,message.stage);
     event({event:'stage_error',evaluation_sequence:message.evaluation_sequence,stage:message.stage,
      worker_index:i,thread_id:w.threadId,error:message.error,error_payload:message.error_payload,
      resource_budget:message.resource_budget});
     w.current=null;
     if(message.resource_budget){void shutdown('original-variation-resource-budget',{resource:true});}
     else if(message.original_stage_failure!==true){void shutdown('worker-source-transport-or-unclassified-flow-error');}
     else {progress();maybeFinish();}
     return;
    }
    throw Error('Unknown R531 worker message');
   }catch(error){w.error=errorSummary(error);void shutdown('coordinator-message-contract-error');}
  });
  worker.on('messageerror',error=>{w.error=errorSummary(error);void shutdown('worker-message-decode-error');});
  worker.on('error',error=>{w.error=errorSummary(error);event({event:'worker_uncaught_error',
   worker_index:i,thread_id:w.threadId,error:w.error});void shutdown('worker-uncaught-error');});
  worker.on('exit',code=>{
   w.exit={code,observed_utc:new Date().toISOString()};
   try{event({event:'worker_exit',worker_index:i,thread_id:w.threadId,code});}
   catch(error){w.exit.event_retention_error=errorSummary(error);}
   if(!closing)void shutdown('worker-ended-before-pool-close');
  });
 }
 function readControl(){
  const file=path.join(base,'control.json');if(!fs.existsSync(file)||closing)return;
  const control=readJSON(file);requireValue(control.schema===SCHEMA+'-control','R531 control schema differs');
  if(control.kind==='close'){void shutdown('requested-close');return;}
  requireValue(control.kind==='evaluate','Unknown R531 pool control');
  if(control.evaluation_sequence===lastSequence)return;
  requireValue(control.evaluation_sequence===lastSequence+1&&!active&&readyCount===workers.length,
   'R531 actual evaluations are sequential and nonoverlapping');
  const raw=checked(control.input),input=deserialize(raw);
  requireValue(input.schema===SCHEMA+'-evaluation-input'&&
   input.evaluation_sequence===control.evaluation_sequence&&input.depth===576&&
   input.M===112&&input.K===224&&input.size===226&&input.stages.length===576,
   'R531 actual complete input binding differs');
  for(let n=0;n<input.stages.length;n++){
   const s=input.stages[n];requireValue(s.stage===n&&
    s.worker_index===s.engine_index%workers.length,'R531 exact original stage map differs');
  }
  for(const e of input.engines)e.stage_addresses=input.stages.filter(s=>s.engine_index===e.engine_index).map(s=>s.stage);
  active={input,input_identity:control.input,directory:path.resolve(control.directory),
   rows:input.stages.map(()=>({status:'unvisited',output:null})),
   errorLimit:null,errors:[],stopReason:null,resourceBudget:false};
  requireValue(active.directory.startsWith(base+path.sep),'R531 result directory must remain in its owned pool');
  lastSequence=control.evaluation_sequence;
  for(const w of workers){w.queue=input.stages.filter(s=>s.worker_index===w.index).map(s=>s.stage);w.current=null;}
  event({event:'evaluation_started',evaluation_sequence:lastSequence,context:input.context,
   input:control.input,actual_engine_count:input.engines.length});
  progress();maybeFinish();
 }
 poll=setInterval(()=>{try{readControl();}catch(e){event({event:'control_error',error:errorSummary(e)});
  void shutdown('coordinator-control-error');}},10);
 watchdog=setInterval(()=>{
  const p=proc(launch.main_owner.pid);
  if(!p||p.start_ticks!==launch.main_owner.start_ticks||p.state==='Z'||p.state==='X')
   void shutdown('original-owner-ended');
  else if(mono()>=launch.deadline_monotonic)void shutdown('original-scientific-deadline',{resource:true});
  else if(active&&eventRows!==lastProgressRows)progress();
 },1000);
 process.once('SIGTERM',()=>void shutdown('SIGTERM',{resource:mono()>=launch.deadline_monotonic}));
 process.once('SIGINT',()=>void shutdown('SIGINT'));
 progress();
 }catch(error){
  event({event:'coordinator-construction-error',error:errorSummary(error)});
  await shutdown('coordinator-construction-error');
  throw error;
 }
}

if(isMainThread){
 try{await runCoordinator();}
 catch(error){
  // This is an actual construction/transport error, never a retry or a
  // mathematical rejection synthesized from a missing component.
  process.stderr.write(String(error?.stack??error)+'\n');process.exitCode=1;
 }
}else{
 try{await runWorker();}
 catch(error){process.stderr.write(String(error?.stack??error)+'\n');throw error;}
}
