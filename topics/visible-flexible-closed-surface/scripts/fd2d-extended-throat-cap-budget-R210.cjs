"use strict";
/* R210: exact rational extension of the R204 complete cap budget.
   All decimal constants below are decimal rationals, not binary64.
   The geometric proof is in R210; this program checks its finite budgets.
   parent is the unchanged fd2d_corner_cap_rational_R199_R204_recovery module.
   No current fitted field, normal, LM, mesh or body is evaluated here. */
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
function Q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const d=gcd(a,b);return{n:a/d,d:b/d};}
function q(s){if(typeof s==="object"&&s.n!==undefined)return s;s=String(s);if(s.includes("/")){const a=s.split("/");return Q(a[0],a[1]);}if(s.includes(".")){const sign=s[0]==="-"?-1n:1n;s=s.replace(/^-/,"");const a=s.split(".");return Q(sign*BigInt(a[0]+a[1]),10n**BigInt(a[1].length));}return Q(s);}
const add=(a,b)=>Q(a.n*b.d+b.n*a.d,a.d*b.d),sub=(a,b)=>Q(a.n*b.d-b.n*a.d,a.d*b.d),mul=(a,b)=>Q(a.n*b.n,a.d*b.d),div=(a,b)=>Q(a.n*b.d,a.d*b.n),sq=a=>mul(a,a),sum=a=>a.reduce(add,q(0)),cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0;
function out(a){return{numerator:String(a.n),denominator:String(a.d),fraction:a.d===1n?String(a.n):a.n+"/"+a.d,decimal:Number(a.n)/Number(a.d)};}
function checkR210(parent){
 if(!parent||typeof parent.checkCap!=="function")throw Error("explicit R204 dependency required");
 const old=parent.checkCap("lower_window");
 if(old.all_cap_and_marked_support_checks_passed!==true)throw Error("R204 parent budget failed");
 const B=q("1.6"),R=q(".097"),a=q(".30"),ac=q(".32"),lambda=q(".01"),epsilon=q(".0001"),delta=q(".000001"),
 c=q(".75"),b=q("1.011"),h=q(".925"),H=q("1.55"),W=q(".85"),A=q("1.30"),g=q(".64"),
 Delta=q("1/50"),Zmin=q(".40"),Zmax=q(".61"),two=q(2);
 // pi>8/3 gives L/4=2 Delta/(3 pi)<Delta/4. I>2, I<22/7.
 const radialLossUpper=div(Delta,q(4));
 const rminLower=sub(sub(a,mul(R,add(q(1),mul(two,lambda)))),radialLossUpper);
 const zcLower=sub(sub(sub(h,epsilon),mul(q(3),R)),mul(mul(lambda,R),q("22/7")));
 const d0Lower=add(mul(two,R),mul(two,mul(lambda,R)));
 const effectiveZmin=add(Zmin,Delta),effectiveZmax=add(Zmax,Delta);
 const hmin=add(effectiveZmin,add(epsilon,add(mul(q(3),R),mul(two,mul(lambda,R)))));
 const Hmin=add(sub(H,h),hmin),farRadius=add(ac,mul(two,R));
 const margins={
  fixed_Delta_positive:Delta,
  true_Z_lower:sub(Zmin,q(".40")),
  effective_height_upper:sub(zcLower,effectiveZmax),
  effective_height_in_old_window:sub(q(".63"),effectiveZmax),
  extended_throat_radius_over_R:sub(rminLower,R),
  planar_base_room:sub(sub(c,delta),add(a,R)),
  cuff_annulus_width:sub(ac,a),
  complete_throat_sphere:sub(sq(B),add(sq(ac),sq(sub(sub(h,epsilon),R)))),
  reference_corner_sphere:sub(sq(sub(sub(B,R),epsilon)),sum([sq(c),sq(sub(b,R)),sq(h)])),
  reference_tip_sphere:sub(sub(B,H),epsilon),
  cap_slab:sub(W,add(c,add(R,epsilon))),
  protrusion_to_throat_distance_over_2R:sub(sub(farRadius,ac),mul(two,R)),
  protrusion_to_convex_distance_over_2R:sub(d0Lower,mul(two,R)),
  opposite_caps_distance_over_2R:sub(mul(two,Zmin),mul(two,R)),
  throat_held_squared:sub(sq(sub(A,ac)),sq(g)),
  convex_cap_held_squared:sub(add(sq(sub(A,add(b,epsilon))),sq(add(Zmin,add(mul(two,R),Delta)))),sq(g)),
  corner_marker_height_over_old_bound:sub(hmin,q(".69304")),
  axis_marker_height_over_old_bound:sub(Hmin,q("1.31804")),
  fixed_set_diameter_over_held:sub(sub(mul(two,Hmin),mul(two,epsilon)),g),
  support_gap_over_one_twentieth_D:sub(sub(sub(b,epsilon),W),div(mul(two,B),q(20))),
  reach_over_three_percent_D:sub(R,mul(q(".03"),mul(two,B))),
  held_over_one_fifth_D:sub(g,div(mul(two,B),q(5)))
 };
 const checks=Object.fromEntries(Object.entries(margins).map(([key,v])=>[key,{...out(v),passed:cmp(v,q(0))>=0}]));
 const passed=Object.values(checks).every(x=>x.passed);
 return{schema:"fd2d-R210-extended-throat-cap-exact-budget-v1",
  parameters:{Delta:out(Delta),Zmin:out(Zmin),Zmax:out(Zmax),effectiveZmin:out(effectiveZmin),effectiveZmax:out(effectiveZmax),farRadius:out(farRadius),R:out(R),a:out(a),ac:out(ac)},
  analytic_definitions:{theta_interval:"[0,pi]","L":"8 Delta/(3 pi)","q":"R(1+lambda/sqrt(sin(theta)))+L sin(theta)^3","r":"a-R sin(theta)-2 lambda R sqrt(sin(theta))-L sin(theta)^4/4","z":"Z+R(1-cos(theta))+lambda R integral_0^theta sqrt(sin(v)) dv+L integral_0^theta sin(v)^4 dv","height_added":"L*3*pi/8=Delta","radius_both_ends":"a"},
  strict_bound_lemmas:["pi>8/3 implies L/4<Delta/4","2<integral_0^pi sqrt(sin(theta)) dtheta<22/7","R111/R113 rolling-ball argument with q>=R and rmin>R","R204 exact polar-vertex budget inherited because all marker heights increase"],
  scalar_bounds:{rmin_strict_lower:out(rminLower),zc_strict_lower:out(zcLower),d0_strict_lower:out(d0Lower),corner_marker_height_strict_lower:out(hmin),axis_marker_height_strict_lower:out(Hmin)},
  checks,ratios:old.ratios,R204_parent_budget:old,parent_core_hypotheses_not_inherited:"The embedded parent report is a scalar cap/marker budget only. Its old |z|<=Z hypothesis is replaced by the R210 whole-core conditions listed below and proved separately.",all_cap_and_marked_support_checks_passed:passed,
  whole_core_still_required:["C2 closed embedded core with two exact radius .32 planar disks and open common-twojet collars","whole closed-core reach >=.097","whole core in B_1.6 and |z|<=Z+.02","every whole-core point with |z|>Z has cylindrical radius >=.514","phase-zero whole activity in |y|<=.85","whole phase-zero core excludes open radius .64 ball about (0,Aactual,0)","actual central Aactual>=1.30 and all metric/common-g requirements"],
  not_claimed:["no current fitted field is certified here","no global reach follows from curvature samples","no change to the running numerical guide or main field"],
  scope:"Exact rational budgets plus the named analytic proof; not sampled cap geometry."};
}
module.exports={checkR210};
