// R108 optional warm predictor, not a shooting solve or a new acceptance rule.
// Use the same full solution tangent as R92, then the existing centered R95
// Q/L retraction. No active worker or engine is modified by importing this file.
import {performance} from 'node:perf_hooks';
import {createPhysicalHeightTangentPredictor as createCanonicalTangent}
 from './78718-tail-tangent-predictor-with-direction.mjs';
import {prepareGeometricShootingRetraction}
 from './78718-tail-geometric-newton-retraction-centered-v3.mjs';

export function createPhysicalHeightTangentPredictor(solution,farGraph,radius,{cells,spacing}={}){
 const base=solution.states.map(row=>Float64Array.from(row)),
  M=base[0].length/2,K=2*M,L=base.length-1;
 if(!Array.isArray(cells)||cells.length!==L||!Number.isInteger(spacing)||spacing<=0)
  throw Error('Geometric tangent warm requires its own complete cells and spacing');
 const linear=createCanonicalTangent({...solution,states:base},Float64Array.from(farGraph),radius);
 const statistics={predictions:0,geometricPreparations:0,exactZeroSteps:0,unchangedCutTargets:0};
 const clone=()=>base.map(row=>Array.from(row));
 function validateHeight(height){
  if(height.length!==M||Array.from(height).some(v=>!Number.isFinite(v)))throw Error('Invalid target height');
 }
 function identityResult(lambda,reason){
  return {states:clone(),diagnostics:{
   kind:'full-shooting-geometric-tangent-warm-v1',modes:M,stages:L,lambda,
   maxChartCondition:linear.maxChartCondition,maxRelativeCorrection:0,
   geometricPreparations:0,exactBaseIdentity:true,identityReason:reason,
   scope:'Warm state only; the original nonlinear solve and branch checks still run.',
  }};
 }
 return {
  maxChartCondition:linear.maxChartCondition,
  statistics,
  predict(height,{lambda=1}={}){
   statistics.predictions++;
   validateHeight(height);
   if(!Number.isFinite(lambda))throw Error('Geometric tangent step is not finite');
   if(lambda===0){statistics.exactZeroSteps++;return identityResult(lambda,'zero homotopy step');}
   const began=performance.now(),canonical=linear.predict(height),delta=canonical.direction;
   const sameCutTarget=canonical.states[0].slice(0,M).every((v,j)=>Object.is(v,base[0][j]));
   const zeroDirection=delta.every(row=>Array.from(row).every(v=>v===0));
   if(sameCutTarget&&zeroDirection){
    statistics.unchangedCutTargets++;
    return identityResult(lambda,'identical binary cut target and zero full tangent');
   }
   // This existing routine owns all node/profile choices, including node0's
   // engine momentum conversion by its actual portRatio. It solves the same
   // full mean equation with the old mean plus its own directional derivative.
   const prepared=prepareGeometricShootingRetraction(base,delta,cells,{spacing});
   statistics.geometricPreparations++;
   const states=prepared.step(lambda);
   let maximumFarPiProjection=0,maximumCutAssignment=0;
   // The original far condition is affine. Keep the base far defect instead
   // of adding the retraction's quadratic boundary drift. This is a warm
   // projection only; it is checked again by the original complete residual.
   for(let j=0;j<M;j++){
    const k=M+j;
    const value=delta[L][k]===0?base[L][k]:
     lambda===1?canonical.states[L][k]:base[L][k]+lambda*delta[L][k];
    maximumFarPiProjection=Math.max(maximumFarPiProjection,Math.abs(states[L][k]-value));
    states[L][k]=value;
   }
   // For the requested endpoint, preserve the same directly divided binary
   // height/radius^4 values as R92, including all high-mode Dirichlet entries.
   // At other lambda, Q follows the interpolated canonical boundary; lambda=0
   // has already returned the original bytes without any root or roundtrip.
   if(lambda===1)for(let j=0;j<M;j++){
    maximumCutAssignment=Math.max(maximumCutAssignment,Math.abs(states[0][j]-canonical.states[0][j]));
    states[0][j]=canonical.states[0][j];
   }
   let maximumGeometricDifference=0,maximumRelativeGeometricDifference=0;
   for(let n=0;n<=L;n++){
    const scale=Math.max(1e-250,...Array.from(base[n],Math.abs));
    if(states[n].length!==K)throw Error('Geometric tangent state dimension changed');
    for(let j=0;j<K;j++){
     if(!Number.isFinite(states[n][j]))throw Error('Nonfinite geometric tangent warm state');
     const linearValue=delta[n][j]===0?base[n][j]:
      lambda===1?canonical.states[n][j]:base[n][j]+lambda*delta[n][j];
     const difference=Math.abs(states[n][j]-linearValue);
     maximumGeometricDifference=Math.max(maximumGeometricDifference,difference);
     maximumRelativeGeometricDifference=Math.max(maximumRelativeGeometricDifference,difference/scale);
    }
   }
   return {states,diagnostics:{
    ...canonical.diagnostics,
    kind:'full-shooting-geometric-tangent-warm-v1',lambda,
    directionSource:'R92 stored full flow Jacobians; original delta before state addition',
    retractionMethod:prepared.diagnostics.method,
    meanInitialization:'base full mean plus lambda times its exact directional derivative',
    cutBoundary:lambda===1?'direct binary height/radius^4':'canonical interpolated boundary',
    farBoundary:'original base affine Robin defect retained in real arithmetic; floating linear rounding remains',
    maxRelativeCorrection:Math.abs(lambda)*canonical.diagnostics.maxRelativeCorrection,
    maximumGeometricDifference,maximumRelativeGeometricDifference,
    maximumFarPiProjection,maximumCutAssignment,
    baseMinimumPreparationA:prepared.diagnostics.minPreparationA,
    baseMinimumPreparationD:prepared.diagnostics.minPreparationD,
    geometricPreparations:1,exactBaseIdentity:false,
    constructionMilliseconds:performance.now()-began,
    actualStageFlows:0,actualShootingSolves:0,
    scope:'Initial guess only. No smaller residual or larger positivity margin is asserted; the original root, all nonlinear flows, boundaries, and acceptance remain authoritative.',
   }};
  },
 };
}
