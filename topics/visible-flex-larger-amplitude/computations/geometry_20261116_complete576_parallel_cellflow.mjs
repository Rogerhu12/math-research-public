// R531: synchronous full576 with-J dispatcher backed by one owned process
// and two-to-four real worker threads. Original no-J trials never enter here.
// Runtime only: this module does not import or construct a scientific engine.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
import {serialize,deserialize} from 'node:v8';
import {pathToFileURL,fileURLToPath} from 'node:url';

export const PARALLEL_CELLFLOW_SCHEMA='R531-complete576-current-cellflow-worker-pool-v1';
const here=path.dirname(fileURLToPath(import.meta.url));
const sha=raw=>crypto.createHash('sha256').update(raw).digest('hex');
const sleepWord=new Int32Array(new SharedArrayBuffer(4));
const mono=()=>Number(process.hrtime.bigint())/1e9;
const plainError=e=>({name:e?.name??'Error',message:e?.message??String(e),
 stack:String(e?.stack??e).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<original-data-url-source>')});
function requireValue(ok,text){if(!ok)throw Error(text);}
function proc(pid){
 try{
  const text=fs.readFileSync('/proc/'+pid+'/stat','utf8'),p=text.lastIndexOf(')'),a=text.slice(p+2).split(' ');
  return {pid:Number(text.slice(0,text.indexOf(' '))),state:a[0],ppid:Number(a[1]),
   pgid:Number(a[2]),sid:Number(a[3]),start_ticks:a[19]};
 }catch(e){if(e?.code==='ENOENT'||e?.code==='ESRCH')return null;throw e;}
}
function identity(file){
 const raw=fs.readFileSync(file);return {file:path.resolve(file),bytes:raw.length,sha256:sha(raw)};
}
function originalNumber(value){
 const b=Buffer.allocUnsafe(8);b.writeDoubleLE(value);
 return {value:Number.isFinite(value)?value:null,float64le_hex:b.toString('hex'),
  classification:Number.isNaN(value)?'NaN':value===Infinity?'positive-infinity':
   value===-Infinity?'negative-infinity':Object.is(value,-0)?'negative-zero':'finite'};
}
function json(value){
 return JSON.stringify(value,(_k,v)=>typeof v==='number'&&(!Number.isFinite(v)||Object.is(v,-0))?
  {R531_original_binary64_number:originalNumber(v)}:v)+'\n';
}
function atomic(file,raw){
 const temporary=file+'.writing';fs.writeFileSync(temporary,raw,{flag:'wx'});fs.renameSync(temporary,file);
}
function writeJSON(file,value){atomic(file,Buffer.from(json(value)));return identity(file);}
function readJSON(file){return JSON.parse(fs.readFileSync(file,'utf8'));}
function binaryRowsHash(rows){
 const h=crypto.createHash('sha256');
 for(const row of rows){
  requireValue(row instanceof Float64Array,'R531 requires actual typed state rows');
  h.update(Buffer.from(row.buffer,row.byteOffset,row.byteLength));
 }
 return h.digest('hex');
}
function restoreError(record){
 const e=new Error(record.message);e.name=record.name??'Error';
 if(record.stack)e.stack=record.stack;
 Object.assign(e,record.properties??{});return e;
}
function sourceFile(row){
 const raw=fs.readFileSync(row.file);
 requireValue(raw.length===row.bytes&&sha(raw)===row.sha256,'R531 actual source differs: '+row.file);
 return row;
}
function keepRaw(file,base){
 const id=identity(file);return {...id,file:path.relative(base,id.file)};
}

// The caller supplies the real bound original factory options and actual
// cell/profile objects. No saved H, state, J, profile midpoint or new geometry
// reconstruction is used. Profile evaluation itself stays in the main thread.
export async function loadParallelCellflowConstructor(){
 const root=process.env.VISIBLE_FLEX_SOURCE_ROOT;
 requireValue(root,'R531 requires the actual restored source root');
 const cusp=path.join(root,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs');
 requireValue(sha(fs.readFileSync(cusp))==='b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f',
  'R531 requires the original exact cusp helper');
 const {splitIntegrationInterval}=await import(pathToFileURL(cusp).href);
 return options=>createController(options,splitIntegrationInterval);
}

function createController({output,spec,sourceFiles,workerCount,workerHeapMb},splitIntegrationInterval){
 requireValue(process.env.GITHUB_ACTIONS==='true'&&
  (process.env.GITHUB_REPOSITORY??'').toLowerCase()==='rogerhu12/math-research-public',
  'R531 execution belongs to the public Actions owner');
 requireValue(Number.isInteger(workerCount)&&workerCount>=2&&workerCount<=4,
  'R531 declares exactly two-to-four real cellflow workers');
 requireValue(Number.isInteger(workerHeapMb)&&workerHeapMb>=256&&workerHeapMb<=6144,
  'R531 requires an explicit worker JS heap bound');
 requireValue(spec.parallel_cellflows.original_node_heap_cap_mb===6144&&
  workerCount*workerHeapMb<=spec.parallel_cellflows.original_node_heap_cap_mb,
  'R531 explicit aggregate worker JS-heap ceilings fit the retained original declared Node heap amount');
 const deadline=Number(process.env.VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC);
 requireValue(Number.isFinite(deadline)&&Number.isFinite(spec.bridge.global_deadline_unix_ms),
  'R531 consumes the original absolute clocks');
 const base=path.resolve(output),temporary=path.resolve(process.env.RUNNER_TEMP??'');
 requireValue(temporary&&base.startsWith(temporary+path.sep)&&base!==temporary,
  'R531 raw belongs to the current owned RUNNER_TEMP namespace');
 fs.mkdirSync(base,{recursive:false});
 const sourceMap=sourceFiles.map(sourceFile);
 const coordinator=path.join(here,'geometry_20261116_complete576_cellflow_pool.mjs');
 requireValue(sourceMap.some(r=>path.resolve(r.file)===coordinator),'R531 pool source must be explicitly bound');
 const self=fileURLToPath(import.meta.url);
 requireValue(sourceMap.some(r=>path.resolve(r.file)===self),'R531 dispatcher source must be explicitly bound');
 const owner=proc(process.pid),launch={
  schema:PARALLEL_CELLFLOW_SCHEMA,repository:process.env.GITHUB_REPOSITORY,
  actions_run_id:process.env.GITHUB_RUN_ID,actions_sha:process.env.GITHUB_SHA,
  source_sha256:identity(self).sha256,spec_sha256:spec.actual_spec_sha256,
  main_owner:owner,source_files:sourceMap,worker_count:workerCount,
  worker_heap_mb:workerHeapMb,original_node_heap_cap_mb:spec.parallel_cellflows.original_node_heap_cap_mb,
  worker_heap_limit_is_not_a_process_RSS_or_ArrayBuffer_limit:true,
  main_original_heap_ceiling_unchanged_and_additional_worker_RSS_not_claimed_free:true,
  actual_main_exec_argv:process.execArgv,
  inherited_NODE_OPTIONS:process.env.NODE_OPTIONS??null,
  child_has_only_explicit_capacity_and_trace_preloads:true,
  deadline_monotonic:deadline,original_deadline_unix_ms:spec.bridge.global_deadline_unix_ms,
  source_topic:process.env.VISIBLE_FLEX_SOURCE_TOPIC,source_root:process.env.VISIBLE_FLEX_SOURCE_ROOT,
  mode_capacity:process.env.VISIBLE_FLEX_TAIL_MODE_CAPACITY,
  coordinator,computations:here,no_stdin_protocol_worker_imported:true,
  no_original_noJ_or_R273_or_final_gate_replaced:true};
 const launchPath=path.join(base,'launch.json');writeJSON(launchPath,launch);
 const stdoutPath=path.join(base,'coordinator.stdout.log'),stderrPath=path.join(base,'coordinator.stderr.log'),
  stdout=fs.openSync(stdoutPath,'wx'),stderr=fs.openSync(stderrPath,'wx');
 let child,spawnError=null,closed=false,sequence=0,preparedStages=[],current=null;
 try{
  // No inherited --import hook, NODE_OPTIONS preload or V8 heap flag is
  // installed in this coordinator. Its workers have explicit resourceLimits.
  child=spawn(process.execPath,[coordinator,'--pool-directory',base,'--launch-sha256',identity(launchPath).sha256],{
   cwd:here,shell:false,detached:false,stdio:['ignore',stdout,stderr],
   env:{...process.env,NODE_OPTIONS:''}});
  child.once('error',e=>{spawnError=plainError(e);});
  child.unref();
 }finally{fs.closeSync(stdout);fs.closeSync(stderr);}
 requireValue(Number.isInteger(child?.pid)&&child.pid>0,'R531 coordinator did not acquire a process id');
 const childStarted=proc(child.pid);
 if(!(childStarted&&childStarted.ppid===process.pid&&childStarted.pgid===owner.pgid&&childStarted.sid===owner.sid)){
  // No controller escapes without owning the real child start identity.
  try{if(childStarted&&childStarted.ppid===process.pid)process.kill(child.pid,'SIGKILL');}catch(_){}
  throw Error('R531 could not bind the real child start ticks and original process group');
 }
 writeJSON(path.join(base,'spawn.json'),{schema:PARALLEL_CELLFLOW_SCHEMA+'-spawn',
  child_pid:child.pid,observed_child:childStarted,main_owner:owner,
  shell:false,detached:false,stdout:keepRaw(stdoutPath,base),stderr:keepRaw(stderrPath,base)});
 function childLive(){
  const now=proc(child.pid);
  return now&&now.state!=='Z'&&now.state!=='X'&&
   now.start_ticks===childStarted.start_ticks;
 }
 function waitFor(file,{allowClosing=false}={}){
  while(!fs.existsSync(file)){
   if(spawnError)throw Object.assign(Error(spawnError.message),{parallelCellflowSpawn:spawnError});
   if(!childLive())throw Error('R531 coordinator ended before '+path.basename(file));
   if(!allowClosing&&mono()>=deadline){
    const e=Error('R531-original-scientific-deadline');
    e.finiteTraceVariation={resource_budget:true};throw e;
   }
   Atomics.wait(sleepWord,0,0,25);
  }
  return readJSON(file);
 }
 function workerDirectory(n){return path.join(base,'worker-'+String(n).padStart(2,'0'));}
 function snapshot(){
  const result={schema:PARALLEL_CELLFLOW_SCHEMA+'-parent-snapshot',pool_directory:base,
   launch:keepRaw(launchPath,base),spawn:keepRaw(path.join(base,'spawn.json'),base),
   sequence,closed,actual_child_pid:child.pid,actual_child_process_now:proc(child.pid),
   same_absolute_scientific_clock:true,current_preparation:current,
   numerical_output_only_returned_after_all576_completed:true,
   main_noJ_and_endpoint_engine_statistics_are_separate:true};
  for(const [key,name] of [['progress','progress.json'],['terminal','pool-closed.json'],['ready','pool-ready.json']]){
   const f=path.join(base,name);result[key]=fs.existsSync(f)?{identity:keepRaw(f,base),actual:readJSON(f)}:null;
  }
  return result;
 }
 function prepareProfile(profile,stage,profileIndex,steps,cuspAwareFlow){
  const breakpoints=Array.from(profile.integrationBreakpoints??[]),rows=[];
  for(let k=0;k<steps;k++){
   const x=k/steps,h=1/steps;
   const grid=cuspAwareFlow?splitIntegrationInterval(x,x+h,breakpoints):[x,x+h];
   const intervals=grid.length===2?[[x,h]]:grid.slice(0,-1).map((a,i)=>[a,grid[i+1]-a]);
   for(let sub=0;sub<intervals.length;sub++){
    const [a,delta]=intervals[sub],xs=[a,a+delta/2,a+delta/2,a+delta];
    for(let field=0;field<4;field++){
     if(mono()>=deadline){
      const e=Error('R531-original-scientific-deadline-during-profile-capture');
      e.finiteTraceVariation={resource_budget:true};throw e;
     }
     current.position={stage,profile_index:profileIndex,ordinary_index:k,sub_index:sub,
      field_index:field,profile_x:originalNumber(xs[field]),phase:'before-original-profile-call'};
     const geometry=profile(xs[field]);
     // serialize/deserialize makes an owned copy, preserving typed words and
     // signed zero. The fixed original profile returns an ordinary value record.
     rows.push({x:xs[field],geometry:deserialize(serialize(geometry)),
      ordinary_index:k,sub_index:sub,field_index:field});
     current.profile_calls_completed++;
     current.position.phase='original-profile-call-captured';
    }
   }
  }
  return {integrationBreakpoints:breakpoints,rows};
 }
 function evaluate(args){
  requireValue(!closed,'R531 pool was already closed');
  const {cells,states,target,scales,M,K,depth,steps,options,context}=args;
  requireValue(M===112&&K===224&&depth===576&&cells.length===depth&&states.length===depth+1,
   'R531 retains the actual original full112/576 layout');
  requireValue(Number.isInteger(steps)&&steps>0,'R531 retains the actual positive RK step count');
  const id=sequence++,directory=path.join(base,'evaluation-'+String(id).padStart(5,'0'));
  fs.mkdirSync(directory,{recursive:false});
  const preparationJournal=path.join(directory,'preparation-events.jsonl');
  fs.writeFileSync(preparationJournal,'',{flag:'wx'});
  const preparationEvent=value=>fs.appendFileSync(preparationJournal,json(value));
  current={evaluation_sequence:id,context,phase:'original-profile-capture',profile_calls_completed:0,
   prepared_stages:[],position:null,preparation_complete:false};
  const engineIds=new Map(),engines=[],stages=[];preparedStages=[];
  try{
   // Establish every real stage address before the first profile call, so
   // a preparation interruption still has an explicit unvisited suffix.
   for(let n=0;n<depth;n++){
    const c=cells[n];if(engineIds.has(c.engine))continue;
    const engineIndex=engines.length;engineIds.set(c.engine,engineIndex);
    engines.push({engine_index:engineIndex,worker_index:engineIndex%workerCount,
     options:{...options,mu:c.mu},original_first_stage:n,
     original_stage_variation_source_sha256:sha(c.engine.flowStateWithJacobian.toString()),
     original_local_field_source_sha256:sha(c.engine.rhsWithJacobian.toString()),
     original_noJ_RK_source_sha256:sha(c.engine.rk4.toString())});
   }
   writeJSON(path.join(directory,'evaluation-start.json'),{schema:PARALLEL_CELLFLOW_SCHEMA+'-actual-start',
    evaluation_sequence:id,context,engines,steps,
    stage_address_columns:['stage','rawCell','rawSegment','engine_index','worker_index'],
    stage_addresses:cells.map((c,n)=>[n,c.rawCell,c.rawSegment,engineIds.get(c.engine),
     engineIds.get(c.engine)%workerCount]),
    actual_state_float64le_sha256:binaryRowsHash(states),
    actual_target_float64le_sha256:binaryRowsHash([target]),
    actual_scales_float64le_sha256:binaryRowsHash([scales]),
    no_profile_or_cellflow_call_completed_by_this_record:true});
   for(let n=0;n<depth;n++){
    const c=cells[n],engineIndex=engineIds.get(c.engine);
    const s=new Float64Array(K+2);s.set(states[n+1]);
    const stage={stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,
     engine_index:engineIndex,worker_index:engineIndex%workerCount,portRatio:c.portRatio,
     initial:s,profiles:[]};
    preparationEvent({event:'stage-profile-capture-started',evaluation_sequence:id,
     stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,engine_index:engineIndex,
     worker_index:stage.worker_index,actual_cellflow_not_yet_started:true});
    for(let p=0;p<c.profiles.length;p++)
     stage.profiles.push(prepareProfile(c.profiles[p],n,p,steps,options.cuspAwareFlow===true));
    stages.push(stage);preparedStages.push(n);current.prepared_stages.push(n);
    preparationEvent({event:'stage-profile-capture-completed',evaluation_sequence:id,
     stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,engine_index:engineIndex,
     worker_index:stage.worker_index,profile_calls_completed:current.profile_calls_completed});
   }
   current.preparation_complete=true;current.phase='waiting-for-workers';
   const input={schema:PARALLEL_CELLFLOW_SCHEMA+'-evaluation-input',evaluation_sequence:id,context,
    M,K,size:K+2,depth,steps,engines,stages,
    actual_state_float64le_sha256:binaryRowsHash(states),
    actual_target_float64le_sha256:binaryRowsHash([target]),
    actual_scales_float64le_sha256:binaryRowsHash([scales]),
    source_spec_sha256:spec.actual_spec_sha256,
    original_profile_call_order:'stage/profile/ordinary-step/cusp-substep/a,b,c,d',
    preparation:current};
   const raw=serialize(input),inputFile=path.join(directory,'input.v8');
   fs.writeFileSync(inputFile,raw,{flag:'wx'});
   writeJSON(path.join(directory,'input-identity.json'),{...keepRaw(inputFile,directory),
    schema:input.schema,evaluation_sequence:id,context,engines,
    stage_addresses:stages.map(s=>[s.stage,s.rawCell,s.rawSegment,s.engine_index,s.worker_index]),
    actual_state_float64le_sha256:input.actual_state_float64le_sha256,
    actual_target_float64le_sha256:input.actual_target_float64le_sha256,
    actual_scales_float64le_sha256:input.actual_scales_float64le_sha256,
    preparation:current});
   waitFor(path.join(base,'pool-ready.json'));
   writeJSON(path.join(base,'control.json'),{schema:PARALLEL_CELLFLOW_SCHEMA+'-control',
    kind:'evaluate',evaluation_sequence:id,input:identity(inputFile),directory});
   const result=waitFor(path.join(directory,'result.json'));
   current.phase='consuming-complete-worker-result';current.result=keepRaw(path.join(directory,'result.json'),base);
   requireValue(result.evaluation_sequence===id&&result.input.sha256===sha(raw),
    'R531 result must identify this exact actual input');
   if(result.original_stage_error){
    const p=path.join(directory,result.original_stage_error.file),r=fs.readFileSync(p);
    requireValue(r.length===result.original_stage_error.bytes&&sha(r)===result.original_stage_error.sha256,
     'R531 original error payload identity changed');
    const e=restoreError(deserialize(r));
    Object.assign(e,{tailStage:result.original_stage_error.stage,
     tailRawCell:result.original_stage_error.rawCell,tailRawSegment:result.original_stage_error.rawSegment,
     parallelCellflow:{evaluation_sequence:id,result:current.result,
      original_first_stage_error_priority_proved:result.original_first_stage_error_priority_proved===true}});
    throw e;
   }
   if(!result.complete){
    const e=Error('R531 full576 parallel evaluation incomplete: '+String(result.stop_reason));
    e.parallelCellflow={evaluation_sequence:id,result:current.result,stop_reason:result.stop_reason};
    if(result.resource_budget===true)e.finiteTraceVariation={resource_budget:true};
    throw e;
   }
   const flows=[];
   for(let n=0;n<depth;n++){
    const row=result.completed[n];
    requireValue(row.stage===n,'R531 consumes every completed result in original stage order');
    const file=path.join(directory,row.file),b=fs.readFileSync(file);
    requireValue(b.length===row.bytes&&sha(b)===row.sha256,'R531 complete stage payload changed');
    const f=deserialize(b),c=cells[n];
    requireValue(f.state instanceof Float64Array&&f.state.length===K+2&&
     f.tangent instanceof Float64Array&&f.tangent.length===(K+2)*K,
     'R531 keeps full226 state and full226x224 tangent before original projection');
    // These are the exact original cellFlow projection expressions and order.
    const out=Float64Array.from(f.state.slice(0,K),(v,j)=>j<M?v:v/c.portRatio);
    const J=new Float64Array(K*K);
    for(let i=0;i<K;i++)for(let j=0;j<K;j++)J[i*K+j]=f.tangent[i*K+j]/(i<M?1:c.portRatio);
    flows.push({out,J,meanHeight:f.state[K]+f.state[K+1],minA:f.minA,minD:f.minD});
   }
   requireValue(binaryRowsHash(states)===input.actual_state_float64le_sha256&&
    binaryRowsHash([target])===input.actual_target_float64le_sha256&&
    binaryRowsHash([scales])===input.actual_scales_float64le_sha256,
    'R531 never mutates the actual native state/target/scales');
   current.phase='all576-original-flow-records-returned';
   writeJSON(path.join(directory,'parent-consumed.json'),{schema:PARALLEL_CELLFLOW_SCHEMA+'-parent-consumed',
    evaluation_sequence:id,input:keepRaw(inputFile,directory),result:keepRaw(path.join(directory,'result.json'),directory),
    original_n_order_complete:true,complete_stages:depth,full226x224_read_before_original_projection:true,
    original_two_mean_sum_retained:true,numerical_gate_added:false,
    noJ_evaluation_unchanged:true,output_finiteness_not_added:true});
   // No raw deletion here. The existing final necessary readback and actual
   // owned quiet/cleanup remain responsible for every temporary pool file.
   return flows;
  }catch(error){
   current.phase='parent-returned-error';current.error=plainError(error);
   current.prepared_stages=preparedStages.slice();
   current.actual_preparation_journal=keepRaw(preparationJournal,directory);
   try{writeJSON(path.join(directory,'parent-failure.json'),{
    schema:PARALLEL_CELLFLOW_SCHEMA+'-parent-failure',current,
    unprepared_stage_addresses:Array.from({length:depth},(_,n)=>n).filter(n=>!preparedStages.includes(n)),
    prior_profile_reads_are_preparation_not_completed_cellflows:true,
    error_is_not_promoted_to_an_original_mathematical_refusal:true});}catch(_){}
   throw error;
  }
 }
 function close(){
  if(closed)return snapshot();closed=true;
  if(childLive()){
   try{writeJSON(path.join(base,'control.json'),{schema:PARALLEL_CELLFLOW_SCHEMA+'-control',kind:'close'});}
   catch(e){try{process.kill(child.pid,'SIGTERM');}catch(_){}}
   const limit=mono()+5;
   while(childLive()&&mono()<limit)Atomics.wait(sleepWord,0,0,25);
   if(childLive()){try{process.kill(child.pid,'SIGKILL');}catch(e){if(e?.code!=='ESRCH')throw e;}}
   // A process in Z/X has no running JavaScript threads. Its parent can reap
   // it after this synchronous callback returns; that is not an observed exit.
   const forcedLimit=mono()+1;
   while(childLive()&&mono()<forcedLimit)Atomics.wait(sleepWord,0,0,25);
  }
  const actual=proc(child.pid);
  writeJSON(path.join(base,'parent-close.json'),{schema:PARALLEL_CELLFLOW_SCHEMA+'-parent-close',
   child_pid:child.pid,actual_process_after_close:actual,
   child_process_not_live:!actual||actual.state==='Z'||actual.state==='X',
   individual_worker_exit_events_only_if_present_in_original_pool_terminal:true,
   original_outer_owned_quiet_and_cleanup_still_required:true,
   close_wait_is_transport_only_not_restarted_science:true});
  return snapshot();
 }
 return {evaluate,snapshot,close,workerDirectory,schema:PARALLEL_CELLFLOW_SCHEMA};
}
