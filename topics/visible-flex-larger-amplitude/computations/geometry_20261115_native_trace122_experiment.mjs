// Request122: one real fresh packet, two explicit base-point trace JVPs.
// This module does not select a nonlinear step or create a native response.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {writeNativeTraceVariationPacket} from './geometry_20261115_native_trace_variation128_bridge.mjs';

const here=path.dirname(fileURLToPath(import.meta.url));
const PINS={
 'geometry_20261115_native_trace_variation128.cpp':'8c40b4c7ed214a16afd06cd0157bf861822cb217a72bd0117bbed7f2c954204d',
 'geometry_20261115_native_trace_variation128.py':'8229212bb6804db7eee99ea661a490d3cced756e8a98471c09e22ad74cdb8b76',
 'geometry_20261115_native_trace_variation128_bridge.mjs':'61e21ded03f1569c7d05742d3059553d1f3830c52a62643fd64883bc821c83a7',
 'geometry_20261115_native_primal128.cpp':'1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d',
 'geometry_20261115_native_primal128_bridge.mjs':'3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8'
};
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
function fileSHA(file){
 const h=crypto.createHash('sha256'),fd=fs.openSync(file,'r'),buffer=Buffer.allocUnsafe(1<<20);
 try{for(;;){const n=fs.readSync(fd,buffer,0,buffer.length,null);if(!n)break;h.update(buffer.subarray(0,n));}}
 finally{fs.closeSync(fd);}return h.digest('hex');
}
function rowsSHA(rows){
 const h=crypto.createHash('sha256');
 for(const row of rows){
  if(!(row instanceof Float64Array))throw Error('Use the actual original Float64Array rows');
  h.update(Buffer.from(row.buffer,row.byteOffset,row.byteLength));
 }return h.digest('hex');
}
function inputHashes(dn,args,delta){
 return {states:rowsSHA(args.states),delta:rowsSHA(delta),target:rowsSHA([args.target]),
  scales:rowsSHA([args.scales]),far:rowsSHA([dn.tail.graphs.at(-1)])};
}
function savedReport(summary){
 const raw=summary.scientific_report;
 if(!raw)return null;
 // Complete per-stage metadata remains covered by the original report and
 // manifest SHA; the science itself never has a stage/angle/mode truncation.
 const result={...raw};delete result.all_stage_accounting;
 return result;
}
function outcome(summary){
 if(!summary)return 'missing-launcher-summary';
 if(summary.actual_error)return 'launcher-error';
 const r=summary.scientific_report;
 if(r?.complete===true)return 'complete-one-direction';
 if(r?.experiment_budget_exhausted===true||summary.child_exit?.timeout_error)return 'resource-budget-partial';
 if(r)return 'returned-partial-or-original-root-trace-failure';
 return 'missing-scientific-report';
}

export function runTrace122Policies(dn,args,delta,splitIntegrationInterval,identity,emit){
 if(process.env.GITHUB_ACTIONS!=='true'||process.env.GITHUB_REPOSITORY!=='Rogerhu12/math-research-public')
  throw Error('Request122 scientific arithmetic is public Actions only');
 if(args.it!==0||identity.nonlinear_iteration!==0||identity.native_call!==1)
  throw Error('Request122 uses the one real first fresh correction only');
 for(const [name,digest] of Object.entries(PINS))
  if(fileSHA(path.join(here,name))!==digest)throw Error('Frozen trace source changed: '+name);
 const totalSeconds=Number(process.env.VISIBLE_NATIVE_TRACE122_SECONDS),
  threads=Number(process.env.VISIBLE_NATIVE_TRACE122_THREADS);
 if(totalSeconds!==7200||threads!==2)throw Error('Request122 fixes7200seconds and2threads');
 const runner=fs.realpathSync(process.env.RUNNER_TEMP),
  work=fs.mkdtempSync(path.join(runner,'native-trace122-owned-'));
 const before=inputHashes(dn,args,delta),records=[];
 let result;
 try{
  // One actual packet is shared by both policy calls.  No old113 packet or
  // old direction is imported and no second fresh64 J/QR is requested.
  const inputs=writeNativeTraceVariationPacket(dn,args,delta,splitIntegrationInterval,identity,work);
  const started=Date.now(),deadline=started+totalSeconds*1000;
  emit({event:'native122_actual_packet',source_sha256:fileSHA(fileURLToPath(import.meta.url)),
   source_pins:PINS,identity,input_array_sha256:before,packet:inputs.packet,binding:inputs.binding,
   current_point:'base',alpha:'0',actual_direction:'one complete fresh original R273 delta',
   total_wall_seconds:totalSeconds,first_policy_science_seconds_maximum:3600,
   per_launch_overhead_reserve_seconds:300,threads,
   tolerance_order:['original','refined'],second_policy_not_gated_by_first_policy_result:true,
   no_original64_noJ_control_or_nonlinear_trial_added:true,native_accepted:false});
  for(const [index,policy] of ['original','refined'].entries()){
   const remaining=Math.floor((deadline-Date.now())/1000);
   // The300s is the explicit compiler+subprocess overhead allowance, not a
   // numerical threshold.  It fits the launcher's180s compile+120s grace.
   const seconds=Math.min(index===0?3600:7200,remaining-300);
   if(seconds<60){
    const skipped={policy,index,attempted:false,reason:'remaining-total-wall-budget-below60plus300',
     remaining_wall_seconds:remaining,complete:false,native_accepted:false};
    records.push(skipped);emit({event:'native122_policy_not_started',...skipped});continue;
   }
   const out=path.join(work,'policy-'+policy),launcher=path.join(here,'geometry_20261115_native_trace_variation128.py');
   const command=[launcher,'--packet',inputs.packet.path,'--packet-binding',inputs.binding.path,
    '--expected-packet-sha256',inputs.packet.sha256,'--expected-binding-sha256',inputs.binding.sha256,
    '--expected-cpp-sha256',PINS['geometry_20261115_native_trace_variation128.cpp'],
    '--policy',policy,'--state-point','base','--seconds',String(seconds),'--threads',String(threads),'--out',out];
   emit({event:'native122_policy_started',policy,index,seconds,remaining_wall_seconds:remaining,
    packet_sha256:inputs.packet.sha256,binding_sha256:inputs.binding.sha256,current_point:'base',alpha:'0',
    original_native_acceptance_not_involved:true});
   const childStart=Date.now();
   // The guard and both launcher/compiler/science descendants remain in
   // the rules runner's process group.  A true rules change stops them all.
   const guard=path.join(here,'geometry_20261115_native_trace122_probe.py');
   const guardReceipt=path.join(work,'guard-'+policy+'.json');
   const child=spawnSync('python',[guard,'--policy-guard-seconds',String(remaining),
    '--policy-guard-receipt',guardReceipt,'--command','python',...command],
    {shell:false,cwd:work,env:{...process.env},stdio:['ignore',2,2]});
   let guardStatus=null;
   if(fs.existsSync(guardReceipt))guardStatus=JSON.parse(fs.readFileSync(guardReceipt,'utf8'));
   const file=path.join(out,'summary.json');let summary=null,readError=null,raw=null;
   try{
    if(fs.existsSync(file)){
     raw=fs.readFileSync(file);summary=JSON.parse(raw);
     if(summary.schema!=='native-finite-root-trace-direction-launch-summary-v1'||
        summary.input_packet.sha256!==inputs.packet.sha256||summary.input_binding.sha256!==inputs.binding.sha256||
        summary.policy!==policy||summary.state_point!=='base')throw Error('The policy returned a different actual packet/point');
    }
   }catch(error){readError=String(error);summary=null;}
   const r={policy,index,attempted:true,science_seconds_allocated:seconds,
    elapsed_wall_seconds:(Date.now()-childStart)/1000,
    child_exit:{status:child.status,signal:child.signal,error:child.error?String(child.error):null},
    summary_receipt:raw?{bytes:raw.length,sha256:sha(raw)}:null,
    summary_read_error:readError,policy_guard:guardStatus,
    outcome:guardStatus?.wall_timeout===true?'total-wall-timeout-partial':outcome(summary),complete:summary?.scientific_report?.complete===true,
    actual_error:summary?.actual_error??null,
    full_scientific_report:summary?.full_scientific_report??null,
    temporary_output_manifest:summary?.temporary_output_manifest??null,
    array_receipts:summary?.array_receipts??null,scientific_report:savedReport(summary),
    native_accepted:false};
   records.push(r);emit({event:'native122_policy_returned',...r});
   if(fileSHA(inputs.packet.path)!==inputs.packet.sha256||fileSHA(inputs.binding.path)!==inputs.binding.sha256)
    throw Error('The shared actual packet or binding was mutated by a consumer');
   if(fs.existsSync(out))fs.rmSync(out,{recursive:true,force:true});
  }
  const after=inputHashes(dn,args,delta);
  if(JSON.stringify(after)!==JSON.stringify(before))throw Error('Independent JVP changed original current arrays');
  result={schema:'request122-fresh-actual-direction-two-base-traces-v1',
   source_sha256:fileSHA(fileURLToPath(import.meta.url)),identity,
   input_packet:{file:inputs.packet.file,bytes:inputs.packet.bytes,sha256:inputs.packet.sha256},
   packet_binding:{file:inputs.binding.file,bytes:inputs.binding.bytes,sha256:inputs.binding.sha256},
   input_array_sha256:before,policy_records:records,
   independent_real_expression_derivative_not_IEEE_roundmap_derivative:true,
   independent_experiment_returned:true,all_requested_policy_slots_accounted_for:records.length===2,
   all_two_policy_directions_complete:records.length===2&&records.every(r=>r.complete===true),
   elapsed_wall_seconds:(Date.now()-started)/1000,
   fresh_snapshot_count:1,fresh_R273_direction_count:1,second_policy_not_gated_by_first:true,
   original_direction_not_returned_to_nonlinear_loop:true,original_nonlinear_trials_not_executed:true,
   complete224_column_trace_J_supplied:false,native_accepted:false,fullDN_or_endpoint_J_or_fresh_audit_supplied:false,
   temporary_raw_cleanup_follows:true};
  emit({event:'native122_finite_trace_policies_complete',result});
  return result;
 }finally{fs.rmSync(work,{recursive:true,force:true});}
}
