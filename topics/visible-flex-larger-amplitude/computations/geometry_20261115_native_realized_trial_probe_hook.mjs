// One original alpha1/512 no-J evaluation at actual73's final state.
// Independent reversible source observations retain original root returns
// and stage boundaries; every original numeric expression is preserved.
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
const variable='VISIBLE_FLEX_ACTUAL73_REALIZED_TRIAL_SPEC';
const specPath=process.env[variable];
if(!specPath)throw Error('A complete original same-state specification is required');
const specRaw=fs.readFileSync(specPath),spec=JSON.parse(unpack(specRaw)),specSHA=sha(specRaw);
const frozenPath=path.join(here,'tail_frozen_worker.mjs');
const frozenSHA='3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054';
const coreSHA='ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3';
const evalSHA='9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9';
const savedStateSHA='f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6';
const snapshotSHA='2f9bf170c0366e9d5adaf003a9d0746f28a536171a32339e8a5f502313495e92';
const enginePath=path.join(here,'tail_resumable_engine.mjs'),
 engineSHA='1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8',
 rootPath=path.join(process.env.VISIBLE_FLEX_SOURCE_TOPIC,'scripts/78718-tail-fourier-root-momentum.mjs'),
 rootSHA='cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88';
const observerKey='visible.actual73.realized-trial.read-only-observer.v1',observerSymbol=Symbol.for(observerKey);
const originalCellCall='try{f=cellFlow(n,states[n+1],withJac);}',
 observedCellCall='try{globalThis[Symbol.for('+JSON.stringify(observerKey)+')]?.stageEnter(n,states[n+1],withJac);f=cellFlow(n,states[n+1],withJac);globalThis[Symbol.for('+JSON.stringify(observerKey)+')]?.stageReturn(n,f);}';
const rootReplacements=[
 {before:'if(err<=8e-14*scale)return last;',
  after:'if(err<=8e-14*scale){globalThis[Symbol.for('+JSON.stringify(observerKey)+')]?.rootReturn(last,state,profile,x);return last;}'},
 {before:'if(err<=5e-12*scale)return {...last,roundoffFallback:true};',
  after:'if(err<=5e-12*scale){const observedRootReturn={...last,roundoffFallback:true};globalThis[Symbol.for('+JSON.stringify(observerKey)+')]?.rootReturn(observedRootReturn,state,profile,x);return observedRootReturn;}'}
];
if(spec.schema!=='actual73-iteration2-realized-noJ-trial-probe-spec-v1'||
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
function restoredEvaluateSource(source){
 if(source.split(observedCellCall).length!==2)throw Error('Exactly one read-only evaluate observation span required');
 const original=source.replace(observedCellCall,originalCellCall);
 equal(sha(original),evalSHA,'restored original evaluate function source');return original;
}
function restoredRootSource(source){
 let original=source;
 for(const item of rootReplacements){
  if(original.split(item.after).length!==2)throw Error('Exactly one original root-return observation required');
  original=original.replace(item.after,item.before);
 }
 return original;
}
function observedMethodIdentities(dn,installation){
 const actualEvaluate=dn.tail.evaluate.toString(),originalEvaluate=restoredEvaluateSource(actualEvaluate);
 const unique=[],sources={},seen=new Map();
 for(let n=0;n<dn.tail.cells.length;n++){
  const engine=dn.tail.cells[n].engine;if(seen.has(engine))continue;
  const source={},hashes={};
  for(const key of ['root','rhs','rk4','rhsWithJacobian','flowStateWithJacobian']){
   const actual=engine[key].toString(),restored=key==='root'?restoredRootSource(actual):actual;
   source[key]={actual_source:actual,actual_sha256:sha(actual),original_source:restored,
    original_sha256:sha(restored),source_observation_only:key==='root'};
   hashes[key]=sha(restored);sources[sha(actual)]=source[key];
  }
  const parent=installation.engines.find(x=>x.stages.includes(n));
  if(!parent)throw Error('Every actual original engine has a parent installation identity');
  for(const key of ['root','rhs','rk4','rhsWithJacobian'])
   equal(hashes[key],parent.original_function_sha256[key],'same original no-J arithmetic method '+key);
  seen.set(engine,unique.length);unique.push({first_stage:n,original_method_sha256:hashes});
 }
 return {schema:'actual73-realized-trial-original-and-observed-source-identities-v1',
  actual_evaluate_source:actualEvaluate,actual_evaluate_sha256:sha(actualEvaluate),
  restored_original_evaluate_source:originalEvaluate,restored_original_evaluate_sha256:sha(originalEvaluate),
  engine_instances:unique,sources,exact_observation_source_roundtrip_verified:true,
  Function_toString_not_modified:true,original_guard_root_RHS_RK_arithmetic_not_changed:true,
  noJ_original_field_functions_called_not_a_reimplementation:true};
}
function readDirection(binding){
 const item=binding.descriptor,p=binding.path,raw=fs.readFileSync(p);
 equal(raw.length,item.bytes,'complete original correction byte length');equal(sha(raw),item.sha256,'complete original correction SHA');
 equal([item.dtype,item.order,item.shape],['<f8','C',[577,224]],'complete original correction array');
 const rows=[];let negativeZeros=0;
 for(let n=0;n<577;n++){
  const row=new Float64Array(224);
  for(let j=0;j<224;j++){
   const value=raw.readDoubleLE((n*224+j)*8);if(!Number.isFinite(value))throw Error('Finite original correction input required');
   row[j]=value;if(Object.is(value,-0))negativeZeros++;
  }
  if(!rawView(row).equals(raw.subarray(n*224*8,(n+1)*224*8)))throw Error('Exact original correction restoration required');
  rows.push(row);
 }
 return {raw,rows,negativeZeros};
}
function actualArrayStats(rows){
 let finite=0,nan=0,positiveInfinity=0,negativeInfinity=0,negativeZero=0;
 for(const row of rows)for(const value of row){
  if(Number.isNaN(value))nan++;else if(value===Infinity)positiveInfinity++;
  else if(value===-Infinity)negativeInfinity++;else finite++;
  if(Object.is(value,-0))negativeZero++;
 }
 return {finite,nan,positive_infinity:positiveInfinity,negative_infinity:negativeInfinity,negative_zero:negativeZero};
}
function changedWords(a,b){
 let different=0,numericDifferent=0;
 for(let n=0;n<a.length;n++){
  const x=rawView(a[n]),y=rawView(b[n]);
  for(let j=0;j<a[n].length;j++){
   if(x.readBigUInt64LE(j*8)!==y.readBigUInt64LE(j*8))different++;
   if(a[n][j]!==b[n][j])numericDifferent++;
  }
 }
 return {bit_different_words:different,numerically_different_words:numericDifferent};
}

let protocolCalls=0;
export async function runRealizedTrialNoJ(dn,zero,cfg){
 if(protocolCalls++!==0)throw Error('Exactly one original selected trial no-J evaluation belongs to this probe');
 const started=Date.now(),launch=JSON.parse(fs.readFileSync(path.join(spec.output,'verified-launch-intent.json')));
 equal(launch.spec_sha256,specSHA,'complete actual verified specification');
 equal(launch.identity_verified_before_evaluation,true,'constructor ready/source/config verified');
 equal(numericalSources(launch.current_sources),spec.original_source_sha256,'all original numerical sources');
 equal(mathematical(cfg),spec.numerical_configuration,'all original numerical configuration');
 if(cfg.initialCheckpoint)throw Error('No geometry remapping of this actual failed state');
 const context=verified(spec.snapshot_inputs.context),snapshot=verified(spec.snapshot_inputs.result),
  manifest=verified(spec.snapshot_inputs.manifest),oldFlow=verified(spec.snapshot_inputs.flow_metadata),
  installation=verified(spec.snapshot_inputs.primal_installation);
 const before=liveIdentity(dn);
 // The only evaluate change is the reversible, read-only stage observer.
 const originalLive={...before,evaluate_function_sha256:sha(restoredEvaluateSource(dn.tail.evaluate.toString()))};
 equal(originalLive,spec.original_live_identity,'all original graph/gain/far/layout/method identities');
 equal([dn.tail.parameters.modes,dn.tail.parameters.depth,dn.tail.cells.length],[112,576,576],'all native dimensions');
 equal(fileSHA(path.join(process.env.VISIBLE_FLEX_SOURCE_TOPIC,'scripts/78718-tail-tangent-core.mjs')),coreSHA,'immutable original core');
 equal(snapshot.current_state_sha256,savedStateSHA,'actual last current state');
 equal(snapshot.actual_current_original_norm,spec.saved_withJ_norm,'original complete saved base norm');
 equal(fileSHA(spec.snapshot_inputs.result.path),snapshotSHA,'actual final snapshot result');
 equal(context.current_original_norm,spec.saved_withJ_norm,'actual original context norm');
 equal(oldFlow.rows.length,576,'all original saved flow records');
 const listed=new Map(manifest.arrays.map(x=>[x.name,x])),arrays={};
 for(const [name,binding] of Object.entries(spec.original_arrays)){
  equal(binding.entry,listed.get(name),'actual original array descriptor '+name);arrays[name]=readArray(binding);
  equal(arrays[name].entry.raw_sha256,context.raw_array_sha256[name],'actual original raw identity '+name);
 }
 const direction=readDirection({descriptor:spec.direction_native_delta,path:spec.direction_inputs.native_delta.path});
 equal(sha(direction.raw),spec.direction_raw_sha256,'actual full original delta');
 equal(fileSHA(spec.direction_inputs.result.path),spec.original_direction_result_sha256,'actual final direction result');
 const M=112,K=224,depth=576,states=arrays['base-states'].rows,delta=direction.rows,
  target=arrays['cut-target'].rows[0],scales=arrays['original-scales'].rows[0],height=arrays['physical-height'].rows[0],
  oldOut=arrays['stage-out'].rows,oldResidual=arrays['stage-residuals'].rows,
  oldCut=arrays['cut-residual'].rows[0],oldEnd=arrays['end-residual'].rows[0];
 equal(binaryRowsHash(states),savedStateSHA,'actual complete original state raw');
 const checkedTarget=Float64Array.from(height,v=>v/zero.radius**4),checkedScales=new Float64Array(577);
 checkedScales[0]=Math.max(1e-250,...Array.from(checkedTarget,Math.abs));
 for(let n=0;n<depth;n++)checkedScales[n+1]=checkedScales[n]/Math.abs(dn.tail.gains[n][0]);
 if(!rawView(checkedTarget).equals(rawView(target))||!rawView(checkedScales).equals(rawView(scales)))
  throw Error('Original H/target/gain-derived scales changed');
 if(!rawView(Float64Array.from(dn.tail.graphs.at(-1))).equals(arrays['original-far-graph'].raw))
  throw Error('The complete original far graph changed');
 if(!Array.from(scales).every(v=>Number.isFinite(v)&&v>0))throw Error('Original finite positive input scales required');
 // The selected original trial expression is copied verbatim, including the
 // two ordinary binary64 operations and the Float64Array assignment.
 const k=9,lambda=2**(-k),cor={delta};
 const trial=states.map((s,n)=>Float64Array.from(s,(v,j)=>v+lambda*cor.delta[n][j]));
 equal(k,spec.actual_trial_index,'the one previously observed original trial index');
 equal(numberRecord(lambda),numberRecord(spec.original_selected_trial.step),'the exact original dyadic step');
 const originalCore=fs.readFileSync(path.join(process.env.VISIBLE_FLEX_SOURCE_TOPIC,'scripts/78718-tail-tangent-core.mjs'),'utf8');
 const originalTrialLine='const lambda=2**(-k),trial=states.map((s,n)=>Float64Array.from(s,(v,j)=>v+lambda*cor.delta[n][j]));';
 if(originalCore.split(originalTrialLine).length!==2)throw Error('Unique frozen original trial expression required');
 fs.mkdirSync(path.join(spec.output,'large-arrays'));
 fs.mkdirSync(path.join(spec.output,'large-arrays/root-return-packets'));
 const methods=writeJSON('actual-observed-method-identities.json.gz',observedMethodIdentities(dn,installation),{compressed:true});
 const outputArrays=[
  saveArray('base-states',[577,224],states),saveArray('native-delta',[577,224],delta),
  saveArray('trial-states',[577,224],trial),saveArray('original-scales',[1,577],[scales]),
  saveArray('cut-target',[1,112],[target]),saveArray('physical-height',[1,112],[height]),
  saveArray('original-far-graph',[1,112],arrays['original-far-graph'].rows),
  saveArray('saved-stage-residuals',[576,224],oldResidual),saveArray('saved-cut-residual',[1,112],[oldCut]),
  saveArray('saved-end-residual',[1,112],[oldEnd])];
 const trialSHA=binaryRowsHash(trial),rootPackets=[];let stage=null,rootCalls=0,observerFailure=null,observerFailures=0;
 const observe=fn=>{try{fn();}catch(error){observerFailures++;observerFailure??={message:String(error),
  stack:String(error?.stack??error),stage:stage?.stage??null,scope:'read-only evidence I/O/contract failure; not an original scientific guard'};}};
 function saveRootStage(completed,flow=null){
  if(!stage)return;
  const n=stage.stage,cell=dn.tail.cells[n];
  const value={schema:'actual73-realized-trial-original-root-returns-v1',source_sha256:spec.source_sha256,
   hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,trial_state_sha256:trialSHA,alpha:numberRecord(lambda),
   stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,entered_shape_state_sha256:stage.input_sha256,
   original_stage_returned:completed,root_return_count:stage.roots.length,roots:stage.roots,
   root_observer_does_not_call_root_rhs_profile_or_geometry:true,
   no_root_convergence_tolerance_or_iteration_policy_changed:true,
   original_returned_flow:flow?{out_raw_sha256:sha(rawView(flow.out)),J_is_null:flow.J===null,
    meanHeight:typeof flow.meanHeight==='number'?numberRecord(flow.meanHeight):{available:false},
    minA:typeof flow.minA==='number'?numberRecord(flow.minA):{available:false},
    minD:typeof flow.minD==='number'?numberRecord(flow.minD):{available:false}}:null};
  rootPackets.push(writeJSON('large-arrays/root-return-packets/stage-'+String(n).padStart(3,'0')+'.json.gz',value,{compressed:true}));
  stage=null;
 }
 if(globalThis[observerSymbol]!==undefined)throw Error('No existing diagnostic observer may be overwritten');
 globalThis[observerSymbol]={
  stageEnter(n,input,withJac){observe(()=>{
   if(stage!==null||n!==rootPackets.length||withJac!==false)throw Error('One original sequential no-J stage pass required');
   stage={stage:n,input_sha256:sha(rawView(input)),roots:[]};
  });},
  rootReturn(rt,state,profile,x){observe(()=>{
   if(stage===null)throw Error('Every observed root belongs to an actual original stage');
   const cell=dn.tail.cells[stage.stage],profileIndex=cell.profiles.indexOf(profile);
   if(profileIndex<0)throw Error('Original profile reference belongs to the active original stage');
   const geometry={};for(const key of Object.keys(rt.g))if(typeof rt.g[key]==='number')geometry[key]=numberRecord(rt.g[key]);
   stage.roots.push({original_root_return_index:stage.roots.length,profile_index:profileIndex,x:numberRecord(x),
    full_state_float64le_sha256:sha(rawView(state)),full_state_length:state.length,
    err:numberRecord(rt.err),scale:numberRecord(rt.scale),iterations:rt.iterations,
    roundoffFallback_present:Object.hasOwn(rt,'roundoffFallback'),roundoffFallback:rt.roundoffFallback??false,
    root_L_float64le_sha256:sha(rawView(rt.L)),root_moments_float64le_sha256:sha(rawView(rt.e.moments)),geometry,
    minA:numberRecord(rt.e.minA),minD:numberRecord(rt.e.minD),minS:numberRecord(rt.e.minS),maxQuad:numberRecord(rt.e.maxQuad)});
   rootCalls++;
  });},
  stageReturn(n,flow){observe(()=>{
   if(stage===null||stage.stage!==n)throw Error('The original flow return must close its actual root records');
   saveRootStage(true,flow);
  });}
 };
 const summary={schema:'actual73-iteration2-realized-noJ-trial-probe-summary-v1',
  source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,
  original_public_run:spec.original_public_run,original_snapshot_result_sha256:snapshotSHA,
  direction_result_sha256:spec.original_direction_result_sha256,base_state_sha256:savedStateSHA,
  direction_sha256:spec.direction_raw_sha256,trial_state_sha256:trialSHA,alpha:numberRecord(lambda),
  original_selected_trial:spec.original_selected_trial,saved_withJ_norm:spec.saved_withJ_norm,
  original_noJ_evaluate_calls:0,original_solve_calls:0,new_withJ_evaluations:0,new_J_evaluations:0,
  newton_corrections:0,original_trial_expression:originalTrialLine,actual_trial_index:k,
  complete_state_and_delta_restored_by_raw_bits:true,base_negative_zero_count:arrays['base-states'].negativeZeros,
  direction_negative_zero_count:direction.negativeZeros,actual_trial_state_stats:actualArrayStats(trial),
  state_change_byte_diagnostics:changedWords(states,trial),actual_method_identities:methods,
  original_noJ_arithmetic_source_restoration_verified:true,only_read_only_observation_and_request_loop_changes:true,
  original_noJ_primal_path_used:true,actual73_new_withJ_function_not_called:true,
  saved_J_payloads_read:false,saved_J_descriptor_only:spec.original_J_descriptor_only.raw_sha256,
  original_failed_state_not_a_success_response:true,no_cut_or_far_projection:true,no_H_threshold:true,
  probe_completed:false,evaluation_returned:false,native_accepted:false,task_completed:false,
  failure_cause_proven:false,no_scientific_acceptance_threshold_added:true};
 console.log(encode({event:'actual73-realized-trial-original-noJ-start',base_state_sha256:savedStateSHA,
  direction_sha256:spec.direction_raw_sha256,trial_state_sha256:trialSHA,alpha:summary.alpha,
  original_evaluate_calls_requested:1}).toString().trim());
 let ev;
 try{
  summary.original_noJ_evaluate_calls++;
  ev=dn.tail.evaluate(trial,target,false,scales);
  summary.evaluation_returned=true;
 }catch(error){
  summary.original_evaluation_error={message:String(error),stack:String(error?.stack??error),
   stage:error?.tailStage??null,rawCell:error?.tailRawCell??null,rawSegment:error?.tailRawSegment??null};
  summary.complete_returned_residuals_available=false;
 }finally{
  delete globalThis[observerSymbol];
  if(stage!==null)observe(()=>saveRootStage(false));
 }
 summary.original_root_returns_observed=rootCalls;
 summary.observer_io_failure=observerFailure;summary.observer_failure_count=observerFailures;
 summary.base_state_unchanged=binaryRowsHash(states)===savedStateSHA;
 summary.direction_unchanged=binaryRowsHash(delta)===spec.direction_raw_sha256;
 summary.actual_trial_state_unchanged_by_call=binaryRowsHash(trial)===trialSHA;
 summary.target_unchanged=rawView(target).equals(arrays['cut-target'].raw);
 summary.scales_unchanged=rawView(scales).equals(arrays['original-scales'].raw);
 if(ev){
  equal([ev.flows.length,ev.residuals.length,ev.end.length],[depth,depth,M],'complete original no-J returned arrays');
  const cut=new Float64Array(M),means=new Float64Array(depth),flowRows=[];
  for(let j=0;j<M;j++)cut[j]=trial[0][j]-target[j];
  for(let n=0;n<depth;n++){
   const f=ev.flows[n];means[n]=f.meanHeight;
   flowRows.push({stage:n,rawCell:dn.tail.cells[n].rawCell,rawSegment:dn.tail.cells[n].rawSegment,
    original_scale:numberRecord(scales[n]),out_raw_sha256:sha(rawView(f.out)),residual_raw_sha256:sha(rawView(ev.residuals[n])),
    meanHeight:numberRecord(f.meanHeight),J_is_null:f.J===null,
    minA:typeof f.minA==='number'?numberRecord(f.minA):{available:false},
    minD:typeof f.minD==='number'?numberRecord(f.minD):{available:false}});
  }
  outputArrays.push(saveArray('trial-stage-out',[576,224],ev.flows.map(f=>f.out)),
   saveArray('trial-stage-residuals',[576,224],ev.residuals),saveArray('trial-cut-residual',[1,112],[cut]),
   saveArray('trial-end-residual',[1,112],[ev.end]),saveArray('trial-mean-height-increments',[1,576],[means]));
  const scan=scanNorm(ev.residuals,cut,ev.end,scales,M,K,dn.tail.cells),
   oldScan=scanNorm(oldResidual,oldCut,oldEnd,scales,M,K,dn.tail.cells);
  summary.complete_flow_metadata=writeJSON('complete-flow-return-metadata.json.gz',{
   schema:'actual73-realized-trial-complete-original-flow-returns-v1',spec_sha256:specSHA,
   trial_state_sha256:trialSHA,rows:flowRows,old_saved_flow_metadata:spec.snapshot_inputs.flow_metadata},{compressed:true});
  Object.assign(summary,{complete_returned_residuals_available:true,completed_stages:depth,
   all_original_noJ_flow_guards_returned:true,actual_original_noJ_norm:numberRecord(ev.norm),
   actual_original_noJ_minA:numberRecord(ev.minA),actual_original_noJ_minD:numberRecord(ev.minD),
   noJ_minA_minD_are_original_aggregate_placeholders:true,actual_noJ_residual_readback:scan,
   saved_withJ_residual_readback:oldScan,
   actual_noJ_norm_scan_same_bits:scan.reconstructed_norm.float64le_hex===numberRecord(ev.norm).float64le_hex,
   actual_original_noJ_norm_equals_saved_trial_bits:numberRecord(ev.norm).float64le_hex===numberRecord(spec.original_selected_trial.trialNorm).float64le_hex,
   actual_trial_strictly_decreases_original_saved_base_norm:ev.norm<decodeNumber(spec.saved_withJ_norm),
   original_comparison_diagnostic_only_no_native_acceptance:true,all_noJ_flow_J_fields_null:ev.flows.every(f=>f.J===null)});
 }
 summary.root_return_packet_manifest=writeJSON('root-return-packet-manifest.json',{
  schema:'actual73-realized-trial-original-root-packets-v1',source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
  trial_state_sha256:trialSHA,actual_root_returns:rootCalls,packets:rootPackets,
  complete_original_stage_return_packets:rootPackets.length===576&&observerFailure===null&&summary.evaluation_returned,
  observer_io_failure:observerFailure,original_root_policy_unchanged:true,extra_root_RHS_geometry_calls:0});
 summary.source_observation_receipts={
  root:receipt(path.join(spec.output,'root-return-observer-instrumentation.json.gz')),
  core:receipt(path.join(spec.output,'evaluate-observer-instrumentation.json.gz')),
  worker:receipt(path.join(spec.output,'worker-instrumentation.json'))};
 const manifestOut=writeJSON('array-manifest.json',{
  schema:'actual73-iteration2-realized-noJ-trial-output-arrays-v1',source_sha256:spec.source_sha256,
  hook_sha256:fileSHA(selfPath),spec_sha256:specSHA,original_snapshot_result_sha256:snapshotSHA,
  direction_result_sha256:spec.original_direction_result_sha256,base_state_sha256:savedStateSHA,
  direction_sha256:spec.direction_raw_sha256,trial_state_sha256:trialSHA,alpha:summary.alpha,
  arrays:outputArrays,all_raw_payloads_artifact_only:true,actual_signed_zero_and_nonfinite_words_preserved:true});
 summary.output_array_manifest=manifestOut;summary.probe_completed=true;summary.elapsed_seconds=(Date.now()-started)/1000;
 const saved=writeJSON('summary.json',summary);
 console.log(encode({event:'actual73-realized-trial-original-noJ-finished',evaluation_returned:summary.evaluation_returned,
  original_noJ_evaluate_calls:summary.original_noJ_evaluate_calls,actual_original_noJ_norm:summary.actual_original_noJ_norm??null,
  observer_io_failure:summary.observer_io_failure,summary:saved,native_accepted:false}).toString().trim());
 return summary;
}

registerHooks({load(url,context,nextLoad){
 const loaded=nextLoad(url,context);
 if(!url.startsWith('file:'))return loaded;
 const actualPath=path.resolve(fileURLToPath(url));
 const original=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 if(actualPath===path.resolve(rootPath)){
  equal(fileSHA(rootPath),rootSHA,'immutable original Fourier momentum root source');
  let transformed=original;
  for(const item of rootReplacements){
   if(transformed.split(item.before).length!==2)throw Error('Unique original root-return observation anchor required');
   transformed=transformed.replace(item.before,item.after);
  }
  let restored=transformed;
  for(const item of [...rootReplacements].reverse()){
   if(restored.split(item.after).length!==2)throw Error('Unique reversible root-return observation span required');
   restored=restored.replace(item.after,item.before);
  }
  equal(restored,original,'complete original runtime root source roundtrip');
  writeJSON('root-return-observer-instrumentation.json.gz',{
   schema:'actual73-realized-trial-root-return-only-observation-v1',hook_sha256:fileSHA(selfPath),
   spec_sha256:specSHA,original_disk_source_sha256:rootSHA,
   original_runtime_source_sha256:sha(original),instrumented_runtime_source_sha256:sha(transformed),
   original_runtime_source:original,instrumented_runtime_source:transformed,replacements:rootReplacements,
   exact_source_roundtrip_verified:true,only_successful_root_return_observed:true,
   original_root_iterations_line_search_and_tolerances_unchanged:true,
   original_root_objects_not_mutated_or_replaced_on_normal_return:true,
   no_extra_root_RHS_or_profile_calls:true,Function_toString_not_modified:true},{compressed:true});
  return {...loaded,source:transformed};
 }
 if(actualPath===path.resolve(enginePath)){
  equal(sha(original),engineSHA,'immutable original retained engine loader source');
  const anchor="const coreURL='data:text/javascript;base64,'+Buffer.from(redirect(core)).toString('base64');";
  if(original.split(anchor).length!==2)throw Error('Unique original completed core-loader anchor required');
  const insertion=`
const originalTrialObservationCore=core;
const originalTrialCellCall=${JSON.stringify(originalCellCall)},observedTrialCellCall=${JSON.stringify(observedCellCall)};
if(core.split(originalTrialCellCall).length!==2)throw Error('Unique actual original cellFlow call required');
core=core.replace(originalTrialCellCall,observedTrialCellCall);
if(core.replace(observedTrialCellCall,originalTrialCellCall)!==originalTrialObservationCore)
 throw Error('The read-only stage observation must restore the whole original runtime core');
fs.writeFileSync(${JSON.stringify(path.join(spec.output,'evaluate-observer-instrumentation.json.gz'))},
 (await import('node:zlib')).gzipSync(Buffer.from(JSON.stringify({
 schema:'actual73-realized-trial-evaluate-stage-observation-v1',hook_sha256:${JSON.stringify(fileSHA(selfPath))},
 spec_sha256:${JSON.stringify(specSHA)},original_disk_core_sha256:sha256(originalCore),
 original_runtime_core_sha256:sha256(originalTrialObservationCore),instrumented_runtime_core_sha256:sha256(core),
 original_runtime_core_source:originalTrialObservationCore,instrumented_runtime_core_source:core,
 before:originalTrialCellCall,after:observedTrialCellCall,exact_source_roundtrip_verified:true,
 original_evaluate_residual_norm_boundary_and_guard_expressions_unchanged:true,
 original_solve_not_called:true,Function_toString_not_modified:true
 })+'\\n')),{flag:'wx'});
`;
  const transformed=original.replace(anchor,insertion+anchor);
  equal(transformed.replace(insertion,''),original,'complete engine-loader insertion roundtrip');
  return {...loaded,source:transformed};
 }
 if(actualPath!==path.resolve(frozenPath))return loaded;
 equal(sha(original),frozenSHA,'immutable original frozen worker source');
 const anchor="try{\n  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));";
 if(original.split(anchor).length!==2)throw Error('Unique original worker final import anchor required');
 const loopStart="for await(const line of readline.createInterface({input:process.stdin,terminal:false})){";
 const loopEnd='process.stdin.destroy();';
 const replacement=`for await(const diagnosticLine of readline.createInterface({input:process.stdin,terminal:false})){
 const request=JSON.parse(diagnosticLine);if(request.stop)break;
 if(request.realized_trial_noJ!==${JSON.stringify(specSHA)})throw Error('The verified selected actual trial request is required');
 const probe=await import(${JSON.stringify(import.meta.url)});
 await probe.runRealizedTrialNoJ(dn,zero,cfg);break;
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
if(diagnosticRestored!==diagnosticOriginal)throw Error('Exact original request-loop source roundtrip required');
fs.writeFileSync(${JSON.stringify(path.join(spec.output,'worker-instrumentation.json'))},JSON.stringify({
 schema:'actual73-realized-trial-original-worker-request-loop-only-v1',hook_sha256:${JSON.stringify(fileSHA(selfPath))},
 spec_sha256:${JSON.stringify(specSHA)},frozen_worker_sha256:${JSON.stringify(frozenSHA)},
 original_compiled_worker_sha256:sha256(diagnosticOriginal),instrumented_compiled_worker_sha256:sha256(source),
 removed_original_loop_sha256:sha256(diagnosticRemoved),diagnostic_loop_sha256:sha256(diagnosticReplacement),
 exact_source_roundtrip_verified:true,only_worker_request_loop_replaced:true,
 other_read_only_root_and_evaluate_observations_separately_declared:true,
 original_constructor_profile_cache_root_RHS_RK_arithmetic_unchanged:true,
 original_solve_and_endpoint_audit_not_called:true,Function_toString_not_modified:true
},null,2)+'\\n',{flag:'wx'});
`;
 const transformed=original.replace(anchor,insertion+anchor);
 equal(transformed.replace(insertion,''),original,'complete worker preload-insertion roundtrip');
 return {...loaded,source:transformed};
}});
