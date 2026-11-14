/* R196: a separate all-zero coefficient strong-gap baseline.
 * This is not an accepted step from the earlier warm branch.
 */
"use strict";
function initializeR196ZeroStrong(runtime,warmBaseline,warmAccepted,bindings){
  const c={schema:"fd2d-R196-zero-coefficients-strong-gap-design-checkpoint-v1",bindings,
    options:JSON.parse(JSON.stringify(warmBaseline.options)),curvatureOptions:{...warmBaseline.curvatureOptions},
    z:Array(warmBaseline.z.length).fill(0),lambda:.01,parentAcceptedIteration:0,localAcceptedSteps:0,history:[],
    seedChange:{kind:"all theta/phi/height/cut-height/radius coefficients exactly zero",
      centralGap:.8,fieldIsOriginalCompleteR187StrongSeed:true,originalB32RadiusAtInitialization:true,
      zeroBaselineCountedAsAcceptedStep:false,comparisonDoesNotTransferOldAcceptance:true},
    parentLastFiniteEvaluation:warmAccepted.lastEvaluation,
    warmComparison:{initial:warmBaseline.lastEvaluation,afterTwoActualAcceptedSteps:warmAccepted.lastEvaluation},
    completePhysicalMetricFixedDuringDesign:false,continuousCertificate:false,strongTargetComplete:false,
    execution:{runtime:"pure JavaScript/V8",OS_subprocess_started:false,OS_exit_code:null}};
  const p=runtime.providers(c),cv=p.curvature.curve,b=p.curvature.base,md=p.metric.definition;
  if(cv.A!==warmBaseline.centralSeed.rawA||cv.B!==warmBaseline.centralSeed.rawB||b.a0!==warmBaseline.centralSeed.baseA0)
    throw Error("zero initializer changed the already declared central seed");
  c.centralSeed=JSON.parse(JSON.stringify(warmBaseline.centralSeed));
  c.providerDefinition=p.curvature.definition;c.backendDefinition=p.lm.backendDefinition;
  const start=Date.now();
  try{const v=p.curvature.value(c.z);c.newQuadratureBaseline=v;c.lastEvaluation=v;c.status="separate_zero_coefficients_actual_fresh_baseline";}
  catch(e){c.newQuadratureBaseline=null;c.lastEvaluation=null;c.status="zero_coefficients_actual_baseline_domain_rejected";c.baselineError={name:String(e.name||"Error"),message:String(e.message||e)};}
  c.baselineMilliseconds=Date.now()-start;c.execution.completed=true;return c;
}
if(typeof module!=="undefined"&&module.exports)module.exports={initializeR196ZeroStrong};
