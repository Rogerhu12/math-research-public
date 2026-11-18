// One predeclared positive binary64 neighbor, never a search or DN solve.
// The original full-Jacobian flow evaluates both affected rows and the full
// candidate.  Only an unchanged original worker may subsequently accept it.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const [topicArg,inputArg,locatorArg,nodeArg,componentArg,outputArg,summaryArg]=process.argv.slice(2);
if(!summaryArg)throw Error('Need topic, failed record, locator, node, component, candidate, summary');
const topic=path.resolve(topicArg),input=path.resolve(inputArg),locator=path.resolve(locatorArg);
const output=path.resolve(outputArg),summaryPath=path.resolve(summaryArg);
if(fs.existsSync(output)||fs.existsSync(summaryPath))throw Error('Outputs must be new');
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const same=(a,b)=>typeof a===typeof b&&(typeof a==='number'?Object.is(a,b):
 a===null||b===null||typeof a!=='object'?a===b:
 Object.keys(a).length===Object.keys(b).length&&Object.keys(a).every(k=>Object.hasOwn(b,k)&&same(a[k],b[k])));
const record=JSON.parse(gunzipSync(fs.readFileSync(input)));
const located=JSON.parse(fs.readFileSync(locator)),cp=record.response?.checkpoint,cfg=record.config;
if(!record.response?.failed||!record.response.lastIteration||!cp?.states||located.inputAccepted||
 located.input_sha256!==sha(input)||located.replayNormalizedResidual!==record.response.lastIteration.norm)
 throw Error('The exact original failed state and completed full locator are required');
if(cfg.sharedEngines||cfg.spacing!==3||cfg.solveTolerance!==2e-9||located.originalGate!==cfg.solveTolerance)
 throw Error('Original nonshared m3 worker and its original gate required');
if(!same(record.request.height,cp.cutHeight))throw Error('Complete physical height changed');
const n=Number(nodeArg),j=Number(componentArg),peak=located.largestResidual[0];
if(!Number.isInteger(n)||!Number.isInteger(j)||peak.stage!==n||peak.component!==j||
 peak.residualInComponentUlps!==1||!(peak.signedResidual>0))
 throw Error('Only the predeclared positive one-ULP peak is eligible');
const sources={...located.source_sha256};
for(const [name,digest] of Object.entries(record.source_sha256))
 sources[path.resolve(topic,'scripts',name)]=digest;
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
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const M=cfg.modes,K=2*M,N=dn.tail.cells.length;
if(!(n>0&&n<N&&j>=0&&j<K)||cp.states.length!==N+1||
 cp.states.some(row=>row.length!==K||row.some(v=>!Number.isFinite(v)||Object.is(v,-0)))||
 !same(cp.rawNode,dn.tail.rawNode))throw Error('Complete finite same-grid state required');
const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
const target=Float64Array.from(cp.cutHeight,v=>v/radius**4);
if(cp.cutHeight[0]===0||!Array.from(target).every((v,i)=>Object.is(v-cp.states[0][i],0)))
 throw Error('Original reload must have ratio one and zero boundary correction');
const scales=new Float64Array(N+1);
scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
for(let i=0;i<N;i++)scales[i+1]=scales[i]/Math.abs(dn.tail.gains[i][0]);
const states=cp.states.map(row=>Float64Array.from(row));
const buffer=new ArrayBuffer(8),view=new DataView(buffer);
function nextPositive(v){
 if(v===0)return Number.MIN_VALUE;
 view.setFloat64(0,v,false);const bits=view.getBigUint64(0,false);
 view.setBigUint64(0,v>0?bits+1n:bits-1n,false);return view.getFloat64(0,false);
}
const before=states[n][j],after=nextPositive(before),ulp=after-before;
if(!Object.is(before,peak.stateValue)||!Object.is(after,peak.flowValue)||!Object.is(ulp,peak.signedResidual))
 throw Error('The prescribed neighbor is not exactly the recorded original flow value');
function local(index,values){
 const cell=dn.tail.cells[index],x=new Float64Array(K+2);x.set(values[index+1]);
 const f=cell.engine.flowStateWithJacobian(x,cell.profiles,{stepsPerSegment:cfg.steps});
 const out=Float64Array.from(f.state.slice(0,K),(v,i)=>v/(i<M?1:cell.portRatio));
 const residual=Float64Array.from(out,(v,i)=>v-values[index][i]);
 let norm=0,component=-1,columnMax=0;
 for(let i=0;i<K;i++){
  const value=Math.abs(residual[i])/scales[index];if(value>norm){norm=value;component=i;}
  columnMax=Math.max(columnMax,Math.abs(f.tangent[i*K+j]/(i<M?1:cell.portRatio)));
 }
 if(!Number.isFinite(norm)||!Number.isFinite(columnMax))throw Error('Nonfinite local flow');
 return {stage:index,norm,component,selectedResidual:residual[j],selectedFlow:out[j],
  inputColumnMax:columnMax,minA:f.minA,minD:f.minD};
}
const began=performance.now();
const originalRows=[local(n-1,states),local(n,states)];
if(!Object.is(originalRows[1].norm,peak.normalizedResidual)||
 !Object.is(originalRows[1].selectedFlow,peak.flowValue))throw Error('Original local replay changed');
states[n][j]=after;
const candidateRows=[local(n-1,states),local(n,states)];
let changes=0;
for(let i=0;i<=N;i++)for(let k=0;k<K;k++)if(!Object.is(states[i][k],cp.states[i][k])){
 if(i!==n||k!==j)throw Error('Another state changed');changes++;
}
if(changes!==1)throw Error('Exactly one named state must change');
const untouched=located.largestResidual.find(row=>row.stage!==n-1&&row.stage!==n);
if(!untouched)throw Error('Locator does not expose the largest untouched row');
let boundaryNorm=0;
for(let k=0;k<M;k++){
 boundaryNorm=Math.max(boundaryNorm,Math.abs(states[0][k]-target[k])/scales[0]);
 boundaryNorm=Math.max(boundaryNorm,Math.abs(states[N][M+k]-dn.tail.graphs[N][k]*states[N][k])/scales[N]);
}
const predicted=Math.max(untouched.normalizedResidual,boundaryNorm,...candidateRows.map(row=>row.norm));
const whole=dn.tail.evaluate(states,target,true,scales);
if(!Object.is(whole.norm,predicted))throw Error('Full original replay disagrees with the two-row dependency');
for(const [file,digest] of Object.entries(sources))if(sha(file)!==digest)throw Error('Executed source changed: '+file);
const improved=Number.isFinite(whole.norm)&&whole.norm<located.replayNormalizedResidual;
const candidate={scope:'UNACCEPTED initial state; one named positive neighbor only. Original worker acceptance is still required.',
 solver_success:false,candidate_only:true,strict_full_replay_improvement:improved,
 request:record.request,config:cfg,source_sha256:record.source_sha256,
 execution_source_sha256:sources,input_failure_sha256:sha(input),
 checkpoint:{parameters:cp.parameters,states:states.map(row=>Array.from(row)),rawNode:cp.rawNode,
  rawStates:cp.rawNode.map(i=>Array.from(states[i])),cutHeight:cp.cutHeight,
  scope:'Unaccepted one-neighbor initializer; complete physical H and both boundary states unchanged.'}};
fs.writeFileSync(output,gzipSync(JSON.stringify(candidate)+'\n'),{flag:'wx'});
const summary={scope:'One predeclared free-state positive neighbor, original local Jacobians and full residual replay; no solver call.',
 command:process.argv,input:{path:input,sha256:sha(input)},locator:{path:locator,sha256:sha(locator)},
 source_sha256:sources,original_gate:cfg.solveTolerance,
 named_change:{node:n,component:j,before,after,positiveUlp:ulp,changedScalars:changes},
 original_local_rows:originalRows,candidate_local_rows:candidateRows,
 largest_untouched_row:{stage:untouched.stage,component:untouched.component,norm:untouched.normalizedResidual},
 upstream_input_ulp_linearized_scale:originalRows[0].inputColumnMax*ulp/scales[n-1],
 before:{norm:located.replayNormalizedResidual},full_candidate_replay:{norm:whole.norm,
  minA:whole.minA,minD:whole.minD,matches_two_row_prediction:true,boundary_norm:boundaryNorm},
 strict_full_replay_improvement:improved,candidate_below_original_gate:whole.norm<cfg.solveTolerance,
 cut_radius:radius,first_height_ratio_on_reload:1,zero_original_worker_boundary_correction:true,
 same_parts_node_copy_required:true,original_solver_invoked:false,solver_success:false,
 candidate:{path:output,sha256:sha(output)},seconds:(performance.now()-began)/1000};
fs.writeFileSync(summaryPath,JSON.stringify(summary,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({event:'named_neighbor_candidate_only',improved,before:located.replayNormalizedResidual,
 after:whole.norm,below_original_gate:whole.norm<cfg.solveTolerance,changed_scalars:changes,solver_invoked:false,
 candidate_sha256:summary.candidate.sha256,seconds:summary.seconds}));
