// Explicit same-density shooting partition warm. See R98 for defect propagation.
// Centered R95 trial plus exact reuse of unchanged same-grid states and heights.
// Original root precision, equations, residual and acceptance are retained.
// R95 geometric trial branch; actual Newton correction and residual acceptance remain original.
// Optional full shooting tangent warm prediction plus Fourier variational assembly.
// Physical configuration, nonlinear equations and success criteria are unchanged.
// New geometric warm embedding only; the original true DN solve and response path follow below.
// Diagnostic-only worker fork; rejection reasons and stage inputs are saved to disk.
// Memory sharing worker; full solve and response protocol are unchanged.
// 950f continuation: frozen weighted metric, own worker; archived constructors unchanged.
// Own wrapper for the frozen physically optimized tail; no metric change on reload.
// Actual custom cut-preserving geometry; recording protocol copied from reviewed split-flux worker.
// Explicit split-flux variant of the reviewed recording worker.
// The complete optional factory has its own algebra and call-path review.
// Optional recording worker. Only checkpoint retention changes relative to
// f6curve_compact_tail_port.mjs SHA256 81834ad36f6cc9767cc4cef850ad0fb6762b8206f54f5f81cff25b76a37fa233.
// Actual compact nonlinear finite-depth physical-height DN for the curve BVP.
// Astra curve_transition, AI-assisted 2026-11-08. No infinite-tail assertion.
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT is required');
import {createSplitFluxCompactTailDN as createCompactTailDN} from './fd2d-bounded-tail-stage-split.mjs';
import {createStagePool} from './fd2d-single-tail-stage-pool.mjs';
import {geometricWarmRemesh} from './78718-tail-geometric-warm-remesh.mjs';
import {partitionWarmRemesh} from './78718-tail-partition-warm-remesh.mjs';
import {geometricAmplitudeWarm} from './78718-tail-geometric-amplitude-warm.mjs';
import {createGeometricTrialHook} from './78718-tail-geometric-newton-retraction-centered-v3.mjs';
import {createFourierProductVariationalEngine} from './78718-tail-fourier-product-flow.mjs';
import {createPhysicalHeightTangentPredictor} from './78718-tail-tangent-predictor.mjs';
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs')));
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import zlib from 'node:zlib';
import readline from 'node:readline';
import v8 from 'node:v8';
import {resourceLimits} from 'node:worker_threads';
const cfg=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const backend=process.env.VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND??'fourier';
const stageWorkers=Number(process.env.VISIBLE_FLEX_TAIL_STAGE_WORKERS);
const predictor=process.env.VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND??'tangent';
if(!['fourier','fourier-root'].includes(backend)||!['linear','tangent'].includes(predictor))
 throw Error('Unknown combined tail implementation');
if(backend!=='fourier-root'||![1,2,4].includes(stageWorkers))
 throw Error('Parallel stage worker requires explicit two- or four-worker Fourier-root selection');
const useTangent=predictor==='tangent';
const backendLabel=backend==='fourier-root'?'fourier-root-and-product-moments-v1':'fourier-product-moments-v1';
const predictorLabel=useTangent?'full-shooting-tangent-v1':'linear-amplitude-and-boundary-v1';
const createFourierRootSplitFluxEngine=backend==='fourier-root'?
 (await import('./78718-tail-fourier-root-split-engine.mjs')).createFourierRootSplitFluxEngine:null;
function trace(row){if(cfg.traceFile)fs.appendFileSync(cfg.traceFile,JSON.stringify({time:new Date().toISOString(),...row})+'\n');}
const physical=createRecalibrationFactory(cfg).assemble();
// The weighted factory already finds zeros of the ACTUAL capped/restored slope.
// The inherited DN factory installs raw-source zeros, so retain both lists.
const actualBreakpoints=physical.cells.map(c=>c.profiles.map(p=>[...(p.integrationBreakpoints??[])]));
let activePool=null;
const stageBatchEvaluator=(inputs,withJac)=>{
 if(!activePool){const e=new Error('Parallel stage evaluator has no active request pool');e.code='TAIL_STAGE_POOL_INFRASTRUCTURE';throw e;}
 return activePool.evaluate(inputs,withJac);
};
const dn=createCompactTailDN({...cfg,tail:physical,retainTangentPredictor:useTangent,stageBatchEvaluator}),M=cfg.modes,zero=dn.cutJets(new Float64Array(2*M));
const transformedEngines=new Set();
for(const cell of dn.tail.cells){
 if(transformedEngines.has(cell.engine))continue;
 transformedEngines.add(cell.engine);
 const original={...cell.engine};
 const options={modes:M,spacing:cfg.spacing,quadrature:cfg.quadrature,mu:cell.mu,
  orientation:dn.tail.parameters.orientation,projectionFloor:dn.tail.parameters.projectionFloor,
  cuspAwareFlow:cfg.cuspAwareFlow===true};
 const updated=backend==='fourier-root'?createFourierRootSplitFluxEngine(options):
  createFourierProductVariationalEngine(options,original);
 Object.assign(cell.engine,updated);
}
const geometricTrial=createGeometricTrialHook(dn.tail.cells,{spacing:cfg.spacing});
function rhsRootStatistics(){
 let evaluations=0,roundoffFallbacks=0,maximumRootRelativeResidual=0;
 for(const engine of transformedEngines){const q=engine.statistics;if(!q)continue;
  evaluations+=q.evaluations;roundoffFallbacks+=q.roundoffFallbacks;maximumRootRelativeResidual=Math.max(maximumRootRelativeResidual,q.maximumRootRelativeResidual);
 }
 const parallel=activePool?.cumulativeStatistics()??null;
 return {evaluations,roundoffFallbacks,maximumRootRelativeResidual,parallel,scope:'Existing parent-engine counters and actual request-pool counters; no extra root or flow.'};
}
trace({event:'solver_resources',heapSizeLimitBytes:v8.getHeapStatistics().heap_size_limit,resourceLimits,cacheRoot:process.env.VISIBLE_FLEX_STAGE_CACHE_ROOT??null});
trace({event:'tail_variational_backend',backend:backendLabel,predictor:predictorLabel});
trace({event:'tail_trial_backend',backend:'same-direction-Q-L-Newton-retraction-centered-v3'});
// The cut restoration can create extra zeros of the actual logarithmic slope.
// Add those zeros to the inherited raw-source cusp grid without changing the
// physical profile. This affects integration only, not any metric parameter.

let last=null,call=0,progressStates=null,progressRow=null,currentHeight=null,warmEmbeddingDiagnostics=null;
let tangentPredictor=null;
// Optional recovery record: this does not change any numerical operation.
// Its state may be unconverged and is only an initial guess for another solve.
if(cfg.iterationCheckpointFile&&fs.existsSync(cfg.iterationCheckpointFile))
 throw new Error('Iteration checkpoint path already exists');
const acceptedCheckpointFile=cfg.iterationCheckpointFile?
 cfg.iterationCheckpointFile.replace(/\.json\.gz$/, '-accepted.json.gz'):null;
if(acceptedCheckpointFile&&fs.existsSync(acceptedCheckpointFile))
 throw new Error('Accepted checkpoint path already exists');
function retainAccepted(row,states){
 if(!acceptedCheckpointFile)return;
 const observed={...row,norm:row.trialNorm,
  scope:'Actual accepted state-only residual; no new full-Jacobian norm or extrema are asserted.'};
 const checkpoint={parameters:dn.tail.parameters,states,rawNode:dn.tail.rawNode,
  rawStates:dn.tail.rawNode.map(n=>states[n]),cutHeight:currentHeight,
  scope:'UNCONVERGED accepted trial state for recovery only; not a solved DN response or geometric certificate.'};
 const data=zlib.gzipSync(JSON.stringify({status:'accepted-trial-recovery-only',call,
  iteration:observed,checkpoint})+'\n');
 if(data.length>=5_000_000)throw new Error('Accepted checkpoint exceeds repository file limit');
 const tmp=acceptedCheckpointFile+'.tmp';fs.writeFileSync(tmp,data);
 fs.renameSync(tmp,acceptedCheckpointFile);
 progressStates=states;progressRow=observed;
 trace({event:'accepted_state_saved',call,iteration:row.iteration,trial:row.trial,step:row.step,
  norm:row.trialNorm,file:acceptedCheckpointFile,bytes:data.length,
  sha256:createHash('sha256').update(data).digest('hex')});
}
function retainRequestedInitial(initial){
 if(!initial||!cfg.iterationCheckpointFile)return;
 const file=cfg.iterationCheckpointFile.replace(/\.json\.gz$/, '-request-initial.json.gz');
 try{
  const states=initial.map(row=>Array.from(row));
  const checkpoint={parameters:dn.tail.parameters,states,rawNode:dn.tail.rawNode,
   rawStates:dn.tail.rawNode.map(n=>states[n]),cutHeight:currentHeight,
   scope:'UNCONVERGED requested initial guess, saved before first residual; not an accepted Newton step or solved DN.'};
  const data=zlib.gzipSync(JSON.stringify({status:'request-initial-recovery-only',call,checkpoint})+'\n');
  if(data.length>=5_000_000)throw new Error('Requested initial checkpoint exceeds file size limit');
  const tmp=file+'.tmp';fs.writeFileSync(tmp,data);fs.renameSync(tmp,file);
  trace({event:'requested_initial_state_saved',call,file,bytes:data.length,
   sha256:createHash('sha256').update(data).digest('hex')});
 }catch(error){trace({event:'recovery_observation_failure',call,kind:'requested-initial',error:String(error)});}
}
function retainIteration(row,states){
 if(!cfg.iterationCheckpointFile)return;
 const checkpoint={parameters:dn.tail.parameters,states,rawNode:dn.tail.rawNode,
  rawStates:dn.tail.rawNode.map(n=>states[n]),cutHeight:currentHeight,
  scope:'UNCONVERGED iteration checkpoint for recovery only; not a solved DN response or geometric certificate.'};
 const data=zlib.gzipSync(JSON.stringify({status:'iteration-recovery-only',call,
  iteration:row,checkpoint})+'\n');
 if(data.length>=5_000_000)throw new Error('Iteration checkpoint exceeds repository file limit');
 const tmp=cfg.iterationCheckpointFile+'.tmp';fs.writeFileSync(tmp,data);
 fs.renameSync(tmp,cfg.iterationCheckpointFile);
}
if(cfg.trialDiagnosticFile&&fs.existsSync(cfg.trialDiagnosticFile))
 throw new Error('Trial diagnostic path already exists');
function retainTrial(row,state){
 if(!cfg.trialDiagnosticFile)return;
 const event={time:new Date().toISOString(),call,...row};
 if(state&&cfg.trialStatePrefix){
  const file=cfg.trialStatePrefix+`-call${call}-iteration${row.iteration}-trial${row.trial}.json.gz`;
  const record={scope:'FAILED trial stage input for diagnostic replay only; not a solved shooting state.',
   parameters:dn.tail.parameters,cutHeight:currentHeight,stage:row.stage,rawCell:row.rawCell,
   rawSegment:row.rawSegment,inputState:state,trial:row};
  const bytes=zlib.gzipSync(JSON.stringify(record)+'\n');
  if(bytes.length>=5_000_000)throw new Error('Trial stage record exceeds repository file limit');
  fs.writeFileSync(file,bytes,{flag:'wx'});
  event.stageInputFile=file;event.stageInputSHA256=createHash('sha256').update(bytes).digest('hex');
  event.stageInputBytes=bytes.length;
 }
 fs.appendFileSync(cfg.trialDiagnosticFile,JSON.stringify(event)+'\n');
}
if(cfg.initialCheckpoint){
 const raw=fs.readFileSync(cfg.initialCheckpoint),record=JSON.parse((cfg.initialCheckpoint.endsWith('.gz')?zlib.gunzipSync(raw):raw).toString());
 const prior=record.response?.checkpoint??record.seam?.tail_checkpoint??record.checkpoint??record;
 if(!prior?.parameters||!prior?.states||!prior?.cutHeight)throw new Error('Initial checkpoint has no complete finite-tail state');
 const old=prior.parameters,now=dn.tail.parameters;
 for(const key of ['pulseCaps','valleyCaps','flatOuterThroughCell','flatOuterStartSegment','flatSlope','capMode','rCut','wCut','width','curvatureBound','slopeCap','capTransition','calibrationSteps','warpSteps','quadratureTolerance','cuspAwareQuadrature','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','warpWeightLevels','constructor','valleyControls','delta0','R','a','etaPower','etaRatioAtN0','rejoinR20At','rejoinIndexOffset','spacing']){
  if(JSON.stringify(old[key]??null)!==JSON.stringify(now[key]??null))throw new Error('Warm tail geometry mismatch: '+key);
 }
 if((old.physicalDepth??old.depth)>cfg.depth)throw new Error('Warm remesh cannot shorten physical depth');

 const oldM=old.modes,keep=Math.min(oldM,M);
 const sameGrid=oldM===M&&old.quadrature===cfg.quadrature&&
  (old.physicalDepth??old.depth)===now.physicalDepth&&old.shootingParts===now.shootingParts&&
  old.steps===now.steps&&JSON.stringify(prior.rawNode)===JSON.stringify(dn.tail.rawNode)&&
  prior.states.length===dn.tail.cells.length+1&&prior.states.every(row=>row.length===2*M&&row.every(Number.isFinite));
 let states;
 if(sameGrid){
  states=prior.states.map(row=>Array.from(row));
  warmEmbeddingDiagnostics={method:'unchanged-same-grid-canonical-state-copy',nodeCount:states.length,
   sourceModes:oldM,targetModes:M,quadrature:cfg.quadrature,maxQChange:0,maxMomentumChange:0,
   rootCallsForCopy:0,knownConvergenceNotInferred:true,sourceScope:prior.scope};
  trace({event:'unchanged_warm_state_copy',source:cfg.initialCheckpoint,...warmEmbeddingDiagnostics});
 }else if(old.shootingParts!==now.shootingParts){
  trace({event:'partition_warm_start',source:cfg.initialCheckpoint,sourceParts:old.shootingParts,
   targetParts:now.shootingParts,sourceSteps:old.steps,targetSteps:now.steps});
  const embedded=partitionWarmRemesh(prior,dn);
  states=embedded.states;warmEmbeddingDiagnostics=embedded.diagnostics;
  trace({event:'partition_warm_complete',source:cfg.initialCheckpoint,...warmEmbeddingDiagnostics});
 }else{
  const embedded=geometricWarmRemesh(prior,dn,createFastSplitFluxMomentumTailEngine);
  states=embedded.states;warmEmbeddingDiagnostics=embedded.diagnostics;
  trace({event:'geometric_warm_embedding',source:cfg.initialCheckpoint,...warmEmbeddingDiagnostics});
 }
 const height=Array(M).fill(0);for(let j=0;j<keep;j++)height[j]=prior.cutHeight[j];
 last={states,jets:{height}};trace({event:'warm_initial_state',source:cfg.initialCheckpoint,sourceModes:oldM,targetModes:M,depth:cfg.depth});
}
const D=[];
for(let j=0;j<M;j++){
 const node=new Float64Array(2*M),q=1e-18;node[j]=q;node[M+j]=q*dn.tail.graphs[0][j];
 const jets=dn.cutJets(node);D.push(jets.slope[j]/jets.height[j]);
}
console.log(JSON.stringify({event:'ready',solverHeapSizeLimitBytes:v8.getHeapStatistics().heap_size_limit,solverResourceLimits:resourceLimits,tailStageWorkers:stageWorkers,tailStageEvaluation:'visible-flex-independent-stage-pool-v4-resumable',parameters:dn.tail.parameters,cut:zero,linearSlope:D,warmEmbedding:warmEmbeddingDiagnostics,tailJacobian:backendLabel,tailPredictor:predictorLabel,amplitudeWarm:'physical-Q-L-amplitude-v1',tailTrial:'same-direction-Q-L-Newton-retraction-centered-v3',shootingGrid:{parts:cfg.shootingParts,stepsPerStage:cfg.steps,auditStepsPerStage:cfg.auditSteps??cfg.steps,nominalRKStepsPerRawProfile:cfg.shootingParts*cfg.steps,nominalAuditStepsPerRawProfile:cfg.shootingParts*(cfg.auditSteps??cfg.steps)}}));
for await(const line of readline.createInterface({input:process.stdin,terminal:false})){
 try{
  const req=JSON.parse(line);if(req.stop)break;currentHeight=req.height;progressStates=null;progressRow=null;
  call++;const start=Date.now();trace({event:'request',call,height:req.height,jacobian:!!req.jacobian,audit:!!req.audit});
  let initial,predicted=false,unchangedWarm=false;
  if(last&&req.height.length===last.jets.height.length&&req.height.every((v,j)=>v===last.jets.height[j])){
   initial=last.states.map(row=>Float64Array.from(row));unchangedWarm=true;
   const r4=zero.radius**4,boundaryMismatch=Math.max(...req.height.map((v,j)=>Math.abs(v/r4-initial[0][j])));
   trace({event:'unchanged_height_canonical_warm',call,actualHeightEqual:true,nodeCount:initial.length,
    rawReprojectionCalls:0,amplitudeScalingCalls:0,boundaryCorrectionApplied:false,
    actualCanonicalBoundaryMismatch:boundaryMismatch,scope:'Initial guess reuse only; the original full residual is evaluated again.'});
  }
  if(!unchangedWarm&&tangentPredictor){
   try{const guess=tangentPredictor.predict(req.height);initial=guess.states;predicted=true;trace({event:'tangent_warm_predictor',call,...guess.diagnostics});}
   catch(error){trace({event:'tangent_warm_fallback',call,error:String(error)});}
  }
  if(!unchangedWarm&&!predicted&&last){
   const prev=last.jets.height[0],ratio=req.height[0]/prev;
   if(Number.isFinite(ratio)&&ratio>.25&&ratio<4){
    const guess=geometricAmplitudeWarm(last.states,dn,ratio);initial=guess.states;
    trace({event:'geometric_amplitude_warm',call,...guess.diagnostics});
   }
  }
  // Warm starts must satisfy the NEW Dirichlet height, including higher modes.
  // Add the exact finite linear response of the height difference; this is only
  // an initial guess. The full nonlinear root/ODE/residual still decides success.
  if(!unchangedWarm&&!predicted&&initial&&cfg.correctInitialBoundary!==false){
   const r4=zero.radius**4,delta=Float64Array.from(req.height,(v,j)=>v/r4-initial[0][j]),add=dn.tail.initial(delta);
   initial=initial.map((row,n)=>row.map((v,j)=>v+add[n][j]));
  }
  retainRequestedInitial(initial);
  activePool=await createStagePool({stages:dn.tail.cells.map((cell,index)=>({index,cell})),
   modes:M,quadrature:cfg.quadrature,spacing:cfg.spacing,orientation:dn.tail.parameters.orientation,
   projectionFloor:dn.tail.parameters.projectionFloor,stepsPerSegment:cfg.steps,workers:stageWorkers,
   cuspAwareFlow:cfg.cuspAwareFlow===true,cacheRoot:process.env.VISIBLE_FLEX_STAGE_CACHE_ROOT,
   cacheDiagnostic:row=>trace({call,...row})});
  trace({event:'stage_pool_ready',call,...activePool.metadata});
  let sol;
  try{
  sol=dn.solve(req.height,{maxIterations:cfg.maxIterations??24,tolerance:cfg.solveTolerance??2e-10,initial,jacobian:!!req.jacobian,audit:!!req.audit,auditSteps:cfg.auditSteps??cfg.steps,retractTrial:geometricTrial.retractTrial,trialDiagnostic:retainTrial,acceptedStep:retainAccepted,observationFailure:row=>trace({event:'recovery_observation_failure',call,...row}),progress:(row,states)=>{const observed={...row,rhsRootStatistics:rhsRootStatistics()};if(states){progressStates=states;progressRow=observed;retainIteration(observed,states);}trace({event:'iteration',call,elapsed_ms:Date.now()-start,...observed});}});
  }finally{
   const pool=activePool,statistics=pool.cumulativeStatistics(),closeStart=Date.now();
   const closeResult=await pool.close();activePool=null;
   trace({event:'stage_pool_closed',call,closeMilliseconds:Date.now()-closeStart,
    statistics,workersExited:true,closeResult,scope:'Threads released before response; transient buffers are no longer retained by the pool.'});
  }
  trace({event:'geometric_trial_statistics',call,...geometricTrial.statistics});
  if(sol.converged){
   last=sol;tangentPredictor=null;
   if(useTangent){
    try{tangentPredictor=createPhysicalHeightTangentPredictor(sol,dn.tail.graphs.at(-1),zero.radius);trace({event:'tangent_predictor_ready',call,maxChartCondition:tangentPredictor.maxChartCondition});}
    catch(error){trace({event:'tangent_predictor_unavailable',call,error:String(error)});}
   }
  }
  trace({event:'response',call,elapsed_ms:Date.now()-start,converged:sol.converged,residual:sol.normalizedResidual,maxChartCondition:Math.max(...sol.history.map(x=>x.chartCondition??0))});
  // Every actual response retains the shooting state. Audit execution itself
  // is still controlled by req.audit and has not been weakened or bypassed.
  const checkpoint={parameters:sol.parameters,states:sol.states,rawNode:dn.tail.rawNode,rawStates:dn.tail.rawNode.map(n=>sol.states[n]),cutHeight:req.height,scope:'Finite Fourier/depth shooting state; the far Robin condition is not an exact rotational collar. Retained for every actual response; an unaudited response is not a final geometric audit.'};
  console.log(JSON.stringify({converged:sol.converged,residual:sol.normalizedResidual,jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,history:sol.history,audit:sol.audit??null,checkpoint}));
 }catch(e){trace({event:'geometric_trial_statistics',call,...geometricTrial.statistics});trace({event:'failure',call,error:String(e),infrastructureErrorCode:e.code??null});console.log(JSON.stringify({failed:String(e),lastIteration:progressRow,checkpoint:progressStates?{parameters:dn.tail.parameters,states:progressStates,rawNode:dn.tail.rawNode,rawStates:dn.tail.rawNode.map(n=>progressStates[n]),cutHeight:currentHeight,scope:'FAILED Newton state; retained only for diagnosis and possible initial guesses.'}:null}));}
}
process.stdin.destroy();
