#!/usr/bin/env node
"use strict";
/* Exact common-chart transport constants. No physical RHS or BVP is run. */
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

const min=xs=>xs.reduce((a,b)=>cmp(a,b)<=0?a:b);
function binom(n,k){if(k<0||k>n)return 0n;k=Math.min(k,n-k);let b=1n;for(let j=1;j<=k;j++)b=b*BigInt(n-k+j)/BigInt(j);return b;}
function polyadd(a,b,scale=O()){
 const result=a.slice();while(result.length<b.length)result.push(Z());
 for(let j=0;j<b.length;j++)result[j]=add(result[j],mul(scale,b[j]));
 return result;
}
function chebyshevPower(c){
 let result=[c[0]],previous=[O()],current=[Z(),O()];
 if(c.length>1)result=polyadd(result,current,c[1]);
 for(let j=2;j<c.length;j++){
  const next=polyadd([Z(),...current.map(x=>mul(F(2),x))],previous,F(-1));
  result=polyadd(result,next,c[j]);previous=current;current=next;
 }
 return result;
}
function bernstein(power){
 const degree=power.length-1,shifted=[];
 for(let k=0;k<=degree;k++){
  let t=Z();for(let j=k;j<=degree;j++)t=add(t,mul(power[j],F(binom(j,k)*(((j-k)%2)?-1n:1n)*(1n<<BigInt(k)))));
  shifted.push(t);
 }
 const b=[];for(let i=0;i<=degree;i++){let t=Z();for(let k=0;k<=i;k++)t=add(t,mul(shifted[k],F(binom(i,k),binom(degree,k))));b.push(t);}return b;
}
function splitHalf(c){
 const rows=[c.slice()];
 while(rows.at(-1).length>1){const old=rows.at(-1),next=[];for(let j=0;j<old.length-1;j++)next.push(div(add(old[j],old[j+1]),F(2)));rows.push(next);}
 return [rows.map(r=>r[0]),rows.slice().reverse().map(r=>r.at(-1))];
}
function positiveCertificate(power,maxDepth=12){
 const queue=[[F(-1),F(1),bernstein(power),0]],leaves=[],unresolved=[],negative=[];
 let lower=null,maxUsed=0;
 while(queue.length){
  const [lo,hi,c,depth]=queue.pop(),lb=min(c),ub=max(c);
  if(cmp(lb,Z())>0){leaves.push({lo:rec(lo),hi:rec(hi),lower:rec(lb),depth});if(lower===null||cmp(lb,lower)<0)lower=lb;maxUsed=Math.max(maxUsed,depth);}
  else if(cmp(c[0],Z())<=0||cmp(c.at(-1),Z())<=0){const left=cmp(c[0],Z())<=0;negative.push({x:rec(left?lo:hi),polynomial_value:rec(left?c[0]:c.at(-1))});}
  else if(depth>=maxDepth)unresolved.push({lo:rec(lo),hi:rec(hi),lower:rec(lb),upper:rec(ub)});
  else{const [left,right]=splitHalf(c),mid=div(add(lo,hi),F(2));queue.push([mid,hi,right,depth+1],[lo,mid,left,depth+1]);}
 }
 return {certified_positive:!unresolved.length&&!negative.length,leaf_count:leaves.length,maximum_depth_used:maxUsed,minimum_certified_leaf_lower:lower?rec(lower):null,positive_leaves:leaves,unresolved,nonpositive_witnesses:negative};
}

function pmul(a,b){const p=Array(a.length+b.length-1).fill(null).map(Z);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)p[i+j]=add(p[i+j],mul(a[i],b[j]));return p;}
function peval(p,x){return p.slice().reverse().reduce((v,a)=>add(mul(v,x),a),Z());}
function bernsteinIdentity(power){
 const b=bernstein(power),n=b.length-1;
 for(const t of [F(0),F(1,4),F(1,2),F(3,4),F(1)]){
  const x=sub(mul(F(2),t),O());let right=Z();
  for(let k=0;k<=n;k++)right=add(right,mul(mul(F(binom(n,k)),b[k]),mul(pow(t,k),pow(sub(O(),t),n-k))));
  if(cmp(peval(power,x),right)!==0)throw Error("Bernstein identity");
 }
 return true;
}
function directLeafCheck(power,certificate){
 const n=power.length-1;
 const read=o=>F(o.numerator,o.denominator);
 const leaves=certificate.positive_leaves.slice().sort((a,b)=>cmp(read(a.lo),read(b.lo)));
 let prior=F(-1);
 for(const leaf of leaves){
  const lo=read(leaf.lo),hi=read(leaf.hi),h=sub(hi,lo);
  if(cmp(lo,prior)!==0||cmp(h,Z())<=0)throw Error("leaf coverage");
  const local=[];
  for(let j=0;j<=n;j++){
   let a=Z();for(let k=j;k<=n;k++)a=add(a,mul(mul(power[k],F(binom(k,j))),pow(lo,k-j)));
   local.push(mul(a,pow(h,j)));
  }
  const b=[];for(let i=0;i<=n;i++){let a=Z();for(let j=0;j<=i;j++)a=add(a,mul(local[j],F(binom(i,j),binom(n,j))));b.push(a);}
  if(cmp(min(b),read(leaf.lower))!==0||cmp(min(b),Z())<=0)throw Error("direct leaf coefficient lower differs");
  prior=hi;
 }
 if(cmp(prior,O())!==0)throw Error("incomplete angular interval");
 return true;
}
function main(){
 const L=fromFloat(3.1496673569886275),coeff=[fromFloat(.09),fromFloat(-.006363961030678927)],frequency=[2,4];
 const d=coeff.map((q,j)=>mul(F(1-frequency[j]*frequency[j]),q));
 const vertex=div(F(-d[0][0],d[0][1]),mul(F(4),d[1]));
 if(cmp(d[1],Z())<=0||cmp(vertex,F(-1))<0||cmp(vertex,O())>0)throw Error("quadratic minimum domain");
 const rhoCoreMin=sub(sub(O(),d[1]),div(mul(d[0],d[0]),mul(F(8),d[1])));
 const rhoMin=min([O(),rhoCoreMin]);requirePositive(rhoMin,"positive chart");
 const A=F(143,1000),Rp=F(81,100);
 const A2=pmul([O(),Z(),F(-1)],pmul([div(d[0],F(2)),div(d[1],F(2))],[div(d[0],F(2)),div(d[1],F(2))]));
 const R2=pmul([O(),Z(),F(-1)],pmul([mul(F(-2),d[0]),mul(F(-8),d[1])],[mul(F(-2),d[0]),mul(F(-8),d[1])]));
 const Acheck=polyadd([mul(A,A)],A2,F(-1)),Rcheck=polyadd([mul(Rp,Rp)],R2,F(-1));
 const Apay=positiveCertificate(Acheck,12),Rpay=positiveCertificate(Rcheck,12);
 if(!Apay.certified_positive||!Rpay.certified_positive)throw Error("quartic bounds");
 const D=add(F(absBig(d[0][0]),d[0][1]),F(absBig(d[1][0]),d[1][1]));
 const B1=div(F(15,8),L),B2=div(F(6),mul(L,L));
 const thetaS=mul(B1,A),rhoS=mul(B1,D),thetaSS=mul(B2,A);
 const v=div(thetaS,rhoMin),vp=div(add(rhoS,mul(v,Rp)),rhoMin),vs=div(add(thetaSS,mul(v,rhoS)),rhoMin);
 const decimalCaps={rho_lower: F(80908,100000),v_upper:F(105216,1000000),vp_upper:F(374231,1000000),vs_upper:F(135190,1000000)};
 if(cmp(rhoMin,decimalCaps.rho_lower)<=0||cmp(v,decimalCaps.v_upper)>=0||
    cmp(vp,decimalCaps.vp_upper)>=0||cmp(vs,decimalCaps.vs_upper)>=0)throw Error("outward decimal caps");
 const weights={
  position:[O(),Z(),Z(),Z(),Z(),Z()],
  s:[Z(),O(),v,Z(),Z(),Z()],
  theta:[Z(),Z(),div(O(),rhoMin),Z(),Z(),Z()],
  ss:[Z(),Z(),add(mul(v,vp),vs),O(),mul(F(2),v),mul(v,v)],
  s_theta:[Z(),Z(),div(vp,rhoMin),Z(),div(O(),rhoMin),div(v,rhoMin)],
  theta_theta:[Z(),Z(),div(Rp,pow(rhoMin,3)),Z(),Z(),div(O(),pow(rhoMin,2))]
 };
 return {
  scope:"Exact common-chart transport constants for the accepted q096 finite-field comparison. No M24/M28 field difference or mean bound has been evaluated.",
  source_summary:"notes/2026-11-12-strong-actual-q096-ci-actions-43302113873-1-strong-summary.json",
  source_summary_sha256:"c3291bbc2de37008f5a9272e762c628a3f4e95106b3382d6253bf4a5b14c3c2a",
  source_reference_lines:[180,187],source_length_lines:[740,762],
  chart_source_sha256:"7678b2b43984b74c94b948efb21ea014f75a25841ed40527e0b76c569190e0cb",
  input:{length:rec(L),coefficients:coeff.map(rec),frequencies:frequency,transition_start:0,transition_end:1},
  exact_polynomial:"rho_core=1-d4+d2*x+2*d4*x^2, x=cos(2*psi)",
  minimum_vertex_x:rec(vertex),rho_min:rec(rhoMin),rho_core_minus_one_abs_bound:rec(D),
  arc_offset_abs_cap:rec(A),rho_psi_abs_cap:rec(Rp),
  arc_offset_squared_cap_certificate:Apay,rho_psi_squared_cap_certificate:Rpay,
  blend_first_abs_bound:rec(B1),blend_second_abs_bound:rec(B2),
  chart_velocity_abs_bound:rec(v),chart_velocity_psi_abs_bound:rec(vp),chart_velocity_s_abs_bound:rec(vs),
  verified_outward_decimal_caps:Object.fromEntries(Object.entries(decimalCaps).map(([k,v])=>[k,rec(v)])),
  error_input_columns:["E00","E10","E01","E20","E11","E02"],
  exact_finite_field_transport_matrix:Object.fromEntries(Object.entries(weights).map(([name,row])=>[name,row.map(rec)])),
  independent_mean_additions:{position:"A0",s:"A1",theta:0,ss:"A2",s_theta:0,theta_theta:0},
  checks:{quadratic_minimizer_in_interval:true,rho_lower_positive:true,
   arc_quartic_bernstein_identity:bernsteinIdentity(Acheck),rho_quartic_bernstein_identity:bernsteinIdentity(Rcheck),
   arc_quartic_independent_leaf_and_full_coverage:directLeafCheck(Acheck,Apay),
   rho_quartic_independent_leaf_and_full_coverage:directLeafCheck(Rcheck,Rpay),
   blend_second_squared_bound:100<108,display_decimal_caps_are_outward:true},
  limitations:["Bounds concern the exact analytic chart with binary64 metadata interpreted as exact reals, not its floating-point evaluation error.",
   "The M28 field is not yet computed. These constants alone do not bound a finite-field difference.",
   "Complete height-mean errors A0,A1,A2 still require continuous bounds; finite quadrature/sample values are not substituted.",
   "Piecewise finite-polynomial jets include both one-sided limits. Floating-point knot continuity is a separate check.",
   "A finite-pair bound is not convergence to an exact immersion, a reach proof, or a closed-family result."]
 };
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(main(),null,2));
