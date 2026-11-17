// Sequential local initial guesses for a complete failed finite tail.
// All physical equations, scales, grids and gates remain the original ones.
// Every changed node causes recomputation of the union of its adjacent rows;
// the full left target and far Robin residual are included in every score.
// Final acceptance can only come from the original full DN solve and audit.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,input,locator,outputRecord,outputSummary,sparseHelper,sourceManifest]=process.argv.slice(2);
if(!sparseHelper||!fs.existsSync(sparseHelper))throw Error('Original sparse helper required');
for(const k of ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'])process.env[k]='1';
process.env.VISIBLE_FLEX_SPARSE_LINEAR_HELPER=path.resolve(sparseHelper);
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const record=JSON.parse(gunzipSync(fs.readFileSync(input)));
const located=JSON.parse(fs.readFileSync(locator));
if(located.input_sha256!==sha(input)||located.inputAccepted||!record.response.failed)
 throw Error('A recorded complete failed input and its exact locator are required');
const sourceHashes={...located.source_sha256};
let additionalSources=record.execution_source_sha256;
if(!additionalSources){
 if(!sourceManifest)throw Error('Native records need their full original source manifest');
 const manifest=JSON.parse(fs.readFileSync(sourceManifest));
 if(manifest.output_record_sha256!==sha(input))throw Error('Source manifest belongs to another input');
 additionalSources=manifest.source_sha256;
}
Object.assign(sourceHashes,additionalSources);
for(const [p,h] of Object.entries(sourceHashes))if(sha(p)!==h)throw Error('Located source changed: '+p);
for(const [name,h] of Object.entries(record.source_sha256)){
 const p=path.resolve(topic,'scripts',name);if(sha(p)!==h)throw Error('Tail source changed: '+p);sourceHashes[p]=h;
}
for(const name of fs.readdirSync(path.join(topic,'scripts/periodic-quadrature'))){
 if(!name.endsWith('.mjs'))continue;
 const p=path.resolve(topic,'scripts/periodic-quadrature',name);
 if(!sourceHashes[p]||sha(p)!==sourceHashes[p])throw Error('Original periodic source binding missing: '+p);
}
sourceHashes[path.resolve(process.argv[1])]=sha(process.argv[1]);
sourceHashes[path.resolve(sparseHelper)]=sha(sparseHelper);
const source=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const cfg=record.config,cp=record.response.checkpoint;
if(!cp?.states||!cp?.cutHeight||cfg.solveTolerance!==2e-9)throw Error('Original complete state and 2e-9 gate required');
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,N=dn.tail.cells.length;
const clone=x=>x.map(v=>Float64Array.from(v));
let states=clone(cp.states);
if(states.length!==N+1||states.some(v=>v.length!==K))throw Error('Complete original grid required');
const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
const target=Float64Array.from(cp.cutHeight,v=>v/radius**4);
const scales=new Float64Array(N+1);
scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
for(let n=0;n<N;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
const began=performance.now();
const original=dn.tail.evaluate(states,target,true,scales);
if(original.norm!==located.replayNormalizedResidual||
 original.norm!==record.response.lastIteration.norm)throw Error('Exact original full replay mismatch');
let residuals=original.residuals.map(v=>Float64Array.from(v));
let norms=residuals.map((r,n)=>Math.max(...Array.from(r,v=>Math.abs(v)/scales[n])));
function boundaryNorm(values){
 let result=0;
 for(let j=0;j<M;j++){
  result=Math.max(result,Math.abs(values[0][j]-target[j])/scales[0]);
  result=Math.max(result,Math.abs(values[N][M+j]-dn.tail.graphs[N][j]*values[N][j])/scales[N]);
 }
 return result;
}
function affectedRows(nodes){
 const rows=new Set();
 for(const n of nodes){if(n>0)rows.add(n-1);if(n<N)rows.add(n);}
 return Array.from(rows).sort((a,b)=>a-b);
}
function local(index,values){
 const cell=dn.tail.cells[index],x=new Float64Array(K+2);x.set(values[index+1]);
 const f=cell.engine.flowStateWithJacobian(x,cell.profiles,{stepsPerSegment:cfg.steps});
 const out=Float64Array.from(f.state.slice(0,K),(v,k)=>k<M?v:v/cell.portRatio);
 const residual=Float64Array.from(out,(v,k)=>v-values[index][k]);
 let norm=0,component=-1;
 for(let k=0;k<K;k++){const v=Math.abs(residual[k])/scales[index];if(v>norm){norm=v;component=k;}}
 return {index,out,residual,norm,component,minA:f.minA,minD:f.minD};
}
function score(values,nodes){
 const indices=affectedRows(nodes),set=new Set(indices);
 const rows=indices.map(n=>local(n,values));
 const untouched=Math.max(boundaryNorm(values),...norms.filter((_,n)=>!set.has(n)));
 return {rows,norm:Math.max(untouched,...rows.map(r=>r.norm)),untouched};
}
const slim=r=>({stage:r.index,norm:r.norm,component:r.component,minA:r.minA,minD:r.minD});
const alphas=[1/8,1/4,5/16,1/3,3/8,1/2,3/4,1];
const betas=[1/8,1/4,1/2,3/4,1],maxPasses=16;
const passes=[];let currentNorm=original.norm,stopped='maximum predeclared passes';
for(let pass=0;pass<maxPasses;pass++){
 if(currentNorm<cfg.solveTolerance){stopped='local full score below original gate; full replay still required';break;}
 let peak={stage:-1,component:-1,norm:0};
 for(let n=2;n<N;n++)for(let j=0;j<K;j++){
  const v=Math.abs(residuals[n][j])/scales[n];
  if(v>peak.norm)peak={stage:n,component:j,norm:v};
 }
 if(peak.norm!==currentNorm){stopped='dominant row is outside the allowed free internal subset';break;}
 const n=peak.stage,j=peak.component,trials=[];
 let best=null;
 function consider(values,alpha,beta,changes){
  let s;
  try{s=score(values,changes.map(c=>c.stage));}
  catch(error){trials.push({alpha,beta,changes,domain_rejected:String(error)});return null;}
  const row={alpha,beta,norm:s.norm,untouched:s.untouched,changes,affected:s.rows.map(slim)};
  trials.push(row);
  if(s.norm<currentNorm&&(!best||s.norm<best.norm))best={...row,states:clone(values),rows:s.rows};
  return s;
 }
 for(const alpha of alphas){
  const values=clone(states);
  values[n][j]=states[n][j]+alpha*residuals[n][j];
  if(values[n][j]===states[n][j])continue;
  const changes=[{stage:n,component:j,before:states[n][j],after:values[n][j]}];
  const s=consider(values,alpha,0,changes);
  if(!s)continue;
  const downstream=s.rows.find(r=>r.index===n),upstream=s.rows.find(r=>r.index===n-1);
  if(downstream.norm>cfg.solveTolerance||upstream.norm<=cfg.solveTolerance||upstream.component<0)continue;
  const k=upstream.component;
  for(const beta of betas){
   const pair=clone(values);
   pair[n-1][k]=states[n-1][k]+beta*upstream.residual[k];
   if(pair[n-1][k]===states[n-1][k])continue;
   consider(pair,alpha,beta,[...changes,
    {stage:n-1,component:k,before:states[n-1][k],after:pair[n-1][k]}]);
  }
 }
 const report={pass,before_norm:currentNorm,peak,local_trial_count:trials.length,trials};
 if(!best){report.selected=null;passes.push(report);stopped='no strict local full-score improvement';break;}
 report.selected={alpha:best.alpha,beta:best.beta,norm:best.norm,changes:best.changes,affected:best.affected};
 passes.push(report);states=best.states;currentNorm=best.norm;
 for(const row of best.rows){residuals[row.index]=Float64Array.from(row.residual);norms[row.index]=row.norm;}
 console.log(JSON.stringify({event:'selected_local_pass',pass,before:report.before_norm,
  after:currentNorm,peak,alpha:best.alpha,beta:best.beta,changes:best.changes}));
}
const summary={scope:'Sequential local flow-relaxation initial guesses, with every changed node dependency union and both original boundary residuals included. Only a strict full-Jacobian residual improvement permits invoking the unchanged original DN solver and full audit. This is not a new acceptance gate.',
 command:process.argv,input_sha256:sha(input),locator_sha256:sha(locator),source_sha256:sourceHashes,
 source_manifest_sha256:sourceManifest?sha(sourceManifest):null,
 original_gate:cfg.solveTolerance,alphas,betas,maxPasses,passes,stopped,
 before:{norm:original.norm,minA:original.minA,minD:original.minD,boundary_norm:boundaryNorm(clone(cp.states))},
 local_predicted_norm:currentNorm,all_physical_and_solver_parameters_unchanged:true};
const whole=dn.tail.evaluate(states,target,true,scales);
summary.full_candidate_replay={norm:whole.norm,minA:whole.minA,minD:whole.minD,
 matches_local_predicted_norm:whole.norm===currentNorm,boundary_norm:boundaryNorm(states)};
console.log(JSON.stringify({event:'full_candidate_replay',...summary.full_candidate_replay}));
let response=null,progressStates=null,progressRow=null;
if(!(whole.norm<original.norm)){
 summary.original_solver_invoked=false;
 summary.reason='No strict full original residual improvement; original solver is not repeated.';
}else{
 summary.original_solver_invoked=true;
 try{
  const sol=dn.solve(cp.cutHeight,{initial:states,maxIterations:cfg.maxIterations,
   tolerance:cfg.solveTolerance,jacobian:true,audit:true,auditSteps:cfg.auditSteps??cfg.steps,
   progress:(row,values)=>{if(values){progressStates=values;progressRow=row;}
    console.log(JSON.stringify({event:'original_solve_iteration',...row}));}});
  const checkpoint={parameters:sol.parameters,states:sol.states,rawNode:dn.tail.rawNode,
   rawStates:dn.tail.rawNode.map(k=>sol.states[k]),cutHeight:cp.cutHeight,
   scope:'Unchanged original finite DN output after a declared initial-state sequence; no prefix or closure acceptance.'};
  response={converged:sol.converged,residual:sol.normalizedResidual,jets:sol.jets,
   heightJetJacobian:sol.heightJetJacobian??null,history:sol.history,audit:sol.audit,checkpoint};
  summary.original_solver_converged=sol.converged;summary.final_residual=sol.normalizedResidual;
  summary.final_minA=sol.minA;summary.final_minD=sol.minD;summary.audit=sol.audit;summary.history=sol.history;
 }catch(error){
  response={failed:String(error),lastIteration:progressRow,checkpoint:progressStates?{
   parameters:dn.tail.parameters,states:progressStates,rawNode:dn.tail.rawNode,
   rawStates:dn.tail.rawNode.map(k=>progressStates[k]),cutHeight:cp.cutHeight,
   scope:'Failed unchanged original solve after sequential local initial-state relaxation.'}:null};
  summary.original_solver_converged=false;summary.error=String(error);
 }
}
const result={request:{height:cp.cutHeight,jacobian:true,audit:true},response,config:cfg,
 source_sha256:record.source_sha256,execution_source_sha256:sourceHashes,
 scope:'Original finite DN response from sequential local initial-state candidates; equations and all gates unchanged.'};
fs.writeFileSync(outputRecord,gzipSync(JSON.stringify(result)+'\n'));
summary.output_record_sha256=sha(outputRecord);summary.seconds=(performance.now()-began)/1000;
fs.writeFileSync(outputSummary,JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify({event:'terminal',invoked:summary.original_solver_invoked,
 converged:summary.original_solver_converged,residual:summary.final_residual,
 error:summary.error,seconds:summary.seconds,output_record_sha256:summary.output_record_sha256}));
