// R441 complete radial readout from the actual refined-resolution frozen-ten450.
// Author: geometry agent (AI), 2026-11-15.
// This is NEW scientific replay, not an unchanged native solve or byte-only audit.
// Every root/RK call is restricted to this repository's public Actions.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {gzipSync,gunzipSync} from 'node:zlib';
import {pathToFileURL,fileURLToPath} from 'node:url';

export const SCHEMA='R441-current-C-resolution450-complete-radial-Cartesian-readout-v1';
const CHECKPOINT='R441-current-continuous-ten-resolution450-physical-DN-checkpoint-v1';
const MODEL='R286-original-stored-continuous-model-convention-C-v1';
const M=112,K=224,SIZE=226,D=576;
const OWNER='geometry_20261115_current_C_general_robin_native.mjs';
const OWNER_SHA='fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349';
const CAPACITY='exact_20261114_tail_capacity_loader.mjs';
const CAPACITY_SHA='07d45b95a970d38489c17142b9202ceeca648a549f76cecaba7c7036261fa395';
const CHECKPOINT_SOURCE='geometry_20261116_continuous_ten_resolution_checkpoint.py';
const CHECKPOINT_SHA='bf7dedd2135e3f6b54bc806a17064428111b502b6ddb8572ec66a883b1ce34ad';
const RELATIVE='repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_relative_development.mjs';
const RELATIVE_SHA='90878cc529bb842743602547d997922de69c8e8966a9fd08ea8a353be1d1ff6e';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const bytes=a=>Buffer.from(a.buffer,a.byteOffset,a.byteLength);
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const word=x=>{const b=Buffer.alloc(8);b.writeDoubleLE(x);return b.toString('hex');};
function actions(){
 if(process.env.GITHUB_ACTIONS!=='true'||process.env.GITHUB_REPOSITORY!=='Rogerhu12/math-research-public')
  throw Error('Scientific replay belongs only to the named public repository Actions');
}
function finite(x,label){if(!Number.isFinite(x))throw Error('Nonfinite '+label);return x;}
function positive(x,label){finite(x,label);if(!(x>0))throw Error('Positive '+label+' required');return x;}
function contained(root,name){
 if(typeof name!=='string'||path.isAbsolute(name))throw Error('Relative contained input required');
 const base=path.resolve(root),p=path.resolve(base,name);
 if(p===base||!p.startsWith(base+path.sep))throw Error('Input escaped its actual owner');
 let v=p;while(v!==base){if(fs.existsSync(v)&&fs.lstatSync(v).isSymbolicLink())throw Error('Payload symlink');v=path.dirname(v);}
 return p;
}
function receipt(file){const b=fs.readFileSync(file);return{file:path.basename(file),bytes:b.length,sha256:sha(b)};}
function readJSON(file,expected){
 const b=fs.readFileSync(file);if(expected&&sha(b)!==expected)throw Error('Actual JSON SHA differs: '+file);
 const compressed=b.length>=2&&b[0]===0x1f&&b[1]===0x8b,decoded=compressed?gunzipSync(b):b;
 return{data:JSON.parse(decoded),receipt:{file:path.basename(file),bytes:b.length,sha256:sha(b),
  gzip_original:compressed,decoded_bytes:decoded.length,decoded_sha256:sha(decoded)}};
}
function member(root,d){
 const file=contained(root,d.file),r=receipt(file);
 if(r.bytes!==d.bytes||r.sha256!==d.sha256)throw Error('Complete parent member differs: '+d.file);
 return file;
}
function writeBytes(file,b){
 const fd=fs.openSync(file,'wx');try{let n=0;while(n<b.length)n+=fs.writeSync(fd,b,n,b.length-n);fs.fsyncSync(fd);}finally{fs.closeSync(fd);}
 return{file:path.basename(file),bytes:b.length,sha256:sha(b)};
}
function writeJSON(file,x){return writeBytes(file,Buffer.from(JSON.stringify(x)+'\n'));}
function append(file,x){
 const b=Buffer.from(JSON.stringify(x)+'\n'),fd=fs.openSync(file,'a');
 try{let n=0;while(n<b.length)n+=fs.writeSync(fd,b,n,b.length-n);fs.fsyncSync(fd);}finally{fs.closeSync(fd);}
}
async function moduleAt(file,expected){
 if(receipt(file).sha256!==expected)throw Error('Bound source differs: '+path.basename(file));
 return import(pathToFileURL(file));
}
class ResourceStop extends Error{constructor(message){super(message);this.name='ResourceStop';}}
class ExternalStop extends Error{constructor(signal){super('Actual external '+signal);this.name='ExternalStop';this.signal=signal;}}
function restoreStates(response){
 const cp=response.checkpoint;
 if(!Array.isArray(cp?.rows)||cp.rows.length!==D+1||!same(cp.rawNode,Array.from({length:9},(_,i)=>72*i)))
  throw Error('All actual577 nodes and raw boundaries required');
 const rows=cp.rows.map((r,n)=>{
  if(r.node!==n||!Array.isArray(r.state)||r.state.length!==K)throw Error('Complete native node/order differs');
  const a=Float64Array.from(r.state);for(const v of a)finite(v,'native shape word');
  const z=r.negative_zero_columns;
  if(!Array.isArray(z)||!same(z,[...new Set(z)].sort((x,y)=>x-y)))throw Error('Original signed-zero list differs');
  for(const j of z){if(!Number.isSafeInteger(j)||j<0||j>=K||a[j]!==0)throw Error('Signed-zero address differs');a[j]=-0;}
  return a;
 });
 const raw=Buffer.concat(rows.map(bytes)),d=cp.raw_states;
 if(d?.dtype!=='<f8'||d.order!=='C'||d.completed!==true||!same(d.shape,[D+1,K])||
    d.bytes!==raw.length||d.sha256!==sha(raw)||!Array.isArray(response.state_sha256)||
    response.state_sha256.length!==D+1||rows.some((a,n)=>response.state_sha256[n]!==sha(bytes(a))))
  throw Error('Complete actual state raw identity differs after signed-zero restoration');
 return rows;
}
function originalGeometry(profile,x){
 const v=profile(x),w=Math.exp(v.logw),w2=Math.exp(2*v.logw);
 positive(v.r,'actual radius');positive(v.drdx,'actual drdx');positive(w,'actual w');
 const wr=w*v.dlogwdx/v.drdx;
 [w2,1+w2,wr].forEach(v=>finite(v,'actual geometry'));
 return{x,r:v.r,drdx:v.drdx,logw:v.logw,dlogwdx:v.dlogwdx,w,w2,E:1+w2,wr,
  words:{x:word(x),r:word(v.r),drdx:word(v.drdx),logw:word(v.logw),
   dlogwdx:word(v.dlogwdx),w:word(w),w2:word(w2),E:word(1+w2),wr:word(wr)}};
}
async function bind(spec,out){
 const computations=path.resolve(spec.computations),directory=path.resolve(spec.checkpoint_directory);
 if(spec.schema!==SCHEMA+'-input-v1')throw Error('An explicit independent radial replay input is required');
 const parent=readJSON(path.join(directory,'checkpoint.json'),spec.checkpoint_sha256);
 const manifest=parent.data;
 if(manifest.schema!==CHECKPOINT||manifest.writer_source?.sha256!==CHECKPOINT_SHA||
    manifest.actual_frozen450_accepted!==true||manifest.actual_dimension!==450||
    manifest.actual_active_parameter_count!==0||manifest.finite_fullDN_accepted_by_original_gates!==true||
    manifest.source453_rows_dropped_relabelled_as_accepted450!==false||
    manifest.run_id!==process.env.GITHUB_RUN_ID||manifest.source_commit!==process.env.GITHUB_SHA)
  throw Error('This actual job must first produce a genuine independent full450 checkpoint');
 if(receipt(path.join(computations,CHECKPOINT_SOURCE)).sha256!==CHECKPOINT_SHA||
    receipt(path.join(computations,CAPACITY)).sha256!==CAPACITY_SHA)
  throw Error('The actual checkpoint reader/capacity source differs');
 const responseFile=member(directory,manifest.members.final_native);
 const configFile=member(directory,manifest.members.native_configuration);
 const response=readJSON(responseFile).data,config=readJSON(configFile).data;
 const actual=manifest.original_native_binding;
 if(response.schema!=='current-C-full112-general-Robin-native-owner-v1'||response.actual_nonlinear_solve!==true||
    response.converged!==true||response.failed!==false||response.audit?.actual_all_stage_finite_audit!==true||
    !Array.isArray(response.heightJetJacobian)||response.heightJetJacobian.length!==338*112||
    !same(response.identity,actual.actual_owner)||response.call!==manifest.final_native_binding.actual_call||
    response.checkpoint.actual_current_native_call!==response.call||
    config.geometry_result_sha256!==manifest.members.native_geometry_result.sha256||
    !same(config.source_sha256,actual.source_sha256)||
    !same(config.original_runtime_sha256,actual.original_runtime_sha256))
  throw Error('Bind the true complete final native response, mean fields, audit and all112 sensitivity');
 for(const [k,v] of Object.entries({max_iterations:32,line_search_trials:10,nonlinear_tolerance:2e-9,sensitivity_eta:0}))
  if(config[k]!==v)throw Error('Original native policy differs at '+k);
 if(config.repository!==process.env.GITHUB_REPOSITORY||config.model_schema!==MODEL||
    !Number.isSafeInteger(config.steps)||config.steps<=0||
    !Number.isSafeInteger(config.quadrature)||config.quadrature<=896||config.quadrature%2!==0||
    manifest.N!==config.quadrature||manifest.actual_resolution?.field_angular_quadrature!==config.quadrature||
    manifest.actual_resolution?.native_quadrature!==config.quadrature||
    manifest.actual_resolution?.native_steps_per_stage!==config.steps||
    actual.actual_owner?.parameter_record?.quadrature!==config.quadrature||
    actual.actual_owner?.parameter_record?.steps!==config.steps)
  throw Error('The original complete current-C quadrature and stage schedule differ');
 for(const [name,h] of Object.entries(config.source_sha256)){
  if(path.basename(name)!==name||receipt(path.join(computations,name)).sha256!==h)
   throw Error('Actual complete current source closure differs: '+name);
 }
 const workerNames=Object.entries(config.source_sha256)
  .filter(([n,h])=>n.endsWith('_native_worker.mjs')&&h===response.checkpoint.source_sha256).map(([n])=>n);
 if(workerNames.length!==1)throw Error('The actual final worker is not uniquely bound');
 const worker=await moduleAt(path.join(computations,workerNames[0]),response.checkpoint.source_sha256);
 const report=readJSON(path.join(spec.geometry_directory,'result.json'),config.geometry_result_sha256).data;
 const samplerNames=Object.entries(config.source_sha256)
  .filter(([n,h])=>n.endsWith('.py')&&h===report.source_sha256).map(([n])=>n);
 if(samplerNames.length!==1||!same(report.geometry,actual.geometry_descriptor)||
    !same(report.actual_original_input_binding,actual.original_C_input_binding))
  throw Error('The actual original complete current geometry differs');
 const geometry=worker.loadGeometry(spec.geometry_directory,config.geometry_result_sha256,
  report.source_sha256,config.steps,out);
 const ownerModule=await moduleAt(path.join(computations,OWNER),OWNER_SHA);
 const runtime=await ownerModule.loadOriginalRuntime(path.resolve(spec.source_topic),computations,config.original_runtime_sha256);
 const relativeFile=path.join(path.resolve(spec.source_topic),RELATIVE);
 const relative=await moduleAt(relativeFile,RELATIVE_SHA);
 if(!same(geometry.numeric_geometry_identity,response.checkpoint.current_C_geometry_identity)||
    !same(geometry.original_C_input_binding,actual.original_C_input_binding))
  throw Error('The replay geometry is not this accepted checkpoint geometry');
 return{parent,manifest,response,config,geometry,runtime,relative,states:restoreStates(response),
  sources:{owner:receipt(path.join(computations,OWNER)),relative:receipt(relativeFile),
   actual_worker:receipt(path.join(computations,workerNames[0])),actual_sampler:receipt(path.join(computations,samplerNames[0])),
   checkpoint:receipt(path.join(computations,CHECKPOINT_SOURCE)),capacity:receipt(path.join(computations,CAPACITY)),
   original_runtime:runtime.receipts,own:receipt(fileURLToPath(import.meta.url))}};
}
export async function produce(spec){
 actions();const start=performance.now();
 positive(spec.budget_seconds,'explicit radial readout budget');
 if(!Number.isSafeInteger(spec.free_bytes_reserve)||spec.free_bytes_reserve<0)throw Error('Explicit disk reserve required');
 const out=path.resolve(spec.out),temp=path.resolve(process.env.RUNNER_TEMP??'');
 if(!process.env.RUNNER_TEMP||out===temp||!out.startsWith(temp+path.sep)||fs.existsSync(out))
  throw Error('Use a fresh owned temporary output');
 fs.mkdirSync(out,{recursive:true});const nodeDir=path.join(out,'nodes');fs.mkdirSync(nodeDir);
 const ledger=path.join(out,'complete-radial-nodes.jsonl'),stageLedger=path.join(out,'actual-stage-replay.jsonl');
 let stopSignal=null;const signalHandler=s=>{stopSignal=s;};
 const term=()=>signalHandler('SIGTERM'),interrupt=()=>signalHandler('SIGINT');
 process.on('SIGTERM',term);process.on('SIGINT',interrupt);
 let input=null,error=null,stage=0,step=0,rootCalls=0,rkCalls=0,rows=[],partialSmall=[],partialBackground=[];
 let meanIncrements=null,backgroundIncrements=null,completedStages=0;
 const check=()=>{
  if(stopSignal)throw new ExternalStop(stopSignal);
  if((performance.now()-start)/1000>=spec.budget_seconds)throw new ResourceStop('Explicit radial readout wall budget exhausted');
  const st=fs.statfsSync(out,{bigint:true}),free=st.bavail*st.bsize;
  if(free<BigInt(spec.free_bytes_reserve))throw new ResourceStop('Owned output disk reserve reached');
 };
 try{
  check();input=await bind(spec,out);check();
  const {config,geometry,runtime,relative,states}=input,steps=config.steps,N=config.quadrature;
  const total=D*steps+1;rows=Array(total).fill(null);partialSmall=new Float64Array(total);
  partialBackground=new Float64Array(total);meanIncrements=new Float64Array(D);
  backgroundIncrements=new Float64Array(D);
  const engineCache=new Map();
  function engineFor(mu){
   const key=word(mu);if(engineCache.has(key)){const v=engineCache.get(key);engineCache.delete(key);engineCache.set(key,v);return v;}
   const args={modes:M,spacing:2,quadrature:N,mu,orientation:1,
    projectionFloor:config.projection_floor,cuspAwareFlow:false};
   const original=runtime.createFourierRootSplitFluxEngine(args);
   const engine=runtime.createNoJMatchedVariationalEngine(args,original,{
    createFourierProductJacobianEngine:runtime.createFourierProductJacobianEngine,
    splitIntegrationInterval:runtime.splitIntegrationInterval});
   const value={engine,evaluator:runtime.createMomentumPhysicalJetEvaluator(engine,{spacing:2})};
   engineCache.set(key,value);while(engineCache.size>2)engineCache.delete(engineCache.keys().next().value);
   return value;
  }
  function savePoint(node,n,x,inputState,multiplier,origin){
   check();if(rows[node])throw Error('Duplicate complete radial node '+node);
   const cell=geometry.cells[n],profile=cell.profiles[0],{engine,evaluator}=engineFor(cell.mu);
   const y=new Float64Array(SIZE);y.set(inputState.slice(0,K));
   if(multiplier!==1)for(let j=0;j<M;j++)y[M+j]*=multiplier;
   const rt=engine.root(y,profile,x);rootCalls++;
   const jets=evaluator(y,profile,x);rootCalls++;
   const developed=relative.relativeActualDevelopment(rt.g,rt.e.rows,jets.perAngle);
   const g=originalGeometry(profile,x);
   if(node%steps===0&&!Object.is(g.r,geometry.node_radii[node/steps]))
    throw Error('An original shooting-node radial word differs from its current geometry');
   if(!(jets.minA>0&&jets.minD>0)||jets.perAngle.length!==N)throw Error('Actual root/jet domain did not return at node '+node);
   const raw=Buffer.alloc(N*12*8);
   for(let a=0;a<N;a++){
    const v=jets.perAngle[a],value=[developed.dx[a],developed.dy[a],v.height,
     developed.dxR[a],developed.dyR[a],v.ur,developed.dxT[a],developed.dyT[a],
     v.ut,v.urr,v.urt,v.utt];
    for(let j=0;j<12;j++)raw.writeDoubleLE(finite(value[j],'complete radial component'),8*(a*12+j));
   }
   const name='node-'+String(node).padStart(6,'0')+'.f64le.gz';
   const compressed=gzipSync(raw,{level:6}),r=writeBytes(path.join(nodeDir,name),compressed);
   const row={node,originalStage:n,step_coordinate:x,step_coordinate_word:word(x),
    source:origin,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
    pi_multiplier:multiplier,pi_multiplier_word:word(multiplier),
    file:'nodes/'+name,bytes:r.bytes,sha256:r.sha256,rawSha256:sha(raw),
    raw_bytes:raw.length,shape:[N,12],dtype:'<f8',order:'C',geometry:g,
    nonmean_state_sha256:sha(bytes(y.slice(0,K))),
    mean_slots_zeroed_only_for_this_shape_readout:true,
    minimum_original_A:jets.minA,minimum_original_D:jets.minD,
    sample_metric_error:developed.actualMetricRelativeOperatorError,
    formal_height_curvature:jets.formalHeightCurvature,
    horizontal_second_radial_derivative_exported:false};
   rows[node]=row;append(ledger,row);
  }
  for(stage=0;stage<D;stage++){
   check();const cell=geometry.cells[stage],profile=cell.profiles[0],{engine}=engineFor(cell.mu);
   if(stage===0)savePoint(0,0,1,states[0],cell.portRatio,'actual accepted outer shooting state with original port');
   savePoint((stage+1)*steps,stage,0,states[stage+1],1,'actual accepted inner shooting state');
   let y=new Float64Array(SIZE);y.set(states[stage+1]);
   for(step=0;step<steps;step++){
    check();const x=step/steps,h=1/steps;
    y=engine.rk4(y,profile,x,h);rkCalls++;
    if(step+1<steps){
     const j=step+1,node=(stage+1)*steps-j;
     savePoint(node,stage,j/steps,y,1,'original full226 RK step return at declared next-grid coordinate');
     partialSmall[node]=y[K];partialBackground[node]=y[K+1];
     append(stageLedger,{event:'actual-interior-association',stage,step:step+1,node,
      original_RK_x_word:word(x),original_RK_h_word:word(h),
      original_RK_x_plus_h_word:word(x+h),declared_node_x_word:word(j/steps),
      step_end_and_next_grid_word_identical:Object.is(x+h,j/steps),
      original_RK_and_endpoint_association_not_exact_C_trajectory_certified:true});
    }
   }
   meanIncrements[stage]=finite(y[K],'small mean increment');
   backgroundIncrements[stage]=finite(y[K+1],'background mean increment');
   let gap=0;for(let j=0;j<K;j++)gap=Math.max(gap,Math.abs(y[j]/(j<M?1:cell.portRatio)-states[stage][j]));
   append(stageLedger,{event:'actual-stage-return',stage,steps,
    small_mean_increment:meanIncrements[stage],background_increment:backgroundIncrements[stage],
    small_mean_word:word(meanIncrements[stage]),background_word:word(backgroundIncrements[stage]),
    endpoint_canonical_max_gap:gap,diagnostic_only_not_a_new_acceptance_gate:true,
    original_full226_RK_schedule_retained:true});
   completedStages++;
   if(completedStages%24===0)process.stdout.write(JSON.stringify({event:'current-C-radial-progress',completed_stages:completedStages,total_stages:D,
    actual_nodes:rows.filter(Boolean).length,root_calls:rootCalls,RK_calls:rkCalls,
    elapsed_seconds:(performance.now()-start)/1000})+'\n');
  }
  if(rows.some(v=>!v))throw Error('A complete stage or radial node is missing');
  const small=new Float64Array(D+1),background=new Float64Array(D+1);
  for(let n=D-1;n>=0;n--){small[n]=small[n+1]+meanIncrements[n];background[n]=background[n+1]+backgroundIncrements[n];}
  for(let n=0;n<rows.length;n++){
   const i=Math.floor(n/steps),rem=n%steps;
   const sm=rem===0?small[i]:small[i+1]+partialSmall[n];
   const bg=rem===0?background[i]:background[i+1]+partialBackground[n];
   rows[n].meanPerturbationInnerAnchor=finite(sm,'complete small mean');
   rows[n].backgroundRKInnerAnchor=finite(bg,'complete background mean');
   rows[n].meanHeightInnerAnchor=finite(sm+bg,'both native means');
  }
  for(let n=1;n<rows.length;n++)if(!(rows[n-1].geometry.r>rows[n].geometry.r))
   throw Error('Actual complete radial words are not strictly ordered at '+n);
  const complete={schema:SCHEMA+'-complete',finished:true,completedNodes:rows.length,
   run_id:process.env.GITHUB_RUN_ID,source_commit:process.env.GITHUB_SHA,
   originalStages:D,steps,angular:N,rows,
   smallMeanIncrements:Array.from(meanIncrements),backgroundRKIncrements:Array.from(backgroundIncrements),
   original_checkpoint:input.parent.receipt,current_target_identity:input.manifest.current_target_identity,
   original_native_binding:input.manifest.original_native_binding,
   final_native:input.manifest.members.final_native,source_sha256_at_start:input.sources,
   all_current_modes_and_DC_and_both_means_retained:true,
   source_geometry_is_numeric_representative_not_common_exact_C_member:true,
   raw_columns:['dx','dy','shape_height','dx_r','dy_r','full_height_r',
    'dx_theta','dy_theta','height_theta','full_height_rr','height_rtheta','height_thetatheta'],
   true_same_C_infinite_trajectory_or_rigorous_replay_error_certified:false,
   original_accepted_field_replaced_or_reaccepted:false};
  const record=writeJSON(path.join(out,'complete.json'),complete);
  const result={schema:SCHEMA,completed:true,source:receipt(fileURLToPath(import.meta.url)),
   run_id:process.env.GITHUB_RUN_ID,source_commit:process.env.GITHUB_SHA,
   checkpoint:input.parent.receipt,current_target_identity:input.manifest.current_target_identity,
   final_native:input.manifest.members.final_native,complete:record,
   actual_stages:completedStages,actual_nodes:rows.length,root_calls:rootCalls,RK_calls:rkCalls,
   actual_original_geometry_usage:geometry.actual_field_usage(),
   node_ledger:receipt(ledger),stage_ledger:receipt(stageLedger),pending:[],
   resource_partial:false,error:null,elapsed_seconds:(performance.now()-start)/1000,
   no_new_BVP_or_native_solve:true,new_root_and_RK_scientific_replay:true,
   exact_radial_Hermite_and_shared_B_to_be_defined_separately:true,
   geometry_or_metric_acceptance_created:false};
  writeJSON(path.join(out,'result.json'),result);
  process.stdout.write(JSON.stringify({event:'current-C-radial-return',schema:SCHEMA,completed:true,
   stages:completedStages,nodes:rows.length,complete:record,root_calls:rootCalls,RK_calls:rkCalls,
   new_scientific_replay:true,geometric_acceptance:false})+'\n');
  return result;
 }catch(e){
  error={type:e.name??'Error',message:String(e),stack:e.stack??null};
  const total=input?D*input.config.steps+1:null;
  const result={schema:SCHEMA,completed:false,source:receipt(fileURLToPath(import.meta.url)),
   run_id:process.env.GITHUB_RUN_ID,source_commit:process.env.GITHUB_SHA,
   checkpoint:input?.parent.receipt??null,current_target_identity:input?.manifest.current_target_identity??null,
   completed_stages:completedStages,current_stage:stage,current_step:step,
   actual_nodes:rows.filter(Boolean).length,total_nodes:total,
   node_ledger:fs.existsSync(ledger)?receipt(ledger):null,
   stage_ledger:fs.existsSync(stageLedger)?receipt(stageLedger):null,
   pending:{all_uncommitted_stages:[completedStages,D],
    uncreated_node_indices:total===null?null:Array.from({length:total},(_,i)=>i).filter(i=>!rows[i]),
    mean_back_accumulation_and_final_radial_order_unpaid:true,
    complete_Hermite_background_and_closed_geometry_unpaid:true},
   resource_partial:e instanceof ResourceStop,external_interruption:e instanceof ExternalStop,
   error,root_calls:rootCalls,RK_calls:rkCalls,elapsed_seconds:(performance.now()-start)/1000,
   geometry_or_metric_acceptance_created:false};
  writeJSON(path.join(out,'result.json'),result);
  process.stdout.write(JSON.stringify({event:'current-C-radial-return',schema:SCHEMA,completed:false,
   completed_stages:completedStages,actual_nodes:result.actual_nodes,root_calls:rootCalls,RK_calls:rkCalls,
   resource_partial:result.resource_partial,external_interruption:result.external_interruption,
   error,complete_result:receipt(path.join(out,'result.json'))})+'\n');
  return result;
 }finally{process.off('SIGTERM',term);process.off('SIGINT',interrupt);}
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 (async()=>{
  if(process.argv.length!==3)throw Error('One bound radial-readout JSON input required');
  const spec=readJSON(path.resolve(process.argv[2])).data;
  const result=await produce(spec);if(!result.completed)process.exitCode=2;
 })().catch(e=>{process.stderr.write(JSON.stringify({event:'current-C-radial-fatal',error:String(e),stack:e.stack??null})+'\n');process.exitCode=1;});
}
