// One live current-C native owner with literal geometry tables and full response.
// Author: geometry agent (AI), 2026-11-15. All scientific execution: public Actions.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import readline from 'node:readline';
import {pathToFileURL,fileURLToPath} from 'node:url';

const M=112,K=224,D=576;
const MODEL='R286-original-stored-continuous-model-convention-C-v1';
const RESULT='current-C-projective-physical-radial-samples-and-general-far-v1';
const SCHEMA='current-C-complete112-live-native-worker-v1';
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const raw=a=>Buffer.from(a.buffer,a.byteOffset,a.byteLength);
const word=x=>{const b=Buffer.alloc(8);b.writeDoubleLE(x);return b.toString('hex');};
const equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
function actions(){
 if(process.env.GITHUB_ACTIONS!=='true'||process.env.GITHUB_REPOSITORY!=='Rogerhu12/math-research-public')
  throw Error('Current-C worker only runs in this public repository Actions');
}
function positive(v,label){if(!(Number.isFinite(v)&&v>0))throw Error('Positive actual '+label+' required');return v;}
function receipt(file){
 const b=fs.readFileSync(file);return {file:path.basename(file),bytes:b.length,sha256:sha(b)};
}
function contained(root,name){
 if(typeof name!=='string'||path.isAbsolute(name))throw Error('Contained payload path required');
 const base=path.resolve(root),p=path.resolve(base,name);
 if(p===base||!p.startsWith(base+path.sep))throw Error('Payload escaped owned root');
 let parent=p;
 while(parent!==base){if(fs.existsSync(parent)&&fs.lstatSync(parent).isSymbolicLink())throw Error('No payload symlinks');parent=path.dirname(parent);}
 return p;
}
function checkedJSON(root,d){
 const p=contained(root,d.file),b=fs.readFileSync(p);
 if(b.length!==d.bytes||sha(b)!==d.sha256)throw Error('Actual source JSON SHA differs: '+d.file);
 return JSON.parse(b);
}
function checkedArray(root,d,shape){
 if(d.completed!==true||d.dtype!=='<f8'||d.order!=='C'||!equal(d.shape,shape))throw Error('Complete array descriptor differs');
 const b=fs.readFileSync(contained(root,d.file));
 if(b.length!==d.bytes||sha(b)!==d.sha256||b.length!==shape.reduce((a,c)=>a*c,1)*8)throw Error('Actual complete array bytes differ');
 const a=new Float64Array(b.length/8);for(let i=0;i<a.length;i++)a[i]=b.readDoubleLE(i*8);
 if(!raw(a).equals(b)||a.some(x=>!Number.isFinite(x)))throw Error('Raw array restoration differs');
 return a;
}
function writeJSON(file,obj){
 const b=Buffer.from(JSON.stringify(obj)+'\n'),fd=fs.openSync(file,'wx');
 try{let pos=0;while(pos<b.length)pos+=fs.writeSync(fd,b,pos,b.length-pos);fs.fsyncSync(fd);}
 finally{fs.closeSync(fd);}
 return {file:path.basename(file),bytes:b.length,sha256:sha(b)};
}
function writeArray(file,parts,shape){
 const fd=fs.openSync(file,'wx'),h=crypto.createHash('sha256');let size=0;
 try{
  for(const a of parts){const b=raw(a);let pos=0;while(pos<b.length)pos+=fs.writeSync(fd,b,pos,b.length-pos);size+=b.length;h.update(b);}
  if(size!==shape.reduce((a,b)=>a*b,1)*8)throw Error('Actual complete output shape differs');
  fs.fsyncSync(fd);
 }finally{fs.closeSync(fd);}
 return {file:path.basename(file),bytes:size,sha256:h.digest('hex'),shape,dtype:'<f8',order:'C',completed:true};
}
function append(file,event){
 const b=Buffer.from(JSON.stringify(event)+'\n'),fd=fs.openSync(file,'a');
 try{let pos=0;while(pos<b.length)pos+=fs.writeSync(fd,b,pos,b.length-pos);fs.fsyncSync(fd);}
 finally{fs.closeSync(fd);}
}
function negativeZeros(a){const out=[];for(let i=0;i<a.length;i++)if(Object.is(a[i],-0))out.push(i);return out;}
function restoreHeight(req){
 if(!Array.isArray(req.height)||req.height.length!==M||req.height.some(v=>!Number.isFinite(v)))
  throw Error('All current physical height coefficients required');
 const H=Float64Array.from(req.height);
 for(const j of req.height_negative_zero_columns??[]){
  if(!Number.isSafeInteger(j)||j<0||j>=M||H[j]!==0)throw Error('Actual height negative-zero sidecar differs');
  H[j]=-0;
 }
 if(req.height_sha256&&sha(raw(H))!==req.height_sha256)throw Error('Actual requested height words differ');
 return H;
}
async function moduleAt(file,expected){
 if(sha(fs.readFileSync(file))!==expected)throw Error('Pinned actual source differs: '+path.basename(file));
 return import(pathToFileURL(file));
}

export function loadGeometry(directory,resultSHA,samplerSourceSHA,steps,diagnosticDirectory){
 const dir=path.resolve(directory),resultRaw=fs.readFileSync(path.join(dir,'result.json'));
 if(sha(resultRaw)!==resultSHA)throw Error('Actual current geometry result differs');
 const result=JSON.parse(resultRaw);
 if(result.schema!==RESULT||result.source_sha256!==samplerSourceSHA||result.target_model_schema!==MODEL||
    result.completed!==true||result.native_geometry_ready!==true||
    result.exact_global_C_realization_of_numeric_representatives_certified!==false||
    result.old_graphs_or_gains_used!==false)
  throw Error('A complete honestly labeled current-C sampling result is required');
 if(result.run_id!==process.env.GITHUB_RUN_ID||result.source_commit!==process.env.GITHUB_SHA)
  throw Error('Current geometry must be produced in this actual job/source');
 const doc=checkedJSON(dir,result.geometry);
 if(doc.schema!=='current-C-native-radial-geometry-bundle-v1'||doc.model_schema!==MODEL||
    doc.modes!==M||doc.spacing!==2||doc.stage_count!==D||doc.steps_per_stage!==steps||
    !equal(doc.rawNode,Array.from({length:9},(_,i)=>72*i))||doc.native_old_graphs_or_gains_used!==false)
  throw Error('Complete current-C stage dimensions differ');
 const nf=doc.field_count_per_stage;
 if(!Number.isSafeInteger(nf)||nf<3)throw Error('Actual full field grid is absent');
 const nodes=checkedArray(dir,doc.arrays.node_radii,[D+1]);
 const mu=checkedArray(dir,doc.arrays.node_mu,[D+1]);
 const fields=checkedArray(dir,doc.arrays.field_geometry,[D,nf,5]);
 const far=checkedArray(dir,doc.arrays.far_matrix,[M,K]);
 if(!Object.is(nodes[0],doc.cut_radius)||!Object.is(nodes[D],doc.finite_far_radius))throw Error('Explicit cut/far words differ');
 const calls=new Uint32Array(D*nf),firstCalls=new Set(),observedFile=path.join(diagnosticDirectory,'actual-original-engine-geometry-words.jsonl');
 const cells=[];
 for(let n=0;n<D;n++){
  positive(nodes[n],'node radius');positive(mu[n],'coordinate mu');
  const packet=doc.stage_packets[n],map=new Map();
  if(packet.stage!==n||packet.rawCell!==Math.floor(n/72)||packet.fields.length!==nf)
   throw Error('Every actual field word and stage must be present');
  for(let j=0;j<nf;j++){
   const start=(n*nf+j)*5,x=fields[start],r=fields[start+1],drdx=fields[start+2],
    logw=fields[start+3],dlogwdx=fields[start+4],key=word(x);
   if(map.has(key)||packet.fields[j].x_word.f64le!==key)throw Error('Actual field argument word mapping differs');
   positive(r,'field radius');positive(drdx,'field radial speed');
   map.set(key,{index:j,x,r,drdx,logw,dlogwdx});
  }
  const port=mu[n]/mu[n+1];
  positive(mu[n+1],'incoming coordinate mu');positive(port,'actual momentum port');
  if(word(port)!==packet.port_ratio_word.f64le||word(mu[n+1])!==packet.mu_word.f64le)
   throw Error('Actual node coordinate / port words differ');
  const profile=x=>{
   const f=map.get(word(x));
   if(!f)throw Error('Original root/flow requested an unproduced current-C field word at stage '+n+': '+word(x));
   calls[n*nf+f.index]++;
   const k=n*nf+f.index;
   if(!firstCalls.has(k)){
    firstCalls.add(k);
    // These are the actual original geometry() exp operations, disclosed separately
    // from the Arb enclosure and from the sampler's auxiliary numeric w field.
    const w=Math.exp(f.logw),w2=Math.exp(2*f.logw),E=1+w2;
    if(!(Number.isFinite(w)&&w>0&&Number.isFinite(w2)&&w2>0&&Number.isFinite(E)))
     throw Error('Actual original exponentials are not finite positive');
    append(observedFile,{schema:SCHEMA+'-actual-field-words',stage:n,field_index:f.index,
     x_f64le:word(x),r_f64le:word(f.r),drdx_f64le:word(f.drdx),logw_f64le:word(f.logw),
     dlogwdx_f64le:word(f.dlogwdx),w_f64le:word(w),w2_f64le:word(w2),E_f64le:word(E),
     original_exp_and_exp_twice_logw_separately_retained:true,
     rigorous_transcendental_rounding_error_not_claimed:true,
     common_global_exact_C_member_not_claimed:true});
   }
   return {r:f.r,drdx:f.drdx,logw:f.logw,dlogwdx:f.dlogwdx};
  };
  cells.push({stage:n,rawCell:packet.rawCell,rawSegment:packet.rawSegment,
   shootingSubsegment:packet.shootingSubsegment,mu:mu[n+1],portRatio:port,profiles:[profile]});
 }
 return {...doc,node_radii:nodes,far_matrix:far,cells,actual_sampler_result:receipt(path.join(dir,'result.json')),
  actual_field_usage:()=>({requested_field_calls:Array.from(calls),
   distinct_requested_fields:firstCalls.size,total_prepared_fields:D*nf,
   complete_unvisited_field_indices:Array.from(calls,(_,i)=>i).filter(i=>calls[i]===0),
   all_unprepared_field_requests_fail_explicitly:true,
   actual_original_engine_geometry_file:fs.existsSync(observedFile)?receipt(observedFile):null})};
}

async function main(){
 actions();
 if(process.argv.length!==3)throw Error('One explicit current-C runtime spec path required');
 const specPath=path.resolve(process.argv[2]),specRaw=fs.readFileSync(specPath),spec=JSON.parse(specRaw);
 if(spec.schema!=='current-C-complete112-native-runtime-spec-v1'||spec.repository!==process.env.GITHUB_REPOSITORY)
  throw Error('Actual independent current-C runtime spec required');
 const comp=path.resolve(spec.computations),out=path.resolve(spec.out);
 if(fs.existsSync(out))throw Error('Fresh current-C native output directory required');
 fs.mkdirSync(out);
 const required=['geometry_20261115_current_C_general_robin_native.mjs',
  'geometry_20261115_current_C_synchronous_linear_bridge.mjs',
  'geometry_20261115_current_C_projective_native_worker.mjs',
  'geometry_20261115_current_C_projective_radial_sampling.py',
  'exact_20261115_current_C_general_robin_chain.py'];
 for(const name of required){
  if(path.basename(name)!==name||sha(fs.readFileSync(path.join(comp,name)))!==spec.source_sha256[name])
   throw Error('Actual new source identity differs: '+name);
 }
 if(sha(fs.readFileSync(fileURLToPath(import.meta.url)))!==spec.source_sha256[path.basename(fileURLToPath(import.meta.url))])
  throw Error('Worker did not execute the bound source');
 const ownerModule=await moduleAt(path.join(comp,required[0]),spec.source_sha256[required[0]]);
 const bridgeModule=await moduleAt(path.join(comp,required[1]),spec.source_sha256[required[1]]);
 const geometry=loadGeometry(spec.geometry_directory,spec.geometry_result_sha256,
  spec.source_sha256[required[3]],spec.steps,out);
 const runtime=await ownerModule.loadOriginalRuntime(spec.source_topic,comp,spec.original_runtime_sha256);
 const linear=bridgeModule.createSynchronousCurrentCLinearBridge({
  directory:path.join(out,'linear-children'),computations:comp,nativeOwnerSource:path.join(comp,required[0]),
  linearSource:path.join(comp,required[4]),ownerSourceSha256:spec.source_sha256[required[0]],
  linearSourceSha256:spec.source_sha256[required[4]],python:spec.python,
  linearBudgetSeconds:spec.linear_budget_seconds,maximumFactorBytes:spec.maximum_factor_bytes});
 const owner=ownerModule.createCurrentCNative({runtime,geometry,linearChild:linear,
  quadrature:spec.quadrature,steps:spec.steps,projectionFloor:spec.projection_floor,
  eta:spec.eta,referenceFloor:spec.reference_floor});
 const cut=owner.cutJets(new Float64Array(K));
 const ready={schema:SCHEMA,ready:true,source_sha256:spec.source_sha256[required[2]],
  runtime_spec:{bytes:specRaw.length,sha256:sha(specRaw)},owner_identity:owner.identity,
  original_C_geometry_result:geometry.actual_sampler_result,
  modes:M,depth:D,cut:{radius:cut.radius,E:cut.E,Ep:cut.Ep},
  linearSlope:null,linearSlope_not_computed_or_assumed:true,
  no_old_node_graphs_or_gains_used:true,
  explicit_zero_cut_root_evaluated:true,zero_height_full_native_response_not_precomputed:true,
  old_metric_or_linear_DN_not_relabelled:true,
  exact_C_and_infinite_nonlinear_DN_certified:false,
  initial_seed:'complete 577-node zero Q/Pi; nonzero cut residual remains part of full model'};
 writeJSON(path.join(out,'ready.json'),ready);process.stdout.write(JSON.stringify(ready)+'\n');
 const log=path.join(out,'native-requests.jsonl');
 let last=null,lastTangent=null,call=0,closed=false;
 function predictor(H){
  if(!last)return {initial:null,receipt:{kind:'initial-complete-zero',has_previous_actual_response:false}};
  let initial=last.states.map(s=>Float64Array.from(s));
  if(lastTangent){
   const d=Float64Array.from(H,(x,j)=>x-last.height[j]),values=lastTangent.values;
   for(let n=0;n<=D;n++)for(let i=0;i<K;i++){
    let add=0;
    for(let j=0;j<M;j++)add+=values[(n*K+i)*M+j]*d[j];
    initial[n][i]+=add;
    if(!Number.isFinite(initial[n][i]))throw Error('Actual all-node current sensitivity predictor is nonfinite');
   }
   return {initial,receipt:{kind:'actual-same-live-current-complete112-sensitivity',
    original_actual_call:last.call,linear_receipt:lastTangent.receipt,
    reference_height_sha256:sha(raw(last.height)),current_height_sha256:sha(raw(H)),
    all_577_nodes_predicted:true,old_Riccati_or_graph_predictor_used:false}};
  }
  return {initial,receipt:{kind:'previous-actual-complete-state-as-initial-guess',
   original_actual_call:last.call,new_height_not_relabelled_as_previous_response:true}};
 }
 const rl=readline.createInterface({input:process.stdin,crlfDelay:Infinity});
 for await(const line of rl){
  if(!line.trim())continue;
  let req;try{req=JSON.parse(line);}catch(error){process.stdout.write(JSON.stringify({ok:false,error:String(error)})+'\n');continue;}
  if(req.close===true){closed=true;break;}
  call++;const dir=path.join(out,'call-'+String(call).padStart(4,'0'));fs.mkdirSync(dir);
  try{
   const H=restoreHeight(req);const input=writeJSON(path.join(dir,'request.json'),req);
   append(log,{event:'current-C-native-request-started',call,actual_height_sha256:sha(raw(H)),
    jacobian:!!req.jacobian,audit:!!req.audit,request:input});
   let pred;
   try{pred=predictor(H);}
   catch(error){pred={initial:last?last.states.map(s=>Float64Array.from(s)):null,
    receipt:{kind:last?'previous-complete-state-after-predictor-arithmetic-failure':'initial-complete-zero',
     error:String(error),no_native_solve_was_retried:true}};}
   writeJSON(path.join(dir,'initial-guess.json'),pred.receipt);
   const response=owner.solve(H,{initial:pred.initial??undefined,jacobian:!!req.jacobian,audit:!!req.audit,
    maxIterations:32,tolerance:2e-9,
    progress:(record,states)=>{
     const stateRows=states.map(s=>Float64Array.from(s));
     const rec=writeArray(path.join(dir,'iteration-'+String(record.iteration).padStart(3,'0')+'-states.f64le'),
      stateRows,[D+1,K]);
     append(path.join(dir,'native-trace.jsonl'),{...record,complete_actual_states:rec});
     process.stderr.write(JSON.stringify({event:'current-C-native-iteration',call,...record})+'\n');
    },
    trialDiagnostic:record=>append(path.join(dir,'native-trials.jsonl'),record),
    failed:record=>{
     const stateRows=record.states.map(s=>Float64Array.from(s));
     const states=writeArray(path.join(dir,'failed-states.f64le'),stateRows,[D+1,K]);
     writeJSON(path.join(dir,'native-failure.json'),{...record,actual_complete_states:states});
    }});
   const stateRows=response.states.map(s=>Float64Array.from(s));
   const stateRaw=writeArray(path.join(dir,'complete-selected-states.f64le'),stateRows,[D+1,K]);
   response.actual_nonlinear_solve=true;response.failed=false;
   response.checkpoint={schema:SCHEMA+'-actual-complete-checkpoint',cutHeight:Array.from(H),
    cutHeight_negative_zero_columns:negativeZeros(H),cutHeight_sha256:sha(raw(H)),
    raw_states:stateRaw,rows:stateRows.map((s,n)=>({node:n,state:Array.from(s),negative_zero_columns:negativeZeros(s)})),
    rawNode:geometry.rawNode,source_sha256:spec.source_sha256[required[2]],
    current_C_geometry_identity:geometry.numeric_geometry_identity,
    actual_current_native_call:call,
    accepted_native_state:response.converged===true,
    accepted_full_BVP_or_closed_surface:false};
   response.predicted=pred.receipt.kind==='actual-same-live-current-complete112-sensitivity';
   response.initialGuess=pred.receipt;
   response.current_C_finite_approximation_scope={
    exact_global_C_realization_of_numerical_representatives_certified:false,
    original_engine_exp_rounding_error_certified:false,
    actual_finite_nonlinear_equations_solved:true,
    infinite_nonlinear_tail_DN_certified:false};
   const result=writeJSON(path.join(dir,'native-result.json'),response);
   if(response.converged){
    last={call,states:stateRows,height:Float64Array.from(H)};
    const tangent=owner.currentCompleteSensitivity();
    lastTangent=tangent?.call===response.call?tangent:null;
   }
   append(log,{event:'current-C-native-request-returned',call,result,
    converged:response.converged,normalizedResidual:response.normalizedResidual,
    jacobian_returned:Array.isArray(response.heightJetJacobian),audit_returned:response.audit!==null});
   process.stdout.write(JSON.stringify({ok:true,result,answer:response})+'\n');
  }catch(error){
   const failure={schema:SCHEMA+'-request-failure',call,error:String(error),actual_nonlinear_solve_failed:true,
    full_BVP_or_closed_surface_not_accepted:true};
   writeJSON(path.join(dir,'request-failure.json'),failure);
   append(log,{event:'current-C-native-request-failed',...failure});
   process.stdout.write(JSON.stringify({ok:false,error:String(error),failure})+'\n');
  }
 }
 const session={schema:SCHEMA+'-completed-session',actual_requests:call,explicit_close:closed,
  bridge:linear.finish(),actual_geometry_usage:geometry.actual_field_usage(),
  last_completed_native_call:last?.call??null,raw_cleanup_not_performed_by_worker:true};
 writeJSON(path.join(out,'session-result.json'),session);
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 main().catch(error=>{process.stderr.write(JSON.stringify({event:'current-C-worker-failed',error:String(error)})+'\n');process.exitCode=1;});
}
