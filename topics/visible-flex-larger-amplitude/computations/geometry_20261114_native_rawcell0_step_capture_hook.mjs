// Independent rawCell0 per-original-step capture. Original constructor and
// complete signed-zero seed binding are reused. The state path is unchanged;
// every local variational block starts at identity. Stream every completed
// block, then stop before original native solve, whole-tail J, trial or audit.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {fileURLToPath} from 'node:url';
import {registerHooks} from 'node:module';
import {createNativeRawCell0StepWindows,loadOriginalIntegrationGrid}
 from './geometry_20261114_native_rawcell0_step_windows.mjs';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('Native rawCell0 original-step science belongs to the public repository Actions');
const specPath=process.env.VISIBLE_FLEX_NATIVE_RAWCELL0_STEP_CAPTURE_SPEC;
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
if(spec.schema!=='original-native-rawcell0-step-capture-spec-v1'||
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
 const failure={schema:'original-native-rawcell0-step-capture-launch-or-binding-failure-v1',spec_sha256:specSHA,
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
  if(launch.schema!=='original-native-rawcell0-step-capture-verified-launch-v1'||
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
  const binding={schema:'original-native-rawcell0-step-capture-seed-binding-v1',spec_sha256:specSHA,
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
  await runRawCell0StepCapture(dn,zero,cfg,request,states,before,scales,target);
  return {states,diagnostics:{seed_binding:descriptor,
   original_candidate_summary_sha256:actual23SHA,candidate_states_float64le_sha256:candidateSHA,
   original_height_float64le_sha256:heightSHA,original_scales_float64le_sha256:scaleSHA,
   nodes:states.length,shape_dimension:K,restored_negative_zero_count:negativeZeros,
   predicted:true,initial_only:true,original_protocol_J_and_audit_flags_retained:true,
   original_full_solve_not_called:true,requested_original_stages:72}};
 }catch(error){
  if(fs.existsSync(path.join(spec.output,'rawcell0-step-summary.json')))throw error;
  const stack=String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,
    '<unchanged-in-memory-native-worker>');
  writeJSON('seed-binding-failure.json',{...failure,error:String(error),stack:stack.slice(0,20000),
   stack_truncated:stack.length>20000,elapsed_seconds:(Date.now()-started)/1000});
  throw error;
 }
}

const STOP='VISIBLE_NATIVE_RAWCELL0_STEP_CAPTURE_COMPLETE_V1';
const windowPath=path.join(here,'geometry_20261114_native_rawcell0_step_windows.mjs');
const windowSHA='07dd6101569097a9524c35457c1467002a250911dd049bcb720b3b8c700efd2b';
const captureSHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7';
if(spec.planned_probe_stop!==STOP||spec.window_module_sha256!==windowSHA||fileSHA(windowPath)!==windowSHA||
   spec.capture.inputs.result.sha256!==captureSHA||
   spec.source_sha256!==fileSHA(path.join(here,'geometry_20261114_native_rawcell0_step_capture.py')))
 throw Error('Bind the new rawCell0 capture source, original-step arithmetic and actual28 reference');
equal(spec.selected_stages,Array.from({length:72},(_,n)=>n),'all actual original rawCell0 stages');

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

async function runRawCell0StepCapture(dn,zero,cfg,request,states,before,scales,target){
 const started=Date.now(),arrays=[],writers=[],metadataPackets=[],reports=[],completed=[];
 const selected=Array.from({length:72},(_,n)=>n),large=path.join(spec.output,'large-arrays');
 fs.mkdirSync(large,{recursive:false});
 const ledgerPath=path.join(spec.output,'large-array-chunks.jsonl');
 fs.writeFileSync(ledgerPath,'',{flag:'wx'});
 let localBlocks=0,localEvaluations=0,fieldCalls=0,fieldEntries=0;
 let phase={name:'binding'},success=false,manifest=null;
 let active=null,lastField=null,prospectiveLayout=null;
 const base={schema:'original-native-rawcell0-step-capture-summary-v1',
  spec_sha256:specSHA,source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
  window_module_sha256:windowSHA,original_capture_result_sha256:captureSHA,
  original_candidate_float64le_sha256:candidateSHA,
  original_height_float64le_sha256:heightSHA,original_scales_float64le_sha256:scaleSHA,
  original_far_graph_float64le_sha256:farSHA,selected_stages:selected,
  original_steps:12,original_native_solve_called:false,new_whole_tail_J_evaluations:0,
  new_original_long_J_evaluations:0,no_J_evaluations:0,nonlinear_trials:0,
  endpoint_J_or_audit_computed:false,additional_ODE_steps:0,
  native_accepted:false,task_completed:false};

 // One completed original step is written before the next tangent reset.
 // No whole rawCell0 Jacobian array is retained in memory.
 function streamArray(name,tailShape,role){
  if(!/^[a-z0-9-]+$/.test(name)||arrays.some(a=>a.name===name))
   throw Error('Unique safe streamed array name required');
  const width=tailShape.reduce((a,b)=>a*b,1),hash=crypto.createHash('sha256');
  const entry={name,dtype:'<f8',order:'C',shape:[0,...tailShape],
   total_bytes:0,raw_sha256:null,completed:false,chunks:[],role};
  arrays.push(entry);let closed=false,rows=0;
  const writer={entry,
   get rows(){return rows;},
   append(values,count=1){
    if(closed||!Number.isInteger(count)||count<=0||values.length!==count*width)
     throw Error('Stream complete contiguous binary64 rows');
    const raw=rawBytes(values),index=entry.chunks.length;
    const relative='large-arrays/'+name+'-'+String(index).padStart(6,'0')+'.f64le';
    fs.writeFileSync(path.join(spec.output,relative),raw,{flag:'wx'});
    const descriptor={array:name,chunk_index:index,row_start:rows,row_stop:rows+count,
     file:relative,bytes:raw.length,raw_sha256:sha(raw)};
    hash.update(raw);entry.chunks.push(descriptor);entry.total_bytes+=raw.length;
    rows+=count;entry.shape[0]=rows;
    fs.appendFileSync(ledgerPath,encode(descriptor));
    return descriptor;
   },
   finish(ok){
    if(!closed){entry.raw_sha256=hash.digest('hex');entry.completed=ok;closed=true;}
    return entry;
   }};
  writers.push(writer);return writer;
 }
 function gzipPacket(name,value){
  const raw=Buffer.from(encode(value)),packed=zlib.gzipSync(raw,{level:9});
  fs.writeFileSync(path.join(spec.output,name),packed,{flag:'wx'});
  const row={file:name,bytes:packed.length,sha256:sha(packed),
   raw_bytes:raw.length,raw_sha256:sha(raw),encoding:'json-gzip'};
  metadataPackets.push(row);return row;
 }
 function saveManifest(completedFlag){
  if(manifest!==null)return manifest;
  for(const writer of writers)writer.finish(false);
  manifest=writeJSON('rawcell0-step-array-manifest.json',{
   schema:'original-native-rawcell0-step-arrays-v1',spec_sha256:specSHA,
   source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
   window_module_sha256:windowSHA,dtype:'<f8',order:'C',
   completed:completedFlag,arrays,metadata_packets:metadataPackets,
   chunk_ledger:{file:'large-array-chunks.jsonl',sha256:fileSHA(ledgerPath),
    bytes:fs.statSync(ledgerPath).size,
    order:'Actual interleaved completion order; identify chunks by(array,chunk_index)'},
   all_completed_chunks_retained:true,large_arrays_artifact_only:true,native_accepted:false});
  return manifest;
 }
 function finishFieldPacket(partial){
  if(!active||active.field_packet)return active?.field_packet??null;
  active.field_packet=gzipPacket('large-arrays/stage-'+String(active.stage).padStart(3,'0')+
   '-field-observations.json.gz',{
    schema:'original-native-rawcell0-actual-field-geometry-v1',stage:active.stage,
    spec_sha256:specSHA,source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
    observed_calls:active.fields.length,partial,fields:active.fields,
    source:'Already returned original rhsWithJacobian root.g; no added RHS, root, geometry or J call',
    complete_field_state_values_are_not_reconstructed_from_this_metadata:true});
  return active.field_packet;
 }
 function saveLayout(){
  const lengths=new Map(reports.map(row=>[row.stage,row.step_count]));
  const oldToNew=[],cells=[];let cursor=0;
  for(let n=0;n<576;n++){
   oldToNew.push(cursor);const count=n<72?lengths.get(n):1;
   if(!Number.isInteger(count)||count<=0)throw Error('Use actual completed original-step counts');
   for(let j=0;j<count;j++){
    const k=count-1-j;
    cells.push({newStage:cursor+j,originalStage:n,
     local_flow_step:n<72?k:null,
     shape_J_source:n<72?'actual-original-step-capture':'unchanged-actual28',
     shape_J_array:n<72?'stage-'+String(n).padStart(3,'0')+'-shape-jacobians':null,
     shape_J_row:n<72?k:null,
     port:n<72?(k===count-1?'original':'one'):'original'});
   }
   cursor+=count;
  }
  oldToNew.push(cursor);
  const explicit=new Float64Array(cursor+1);
  for(let n=0;n<=576;n++)explicit[oldToNew[n]]=scales[n];
  for(let n=0;n<576;n++)for(let k=oldToNew[n]+1;k<oldToNew[n+1];k++)explicit[k]=scales[n];
  const writer=streamArray('explicit-step-node-scales',[cursor+1],
   'All old-node sigma bits retained; every inserted node uses its original parent-stage sigma');
  writer.append(explicit);writer.finish(true);
  const nodes=cursor+1,dimension=nodes*224,bandRows=560;
  return writeJSON('prospective-rawcell0-step-layout.json',{
   schema:'original-native-rawcell0-step-layout-v1',originalDepth:576,newDepth:cursor,
   selectedOriginalStages:selected,oldToNew,cells,
   explicit_node_sigma_array:writer.entry.name,old_node_sigma_sha256:scaleSHA,
   inserted_node_sigma_rule:'sigma at original parent stage n, copied as binary64; old node boundaries unchanged',
   flow_order:'inner-to-outer within each original stage',
   shooting_order:'outer-to-inner, reverse actual local flow-step order within original stage',
   ordinary_or_cusp_count_only_from_actual_original_profile_schedule:true,
   resource_estimate:{M:112,K:224,nodes,dimension,lower_bandwidth:112,upper_bandwidth:335,
    LAPACK_band_rows:bandRows,band_bytes:bandRows*dimension*8,
    one_unfactored_band_only:true,possible_LU_copy_bytes:bandRows*dimension*8,
    does_not_include_other_arrays_or_actual_peak_RSS:true},
   not_installed_in_original_dn:true,not_a_solved_new_system:true,
   no_old_long_J_defect_acceptance_gate:true});
 }
 try{
  if(cfg.steps!==12||dn.tail.parameters.steps!==12)throw Error('Keep the original complete RK12 configuration');
  equal(dn.tail.cells.map((c,n)=>c.rawCell===0?n:null).filter(n=>n!==null),selected,
   'exactly the actual original72 rawCell0 stages');
  equal(binaryRowsHash(states),candidateSHA,'complete unchanged original base');
  equal(binaryRowsHash([scales]),scaleSHA,'all unchanged original sigma bits');
  const capture={};for(const [name,row] of Object.entries(spec.capture.inputs))capture[name]=readVerified(row);
  equal(capture.result.diagnostic_complete,true,'completed original actual28 capture');
  equal(capture.capture_spec.fresh_request,request,'same complete original H request');
  equal(capture.original_live_identity_before_seed,before,'same actual original native layout/functions');
  equal(spec.references.capture_binding.raw_array_sha256,spec.capture.array_sha256,
   'all actual28 reference-array identities');
  const originalGrid=await loadOriginalIntegrationGrid({
   sourceRoot:process.env.VISIBLE_FLEX_SOURCE_ROOT,originalSourceSHA256:spec.original_source_sha256});
  writeJSON('original-integration-grid-identity.json',originalGrid.identity);
  writeJSON('rawcell0-step-binding.json',{...base,capture_inputs:spec.capture.inputs,
   references:spec.references,original_live_identity:before,
   original_target_float64le_sha256:binaryRowsHash([target]),
   original_full_H:request.height,original_configuration:mathematical(cfg),
   source_integration_grid:originalGrid.identity,
   no_initialCheckpoint_no_remap_no_threshold:true});
  for(const n of selected){
   phase={stage:n,name:'reference-and-factory'};lastField=null;
   const prefix='stage-'+String(n).padStart(3,'0'),reference=spec.references.selected_stages[String(n)];
   const cell=dn.tail.cells[n];
   equal(reference.original_live_stage,before.stages[n],'same original selected stage '+n);
   const originalInput=readRaw(reference.input,[224]),
    originalOutput=readRaw(reference.output,[224]),
    originalGuardMean=readRaw(reference['guard-mean'],[3]);
   equal(binaryRowsHash([originalInput]),binaryRowsHash([states[n+1]]),
    'complete unchanged original stage input '+n);
   const fullInput=new Float64Array(226);fullInput.set(states[n+1]);
   const windows=createNativeRawCell0StepWindows({engine:cell.engine,cell,
    sourceTopic:process.env.VISIBLE_FLEX_SOURCE_TOPIC,stageIndex:n,originalGrid,steps:12});
   const identity=writeJSON(prefix+'-step-window-identity.json',windows.identity);
   const fullStates=streamArray(prefix+'-full-states',[226],
    'All original226 state words, initial input then each completed original step; no port applied');
   const shapeOutputs=streamArray(prefix+'-shape-outputs',[224],
    'Local original shape output; original Pi port only on the final step of the original stage');
   const shapeJacobians=streamArray(prefix+'-shape-jacobians',[224,224],
    'Each original RK step from identity tangent; original Pi port only on the final step');
   const meanTangents=streamArray(prefix+'-mean-tangent-rows',[2,224],
    'Both actual local variational mean rows, before port; not discarded from the evidence');
   fullStates.append(fullInput);
   active={stage:n,schedule:[],profile_schedules:[],fields:[],field_packet:null,
    arrays:{full_states:fullStates.entry.name,shape_outputs:shapeOutputs.entry.name,
     shape_jacobians:shapeJacobians.entry.name,mean_tangent_rows:meanTangents.entry.name},
    writers:[fullStates,shapeOutputs,shapeJacobians,meanTangents],identity};
   const flow=windows.run(fullInput,{
    profileSchedule(row){
     active.profile_schedules.push({profile_index:row.profile_index,
      grid_branch:row.grid?'integrationGrid':'ordinary',step_count:row.count,
      cuts:Array.from(row.cuts,numberRecord),grid:row.grid?Array.from(row.grid,numberRecord):null,
      ordinary_h:numberRecord(row.ordinaryH),
      ordinary_h_not_reconstructed_from_neighboring_grid_values:true});
    },
    beforeStep(row){
     phase={stage:n,name:'original-step',global_step:row.global_step,
      profile_index:row.profile_index,grid_index:row.grid_index,grid_branch:row.grid_branch,
      x:numberRecord(row.x),h:numberRecord(row.h)};
    },
    beforeField(row){
     fieldEntries++;
     phase={stage:n,name:'original-RK-field',global_step:row.global_step,
      profile_index:row.profile_index,grid_index:row.grid_index,grid_branch:row.grid_branch,
      field_index:row.field_index,x:numberRecord(row.x),h:numberRecord(row.h)};
     lastField={...phase,state:Float64Array.from(row.state)};
    },
    afterField(row){
     fieldCalls++;
     const g=row.root.g,fields={};
     for(const key of Object.keys(g).sort())if(typeof g[key]==='number')fields[key]=numberRecord(g[key]);
     active.fields.push({global_step:row.global_step,profile_index:row.profile_index,
      grid_index:row.grid_index,grid_branch:row.grid_branch,field_index:row.field_index,
      x:numberRecord(row.x),h:numberRecord(row.h),
      state_float64le_sha256:sha(rawBytes(row.state)),geometry_number_fields:fields,
      requested_geometry_keys_present:Object.fromEntries(['r','drdx','w','w2','E'].map(k=>[k,typeof g[k]==='number'])),
      root_minA:numberRecord(row.root.e.minA),root_minD:numberRecord(row.root.e.minD),
      root_error:numberRecord(row.root.err),root_scale:numberRecord(row.root.scale),
      cumulative_minA:numberRecord(row.cumulative.minA),cumulative_minD:numberRecord(row.cumulative.minD),
      cumulative_maxRootRelative:numberRecord(row.cumulative.maxRootRelative)});
    },
    afterStep(row){
     localEvaluations++;
     phase={stage:n,name:'streaming-completed-original-step',global_step:row.global_step,
      profile_index:row.profile_index,grid_index:row.grid_index};
     fullStates.append(row.state);shapeOutputs.append(row.out);
     shapeJacobians.append(row.J);meanTangents.append(row.mean_tangent_rows);
     active.schedule.push({global_step:row.global_step,profile_index:row.profile_index,
      grid_index:row.grid_index,grid_branch:row.grid_branch,
      x:numberRecord(row.x),h:numberRecord(row.h),
      final_original_step:row.final_original_step,port_applied:row.port_applied,
      port_ratio:numberRecord(row.port_ratio),field_calls:row.field_calls,
      full_state_row:row.global_step+1,shape_output_row:row.global_step,
      shape_J_row:row.global_step,shape_J_statistics:arrayStats(row.J),
      cumulative_minA:numberRecord(row.cumulative.minA),cumulative_minD:numberRecord(row.cumulative.minD),
      cumulative_maxRootRelative:numberRecord(row.cumulative.maxRootRelative)});
     localBlocks++;
    }});
   phase={stage:n,name:'completed-original-stage-comparison'};
   const expected=active.profile_schedules.reduce((s,row)=>s+row.step_count,0);
   if(flow.step_count!==expected||active.schedule.length!==expected||
      active.fields.length!==4*expected||fullStates.rows!==expected+1||
      shapeOutputs.rows!==expected||shapeJacobians.rows!==expected||meanTangents.rows!==expected)
    throw Error('Every actual original step, complete state and local tangent must be retained');
   for(const writer of active.writers)writer.finish(true);
   const fieldPacket=finishFieldPacket(false);
   const guardMean=Float64Array.of(flow.minA,flow.minD,flow.meanHeight);
   const report={schema:'original-native-rawcell0-original-stage-steps-v1',
    stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,part:cell.part,parts:cell.parts,
    step_count:flow.step_count,identity,arrays:active.arrays,
    profile_schedules:active.profile_schedules,schedule:active.schedule,
    field_observations:fieldPacket,completed_original_field_calls:active.fields.length,
    original_input_reference:reference.input,original_output_reference:reference.output,
    original_guard_mean_reference:reference['guard-mean'],
    original_sigma:numberRecord(scales[n]),original_port_ratio:numberRecord(cell.portRatio),
    withJac_comparison_to_actual28:{output:compareVectors(flow.out,originalOutput,scales[n]),
     minA_minD_meanHeight:compareVectors(guardMean,originalGuardMean)},
    final_mean_state:{first:numberRecord(flow.state[224]),second:numberRecord(flow.state[225]),
     original_sum:numberRecord(flow.meanHeight)},
    original_guards_returned:true,all_actual_original_steps_saved:true,
    complete226_state_kept_between_all_steps:true,mean_not_reset_at_new_nodes:true,
    original_profile_grid_and_x_h_retained:true,original_port_applied_only_at_final_step:true,
    no_product_of_short_J_blocks_formed:true,new_J_is_not_claimed_old_long_J:true,
    no_noJ_flow_or_whole_long_J_reference_recomputed:true,
    numerical_exit_comparisons_are_observations_not_added_acceptance_gates:true,
    native_accepted:false};
   const descriptor=writeJSON(prefix+'-completed-report.json',report);
   reports.push({stage:n,step_count:flow.step_count,descriptor});completed.push(n);
   fs.appendFileSync(path.join(spec.output,'completed-original-stage-records.jsonl'),encode(descriptor));
   equal(binaryRowsHash(states),candidateSHA,'all original node bytes unchanged after original stage '+n);
   equal(originalSnapshot(dn),before,'original functions/graphs/gains/far unchanged after original stage '+n);
   active=null;lastField=null;
  }
  prospectiveLayout=saveLayout();
  const descriptor=saveManifest(true);
  writeJSON('rawcell0-step-summary.json',{...base,capture_completed:true,
   completed_original_stages:completed,total_step_count:localBlocks,
   completed_local_J_blocks:localBlocks,completed_original_RK_field_calls:fieldCalls,
   completed_local_J_evaluations:localEvaluations,original_RK_field_entries:fieldEntries,
   stage_reports:reports.map(row=>row.descriptor),array_manifest:descriptor,
   prospective_layout:prospectiveLayout,
   original_live_functions_graphs_gains_far_and_scales_unchanged:true,
   all_original_seed_bytes_unchanged:true,planned_probe_stop:STOP,
   original_native_request_intentionally_stopped_before_solve:true,
   elapsed_seconds:(Date.now()-started)/1000});
  success=true;
 }catch(error){
  const partialFields=finishFieldPacket(true);
  let failingInput=null;
  if(lastField){
   const w=streamArray('failure-last-original-field-input',[226],
    'Full original state passed to the most recent RK field, including the actually failing call if it threw');
   w.append(lastField.state);w.finish(true);
   const {state:_state,...meta}=lastField;failingInput={...meta,array:w.entry.name};
  }
  const descriptor=saveManifest(false);
  writeJSON('rawcell0-step-summary.json',{...base,capture_completed:false,
   completed_original_stages:completed,total_step_count:localBlocks,
   completed_local_J_blocks:localBlocks,completed_original_RK_field_calls:fieldCalls,
   completed_local_J_evaluations:localEvaluations,original_RK_field_entries:fieldEntries,
   stage_reports:reports.map(row=>row.descriptor),array_manifest:descriptor,
   partial_current_stage:active?{stage:active.stage,arrays:active.arrays,
    schedule:active.schedule,profile_schedules:active.profile_schedules,
    identity:active.identity,field_observations:partialFields}:null,
   actual_failure:{phase,error:String(error),most_recent_field_input:failingInput},
   elapsed_seconds:(Date.now()-started)/1000});
  throw error;
 }
 if(success)throw Error(STOP);
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
  "   trace({event:'actual23_original_inputs_for_original_rawcell0_step_capture',call,...completeSeed.diagnostics});",
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
  " schema:'original-native-first-request-rawcell0-step-capture-insertion-v1',",
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
