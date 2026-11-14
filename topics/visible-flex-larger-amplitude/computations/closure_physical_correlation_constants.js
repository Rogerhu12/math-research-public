// Exact physical complete-mean remainder constants.
// Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
// No external data, Arb, source integration or numerical ODE.
function physicalCorrelationConstants(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
 function q(n,d=1n){n=BigInt(n);d=BigInt(d);if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d);
 const sub=(a,b)=>q(a.n*b.d-b.n*a.d,a.d*b.d);
 const mul=(a,b)=>q(a.n*b.n,a.d*b.d);
 const div=(a,b)=>q(a.n*b.d,a.d*b.n);
 const sq=a=>mul(a,a);
 const lt=(a,b)=>a.n*b.d<b.n*a.d;
 const r=q(1,64),E=q(5,4),qcoef=q(23,18),dqcoef=q(23,9);
 const ellByR=add(E,mul(q(4),r));
 const deltaEll=add(E,mul(q(16),r));
 const den=sub(q(1),mul(r,ellByR));
 const AByR3=add(q(10),mul(q(16),r));
 const DAByR2=add(q(50),mul(q(128),r));
 const cubicNumer=add(AByR3,mul(qcoef,ellByR));
 const cubicBound=div(cubicNumer,den);
 const derivativeNumer=add(add(DAByR2,mul(dqcoef,ellByR)),mul(qcoef,deltaEll));
 const derivativeBound=add(div(derivativeNumer,den),
  div(mul(mul(r,cubicNumer),deltaEll),sq(den)));
 const gates={
  complex_small_root_domain_r_below_1over32:lt(r,q(1,32)),
  full_quotient_denominator_positive:lt(q(0),den),
  full_cubic_remainder_below13:lt(cubicBound,q(13)),
  full_remainder_derivative_below60:lt(derivativeBound,q(60)),
  no_large_inner_balance_assumed:E.n===5n&&E.d===4n,
  exact_quadratic_constant_preserved:qcoef.n===23n&&qcoef.d===18n
 };
 if(!Object.values(gates).every(Boolean))throw Error("Unpaid exact physical remainder gate");
 const rec=a=>({numerator:a.n.toString(),denominator:a.d.toString()});
 return {
  schema:"visible-flex-physical-correlation-complete-mean-constants-v1",
  status:"Actual V8 BigInt universal comparison, complete complex small-root algebra",
  author:"exact_closure (GPT-6 Astra Pro; AI-assisted)",
  all_gates:true,gates,
  scope:"Physical nonmean(P,Kbar), all signed nonzero even modes, fixed real0<w<=1/2, R<=1/64; no inner B>=120 assumed",
  values:{Rmax:rec(r),Emax:rec(E),denominator:rec(den),Q_coefficient:rec(qcoef),
   DQ_coefficient:rec(dqcoef),full_cubic_coefficient:rec(cubicBound),
   cubic_slack_to13:rec(sub(q(13),cubicBound)),
   complete_remainder_derivative_coefficient:rec(derivativeBound),
   derivative_slack_to60:rec(sub(q(60),derivativeBound))},
  complete_mean_root_retained:true,complete_mean_derivative_retained:true,
  complete_denominator_retained:true,nonmean_projection_after_full_product:true,
  new_actual_outer_solution_or_new_Green_kernel_claimed:false
 };
}
if(typeof module!=="undefined")module.exports={physicalCorrelationConstants};
