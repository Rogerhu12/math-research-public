// One fixed candidate from the complete original stage-86 residual row:
// c8 takes its positive neighbor; c11 takes its negative neighbor.
// Reuse the saved complete before rows. No scalar/ratio search or DN solve.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const args=process.argv.slice(2);
if(args.length!==6)throw Error('Need topic, failure, completed baseline, complete-row inspection, candidate, summary');
const [topic,input,baseline,localFile,output,summaryFile]=args.map(p=>path.resolve(p));
if(fs.existsSync(output)||fs.existsSync(summaryFile))throw Error('Use fresh outputs');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const same=(a,b)=>typeof a===typeof b&&(typeof a==='number'?Object.is(a,b):
 a===null||b===null||typeof a!=='object'?a===b:
 Object.keys(a).length===Object.keys(b).length&&Object.keys(a).every(k=>Object.hasOwn(b,k)&&same(a[k],b[k])));
const required={input:'6f0cdfa7bdc27c330bd3320ba94417e1fb410430dfdcdd3bd685c2944d2411ac',
 baseline:'f983a5d142e6f0c2c1b8d6578ae1cd1fe4113ef320c65ab881a40e4540a1a0d1',
 local:'d6df8637ab753342eb822aa6f6a945bdbfe244b8412bccffd226835e6197dbad'};
if(sha(input)!==required.input||sha(baseline)!==required.baseline||sha(localFile)!==required.local)
 throw Error('Only this original partial-path failure and completed inspections are eligible');
const record=JSON.parse(gunzipSync(fs.readFileSync(input))),b=JSON.parse(fs.readFileSync(baseline));
const inspected=JSON.parse(fs.readFileSync(localFile)),cfg=record.config,cp=record.response?.checkpoint;
const node=86,components=[8,11],directions=[1,-1];
if(!record.response?.failed||!cp?.states||b.input.sha256!==required.input||
 b.original_solver_invoked!==false||b.strict_full_replay_improvement!==false||
 !Object.is(b.before.norm,record.response.lastIteration.norm)||
 !Object.is(b.full_candidate_replay.norm,b.before.norm)||
 inspected.input.sha256!==required.input||inspected.baseline.sha256!==required.baseline||
 inspected.statesChanged!==false||inspected.originalSolverInvoked!==false||
 inspected.row!==node||!same(inspected.components,Array.from({length:16},(_,i)=>i))||
 !same(inspected.rows.map(r=>r.stage),[85,86]))throw Error('The complete original-row evidence changed');
if(cfg.modes!==8||cfg.shootingParts!==16||cfg.steps!==16||cfg.spacing!==3||
 cfg.solveTolerance!==2e-9||cfg.sharedEngines||!same(record.request.height,cp.cutHeight))
 throw Error('Original M8/parts16/RK16/nonshared/full-H/2e-9 identity required');
const originalRows=inspected.rows;
if(originalRows.some(r=>r.named.length!==16)||!Object.is(originalRows[1].norm,b.before.norm)||
 !same(originalRows[1].named.filter(p=>p.normalizedResidual>=cfg.solveTolerance).map(p=>p.component),components)||
 originalRows[0].named.some(p=>p.normalizedResidual>=cfg.solveTolerance))
 throw Error('The complete over-gate set must be exactly the predeclared two coordinates');
const sources={...b.source_sha256,...inspected.source_sha256};
for(const [name,digest] of Object.entries(record.source_sha256))sources[path.resolve(topic,'scripts',name)]=digest;
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Source changed: '+file);
sources[path.resolve(process.argv[1])]=sha(process.argv[1]);
const root=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=root;
process.env.CLOSING_TAIL_CACHE=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,N=dn.tail.cells.length;
if(N!==1152||cp.states.length!==N+1||cp.states.some(r=>r.length!==K||
 r.some(v=>!Number.isFinite(v)||Object.is(v,-0)))||!same(cp.rawNode,dn.tail.rawNode))
 throw Error('The complete original finite grid and states are required');
const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
const target=Float64Array.from(cp.cutHeight,v=>v/radius**4);
if(cp.cutHeight[0]===0||!Array.from(target).every((v,j)=>Object.is(v-cp.states[0][j],0)))
 throw Error('The same-H worker reload must have ratio one and zero boundary correction');
const scales=new Float64Array(N+1);scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
for(let i=0;i<N;i++)scales[i+1]=scales[i]/Math.abs(dn.tail.gains[i][0]);
for(const row of originalRows){
 if(!Object.is(row.normalizationScale,scales[row.stage]))throw Error('Original residual scale changed');
 for(const p of row.named){
  if(!Object.is(p.state,cp.states[row.stage][p.component])||
   !Object.is(p.flow-p.state,p.signedResidual)||
   !Object.is(Math.abs(p.signedResidual)/scales[row.stage],p.normalizedResidual))
   throw Error('Saved complete original row differs from the exact finite state');
 }
}
const states=cp.states.map(r=>Float64Array.from(r)),view=new DataView(new ArrayBuffer(8));
function neighbor(v,d){
 if(v===0)return d*Number.MIN_VALUE;
 view.setFloat64(0,v,false);const bits=view.getBigUint64(0,false);
 view.setBigUint64(0,(v>0)===(d>0)?bits+1n:bits-1n,false);return view.getFloat64(0,false);
}
const changes=components.map((j,k)=>{
 const evidence=originalRows[1].named[j],before=states[node][j],direction=directions[k],after=neighbor(before,direction);
 if(evidence.component!==j||evidence.direction!==direction||!evidence.isExactlyOneDirectedNeighbor||
  !Object.is(after,evidence.flow)||!Object.is(after-before,evidence.signedResidual))
  throw Error('Only the two evidence-bound one-neighbor directions are eligible');
 return {node,component:j,before,after,direction,signed_step:after-before};
});
for(const change of changes)states[node][change.component]=change.after;
const found=[];
for(let i=0;i<=N;i++)for(let j=0;j<K;j++)if(!Object.is(states[i][j],cp.states[i][j]))found.push([i,j]);
if(!same(found,[[86,8],[86,11]]))throw Error('Exactly the two free internal values must change');
function local(index){
 const cell=dn.tail.cells[index],x=new Float64Array(K+2);x.set(states[index+1]);
 const f=cell.engine.flowStateWithJacobian(x,cell.profiles,{stepsPerSegment:cfg.steps});
 const flow=Array.from(f.state.slice(0,K),(v,j)=>v/(j<M?1:cell.portRatio));
 const residual=flow.map((v,j)=>v-states[index][j]);
 const norm=Math.max(...residual.map(v=>Math.abs(v)/scales[index]));
 if(!Number.isFinite(norm))throw Error('Nonfinite original local flow');
 return {stage:index,norm,minA:f.minA,minD:f.minD,normalizationScale:scales[index],
  complete_state:Array.from(states[index]),complete_flow:flow,complete_residual:residual};
}
const began=performance.now(),candidateRows=[local(85),local(86)];
let boundaryNorm=0;
for(let j=0;j<M;j++){
 boundaryNorm=Math.max(boundaryNorm,Math.abs(states[0][j]-target[j])/scales[0]);
 boundaryNorm=Math.max(boundaryNorm,Math.abs(states[N][M+j]-dn.tail.graphs[N][j]*states[N][j])/scales[N]);
}
if(!Object.is(boundaryNorm,b.full_candidate_replay.boundary_norm))throw Error('Boundary residual changed');
const untouched=b.largest_untouched_row;
if([85,86].includes(untouched.stage))throw Error('The recorded untouched maximum is affected');
const predicted=Math.max(untouched.norm,boundaryNorm,...candidateRows.map(r=>r.norm));
const whole=dn.tail.evaluate(states,target,true,scales);
if(!Object.is(whole.norm,predicted))throw Error('Full original replay differs from the exact two-row dependency');
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Executed source changed: '+file);
const improved=Number.isFinite(whole.norm)&&whole.norm<b.before.norm;
const candidate={scope:'UNACCEPTED initializer: c8 positive neighbor and c11 negative neighbor at node86; only the original worker may accept it.',
 solver_success:false,candidate_only:true,strict_full_replay_improvement:improved,named_changes:changes,
 request:record.request,config:cfg,source_sha256:record.source_sha256,execution_source_sha256:sources,
 input_failure_sha256:sha(input),checkpoint:{parameters:cp.parameters,states:states.map(r=>Array.from(r)),
  rawNode:cp.rawNode,rawStates:cp.rawNode.map(i=>Array.from(states[i])),cutHeight:cp.cutHeight,
  scope:'Both complete boundary states and physical H unchanged; no original solve yet.'}};
fs.writeFileSync(output,gzipSync(JSON.stringify(candidate)+'\n'),{flag:'wx'});
const summary={scope:'One complete-row-defined pair, existing original before rows reused, original after local Jacobians and full residual replay; no solve.',
 command:process.argv,input:{path:input,sha256:sha(input)},baseline:{path:baseline,sha256:sha(baseline)},
 local_inspection:{path:localFile,sha256:sha(localFile)},source_sha256:sources,
 original_gate:cfg.solveTolerance,named_changes:changes,changed_scalars:2,
 original_local_rows_reused:true,original_local_rows:originalRows,candidate_local_rows:candidateRows,
 largest_untouched_row:untouched,before:{norm:b.before.norm},
 full_candidate_replay:{norm:whole.norm,minA:whole.minA,minD:whole.minD,
  matches_two_row_prediction:true,boundary_norm:boundaryNorm},strict_full_replay_improvement:improved,
 candidate_below_original_gate:whole.norm<cfg.solveTolerance,first_height_ratio_on_reload:1,
 zero_original_worker_boundary_correction:true,original_solver_invoked:false,solver_success:false,
 candidate:{path:output,sha256:sha(output)},seconds:(performance.now()-began)/1000};
fs.writeFileSync(summaryFile,JSON.stringify(summary,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({event:'fixed_complete_peak_pair_candidate',improved,before:b.before.norm,
 after:whole.norm,below_original_gate:whole.norm<cfg.solveTolerance,changed_scalars:2,
 candidate_sha256:summary.candidate.sha256,solver_invoked:false,seconds:summary.seconds}));
