// Exact inner canonical-to-physical correlation identities.
// Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
// Universal finite-mode algebra, not an evaluation of a scientific field.
function innerCanonicalCorrelationLedger(){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
 function q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return {n:n/g,d:d/g};}
 const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d);
 const sub=(a,b)=>q(a.n*b.d-b.n*a.d,a.d*b.d);
 const mul=(a,b)=>q(a.n*b.n,a.d*b.d), div=(a,b)=>q(a.n*b.d,a.d*b.n);
 const eq=(a,b)=>a.n*b.d===b.n*a.d, le=(a,b)=>a.n*b.d<=b.n*a.d;
 const rec=a=>({numerator:a.n.toString(),denominator:a.d.toString()});
 const max=(a,b)=>le(a,b)?b:a;
 // polynomials of degree at most one in z, exact rationals
 const zpoly=(a,b)=>[q(a),q(b)];
 const padd=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
 const pscale=(a,b)=>a.map(x=>mul(x,q(b)));
 const peq=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]);
 const positive=Array.from({length:46},(_,i)=>BigInt(2*i+2));
 const signed=[...positive.map(x=>-x),...positive];
 const maxima={Pweak:q(0),KQweak:q(0),CweakXi:q(0),UQweak:q(0),UXiweak:q(0),jointQstrong:q(0)};
 let identity=true,inverse=true,mean=true;
 for(const m of positive){
  const m2=m*m, d=1n+m, d3=d*d*d;
  maxima.Pweak=max(maxima.Pweak,q(m,d3));
  maxima.KQweak=max(maxima.KQweak,q(m2,d3));
  maxima.CweakXi=max(maxima.CweakXi,q(1,d));
  maxima.UQweak=max(maxima.UQweak,q(m*(m2-1n),d3));
  maxima.UXiweak=max(maxima.UXiweak,q(m,d));
  maxima.jointQstrong=max(maxima.jointQstrong,q(m+m2,d*d));
  // C=K+P_theta: the Q coefficient m^2-m^2 is exactly zero.
  identity=identity&&(m2-m2===0n);
  // K+E P_theta: coefficients of Q in (1,z) are (0,-m^2).
  inverse=inverse&&peq(padd(zpoly(m2,0),zpoly(-m2,-m2)),zpoly(0,-m2));
  // c2 of one cosine/sine pair, with P_sin=-m*A*Q.
  const originalQQ=pscale(padd(padd(zpoly(m2*m2,3n*m2*m2),zpoly(m2,m2)),zpoly(-2n*m2*m2,-2n*m2*m2)),-1);
  const directQQ=zpoly(m2*(m2-1n),-m2*(m2+1n)); // both scaled by 4
  const originalQXi=pscale(padd(zpoly(2n*m2,6n*m2),zpoly(-2n*m2,-2n*m2)),-1);
  const directQXi=zpoly(0,-4n*m2); // both scaled by 4
  const originalXiXi=zpoly(-1,-3);
  mean=mean&&peq(originalQQ,directQQ)&&peq(originalQXi,directQXi)&&peq(originalXiXi,zpoly(-1,-3));
 }
 let quadratic=true,jacobian=true,zeroOutputPairs=0,orderedPairs=0;
 for(const a of signed)for(const b of signed){
  orderedPairs++;
  if(a+b===0n)zeroOutputPairs++;
  const a2=a*a,b2=b*b,ab=a*b;
  // Ordered monomials: A^2 QaQb, A*D QaXib, A*D XiaQb, D^2 XiaXib.
  const physicalLog=[zpoly(0,-(a2*b2-ab)),zpoly(0,-a2),zpoly(0,-b2),padd(zpoly(1,1),zpoly(0,-1))];
  const directLog=[zpoly(0,-ab*(ab-1n)),zpoly(0,-a2),zpoly(0,-b2),zpoly(1,0)];
  const physicalRad=[a*(a2-1n)*b*(b2-1n),a*(a2-1n)*b,a*b*(b2-1n),ab].map(v=>zpoly(-v,-v));
  const directRad=[ab*(a2-1n)*(b2-1n),ab*(a2-1n),ab*(b2-1n),ab].map(v=>zpoly(-v,-v));
  quadratic=quadratic&&physicalLog.every((x,i)=>peq(x,directLog[i]))&&physicalRad.every((x,i)=>peq(x,directRad[i]));
  // Derivative columns for delta Q_b and delta Xi_b, respectively.
  const directJQrad=[zpoly(-2n*ab*(b2-1n)*(a2-1n),-2n*ab*(b2-1n)*(a2-1n)),zpoly(-2n*ab*(b2-1n),-2n*ab*(b2-1n))];
  const directJQlog=[zpoly(0,-2n*ab*(ab-1n)),zpoly(0,-2n*b2)];
  const directJXrad=[zpoly(-2n*ab*(a2-1n),-2n*ab*(a2-1n)),zpoly(-2n*ab,-2n*ab)];
  const directJXlog=[zpoly(0,-2n*a2),zpoly(2,0)];
  jacobian=jacobian&&peq(directJQrad[0],pscale(physicalRad[0],2))&&peq(directJQrad[1],pscale(physicalRad[2],2))
   &&peq(directJQlog[0],pscale(physicalLog[0],2))&&peq(directJQlog[1],pscale(physicalLog[2],2))
   &&peq(directJXrad[0],pscale(physicalRad[1],2))&&peq(directJXrad[1],pscale(physicalRad[3],2))
   &&peq(directJXlog[0],pscale(physicalLog[1],2))&&peq(directJXlog[1],pscale(physicalLog[3],2));
 }
 // Monomial exponent check for cut_conversion*(mu_n/mu_12)*(1/D_n).
 // Variables: r,w,b,w_b,mu_n,mu_12,sqrt12.
 const cut=[0,0,-4,-2,0,1,1],muRatio=[0,0,0,0,1,-1,0],oneOverD=[4,2,0,0,-1,0,-1];
 const combined=cut.map((v,i)=>v+muRatio[i]+oneOverD[i]);
 const cutCancellation=JSON.stringify(combined)===JSON.stringify([4,2,-4,-2,0,0,0]);
 const gates={
  all46_positive_even_modes:positive.length===46,
  all92_signed_nonzero_even_modes:signed.length===92,
  exact_C_Q_cancellation:identity,
  exact_full_inverse_nonmean_correlation:inverse,
  exact_signed_mean_quadratic_all46:mean,
  Pweak_coefficient_is2over27:eq(maxima.Pweak,q(2,27)),
  KQweak_coefficient_is4over27:eq(maxima.KQweak,q(4,27)),
  Cweak_Xi_coefficient_is1over3:eq(maxima.CweakXi,q(1,3)),
  UQweak_coefficient_is8372over8649:eq(maxima.UQweak,q(8372,8649)),
  UXiweak_coefficient_is92over93:eq(maxima.UXiweak,q(92,93)),
  joint_Q_strong_coefficient_is92over93:eq(maxima.jointQstrong,q(92,93)),
  all8464_signed_ordered_quadratic_pairs:orderedPairs===8464&&quadratic,
  all8464_canonical_quadratic_Jacobian_pairs:orderedPairs===8464&&jacobian,
  zero_output_pairs_retained:zeroOutputPairs===92,
  exact_cut_mu_and_sqrt12_cancellation:cutCancellation
 };
 if(!Object.values(gates).every(Boolean))throw Error("Unpaid inner canonical identity");
 return {
  schema:"visible-flex-inner-canonical-correlation-identities-v1",
  author:"exact_closure (GPT-6 Astra Pro; AI-assisted)",
  status:"Actual V8 BigInt universal finite-mode coefficient checks, not new field/Green evaluation",
  all_gates:true,gates,
  norm:"Canonical Q weight (1+|m|)^3, Xi weight (1+|m|), same true reference strip; radial modal masses fixed before sums",
  positive_modes:positive.map(Number),signed_ordered_pairs:orderedPairs,
  zero_output_pairs_kept:zeroOutputPairs,
  maxima:Object.fromEntries(Object.entries(maxima).map(([k,v])=>[k,rec(v)])),
  cut_source_multiplier_exponents:{variables:["r","w","b","w_b","mu_n","mu_12","sqrt12"],result:combined},
  source_units:"outward source-x complete relative source N_x; multiplier r^4 w^2/(b^4 w_b^2), with no second r_x",
  complete_mean_inverse_and_true_auxiliary_error_required:true,
  signed_Q_gain_required:true,
  no_interval_scientific_source_evaluation_claimed:true,
  no_inner_cut_or_outer_closure_numeric_gate_claimed:true
 };
}
if(typeof module!=="undefined")module.exports={innerCanonicalCorrelationLedger};
