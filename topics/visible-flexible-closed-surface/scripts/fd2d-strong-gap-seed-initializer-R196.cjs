/* Explicit finite strong-gap initialization from a saved R196 nonuniform
 * small-gap state. Only the central seed changes initially; all actual
 * parameter coefficients and exact knots are copied. This is a new field.
 */
"use strict";
function initializeR196StrongGap(runtime,smallState,bindings){
  const c={
    schema:"fd2d-R196-strong-gap-nonuniform-design-checkpoint-v1",bindings,
    options:{...smallState.options,gap:.8,radialKnots:smallState.options.radialKnots.map(x=>Array.from(x))},
    curvatureOptions:{...smallState.curvatureOptions},z:Array.from(smallState.z),lambda:.01,
    parentAcceptedIteration:smallState.localAcceptedSteps,localAcceptedSteps:0,history:[],
    parentLastFiniteEvaluation:smallState.lastEvaluation,
    seedChange:{oldGap:smallState.options.gap,newRequestedGap:.8,
      coefficientsCopiedIdentically:true,radialKnotsCopiedExactly:true,
      oldFieldOrOldAcceptedValueClaimed:false,
      initialDamping:.01,allLaterTrialsUseFrozenR195ArmijoPolicy:true},
    completePhysicalMetricFixedDuringDesign:false,continuousCertificate:false,strongTargetComplete:false,
    execution:{runtime:"pure JavaScript/V8",OS_subprocess_started:false,OS_exit_code:null}
  };
  const p=runtime.providers(c),cv=p.curvature.curve,base=p.curvature.base,md=p.metric.definition;
  function bits(x){const d=new DataView(new ArrayBuffer(8));d.setFloat64(0,x,false);return d.getUint32(0,false).toString(16).padStart(8,"0")+d.getUint32(4,false).toString(16).padStart(8,"0");}
  c.centralSeed={schema:"fd2d-complete-material-ellipse-numeric-seed-identity-v1",
    rawA:cv.A,rawB:cv.B,rawArcA0:cv.a0,rawQuarter:cv.quarter,
    baseA0:base.a0,normalization:base.a0/cv.a0,
    actualCentralA:md.centralA,actualCentralB:md.centralB,actualCentralGap:md.centralGap,
    binary64:{rawA:bits(cv.A),rawB:bits(cv.B),rawArcA0:bits(cv.a0),rawQuarter:bits(cv.quarter),
      baseA0:bits(base.a0),normalization:bits(base.a0/cv.a0),actualCentralA:bits(md.centralA),actualCentralB:bits(md.centralB),actualCentralGap:bits(md.centralGap)},
    normalizationSemantics:"same R187 material ellipse definition: Xcentral=baseA0*gammaRaw/rawArcA0; accurate-target errors remain explicit",
    accurateEllipticIntegralOrInverseCertificate:false};
  c.providerDefinition=p.curvature.definition;c.backendDefinition=p.lm.backendDefinition;
  const start=Date.now();
  try{const v=p.curvature.value(c.z);c.newQuadratureBaseline=v;c.lastEvaluation=v;c.status="new_gap_actual_fresh_baseline";}
  catch(e){c.newQuadratureBaseline=null;c.lastEvaluation=null;c.status="new_gap_actual_baseline_domain_rejected";c.baselineError={name:String(e.name||"Error"),message:String(e.message||e)};}
  c.baselineMilliseconds=Date.now()-start;c.execution.completed=true;
  return c;
}
if(typeof module!=="undefined"&&module.exports)module.exports={initializeR196StrongGap};
