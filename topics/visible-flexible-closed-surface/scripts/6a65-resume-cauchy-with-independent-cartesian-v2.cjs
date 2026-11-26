"use strict";
/* Recovered source003 entry: a real same-objective Cauchy attempt followed,
 * only at the stage's actual observer, by an independently labelled model.
 * No Cauchy coefficient layout or curvature tau is changed here. */
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const branch=require("./6a65-cauchy-global-position.cjs");
const old=require("./6a65-run-cauchy-same-job-recovered-v2.cjs");
const SCHEMA="6a65-independent-Cartesian-after-actual-Cauchy-observer-v1";
const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const emit=x=>process.stdout.write(JSON.stringify(x)+"\n");
function fresh(p){if(fs.existsSync(p))throw Error("Fresh own output required: "+p);}
function write(p,x){fresh(p);fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,JSON.stringify(x)+"\n");}
function same(a,b){return JSON.stringify(a)===JSON.stringify(b);}
function objective(x){
  return {options:x.options,baseModel:x.baseModel,metricTau:x.metricTau,curvatureTau:x.curvatureTau,
    curvatureModel:x.curvatureModel,curvatureOptions:x.curvatureOptions,geometryOptions:x.geometryOptions};
}
function loadInput(candidateFile,inputFile){
  const candidateSHA256=hash(candidateFile),inputSHA256=hash(inputFile);
  const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile));
  old.assertState(input,candidateSHA256);
  if(input.interfaceProbeOnly===true)throw Error("An interface probe cannot enter an actual continuation");
  return {candidate,input,candidateSHA256,inputSHA256};
}
function initialize(candidateFile,inputFile,prefix,observerFile,recipeFile){
  const start=Date.now(),a=loadInput(candidateFile,inputFile),frozen=path.resolve(__dirname,"../../..");
  const recipeRepoRelative=path.relative(frozen,path.resolve(recipeFile)).split(path.sep).join("/");
  if(!/^topics\/visible-flexible-closed-surface\/ci-requests\/6a65-[A-Za-z0-9_.-]+\.json$/.test(recipeRepoRelative))
    throw Error("Explicit recipe inside the frozen topic snapshot required");
  if(fs.statSync(recipeFile).size>=100000)throw Error("Only a small reproducible recipe is allowed");
  const recipe=JSON.parse(fs.readFileSync(recipeFile));
  if(recipe.schema!=="6a65-complete-fixed-g-Cartesian-experiment-recipe-v1"||
     recipe.sourceKind!=="actual-short-Cauchy-checkpoint")throw Error("Explicit independent Cartesian recipe required");
  const observed=JSON.parse(fs.readFileSync(observerFile));
  if((observed.mathematicalObservationSchema??observed.schema)!=="6a65-Cauchy-same-field-refined-metric-observation-v1"||
     observed.inputs?.inputSHA256!==a.inputSHA256||observed.inputs?.candidateSHA256!==a.candidateSHA256||
     !["fieldCoefficientsUnchanged","physicalMetricUnchanged","sourceAngularPrimitiveUnchanged"].every(k=>observed[k]===true))
    throw Error("Actual matching original Cauchy observer required");
  const stage=path.basename(prefix).replace(/-initial$/,"");
  if(!/^[A-Za-z0-9_-]{1,50}$/.test(stage))throw Error("Explicit bounded stage label required");
  const q=branch.build(a.candidate,a.input);
  if(q.z.length!==a.input.z.length||q.z.some((v,i)=>!Object.is(v,a.input.z[i])))
    throw Error("Same-objective initializer changed the actual field");
  const value=q.provider.value(q.z);q.position.clearSliceReuse?.();if(global.gc)global.gc();
  if(!Number.isFinite(value.squaredNorm))throw Error("Actual complete baseline did not return");
  const output=prefix+"-initial.json",reportFile=prefix+"-report.json";
  fresh(output);fresh(reportFile);
  const downstream={schema:SCHEMA,sourceStageLabel:stage,recipeRepoRelative,
    recipeSHA256:hash(recipeFile),originalSourceSHA256:a.inputSHA256,
    originalObserverSHA256:hash(observerFile),cauchyObjectiveAndLayoutUnchanged:true,
    originalCauchyAcceptedStepsAtTransition:a.input.cauchyAcceptedSteps,
    independentModel:"complete-proper-half-turn-Cartesian-fixed-g",
    independentModelCountsNeverAddedToCauchy:true};
  const out={...a.input,schema:branch.INITIAL,z:Array.from(q.z),baseline:value,evaluation:value,
    accepted:false,history:[],actualDesign:q.design,providerDefinition:q.provider.definition,
    cauchyAcceptedSteps:a.input.cauchyAcceptedSteps,cauchySameObjectiveContinuationSteps:0,
    cartesianDownstream:downstream,
    source:{...a.input.source,inputSHA256:a.inputSHA256,candidateSHA256:a.candidateSHA256,
      scriptSHA256:hash(__filename)},
    execution:{actualValueBaseline:true,actualFullNormal:false,actualAcceptedSteps:0,
      seconds:(Date.now()-start)/1000,OSExitCode:null,externalExitReceiptRequired:true},
    continuousCertificate:false,strongTargetComplete:false};
  if(!same(objective(out),objective(a.input)))throw Error("Initialization changed the original objective/layout");
  write(output,out);
  write(reportFile,{schema:"6a65-same-objective-Cauchy-independent-consumer-initialization-v2",
    inputSHA256:a.inputSHA256,originalObserverSHA256:hash(observerFile),initialSHA256:hash(output),
    recipeSHA256:hash(recipeFile),scriptSHA256:hash(__filename),sourceStageLabel:stage,
    cauchyCoefficientsUnchanged:true,cauchyObjectiveAndLayoutUnchanged:true,
    inheritedActualCauchyAcceptedSteps:a.input.cauchyAcceptedSteps,newPhaseAcceptedSteps:0,
    independentCartesianAcceptedSteps:0,newCartesianExperimentExecuted:false,
    actualBaselineSquaredNorm:value.squaredNorm,continuousCertificate:false,strongTargetComplete:false});
  emit({event:"same-objective-Cauchy-initial-complete",initialSHA256:hash(output),
    cauchyAcceptedSteps:out.cauchyAcceptedSteps,phaseAcceptedSteps:0,
    R2:value.squaredNorm,metric:value.maxRelativeMetric,curvature:value.curvature?.maxCurvature});
  return out;
}
async function run(candidateFile,inputFile,prefix){
  const start=Date.now(),a=loadInput(candidateFile,inputFile),output=prefix+"-state.json";
  fresh(output);
  if(a.input.cartesianDownstream?.schema!==SCHEMA||
     !Number.isInteger(a.input.cauchySameObjectiveContinuationSteps)||
     a.input.cauchySameObjectiveContinuationSteps<0)
    throw Error("Actual own same-objective phase input required");
  const out=await old.runOne(a.candidate,a.input,{candidateSHA256:a.candidateSHA256,inputSHA256:a.inputSHA256});
  out.cauchySameObjectiveContinuationSteps=a.input.cauchySameObjectiveContinuationSteps+(out.accepted===true?1:0);
  out.cartesianDownstream={...a.input.cartesianDownstream};
  out.source={...out.source,scriptSHA256:hash(__filename),inputSHA256:a.inputSHA256};
  out.execution={actualFullNormal:true,actualAcceptedSteps:out.accepted?1:0,
    inheritedOriginalCauchyCount:a.input.cauchyAcceptedSteps,seconds:(Date.now()-start)/1000,
    OSExitCode:null,externalExitReceiptRequired:true};
  if(!same(objective(out),objective(a.input)))throw Error("The original Cauchy attempt changed its objective/layout");
  write(output,out);
  const value=out.accepted?out.evaluation:out.baseline;
  emit({event:"same-objective-Cauchy-attempt-complete",accepted:out.accepted,
    cauchyAcceptedSteps:out.cauchyAcceptedSteps,phaseAcceptedSteps:out.cauchySameObjectiveContinuationSteps,
    R2:value.squaredNorm,metric:value.maxRelativeMetric,curvature:value.curvature?.maxCurvature,
    outputSHA256:hash(output),independentCartesianExperimentExecuted:false});
  return out;
}
module.exports={initialize,run,SCHEMA};
if(require.main===module){
  const [mode,candidateFile,inputFile,prefix,observerFile,recipeFile]=process.argv.slice(2);
  if(!["init","run"].includes(mode)||!candidateFile||!inputFile||!prefix||
     mode==="init"&&(!observerFile||!recipeFile))throw Error("init candidate input prefix observer recipe | run candidate input prefix");
  Promise.resolve().then(()=>mode==="init"?initialize(candidateFile,inputFile,prefix,observerFile,recipeFile):
    run(candidateFile,inputFile,prefix)).catch(error=>{process.stderr.write(String(error.stack||error)+"\n");process.exitCode=1;});
}
