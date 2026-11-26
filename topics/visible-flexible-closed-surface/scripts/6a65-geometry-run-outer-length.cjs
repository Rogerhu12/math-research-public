"use strict";
/* Complete fixed-Delta R206 LM branch. All saved states are reproducible raw
 * outputs and belong in scratch, not in Git. No tail/cap or metric tolerance
 * is replaced with a penalty value. */
async function run(candidate,input,extraLength,count,options={}) {
  if(!Number.isInteger(count)||count<1)throw Error("Positive actual step count required");
  const factory=require("./6a65-geometry-outer-length-design.cjs"),factoryOptions={lazyCurvature:true,referenceCacheLimit:0,...options.factoryOptions};
  const state=factory.createOuterLengthRunProvider(candidate,input,extraLength,factoryOptions);
  const kernel=require("./fd2d_appended_global_schur_R206.cjs").createR206AppendedGlobalKernel(require("./fd2d-R201-R205-band-border-layout.cjs"));
  const lm=require("./fd2d_band_border_lm_adapter_v2_R195.cjs").createBandBorderLM(kernel,state.provider.definition,{halfBandwidthBlocks:4});
  let z=state.z,lambda=input.nextLambda??input.lambda??1e-3,accepted=input.outerLengthAcceptedSteps||0;
  const history=Array.from(input.outerLengthHistory||[]);
  const actualStart=new Date().toISOString(),actualStartMilliseconds=Date.now();
  const summary=o=>Object.fromEntries(Object.entries(o).filter(([k])=>!["H","g","diagonal","residuals","jvp","z"].includes(k)));
  function checkpoint(record) {
    return {...input,schema:"6a65-outer-length-actual-checkpoint-v1",z,lambda,nextLambda:lambda,
      outerLengthDesign:state.design,outerLengthFactoryOptions:factoryOptions,outerLengthAcceptedSteps:accepted,outerLengthHistory:history,
      evaluation:record.evaluation??record.baseline,providerDefinition:state.provider.definition,backendDefinition:lm.backendDefinition,
      inheritedParentExecution:input.execution??null,
      execution:{runtime:"Node.js "+process.version,start:actualStart,updated:new Date().toISOString(),
        elapsedSeconds:(Date.now()-actualStartMilliseconds)/1000,OSExitCode:null,exitReceiptBelongsToCallingProcess:true},
      physicalMetricIsDesignVariable:true,continuousCertificate:false,wholeClosedReachCertified:false,strongTargetComplete:false};
  }
  let latest;
  function releaseTemporarySlices(){state.position.clearSliceReuse?.();if(typeof global.gc==="function")global.gc();}
  for(let j=0;j<count;j++) {
    const begin=Date.now(),normal=state.provider.normal(z),normalSeconds=(Date.now()-begin)/1000;
    releaseTemporarySlices();
    const result=await lm.lmStep({z,normal,value:v=>{const actual=state.provider.value(v);releaseTemporarySlices();return actual;},
      lambda,maxDampingAttempts:8,alphas:[1,.5,.25]});
    const record={iteration:accepted+1,accepted:result.accepted,status:result.status,baseline:summary(normal),
      baselineSquaredNorm:normal.squaredNorm,squaredNorm:result.squaredNorm,lambda:result.lambda,nextLambda:result.nextLambda,
      alpha:result.alpha??null,evaluation:result.evaluation??null,trace:result.trace,solveInfo:result.solveInfo??result.lastSolveInfo,
      actualValueEvaluations:result.actualValueEvaluations,normalSeconds,elapsedSeconds:(Date.now()-begin)/1000};
    if(result.accepted){z=Array.from(result.z);lambda=result.nextLambda;accepted++;}
    history.push(record);latest=checkpoint(record);
    if(options.onStep)await options.onStep(latest,record);
    releaseTemporarySlices();
    if(!result.accepted)break;
  }
  return latest;
}
module.exports={run};
if(require.main===module) {
  const fs=require("node:fs"),path=require("node:path");
  const [candidateFile,inputFile,prefix,deltaText,countText="3"]=process.argv.slice(2);
  if(!candidateFile||!inputFile||!prefix||deltaText===undefined||fs.existsSync(prefix+"-final.json"))throw Error("candidate input fresh-prefix Delta [count] required");
  const write=(p,o)=>{fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,JSON.stringify(o,null,2)+"\n");};
  run(JSON.parse(fs.readFileSync(candidateFile)),JSON.parse(fs.readFileSync(inputFile)),Number(deltaText),Number(countText),
    {onStep:(s,r)=>{write(prefix+"-step-"+r.iteration+".json",s);process.stdout.write(JSON.stringify({iteration:r.iteration,
      accepted:r.accepted,R2:r.squaredNorm,metric:r.evaluation?.maxRelativeMetric,curvature:r.evaluation?.curvature?.maxCurvature,
      width:r.evaluation?.geometry?.maxAbsoluteY,held:r.evaluation?.geometry?.minHeldDistance,alpha:r.alpha,seconds:r.elapsedSeconds})+"\n");}})
    .then(s=>write(prefix+"-final.json",s)).catch(e=>{process.stderr.write(String(e.stack||e)+"\n");process.exitCode=1;});
}
