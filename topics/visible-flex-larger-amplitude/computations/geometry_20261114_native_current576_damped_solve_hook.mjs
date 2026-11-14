// Continue the actual59 selected full state through the original native loop.
// Only the nonlinear correction call is redirected to a synchronous current
// with-J snapshot / R273 bridge. Original evaluate, ten trials, all guards,
// tolerances, iteration limit and final endpoint J/audit remain unchanged.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {fileURLToPath} from 'node:url';
import {registerHooks} from 'node:module';
import {spawnSync} from 'node:child_process';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('Current native576 execution belongs only to this public repository Actions');
const specPath=process.env.VISIBLE_FLEX_NATIVE_CURRENT576_DAMPED_SOLVE_SPEC;
if(!specPath)throw Error('An explicit selected59/current576 specification is required');
const selfPath=fileURLToPath(import.meta.url),here=path.dirname(selfPath);
const sha=value=>crypto.createHash('sha256').update(value).digest('hex');
const fileSHA=file=>sha(fs.readFileSync(file));
const unpack=raw=>raw[0]===31&&raw[1]===139?zlib.gunzipSync(raw):raw;
const specRaw=fs.readFileSync(specPath),spec=JSON.parse(unpack(specRaw)),specSHA=sha(specRaw);
const KEY='visible-flex.native-current576-damped-solve.v1';
const frozenPath=path.join(here,'tail_frozen_worker.mjs');
const enginePath=path.join(here,'tail_resumable_engine.mjs');
const frozenSHA='3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054';
const engineSHA='1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8';
const coreSHA='ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3';
const runtimeSHA='f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f';
const evaluateSHA='9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9';
const internalSolveSHA='d7d063fe2fca25c1742c68ec8056902a583952b61cdda98e1d9eaab7c09f3615';
const trialSHA='603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99';
const selectedSHA='384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03';
const heightSHA='c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f';
const scaleSHA='ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc';
const farSHA='395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54';
const targetSHA='e2ea4563e7afc7d993db2ebc29ef63a1d853355c9d1ceeaf10f296b84391a14d';
if(spec.schema!=='native-current576-damped-solve-spec-v1'||spec.hook_sha256!==fileSHA(selfPath)||
   spec.selected_state_float64le_sha256!==selectedSHA||spec.exact_height_float64le_sha256!==heightSHA||
   spec.original_scales_float64le_sha256!==scaleSHA||spec.original_far_graph_float64le_sha256!==farSHA||
   spec.original_cut_target_float64le_sha256!==targetSHA||spec.original_runtime_core_sha256!==runtimeSHA)
 throw Error('The actual selected59 or current bridge specification changed');
for(const [name,digest] of Object.entries(spec.frozen_sources)){
 if(path.basename(name)!==name||fileSHA(path.join(here,name))!==digest)
  throw Error('Frozen original or current correction source changed: '+name);
}
// Native raw arrays are copied as bytes, not reformatted through JSON.
if(Buffer.from(new Float64Array([1]).buffer).toString('hex')!=='000000000000f03f')
 throw Error('The declared original little-endian binary64 array layout is unavailable');

function stable(value){
 if(Array.isArray(value))return value.map(stable);
 if(value&&typeof value==='object')return Object.fromEntries(Object.keys(value).sort().map(k=>[k,stable(value[k])]));
 return value;
}
function equal(a,b,label){if(JSON.stringify(stable(a))!==JSON.stringify(stable(b)))throw Error('Current native identity differs: '+label);}
function mathematical(value){return Object.fromEntries(Object.entries(value).filter(([key])=>!spec.io_keys.includes(key)));}
function numericalSources(value){return Object.fromEntries(Object.entries(value).filter(([key])=>!['input_config','runtime_config'].includes(key)));}
function encode(value){return JSON.stringify(value,(_key,x)=>{
 if(typeof x==='number'&&!Number.isFinite(x))throw Error('Use an explicit numberRecord for nonfinite metadata');
 return x;
})+'\n';}
function numberRecord(value){
 const raw=Buffer.allocUnsafe(8);raw.writeDoubleLE(value);
 return {value:Number.isFinite(value)?value:null,float64le_hex:raw.toString('hex'),
  classification:Number.isNaN(value)?'NaN':value===Infinity?'positive-infinity':value===-Infinity?'negative-infinity':
   Object.is(value,-0)?'negative-zero':'finite'};
}
function safeWithin(directory,file){
 if(typeof file!=='string'||!file||path.isAbsolute(file))throw Error('A relative complete evidence path is required');
 const result=path.resolve(directory,file),base=path.resolve(directory);
 if(result===base||!result.startsWith(base+path.sep))throw Error('Escaping complete evidence path');
 if(fs.lstatSync(result).isSymbolicLink()||!fs.statSync(result).isFile())throw Error('A regular evidence file is required');
 return result;
}
function receipt(file,base=path.dirname(file)){
 return {file:path.relative(base,file),bytes:fs.statSync(file).size,sha256:fileSHA(file)};
}
function readVerified(descriptor,directory=null){
 const file=directory===null?descriptor.path:safeWithin(directory,descriptor.file),raw=fs.readFileSync(file);
 if(sha(raw)!==descriptor.sha256||raw.length!==descriptor.bytes)throw Error('Changed complete evidence: '+file);
 const full=unpack(raw);
 if(descriptor.raw_sha256&&sha(full)!==descriptor.raw_sha256)throw Error('Changed uncompressed evidence: '+file);
 if(descriptor.raw_bytes!==undefined&&full.length!==descriptor.raw_bytes)throw Error('Changed uncompressed byte count: '+file);
 return JSON.parse(full);
}
function writeJSON(directory,file,value,{compressed=false}={}){
 const full=Buffer.from(encode(value)),raw=compressed?zlib.gzipSync(full,{level:9,mtime:0}):full;
 if(raw.length>=4_900_000)throw Error('Large complete metadata must be packeted, never truncated');
 const filename=path.join(directory,file);fs.writeFileSync(filename,raw,{flag:'wx'});
 const row={file,bytes:raw.length,sha256:sha(raw)};
 if(compressed)Object.assign(row,{raw_bytes:full.length,raw_sha256:sha(full),encoding:'json-gzip'});
 return row;
}
function rawView(row){
 if(!(row instanceof Float64Array))throw Error('Retain the original Float64Array instance bytes');
 return Buffer.from(row.buffer,row.byteOffset,row.byteLength);
}
function binaryRowsHash(rows){
 const h=crypto.createHash('sha256');
 for(const row of rows){
  if(row instanceof Float64Array)h.update(rawView(row));
  else {const raw=Buffer.allocUnsafe(8*row.length);for(let j=0;j<row.length;j++)raw.writeDoubleLE(row[j],8*j);h.update(raw);}
 }
 return h.digest('hex');
}
function cleanError(error){return {name:error?.name??'Error',message:String(error),
 stack:String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<retained-original-data-url-module>')};}
function methodIdentity(dn){
 const coreFile=path.join(spec.output,'core-instrumentation.json'),coreRaw=fs.readFileSync(coreFile),core=JSON.parse(coreRaw);
 if(core.spec_sha256!==specSHA||core.hook_sha256!==fileSHA(selfPath)||
    core.original_core_file_sha256!==coreSHA||core.original_runtime_core_sha256!==runtimeSHA||
    core.exact_correction_call_roundtrip_verified!==true||core.original_ten_trial_body_byte_identical!==true)
  throw Error('Only the declared original nonlinear correction call may be replaced');
 const inside=core.internal_solve_source_identity;
 if(sha(inside.original_internal_solve_source)!==internalSolveSHA||
    sha(inside.instrumented_internal_solve_source)!==inside.instrumented_internal_solve_source_sha256||
    inside.instrumented_internal_solve_source.replace(inside.replacement.after,inside.replacement.before)!==inside.original_internal_solve_source)
  throw Error('The actual internal solve source is not exactly reversible');
 const actualEvaluate=dn.tail.evaluate.toString(),publicSolve=dn.tail.solve.toString(),fullSolve=dn.solve.toString();
 equal(sha(actualEvaluate),evaluateSHA,'unchanged original actual public evaluate');
 equal(sha(publicSolve),'283de19115a958e0268f6a719e17c53aa9c0a5473692d8a22aa09bf28b81378a','unchanged original public split solve');
 equal(sha(fullSolve),'f80eaeff1cd31347ddfa9132fa42ff7b330297dc9fd37383b8727fb48ea46b8e','unchanged full DN/final Jacobian wrapper');
 return {schema:'current576-actual-public-and-internal-source-identities-v1',
  actual_public_evaluate_source:actualEvaluate,actual_public_evaluate_sha256:sha(actualEvaluate),
  actual_public_tail_solve_source:publicSolve,actual_public_tail_solve_sha256:sha(publicSolve),
  actual_public_dn_solve_source:fullSolve,actual_public_dn_solve_sha256:sha(fullSolve),
  internal_solve_source_identity:inside,core_instrumentation_file:'core-instrumentation.json',
  core_instrumentation_sha256:sha(coreRaw),Function_toString_not_modified:true,
  internal_solve_is_not_public_wrapper_Function_toString:true,original_evaluate_has_no_new_observers:true};
}
function liveIdentity(dn){
 return {parameters:mathematical(dn.tail.parameters),rawNode:Array.from(dn.tail.rawNode),
  graphs_float64le_sha256:binaryRowsHash(dn.tail.graphs),gains_float64le_sha256:binaryRowsHash(dn.tail.gains),
  far_graph_float64le_sha256:binaryRowsHash([dn.tail.graphs.at(-1)]),
  initial_function_sha256:sha(dn.tail.initial.toString()),evaluate_function_sha256:sha(dn.tail.evaluate.toString()),
  tail_solve_function_sha256:sha(dn.tail.solve.toString()),dn_solve_function_sha256:sha(dn.solve.toString()),
  stages:dn.tail.cells.map(c=>({rawCell:c.rawCell,rawSegment:c.rawSegment,portRatio:c.portRatio,mu:c.mu,
   profiles:c.profiles.map(p=>Array.from(p.integrationBreakpoints??[]))}))};
}
function restoreRows(packet,raw,label){
 if(!Array.isArray(packet.rows)||packet.rows.length!==577)throw Error(label+': every577 node is required');
 const states=[];let negativeZeros=0;
 for(let n=0;n<577;n++){
  const row=packet.rows[n];
  if(row.node!==n||!Array.isArray(row.state)||row.state.length!==224||!row.state.every(Number.isFinite)||
     !Array.isArray(row.negative_zero_columns))throw Error(label+': complete finite ordered224-word row required');
  const state=Float64Array.from(row.state),seen=new Set();
  for(const j of row.negative_zero_columns){
   if(!Number.isInteger(j)||j<0||j>=224||seen.has(j)||state[j]!==0)throw Error(label+': invalid signed-zero sidecar');
   state[j]=-0;seen.add(j);negativeZeros++;
  }
  if(!rawView(state).equals(raw.subarray(n*224*8,(n+1)*224*8)))throw Error(label+': original raw/JSON word mismatch');
  states.push(state);
 }
 return {states,negativeZeros};
}

let preparedCalls=0;
export function restoreSelectedAndInstallBridge(dn,zero,cfg,live,request,call){
 try{
  if(call!==1||preparedCalls++!==0)throw Error('Restore the actual selected state only for the first fresh request');
  equal(request,spec.fresh_request,'same complete physical H and true final J/audit request');
  if(request.jacobian!==true||request.audit!==true)throw Error('The unchanged complete endpoint J and audit are required');
  const launchRaw=fs.readFileSync(path.join(spec.output,'verified-launch-intent.json')),launch=JSON.parse(launchRaw);
  for(const [key,value] of Object.entries({schema:'native-current576-damped-verified-launch-v1',spec_sha256:specSHA,
   source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),identity_verified_before_request:true,
   initial_native_solve_calls:0,initial_response_cache_empty:true}))equal(launch[key],value,'verified current launch '+key);
  equal(launch.inputs,spec.inputs,'all actual59 bounded source inputs');
  equal(launch.parent_selected59,spec.parent_selected59,'actual selected parent receipts');
  equal(launch.request,request,'verified actual complete request');
  equal(numericalSources(launch.current_sources),numericalSources(spec.original_source_sha256),'all unchanged actual original numerical sources');
  const ready=readVerified({path:path.join(spec.output,'native_ready.json.gz'),bytes:fs.statSync(path.join(spec.output,'native_ready.json.gz')).size,
   sha256:launch.complete_current_ready_sha256});
  for(const key of ['storedMetricAdapter','stableGraphAdapter','endpointJacobianAdapter','tailJacobian','tailPredictor'])
   equal(live[key],ready[key],'actual live original adapter '+key);
  equal(mathematical(cfg),spec.numerical_configuration,'unchanged original numerical configuration');
  if(cfg.initialCheckpoint||ready.warmEmbedding!==null)throw Error('No checkpoint geometry remapping or imported worker predictor');
  equal(mathematical(dn.tail.parameters),spec.numerical_parameters,'complete current actual original stage parameters');
  equal([dn.tail.parameters.modes,dn.tail.parameters.depth,dn.tail.cells.length],[112,576,576],'original complete dimensions');
  equal(binaryRowsHash([request.height]),heightSHA,'unchanged nonzero112-mode H');
  const result=readVerified(spec.inputs['result.json']),summary=readVerified(spec.inputs['trial-replay-summary.json']);
  const packet=readVerified(spec.inputs['selected-state-checkpoint.json.gz']);
  const oldLive=readVerified(spec.inputs['restored-original-mathematical-identity-before-seed.json']);
  if(result.replay_completed!==true||result.trial_accepted!==true||result.native_accepted!==false||
     summary.trial_accepted!==true||summary.trials.length!==1||summary.trials[0].kind!=='accepted'||
     packet.selected_by_original_strict_norm_decrease!==true||packet.converged!==false||packet.native_tail_response!==false)
   throw Error('Use actual59 selected full state without promoting it to a complete native response');
  equal(packet.cutHeight,request.height,'selected complete physical H');
  equal(packet.selected_state_float64le_sha256,selectedSHA,'actual59 selected raw identity');
  equal(packet.parameters,spec.numerical_parameters,'actual59 selected complete parameters');
  equal(packet.rawNode,Array.from(dn.tail.rawNode),'actual59 physical-node map');
  const binDesc=spec.inputs['selected-state.f64le.gz'],packed=fs.readFileSync(binDesc.path);
  equal(sha(packed),binDesc.sha256,'selected compressed binary bytes');
  equal(packed.length,binDesc.bytes,'selected compressed binary byte count');
  const raw=unpack(packed);equal(raw.length,577*224*8,'full selected raw shape');equal(sha(raw),selectedSHA,'complete selected raw binary');
  const {states,negativeZeros}=restoreRows(packet,raw,'selected actual59 state');
  equal(negativeZeros,spec.selected_negative_zero_count,'selected negative-zero count');
  const methods=methodIdentity(dn);writeJSON(spec.output,'actual-current-method-identities.json',methods);
  const before=liveIdentity(dn);equal(before,oldLive,'actual unchanged original methods/graphs/gains/far/layout');
  equal(before,spec.original_live_identity,'parent original live identity');
  equal(before.far_graph_float64le_sha256,farSHA,'all original far Robin coefficients');
  const liveFile=writeJSON(spec.output,'original-live-identity-before-selected-seed.json',before);
  // Deliberately do not replace Q0 by target or impose zero cut/far residual.
  const binding=writeJSON(spec.output,'selected-seed-binding.json',{
   schema:'native-current576-actual59-selected-seed-binding-v1',spec_sha256:specSHA,source_sha256:spec.source_sha256,
   hook_sha256:fileSHA(selfPath),parent_selected59:spec.parent_selected59,actual_selected_state_sha256:sha(raw),
   restored_negative_zero_count:negativeZeros,nodes:577,shape_dimension:224,full_height_float64le_sha256:heightSHA,
   original_live_identity:liveFile,actual_method_identity:receipt(path.join(spec.output,'actual-current-method-identities.json')),
   original_selected_noJ_norm:summary.trials[0].number_bits.trialNorm,
   first_initial_assignment_only:true,predicted:true,worker_last_or_tangentPredictor_not_imported:true,
   no_cut_or_far_projection:true,no_H_threshold_or_amplitude_ratio:true,no_initialCheckpoint_remapping:true,
   original_full_loop_and_endpoint_J_and_fresh_audit_follow:true,native_accepted:false,task_completed:false});
  installBridge(dn,request,call,before);
  return {states,diagnostics:{selected_binding:binding,selected_state_float64le_sha256:sha(raw),
   original_height_float64le_sha256:heightSHA,nodes:577,restored_negative_zero_count:negativeZeros,predicted:true,
   first_current_withJ_is_fresh:true,no_cached_baseline:true,full_original_native_loop_and_final_J_audit_requested:true}};
 }catch(error){
  writeJSON(spec.output,'selected-seed-binding-failure.json',{schema:'native-current576-selected-binding-failure-v1',
   spec_sha256:specSHA,error:cleanError(error),native_accepted:false,task_completed:false});
  throw error;
 }
}

function saveArray(directory,name,shape,rowAt,{chunkRows=4}={}){
 const width=shape.slice(1).reduce((a,b)=>a*b,1),chunks=[],hash=crypto.createHash('sha256');
 const rows=shape[0];let total=0;
 for(let start=0,index=0;start<rows;start+=chunkRows,index++){
  const stop=Math.min(rows,start+chunkRows),parts=[];
  for(let n=start;n<stop;n++){
   const row=rowAt(n);if(!(row instanceof Float64Array)||row.length!==width)throw Error('Complete original array row required: '+name);
   parts.push(rawView(row));
  }
  const raw=Buffer.concat(parts),file='large-arrays/'+name+'-'+String(index).padStart(4,'0')+'.f64le';
  fs.writeFileSync(path.join(directory,file),raw,{flag:'wx'});hash.update(raw);total+=raw.length;
  const digest=sha(raw);chunks.push({array:name,chunk_index:index,row_start:start,row_stop:stop,file,bytes:raw.length,
   sha256:digest,raw_sha256:digest});
 }
 return {name,dtype:'<f8',order:'C',shape,total_bytes:total,raw_sha256:hash.digest('hex'),completed:true,chunks};
}
function captureCurrent(directory,{ev,states,target,scales,it,M,K,depth},call,sequence,before){
 if(M!==112||K!==224||depth!==576||states.length!==577||ev.flows.length!==576||ev.residuals.length!==576)
  throw Error('The complete current original576 system is required');
 fs.mkdirSync(directory,{recursive:false});fs.mkdirSync(path.join(directory,'large-arrays'));
 const coreRaw=fs.readFileSync(path.join(spec.output,'core-instrumentation.json'));
 fs.writeFileSync(path.join(directory,'core-instrumentation.json'),coreRaw,{flag:'wx'});
 const coreReceipt=receipt(path.join(directory,'core-instrumentation.json'),directory);
 const cut=new Float64Array(M);for(let j=0;j<M;j++)cut[j]=states[0][j]-target[j];
 const arrays=[
  saveArray(directory,'base-states',[577,224],n=>states[n]),
  saveArray(directory,'stage-residuals',[576,224],n=>ev.residuals[n]),
  saveArray(directory,'stage-out',[576,224],n=>ev.flows[n].out),
  saveArray(directory,'original-scales',[1,577],()=>scales),
  saveArray(directory,'cut-residual',[1,112],()=>cut),
  saveArray(directory,'end-residual',[1,112],()=>ev.end),
  saveArray(directory,'original-far-graph',[1,112],()=>installedDN.tail.graphs.at(-1)),
  saveArray(directory,'physical-height',[1,112],()=>Float64Array.from(spec.fresh_request.height)),
  saveArray(directory,'cut-target',[1,112],()=>target),
  saveArray(directory,'stage-jacobians',[576,224,224],n=>ev.flows[n].J),
 ];
 const hashes=Object.fromEntries(arrays.map(a=>[a.name,a.raw_sha256]));
 if(it===0)equal(hashes['base-states'],selectedSHA,'first actual current withJ selected59 words');
 for(const [name,digest] of [['physical-height',heightSHA],['original-scales',scaleSHA],['original-far-graph',farSHA],['cut-target',targetSHA]])
  equal(hashes[name],digest,'unchanged original current '+name+' words');
 const flowMetadata=writeJSON(directory,'flow-return-metadata.json.gz',{
  schema:'current-native576-original-flow-return-scalars-v1',native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,
  scope:'Read-only original returned meanHeight/minA/minD; no extra flow call or recomputation',
  rows:ev.flows.map((f,n)=>({stage:n,rawCell:before.stages[n].rawCell,rawSegment:before.stages[n].rawSegment,
   meanHeight:numberRecord(f.meanHeight),minA:numberRecord(f.minA),minD:numberRecord(f.minD)}))
 },{compressed:true});
 const manifest=writeJSON(directory,'array-manifest.json',{
  schema:'current-native576-withJ-snapshot-arrays-v1',source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
  native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,M,K,depth,arrays,
  all_original_payloads_artifact_only:true,signed_zero_and_actual_nonfinite_payload_bits_retained:true});
 const context=writeJSON(directory,'context.json.gz',{
  schema:'current-native576-withJ-snapshot-context-v1',source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
  native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,parent_selected59:spec.parent_selected59,
  original_sources:numericalSources(spec.original_source_sha256),numerical_configuration:spec.numerical_configuration,
  parameters:before.parameters,rawNode:before.rawNode,cells:before.stages,
  graphs_sha256:before.graphs_float64le_sha256,gains_sha256:before.gains_float64le_sha256,
  far_graph_sha256:before.far_graph_float64le_sha256,raw_array_sha256:hashes,core_instrumentation:coreReceipt,
  flow_return_metadata:flowMetadata,fresh_current_evaluate_completed:true,no_cached_baseline:true,
  snapshot_does_not_call_RHS_J_ODE:true,current_original_norm:numberRecord(ev.norm),
  current_original_minA:numberRecord(ev.minA),current_original_minD:numberRecord(ev.minD),
  cut_residual_is_actual_current_subtraction:true,no_cut_or_far_zero_assumption:true,
  original_evaluate_and_flow_source_not_instrumented:true
 },{compressed:true});
 const result=writeJSON(directory,'result.json',{
  schema:'current-native576-withJ-snapshot-result-v1',snapshot_completed:true,source_sha256:spec.source_sha256,
  hook_sha256:fileSHA(selfPath),native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,M,K,depth,
  manifest,context,actual_current_original_norm:numberRecord(ev.norm),actual_current_original_minA:numberRecord(ev.minA),
  actual_current_original_minD:numberRecord(ev.minD),current_state_sha256:hashes['base-states'],
  original_fresh_withJ_already_returned:true,new_RHS_J_ODE_calls_by_snapshot:0,native_accepted:false,task_completed:false});
 return {result,manifest,context,raw_array_sha256:hashes,current_state_sha256:hashes['base-states']};
}

function checkedCurrentDirection(directory,snapshot,{it,call,sequence}){
 const file=path.join(directory,'result.json.gz'),raw=fs.readFileSync(file),result=JSON.parse(unpack(raw));
 const expected={schema:'complete-native-current576-damped-square-root-direction-v1',
  source_sha256:spec.bridge.source_sha256,system_source_sha256:spec.bridge.system_source_sha256,
  factor_engine_source_sha256:spec.bridge.factor_engine_source_sha256,kernel_source_sha256:spec.bridge.kernel_source_sha256,
  model_scope:spec.bridge.model_scope,diagnostic_completed:true,linear_direction_computed:true,
  native_accepted:false,task_completed:false,native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,
  current_state_sha256:snapshot.current_state_sha256};
 for(const [key,value] of Object.entries(expected))equal(result[key],value,'complete actual current QR result '+key);
 if(result.actual_error)throw Error('The current complete linear direction did not finish: '+result.actual_error);
 equal(result.eta_cli_text,spec.bridge.eta_cli_text,'unchanged explicit eta CLI');
 equal(result.eta_binary64,spec.bridge.eta_binary64,'unchanged explicit eta binary value');
 equal(result.snapshot_result,snapshot.result,'this actual current snapshot receipt');
 const binding=readVerified(result.input_binding,directory);
 for(const [key,value] of Object.entries({schema:'current-native576-complete-linear-system-binding-v1',
  adapter_source_sha256:spec.bridge.system_source_sha256,snapshot_result_sha256:snapshot.result.sha256,
  snapshot_context_sha256:snapshot.context.sha256,snapshot_manifest_sha256:snapshot.manifest.sha256,
  current_state_sha256:snapshot.current_state_sha256,raw_array_sha256:snapshot.raw_array_sha256,
  native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,modes:112,shape_dimension:224,
  depth:576,original_depth:576,node_count:577,old_to_new:Array.from({length:577},(_,i)=>i),
  fresh_current_evaluate_completed:true,no_cached_baseline:true,no_zero_cut_or_far_assumption:true,
  current_cut_far_errors_not_projected_or_zeroed:true,parent_selected59:spec.parent_selected59}))
  equal(binding[key],value,'complete actual current system binding '+key);
 equal(result.new_matrix_identity_sha256,binding.new_matrix_identity_sha256,'this current matrix identity');
 const packet=readVerified(result.native_direction_checkpoint,directory),manifest=readVerified(result.array_manifest,directory);
 for(const [key,value] of Object.entries({schema:'complete-native-current576-damped-direction-arrays-v1',
  source_sha256:spec.bridge.source_sha256,new_matrix_identity_sha256:binding.new_matrix_identity_sha256,
  factor_engine_source_sha256:spec.bridge.factor_engine_source_sha256,all_arrays_artifact_only:true,native_accepted:false}))
  equal(manifest[key],value,'current output manifest '+key);
 const entries=new Map();
 for(const entry of manifest.arrays){if(entries.has(entry.name))throw Error('Unique output array names required');entries.set(entry.name,entry);}
 const entry=result.native_delta;equal(entries.get('complete-original-coordinate-delta'),entry,'full current direction descriptor');
 equal(entry.shape,[577,224],'complete current direction shape');equal(entry.dtype,'<f8','current direction binary dtype');equal(entry.order,'C','current direction order');
 const deltaFile=safeWithin(directory,entry.file),deltaRaw=fs.readFileSync(deltaFile);
 equal(deltaRaw.length,577*224*8,'full current delta byte count');equal(deltaRaw.length,entry.bytes,'delta descriptor bytes');equal(sha(deltaRaw),entry.sha256,'full current delta raw hash');
 for(const [key,value] of Object.entries({schema:'complete-native-current576-damped-direction-v1',
  source_sha256:spec.bridge.source_sha256,system_source_sha256:spec.bridge.system_source_sha256,
  factor_engine_source_sha256:spec.bridge.factor_engine_source_sha256,input_binding:binding,M:112,K:224,depth:576,
  original_depth:576,old_to_new:Array.from({length:577},(_,i)=>i),eta_binary64:spec.bridge.eta_binary64,
  model_scope:spec.bridge.model_scope,native_accepted:false,task_completed:false,native_call:call,
  nonlinear_iteration:it,snapshot_sequence:sequence,current_state_sha256:snapshot.current_state_sha256}))
  equal(packet[key],value,'complete current direction checkpoint '+key);
 equal(packet.delta_float64le_sha256,sha(deltaRaw),'current checkpoint raw identity');
 const {states:delta,negativeZeros}=restoreRows(packet,deltaRaw,'complete current original-coordinate direction');
 equal(entry.finite,577*224,'all actual current direction words are finite');equal(entry.negative_zero,negativeZeros,'current direction signed-zero count');
 // Factor-model, gradient, exact linear defect and L2 values are diagnostics.
 // They are not used here as additional nonlinear acceptance tests.
 return {delta,result_receipt:receipt(file,directory),input_binding:result.input_binding,
  direction_checkpoint:result.native_direction_checkpoint,array_manifest:result.array_manifest,
  delta_receipt:entry,new_matrix_identity_sha256:binding.new_matrix_identity_sha256,
  negative_zero_count:negativeZeros,complete_model_diagnostics_not_used_as_acceptance_gate:true};
}

let installedDN=null,installedContext=false;
function installBridge(dn,request,call,before){
 if(installedContext||globalThis[Symbol.for(KEY)])throw Error('Install only one current complete correction bridge');
 installedDN=dn;installedContext=true;
 const started=Date.now(),records=[];let snapshots=0,directions=0,actualFailure=null,summaryWritten=false;
 function finish(){
  if(summaryWritten)return;summaryWritten=true;
  writeJSON(spec.output,'current-correction-summary.json',{
   schema:'native-current576-damped-correction-bridge-summary-v1',source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
   spec_sha256:specSHA,parent_selected59:spec.parent_selected59,native_call:call,
   current_direction_source_sha256:spec.bridge.source_sha256,current_system_source_sha256:spec.bridge.system_source_sha256,
   eta_cli_text:spec.bridge.eta_cli_text,eta_binary64:spec.bridge.eta_binary64,model_scope:spec.bridge.model_scope,
   snapshots_completed:snapshots,directions_returned:directions,iterations:records,actual_bridge_failure:actualFailure,
   current_withJ_only:true,no_cached_actual28_or_other_baseline:true,no_cut_or_far_direction_projection:true,
   original_full_native_loop_and_final_endpoint_J_audit_retained:true,
   this_summary_does_not_claim_native_convergence:true,native_accepted:false,task_completed:false,
   elapsed_seconds:(Date.now()-started)/1000});
 }
 process.once('exit',()=>{try{finish();}catch(error){process.stderr.write('Current bridge summary write failed: '+String(error)+'\n');}});
 globalThis[Symbol.for(KEY)]={correction(args){
  const {ev,states,target,scales,it,M,K,depth}=args;
  const sequence=records.length;
  if(!Number.isInteger(it)||it<0||it!==sequence)throw Error('Use each actual original nonlinear iteration once in original order');
  const iterationName='iteration-'+String(it).padStart(3,'0'),iterationDir=path.join(spec.output,iterationName);
  const record={native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,iteration_directory:iterationName,
   snapshot_completed:false,linear_direction_returned:false,source_current_withJ_norm:numberRecord(ev.norm)};
  records.push(record);
  fs.mkdirSync(iterationDir,{recursive:false});
  try{
   equal(liveIdentity(dn),before,'unchanged original methods/graphs/gains/layout before current capture');
   const snapshotDir=path.join(iterationDir,'snapshot'),snapshot=captureCurrent(snapshotDir,args,call,sequence,before);
   snapshots++;record.snapshot_completed=true;record.snapshot={...snapshot.result,file:iterationName+'/snapshot/result.json'};
   record.current_state_sha256=snapshot.current_state_sha256;
   const qrDir=path.join(iterationDir,'qr'),command=[spec.bridge.python_executable,path.join(here,spec.bridge.source_file),
    '--snapshot-directory',snapshotDir,'--snapshot-result-sha256',snapshot.result.sha256,
    '--eta',spec.bridge.eta_cli_text,'--out',qrDir,
    '--max-factor-bytes',String(spec.bridge.max_factor_bytes),'--exact-workers',String(spec.bridge.exact_workers)];
   const launch={schema:'current-native576-synchronous-QR-launch-v1',native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,
    command,shell:false,original_evaluate_already_returned:true,snapshot_result:snapshot.result,
    source_sha256:spec.bridge.source_sha256,system_source_sha256:spec.bridge.system_source_sha256,
    stdout:'qr.stdout.log',stderr:'qr.stderr.log',original_worker_stdout_protocol_not_used_by_child:true};
   writeJSON(iterationDir,'qr-launch.json',launch);
   const stdout=fs.openSync(path.join(iterationDir,'qr.stdout.log'),'wx'),stderr=fs.openSync(path.join(iterationDir,'qr.stderr.log'),'wx');
   let completed;
   try{completed=spawnSync(command[0],command.slice(1),{shell:false,cwd:here,
    env:{...process.env,OPENBLAS_NUM_THREADS:'1',OMP_NUM_THREADS:'1',MKL_NUM_THREADS:'1'},stdio:['ignore',stdout,stderr]});}
   finally{fs.closeSync(stdout);fs.closeSync(stderr);}
   const exit={schema:'current-native576-synchronous-QR-exit-v1',native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,
    status:completed.status,signal:completed.signal,error:completed.error?cleanError(completed.error):null,
    stdout:receipt(path.join(iterationDir,'qr.stdout.log'),iterationDir),stderr:receipt(path.join(iterationDir,'qr.stderr.log'),iterationDir)};
   writeJSON(iterationDir,'qr-exit.json',exit);record.qr_exit=exit;
   if(completed.error||completed.status!==0)throw Error('Current576 QR process failed; complete current snapshot and child logs retained');
   const answer=checkedCurrentDirection(qrDir,snapshot,{it,call,sequence});
   // Original state/target/scales must still be the exact captured values.
   equal(binaryRowsHash(states),snapshot.raw_array_sha256['base-states'],'bridge did not mutate actual current states');
   equal(binaryRowsHash([target]),snapshot.raw_array_sha256['cut-target'],'bridge did not mutate original target');
   equal(binaryRowsHash([scales]),snapshot.raw_array_sha256['original-scales'],'bridge did not mutate original residual scales');
   equal(liveIdentity(dn),before,'bridge did not change original numerical object');
   const directionRecord={schema:'current-native576-returned-correction-v1',native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,
    current_state_sha256:snapshot.current_state_sha256,snapshot_result:snapshot.result,
    result:answer.result_receipt,input_binding:answer.input_binding,direction_checkpoint:answer.direction_checkpoint,
    array_manifest:answer.array_manifest,native_delta:answer.delta_receipt,new_matrix_identity_sha256:answer.new_matrix_identity_sha256,
    restored_negative_zero_count:answer.negative_zero_count,complete_current576_original_coordinates:true,
    no_cut_or_far_projection:true,chartCondition_not_computed:true,returned_maxChartCondition:null,
    original_ten_noJ_trials_follow:true,no_extra_L2_or_exact_defect_acceptance_gate:true,native_accepted:false};
   writeJSON(iterationDir,'returned-correction.json',directionRecord);
   record.direction=directionRecord;record.linear_direction_returned=true;directions++;
   fs.appendFileSync(path.join(spec.output,'current-corrections.jsonl'),encode(record));
   return {delta:answer.delta,maxChartCondition:null};
  }catch(error){
   record.actual_error=cleanError(error);actualFailure={native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,error:record.actual_error};
   try{writeJSON(iterationDir,'bridge-failure.json',{schema:'current-native576-correction-bridge-failure-v1',...record,native_accepted:false});
       fs.appendFileSync(path.join(spec.output,'current-corrections.jsonl'),encode(record));}catch(retentionError){
    process.stderr.write('Current bridge failure-record error: '+String(retentionError)+'\n');
   }
   throw error;
  }
 }};
}

const correctionReplacement={before:'const cor=correction(ev,states,target);',
 after:'const cor=globalThis[Symbol.for("visible-flex.native-current576-damped-solve.v1")].correction({ev,states,target,scales,it,M,K,depth});'};
let engineLoadCount=0;
function transformEngine(loaded){
 if(engineLoadCount++!==0)throw Error('Only one original stored/recovery engine load is permitted');
 const source=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 if(sha(source)!==engineSHA)throw Error('The original stored/recovery engine source changed');
 const anchor="const coreURL='data:text/javascript;base64,'+Buffer.from(redirect(core)).toString('base64');";
 if(source.split(anchor).length!==2)throw Error('Unique original engine compile anchor required');
 const program=[
  'const currentNativeOriginalCore=core;',
  'if(sha256(originalCore)!=='+JSON.stringify(coreSHA)+')throw Error("Original native core changed");',
  'if(sha256(core)!=='+JSON.stringify(runtimeSHA)+')throw Error("Original runtime core changed");',
  'const currentNativeChange='+JSON.stringify(correctionReplacement)+';',
  'if(core.split(currentNativeChange.before).length!==2)throw Error("Unique original nonlinear correction call required");',
  'function currentNativeSlice(text,start,stop){',
  ' if(text.split(start).length!==2||text.split(stop).length!==2)throw Error("Unique original source boundaries required");',
  ' return text.slice(text.indexOf(start),text.indexOf(stop)).trim();',
  '}',
  'const currentNativeSolveStart=" function solve(target,opts={}){",currentNativeSolveEnd="\\n return {solve,initial,evaluate";',
  'const currentNativeEvalStart=" function evaluate(states,target,withJac,scales){",currentNativeEvalEnd="\\n function correction(";',
  'const currentNativeTrialStart="   for(let k=0;k<10;k++){",currentNativeTrialEnd=\'   if(!accepted)throw new Error("multiple-shooting line search failed at "+ev.norm);\';',
  'const currentNativeOriginalSolve=currentNativeSlice(core,currentNativeSolveStart,currentNativeSolveEnd);',
  'const currentNativeOriginalEvaluate=currentNativeSlice(core,currentNativeEvalStart,currentNativeEvalEnd);',
  'if(sha256(currentNativeOriginalSolve)!=='+JSON.stringify(internalSolveSHA)+')throw Error("Original internal solve source changed");',
  'if(sha256(currentNativeOriginalEvaluate)!=='+JSON.stringify(evaluateSHA)+')throw Error("Original evaluate source changed");',
  'if(core.split(currentNativeTrialStart).length!==2||core.split(currentNativeTrialEnd).length!==2)throw Error("Unique original ten-trial source boundaries required");',
  'const currentNativeTrialText=core.slice(core.indexOf(currentNativeTrialStart),core.indexOf(currentNativeTrialEnd));',
  'if(sha256(currentNativeTrialText)!=='+JSON.stringify(trialSHA)+')throw Error("Original ten-trial source changed");',
  'core=core.replace(currentNativeChange.before,currentNativeChange.after);',
  'if(core.split(currentNativeChange.after).length!==2||core.replace(currentNativeChange.after,currentNativeChange.before)!==currentNativeOriginalCore)',
  ' throw Error("Source change exceeds the one original nonlinear correction call");',
  'const currentNativeInstrumentedSolve=currentNativeSlice(core,currentNativeSolveStart,currentNativeSolveEnd);',
  'const currentNativeUnchangedEvaluate=currentNativeSlice(core,currentNativeEvalStart,currentNativeEvalEnd);',
  'const currentNativeUnchangedTrial=core.slice(core.indexOf(currentNativeTrialStart),core.indexOf(currentNativeTrialEnd));',
  'if(currentNativeUnchangedEvaluate!==currentNativeOriginalEvaluate||currentNativeUnchangedTrial!==currentNativeTrialText)',
  ' throw Error("Original evaluate or trial arithmetic changed");',
  'const currentNativeSolveIdentity={schema:"current-native576-internal-solve-source-roundtrip-v1",',
  ' original_internal_solve_source:currentNativeOriginalSolve,original_internal_solve_source_sha256:sha256(currentNativeOriginalSolve),',
  ' instrumented_internal_solve_source:currentNativeInstrumentedSolve,instrumented_internal_solve_source_sha256:sha256(currentNativeInstrumentedSolve),',
  ' replacement:currentNativeChange,exact_internal_source_roundtrip_verified:true,',
  ' source_scope:"trimmed unique internal solve declaration in actual compiled runtime core",',
  ' distinct_from_public_split_wrapper_Function_toString:true,Function_toString_not_modified:true};',
  'fs.writeFileSync('+JSON.stringify(path.join(spec.output,'core-instrumentation.json'))+',JSON.stringify({',
  ' schema:"current-native576-correction-only-core-instrumentation-v1",spec_sha256:'+JSON.stringify(specSHA)+',',
  ' source_sha256:'+JSON.stringify(spec.source_sha256)+',hook_sha256:'+JSON.stringify(fileSHA(selfPath))+',',
  ' original_core_file_sha256:sha256(originalCore),original_runtime_core_sha256:sha256(currentNativeOriginalCore),',
  ' instrumented_runtime_core_sha256:sha256(core),exact_correction_call_roundtrip_verified:true,',
  ' internal_solve_source_identity:currentNativeSolveIdentity,original_evaluate_source_sha256:sha256(currentNativeOriginalEvaluate),',
  ' actual_evaluate_source_sha256:sha256(currentNativeUnchangedEvaluate),original_evaluate_body_byte_identical:true,',
  ' original_ten_trial_body_sha256:sha256(currentNativeTrialText),instrumented_ten_trial_body_sha256:sha256(currentNativeUnchangedTrial),',
  ' original_ten_trial_body_byte_identical:true,original_withJ_evaluate_calls_retained:true,',
  ' original_full_loop_and_tolerances_and_iteration_limit_retained:true,',
  ' original_final_endpoint_sensitivity_and_J_and_audit_not_replaced:true,',
  ' only_nonlinear_correction_call_replaced:true,no_cached_baseline:true,no_planned_one_step_stop:true,',
  ' native_accepted:false,task_completed:false},null,2)+"\\n",{flag:"wx"});'
 ].join('\n')+'\n';
 const transformed=source.replace(anchor,program+anchor);
 if(transformed.replace(program,'')!==source)throw Error('Engine loader source insertion is not exactly reversible');
 writeJSON(spec.output,'engine-loader-instrumentation.json',{
  schema:'current-native576-engine-loader-source-roundtrip-v1',source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,
  original_engine_sha256:engineSHA,instrumented_engine_sha256:sha(transformed),inserted_program_sha256:sha(program),
  exact_loader_insertion_roundtrip_verified:true,insertion_after_original_identity_checks:true,
  original_disk_source_and_original_ready_manifest_retained:true});
 return {...loaded,source:transformed};
}

registerHooks({load(url,context,nextLoad){
 const loaded=nextLoad(url,context);
 if(url.startsWith('file:')&&path.resolve(fileURLToPath(url))===path.resolve(enginePath))return transformEngine(loaded);
 if(!url.startsWith('file:')||path.resolve(fileURLToPath(url))!==path.resolve(frozenPath))return loaded;
 const source=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 if(sha(source)!==frozenSHA)throw Error('The frozen original mathematical worker changed');
 const outerAnchor="try{\n  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));";
 if(source.split(outerAnchor).length!==2)throw Error('Unique original frozen-worker execution anchor required');
 const initialAnchor='  let initial,predicted=false;';
 const injection=[
  '',
  '  if(call===1){',
  '   if(last!==null||tangentPredictor!==null)throw Error("The selected seed must not import worker prediction state");',
  '   const selectedModule=await import('+JSON.stringify(import.meta.url)+');',
  '   const selectedSeed=selectedModule.restoreSelectedAndInstallBridge(dn,zero,cfg,{',
  '    storedMetricAdapter:storedGeometry.manifest,stableGraphAdapter:storedEngineManifest,',
  '    endpointJacobianAdapter:adapterManifest,tailJacobian:backendLabel,tailPredictor:predictorLabel},req,call);',
  '   initial=selectedSeed.states;predicted=true;',
  '   trace({event:"actual59_selected_start_for_complete_current576_native_solve",call,...selectedSeed.diagnostics});',
  '  }'
 ].join('\n');
 const insert=[
  'const currentSelectedAnchor='+JSON.stringify(initialAnchor)+';',
  'if(source.split(currentSelectedAnchor).length!==2)throw Error("Unique original initial declaration required");',
  'const currentSelectedOriginalSource=source,currentSelectedAt=source.indexOf(currentSelectedAnchor)+currentSelectedAnchor.length;',
  'const currentSelectedInjection='+JSON.stringify(injection)+';',
  'source=source.slice(0,currentSelectedAt)+currentSelectedInjection+source.slice(currentSelectedAt);',
  'if(source.slice(0,currentSelectedAt)+source.slice(currentSelectedAt+currentSelectedInjection.length)!==currentSelectedOriginalSource)',
  ' throw Error("Selected initializer instrumentation must be insertion-only");',
  'fs.writeFileSync('+JSON.stringify(path.join(spec.output,'worker-instrumentation.json'))+',JSON.stringify({',
  ' schema:"current-native576-first-selected-initial-assignment-v1",',
  ' source_sha256:'+JSON.stringify(spec.source_sha256)+',hook_sha256:'+JSON.stringify(fileSHA(selfPath))+',spec_sha256:'+JSON.stringify(specSHA)+',',
  ' frozen_worker_sha256:'+JSON.stringify(frozenSHA)+',original_compiled_worker_sha256:sha256(currentSelectedOriginalSource),',
  ' instrumented_compiled_worker_sha256:sha256(source),injection_sha256:sha256(currentSelectedInjection),',
  ' exact_insertion_roundtrip_verified:true,first_initial_assignment_only:true,predicted_set_true_only_for_seed:true,',
  ' worker_last_and_tangentPredictor_not_fabricated:true,no_initialCheckpoint_geometry_remapping:true,',
  ' original_request_loop_and_final_J_and_audit_retained:true,no_planned_stop:true',
  '},null,2)+"\\n",{flag:"wx"});'
 ].join('\n')+'\n';
 const transformed=source.replace(outerAnchor,insert+outerAnchor);
 if(transformed.replace(insert,'')!==source)throw Error('Frozen-worker loader insertion is not reversible');
 return {...loaded,source:transformed};
}});
