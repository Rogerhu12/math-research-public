// Change one internal floating-point initial value, then use the original DN
// solve and full audit. No residual, root equation, or acceptance gate changes.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,input,diagnostic,outputRecord,outputSummary,sparseHelper] = process.argv.slice(2);
if(!sparseHelper || !fs.existsSync(sparseHelper))throw Error('The original sparse linear helper is required');
process.env.VISIBLE_FLEX_SPARSE_LINEAR_HELPER=path.resolve(sparseHelper);
for(const key of ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'])process.env[key]='1';
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const record=JSON.parse(gunzipSync(fs.readFileSync(input))),diag=JSON.parse(fs.readFileSync(diagnostic));
if(sha(input)!==diag.input_sha256)throw Error('Diagnostic input hash differs');
const source=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
for(const name of ['950f-tail-stage-core.mjs','950f-tail-stage-split.mjs','950f-tail-subdivision.mjs','closing_weighted_tail.mjs']){
 const file=path.join(topic,'scripts',name);
 if(sha(file)!==diag.source_sha256[file])throw Error('Original replay source differs: '+name);
}
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const cfg=record.config,cp=record.response.checkpoint,physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical}),M=cfg.modes,K=2*M;
const states=cp.states.map(v=>Float64Array.from(v)),peak=diag.largestResidual[0];
if(!(peak.stage>0 && peak.stage<dn.tail.cells.length && peak.residualInComponentUlps===1))throw Error('One interior ULP must be the diagnosed candidate');
if(states[peak.stage][peak.component]!==peak.stateValue)throw Error('Recorded candidate value differs');
const radius=dn.tail.cells[0].profiles.at(-1)(1).r,target=Float64Array.from(cp.cutHeight,v=>v/radius**4);
const scales=new Float64Array(states.length);scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
function stage(n,values){
 const cell=dn.tail.cells[n],s=new Float64Array(K+2);s.set(values[n+1]);
 const flow=cell.engine.flowStateWithJacobian(s,cell.profiles,{stepsPerSegment:cfg.steps});
 const out=Float64Array.from(flow.state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio);
 let norm=0;
 for(let j=0;j<K;j++)norm=Math.max(norm,Math.abs(out[j]-values[n][j])/scales[n]);
 return {stage:n,out,normalizedResidual:norm,minA:flow.minA,minD:flow.minD};
}
const affected=[peak.stage-1,peak.stage];
const before=affected.map(n=>stage(n,states));
if(before[1].out[peak.component]!==peak.flowValue)throw Error('Original local replay no longer agrees');
states[peak.stage][peak.component]=before[1].out[peak.component];
const after=affected.map(n=>stage(n,states));
const slim=row=>({stage:row.stage,normalizedResidual:row.normalizedResidual,minA:row.minA,minD:row.minD});
const summary={scope:'One diagnosed interior one-ULP initial-value candidate, followed by the unchanged full DN solve and audit. No completed prefix is asserted.',
 command:process.argv,input_sha256:sha(input),diagnostic_sha256:sha(diagnostic),source_sha256:{...diag.source_sha256,[process.argv[1]]:sha(process.argv[1]),[path.resolve(sparseHelper)]:sha(sparseHelper)},
 candidate:{stage:peak.stage,component:peak.component,oldValue:peak.stateValue,newValue:peak.flowValue,absoluteChange:peak.flowValue-peak.stateValue,componentUlps:1},
 originalGate:cfg.solveTolerance,originalFullReplayResidual:diag.replayNormalizedResidual,
 affectedStagesBefore:before.map(slim),affectedStagesAfter:after.map(slim)};
console.log(JSON.stringify({event:'neighbor_check',...summary.candidate,before:summary.affectedStagesBefore,after:summary.affectedStagesAfter}));
let response,progressStates=null,progressRow=null;
try{
 const sol=dn.solve(cp.cutHeight,{initial:states,maxIterations:cfg.maxIterations,tolerance:cfg.solveTolerance,
   jacobian:true,audit:true,auditSteps:cfg.auditSteps??cfg.steps,
   progress:(row,values)=>{if(values){progressStates=values;progressRow=row;}console.log(JSON.stringify({event:'original_solve_iteration',...row}));}});
 const checkpoint={parameters:sol.parameters,states:sol.states,rawNode:dn.tail.rawNode,
   rawStates:dn.tail.rawNode.map(n=>sol.states[n]),cutHeight:cp.cutHeight,
   scope:'Actual original finite DN solver output with full audit. No prefix state or complete coupled acceptance is supplied by this record.'};
 response={converged:sol.converged,residual:sol.normalizedResidual,jets:sol.jets,
   heightJetJacobian:sol.heightJetJacobian??null,history:sol.history,audit:sol.audit,checkpoint};
 summary.originalSolverConverged=sol.converged;summary.finalResidual=sol.normalizedResidual;
 summary.minA=sol.minA;summary.minD=sol.minD;summary.audit=sol.audit;summary.history=sol.history;
}catch(error){
 response={failed:String(error),lastIteration:progressRow,checkpoint:progressStates?{
   parameters:dn.tail.parameters,states:progressStates,rawNode:dn.tail.rawNode,
   rawStates:dn.tail.rawNode.map(n=>progressStates[n]),cutHeight:cp.cutHeight,
   scope:'Failed original solve from the one-ULP initial-value candidate.'}:null};
 summary.originalSolverConverged=false;summary.error=String(error);
}
const result={request:{height:cp.cutHeight,jacobian:true,audit:true},response,config:cfg,
 source_sha256:record.source_sha256,execution_source_sha256:summary.source_sha256,
 numerical_initialization:summary.candidate,
 scope:'Direct invocation of the original finite DN solve and full audit. The response is formed from its actual return, not from the local candidate check.'};
fs.writeFileSync(outputRecord,gzipSync(JSON.stringify(result)+'\n'));
summary.output_record_sha256=sha(outputRecord);
fs.writeFileSync(outputSummary,JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify({event:'terminal',converged:summary.originalSolverConverged,residual:summary.finalResidual,error:summary.error,output_record_sha256:summary.output_record_sha256}));
