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
import {spawn} from 'node:child_process';
import {createInterface} from 'node:readline';
import {loadOriginalIntegrationGrid} from './geometry_20261114_native_rawcell0_step_windows.mjs';
import {createDirectLDLocalAWindow} from './geometry_20261114_native_rawcell0_direct_ld_window.mjs';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('Native rawCell0 original-step science belongs to the public repository Actions');
const specPath=process.env.VISIBLE_FLEX_NATIVE_RAWCELL0_DIRECT_LD_SPEC;
if(!specPath)throw Error('Explicit verified complete native seed specification required');
const selfPath=fileURLToPath(import.meta.url),here=path.dirname(selfPath);
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const fileSHA=p=>sha(fs.readFileSync(p));
const specRaw=fs.readFileSync(specPath),specJSON=specRaw[0]===31&&specRaw[1]===139?zlib.gunzipSync(specRaw):specRaw;
const spec=JSON.parse(specJSON),specSHA=sha(specRaw);
const frozenPath=path.join(here,'tail_frozen_worker.mjs');
const frozenSHA='3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054';
const actual23SHA='aa93fb8afbd0c8ce3ec49859f3bcfae465696654f626ed1678ceb430329ec6ea';
const candidateSHA='6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8';
const heightSHA='c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f';
const scaleSHA='ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc';
const farSHA='395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54';
if(spec.schema!=='original-native-rawcell0-direct-ld-spec-v1'||
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
 const failure={schema:'original-native-rawcell0-direct-ld-launch-or-binding-failure-v1',spec_sha256:specSHA,
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
  if(launch.schema!=='original-native-rawcell0-direct-ld-verified-launch-v1'||
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
  const binding={schema:'original-native-rawcell0-direct-ld-seed-binding-v1',spec_sha256:specSHA,
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
  await runRawCell0DirectLD(dn,zero,cfg,request,states,before,scales,target);
  return {states,diagnostics:{seed_binding:descriptor,
   original_candidate_summary_sha256:actual23SHA,candidate_states_float64le_sha256:candidateSHA,
   original_height_float64le_sha256:heightSHA,original_scales_float64le_sha256:scaleSHA,
   nodes:states.length,shape_dimension:K,restored_negative_zero_count:negativeZeros,
   predicted:true,initial_only:true,original_protocol_J_and_audit_flags_retained:true,
   original_full_solve_not_called:true,requested_original_stages:72}};
 }catch(error){
  if(fs.existsSync(path.join(spec.output,'direct-ld-summary.json')))throw error;
  const stack=String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,
    '<unchanged-in-memory-native-worker>');
  writeJSON('seed-binding-failure.json',{...failure,error:String(error),stack:stack.slice(0,20000),
   stack_truncated:stack.length>20000,elapsed_seconds:(Date.now()-started)/1000});
  throw error;
 }
}

const STOP='VISIBLE_NATIVE_RAWCELL0_DIRECT_LD_COMPLETE_V1';
const windowPath=path.join(here,'geometry_20261114_native_rawcell0_direct_ld_window.mjs');
const windowSHA='1ba3f30702b26aa78b4aceb0b2d3d5d71ea8fa858b114d982ead185330faa5d9';
const captureSHA='ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7';
if(spec.planned_probe_stop!==STOP||spec.window_module_sha256!==windowSHA||fileSHA(windowPath)!==windowSHA||
   spec.capture.inputs.result.sha256!==captureSHA||
   spec.source_sha256!==fileSHA(path.join(here,'geometry_20261114_native_rawcell0_direct_ld_capture.py')))
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

class DirectLDWorker {
 constructor(){
  this.queue=[];this.pending=null;this.closed=false;this.exitCode=null;this.fatal=null;
  const stderr=fs.openSync(path.join(spec.output,'direct-ld-worker-stderr.log'),'wx');
  const command=[spec.python_executable,path.join(here,'geometry_20261114_rawcell0_direct_ld_worker.py'),
   '--out',spec.output,'--spec',specPath];
  this.child=spawn(command[0],command.slice(1),{stdio:['pipe','pipe',stderr]});
  fs.closeSync(stderr);this.command=command;
  this.lines=createInterface({input:this.child.stdout,crlfDelay:Infinity});
  this.lines.on('line',line=>{
   try{const value=JSON.parse(line);
    if(this.pending){const p=this.pending;this.pending=null;p.resolve(value);}else this.queue.push(value);
   }catch(error){this.fail(error);}
  });
  this.child.on('error',error=>this.fail(error));
  this.closedPromise=new Promise(resolve=>this.child.once('close',(code,signal)=>{
   this.closed=true;this.exitCode=code;this.signal=signal;
   if(this.pending){const p=this.pending;this.pending=null;
    p.reject(Error('Direct LD worker closed before its complete response: '+code+' '+signal));}
   resolve({exit_code:code,signal});
  }));
 }
 fail(error){this.fatal=error;if(this.pending){const p=this.pending;this.pending=null;p.reject(error);}}
 next(){
  if(this.queue.length)return Promise.resolve(this.queue.shift());
  if(this.fatal)return Promise.reject(this.fatal);
  if(this.closed)return Promise.reject(Error('Direct LD worker is already closed: '+this.exitCode));
  if(this.pending)throw Error('Only one declared worker response may be awaited');
  return new Promise((resolve,reject)=>{this.pending={resolve,reject};});
 }
 write(raw){return new Promise((resolve,reject)=>this.child.stdin.write(raw,error=>error?reject(error):resolve()));}
 async request(header,payload=[]){
  await this.write(Buffer.from(encode(header)));
  for(const raw of payload)await this.write(raw);
  const response=await this.next();
  if(response.event==='failed'){
   this.failure=response;throw Error('Direct longdouble worker failed: '+response.error);
  }
  return response;
 }
 async ready(){
  const ready=await this.next();
  equal(ready.schema,'native-rawcell0-direct-longdouble-pipe-v1','worker protocol');
  equal(ready.event,'ready','worker ready');
  equal(ready.source_sha256,spec.worker_source_sha256,'actual worker source');
  equal(ready.direct_arithmetic_source_sha256,spec.direct_arithmetic_source_sha256,'frozen actual50 direct function');
  equal(ready.spec_sha256,specSHA,'worker original request binding');
  this.readyRecord=writeJSON('direct-ld-worker-ready.json',ready);
  writeJSON('direct-ld-worker-launch.json',{command:this.command,spec_sha256:specSHA,
   worker_source_sha256:spec.worker_source_sha256,direct_arithmetic_source_sha256:spec.direct_arithmetic_source_sha256,
   one_persistent_worker:true,no_native_or_RHS_call_in_worker:true});
  return ready;
 }
 async finish(count){
  const result=await this.request({op:'finish',completed_steps:count});
  equal(result.event,'finished','worker complete inventory');
  equal(result.completed_steps,count,'worker all complete steps');
  this.child.stdin.end();const closed=await this.closedPromise;
  equal(closed.exit_code,0,'worker normal exit after complete inventory');
  this.summaryRecord=writeJSON('direct-ld-worker-summary.json',{...result,...closed});
  return this.summaryRecord;
 }
 async abort(){
  if(!this.closed){this.child.stdin.destroy();this.child.kill('SIGTERM');}
  return await this.closedPromise;
 }
}

function actual41Path(relative){
 if(typeof relative!=='string'||path.isAbsolute(relative)||relative.split(/[\\/]/).includes('..'))
  throw Error('Bound original input stays in the actual41 immutable extraction');
 return path.join(spec.step_references.directory,relative);
}
function originalObject(descriptor){
 const file=actual41Path(descriptor.file),raw=fs.readFileSync(file);
 if(raw.length!==descriptor.bytes||sha(raw)!==descriptor.sha256)
  throw Error('Changed consumed actual41 metadata: '+descriptor.file);
 const unpacked=raw[0]===31&&raw[1]===139?zlib.gunzipSync(raw):raw;
 if(descriptor.raw_sha256&&(sha(unpacked)!==descriptor.raw_sha256||unpacked.length!==descriptor.raw_bytes))
  throw Error('Changed complete original field packet');
 return JSON.parse(unpacked);
}
function originalArray(entry,shape){
 equal(entry.shape,shape,'complete consumed original array shape');
 equal(entry.dtype,'<f8','complete consumed original array dtype');
 equal(entry.order,'C','complete consumed original array order');
 equal(entry.completed,true,'complete consumed original array');
 const width=shape.slice(1).reduce((a,b)=>a*b,1)*8,blocks=[];
 let cursor=0;const hash=crypto.createHash('sha256');
 for(const [index,row] of entry.chunks.entries()){
  equal(row.array,entry.name,'original chunk array');equal(row.chunk_index,index,'original chunk order');
  equal(row.row_start,cursor,'original complete contiguous rows');
  if(!Number.isInteger(row.row_stop)||row.row_stop<=cursor)throw Error('Original complete row count is required');
  const raw=fs.readFileSync(actual41Path(row.file));
  if(raw.length!==row.bytes||raw.length!==(row.row_stop-cursor)*width||sha(raw)!==row.raw_sha256)
   throw Error('Original consumed array chunk changed');
  blocks.push(raw);hash.update(raw);cursor=row.row_stop;
 }
 equal(cursor,shape[0],'every original row consumed');
 const raw=Buffer.concat(blocks);
 equal(raw.length,entry.total_bytes,'complete original array bytes');
 equal(hash.digest('hex'),entry.raw_sha256,'complete original consumed array SHA');
 return {raw,row(index){
  if(!Number.isInteger(index)||index<0||index>=shape[0])throw Error('Original row index out of range');
  const bytes=raw.subarray(index*width,(index+1)*width),value=new Float64Array(width/8);
  for(let j=0;j<value.length;j++)value[j]=bytes.readDoubleLE(j*8);
  equal(sha(rawBytes(value)),sha(bytes),'signed-zero original row decode');
  return value;
 }};
}
const canonicalSHA=value=>sha(Buffer.from(JSON.stringify(stable(value))));

async function runRawCell0DirectLD(dn,zero,cfg,request,states,before,scales,target){
 const started=Date.now(),arrays=[],writers=[],metadataPackets=[],reports=[],completed=[];
 const selected=Array.from({length:72},(_,n)=>n),large=path.join(spec.output,'large-arrays');
 fs.mkdirSync(large,{recursive:false});
 const ledgerPath=path.join(spec.output,'large-array-chunks.jsonl');
 fs.writeFileSync(ledgerPath,'',{flag:'wx'});
 let localBlocks=0,fieldCalls=0,fieldEntries=0,worker=null,workerSummary=null;
 let phase={name:'binding'},success=false,manifest=null,active=null,lastField=null,activeRawA=[];
 const base={schema:'native-rawcell0-saved-step-direct-longdouble-summary-v1',
  spec_sha256:specSHA,source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
  window_module_sha256:windowSHA,worker_source_sha256:spec.worker_source_sha256,
  direct_arithmetic_source_sha256:spec.direct_arithmetic_source_sha256,
  original_capture_result_sha256:captureSHA,capture_result_sha256:captureSHA,
  actual41_result_sha256:spec.actual41_result_sha256,
  original_candidate_float64le_sha256:candidateSHA,
  original_height_float64le_sha256:heightSHA,original_scales_float64le_sha256:scaleSHA,
  original_far_graph_float64le_sha256:farSHA,selected_stages:selected,
  original_steps:12,original_native_solve_called:false,new_whole_tail_J_evaluations:0,
  new_original_long_J_evaluations:0,no_J_evaluations:0,nonlinear_trials:0,
  endpoint_J_or_audit_computed:false,additional_ODE_steps:0,
  target_is_new_original_coordinate_binary64_J:true,
  original1372_base_residuals_boundaries_scales_and_old_to_new_not_recomputed:true,
  no_node_gauge_shadow_formed:true,native_accepted:false,task_completed:false};
 function streamArray(name,tailShape,role){
  const width=tailShape.reduce((a,b)=>a*b,1),hash=crypto.createHash('sha256');
  const entry={name,dtype:'<f8',order:'C',shape:[0,...tailShape],total_bytes:0,
   raw_sha256:null,completed:false,chunks:[],role};
  if(arrays.some(row=>row.name===name))throw Error('Unique direct-LD array name required');
  arrays.push(entry);let closed=false,rows=0;
  const writer={entry,get rows(){return rows;},appendFile(descriptor){
   if(closed)throw Error('Cannot append to a completed direct-LD array');
   equal(descriptor.shape,[1,...tailShape],'worker complete binary chunk shape');
   equal(descriptor.dtype,'<f8','worker final target dtype');equal(descriptor.order,'C','worker array order');
   const relative=descriptor.file;
   if(!relative.startsWith('large-arrays/')||path.isAbsolute(relative)||relative.split(/[\\/]/).includes('..'))
    throw Error('New worker arrays must stay in the independent output');
   const raw=fs.readFileSync(path.join(spec.output,relative));
   if(raw.length!==width*8||raw.length!==descriptor.bytes||sha(raw)!==descriptor.sha256||
      descriptor.raw_sha256!==descriptor.sha256)throw Error('Worker returned wrong complete binary64 bytes');
   const row={array:name,chunk_index:entry.chunks.length,row_start:rows,row_stop:rows+1,
    file:relative,bytes:raw.length,sha256:sha(raw),raw_sha256:sha(raw)};
   hash.update(raw);entry.chunks.push(row);entry.total_bytes+=raw.length;rows++;entry.shape[0]=rows;
   fs.appendFileSync(ledgerPath,encode(row));return row;
  },finish(ok){if(!closed){entry.raw_sha256=hash.digest('hex');entry.completed=ok;closed=true;}return entry;}};
  writers.push(writer);return writer;
 }
 function gzipPacket(name,value){
  const raw=Buffer.from(encode(value)),packed=zlib.gzipSync(raw,{level:9});
  fs.writeFileSync(path.join(spec.output,name),packed,{flag:'wx'});
  const row={file:name,bytes:packed.length,sha256:sha(packed),raw_bytes:raw.length,
   raw_sha256:sha(raw),encoding:'json-gzip'};metadataPackets.push(row);return row;
 }
 function saveManifest(ok){
  if(manifest)return manifest;
  for(const writer of writers)writer.finish(false);
  manifest=writeJSON('direct-ld-array-manifest.json',{
   ...base,schema:'native-rawcell0-direct-longdouble-output-arrays-v1',
   completed:ok,arrays,metadata_packets:metadataPackets,
   chunk_ledger:{file:'large-array-chunks.jsonl',bytes:fs.statSync(ledgerPath).size,sha256:fileSHA(ledgerPath),
    order:'Actual interleaved completion order; identify chunks by(array,chunk_index)'},
   full_four_A_raw_not_required_for_future_target_byte_readback:true,
   all_four_A_full_hashes_and_source_identities_retained:true,
   failure_step_local_A_raw_preserved_when_available:true,large_arrays_artifact_only:true});
  return manifest;
 }
 function finishStepPacket(partial){
  if(!active||active.packet)return active?.packet??null;
  active.packet=gzipPacket('large-arrays/stage-'+String(active.stage).padStart(3,'0')+'-direct-ld-steps.json.gz',{
   schema:'native-rawcell0-direct-longdouble-step-evidence-v1',original_stage:active.stage,
   completed:!partial,partial,source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
   window_module_sha256:windowSHA,worker_source_sha256:spec.worker_source_sha256,
   spec_sha256:specSHA,steps:active.steps,fields:active.fields,
   full_original_A_raw_reproducible_from_bound_original_sources_and_saved_inputs:true,
   all_four_A_hashes_preserved_without_threshold_or_mode_omission:true});
  return active.packet;
 }
 try{
  if(cfg.steps!==12||dn.tail.parameters.steps!==12)throw Error('Retain original RK12 parameters');
  equal(dn.tail.cells.map((c,n)=>c.rawCell===0?n:null).filter(n=>n!==null),selected,'all original rawCell0 stages');
  equal(binaryRowsHash(states),candidateSHA,'all actual28 original base state bits');
  equal(binaryRowsHash([scales]),scaleSHA,'all original sigma bits');
  const capture={};for(const [name,row] of Object.entries(spec.capture.inputs))capture[name]=readVerified(row);
  equal(capture.result.diagnostic_complete,true,'completed original actual28 capture');
  equal(capture.capture_spec.fresh_request,request,'same original full H request');
  equal(capture.original_live_identity_before_seed,before,'same original complete native identity');
  equal(spec.references.capture_binding.raw_array_sha256,spec.capture.array_sha256,'all actual28 references');
  equal(spec.step_references.actual41_result_sha256,spec.actual41_result_sha256,'actual41 input receipt');
  const originalGrid=await loadOriginalIntegrationGrid({sourceRoot:process.env.VISIBLE_FLEX_SOURCE_ROOT,
   originalSourceSHA256:spec.original_source_sha256});
  writeJSON('original-integration-grid-identity.json',originalGrid.identity);
  writeJSON('direct-ld-binding.json',{...base,capture_inputs:spec.capture.inputs,
   references:spec.references,step_references:spec.step_references,original_live_identity:before,
   original_target_float64le_sha256:binaryRowsHash([target]),original_full_H:request.height,
   original_configuration:mathematical(cfg),source_integration_grid:originalGrid.identity,
   no_initialCheckpoint_no_remap_no_threshold:true});
  worker=new DirectLDWorker();const ready=await worker.ready();
  for(const n of selected){
   phase={stage:n,name:'original-identity'};lastField=null;
   const prefix='stage-'+String(n).padStart(3,'0'),reference=spec.references.selected_stages[String(n)],
    oldref=spec.step_references.stages[String(n)],old=originalObject(oldref.report),
    oldWindow=originalObject(oldref.window),fieldPacket=originalObject(oldref.field_packet),cell=dn.tail.cells[n];
   equal(old.stage,n,'original stage report');equal(reference.original_live_stage,before.stages[n],'original live stage');
   const count=old.step_count;
   const full=originalArray(oldref.arrays.full_states,[count+1,226]);
   const outputs=originalArray(oldref.arrays.shape_outputs,[count,224]);
   equal(sha(rawBytes(full.row(0).subarray(0,224))),sha(rawBytes(states[n+1])),'same original stage input');
   equal(fieldPacket.stage,n,'complete original field packet stage');
   equal(fieldPacket.partial,false,'complete original field packet');
   equal(fieldPacket.fields.length,4*count,'all original field records');
   const window=createDirectLDLocalAWindow({engine:cell.engine,cell,sourceTopic:process.env.VISIBLE_FLEX_SOURCE_TOPIC,
    stageIndex:n,originalGrid});
   for(const key of ['stage','rawCell','rawSegment','part','parts','rawLeft','rawRight','mu','original_port_ratio',
      'steps','profiles','profile_function_sha256','original_rhs_with_J_function_sha256','original_flow_function_object_sha256'])
    equal(window.identity[key],oldWindow[key],'original window identity '+key);
   equal(window.identity.parent,oldWindow.source,'literal actual41 original RK source');
   for(const key of ['source_key','source_sha256','function_sha256'])
    equal(originalGrid.identity[key],oldWindow.integration_grid[key],'original grid '+key);
   const identity=writeJSON(prefix+'-direct-ld-window-identity.json',window.identity);
   const J=streamArray(prefix+'-shape-jacobians',[224,224],
    'Once-cast direct-longdouble full original-coordinate local RK map; original Pi port only at original exit');
   const mean=streamArray(prefix+'-mean-jacobians',[2,224],
    'Both original-coordinate mean rows from the same full226 map; never port scaled or shape feedback');
   active={stage:n,steps:[],fields:[],packet:null,identity,arrays:{shape_jacobians:J.entry.name,mean_jacobians:mean.entry.name}};
   let cumulativeMinA=Infinity,cumulativeMinD=Infinity,cumulativeMaxRootRelative=0;
   for(let k=0;k<count;k++){
    const schedule=old.schedule[k],oldFields=fieldPacket.fields.slice(4*k,4*k+4),input=full.row(k),
     expectedOutput=full.row(k+1),expectedShape=outputs.row(k),newFields=[];
    equal(schedule.global_step,k,'all original steps in inner-to-outer order');
    equal(sha(rawBytes(input)),oldFields[0].state_float64le_sha256,'original saved full226 input');
    activeRawA=[];let observedOutput=null,observedShape=null;
    window.run(input,schedule,old.profile_schedules,{
     beforeStep(row){phase={stage:n,original_step:k,name:'four-original-local-A',x:numberRecord(row.x),h:numberRecord(row.h)};},
     beforeField(row){fieldEntries++;lastField={stage:n,original_step:k,field_index:row.field_index,
      x:numberRecord(row.x),h:numberRecord(row.h),state:Float64Array.from(row.state)};},
     afterField(row){
      fieldCalls++;
      const g=row.root.g,geometry={};
      for(const key of Object.keys(g).sort())if(typeof g[key]==='number')geometry[key]=numberRecord(g[key]);
      cumulativeMinA=Math.min(cumulativeMinA,row.root.e.minA);
      cumulativeMinD=Math.min(cumulativeMinD,row.root.e.minD);
      cumulativeMaxRootRelative=Math.max(cumulativeMaxRootRelative,row.root.err/row.root.scale);
      const current={global_step:k,profile_index:row.profile_index,grid_index:row.grid_index,
       grid_branch:row.grid_branch,field_index:row.field_index,x:numberRecord(row.x),h:numberRecord(row.h),
       state_float64le_sha256:sha(rawBytes(row.state)),geometry_number_fields:geometry,
       requested_geometry_keys_present:Object.fromEntries(['r','drdx','w','w2','E'].map(key=>[key,typeof g[key]==='number'])),
       root_minA:numberRecord(row.root.e.minA),root_minD:numberRecord(row.root.e.minD),
       root_error:numberRecord(row.root.err),root_scale:numberRecord(row.root.scale),
       cumulative_minA:numberRecord(cumulativeMinA),cumulative_minD:numberRecord(cumulativeMinD),
       cumulative_maxRootRelative:numberRecord(cumulativeMaxRootRelative)};
      const oldField=oldFields[row.field_index];
      // Identity comparison, not a tolerance on an approximate new numerical field.
      equal(current,oldField,'complete original state/geometry/root/schedule at stage '+n+' step '+k+' field '+row.field_index);
      const raw=Buffer.from(rawBytes(row.jacobian));activeRawA.push(raw);
      const descriptor={field_index:row.field_index,shape:[226,224],dtype:'<f8',order:'C',
       bytes:raw.length,sha256:sha(raw),raw_sha256:sha(raw),
       original_full_state_sha256:oldField.state_float64le_sha256,
       observed_full_state_sha256:current.state_float64le_sha256,
       original_geometry_sha256:canonicalSHA(oldField.geometry_number_fields),
       observed_geometry_sha256:canonicalSHA(current.geometry_number_fields),
       original_field_record_sha256:canonicalSHA(oldField),observed_field_record_sha256:canonicalSHA(current),
       original_RHS_derivative_sha256:sha(rawBytes(row.derivative)),full_original_A_raw_not_persisted:true};
      newFields.push({...current,local_A:descriptor});active.fields.push({...current,local_A:descriptor});
     },
     afterStep(row){
      observedOutput=Float64Array.from(row.state);observedShape=Float64Array.from(row.out);
      equal(numberRecord(row.port_ratio),schedule.port_ratio,'original single exit port bits');
      equal(row.port_applied,schedule.port_applied,'original port location');
      equal(sha(rawBytes(row.state)),sha(rawBytes(expectedOutput)),'original complete226 state output');
      equal(sha(rawBytes(row.out)),sha(rawBytes(expectedShape)),'original post-port shape output');
     }});
    equal(activeRawA.length,4,'all four actual local A');
    const header={op:'step',sequence:localBlocks,stage:n,original_step:k,
     h:schedule.h,port_ratio:schedule.port_ratio,final_original_step:schedule.final_original_step,
     local_A:newFields.map(row=>row.local_A),payload_bytes:4*226*224*8,
     full_input_sha256:sha(rawBytes(input)),actual41_field_record_sha256:oldFields.map(canonicalSHA)};
    phase={stage:n,original_step:k,name:'direct-longdouble-worker'};
    const reply=await worker.request(header,activeRawA);
    equal(reply.event,'step-completed','complete new direct-LD map');
    equal(reply.sequence,localBlocks,'worker completion order');equal(reply.stage,n,'worker original stage');
    equal(reply.original_step,k,'worker original step');equal(reply.local_A,header.local_A,'worker complete original A identities');
    equal(reply.original_h,header.h,'worker same h bits');equal(reply.original_port_ratio,header.port_ratio,'worker same port');
    equal(reply.source_sha256,spec.worker_source_sha256,'same worker byte source');
    const jc=J.appendFile(reply.arrays.shape_jacobians),mc=mean.appendFile(reply.arrays.mean_jacobians);
    const combined=Buffer.concat([fs.readFileSync(path.join(spec.output,jc.file)),fs.readFileSync(path.join(spec.output,mc.file))]);
    equal(sha(combined),reply.full_original_output_sha256,'all226 original-coordinate map rows');
    active.steps.push({original_stage:n,original_step:k,schedule,
     same_original_full_input_bits:true,same_four_field_states_bits:true,
     same_four_geometry_records:true,same_original_h_bits:true,
     original_port_applied_only_at_final_step:true,same_four_root_records:true,
     same_original_full_output_bits:true,same_original_shape_output_bits:true,
     full_input_sha256:sha(rawBytes(input)),full_output_sha256:sha(rawBytes(observedOutput)),
     shape_output_sha256:sha(rawBytes(observedShape)),
     local_A_sha256:newFields.map(row=>row.local_A.sha256),
     four_field_bindings:newFields.map(row=>row.local_A),
     completed_original_field_calls:4,worker_reply:reply,
     target_is_new_original_coordinate_binary64_J:true,
     copied_schedule_shape_J_statistics_are_original_actual41_not_new_target:true});
    localBlocks++;activeRawA=[];lastField=null;
   }
   equal(J.rows,count,'all stage target blocks');equal(mean.rows,count,'all stage mean blocks');
   J.finish(true);mean.finish(true);
   const packet=finishStepPacket(false);
   const report={schema:'native-rawcell0-direct-longdouble-stage-report-v1',
    stage:n,original_stage:n,step_count:count,rawCell:cell.rawCell,rawSegment:cell.rawSegment,part:cell.part,parts:cell.parts,
    actual41_result_sha256:spec.actual41_result_sha256,original_report:oldref.report,
    actual41_full_states_raw_sha256:oldref.arrays.full_states.raw_sha256,
    actual41_shape_outputs_raw_sha256:oldref.arrays.shape_outputs.raw_sha256,
    actual41_field_packet:oldref.field_packet,actual41_window:oldref.window,
    identity,arrays:active.arrays,schedule:old.schedule,profile_schedules:old.profile_schedules,
    schedule_is_verbatim_actual41_including_its_old_J_statistics:true,
    direct_ld_step_reports:packet,completed_original_field_calls:4*count,
    original_sigma:numberRecord(scales[n]),original_port_ratio:numberRecord(cell.portRatio),
    original_full226_inputs_outputs_fields_geometry_and_roots_reproduced_bitwise:true,
    root_identity_scope:'Saved root scalar records e.minA/e.minD/err/scale and cumulative values; no claim about unsaved complete root coefficient arrays',
    all_original_modes_and_both_mean_rows_retained:true,old_binary64_tangent_products_not_recomputed:true,
    full_four_A_hashes_retained:true,only_target_shape_and_mean_arrays_persisted:true,
    original1372_base_residuals_boundaries_and_scales_not_recomputed:true,
    no_changes_to_original_graphs_gains_far_sigma_or_acceptance:true,native_accepted:false};
   const descriptor=writeJSON(prefix+'-direct-ld-completed-report.json',report);
   reports.push(descriptor);completed.push(n);
   fs.appendFileSync(path.join(spec.output,'completed-original-stage-records.jsonl'),encode(descriptor));
   equal(binaryRowsHash(states),candidateSHA,'all original577 node bits unchanged after stage '+n);
   equal(originalSnapshot(dn),before,'original complete functions/graphs/gains/far unchanged');
   active=null;
  }
  workerSummary=await worker.finish(localBlocks);
  const descriptor=saveManifest(true);
  writeJSON('direct-ld-summary.json',{...base,completed:true,capture_completed:true,
   completed_original_stages:completed,total_step_count:localBlocks,completed_local_J_blocks:localBlocks,
   completed_original_RK_field_calls:fieldCalls,original_RK_field_entries:fieldEntries,
   stage_reports:reports,array_manifest:descriptor,direct_ld_worker_summary:workerSummary,
   working_precision:ready.runtime.working_precision,
   all_original_seed_bytes_unchanged:true,original_live_functions_graphs_gains_far_and_scales_unchanged:true,
   original_native_request_intentionally_stopped_before_solve:true,planned_probe_stop:STOP,
   elapsed_seconds:(Date.now()-started)/1000});
  success=true;
 }catch(error){
  const retained=[];
  for(const [index,raw] of activeRawA.entries()){
   const relative='large-arrays/failure-current-step-A'+index+'.f64le';
   fs.writeFileSync(path.join(spec.output,relative),raw,{flag:'wx'});
   retained.push({file:relative,bytes:raw.length,sha256:sha(raw),dtype:'<f8',order:'C',shape:[226,224]});
  }
  let failingInput=null;
  if(lastField){const relative='large-arrays/failure-most-recent-full226-input.f64le',raw=rawBytes(lastField.state);
   fs.writeFileSync(path.join(spec.output,relative),raw,{flag:'wx'});
   const {state:_state,...where}=lastField;
   failingInput={...where,file:relative,bytes:raw.length,sha256:sha(raw),dtype:'<f8',order:'C',shape:[226]};}
  const packet=finishStepPacket(true),descriptor=saveManifest(false);
  const workerExit=worker?await worker.abort():null;
  writeJSON('direct-ld-summary.json',{...base,completed:false,capture_completed:false,
   completed_original_stages:completed,total_step_count:localBlocks,completed_local_J_blocks:localBlocks,
   completed_original_RK_field_calls:fieldCalls,original_RK_field_entries:fieldEntries,
   stage_reports:reports,array_manifest:descriptor,
   partial_current_stage:active?{stage:active.stage,arrays:active.arrays,direct_ld_step_reports:packet}:null,
   actual_failure:{phase,error:String(error),most_recent_field_input:failingInput,
    retained_current_step_local_A:retained,worker_failure:worker?.failure??null,worker_exit:workerExit},
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
  "   trace({event:'actual23_original_inputs_for_original_rawcell0_direct_ld',call,...completeSeed.diagnostics});",
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
  " schema:'original-native-first-request-rawcell0-direct-ld-insertion-v1',",
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

