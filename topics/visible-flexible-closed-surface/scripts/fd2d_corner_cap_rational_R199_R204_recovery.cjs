"use strict";
/* R199 recovery and R204 new complete low-cap rational budgets.
   New implementation after fifth environment loss. It does not claim the
   SHA or execution receipt of the unavailable original 2026-11-13 source.
   All decimals accepted here are exact decimal rationals, not binary64. */
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
function Q(a,b=1n){a=BigInt(a);b=BigInt(b);if(b===0n)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const d=gcd(a,b);return {n:a/d,d:b/d};}
function q(s){if(typeof s==="object"&&s.n!==undefined)return s;if(typeof s==="bigint")return Q(s);s=String(s);if(s.includes("/")){const[a,b]=s.split("/");return Q(a,b);}if(s.includes(".")){const sign=s.startsWith("-")?-1n:1n;s=s.replace(/^-/,"");const[a,b]=s.split(".");return Q(sign*BigInt(a+b),10n**BigInt(b.length));}return Q(s);}
const add=(a,b)=>Q(a.n*b.d+b.n*a.d,a.d*b.d),neg=a=>Q(-a.n,a.d),sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>Q(a.n*b.n,a.d*b.d),div=(a,b)=>Q(a.n*b.d,a.d*b.n),sq=a=>mul(a,a),cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0;
const zero=q(0),one=q(1),two=q(2);
function out(a){return {numerator:String(a.n),denominator:String(a.d),fraction:a.d===1n?String(a.n):String(a.n)+"/"+String(a.d),decimal:Number(a.n)/Number(a.d)};}
function sum(a){return a.reduce(add,zero);}
function dot(a,b){return sum(a.map((x,i)=>mul(x,b[i])));}
function det3(a){return add(sub(mul(a[0][0],sub(mul(a[1][1],a[2][2]),mul(a[1][2],a[2][1]))),mul(a[0][1],sub(mul(a[1][0],a[2][2]),mul(a[1][2],a[2][0])))),mul(a[0][2],sub(mul(a[1][0],a[2][1]),mul(a[1][1],a[2][0]))));}
function solve3(A,b){const d=det3(A);if(d.n===0n)return null;return [0,1,2].map(j=>div(det3(A.map((r,i)=>r.map((v,k)=>k===j?b[i]:v))),d));}
function polarVertices(A,b,c,h,H){
 const planes=[{name:"x>=0",a:[neg(one),zero,zero],b:zero},{name:"y>=0",a:[zero,neg(one),zero],b:zero},{name:"z>=0",a:[zero,zero,neg(one)],b:zero},{name:"Ax<=1",a:[A,zero,zero],b:one},{name:"Hz<=1",a:[zero,zero,H],b:one},{name:"cx+by+hz<=1",a:[c,b,h],b:one}];
 const unique=new Map();
 for(let i=0;i<planes.length;i++)for(let j=i+1;j<planes.length;j++)for(let k=j+1;k<planes.length;k++){
  const active=[planes[i],planes[j],planes[k]],v=solve3(active.map(x=>x.a),active.map(x=>x.b));if(!v||planes.some(p=>cmp(dot(p.a,v),p.b)>0))continue;
  const key=v.map(x=>out(x).fraction).join(",");
  if(!unique.has(key))unique.set(key,{v,active:active.map(x=>x.name)});
 }
 return [...unique.values()].map(({v,active})=>({point:v.map(out),active,squared_norm:out(dot(v,v)),unit_ball_margin:out(sub(one,mul(sq(b),dot(v,v))))}));
}
const DESIGNS={
 recovered_original:{c:".60",h:"1.03",H:"1.55",Zmin:".60",Zmax:".73"},
 lower_window:{A:"1.30",c:".75",h:".925",H:"1.55",Zmin:".40",Zmax:".63"}
};
function checkCap(name="recovered_original"){
 if(!Object.prototype.hasOwnProperty.call(DESIGNS,name))throw Error("unknown explicit cap design");
 const p=Object.fromEntries(Object.entries({B:"1.6",R:".097",a:".30",ac:".32",lambda:".01",epsilon:".0001",delta:".000001",W:".85",A:"1.28",b:"1.011",g:".64",...DESIGNS[name]}).map(([k,v])=>[k,q(v)]));
 const {B,R,a,ac,lambda,epsilon,delta,W,A,b,g,c,h,H,Zmin,Zmax}=p;
 const zcLower=sub(sub(sub(h,epsilon),mul(q(3),R)),mul(mul(lambda,R),q("22/7")));
 const zcUpper=sub(sub(sub(h,epsilon),mul(q(3),R)),mul(two,mul(lambda,R)));
 const hmin=add(Zmin,add(epsilon,add(mul(q(3),R),mul(two,mul(lambda,R)))));
 const Hmin=add(sub(H,h),hmin);
 const margins={
  pyramid_height:sub(sub(H,R),h),
  planar_base_room:sub(sub(cmp(c,sub(b,R))<0?c:sub(b,R),delta),add(a,R)),
  throat_normal_ball:sub(sub(a,mul(R,add(one,mul(two,lambda)))) ,R),
  cuff_annulus_width:sub(ac,a),
  reference_corner_sphere:sub(sq(sub(sub(B,R),epsilon)),sum([sq(c),sq(sub(b,R)),sq(h)])),
  reference_tip_sphere:sub(sub(B,H),epsilon),
  complete_throat_sphere:sub(sq(B),add(sq(ac),sq(sub(sub(h,epsilon),R)))),
  cap_slab:sub(W,add(c,add(R,epsilon))),
  allowed_height_upper:sub(zcLower,Zmax),
  positive_height:Zmin,
  opposite_caps_separation:sub(mul(two,Zmin),mul(two,R)),
  throat_and_annulus_held_squared:sub(sq(sub(A,ac)),sq(g)),
  convex_cap_held_squared:sub(add(sq(sub(A,add(b,epsilon))),sq(add(Zmin,mul(two,R)))),sq(g)),
  remaining_flat_disk_held_squared:sub(add(sq(sub(A,q(".8"))),sq(Zmin)),sq(g)),
  support_gap:sub(sub(sub(b,epsilon),W),div(mul(two,B),q(20))),
  reach_ratio:sub(R,div(mul(two,B),q("100/3"))),
  held_ratio:sub(g,div(mul(two,B),q(5))),
  fixed_set_diameter:sub(sub(mul(two,Hmin),mul(two,epsilon)),g)
 };
 // The flat-disk estimate is conditional on using a remaining planar piece
 // with radius <=.8 at z=+-Z. It is not a certificate for a bent active tail.
 const checks=Object.fromEntries(Object.entries(margins).map(([k,v])=>[k,{...out(v),passed:cmp(v,zero)>=0}]));
 const vertices=polarVertices(A,b,c,hmin,Hmin);
 const exactChecks=Object.entries(checks);
 const passed=exactChecks.every(([,v])=>v.passed)&&vertices.length===8&&vertices.every(v=>BigInt(v.unit_ball_margin.numerator)>=0n);
 return {schema:"fd2d-R199-exact-cap-budget-recovery-v1",design:name,parameters:Object.fromEntries(Object.entries(p).map(([k,v])=>[k,out(v)])),zc_open_bounds:[out(zcLower),out(zcUpper)],minimum_corner_height:out(hmin),minimum_axial_height:out(Hmin),checks,positive_octant_polar_vertices:vertices,all_cap_and_marked_support_checks_passed:passed,
  held_flat_disk_bound_is_separate_conditional:checks.remaining_flat_disk_held_squared.passed,
  ratios:{diameter_upper:out(mul(two,B)),held_lower:out(div(g,mul(two,B))),E3_quotient_lower:out(div(sub(sub(b,epsilon),W),mul(two,B))),reach_lower:out(div(R,mul(two,B)))},
  still_required:["actual entire flat-disk-closed core is C2 embedded","core global reach >=R, with all point pairs","whole core ball B_B and |z|<=Z","phase-zero whole active core slab |y|<=W","core excludes open held ball centered (0,Aactual,0) radius g","central Aactual>=A and true circular planar cuff twojet","one fixed actual metric and exact-solution approximation requirement"]};
}
function ellipseBounds(A,B){A=q(A);B=q(B);const r=div(add(A,B),two),e=div(sub(A,B),add(A,B)),t=sq(e),L=mul(r,add(one,div(t,q(4)))),U=mul(r,add(add(one,div(t,q(4))),div(sq(t),mul(q(64),sub(one,t)))));return{lower:L,upper:U};}
function centralThresholds(){const base=ellipseBounds("1.4",".5"),trial=ellipseBounds("1.28",".68");return{schema:"fd2d-R199-central-threshold-rationals-v1",base_a0_lower:out(base.lower),base_a0_upper:out(base.upper),gap_06_A128_trial_upper:out(trial.upper),strict_A_threshold_margin:out(sub(base.lower,trial.upper)),central_B_upper_at_gap_064:out(sub(base.upper,q(".32"))),passed:cmp(base.lower,trial.upper)>0&&cmp(sub(base.upper,q(".32")),q(".85"))<0,qualification:"Exact normalized ellipse gap>=.60 implies A>1.28; gap>=.64 gives central ellipse held distance>=.64. This is not a whole-core certificate."};}
module.exports={checkCap,centralThresholds,DESIGNS};
