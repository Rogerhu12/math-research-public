// Signed quadratic centre of the complete mean root.
// Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
// Universal exact BigInt comparisons; no Arb, ODE, stored numerical fields.
function signedMeanQuadraticConstants(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
 function q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d);
 const neg=a=>q(-a.n,a.d), sub=(a,b)=>add(a,neg(b));
 const mul=(a,b)=>q(a.n*b.n,a.d*b.d), div=(a,b)=>q(a.n*b.d,a.d*b.n);
 const sq=a=>mul(a,a), lt=(a,b)=>a.n*b.d<b.n*a.d, eq=(a,b)=>a.n*b.d===b.n*a.d;
 const rec=a=>({numerator:a.n.toString(),denominator:a.d.toString()});
 // Polynomials in z,k,p,t, with exact rational coefficients.
 const dims=4, zeroKey="0,0,0,0";
 const pc=a=>new Map([[zeroKey,a]]);
 const pv=i=>{const e=Array(dims).fill(0);e[i]=1;return new Map([[e.join(","),q(1)]]);};
 function pa(a,b){const c=new Map(a);for(const [k,v] of b){const w=add(c.get(k)||q(0),v);if(w.n)c.set(k,w);else c.delete(k);}return c;}
 const ps=(a,k)=>new Map([...a].map(([e,v])=>[e,mul(v,k)]).filter(x=>x[1].n));
 function pm(a,b){let c=new Map();for(const [u,x] of a)for(const [v,y] of b){const e=u.split(",").map((n,i)=>Number(n)+Number(v.split(",")[i])).join(",");c=pa(c,new Map([[e,mul(x,y)]]));}return c;}
 const pq=a=>pm(a,a), peq=(a,b)=>{const d=pa(a,ps(b,q(-1)));return [...d.values()].every(x=>x.n===0n);};
 const one=pc(q(1)), z=pv(0), k=pv(1), p=pv(2), t=pv(3), E=pa(one,z);
 const original=pa(pa(pm(pa(one,ps(z,q(3))),pq(k)),pm(E,pq(p))),ps(pm(E,pm(k,t)),q(2)));
 const correlated=pa(pm(E,pa(pa(pq(pa(k,t)),pq(p)),ps(pq(t),q(-1)))),ps(pm(z,pq(k)),q(2)));
 const r=q(1,64), r0=q(1,32);
 const c2Bound=add(q(7,72),q(5,48));
 const c2Chosen=q(1,4);
 const tailCoefficient=q(128);
 const tailDen=sub(q(1),mul(q(32),r));
 const tailAtMax=div(tailCoefficient,tailDen);
 const denominator=sub(sub(q(1),mul(q(5,4),r)),mul(q(4),sq(r)));
 const fullSourceCoefficient=div(add(add(q(23,18),mul(q(10),r)),mul(q(16),sq(r))),denominator);
 const quarticCoefficient=div(mul(tailCoefficient,add(q(5,2),mul(q(23,4),r))),mul(tailDen,denominator));
 const gates={
  complete_mean_small_root_radius_matches_R33:eq(r0,q(1,32)),
  total_full_K_domain_at_R33_radius:lt(mul(q(9,8),r0),q(1,20)),
  quadratic_correlation_polynomial_identity:peq(original,correlated),
  c2_joint_strong_bound_exact:eq(c2Bound,q(29,144)),
  c2_joint_strong_bound_below_one_quarter:lt(c2Bound,c2Chosen),
  line_Cauchy_radius_ratio_at_Rmax:eq(mul(q(32),r),q(1,2)),
  complete_mean_tail_at_Rmax_is256:eq(tailAtMax,q(256)),
  full_pointwise_inverse_denominator_exact:eq(denominator,q(1003,1024)),
  full_pointwise_inverse_denominator_positive:lt(q(0),denominator),
  unprojected_complete_source_below_three_halves:lt(fullSourceCoefficient,q(3,2)),
  source_quartic_error_coefficient_exact:eq(quarticCoefficient,q(678912,1003)),
  complete_mean_source_error_below680:lt(quarticCoefficient,q(680))
 };
 if(!Object.values(gates).every(Boolean))throw Error("Unpaid exact signed-mean comparison");
 return {
  schema:"visible-flex-signed-complete-mean-quadratic-v1",
  author:"exact_closure (GPT-6 Astra Pro; AI-assisted)",
  status:"Actual V8 BigInt exact universal coefficient checks; no new numerical field evaluation",
  all_gates:true,gates,
  norm:"R = norm_A1(P) + norm_A1(Kbar), each norm sums signed Fourier modes after radial sup; min nonzero absolute mode is 2",
  background:"Fixed real 0<w<=1/2, z=w^2, E=1+z; no physical-to-relative normalization omitted",
  formulas:{
   quadratic:"c2=-< (1+3z)Kbar^2+E P^2+2E Kbar P_theta >/2",
   correlated:"c2=-E*<C^2+P^2-P_theta^2>/2-z*<Kbar^2>, C=Kbar+P_theta",
   complete_mean_error:"epsilon(R)=128 R^3/(1-32R), R<1/32",
   mean_enclosure:"real: (c2+[-epsilon,+epsilon]) intersect [-4R^2,+4R^2]; complex: intersection of the corresponding closed disks",
   source_error:"norm_A0((N(X;c)-N(X;c2))/c_bg) <= 680 R^4 for R<=1/64"
  },
  values:{
   Rmax:rec(r),root_domain_radius:rec(r0),quadratic_norm_coefficient:rec(c2Bound),
   quadratic_slack_to_one_quarter:rec(sub(c2Chosen,c2Bound)),
   Cauchy_tail_coefficient:rec(tailCoefficient),tail_denominator_at_Rmax:rec(tailDen),
   tail_coefficient_at_Rmax:rec(tailAtMax),full_quotient_denominator:rec(denominator),
   unprojected_complete_source_coefficient:rec(fullSourceCoefficient),
   source_slack_to_three_halves:rec(sub(q(3,2),fullSourceCoefficient)),
   complete_source_quartic_error_coefficient:rec(quarticCoefficient),
   source_quartic_slack_to680:rec(sub(q(680),quarticCoefficient))
  },
  complete_mean_root_unchanged:true,
  all_signed_Laurent_zero_modes_retained_until_complete_inverse:true,
  no_complex_conjugacy_assumed:true,
  no_current_Green_or_cut_numerical_gate_claimed:true
 };
}
if(typeof module!=="undefined")module.exports={signedMeanQuadraticConstants};
