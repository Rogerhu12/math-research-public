// R493 one real current-H call: original64 capture/R273, persistent128 solve,
// complete same-call components, explicit RN64 protocol. No old solve is invoked.
// Numerical evaluation is permitted only in this public repository Actions.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {writeNativeTraceVariationPacket} from './geometry_20261115_native_trace_variation128_bridge.mjs';
import {writeNativeFinal128PhysicalPacket} from './geometry_20261115_native_final128_packet.mjs';

const selfPath=fileURLToPath(import.meta.url),here=path.dirname(selfPath);
const sha=value=>crypto.createHash('sha256').update(value).digest('hex');
const fileSHA=file=>{const h=crypto.createHash('sha256'),fd=fs.openSync(file,'r'),b=Buffer.allocUnsafe(1<<20);
 try{for(;;){const n=fs.readSync(fd,b,0,b.length,null);if(!n)break;h.update(b.subarray(0,n));}}finally{fs.closeSync(fd);}return h.digest('hex');};
const unpack=raw=>raw[0]===31&&raw[1]===139?zlib.gunzipSync(raw):raw;
if(process.env.GITHUB_ACTIONS!=='true'||
 (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('R493 scientific calls belong only to this public repository Actions');
const specPath=process.env.VISIBLE_FLEX_LIVE128_SPEC;
if(!specPath)throw Error('An explicit real live128 session specification is required');
const specRaw=fs.readFileSync(specPath),spec=JSON.parse(specRaw),specSHA=sha(specRaw);
if(spec.schema!=='R493-current-H-live128-tail-client-spec-v1'||
 spec.hook_sha256!==fileSHA(selfPath)||
 spec.source_sha256!==fileSHA(path.join(here,'geometry_20261116_live128_tail_client.py'))||
 spec.session_origin?.schema!=='R493-current-H-live128-worker-session-v1')
 throw Error('The actual current-H source/specification identity differs');
for(const [name,digest] of Object.entries(spec.frozen_sources)){
 if(path.basename(name)!==name||fileSHA(path.join(here,name))!==digest)
  throw Error('The full explicit original/new source binding differs: '+name);
}
if(Buffer.from(new Float64Array([1]).buffer).toString('hex')!=='000000000000f03f')
 throw Error('The original little-endian binary64 arrays are required');
let installedDN=null,lastCall=0;
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
function captureCurrent(directory,{ev,states,target,scales,it,M,K,depth},ctx,sequence){
 const {call,before}=ctx;
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
  saveArray(directory,'physical-height',[1,112],()=>Float64Array.from(ctx.metadata.request.height)),
  saveArray(directory,'cut-target',[1,112],()=>target),
  saveArray(directory,'stage-jacobians',[576,224,224],n=>ev.flows[n].J),
 ];
 const hashes=Object.fromEntries(arrays.map(a=>[a.name,a.raw_sha256]));
 equal(hashes['physical-height'],ctx.metadata.request_height_float64le_sha256,'actual this-call complete physical H');
 equal(hashes['original-far-graph'],before.far_graph_float64le_sha256,'unchanged original far Robin bits');
 const localInputs=Object.fromEntries(['physical-height','original-scales','original-far-graph','cut-target'].map(name=>[name,hashes[name]]));
 if(ctx.inputHashes===null)ctx.inputHashes=localInputs;
 else equal(localInputs,ctx.inputHashes,'unchanged original H/target/scales within this request');
 const requestRaw=fs.readFileSync(path.join(ctx.directory,'request.json'));
 equal(sha(requestRaw),ctx.requestFile.sha256,'actual complete request receipt');
 fs.writeFileSync(path.join(directory,'request.json'),requestRaw,{flag:'wx'});
 const currentRequest={...ctx.metadata,request_file:receipt(path.join(directory,'request.json'),directory)};
 const flowMetadata=writeJSON(directory,'flow-return-metadata.json.gz',{
  schema:'original-r273-current-native576-original-flow-return-scalars-v1',native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,
  scope:'Read-only original returned meanHeight/minA/minD; no extra flow call or recomputation',
  rows:ev.flows.map((f,n)=>({stage:n,rawCell:before.stages[n].rawCell,rawSegment:before.stages[n].rawSegment,
   meanHeight:numberRecord(f.meanHeight),minA:numberRecord(f.minA),minD:numberRecord(f.minD)}))
 },{compressed:true});
 const manifest=writeJSON(directory,'array-manifest.json',{
  schema:'original-r273-current-native576-withJ-snapshot-arrays-v1',source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
  native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,M,K,depth,arrays,
  all_original_payloads_temporary_only:true,signed_zero_and_actual_nonfinite_payload_bits_retained:true});
 const context=writeJSON(directory,'context.json.gz',{
  schema:'original-r273-current-native576-withJ-snapshot-context-v1',source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
  native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,session_origin:spec.session_origin,current_request:currentRequest,
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
  schema:'original-r273-current-native576-withJ-snapshot-result-v1',snapshot_completed:true,source_sha256:spec.source_sha256,
  hook_sha256:fileSHA(selfPath),native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,M,K,depth,
  manifest,context,actual_current_original_norm:numberRecord(ev.norm),actual_current_original_minA:numberRecord(ev.minA),
  actual_current_original_minD:numberRecord(ev.minD),current_state_sha256:hashes['base-states'],
  original_fresh_withJ_already_returned:true,new_RHS_J_ODE_calls_by_snapshot:0,native_accepted:false,task_completed:false});
 return {result,manifest,context,current_request:currentRequest,raw_array_sha256:hashes,current_state_sha256:hashes['base-states']};
}

function checkedCurrentDirection(directory,snapshot,{it,call,sequence}){
 const file=path.join(directory,'result.json.gz'),raw=fs.readFileSync(file),result=JSON.parse(unpack(raw));
 const expected={schema:'complete-native-original-r273-current576-damped-square-root-direction-v1',
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
 for(const [key,value] of Object.entries({schema:'original-r273-current-native576-complete-linear-system-binding-v1',
  adapter_source_sha256:spec.bridge.system_source_sha256,snapshot_result_sha256:snapshot.result.sha256,
  snapshot_context_sha256:snapshot.context.sha256,snapshot_manifest_sha256:snapshot.manifest.sha256,
  current_state_sha256:snapshot.current_state_sha256,raw_array_sha256:snapshot.raw_array_sha256,
  native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,modes:112,shape_dimension:224,
  depth:576,original_depth:576,node_count:577,old_to_new:Array.from({length:577},(_,i)=>i),
  fresh_current_evaluate_completed:true,no_cached_baseline:true,no_zero_cut_or_far_assumption:true,
  current_cut_far_errors_not_projected_or_zeroed:true,session_origin:spec.session_origin,current_request:snapshot.current_request}))
  equal(binding[key],value,'complete actual current system binding '+key);
 equal(result.new_matrix_identity_sha256,binding.new_matrix_identity_sha256,'this current matrix identity');
 const packet=readVerified(result.native_direction_checkpoint,directory),manifest=readVerified(result.array_manifest,directory);
 for(const [key,value] of Object.entries({schema:'complete-native-original-r273-current576-damped-direction-arrays-v1',
  source_sha256:spec.bridge.source_sha256,new_matrix_identity_sha256:binding.new_matrix_identity_sha256,
  factor_engine_source_sha256:spec.bridge.factor_engine_source_sha256,all_arrays_temporary_only:true,native_accepted:false}))
  equal(manifest[key],value,'current output manifest '+key);
 const entries=new Map();
 for(const entry of manifest.arrays){if(entries.has(entry.name))throw Error('Unique output array names required');entries.set(entry.name,entry);}
 const entry=result.native_delta;equal(entries.get('complete-original-coordinate-delta'),entry,'full current direction descriptor');
 equal(entry.shape,[577,224],'complete current direction shape');equal(entry.dtype,'<f8','current direction binary dtype');equal(entry.order,'C','current direction order');
 const deltaFile=safeWithin(directory,entry.file),deltaRaw=fs.readFileSync(deltaFile);
 equal(deltaRaw.length,577*224*8,'full current delta byte count');equal(deltaRaw.length,entry.bytes,'delta descriptor bytes');equal(sha(deltaRaw),entry.sha256,'full current delta raw hash');
 for(const [key,value] of Object.entries({schema:'complete-native-original-r273-current576-damped-direction-v1',
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


function absoluteReceipt(file){
 const real=fs.realpathSync(file);return {file:real,bytes:fs.statSync(real).size,sha256:fileSHA(real)};
}
function ownedFile(desc,root){
 if(typeof desc?.file!=='string'||!path.isAbsolute(desc.file))throw Error('Actual absolute same-job file required');
 const real=fs.realpathSync(desc.file),base=fs.realpathSync(root);
 if(real===base||!real.startsWith(base+path.sep)||fs.lstatSync(desc.file).isSymbolicLink()||
    !fs.statSync(real).isFile()||fs.statSync(real).size!==desc.bytes||fileSHA(real)!==desc.sha256)
  throw Error('Changed, missing or unowned actual file: '+desc.file);
 return real;
}
function readSeed(dn){
 const runner=fs.realpathSync(process.env.RUNNER_TEMP),seedFile=ownedFile(spec.initial_guess,runner);
 const seed=JSON.parse(fs.readFileSync(seedFile,'utf8'));
 if(seed.schema!=='R493-actual91-failed73-full-state-initial-guess-binding-v1'||
    seed.initial_guess_only!==true||seed.original_native_accepted!==false||
    seed.imported_response_cache!==false||seed.imported_worker_predictor!==false)
  throw Error('Actual91 may supply only its declared original failed-state guess');
 equal(seed.rawNode,Array.from(dn.tail.rawNode),'seed original raw-node layout');
 equal(mathematical(seed.numerical_configuration),spec.numerical_configuration,'seed actual original finite configuration');
 equal(mathematical(seed.original_numerical_parameters),mathematical(dn.tail.parameters),
       'seed actual original physical/numerical parameters');
 const stateFile=ownedFile(seed.initial_state,runner),heightFile=ownedFile(seed.initial_height,runner);
 const raw=fs.readFileSync(stateFile),hraw=fs.readFileSync(heightFile);
 if(raw.length!==577*224*8||hraw.length!==112*8)throw Error('Every initial577x224 and112 height word is required');
 const states=Array.from({length:577},(_,n)=>Array.from({length:224},(_,j)=>raw.readDoubleLE(8*(n*224+j))));
 const height=Array.from({length:112},(_,j)=>hraw.readDoubleLE(8*j));
 if(states.some(row=>row.some(x=>!Number.isFinite(x)))||height.some(x=>!Number.isFinite(x)))
  throw Error('The actual supplied initial guess must be finite');
 return {states,jets:{height},initial_guess_only:true,converged:false,
   source:spec.initial_guess,original_response_cache_imported:false};
}
function runPipeline(mode,ctx,fields){
 const input={schema:'R493-current-H-live128-call-pipeline-input-v1',
   mode,call_directory:ctx.directory,call_number:ctx.call,job_deadline:spec.job_deadline,
   original_source_root:spec.original_source_root,
   resources:spec.resources,bridge:spec.bridge,
   request:{jacobian:ctx.metadata.request.jacobian,audit:ctx.metadata.request.audit},
   retain_optional_tangent_predictor:spec.retain_optional_tangent_predictor===true,...fields};
 const filename=path.join(ctx.directory,'pipeline-'+mode+'-input.json');
 fs.writeFileSync(filename,encode(input),{flag:'wx'});
 const script=path.join(here,spec.pipeline.source_file);
 if(fileSHA(script)!==spec.pipeline.source_sha256)throw Error('Actual same-clock call pipeline changed');
 const command=[spec.python_executable,script,'--input',filename,'--input-sha256',fileSHA(filename)];
 const stdoutFile=path.join(ctx.directory,'pipeline-'+mode+'.stdout.log');
 const stderrFile=path.join(ctx.directory,'pipeline-'+mode+'.stderr.log');
 const stdout=fs.openSync(stdoutFile,'wx'),stderr=fs.openSync(stderrFile,'wx');
 const launch=writeJSON(ctx.directory,'pipeline-'+mode+'-launch.json',{
   schema:'R493-current-H-live128-synchronous-child-launch-v1',native_call:ctx.call,mode,command,
   input:absoluteReceipt(filename),same_original_job_deadline:spec.job_deadline,
   original_worker_stdout_protocol_not_used_by_child:true,start_new_session:false});
 let completed;
 try{completed=spawnSync(command[0],command.slice(1),{
   shell:false,cwd:here,env:{...process.env,OPENBLAS_NUM_THREADS:'1',OMP_NUM_THREADS:'1',MKL_NUM_THREADS:'1'},
   stdio:['ignore',stdout,stderr]});}
 finally{fs.closeSync(stdout);fs.closeSync(stderr);}
 const exit={mode,launch,status:completed.status,signal:completed.signal,
   error:completed.error?cleanError(completed.error):null,
   stdout:absoluteReceipt(stdoutFile),stderr:absoluteReceipt(stderrFile)};
 writeJSON(ctx.directory,'pipeline-'+mode+'-exit.json',exit);
 ctx.record.children.push(exit);
 const resultFile=path.join(ctx.directory,'pipeline-'+mode+'-result.json');
 let result=null;
 if(fs.existsSync(resultFile)){result=JSON.parse(fs.readFileSync(resultFile,'utf8'));
  ctx.record['pipeline_'+mode.replaceAll('-','_')]=absoluteReceipt(resultFile);}
 if(completed.error||completed.status!==0||result?.complete!==true){
  const error=Error('Current-H '+mode+' did not complete; real child result/stderr retained');
  error.live128_location={call:ctx.call,mode,result:resultFile,status:completed.status,
    actual_error:result?.error??null};throw error;
 }
 return result;
}
function loadProjectedMaps(desc,callDirectory){
 const file=ownedFile(desc,callDirectory),manifest=JSON.parse(fs.readFileSync(file,'utf8'));
 if(manifest.complete!==true||manifest.stages_completed!==576||manifest.files.length!==576)
  throw Error('No partial optional stage maps can be passed to the original warm predictor');
 return manifest.files.map((item,n)=>{
  const rawFile=ownedFile(item,callDirectory),raw=fs.readFileSync(rawFile);
  if(raw.length!==224*224*8)throw Error('Incomplete optional stage map at '+n);
  const row=new Float64Array(224*224);
  for(let j=0;j<row.length;j++){row[j]=raw.readDoubleLE(j*8);if(!Number.isFinite(row[j]))throw Error('Nonfinite optional projected stage map');}
  return row;
 });
}
export function createLive128Session(dn,zero,cfg,live,splitIntegrationInterval){
 if(installedDN!==null)throw Error('One original finite object per actual live128 worker');
 const runner=fs.realpathSync(process.env.RUNNER_TEMP),output=fs.realpathSync(spec.output);
 if(!output.startsWith(runner+path.sep)||!fs.statSync(output).isDirectory()||
    !Number.isFinite(zero.radius)||zero.radius<=0)throw Error('Actual owned session and original cut required');
 equal(mathematical(cfg),spec.numerical_configuration,'actual current original configuration');
 if(cfg.modes!==112||cfg.quadrature!==2048||cfg.spacing!==2||cfg.maxIterations!==32||
    cfg.solveTolerance!==2e-9||cfg.cuspAwareFlow!==true||
    dn.tail.cells.length!==576||dn.tail.parameters.depth!==576)
  throw Error('The original complete112 finite problem and original gate parameters are required');
 const originalCore=path.join(spec.original_source_topic,'scripts/78718-tail-tangent-core.mjs');
 if(fileSHA(originalCore)!=='ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3')
  throw Error('Original complete finite shooting core source changed');
 const actualEvaluate=dn.tail.evaluate.toString();
 if(sha(actualEvaluate)!=='9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9')
  throw Error('The actual original complete evaluate function changed');
 installedDN=dn;
 const before=liveIdentity(dn);
 const seed=readSeed(dn);
 writeJSON(output,'core-instrumentation.json',{
  schema:'R493-original64-direct-complete-evaluate-source-binding-v1',
  source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,
  original_core_file_sha256:fileSHA(originalCore),actual_evaluate_source_sha256:sha(actualEvaluate),
  actual_evaluate_source:actualEvaluate,original_evaluate_body_byte_identical:true,
  actual_direct_evaluate_call_before_owner:true,
  original_core_nonlin_solve_not_invoked:true,no_correction_only_capture_bypass:true,
  original64_capture_not_claimed_to_be_final128_state:true,
  all224_directions_and226_local_states_retained:true});
 writeJSON(output,'actual-live-geometry-and-initial-guess.json',{
  schema:'R493-current-H-live128-source-and-initial-guess-v1',
  actual_live_identity:before,ready_geometry:live,session_origin:spec.session_origin,
  initial_guess:spec.initial_guess,actual_imported_guess_is_not_completed_native:true,
  original_same_H_client_cache_is_initially_empty:true});
 return {
  initialSeed(){return seed;},
  async solve(height,opts,call,initialization){
   if(!Number.isInteger(call)||call!==lastCall+1)throw Error('Actual sequential protocol calls required');
   lastCall=call;
   if(!Array.isArray(height)||height.length!==112||!height.every(Number.isFinite))
    throw Error('All112 finite current physical heights required');
   const directory=path.join(output,'call-'+String(call).padStart(4,'0'));
   fs.mkdirSync(directory,{recursive:false});
   const metadata={schema:'original-r273-current576-native-request-context-v1',native_call:call,
    request:{height:Array.from(height),jacobian:!!opts.jacobian,audit:!!opts.audit},
    request_height_float64le_sha256:binaryRowsHash([height]),
    height_negative_zero_columns:height.flatMap((v,j)=>Object.is(v,-0)?[j]:[]),
    bootstrap_request:call===1,seed_assigned:call===1,
    original_worker_predictor_and_fallback_unmodified:true,original_request_flags_retained:true,
    original_final_sensitivity_not_redirected:false,same_call_complete128_final_components_required:true,
    initialization,initial_guess_is_not_a_current_solution:true};
   const requestFile=writeJSON(directory,'request.json',metadata);
   const ctx={call,directory,before,metadata,requestFile,inputHashes:null,record:{
    schema:'R493-current-H-live128-one-call-record-v1',native_call:call,request:metadata,
    job_deadline:spec.job_deadline,source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
    children:[],fresh_original_withJ_returned:false,original_current_R273_returned:false,
    literal_packets_returned:false,owner_response_assembled:false,protocol_response_returned:false,
    actual_error:null,native_accepted:false,fullDN_accepted:false}};
   const started=Date.now();
   try{
    // Identical target/scales formation to the original public DN and solve.
    const M=112,K=224,depth=576,it=0,sequence=0;
    const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
    const target=Float64Array.from(height,v=>v/radius**4);
    const scales=new Float64Array(depth+1);scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
    for(let n=0;n<depth;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
    const states=opts.initial?opts.initial.map(x=>Float64Array.from(x)):dn.tail.initial(target);
    if(states.length!==577||states.some(row=>row.length!==224))throw Error('Complete actual initial state layout');
    runPipeline('clock',ctx,{});
    equal(liveIdentity(dn),before,'same original geometry before current complete evaluate');
    const ev=dn.tail.evaluate(states,target,true,scales);
    ctx.record.fresh_original_withJ_returned=true;
    const args={ev,states,target,scales,it,M,K,depth};
    const snapshotDir=path.join(directory,'snapshot'),snapshot=captureCurrent(snapshotDir,args,ctx,sequence);
    ctx.record.snapshot=absoluteReceipt(path.join(snapshotDir,'result.json'));
    ctx.record.actual_current_original_norm=numberRecord(ev.norm);
    const factor=runPipeline('factor',ctx,{snapshot_result:ctx.record.snapshot});
    const qrDir=path.join(directory,'qr');
    const answer=checkedCurrentDirection(qrDir,snapshot,{it,call,sequence});
    ctx.record.original_current_R273_returned=true;
    ctx.record.complete_QR_result=absoluteReceipt(path.join(qrDir,'result.json.gz'));
    ctx.record.complete_QR_summary=absoluteReceipt(path.join(qrDir,'summary.json'));
    const identity={source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
     native_call:call,nonlinear_iteration:0,snapshot_sequence:0,
     fresh_snapshot_result_sha256:snapshot.result.sha256,
     complete_current_delta_sha256:answer.delta_receipt.sha256,
     complete_current_array_sha256:snapshot.raw_array_sha256,
     original_cuspAwareFlow:true,complete_current_R273_eta:spec.bridge.eta_cli_text,
     state_point:'actual-current-H-fresh-original64-full-J-initial-guess',
     current_H_is_not_fixed_historical_probe:true};
    const packetDir=path.join(directory,'literal-packet');fs.mkdirSync(packetDir);
    const primal=writeNativeTraceVariationPacket(dn,args,answer.delta,splitIntegrationInterval,identity,packetDir);
    const physical=writeNativeFinal128PhysicalPacket(dn,splitIntegrationInterval,{
     outDirectory:path.join(directory,'physical-packet'),
     primalPacket:primal.packet.path,primalPacketSHA:primal.packet.sha256,
     primalBinding:primal.binding.path,primalBindingSHA:primal.binding.sha256,
     configurationIdentity:identity,
     sourceReceipts:Object.entries(spec.frozen_sources).map(([file,digest])=>({
      file,bytes:fs.statSync(path.join(here,file)).size,sha256:digest})),
     auditSteps:cfg.auditSteps??cfg.steps});
    ctx.record.literal_packets_returned=true;
    ctx.record.literal_packet=absoluteReceipt(primal.packet.path);
    ctx.record.physical_packet=absoluteReceipt(physical.packet.path);
    const result=runPipeline('solve-response',ctx,{
     snapshot_result:ctx.record.snapshot,packet:absoluteReceipt(primal.packet.path),
     packet_binding:absoluteReceipt(primal.binding.path),
     physical_packet:absoluteReceipt(physical.packet.path),
     physical_binding:absoluteReceipt(physical.binding.path)});
    const responseFile=ownedFile(result.response,directory),responseText=fs.readFileSync(responseFile,'utf8');
    const response=JSON.parse(responseText);
    if(response.converged!==true||!response.checkpoint)throw Error('Actual current-H128 response is incomplete');
    ctx.record.owner_response_assembled=true;ctx.record.actual_response=absoluteReceipt(responseFile);
    const sol={...response,states:response.checkpoint.states,parameters:response.checkpoint.parameters,
     normalizedResidual:response.residual,jets:response.jets,converged:response.converged};
    if(spec.retain_optional_tangent_predictor===true&&result.optional_predictor_manifest){
     try{sol.linearizedFlowJacobians=loadProjectedMaps(result.optional_predictor_manifest,directory);
      ctx.record.optional_predictor_maps_returned=true;}
     catch(error){ctx.record.optional_predictor_maps_returned=false;
      ctx.record.optional_predictor_error=cleanError(error);}
    }
    opts.progress?.({phase:'actual-live128-complete-response-projection',native_call:call,
     norm:response.residual,actual_response_receipt:ctx.record.actual_response,
     not_an_original64_iteration_record:true},sol.states);
    equal(liveIdentity(dn),before,'same original geometry after128 response');
    ctx.record.elapsed_seconds=(Date.now()-started)/1000;
    // This file is closed before the worker writes the actual raw JSON response.
    writeJSON(directory,'call-result.json',ctx.record);
    return {sol,responseText,callDirectory:directory,responseFile,
     markReturned(){const record={schema:'R493-current-H-live128-protocol-write-v1',native_call:call,
       response:absoluteReceipt(responseFile),raw_response_text_forwarded_without_reserialization:true,
       requested_jacobian:!!opts.jacobian,requested_audit:!!opts.audit};
      writeJSON(directory,'protocol-written.json',record);}};
   }catch(error){
    ctx.record.actual_error=cleanError(error);
    ctx.record.actual_failure_location=error.live128_location??null;
    ctx.record.elapsed_seconds=(Date.now()-started)/1000;
    if(!fs.existsSync(path.join(directory,'call-result.json')))writeJSON(directory,'call-result.json',ctx.record);
    throw error;
   }
  }
 };
}
