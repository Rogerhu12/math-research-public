"use strict";
// Exact rational gates for the closed ruled-annulus reach estimate.
// No geometry sampling, floating-point arithmetic, file I/O, or solver.
function ruledAnnulusReachRationalCertificate() {
  function gcd(a,b) { a=a<0n?-a:a; b=b<0n?-b:b; while(b){const c=a%b;a=b;b=c;} return a; }
  function Q(n,d=1n) { n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g]; }
  const add=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=a=>Q(-a[0],a[1]);
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>Q(a[0]*b[1],a[1]*b[0]);
  const sq=a=>mul(a,a);
  const one=Q(1),two=Q(2),checks=[];
  function gate(name,a,op,b) {const x=a[0]*b[1],y=b[0]*a[1];const ok=op==="<"?x<y:op===">"?x>y:x===y;if(!ok)throw Error(name);checks.push(name);}
  gate("sqrt2 lower squared",sq(Q(113,80)),"<",two);
  gate("sqrt2 upper squared",sq(Q(17,12)),">",two);
  gate("sigma lower squared",sq(Q(49,50)),"<",sub(one,sq(Q(7,40))));
  const L=div(mul(Q(49,50),Q(193,40)),two);
  gate("horizontal Fourier chord coefficient",L,"=",Q(9457,4000));
  const chord=sub(mul(two,L),div(Q(22,7),Q(40)));
  gate("perturbed sine chord",chord,">",Q(23,5));
  const parameterChord=div(Q(23,5),Q(22,7));
  gate("parameter chord",parameterChord,"=",Q(161,110));
  gate("centerline reach",div(sq(parameterChord),Q(7)),">",Q(3,10));
  gate("normal tube projection factor",sub(one,div(Q(1,20),Q(3,10))),"=",Q(5,6));
  const sineLimit=div(mul(Q(6,5),Q(2,5)),Q(23,5));
  gate("near-pair sine limit",sineLimit,"=",Q(12,115));
  const x=Q(21,200),sineLower=sub(x,div(mul(sq(x),x),Q(6)));
  gate("near-pair angle",sineLower,">",sineLimit);
  gate("speed lower margin",sq(Q(14,5)),"<",Q(8));
  gate("speed upper margin",Q(31,10),">",Q(3));
  const phiDerivativeUpper=sub(Q(8),mul(Q(3,2),add(Q(17),mul(Q(3),Q(-7,40)))));
  gate("Phi derivative sign",phiDerivativeUpper,"<",Q(0));
  const kappaUpper=div(add(Q(17),mul(Q(3),Q(-1,6))),mul(Q(16),Q(113,80)));
  gate("baseline geodesic curvature",kappaUpper,"=",Q(165,226));
  gate("geodesic curvature perturbation margin",kappaUpper,"<",Q(3,4));
  gate("shape operator radical",Q(73),"<",sq(Q(9)));
  gate("metric radius bound",Q(401,400),"<",sq(Q(801,800)));
  gate("upper angular speed",mul(Q(31,10),Q(801,800)),"<",Q(25,8));
  gate("Taylor remainder coefficient",div(add(Q(7),mul(Q(1,20),Q(20))),two),"=",Q(4));
  gate("relative Taylor remainder",mul(div(Q(4),Q(14,5)),Q(21,100)),"=",Q(3,10));
  const pathRatio=div(Q(25,8),Q(14,5));
  gate("path to tangent ratio",pathRatio,"=",Q(125,112));
  const C=div(pathRatio,Q(7,10));
  gate("geodesic to spatial chord ratio",C,"=",Q(625,392));
  const uniqueness=mul(mul(Q(1,5),Q(3,2)),sq(C));
  gate("near-pair nearest-point uniqueness",uniqueness,"<",one);
  const normalized=div(Q(1,5),Q(13,2));
  gate("whole-diameter normalization",normalized,"=",Q(2,65));
  gate("three percent threshold",normalized,">",Q(3,100));
  return {status:"PASS_EXACT_RATIONAL_GATES_ONLY",checks:checks.length,
    reach_over_b:"1/5",diameter_over_b_upper:"13/2",
    reach_over_initial_diameter_strict_lower:"2/65",
    proves_geodesic_existence:false,proves_full_annulus_theorem:false,
    numerical_solver_calls:0};
}
if (typeof module !== "undefined" && module.exports) module.exports=ruledAnnulusReachRationalCertificate;
if (typeof require !== "undefined" && typeof module !== "undefined" && require.main===module) {
  console.log(JSON.stringify(ruledAnnulusReachRationalCertificate(),null,2));
}
