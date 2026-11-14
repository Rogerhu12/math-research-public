// One actual cold-state diagnostic protocol; original numerical methods stay unchanged.
// Node --import preload.  It changes only the frozen worker's request loop,
// retaining the original constructor, full modes, RK count and evaluate(false).
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import readline from 'node:readline';
import {fileURLToPath} from 'node:url';
import {registerHooks} from 'node:module';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('Actual native replay belongs to this public repository Actions');
const specPath=process.env.VISIBLE_FLEX_COLD_REPLAY_SPEC;
if(!specPath)throw Error('Explicit actual failed-input replay specification required');
const selfPath=fileURLToPath(import.meta.url),here=path.dirname(selfPath);
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const fileSHA=p=>sha(fs.readFileSync(p));
const specRaw=fs.readFileSync(specPath),spec=JSON.parse(specRaw),specSHA=sha(specRaw);
const expectedFrozenSHA='3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054';
const frozenPath=path.join(here,'tail_frozen_worker.mjs');
if(spec.schema!=='actual-cold-tail-stage-replay-spec-v1'||spec.hook_sha256!==fileSHA(selfPath))
 throw Error('Cold replay source/specification identity differs');

function stable(v){
 if(Array.isArray(v))return v.map(stable);
 if(v&&typeof v==='object')return Object.fromEntries(Object.keys(v).sort().map(k=>[k,stable(v[k])]));
 return v;
}
function same(a,b){return JSON.stringify(stable(a))===JSON.stringify(stable(b));}
function mathematical(v){return Object.fromEntries(Object.entries(v).filter(([k])=>!spec.io_keys.includes(k)));}
function readVerified(row){
 const b=fs.readFileSync(row.path);
 if(sha(b)!==row.sha256)throw Error('Changed original replay input: '+row.path);
 return JSON.parse((b[0]===31&&b[1]===139?zlib.gunzipSync(b):b).toString());
}
function encode(v){
 return JSON.stringify(v,(_k,x)=>{
  if(typeof x==='number'&&!Number.isFinite(x))throw Error('Nonfinite value in a completed diagnostic record');
  return x;
 })+'\n';
}
function writeJSON(name,value){
 const raw=Buffer.from(encode(value)),p=path.join(spec.output,name);
 if(raw.length>=1_000_000)throw Error('Use a gzip evidence file for a large diagnostic');
 fs.writeFileSync(p,raw,{flag:'wx'});
 return {file:name,sha256:sha(raw),bytes:raw.length};
}
function writeChunks(stem,rows,header){
 const pending=[rows],out=[];
 while(pending.length){
  const row=pending.shift(),raw=Buffer.from(encode({...header,rows:row})),packed=zlib.gzipSync(raw);
  if(packed.length>=4_000_000&&row.length>1){
   const m=Math.floor(row.length/2);pending.unshift(row.slice(m));pending.unshift(row.slice(0,m));continue;
  }
  if(packed.length>=5_000_000)throw Error('One original diagnostic row exceeds the file budget');
  const name=stem+'-'+String(out.length).padStart(3,'0')+'.json.gz';
  fs.writeFileSync(path.join(spec.output,name),packed,{flag:'wx'});
  out.push({file:name,sha256:sha(packed),bytes:packed.length,raw_sha256:sha(raw),rows:row.length});
 }
 return out;
}

export async function runColdReplay(dn,zero,cfg){
 const started=Date.now(),failure=readVerified(spec.inputs.failed_response),
  recovery=readVerified(spec.inputs.iteration),originalReady=readVerified(spec.inputs.ready),
  checkpoint=failure.response.checkpoint,H=failure.request.height,M=dn.tail.parameters.modes,
  K=2*M,depth=dn.tail.parameters.depth;
 if(!same(mathematical(cfg),spec.numerical_configuration)||cfg.initialCheckpoint)
  throw Error('Keep the original cold configuration, including all numerical settings');
 if(!same(mathematical(dn.tail.parameters),spec.numerical_parameters)||
    !same(mathematical(checkpoint.parameters),spec.numerical_parameters))
  throw Error('Actual stage parameters differ');
 if(!failure.response.failed||failure.response.lastIteration?.iteration!==0||
    recovery.status!=='iteration-recovery-only'||recovery.call!==1||recovery.iteration.iteration!==0)
  throw Error('This replay requires the actual unaccepted first iteration');
 for(const key of ['parameters','states','rawNode','rawStates','cutHeight'])
  if(!same(checkpoint[key],recovery.checkpoint[key]))throw Error('Failure/recovery checkpoint differs: '+key);
 if(!same(H,checkpoint.cutHeight)||!Array.isArray(H)||H.length!==M||
    !H.every(Number.isFinite)||!H.some(v=>v!==0)||checkpoint.states.length!==depth+1||
    !checkpoint.states.every(s=>s.length===K&&s.every(Number.isFinite)))
  throw Error('Retain the exact nonzero complete height and complete saved states');
 if(originalReady.warmEmbedding!==null||spec.original_public_run!=='43598917532')
  throw Error('The recorded initial worker was not the selected cold run');
 const states=checkpoint.states.map(row=>Float64Array.from(row)),
  target=Float64Array.from(H,v=>v/zero.radius**4),initial=dn.tail.initial(target),
  scales=new Float64Array(depth+1);
 // This is exactly scaleFor from the frozen source, including its mode-0 rule.
 scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
 for(let n=0;n<depth;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
 if(!Array.from(scales).every(v=>Number.isFinite(v)&&v>0))
  throw Error('The original residual scale is nonfinite or nonpositive; no replacement scale is installed');
 const differences=[],nodeSummaries=[];
 let signedZeroDifferences=0,maximumDifference=0,worstDifference=null;
 for(let n=0;n<=depth;n++){
  if(initial[n].length!==K)throw Error('Original initial-state dimension differs');
  let qmax=0,pmax=0,qmode=1,pmode=1;
  for(let j=0;j<K;j++){
   const old=states[n][j],cold=initial[n][j];
   if(!Number.isFinite(cold))throw Error('The original cold initial state is nonfinite');
   if(old!==cold){
    const d=Math.abs(old-cold),record={node:n,column:j,block:j<M?'Q':'Pi',mode:j%M+1,
      recorded:old,original_cold:cold,absolute_difference:d};
    differences.push(record);if(d>maximumDifference){maximumDifference=d;worstDifference=record;}
   }else if(!Object.is(old,cold))signedZeroDifferences++;
   if(j<M&&Math.abs(old)>qmax){qmax=Math.abs(old);qmode=j+1;}
   if(j>=M&&Math.abs(old)>pmax){pmax=Math.abs(old);pmode=j-M+1;}
  }
  nodeSummaries.push({node:n,original_scale:scales[n],max_abs_Q:qmax,max_abs_Pi:pmax,Q_mode:qmode,Pi_mode:pmode});
 }
 const header={schema:'actual-cold-tail-replay-evidence-v1',spec_sha256:specSHA,
  failed_response_sha256:spec.inputs.failed_response.sha256,iteration_sha256:spec.inputs.iteration.sha256,
  numerical_parameters:spec.numerical_parameters,modes:M,retained_all_modes:true};
 const graphRows=dn.tail.graphs.map((row,n)=>({node:n,graphs:Array.from(row),
   gains_to_next:n<depth?Array.from(dn.tail.gains[n]):null,original_scale:scales[n]}));
 const graphFiles=writeChunks('original-graphs-gains',graphRows,header),
  comparisonFiles=writeChunks('original-cold-comparison',differences,header),
  stateSummaryFiles=writeChunks('saved-node-magnitudes',nodeSummaries,header);
 const summary={schema:'actual-cold-tail-no-J-stage-replay-v1',finished:false,
  hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,original_public_run:spec.original_public_run,
  inputs:spec.inputs,numerical_parameters:spec.numerical_parameters,
  exact_height:H,normalization:'Original scaleFor: target H/rCut^4, floor 1e-250, repeated division by abs(gains[n][0])',
  original_recorded_with_J_norm:failure.response.lastIteration.norm,
  actual_original_initial_function_sha256:sha(dn.tail.initial.toString()),
  actual_original_evaluate_function_sha256:sha(dn.tail.evaluate.toString()),
  initial_comparison:{exact_numeric_equality:differences.length===0,compared_entries:(depth+1)*K,
   nonzero_differences:differences.length,signed_zero_only_differences:signedZeroDifferences,
   maximum_absolute_difference:maximumDifference,worst:worstDifference,artifacts:comparisonFiles},
  original_graphs_gains_artifacts:graphFiles,saved_state_magnitude_artifacts:stateSummaryFiles,
  actual_evaluation:'dn.tail.evaluate(savedStates, exactOriginalTarget, false, originalScales)',
  nonlinear_solve_called:false,newton_correction_called:false,full_J_requested:false,zero_anchor_recomputed:false,
  H_modified_or_thresholded:false,initial_state_replaced:false,original_RK_or_guard_changed:false,
  no_new_tail_acceptance:true,task_completed:false};
 console.log(encode({event:'cold-replay-evaluate-start',stages:depth,modes:M,
  all_saved_states_equal_original_initial:differences.length===0}).trim());
 try{
  // The ONLY stage pass.  It calls the original no-J cellFlow/rk4/guards.
  const ev=dn.tail.evaluate(states,target,false,scales);
  if(ev.flows.length!==depth||ev.residuals.length!==depth||ev.flows.some(f=>f.J!==null))
   throw Error('The original no-J stage API returned a different structure');
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
  if(worst.normalized!==ev.norm)throw Error('Retained per-component residuals do not reconstruct the original evaluate norm');
  // Bound genuine evidence chunks without omitting modes or failed cells.
  const grouped=[];for(let i=0;i<stageRows.length;i+=64)grouped.push(stageRows.slice(i,i+64));
  const stageFiles=[];
  for(let i=0;i<grouped.length;i++)stageFiles.push(...writeChunks('stage-residuals-'+String(i).padStart(3,'0'),grouped[i],header));
  Object.assign(summary,{finished:true,evaluation_completed:true,original_no_J_norm:ev.norm,
   difference_from_recorded_with_J_norm:ev.norm-failure.response.lastIteration.norm,
   worst_actual_residual_location:worst,original_scalar_norm_reconstructed_exactly:true,
   completed_stages:depth,full_stage_residual_artifacts:stageFiles,
   boundary_residual_artifacts:writeChunks('boundary-residuals',boundaryRows,header),
   all_original_no_J_flow_guards_passed:true,
   minA_minD_not_returned_by_no_J_API:true,
   cause_inferred_by_this_probe:false});
 }catch(error){
  Object.assign(summary,{finished:true,evaluation_completed:false,
   error:String(error),stack:String(error?.stack??error),
   observed_failure_location:{stage:error?.tailStage??null,rawCell:error?.tailRawCell??null,
    rawSegment:error?.tailRawSegment??null},
   complete_residual_table_available:false,cause_inferred_by_this_probe:false});
 }
 summary.elapsed_seconds=(Date.now()-started)/1000;
 const result=writeJSON('summary.json',summary);
 console.log(encode({event:'cold-replay-complete',evaluation_completed:summary.evaluation_completed,
  original_no_J_norm:summary.original_no_J_norm??null,result}).trim());
 return summary;
}

registerHooks({load(url,context,nextLoad){
 const loaded=nextLoad(url,context);
 if(!url.startsWith('file:')||path.resolve(fileURLToPath(url))!==path.resolve(frozenPath))return loaded;
 const source=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 if(sha(source)!==expectedFrozenSHA)throw Error('The frozen worker source changed');
 const before="try{\n  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));";
 if(source.split(before).length!==2)throw Error('Unique frozen worker import anchor missing');
 const loopStart="for await(const line of readline.createInterface({input:process.stdin,terminal:false})){";
 const loopEnd='process.stdin.destroy();';
 const replacement=`for await(const probeLine of readline.createInterface({input:process.stdin,terminal:false})){
 const request=JSON.parse(probeLine);if(request.stop)break;
 if(request.cold_replay!==${JSON.stringify(specSHA)})throw Error('Unverified cold replay protocol');
 const probe=await import(${JSON.stringify(import.meta.url)});
 await probe.runColdReplay(dn,zero,cfg);break;
}
process.stdin.destroy();`;
 const insert=`
const probeLoopStart=${JSON.stringify(loopStart)},probeLoopEnd=${JSON.stringify(loopEnd)};
if(source.split(probeLoopStart).length!==2||source.split(probeLoopEnd).length!==2)
 throw Error('Unique original request loop missing');
const probeAt=source.indexOf(probeLoopStart),probeEnd=source.indexOf(probeLoopEnd,probeAt)+probeLoopEnd.length;
const probeRemoved=source.slice(probeAt,probeEnd),probeOriginalCompiledSHA=sha256(source);
source=source.slice(0,probeAt)+${JSON.stringify(replacement)}+source.slice(probeEnd);
fs.writeFileSync(${JSON.stringify(path.join(spec.output,'instrumentation.json'))},JSON.stringify({
 schema:'actual-cold-replay-request-loop-only-v1',hook_sha256:${JSON.stringify(fileSHA(selfPath))},
 frozen_worker_sha256:${JSON.stringify(expectedFrozenSHA)},
 original_compiled_worker_sha256:probeOriginalCompiledSHA,removed_original_loop_sha256:sha256(probeRemoved),
 instrumented_compiled_worker_sha256:sha256(source),only_request_loop_replaced:true,
 constructor_and_initial_and_evaluate_and_numerical_sources_unchanged:true,
 replacement_protocol:'One verified original no-J evaluate; no dn.solve/Newton/zero solve'
},null,2)+'\\n',{flag:'wx'});
`;
 return {...loaded,source:source.replace(before,insert+before)};
}});
