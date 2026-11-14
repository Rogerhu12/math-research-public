// Diagnostic only: restore the identical actual23 seed, preserve the original
// first withJac and correction arithmetic, capture, then stop before trials.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {fileURLToPath} from 'node:url';
import {registerHooks} from 'node:module';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('This native correction diagnostic belongs to the public repository Actions');
const specPath=process.env.VISIBLE_FLEX_NATIVE_CORRECTION_CAPTURE_SPEC;
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
if(spec.schema!=='native-first-correction-capture-spec-v1'||
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
export function restoreBoundCandidate(dn,zero,cfg,live,request,call){
 const started=Date.now();
 const failure={schema:'native-first-correction-capture-seed-binding-failure-v1',spec_sha256:specSHA,
  hook_sha256:fileSHA(selfPath),original_public_run:spec.original_public_run,
  completed_probe_public_run:spec.completed_probe_public_run,
  candidate_states_float64le_sha256:candidateSHA,seed_is_not_accepted_response:true,
  no_native_success_claimed:true,planned_diagnostic_stop_before_trials:true};
 try{
  if(call!==1||preparedCalls!==0)throw Error('Restore this candidate only for the first original native request');
  preparedCalls++;
  equal(request,spec.fresh_request,'one full original request with fresh J and audit');
  if(request.jacobian!==true||request.audit!==true)throw Error('The complete original J and fresh audit are required');
  const launchPath=path.join(spec.output,'verified-launch-intent.json'),launchRaw=fs.readFileSync(launchPath);
  const launch=JSON.parse(launchRaw);
  if(launch.schema!=='native-first-correction-capture-verified-launch-v1'||
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
  installCaptureContext(dn,zero,cfg,request,states,before);
  const liveRecord=writeJSON('original-live-identity-before-seed.json',before);
  const binding={schema:'native-first-correction-capture-seed-binding-v1',spec_sha256:specSHA,
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
   original_constructor_graphs_and_exported_method_sources_verified:true,
   original_runtime_arithmetic_retained_until_planned_stop:true,all_original_modes_and_nodes_retained:true,
   original_first_withJac_and_correction_follow:true,planned_stop_before_trials:true,final_DN_J_and_audit_not_run:true,no_initialCheckpoint_remesh:true,
   no_height_threshold_or_amplitude_ratio_prediction:true,no_candidate_regeneration:true,
   no_zero_solve:true,task_completed:false,elapsed_seconds:(Date.now()-started)/1000};
  const descriptor=writeJSON('seed-binding.json',binding);
  return {states,diagnostics:{seed_binding:descriptor,
   original_candidate_summary_sha256:actual23SHA,candidate_states_float64le_sha256:candidateSHA,
   original_height_float64le_sha256:heightSHA,original_scales_float64le_sha256:scaleSHA,
   nodes:states.length,shape_dimension:K,restored_negative_zero_count:negativeZeros,
   predicted:true,initial_only:true,original_J_and_audit_requested:true,planned_stop_before_trials:true}};
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
const CAPTURE_KEY='visible-flex.native-first-correction-capture.v1';
const STOP='VISIBLE_NATIVE_CORRECTION_CAPTURE_COMPLETE_V1';
const actual25ResultSHA='f5f4acdb055c6964fd591ac2da566bc581607b1d32ebc8096af557f4a3f8abbf';
if(spec.planned_stop!==STOP||spec.actual25?.inputs?.['result.json']?.sha256!==actual25ResultSHA||
   spec.source_sha256!==fileSHA(path.join(here,'geometry_20261114_native_correction_capture.py')))
 throw Error('Bind the independent capture source and the actual25 failure');
const hostLittleEndian=new Uint8Array(new Uint16Array([1]).buffer)[0]===1;
function f64Bytes(row){
 // All original native vectors are Float64Arrays. Copy their underlying bytes
 // rather than round-tripping through Number or JSON, preserving NaN payloads
 // as well as both signed zeros. The fallback records new diagnostic arrays.
 let bytes;
 if(row instanceof Float64Array)bytes=Buffer.from(row.buffer,row.byteOffset,row.byteLength);
 else{
  bytes=Buffer.allocUnsafe(8*row.length);
  for(let j=0;j<row.length;j++)bytes.writeDoubleLE(row[j],8*j);
  return bytes;
 }
 if(hostLittleEndian)return bytes;
 const little=Buffer.allocUnsafe(bytes.length);
 for(let k=0;k<bytes.length;k+=8)for(let j=0;j<8;j++)little[k+j]=bytes[k+7-j];
 return little;
}
function exactRowsSHA(rows){
 const h=crypto.createHash('sha256');for(const row of rows)h.update(f64Bytes(row));return h.digest('hex');
}
function numberRecord(value){
 const bytes=Buffer.allocUnsafe(8);bytes.writeDoubleLE(value);
 return {value:Number.isFinite(value)?value:null,float64le_hex:bytes.toString('hex'),
  classification:Number.isNaN(value)?'NaN':value===Infinity?'positive-infinity':
   value===-Infinity?'negative-infinity':Object.is(value,-0)?'negative-zero':'finite'};
}
function arrayStats(values){
 let finite=0,nan=0,positiveInfinity=0,negativeInfinity=0,zeros=0,negativeZeros=0,maxAbs=0;
 for(const x of values){
  if(Number.isNaN(x))nan++;
  else if(x===Infinity)positiveInfinity++;
  else if(x===-Infinity)negativeInfinity++;
  else{finite++;maxAbs=Math.max(maxAbs,Math.abs(x));if(x===0){zeros++;if(Object.is(x,-0))negativeZeros++;}}
 }
 return {entries:values.length,finite,nan,positive_infinity:positiveInfinity,negative_infinity:negativeInfinity,
  zeros,negative_zeros:negativeZeros,max_abs_finite:maxAbs};
}
function sumStats(a,b){
 for(const key of ['entries','finite','nan','positive_infinity','negative_infinity','zeros','negative_zeros'])a[key]+=b[key];
 a.max_abs_finite=Math.max(a.max_abs_finite,b.max_abs_finite);
}
function copyF64(source){
 if(!(source instanceof Float64Array))return Float64Array.from(source);
 const result=new Float64Array(source.length);
 new Uint8Array(result.buffer).set(new Uint8Array(source.buffer,source.byteOffset,source.byteLength));
 return result;
}
function appendJSON(name,value){fs.appendFileSync(path.join(spec.output,name),encode(value));}
function maximumTracker(){
 let largest=0,worst=null,nanCount=0,infinityCount=0,firstNonfinite=null;
 return {
  add(value,location){
   if(!Number.isFinite(value)){
    if(firstNonfinite===null)firstNonfinite={...location,value:numberRecord(value)};
    if(Number.isNaN(value))nanCount++;else infinityCount++;
   }
   const absolute=Math.abs(value);
   if(absolute>largest){largest=absolute;worst={...location,value:numberRecord(value)};}
  },
  report(){const maximum=nanCount?NaN:largest;return {
   max_abs:Number.isFinite(maximum)?maximum:null,max_abs_record:numberRecord(maximum),
   worst,first_nonfinite:firstNonfinite,nan_count:nanCount,infinity_count:infinityCount};}
 };
}

let installedContext=false;
function installCaptureContext(dn,zero,cfg,request,seed,before){
 if(installedContext||Object.hasOwn(globalThis,Symbol.for(CAPTURE_KEY)))
  throw Error('Only one complete native correction capture context is permitted');
 installedContext=true;
 // The complete actual25 failure is evidence, never a successful cache entry.
 const oldInputs=spec.actual25.inputs;
 for(const [name,row] of Object.entries(oldInputs)){
  if(path.basename(row.path)!==name||fileSHA(row.path)!==row.sha256||fs.statSync(row.path).size!==row.bytes)
   throw Error('Changed actual25 original failure input: '+name);
 }
 const oldResult=readVerified(oldInputs['result.json']),oldResponse=readVerified(oldInputs['native_0001.json.gz']);
 const oldBinding=readVerified(oldInputs['seed-binding.json']),oldLive=readVerified(oldInputs['original-live-identity-before-seed.json']);
 if(oldResult.success!==false||oldResult.actual_full_J_present!==false||oldResult.actual_audit_present!==false||
    oldResponse.response.failed!=='Error: multiple-shooting line search failed at 0.04177307820740199')
  throw Error('Actual25 must remain the recorded unsuccessful original native solve');
 equal(oldResponse.request,request,'actual25 identical native request');
 equal(mathematical(oldResponse.config),mathematical(cfg),'actual25 original complete numerical config');
 equal(numericalSources(oldResponse.source_sha256),numericalSources(spec.original_source_sha256),
  'actual25 original complete numerical source identities');
 equal(oldBinding.candidate_states_float64le_sha256,candidateSHA,'actual25 identical full seed');
 equal(oldLive,before,'actual25 original graph, method and stage identity');
 const launch=readVerified({path:path.join(spec.output,'verified-launch-intent.json'),
  sha256:fileSHA(path.join(spec.output,'verified-launch-intent.json'))});
 equal(launch.actual25,spec.actual25,'actual25 complete verified input inventory');
 const M=dn.tail.parameters.modes,K=2*M,depth=dn.tail.parameters.depth;
 const largePath=path.join(spec.output,spec.large_array_directory);
 if(spec.large_array_directory!=='large-arrays'||fs.existsSync(largePath))
  throw Error('Use the fresh independent artifact-only large-arrays directory');
 fs.mkdirSync(largePath);
 const arrays=[],stageSummaries=[],began=Date.now();
 let phase='installed-before-original-evaluate',beginCount=0,finishCount=0,
   originalEv=null,originalStates=null,originalTarget=null,originalScales=null,
   maximumChart=null,maximumFiniteCondition=null,manifestWritten=false,summaryWritten=false;
 const manifestBase={schema:'native-first-correction-capture-binary-manifest-v1',
  dtype:'<f8',order:'C',host_little_endian:hostLittleEndian,raw_bits_preserved:true,
  spec_sha256:specSHA,hook_sha256:fileSHA(selfPath),source_sha256:spec.source_sha256,
  original_native_failure_public_run:spec.original_native_failure_public_run,
  original_native_failure_result_sha256:actual25ResultSHA,
  completed_probe_public_run:spec.completed_probe_public_run,candidate_states_float64le_sha256:candidateSHA,
  original_source_sha256:spec.original_source_sha256,actual25_inputs:oldInputs,
  original_far_graph_float64le_sha256:farSHA,original_scales_float64le_sha256:scaleSHA,
  large_arrays_artifact_only:true,native_accepted:false,task_completed:false};
 function saveRows(name,rows,shape,role,chunkRows=8){
  if(!/^[a-z][a-z0-9-]*$/.test(name)||!Array.isArray(rows)||!shape.length||shape[0]!==rows.length)
   throw Error('Invalid native capture array metadata');
  const columns=shape.slice(1).reduce((a,b)=>a*b,1),descriptor={name,shape,dtype:'<f8',order:'C',role,
   completed:false,total_bytes:0,raw_sha256:null,chunks:[],statistics:arrayStats([])};
  arrays.push(descriptor);
  const full=crypto.createHash('sha256');
  for(let first=0,chunkIndex=0;first<rows.length;first+=chunkRows,chunkIndex++){
   const stop=Math.min(rows.length,first+chunkRows),bytes=Buffer.allocUnsafe((stop-first)*columns*8);
   let offset=0;
   for(let j=first;j<stop;j++){
    if(rows[j].length!==columns)throw Error('Original native array shape differs: '+name+' row '+j);
    const raw=f64Bytes(rows[j]);raw.copy(bytes,offset);offset+=raw.length;
    sumStats(descriptor.statistics,arrayStats(rows[j]));
   }
   const filename=name+'-'+String(chunkIndex).padStart(4,'0')+'.f64le',relative='large-arrays/'+filename;
   fs.writeFileSync(path.join(largePath,filename),bytes,{flag:'wx'});
   const row={array:name,file:relative,chunk_index:chunkIndex,row_start:first,row_stop:stop,
    bytes:bytes.length,raw_sha256:sha(bytes)};
   full.update(bytes);descriptor.total_bytes+=bytes.length;descriptor.chunks.push(row);
   // A successfully written chunk remains discoverable even after an abrupt
   // later failure or kill, without waiting for the global final manifest.
   appendJSON('large-array-chunks.jsonl',row);
  }
  descriptor.raw_sha256=full.digest('hex');descriptor.completed=true;
  return descriptor;
 }
 function saveVector(name,values,role){return saveRows(name,[values],[1,values.length],role,1);}
 function writeManifest(completed){
  if(manifestWritten)return null;
  manifestWritten=true;
  return writeJSON('capture-manifest.json',{...manifestBase,completed,phase,arrays,
   backward_stages_observed:stageSummaries.length,elapsed_seconds:(Date.now()-began)/1000});
 }
 function maxChartSummary(){
  if(!maximumChart)return null;
  return {stage:maximumChart.stage,rawCell:dn.tail.cells[maximumChart.stage].rawCell,
   rawSegment:dn.tail.cells[maximumChart.stage].rawSegment,condition:maximumChart.condition,
   norm_G:maximumChart.norm_G,norm_G_inverse:maximumChart.norm_G_inverse,
   original_running_maximum:maximumChart.original_running_maximum,
   selection:'first nonfinite condition if any, otherwise greatest finite observed product',
   largest_finite_condition:maximumFiniteCondition,
   interpretation:'Original local Riccati chart diagnostic; not a full-system condition number or a certified error bound'};
 }
 function saveMaximumChart(){
  if(!maximumChart||maximumChart.saved)return;
  maximumChart.saved=true;
  for(const [name,values] of Object.entries(maximumChart.arrays)){
   const matrix=values.length===M*M;
   saveRows('maximum-chart-'+name,[values],matrix?[1,M,M]:[1,values.length],
    'Original backward recurrence array at recorded chart stage '+maximumChart.stage,1);
  }
 }
 function writePartial(reason){
  if(summaryWritten)return;
  try{saveMaximumChart();}catch(error){appendJSON('capture-preservation-errors.jsonl',{when:'maximum-chart',error:String(error)});}
  const manifest=writeManifest(false);
  summaryWritten=true;
  writeJSON('capture-summary.json',{...manifestBase,capture_completed:false,phase,reason,
   begin_calls:beginCount,finish_calls:finishCount,backward_stages_observed:stageSummaries.length,
   maximum_chart_summary:maxChartSummary(),manifest,original_trials_executed_by_capture:0,
   final_endpoint_J_or_audit_computed:false,elapsed_seconds:(Date.now()-began)/1000});
 }
 process.once('exit',code=>{
  if(beginCount&&!summaryWritten){
   try{writePartial('Process exited before complete correction capture; exit code '+code);}
   catch(error){try{fs.writeSync(2,'Partial capture metadata preservation failed: '+String(error)+'\n');}catch{}}
  }
 });
 function begin({ev,states,target,scales,it,M:actualM,K:actualK,depth:actualDepth}){
  if(beginCount++!==0||it!==0||actualM!==M||actualK!==K||actualDepth!==depth||M!==112||depth!==576)
   throw Error('Capture only the same original first complete native model');
  equal(exactRowsSHA(states),candidateSHA,'original solve copies preserve the full candidate bits');
  equal(exactRowsSHA([target]),exactRowsSHA([seed[0].subarray(0,M)]),'original exact cut target');
  equal(exactRowsSHA([scales]),scaleSHA,'original scaleFor output before correction');
  equal(exactRowsSHA([dn.tail.graphs[depth]]),farSHA,'original far graph before correction');
  if(ev.flows.length!==depth||ev.residuals.length!==depth||ev.end.length!==M)
   throw Error('Keep the complete original native residual/J layout');
  originalEv=ev;originalStates=states;originalTarget=target;originalScales=scales;
  phase='original-first-withJac-complete-before-correction';
  writeJSON('capture-begin.json',{...manifestBase,phase,iteration:it,M,K,depth,
   original_norm:numberRecord(ev.norm),original_minA:numberRecord(ev.minA),original_minD:numberRecord(ev.minD),
   actual25_iteration:spec.actual25.original_last_iteration,
   equals_actual25_norm:ev.norm===spec.actual25.original_last_iteration.norm,
   rawNode:Array.from(dn.tail.rawNode),physical_height_float64le_sha256:exactRowsSHA([request.height]),
   original_evaluate_completed:true,all_original_withJac_stage_guards_returned:true,
   final_endpoint_J_or_audit_computed:false,elapsed_seconds:(Date.now()-began)/1000});
  saveRows('stage-jacobians',ev.flows.map(f=>f.J),[depth,K,K],
   'Original computed withJac cell-flow Jacobians, row-major, including original port conversion',8);
  saveRows('stage-residuals',ev.residuals,[depth,K],'Original computed flow(state[n+1]) minus state[n]',256);
  saveRows('stage-out',ev.flows.map(f=>f.out),[depth,K],'Original computed cell-flow output',256);
  saveRows('base-states',states,[depth+1,K],'Original first solve input after exact signed-zero seed copy',256);
  saveVector('end-residual',ev.end,'Original computed far Robin residual');
  saveVector('cut-target',target,'Original physical H divided by original cut radius to the fourth power');
  saveVector('original-scales',scales,'Original scaleFor using original stored gains, unmodified');
  saveVector('original-far-graph',dn.tail.graphs[depth],'Original far Robin diagonal, unmodified');
  saveVector('physical-height',Float64Array.from(request.height),'All original physical H modes, no threshold');
  const cutResidual=Float64Array.from(target,(_v,j)=>states[0][j]-target[j]);
  saveVector('cut-residual',cutResidual,'Original cut residual subtraction in its original order');
  const guardRows=ev.flows.map(f=>Float64Array.of(f.minA,f.minD,f.meanHeight));
  saveRows('stage-guard-mean',guardRows,[depth,3],
   'Original already-computed per-stage minA, minD, meanHeight; no new flow evaluation',256);
  writeJSON('capture-initial-arrays.json',{...manifestBase,phase,arrays,
   original_correction_has_not_yet_run:true,original_trials_executed_by_capture:0});
  phase='original-backward-correction-running';
 }
 function stage(value){
  const {n,G,H,Gi,gsn,bsn,nextGs,nextBs,t,u,at,maxChartCondition,normG,normGi}=value;
  if(beginCount!==1||finishCount!==0||n!==depth-1-stageSummaries.length)
   throw Error('Observe each original backward stage exactly once in its original order');
  const condition=normG*normGi;
  const summary={stage:n,rawCell:dn.tail.cells[n].rawCell,rawSegment:dn.tail.cells[n].rawSegment,
   norm_G:numberRecord(normG),norm_G_inverse:numberRecord(normGi),condition:numberRecord(condition),
   original_running_maximum:numberRecord(maxChartCondition),
   G:arrayStats(G),H:arrayStats(H),G_inverse:arrayStats(Gi),next_graph:arrayStats(nextGs),
   graph:arrayStats(gsn),next_affine:arrayStats(nextBs),affine:arrayStats(bsn),
   t:arrayStats(t),u:arrayStats(u),graph_times_t:arrayStats(at)};
  appendJSON('chart-stage-summaries.jsonl',summary);stageSummaries.push(summary);
  if(Number.isFinite(condition)&&(!maximumFiniteCondition||condition>maximumFiniteCondition.value))
   maximumFiniteCondition={stage:n,value:condition,float64le_hex:numberRecord(condition).float64le_hex};
  const prefer=maximumChart===null||
   (!Number.isFinite(condition)&&Number.isFinite(maximumChart.numericCondition))||
   (Number.isFinite(condition)&&Number.isFinite(maximumChart.numericCondition)&&condition>maximumChart.numericCondition);
  if(prefer)maximumChart={stage:n,numericCondition:condition,condition:numberRecord(condition),
   norm_G:numberRecord(normG),norm_G_inverse:numberRecord(normGi),original_running_maximum:numberRecord(maxChartCondition),
   arrays:{g:copyF64(G),h:copyF64(H),'g-inverse':copyF64(Gi),'next-graph':copyF64(nextGs),
    graph:copyF64(gsn),'next-affine':copyF64(nextBs),affine:copyF64(bsn),
    t:copyF64(t),u:copyF64(u),'graph-times-t':copyF64(at)},saved:false};
 }
 function finish({ev,states,target,scales,it,M:actualM,K:actualK,depth:actualDepth,cor,matrixVector}){
  if(beginCount!==1||finishCount++!==0||it!==0||actualM!==M||actualK!==K||actualDepth!==depth||
    ev!==originalEv||states!==originalStates||target!==originalTarget||scales!==originalScales||
    stageSummaries.length!==depth)
   throw Error('Capture the one original returned correction of the saved complete model');
  phase='original-correction-returned-before-trials';
  saveRows('original-delta',cor.delta,[depth+1,K],
   'Original correction return, before any trial state or additional flow evaluation',256);
  saveMaximumChart();
  const defects=[],normalized=[],products=[],allMax=maximumTracker(),stageMax=maximumTracker();
  for(let n=0;n<depth;n++){
   const product=matrixVector(ev.flows[n].J,cor.delta[n+1],K),raw=new Float64Array(K),scaled=new Float64Array(K);
   for(let j=0;j<K;j++){
    raw[j]=(product[j]-cor.delta[n][j])+ev.residuals[n][j];scaled[j]=raw[j]/scales[n];
    const where={kind:'stage',stage:n,rawCell:dn.tail.cells[n].rawCell,rawSegment:dn.tail.cells[n].rawSegment,
     residual_row:j,component:j<M?'Q':'Pi',mode:j%M+1,frequency:dn.tail.parameters.spacing*(j%M+1)};
    allMax.add(scaled[j],where);stageMax.add(scaled[j],where);
   }
   products.push(product);defects.push(raw);normalized.push(scaled);
  }
  saveRows('diagnostic-j-delta',products,[depth,K],
   'Diagnostic product using the unchanged original matrixVector arithmetic, not a new flow',256);
  saveRows('linear-stage-defects',defects,[depth,K],
   'Computed diagnostic (J[n]*delta[n+1] - delta[n]) + original residual[n]',256);
  saveRows('scaled-linear-stage-defects',normalized,[depth,K],
   'Each computed stage linear defect divided by its original scale[n]',256);
  const cutBase=Float64Array.from(target,(_v,j)=>states[0][j]-target[j]);
  const cutDefect=new Float64Array(M),cutScaled=new Float64Array(M),farDefect=new Float64Array(M),farScaled=new Float64Array(M);
  const cutMax=maximumTracker(),farMax=maximumTracker();
  for(let j=0;j<M;j++){
   cutDefect[j]=cor.delta[0][j]+cutBase[j];cutScaled[j]=cutDefect[j]/scales[0];
   farDefect[j]=(cor.delta[depth][M+j]-dn.tail.graphs[depth][j]*cor.delta[depth][j])+ev.end[j];
   farScaled[j]=farDefect[j]/scales[depth];
   const cutWhere={kind:'cut',node:0,component:'Q',mode:j+1,frequency:dn.tail.parameters.spacing*(j+1)};
   const farWhere={kind:'far',node:depth,component:'Pi-minus-GQ',mode:j+1,frequency:dn.tail.parameters.spacing*(j+1)};
   cutMax.add(cutScaled[j],cutWhere);farMax.add(farScaled[j],farWhere);
   allMax.add(cutScaled[j],cutWhere);allMax.add(farScaled[j],farWhere);
  }
  saveVector('linear-cut-defects',cutDefect,'delta0Q + original (state0Q - target), preserving cut residual subtraction order');
  saveVector('scaled-linear-cut-defects',cutScaled,'Original cut scale[0]');
  saveVector('linear-far-defects',farDefect,'(deltaDPi - originalGdeep*deltaDQ) + original far residual');
  saveVector('scaled-linear-far-defects',farScaled,'Original far scale[depth]');
  const linearSummary={all_original_rows:allMax.report(),stage_rows:stageMax.report(),
   cut_rows:cutMax.report(),far_rows:farMax.report(),original_base_norm:numberRecord(ev.norm),
   stage_rows_count:depth*K,cut_rows_count:M,far_rows_count:M,
   all_original_scales_retained:true,
   computed_diagnostic_only:true,
   exact_binary_array_algebra_reconstructible_from_saved_bytes:true,
   not_an_exact_DF_certificate:true,
   scope:'This floating diagnostic is not the exact real defect of the stored binary arrays or a validated derivative of the nonlinear map. Raw J/r/delta/scales/boundaries are preserved for independent reconstruction.'};
  phase='complete-planned-stop-before-all-trials';
  const manifest=writeManifest(true);
  summaryWritten=true;
  writeJSON('capture-summary.json',{...manifestBase,capture_completed:true,phase,
   begin_calls:beginCount,finish_calls:finishCount,backward_stages_observed:stageSummaries.length,
   original_norm:numberRecord(ev.norm),original_minA:numberRecord(ev.minA),original_minD:numberRecord(ev.minD),
   original_returned_chart_condition:numberRecord(cor.maxChartCondition),maximum_chart_summary:maxChartSummary(),
   linear_defect_summary:linearSummary,manifest,original_first_withJac_and_correction_completed:true,
   original_trials_executed_by_capture:0,final_endpoint_J_or_audit_computed:false,
   planned_stop:STOP,elapsed_seconds:(Date.now()-began)/1000});
  throw Error(STOP);
 }
 Object.defineProperty(globalThis,Symbol.for(CAPTURE_KEY),{value:Object.freeze({begin,stage,finish}),
  writable:false,configurable:false,enumerable:false});
}

// This is data for insertion-only transformation. Removing each exact added
// fragment recovers the unchanged frozen runtime source byte for byte.
const captureInsertions=[
 {
  "anchor": "cache[n]={Gi,t};",
  "where": "after",
  "code": "\n   globalThis[Symbol.for(\"visible-flex.native-first-correction-capture.v1\")].stage({n,M,K,depth,G,H,Gi,gsn:gs[n],bsn:bs[n],nextGs:gs[n+1],nextBs:bs[n+1],t,u,at,maxChartCondition,normG:infinityNorm(G,M),normGi:infinityNorm(Gi,M)});\n"
 },
 {
  "anchor": "const cor=correction(ev,states,target);",
  "where": "before",
  "code": "globalThis[Symbol.for(\"visible-flex.native-first-correction-capture.v1\")].begin({ev,states,target,scales,it,M,K,depth});\n   "
 },
 {
  "anchor": "const cor=correction(ev,states,target);",
  "where": "after",
  "code": "\n   globalThis[Symbol.for(\"visible-flex.native-first-correction-capture.v1\")].finish({ev,states,target,scales,it,M,K,depth,cor,matrixVector});\n   "
 }
];
let engineLoadCount=0;
function transformEngine(loaded){
 if(engineLoadCount++!==0)throw Error('Only one frozen original engine load is permitted');
 const source=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 if(sha(source)!==engineSHA)throw Error('The original stored/recovery engine source changed');
 const anchor="const coreURL='data:text/javascript;base64,'+Buffer.from(redirect(core)).toString('base64');";
 if(source.split(anchor).length!==2)throw Error('Unique frozen engine compile anchor required');
 const program=[
  'const nativeCaptureOriginalCore=core;',
  'if(sha256(originalCore)!=='+JSON.stringify(coreSHA)+')throw Error("Original native core source changed");',
  'const nativeCaptureInsertions='+JSON.stringify(captureInsertions)+';',
  'for(const item of nativeCaptureInsertions){',
  ' if(core.split(item.anchor).length!==2)throw Error("Unique original correction capture anchor required");',
  ' const at=core.indexOf(item.anchor)+(item.where==="after"?item.anchor.length:0);',
  ' core=core.slice(0,at)+item.code+core.slice(at);',
  '}',
  'let nativeCaptureRoundtrip=core;',
  'for(const item of [...nativeCaptureInsertions].reverse()){',
  ' if(nativeCaptureRoundtrip.split(item.code).length!==2)throw Error("Unique capture fragment required");',
  ' nativeCaptureRoundtrip=nativeCaptureRoundtrip.replace(item.code,"");',
  '}',
  'if(nativeCaptureRoundtrip!==nativeCaptureOriginalCore)throw Error("Capture changed original numerical text");',
  'fs.writeFileSync('+JSON.stringify(path.join(spec.output,'core-instrumentation.json'))+',JSON.stringify({',
  ' schema:"native-first-correction-core-observers-v1",spec_sha256:'+JSON.stringify(specSHA)+',',
  ' hook_sha256:'+JSON.stringify(fileSHA(selfPath))+',original_core_file_sha256:sha256(originalCore),',
  ' original_runtime_core_sha256:sha256(nativeCaptureOriginalCore),instrumented_runtime_core_sha256:sha256(core),',
  ' insertion_sha256:sha256(JSON.stringify(nativeCaptureInsertions)),exact_insertion_roundtrip_verified:true,',
  ' original_evaluate_and_correction_arithmetic_retained:true,',
  ' original_graphs_gains_far_scales_guards_tolerances_retained:true,',
  ' planned_stop:"'+STOP+'",planned_stop_after_original_correction_before_trials:true',
  '},null,2)+"\\n",{flag:"wx"});'
 ].join('\n')+'\n';
 const transformed=source.replace(anchor,program+anchor);
 if(transformed.replace(program,'')!==source)throw Error('Engine observer insertion is not exactly reversible');
 writeJSON('engine-loader-instrumentation.json',{schema:'native-first-correction-engine-loader-v1',
  spec_sha256:specSHA,hook_sha256:fileSHA(selfPath),original_engine_sha256:engineSHA,
  instrumented_engine_sha256:sha(transformed),inserted_program_sha256:sha(program),
  exact_insertion_roundtrip_verified:true,insertion_after_original_identity_checks:true,
  unchanged_disk_source_and_original_ready_manifest:true,
  separate_loaded_instrumentation_recorded:true});
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
  "   trace({event:'actual23_candidate_for_first_correction_capture',call,...completeSeed.diagnostics});",
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
  " schema:'native-first-correction-capture-worker-insertion-v1',",
  ' hook_sha256:'+JSON.stringify(fileSHA(selfPath))+',spec_sha256:'+JSON.stringify(specSHA)+',',
  ' frozen_worker_sha256:'+JSON.stringify(frozenSHA)+',',
  ' original_compiled_worker_sha256:sha256(nativeSeedOriginalSource),',
  ' instrumented_compiled_worker_sha256:sha256(source),injected_code_sha256:sha256(nativeSeedInjection),',
  ' unchanged_anchor_sha256:sha256(nativeSeedInitialAnchor),exact_insertion_roundtrip_verified:true,',
  ' original_request_loop_retained:true,only_first_initial_assignment_added:true,',
  ' original_numerical_operations_before_diagnostic_stop_unchanged:true,planned_stop_after_first_correction:true,',
  " candidate_source:'Actual request23 completed full no-J candidate, restored signed-zero binary identity'",
  "},null,2)+'\\n',{flag:'wx'});"
 ].join('\n')+'\n';
 return {...loaded,source:source.replace(outerAnchor,insert+outerAnchor)};
}});
