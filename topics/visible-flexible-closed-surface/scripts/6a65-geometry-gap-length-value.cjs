"use strict";
/*
 * Build one genuine new central-gap / outer-length input from an actual
 * checkpoint.  Both complete nonlinear objectives are rebuilt:
 * R211 quartic curvature (tau=2), quartic metric (tau=.05), and the complete
 * new R215 fixed-cap guide (width=.885, conservative extended-throat height).
 * No LM step is performed by this CLI.  Raw reports/states belong in scratch.
 */
function createGapLengthState(candidate,input,options={}) {
  if(!input || !Array.isArray(input.z) || !input.options)throw Error("Actual complete checkpoint required");
  const saved=input.gapLengthDesign;
  const gap=options.gap??saved?.gap??1;
  const extraLength=options.extraLength??saved?.extraLength??.05;
  const metricTau=options.metricTau??saved?.metricTau??.05;
  if(!(gap>0 && Number.isFinite(gap) && extraLength>=0 && Number.isFinite(extraLength) &&
       metricTau>0 && Number.isFinite(metricTau)))throw Error("Finite design parameters required");
  if(saved && (gap!==saved.gap || extraLength!==saved.extraLength || metricTau!==saved.metricTau))
    throw Error("Saved new-design state must keep its frozen gap, length and objective");
  if(input.outerLengthDesign && !saved)
    throw Error("First gap/length transfer requires an original-length parent; explicit old clock conversion is otherwise needed");
  const inheritedGap=input.options.gap;
  const seedInput={...input,options:{...input.options,gap}};
  const factoryOptions={lazyCurvature:true,quartic:true,referenceCacheLimit:0};
  const q=require("./6a65-geometry-outer-length-design.cjs")
    .createOuterLengthRunProvider(candidate,seedInput,extraLength,factoryOptions);
  const metricPosition=require("./6a65-quartic-metric-recovered-20261126.cjs")
    .createQuarticMetricProvider(q.position,q.engine,metricTau);
  const provider=require("./6a65-geometry-wide-cap-provider.cjs")
    .createR215WideCapGeometryProvider(metricPosition,input.geometryOptions);
  const amplitudeIndex=q.position.definition.amplitudeIndex;
  const cutHeightIndex=q.cutHeightIndex;
  if(!Number.isInteger(amplitudeIndex) || q.z.length!==provider.dimension)throw Error("Complete amplitude/state layout mismatch");
  const parentBaseHeight=saved?q.base.height:q.oldBase.height;
  const parentTrueCuffHeight=parentBaseHeight+input.z[cutHeightIndex];
  const trueCuffHeight=q.base.height+q.z[cutHeightIndex];
  const heightTransferError=trueCuffHeight-parentTrueCuffHeight;
  if(Math.abs(heightTransferError)>8*Number.EPSILON*Math.max(1,Math.abs(parentTrueCuffHeight)))
    throw Error("Physical cuff height was not preserved");
  if(q.z[amplitudeIndex]!==input.z[amplitudeIndex])throw Error("Physical bend amplitude changed during transfer");
  const central=q.metric.definition;
  const centralSeed={schema:"6a65-gap-length-central-numeric-seed-v1",
    exactPerimeterDefinition:"P(Aq,Bq)=P(7/5,1/2), Aq-Bq=gap, with material normalized arclength",
    baseA0:q.base.a0,actualCentralA:central.centralA,actualCentralB:central.centralB,
    actualCentralGap:central.centralGap,
    finiteEllipticIntegralAndInverse:true,accurateIntegralCertificate:false};
  const design={schema:"6a65-gap-length-new-input-v1",gap,extraLength,metricTau,
    curvatureQuarticTau:2,completeCapSchema:"6a65-R215-wider-core-complete-fixed-caps-v1",inheritedGap,centralSeed,
    physicalMetricChangedByLength:extraLength>0,
    centralGapAloneChangesEmbeddingSeed:true,
    allCompleteParameterChannelsRetained:true,
    amplitudeIndex,cutHeightIndex,amplitude:q.z[amplitudeIndex],
    parentTrueCuffHeight,trueCuffHeight,heightTransferError,
    trueCuffHeightPreserved:true,amplitudePreserved:true,
    outerLengthDesign:{...q.design,centralSeedUnchanged:gap===inheritedGap},
    continuousMetricOrReachCertificate:false,strongTargetComplete:false};
  return {...q,provider,metricPosition,centralSeed,design,gap,extraLength,metricTau,factoryOptions,
    geometryOptions:provider.r215GeometryOptions};
}
function evaluateGapLength(candidate,input,options={}) {
  const started=new Date().toISOString(),begin=Date.now(),q=createGapLengthState(candidate,input,options);
  const value=q.provider.value(q.z);
  q.position.clearSliceReuse?.();
  if(typeof global.gc==="function")global.gc();
  const seed={...input,schema:"6a65-gap-length-value-only-seed-v1",
    z:Array.from(q.z),options:{...input.options,gap:q.gap},geometryOptions:q.geometryOptions,
    centralSeed:q.centralSeed,inheritedCentralSeed:input.centralSeed??null,
    gapLengthDesign:q.design,outerLengthDesign:q.design.outerLengthDesign,
    outerLengthFactoryOptions:q.factoryOptions,
    providerDefinition:q.provider.definition,evaluation:value,
    newDesignAcceptedSteps:0,gapLengthAcceptedSteps:0,outerLengthAcceptedSteps:0,outerLengthHistory:[],
    inheritedParentCounters:{schema:input.schema,acceptedSteps:input.acceptedSteps??null,
      metricBranchAcceptedSteps:input.metricBranchAcceptedSteps??null,branchAcceptedSteps:input.branchAcceptedSteps??null},
    intendedCompleteMetricObjective:"quartic metric tau="+q.metricTau+" plus R211 quartic curvature tau=2 and complete new R215 cap guide",
    physicalMetricIsDesignVariable:true,continuousCertificate:false,wholeClosedReachCertified:false,strongTargetComplete:false,
    inheritedParentExecution:input.execution??null,
    execution:{runtime:"Node.js "+process.version,start:started,updated:new Date().toISOString(),
      elapsedSeconds:(Date.now()-begin)/1000,actualValueEvaluations:1,actualNormalEvaluations:0,
      actualAcceptedLMSteps:0,OSExitCode:null,exitReceiptBelongsToCallingProcess:true}};
  delete seed.acceptedSteps;
  delete seed.history;
  delete seed.metricBranchAcceptedSteps;
  delete seed.branchAcceptedSteps;
  delete seed.branchHistory;
  delete seed.accepted;
  delete seed.status;
  delete seed.baseline;
  seed.objectiveTransition={newGap:q.gap,newOuterLength:q.extraLength,newCompleteCap:"R215",
    inheritedNormalReused:false,actualNewValueEvaluations:1,actualNewNormalEvaluations:0,actualNewAcceptedSteps:0};
  return {seed,value,design:q.design,elapsedSeconds:(Date.now()-begin)/1000};
}
module.exports={createGapLengthState,evaluateGapLength};
if(require.main===module) {
  const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
  const [candidateFile,inputFile,prefix,gapText="1",deltaText=".05",tauText=".05"]=process.argv.slice(2);
  if(!candidateFile||!inputFile||!prefix)throw Error("candidate input fresh-prefix [gap=1] [Delta=.05] [metricTau=.05] required");
  const seedFile=prefix+"-seed.json",valueFile=prefix+"-value.json";
  if(fs.existsSync(seedFile)||fs.existsSync(valueFile))throw Error("Output paths must be fresh");
  const hash=p=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
  const candidate=JSON.parse(fs.readFileSync(candidateFile)),input=JSON.parse(fs.readFileSync(inputFile));
  const out=evaluateGapLength(candidate,input,{gap:Number(gapText),extraLength:Number(deltaText),metricTau:Number(tauText)});
  const source={candidate:candidateFile,candidateSHA256:hash(candidateFile),
    input:inputFile,inputSHA256:hash(inputFile),entrySHA256:hash(__filename),
    commitFromExecutionEnvironment:process.env.GITHUB_SHA??null,
    dependencies:Object.fromEntries(["6a65-geometry-outer-length-design.cjs","6a65-quartic-metric-recovered-20261126.cjs",
      "fd2d-curvature-quartic-hinge-R211.cjs","6a65-geometry-wide-cap-provider.cjs",
      "fd2d-R210-amplitude-height-allowance-geometric-guide.cjs"]
      .map(p=>[p,hash(path.join(__dirname,p))]))};
  out.seed.source=source;
  const report={schema:"6a65-gap-length-complete-value-v1",source,design:out.design,value:out.value,
    elapsedSeconds:out.elapsedSeconds,actualValueEvaluations:1,actualNormalEvaluations:0,actualAcceptedLMSteps:0,
    finiteQuadratureNotContinuousCertificate:true,strongTargetComplete:false};
  fs.mkdirSync(path.dirname(prefix),{recursive:true});
  fs.writeFileSync(seedFile,JSON.stringify(out.seed,null,2)+"\n");
  fs.writeFileSync(valueFile,JSON.stringify(report,null,2)+"\n");
  process.stdout.write(JSON.stringify({gap:out.design.gap,Delta:out.design.extraLength,
    R2:out.value.squaredNorm,metric:out.value.maxRelativeMetric,
    curvature:out.value.curvature,geometry:out.value.geometry,
    centralSeed:out.design.centralSeed,A:out.design.amplitude,Z:out.design.trueCuffHeight,
    heightTransferError:out.design.heightTransferError,seconds:out.elapsedSeconds,
    actualAcceptedLMSteps:0,seedSHA256:hash(seedFile),reportSHA256:hash(valueFile)})+"\n");
}
