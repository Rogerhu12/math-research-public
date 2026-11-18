// One deterministic candidate: move every saved over-gate internal component
// one float neighbor toward its original full-Jac flow, once and together.
// The remaining old-flow discrepancy need not be zero; fresh complete rows
// and the unchanged original native stopping gate decide viability/acceptance.
// Recompute only the complete changed/upstream rows. All other components and
// both boundary rows retain the saved original bound. The original native DN
// must still perform its own full stopping test/Jacobian/audit.
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
const view=new DataView(new ArrayBuffer(8));
function neighbor(v,direction){
 if(v===0)return direction*Number.MIN_VALUE;
 view.setFloat64(0,v,false);const bits=view.getBigUint64(0,false);
 view.setBigUint64(0,(v>0)===(direction>0)?bits+1n:bits-1n,false);return view.getFloat64(0,false);
}
const changes=[],seen=new Set();
for(const r of saved.completeOverGateComponents){
 const n=r.stage,j=r.component,key=n+':'+j;
 if(!Number.isInteger(n)||!(n>0&&n<N)||!Number.isInteger(j)||!(j>=0&&j<K)||seen.has(key)||
  !(r.normalizedResidual>=cfg.solveTolerance)||![-1,1].includes(r.direction)||
  !Object.is(old.states[n][j],r.state)||!Object.is(neighbor(r.state,r.direction),r.adjacentTowardFlow)||
  !(Math.abs(r.flow-r.adjacentTowardFlow)<Math.abs(r.flow-r.state)))
  throw Error('Each complete over-gate member must take one original directed internal neighbor toward its saved flow');
 seen.add(key);cp.states[n][j]=r.adjacentTowardFlow;
 changes.push({node:n,component:j,before:r.state,after:r.adjacentTowardFlow,direction:r.direction,
  signedStep:r.adjacentTowardFlow-r.state,originalFlow:r.flow,remainingToOriginalFlow:r.flow-r.adjacentTowardFlow});
}
const actualChanges=[];
for(let n=0;n<=N;n++)for(let j=0;j<K;j++)if(!Object.is(old.states[n][j],cp.states[n][j]))actualChanges.push(n+':'+j);
if(actualChanges.length!==seen.size||actualChanges.some(key=>!seen.has(key)))throw Error('An undeclared state changed');
cp.rawStates=cp.rawNode.map(n=>cp.states[n].slice());
cp.scope='UNACCEPTED one-directed-neighbor-per-over-gate-component initializer. One simultaneous step only; original native solver decides full acceptance.';
const source=path.join(topic,'repro/source-root');process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
if(dn.tail.cells.length!==N)throw Error('The original stage grid changed');
const impacted=[...new Set(changes.flatMap(r=>[r.node-1,r.node]))].sort((a,b)=>a-b);
const after=[];
for(const n of impacted){
 const before=saved.fullAffectedAndUpstreamRows.find(r=>r.stage===n);
 if(!before||before.components.length!==K)throw Error('The complete prior impacted row is missing');
 const cell=dn.tail.cells[n],state=new Float64Array(K+2);state.set(cp.states[n+1]);
 const f=cell.engine.flowStateWithJacobian(state,cell.profiles,{stepsPerSegment:cfg.steps});
 const flow=Array.from(f.state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio);
 const residual=flow.map((v,j)=>v-cp.states[n][j]);
 const norm=Math.max(...residual.map(v=>Math.abs(v)/before.components[0].normalizationScale));
 after.push({stage:n,norm,flow,residual,normalizationScale:before.components[0].normalizationScale,minA:f.minA,minD:f.minD});
}
const upper=Math.max(saved.otherComponentMaximum,saved.before.boundary.cut,saved.before.boundary.deep,...after.map(r=>r.norm));
const viable=Number.isFinite(upper)&&upper<cfg.solveTolerance&&upper<saved.before.norm;
const candidate={candidate_only:true,solver_success:false,scope:cp.scope,
 input_failure:{path:path.resolve(input),sha256:sha(input)},complete_rows:{path:path.resolve(rowsFile),sha256:sha(rowsFile)},
 request:structuredClone(original.request),config:structuredClone(cfg),source_sha256:structuredClone(original.source_sha256),
 checkpoint:cp,named_changes:changes,locality_bound_viable:viable};
fs.writeFileSync(candidateFile,gzipSync(JSON.stringify(candidate)+'\n'),{flag:'wx'});
const result={scope:'One candidate only. Fresh original full-Jac flows cover the union of changed and upstream rows. The saved complete replay bounds every unchanged row/component; the combined quantity is an upper bound, not a newly executed whole-state norm. Original native full solve still required.',
 command:process.argv,input:{path:path.resolve(input),sha256:sha(input)},complete_rows:{path:path.resolve(rowsFile),sha256:sha(rowsFile)},
 candidate:{path:path.resolve(candidateFile),sha256:sha(candidateFile)},source_sha256:sources,
 originalGate:cfg.solveTolerance,before:saved.before,named_changes:changes,changed_scalars:changes.length,
 afterImpactedRows:after,unchangedComponentBound:saved.otherComponentMaximum,candidateNormUpperBound:upper,
 locality_bound_viable:viable,full_candidate_replay_invoked:false,original_solver_invoked:false,
 locality_reason:'Stage n reads only states[n+1] and subtracts states[n]. H/config/scales and node0/deep states are unchanged.'};
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Executed source changed: '+file);
fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({output,sha256:sha(output),changes,candidateNormUpperBound:upper,viable,original_solver_invoked:false}));
