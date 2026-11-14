// Candidate-only live-native probe. The original constructor and every
// numerical source/method remain unchanged; only the request loop is replaced.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {registerHooks} from 'node:module';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('Actual native candidate probe belongs to this public repository Actions');
const specPath=process.env.VISIBLE_FLEX_ZERO_RK_NATIVE_PROBE_V2_SPEC;
if(!specPath)throw Error('Explicit actual candidate-probe specification required');
const selfPath=fileURLToPath(import.meta.url),here=path.dirname(selfPath);
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const fileSHA=p=>sha(fs.readFileSync(p));
const specRaw=fs.readFileSync(specPath),spec=JSON.parse(specRaw),specSHA=sha(specRaw);
const expectedFrozenSHA='3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054';
const expectedInitializerSHA='c6146b9566031ec636949f94bcbbe4b6fd051002bdb5949a6c70821e0d0c1879';
const expectedGridSHA='b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f';
const frozenPath=path.join(here,'tail_frozen_worker.mjs');
const initializerPath=path.join(here,'geometry_20261114_zero_rk_stage_initializer_v2.mjs');
if(spec.schema!=='actual-same-RK-candidate-native-probe-spec-v2'||
   spec.hook_sha256!==fileSHA(selfPath)||spec.initializer_sha256!==expectedInitializerSHA||
   fileSHA(initializerPath)!==expectedInitializerSHA||
   spec.original_integration_grid_sha256!==expectedGridSHA)
 throw Error('Candidate probe source/specification identity differs');

function stable(v){
 if(Array.isArray(v))return v.map(stable);
 if(v&&typeof v==='object')return Object.fromEntries(Object.keys(v).sort().map(k=>[k,stable(v[k])]));
 return v;
}
function same(a,b){return JSON.stringify(stable(a))===JSON.stringify(stable(b));}
function mathematical(v){return Object.fromEntries(Object.entries(v).filter(([k])=>!spec.io_keys.includes(k)));}
function readVerified(row){
 const b=fs.readFileSync(row.path);
 if(sha(b)!==row.sha256)throw Error('Changed actual candidate-probe input: '+row.path);
 return JSON.parse((b[0]===31&&b[1]===139?zlib.gunzipSync(b):b).toString());
}
function encode(v){
 return JSON.stringify(v,(_k,x)=>{
  if(typeof x==='number'&&!Number.isFinite(x))throw Error('Nonfinite value in a completed evidence record');
  return x;
 })+'\n';
}
function writeJSON(name,value){
 const raw=Buffer.from(encode(value));
 if(raw.length>=1_000_000)throw Error('Use a bounded gzip evidence packet for a large record');
 fs.writeFileSync(path.join(spec.output,name),raw,{flag:'wx'});
 return {file:name,sha256:sha(raw),bytes:raw.length};
}
function writeChunks(stem,rows,header){
 const pending=[rows],out=[];
 while(pending.length){
  const row=pending.shift(),raw=Buffer.from(encode({...header,rows:row})),packed=zlib.gzipSync(raw);
  if(packed.length>=4_000_000&&row.length>1){
   const m=Math.floor(row.length/2);pending.unshift(row.slice(m));pending.unshift(row.slice(0,m));continue;
  }
  if(packed.length>=5_000_000)throw Error('One complete evidence row exceeds the file budget');
  const name=stem+'-'+String(out.length).padStart(3,'0')+'.json.gz';
  fs.writeFileSync(path.join(spec.output,name),packed,{flag:'wx'});
  out.push({file:name,sha256:sha(packed),bytes:packed.length,raw_sha256:sha(raw),rows:row.length});
 }
 return out;
}
function binaryRowsHash(rows){
 const hash=crypto.createHash('sha256');
 for(const row of rows){
  const data=Buffer.allocUnsafe(row.length*8);
  for(let j=0;j<row.length;j++)data.writeDoubleLE(row[j],8*j);
  hash.update(data);
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
function errorRecord(error){
 const stack=String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,
  '<unchanged-in-memory-native-worker>');
 const message=String(error),where=message.match(/(?:block|chart|graph|momentum|height) (\d+) mode (\d+)/);
 return {error:String(error),stack:stack.slice(0,20000),stack_truncated:stack.length>20000,
  initializer_reported_location:where?{raw_stage_or_node_index:Number(where[1]),
   zero_based_mode_index:Number(where[2]),one_based_mode:Number(where[2])+1,
   interpretation:'Exact original initializer error text retained; height propagation labels its source node'}:null,
  observed_failure_location:{stage:error?.tailStage??null,rawCell:error?.tailRawCell??null,
   rawSegment:error?.tailRawSegment??null}};
}

export async function runCandidateProbe(dn,zero,cfg,live,request){
 const started=Date.now(),failure=readVerified(spec.inputs.failed_response),
  recovery=readVerified(spec.inputs.iteration),originalReady=readVerified(spec.inputs.ready),
  cold=readVerified(spec.inputs.cold_probe_summary),first=readVerified(spec.inputs.first_candidate_summary),
  checkpoint=failure.response.checkpoint,
  H=failure.request.height,M=dn.tail.parameters.modes,K=2*M,depth=dn.tail.parameters.depth;
 const launchPath=path.join(spec.output,'verified-launch-intent.json'),launchRaw=fs.readFileSync(launchPath);
 if(sha(launchRaw)!==request.verified_launch_intent_sha256)
  throw Error('The verified current original constructor identity was not supplied');
 const launch=JSON.parse(launchRaw);
 if(launch.spec_sha256!==specSHA||launch.identity_verified_before_stage_pass!==true)
  throw Error('Wait for original constructor, source, config, ready and capacity verification');
 const currentReady=readVerified({path:path.join(spec.output,'original-constructor_ready.json.gz'),
  sha256:launch.complete_current_ready_sha256});
 for(const key of ['storedMetricAdapter','stableGraphAdapter','endpointJacobianAdapter','tailJacobian','tailPredictor'])
  if(!same(live[key],currentReady[key]))throw Error('Live worker and verified ready differ: '+key);
 if(!same(mathematical(cfg),spec.numerical_configuration)||cfg.initialCheckpoint||
    !same(mathematical(dn.tail.parameters),spec.numerical_parameters)||
    !same(mathematical(checkpoint.parameters),spec.numerical_parameters))
  throw Error('Keep every original numerical config and stage parameter');
 for(const key of ['parameters','states','rawNode','rawStates','cutHeight'])
  if(!same(checkpoint[key],recovery.checkpoint[key]))throw Error('Failure/recovery checkpoint differs: '+key);
 if(!same(H,checkpoint.cutHeight)||!same(H,cold.exact_height)||!same(H,first.exact_height)||!Array.isArray(H)||H.length!==M||
    !H.every(Number.isFinite)||!H.some(v=>v!==0)||checkpoint.states.length!==depth+1||
    !checkpoint.states.every(s=>s.length===K&&s.every(Number.isFinite)))
  throw Error('Retain the exact nonzero complete H and original comparison states');
 if(originalReady.warmEmbedding!==null||spec.original_public_run!=='43598917532'||
    cold.evaluation_completed!==true||cold.initial_comparison.exact_numeric_equality!==true||
    first.factory_constructed!==false||first.evaluate_calls!==0||
    first.error!=='Error: Zero-RK initializer: nonfinite or numerically singular stage block 12 mode 92')
  throw Error('The actual baseline is not the selected completed cold replay');
 const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
 if(!sourceRoot)throw Error('The actual restored source root is missing');
 const gridPath=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs');
 if(fileSHA(gridPath)!==expectedGridSHA||
    launch.current_sources[spec.original_integration_grid_source_key]!==expectedGridSHA)
  throw Error('Use integrationGrid from the verified original consumed source, not a rewritten grid');
 const {integrationGrid}=await import(pathToFileURL(gridPath).href);
 const {createZeroRKStageInitializer}=await import(pathToFileURL(initializerPath).href);
 if(typeof integrationGrid!=='function'||typeof createZeroRKStageInitializer!=='function')
  throw Error('Original grid or frozen candidate initializer API differs');
 const target=Float64Array.from(H,v=>v/zero.radius**4),scales=new Float64Array(depth+1);
 // This is exactly the ORIGINAL scaleFor. Candidate transfer denominators
 // never enter this formula, even when their values differ substantially.
 scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
 for(let n=0;n<depth;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
 if(!Array.from(scales).every(v=>Number.isFinite(v)&&v>0))
  throw Error('Original residual scales invalid; no alternative normalization is installed');
 const unchanged=originalSnapshot(dn),header={schema:'actual-same-RK-candidate-probe-evidence-v2',
  spec_sha256:specSHA,failed_response_sha256:spec.inputs.failed_response.sha256,
  cold_probe_summary_sha256:spec.inputs.cold_probe_summary.sha256,
  first_candidate_summary_sha256:spec.inputs.first_candidate_summary.sha256,
  numerical_parameters:spec.numerical_parameters,modes:M,retained_all_modes:true};
 const summary={schema:'actual-same-RK-candidate-native-no-J-probe-v2',finished:false,
  hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,initializer_sha256:expectedInitializerSHA,
  original_integration_grid_sha256:expectedGridSHA,
  original_integration_grid_function_sha256:sha(integrationGrid.toString()),
  verified_launch_intent_sha256:sha(launchRaw),inputs:spec.inputs,
  original_public_run:spec.original_public_run,cold_baseline_public_run:spec.cold_baseline_public_run,
  first_candidate_public_run:spec.first_candidate_public_run,
  candidate_change:spec.candidate_change,
  actual21_merged_error_did_not_identify_det_branch:true,
  numerical_parameters:spec.numerical_parameters,exact_height:Array.from(H),
  exact_height_float64le_sha256:binaryRowsHash([H]),original_radius:zero.radius,
  original_no_J_cold_norm:cold.original_no_J_norm,
  original_recorded_with_J_cold_norm:failure.response.lastIteration.norm,
  original_native_solve_tolerance:spec.original_native_solve_tolerance,
  normalization:'Original scaleFor: H/rCut^4, floor 1e-250, divided by abs(original gains[n][0])',
  actual_evaluation:'dn.tail.evaluate(candidateStates, exactOriginalTarget, false, originalScales)',
  factory_constructed:false,candidate_constructed:false,evaluation_completed:false,evaluate_calls:0,
  nonlinear_solve_called:false,newton_correction_called:false,full_J_requested:false,
  final_audit_requested:false,zero_anchor_recomputed:false,H_modified_or_thresholded:false,
  original_graphs_gains_far_boundary_scales_unchanged:true,
  original_RK_or_guard_changed:false,no_automatic_Newton:true,
  no_new_tail_acceptance:true,task_completed:false,phase:'constructing-same-RK-candidate'};
 const graphs=dn.tail.graphs.map((row,n)=>({node:n,graphs:Array.from(row),
  gains_to_next:n<depth?Array.from(dn.tail.gains[n]):null,original_scale:scales[n]}));
 summary.original_graphs_gains_artifacts=writeChunks('original-graphs-gains',graphs,header);
 summary.original_live_identity=writeJSON('original-live-identity.json',unchanged);
 const eventFiles=[],eventCounts={},pendingEvents=[];
 let eventBatch=0,lastEventLocation=null,actual21Block=null,eventTotal=0;
 function flushEvents(){
  if(!pendingEvents.length)return;
  eventFiles.push(...writeChunks('initializer-v2-construction-'+String(eventBatch++).padStart(3,'0'),
    pendingEvents.splice(0),header));
 }
 function observeConstruction(record){
  if(record.initializer_source_sha256!==expectedInitializerSHA)
   throw Error('Construction diagnostic came from another initializer source');
  eventTotal++;eventCounts[record.kind]=(eventCounts[record.kind]??0)+1;
  lastEventLocation={kind:record.kind,sequence:record.sequence,
    stage:record.stage??null,node:record.node??record.source_node??null,
    mode:record.mode??null,rawCell:record.rawCell??null,rawSegment:record.rawSegment??null};
  if(record.kind==='stage-blocks'&&record.stage===12)
   actual21Block=record.blocks.find(row=>row.zero_based_mode_index===92)??null;
  pendingEvents.push(record);
  if(pendingEvents.length>=32||record.kind.includes('rejected'))flushEvents();
 }
 let candidate=null;
 console.log(encode({event:'same-RK-candidate-construction-start',stages:depth,modes:M,
  retained_original_no_J_baseline:cold.original_no_J_norm}).trim());
 try{
  const sourceIdentity={sourceSHA256:{...launch.current_sources,
    candidate_initializer:expectedInitializerSHA,candidate_probe_hook:fileSHA(selfPath),
    candidate_probe_launcher:spec.source_sha256},
   physicalIdentity:live.storedMetricAdapter,backendIdentity:{
    tailJacobian:live.tailJacobian,tailPredictor:live.tailPredictor,
    endpointJacobianAdapter:live.endpointJacobianAdapter,stableGraphAdapter:live.stableGraphAdapter}};
  const factory=createZeroRKStageInitializer(dn,{radius:zero.radius,integrationGrid,expectedSteps:12,sourceIdentity,
    onConstructionEvent:observeConstruction});
  flushEvents();
  // Retain every completed linear block and the private-chart summary BEFORE
  // predict: its deliberate nonzero-underflow failure must not erase this
  // completed construction evidence. The frozen initializer is not modified.
  summary.factory_constructed=true;
  summary.factory_identity=writeJSON('candidate-factory-identity.json',factory.identity);
  const blockRows=[];
  for(let n=0;n<depth;n++){
   const blocks=[];
   for(let j=0;j<M;j++)blocks.push(factory.stageBlock(n,j));
   blockRows.push({stage:n,mode_2x2_row_major_blocks:blocks});
  }
  summary.zero_linear_stage_blocks=writeChunks('candidate-zero-linear-stage-blocks',blockRows,header);
  summary.completed_linear_blocks_retained_before_prediction=true;
  summary.phase='propagating-complete-nonzero-H';
  candidate=factory.predict(H);
  const states=candidate.states.map(row=>Float64Array.from(row));
  if(states.length!==depth+1||states.some(row=>row.length!==K||!Array.from(row).every(Number.isFinite)))
   throw Error('The candidate does not contain every original finite shooting component');
  if(binaryRowsHash([H])!==summary.exact_height_float64le_sha256)
   throw Error('The original complete H changed during candidate construction');
  if(binaryRowsHash(states)!==candidate.diagnostics.candidateStatesFloat64LESHA256)
   throw Error('Candidate state conversion changed the frozen initializer output');
  summary.candidate_constructed=true;
  summary.initializer_identity=writeJSON('candidate-initializer-identity.json',candidate.diagnostics);
  const nodeRows=states.map((row,n)=>({node:n,state:Array.from(row),
    negative_zero_columns:Array.from(row).flatMap((v,j)=>Object.is(v,-0)?[j]:[])}));
  summary.candidate_state_artifacts=writeChunks('candidate-states',nodeRows,header);
  summary.candidate_checkpoint=writeJSON('candidate-checkpoint.json',{
   schema:'unaccepted-complete-shooting-candidate-chunked-v1',parameters:dn.tail.parameters,
   cutHeight:Array.from(H),rawNode:Array.from(dn.tail.rawNode),nodes:depth+1,shape_dimension:K,
   states_float64le_sha256:candidate.diagnostics.candidateStatesFloat64LESHA256,
   states_artifacts:summary.candidate_state_artifacts,rawStates_definition:'states[rawNode[j]]',
   signed_zero_restoration:'Set listed negative_zero_columns to -0 before checking binary64 state hash',
   initializer_identity:summary.initializer_identity,spec_sha256:specSHA,
   success:false,converged:false,native_tail_response:false,
   scope:'Complete private initial guess only; not an accepted nonlinear response, J or audit.'});
  summary.phase='retaining-candidate-linear-residuals';
  const linearRows=[];
  let linearWorst={normalized:0,kind:'none'};
  for(let n=0;n<depth;n++){
   const residual=Array(K);
   for(let j=0;j<M;j++){
    const t=blockRows[n].mode_2x2_row_major_blocks[j],q=states[n+1][j],pi=states[n+1][M+j];
    residual[j]=(t[0]*q+t[1]*pi)-states[n][j];
    residual[M+j]=(t[2]*q+t[3]*pi)-states[n][M+j];
   }
   const normalized=residual.map((v,j)=>{
    const x=Math.abs(v)/scales[n];
    if(!Number.isFinite(x))throw Error('Constructed zero-linear residual normalization is nonfinite');
    if(x>linearWorst.normalized)linearWorst={normalized:x,residual:v,original_scale:scales[n],
     stage:n,rawCell:dn.tail.cells[n].rawCell,rawSegment:dn.tail.cells[n].rawSegment,
     block:j<M?'Q':'Pi',mode:j%M+1};
    return x;
   });
   linearRows.push({stage:n,original_scale:scales[n],residual,
    original_scale_normalized_absolute_residual:normalized});
  }
  summary.zero_linear_stage_residuals=writeChunks('candidate-zero-linear-residuals',linearRows,header);
  summary.zero_linear_residual_maximum=linearWorst;
  summary.zero_linear_residual_is_not_original_nonlinear_residual=true;
  if(!same(originalSnapshot(dn),unchanged))throw Error('Original methods, graphs, gains, far boundary or stage layout changed');
  summary.phase='original-no-J-evaluate';
  console.log(encode({event:'same-RK-candidate-evaluate-start',stages:depth,modes:M,
   candidate_states_sha256:candidate.diagnostics.candidateStatesFloat64LESHA256,
   zero_linear_residual_maximum:linearWorst}).trim());
  summary.evaluate_calls++;
  // The ONLY original nonlinear stage pass. No call to dn.solve, tail.solve,
  // any Newton/J/audit routine, or a zero-response solve occurs here.
  const ev=dn.tail.evaluate(states,target,false,scales);
  if(ev.flows.length!==depth||ev.residuals.length!==depth||ev.flows.some(f=>f.J!==null))
   throw Error('The unchanged original no-J API returned a different structure');
  const stageRows=[],boundaryRows=[];
  let worst={normalized:0,kind:'none'};
  function inspect(value,scale,where){
   const absolute=Math.abs(value),normalized=absolute/scale;
   if(!Number.isFinite(normalized))throw Error('Original no-J residual normalization is nonfinite');
   if(normalized>worst.normalized)worst={...where,residual:value,absolute,scale,normalized};
   return normalized;
  }
  for(let n=0;n<depth;n++){
   const cell=dn.tail.cells[n],residual=Array.from(ev.residuals[n]),
    normalized=residual.map((v,j)=>inspect(v,scales[n],{kind:'stage',stage:n,
     rawCell:cell.rawCell,rawSegment:cell.rawSegment,column:j,block:j<M?'Q':'Pi',mode:j%M+1}));
   stageRows.push({stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
    original_scale:scales[n],residual,absolute_residual:residual.map(Math.abs),
    original_scale_normalized_absolute_residual:normalized,
    original_mean_height_increment:ev.flows[n].meanHeight});
  }
  for(let j=0;j<M;j++){
   const deep=ev.end[j],cut=states[0][j]-target[j];
   boundaryRows.push({mode:j+1,deep_residual:deep,
    deep_normalized:inspect(deep,scales[depth],{kind:'deep-Robin',node:depth,mode:j+1}),
    cut_residual:cut,cut_normalized:inspect(cut,scales[0],{kind:'cut-height',node:0,mode:j+1})});
  }
  if(worst.normalized!==ev.norm)throw Error('Complete component rows do not reconstruct the original norm');
  const stageFiles=[];
  for(let i=0;i<stageRows.length;i+=64)
   stageFiles.push(...writeChunks('candidate-stage-residuals-'+String(i/64).padStart(3,'0'),stageRows.slice(i,i+64),header));
  Object.assign(summary,{evaluation_completed:true,phase:'completed-original-no-J-pass',
   candidate_original_no_J_norm:ev.norm,candidate_to_original_no_J_cold_norm_ratio:ev.norm/cold.original_no_J_norm,
   difference_from_original_no_J_cold_norm:ev.norm-cold.original_no_J_norm,
   candidate_norm_below_original_solver_tolerance:ev.norm<spec.original_native_solve_tolerance,
   tolerance_comparison_is_not_solve_acceptance:true,
   worst_actual_residual_location:worst,original_scalar_norm_reconstructed_exactly:true,
   completed_stages:depth,full_stage_residual_artifacts:stageFiles,
   boundary_residual_artifacts:writeChunks('candidate-boundary-residuals',boundaryRows,header),
   all_original_no_J_flow_guards_passed:true,minA_minD_not_returned_by_no_J_API:true,
   cause_inferred_by_this_probe:false});
 }catch(error){
  Object.assign(summary,errorRecord(error),{evaluation_completed:false,
   unreturned_private_partial_arrays_not_invented:true,
   complete_nonlinear_residual_table_available:false,cause_inferred_by_this_probe:false});
 }
 flushEvents();
 summary.initializer_construction_evidence={artifacts:eventFiles,events:eventTotal,
  counts:eventCounts,last_event_location:lastEventLocation,
  complete_successful_and_rejected_stage_blocks_retained:true,
  nonfinite_numbers_recorded_by_explicit_classification:true};
 summary.actual21_failed_block_observed_in_v2=actual21Block;
 if(actual21Block)summary.actual21_block_current_determinant_branch=
  !actual21Block.all_entries_finite?'nonfinite-block-entries':
  !actual21Block.products_and_determinant_finite?'nonfinite-products-or-determinant':
  actual21Block.finite_rounded_zero_determinant?'finite-rounded-zero':'finite-nonzero';
 summary.v1_unobserved_block_values_not_retroactively_invented=true;
 const unchangedAfter=same(originalSnapshot(dn),unchanged);
 summary.original_methods_graphs_gains_far_boundary_and_layout_verified_unchanged=unchangedAfter;
 if(!unchangedAfter){
  summary.evaluation_completed=false;
  summary.original_identity_error='Original live data changed; do not use the candidate as an equivalent initial guess';
 }
 summary.finished=true;
 summary.elapsed_seconds=(Date.now()-started)/1000;
 const result=writeJSON('summary.json',summary);
 console.log(encode({event:'same-RK-candidate-probe-complete',candidate_constructed:summary.candidate_constructed,
  evaluation_completed:summary.evaluation_completed,evaluate_calls:summary.evaluate_calls,
  candidate_original_no_J_norm:summary.candidate_original_no_J_norm??null,
  original_no_J_cold_norm:cold.original_no_J_norm,new_tail_acceptance:false,result}).trim());
 return summary;
}

registerHooks({load(url,context,nextLoad){
 const loaded=nextLoad(url,context);
 if(!url.startsWith('file:')||path.resolve(fileURLToPath(url))!==path.resolve(frozenPath))return loaded;
 const source=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 if(sha(source)!==expectedFrozenSHA)throw Error('The frozen worker source changed');
 const before="try{\n  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));";
 if(source.split(before).length!==2)throw Error('Unique original frozen-worker import anchor missing');
 const loopStart="for await(const line of readline.createInterface({input:process.stdin,terminal:false})){";
 const loopEnd='process.stdin.destroy();';
 const replacement=[
  'for await(const probeLine of readline.createInterface({input:process.stdin,terminal:false})){',
  ' const request=JSON.parse(probeLine);if(request.stop)break;',
  ' if(request.zero_rk_native_probe!=='+JSON.stringify(specSHA)+")throw Error('Unverified candidate-probe protocol');",
  ' const probe=await import('+JSON.stringify(import.meta.url)+');',
  ' await probe.runCandidateProbe(dn,zero,cfg,{storedMetricAdapter:storedGeometry.manifest,',
  '  stableGraphAdapter:storedEngineManifest,endpointJacobianAdapter:adapterManifest,',
  '  tailJacobian:backendLabel,tailPredictor:predictorLabel},request);break;',
  '}',
  'process.stdin.destroy();'
 ].join('\n');
 const insert=[
  'const probeLoopStart='+JSON.stringify(loopStart)+',probeLoopEnd='+JSON.stringify(loopEnd)+';',
  'if(source.split(probeLoopStart).length!==2||source.split(probeLoopEnd).length!==2)',
  " throw Error('Unique original request loop missing');",
  'const probeAt=source.indexOf(probeLoopStart),probeEnd=source.indexOf(probeLoopEnd,probeAt)+probeLoopEnd.length;',
  'const probeRemoved=source.slice(probeAt,probeEnd),probeOriginalCompiledSHA=sha256(source);',
  'source=source.slice(0,probeAt)+'+JSON.stringify(replacement)+'+source.slice(probeEnd);',
  'fs.writeFileSync('+JSON.stringify(path.join(spec.output,'instrumentation.json'))+',JSON.stringify({',
  " schema:'actual-same-RK-native-probe-request-loop-only-v2',",
  ' hook_sha256:'+JSON.stringify(fileSHA(selfPath))+',initializer_sha256:'+JSON.stringify(expectedInitializerSHA)+',',
  ' frozen_worker_sha256:'+JSON.stringify(expectedFrozenSHA)+',',
  ' original_compiled_worker_sha256:probeOriginalCompiledSHA,removed_original_loop_sha256:sha256(probeRemoved),',
  ' instrumented_compiled_worker_sha256:sha256(source),only_request_loop_replaced:true,',
  ' constructor_and_initial_and_evaluate_and_numerical_sources_unchanged:true,',
  " replacement_protocol:'One private same-RK candidate and one original no-J evaluate; no solve/Newton/J/audit/zero solve'",
  "},null,2)+'\\n',{flag:'wx'});"
 ].join('\n')+'\n';
 return {...loaded,source:source.replace(before,insert+before)};
}});
