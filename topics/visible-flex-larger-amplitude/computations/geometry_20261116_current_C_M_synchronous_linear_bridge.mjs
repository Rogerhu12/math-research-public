// Actual complete-M current-C native -> synchronous general-chain child, full raw words.
// Author: exact-refinement agent (AI), 2026-11-16. Independent dimension binding; no old source edits.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

export const SCHEMA='current-C-complete-M-synchronous-general-Robin-bridge-v1';
const SNAPSHOT='current-C-complete-M-native-linear-snapshot-v1';
const RESULT='current-C-complete-M-general-Robin-complete-chain-linear-result-v1';
const MODEL='R286-original-stored-continuous-model-convention-C-v1';
const D=576;
function fieldModes(value){
 if(!Number.isSafeInteger(value)||value<112)
  throw Error('Explicit field_modes integer at least112 required for complete mode expansion');
 return value;
}
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const canonical=x=>JSON.stringify(x,Object.keys(x).sort()); // unused for nested input identities
function actions(){
 if(process.env.GITHUB_ACTIONS!=='true'||process.env.GITHUB_REPOSITORY!=='Rogerhu12/math-research-public')
  throw Error('Current-C bridge is scientific execution in the named public repository only');
 if(os.endianness()!=='LE')throw Error('Actual raw arrays require little-endian runtime');
}
function jsonBytes(value){return Buffer.from(JSON.stringify(value,null,2)+'\n');}
function numberRecord(x){
 if(typeof x!=='number')throw Error('Actual Number required for original word record');
 const b=Buffer.alloc(8);b.writeDoubleLE(x);
 return {value:Number.isFinite(x)?x:null,f64le:b.toString('hex'),
  classification:Number.isNaN(x)?'NaN':x===Infinity?'positive-infinity':
   x===-Infinity?'negative-infinity':Object.is(x,-0)?'negative-zero':'finite'};
}
function fileReceipt(file){
 const fd=fs.openSync(file,'r');const buffer=Buffer.allocUnsafe(1<<20);
 const h=crypto.createHash('sha256');let bytes=0;
 try{for(;;){const n=fs.readSync(fd,buffer,0,buffer.length,null);if(!n)break;bytes+=n;h.update(buffer.subarray(0,n));}}
 finally{fs.closeSync(fd);}
 return {file:path.basename(file),bytes,sha256:h.digest('hex')};
}
function writeBytes(file,bytes){
 const fd=fs.openSync(file,'wx');
 try{let pos=0;while(pos<bytes.length)pos+=fs.writeSync(fd,bytes,pos,bytes.length-pos);fs.fsyncSync(fd);}
 finally{fs.closeSync(fd);}
 return {file:path.basename(file),bytes:bytes.length,sha256:hash(bytes)};
}
function writeJSON(file,value){return writeBytes(file,jsonBytes(value));}
function contained(root,relative){
 if(typeof relative!=='string'||relative.length===0||path.isAbsolute(relative))throw Error('Contained original file required');
 const base=path.resolve(root),p=path.resolve(base,relative);
 if(p===base||!p.startsWith(base+path.sep))throw Error('Payload path escaped request root');
 let cur=p;
 while(cur!==base){if(fs.existsSync(cur)&&fs.lstatSync(cur).isSymbolicLink())throw Error('No symlink payload path');cur=path.dirname(cur);}
 return p;
}
function bytes(view){return Buffer.from(view.buffer,view.byteOffset,view.byteLength);}
function typed(value,shape,label){
 const n=shape.reduce((a,b)=>a*b,1);
 if(!(value instanceof Float64Array)||value.length!==n)throw Error('Complete actual typed array differs: '+label);
 for(const x of value)if(!Number.isFinite(x))throw Error('Nonfinite actual input: '+label);
 return value;
}
function saveArray(root,name,shape,parts){
 const target=contained(root,'large-arrays/'+name+'.f64le'),fd=fs.openSync(target,'wx');
 const h=crypto.createHash('sha256');let count=0,words=0;
 try{
  for(const part of parts){
   if(!(part instanceof Float64Array))throw Error('Original Float64Array parts required: '+name);
   for(const x of part)if(!Number.isFinite(x))throw Error('Nonfinite actual input '+name);
   const b=bytes(part);let pos=0;
   while(pos<b.length)pos+=fs.writeSync(fd,b,pos,b.length-pos);
   h.update(b);count+=b.length;words+=part.length;
  }
  if(words!==shape.reduce((a,b)=>a*b,1))throw Error('Incomplete current array '+name);
  fs.fsyncSync(fd);
 }finally{fs.closeSync(fd);}
 return {name,file:'large-arrays/'+name+'.f64le',bytes:count,sha256:h.digest('hex'),
  dtype:'<f8',order:'C',shape,completed:true};
}
function readJSON(root,desc){
 const file=contained(root,desc.file),b=fs.readFileSync(file);
 if(b.length!==desc.bytes||hash(b)!==desc.sha256)throw Error('Actual JSON bytes differ: '+desc.file);
 return JSON.parse(b);
}
function readArray(root,desc,shape){
 if(!desc||desc.dtype!=='<f8'||desc.order!=='C'||desc.completed!==true||
    JSON.stringify(desc.shape)!==JSON.stringify(shape))throw Error('Complete recovered array descriptor differs');
 const b=fs.readFileSync(contained(root,desc.file));
 if(b.length!==desc.bytes||hash(b)!==desc.sha256||b.length!==shape.reduce((a,c)=>a*c,1)*8)
  throw Error('Actual recovered complete binary words differ');
 const a=new Float64Array(b.length/8);
 for(let i=0;i<a.length;i++){a[i]=b.readDoubleLE(8*i);if(!Number.isFinite(a[i]))throw Error('Nonfinite current child answer');}
 if(!bytes(a).equals(b))throw Error('Full answer restoration changed an original signed-zero word');
 return a;
}
function sorted(value){
 if(Array.isArray(value))return value.map(sorted);
 if(value!==null&&typeof value==='object')return Object.fromEntries(Object.keys(value).sort().map(k=>[k,sorted(value[k])]));
 return value;
}
function same(a,b,label){
 if(JSON.stringify(sorted(a))!==JSON.stringify(sorted(b)))throw Error('Actual identity differs: '+label);
}
function source(file,expected,label){
 const r=fileReceipt(file);
 if(!/^[0-9a-f]{64}$/.test(expected??'')||r.sha256!==expected)throw Error('Actual pinned '+label+' source differs');
 return r;
}
function writeEvent(file,event){
 const fd=fs.openSync(file,'a');
 try{const b=Buffer.from(JSON.stringify(event)+'\n');let pos=0;
  while(pos<b.length)pos+=fs.writeSync(fd,b,pos,b.length-pos);fs.fsyncSync(fd);}
 finally{fs.closeSync(fd);}
}
function stableArrayCopy(a){const b=new Float64Array(a.length);b.set(a);return b;}

export function createSynchronousCurrentCLinearBridge(options){
 actions();
 const M=fieldModes(options.fieldModes),K=2*M;
 const root=path.resolve(options.directory),comps=path.resolve(options.computations);
 const owner=path.resolve(options.nativeOwnerSource),solver=path.resolve(options.linearSource);
 if(fs.existsSync(root))throw Error('A fresh exclusively owned bridge directory is required');
 const sourceRecord={
  bridge:fileReceipt(fileURLToPath(import.meta.url)),
  owner:source(owner,options.ownerSourceSha256,'native owner'),
  linear:source(solver,options.linearSourceSha256,'general Robin child')
 };
 if(path.dirname(solver)!==comps)throw Error('The pinned child must be from the bound computation directory');
 if(typeof options.python!=='string'||!options.python.length)throw Error('Explicit Python executable required');
 if(!(Number.isFinite(options.linearBudgetSeconds)&&options.linearBudgetSeconds>0)||
    !Number.isSafeInteger(options.maximumFactorBytes)||options.maximumFactorBytes<=0)
  throw Error('Explicit positive linear resource budgets required');
 fs.mkdirSync(root,{recursive:false});
 const events=path.join(root,'bridge-events.jsonl');
 const completeRecords=[];
 let sequence=0,active=false;
 const bridgeIdentity={schema:SCHEMA,source_records:sourceRecord,
  field_modes:M,shape_dimension:K,stage_count:D,
  original_algorithms_replaced:false,
  current_general_far_matrix_is_used_in_factor_and_readback:true,
  correction_eta_is_not_reused_for_sensitivity:true,
  no_linear_residual_acceptance_gate:true,
  negative_zero_words_retained:true,
  raw_owned_temporary_only:true};
 writeJSON(path.join(root,'bridge-identity.json'),bridgeIdentity);

 function run(request){
  actions();
  if(active)throw Error('A synchronous owner may not overlap current-chain requests');
  active=true;const id=sequence++;
  const local='call-'+String(request.call).padStart(4,'0')+'-seq-'+String(id).padStart(4,'0')+'-'+request.kind;
  const dir=contained(root,local),snapshot=path.join(dir,'snapshot'),out=path.join(dir,'linear-result');
  fs.mkdirSync(dir);fs.mkdirSync(snapshot);fs.mkdirSync(path.join(snapshot,'large-arrays'));
  const started=Date.now();let processResult=null,snapshotReceipt=null,resultReceipt=null;
  let stage='snapshot',actualResult=null;
  try{
   if(request.kind!=='correction'&&request.kind!=='sensitivity')throw Error('Unknown current linear operation');
   if(!Number.isSafeInteger(request.call)||request.call<1||
      (request.kind==='correction'&&(!Number.isSafeInteger(request.iteration)||request.iteration<0))||
      (request.kind==='sensitivity'&&request.iteration!==null))
    throw Error('Actual native call and iteration metadata required');
   if(request.modes!==M||request.stage_count!==D||JSON.stringify(request.full_shape)!==JSON.stringify([D+1,K]))
    throw Error('Current complete chain dimensions changed');
   if(request.identity.source_sha256!==sourceRecord.owner.sha256||
      request.identity.parameters?.old_graphs_or_gains_used===true||
      request.identity.parameter_record?.old_graphs_or_gains_used!==false)
    throw Error('Current owner/source scope differs');
   if(!request.identity.original_C_input_binding||!request.identity.numeric_geometry_identity)
    throw Error('Complete same-C geometry and actual sampling identity required');
   if(!Array.isArray(request.states)||request.states.length!==D+1||
      !Array.isArray(request.ev.flows)||request.ev.flows.length!==D||
      !Array.isArray(request.ev.residuals)||request.ev.residuals.length!==D)
    throw Error('All actual original nodes/stages are required');
   if(!(Number.isFinite(request.cutRadius)&&request.cutRadius>0)||
      !(Number.isFinite(request.cutHeightDenominator)&&request.cutHeightDenominator>0))
    throw Error('Actual native cut/denominator words required');
   const states=request.states.map((v,i)=>typed(v,[K],'state '+i));
   const flows=request.ev.flows;
   const arrays={
    'base-states':saveArray(snapshot,'base-states',[D+1,K],states),
    'target':saveArray(snapshot,'target',[M],[typed(request.target,[M],'target')]),
    'scales':saveArray(snapshot,'scales',[D+1],[typed(request.scales,[D+1],'scales')]),
    'stage-jacobians':saveArray(snapshot,'stage-jacobians',[D,K,K],flows.map((f,i)=>typed(f.J,[K,K],'fresh stage J '+i))),
    'stage-residuals':saveArray(snapshot,'stage-residuals',[D,K],request.ev.residuals.map((v,i)=>typed(v,[K],'actual residual '+i))),
    'cut-residual':saveArray(snapshot,'cut-residual',[M],[typed(request.ev.cut,[M],'actual cut residual')]),
    'far-residual':saveArray(snapshot,'far-residual',[M],[typed(request.ev.end,[M],'actual general far residual')]),
    'far-matrix':saveArray(snapshot,'far-matrix',[M,K],[typed(request.farMatrix,[M,K],'complete general far matrix')]),
    'stage-out':saveArray(snapshot,'stage-out',[D,K],flows.map((f,i)=>typed(f.out,[K],'actual stage output '+i))),
    'stage-mean-state':saveArray(snapshot,'stage-mean-state',[D,2],flows.map((f,i)=>typed(f.completeMeanState,[2],'both complete means '+i))),
    'stage-mean-jacobians':saveArray(snapshot,'stage-mean-jacobians',[D,2,K],flows.map((f,i)=>typed(f.meanRows,[2,K],'both complete mean tangent rows '+i)))
   };
   const metadata={schema:SNAPSHOT,model_schema:MODEL,native_owner_source_sha256:sourceRecord.owner.sha256,
    bridge_source_sha256:sourceRecord.bridge.sha256,linear_child_source_sha256:sourceRecord.linear.sha256,
    repository:process.env.GITHUB_REPOSITORY,run_id:process.env.GITHUB_RUN_ID,
    source_commit:process.env.GITHUB_SHA,kind:request.kind,call:request.call,
    iteration:request.iteration,snapshot_sequence:id,modes:M,depth:D,shape_dimension:K,
    old_graphs_or_gains_used:false,
    original_C_input_binding:request.identity.original_C_input_binding,
    numeric_geometry_identity:request.identity.numeric_geometry_identity,
    owner_identity:request.identity,cut_radius:request.cutRadius,
    cut_height_denominator:request.cutHeightDenominator,
    cut_radius_word:numberRecord(request.cutRadius),
    cut_height_denominator_word:numberRecord(request.cutHeightDenominator),
    arrays,actual_norm:numberRecord(request.ev.norm),actual_minA:numberRecord(request.ev.minA),
    actual_minD:numberRecord(request.ev.minD),
    original_stage_returns:flows.map((f,i)=>({stage:i,meanHeight:numberRecord(f.meanHeight),
     minA:numberRecord(f.minA),minD:numberRecord(f.minD)})),
    source_of_snapshot:'One actual completed current native withJ evaluation, never a relabelled historical state',
    complete_means_do_not_feed_shape_again:true};
   snapshotReceipt=writeJSON(path.join(snapshot,'snapshot.json'),metadata);
   writeJSON(path.join(dir,'launch.json'),{schema:SCHEMA+'-launch',source_records:sourceRecord,
    snapshot:snapshotReceipt,kind:request.kind,call:request.call,iteration:request.iteration,
    sequence:id,eta:numberRecord(request.eta),
    linear_budget_seconds:options.linearBudgetSeconds,
    maximum_factor_bytes:options.maximumFactorBytes,
    output:path.basename(out),shell:false,child_stdout:'linear.stdout.log',child_stderr:'linear.stderr.log'});
   writeEvent(events,{event:'current-C-linear-child-started',sequence:id,call:request.call,
    iteration:request.iteration,kind:request.kind,directory:local,snapshot:snapshotReceipt});
   stage='child';
   const args=[solver,'--field-modes',String(M),'--snapshot-directory',snapshot,'--snapshot-result-sha256',snapshotReceipt.sha256,
    '--native-owner-source',owner,'--computations',comps,'--eta',String(request.eta),
    '--budget-seconds',String(options.linearBudgetSeconds),'--max-factor-bytes',String(options.maximumFactorBytes),
    '--out',out];
   const env={...process.env,PYTHONDONTWRITEBYTECODE:'1',PYTHONUNBUFFERED:'1'};
   for(const name of ['GH_TOKEN','GITHUB_TOKEN','MR_TOKEN'])delete env[name];
   const stdout=fs.openSync(path.join(dir,'linear.stdout.log'),'wx');
   const stderr=fs.openSync(path.join(dir,'linear.stderr.log'),'wx');
   try{
    processResult=spawnSync(options.python,args,{cwd:comps,env,shell:false,
     stdio:['ignore',stdout,stderr],timeout:Math.ceil((options.linearBudgetSeconds+120)*1000),
     killSignal:'SIGTERM'});
   }finally{fs.fsyncSync(stdout);fs.fsyncSync(stderr);fs.closeSync(stdout);fs.closeSync(stderr);}
   const exit={schema:SCHEMA+'-exit',sequence:id,status:processResult.status,
    signal:processResult.signal??null,error:processResult.error?String(processResult.error):null,
    elapsed_wall_milliseconds:Date.now()-started,
    stdout:fileReceipt(path.join(dir,'linear.stdout.log')),stderr:fileReceipt(path.join(dir,'linear.stderr.log'))};
   writeJSON(path.join(dir,'child-exit.json'),exit);
   const resultFile=path.join(out,'result.json');
   if(fs.existsSync(resultFile)){
    resultReceipt=fileReceipt(resultFile);actualResult=JSON.parse(fs.readFileSync(resultFile));
   }
   if(processResult.error||processResult.signal||processResult.status!==0)
    throw Error('Actual current linear child failed; status='+processResult.status+' signal='+processResult.signal+
     ' child_error='+(actualResult?.error??String(processResult.error??'')));
   stage='readback';
   if(!actualResult||actualResult.schema!==RESULT||actualResult.source_sha256!==sourceRecord.linear.sha256||
      actualResult.completed!==true||actualResult.failed!==false||actualResult.kind!==request.kind||
      !Object.is(actualResult.eta,request.eta)||actualResult.nonlinear_native_accepted!==false||
      actualResult.new_RHS_calls!==0||actualResult.new_J_calls!==0||actualResult.new_ODE_steps!==0||
      actualResult.exact_saved_matrix_nonresonance_certified!==false)
    throw Error('Actual current complete child result scope differs');
   const input=actualResult.input_binding;
   same(input.snapshot,snapshotReceipt,'complete actual snapshot receipt');
   if(input.native_owner_source_sha256!==sourceRecord.owner.sha256||input.source_sha256!==sourceRecord.linear.sha256||
      input.call!==request.call||input.iteration!==request.iteration||input.kind!==request.kind||
      input.no_old_graph_or_gain_used!==true||input.no_interior_height_divisibility_assumed!==true)
    throw Error('Actual child current identity differs');
   same(input.original_C_input_binding,metadata.original_C_input_binding,'same original C');
   same(input.numeric_geometry_identity,metadata.numeric_geometry_identity,'same actual geometry sampler');
   same(input.all_arrays,arrays,'complete exact original array descriptors');
   same(input.actual_cut_height_denominator,numberRecord(request.cutHeightDenominator),'native denominator word');
   same(readJSON(out,actualResult.input_binding_file),input,'retained actual binding');
   const manifest=readJSON(out,actualResult.output_array_manifest);
   if(manifest.schema!=='current-C-complete-M-general-chain-arrays-v1'||!Array.isArray(manifest.arrays))
    throw Error('Current complete output manifest differs');
   const answerDesc=request.kind==='correction'?actualResult.delta:actualResult.cut_sensitivity;
   const inManifest=manifest.arrays.filter(d=>d.file===answerDesc?.file);
   if(inManifest.length!==1)throw Error('Original answer absent from complete output manifest');
   same(inManifest[0],answerDesc,'actual complete answer descriptor');
   const answer=readArray(out,answerDesc,request.kind==='correction'?[D+1,K,1]:[K,M]);
   const common={kind:request.kind,eta:request.eta,columns:request.kind==='correction'?1:M,
    receipt:{schema:SCHEMA+'-returned',call:request.call,iteration:request.iteration,sequence:id,
     directory:local,actual_snapshot:snapshotReceipt,actual_child_result:resultReceipt,
     actual_input_matrix_identity:actualResult.input_matrix_identity,answer:answerDesc,
     source_records:sourceRecord,complete_original_words_verified:true,
     exact_readback_is_not_an_acceptance_gate:true,
     exact_saved_matrix_nonresonance_certified:false},
    exact_saved_matrix_nonresonance_certified:false};
   let response;
   if(request.kind==='correction'){
    response={...common,delta:Array.from({length:D+1},(_,n)=>stableArrayCopy(answer.subarray(n*K,(n+1)*K)))};
   }else{
    const fullDesc=actualResult.complete_all_node_sensitivity;
    const fullEntries=manifest.arrays.filter(d=>d.file===fullDesc?.file);
    if(fullEntries.length!==1)throw Error('Complete all-node sensitivity absent from original manifest');
    same(fullEntries[0],fullDesc,'all 577 node sensitivity descriptor');
    const all=readArray(out,fullDesc,[D+1,K,M]);
    if(!bytes(all.subarray(0,K*M)).equals(bytes(answer)))
     throw Error('Cut sensitivity differs from node0 of complete original sensitivity');
    common.receipt.complete_all_node_sensitivity=fullDesc;
    response={...common,cut_sensitivity:answer,complete_all_node_sensitivity:all};
   }
   writeJSON(path.join(dir,'returned-correction.json'),common.receipt);
   writeEvent(events,{event:'current-C-linear-child-returned',sequence:id,call:request.call,
    iteration:request.iteration,kind:request.kind,directory:local,receipt:common.receipt});
   completeRecords.push(common.receipt);
   // Only independent answer words are returned. Future native calls do not read this old raw directory.
   return response;
  }catch(error){
   const failure={schema:SCHEMA+'-failure',sequence:id,call:request.call??null,iteration:request.iteration??null,
    kind:request.kind??null,stage,error:String(error),snapshot:snapshotReceipt,actual_child_result:resultReceipt,
    child_status:processResult?.status??null,child_signal:processResult?.signal??null,
    elapsed_wall_milliseconds:Date.now()-started,complete_answer_not_returned:true,
    nonlinear_trial_rejection_not_inferred:true,raw_retained_under_owned_directory:true};
   writeJSON(path.join(dir,'bridge-failure.json'),failure);
   writeEvent(events,{event:'current-C-linear-child-failed',directory:local,...failure});
   throw error;
  }finally{active=false;}
 }
 run.identity=bridgeIdentity;
 run.finish=()=>{
  if(active)throw Error('Cannot finish while the actual child is running');
  const result={schema:SCHEMA+'-session',source_records:sourceRecord,attempted_children:sequence,
   completed_children:completeRecords.length,complete_records:completeRecords,
   old_graphs_or_gains_used:false,raw_deleted_by_bridge:false,
   raw_cleanup_owner:'outer Actions wrapper after all actual scalar readouts'};
  return writeJSON(path.join(root,'session-result.json'),result);
 };
 return run;
}
