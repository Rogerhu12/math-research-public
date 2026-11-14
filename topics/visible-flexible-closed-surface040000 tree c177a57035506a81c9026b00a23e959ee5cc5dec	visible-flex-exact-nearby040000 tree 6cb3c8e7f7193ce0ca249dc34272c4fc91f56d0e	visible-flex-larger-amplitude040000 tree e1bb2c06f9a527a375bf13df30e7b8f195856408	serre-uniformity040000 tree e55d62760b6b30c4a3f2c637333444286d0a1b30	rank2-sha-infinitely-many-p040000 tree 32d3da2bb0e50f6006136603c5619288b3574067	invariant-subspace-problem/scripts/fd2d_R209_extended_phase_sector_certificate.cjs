"use strict";
/*
 R209 extension only: the original unit budget and seed certificate are unchanged.
 The exact BigInt coefficient audit is independent of F/J/LM and is not a new gate.
*/
function createR209ExtendedPhaseSectorCertificate(base){
  if(!base && typeof require==="function")
    base=require("./fd2d_R201_strong_phase_sector_certificate.cjs").createR201PhaseSectorCertificate();
  if(!base || typeof base.certifyState!=="function")throw Error("Original R209 coefficient consumer required");
  const BASE_SHA256="7b92c7a478b1a4b7f6053063cdc493e1cef62e5bb808b9a6487c73f130f39f00";
  const abs=x=>x<0n?-x:x;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;}
  function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("Zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
  const R=x=>Array.isArray(x)&&x.length===2?F(x[0],x[1]):(()=>{throw Error("Exact pair required");})();
  const add=(x,y)=>F(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
  const sub=(x,y)=>F(x[0]*y[1]-y[0]*x[1],x[1]*y[1]);
  const mul=(x,y)=>F(x[0]*y[0],x[1]*y[1]);
  const div=(x,y)=>F(x[0]*y[1],x[1]*y[0]);
  const cmp=(x,y)=>{const n=x[0]*y[1]-y[0]*x[1];return n<0n?-1:n>0n?1:0;};
  const out=x=>({exact:x.map(String),display:Number(x[0])/Number(x[1])});
  function cosineLowerSixth(x){
    if(cmp(x,F(0))<0||cmp(x,F(3,2))>0)throw Error("The elementary cosine proof uses 0<=sector<=3/2<pi/2");
    const x2=mul(x,x),x4=mul(x2,x2),x6=mul(x4,x2);
    return sub(add(sub(F(1),div(x2,F(2))),div(x4,F(24))),div(x6,F(720)));
  }
  function certifyState(parameters,layout,seed,options={}){
    const {budgetLimit=["17","16"],cosineFloor=["1","10"],stateIdentity,basisDefinition}=options;
    const limit=R(budgetLimit),floor=R(cosineFloor);
    if(cmp(limit,F(0))<0||cmp(floor,F(0))<=0)throw Error("Positive sufficient-sector data required");
    const sector=add(F(2,5),limit),cosineLower=cosineLowerSixth(sector);
    if(cmp(cosineLower,floor)<=0)throw Error("Requested cosine floor is not certified by the exact polynomial");
    const old=base.certifyState(parameters,layout,seed,{stateIdentity,basisDefinition});
    const budget=R(old.amplitude_plus_maximum_control_L1.exact),slack=sub(limit,budget);
    const passed=cmp(slack,F(0))>=0;
    return{
      schema:"fd2d-R209-extended-continuous-phase-sector-state-v1",passed,
      original_consumer_sha256:BASE_SHA256,original_unit_budget_passed:old.passed,
      state_identity:stateIdentity,layout,basis_definition:basisDefinition,
      seed_checkpoint_sha256:old.seed_certificate_input,seed_row_checks_sha256:old.seed_row_checks_sha256,
      amplitude:old.amplitude,maximum_phase_control_L1:old.maximum_phase_control_L1,
      maximizing_radial_block:old.maximizing_radial_block,
      amplitude_plus_maximum_control_L1:old.amplitude_plus_maximum_control_L1,
      exact_remaining_extended_budget:out(slack),declared_budget_limit:out(limit),
      actual_complete_phase_absolute_upper:old.complete_phase_absolute_upper,
      declared_phase_absolute_upper:out(sector),exact_cosine_polynomial_lower:out(cosineLower),
      cosine_floor:out(floor),
      continuous_conclusions:passed?{
        whole_radial_interval:true,whole_material_circle:true,
        Re_half_integral_strict_lower:out(mul(F(3),floor)),
        modulus_half_integral_strict_lower:out(mul(F(3),floor)),
        phase_branch:"The right half-plane; exact beta and normalized phase have the original complete C2 chain.",
        reason:"R209 seed |psi_seed|<2/5, tail <=A, complete nonnegative spline bound <=M, exact cos bound, pi>3."
      }:null,
      row_bounds:old.row_bounds,
      no_inverse_cell_recomputed:true,no_new_phase_quadrature:true,no_candidate_F_J_or_optimization:true,
      not_a_necessary_domain_or_solver_gate:true,no_whole_metric_curvature_reach_certificate:true
    };
  }
  function consumeSplineRoundoff(prolongation){
    if(prolongation.schema!=="fd2d-R201-R205-complete-radial-prolongation-v1")
      throw Error("Explicit R208 full-half prolongation schema required");
    const K=prolongation.angularModes, e=prolongation.storedSplineRoundoffBounds;
    if(!Number.isInteger(K)||K<1||!e||e.value_per_channel.length!==4*K+3)
      throw Error("All actual channel value roundoff bounds required");
    if(!prolongation.exactRealAllChannelFieldPreserved||
       !prolongation.globalCutAndAmplitudeCopiedByObjectIs)
      throw Error("Same exact field and unchanged global amplitude required");
    const channels=[];for(let k=0;k<K;k++)channels.push(K+k);
    for(let k=0;k<K;k++)channels.push(3*K+3+k);
    let eps=F(0);
    for(const c of channels){const v=R(e.value_per_channel[c]);if(cmp(v,F(0))<0)throw Error("Negative error bound");eps=add(eps,v);}
    return{
      schema:"fd2d-R209-R208-phase-roundoff-consumption-v1",
      phase_channel_indices:channels,phase_function_error_upper:out(eps),
      unchanged_amplitude:true,exact_real_same_field:true,
      bound_kind:"Sum of the supplied global per-channel value bounds; this is a function error, not a sampled twojet difference.",
      basis_numerical_evaluation_error_included:prolongation.basisNumericalEvaluationErrorIncluded,
      formula:"|psi_stored_refined-psi_exact_prolongation| <= sum of actual psi sine/cosine value_per_channel bounds.",
      additional_application:"A parent sector gamma stays below a declared larger sector when the exact error is at most the available parent sector slack.",
      interval_or_error_source_recomputed:false
    };
  }
  return{certifyState,consumeSplineRoundoff,cosineLowerSixth};
}
if(typeof module!=="undefined"&&module.exports)module.exports={createR209ExtendedPhaseSectorCertificate};
