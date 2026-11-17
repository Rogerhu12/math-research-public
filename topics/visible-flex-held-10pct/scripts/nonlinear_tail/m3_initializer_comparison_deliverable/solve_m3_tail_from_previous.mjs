// Use an accepted complete state as an initial guess for a new Dirichlet
// target. The original multiple-shooting residual already includes that
// target and its Newton boundary rows. No boundary is pre-forced and no
// equation, local root guard, line search or acceptance test is changed.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,oldFile,requestFile,outFile]=process.argv.slice(2);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const read=p=>JSON.parse(gunzipSync(fs.readFileSync(p)));
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const old=read(oldFile),request=read(requestFile),prior=old.response.checkpoint;
if(!old.response.converged||!prior?.states)throw Error('An accepted complete initial state is required');
const traceFile=outFile.replace(/\.json\.gz$/,'.trace.jsonl');
const cfg={...request.config,initialCheckpoint:oldFile,traceFile};
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const {remeshCheckpoint}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-warm-remesh.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,'f6tail_fast_split_flux_engine.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const checks=['pulseCaps','valleyCaps','flatOuterThroughCell','flatOuterStartSegment','flatSlope','capMode',
 'rCut','wCut','width','curvatureBound','slopeCap','capTransition','calibrationSteps','warpSteps',
 'quadratureTolerance','cuspAwareQuadrature','orientation','prefixR','prefixEnd','prefixReturnStart',
 'protectCell','warpWeightLevels','constructor','valleyControls','delta0','R','a','etaPower',
 'etaRatioAtN0','rejoinR20At','rejoinIndexOffset','spacing'];
for(const key of checks)if(JSON.stringify(prior.parameters[key]??null)!==JSON.stringify(dn.tail.parameters[key]??null))
 throw Error('Physical warm parameter differs: '+key);
const initial=remeshCheckpoint(prior,dn,createFastSplitFluxMomentumTailEngine),height=request.request.height;
const start=Date.now();let lastStates=null,lastRow=null;
const trace=row=>fs.appendFileSync(traceFile,JSON.stringify({time:new Date().toISOString(),...row})+'\n');
const record={scope:'Actual original finite DN solve from an unscaled accepted initial state. New Dirichlet data are paid by the full original residual and Newton boundary rows. A successful tail alone is not a new coupled prefix or a closed family.',
 request:{height,jacobian:false,audit:true},config:cfg,source_sha256:{runner:sha(process.argv[1]),
  stage_core:sha(path.join(topic,'scripts/950f-tail-stage-core.mjs')),
  stage_split:sha(path.join(topic,'scripts/950f-tail-stage-split.mjs')),
  physical_factory:sha(path.join(topic,'scripts/closing_weighted_tail.mjs'))},
 initial_state_sha256:sha(oldFile),requested_vector_source_sha256:sha(requestFile),
 initialization:'unscaled accepted previous states; no linear boundary correction',
 physical_checks:checks};
trace({event:'start',initialization:record.initialization,requested_primary_ratio:height[0]/prior.cutHeight[0]});
try{
 const sol=dn.solve(height,{maxIterations:cfg.maxIterations??24,tolerance:cfg.solveTolerance??2e-10,
  initial,jacobian:false,audit:true,auditSteps:cfg.auditSteps??cfg.steps,
  progress:(row,states)=>{if(states){lastStates=states;lastRow=row;}trace({event:'iteration',elapsed_ms:Date.now()-start,...row});}});
 const checkpoint={parameters:sol.parameters,states:sol.states,rawNode:dn.tail.rawNode,
  rawStates:dn.tail.rawNode.map(n=>sol.states[n]),cutHeight:height,
  scope:'Finite nonlinear multiple-shooting response. Accepted only if response.converged is true; no infinite or closed-family claim.'};
 record.response={converged:sol.converged,residual:sol.normalizedResidual,jets:sol.jets,
  heightJetJacobian:null,history:sol.history,audit:sol.audit,checkpoint};
 trace({event:'response',converged:sol.converged,residual:sol.normalizedResidual,elapsed_ms:Date.now()-start});
}catch(error){
 record.response={failed:String(error),lastIteration:lastRow,checkpoint:lastStates?{
  parameters:dn.tail.parameters,states:lastStates,rawNode:dn.tail.rawNode,
  rawStates:dn.tail.rawNode.map(n=>lastStates[n]),cutHeight:height,
  scope:'Failed or incomplete Newton iterate, initial guesses/diagnostics only.'}:null};
 trace({event:'failure',error:String(error),elapsed_ms:Date.now()-start});
}
record.seconds=(Date.now()-start)/1000;
fs.writeFileSync(outFile,gzipSync(JSON.stringify(record)));
const summary={scope:record.scope,initialization:record.initialization,
 converged:record.response.converged??false,error:record.response.failed??null,
 residual:record.response.residual??null,lastIteration:record.response.lastIteration??null,
 audit:record.response.audit??null,seconds:record.seconds,output_sha256:sha(outFile),
 trace_sha256:sha(traceFile),source_sha256:record.source_sha256};
fs.writeFileSync(outFile.replace(/\.json\.gz$/,'.summary.json'),JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify(summary));
