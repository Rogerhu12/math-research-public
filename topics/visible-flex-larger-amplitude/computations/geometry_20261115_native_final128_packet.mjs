// New physical-readout inputs for one still-live original DN configuration.
// This exporter calls geometry/profile factories and creates their literal64
// tables. It never calls root, RHS, RK, solve, evaluate, J or audit.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
function fileSHA(file){
 const h=crypto.createHash('sha256'),fd=fs.openSync(file,'r'),block=Buffer.allocUnsafe(1<<20);
 try{for(;;){const n=fs.readSync(fd,block,0,block.length,null);if(!n)break;h.update(block.subarray(0,n));}}
 finally{fs.closeSync(fd);}return h.digest('hex');
}
function assert(test,label){if(!test)throw Error(label);}
function descriptor(file,root){return {file:path.relative(root,file),bytes:fs.statSync(file).size,sha256:fileSHA(file)};}
function bytes64(values){
 const b=Buffer.allocUnsafe(values.length*8);
 for(let i=0;i<values.length;i++){
  assert(Number.isFinite(values[i]),'Finite original geometry/table word');
  b.writeDoubleLE(values[i],i*8);
 }
 return b;
}
function words(g){return [g.r,g.drdx,g.w,g.w2,g.E];}
function fullWords(g){return [...words(g),g.dlogwdx];}

export function writeNativeFinal128PhysicalPacket(dn,splitIntegrationInterval,
 {outDirectory,primalPacket,primalPacketSHA,primalBinding,primalBindingSHA,
  configurationIdentity,sourceReceipts,auditSteps}){
 assert(process.env.GITHUB_ACTIONS==='true'&&
  (process.env.GITHUB_REPOSITORY??'').toLowerCase()==='rogerhu12/math-research-public',
  'Public Actions only');
 assert(dn?.tail&&Array.isArray(dn.tail.cells),'Actual live DN required');
 assert(typeof splitIntegrationInterval==='function','Original splitIntegrationInterval required');
 const root=fs.realpathSync(process.env.RUNNER_TEMP??''),out=path.resolve(outDirectory);
 assert(out.startsWith(root+path.sep)&&!fs.existsSync(out),'Fresh RUNNER_TEMP output required');
 assert(fileSHA(primalPacket)===primalPacketSHA&&fileSHA(primalBinding)===primalBindingSHA,
  'Exact still-live primal packet and binding required');
 const p=dn.tail.parameters,M=p.modes,K=2*M,N=p.quadrature,depth=p.depth;
 assert(M===112&&K===224&&depth===576&&N>0&&(N&(N-1))===0,'Full actual finite layout');
 assert(Number.isSafeInteger(auditSteps)&&auditSteps>0&&auditSteps<=100000,'Explicit original audit steps');
 assert(dn.tail.cells.length===depth,'All576 original cells');
 assert(configurationIdentity&&typeof configurationIdentity==='object','Actual configuration identity');
 assert(Array.isArray(sourceReceipts)&&sourceReceipts.length>0,'Complete original source receipts');
 for(const item of sourceReceipts)
  assert(typeof item.file==='string'&&Number.isSafeInteger(item.bytes)&&/^[0-9a-f]{64}$/.test(item.sha256),
   'Original source receipt');
 fs.mkdirSync(out,{recursive:false});
 const packetFile=path.join(out,'physical-input.packet'),fd=fs.openSync(packetFile,'wx');
 const chunks=[];
 function put(name,bytes){
  const start=fs.fstatSync(fd).size;fs.writeSync(fd,bytes);
  chunks.push({name,offset:start,bytes:bytes.length,sha256:sha(bytes)});
 }
 function u32(name,n){const b=Buffer.alloc(4);b.writeUInt32LE(n);put(name,b);}
 function f64(name,a){put(name,bytes64(a));}
 const sq2=Math.sqrt(2),freq=Array.from({length:M},(_,j)=>p.spacing*(j+1));
 const physicalCos=[],physicalSin=[],theta=[];
 // Independent expressions from f6tail_momentum_physical_jets.mjs.
 // Their words are retained even if they differ from the root tables.
 for(let n=0;n<N;n++){
  for(let j=0;j<=M;j++)physicalCos.push(j?sq2*Math.cos(freq[j-1]*2*Math.PI*n/N):1);
  for(let j=0;j<M;j++)physicalSin.push(sq2*Math.sin(freq[j]*2*Math.PI*n/N));
  theta.push(2*Math.PI*n/N);
 }
 const fft=[];
 for(let len=2;len<=N;len*=2){
  for(const inverse of [false,true]){
   const a=(inverse?2:-2)*Math.PI/len;fft.push(Math.cos(a),Math.sin(a));
  }
 }
 const c0=dn.tail.cells[0],profile0=c0.profiles.at(-1),cut=c0.engine.geometry(profile0,1);
 const rho=2**p.a;
 const policies={differenceStep:1e-4,scaleFloor:1e-250,relativeStepFloor:.1};
 const functionReceipts=[];
 let queryCount=0,atomicSteps=0;
 try{
  put('magic',Buffer.from('QPFI1281','ascii'));
  u32('modes',M);u32('quadrature',N);u32('depth',depth);u32('auditSteps',auditSteps);
  f64('rho-and-original-difference-policy',[rho,policies.differenceStep,policies.scaleFloor,policies.relativeStepFloor]);
  f64('cut-geometry-with-dlogwdx',fullWords(cut));
  // Preserve the old binary64 r**4 as an independent provenance literal.
  // The declared new local height extension uses the explicitly written
  // binary128 (r*r)*(r*r); it is not the derivative of a rounding map.
  f64('physical-literal-constants',[cut.r**4,2*Math.PI,Math.sqrt(2),Math.sqrt(12)]);
  f64('physical-jet-frequency-table',freq);
  f64('physical-jet-cosine-table',physicalCos);f64('physical-jet-sine-table',physicalSin);
  f64('material-angle-literal-table',theta);f64('original-FFT-base-twiddles',fft);
  const stageQueries=[];
  for(let n=0;n<depth;n++){
   const c=dn.tail.cells[n],queries=[];
   for(let segment=0;segment<c.profiles.length;segment++){
    const profile=c.profiles[segment];
    for(let k=0;k<=auditSteps;k++){
     const x=k/auditSteps,g=c.engine.geometry(profile,x),advance=[];
     if(k<auditSteps){
      const h=1/auditSteps;
      const grid=splitIntegrationInterval(x,x+h,profile.integrationBreakpoints);
      assert(Array.isArray(grid)&&grid.length>=2,'Original audit interval split');
      // The original wrapper retains h exactly when no interior split exists.
      for(let z=0;z<grid.length-1;z++){
       const a=grid[z],hs=grid.length===2?h:grid[z+1]-grid[z];
       advance.push({h:hs,g:[c.engine.geometry(profile,a),
        c.engine.geometry(profile,a+hs/2),c.engine.geometry(profile,a+hs)]});
      }
     }
     queries.push({segment,k,x,g,advance});queryCount++;atomicSteps+=advance.length;
    }
   }
   stageQueries.push({stage:n,queries:queries.length,profiles:c.profiles.length,
    rawCell:c.rawCell,rawSegment:c.rawSegment});
   u32('stage-'+n+'-query-count',queries.length);
   for(let qi=0;qi<queries.length;qi++){
    const q=queries[qi],prefix='stage-'+n+'-query-'+qi;
    u32(prefix+'-segment',q.segment);u32(prefix+'-k',q.k);
    f64(prefix+'-x-and-geometry',[q.x,...fullWords(q.g)]);
    u32(prefix+'-advance-atomic-steps',q.advance.length);
    for(let k=0;k<q.advance.length;k++)
     f64(prefix+'-advance-'+k,[q.advance[k].h,...q.advance[k].g.flatMap(words)]);
   }
   functionReceipts.push({stage:n,geometry_sha256:sha(Buffer.from(c.engine.geometry.toString())),
    root_sha256:sha(Buffer.from(c.engine.root.toString())),
    rhs_sha256:sha(Buffer.from(c.engine.rhs.toString())),rk4_sha256:sha(Buffer.from(c.engine.rk4.toString())),
    profile_source_sha256:c.profiles.map(f=>sha(Buffer.from(f.toString())))});
  }
  fs.closeSync(fd);
  const binding={
   schema:'native-persistent128-physical-query-packet-binding-v1',
   exporter_source_sha256:fileSHA(new URL(import.meta.url)),
   original_primal_packet:{file:path.basename(primalPacket),bytes:fs.statSync(primalPacket).size,sha256:primalPacketSHA},
   original_primal_binding:{file:path.basename(primalBinding),bytes:fs.statSync(primalBinding).size,sha256:primalBindingSHA},
   configuration_identity:configurationIdentity,source_receipts:sourceReceipts,
   complete_parameters:p,M,K,N,depth,auditSteps,query_count:queryCount,atomic_audit_steps:atomicSteps,
   original_split_function_sha256:sha(Buffer.from(splitIntegrationInterval.toString())),
   cut_geometry:cut,cut_rho:rho,original_difference_policy:policies,
   physical_height_extension:'Q_target(H+dH)=saved_Q_target+diag(1/binary128((r*r)*(r*r)))*dH',
   physical_height_extension_is_not_derivative_of_IEEE_division_map:true,
   all_physical_jet_tables_independently_exported:true,all_original_fft_base_twiddles_exported:true,
   model_constants_and_query_points_are_fixed_literal_binary64:true,
   nonlinear_metric_sin_cos_after_development_require_binary128_transcendentals:true,
   root_RHS_RK_solve_J_audit_called_by_exporter:false,
   actual128_final_state_not_created_or_selected_by_exporter:true,
   native_accepted:false,source_function_receipts:functionReceipts,
   chunks,packet:descriptor(packetFile,out),stages:stageQueries,
  };
  const bindingFile=path.join(out,'physical-input-binding.json');
  fs.writeFileSync(bindingFile,JSON.stringify(binding,null,2)+'\n',{flag:'wx'});
  return {schema:'native-persistent128-physical-query-packet-export-v1',
   packet:{...descriptor(packetFile,out),path:packetFile},
   binding:{...descriptor(bindingFile,out),path:bindingFile},
   query_count:queryCount,atomic_audit_steps:atomicSteps,native_accepted:false};
 }catch(error){
  try{fs.closeSync(fd);}catch{}
  fs.writeFileSync(path.join(out,'export-failure.json'),JSON.stringify({
   schema:'native-persistent128-physical-query-packet-export-v1',complete:false,
   error:String(error),chunks_written:chunks.length,query_count:queryCount,
   root_RHS_RK_solve_J_audit_called:false,native_accepted:false})+'\n');
  throw error;
 }
}
