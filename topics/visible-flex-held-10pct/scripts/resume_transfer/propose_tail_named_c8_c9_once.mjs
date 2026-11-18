// Exactly one negative binary64 neighbor in each of node 86 components 8/9.
// Component 8 reaches its flow. Component 9 intentionally retains one ULP
// of its original two-ULP residual. No search and no DN solve.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const [topicArg,inputArg,baselineArg,localArg,outputArg,summaryArg]=process.argv.slice(2);
if(!summaryArg)throw Error('Need original topic, failure, completed baseline, local inspection, candidate, summary');
const [topic,input,baseline,localFile,output,summaryFile]=
 [topicArg,inputArg,baselineArg,localArg,outputArg,summaryArg].map(p=>path.resolve(p));
if(fs.existsSync(output)||fs.existsSync(summaryFile))throw Error('Use fresh outputs');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const same=(a,b)=>typeof a===typeof b&&(typeof a==='number'?Object.is(a,b):
 a===null||b===null||typeof a!=='object'?a===b:
 Object.keys(a).length===Object.keys(b).length&&Object.keys(a).every(k=>Object.hasOwn(b,k)&&same(a[k],b[k])));
const required={
 input:'845d89e7695d3bf158db56661632e64e38ade4c0d2ea707c32ed1f959eaef8f3',
 baseline:'274fd0a06bbe44aff8a345bae02e4549f8f8bc7ef6cd8e3d382bac360fd86799',
 local:'9dafa132672d8f9e73307199d17eccf28dbd441182adbfc84ef40e56edabebcd'};
if(sha(input)!==required.input||sha(baseline)!==required.baseline||sha(localFile)!==required.local)
 throw Error('Only the predeclared q060 saved-inner H_new failure and completed inspections are eligible');
const record=JSON.parse(gunzipSync(fs.readFileSync(input))),b=JSON.parse(fs.readFileSync(baseline));
const inspected=JSON.parse(fs.readFileSync(localFile)),cfg=record.config,cp=record.response?.checkpoint;
const node=86,components=[8,9];
if(!record.response?.failed||!cp?.states||!record.response.lastIteration||
 b.input.sha256!==required.input||b.original_solver_invoked!==false||b.strict_full_replay_improvement!==false||
 !Object.is(b.before.norm,record.response.lastIteration.norm)||
 !Object.is(b.full_candidate_replay.norm,b.before.norm)||b.passes.length!==1||b.passes[0].selected!==null||
 inspected.input.sha256!==required.input||inspected.baseline.sha256!==required.baseline||
 inspected.statesChanged!==false||inspected.originalSolverInvoked!==false||
 inspected.row!==node||!same(inspected.components,components))
 throw Error('The unchanged failed-state baseline and local inspection are required');
if(cfg.modes!==8||cfg.shootingParts!==16||cfg.steps!==16||cfg.spacing!==3||
 cfg.solveTolerance!==2e-9||cfg.sharedEngines||!same(record.request.height,cp.cutHeight))
 throw Error('Complete original H and M8/parts16/RK16/nonshared/original-gate identity required');
const witness=b.passes[0].trials.find(t=>t.alpha===0.5&&t.beta===0);
if(!witness||witness.changes.length!==1||witness.changes[0].stage!==node||
 witness.changes[0].component!==8||!same(witness.affected.map(r=>r.stage),[85,86])||
 !Object.is(witness.norm,Math.max(witness.untouched,...witness.affected.map(r=>r.norm)))||
 !Object.is(witness.norm,b.before.norm))throw Error('Recorded untouched maximum lacks the exact two-row dependency');
const sources={...b.source_sha256,...inspected.source_sha256};
for(const [name,digest] of Object.entries(record.source_sha256))sources[path.resolve(topic,'scripts',name)]=digest;
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Source changed: '+file);
sources[path.resolve(process.argv[1])]=sha(process.argv[1]);
const root=path.join(topic,'repro/source-root');
function addRuntime(directory){
 for(const entry of fs.readdirSync(directory,{withFileTypes:true})){
  const file=path.join(directory,entry.name);
  if(entry.isDirectory())addRuntime(file);
  else if(/\.(py|mjs|js)$/.test(entry.name))sources[path.resolve(file)]=sha(file);
 }
}
addRuntime(root);
process.env.VISIBLE_FLEX_SOURCE_ROOT=root;
process.env.CLOSING_TAIL_CACHE=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,N=dn.tail.cells.length;
if(N!==1152||cp.states.length!==N+1||cp.states.some(r=>r.length!==K||
 r.some(v=>!Number.isFinite(v)||Object.is(v,-0)))||!same(cp.rawNode,dn.tail.rawNode))
 throw Error('The complete finite same-grid state is required');
const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
const target=Float64Array.from(cp.cutHeight,v=>v/radius**4);
if(target.length!==M||cp.cutHeight[0]===0||!Array.from(target).every((v,j)=>Object.is(v-cp.states[0][j],0)))
 throw Error('Original reload must have ratio one and zero boundary correction');
const scales=new Float64Array(N+1);scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
for(let i=0;i<N;i++)scales[i+1]=scales[i]/Math.abs(dn.tail.gains[i][0]);
const states=cp.states.map(r=>Float64Array.from(r)),view=new DataView(new ArrayBuffer(8));
function nextNegative(v){
 if(v===0)return -Number.MIN_VALUE;
 view.setFloat64(0,v,false);const bits=view.getBigUint64(0,false);
 view.setBigUint64(0,v>0?bits-1n:bits+1n,false);return view.getFloat64(0,false);
}
function local(index,values){
 const cell=dn.tail.cells[index],x=new Float64Array(K+2);x.set(values[index+1]);
 const f=cell.engine.flowStateWithJacobian(x,cell.profiles,{stepsPerSegment:cfg.steps});
 const out=Float64Array.from(f.state.slice(0,K),(v,j)=>v/(j<M?1:cell.portRatio));
 const residual=Float64Array.from(out,(v,j)=>v-values[index][j]);
 let norm=0,component=-1;
 for(let j=0;j<K;j++){const v=Math.abs(residual[j])/scales[index];if(v>norm){norm=v;component=j;}}
 if(!Number.isFinite(norm))throw Error('Nonfinite original local flow');
 return {stage:index,norm,component,minA:f.minA,minD:f.minD,
  named:components.map(j=>{
   let columnMax=0;
   for(let i=0;i<K;i++)columnMax=Math.max(columnMax,Math.abs(f.tangent[i*K+j]/(i<M?1:cell.portRatio)));
   if(!Number.isFinite(columnMax))throw Error('Nonfinite original local tangent');
   return {component:j,state:values[index][j],flow:out[j],signedResidual:residual[j],
    normalizedResidual:Math.abs(residual[j])/scales[index],inputColumnMax:columnMax};
  })};
}
const began=performance.now(),originalRows=[local(node-1,states),local(node,states)];
for(let i=0;i<2;i++){
 const old=inspected.rows[i],fresh=originalRows[i];
 if(old.stage!==fresh.stage||!Object.is(old.norm,fresh.norm))throw Error('Original local row identity changed');
 for(let k=0;k<2;k++)for(const name of ['component','state','flow','signedResidual','normalizedResidual','inputColumnMax'])
  if(!Object.is(old.named[k][name],fresh.named[k][name]))throw Error('Original named local value changed: '+name);
}
if(!Object.is(originalRows[1].norm,b.before.norm))throw Error('Named row no longer equals the recorded maximum');
const changes=components.map((j,k)=>{
 const p=inspected.rows[1].named[k],before=states[node][j],after=nextNegative(before);
 const distance=k===0?1:2,expectedFlow=k===0?after:nextNegative(after);
 if(p.component!==j||p.direction!==-1||p.isExactlyOneDirectedNeighbor!==(k===0)||
  !Object.is(before,p.state)||!Object.is(after,p.adjacentTowardFlow)||
  !Object.is(expectedFlow,p.flow)||!Object.is(expectedFlow-before,p.signedResidual))
  throw Error('The predeclared one-ULP/two-ULP residual evidence changed');
 const remaining=p.flow-after;
 if(!(Math.abs(remaining)/scales[node]<cfg.solveTolerance))
  throw Error('One step in each named component would not bring both below the original gate');
 return {node,component:j,before,after,direction:-1,signed_step:after-before,
  original_flow:p.flow,original_flow_neighbor_distance:distance,applied_neighbor_steps:1,
  expected_remaining_residual:remaining};
});
if(!Object.is(witness.changes[0].before,changes[0].before)||
 !Object.is(witness.changes[0].after,changes[0].after))throw Error('Untouched witness used another initializer');
for(const change of changes)states[node][change.component]=change.after;
const candidateRows=[local(node-1,states),local(node,states)];
for(let k=0;k<2;k++)if(!Object.is(candidateRows[1].named[k].signedResidual,changes[k].expected_remaining_residual))
 throw Error('The actual affected row differs from the prescribed remaining residual');
const found=[];
for(let i=0;i<=N;i++)for(let j=0;j<K;j++)if(!Object.is(states[i][j],cp.states[i][j]))found.push([i,j]);
if(!same(found,[[86,8],[86,9]]))throw Error('Exactly the two predeclared scalar changes are required');
let boundaryNorm=0;
for(let j=0;j<M;j++){
 boundaryNorm=Math.max(boundaryNorm,Math.abs(states[0][j]-target[j])/scales[0]);
 boundaryNorm=Math.max(boundaryNorm,Math.abs(states[N][M+j]-dn.tail.graphs[N][j]*states[N][j])/scales[N]);
}
if(!Object.is(boundaryNorm,b.before.boundary_norm))throw Error('A boundary residual changed');
const predicted=Math.max(witness.untouched,boundaryNorm,...candidateRows.map(r=>r.norm));
const whole=dn.tail.evaluate(states,target,true,scales);
if(!Object.is(whole.norm,predicted))throw Error('Complete original replay differs from the exact two-row dependency');
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Execution source changed: '+file);
const improved=Number.isFinite(whole.norm)&&whole.norm<b.before.norm;
const candidate={scope:'UNACCEPTED initializer: exactly one negative nextafter at node86/c8 and node86/c9; c9 retains one ULP before its original flow. Original worker acceptance is required.',
 solver_success:false,candidate_only:true,strict_full_replay_improvement:improved,named_changes:changes,
 request:record.request,config:cfg,source_sha256:record.source_sha256,execution_source_sha256:sources,
 input_failure_sha256:sha(input),
 checkpoint:{parameters:cp.parameters,states:states.map(r=>Array.from(r)),rawNode:cp.rawNode,
  rawStates:cp.rawNode.map(i=>Array.from(states[i])),cutHeight:cp.cutHeight,
  scope:'Unaccepted two-named-neighbor initializer; complete physical H, grid and both boundary states unchanged.'}};
fs.writeFileSync(output,gzipSync(JSON.stringify(candidate)+'\n'),{flag:'wx'});
const summary={scope:'One predeclared pair of negative neighbors, original local full Jacobians and complete residual replay. No dn.solve call.',
 command:process.argv,input:{path:input,sha256:sha(input)},baseline:{path:baseline,sha256:sha(baseline)},
 local_inspection:{path:localFile,sha256:sha(localFile)},source_sha256:sources,
 original_gate:cfg.solveTolerance,named_changes:changes,changed_scalars:found.length,
 original_local_rows:originalRows,candidate_local_rows:candidateRows,
 untouched_bound_from_completed_baseline:{pass:0,alpha:0.5,beta:0,affected_rows:[85,86],norm:witness.untouched},
 before:{norm:b.before.norm},full_candidate_replay:{norm:whole.norm,minA:whole.minA,minD:whole.minD,
  matches_two_row_prediction:true,boundary_norm:boundaryNorm},
 strict_full_replay_improvement:improved,candidate_below_original_gate:whole.norm<cfg.solveTolerance,
 cut_radius:radius,first_height_ratio_on_reload:1,zero_original_worker_boundary_correction:true,
 same_parts_node_copy_required:true,original_solver_invoked:false,solver_success:false,
 candidate:{path:output,sha256:sha(output)},seconds:(performance.now()-began)/1000};
fs.writeFileSync(summaryFile,JSON.stringify(summary,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({event:'named_c8_c9_one_step_candidate_only',improved,before:b.before.norm,
 after:whole.norm,below_original_gate:whole.norm<cfg.solveTolerance,changed_scalars:found.length,
 candidate_sha256:summary.candidate.sha256,solver_invoked:false,seconds:summary.seconds}));
