// R532: evaluate a binary64 Newton linear model at once-projected owner128 nodes.
// This library receives the real already-installed DN object. It creates no
// engine, profile, owner, solution or clock. Its future same-worker caller and
// the exact binary64-to-binary128 model lift are deliberately not registered.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {fileURLToPath} from 'node:url';

export const SCHEMA='R532-current-owner-projected64-complete-stage-model-v1';
const BINDING_SCHEMA='R532-current-H-owner128-once-projected-stage-binding-v1';
const BINDING_NAME='geometry_20261116_live128_projected_stage_binding.py';
const BINDING_SHA='fab3790936e6516bd39f445a2fc8384196cb1479405a10588f9007d821751cbf';
const SELF=fileURLToPath(import.meta.url),HERE=path.dirname(SELF);
const M=112,K=224,SIZE=226,DEPTH=576;
const RUN_KEYS=['GITHUB_REPOSITORY','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','GITHUB_SHA'];
const TUPLE_SCHEMA='R532-declared-current128-source-tuple-v1';
const SOURCE_ROLES=['owner','client','current_call','worker'];
const SCHEMA_ROLES=['owner_input','owner_summary','session','geometry','snapshot','snapshot_context','snapshot_manifest'];
const STORED_ENGINE_SHA='1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8';
const ORIGINAL_PINS={
 'scripts/78718-tail-tangent-core.mjs':'ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3',
 'scripts/78718-tail-fourier-product-flow.mjs':'717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f',
 'scripts/78718-tail-fourier-root-split-engine.mjs':'a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372',
 'scripts/78718-prefix-tail-tangent-fourier-worker.mjs':'36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a'
};

class BindingFailure extends Error {}
class NonfiniteModel extends Error {}
const require=(ok,message)=>{if(!ok)throw new BindingFailure(message);};
const sha=value=>crypto.createHash('sha256').update(value).digest('hex');
function fileSHA(file){
 const h=crypto.createHash('sha256'),fd=fs.openSync(file,'r'),buffer=Buffer.allocUnsafe(1<<20);
 try{for(;;){const n=fs.readSync(fd,buffer,0,buffer.length,null);if(!n)break;h.update(buffer.subarray(0,n));}}
 finally{fs.closeSync(fd);}
 return h.digest('hex');
}
function receipt(file){
 const absolute=fs.realpathSync(file);
 return {file:absolute,bytes:fs.statSync(absolute).size,sha256:fileSHA(absolute)};
}
function within(root,file){
 const p=path.resolve(file),r=path.resolve(root);
 require(p!==r&&p.startsWith(r+path.sep),'The actual file must remain in its recorded owner directory');
 return p;
}
function checked(desc,root=null){
 require(desc&&typeof desc.file==='string'&&path.isAbsolute(desc.file)&&
  Number.isSafeInteger(desc.bytes)&&desc.bytes>=0&&/^[0-9a-f]{64}$/.test(desc.sha256),
  'An actual absolute full-file bytes/SHA receipt is required');
 const p=path.resolve(desc.file);
 require(!fs.lstatSync(p).isSymbolicLink()&&fs.statSync(p).isFile(),'A retained nonsymlinked actual file is required');
 if(root!==null)within(root,fs.realpathSync(p));
 require(fs.statSync(p).size===desc.bytes&&fileSHA(p)===desc.sha256,'Complete actual file identity differs: '+p);
 return fs.realpathSync(p);
}
function read(desc,root=null){
 const file=checked(desc,root),raw=fs.readFileSync(file);
 const full=raw[0]===31&&raw[1]===139?zlib.gunzipSync(raw):raw;
 if(Object.hasOwn(desc,'raw_bytes'))require(full.length===desc.raw_bytes,'Decoded JSON byte count differs');
 if(Object.hasOwn(desc,'raw_sha256'))require(sha(full)===desc.raw_sha256,'Decoded JSON identity differs');
 return JSON.parse(full);
}
function stable(value){
 if(Array.isArray(value))return value.map(stable);
 if(value&&typeof value==='object')return Object.fromEntries(Object.keys(value).sort().map(k=>[k,stable(value[k])]));
 return value;
}
function equal(a,b,label){
 require(JSON.stringify(stable(a))===JSON.stringify(stable(b)),'Same actual current-call identity: '+label);
}
function samePayload(a,b,label){require(a.bytes===b.bytes&&a.sha256===b.sha256,label);}
function encode(value){
 return JSON.stringify(value,(_key,x)=>{
  if(typeof x==='number'&&!Number.isFinite(x))throw new BindingFailure('Use numberRecord for nonfinite diagnostics');
  return x;
 })+'\n';
}
function writeJSON(file,value){
 const raw=Buffer.from(encode(value));fs.writeFileSync(file,raw,{flag:'wx'});
 return {file:path.resolve(file),bytes:raw.length,sha256:sha(raw)};
}
function numberRecord(value){
 require(typeof value==='number','An actual numerical diagnostic must be a number');
 const raw=Buffer.allocUnsafe(8);raw.writeDoubleLE(value);
 return {value:Number.isFinite(value)?value:null,float64le_hex:raw.toString('hex'),
  classification:Number.isNaN(value)?'NaN':value===Infinity?'positive-infinity':
   value===-Infinity?'negative-infinity':Object.is(value,-0)?'negative-zero':'finite'};
}
function rawView(row){
 require(row instanceof Float64Array,'The original Float64Array return type is required');
 return Buffer.from(row.buffer,row.byteOffset,row.byteLength);
}
function binaryRowsHash(rows){
 const h=crypto.createHash('sha256');
 for(const row of rows){
  if(row instanceof Float64Array)h.update(rawView(row));
  else{const raw=Buffer.allocUnsafe(8*row.length);for(let j=0;j<row.length;j++)raw.writeDoubleLE(row[j],8*j);h.update(raw);}
 }
 return h.digest('hex');
}
function finiteArray(row,shape,label){
 const count=shape.reduce((a,b)=>a*b,1);
 require(row instanceof Float64Array&&row.length===count,'Complete actual array dimensions: '+label);
 for(let i=0;i<row.length;i++)if(!Number.isFinite(row[i])){
  const error=new NonfiniteModel('The projected64 model has an actual nonfinite array entry');
  error.location={array:label,index:i,shape,actual:numberRecord(row[i])};throw error;
 }
}
function loadArray(desc,shape,root){
 equal(desc.shape,shape,'complete input array dimensions');
 require(desc.dtype==='<f8'&&desc.order==='C','Original binary64 little-endian row-major array');
 const raw=fs.readFileSync(checked(desc,root));
 require(raw.length===8*shape.reduce((a,b)=>a*b,1),'Complete input words');
 const row=new Float64Array(raw.length/8);
 for(let j=0;j<row.length;j++)row[j]=raw.readDoubleLE(8*j);
 finiteArray(row,shape,'input:'+path.basename(desc.file));
 return row;
}
function cleanError(error){
 return {type:error?.name??'Error',message:String(error?.message??error),
  location:error?.location??null,
  stack:String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<original-retained-data-url-module>')};
}
function liveIdentity(dn,ioKeys){
 const mathematical=Object.fromEntries(Object.entries(dn.tail.parameters).filter(([key])=>!ioKeys.includes(key)));
 return {parameters:mathematical,rawNode:Array.from(dn.tail.rawNode),
  graphs_float64le_sha256:binaryRowsHash(dn.tail.graphs),
  gains_float64le_sha256:binaryRowsHash(dn.tail.gains),
  far_graph_float64le_sha256:binaryRowsHash([dn.tail.graphs.at(-1)]),
  initial_function_sha256:sha(dn.tail.initial.toString()),
  evaluate_function_sha256:sha(dn.tail.evaluate.toString()),
  tail_solve_function_sha256:sha(dn.tail.solve.toString()),
  dn_solve_function_sha256:sha(dn.solve.toString()),
  stages:dn.tail.cells.map(c=>({rawCell:c.rawCell,rawSegment:c.rawSegment,portRatio:c.portRatio,mu:c.mu,
   profiles:c.profiles.map(p=>Array.from(p.integrationBreakpoints??[]))}))};
}
function captureReferences(dn){
 return {dn,tail:dn.tail,cells:dn.tail.cells,graphs:dn.tail.graphs,gains:dn.tail.gains,
  rawNode:dn.tail.rawNode,parameters:dn.tail.parameters,initial:dn.tail.initial,
  evaluate:dn.tail.evaluate,tailSolve:dn.tail.solve,dnSolve:dn.solve,
  stages:dn.tail.cells.map(c=>({cell:c,engine:c.engine,flow:c.engine.flowStateWithJacobian,
   profiles:c.profiles,profileFunctions:Array.from(c.profiles),
   flow_source_sha256:sha(c.engine.flowStateWithJacobian.toString()),
   profile_source_sha256:c.profiles.map(p=>sha(p.toString()))}))};
}
function assertReferences(dn,refs){
 require(dn===refs.dn&&dn.tail===refs.tail&&dn.tail.cells===refs.cells&&
  dn.tail.graphs===refs.graphs&&dn.tail.gains===refs.gains&&dn.tail.rawNode===refs.rawNode&&
  dn.tail.parameters===refs.parameters&&dn.tail.initial===refs.initial&&
  dn.tail.evaluate===refs.evaluate&&dn.tail.solve===refs.tailSolve&&dn.solve===refs.dnSolve,
  'The same already-loaded DN object and original functions must remain installed');
 require(dn.tail.cells.length===DEPTH,'All actual576 cells remain present');
 for(let n=0;n<DEPTH;n++){
  const c=dn.tail.cells[n],r=refs.stages[n];
  require(c===r.cell&&c.engine===r.engine&&c.engine.flowStateWithJacobian===r.flow&&
   c.profiles===r.profiles&&c.profiles.length===r.profileFunctions.length&&
   c.profiles.every((p,i)=>p===r.profileFunctions[i]),
   'The actual cell/engine/profile objects changed at stage '+n);
 }
}
function bindCurrentSources(registration){
 require(registration?.schema===TUPLE_SCHEMA,'Explicit actual current128 source registration');
 equal(Object.keys(registration.sources).sort(),[...SOURCE_ROLES].sort(),'all four current producer roles');
 equal(Object.keys(registration.schemas).sort(),[...SCHEMA_ROLES].sort(),'all seven current producer schemas');
 const actual={};
 for(const [role,desc] of Object.entries(registration.sources)){
  require(typeof desc.file==='string'&&path.basename(desc.file)===desc.file,
   'Each explicitly registered current source is a basename');
  const file=path.join(HERE,desc.file);
  require(!fs.lstatSync(file).isSymbolicLink()&&fs.statSync(file).isFile(),'Actual current source: '+role);
  actual[role]=receipt(file);samePayload(actual[role],desc,'Full registered source identity: '+role);
 }
 require(Object.values(registration.schemas).every(x=>typeof x==='string'&&x.length>0),
  'Explicit actual current schema strings');
 return actual;
}
function checkedClock(desc,runner){
 const file=checked(desc,runner),raw=fs.readFileSync(file,'utf8'),clock=JSON.parse(raw);
 require(clock.schema==='R493-original-full112-live128-job-deadline-v1'&&clock.total_seconds===19200&&
  Number.isInteger(clock.readback_cleanup_reserve_seconds)&&clock.readback_cleanup_reserve_seconds>=60&&
  clock.readback_cleanup_reserve_seconds<=600,'One original full112 clock and original reserve');
 for(const key of RUN_KEYS)require(clock.run[key]===process.env[key],'Actual original run clock: '+key);
 const matches=[...raw.matchAll(/"absolute_monotonic_deadline_ns"\s*:\s*([0-9]+)/g)];
 require(matches.length===1,'The original integral deadline word is retained exactly');
 const until=BigInt(matches[0][1])-BigInt(clock.readback_cleanup_reserve_seconds)*1000000000n;
 return {clock,scientific_deadline_monotonic_ns_text:until.toString()};
}
function makeWriter(file,width,requestedShape){
 const fd=fs.openSync(file,'wx'),digest=crypto.createHash('sha256');let bytes=0,closed=false;
 return {
  append(row){
   require(row instanceof Float64Array&&row.length===width,'One complete actual output row');
   const raw=rawView(row);let offset=0;
   while(offset<raw.length){const n=fs.writeSync(fd,raw,offset,raw.length-offset,null);
    require(n>0,'A temporary output write made no progress');
    digest.update(raw.subarray(offset,offset+n));offset+=n;bytes+=n;}
   return {bytes:raw.length,sha256:sha(raw)};
  },
  finish(){
   if(!closed){fs.closeSync(fd);closed=true;}
   return {file:path.resolve(file),bytes,sha256:digest.digest('hex'),requested_shape:requestedShape,
    complete_rows:Math.floor(bytes/(width*8)),trailing_bytes:bytes%(width*8),dtype:'<f8',order:'C'};
  }
 };
}
function makeLedger(file){
 const fd=fs.openSync(file,'wx'),digest=crypto.createHash('sha256');let bytes=0,rows=0,closed=false;
 return {
  append(value){
   const raw=Buffer.from(encode(value));let at=0;
   while(at<raw.length){const n=fs.writeSync(fd,raw,at,raw.length-at,null);require(n>0,'Stage ledger write made no progress');
    digest.update(raw.subarray(at,at+n));at+=n;bytes+=n;}rows++;
  },
  finish(){
   if(!closed){fs.closeSync(fd);closed=true;}
   return {file:path.resolve(file),bytes,sha256:digest.digest('hex'),complete_rows:rows,
    encoding:'ordered-original-stage-json-lines',body_returned_in_necessary_summary:false};
  }
 };
}

/**
 * Bind the exact already-installed DN while it is still in the original worker.
 *
 * sessionSpecification is a real absolute file/bytes/SHA receipt. currentSourceTuple
 * is the caller's explicit four-source/seven-schema registration, equal to the
 * Python binding input; hashes alone do not prove a new producer's semantics.
 * originalDeadline is the same receipt carried by that session and the binding.
 * checkResource is the original caller's synchronous or async deadline callback:
 * it MUST check that receipt's absolute science deadline and throw when exhausted.
 * The library calls it before/between full cells. A synchronous native cell
 * cannot be interrupted here; the actual owned caller must additionally enforce
 * its existing process deadline. That caller is not registered by this file.
 */
export function createLive128ProjectedStageLibrary(dn,{
 sessionSpecification,originalDeadline,currentSourceTuple,checkResource
}={}){
 require(process.env.GITHUB_ACTIONS==='true'&&
  (process.env.GITHUB_REPOSITORY??'').toLowerCase()==='rogerhu12/math-research-public',
  'Scientific source calls belong only to this public repository Actions');
 require(Buffer.from(new Float64Array([1]).buffer).toString('hex')==='000000000000f03f',
  'The original little-endian binary64 runtime is required');
 require(typeof checkResource==='function','An original-clock deadline callback is mandatory');
 const currentSources=bindCurrentSources(currentSourceTuple),schemas=currentSourceTuple.schemas;
 const runner=fs.realpathSync(process.env.RUNNER_TEMP),session=read(sessionSpecification,runner);
 require(session.schema===schemas.session&&session.source_sha256===currentSources.client.sha256&&
  session.hook_sha256===currentSources.current_call.sha256,'The actual registered live worker session');
 const sessionRoot=fs.realpathSync(session.output);within(runner,sessionRoot);
 samePayload(session.job_deadline,originalDeadline,'Same original caller deadline');
 const clock=checkedClock(originalDeadline,runner);
 require(fileSHA(path.join(HERE,BINDING_NAME))===BINDING_SHA,'The actual R532 projection binding source');
 require(fileSHA(path.join(HERE,'tail_resumable_engine.mjs'))===STORED_ENGINE_SHA&&
  session.frozen_sources['tail_resumable_engine.mjs']===STORED_ENGINE_SHA,
  'The unchanged original stored DN engine');
 for(const [role,desc] of Object.entries(currentSourceTuple.sources))
  require(session.frozen_sources[desc.file]===desc.sha256,'The actual session carries its registered source: '+role);
 const originalSources={};
 for(const [relative,digest] of Object.entries(ORIGINAL_PINS)){
  const file=path.join(session.original_source_topic,relative);
  require(fileSHA(file)===digest&&
   session.original_source_sha256['topics/visible-flexible-closed-surface/'+relative]===digest,
   'The original installed finite flow source: '+relative);
  originalSources[relative]=receipt(file);
 }
 require(dn?.tail?.cells?.length===DEPTH&&dn.tail.parameters.depth===DEPTH&&
  dn.tail.parameters.modes===M&&dn.tail.parameters.quadrature===2048&&
  dn.tail.parameters.spacing===2&&Number.isInteger(dn.tail.parameters.steps)&&dn.tail.parameters.steps>0,
  'The real original complete112/576/N2048 object is required');
 require(typeof dn.tail.evaluate==='function'&&typeof dn.tail.initial==='function'&&
  typeof dn.tail.solve==='function'&&typeof dn.solve==='function',
  'The actual original DN functions are still present');
 const refs=captureReferences(dn),initialIdentity=liveIdentity(dn,session.io_keys);
 const originalGeometry=receipt(path.join(sessionRoot,'actual-live-geometry-and-initial-guess.json'));
 const geometry=read(originalGeometry,sessionRoot);
 require(geometry.schema===schemas.geometry,
  'The real original worker geometry record');
 equal(initialIdentity,geometry.actual_live_identity,'actual already-loaded finite geometry');
 equal(geometry.session_origin,session.session_origin,'same original session');
 let busy=false;
 return {
  describe(){
   return {schema:SCHEMA+'-library-v1',source:receipt(SELF),projection_binding_source:receipt(path.join(HERE,BINDING_NAME)),
    actual_session_spec:sessionSpecification,actual_job_deadline:originalDeadline,
    actual_current_source_tuple:currentSourceTuple,actual_current_sources:currentSources,
    scientific_deadline_monotonic_ns_text:clock.scientific_deadline_monotonic_ns_text,
    actual_live_geometry_record:originalGeometry,original_sources:originalSources,
    all576_cells:true,local_rows:SIZE,shape_columns:K,
    model:'current-owner-once-projected64-full-stage-linear-model',
    native_or_fullDN_acceptance_claimed:false,original_owned_caller_registered:false,
    exact_model_lift_to128_registered:false};
  },
  async produce({bindingResult,out}){
   require(!busy,'One real same-DN model operation at a time');busy=true;
   let directory=null,record=null,ledger=null;const writers={};
   const started=process.hrtime.bigint();let phase='binding',nextStage=0;
   const clockCheck=async()=>{
    phase='original-clock-callback';
    await checkResource({actual_job_deadline:originalDeadline,
     scientific_deadline_monotonic_ns_text:clock.scientific_deadline_monotonic_ns_text,
     stage:nextStage,complete_stages:record?.completed_stages??0});
    phase='model';
   };
   try{
    const bindingPath=checked(bindingResult,sessionRoot),binding=read(bindingResult,sessionRoot);
    require(binding.schema===BINDING_SCHEMA&&binding.complete===true&&
     binding.projection_completed===true&&binding.actual_current_H_binding_complete===true&&
     binding.source.sha256===BINDING_SHA&&binding.owner_binary128_residual_remains_authoritative===true&&
     binding.original_owner_state_modified===false&&binding.binary64_projected_point_accepted_as_solution===false,
     'One complete actual R532 owner128 binding/projection is required');
    equal(binding.actual_current_source_tuple,currentSourceTuple,'same explicitly registered current producer tuple');
    samePayload(binding.actual_session_spec,sessionSpecification,'Same actual live worker specification');
    samePayload(binding.actual_job_deadline,originalDeadline,'One original absolute deadline');
    require(binding.scientific_deadline_monotonic_ns_text===clock.scientific_deadline_monotonic_ns_text,
     'The exact original deadline word and reserve are unchanged');
    for(const key of RUN_KEYS)require(binding.run[key]===process.env[key],'Actual current run/source: '+key);
    const callRoot=fs.realpathSync(binding.actual_call_directory);
    require(path.dirname(callRoot)===sessionRoot,'The actual current call belongs to this worker');
    within(callRoot,bindingPath);
    const currentGeometry=read(binding.actual_live_geometry_record,sessionRoot);
    samePayload(binding.actual_live_geometry_record,originalGeometry,'The actual original already-loaded object record');
    equal(currentGeometry.actual_live_identity,initialIdentity,'same original geometry object record');
    equal(binding.parameters,initialIdentity.parameters,'actual full finite parameters');
    equal(binding.raw_node,initialIdentity.rawNode,'actual576-stage raw mesh');
    require(binding.actual_call_identity?.source_sha256===session.source_sha256&&
     binding.actual_call_identity?.hook_sha256===session.hook_sha256&&
     binding.actual_call_identity?.original_cuspAwareFlow===true,
     'The complete original current-H/cusp call identity');
    checked(binding.actual_final_state128,callRoot);
    checked(binding.actual_owner_summary,callRoot);
    const context=read(binding.actual_snapshot_context,callRoot);
    const manifest=read(binding.actual_snapshot_manifest,callRoot);
    equal(context.raw_array_sha256,binding.actual_call_identity.complete_current_array_sha256,
     'All actual current array identities remain bound');
    require(manifest.schema===schemas.snapshot_manifest,
     'The complete original current-array manifest remains present');
    const nodeWords=loadArray(binding.actual_projected_state64,[DEPTH+1,K],callRoot);
    require(binding.projection.complete===true&&binding.projection.completed_words===(DEPTH+1)*K&&
     binding.projection.expected_words===(DEPTH+1)*K&&binding.projection.first_unprojected_index===null&&
     binding.actual_projected_state64.sha256===binding.projection.projected_binary64le_sha256,
     'Every original128 node word underwent one complete explicit RN64 projection');
    const states=Array.from({length:DEPTH+1},(_,n)=>nodeWords.subarray(n*K,(n+1)*K));
    const arrays=binding.actual_current_arrays;
    const height=loadArray(arrays['physical-height'],[1,M],callRoot);
    const scales=loadArray(arrays['original-scales'],[1,DEPTH+1],callRoot);
    const target=loadArray(arrays['cut-target'],[1,M],callRoot);
    const far=loadArray(arrays['original-far-graph'],[1,M],callRoot);
    require(binaryRowsHash([height])===binding.actual_call_identity.complete_current_array_sha256['physical-height']&&
     binaryRowsHash([far])===initialIdentity.far_graph_float64le_sha256,
     'The full original physical-H and far graph words are unchanged');
    assertReferences(dn,refs);equal(liveIdentity(dn,session.io_keys),initialIdentity,'same live object before model');
    directory=path.resolve(out);within(callRoot,directory);require(!fs.existsSync(directory),'A fresh same-call stage-model output');
    fs.mkdirSync(directory,{recursive:false});
    record={schema:SCHEMA,source:receipt(SELF),projection_binding:bindingResult,
     projection_binding_source:receipt(path.join(HERE,BINDING_NAME)),
     run:Object.fromEntries(RUN_KEYS.map(k=>[k,process.env[k]??null])),
     actual_call_directory:callRoot,actual_call_identity:binding.actual_call_identity,
     actual_session_spec:sessionSpecification,actual_job_deadline:originalDeadline,
     actual_current_source_tuple:currentSourceTuple,actual_current_sources:currentSources,
     caller_registration_semantics_not_proved_by_hashes_alone:true,
     scientific_deadline_monotonic_ns_text:clock.scientific_deadline_monotonic_ns_text,
     actual_live_geometry_record:originalGeometry,actual_final_state128:binding.actual_final_state128,
     actual_owner_summary:binding.actual_owner_summary,actual_projected_state64:binding.actual_projected_state64,
     actual_current_arrays:arrays,original_request_flags:binding.original_request_flags,
     original_sources:originalSources,parameters:binding.parameters,
     model:'current-owner-once-projected64-full-stage-linear-model',
     mathematical_engine_or_profiles_recreated:false,
     original_flowStateWithJacobian_invocations:0,requested_stages:DEPTH,completed_stages:0,
     before_port_shape:[DEPTH,SIZE,K],after_port_shape:[DEPTH,K,K],mean_shape:[DEPTH,2,K],
     projection_performed_again_here:false,finite_difference_columns_used:false,
     original_two_mean_inputs_are_zero:true,mean_input_columns_added:false,
     actual_128_owner_state_modified:false,owner128_value_and_replay_remain_authoritative:true,
     binary64_projected_state_accepted:false,binary64_model_claimed_equal_to128_derivative:false,
     original_128_boundary_endpoint_fresh_audit_still_required:true,
     exact_model_lift_to128_registered:false,original_owned_caller_registered:false,
     original_clock_callback_source_sha256:sha(checkResource.toString()),
     callback_checks_required_before_and_between_full_cells:true,
     synchronous_cell_hard_interrupt_requires_original_owned_caller:true,
     stage_success_ledger_body_returned:false,all_raw_retained:true,
     complete:false,resource_partial:false,error:null,current_stage:null,unvisited_stage_addresses:[]};
    await clockCheck();
    for(const [key,width,shape] of [
     ['before-port-jacobians',SIZE*K,[DEPTH,SIZE,K]],
     ['after-port-jacobians',K*K,[DEPTH,K,K]],
     ['mean-jacobians',2*K,[DEPTH,2,K]],
     ['before-port-primal',SIZE,[DEPTH,SIZE]],
     ['after-port-primal',K,[DEPTH,K]],
     ['shooting-residuals',K,[DEPTH,K]]]){
      writers[key]=makeWriter(path.join(directory,key+'.f64le'),width,shape);
    }
    ledger=makeLedger(path.join(directory,'all-stage-return-records.jsonl'));
    let norm=0,minA=Infinity,minD=Infinity,meanHeight=0;
    for(let n=0;n<DEPTH;n++){
     nextStage=n;
     const c=dn.tail.cells[n];
     record.current_stage={stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,
      projected_input_node:n+1,all_shape_column_indices:[0,K],
      local_mean_input_words:['0000000000000000','0000000000000000'],
      original_engine_returned:false,all_outputs_committed:false};
     await clockCheck();assertReferences(dn,refs);
     const initial=new Float64Array(SIZE);initial.set(states[n+1]);
     // This is exactly the original cellFlow's withJac engine invocation.
     record.original_flowStateWithJacobian_invocations++;
     const f=c.engine.flowStateWithJacobian(initial,c.profiles,
      {stepsPerSegment:dn.tail.parameters.steps});
     record.current_stage.original_engine_returned=true;
     record.current_stage.actual_return_dimensions={};
     if(f&&Object.hasOwn(f,'state'))record.current_stage.actual_return_dimensions.state_length=f.state?.length??null;
     if(f&&Object.hasOwn(f,'tangent'))record.current_stage.actual_return_dimensions.tangent_length=f.tangent?.length??null;
     if(f&&Object.hasOwn(f,'shapeDimension'))record.current_stage.actual_return_dimensions.shape_dimension=f.shapeDimension;
     require(f&&f.state instanceof Float64Array&&f.state.length===SIZE&&
      f.tangent instanceof Float64Array&&f.tangent.length===SIZE*K,
      'Every226 local output and all224 original shape columns must return');
     if(Object.hasOwn(f,'shapeDimension'))require(f.shapeDimension===K,'Actual returned shapeDimension');
     const rows={};
     // Retain the actual full returns before diagnosing nonfinite model words.
     rows['before-port-primal']=writers['before-port-primal'].append(f.state);
     rows['before-port-jacobians']=writers['before-port-jacobians'].append(f.tangent);
     finiteArray(f.state,[SIZE],'before-port-primal');
     finiteArray(f.tangent,[SIZE,K],'before-port-jacobians');
     const after=Float64Array.from(f.state.slice(0,K),(v,j)=>j<M?v:v/c.portRatio);
     const jac=new Float64Array(K*K);
     for(let i=0;i<K;i++)for(let j=0;j<K;j++)
      jac[i*K+j]=f.tangent[i*K+j]/(i<M?1:c.portRatio);
     const means=f.tangent.slice(K*K,SIZE*K);
     const residual=Float64Array.from(after,(v,j)=>v-states[n][j]);
     rows['after-port-primal']=writers['after-port-primal'].append(after);
     rows['after-port-jacobians']=writers['after-port-jacobians'].append(jac);
     rows['mean-jacobians']=writers['mean-jacobians'].append(means);
     rows['shooting-residuals']=writers['shooting-residuals'].append(residual);
     finiteArray(after,[K],'after-port-primal');finiteArray(jac,[K,K],'after-port-jacobians');
     finiteArray(means,[2,K],'mean-jacobians');finiteArray(residual,[K],'shooting-residuals');
     const stageNorm=Math.max(...Array.from(residual,v=>Math.abs(v)/scales[n]));
     norm=Math.max(norm,stageNorm);
     minA=Math.min(minA,f.minA);minD=Math.min(minD,f.minD);
     const localMean=f.state[K]+f.state[K+1];meanHeight+=localMean;
     const diagnostics={normalized_stage_residual:numberRecord(stageNorm),
      first_mean:numberRecord(f.state[K]),second_mean:numberRecord(f.state[K+1]),
      mean_height_sum:numberRecord(localMean)};
     for(const key of ['minA','minD','maxRootRelative'])
      if(Object.hasOwn(f,key))diagnostics[key]=numberRecord(f[key]);
     const row={stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,
      projected_input_node:n+1,projected_input_words_sha256:sha(rawView(states[n+1])),
      local_mean_input_words:['0000000000000000','0000000000000000'],
      portRatio:numberRecord(c.portRatio),steps_per_segment:dn.tail.parameters.steps,
      engine_flow_source_sha256:refs.stages[n].flow_source_sha256,
      profile_source_sha256:refs.stages[n].profile_source_sha256,
      actual_complete_rows:rows,diagnostics,all_shape_columns:K,both_mean_rows:true};
     ledger.append(row);
     record.completed_stages=n+1;record.current_stage.all_outputs_committed=true;
     record.last_completed_stage={stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment};
     nextStage=n+1;
     await clockCheck();
    }
    const end=new Float64Array(M),cut=new Float64Array(M);
    for(let j=0;j<M;j++){
     end[j]=states[DEPTH][M+j]-far[j]*states[DEPTH][j];
     norm=Math.max(norm,Math.abs(end[j])/scales[DEPTH]);
    }
    for(let j=0;j<M;j++){
     cut[j]=states[0][j]-target[j];norm=Math.max(norm,Math.abs(cut[j])/scales[0]);
    }
    const boundaryRows={};
    for(const [name,row] of [['projected-point-end-residual',end],['projected-point-cut-residual',cut]]){
     const file=path.join(directory,name+'.f64le');fs.writeFileSync(file,rawView(row),{flag:'wx'});
     boundaryRows[name]={...receipt(file),shape:[M],dtype:'<f8',order:'C'};
    }
    record.projected_point_primal_diagnostics={original_normalized_residual:numberRecord(norm),
     minA:numberRecord(minA),minD:numberRecord(minD),mean_height_sum:numberRecord(meanHeight),
     boundary_rows:boundaryRows,owner_tolerance_test_not_applied_here:true,
     these_values_are_not_substituted_for_owner128_residual_or_replay:true};
    assertReferences(dn,refs);equal(liveIdentity(dn,session.io_keys),initialIdentity,'same geometry after complete model');
    checked(binding.actual_final_state128,callRoot);
    checked(binding.actual_projected_state64,callRoot);
    await clockCheck();
    record.complete=true;record.current_stage=null;
   }catch(error){
    if(record){
     record.resource_partial=phase==='original-clock-callback';
     record.original_clock_callback_threw=phase==='original-clock-callback';
     if(record.original_clock_callback_threw)
      record.resource_partial_scope='Required original-clock callback did not return; its actual error is preserved, not diagnosed as an independent timeout';
     record.error={...cleanError(error),phase};
    }else{throw error;}
   }finally{
    for(const [key,writer] of Object.entries(writers)){
     try{const item=writer.finish();if(record)(record.actual_output_arrays??={})[key]=item;}
     catch(error){if(record){record.complete=false;(record.output_finalization_errors??=[]).push(cleanError(error));}}
    }
    if(ledger){
     try{record.complete_stage_ledger=ledger.finish();}
     catch(error){record.complete=false;(record.output_finalization_errors??=[]).push(cleanError(error));}
    }
    busy=false;
   }
   record.unvisited_stage_addresses=Array.from({length:DEPTH-record.completed_stages},(_,i)=>{
    const n=record.completed_stages+i,c=initialIdentity.stages[n];
    return {stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment};
   });
   record.current_partial_stage_remains_in_unvisited_suffix=record.completed_stages<DEPTH;
   record.full_stage_shapes_complete=record.complete&&record.completed_stages===DEPTH&&
    Object.keys(record.actual_output_arrays??{}).length===6&&
    Object.values(record.actual_output_arrays??{}).every(x=>x.complete_rows===DEPTH&&x.trailing_bytes===0);
   if(!record.full_stage_shapes_complete)record.complete=false;
   record.elapsed_seconds=Number(process.hrtime.bigint()-started)/1e9;
   const resultFile=writeJSON(path.join(directory,'result.json'),record);
   const raw=Buffer.from(encode(record)),necessaryExit=raw.length>90000?70:record.complete?0:2;
   let necessary=null;
   if(raw.length<=90000){
    const filename=path.join(directory,'necessary-summary.json');fs.writeFileSync(filename,raw,{flag:'wx'});
    necessary={file:filename,bytes:raw.length,sha256:sha(raw)};
   }
   const delivery={schema:SCHEMA+'-delivery-v1',result:resultFile,complete:record.complete,
    necessary_exit_code:necessaryExit,necessary_summary:necessary,
    attempted_necessary_bytes:raw.length,attempted_necessary_sha256:sha(raw),
    no_split_no_encoding_of_large_raw:true,all_raw_retained:true,cleanup_authorized:false,
    current_worker_stdout_protocol_untouched:true};
   writeJSON(path.join(directory,'delivery.json'),delivery);
   return {result:record,delivery};
  }
 };
}
