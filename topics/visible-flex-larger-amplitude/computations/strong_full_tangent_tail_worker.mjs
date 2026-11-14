// Fresh storage-only extension of the retained exact-stage worker.
// The original mathematical MJS files remain unchanged. Full flow-J data are
// persisted only after the original nonlinear solve converges, then reused
// only by the unchanged original full-shooting tangent predictor as a guess.
// Explicit complete-input stage persistence around the retained exact-raw worker.
// All original nonlinear residual, line search, full-H Jacobian and audit paths
// remain. The diagnostic request compares the full actual evaluate only and
// never returns a converged DN response.
import fs from 'node:fs';
import crypto from 'node:crypto';

const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
const templateURL=new URL('./strong_exact_raw_tail_worker.mjs',import.meta.url);
const original=fs.readFileSync(templateURL,'utf8');
const expected='ec69703a4b0786313c2506aae5f82ec8da39330876d15519225e2d4b7f7d2cc8';
if(sha(original)!==expected)throw Error('The original exact-raw worker changed');


const retainedStageURL=new URL('./strong_exact_stage_tail_worker.mjs',import.meta.url);
if(sha(fs.readFileSync(retainedStageURL))!=='b7bb40dc25a8a4add993fdb99e8cc48aa0b636d6200e31818f9f1e8844cc9e35')
 throw Error('The retained exact-stage worker template differs');

const lowerEdits=[{
 before:' const prior=record.response?.checkpoint??record.seam?.tail_checkpoint??record.checkpoint??record;',
 after:' const prior=restoreExactInitialSeed(record.response?.checkpoint??record.seam?.tail_checkpoint??record.checkpoint??record,dn);'
},{
 before:"console.log(JSON.stringify({event:'ready',exactRawWarmAdapter:exactRawWarmAdapterManifest,",
 after:"console.log(JSON.stringify({event:'ready',exactStageCacheAdapter:stageCacheWorkerManifest,exactStageStorage:dn.tail.exactStagePersistence,exactRawWarmAdapter:exactRawWarmAdapterManifest,"
},{
 before:'const sol=dn.solve(req.height,',
 after:`const exactInitialSeed=saveExactInitialSeed({dn,height:req.height,states:initial,call,
    prefix:process.env.VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX,sourceIdentity:{...stageCacheWorkerManifest,
     engineSHA256:stageCacheWorkerManifest.stageEngineSHA256,helperSHA256:stageCacheWorkerManifest.seedHelperSHA256}});
  trace({event:'exact_initial_stage_seed_saved',call,...exactInitialSeed});
  if(req.exactStageDiagnostic===true){
   const check=compareCompleteStageEvaluation(dn,initial,req.height,row=>trace({...row,call}));
   console.log(JSON.stringify({exactStageDiagnostic:check,exactInitialSeed,
    prefixAccepted:false,tailConverged:false}));continue;
  }
  const sol=dn.solve(req.height,`
}];
lowerEdits.push(...[{"before":"let tangentPredictor=null;","after":"let tangentPredictor=null;\nlet fullFlowTangentRestored=null;\nconst tangentStaticIdentity=storedEngineManifest.exactStageHost.sourceIdentity;\nconst fullFlowTangentSourceSHA=Object.fromEntries([\n ...Object.entries(tangentStaticIdentity.pinnedMjs).map(([k,v])=>['pinned/'+k,v]),\n ...Object.entries(tangentStaticIdentity.pinnedTopicMjs).map(([k,v])=>['pinned-topic/'+k,v]),\n ...Object.entries(tangentStaticIdentity.adapterMjs).map(([k,v])=>['adapter/'+k,v]),\n ['worker',fullFlowTangentAdapterManifest.workerSHA256],\n ['storage-helper',fullFlowTangentAdapterManifest.storageHelperSHA256]\n]);\nconst tangentGeometry=storedGeometry.manifest;\nconst tangentNonIO=x=>Object.fromEntries(Object.entries(x).filter(([k])=>\n !['traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint'].includes(k)));\nconst fullFlowTangentIdentity=describeTailTangentIdentity({dn,radius:zero.radius,\n sourceSha256:fullFlowTangentSourceSHA,\n physicalIdentity:{parameters:tangentNonIO(tangentGeometry.physicalParameters),\n  frozenWarpAlpha:tangentGeometry.frozenWarpAlpha,\n  profileFingerprintBefore:tangentGeometry.profileFingerprintBefore,\n  profileFingerprintAfter:tangentGeometry.profileFingerprintAfter,\n  fingerprintFields:tangentGeometry.fingerprintFields,\n  fingerprintFractions:tangentGeometry.fingerprintFractions,\n  calibrationLedgerSHA256:tangentStaticIdentity.calibrationLedgerSHA256,\n  storedReferenceReadySHA256:tangentStaticIdentity.storedReferenceReadySHA256},\n backendIdentity:{backend,predictor,backendLabel,predictorLabel,\n  completeStageEngine:'split-linear-flux-v1',\n  sourceRevision:tangentStaticIdentity.pinnedSourceRevision,\n  sourceManifest:tangentStaticIdentity.pinnedSourceManifest}});\nif(!process.env.VISIBLE_FLEX_FULL_TANGENT_OUTPUT_PREFIX)\n throw Error('An explicit full-flow tangent output prefix is required');\nif(process.env.VISIBLE_FLEX_FULL_TANGENT_INPUT&&!cfg.initialCheckpoint)\n throw Error('A saved full-flow tangent requires its exact complete checkpoint');"},{"before":" last={states,jets:{height}};trace({event:'warm_initial_state',source:cfg.initialCheckpoint,sourceModes:oldM,targetModes:M,depth:cfg.depth});","after":" last={states,jets:{height}};trace({event:'warm_initial_state',source:cfg.initialCheckpoint,sourceModes:oldM,targetModes:M,depth:cfg.depth});\n if(process.env.VISIBLE_FLEX_FULL_TANGENT_INPUT){\n  const restored=readFullFlowTangentSnapshot({\n   manifestPath:process.env.VISIBLE_FLEX_FULL_TANGENT_INPUT,\n   manifestSha256:process.env.VISIBLE_FLEX_FULL_TANGENT_INPUT_SHA256||undefined,\n   checkpoint:prior,identity:fullFlowTangentIdentity});\n  tangentPredictor=createPhysicalHeightTangentPredictor(restored.solution,restored.farGraph,restored.radius);\n  fullFlowTangentRestored={...restored.diagnostics,\n   maxChartCondition:tangentPredictor.maxChartCondition,\n   originalFactoryCalled:true,initialGuessOnly:true};\n  trace({event:'full_flow_tangent_restored',...fullFlowTangentRestored});\n }"},{"before":"console.log(JSON.stringify({event:'ready',exactStageCacheAdapter:stageCacheWorkerManifest,","after":"console.log(JSON.stringify({event:'ready',fullFlowTangentAdapter:fullFlowTangentAdapterManifest,fullFlowTangentRestored,exactStageCacheAdapter:stageCacheWorkerManifest,"},{"before":"  trace({event:'response',call,elapsed_ms:Date.now()-start,converged:sol.converged,residual:sol.normalizedResidual,maxChartCondition:Math.max(...sol.history.map(x=>x.chartCondition??0))});","after":"  let fullFlowTangentSnapshot=null,fullFlowTangentStorageError=null;\n  if(sol.converged){\n   try{\n    const saved=writeFullFlowTangentSnapshot({\n     outPrefix:process.env.VISIBLE_FLEX_FULL_TANGENT_OUTPUT_PREFIX+'-call'+String(call).padStart(4,'0'),\n     solution:sol,cutHeight:req.height,identity:fullFlowTangentIdentity,\n     solveTolerance:cfg.solveTolerance??2e-10});\n    const prior={parameters:sol.parameters,states:sol.states,rawNode:dn.tail.rawNode,\n     rawStates:dn.tail.rawNode.map(n=>sol.states[n]),cutHeight:req.height};\n    const restored=readFullFlowTangentSnapshot({manifestPath:saved.manifestPath,\n     manifestSha256:saved.manifestSha256,checkpoint:prior,identity:fullFlowTangentIdentity});\n    let checkedValues=0;\n    for(let n=0;n<sol.states.length;n++)for(let j=0;j<sol.states[n].length;j++){\n     if(!Object.is(sol.states[n][j],restored.solution.states[n][j]))throw Error('Full-flow base bit roundtrip failed');\n     checkedValues++;\n    }\n    for(let j=0;j<req.height.length;j++){\n     if(!Object.is(req.height[j],restored.baseHeight[j])||\n        !Object.is(dn.tail.graphs.at(-1)[j],restored.farGraph[j]))\n      throw Error('Full-flow complete height or far-graph bit roundtrip failed');\n     checkedValues+=2;\n    }\n    if(!Object.is(zero.radius,restored.radius))throw Error('Full-flow radius bit roundtrip failed');\n    checkedValues++;\n    for(let n=0;n<sol.linearizedFlowJacobians.length;n++)for(let j=0;j<sol.linearizedFlowJacobians[n].length;j++){\n     if(!Object.is(sol.linearizedFlowJacobians[n][j],restored.solution.linearizedFlowJacobians[n][j]))\n      throw Error('Full-flow Jacobian bit roundtrip failed');\n     checkedValues++;\n    }\n    let originalFactoryPredictorCheck=null;\n    if(call===1&&tangentPredictor){\n     const recovered=createPhysicalHeightTangentPredictor(restored.solution,restored.farGraph,restored.radius);\n     const probe=req.height.map((v,j)=>v*(1+2**-20)+req.height[0]*2**(-40-j));\n     const a=tangentPredictor.predict(probe),b=recovered.predict(probe);let count=0;\n     for(let n=0;n<a.states.length;n++)for(let j=0;j<a.states[n].length;j++){\n      if(!Object.is(a.states[n][j],b.states[n][j]))throw Error('Original predictor differs after full-flow storage');\n      count++;\n     }\n     originalFactoryPredictorCheck={allStateValuesBitwiseEqual:true,values:count,\n      probeCompleteHeight:probe,probePurpose:'Storage equivalence only; no probe nonlinear solve or accepted target.'};\n    }\n    fullFlowTangentSnapshot={...saved,roundtrip:{allBaseAndFlowValuesBitwiseEqual:true,\n     checkedValues,originalFactoryPredictorCheck}};\n    trace({event:'full_flow_tangent_saved',call,...fullFlowTangentSnapshot});\n   }catch(error){\n    fullFlowTangentStorageError=String(error);\n    trace({event:'full_flow_tangent_storage_failed',call,error:String(error),\n     originalConvergedResponseRetained:true,predictorSidecarNotUsed:true});\n   }\n  }\n  trace({event:'response',call,elapsed_ms:Date.now()-start,converged:sol.converged,residual:sol.normalizedResidual,maxChartCondition:Math.max(...sol.history.map(x=>x.chartCondition??0))});"},{"before":"audit:sol.audit??null,checkpoint}));","after":"audit:sol.audit??null,checkpoint,fullFlowTangentSnapshot,fullFlowTangentStorageError}));"}]);
const extraTemplateEdits=[{
 before:"const engineURL=new URL('./tail_resumable_engine.mjs',import.meta.url).href;",
 after:"const engineURL=new URL('./strong_exact_stage_engine.mjs',import.meta.url).href;"
},{
 before:"const rawWarmURL=new URL('./strong_exact_raw_tail_warm.mjs',import.meta.url).href;",
 after:`const rawWarmURL=new URL('./strong_exact_raw_tail_warm.mjs',import.meta.url).href;
const stageSeedURL=new URL('./strong_exact_stage_seed.mjs',import.meta.url).href;
const stageCheckURL=new URL('./strong_exact_stage_evaluation_check.mjs',import.meta.url).href;
const stageCacheWorkerManifest={name:'exact-input-persistent-actual-stage-worker-v1',
 workerSHA256:sha256(fs.readFileSync(new URL(import.meta.url))),
 exactRawWorkerSHA256:${JSON.stringify(expected)},
 stageEngineSHA256:sha256(fs.readFileSync(new URL(engineURL))),
 seedHelperSHA256:sha256(fs.readFileSync(new URL(stageSeedURL))),
 evaluationCheckSHA256:sha256(fs.readFileSync(new URL(stageCheckURL))),
 transformedExactRawHostSHA256:process.env.STRONG_EXACT_STAGE_HOST_SHA,
 sourceTransforms:JSON.parse(process.env.STRONG_EXACT_STAGE_SOURCE_TRANSFORMS),
 actualVariationalBackend:'fourier-root-and-product-moments-v1',
 scope:'Exact binary stage persistence and unaccepted initial-seed retention only. Every original full nonlinear solve, Jacobian, positivity, line search and final audit gate remains.'};`
},{
 before:'const dn=createSourceCompactTailDN(options),sourceSolve=dn.solve;',
 after:`if(backend!=='fourier-root')throw Error('The explicitly verified cache requires the actual Fourier-root backend');
  if(!process.env.VISIBLE_FLEX_EXACT_STAGE_CACHE||!process.env.VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX)
   throw Error('Exact-stage storage and initial-seed paths must be explicit');
  const dn=createSourceCompactTailDN({...options,exactStageCache:{
   directory:process.env.VISIBLE_FLEX_EXACT_STAGE_CACHE,
   identity:{worker:stageCacheWorkerManifest,actualVariationalBackend:backend,predictor,
    splitConstructorFollowedByOriginalFourierRootObjectAssign:true},
   event:row=>trace({event:'exact_stage_cache',...row})}}),sourceSolve=dn.solve;`
},{
 before:'const importRedirects=[];',
 after:'for(const {before,after} of '+JSON.stringify(lowerEdits)+')replaceOnce(before,after);\nconst importRedirects=[];'
},{
 before:'source=`import {preserveExactRawWarm,samePhysicalHeight,rawWarmGarbageCollection} from ${JSON.stringify(rawWarmURL)};\\n`+',
 after:'source=`import {saveExactInitialSeed,restoreExactInitialSeed} from ${JSON.stringify(stageSeedURL)};\\n`+\n'+
       '  `import {compareCompleteStageEvaluation} from ${JSON.stringify(stageCheckURL)};\\n`+\n'+
       '  `const stageCacheWorkerManifest=${JSON.stringify(stageCacheWorkerManifest)};\\n`+\n'+
       '  `import {preserveExactRawWarm,samePhysicalHeight,rawWarmGarbageCollection} from ${JSON.stringify(rawWarmURL)};\\n`+'
},{
 before:'  exactRawWarmAdapter:rawWarmAdapterManifest,',
 after:'  exactStageCacheAdapter:stageCacheWorkerManifest,\n  exactRawWarmAdapter:rawWarmAdapterManifest,'
}];
extraTemplateEdits.push(...[{"before":"const stageCacheWorkerManifest={name:'exact-input-persistent-actual-stage-worker-v1',","after":"const fullFlowTangentStoreURL=new URL('./strong_full_flow_tangent_storage.mjs',import.meta.url).href;\nconst fullFlowTangentAdapterManifest={name:'original-full-shooting-tangent-storage-worker-v1',\n workerSHA256:sha256(fs.readFileSync(new URL(import.meta.url))),\n stageTemplateSHA256:'b7bb40dc25a8a4add993fdb99e8cc48aa0b636d6200e31818f9f1e8844cc9e35',\n storageHelperSHA256:sha256(fs.readFileSync(new URL(fullFlowTangentStoreURL))),\n originalPredictorSHA256:sha256(fs.readFileSync(path.join(topic,'scripts/78718-tail-tangent-predictor.mjs'))),\n scope:'Only binary persistence and exact-identity restoration of the original converged full flow Jacobians. The unchanged original predictor factory supplies an initial guess; every original full nonlinear, positivity, Jacobian and audit gate remains.'};\nconst stageCacheWorkerManifest={name:'exact-input-persistent-actual-stage-worker-v1',"},{"before":"source=`import {saveExactInitialSeed,restoreExactInitialSeed} from ${JSON.stringify(stageSeedURL)};\\n`+","after":"source=`import {describeTailTangentIdentity,writeFullFlowTangentSnapshot,readFullFlowTangentSnapshot} from ${JSON.stringify(fullFlowTangentStoreURL)};\\n`+\n  `const fullFlowTangentAdapterManifest=${JSON.stringify(fullFlowTangentAdapterManifest)};\\n`+\n  `import {saveExactInitialSeed,restoreExactInitialSeed} from ${JSON.stringify(stageSeedURL)};\\n`+"},{"before":"  exactStageCacheAdapter:stageCacheWorkerManifest,","after":"  fullFlowTangentAdapter:fullFlowTangentAdapterManifest,\n  exactStageCacheAdapter:stageCacheWorkerManifest,"},{"before":"  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));","after":"  if(process.env.VISIBLE_FLEX_FULL_TANGENT_SOURCE_ONLY){\n   const destination=process.env.VISIBLE_FLEX_FULL_TANGENT_SOURCE_ONLY;\n   fs.writeFileSync(destination,source,{flag:'wx'});\n   console.log(JSON.stringify({event:'full_tangent_worker_source_prepared',file:destination,\n    sourceSHA256:sha256(source),fullFlowTangentAdapterManifest,\n    sourceTransforms:JSON.parse(process.env.STRONG_EXACT_STAGE_SOURCE_TRANSFORMS),\n    noTailEngineInstantiated:true,noNumericalSolvePerformed:true}));\n  }else await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));"}]);
const hostEdits=[{
 before:'for(const {before,after} of templateEdits){',
 after:'templateEdits.push(...'+JSON.stringify(extraTemplateEdits)+');\nfor(const {before,after} of templateEdits){'
},{
 before:"const templateURL=new URL('./tail_frozen_worker.mjs',import.meta.url);",
 after:'const templateURL=new URL('+JSON.stringify(new URL('./tail_frozen_worker.mjs',import.meta.url).href)+');'
},{
 before:"source=source.replaceAll('import.meta.url',JSON.stringify(import.meta.url));",
 after:"source=source.replaceAll('import.meta.url',JSON.stringify("+JSON.stringify(import.meta.url)+'));'
}];
let transformed=original;
for(const {before,after} of hostEdits){
 if(transformed.split(before).length!==2)throw Error('Exact-stage host source anchor is not unique');
 transformed=transformed.replace(before,after);
}
process.env.STRONG_EXACT_STAGE_HOST_SHA=sha(transformed);
process.env.STRONG_EXACT_STAGE_SOURCE_TRANSFORMS=JSON.stringify({originalExactRawWorkerSHA256:expected,
 hostEdits,extraTemplateEdits,lowerEdits});
try{await import('data:text/javascript;base64,'+Buffer.from(transformed).toString('base64'));}
catch(error){
 console.error(String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<exact-stage-worker>'));
 process.exitCode=1;
}
