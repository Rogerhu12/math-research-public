"use strict";
/* R205 fixed-amplitude continuation. R203 position rows and the original R195
 * actual-value/Armijo/damping policy are retained. A is a frozen input, not a
 * silently added finite column. No accepted state is inferred from this source.
 */
function createR205FixedRunProvider(candidate,input,modules){
  const m=modules||{
    createR187:require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187,
    createR196CubicSplines:require("./fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines,
    createR191Algebra:require("./fd2d-position-curvature-chain-R191.cjs").createR191Algebra,
    createR205BentAnnulusReference:require("./fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference,
    createR205MetricProvider:require("./fd2d-direct-position-bent-annulus-metric-R205.cjs").createR205MetricProvider,
    createR205CurvatureProvider:require("./fd2d-direct-position-bent-annulus-curvature-R205.cjs").createR205CurvatureProvider,
    createR203GeometryProvider:require("./fd2d-complete-position-geometric-guide-R203.cjs").createR203GeometryProvider,
    createBandBorderLM:require("./fd2d_band_border_lm_adapter_v2_R195.cjs").createBandBorderLM,
    kernel:require("./fd2d_scaled_band_border_lm_R203.cjs")
  };
  const A=input.options?.bentAnnulus?.amplitude;
  if(!Number.isFinite(A)||A<0||A>1.2)throw Error("Explicit frozen R205 amplitude in [0,1.2] required");
  const engine=m.createR187(),core=m.createR205MetricProvider(engine,candidate,input.options,m.createR196CubicSplines(),m.createR205BentAnnulusReference),
    curvature=m.createR205CurvatureProvider(engine,core,input.guide||input.curvatureOptions,m.createR191Algebra()),
    provider=m.createR203GeometryProvider(curvature,input.geometryGuide),
    lm=m.createBandBorderLM(m.kernel,provider.definition,{halfBandwidthBlocks:4,kernelSourceSHA256:input.sourceBindings?.kernelSHA256||null});
  return {core,curvature,provider,lm,amplitude:A};
}
async function continueR205Fixed(candidate,input,count,config={},modules){
  if(!Number.isInteger(count)||count<1)throw Error("Positive number of attempted actual steps required");
  const {core,provider,lm,amplitude}=createR205FixedRunProvider(candidate,input,modules);
  let z=Array.from(input.z),lambda=input.lambda,iteration=input.iteration||0;
  const history=Array.from(input.history||[]),started=new Date().toISOString(),tick=Date.now();
  function snapshot(){
    return {...input,schema:"R205-fixed-amplitude-R203-geometry-actual-continuation-v1",z,lambda,iteration,history,
      fixedTailAmplitude:amplitude,actualFiniteCuffPlaneHeight:core.base.height+z[core.definition.stateLayout.cutHeight],
      actualFiniteOuterCutMeanHeight:core.bentReference.cutSectionMeanJets(core.base.height+z[core.definition.stateLayout.cutHeight]).value,
      execution:{runtime:config.runtime||"unspecified caller",start:started,updated:new Date().toISOString(),elapsedSeconds:(Date.now()-tick)/1000},
      physicalMetricIsDesignVariable:true,continuousCertificate:false,strongTargetComplete:false};
  }
  for(let k=0;k<count;k++){
    const t=Date.now(),normal=provider.normal(z),normalSeconds=(Date.now()-t)/1000;
    if(config.onNormal)await config.onNormal({iteration:iteration+1,normalSeconds,squaredNorm:normal.squaredNorm});
    const step=await lm.lmStep({z,normal,value:v=>provider.value(v),lambda,maxDampingAttempts:8,alphas:[1,.5,.25]});
    const record={iteration:iteration+1,accepted:step.accepted,status:step.status,baselineSquaredNorm:normal.squaredNorm,
      squaredNorm:step.squaredNorm,lambda:step.lambda,nextLambda:step.nextLambda,alpha:step.alpha??null,
      evaluation:step.evaluation??null,trace:step.trace,solveInfo:step.solveInfo??step.lastSolveInfo,
      actualValueEvaluations:step.actualValueEvaluations,normalSeconds,elapsedSeconds:(Date.now()-t)/1000};
    history.push(record);
    if(step.accepted){z=Array.from(step.z);lambda=step.nextLambda;iteration++;}
    if(config.onStep)await config.onStep(snapshot(),record);
    if(!step.accepted)break;
  }
  return snapshot();
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR205FixedRunProvider,continueR205Fixed};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
  const fs=require("node:fs"),path=require("node:path"),[inputPath,candidatePath,stem,countText="2"]=process.argv.slice(2);
  if(!inputPath||!candidatePath||!stem)throw Error("Usage: input.json candidate.json fresh-output-stem count");
  if(fs.existsSync(stem+"-report.json")||fs.existsSync(stem+"-progress.json"))throw Error("Fresh output stem required");
  const input=JSON.parse(fs.readFileSync(inputPath)),candidate=JSON.parse(fs.readFileSync(candidatePath));
  const atomic=(p,x)=>{fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p+".tmp",JSON.stringify(x,null,2)+"\n");fs.renameSync(p+".tmp",p);};
  continueR205Fixed(candidate,input,Number(countText),{runtime:"Node actual terminal child; exit requires the external receipt",onStep:(s,r)=>{
    atomic(stem+"-progress.json",s);console.log(JSON.stringify({iteration:r.iteration,accepted:r.accepted,R2:r.squaredNorm,
      metric:r.evaluation?.maxRelativeMetric,curvature:r.evaluation?.curvature?.maxCurvature,geometry:r.evaluation?.geometryPenaltySquaredNorm,cuff:s.actualFiniteCuffPlaneHeight}));
  }}).then(r=>atomic(stem+"-report.json",r)).catch(e=>{console.error(e.stack||e);process.exitCode=1;});
}
