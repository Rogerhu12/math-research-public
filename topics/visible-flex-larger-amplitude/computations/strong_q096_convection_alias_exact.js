#!/usr/bin/env node
"use strict";
/* Exact all-phase angular alias bounds for only the fixed-q096 convective mean.
   Uses the saved reference chart, not an actual M28 field or floating table. */
const ENGINE_SHA="ac4a3e419e064c23a2eb42a1cb626507866d5e74e0ef608313fb887f8dbfcb80";
function buildConvectionAlias(Q,hash){
 const O=Q(1),Z=Q(0);
 function assert(ok,message){if(!ok)throw Error(message);}
 function power(x,n){let z=O;for(;n;n=Math.floor(n/2),x=x.mul(x))if(n%2)z=z.mul(x);return z;}
 function dyadic(n){return n>=0?Q(1n<<BigInt(n)):O.div(Q(1n<<BigInt(-n)));}
 function cap(q){
  assert(q.cmp(Z)>0,"strict positive cap input");
  let k=q.d.toString(2).length-q.n.toString(2).length;
  while(q.cmp(dyadic(-k))>=0)k--;
  while(q.cmp(dyadic(-(k+1)))<0)k++;
  const bits=k+96;assert(bits>0,"relative dyadic precision");
  const scale=1n<<BigInt(bits),ceil=(q.n*scale+q.d-1n)/q.d,out=Q(ceil).div(Q(scale));
  assert(out.cmp(q)>=0&&out.cmp(dyadic(-k))<0,"outward upper cap failed");
  return {exact_upper:out.toString(),strict_power_two_upper_exponent:-k,
   exact_unrounded_sha256:hash(q.toString()),outward_rounding_verified:true,
   decimal_display:Number(out.n)/Number(out.d)};
 }
 function run(){
  const c2=Q("3242591731706757/36028797018963968"),
   c4=Q("-7337147526749689/1152921504606846976"),
   L=Q("7092420367637499/2251799813685248"),q=c2;
  const d2=c2.mul(-3),d4=c4.mul(-15),r=d2.abs().add(d4.abs()),
   A=d2.abs().div(2).add(d4.abs().div(4)),gap=O.sub(r);
  const bs=Q(15).div(L.mul(8)),bss=Q(6).div(L.mul(L));
  const M=28,counts=[768,1024,1168,1360,1536],checks={};
  function check(name,ok){checks[name]=!!ok;assert(ok,name);}
  check("exact_saved_chart_inputs",c2.cmp(Z)>0&&c4.cmp(Z)<0&&L.cmp(Z)>0);
  check("uniform_geometric_domain",r.cmp(Z)>0&&r.cmp(O)<0);
  check("all_original_angular_counts_even_and_above_field_support",counts.every(N=>N%2===0&&N>2*M+4));
  const rows=counts.map(N=>{
   const K=Math.floor((N-1-(2*M+4))/4),n=K+1,maxRetained=2*M+4+4*K;
   assert(maxRetained<N&&2*M+4+4*n>=N,"sharp support cutoff wrong");
   const rn=power(r,n);
   const E=Q(2).mul(A).mul(rn).div(gap);
   const Eb=Q(2).mul(A).mul(rn).mul(Q(n).div(gap).add(r.div(gap.mul(gap))));
   const w1=q.abs().mul(bs).mul(E),
    w2=q.abs().mul(bss.mul(E).add(bs.mul(bs).mul(Eb)));
   // Independent exact geometric-tail derivative identity.
   const equivalent=E.mul(Q(n).add(r.div(gap)));
   assert(Eb.eq(equivalent),"derivative tail identity");
   return {angular:N,all_modes_covered:M,physical_frequencies:"2,4,...,56",
    retained_geometric_powers:[0,K],first_discarded_power:n,maximum_retained_physical_frequency:maxRetained,
    max_retained_strictly_below_grid_count:maxRetained<N,
    Cj_average_alias_abs:cap(E),Cj_b_derivative_alias_abs:cap(Eb),
    m_alias_per_normalized_weighted_state_l1:cap(w1),
    mprime_alias_per_normalized_weighted_state_l1:cap(w2),
    mprime_alias_per_normalized_weighted_state_derivative_l1:cap(w1)};
  });
  check("all_five_exact_support_cutoffs",rows.every(x=>x.max_retained_strictly_below_grid_count));
  check("all_28_modes_uniformly_covered",rows.every(x=>x.all_modes_covered===28));
  check("all_derivative_geometric_tails_exact",rows.length===5);
  check("all_caps_outward",rows.every(x=>[x.Cj_average_alias_abs,x.Cj_b_derivative_alias_abs,
   x.m_alias_per_normalized_weighted_state_l1,x.mprime_alias_per_normalized_weighted_state_l1,
   x.mprime_alias_per_normalized_weighted_state_derivative_l1].every(c=>c.outward_rounding_verified)));
  check("all_768_and_finer_mean_coefficients_below_2_to_minus_250",
   rows.every(x=>Q(x.m_alias_per_normalized_weighted_state_l1.exact_upper).cmp(dyadic(-250))<0&&
    Q(x.mprime_alias_per_normalized_weighted_state_l1.exact_upper).cmp(dyadic(-250))<0));
  return {
   schema:"strong-q096-convection-angular-alias-v1",
   scope:"Only the exact fixed-chart convective contribution; field norms, normal velocity and original floating angular evaluation remain external.",
   exact_chart:{c2:c2.toString(),c4:c4.toString(),gauge_q:q.toString(),physical_length:L.toString(),
    d2:d2.toString(),d4:d4.toString(),B_sup_upper:r.toString(),A_sup_upper:A.toString(),
    bs_abs_upper:bs.toString(),bss_abs_upper:bss.toString(),
    prior_chart_certificate_sha256:"da4709e9bfdc6330e440c8a69a556ddd760ffd364bb05fa45a4caf28eff4e618",
    prior_convection_certificate_sha256:"7a58d73cd20c45f790e5c930b5136fc87470267cd3c14088be557fe2f9d86e02"},
   all_checks_passed:Object.values(checks).every(Boolean),check_count:Object.keys(checks).length,checks,rows,
   weighted_state_norm:"T=sum_{j=1}^28 (2j)*sup_s |Y_j(s)|; T1=sum_{j=1}^28 (2j)*sup_s |Y'_j(s)|. Y is the original normalized vertical state; q is already included in reported weights.",
   error_formula:"|m_conv,N-m_conv|<=w1*T; |mprime_conv,N-mprime_conv|<=w2*T+w1*T1.",
   uniformity:"All b in [0,1], all represented modes 1..28, and every uniform angular-grid phase offset independent of s.",
   exactness_argument:"A*sin(2j psi)*B^k has maximum physical frequency 2j+4+4k<N, so its continuous mean equals its N-point uniform mean at every phase offset. Bound the two positive means of the remaining geometric tail by twice its supremum; differentiate the same absolutely convergent series for the b derivative.",
   no_original_source_changes:true,MJS_modified:false,physical_RHS_calls:0,Node_workers:0,newton_solves:0,
   actual_M24_or_M28_field_loaded:false,actual_NumPy_or_trigonometric_evaluation_paid:false,
   normal_velocity_mean_alias_paid:false,actual_full_mean_certificate:false,
   separate_obligations:["Actual complete weighted vertical-state norms and their radial derivatives.",
    "Nonlinear normal-velocity angular quadrature, all profile/chart floating evaluation and actual sampled-sum roundoff.",
    "Separate errors for different coarse/fine N or original radial quadrature meshes.",
    "Complete tail/audit, exact background/nonmean seams, PDE, closed family and reach."]
  };
 }
 return {run};
}
if(typeof module!=="undefined")module.exports={buildConvectionAlias};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
 const k=process.argv.indexOf("--out");if(k<0||!process.argv[k+1])throw Error("--out required");
 const out=process.argv[k+1];if(fs.existsSync(out))throw Error("fresh --out required");
 const helper=path.join(__dirname,"strong_exact_rational_fast.js"),hash=s=>crypto.createHash("sha256").update(s).digest("hex");
 if(hash(fs.readFileSync(helper))!==ENGINE_SHA)throw Error("rational helper differs");
 const {Q}=require(helper),result=buildConvectionAlias(Q,hash).run();
 result.executed_source_sha256=hash(fs.readFileSync(__filename));result.rational_helper_sha256=ENGINE_SHA;
 fs.writeFileSync(out,JSON.stringify(result,null,2)+"\n",{flag:"wx"});
 process.stdout.write(JSON.stringify({checks:result.check_count,all_passed:result.all_checks_passed})+"\n");
}
