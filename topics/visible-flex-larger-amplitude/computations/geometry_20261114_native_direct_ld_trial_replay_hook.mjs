// Independent first original line-search replay. Restore the exact actual23
// base, reuse the bound actual28 withJac baseline, and inject one complete
// saved direction. Original ten-alpha trials/guards/strict merit remain intact.
// This stops before another Newton iteration, endpoint J, or fresh audit.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {fileURLToPath} from 'node:url';
import {registerHooks} from 'node:module';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('Original native trial replay belongs to the public repository Actions');
const specPath=process.env.VISIBLE_FLEX_NATIVE_DIRECT_LD_TRIAL_REPLAY_SPEC;
if(!specPath)throw Error('Explicit verified complete native seed specification required');
const selfPath=fileURLToPath(import.meta.url),here=path.dirname(selfPath);
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const fileSHA=p=>sha(fs.readFileSync(p));
const specRaw=fs.readFileSync(specPath),spec=JSON.parse(specRaw),specSHA=sha(specRaw);
const frozenPath=path.join(here,'tail_frozen_worker.mjs');
const frozenSHA='3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054';
const actual23SHA='aa93fb8afbd0c8ce3ec49859f3bcfae465696654f626ed1678ceb430329ec6ea';
const candidateSHA='6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8';
const heightSHA='c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f';
const scaleSHA='ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc';
const farSHA='395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54';
if(spec.schema!=='original-native-direct-LD1372-trial-replay-spec-v1'||
   spec.hook_sha256!==fileSHA(selfPath)||spec.inputs.v3_candidate_summary.sha256!==actual23SHA||
   spec.candidate_states_float64le_sha256!==candidateSHA||spec.exact_height_float64le_sha256!==heightSHA||
   spec.original_scales_float64le_sha256!==scaleSHA||spec.original_far_graph_float64le_sha256!==farSHA)
 throw Error('Native seed source or original candidate specification differs');
for(const [name,digest] of Object.entries(spec.frozen_sources)){
 if(path.basename(name)!==name||fileSHA(path.join(here,name))!==digest)
  throw Error('Frozen original or provenance source changed: '+name);
}

function stable(v){
 if(Array.isArray(v))return v.map(stable);
 if(v&&typeof v==='object')return Object.fromEntries(Object.keys(v).sort().map(k=>[k,stable(v[k])]));
 return v;
}
function same(a,b){return JSON.stringify(stable(a))===JSON.stringify(stable(b));}
function equal(a,b,label){if(!same(a,b))throw Error('Native seed identity differs: '+label);}
function mathematical(v){return Object.fromEntries(Object.entries(v).filter(([k])=>!spec.io_keys.includes(k)));}
function numericalSources(v){return Object.fromEntries(Object.entries(v).filter(([k])=>!['input_config','runtime_config'].includes(k)));}
function readVerified(row){
 const raw=fs.readFileSync(row.path);
 if(sha(raw)!==row.sha256||('bytes' in row&&raw.length!==row.bytes))
  throw Error('Changed original complete seed evidence: '+row.path);
 const unpacked=raw[0]===31&&raw[1]===139?zlib.gunzipSync(raw):raw;
 if(row.raw_sha256&&sha(unpacked)!==row.raw_sha256)
  throw Error('Unpacked complete seed evidence changed: '+row.path);
 const value=JSON.parse(unpacked.toString());
 if('rows' in row&&(!Array.isArray(value.rows)||value.rows.length!==row.rows))
  throw Error('Complete evidence row count changed: '+row.path);
 return value;
}
function encode(value){
 return JSON.stringify(value,(_key,x)=>{
  if(typeof x==='number'&&!Number.isFinite(x))throw Error('Nonfinite completed seed evidence record');
  return x;
 })+'\n';
}
function writeJSON(name,value){
 const raw=Buffer.from(encode(value));
 if(raw.length>=1_000_000)throw Error('Use bounded gzip packets for a large evidence record');
 fs.writeFileSync(path.join(spec.output,name),raw,{flag:'wx'});
 return {file:name,sha256:sha(raw),bytes:raw.length};
}
function binaryRowsHash(rows){
 const hash=crypto.createHash('sha256');
 for(const row of rows){
  const bytes=Buffer.allocUnsafe(8*row.length);
  for(let j=0;j<row.length;j++)bytes.writeDoubleLE(row[j],8*j);
  hash.update(bytes);
 }
 return hash.digest('hex');
}
// The split adapter exports an unchanged arrow wrapper around the internal
// core solve. Hash that actual public function unchanged. Independently record
// the compiled internal source slice and its exact three-site source reversal;
// neither source slice is represented as the public wrapper's Function.toString.
function actualMethodAndInternalSourceIdentity(dn){
 const coreFile=path.join(spec.output,'core-instrumentation.json'),raw=fs.readFileSync(coreFile);
 const core=JSON.parse(raw),inside=core.internal_solve_source_identity;
 if(core.spec_sha256!==specSHA||core.hook_sha256!==fileSHA(selfPath)||
    core.original_runtime_core_sha256!==spec.capture.original_runtime_core_sha256||
    core.exact_two_replacements_and_observer_roundtrip_verified!==true||
    !inside||inside.exact_internal_source_roundtrip_verified!==true||
    sha(inside.instrumented_internal_solve_source)!==inside.instrumented_internal_solve_source_sha256||
    sha(inside.restored_original_internal_solve_source)!==inside.original_internal_solve_source_sha256)
  throw Error('Declared actual internal core source identity is incomplete');
 const actual=dn.tail.solve.toString();
 return {schema:'original-native-step-trial-public-and-internal-solve-identity-v1',
  actual_public_tail_solve_function_sha256:sha(actual),actual_public_tail_solve_function_source:actual,
  public_method_is_unchanged_split_adapter_wrapper:true,
  core_instrumentation_file:'core-instrumentation.json',core_instrumentation_sha256:sha(raw),
  internal_solve_source_identity:inside,
  actual_public_function_and_Function_toString_not_modified:true,
  internal_source_slice_is_not_public_Function_toString:true};
}

function verifiedOriginalSnapshot(dn){
 return {parameters:mathematical(dn.tail.parameters),rawNode:Array.from(dn.tail.rawNode),
  graphs_float64le_sha256:binaryRowsHash(dn.tail.graphs),
  gains_float64le_sha256:binaryRowsHash(dn.tail.gains),
  far_graph_float64le_sha256:binaryRowsHash([dn.tail.graphs.at(-1)]),
  initial_function_sha256:sha(dn.tail.initial.toString()),
  evaluate_function_sha256:sha(dn.tail.evaluate.toString()),
  tail_solve_function_sha256:sha(dn.tail.solve.toString()),
  dn_solve_function_sha256:sha(dn.solve.toString()),
  stages:dn.tail.cells.map(c=>({rawCell:c.rawCell,rawSegment:c.rawSegment,
   portRatio:c.portRatio,mu:c.mu,profiles:c.profiles.map(p=>Array.from(p.integrationBreakpoints??[]))}))};
}
function checkedPacket(row,probe){
 const packet=readVerified(row);
 if(packet.schema!=='actual-same-RK-candidate-probe-evidence-v3'||
    packet.retained_all_modes!==true||packet.modes!==112)
  throw Error('Wrong complete actual23 evidence packet');
 equal(packet.spec_sha256,probe.spec_sha256,'packet original specification');
 equal(packet.numerical_parameters,spec.numerical_parameters,'packet complete stage parameters');
 for(const [packetKey,inputKey] of [
   ['failed_response_sha256','failed_response'],['cold_probe_summary_sha256','cold_probe_summary'],
   ['first_candidate_summary_sha256','first_candidate_summary'],['v2_candidate_summary_sha256','v2_candidate_summary'],
   ['actual_v2_underflow_event_packet_sha256','v2_underflow_event_packet']])
  equal(packet[packetKey],spec.inputs[inputKey].sha256,'packet original ancestry '+inputKey);
 return packet.rows;
}

let preparedCalls=0;
export function restoreBoundCandidate(dn,zero,cfg,live,request,call){
 const started=Date.now();
 const failure={schema:'original-native-trial-base-binding-failure-v1',spec_sha256:specSHA,
  hook_sha256:fileSHA(selfPath),original_public_run:spec.original_public_run,
  completed_probe_public_run:spec.completed_probe_public_run,
  candidate_states_float64le_sha256:candidateSHA,seed_is_not_accepted_response:true,
  intentional_one_line_search_only:true,original_native_acceptance:false};
 try{
  if(call!==1||preparedCalls!==0)throw Error('Restore this candidate only for the first original native request');
  preparedCalls++;
  equal(request,spec.fresh_request,'same original protocol request; replay stops before endpoint J/audit');
  if(request.jacobian!==true||request.audit!==true)throw Error('Retain the original protocol flags; no endpoint J/audit is claimed by replay');
  const launchPath=path.join(spec.output,'verified-launch-intent.json'),launchRaw=fs.readFileSync(launchPath);
  const launch=JSON.parse(launchRaw);
  if(launch.schema!=='original-native-direct-LD1372-trial-replay-verified-launch-v1'||
     launch.spec_sha256!==specSHA||launch.hook_sha256!==fileSHA(selfPath)||
     launch.identity_verified_before_request!==true||launch.initial_native_solve_calls!==0||
     launch.initial_response_cache_empty!==true)
   throw Error('The original current constructor must be completely verified before native injection');
  equal(launch.inputs,spec.inputs,'verified original evidence inventory');
  equal(launch.request,request,'verified original full request');
  equal(numericalSources(launch.current_sources),numericalSources(spec.original_source_sha256),
    'all current original consumed numerical source bytes');
  const currentReady=readVerified({path:path.join(spec.output,'native_ready.json.gz'),
    sha256:launch.complete_current_ready_sha256});
  for(const key of ['storedMetricAdapter','stableGraphAdapter','endpointJacobianAdapter','tailJacobian','tailPredictor'])
   equal(live[key],currentReady[key],'live original adapter '+key);
  equal(mathematical(cfg),spec.numerical_configuration,'all original config values');
  if(cfg.initialCheckpoint||currentReady.warmEmbedding!==null)
   throw Error('Do not use a geometric checkpoint remap or imported old worker state');
  equal(mathematical(dn.tail.parameters),spec.numerical_parameters,'all actual original stage parameters');

  const oldFailure=readVerified(spec.inputs.failed_response),oldIteration=readVerified(spec.inputs.iteration),
    cold=readVerified(spec.inputs.cold_probe_summary),first=readVerified(spec.inputs.first_candidate_summary),
    v2=readVerified(spec.inputs.v2_candidate_summary),probe=readVerified(spec.inputs.v3_candidate_summary),
    checkpoint=readVerified(spec.inputs.v3_checkpoint),identity=readVerified(spec.inputs.v3_initializer_identity),
    factory=readVerified(spec.inputs.v3_factory_identity),oldLive=readVerified(spec.inputs.v3_original_live_identity),
    probeSpec=readVerified(spec.inputs.v3_specification),probeLaunch=readVerified(spec.inputs.v3_verified_launch),
    probeInstrumentation=readVerified(spec.inputs.v3_instrumentation);
  const M=dn.tail.parameters.modes,K=2*M,depth=dn.tail.parameters.depth,H=request.height;
  if(M!==112||K!==224||depth!==576||checkpoint.nodes!==577||checkpoint.shape_dimension!==K||
     !Array.isArray(H)||H.length!==M||!H.every(Number.isFinite)||!H.some(x=>x!==0))
   throw Error('Retain every original nonzero physical-height mode and every shooting node');
  if(probe.evaluation_completed!==true||probe.evaluate_calls!==1||probe.completed_stages!==depth||
     probe.all_original_no_J_flow_guards_passed!==true||probe.nonlinear_solve_called!==false||
     probe.original_methods_graphs_gains_far_boundary_and_layout_verified_unchanged!==true||
     checkpoint.success!==false||checkpoint.converged!==false||checkpoint.native_tail_response!==false)
   throw Error('A completed original no-J probe is required; it is not a solved native response');
  for(const [label,value] of [['request17',oldFailure.request.height],['request19',cold.exact_height],
      ['request21',first.exact_height],['request22',v2.exact_height],['request23',probe.exact_height],
      ['original iteration',oldIteration.checkpoint.cutHeight],['candidate',checkpoint.cutHeight]]){
   equal(value,H,label+' full original H');
   equal(binaryRowsHash([value]),heightSHA,label+' original H binary64');
  }
  equal(probe.inputs,probeSpec.inputs,'actual23 summary/specification inputs');
  // Old files carry historical absolute paths. Their immutable byte hashes,
  // not their old locations, bind this relocated public Actions execution.
  for(const [key,row] of Object.entries(probe.inputs))
   equal(row.sha256,spec.inputs[key].sha256,'relocated actual23 original input '+key);
  equal(checkpoint.spec_sha256,probe.spec_sha256,'candidate originating probe');
  const withoutPath=rows=>rows.map(({path:_path,...row})=>row);
  equal(withoutPath(spec.candidate_state_chunks),checkpoint.states_artifacts,'complete restored state manifest');
  equal(withoutPath(spec.original_graph_scale_chunks),probe.original_graphs_gains_artifacts,'original graph/scale manifest');
  equal(checkpoint.states_float64le_sha256,candidateSHA,'candidate checkpoint state bytes');
  equal(identity.candidateStatesFloat64LESHA256,candidateSHA,'initializer recorded state bytes');
  equal(identity.physicalHeightFloat64LESHA256,heightSHA,'initializer recorded H bytes');
  equal(identity.originalResidualScalesFloat64LESHA256,scaleSHA,'initializer original residual scales');
  equal(identity.originalFarGraphSHA256,farSHA,'initializer original far Robin graph');
  equal(probeLaunch.spec_sha256,probe.spec_sha256,'actual23 verified launch');
  equal(probeInstrumentation.hook_sha256,probe.hook_sha256,'actual23 instrumentation');
  for(const [key,value] of Object.entries(factory))equal(identity[key],value,'unchanged initializer factory '+key);

  const methodIdentity=actualMethodAndInternalSourceIdentity(dn);
  writeJSON('actual-replay-method-identities.json',methodIdentity);
  const before=verifiedOriginalSnapshot(dn);
  equal(before,oldLive,'unchanged actual public function sources, graphs, gains, parameters and stage layout');
  equal(before.far_graph_float64le_sha256,farSHA,'all original far Robin coefficients');
  equal(Array.from(dn.tail.rawNode),checkpoint.rawNode,'all raw-node indices');
  equal(mathematical(checkpoint.parameters),spec.numerical_parameters,'complete seed parameters');
  equal(zero.radius,probe.original_radius,'original physical cut radius');
  const graphRows=spec.original_graph_scale_chunks.flatMap(row=>checkedPacket(row,probe));
  const target=Float64Array.from(H,x=>x/zero.radius**4),scales=new Float64Array(depth+1);
  // Exactly the original scaleFor; the candidate's private Riccati chart is
  // never used as a normalization or as a replacement far condition.
  scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
  for(let n=0;n<depth;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
  if(graphRows.length!==depth+1||!Array.from(scales).every(x=>Number.isFinite(x)&&x>0))
   throw Error('Original graph/scale dimensions or finite values differ');
  equal(binaryRowsHash([scales]),scaleSHA,'same original scaleFor binary64 output');
  for(let n=0;n<=depth;n++){
   const row=graphRows[n];
   if(row.node!==n)throw Error('Keep the complete original node order');
   equal(row.graphs,Array.from(dn.tail.graphs[n]),'original graph at node '+n);
   equal(row.gains_to_next,n<depth?Array.from(dn.tail.gains[n]):null,'original gain at node '+n);
   equal(binaryRowsHash([[row.original_scale]]),binaryRowsHash([[scales[n]]]),'original residual scale at node '+n);
  }
  const rows=spec.candidate_state_chunks.flatMap(row=>checkedPacket(row,probe));
  if(rows.length!==depth+1)throw Error('Restore every candidate shooting node');
  const states=[];let negativeZeros=0;
  for(let n=0;n<=depth;n++){
   const row=rows[n];
   if(row.node!==n||!Array.isArray(row.state)||row.state.length!==K||!row.state.every(Number.isFinite)||
      !Array.isArray(row.negative_zero_columns))
    throw Error('Invalid complete finite candidate node '+n);
   const state=Float64Array.from(row.state),seen=new Set();
   for(const j of row.negative_zero_columns){
    if(!Number.isInteger(j)||j<0||j>=K||state[j]!==0||seen.has(j))
     throw Error('A signed-zero sidecar must name distinct stored zeros');
    seen.add(j);state[j]=-0;negativeZeros++;
   }
   states.push(state);
  }
  equal(negativeZeros,spec.restored_negative_zero_count,'restored signed-zero count');
  equal(binaryRowsHash(states),candidateSHA,'all restored 577 by 224 candidate bytes');
  equal(binaryRowsHash([states[0].subarray(0,M)]),binaryRowsHash([target]),'unchanged original H/rCut^4 boundary input');
  equal(verifiedOriginalSnapshot(dn),before,'actual public method sources and graph/gain/geometry remain stable during restoration');
  const liveRecord=writeJSON('original-live-identity-before-seed.json',before);
  const binding={schema:'original-native-trial-base-binding-v1',spec_sha256:specSHA,
   hook_sha256:fileSHA(selfPath),verified_launch_intent_sha256:sha(launchRaw),
   original_public_run:spec.original_public_run,cold_baseline_public_run:spec.cold_baseline_public_run,
   first_candidate_public_run:spec.first_candidate_public_run,v2_candidate_public_run:spec.v2_candidate_public_run,
   completed_probe_public_run:spec.completed_probe_public_run,
   inputs:spec.inputs,source_sha256:spec.source_sha256,request:request,call:call,
   candidate_state_chunks:spec.candidate_state_chunks,original_graph_scale_chunks:spec.original_graph_scale_chunks,
   nodes:states.length,shape_dimension:K,restored_negative_zero_count:negativeZeros,
   candidate_states_float64le_sha256:binaryRowsHash(states),height_float64le_sha256:binaryRowsHash([H]),
   original_target_float64le_sha256:binaryRowsHash([target]),original_scales_float64le_sha256:binaryRowsHash([scales]),
   original_far_graph_float64le_sha256:before.far_graph_float64le_sha256,original_live_identity:liveRecord,
   retained_original_no_J_probe_norm:probe.candidate_original_no_J_norm,
   candidate_prepared_for_first_initial_assignment:true,candidate_is_accepted_response:false,
   constructor_and_exported_method_sources_verified_against_original:true,all_original_modes_and_nodes_retained:true,
   separate_runtime_trial_replay_instrumentation:true,
   original_full_solve_and_J_and_audit_follow:false,one_original_trial_loop_only:true,no_initialCheckpoint_remesh:true,
   no_height_threshold_or_amplitude_ratio_prediction:true,no_candidate_regeneration:true,
   no_zero_solve:true,task_completed:false,elapsed_seconds:(Date.now()-started)/1000};
  const descriptor=writeJSON('seed-binding.json',binding);
  installTrialReplayContext(dn,zero,cfg,request,states,before);
  return {states,diagnostics:{seed_binding:descriptor,
   original_candidate_summary_sha256:actual23SHA,candidate_states_float64le_sha256:candidateSHA,
   original_height_float64le_sha256:heightSHA,original_scales_float64le_sha256:scaleSHA,
   nodes:states.length,shape_dimension:K,restored_negative_zero_count:negativeZeros,
   predicted:true,original_protocol_J_and_audit_flags_retained:true,
   cached_actual28_baseline:true,one_saved_complete_restricted_step_direction:true,endpoint_J_and_audit_not_run:true}};
 }catch(error){
  const stack=String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,
    '<unchanged-in-memory-native-worker>');
  writeJSON('seed-binding-failure.json',{...failure,error:String(error),stack:stack.slice(0,20000),
   stack_truncated:stack.length>20000,elapsed_seconds:(Date.now()-started)/1000});
  throw error;
 }
}

const enginePath=path.join(here,'tail_resumable_engine.mjs');
const engineSHA='1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8';
const coreSHA='ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3';
const directionSourceSHA=spec.direction.source_sha256;
if(!/^[0-9a-f]{64}$/.test(directionSourceSHA)||path.basename(spec.direction.source_file)!==spec.direction.source_file||
   fileSHA(path.join(here,spec.direction.source_file))!==directionSourceSHA)
 throw Error('Explicit saved-direction producer source bytes required');
const captureResultSHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7';
const captureSummarySHA='48d8c012aa0e266bd9c39d1ce6342a97ef54c7d01a6dcfb37997da6ede4b22c1';
const captureManifestSHA='3ed8c1bf3458f2f5852c5e74ebaec77292233a6b940b494c73e4289bbdf95ae3';
const REPLAY_KEY='visible-flex.native-direct-LD1372-trial-replay.v1';
const STOP='VISIBLE_NATIVE_DIRECT_LD_TRIAL_REPLAY_ACCEPTED_STOP_V1';
if(spec.planned_accepted_trial_stop!==STOP||
   spec.source_sha256!==fileSHA(path.join(here,'geometry_20261114_native_direct_ld_trial_replay.py'))||
   spec.direction.source_sha256!==directionSourceSHA||spec.capture.inputs.result.sha256!==captureResultSHA||
   spec.capture.inputs.capture_summary.sha256!==captureSummarySHA||
   spec.capture.inputs.capture_manifest.sha256!==captureManifestSHA)
 throw Error('Bind this replay source, actual28 baseline and a complete actual step-system direction');

function numberRecord(value){
 const bytes=Buffer.allocUnsafe(8);bytes.writeDoubleLE(value);
 return {value:Number.isFinite(value)?value:null,float64le_hex:bytes.toString('hex'),
  classification:Number.isNaN(value)?'NaN':value===Infinity?'positive-infinity':
   value===-Infinity?'negative-infinity':Object.is(value,-0)?'negative-zero':'finite'};
}
function exactNumber(record,label){
 if(!record||!Number.isFinite(record.value)||!/^[0-9a-f]{16}$/.test(record.float64le_hex))
  throw Error('Finite cached binary64 scalar required: '+label);
 equal(numberRecord(record.value),record,'exact cached scalar '+label);
 return Buffer.from(record.float64le_hex,'hex').readDoubleLE();
}
function writeGzip(name,value){
 const raw=Buffer.from(encode(value)),packed=zlib.gzipSync(raw);
 fs.writeFileSync(path.join(spec.output,name),packed,{flag:'wx'});
 return {file:name,sha256:sha(packed),bytes:packed.length,raw_sha256:sha(raw),raw_bytes:raw.length};
}
function writeBinaryGzip(name,rows){
 const chunks=rows.map(row=>{
  const bytes=Buffer.allocUnsafe(8*row.length);
  for(let j=0;j<row.length;j++)bytes.writeDoubleLE(row[j],8*j);
  return bytes;
 });
 const raw=Buffer.concat(chunks),packed=zlib.gzipSync(raw);
 fs.writeFileSync(path.join(spec.output,name),packed,{flag:'wx'});
 return {file:name,sha256:sha(packed),bytes:packed.length,raw_sha256:sha(raw),raw_bytes:raw.length,
  dtype:'<f8',order:'C',shape:[rows.length,rows[0]?.length??0],signed_zero_bits_preserved:true};
}
function stateRows(rows){
 return rows.map((state,node)=>({node,state:Array.from(state,x=>Number.isFinite(x)?x:null),
  negative_zero_columns:Array.from(state.keys()).filter(j=>Object.is(state[j],-0)),
  nonfinite_columns:Array.from(state.keys()).filter(j=>!Number.isFinite(state[j]))
   .map(column=>({column,...numberRecord(state[column])}))}));
}
function checkDirection(direction,checkpoint,manifest){
 const producer='26e181ffcede90c3b2daff0c68a6725c937ecbdc7a87f017e79d7c9620700623';
 const adapter='43d633002ea1fde869b95767c0fd26619cd6b7385cbd040bf6c740c2432f5a2c';
 const probeSource='c2341018c6293e15ee8e5ba9109b331b29bee2e3e944514e1a0308afe8e6ffd5';
 const probeHook='2695cd2dc0abc66fe3f8ae8987b6ae3b50b884f692a418198347a61dddf24435';
 const windowSource='07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b';
 for(const [key,value] of Object.entries({
  schema:'native-rawcell0-direct-LD-f64-J1372-equilibrated-band-correction-v1',
  source_sha256:producer,direct_adapter_sha256:adapter,original_capture_result_sha256:captureResultSHA,
  actual_step_result_sha256:spec.direction.step_result_sha256,
  actual_direct_result_sha256:spec.direction.direct_result_sha256,
  original1372_matrix_identity_sha256:spec.direction.original1372_matrix_identity_sha256,
  target_is_new_original_coordinate_f64_J:true,no_G_shadow_or_second_target:true,
  original1372_base_r_scales_cut_far_H_unchanged:true,
  diagnostic_completed:true,linear_direction_computed:true,native_accepted:false,task_completed:false,
  original_native_calls:0,new_J_calls:0,new_ODE_steps:0,nonlinear_trials:0,
  lapack_factor_info:0,lapack_solve_info:0,M:112,K:224,
  original576_long_matrix_not_claimed_solved:true,old_long_J_defect_is_diagnostic_not_gate:true
 }))equal(direction[key],value,'actual step-direction '+key);
 equal(producer,directionSourceSHA,'unchanged frozen step direction producer');
 if(direction.actual_error)throw Error('Only a complete finite-direction artifact can be replayed');
 const full=readVerified(spec.direction.inputs.full_direction_checkpoint);
 const binding=readVerified(spec.direction.inputs.input_binding);
 const stepResult=readVerified(spec.direction.inputs.step_result);
 const stepSpec=readVerified(spec.direction.inputs.step_spec);
 const stepSummary=readVerified(spec.direction.inputs.step_summary);
 equal(full.input_binding,binding,'full direction complete captured-system identity');
 equal(checkpoint.input_binding,binding,'restricted direction complete captured-system identity');
 equal(binding.schema,'native-rawcell0-direct-longdouble-system-binding-v1','new direct-LD representation');
 const original1372=binding.original1372_input_binding;
 equal(original1372.schema,'native-rawcell0-original-step-system-binding-v1','original1372 provenance');
 equal(original1372.adapter_source_sha256,'fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81','frozen original step binder');
 equal(original1372.new_matrix_identity_sha256,'e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521','original1372 finite identity');
 equal(binding.original1372_matrix_identity_sha256,original1372.new_matrix_identity_sha256,'unchanged original target provenance');
 equal(binding.adapter_source_sha256,adapter,'new captured-system adapter source');
 equal(binding.actual41_result_sha256,spec.direction.step_result_sha256,'actual per-step result');
 equal(binding.new_matrix_identity_sha256,spec.direction.new_matrix_identity_sha256,'new finite matrix identity');
 equal(direction.new_matrix_identity_sha256,binding.new_matrix_identity_sha256,'direction new matrix');
 const original=original1372.original_capture_binding;
 for(const [key,value] of Object.entries({
  capture_result_sha256:captureResultSHA,capture_summary_sha256:captureSummarySHA,
  capture_manifest_sha256:captureManifestSHA,original_core_sha256:coreSHA,
  raw_array_sha256:spec.capture.array_sha256
 }))equal(original[key],value,'same original28 captured input '+key);
 for(const [key,value] of Object.entries({
  schema:'original-native-rawcell0-step-capture-result-v1',capture_completed:true,
  source_sha256:probeSource,hook_sha256:probeHook,window_module_sha256:windowSource,
  capture_result_sha256:captureResultSHA,original_native_solve_called:false,
  new_whole_tail_J_evaluations:0,new_original_long_J_evaluations:0,
  no_J_evaluations:0,additional_ODE_steps:0,endpoint_J_or_audit_computed:false,
  native_accepted:false,task_completed:false,original_protocol_requests:1,worker_exit_code:0,
  planned_probe_stop_observed:true,completed_original_stages:Array.from({length:72},(_,n)=>n)
 }))equal(stepResult[key],value,'completed actual per-step capture '+key);
 equal(spec.direction.inputs.step_result.sha256,spec.direction.step_result_sha256,'explicit actual capture result SHA');
 equal(spec.direction.inputs.step_spec.sha256,stepResult.spec_sha256,'actual step specification');
 equal(spec.direction.inputs.step_summary.sha256,stepResult.capture_summary_sha256,'actual step summary');
 equal(stepSummary.capture_completed,true,'all actual step records completed');
 equal(stepSpec.references.capture_binding,original,'step capture same complete original data');
 equal(stepSpec.capture.array_sha256,spec.capture.array_sha256,'step capture same original-array identities');
 const inventory=Object.fromEntries(stepResult.small_output_files.map(row=>[row.file,row]));
 equal(inventory,original1372.actual_step_small_files,'all actual step-capture metadata identities');
 for(const [name,descriptor] of Object.entries(spec.direction.step_files)){
  const listed=inventory[name];
  if(!listed||descriptor.sha256!==listed.sha256||descriptor.bytes!==listed.bytes)
   throw Error('Bound actual step metadata inventory differs');
  const raw=fs.readFileSync(descriptor.path);
  if(raw.length!==descriptor.bytes||sha(raw)!==descriptor.sha256)
   throw Error('Changed actual step metadata bytes: '+name);
 }
 const direct=readVerified(spec.direction.inputs.direct_result);
 equal(spec.direction.inputs.direct_result.sha256,spec.direction.direct_result_sha256,'actual direct capture SHA');
 equal(binding.actual_direct_result,{file:'result.json',bytes:spec.direction.inputs.direct_result.bytes,
  sha256:spec.direction.inputs.direct_result.sha256},'complete new capture descriptor');
 equal(direct.schema,'native-rawcell0-saved-step-direct-longdouble-maps-v1','new map producer schema');
 equal(direct.completed,true,'all new direct maps completed');
 equal(direct.capture_completed,true,'all original steps captured');
 equal(direct.original_capture_result_sha256,captureResultSHA,'new capture same original28');
 equal(direct.actual41_result_sha256,spec.direction.step_result_sha256,'new capture same original41');
 equal(binding.direct_source_sha256,spec.direction.actual_direct_source_sha256,'all four new source identities');
 const directNames={source_sha256:'geometry_20261114_native_rawcell0_direct_ld_capture.py',
  hook_sha256:'geometry_20261114_native_rawcell0_direct_ld_capture_hook.mjs',
  window_module_sha256:'geometry_20261114_native_rawcell0_direct_ld_window.mjs',
  worker_source_sha256:'geometry_20261114_rawcell0_direct_ld_worker.py'};
 for(const [key,name] of Object.entries(directNames)){
  equal(direct[key],binding.direct_source_sha256[name],'actual direct producer '+key);
  equal(fileSHA(path.join(here,name)),direct[key],'current direct source bytes '+name);
 }
 equal(direct.summary,binding.direct_summary,'same actual direct summary');
 equal(direct.array_manifest,binding.direct_array_manifest,'same actual direct array manifest');
 for(const [name,descriptor] of Object.entries(spec.direction.direct_files)){
  const listed=binding.all_bound_metadata[name];
  if(!listed||descriptor.sha256!==listed.sha256||descriptor.bytes!==listed.bytes)
   throw Error('Bound new direct metadata inventory differs: '+name);
  const raw=fs.readFileSync(descriptor.path);
  if(raw.length!==descriptor.bytes||sha(raw)!==descriptor.sha256)
   throw Error('Changed new direct metadata bytes: '+name);
 }
 equal(binding.old_to_new,original1372.old_to_new,'same complete577 restriction');
 equal(binding.cells,original1372.cells,'same complete1372 cell layout');
 equal(binding.original1372_base_residual_output_sigma_cut_far_H_reused_byte_for_byte,true,
  'original nonlinear base and residual data preserved');
 equal(binding.new_matrix_is_original_coordinate_binary64,true,'only new original-coordinate f64 target');
 equal(binding.no_G_shadow_or_alternative_target_matrix,true,'no second finite target');
 const depth=binding.new_depth,mapping=binding.old_to_new;
 if(!Number.isInteger(depth)||depth<576||!Array.isArray(mapping)||mapping.length!==577||
    mapping[0]!==0||mapping.at(-1)!==depth||
    mapping.some((v,j)=>!Number.isInteger(v)||v<0||v>depth||(j>0&&v<=mapping[j-1])))
  throw Error('All original577 nodes require their actual strictly ordered expanded-node map');
 equal(mapping,spec.direction.old_to_new,'verified actual original-node restriction map');
 equal(depth,spec.direction.step_depth,'verified actual new depth');
 equal([direction.depth,direction.dimension],[depth,(depth+1)*224],'complete actual new linear system');
 equal(manifest.schema,'native-direct-LD-f64-J1372-shooting-direction-arrays-v1','new direction manifest');
 equal(manifest.source_sha256,producer,'new direction manifest producer');
 equal(manifest.original_capture_result_sha256,captureResultSHA,'new direction original parent');
 equal(manifest.actual_step_result_sha256,spec.direction.step_result_sha256,'new direction actual step parent');
 equal(manifest.actual_direct_result_sha256,spec.direction.direct_result_sha256,'new direction actual direct parent');
 equal(manifest.new_matrix_identity_sha256,binding.new_matrix_identity_sha256,'manifest same new matrix');
 const entries=Object.fromEntries(manifest.arrays.map(row=>[row.name,row]));
 if(Object.keys(entries).length!==manifest.arrays.length)throw Error('Unique direction arrays are required');
 function decode(packet,schema,count,restricted,entry,name,rawDescriptor){
  for(const [key,value] of Object.entries({
   schema,source_sha256:producer,native_accepted:false,task_completed:false,
   M:112,K:224,depth:count-1,original_depth:576,step_depth:depth,old_to_new:mapping,
   produced_by_new_direct_LD_f64_J1372_matrix:true,solved_original576_long_matrix_claimed:false,solved_original41_J1372_matrix_claimed:false,
   restricted_to_original_nodes:restricted,original_nonlinear_readback_required:true,no_nonlinear_trial:true
  }))equal(packet[key],value,'complete actual direction packet '+key);
  equal(packet.scaling,direction.scaling,'actual direction scaling');
  if(!Array.isArray(packet.rows)||packet.rows.length!==count)throw Error('Keep every direction row');
  let negativeZeros=0;
  const rows=packet.rows.map((row,node)=>{
   if(row.node!==node||!Array.isArray(row.state)||row.state.length!==224||
      !row.state.every(Number.isFinite)||!Array.isArray(row.negative_zero_columns))
    throw Error('All complete finite direction coordinates are required');
   const values=Float64Array.from(row.state),seen=new Set();
   for(const j of row.negative_zero_columns){
    if(!Number.isInteger(j)||j<0||j>=224||seen.has(j)||values[j]!==0)
     throw Error('Valid complete signed-zero sidecar required');
    seen.add(j);values[j]=-0;negativeZeros++;
   }
   return values;
  });
  const digest=binaryRowsHash(rows);
  equal(digest,packet.delta_float64le_sha256,'complete checkpoint binary64 words');
  equal(entry,entries[name],'complete raw direction manifest entry');
  equal(entry.shape,[count,224],'complete raw direction dimensions');
  equal(entry.finite,count*224,'complete finite direction count');
  equal(entry.negative_zero,negativeZeros,'complete direction negative-zero count');
  const raw=fs.readFileSync(rawDescriptor.path);
  if(raw.length!==count*224*8||raw.length!==rawDescriptor.bytes||
     sha(raw)!==rawDescriptor.sha256||sha(raw)!==entry.sha256||sha(raw)!==digest)
   throw Error('Complete raw direction and checkpoint bytes differ');
  return {rows,digest,negativeZeros};
 }
 const fullDirection=decode(full,'complete-native-direct-LD-f64-J1372-shooting-direction-v1',
  depth+1,false,direction.step_delta,'complete-step-coordinate-delta',
  spec.direction.raw_complete_step_direction);
 const restricted=decode(checkpoint,'complete-original-node-restriction-of-direct-LD-f64-J1372-direction-v1',
  577,true,direction.restricted_old_node_delta,'complete-old-node-restricted-delta',
  spec.direction.raw_restricted_direction);
 equal(binaryRowsHash(mapping.map(n=>fullDirection.rows[n])),restricted.digest,
  'all577 rows are the bitwise restriction of the complete new-system direction');
 equal(restricted.digest,spec.direction.delta_float64le_sha256,'bound restricted direction bits');
 equal(fullDirection.digest,spec.direction.complete_step_delta_float64le_sha256,'bound full direction bits');
 equal(restricted.negativeZeros,spec.direction.restored_negative_zero_count,'restricted signed-zero count');
 equal(fullDirection.negativeZeros,spec.direction.complete_step_negative_zero_count,'full signed-zero count');
 equal(direction.step_direction_checkpoint.sha256,spec.direction.inputs.full_direction_checkpoint.sha256,
  'full checkpoint file pin');
 equal(direction.step_direction_checkpoint.bytes,spec.direction.inputs.full_direction_checkpoint.bytes,
  'full checkpoint file size');
 equal(spec.direction.full_step_capture_and_original28_raw_identity_reconstructed,true,
  'all step/oldJ provenance was verified by the frozen Python finite-array binder');
 // No old-long or new-step linear norm is used as an additional trial gate.
 return restricted.rows;
}


let installedContext=false;
function installTrialReplayContext(dn,zero,cfg,request,seed,before){
 if(installedContext||globalThis[Symbol.for(REPLAY_KEY)])throw Error('Install exactly one replay context');
 const started=Date.now(),captured={};
 for(const [key,record] of Object.entries(spec.capture.inputs))captured[key]=readVerified(record);
 const originalResult=captured.result,originalSummary=captured.capture_summary,originalManifest=captured.capture_manifest;
 equal(originalResult.source_sha256,'0b49f14218e4d62f0b18d77dd3fa8aee1cb6225f84d92bb81dace173cf74dcc0',
  'actual28 capture source');
 equal(originalResult.hook_sha256,'b20aee4da9b9dd927a2d78c6691739508798c81e73501b31e14a43ad55b64d30',
  'actual28 capture hook');
 if(originalResult.diagnostic_complete!==true||originalResult.planned_diagnostic_stop_observed!==true||
    originalResult.trials_executed!==0||originalResult.original_native_requests!==1||
    originalSummary.capture_completed!==true||captured.capture_begin.original_evaluate_completed!==true||
    captured.capture_begin.all_original_withJac_stage_guards_returned!==true)
  throw Error('Reuse only the completed original actual28 withJac baseline');
 equal(captured.core_instrumentation.original_core_file_sha256,coreSHA,'actual28 original core');
 equal(captured.core_instrumentation.original_runtime_core_sha256,spec.capture.original_runtime_core_sha256,
  'actual28 original runtime core');
 equal(captured.capture_spec.fresh_request,request,'actual28 original full physical H request');
 equal(captured.capture_spec.numerical_configuration,mathematical(cfg),'same original complete configuration');
 equal(numericalSources(captured.capture_spec.original_source_sha256),numericalSources(spec.original_source_sha256),
  'actual28 original consumed sources');
 equal(captured.original_live_identity_before_seed,before,'original exported methods and all graph/layout identities');
 const arrays=Object.fromEntries(originalManifest.arrays.map(row=>[row.name,row.raw_sha256]));
 equal(arrays,spec.capture.array_sha256,'all retained original raw-array hashes');
 for(const [key,digest] of [['base-states',candidateSHA],['physical-height',heightSHA],
  ['original-scales',scaleSHA],['original-far-graph',farSHA]])equal(arrays[key],digest,'captured '+key);
 const base={};
 for(const [key,label] of [['norm','original_norm'],['minA','original_minA'],['minD','original_minD']]){
  equal(spec.capture.baseline[key],originalSummary[label],'actual cached '+key);
  equal(originalSummary[label],captured.capture_begin[label],'actual begin/finish '+key);
  base[key]=exactNumber(originalSummary[label],label);
 }
 const direction=readVerified(spec.direction.inputs.result),checkpoint=readVerified(spec.direction.inputs.direction_checkpoint),
  manifest=readVerified(spec.direction.inputs.array_manifest);
 equal(spec.direction.inputs.result.sha256,spec.direction.result_sha256,'explicit actual direction result pin');
 equal(direction.restricted_direction_checkpoint.sha256,spec.direction.inputs.direction_checkpoint.sha256,'complete direction packet pin');
 equal(direction.restricted_direction_checkpoint.bytes,spec.direction.inputs.direction_checkpoint.bytes,'complete direction packet size');
 equal(direction.array_manifest.sha256,spec.direction.inputs.array_manifest.sha256,'complete direction manifest pin');
 equal(direction.array_manifest.bytes,spec.direction.inputs.array_manifest.bytes,'complete direction manifest size');
 const delta=checkDirection(direction,checkpoint,manifest);
 const trials=[];let baselineCalls=0,directionCalls=0,finished=false,activeStates,activeTarget,activeScales;
 const provenance={schema:'original-native-direct-LD1372-trial-replay-summary-v1',spec_sha256:specSHA,
  source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),capture_result_sha256:captureResultSHA,
  capture_summary_sha256:captureSummarySHA,capture_manifest_sha256:captureManifestSHA,
  direction_result_sha256:spec.direction.result_sha256,direction_float64le_sha256:binaryRowsHash(delta),
  actual_step_result_sha256:spec.direction.step_result_sha256,
  actual_direct_result_sha256:spec.direction.direct_result_sha256,
  target_is_new_original_coordinate_f64_J:true,original41_matrix_claimed_solved:false,
  new_matrix_identity_sha256:spec.direction.new_matrix_identity_sha256,
  direction_is_original_node_restriction_of_actual_step_system:true,
  original576_long_matrix_claimed_solved:false,old_long_J_defect_used_as_gate:false,
  original_base_float64le_sha256:candidateSHA,original_height_float64le_sha256:heightSHA,
  original_scales_float64le_sha256:scaleSHA,original_far_graph_float64le_sha256:farSHA,
  cached_original_withJac_baseline:spec.capture.baseline,baseline_is_cached_from_actual28:true,
  new_baseline_evaluations:0,new_J_evaluations:0,new_corrections:0,
  original_trial_loop_and_guard_and_merit_retained:true,
  original_graphs_gains_far_scales_and_tolerances_retained:true,
  native_accepted:false,endpoint_J_computed:false,fresh_endpoint_audit_computed:false,task_completed:false};
 const diagnosticView=value=>{
  const out={};for(const [key,x] of Object.entries(value))out[key]=typeof x==='number'&&!Number.isFinite(x)?null:x;
  out.number_bits={};for(const key of ['step','baseNorm','trialNorm'])if(typeof value[key]==='number')
   out.number_bits[key]=numberRecord(value[key]);
  return out;
 };
 function verifyBase({states,target,scales,it,M,K,depth}){
  equal([it,M,K,depth],[0,112,224,576],'only the first original line search');
  equal(binaryRowsHash(states),candidateSHA,'same complete native base state bits');
  equal(binaryRowsHash([target]),arrays['cut-target'],'same original target bits');
  equal(binaryRowsHash([scales]),scaleSHA,'same original residual-scale bits');
  equal(verifiedOriginalSnapshot(dn),before,'original exported methods, graphs, gains and stage layout retained');
 }
 function observeTrial(d,y){
  if(finished||d.iteration!==0||d.trial!==trials.length||d.trial<0||d.trial>=10||
     !Object.is(d.step,2**(-d.trial))||!Object.is(d.baseNorm,base.norm))
   throw Error('Observe the same first original ten-alpha trial sequence');
  const record=diagnosticView(d);
  if(y!==null&&y!==undefined){
   if(y.length!==224)throw Error('Original reported rejected-stage input has the wrong shape');
   record.actual_rejected_stage_input=writeBinaryGzip('trial-'+String(d.trial).padStart(2,'0')+'-stage-input.f64le.gz',[y]);
   record.actual_rejected_stage_node=d.stage===undefined?null:d.stage+1;
  }
  trials.push(record);
  fs.appendFileSync(path.join(spec.output,'trial-replay-records.jsonl'),encode(record));
 }
 function finishSummary(extra){
  if(finished)throw Error('A replay summary may be finalized only once');
  finished=true;
  return writeJSON('trial-replay-summary.json',{...provenance,...extra,trials,
   original_no_J_trial_evaluations:extra.replay_completed===true?trials.length:null,
   observed_complete_original_trial_callbacks:trials.length,
   partial_execution_call_count_not_inferred:extra.replay_completed!==true,
   baseline_reuse_calls:baselineCalls,saved_direction_calls:directionCalls,
   elapsed_seconds:(Date.now()-started)/1000});
 }
 const context={
  baseline(args){
   if(baselineCalls++!==0)throw Error('Do not run a second Newton iteration in trial replay');
   verifyBase(args);activeStates=args.states;activeTarget=args.target;activeScales=args.scales;
   if(args.opts.tolerance!==cfg.solveTolerance||args.opts.maxIterations!==cfg.maxIterations)
    throw Error('Retain the original native tolerance and iteration setting');
   const prior=args.opts.trialDiagnostic;
   args.opts.trialDiagnostic=function(d,y){const value=prior?.call(this,d,y);observeTrial(d,y);return value;};
   writeJSON('baseline-reuse.json',{...provenance,original_evaluate_not_called_for_this_baseline:true,
    cached_from_public_run:'43611175099',same_base_target_scales_and_sources_verified:true,
    original_tol:args.opts.tolerance,original_max_iterations:args.opts.maxIterations,
    actual_loaded_core_instrumentation_sha256:fileSHA(path.join(spec.output,'core-instrumentation.json'))});
   return {...base,baseline_is_cached_from_actual28:true};
  },
  direction(args){
   if(directionCalls++!==0||baselineCalls!==1||args.states!==activeStates||args.target!==activeTarget||
      args.scales!==activeScales||args.it!==0)throw Error('Use the same complete saved direction once');
   equal(binaryRowsHash(delta),spec.direction.delta_float64le_sha256,'unchanged saved direction bits');
   // No Riccati chart was computed for this saved step-system direction. Do not attach the
   // old chart condition, the full-system condition, or an invented estimate.
   return {delta,maxChartCondition:null};
  },
  finish(args){
   if(baselineCalls!==1||directionCalls!==1||args.it!==0||args.target!==activeTarget||args.scales!==activeScales)
    throw Error('Stop only after the one original bound line search');
   const accepted=trials.filter(row=>row.kind==='accepted');
   if(args.accepted){
    if(accepted.length!==1||trials.at(-1)!==accepted[0]||!Number.isFinite(accepted[0].trialNorm)||
       !(accepted[0].trialNorm<base.norm))throw Error('The unchanged original trial must select this state');
    const raw=writeBinaryGzip('selected-state.f64le.gz',args.states);
    const packet=writeGzip('selected-state-checkpoint.json.gz',{
     schema:'original-native-one-trial-selected-state-v1',source_sha256:spec.source_sha256,
     hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,direction_result_sha256:spec.direction.result_sha256,
     capture_result_sha256:captureResultSHA,original_base_float64le_sha256:candidateSHA,
     actual_step_result_sha256:spec.direction.step_result_sha256,
     actual_direct_result_sha256:spec.direction.direct_result_sha256,
     original41_matrix_claimed_solved:false,
     new_matrix_identity_sha256:spec.direction.new_matrix_identity_sha256,
     selected_using_original_node_restriction_of_actual_step_direction:true,
     direction_float64le_sha256:spec.direction.delta_float64le_sha256,
     selected_state_float64le_sha256:raw.raw_sha256,states_binary:raw,rows:stateRows(args.states),
     rawNode:Array.from(dn.tail.rawNode),parameters:mathematical(dn.tail.parameters),cutHeight:request.height,
     trial:accepted[0],selected_by_original_strict_norm_decrease:true,
     success:false,converged:false,native_tail_response:false,
     endpoint_J_computed:false,fresh_endpoint_audit_computed:false,task_completed:false});
    finishSummary({replay_completed:true,trial_accepted:true,selected_state:packet,selected_state_binary:raw,
     expected_original_failure:'Error: '+STOP,planned_accepted_trial_stop:true,
     next_Newton_iteration_not_run:true,complete_native_response_not_returned:true});
    throw Error(STOP);
   }
   if(accepted.length!==0||trials.length!==10)throw Error('Original exhaustion must contain all ten rejected trials');
   finishSummary({replay_completed:true,trial_accepted:false,selected_state:null,
    expected_original_failure:'Error: multiple-shooting line search failed at '+args.ev.norm,
    original_all_trials_rejected_failure_preserved:true});
   // Return to the original, byte-for-byte unchanged failure statement.
  }
 };
 process.once('exit',()=>{
  if(!finished){try{finishSummary({replay_completed:false,trial_accepted:false,
   partial_record_only:true,observed_complete_trial_callbacks:trials.length});}catch(_error){}}
 });
 globalThis[Symbol.for(REPLAY_KEY)]=context;installedContext=true;
 writeJSON('trial-direction-binding.json',{...provenance,capture_inputs:spec.capture.inputs,direction_inputs:spec.direction.inputs,
  complete_original_coordinate_direction_restored:true,
  new_system_complete_direction_and_restriction_bound:true,
  actual_public_and_internal_solve_identity_file:'actual-replay-method-identities.json',
  direction_negative_zero_count:spec.direction.restored_negative_zero_count,
  no_extra_residual_threshold:true,original_strict_merit_test_required:true});
}

const replayReplacements=[
 {before:'const ev=evaluate(states,target,true,scales);',
  after:'const ev=globalThis[Symbol.for("visible-flex.native-direct-LD1372-trial-replay.v1")].baseline({states,target,scales,it,M,K,depth,opts});'},
 {before:'const cor=correction(ev,states,target);',
  after:'const cor=globalThis[Symbol.for("visible-flex.native-direct-LD1372-trial-replay.v1")].direction({ev,states,target,scales,it,M,K,depth});'}
];
const replayFinishAnchor='   if(!accepted)throw new Error("multiple-shooting line search failed at "+ev.norm);';
const replayFinishCode='   globalThis[Symbol.for("visible-flex.native-direct-LD1372-trial-replay.v1")].finish({states,accepted,ev,cor,target,scales,it,M,K,depth});\n';
let engineLoadCount=0;
function transformEngine(loaded){
 if(engineLoadCount++!==0)throw Error('Only one frozen original engine load is permitted');
 const source=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 if(sha(source)!==engineSHA)throw Error('The original stored/recovery engine source changed');
 const anchor="const coreURL='data:text/javascript;base64,'+Buffer.from(redirect(core)).toString('base64');";
 if(source.split(anchor).length!==2)throw Error('Unique frozen engine compile anchor required');
 const program=[
  'const nativeReplayOriginalCore=core;',
  'if(sha256(originalCore)!=='+JSON.stringify(coreSHA)+')throw Error("Original native core changed");',
  'if(sha256(core)!=='+JSON.stringify(spec.capture.original_runtime_core_sha256)+')throw Error("Use the same actual28 runtime core");',
  'const nativeReplayChanges='+JSON.stringify(replayReplacements)+';',
  'const nativeReplayFinishAnchor='+JSON.stringify(replayFinishAnchor)+';',
  'const nativeReplayFinishCode='+JSON.stringify(replayFinishCode)+';',
  'const nativeReplayLoopStart="   for(let k=0;k<10;k++){";',
  'if(core.split(nativeReplayLoopStart).length!==2||core.split(nativeReplayFinishAnchor).length!==2)',
  ' throw Error("Unique original ten-trial loop and exhausted-line-search anchors required");',
  'const nativeReplayTrialText=core.slice(core.indexOf(nativeReplayLoopStart),core.indexOf(nativeReplayFinishAnchor));',
  'for(const item of nativeReplayChanges){',
  ' if(core.split(item.before).length!==2)throw Error("Unique original first baseline/correction call required");',
  ' core=core.replace(item.before,item.after);',
  '}',
  'core=core.replace(nativeReplayFinishAnchor,nativeReplayFinishCode+nativeReplayFinishAnchor);',
  'let nativeReplayRoundtrip=core;',
  'if(nativeReplayRoundtrip.split(nativeReplayFinishCode).length!==2)throw Error("Unique replay finish observer required");',
  'nativeReplayRoundtrip=nativeReplayRoundtrip.replace(nativeReplayFinishCode,"");',
  'const nativeReplayUnchangedTrialText=nativeReplayRoundtrip.slice(nativeReplayRoundtrip.indexOf(nativeReplayLoopStart),nativeReplayRoundtrip.indexOf(nativeReplayFinishAnchor));',
  'if(nativeReplayUnchangedTrialText!==nativeReplayTrialText)throw Error("Original trial arithmetic/guards/merit changed");',
  'for(const item of [...nativeReplayChanges].reverse()){',
  ' if(nativeReplayRoundtrip.split(item.after).length!==2)throw Error("Unique replay replacement required");',
  ' nativeReplayRoundtrip=nativeReplayRoundtrip.replace(item.after,item.before);',
  '}',
  'if(nativeReplayRoundtrip!==nativeReplayOriginalCore)throw Error("Replay changed source outside its explicit two call replacements and finish observer");',
  'const nativeReplaySolveStart=" function solve(target,opts={}){";',
  'const nativeReplaySolveEnd="\\n return {solve,initial,evaluate";',
  'function nativeReplaySolveSlice(text){',
  ' if(text.split(nativeReplaySolveStart).length!==2||text.split(nativeReplaySolveEnd).length!==2)',
  '  throw Error("Unique original internal solve source boundaries required");',
  ' const first=text.indexOf(nativeReplaySolveStart),last=text.indexOf(nativeReplaySolveEnd);',
  ' if(last<=first)throw Error("Internal solve source boundaries are out of order");',
  ' return text.slice(first,last).trim();',
  '}',
  'const nativeReplayOriginalSolve=nativeReplaySolveSlice(nativeReplayOriginalCore);',
  'const nativeReplayInstrumentedSolve=nativeReplaySolveSlice(core);',
  'let nativeReplayRestoredSolve=nativeReplayInstrumentedSolve;',
  'if(nativeReplayRestoredSolve.split(nativeReplayFinishCode).length!==2)throw Error("Unique internal finish observer required");',
  'nativeReplayRestoredSolve=nativeReplayRestoredSolve.replace(nativeReplayFinishCode,"");',
  'for(const item of [...nativeReplayChanges].reverse()){',
  ' if(nativeReplayRestoredSolve.split(item.after).length!==2)throw Error("Unique internal replay call required");',
  ' nativeReplayRestoredSolve=nativeReplayRestoredSolve.replace(item.after,item.before);',
  '}',
  'if(nativeReplayRestoredSolve!==nativeReplayOriginalSolve)throw Error("Internal solve source reversal differs from original runtime source");',
  'const nativeReplaySolveIdentity={',
  ' schema:"original-native-internal-solve-source-roundtrip-v1",',
  ' instrumented_internal_solve_source_sha256:sha256(nativeReplayInstrumentedSolve),',
  ' original_internal_solve_source_sha256:sha256(nativeReplayOriginalSolve),',
  ' instrumented_internal_solve_source:nativeReplayInstrumentedSolve,',
  ' restored_original_internal_solve_source:nativeReplayRestoredSolve,',
  ' replacements:nativeReplayChanges,finish_anchor:nativeReplayFinishAnchor,finish_insertion:nativeReplayFinishCode,',
  ' exact_internal_source_roundtrip_verified:true,',
  ' source_scope:"trimmed unique internal solve declaration in the actual compiled runtime core",',
  ' distinct_from_public_split_wrapper_Function_toString:true,Function_toString_not_modified:true',
  '};',
  'fs.writeFileSync('+JSON.stringify(path.join(spec.output,'core-instrumentation.json'))+',JSON.stringify({',
  ' schema:"original-native-one-line-search-replay-core-v1",spec_sha256:'+JSON.stringify(specSHA)+',',
  ' hook_sha256:'+JSON.stringify(fileSHA(selfPath))+',original_core_file_sha256:sha256(originalCore),',
  ' original_runtime_core_sha256:sha256(nativeReplayOriginalCore),instrumented_runtime_core_sha256:sha256(core),',
  ' replacements_sha256:sha256(JSON.stringify(nativeReplayChanges)),finish_observer_sha256:sha256(nativeReplayFinishCode),',
  ' exact_two_replacements_and_observer_roundtrip_verified:true,',
  ' internal_solve_source_identity:nativeReplaySolveIdentity,',
  ' original_trial_loop_sha256:sha256(nativeReplayTrialText),',
  ' replay_trial_loop_sha256:sha256(nativeReplayUnchangedTrialText),original_ten_trial_body_byte_identical:true,',
  ' first_withJac_call_replaced_by_bound_actual28_cached_baseline:true,',
  ' first_correction_call_replaced_by_bound_complete_restricted_step_direction:true,',
  ' original_evaluate_false_and_trial_guards_and_strict_norm_test_retained:true,',
  ' original_graphs_gains_far_scales_and_tolerances_retained:true,',
  ' planned_accepted_trial_stop:'+JSON.stringify(STOP)+',next_Newton_iteration_not_run:true,',
  ' native_accepted:false,task_completed:false',
  '},null,2)+"\\n",{flag:"wx"});'
 ].join('\n')+'\n';
 const transformed=source.replace(anchor,program+anchor);
 if(transformed.replace(program,'')!==source)throw Error('Engine loader insertion is not exactly reversible');
 writeJSON('engine-loader-instrumentation.json',{schema:'original-native-trial-replay-engine-loader-v1',
  spec_sha256:specSHA,hook_sha256:fileSHA(selfPath),original_engine_sha256:engineSHA,
  instrumented_engine_sha256:sha(transformed),inserted_program_sha256:sha(program),
  exact_loader_insertion_roundtrip_verified:true,insertion_after_original_identity_checks:true,
  original_disk_sources_and_original_ready_manifest_retained:true,
  separate_loaded_core_call_replacements_recorded:true});
 return {...loaded,source:transformed};
}


registerHooks({load(url,context,nextLoad){
 const loaded=nextLoad(url,context);
 if(url.startsWith('file:')&&path.resolve(fileURLToPath(url))===path.resolve(enginePath))return transformEngine(loaded);
 if(!url.startsWith('file:')||path.resolve(fileURLToPath(url))!==path.resolve(frozenPath))return loaded;
 const source=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 if(sha(source)!==frozenSHA)throw Error('The original frozen mathematical worker changed');
 const outerAnchor="try{\n  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));";
 if(source.split(outerAnchor).length!==2)throw Error('Unique original frozen-worker execution anchor missing');
 const initialAnchor='  let initial,predicted=false;';
 const injection=[
  '',
  '  if(call===1){',
  "   if(last!==null||tangentPredictor!==null)throw Error('The first native seed must not import prior worker prediction state');",
  '   const seedModule=await import('+JSON.stringify(import.meta.url)+');',
  '   const completeSeed=seedModule.restoreBoundCandidate(dn,zero,cfg,{',
  '    storedMetricAdapter:storedGeometry.manifest,stableGraphAdapter:storedEngineManifest,',
  '    endpointJacobianAdapter:adapterManifest,tailJacobian:backendLabel,tailPredictor:predictorLabel},req,call);',
  '   initial=completeSeed.states;predicted=true;',
  "   trace({event:'actual23_base_for_original_line_search_cached_actual28_baseline',call,...completeSeed.diagnostics});",
  '  }'
 ].join('\n');
 const insert=[
  'const nativeSeedInitialAnchor='+JSON.stringify(initialAnchor)+';',
  'if(source.split(nativeSeedInitialAnchor).length!==2)',
  " throw Error('Exactly one original initial declaration is required');",
  'const nativeSeedOriginalSource=source,nativeSeedAt=source.indexOf(nativeSeedInitialAnchor)+nativeSeedInitialAnchor.length;',
  'const nativeSeedInjection='+JSON.stringify(injection)+';',
  'source=source.slice(0,nativeSeedAt)+nativeSeedInjection+source.slice(nativeSeedAt);',
  'if(source.slice(0,nativeSeedAt)+source.slice(nativeSeedAt+nativeSeedInjection.length)!==nativeSeedOriginalSource)',
  " throw Error('Native instrumentation must be insertion-only and exactly reversible');",
  'fs.writeFileSync('+JSON.stringify(path.join(spec.output,'instrumentation.json'))+',JSON.stringify({',
  " schema:'original-native-trial-replay-first-base-assignment-v1',",
  ' hook_sha256:'+JSON.stringify(fileSHA(selfPath))+',spec_sha256:'+JSON.stringify(specSHA)+',',
  ' frozen_worker_sha256:'+JSON.stringify(frozenSHA)+',',
  ' original_compiled_worker_sha256:sha256(nativeSeedOriginalSource),',
  ' instrumented_compiled_worker_sha256:sha256(source),injected_code_sha256:sha256(nativeSeedInjection),',
  ' unchanged_anchor_sha256:sha256(nativeSeedInitialAnchor),exact_insertion_roundtrip_verified:true,',
  ' original_request_loop_retained:true,only_first_initial_assignment_added:true,',
  ' original_worker_request_loop_progress_and_tolerances_retained:true,',
  ' separate_loaded_core_baseline_direction_replacements_recorded:true,',
  " candidate_source:'Actual request23 completed full no-J candidate, restored signed-zero binary identity'",
  "},null,2)+'\\n',{flag:'wx'});"
 ].join('\n')+'\n';
 return {...loaded,source:source.replace(outerAnchor,insert+outerAnchor)};
}});
