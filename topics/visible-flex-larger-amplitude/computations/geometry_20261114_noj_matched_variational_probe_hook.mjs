// One original no-J evaluation of actual61's last complete current state.
// Only the worker request loop is replaced. No RHS, RK, root, evaluate,
// graph, scale, line-search, solver, or cache implementation is modified.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import readline from 'node:readline';
import os from 'node:os';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {registerHooks} from 'node:module';

if(process.env.GITHUB_ACTIONS!=='true'||
   (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('This actual no-J replay belongs only to the public repository Actions');
if(os.endianness()!=='LE')throw Error('Record original Float64Array words on the actual little-endian runtime');
const selfPath=fileURLToPath(import.meta.url),here=path.dirname(selfPath);
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const fileSHA=p=>sha(fs.readFileSync(p));
const unpack=b=>b[0]===31&&b[1]===139?zlib.gunzipSync(b):b;
const rawView=x=>Buffer.from(x.buffer,x.byteOffset,x.byteLength);
const variable='VISIBLE_FLEX_NOJ_MATCHED_PRIMAL_PROBE_SPEC';
const specPath=process.env[variable];
if(!specPath)throw Error('A complete original same-state specification is required');
const specRaw=fs.readFileSync(specPath),spec=JSON.parse(unpack(specRaw)),specSHA=sha(specRaw);
const frozenPath=path.join(here,'tail_frozen_worker.mjs');
const frozenSHA='3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054';
const coreSHA='ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3';
const evalSHA='9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9';
const savedStateSHA='b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013';
const snapshotSHA='5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286';
if(spec.schema!=='actual61-noJ-matched-variational-probe-spec-v1'||
   spec.hook_sha256!==fileSHA(selfPath)||spec.current_state_sha256!==savedStateSHA||
   spec.original_snapshot_result_sha256!==snapshotSHA)
 throw Error('The actual same-state source/specification differs');

function stable(v){
 if(Array.isArray(v))return v.map(stable);
 if(v&&typeof v==='object')return Object.fromEntries(Object.keys(v).sort().map(k=>[k,stable(v[k])]));
 return v;
}
function equal(a,b,label){if(JSON.stringify(stable(a))!==JSON.stringify(stable(b)))throw Error('Same-state identity: '+label);}
function mathematical(v){return Object.fromEntries(Object.entries(v).filter(([k])=>!spec.io_keys.includes(k)));}
function numericalSources(v){return Object.fromEntries(Object.entries(v).filter(([k])=>!['input_config','runtime_config'].includes(k)));}
function safe(root,name){
 if(typeof name!=='string'||path.isAbsolute(name)||name.split(/[\\/]/).includes('..'))throw Error('Relative original evidence path required');
 const p=path.resolve(root,name),rel=path.relative(path.resolve(root),p);
 if(rel.startsWith('..')||path.isAbsolute(rel)||!fs.statSync(p).isFile())throw Error('Missing or escaping original evidence');
 return p;
}
function receipt(p,root=spec.output){
 const raw=fs.readFileSync(p);return {file:path.relative(root,p),bytes:raw.length,sha256:sha(raw)};
}
function verified(row){
 const raw=fs.readFileSync(row.path);
 equal(raw.length,row.bytes,'original evidence length '+row.path);equal(sha(raw),row.sha256,'original evidence SHA '+row.path);
 return JSON.parse(unpack(raw));
}
function numberRecord(v){
 if(typeof v!=='number')throw Error('A real original Number value is required');
 const b=Buffer.alloc(8);b.writeDoubleLE(v);
 return {value:Number.isFinite(v)?v:null,float64le_hex:b.toString('hex'),
  classification:Number.isNaN(v)?'NaN':v===Infinity?'positive-infinity':v===-Infinity?'negative-infinity':Object.is(v,-0)?'negative-zero':'finite'};
}
function decodeNumber(record){
 const raw=Buffer.from(record.float64le_hex,'hex');if(raw.length!==8)throw Error('Original scalar bits required');
 const value=raw.readDoubleLE();equal(numberRecord(value),record,'saved original number classification/value/bits');return value;
}
function encode(value){
 return Buffer.from(JSON.stringify(value,(_k,v)=>{
  if(typeof v==='number'&&!Number.isFinite(v))throw Error('Keep original nonfinite values in explicit number records');
  return v;
 })+'\n');
}
function writeJSON(name,value,{compressed=false}={}){
 const raw=encode(value),packed=compressed?zlib.gzipSync(raw):raw,p=path.join(spec.output,name);
 if(packed.length>=4_900_000)throw Error('Use complete bounded metadata packets without deleting fields');
 fs.writeFileSync(p,packed,{flag:'wx'});
 const out={file:name,bytes:packed.length,sha256:sha(packed)};
 if(compressed)Object.assign(out,{raw_bytes:raw.length,raw_sha256:sha(raw),encoding:'json-gzip'});
 return out;
}
function saveArray(name,shape,rows){
 const width=shape.slice(1).reduce((a,b)=>a*b,1),parts=[];
 if(rows.length!==shape[0])throw Error('Every actual output row is required: '+name);
 for(const row of rows){if(!(row instanceof Float64Array)||row.length!==width)throw Error('Original typed output row required: '+name);parts.push(rawView(row));}
 const raw=Buffer.concat(parts),file='large-arrays/'+name+'.f64le';
 fs.writeFileSync(path.join(spec.output,file),raw,{flag:'wx'});
 return {name,file,dtype:'<f8',order:'C',shape,bytes:raw.length,sha256:sha(raw)};
}
function readArray(binding){
 const entry=binding.entry,shape=entry.shape,width=shape.slice(1).reduce((a,b)=>a*b,1),parts=[];
 if(entry.dtype!=='<f8'||entry.order!=='C'||entry.completed!==true)throw Error('Complete saved little-endian array required');
 let row=0;
 for(let i=0;i<entry.chunks.length;i++){
  const item=entry.chunks[i],p=safe(binding.directory,item.file),raw=fs.readFileSync(p);
  equal([item.array,item.chunk_index,item.row_start],[entry.name,i,row],'complete original chunk order');
  if(!Number.isInteger(item.row_stop)||item.row_stop<=row||item.row_stop>shape[0])throw Error('Original chunk coverage');
  equal(raw.length,(item.row_stop-row)*width*8,'original chunk length');
  equal(raw.length,item.bytes,'original descriptor bytes');equal(sha(raw),item.sha256,'original chunk SHA');
  equal(sha(raw),item.raw_sha256,'original chunk raw SHA');parts.push(raw);row=item.row_stop;
 }
 const raw=Buffer.concat(parts);equal(row,shape[0],'all original rows');equal(raw.length,entry.total_bytes,'all original bytes');
 equal(sha(raw),entry.raw_sha256,'complete original array SHA');
 const rows=[];let negativeZeros=0;
 for(let n=0;n<shape[0];n++){
  const values=new Float64Array(width);
  for(let j=0;j<width;j++){
   const value=raw.readDoubleLE((n*width+j)*8);
   if(!Number.isFinite(value))throw Error('Finite saved input words required');
   values[j]=value;if(Object.is(value,-0))negativeZeros++;
  }
  if(!rawView(values).equals(raw.subarray(n*width*8,(n+1)*width*8)))throw Error('Original input word restoration differs');
  rows.push(values);
 }
 return {raw,rows,shape,entry,negativeZeros};
}
function binaryRowsHash(rows){const h=crypto.createHash('sha256');for(const row of rows)h.update(rawView(row instanceof Float64Array?row:Float64Array.from(row)));return h.digest('hex');}
function liveIdentity(dn){
 return {parameters:mathematical(dn.tail.parameters),rawNode:Array.from(dn.tail.rawNode),
  graphs_float64le_sha256:binaryRowsHash(dn.tail.graphs),gains_float64le_sha256:binaryRowsHash(dn.tail.gains),
  far_graph_float64le_sha256:binaryRowsHash([dn.tail.graphs.at(-1)]),
  initial_function_sha256:sha(dn.tail.initial.toString()),evaluate_function_sha256:sha(dn.tail.evaluate.toString()),
  tail_solve_function_sha256:sha(dn.tail.solve.toString()),dn_solve_function_sha256:sha(dn.solve.toString()),
  stages:dn.tail.cells.map(c=>({rawCell:c.rawCell,rawSegment:c.rawSegment,portRatio:c.portRatio,mu:c.mu,
    profiles:c.profiles.map(p=>Array.from(p.integrationBreakpoints??[]))}))};
}
function originalMethods(dn){
 const names=['root','rhs','rk4','rhsWithJacobian','flowStateWithJacobian'],sources={},engines=[],seen=new Map();
 for(let n=0;n<dn.tail.cells.length;n++){
  const engine=dn.tail.cells[n].engine;if(seen.has(engine))continue;
  const methods={};for(const name of names){const src=engine[name].toString(),digest=sha(src);sources[digest]={name,source:src};methods[name]=digest;}
  seen.set(engine,engines.length);engines.push({first_stage:n,method_sha256:methods});
 }
 return {original_evaluate_sha256:sha(dn.tail.evaluate.toString()),
  original_evaluate_source:dn.tail.evaluate.toString(),engine_instances:engines,sources,
  Function_toString_unmodified:true,source_text_observation_only:true};
}
function location(kind,n,j,M,K,cells){
 if(kind==='stage')return {kind,stage:n,rawCell:cells[n].rawCell,rawSegment:cells[n].rawSegment,
  column:j,block:j<M?'Q':'Pi',mode:j%M+1,frequency:2*(j%M+1),global_row:M+n*K+j};
 return {kind,node:kind==='cut'?0:n,column:j,mode:j+1,frequency:2*(j+1),
  global_row:kind==='cut'?j:M+n*K+j};
}
function scanNorm(residuals,cut,end,scales,M,K,cells){
 let reconstructed=0,worst=null,nonfiniteTerms=0;
 function inspect(value,scale,where){
  const normalized=Math.abs(value)/scale;
  if(!Number.isFinite(normalized))nonfiniteTerms++;
  if(worst===null||normalized>worst.comparison_value)worst={...where,comparison_value:normalized,
   residual:numberRecord(value),scale:numberRecord(scale),normalized_absolute:numberRecord(normalized)};
  reconstructed=Math.max(reconstructed,normalized);
 }
 for(let n=0;n<residuals.length;n++)for(let j=0;j<K;j++)inspect(residuals[n][j],scales[n],location('stage',n,j,M,K,cells));
 for(let j=0;j<M;j++)inspect(end[j],scales[residuals.length],location('far',residuals.length,j,M,K,cells));
 for(let j=0;j<M;j++)inspect(cut[j],scales[0],location('cut',0,j,M,K,cells));
 if(worst)delete worst.comparison_value;
 return {reconstructed_norm:numberRecord(reconstructed),worst,nonfiniteTerms};
}
function compareRow(before,after,scale,base){
 const rawA=rawView(before),rawB=rawView(after),difference=new Float64Array(before.length);
 let different=0,numericallyDifferent=0,maxAbs=0,maxNormalized=0,worst=null,nonfinite=0;
 for(let j=0;j<before.length;j++){
  if(rawA.readBigUInt64LE(j*8)!==rawB.readBigUInt64LE(j*8))different++;
  if(before[j]!==after[j])numericallyDifferent++;
  const value=after[j]-before[j],absolute=Math.abs(value),normalized=absolute/scale;difference[j]=value;
  if(!Number.isFinite(normalized))nonfinite++;
  if(worst===null||normalized>maxNormalized){maxNormalized=normalized;maxAbs=absolute;worst={...base,column:j,
    block:base.stage!==undefined?(j<112?'Q':'Pi'):base.kind==='far'?'Pi-minus-GQ':'Q',
    mode:j%112+1,frequency:2*(j%112+1),
    saved_withJ:numberRecord(before[j]),actual_noJ:numberRecord(after[j]),difference:numberRecord(value),
    original_scale:numberRecord(scale),normalized_difference:numberRecord(normalized)};}
 }
 return {difference,summary:{bit_different_words:different,numerically_different_words:numericallyDifferent,
  maximum_absolute_difference:numberRecord(maxAbs),maximum_original_scale_difference:numberRecord(maxNormalized),
  nonfinite_difference_terms:nonfinite,worst}};
}

let protocolCalls=0;
export async function runMatchedPrimalProbe(dn,zero,cfg){
 if(protocolCalls++!==0)throw Error('One selected-stage diagnostic protocol request only');
 const started=Date.now(),launch=JSON.parse(fs.readFileSync(path.join(spec.output,'verified-launch-intent.json')));
 equal(launch.spec_sha256,specSHA,'verified launch specification');
 equal(launch.identity_verified_before_evaluation,true,'verified original ready/config/sources');
 equal(numericalSources(launch.current_sources),spec.original_source_sha256,'all original consumed source bytes');
 equal(mathematical(cfg),spec.numerical_configuration,'the same original numerical configuration');
 equal(liveIdentity(dn),spec.original_live_identity,'all original profiles/graphs/gains/far/methods');
 equal(sha(dn.tail.evaluate.toString()),evalSHA,'original evaluate source remains untouched');
 const modulePath=path.join(here,spec.candidate_module.file);
 equal(fileSHA(modulePath),spec.candidate_module.sha256,'new candidate source bytes');
 const productPath=path.join(process.env.VISIBLE_FLEX_SOURCE_TOPIC,'scripts/78718-tail-fourier-product-jacobian.mjs'),
  cuspPath=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs');
 equal(fileSHA(productPath),spec.original_dependencies.product_jacobian,'original local product-J formula');
 equal(fileSHA(cuspPath),spec.original_dependencies.local_cusp_grid,'original local cusp interval splitting');
 const {createNoJMatchedVariationalEngine}=await import(pathToFileURL(modulePath)),
  {createFourierProductJacobianEngine}=await import(pathToFileURL(productPath)),
  {splitIntegrationInterval}=await import(pathToFileURL(cuspPath));
 const context=verified(spec.snapshot_inputs.context),manifest=verified(spec.snapshot_inputs.manifest),
  snapshot=verified(spec.snapshot_inputs.result),arrays={};
 equal(sha(fs.readFileSync(spec.snapshot_inputs.result.path)),snapshotSHA,'same actual61 final snapshot');
 equal(snapshot.current_state_sha256,savedStateSHA,'same actual current state');
 const listed=new Map(manifest.arrays.map(a=>[a.name,a]));
 for(const [name,binding] of Object.entries(spec.original_arrays)){
  equal(binding.entry,listed.get(name),'same original input array descriptor '+name);
  arrays[name]=readArray(binding);
  equal(arrays[name].entry.raw_sha256,context.raw_array_sha256[name],'same full original input bytes '+name);
 }
 const M=112,K=224,size=226,steps=dn.tail.parameters.steps,
  cases=[],outputArrays=[];
 if(!Number.isInteger(steps)||steps<=0)throw Error('Read the exact original native step count');
 if(!Array.isArray(spec.stages)||spec.stages.length===0||new Set(spec.stages).size!==spec.stages.length||
   !spec.stages.every(n=>Number.isInteger(n)&&n>=0&&n<576))throw Error('Explicit distinct actual stage indices required');
 fs.mkdirSync(path.join(spec.output,'large-arrays'));
 const actualMethods=writeJSON('actual-original-method-identities.json.gz',originalMethods(dn),{compressed:true});
 const result={schema:'actual61-noJ-matched-variational-selected-stage-probe-v1',
  source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),candidate_module:spec.candidate_module,
  spec_sha256:specSHA,original_snapshot_result_sha256:snapshotSHA,current_state_sha256:savedStateSHA,
  stages:spec.stages,stepsPerSegment:steps,actual_original_methods:actualMethods,
  original_noJ_stage_flows_started:0,original_noJ_stage_flows_returned:0,
  candidate_withJ_stage_flows_started:0,candidate_withJ_stage_flows_returned:0,
  complete_native_evaluate_calls:0,native_solve_calls:0,nonlinear_trials:0,
  old_saved_J_reused:false,old_saved_J_payloads_read:false,new_candidate_J_produced:true,
  original_noJ_function_replaced:false,original_H_target_scales_profiles_unchanged:true,
  acceptance_or_error_threshold_added:false,native_accepted:false,task_completed:false,cases};
 function caseArray(name,shape,rows){const row=saveArray(name,shape,rows);outputArrays.push(row);return row;}
 for(const n of spec.stages){
  const cell=dn.tail.cells[n],id=String(n).padStart(3,'0'),input=new Float64Array(size);
  input.set(arrays['base-states'].rows[n+1]);
  const item={stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,port_ratio:numberRecord(cell.portRatio),
   input:caseArray('stage-'+id+'-full-original-input',[1,size],[input]),
   original_scale:numberRecord(arrays['original-scales'].rows[0][n]),
   parent_saved_withJ_out_raw_sha256:sha(rawView(arrays['stage-out'].rows[n])),
   original_noJ_returned:false,candidate_withJ_returned:false,all_comparisons_available:false};
  cases.push(item);
  let baseline=null,candidate=null;
  try{
   result.original_noJ_stage_flows_started++;
   let state=Float64Array.from(input);
   const evaluationsBefore=cell.engine.statistics?.evaluations;
   for(const profile of cell.profiles)for(let k=0;k<steps;k++)
    state=cell.engine.rk4(state,profile,k/steps,1/steps);
   baseline=state;item.original_noJ_returned=true;result.original_noJ_stage_flows_returned++;
   item.original_noJ_rhs_evaluation_counter_delta=(typeof evaluationsBefore==='number'&&typeof cell.engine.statistics?.evaluations==='number')?
    cell.engine.statistics.evaluations-evaluationsBefore:null;
   item.original_noJ_complete_state=caseArray('stage-'+id+'-original-noJ-full-state',[1,size],[baseline]);
  }catch(error){item.original_noJ_error={message:String(error),stack:String(error?.stack??error)};}
  const stepRecords=[];
  try{
   result.candidate_withJ_stage_flows_started++;
   const engine=createNoJMatchedVariationalEngine({modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,
    mu:cell.mu,orientation:dn.tail.parameters.orientation,projectionFloor:dn.tail.parameters.projectionFloor,
    cuspAwareFlow:cfg.cuspAwareFlow===true},cell.engine,{createFourierProductJacobianEngine,splitIntegrationInterval});
   if(engine.rk4!==cell.engine.rk4||engine.rhs!==cell.engine.rhs||engine.root!==cell.engine.root)
    throw Error('The original no-J/root/RHS references must remain untouched');
   candidate=engine.flowStateWithJacobian(Float64Array.from(input),cell.profiles,{stepsPerSegment:steps,
    onStep(record){
     stepRecords.push({profile_index:record.profile_index,ordinary_index:record.ordinary_index,
      sub_index:record.sub_index,branch:record.branch,x:numberRecord(record.x),h:numberRecord(record.h),
      original_ordinary_x:numberRecord(record.original_ordinary_x),original_ordinary_h:numberRecord(record.original_ordinary_h),
      input_state_raw_sha256:sha(rawView(record.input_state)),output_state_raw_sha256:sha(rawView(record.output_state)),
      input_tangent_raw_sha256:sha(rawView(record.input_tangent)),output_tangent_raw_sha256:sha(rawView(record.output_tangent)),
      fields:record.fields.map(f=>({index:f.index,x:numberRecord(f.x),
       state_raw_sha256:sha(rawView(f.state)),derivative_raw_sha256:sha(rawView(f.derivative)),
       geometry:Object.fromEntries(Object.entries(f.geometry).map(([k,v])=>[k,numberRecord(v)])),
       root_err:numberRecord(f.err),root_scale:numberRecord(f.scale),minA:numberRecord(f.minA),minD:numberRecord(f.minD),
       local_J_raw_sha256:sha(rawView(f.local_jacobian))}))});
    }});
   item.candidate_withJ_returned=true;result.candidate_withJ_stage_flows_returned++;
   item.candidate_complete_state=caseArray('stage-'+id+'-candidate-full-state',[1,size],[candidate.state]);
   item.candidate_complete_tangent=caseArray('stage-'+id+'-candidate-full-tangent',[size,K],
    Array.from({length:size},(_,i)=>candidate.tangent.subarray(i*K,(i+1)*K)));
   const out=Float64Array.from(candidate.state.slice(0,K)),J=Float64Array.from(candidate.tangent.slice(0,K*K));
   for(let j=0;j<M;j++){out[M+j]/=cell.portRatio;for(let k=0;k<K;k++)J[(M+j)*K+k]/=cell.portRatio;}
   item.candidate_post_port_out=caseArray('stage-'+id+'-candidate-post-port-out',[1,K],[out]);
   item.candidate_post_port_J=caseArray('stage-'+id+'-candidate-post-port-J',[K,K],
    Array.from({length:K},(_,i)=>J.subarray(i*K,(i+1)*K)));
   item.originalRootCalls=candidate.originalRootCalls;item.originalRhsCalls=candidate.originalRhsCalls;
   item.capturedJacobianCalls=candidate.capturedJacobianCalls;
   item.root_or_RHS_reexecuted_during_tangent_phase=candidate.root_or_RHS_reexecuted_during_tangent_phase;
   item.minA=numberRecord(candidate.minA);item.minD=numberRecord(candidate.minD);item.maxRootRelative=numberRecord(candidate.maxRootRelative);
   if(baseline){
    const originalOut=Float64Array.from(baseline.slice(0,K));for(let j=0;j<M;j++)originalOut[M+j]/=cell.portRatio;
    item.original_noJ_post_port_out=caseArray('stage-'+id+'-original-noJ-post-port-out',[1,K],[originalOut]);
    item.all_comparisons_available=true;
    item.complete_226_state_bitwise_equal=rawView(baseline).equals(rawView(candidate.state));
    item.post_port_shape_bitwise_equal=rawView(originalOut).equals(rawView(out));
    item.mean_correction_state_bitwise_equal=rawView(baseline.subarray(K,K+1)).equals(rawView(candidate.state.subarray(K,K+1)));
    item.background_mean_bitwise_equal=rawView(baseline.subarray(K+1,K+2)).equals(rawView(candidate.state.subarray(K+1,K+2)));
    item.original_noJ_meanHeight=numberRecord(baseline[K]+baseline[K+1]);
    item.candidate_meanHeight=numberRecord(candidate.state[K]+candidate.state[K+1]);
    item.mean_height_sum_bitwise_equal=item.original_noJ_meanHeight.float64le_hex===item.candidate_meanHeight.float64le_hex;
    item.original_vs_candidate_out=compareRow(originalOut,out,arrays['original-scales'].rows[0][n],{stage:n}).summary;
    item.saved_old_withJ_vs_current_original_noJ=compareRow(arrays['stage-out'].rows[n],originalOut,
     arrays['original-scales'].rows[0][n],{stage:n}).summary;
   }
  }catch(error){item.candidate_error={message:String(error),stack:String(error?.stack??error)};}
  item.candidate_step_records=writeJSON('stage-'+id+'-step-records.json.gz',{
   schema:'noJ-matched-captured-variational-step-observations-v1',stage:n,source_sha256:spec.source_sha256,
   candidate_module:spec.candidate_module,records:stepRecords},{compressed:true});
  item.original_input_bits_after_calls_sha256=sha(rawView(input));
  writeJSON('stage-'+id+'-result.json',item);
  console.log(encode({event:'noJ-matched-selected-stage-finished',stage:n,
   original_noJ_returned:item.original_noJ_returned,candidate_withJ_returned:item.candidate_withJ_returned,
   complete_226_state_bitwise_equal:item.complete_226_state_bitwise_equal??null}).toString().trim());
 }
 result.probe_completed=true;
 result.every_requested_case_returned=cases.every(c=>c.all_comparisons_available);
 result.all_completed_primal_states_bitwise_equal=cases.filter(c=>c.all_comparisons_available).every(c=>c.complete_226_state_bitwise_equal);
 result.output_array_manifest=writeJSON('array-manifest.json',{
  schema:'noJ-matched-variational-selected-stage-arrays-v1',source_sha256:spec.source_sha256,
  candidate_module:spec.candidate_module,current_state_sha256:savedStateSHA,arrays:outputArrays,
  full_J_and_state_payloads_artifact_only:true});
 result.elapsed_seconds=(Date.now()-started)/1000;
 const saved=writeJSON('summary.json',result);
 console.log(encode({event:'noJ-matched-probe-finished',summary:saved,
  every_requested_case_returned:result.every_requested_case_returned,
  all_completed_primal_states_bitwise_equal:result.all_completed_primal_states_bitwise_equal}).toString().trim());
 return result;
}

registerHooks({load(url,context,nextLoad){
 const loaded=nextLoad(url,context);
 if(!url.startsWith('file:')||path.resolve(fileURLToPath(url))!==path.resolve(frozenPath))return loaded;
 const original=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 equal(sha(original),frozenSHA,'the unchanged frozen original worker');
 const anchor="try{\n  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));";
 if(original.split(anchor).length!==2)throw Error('Unique frozen worker import anchor required');
 const loopStart="for await(const line of readline.createInterface({input:process.stdin,terminal:false})){";
 const loopEnd='process.stdin.destroy();';
 const replacement=`for await(const diagnosticLine of readline.createInterface({input:process.stdin,terminal:false})){
 const request=JSON.parse(diagnosticLine);if(request.stop)break;
 if(request.matched_primal!==${JSON.stringify(specSHA)})throw Error('Verified same-state diagnostic request required');
 const probe=await import(${JSON.stringify(import.meta.url)});
 await probe.runMatchedPrimalProbe(dn,zero,cfg);break;
}
process.stdin.destroy();`;
 const insertion=`
const diagnosticLoopStart=${JSON.stringify(loopStart)},diagnosticLoopEnd=${JSON.stringify(loopEnd)};
if(source.split(diagnosticLoopStart).length!==2||source.split(diagnosticLoopEnd).length!==2)
 throw Error('Unique original request loop required');
const diagnosticAt=source.indexOf(diagnosticLoopStart),diagnosticEnd=source.indexOf(diagnosticLoopEnd,diagnosticAt)+diagnosticLoopEnd.length;
const diagnosticRemoved=source.slice(diagnosticAt,diagnosticEnd),diagnosticOriginal=source;
const diagnosticReplacement=${JSON.stringify(replacement)};
source=source.slice(0,diagnosticAt)+diagnosticReplacement+source.slice(diagnosticEnd);
const diagnosticRestored=source.slice(0,diagnosticAt)+diagnosticRemoved+source.slice(diagnosticAt+diagnosticReplacement.length);
if(diagnosticRestored!==diagnosticOriginal)throw Error('Exact request-loop source roundtrip failed');
fs.writeFileSync(${JSON.stringify(path.join(spec.output,'worker-instrumentation.json'))},JSON.stringify({
 schema:'actual61-noJ-matched-primal-test-request-loop-only-v1',hook_sha256:${JSON.stringify(fileSHA(selfPath))},
 frozen_worker_sha256:${JSON.stringify(frozenSHA)},original_compiled_worker_sha256:sha256(diagnosticOriginal),
 instrumented_compiled_worker_sha256:sha256(source),removed_original_loop_sha256:sha256(diagnosticRemoved),
 diagnostic_loop_sha256:sha256(diagnosticReplacement),exact_source_roundtrip_verified:true,
 only_request_loop_replaced:true,original_constructor_root_rhs_rk_evaluate_and_caches_unchanged:true,
 original_solve_and_endpoint_audit_not_called:true,Function_toString_not_modified:true
},null,2)+'\\n',{flag:'wx'});
`;
 const transformed=original.replace(anchor,insertion+anchor);
 equal(transformed.replace(insertion,''),original,'preload insertion source roundtrip');
 return {...loaded,source:transformed};
}});
