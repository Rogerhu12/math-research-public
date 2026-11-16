// Independent204: original complete SIMD chain with the retained three-call view and R445 stage type qualification.
// The original133 sources remain unchanged; this bridge exports only live
// physical tables/geometry before the owner and never claims native success.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {writeNativeTraceVariationPacket} from './geometry_20261115_native_trace_variation128_bridge.mjs';
import {writeNativeFinal128PhysicalPacket} from './geometry_20261115_native_final128_packet.mjs';

const here=path.dirname(fileURLToPath(import.meta.url));
const LAUNCHER='geometry_20261116_native_simd_stats_qualified_final128_same_job.py';
const CPP='geometry_20261115_native_persistent128.cpp';
const PHYSICAL_WRITER_SHA='824b7440d2604e828df4326b1cef1b1bf332d203eeb7e81968704d2febdcd7c2';
// The new entry supplies its actual workflow-pinned source SHA. This avoids
// a cyclic source hash between that entry and this bridge.
const launcherSHA=()=>{
 const value=process.env.VISIBLE_OPERATOR_FINAL128_OWNER_LAUNCHER_SHA;
 if(!/^[0-9a-f]{64}$/.test(value??''))throw Error('Explicit final-components owner source SHA');
 return value;
};
const CPP_SHA='7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd';
const WRITER_SHA='61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7';
const hash=file=>{
 const h=crypto.createHash('sha256'),fd=fs.openSync(file,'r'),block=Buffer.allocUnsafe(1<<20);
 try{for(;;){const n=fs.readSync(fd,block,0,block.length,null);if(n===0)break;h.update(block.subarray(0,n));}}
 finally{fs.closeSync(fd);}return h.digest('hex');
};
const sha=raw=>crypto.createHash('sha256').update(raw).digest('hex');
function receipt(file){return {file:path.basename(file),bytes:fs.statSync(file).size,sha256:hash(file)};}
function same(a,b,label){if(JSON.stringify(a)!==JSON.stringify(b))throw Error(label);}
function integerEnv(name,minimum,maximum){
 const text=process.env[name];if(!/^[0-9]+$/.test(text??''))throw Error('Explicit integer '+name);
 const value=Number(text);if(!Number.isSafeInteger(value)||value<minimum||value>maximum)throw Error('Declared resource '+name);return value;
}

function originalSourceReceipts(root,destination){
 root=fs.realpathSync(root);fs.mkdirSync(destination,{recursive:false});
 const origin=JSON.parse(fs.readFileSync(path.join(root,'source-origin.json')));
 const prefix='topics/visible-flexible-closed-surface/';
 if(origin.verified_file_count!==78||!Array.isArray(origin.restored_files)||origin.restored_files.length!==78)
  throw Error('Actual complete original78 source restoration');
 const receipts=[],seen=new Set();
 for(const row of origin.restored_files){
  if(typeof row.path!=='string'||!row.path.startsWith(prefix))throw Error('Original source prefix');
  const rel=row.path.slice(prefix.length),parts=rel.split('/');
  if(!rel||rel.includes('\\')||parts.some(x=>x==='..'||x==='.'||x===''))throw Error('Contained original source path');
  const file=path.join(root,rel),actual=fs.realpathSync(file);
  if(!actual.startsWith(root+path.sep)||fs.lstatSync(file).isSymbolicLink()||seen.has(rel))
   throw Error('Unique regular source file');
  seen.add(rel);
  if(fs.statSync(file).size!==row.bytes||hash(file)!==row.sha256)throw Error('Actual original source bytes '+rel);
  const recorded='original78/'+rel,target=path.join(destination,recorded);
  fs.mkdirSync(path.dirname(target),{recursive:true});
  fs.copyFileSync(file,target,fs.constants.COPYFILE_EXCL);
  if(hash(target)!==row.sha256)throw Error('Complete original source copy '+rel);
  receipts.push({file:recorded,bytes:row.bytes,sha256:row.sha256});
 }
 const slopeName='numerical-tail-slope-jacobian.mjs',slopeSHA='206d82d3b41e6b9ce24b26447a2026c19c1c7126765107c23d58e55da25639e2',
  slope=path.join(here,slopeName),slopeCopy=path.join(destination,'current-adapters',slopeName);
 if(hash(slope)!==slopeSHA)throw Error('Original analytic-slope adapter source');
 fs.mkdirSync(path.dirname(slopeCopy));fs.copyFileSync(slope,slopeCopy,fs.constants.COPYFILE_EXCL);
 receipts.push({file:'current-adapters/'+slopeName,bytes:fs.statSync(slopeCopy).size,sha256:hash(slopeCopy)});
 return receipts;
}
function reportOwnedChildStderr(file,emit){
 // The whole original stderr stays in this owned temporary tree. The final
 // single necessary reader selects actual engineering errors with file SHA;
 // neither scientific stdout nor errors are encoded or split for transport.
 const desc=receipt(file);
 const value={receipt:desc,original_file_complete:true,
  original_stderr_retained_for_necessary_reader:true,
  complete_bytes_in_compute_log:false,no_segmented_or_encoded_transport:true,
  scientific_failure_not_inferred:true};
 emit({event:'persistent128_owned_child_stderr',child_stderr:value});return value;
}
function currentGlobalBudget(python){
 const child=spawnSync(python,[path.join(here,LAUNCHER),'--budget-read'],{
  shell:false,env:{...process.env},stdio:['ignore','pipe',2],encoding:'utf8',
  detached:false,timeout:10000,maxBuffer:65536});
 if(child.status!==0||child.error)throw Error('Actual global resource metadata read failed: '+String(child.error??child.status));
 const value=JSON.parse(child.stdout);
 if(value.schema!=='native-simd_stats_qualified_digit-operator-final128-current-global-resource-plan-v1'||
    value.absolute_monotonic_deadline_ns!==process.env.VISIBLE_OPERATOR_FINAL128_GLOBAL_MONOTONIC_DEADLINE_NS||
    !Number.isSafeInteger(value.guard_seconds)||value.guard_seconds<0||value.guard_seconds>19500)
  throw Error('Actual inherited whole-science deadline');
 return value;
}
export function runPersistent128(dn,args,delta,splitIntegrationInterval,identity,emit){
 if(process.env.GITHUB_ACTIONS!=='true'||(process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('The persistent128 experiment runs only in public Actions');
 const LAUNCHER_SHA_FOR_BINDING=launcherSHA();
 for(const [name,expected] of [[LAUNCHER,LAUNCHER_SHA_FOR_BINDING],[CPP,CPP_SHA],['geometry_20261115_native_trace_variation128_bridge.mjs',WRITER_SHA],
  ['geometry_20261115_native_final128_packet.mjs',PHYSICAL_WRITER_SHA]])
  if(hash(path.join(here,name))!==expected)throw Error('Independent source identity '+name);
 const LAUNCHER_SHA=launcherSHA();
 const requestedSeconds=integerEnv('VISIBLE_PERSISTENT128_SECONDS',600,20000),threads=integerEnv('VISIBLE_PERSISTENT128_THREADS',1,4),
  requestedReserve=integerEnv('VISIBLE_PERSISTENT128_REPLAY_RESERVE',60,19900),
  columns=integerEnv('VISIBLE_PERSISTENT128_FINAL_COLUMNS',0,224),matched=process.env.VISIBLE_PERSISTENT128_MATCHED_TRACE;
 if(columns!==0||!['each-direction','none'].includes(matched)||requestedReserve>=requestedSeconds-300)
  throw Error('Explicit persistent128 trace/replay/full-column resources required');
 if(args.it!==0||identity.native_call!==1||identity.nonlinear_iteration!==0)
  throw Error('Use one actual first fresh64 model as the declared fixed chord matrix');
 const runner=fs.realpathSync(process.env.RUNNER_TEMP??''),snapshot=fs.realpathSync(identity.fresh_snapshot_directory);
 if(snapshot===runner||!snapshot.startsWith(runner+path.sep)||
    hash(path.join(snapshot,'result.json'))!==identity.fresh_snapshot_result_sha256)
  throw Error('Use the actual still-live fresh snapshot directory');
 const sourceRoot=fs.realpathSync(process.env.VISIBLE_OPERATOR_FINAL128_ORIGINAL_SOURCE_ROOT??''),
  python=process.env.VISIBLE_PERSISTENT128_PYTHON??'python';
 const workRoot=fs.realpathSync(process.env.VISIBLE_OPERATOR_FINAL128_OWNED_WORK_ROOT??'');
 if(workRoot===runner||!workRoot.startsWith(runner+path.sep))throw Error('Request-owned independent component root');
 const work=fs.mkdtempSync(path.join(workRoot,'owner-'));
 let result,closed=false;
 try{
  // The exact frozen writer binds the initial 64-bit state, direction,
  // all independent literal tables and all6943 original atomic RK steps.
  const inputs=writeNativeTraceVariationPacket(dn,args,delta,splitIntegrationInterval,identity,work);
  const componentSources=path.join(work,'physical-source-inputs');
  const physical=writeNativeFinal128PhysicalPacket(dn,splitIntegrationInterval,{
   outDirectory:path.join(work,'physical-input'),primalPacket:inputs.packet.path,primalPacketSHA:inputs.packet.sha256,
   primalBinding:inputs.binding.path,primalBindingSHA:inputs.binding.sha256,
   configurationIdentity:identity,sourceReceipts:originalSourceReceipts(sourceRoot,componentSources),auditSteps:dn.tail.parameters.steps});
  const budget=currentGlobalBudget(python),seconds=budget.actual_owner_seconds,
   reserve=budget.actual_replay_reserve_seconds,guardSeconds=budget.guard_seconds;
  emit({event:'persistent128_actual_packet',packet:inputs.packet,binding:inputs.binding,
   input_array_sha256:inputs.input_array_sha256,fresh_snapshot_result_sha256:identity.fresh_snapshot_result_sha256,
   new_launcher_sha256:LAUNCHER_SHA,new_CPP_sha256:CPP_SHA,packet_writer_sha256:WRITER_SHA,
   seconds,threads,matched_trace:matched,fresh_replay_reserve_seconds:reserve,final_stage_columns_requested:columns,
   physical_packet:physical,actual_global_budget:budget,guard_seconds:guardSeconds,
   final_components_use_default_original_audit_steps:true,final_component_writer_sha256:PHYSICAL_WRITER_SHA,
   initial64_delta_is_packet_provenance_not_the_persistent_iteration_RHS:true,
   only_fixed64_J_is_reused_as_approximate_chord:true,native_accepted:false});
  if(!budget.owner_can_start){
   const summary={schema:'native-persistent128-simd_stats_qualified_digit-owner-not-started-resource-v1',
    source_sha256:LAUNCHER_SHA,cpp_source_sha256:CPP_SHA,summary_complete:true,transport_complete:true,
    actual_global_budget:budget,owner_attempted:false,
    reason:'whole-science-deadline-cannot-pay-owner-and-reserved-audit',
    native_accepted:false,fullDN_completed:false,
    post_owner_components:{attempted:false,reason:'actual128-final-state-not-produced'}};
   result={schema:'native-persistent128-simd_stats_qualified_digit-precleanup-owner-return-v1',
    independent_experiment_returned:true,scientific_summary:summary,summary:null,
    packet:inputs.packet,binding:inputs.binding,physical_packet:physical,
    child_exit:{status:2,signal:null,error:null},summary_complete:true,transport_complete:true,
    owner_child_not_started:true,resource_partial:true,native_accepted:false,
    original64_worker_controlled_stop_follows:true};
   closed=true;emit({event:'persistent128_bridge_returned',result});return result;
  }
  const out=path.join(work,'result'),launcher=path.join(here,LAUNCHER);
  const command=[python,launcher,'--owner-child','--packet',inputs.packet.path,'--packet-binding',inputs.binding.path,
   '--expected-packet-sha256',inputs.packet.sha256,'--expected-binding-sha256',inputs.binding.sha256,
   '--expected-cpp-sha256',CPP_SHA,'--snapshot-directory',snapshot,
   '--snapshot-result-sha256',identity.fresh_snapshot_result_sha256,
   '--seconds',String(seconds),'--threads',String(threads),'--fresh-replay-reserve-seconds',String(reserve),
   '--matched-trace',matched,'--final-stage-columns',String(columns),'--out',out];
  const guardFile=path.join(work,'wall-guard.json');
  const childEnv={...process.env,OPENBLAS_NUM_THREADS:'1',MKL_NUM_THREADS:'1',
   VISIBLE_OPERATOR_FINAL128_PHYSICAL_PACKET:physical.packet.path,VISIBLE_OPERATOR_FINAL128_PHYSICAL_PACKET_SHA:physical.packet.sha256,
   VISIBLE_OPERATOR_FINAL128_PHYSICAL_BINDING:physical.binding.path,VISIBLE_OPERATOR_FINAL128_PHYSICAL_BINDING_SHA:physical.binding.sha256,
   VISIBLE_OPERATOR_FINAL128_COMPONENT_SOURCE_ROOT:componentSources};
  const stderrFile=path.join(work,'owner-child.stderr.log'),stderrFD=fs.openSync(stderrFile,'wx');
  let child,childStderr;
  try{
   child=spawnSync(python,[launcher,'--wall-guard-seconds',String(guardSeconds),'--wall-guard-receipt',guardFile,
    '--command',...command],{shell:false,cwd:here,env:childEnv,
    stdio:['ignore',2,stderrFD],detached:false,timeout:(guardSeconds+30)*1000});
  }finally{
   fs.closeSync(stderrFD);childStderr=reportOwnedChildStderr(stderrFile,emit);
  }
  closed=fs.existsSync(guardFile);
  const summaryFile=path.join(out,'compact-summary.json');
  let summary=null,summaryReceipt=null;
  if(fs.existsSync(summaryFile)){
   const raw=fs.readFileSync(summaryFile);summary=JSON.parse(raw);summaryReceipt=receipt(summaryFile);
   same(summary.schema,'native-persistent128-chord-launch-summary-v1','Actual persistent128 summary schema');
   same(summary.source_sha256,LAUNCHER_SHA,'Actual persistent128 launcher identity');
   same(summary.cpp_source_sha256,CPP_SHA,'Actual persistent128 owner source identity');
   // A bounded fallback may intentionally omit packet fields; the full
   // source-bound summary identity still appears in the streamed record.
   if(summary.input_packet)same(summary.input_packet.sha256,inputs.packet.sha256,'Actual complete input packet');
   if(summary.packet_binding)same(summary.packet_binding.sha256,inputs.binding.sha256,'Actual input packet binding');
   if(summary.actual_call_identity)same(summary.actual_call_identity.fresh_snapshot_result_sha256,
    identity.fresh_snapshot_result_sha256,'Actual initial fixed chord source point');
   same(summary.native_accepted,false,'The original native final response is not manufactured');
  }
  result={schema:'native-persistent128-simd_stats_qualified_digit-precleanup-owner-return-v1',independent_experiment_returned:true,
   actual_post_owner_component_flags:summary?.post_owner_components?{
    all_requested_components_completed:summary.post_owner_components.all_requested_components_completed??false,
    complete_stage_maps:summary.post_owner_components.complete_stage_maps??false,
    complete_boundary112_response:summary.post_owner_components.complete_boundary112_response??false,
    complete_mixed_endpoint338x112_readout:summary.post_owner_components.complete_mixed_endpoint338x112_readout??false,
    complete_original_C_based_physical_program_audit:summary.post_owner_components.complete_original_C_based_physical_program_audit??false,
    native_accepted:false,fullDN_accepted:false}:null,
   physical_packet:physical,source_closure_checked_before_owner:true,
   stage_derivative_implementation:'R402-recorded-literal-simd_digit-maps-nominal-factor-binary128',
   old_dL_graph_word_equality_claimed:false,nominal_factor_residual_derivatives_proved_zero:false,
   packet:inputs.packet,binding:inputs.binding,summary:summaryReceipt,scientific_summary:summary,
   child_exit:{status:child.status,signal:child.signal,error:child.error?String(child.error):null},
   child_stderr:childStderr,
   summary_complete:summary?.summary_complete===true,
   transport_complete:child.status!==70&&summary?.transport_complete===true&&childStderr.original_file_complete===true,
   wall_guard:fs.existsSync(guardFile)?{receipt:receipt(guardFile),record:JSON.parse(fs.readFileSync(guardFile))}:null,
   persistent128_state_was_not_written_into_original64_worker:true,
   original64_worker_controlled_stop_follows:true,native_accepted:false,
   complete_endpoint_sensitivity_or_original_geometric_audit_not_fabricated:true};
  emit({event:'persistent128_bridge_returned',result});
  return result;
 }finally{
  // The original owner/probe also defer their final raw deletion. Only the
  // outer always step, after its one necessary summary and quiet evidence,
  // may remove this regenerable tree. No failed field becomes an anchor.
  emit({event:'persistent128_cleanup_deferred',
   reason:'retain-until-single-necessary-summary-and-owned-quiet-evidence',
   owned_child_guard_completion_observed:closed,
   temporary_directory:work,no_raw_upload_follows:true,native_accepted:false});
 }
}
