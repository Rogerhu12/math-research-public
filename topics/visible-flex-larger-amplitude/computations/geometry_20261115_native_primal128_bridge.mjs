// Request113: export the same fresh full native input to an independent
// binary128 evaluator.  This observer never replaces the original delta,
// native residual, ten original trials, tolerance, final J or final audit.
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

export function runPrimal128Experiment(dn,args,delta,splitIntegrationInterval,identity,emit){
 if(process.env.GITHUB_ACTIONS!=='true'||(process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('The independent complete primal experiment belongs only to public Actions');
 const p=dn.tail.parameters,{M,K,depth,it,states,target,scales}=args;
 if(it!==0||M!==112||K!==224||depth!==576||states.length!==577||delta.length!==577||
    p.modes!==M||p.depth!==depth||p.spacing!==2||p.orientation!==1||identity.original_cuspAwareFlow!==true||
    typeof splitIntegrationInterval!=='function'||!states.every(v=>v.length===K)||!delta.every(v=>v.length===K))
  throw Error('The actual full first-correction 112/576 context is required');
 const executable=process.env.VISIBLE_FLEX_PRIMAL128_EXECUTABLE,
  expected=process.env.VISIBLE_FLEX_PRIMAL128_EXECUTABLE_SHA256,
  cppSHA=process.env.VISIBLE_FLEX_PRIMAL128_CPP_SHA256,
  seconds=Number(process.env.VISIBLE_FLEX_PRIMAL128_SECONDS),
  threads=Number(process.env.VISIBLE_FLEX_PRIMAL128_THREADS);
 if(!executable||!path.isAbsolute(executable)||!expected||fileSHA(executable)!==expected||
    !/^[0-9a-f]{64}$/.test(cppSHA??'')||!Number.isInteger(seconds)||seconds<60||seconds>14400||
    !Number.isInteger(threads)||threads<1||threads>4)throw Error('Explicit compiled binary128 source/executable/budget binding required');
 const tmp=path.resolve(process.env.RUNNER_TEMP??''),work=fs.mkdtempSync(path.join(tmp,'native113-primal-'));
 if(work===tmp||!work.startsWith(tmp+path.sep)||fs.lstatSync(work).isSymbolicLink())throw Error('Independent owned RUNNER_TEMP directory required');
 const original={states:rowsSHA(states),delta:rowsSHA(delta),target:rowsSHA([target]),scales:rowsSHA([scales]),
  far:rowsSHA([dn.tail.graphs.at(-1)])};
 let result;
 try{
  const packet=writePacket(path.join(work,'complete-input.bin'),dn,args,delta,splitIntegrationInterval);
  // A literal no-J control on the same base, separate from the already paid
  // fresh matched-withJ primal.  It neither selects nor changes a direction.
  let original64Base;
  try{
   const control=args.evaluate(states,target,false,scales);
   original64Base={complete:true,norm:control.norm,
    stage_residual_sha256:rowsSHA(control.residuals),far_residual_sha256:rowsSHA([control.end]),
    original_row_count:(depth+1)*K,stage_count:control.residuals.length,
    fresh_withJ_primal_norm:args.ev.norm,
    same_numeric_norm_as_fresh_withJ:control.norm===args.ev.norm,
    noJ_minA_minD_not_tracked_by_original_evaluate:true};
  }catch(error){
   original64Base={complete:false,error:String(error),stage:error?.tailStage??null,
    rawCell:error?.tailRawCell??null,rawSegment:error?.tailRawSegment??null};
  }
  emit({event:'native113_full_primal_input',...identity,source_sha256:fileSHA(fileURLToPath(import.meta.url)),
   driver_source_sha256:identity.source_sha256,cpp_source_sha256:cppSHA,executable_sha256:expected,packet,input_array_sha256:original,
   original64_full_noJ_base_control:original64Base,additional_original_noJ_control_calls:1,
   seconds,threads,policies:[{label:'binary128-e-original-inner-stop',stop:'original binary64 8e-14',fallback:'original binary64 5e-12'},
    {label:'binary128-e-refined-inner-stop',stop:'binary128 decimal 1e-28',fallback:'binary128 decimal 5e-27'}],
   each_policy_states:['base',1,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625,.001953125],
   uses_same_original_fresh_R273_delta:true,original64_J_is_not_claimed_exact_DF_of_new128_evaluator:true,
   does_not_replace_native_acceptance_or_final_audit:true,native_accepted:false});
  // Child marker lines stream to the existing bounded scalar watcher while
  // the synchronous native correction is paused.  A separate tiny text copy
  // is consumed below; raw residual vectors remain owned temporary files.
  const completed=spawnSync(executable,[path.join(work,'complete-input.bin'),work,String(seconds),String(threads)],
   {shell:false,cwd:work,env:{...process.env,OMP_NUM_THREADS:String(threads)},stdio:['ignore',2,2],timeout:(seconds+120)*1000});
  const reportFile=path.join(work,'evaluation-records.jsonl'),records=[];
  if(fs.existsSync(reportFile)){
   const raw=fs.readFileSync(reportFile);
   for(const line of raw.toString('utf8').split('\n')){
    if(!line.trim())continue;if(!line.startsWith('NATIVE113 '))throw Error('Explicit binary128 marker required');
    const r=JSON.parse(line.slice(10));
    if(r.event==='native113_complete_primal_evaluation'){
     const f=path.resolve(r.temporary_residual_file);
     if(path.dirname(f)!==work||fs.lstatSync(f).isSymbolicLink()||fs.statSync(f).size!==r.temporary_residual_bytes)
      throw Error('Owned full binary128 residual file/size required');
     r.residual_array_sha256=fileSHA(f);r.residual_array_storage='runner-temporary binary128 little-endian; removed after SHA';
     delete r.temporary_residual_file;
     emit({event:'native113_complete_primal_array_identity',policy:r.policy,trial:r.trial,
      rows:r.all_rows,rows_completed:r.rows_completed,bytes:r.temporary_residual_bytes,
      sha256:r.residual_array_sha256,complete:r.complete,not_a_native_acceptance:true});
     fs.unlinkSync(f);
    }
    records.push(r);
   }
   result={schema:'native113-primal128-independent-evaluation-summary-v1',
    report_file_bytes:raw.length,report_file_sha256:sha(raw),input_packet:packet,
    record_count:records.length,evaluations:records.filter(r=>r.event==='native113_complete_primal_evaluation').map(r=>({
     policy:r.policy,trial:r.trial,alpha:r.alpha,complete:r.complete,norm_decimal:r.norm_decimal,
     strict_decrease_from_same_policy_base:r.strict_decrease_from_same_policy_base,
     below_original_native_tolerance:r.below_original_native_tolerance??null,
     worst_original_row:r.worst_original_row??null,root_statistics:r.root_statistics,
     residual_array_sha256:r.residual_array_sha256,budget:r.experiment_budget_exhausted})),
    finished:records.find(r=>r.event==='native113_binary128_finished')??null,
    exit:{status:completed.status,signal:completed.signal,error:completed.error?String(completed.error):null},
    original_delta_returned_unchanged:true,native_accepted:false};
  }else result={schema:'native113-primal128-independent-evaluation-summary-v1',report_missing:true,
   exit:{status:completed.status,signal:completed.signal,error:completed.error?String(completed.error):null},native_accepted:false};
  for(const [key,rows] of Object.entries({states,delta,target:[target],scales:[scales],far:[dn.tail.graphs.at(-1)]}))
   if(rowsSHA(rows)!==original[key])throw Error('Independent experiment mutated original '+key);
  emit({event:'native113_primal128_experiment_returned',summary:result,
   original_ten64_noJ_trials_follow_unchanged:true,experiment_is_not_a_new_acceptance_gate:true});
  return result;
 }finally{
  fs.rmSync(work,{recursive:true,force:true});
 }
}
