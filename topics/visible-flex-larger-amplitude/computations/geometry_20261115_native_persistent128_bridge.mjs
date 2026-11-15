// Independent persistent128 state owner. No 128 state is returned into the
// original Float64Array native worker or declared its accepted checkpoint.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {writeNativeTraceVariationPacket} from './geometry_20261115_native_trace_variation128_bridge.mjs';

const here=path.dirname(fileURLToPath(import.meta.url));
const LAUNCHER='geometry_20261115_native_persistent128.py';
const CPP='geometry_20261115_native_persistent128.cpp';
const LAUNCHER_SHA='767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322';
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

export function runPersistent128(dn,args,delta,splitIntegrationInterval,identity,emit){
 if(process.env.GITHUB_ACTIONS!=='true'||(process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('The persistent128 experiment runs only in public Actions');
 for(const [name,expected] of [[LAUNCHER,LAUNCHER_SHA],[CPP,CPP_SHA],['geometry_20261115_native_trace_variation128_bridge.mjs',WRITER_SHA]])
  if(hash(path.join(here,name))!==expected)throw Error('Independent source identity '+name);
 const seconds=integerEnv('VISIBLE_PERSISTENT128_SECONDS',600,20000),threads=integerEnv('VISIBLE_PERSISTENT128_THREADS',1,4),
  reserve=integerEnv('VISIBLE_PERSISTENT128_REPLAY_RESERVE',60,19900),
  columns=integerEnv('VISIBLE_PERSISTENT128_FINAL_COLUMNS',0,224),matched=process.env.VISIBLE_PERSISTENT128_MATCHED_TRACE;
 if(![0,224].includes(columns)||!['each-direction','none'].includes(matched)||reserve>=seconds-300)
  throw Error('Explicit persistent128 trace/replay/full-column resources required');
 if(args.it!==0||identity.native_call!==1||identity.nonlinear_iteration!==0)
  throw Error('Use one actual first fresh64 model as the declared fixed chord matrix');
 const runner=fs.realpathSync(process.env.RUNNER_TEMP??''),snapshot=fs.realpathSync(identity.fresh_snapshot_directory);
 if(snapshot===runner||!snapshot.startsWith(runner+path.sep)||
    hash(path.join(snapshot,'result.json'))!==identity.fresh_snapshot_result_sha256)
  throw Error('Use the actual still-live fresh snapshot directory');
 const work=fs.mkdtempSync(path.join(runner,'native-persistent128-'));
 let result,closed=false;
 try{
  // The exact frozen writer binds the initial 64-bit state, direction,
  // all independent literal tables and all6943 original atomic RK steps.
  const inputs=writeNativeTraceVariationPacket(dn,args,delta,splitIntegrationInterval,identity,work);
  emit({event:'persistent128_actual_packet',packet:inputs.packet,binding:inputs.binding,
   input_array_sha256:inputs.input_array_sha256,fresh_snapshot_result_sha256:identity.fresh_snapshot_result_sha256,
   new_launcher_sha256:LAUNCHER_SHA,new_CPP_sha256:CPP_SHA,packet_writer_sha256:WRITER_SHA,
   seconds,threads,matched_trace:matched,fresh_replay_reserve_seconds:reserve,final_stage_columns_requested:columns,
   initial64_delta_is_packet_provenance_not_the_persistent_iteration_RHS:true,
   only_fixed64_J_is_reused_as_approximate_chord:true,native_accepted:false});
  const out=path.join(work,'result'),launcher=path.join(here,LAUNCHER),python=process.env.VISIBLE_PERSISTENT128_PYTHON??'python';
  const command=[python,launcher,'--packet',inputs.packet.path,'--packet-binding',inputs.binding.path,
   '--expected-packet-sha256',inputs.packet.sha256,'--expected-binding-sha256',inputs.binding.sha256,
   '--expected-cpp-sha256',CPP_SHA,'--snapshot-directory',snapshot,
   '--snapshot-result-sha256',identity.fresh_snapshot_result_sha256,
   '--seconds',String(seconds),'--threads',String(threads),'--fresh-replay-reserve-seconds',String(reserve),
   '--matched-trace',matched,'--final-stage-columns',String(columns),'--out',out];
  const guardFile=path.join(work,'wall-guard.json'),guardSeconds=seconds+330;
  const child=spawnSync(python,[launcher,'--wall-guard-seconds',String(guardSeconds),'--wall-guard-receipt',guardFile,
   '--command',...command],{shell:false,cwd:here,env:{...process.env,OPENBLAS_NUM_THREADS:'1',MKL_NUM_THREADS:'1'},
   stdio:['ignore',2,2],detached:false,timeout:(guardSeconds+30)*1000});
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
  result={schema:'native-persistent128-independent-owner-return-v1',independent_experiment_returned:true,
   packet:inputs.packet,binding:inputs.binding,summary:summaryReceipt,scientific_summary:summary,
   child_exit:{status:child.status,signal:child.signal,error:child.error?String(child.error):null},
   summary_complete:summary?.summary_complete===true,
   transport_complete:child.status!==70&&summary?.transport_complete===true,
   wall_guard:fs.existsSync(guardFile)?{receipt:receipt(guardFile),record:JSON.parse(fs.readFileSync(guardFile))}:null,
   persistent128_state_was_not_written_into_original64_worker:true,
   original64_worker_controlled_stop_follows:true,native_accepted:false,
   complete_endpoint_sensitivity_or_original_geometric_audit_not_fabricated:true};
  emit({event:'persistent128_bridge_returned',result});
  return result;
 }finally{
  // Each child has exited or was stopped by the bounded guard before raw
  // packet cleanup. A failed native iteration is never turned into cache.
  if(closed)fs.rmSync(work,{recursive:true,force:true});
  else emit({event:'persistent128_cleanup_deferred',reason:'owned-child-guard-completion-not-observed',
   temporary_directory:work,no_raw_upload_follows:true,native_accepted:false});
 }
}
