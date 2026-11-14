#!/usr/bin/env node
// R118 true Newton quadratic source and moving spherical chart.
// Exact rational bounds at the worst allowed a=1/100. All displayed
// expressions are monotone in a on [0,1/100]; no actual inverse is assumed.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let b=F(1);for(let k=0;k<n;k++)b=mul(b,a);return b;}
const cmp=(a,b)=>a[0]*b[1]-b[0]*a[1];
const str=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];


export function certifyQuadraticMovingChart(){
 const gates=[];
 function gate(name,a,b,strict=true){
  const ok=strict?cmp(a,b)<0n:cmp(a,b)<=0n;
  gates.push({name,left:str(a),relation:strict?"<":"<=",right:str(b),passed:ok});
  if(!ok)throw Error("unpaid R118 gate: "+name);
 }
 const a=F(1,100),r=sub(F(1),a),ri=div(F(1),r),sqrt2=F(3,2);
 gate("sqrt(2) strictly below 3/2",F(2),pow(sqrt2,2));
 const d=add(ri,mul(F(2),pow(ri,2)));
 const E1=add(mul(F(2),ri),d);
 gate("normalization C0 difference per a",ri,F(2));
 gate("ambient first derivative difference per a",E1,F(6));
 const E2=add(add(mul(F(72),pow(ri,3)),
   mul(add(mul(F(24),sqrt2),mul(F(24),a)),pow(ri,2))),
   add(mul(F(4),ri),mul(sqrt2,d)));
 gate("complete ambient second derivative difference per a",E2,F(120));
 gate("sphere-map Hessian including projection difference per a",add(F(120),mul(sqrt2,ri)),F(122));
 const margin=sub(F(1),mul(F(6),a)),J1=div(F(1),margin),J2=div(mul(F(122),a),pow(margin,3));
 gate("strict global local-diffeomorphism margin",F(0),margin);
 gate("inverse first derivative",J1,F(50,47),false);
 const composition=add(pow(J1,2),J2);
 gate("complete inverse-chart C2 composition",composition,F(3));
 const vp=add(F(6),mul(F(4),a)),vpp=add(F(19),mul(F(16),a));
 const h1=mul(F(1,2),mul(vp,pow(ri,3)));
 const h2=add(mul(F(3,4),mul(mul(pow(vp,2),a),pow(ri,5))),mul(F(1,2),mul(vpp,pow(ri,3))));
 const k1=mul(F(1,2),mul(vp,ri));
 const k2=add(mul(F(1,4),mul(mul(pow(vp,2),a),pow(ri,3))),mul(F(1,2),mul(vpp,ri)));
 gate("inverse radius first derivative per a",h1,F(4));
 gate("inverse radius complete Hessian per a",h2,F(11));
 gate("radius first derivative per a",k1,F(4));
 gate("radius complete Hessian per a",k2,F(10));
 gate("rho times inverse-radius deviation C2",add(add(F(2),mul(F(2),F(4))),F(11)),F(21),false);
 gate("R times radius deviation C2",add(add(F(1),mul(F(2),F(4))),F(10)),F(19),false);
 gate("updated rho and radius relative to one fixed reference",mul(F(3),add(F(1),mul(F(21),a))),F(4));
 gate("quadratic source full coefficient",add(add(F(1),F(4)),F(6)),F(11),false);
 gate("updated defect C0 coefficient",pow(F(3),2),F(9),false);
 gate("updated defect C1 coefficient",mul(F(2),pow(F(3),2)),F(18),false);
 gate("updated compatibility source coefficient",mul(F(11),mul(pow(F(4),2),pow(F(3),2))),F(1584),false);
 gate("actual Newton scalar RHS coefficient",mul(F(11,2),mul(pow(F(4),2),pow(F(3),2))),F(792),false);
 return{kind:"R118_true_Newton_quadratic_source_and_moving_chart",execution:"actual V8 BigInt rational arithmetic",
  allowed_a:"0 <= ||rho||C2 * ||V||C2 <= 1/100",gates,gate_count:gates.length,passed:gates.every(x=>x.passed),
  constants:{ambient_chart_difference_C1:6,ambient_chart_difference_C2:120,intrinsic_chart_Hessian:122,
   inverse_chart_C2_composition:3,new_rho_radius_reference_factor:4,metric_defect_C0:9,metric_defect_C1:18,
   compatibility_source:1584,Newton_scalar_RHS:792},
  limitations:["The actual full linearized metric equation must be solved exactly for the quadratic-only conclusion.",
   "An approximate inverse retains the complete compatibility source of its true strain residual.",
   "No arbitrary mixed-type PDE C0-to-C2 inverse, candidate numerical neighborhood, high angular norm or nonlinear convergence is asserted."]};
}
if(typeof process!=="undefined"&&process.argv?.[1]&&import.meta.url===new URL("file://"+process.argv[1]).href){
 const {writeFileSync}=await import("node:fs");const output=JSON.stringify(certifyQuadraticMovingChart(),null,2)+"\n";
 if(process.argv[2])writeFileSync(process.argv[2],output);else process.stdout.write(output);
}
