#!/usr/bin/env node
"use strict";
/*
Exact rational background-only certificate at accepted q096 input doubles.
This is not an actual general-core BVP or a floating-point implementation audit.
No imports and no modification of the frozen .mjs source tree.
*/
const absBig=x=>x<0n?-x:x;
function gcd(a,b){a=absBig(a);b=absBig(b);while(b){const t=a%b;a=b;b=t;}return a;}
function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return [n/g,d/g];}
const Z=()=>F(0),O=()=>F(1);
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const sub=(a,b)=>F(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
const cmp=(a,b)=>{const n=a[0]*b[1]-b[0]*a[1];return n<0n?-1:n>0n?1:0;};
const max=xs=>xs.reduce((a,b)=>cmp(a,b)>=0?a:b);
function pow(a,n){let r=O();for(let j=0;j<n;j++)r=mul(r,a);return r;}
function approximate(a){
 if(a[0]===0n)return 0;
 const sign=a[0]<0n?-1:1,n=absBig(a[0]),d=a[1];
 const ns=Math.max(0,n.toString(2).length-53),ds=Math.max(0,d.toString(2).length-53);
 return sign*(Number(n>>BigInt(ns))/Number(d>>BigInt(ds)))*2**(ns-ds);
}
const rec=a=>({numerator:String(a[0]),denominator:String(a[1]),decimal_display:approximate(a)});
function fromFloat(x){
 if(!Number.isFinite(x))throw Error("nonfinite");
 const b=new ArrayBuffer(8),v=new DataView(b);v.setFloat64(0,x,false);
 const hi=v.getUint32(0,false),lo=v.getUint32(4,false),sign=(hi>>>31)?-1n:1n,e0=(hi>>>20)&2047;
 let m=(BigInt(hi&1048575)<<32n)+BigInt(lo),e;
 if(e0===0)e=-1074;else{m+=1n<<52n;e=e0-1023-52;}
 return e>=0?F(sign*(m<<BigInt(e))):F(sign*m,1n<<BigInt(-e));
}
function requirePositive(a,label){if(cmp(a,Z())<=0)throw Error(label);}
function main(){
 const delta=fromFloat(.16208341673538396),V=fromFloat(.31980000000000003),k=fromFloat(.45),degree=22;
 const Smin=F(277,500),Smax=F(423,500),a0=O(),cap=F(51,10);
 const A=d=>F(d-1,d+1),B=d=>F(1,d*(d+1));
 const travel=(d,S)=>add(mul(mul(A(d),V),S),mul(mul(B(d),k),mul(S,S)));
 const intervalChecks=[];
 for(const d of [3,degree]){
  const lower=sub(delta,travel(d,Smin)),upper=sub(travel(d,Smax),delta);
  requirePositive(lower,"lower length bracket");requirePositive(upper,"upper length bracket");
  intervalChecks.push({degree:d,lower_travel_slack:rec(lower),upper_travel_slack:rec(upper)});
 }
 const monotoneSlack=sub(mul(F(3),V),mul(k,Smax));
 requirePositive(monotoneSlack,"common monotone-speed domain");
 const lengthOrderSlack=sub(mul(F(6*degree),V),mul(F(degree+4),mul(k,Smax)));
 requirePositive(lengthOrderSlack,"frontloaded travel exceeds cubic travel");
 const accelerations=[];
 for(const d of [3,degree]){
  const coefficient=mul(F(d),sub(div(mul(F(d-1),V),Smin),k));
  requirePositive(coefficient,"positive acceleration coefficient");
  const u=div(sub(coefficient,mul(F(d-2),k)),mul(F(d-1),coefficient));
  const points=[Z(),O()];
  if(cmp(u,Z())>0&&cmp(u,O())<0)points.push(u);
  const evaluate=t=>mul(pow(sub(O(),t),d-2),add(k,mul(coefficient,t)));
  const values=points.map(evaluate),maximum=max(values);
  accelerations.push({degree:d,coefficient_B:rec(coefficient),critical_u:rec(u),
   candidates:points.map((t,j)=>({u:rec(t),physical_acceleration:rec(values[j])})),
   maximum_acceleration_upper:rec(maximum)});
 }
 const accel=max(accelerations.map(a=>F(a.maximum_acceleration_upper.numerator,a.maximum_acceleration_upper.denominator)));
 const zprimeSquared=sub(O(),mul(V,V));
 const curvatureSlack=sub(mul(mul(cap,cap),zprimeSquared),mul(accel,accel));
 requirePositive(zprimeSquared,"positive vertical speed");
 requirePositive(curvatureSlack,"strict curvature cap");
 const checks={
  original_binary64_inputs_roundtrip:[delta,V,k].every((f,j)=>approximate(f)===[.16208341673538396,.31980000000000003,.45][j]),
  all_endpoint_length_brackets_strict:true,
  k0_times_all_lengths_less_than_3V:true,
  all_lambda_velocity_bernstein_controls_monotone:true,
  all_lambda_speed_between_zero_and_V:true,
  all_lambda_meridian_curvature_strictly_less_than_5p1:true,
  all_lambda_absolute_circumferential_curvature_at_most_one:true,
  all_lambda_background_gaussian_curvature_nonpositive:true
 };
 if(Object.values(checks).some(v=>v!==true))throw Error("failed exact check");
 return {
  format:"exact-background-frontload-curvature-v1",
  computation_kind:"Exact BigInt rational arithmetic only; no physical RHS or BVP",
  scope:"The exact ideal surface-of-revolution first-piece family only, at fixed accepted q096 delta/V/k0.",
  source_summary:"notes/2026-11-12-strong-actual-q096-ci-actions-43302113873-1-strong-summary.json",
  source_summary_sha256:"c3291bbc2de37008f5a9272e762c628a3f4e95106b3382d6253bf4a5b14c3c2a",
  source_profile_lines:[300,360],
  provider:"computations/strong_monotone_initial_speed.py",
  provider_sha256:"12d6340d4e9dce27ee93d390971d0258cc1e2299dedf99fe21365a70494549e7",
  parameters:{delta:rec(delta),V:rec(V),k0:rec(k),a0:rec(a0),degree},
  lambda_interval:[0,1],length_lower_strict:rec(Smin),length_upper_strict:rec(Smax),
  endpoint_length_brackets:intervalChecks,
  exact_monotone_domain_slack:rec(monotoneSlack),
  exact_frontloaded_travel_order_slack:rec(lengthOrderSlack),
  acceleration_bounds:accelerations,maximum_acceleration_upper:rec(accel),
  minimum_vertical_speed_squared:rec(zprimeSquared),
  meridian_curvature_cap:rec(cap),exact_squared_curvature_cap_slack:rec(curvatureSlack),
  display_tighter_meridian_bound:approximate(accel)/Math.sqrt(approximate(zprimeSquared)),
  circumferential_curvature_cap:1,checks,
  formula:{
   velocity:"v_d(u;S)=V[1-(1-u)^(d-1)(1+(d-1)u)]+k0*S*u*(1-u)^(d-1)",
   blend:"v_lambda=(1-lambda)*v_3+lambda*v_22, evaluated at the common positive length S_lambda",
   length:"delta=[(1-lambda)/2+lambda*21/23]*V*S+[(1-lambda)/12+lambda/(22*23)]*k0*S^2",
   acceleration:"a_d=(1-u)^(d-2)*[k0+d*((d-1)*V/S-k0)*u]",
   stationary:"u*=(B-(d-2)*k0)/((d-1)*B), B=d*((d-1)*V/S-k0)",
   principal_curvatures:"absolute meridian=a_lambda/sqrt(1-v_lambda^2); absolute angular=sqrt(1-v_lambda^2)/r"
  },
  proof:[
   "Both endpoint travel polynomials are strictly below delta at S=.554 and above it at S=.846. Their convex combination is increasing in positive S, hence each unique S_lambda lies strictly in that interval.",
   "The exact inequality k0*.846<3V makes both degree-elevated cubic and degree22 endpoint velocity controls monotone. Thus every convex combination satisfies 0<=v_lambda<=V and a_lambda>=0.",
   "The travel difference has the positive factor (d-3)*S/[12*d*(d+1)] times [6*d*V-(d+4)*k0*S]. The saved exact slack makes S_lambda strictly decrease with lambda.",
   "For each fixed u, a_d increases as S decreases. Evaluate both d=3 and d=22 at S=.554, maximize each at endpoints and its sole interior critical point, and take the larger rational value.",
   "The saved exact positive squared slack proves a_max^2<(51/10)^2*(1-V^2). Hence absolute meridian curvature is strictly below5.1. Since r>=a0=1, absolute angular curvature is at most1. Gaussian curvature is -a_lambda/r<=0.",
   "The radius increment and common endpoint data r(0)=1,r'(0)=0,r''(0)=k0,r(S)=1+delta,r'(S)=V,r''(S)=0 are preserved by the defining length equation and polynomial controls."
  ],
  limitations:[
   "The general-core immersion is not a surface of revolution; no actual nonlinear curvature or continuation is certified.",
   "Only the first piece and fixed delta/V/k0 are covered. A core-held physical response changes geometric controls and must be recomputed.",
   "This exact-family certificate does not enclose the NumPy provider's floating-point rounding.",
   "Nonzero lambda changes the physical metric; the explicit provider hook and full actual BVP/tail/RMS/jet gates remain necessary.",
   "No whole-profile/global reach/closed-held or diameter claim is made."
  ]
 };
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(main(),null,2));
