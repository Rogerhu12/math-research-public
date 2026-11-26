"use strict";
/* Text recovered after executor loss on 2026-11-26. New source identity.
 * Same complete R211 finite formula; both independent cache families bounded. */
function createMemoryBoundR211RunProvider(candidate,input){
  const engine=require("./fd2d-direct-position-tangent-lift-baseline-R187.cjs").createR187();
  const splines=require("./fd2d-cubic-spline-refinement-R196.cjs").createR196CubicSplines();
  const metric=require("./fd2d-nonuniform-metric-provider-R196.cjs").createR196MetricProvider(engine,candidate,input.options,splines);
  const originalAlgebra=require("./fd2d-position-curvature-chain-R191.cjs").createR191Algebra();
  const algebra=require("./fd2d-curvature-quartic-hinge-R211.cjs").createR211AmplifiedCurvatureAlgebra(originalAlgebra,{tau:2});
  const references=A=>require("./fd2d-bent-annulus-reference-R205.cjs").createR205BentAnnulusReference(engine,metric.base,{amplitude:A,angles:input.options.angles,cacheLimit:512});
  const position=require("./fd2d-R201-R205-variable-amplitude-lazy-curvature.cjs").createR201R205AmplitudeProvider(engine,metric,references,{...input.curvatureOptions,sliceReuse:{valueLimit:0,derivativeLimit:0}},algebra);
  position.definition={...position.definition,curvaturePenaltyModel:algebra.definition,completeSquaredPenaltyEqualsSumPrincipalCurvatureHingesSquared:false,
    baseProvider:{...position.definition.baseProvider,curvaturePenaltyModel:algebra.definition,completeSquaredPenaltyEqualsSumPrincipalCurvatureHingesSquared:false}};
  if(input.z.length!==position.dimension)throw Error("Complete state dimension mismatch");
  if(input.centralSeed&&(input.centralSeed.rawA!==metric.curve.A||input.centralSeed.rawB!==metric.curve.B))throw Error("Saved central seed changed");
  return {engine,metric,position};
}
module.exports={createMemoryBoundR211RunProvider};

