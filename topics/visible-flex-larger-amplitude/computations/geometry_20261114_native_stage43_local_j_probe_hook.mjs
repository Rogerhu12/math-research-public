// Independent single original step and four full local-A capture.
// The original constructor and complete signed-zero seed chain are retained.
// One saved full226 input carries both means; the original four state stages
// are replayed once, without preceding steps, solve, trial, or endpoint audit.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {fileURLToPath} from 'node:url';
import {registerHooks} from 'node:module';
import {createStage43Step11Window} from './geometry_20261114_native_stage43_local_j_window.mjs';
import {loadOriginalIntegrationGrid} from './geometry_20261114_native_rawcell0_step_windows.mjs';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('Native rawCell0 original-step science belongs to the public repository Actions');
const specPath=process.env.VISIBLE_FLEX_NATIVE_STAGE43_LOCAL_J_PROBE_SPEC;
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
if(spec.schema!=='original-native-stage43-local-j-capture-spec-v1'||
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
 if(raw.length>=4_900_000)throw Error('Keep individual metadata below the public5MB limit');
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
function originalSnapshot(dn){
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
export async function restoreBoundCandidate(dn,zero,cfg,live,request,call){
 const started=Date.now();
 const failure={schema:'original-native-stage43-local-j-capture-launch-or-binding-failure-v1',spec_sha256:specSHA,
  hook_sha256:fileSHA(selfPath),original_public_run:spec.original_public_run,
  completed_probe_public_run:spec.completed_probe_public_run,
  candidate_states_float64le_sha256:candidateSHA,seed_is_not_accepted_response:true,
  original_native_solve_intentionally_not_called:true,local_probe_only:true};
 try{
  if(call!==1||preparedCalls!==0)throw Error('Restore this candidate only for the first original native request');
  preparedCalls++;
  equal(request,spec.fresh_request,'same original protocol flags; scoped probe intentionally stops before solve');
  if(request.jacobian!==true||request.audit!==true)throw Error('Retain original protocol flags without claiming final J/audit was run');
  const launchPath=path.join(spec.output,'verified-launch-intent.json'),launchRaw=fs.readFileSync(launchPath);
  const launch=JSON.parse(launchRaw);
  if(launch.schema!=='original-native-stage43-local-j-capture-verified-launch-v1'||
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

  const before=originalSnapshot(dn);
  equal(before,oldLive,'complete live functions, graphs, gains, parameters and stage layout');
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
  equal(originalSnapshot(dn),before,'no original function, graph, gain or geometry changed during seed restoration');
  const liveRecord=writeJSON('original-live-identity-before-seed.json',before);
  const binding={schema:'original-native-stage43-local-j-capture-seed-binding-v1',spec_sha256:specSHA,
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
   candidate_restored_only_for_scoped_original_stage_inputs:true,candidate_is_accepted_response:false,
   constructor_and_numerical_methods_verified_unchanged:true,all_original_modes_and_nodes_retained:true,
   original_full_solve_and_J_and_audit_follow:false,local_original_step_capture_only:true,no_initialCheckpoint_remesh:true,
   no_height_threshold_or_amplitude_ratio_prediction:true,no_candidate_regeneration:true,
   no_zero_solve:true,task_completed:false,elapsed_seconds:(Date.now()-started)/1000};
  const descriptor=writeJSON('seed-binding.json',binding);
  await runStage43LocalJProbe(dn,zero,cfg,request,states,before,scales,target);
  return {states,diagnostics:{seed_binding:descriptor,
   original_candidate_summary_sha256:actual23SHA,candidate_states_float64le_sha256:candidateSHA,
   original_height_float64le_sha256:heightSHA,original_scales_float64le_sha256:scaleSHA,
   nodes:states.length,shape_dimension:K,restored_negative_zero_count:negativeZeros,
   predicted:true,initial_only:true,original_protocol_J_and_audit_flags_retained:true,
   original_full_solve_not_called:true,requested_original_stages:1}};
 }catch(error){
  if(fs.existsSync(path.join(spec.output,'stage43-local-j-summary.json')))throw error;
  const stack=String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,
    '<unchanged-in-memory-native-worker>');
  writeJSON('seed-binding-failure.json',{...failure,error:String(error),stack:stack.slice(0,20000),
   stack_truncated:stack.length>20000,elapsed_seconds:(Date.now()-started)/1000});
  throw error;
 }
}

const STOP='VISIBLE_NATIVE_STAGE43_LOCAL_J_PROBE_COMPLETE_V1';
const windowPath=path.join(here,'geometry_20261114_native_stage43_local_j_window.mjs');
const windowSHA='966ddc4946cc63f69260dd1871c2ac31ad0383eb5593f6c3a0b45b0cfcdef5ec';
const captureSHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7';
if(spec.planned_probe_stop!==STOP||spec.window_module_sha256!==windowSHA||fileSHA(windowPath)!==windowSHA||
   spec.capture.inputs.result.sha256!==captureSHA||
   spec.source_sha256!==fileSHA(path.join(here,'geometry_20261114_native_stage43_local_j_probe.py')))
 throw Error('Bind the new rawCell0 capture source, original-step arithmetic and actual28 reference');
equal(spec.selected_stages,[43],'one actual original old43 stage');

function numberRecord(value){
 const raw=Buffer.allocUnsafe(8);raw.writeDoubleLE(value);
 return {value:Number.isFinite(value)?value:null,float64le_hex:raw.toString('hex'),
  classification:Number.isNaN(value)?'NaN':value===Infinity?'positive-infinity':
   value===-Infinity?'negative-infinity':Object.is(value,-0)?'negative-zero':'finite'};
}
function arrayStats(values){
 let finite=0,nan=0,posInf=0,negInf=0,zeros=0,negativeZeros=0,maxAbs=0,maxIndex=0;
 for(let j=0;j<values.length;j++){
  const value=values[j];
  if(Number.isNaN(value))nan++;
  else if(value===Infinity)posInf++;
  else if(value===-Infinity)negInf++;
  else{finite++;if(value===0){zeros++;if(Object.is(value,-0))negativeZeros++;}
   if(Math.abs(value)>maxAbs){maxAbs=Math.abs(value);maxIndex=j;}}
 }
 return {entries:values.length,finite,nan,positive_infinity:posInf,negative_infinity:negInf,
  zeros,negative_zeros:negativeZeros,max_abs_finite:numberRecord(maxAbs),
  max_abs_finite_index:maxIndex,max_abs_finite_entry:numberRecord(values[maxIndex]??0)};
}
const littleEndianHost=new Uint8Array(new Uint16Array([1]).buffer)[0]===1;
function rawBytes(values){
 if(values instanceof Float64Array){
  const direct=Buffer.from(values.buffer,values.byteOffset,values.byteLength);
  if(littleEndianHost)return direct;
  const little=Buffer.from(direct);little.swap64();return little;
 }
 const bytes=Buffer.allocUnsafe(values.length*8);
 for(let j=0;j<values.length;j++)bytes.writeDoubleLE(values[j],j*8);
 return bytes;
}
function readRaw(record,shape){
 equal(record.shape,shape,'bound original reference dimensions');
 equal(record.dtype,'<f8','bound original reference binary format');
 const raw=fs.readFileSync(record.path);
 if(sha(raw)!==record.sha256||raw.length!==record.bytes||raw.length!==shape.reduce((a,b)=>a*b,1)*8)
  throw Error('Changed original stage reference bytes: '+record.path);
 const values=new Float64Array(raw.length/8);
 for(let j=0;j<values.length;j++)values[j]=raw.readDoubleLE(j*8);
 if(sha(rawBytes(values))!==record.sha256)throw Error('Reference binary64 interpretation did not preserve original bits');
 return values;
}
function compareVectors(actual,reference,sigma=null){
 if(actual.length!==reference.length)throw Error('Original-coordinate comparison dimensions differ');
 let mismatches=0,maxDifference=0,maxIndex=0,nonfiniteDifferences=0;const examples=[];
 const actualBytes=rawBytes(actual),referenceBytes=rawBytes(reference);
 for(let j=0;j<actual.length;j++){
  if(actualBytes.readBigUInt64LE(j*8)!==referenceBytes.readBigUInt64LE(j*8)){
   mismatches++;if(examples.length<4)examples.push({column:j,actual:numberRecord(actual[j]),reference:numberRecord(reference[j])});
  }
  const difference=actual[j]-reference[j];
  if(!Number.isFinite(difference))nonfiniteDifferences++;
  else if(Math.abs(difference)>maxDifference){maxDifference=Math.abs(difference);maxIndex=j;}
 }
 return {actual_float64le_sha256:sha(rawBytes(actual)),reference_float64le_sha256:sha(rawBytes(reference)),
  all_bits_equal:mismatches===0,mismatching_entries:mismatches,
  floating_max_abs_difference:numberRecord(maxDifference),floating_max_difference_column:maxIndex,
  floating_max_difference_divided_by_original_sigma:sigma===null?null:numberRecord(maxDifference/sigma),
  original_sigma:sigma===null?null:numberRecord(sigma),nonfinite_differences:nonfiniteDifferences,examples,
  difference_is_diagnostic_not_a_new_scientific_gate:true};
}

async function runStage43LocalJProbe(dn,zero,cfg,request,states,before,scales,target){
 const started=Date.now(),arrays=[],fields=[],localJ=[],inputs=spec.local_reference;
 const large=path.join(spec.output,'large-arrays');fs.mkdirSync(large,{recursive:true});
 let phase={name:'binding'},entries=0,returned=0,stepCount=0,observed=null,lastInput=null;
 let sameState=true,sameGeometry=true,manifest=null,completeComparisons=null;
 const base={schema:'original-native-stage43-local-j-capture-summary-v1',
  spec_sha256:specSHA,source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
  window_module_sha256:windowSHA,original_capture_result_sha256:captureSHA,
  actual41_result_sha256:inputs.actual41_result_sha256,
  actual44_field_receipt_sha256:inputs.actual44_field_receipt_sha256,
  original_candidate_float64le_sha256:candidateSHA,original_height_float64le_sha256:heightSHA,
  original_scales_float64le_sha256:scaleSHA,original_far_graph_float64le_sha256:farSHA,
  original_stage:43,original_flow_step:11,new_shooting_stage:519,new_input_node:520,
  original_steps:12,original_h:inputs.original_schedule.h,
  original_port_ratio:inputs.original_port_ratio,original_sigma:inputs.original_sigma,
  original_native_solve_called:false,new_whole_tail_J_evaluations:0,
  new_original_long_J_evaluations:0,no_J_evaluations:0,nonlinear_trials:0,
  endpoint_J_or_audit_computed:false,additional_ODE_steps:0,
  reference_arrays:inputs.references,
  actual41_did_not_save_the_original_four_local_A_arrays:true,
  current_local_A_are_new_calls_to_the_same_original_function:true,
  same_state_geometry_and_source_are_reproduction_evidence_not_old_A_byte_comparison:true,
  local_cumulative_guards_cover_selected_step_only:true,
  actual41_stage_cumulative_guards_not_claimed_equal:true,
  native_accepted:false,task_completed:false};
 function save(name,values,shape,role){
  if(!/^[a-z0-9-]+$/.test(name)||arrays.some(row=>row.name===name)||
     values.length!==shape.reduce((a,b)=>a*b,1))
   throw Error('Unique complete local-array name and shape required');
  const raw=rawBytes(values),file='large-arrays/'+name+'.f64le';
  fs.writeFileSync(path.join(spec.output,file),raw,{flag:'wx'});
  const row={name,file,bytes:raw.length,sha256:sha(raw),dtype:'<f8',order:'C',
   shape,role,statistics:arrayStats(values)};
  arrays.push(row);return row;
 }
 function saveManifest(complete){
  if(manifest)return manifest;
  manifest=writeJSON('stage43-local-j-array-manifest.json',{
   schema:'original-native-stage43-local-j-arrays-v1',
   source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
   window_module_sha256:windowSHA,spec_sha256:specSHA,completed:complete,
   actual41_result_sha256:inputs.actual41_result_sha256,
   actual44_field_receipt_sha256:inputs.actual44_field_receipt_sha256,
   original_stage:43,original_flow_step:11,arrays,
   complete_binary64_bits_including_negative_zero_retained:true,
   arrays_are_artifact_only:true,native_accepted:false});
  return manifest;
 }
 function summary(complete,error=null){
  const arrayManifest=saveManifest(complete);
  return writeJSON('stage43-local-j-summary.json',{...base,capture_completed:complete,
   completed_original_stages:complete?[43]:[],total_step_count:stepCount,
   completed_local_J_blocks:stepCount,completed_local_J_evaluations:stepCount,
   completed_original_RK_field_calls:returned,original_RK_field_entries:entries,
   returned_pointwise_local_J_matrices:returned,
   completed_local_J_evaluations_role:'Complete short RK blocks, distinct from four pointwise local matrices',
   exactly_one_existing_RK_step_requested:true,preceding_steps_evaluated:0,
   field_reports:fields,local_J_arrays:localJ,observed_step_arrays:observed,
   same_state_path_as_actual41:sameState&&fields.length===4,
   all_four_geometry_records_equal:sameGeometry&&fields.length===4,
   complete_step_comparisons:completeComparisons,stage_reports:[],
   array_manifest:arrayManifest,original_live_functions_graphs_gains_far_and_scales_unchanged:complete,
   all_original_seed_bytes_unchanged:complete,
   planned_probe_stop:complete?STOP:null,
   original_native_request_intentionally_stopped_before_solve:true,
   actual_failure:error?{phase,error:String(error),most_recent_field_input:lastInput}:null,
   elapsed_seconds:(Date.now()-started)/1000});
 }
 try{
  if(cfg.steps!==12||dn.tail.parameters.steps!==12||
     inputs.schema!=='original-stage43-step11-input-references-v1'||
     inputs.actual41_result_sha256!=='6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf'||
     inputs.actual44_field_receipt_sha256!=='d7d00de365b2118e1346e8f8630d5bad408957da91fdf51f38496f73b0e0c5f2')
   throw Error('Keep the exact actual41/44 selected original RK12 identity');
  equal(binaryRowsHash(states),candidateSHA,'complete unchanged original base');
  equal(binaryRowsHash([scales]),scaleSHA,'complete unchanged original scales');
  equal(numberRecord(scales[43]),inputs.original_sigma,'original old43 sigma');
  const capture={};for(const [name,row] of Object.entries(spec.capture.inputs))capture[name]=readVerified(row);
  equal(capture.result.diagnostic_complete,true,'completed actual28 original capture');
  equal(capture.capture_spec.fresh_request,request,'unchanged original complete H request');
  equal(capture.original_live_identity_before_seed,before,'actual28 live constructor identity');
  equal(spec.references.capture_binding.raw_array_sha256,spec.capture.array_sha256,
   'original actual28 complete reference-array identities');
  const old=spec.references.selected_stages['43'];
  equal(old.original_live_stage,before.stages[43],'old43 full source profile closure metadata');
  equal(binaryRowsHash([readRaw(old.input,[224])]),binaryRowsHash([states[44]]),
   'old43 stage input belongs to the unchanged original full seed');

  const copied=readVerified(inputs.inputs.field_receipt);
  equal(copied.inputs.result.sha256,inputs.actual41_result_sha256,'actual41 result in copied receipt');
  equal(copied.complete_original_fields,inputs.original_fields,'all original four field records');
  equal(copied.window_identity,inputs.original_window,'complete original window identity');
  equal(copied.original_step_schedule,inputs.original_schedule,'same original selected x/h schedule');
  for(const [name,row] of Object.entries(inputs.inputs)){
   if(name!=='field_receipt')readVerified(row);
  }
  const refs={};
  for(const [name,row] of Object.entries(inputs.references)){
   refs[name]=readRaw(row,row.shape);
   if(!row.file.startsWith('large-arrays/')||row.path!==path.join(spec.output,row.file))
    throw Error('Selected reference arrays must be immutable copies within this artifact');
   arrays.push({...row,name:'reference-'+name,role:'Bound original actual41 array bytes'});
  }
  if(refs['full-input'].length!==226||refs['full-output'].length!==226||
     refs['short-J'].length!==224*224||refs['mean-tangent-rows'].length!==2*224)
   throw Error('Keep the full original state, complete shape J, and both mean rows');
  equal(sha(rawBytes(refs['full-input'])),inputs.original_fields[0].state_float64le_sha256,
   'same full226 original field0 state');
  const grid=await loadOriginalIntegrationGrid({
   sourceRoot:process.env.VISIBLE_FLEX_SOURCE_ROOT,originalSourceSHA256:spec.original_source_sha256});
  writeJSON('original-integration-grid-identity.json',grid.identity);
  const cell=dn.tail.cells[43];
  const window=createStage43Step11Window({engine:cell.engine,cell,
   sourceTopic:process.env.VISIBLE_FLEX_SOURCE_TOPIC,originalGrid:grid});
  equal(window.identity.profile_function_sha256,inputs.original_window.profile_function_sha256[0],
   'same original actual41 profile function');
  equal(window.identity.original_rhs_with_J_function_sha256,
   inputs.original_window.original_rhs_with_J_function_sha256,'same original full local-J function');
  equal(window.identity.original_flow_function_object_sha256,
   inputs.original_window.original_flow_function_object_sha256,'unchanged original flow function object');
  equal(window.identity.parent,inputs.original_window.source,'same actual41 prepared source body');
  const windowFile=writeJSON('stage43-local-j-window-identity.json',window.identity);
  writeJSON('stage43-local-j-binding.json',{...base,capture_inputs:spec.capture.inputs,
   selected_original_inputs:inputs,original_live_identity:before,window_identity:windowFile,
   full_original_H:request.height,original_configuration:mathematical(cfg),
   original_target_float64le_sha256:binaryRowsHash([target]),
   no_initialCheckpoint_no_remap_no_threshold:true});
  phase={name:'single-original-step'};
  const flow=window.run(refs['full-input'],{
   profileSchedule(row){
    equal(row.profile_index,0,'original single profile index');
    equal(row.cuts,[],'original ordinary branch');
    equal(row.grid,null,'original ordinary grid');
    equal(row.count,12,'original full profile step count');
   },
   beforeStep(row){
    equal(numberRecord(row.x),inputs.original_schedule.x,'exact original step x');
    equal(numberRecord(row.h),inputs.original_schedule.h,'exact original step h');
    equal(sha(rawBytes(row.state)),inputs.references['full-input'].sha256,'no input mean reset');
   },
   beforeField(row){
    entries++;
    phase={name:'original-local-field',field_index:row.field_index,
     original_stage:43,original_flow_step:11,x:numberRecord(row.x),h:numberRecord(row.h)};
    const input=save('field-'+row.field_index+'-state',row.state,[226],
     'Full original complete226 state passed to the actual local RHS/J');
    lastInput={...phase,array:input};
   },
   afterField(row){
    returned++;
    const expected=inputs.original_fields[row.field_index],geometry={};
    for(const key of Object.keys(row.root.g).sort())
     if(typeof row.root.g[key]==='number')geometry[key]=numberRecord(row.root.g[key]);
    const derivative=save('field-'+row.field_index+'-derivative',row.derivative,[226],
      'Actual original returned complete226 RHS without recomputation');
    const A=save('field-'+row.field_index+'-local-jacobian',row.jacobian,[226,224],
      'Actual original returned complete local Jacobian; unported, all modes and mean rows');
    const record={global_step:11,profile_index:0,grid_index:11,grid_branch:'ordinary',
     field_index:row.field_index,x:numberRecord(row.x),h:numberRecord(row.h),
     state_float64le_sha256:sha(rawBytes(row.state)),geometry_number_fields:geometry,
     root_minA:numberRecord(row.root.e.minA),root_minD:numberRecord(row.root.e.minD),
     root_error:numberRecord(row.root.err),root_scale:numberRecord(row.root.scale),
     single_step_cumulative_minA:numberRecord(row.cumulative.minA),
     single_step_cumulative_minD:numberRecord(row.cumulative.minD),
     single_step_cumulative_maxRootRelative:numberRecord(row.cumulative.maxRootRelative),
     arrays:{state:lastInput.array,derivative,local_jacobian:A},
     original_actual41_field:expected};
    record.original_state_bits_equal=record.state_float64le_sha256===expected.state_float64le_sha256;
    record.original_geometry_records_equal=same(record.geometry_number_fields,expected.geometry_number_fields);
    record.original_x_h_records_equal=same(record.x,expected.x)&&same(record.h,expected.h);
    record.original_root_scalar_records_equal=['root_minA','root_minD','root_error','root_scale']
      .every(key=>same(record[key],expected[key]));
    sameState= sameState&&record.original_state_bits_equal;
    sameGeometry=sameGeometry&&record.original_geometry_records_equal&&record.original_x_h_records_equal;
    fields.push(record);localJ.push(A);
    writeJSON('field-'+row.field_index+'-returned-report.json',record);
   },
   afterStep(row){
    stepCount++;
    observed={
     full_input:inputs.references['full-input'],
     full_output:save('observed-full-output',row.state,[226],'Full original one-step state with carried means'),
     shape_output:save('observed-shape-output',row.out,[224],'Original final stored shape after original port'),
     shape_J:save('observed-short-j',row.J,[224,224],'Original floating tangent recurrence and original final port'),
     mean_tangent_rows:save('observed-mean-tangent-rows',row.mean_tangent_rows,[2,224],
      'Both original tangent mean rows, with no port applied')};
    completeComparisons={
     full226_state:compareVectors(row.state,refs['full-output']),
     stored_shape:compareVectors(row.out,refs['shape-output'],scales[43]),
     shape_J:compareVectors(row.J,refs['short-J']),
     mean_tangent_rows:compareVectors(row.mean_tangent_rows,refs['mean-tangent-rows']),
     all_comparisons_are_observations_not_added_native_acceptance_gates:true};
   }});
  if(entries!==4||returned!==4||fields.length!==4||stepCount!==1||
     flow.returned_local_J!==4||flow.selected_steps!==1)
   throw Error('The complete single existing step requires exactly four returned local matrices');
  equal(binaryRowsHash(states),candidateSHA,'all original577 seed nodes unchanged');
  equal(binaryRowsHash([scales]),scaleSHA,'all original scales unchanged');
  equal(originalSnapshot(dn),before,'original functions/graphs/gains/far unchanged after one-step probe');
  summary(true);
 }catch(error){
  summary(false,error);throw error;
 }
 throw Error(STOP);
}


registerHooks({load(url,context,nextLoad){
 const loaded=nextLoad(url,context);
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
  '   const completeSeed=await seedModule.restoreBoundCandidate(dn,zero,cfg,{',
  '    storedMetricAdapter:storedGeometry.manifest,stableGraphAdapter:storedEngineManifest,',
  '    endpointJacobianAdapter:adapterManifest,tailJacobian:backendLabel,tailPredictor:predictorLabel},req,call);',
  '   initial=completeSeed.states;predicted=true;',
  "   trace({event:'actual23_original_inputs_for_original_stage43_local_J_probe',call,...completeSeed.diagnostics});",
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
  " schema:'original-native-first-request-stage43-local-j-capture-insertion-v1',",
  ' hook_sha256:'+JSON.stringify(fileSHA(selfPath))+',spec_sha256:'+JSON.stringify(specSHA)+',',
  ' frozen_worker_sha256:'+JSON.stringify(frozenSHA)+',',
  ' original_compiled_worker_sha256:sha256(nativeSeedOriginalSource),',
  ' instrumented_compiled_worker_sha256:sha256(source),injected_code_sha256:sha256(nativeSeedInjection),',
  ' unchanged_anchor_sha256:sha256(nativeSeedInitialAnchor),exact_insertion_roundtrip_verified:true,',
  ' original_request_loop_retained:true,only_first_scoped_probe_call_added:true,',
  ' original_numerical_sources_and_tolerances_unchanged:true,planned_stop_before_original_solve:true,',
  " candidate_source:'Actual request23 completed full no-J candidate, restored signed-zero binary identity'",
  "},null,2)+'\\n',{flag:'wx'});"
 ].join('\n')+'\n';
 return {...loaded,source:source.replace(outerAnchor,insert+outerAnchor)};
}});
