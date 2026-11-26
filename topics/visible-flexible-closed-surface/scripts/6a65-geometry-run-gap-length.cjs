"use strict";
/* Complete R215 gap/length LM. Each CLI invocation deliberately performs
 * exactly one full normal and one actual LM search, then exits. A supervisor
 * may resume the saved state in a fresh process to bound memory. */
async function runOne(candidate,input,options={}) {
  const state=require("./6a65-geometry-gap-length-value.cjs").createGapLengthState(candidate,input);
  const kernel=require("./fd2d_appended_global_schur_R206.cjs")
    .createR206AppendedGlobalKernel(require("./fd2d-R201-R205-band-border-layout.cjs"));
  const lm=require("./fd2d_band_border_lm_adapter_v2_R195.cjs")
    .createBandBorderLM(kernel,state.provider.definition,{halfBandwidthBlocks:4});
  const inherited=input.schema==="6a65-gap-length-R215-checkpoint-v1";
  const priorAccepted=inherited?input.gapLengthAcceptedSteps:0;
  if(!Number.isInteger(priorAccepted)||priorAccepted<0)throw Error("Valid new-design accepted count required");
  let z=Array.from(state.z),lambda=input.nextLambda??input.lambda??1e-3;
  const started=new Date().toISOString(),start=Date.now();
  const summary=q=>Object.fromEntries(Object.entries(q).filter(([k])=>
    !["H","g","diagonal","residuals","jvp","z"].includes(k)));
  const release=()=>{state.position.clearSliceReuse?.();if(typeof global.gc==="function")global.gc();};
  const normal=state.provider.normal(z),normalSeconds=(Date.now()-start)/1000;
  release();
  if(options.onEvent)options.onEvent({event:"normal",iteration:priorAccepted+1,seconds:normalSeconds,
    R2:normal.squaredNorm,metric:normal.maxRelativeMetric,curvature:normal.curvature?.maxCurvature});
  const result=await lm.lmStep({z,normal,lambda,maxDampingAttempts:8,alphas:[1,.5,.25],
    value:q=>{const v=state.provider.value(q);release();return v;},
    onTrial:t=>options.onEvent?.({event:"trial",iteration:priorAccepted+1,attempt:t.attempt,
      alpha:t.alpha,accepted:t.accepted,R2:t.squaredNorm,error:t.error?.message})});
  if(result.accepted){z=Array.from(result.z);lambda=result.nextLambda;}
  const record={iteration:priorAccepted+1,accepted:result.accepted,status:result.status,
    baseline:summary(normal),evaluation:result.evaluation??null,alpha:result.alpha??null,
    squaredNorm:result.squaredNorm,nextLambda:lambda,trace:result.trace,
    solveInfo:result.solveInfo??result.lastSolveInfo,actualValueEvaluations:result.actualValueEvaluations,
    normalSeconds,elapsedSeconds:(Date.now()-start)/1000};
  const checkpoint={schema:"6a65-gap-length-R215-checkpoint-v1",
    options:{...input.options,gap:state.gap},curvatureOptions:input.curvatureOptions,
    geometryOptions:state.geometryOptions,centralSeed:state.centralSeed,z,nextLambda:lambda,
    gapLengthAcceptedSteps:priorAccepted+(result.accepted?1:0),newDesignAcceptedSteps:priorAccepted+(result.accepted?1:0),
    accepted:result.accepted,status:result.status,
    gapLengthDesign:{...state.design,amplitude:z[state.design.amplitudeIndex],
      trueCuffHeight:state.base.height+z[state.cutHeightIndex]},
    initialGapLengthTransfer:input.initialGapLengthTransfer??input.gapLengthDesign,
    outerLengthDesign:state.design.outerLengthDesign,outerLengthFactoryOptions:state.factoryOptions,
    metricTau:state.metricTau,providerDefinition:state.provider.definition,backendDefinition:lm.backendDefinition,
    history:[record],historyMeaning:"This single-normal invocation; parentInput names the previous accepted state",
    baseline:record.baseline,evaluation:record.evaluation,
    execution:{runtime:"Node.js "+process.version,start:started,updated:new Date().toISOString(),
      elapsedSeconds:record.elapsedSeconds,actualNormalEvaluations:1,
      actualAcceptedLMSteps:result.accepted?1:0,OSExitCode:null,externalExitReceiptRequired:true},
    physicalMetricIsDesignVariable:true,continuousCertificate:false,wholeClosedReachCertified:false,strongTargetComplete:false};
  release();
  return {checkpoint,record};
}
module.exports={runOne};
if(require.main===module) {
  const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
  const [candidateFile,inputFile,prefix]=process.argv.slice(2);
  if(!candidateFile||!inputFile||!prefix||fs.existsSync(prefix+"-state.json"))
    throw Error("candidate input fresh-output-prefix required");
  const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
  const emit=o=>process.stdout.write(JSON.stringify(o)+"\n");
  const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile));
  runOne(candidate,input,{onEvent:emit}).then(({checkpoint,record})=>{
    checkpoint.parentInput=inputFile;
    checkpoint.source={candidate:candidateFile,candidateSHA256:hash(candidateFile),
      inputSHA256:hash(inputFile),entrySHA256:hash(__filename),
      factorySHA256:hash(path.join(__dirname,"6a65-geometry-gap-length-value.cjs")),
      completeCapGuideSHA256:hash(path.join(__dirname,"6a65-geometry-wide-cap-provider.cjs"))};
    fs.mkdirSync(path.dirname(prefix),{recursive:true});
    fs.writeFileSync(prefix+"-state.json",JSON.stringify(checkpoint)+"\n");
    emit({event:"complete",accepted:record.accepted,iteration:record.iteration,
      acceptedTotal:checkpoint.gapLengthAcceptedSteps,R2:record.squaredNorm,
      metric:record.evaluation?.maxRelativeMetric,curvature:record.evaluation?.curvature?.maxCurvature,
      geometry:record.evaluation?.geometry,A:checkpoint.gapLengthDesign.amplitude,
      Z:checkpoint.gapLengthDesign.trueCuffHeight,alpha:record.alpha,seconds:record.elapsedSeconds,
      outputSHA256:hash(prefix+"-state.json")});
  }).catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
