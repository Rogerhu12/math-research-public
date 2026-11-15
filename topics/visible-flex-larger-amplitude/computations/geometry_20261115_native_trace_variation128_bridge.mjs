// R283: a new actual literal packet for finite-root-trace variation.
// The private writePacket body below is byte-identical to frozen113.
// No existing native source is modified or installed by this module.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const fileSHA=file=>{
 const h=crypto.createHash('sha256'),fd=fs.openSync(file,'r'),b=Buffer.allocUnsafe(1<<20);
 try{for(;;){const n=fs.readSync(fd,b,0,b.length,null);if(n===0)break;h.update(b.subarray(0,n));}}
 finally{fs.closeSync(fd);}return h.digest('hex');
};
const rowsSHA=rows=>{
 const h=crypto.createHash('sha256');
 for(const row of rows){
  if(!(row instanceof Float64Array))throw Error('The actual original Float64Array rows are required');
  h.update(Buffer.from(row.buffer,row.byteOffset,row.byteLength));
 }
 return h.digest('hex');
};
const here=path.dirname(fileURLToPath(import.meta.url));
function writePacket(file,dn,args,delta,splitIntegrationInterval){
 const {states,target,scales,M,K,depth}=args,p=dn.tail.parameters,
  N=p.quadrature,J=M+1,size=K+2,fd=fs.openSync(file,'wx');
 const h=crypto.createHash('sha256');let bytes=0,geometryCalls=0,rkSteps=0;
 const write=b=>{let at=0;while(at<b.length){const n=fs.writeSync(fd,b,at,b.length-at);if(n<=0)throw Error('Complete packet write failed');at+=n;}h.update(b);bytes+=b.length;};
 const u32=v=>{if(!Number.isInteger(v)||v<0||v>0xffffffff)throw Error('u32 packet field');const b=Buffer.allocUnsafe(4);b.writeUInt32LE(v);write(b);};
 const word=v=>{if(!Number.isFinite(v))throw Error('Only finite original input words may be lifted');const b=Buffer.allocUnsafe(8);b.writeDoubleLE(v);write(b);};
 const row=v=>{
  const b=Buffer.allocUnsafe(v.length*8);
  for(let j=0;j<v.length;j++){if(!Number.isFinite(v[j]))throw Error('Nonfinite input row');b.writeDoubleLE(v[j],8*j);}
  write(b);
 };
 const geometry=(cell,profile,x)=>{
  const g=cell.engine.geometry(profile,x);geometryCalls++;
  // Preserve the existing binary64 profile/exp/E evaluations as coefficient
  // inputs.  The experiment does not silently replace the scalar profile.
  return [g.r,g.drdx,g.w,g.w2,g.E];
 };
 const cells=[];
 try{
  write(Buffer.from('QPR11301'));u32(M);u32(N);u32(depth);u32(p.orientation===1?1:2);
  row([Math.sqrt(2),Math.sqrt(12),p.projectionFloor,2e-9,8e-14,5e-12]);
  const frequency=Float64Array.from({length:M},(_,j)=>(j+1)*p.spacing);row(frequency);
  // These expressions/loop order are the actual frozen root/split table
  // definitions.  Math.sin/cos are evaluated only in the original precision.
  const cosine=[],sine=[],gram=[];
  for(let n=0;n<N;n++){
   const theta=2*Math.PI*n/N,cs=new Float64Array(J),sn=new Float64Array(M);
   cs[0]=1;for(let j=0;j<M;j++){cs[j+1]=Math.sqrt(2)*Math.cos(frequency[j]*theta);sn[j]=Math.sqrt(2)*Math.sin(frequency[j]*theta);}
   cosine.push(cs);sine.push(sn);
   gram.push(Float64Array.from({length:2*M+1},(_,k)=>Math.cos(p.spacing*k*(2*Math.PI*n/N))));
  }
  for(const r of cosine)row(r);for(const r of sine)row(r);for(const r of gram)row(r);
  for(const r of states)row(r);for(const r of delta)row(r);
  row(target);row(scales);row(dn.tail.graphs.at(-1));
  for(let n=0;n<depth;n++){
   const cell=dn.tail.cells[n],records=[],schedule=[];
   for(let pi=0;pi<cell.profiles.length;pi++){
    const profile=cell.profiles[pi];
    for(let k=0;k<p.steps;k++){
     const x=k/p.steps,hh=1/p.steps;
     const grid=splitIntegrationInterval(x,x+hh,profile.integrationBreakpoints);
     // The original cusp wrapper retains (x,hh) if there is no split.  Do
     // not replace hh by fl((x+hh)-x) in that case.
     const parts=grid.length===2?[[x,hh]]:grid.slice(0,-1).map((a,i)=>[a,grid[i+1]-a]);
     for(const [a,hh0] of parts){
      const xs=[a,a+hh0/2,a+hh0];
      records.push({h:hh0,g:xs.map(z=>geometry(cell,profile,z))});
      schedule.push({profile:pi,nominal_step:k,x:xs,h:hh0});
     }
    }
   }
   row([cell.mu,cell.portRatio]);u32(records.length);
   for(const r of records){word(r.h);for(const g of r.g)row(g);}
   rkSteps+=records.length;
   const scheduleBytes=Buffer.from(JSON.stringify(schedule));
   cells.push({stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
    original_profiles:cell.profiles.length,RK_steps:records.length,
    schedule_json_sha256:sha(scheduleBytes)});
  }
  fs.fsyncSync(fd);
  return {file:path.basename(file),bytes,sha256:h.digest('hex'),
   geometry_calls:geometryCalls,RK_steps:rkSteps,angular_cosine_sha256:rowsSHA(cosine),
   angular_sine_sha256:rowsSHA(sine),angular_gram_sha256:rowsSHA(gram),
   schedule_cell_count:cells.length,schedule_json_sha256:sha(JSON.stringify(cells)),
   original_steps_per_profile:p.steps,quadrature:N,shape_dimension:K,complete_state_dimension:size,
   full_stage_count:depth,full_residual_count:(depth+1)*K,
   geometry_is_original_binary64_sample_not_recalibrated:true,
   no_RHS_or_root_or_J_is_called_by_packet_writer:true};
 }finally{fs.closeSync(fd);}
}

const ORIGINAL_CPP_SHA='1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d';
const ORIGINAL_BRIDGE_SHA='3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8';
const LAUNCHER='geometry_20261115_native_trace_variation128.py';
const CPP='geometry_20261115_native_trace_variation128.cpp';
const validSHA=x=>typeof x==='string'&&/^[0-9a-f]{64}$/.test(x);
const stable=x=>Array.isArray(x)?x.map(stable):x&&typeof x==='object'?
 Object.fromEntries(Object.keys(x).sort().map(k=>[k,stable(x[k])])):x;
const equalJSON=(a,b)=>JSON.stringify(stable(a))===JSON.stringify(stable(b));
function requireActions(){
 if(process.env.GITHUB_ACTIONS!=='true'||(process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('The finite-trace derivative experiment runs only in public Actions');
}
function currentIdentity(dn,args,delta,splitIntegrationInterval,identity){
 const p=dn.tail.parameters,{M,K,depth,it,states,target,scales}=args;
 if(M!==112||K!==224||depth!==576||states.length!==577||delta.length!==577||
    p.modes!==M||p.depth!==depth||p.spacing!==2||p.orientation!==1||
    typeof splitIntegrationInterval!=='function'||identity.original_cuspAwareFlow!==true||
    !states.every(v=>v instanceof Float64Array&&v.length===K)||
    !delta.every(v=>v instanceof Float64Array&&v.length===K)||
    !(target instanceof Float64Array)||target.length!==M||
    !(scales instanceof Float64Array)||scales.length!==depth+1||
    !Number.isInteger(it)||it<0||it!==identity.nonlinear_iteration||
    !Number.isInteger(identity.native_call)||identity.native_call<1)
  throw Error('A real complete current native call, all577 state/direction rows and original cusp function are required');
 for(const key of ['source_sha256','hook_sha256','fresh_snapshot_result_sha256','complete_current_delta_sha256'])
  if(!validSHA(identity[key]))throw Error('Actual caller provenance is missing '+key);
 const hashes={states:rowsSHA(states),delta:rowsSHA(delta),target:rowsSHA([target]),scales:rowsSHA([scales]),
  far:rowsSHA([dn.tail.graphs.at(-1)])};
 for(const [key,original] of Object.entries({states:'base-states',target:'cut-target',scales:'original-scales',far:'original-far-graph'}))
  if(hashes[key]!==identity.complete_current_array_sha256?.[original])throw Error('Current snapshot bytes do not match '+original);
 if(hashes.delta!==identity.complete_current_delta_sha256)throw Error('Actual full current direction bytes do not match');
 return {hashes,identity:JSON.parse(JSON.stringify(identity))};
}

// This public writer may be called at an actually supplied fresh correction
// site.  It does not run root/RHS/J, solve, choose a direction or infer a seed.
// The caller owns the new packet until its scientific consumers have finished.
export function writeNativeTraceVariationPacket(dn,args,delta,splitIntegrationInterval,identity,output){
 requireActions();
 if(fileSHA(path.join(here,'geometry_20261115_native_primal128.cpp'))!==ORIGINAL_CPP_SHA||
    fileSHA(path.join(here,'geometry_20261115_native_primal128_bridge.mjs'))!==ORIGINAL_BRIDGE_SHA)
  throw Error('Both original frozen113 sources must remain unchanged');
 const before=currentIdentity(dn,args,delta,splitIntegrationInterval,identity);
 const directory=path.resolve(output),runner=fs.realpathSync(process.env.RUNNER_TEMP??'');
 if(directory===runner||!directory.startsWith(runner+path.sep)||
    !fs.statSync(directory).isDirectory()||fs.lstatSync(directory).isSymbolicLink())
  throw Error('The caller-owned new packet directory must be below actual RUNNER_TEMP');
 const packet=writePacket(path.join(directory,'complete-input.bin'),dn,args,delta,splitIntegrationInterval);
 const after=currentIdentity(dn,args,delta,splitIntegrationInterval,identity);
 if(!equalJSON(before,after))throw Error('The literal packet writer mutated actual input arrays or provenance');
 const binding={schema:'native-finite-root-trace-packet-binding-v1',
  source_file:path.basename(fileURLToPath(import.meta.url)),source_sha256:fileSHA(fileURLToPath(import.meta.url)),
  original_cpp_sha256:ORIGINAL_CPP_SHA,original_packet_writer_bridge_sha256:ORIGINAL_BRIDGE_SHA,
  actual_call_identity:before.identity,input_array_sha256:before.hashes,packet,
  packet_writer_body_byte_identical_to_frozen113:true,
  literal_tables_created_by_original_binary64_definitions_at_this_actual_call:true,
  previous113_packet_bytes_not_available_and_not_claimed_identical:true,
  geometry_and_three_tables_are_independent_fixed_coefficients_for_the_new_variation:true,
  no_native_call_RHS_root_J_or_QR_by_packet_writer:true,
  no_C_equals_F_e_assumption:true,native_accepted:false,
  original_native_acceptance_and_final_checks_not_replaced:true};
 const bytes=Buffer.from(JSON.stringify(binding)+'\n'),file=path.join(directory,'packet-binding.json');
 fs.writeFileSync(file,bytes,{flag:'wx'});
 return {packet:{...packet,path:path.join(directory,packet.file)},
  binding:{file:path.basename(file),path:file,bytes:bytes.length,sha256:sha(bytes)},
  input_array_sha256:before.hashes};
}

// Optional synchronous observer wrapper.  No frozen hook imports or invokes
// it yet: selecting a real call and an explicit run/budget is future wiring.
// Every returned/failed diagnostic leaves original delta and native gates as
// supplied; raw work remains owned temporary material, with no upload step.
export function runNativeTraceVariation128(dn,args,delta,splitIntegrationInterval,identity,options,emit){
 requireActions();
 const {seconds,threads,policy,state_point,launcher_sha256,cpp_sha256}=options;
 if(!Number.isInteger(seconds)||seconds<60||seconds>14400||!Number.isInteger(threads)||threads<1||threads>4||
    !['original','refined'].includes(policy)||!(state_point==='base'||/^trial:[0-9]$/.test(state_point))||
    !validSHA(launcher_sha256)||!validSHA(cpp_sha256)||typeof emit!=='function')
  throw Error('Explicit finite-trace policy/point/source/budget options required');
 const launcher=path.join(here,LAUNCHER),cpp=path.join(here,CPP);
 if(fileSHA(launcher)!==launcher_sha256||fileSHA(cpp)!==cpp_sha256)
  throw Error('Actual new launcher and derivative source must match their declared pins');
 const runner=fs.realpathSync(process.env.RUNNER_TEMP??'');
 const work=fs.mkdtempSync(path.join(runner,'native-finite-trace-'));
 let result;
 try{
  const before=currentIdentity(dn,args,delta,splitIntegrationInterval,identity);
  const inputs=writeNativeTraceVariationPacket(dn,args,delta,splitIntegrationInterval,identity,work);
  emit({event:'native_finite_trace_input',...before.identity,
   experiment_bridge_sha256:fileSHA(fileURLToPath(import.meta.url)),launcher_sha256,cpp_sha256,
   original_cpp_sha256:ORIGINAL_CPP_SHA,packet:inputs.packet,binding:inputs.binding,
   input_array_sha256:before.hashes,seconds,threads,policy,state_point,
   independent_scientific_arithmetic:true,native_accepted:false,new_acceptance_gate:false});
  const out=path.join(work,'result');
  const command=[launcher,'--packet',inputs.packet.path,'--packet-binding',inputs.binding.path,
   '--expected-packet-sha256',inputs.packet.sha256,'--expected-binding-sha256',inputs.binding.sha256,
   '--expected-cpp-sha256',cpp_sha256,'--policy',policy,'--state-point',state_point,
   '--seconds',String(seconds),'--threads',String(threads),'--out',out];
  const child=spawnSync(options.python??'python',command,{shell:false,cwd:work,env:{...process.env},
   stdio:['ignore',2,2],detached:true,timeout:(seconds+600)*1000});
  if(child.error?.code==='ETIMEDOUT'&&Number.isInteger(child.pid)){
   try{process.kill(-child.pid,'SIGTERM');}catch(error){if(error.code!=='ESRCH')throw error;}
  }
  const file=path.join(out,'summary.json');
  if(fs.existsSync(file)){
   const raw=fs.readFileSync(file),summary=JSON.parse(raw);
   if(summary.schema!=='native-finite-root-trace-direction-launch-summary-v1'||
      summary.input_packet.sha256!==inputs.packet.sha256||summary.input_binding.sha256!==inputs.binding.sha256||
      !equalJSON(summary.actual_call_identity,before.identity))throw Error('Returned variation report is not the actual supplied current point');
   result={schema:'native-finite-root-trace-observer-return-v1',
    summary_sha256:sha(raw),summary_bytes:raw.length,
    complete:summary.scientific_report?.complete??false,
    actual_error:summary.actual_error??null,
    experiment_budget_exhausted:summary.scientific_report?.experiment_budget_exhausted??null,
    scientific_report:summary.scientific_report??null,array_receipts:summary.array_receipts??null,
    temporary_output_manifest:summary.temporary_output_manifest??null,
    child_exit:{status:child.status,signal:child.signal,error:child.error?String(child.error):null},
    native_accepted:false,original_delta_returned_unchanged:true,new_acceptance_gate:false};
  }else result={schema:'native-finite-root-trace-observer-return-v1',complete:false,summary_missing:true,
   child_exit:{status:child.status,signal:child.signal,error:child.error?String(child.error):null},
   native_accepted:false,original_delta_returned_unchanged:true,new_acceptance_gate:false};
  const after=currentIdentity(dn,args,delta,splitIntegrationInterval,identity);
  if(!equalJSON(before,after))throw Error('Independent trace variation mutated original inputs');
  // The launcher already printed its bounded scientific summary.  This last
  // event is deliberately small and does not duplicate all stage metadata.
  emit({event:'native_finite_trace_observer_returned',summary_sha256:result.summary_sha256??null,
   summary_bytes:result.summary_bytes??null,complete:result.complete,
   actual_error:result.actual_error??null,child_exit:result.child_exit,
   original_input_array_sha256:before.hashes,
   original_delta_returned_unchanged:true,original_native_loop_not_modified_by_this_module:true,
   no_frozen_source_or_native_acceptance_replaced:true,native_accepted:false});
  return result;
 }finally{fs.rmSync(work,{recursive:true,force:true});}
}
