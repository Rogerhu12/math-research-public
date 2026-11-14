/* R211: fixed tau=2 quartic amplification of the complete R191 spectral hinge.
 * This is an explicitly new finite objective. Original curvature, variation,
 * eigenvalue branches and exact-threshold generalized derivative are retained.
 */
"use strict";
function createR211AmplifiedCurvatureAlgebra(original,options={}){
  if(!original||["curvature","variation","hinge"].some(k=>typeof original[k]!=="function"))
    throw Error("The original complete R191 algebra is required");
  if(options.tau!==undefined&&options.tau!==2)
    throw Error("This R211 definition fixes tau=2; a different tau is a new definition");
  const tau=2,tauSquared=4;
  const definition=Object.freeze({
    schema:"fd2d-R211-fixed-tau-quartic-spectral-hinge-v1",tau,tauSquared,
    originalAlgebraSource:"scripts/fd2d-position-curvature-chain-R191.cjs",
    originalAlgebraSHA256:"d30e2fe21ca065a84776313d8ababba2a8eccc6693e5f60a5c7ba3628652d812",
    inputResidual:"Original unweighted (Q11,sqrt(2)*Q12,Q22), Q=S-clip(S,[-guide,guide])",
    q:"dot(originalResidual,originalResidual)",
    scale:"sqrt(1+q/4)",
    residual:"originalResidual*sqrt(1+q/4)",
    squaredObjective:"q+q*q/4, per actual curvature point before the original quadrature weight",
    derivative:"h*Dr + r*(dot(r,Dr)/(4*h))",
    unchanged:["actual Gram/normal/orthonormal II","complete curvature variation","original spectral branches","eigenvalues","guide","exact-threshold inactive slope convention","original external weights and sample points"],
    zeroSetUnchanged:true,finiteObjectiveChanged:true,allStateColumnsPreservedByComposition:true,
    hiddenShiftOrResidualClipping:false,continuousReachOrCurvatureCertificate:false
  });
  function hinge(S,guide){
    const old=original.hinge(S,guide),r=old.residual,q=old.squared;
    if(!r||r.length!==3||r.some(x=>!Number.isFinite(x))||!(Number.isFinite(q)&&q>=0))
      throw Error("Nonfinite original R191 hinge");
    const h=Math.sqrt(1+q/tauSquared),residual=r.map(x=>h*x);
    const squared=q+q*q/tauSquared;
    if(!Number.isFinite(h)||!Number.isFinite(squared)||residual.some(x=>!Number.isFinite(x)))
      throw Error("R211 amplified residual or objective overflow");
    function apply(H){
      const d=old.apply(H);
      if(!d||d.length!==3||d.some(x=>!Number.isFinite(x)))
        throw Error("Nonfinite original R191 hinge variation");
      const projection=(r[0]*d[0]+r[1]*d[1]+r[2]*d[2])/(tauSquared*h);
      const out=d.map((x,k)=>h*x+r[k]*projection);
      if(out.some(x=>!Number.isFinite(x)))throw Error("R211 amplified variation overflow");
      return out;
    }
    return {...old,residual,squared,apply,
      originalResidual:Array.from(r),originalSquared:q,amplification:h,
      residualObjectiveDefinition:definition.schema};
  }
  return {curvature:original.curvature,variation:original.variation,hinge,definition};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR211AmplifiedCurvatureAlgebra};
