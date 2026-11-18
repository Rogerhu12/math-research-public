// One deterministic unaccepted initializer for the saved complete over-gate set.
// Visit the union of changed and upstream rows in decreasing stage order.
// In each named row set only its originally over-gate components to that row's
// current original full-Jac flow. Later smaller-node updates cannot change it.
// Reuse a saved flow only when its whole input state is bit-identical; otherwise
// evaluate that original row once. Preserve H, all boundary data and other state
// components. A finite improved locality bound is only an initial-guess filter;
// the unchanged original full DN/Jacobian/audit must decide acceptance.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const [topic,input,rowsFile,candidateFile,output]=process.argv.slice(2);
if(!output||fs.existsSync(candidateFile)||fs.existsSync(output))throw Error('Use fresh candidate and summary files');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const original=JSON.parse(gunzipSync(fs.readFileSync(input))),saved=JSON.parse(fs.readFileSync(rowsFile));
const cfg=original.config,old=original.response.checkpoint;
if(!original.response.failed||saved.input.sha256!==sha(input)||saved.statesChanged!==false||
 saved.original_solver_invoked!==false||!Object.is(saved.before.norm,original.response.lastIteration.norm)||
 !(saved.otherComponentMaximum<cfg.solveTolerance)||!saved.completeOverGateComponents.length)
 throw Error('Need the one complete original failed-state replay');
const sources={...saved.source_sha256,[path.resolve(process.argv[1])]:sha(process.argv[1])};
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Source changed: '+file);
const cp=structuredClone(old),M=cfg.modes,K=2*M,N=old.states.length-1;
const selected=new Map(),seen=new Set();
for(const r of saved.completeOverGateComponents){
 const n=r.stage,j=r.component,key=n+':'+j;
 if(!Number.isInteger(n)||!(n>0&&n<N)||!Number.isInteger(j)||!(j>=0&&j<K)||seen.has(key)||
  !(r.normalizedResidual>=cfg.solveTolerance)||!Object.is(old.states[n][j],r.state)||
  !Number.isFinite(r.flow)||!Number.isFinite(r.state))
  throw Error('Require the complete actual over-gate internal component set');
 seen.add(key);if(!selected.has(n))selected.set(n,[]);selected.get(n).push(r);
}
const source=path.join(topic,'repro/source-root');process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
if(dn.tail.cells.length!==N)throw Error('The original stage grid changed');
const impacted=[...new Set([...selected.keys()].flatMap(n=>[n-1,n]))].sort((a,b)=>b-a);
const after=[],changes=[];let freshFlows=0,reusedFlows=0;
for(const n of impacted){
 const before=saved.fullAffectedAndUpstreamRows.find(r=>r.stage===n);
 if(!before||before.components.length!==K||before.components.some((r,j)=>r.component!==j||
  !Object.is(r.state,old.states[n][j])||!Object.is(r.normalizationScale,before.components[0].normalizationScale)))
  throw Error('The complete prior impacted row/scale is missing');
 const sameInput=cp.states[n+1].every((v,j)=>Object.is(v,old.states[n+1][j]));
 let flow,minA,minD;
 if(sameInput){
  flow=before.components.map(r=>r.flow);minA=before.minA;minD=before.minD;reusedFlows++;
 }else{
  const cell=dn.tail.cells[n],state=new Float64Array(K+2);state.set(cp.states[n+1]);
  const f=cell.engine.flowStateWithJacobian(state,cell.profiles,{stepsPerSegment:cfg.steps});
  flow=Array.from(f.state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio);
  minA=f.minA;minD=f.minD;freshFlows++;
 }
 if(flow.length!==K||flow.some(v=>!Number.isFinite(v)))throw Error('A current original flow is not finite');
 for(const r of selected.get(n)||[]){
  const value=flow[r.component];cp.states[n][r.component]=value;
  changes.push({node:n,component:r.component,before:r.state,after:value,signedStep:value-r.state,
   originalFlow:r.flow,currentFlow:value,remainingToCurrentFlow:0,
   currentFlowInputWasOriginal:sameInput});
 }
 const residual=flow.map((v,j)=>v-cp.states[n][j]);
 const norm=Math.max(...residual.map(v=>Math.abs(v)/before.components[0].normalizationScale));
 after.push({stage:n,norm,flow,residual,normalizationScale:before.components[0].normalizationScale,
  minA,minD,originalSavedFlowReused:sameInput,inputNode:n+1});
 console.log(JSON.stringify({event:'reverse_selected_flow_row_completed',stage:n,
  selectedComponents:(selected.get(n)||[]).map(r=>r.component),norm,minA,minD,originalSavedFlowReused:sameInput}));
}
changes.sort((a,b)=>a.node-b.node||a.component-b.component);
const actualChanges=[];
for(let n=0;n<=N;n++)for(let j=0;j<K;j++)if(!Object.is(old.states[n][j],cp.states[n][j]))actualChanges.push(n+':'+j);
const expectedChanges=changes.filter(r=>!Object.is(r.before,r.after)).map(r=>r.node+':'+r.component);
if(JSON.stringify(actualChanges)!==JSON.stringify(expectedChanges)||actualChanges.some(key=>!seen.has(key)))
 throw Error('An undeclared state changed');
cp.rawStates=cp.rawNode.map(n=>cp.states[n].slice());
cp.scope='UNACCEPTED one reverse selected-flow initializer. Only the saved complete over-gate coordinates may change; no repeated pass or full-state acceptance is asserted.';
const upper=Math.max(saved.otherComponentMaximum,saved.before.boundary.cut,saved.before.boundary.deep,...after.map(r=>r.norm));
const viable=Number.isFinite(upper)&&upper<saved.before.norm;
const method='one_reverse_selected_flow_pass_v1';
const candidate={candidate_only:true,solver_success:false,scope:cp.scope,method,
 input_failure:{path:path.resolve(input),sha256:sha(input)},complete_rows:{path:path.resolve(rowsFile),sha256:sha(rowsFile)},
 request:structuredClone(original.request),config:structuredClone(cfg),source_sha256:structuredClone(original.source_sha256),
 checkpoint:cp,named_changes:changes,actual_changed_coordinates:actualChanges,locality_bound_viable:viable};
fs.writeFileSync(candidateFile,gzipSync(JSON.stringify(candidate)+'\n'),{flag:'wx'});
const result={scope:'One reverse selected-flow pass only. Full affected/upstream rows are exact for the final candidate because stage n reads only state[n+1]. Saved flows are reused only for bit-identical whole inputs; other affected flows are evaluated once with the original full-Jac arithmetic and port conversion. The unchanged complete replay bounds the other components and both boundaries. This is a candidate locality upper bound, not a new whole-state replay or accepted response.',
 method,command:process.argv,input:{path:path.resolve(input),sha256:sha(input)},complete_rows:{path:path.resolve(rowsFile),sha256:sha(rowsFile)},
 candidate:{path:path.resolve(candidateFile),sha256:sha(candidateFile)},source_sha256:sources,
 originalGate:cfg.solveTolerance,before:saved.before,named_changes:changes,actual_changed_coordinates:actualChanges,
 changed_scalars:actualChanges.length,declared_components:seen.size,descending_stage_order:impacted,
 afterImpactedRows:after,unchangedComponentBound:saved.otherComponentMaximum,candidateNormUpperBound:upper,
 locality_bound_viable:viable,locality_bound_below_original_gate:upper<cfg.solveTolerance,
 fresh_original_flows:freshFlows,reused_original_flows:reusedFlows,
 full_candidate_replay_invoked:false,original_solver_invoked:false,original_full_native_acceptance_required:true,
 original_final_gate_unchanged:true,passes:1};
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Executed source changed: '+file);
fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({output,sha256:sha(output),changes,candidateNormUpperBound:upper,viable,
 locality_bound_below_original_gate:upper<cfg.solveTolerance,freshFlows,reusedFlows,original_solver_invoked:false}));
