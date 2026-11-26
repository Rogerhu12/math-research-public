"use strict";
/* Explicit new startup/continuation objective. R211 remains fixed at tau=2.
 * All original R191 spectral branches and complete geometric variations stay
 * intact; only this declared positive scalar amplification changes.
 */
function createExplicitTauCurvatureAlgebra(original,options){
  if(!original||["curvature","variation","hinge"].some(k=>typeof original[k]!=="function"))
    throw Error("The complete original R191 algebra is required");
  const tau=options?.tau,tauSquared=tau*tau;
  if(!(Number.isFinite(tau)&&tau>0&&Number.isFinite(tauSquared)&&tauSquared>0))
    throw Error("An explicit finite positive curvature tau is required");
  const definition=Object.freeze({schema:"6a65-explicit-tau-quartic-curvature-hinge-v1",tau,tauSquared,
    ancestry:"R191 spectral hinge and the R211 chain formula; this is not fixed-tau R211",
    inputResidual:"Original complete (Q11,sqrt(2)*Q12,Q22), Q=S-clip(S,[-guide,guide])",
    q:"dot(originalResidual,originalResidual)",scale:"sqrt(1+q/tau^2)",
    residual:"originalResidual*sqrt(1+q/tau^2)",squaredObjective:"q+q*q/tau^2",
    derivative:"h*Dr+r*(dot(r,Dr)/(tau^2*h))",
    actualGramAndCurvatureUnchanged:true,externalWeightsAndAllColumnsUnchanged:true,
    zeroSetUnchanged:true,finiteObjectiveExplicitlyChanged:true,
    noResidualClipping:true,continuousCertificate:false});
  function hinge(S,guide){
    const old=original.hinge(S,guide),r=old.residual,q=old.squared;
    if(!r||r.length!==3||r.some(v=>!Number.isFinite(v))||!(Number.isFinite(q)&&q>=0))throw Error("Invalid original hinge");
    const h=Math.sqrt(1+q/tauSquared),residual=r.map(v=>h*v),squared=q+q*q/tauSquared;
    if(!Number.isFinite(squared)||residual.some(v=>!Number.isFinite(v)))throw Error("Explicit curvature objective overflow");
    function apply(H){
      const d=old.apply(H),projection=(r[0]*d[0]+r[1]*d[1]+r[2]*d[2])/(tauSquared*h);
      const out=d.map((v,k)=>h*v+r[k]*projection);
      if(out.some(v=>!Number.isFinite(v)))throw Error("Explicit curvature derivative overflow");
      return out;
    }
    return {...old,residual,squared,apply,originalResidual:Array.from(r),originalSquared:q,
      amplification:h,residualObjectiveDefinition:definition.schema};
  }
  return {curvature:original.curvature,variation:original.variation,hinge,definition};
}
module.exports={createExplicitTauCurvatureAlgebra};
