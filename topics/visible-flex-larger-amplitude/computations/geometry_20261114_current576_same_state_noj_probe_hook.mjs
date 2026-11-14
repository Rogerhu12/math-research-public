// One original no-J evaluation of actual61's last complete current state.
// Only the worker request loop is replaced. No RHS, RK, root, evaluate,
// graph, scale, line-search, solver, or cache implementation is modified.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import readline from 'node:readline';
import os from 'node:os';
import {fileURLToPath} from 'node:url';
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
const variable='VISIBLE_FLEX_CURRENT576_SAME_STATE_NOJ_SPEC';
const specPath=process.env[variable];
if(!specPath)throw Error('A complete original same-state specification is required');
const specRaw=fs.readFileSync(specPath),spec=JSON.parse(unpack(specRaw)),specSHA=sha(specRaw);
const frozenPath=path.join(here,'tail_frozen_worker.mjs');
const frozenSHA='3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054';
const coreSHA='ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3';
const evalSHA='9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9';
const savedStateSHA='b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013';
const snapshotSHA='5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286';
if(spec.schema!=='actual61-current576-same-state-noJ-probe-spec-v1'||
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
export async function runSameStateNoJ(dn,zero,cfg){
 if(protocolCalls++!==0)throw Error('Only one diagnostic original no-J call is allowed in this probe');
 const started=Date.now(),launch=JSON.parse(fs.readFileSync(path.join(spec.output,'verified-launch-intent.json')));
 equal(launch.spec_sha256,specSHA,'verified launch specification');
 equal(launch.identity_verified_before_evaluation,true,'parent verified ready/config/source identity');
 equal(numericalSources(launch.current_sources),spec.original_source_sha256,'unchanged consumed numerical sources');
 equal(mathematical(cfg),spec.numerical_configuration,'unchanged original numerical configuration');
 if(cfg.initialCheckpoint)throw Error('No geometric remapping of a saved current state');
 const before=liveIdentity(dn);equal(before,spec.original_live_identity,'all original methods/graphs/gains/far/profiles');
 equal([dn.tail.parameters.modes,dn.tail.parameters.depth,dn.tail.cells.length],[112,576,576],'full original dimensions');
 equal(sha(dn.tail.evaluate.toString()),evalSHA,'original evaluate source without any observer');
 equal(fileSHA(path.join(process.env.VISIBLE_FLEX_SOURCE_TOPIC,'scripts/78718-tail-tangent-core.mjs')),coreSHA,'original core source');
 const context=verified(spec.snapshot_inputs.context),snapshot=verified(spec.snapshot_inputs.result),
  manifest=verified(spec.snapshot_inputs.manifest),oldFlow=verified(spec.snapshot_inputs.flow_metadata);
 equal(snapshot.current_state_sha256,savedStateSHA,'original last state source');
 equal(snapshot.actual_current_original_norm,spec.saved_withJ_norm,'original saved withJ norm');
 equal(sha(fs.readFileSync(spec.snapshot_inputs.result.path)),snapshotSHA,'actual snapshot result bytes');
 equal(context.current_original_norm,spec.saved_withJ_norm,'original context norm');
 equal(oldFlow.rows.length,576,'all saved original mean/guard rows');
 const listed=new Map(manifest.arrays.map(a=>[a.name,a]));
 const arrays={};for(const [name,binding] of Object.entries(spec.original_arrays)){
  equal(binding.entry,listed.get(name),'actual snapshot array descriptor '+name);arrays[name]=readArray(binding);
  equal(arrays[name].entry.raw_sha256,context.raw_array_sha256[name],'actual raw identity '+name);
 }
 equal(arrays['base-states'].entry.raw_sha256,savedStateSHA,'all actual input state words');
 const M=112,K=224,depth=576,states=arrays['base-states'].rows,target=arrays['cut-target'].rows[0],
  scales=arrays['original-scales'].rows[0],height=arrays['physical-height'].rows[0],
  oldOut=arrays['stage-out'].rows,oldResidual=arrays['stage-residuals'].rows,
  oldCut=arrays['cut-residual'].rows[0],oldEnd=arrays['end-residual'].rows[0];
 // Rebuild only the original scaleFor/height conversion as an identity
 // check. The actual call below still receives the saved original arrays.
 const checkedTarget=Float64Array.from(height,v=>v/zero.radius**4),checkedScales=new Float64Array(577);
 checkedScales[0]=Math.max(1e-250,...Array.from(checkedTarget,Math.abs));
 for(let n=0;n<depth;n++)checkedScales[n+1]=checkedScales[n]/Math.abs(dn.tail.gains[n][0]);
 if(!rawView(checkedTarget).equals(rawView(target))||!rawView(checkedScales).equals(rawView(scales)))
  throw Error('The same original H/target/gains/scaleFor words are required');
 if(!rawView(Float64Array.from(dn.tail.graphs.at(-1))).equals(arrays['original-far-graph'].raw))
  throw Error('Original far graph words differ');
 if(!Array.from(scales).every(v=>Number.isFinite(v)&&v>0))throw Error('Use the finite positive saved original scales');
 fs.mkdirSync(path.join(spec.output,'large-arrays'));
 const methods=writeJSON('actual-primal-method-identities.json.gz',originalMethods(dn),{compressed:true});
 const enteredState=saveArray('actual-evaluate-input-states',[577,224],states),
  enteredTarget=saveArray('actual-evaluate-input-target',[1,112],[target]),
  enteredScales=saveArray('actual-evaluate-input-scales',[1,577],[scales]);
 const summary={schema:'actual61-current576-same-state-noJ-comparison-v1',
  source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,
  original_public_run:spec.original_public_run,input_native_result_sha256:spec.original_native_result_sha256,
  input_snapshot_result_sha256:snapshotSHA,original_native_call:1,original_nonlinear_iteration:3,
  current_state_sha256:savedStateSHA,saved_withJ_norm:spec.saved_withJ_norm,
  original_noJ_evaluate_calls:0,original_solve_calls:0,new_withJ_evaluations:0,new_J_evaluations:0,
  newton_corrections:0,nonlinear_trials:0,complete_current_state_restored_by_raw_bits:true,
  input_negative_zero_count:arrays['base-states'].negativeZeros,entered_state:enteredState,
  entered_target:enteredTarget,entered_scales:enteredScales,actual_method_identities:methods,
  current_original_evaluate_function_unmodified:true,only_worker_request_loop_changed:true,
  saved_J_payloads_read:false,saved_J_descriptor_only:spec.original_J_descriptor_only.raw_sha256,
  saved_original_full_state_not_a_response_cache:true,no_cut_or_far_projection:true,no_H_threshold:true,
  probe_completed:false,evaluation_returned:false,native_accepted:false,task_completed:false,
  difference_cause_proven:false,no_scientific_acceptance_threshold_added:true};
 console.log(encode({event:'same-state-original-noJ-start',original_state_sha256:savedStateSHA,
  saved_snapshot_sha256:snapshotSHA,stages:576,original_evaluate_calls_requested:1}).toString().trim());
 let ev;
 try{
  summary.original_noJ_evaluate_calls++;
  // The sole scientific stage pass. Do not substitute a with-J value path,
  // modify the original engine, or call a fresh Jacobian for comparison.
  ev=dn.tail.evaluate(states,target,false,scales);
  summary.evaluation_returned=true;
 }catch(error){
  summary.original_evaluation_error={message:String(error),stack:String(error?.stack??error),
   stage:error?.tailStage??null,rawCell:error?.tailRawCell??null,rawSegment:error?.tailRawSegment??null};
  summary.complete_returned_residuals_available=false;
 }
 const outputArrays=[enteredState,enteredTarget,enteredScales];
 summary.input_state_raw_sha256_after_call=binaryRowsHash(states);
 summary.input_state_unchanged_by_actual_call=summary.input_state_raw_sha256_after_call===savedStateSHA;
 summary.input_target_unchanged_by_actual_call=rawView(target).equals(arrays['cut-target'].raw);
 summary.input_scales_unchanged_by_actual_call=rawView(scales).equals(arrays['original-scales'].raw);
 if(ev){
  equal([ev.flows.length,ev.residuals.length,ev.end.length],[depth,depth,M],'complete original no-J returned structure');
  const newOut=ev.flows.map(f=>f.out),newResidual=ev.residuals,cut=new Float64Array(M);
  for(let j=0;j<M;j++)cut[j]=states[0][j]-target[j];
  outputArrays.push(saveArray('original-noJ-stage-out',[576,224],newOut),
   saveArray('original-noJ-stage-residuals',[576,224],newResidual),
   saveArray('original-noJ-cut-residual',[1,112],[cut]),saveArray('original-noJ-end-residual',[1,112],[ev.end]));
  const differencesOut=[],differencesResidual=[],rows=[],means=new Float64Array(depth);
  let allMeans=true;
  for(let n=0;n<depth;n++){
   const cell=dn.tail.cells[n],f=ev.flows[n],place={stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment};
   const out=compareRow(oldOut[n],newOut[n],scales[n],place),r=compareRow(oldResidual[n],newResidual[n],scales[n],place);
   differencesOut.push(out.difference);differencesResidual.push(r.difference);
   equal(oldFlow.rows[n].stage,n,'all original saved scalar rows');
   const oldMean=decodeNumber(oldFlow.rows[n].meanHeight);
   const isMean=typeof f.meanHeight==='number';allMeans=allMeans&&isMean;if(isMean)means[n]=f.meanHeight;
   rows.push({...place,original_scale:numberRecord(scales[n]),
    saved_withJ_out_raw_sha256:sha(rawView(oldOut[n])),actual_noJ_out_raw_sha256:sha(rawView(newOut[n])),
    saved_withJ_residual_raw_sha256:sha(rawView(oldResidual[n])),actual_noJ_residual_raw_sha256:sha(rawView(newResidual[n])),
    out_comparison:out.summary,residual_comparison:r.summary,
    original_noJ_J_is_null:f.J===null,
    saved_withJ_meanHeight:oldFlow.rows[n].meanHeight,
    actual_noJ_meanHeight:isMean?numberRecord(f.meanHeight):{available:false},
    meanHeight_difference:isMean?numberRecord(f.meanHeight-oldMean):{available:false},
    saved_withJ_minA:oldFlow.rows[n].minA,saved_withJ_minD:oldFlow.rows[n].minD,
    actual_noJ_flow_minA:typeof f.minA==='number'?numberRecord(f.minA):{available:false},
    actual_noJ_flow_minD:typeof f.minD==='number'?numberRecord(f.minD):{available:false}});
  }
  outputArrays.push(saveArray('noJ-minus-withJ-stage-out',[576,224],differencesOut),
   saveArray('noJ-minus-withJ-stage-residuals',[576,224],differencesResidual));
  if(allMeans)outputArrays.push(saveArray('original-noJ-mean-height-increments',[1,576],[means]));
  const oldScan=scanNorm(oldResidual,oldCut,oldEnd,scales,M,K,dn.tail.cells),
   newScan=scanNorm(newResidual,cut,ev.end,scales,M,K,dn.tail.cells);
  const paired=writeJSON('complete-stage-comparisons.json.gz',{
   schema:'actual61-same-state-noJ-withJ-full-stage-comparisons-v1',spec_sha256:specSHA,
   original_snapshot_result_sha256:snapshotSHA,current_state_sha256:savedStateSHA,rows,
   cut_comparison:compareRow(oldCut,cut,scales[0],{kind:'cut'}).summary,
   far_comparison:compareRow(oldEnd,ev.end,scales[depth],{kind:'far'}).summary,
   scope:'Original saved and newly returned arrays; subtraction/normalization are binary64 diagnostics, not rigorous error bounds.'
  },{compressed:true});
  Object.assign(summary,{complete_returned_residuals_available:true,completed_stages:depth,
   all_original_noJ_flow_guards_returned:true,actual_original_noJ_norm:numberRecord(ev.norm),
   actual_original_noJ_minA:numberRecord(ev.minA),actual_original_noJ_minD:numberRecord(ev.minD),
   noJ_minA_minD_are_original_aggregate_placeholders:true,
   original_noJ_minus_saved_withJ_norm:numberRecord(ev.norm-decodeNumber(spec.saved_withJ_norm)),
   saved_withJ_residual_readback:oldScan,actual_noJ_residual_readback:newScan,
   saved_withJ_norm_reconstructed_same_bits:oldScan.reconstructed_norm.float64le_hex===spec.saved_withJ_norm.float64le_hex,
   actual_noJ_norm_reconstructed_same_bits:newScan.reconstructed_norm.float64le_hex===numberRecord(ev.norm).float64le_hex,
   all_noJ_flow_J_fields_null:ev.flows.every(f=>f.J===null),full_stage_comparison:paired});
 }
 const manifestOut=writeJSON('array-manifest.json',{
  schema:'actual61-current576-same-state-noJ-output-arrays-v1',source_sha256:spec.source_sha256,
  hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,current_state_sha256:savedStateSHA,
  arrays:outputArrays,all_raw_payloads_artifact_only:true,actual_nonfinite_and_signed_zero_words_retained:true});
 summary.output_array_manifest=manifestOut;summary.probe_completed=true;summary.elapsed_seconds=(Date.now()-started)/1000;
 const saved=writeJSON('summary.json',summary);
 console.log(encode({event:'same-state-original-noJ-finished',evaluation_returned:summary.evaluation_returned,
  original_noJ_evaluate_calls:summary.original_noJ_evaluate_calls,actual_original_noJ_norm:summary.actual_original_noJ_norm??null,
  saved_withJ_norm:summary.saved_withJ_norm,summary:saved,native_accepted:false}).toString().trim());
 return summary;
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
 if(request.same_state_noJ!==${JSON.stringify(specSHA)})throw Error('Verified same-state diagnostic request required');
 const probe=await import(${JSON.stringify(import.meta.url)});
 await probe.runSameStateNoJ(dn,zero,cfg);break;
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
 schema:'actual61-current576-same-state-noJ-request-loop-only-v1',hook_sha256:${JSON.stringify(fileSHA(selfPath))},
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
