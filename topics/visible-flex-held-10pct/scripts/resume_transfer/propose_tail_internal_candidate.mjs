// Candidate only: never call dn.solve and never report convergence.
// Only original free internal shooting states are relaxed. The original
// full-Jacobian evaluator decides strict residual improvement. A separate
// unchanged original worker must solve and accept this candidate.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const [topicArg,inputArg,outputArg,summaryArg,locatorArg] = process.argv.slice(2);
const topic=path.resolve(topicArg),input=path.resolve(inputArg);
const output=path.resolve(outputArg),summaryPath=path.resolve(summaryArg);
if(fs.existsSync(output)||fs.existsSync(summaryPath))throw Error('Candidate outputs must be new');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const same=(a,b)=>typeof a===typeof b && (typeof a==='number'?Object.is(a,b):
  a===null||b===null||typeof a!=='object'?a===b:
  Object.keys(a).length===Object.keys(b).length && Object.keys(a).every(k=>Object.hasOwn(b,k)&&same(a[k],b[k])));
const record=JSON.parse(gunzipSync(fs.readFileSync(input))),cfg=record.config,cp=record.response?.checkpoint;
if(!record.response?.failed||!cp?.states||!cp?.cutHeight||!record.response.lastIteration)
  throw Error('A complete original failed response is required');
if(cfg.solveTolerance!==2e-9||cfg.sharedEngines===true||cfg.spacing!==3)
  throw Error('This adapter binds the original nonshared m3 2e-9 worker');
if(!same(record.request.height,cp.cutHeight))throw Error('Request and failed checkpoint heights differ');
const sources={};
for(const [name,digest] of Object.entries(record.source_sha256)){
  const p=path.resolve(topic,'scripts',name);
  if(sha(p)!==digest)throw Error('Original source changed: '+p);
  sources[p]=digest;
}
let located=null;
if(locatorArg){
  located=JSON.parse(fs.readFileSync(locatorArg));
  if(located.input_sha256!==sha(input)||located.inputAccepted)
    throw Error('Locator belongs to a different or accepted state');
  for(const [p,digest] of Object.entries(located.source_sha256)){
    if(sha(p)!==digest)throw Error('Locator source changed: '+p);
    sources[path.resolve(p)]=digest;
  }
}
sources[path.resolve(process.argv[1])]=sha(process.argv[1]);
const source=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,N=dn.tail.cells.length;
const clone=x=>x.map(v=>Float64Array.from(v));
let states=clone(cp.states);
if(states.length!==N+1||states.some(v=>v.length!==K||!v.every(Number.isFinite)))
  throw Error('The complete original grid and finite values are required');
if(!same(cp.rawNode,dn.tail.rawNode))throw Error('The original raw-node subdivision changed');
const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
const target=Float64Array.from(cp.cutHeight,v=>v/radius**4);
if(target.length!==M||cp.cutHeight[0]===0)throw Error('Nonzero first height and exact original target required');
const zeroBoundary=values=>Array.from(target).every((v,j)=>Object.is(v-values[0][j],0));
if(!zeroBoundary(states))throw Error('Original worker boundary correction would be nonzero');
const scales=new Float64Array(N+1);
scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
for(let n=0;n<N;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
const began=performance.now();
const original=dn.tail.evaluate(states,target,true,scales);
if(original.norm!==record.response.lastIteration.norm||
   (located&&original.norm!==located.replayNormalizedResidual))
  throw Error('Original full-Jacobian replay does not match the recorded failure');
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
  if(!out.every(Number.isFinite))throw Error('Nonfinite local candidate');
  const residual=Float64Array.from(out,(v,k)=>v-values[index][k]);
  let norm=0,component=-1;
  for(let k=0;k<K;k++){const v=Math.abs(residual[k])/scales[index];if(v>norm){norm=v;component=k;}}
  return {index,residual,norm,component,minA:f.minA,minD:f.minD};
}
function score(values,nodes){
  const indices=affectedRows(nodes),set=new Set(indices),rows=indices.map(n=>local(n,values));
  const untouched=Math.max(boundaryNorm(values),...norms.filter((_,n)=>!set.has(n)));
  return {rows,norm:Math.max(untouched,...rows.map(r=>r.norm)),untouched};
}
const slim=r=>({stage:r.index,norm:r.norm,component:r.component,minA:r.minA,minD:r.minD});
const alphas=[1/8,1/4,5/16,1/3,3/8,1/2,3/4,1];
const betas=[1/8,1/4,1/2,3/4,1],maxPasses=16;
const passes=[];let currentNorm=original.norm,stopped='maximum predeclared passes';
for(let pass=0;pass<maxPasses;pass++){
  if(currentNorm<cfg.solveTolerance){stopped='candidate full score below original gate; not solver acceptance';break;}
  let peak={stage:-1,component:-1,norm:0};
  for(let n=2;n<N;n++)for(let j=0;j<K;j++){
    const v=Math.abs(residuals[n][j])/scales[n];if(v>peak.norm)peak={stage:n,component:j,norm:v};
  }
  if(peak.norm!==currentNorm){stopped='dominant residual outside the allowed internal subset';break;}
  const n=peak.stage,j=peak.component,trials=[];let best=null;
  function consider(values,alpha,beta,changes){
    let s;try{s=score(values,changes.map(c=>c.stage));}
    catch(error){trials.push({alpha,beta,changes,domain_rejected:String(error)});return null;}
    const row={alpha,beta,norm:s.norm,untouched:s.untouched,changes,affected:s.rows.map(slim)};
    trials.push(row);
    if(s.norm<currentNorm&&(!best||s.norm<best.norm))best={...row,states:clone(values),rows:s.rows};
    return s;
  }
  for(const alpha of alphas){
    const values=clone(states);values[n][j]=states[n][j]+alpha*residuals[n][j];
    if(values[n][j]===states[n][j])continue;
    const changes=[{stage:n,component:j,before:states[n][j],after:values[n][j]}];
    const s=consider(values,alpha,0,changes);if(!s)continue;
    const downstream=s.rows.find(r=>r.index===n),upstream=s.rows.find(r=>r.index===n-1);
    if(downstream.norm>cfg.solveTolerance||upstream.norm<=cfg.solveTolerance||upstream.component<0)continue;
    const k=upstream.component;
    for(const beta of betas){
      const pair=clone(values);pair[n-1][k]=states[n-1][k]+beta*upstream.residual[k];
      if(pair[n-1][k]===states[n-1][k])continue;
      consider(pair,alpha,beta,[...changes,{stage:n-1,component:k,before:states[n-1][k],after:pair[n-1][k]}]);
    }
  }
  const report={pass,before_norm:currentNorm,peak,local_trial_count:trials.length,trials};
  if(!best){report.selected=null;passes.push(report);stopped='no strict local full-score improvement';break;}
  report.selected={alpha:best.alpha,beta:best.beta,norm:best.norm,changes:best.changes,affected:best.affected};
  passes.push(report);states=best.states;currentNorm=best.norm;
  for(const row of best.rows){residuals[row.index]=Float64Array.from(row.residual);norms[row.index]=row.norm;}
  console.log(JSON.stringify({event:'selected_candidate_pass',pass,before:report.before_norm,
    after:currentNorm,peak,alpha:best.alpha,beta:best.beta,changes:best.changes}));
}
if(!zeroBoundary(states)||!same(Array.from(states[0]),cp.states[0])||!same(Array.from(states[N]),cp.states[N]))
  throw Error('A candidate changed an original boundary state');
const whole=dn.tail.evaluate(states,target,true,scales);
if(whole.norm!==currentNorm)throw Error('Local dependency cache differs from the complete original replay');
const improved=Number.isFinite(whole.norm)&&whole.norm<original.norm;
const candidate={scope:'UNACCEPTED initial shooting state only; an unchanged original worker must solve it.',
  solver_success:false,candidate_only:true,strict_full_replay_improvement:improved,
  request:record.request,config:cfg,source_sha256:record.source_sha256,
  execution_source_sha256:sources,input_failure_sha256:sha(input),
  checkpoint:{parameters:cp.parameters,states:states.map(v=>Array.from(v)),rawNode:cp.rawNode,
    rawStates:cp.rawNode.map(n=>Array.from(states[n])),cutHeight:cp.cutHeight,
    scope:'Unaccepted free-internal-state initializer; physical target and both boundary states unchanged.'}};
fs.writeFileSync(output,gzipSync(JSON.stringify(candidate)+'\n'),{flag:'wx'});
const summary={scope:'New internal initializer and exact original full-Jacobian replay only. dn.solve was never called.',
  command:process.argv,input:{path:input,sha256:sha(input)},
  locator:locatorArg?{path:path.resolve(locatorArg),sha256:sha(locatorArg)}:null,
  source_sha256:sources,original_gate:cfg.solveTolerance,alphas,betas,maxPasses,passes,stopped,
  before:{norm:original.norm,minA:original.minA,minD:original.minD,boundary_norm:boundaryNorm(clone(cp.states))},
  full_candidate_replay:{norm:whole.norm,minA:whole.minA,minD:whole.minD,
    matches_local_predicted_norm:true,boundary_norm:boundaryNorm(states)},
  strict_full_replay_improvement:improved,zero_original_worker_boundary_correction:true,
  first_height_ratio_on_reload:cp.cutHeight[0]/cp.cutHeight[0],
  original_solver_invoked:false,solver_success:false,
  candidate:{path:output,sha256:sha(output)},seconds:(performance.now()-began)/1000};
fs.writeFileSync(summaryPath,JSON.stringify(summary,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({event:'candidate_only_terminal',improved,
  original_norm:original.norm,candidate_norm:whole.norm,solver_invoked:false,
  candidate_sha256:summary.candidate.sha256,seconds:summary.seconds}));
