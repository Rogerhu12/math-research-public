"use strict";
/* Exact replay of strong_core_corridor_refresh.py for the original accepted
 * q096 summary coefficients. Pure rational computation; no prefix/tail solve.
 * The floating decimal displays are informational only. */
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r;}return a;}
function F(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return[n/g,d/g];}
const Z=()=>[0n,1n],O=()=>[1n,1n];
const add=(a,b)=>F(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>F(a[0]*b[0],a[1]*b[1]);
const div=(a,b)=>F(a[0]*b[1],a[1]*b[0]);
const cmp=(a,b)=>{const d=a[0]*b[1]-b[0]*a[1];return d<0n?-1:d>0n?1:0;};
const abs=a=>a[0]<0n?neg(a):a;
const sum=a=>a.reduce(add,Z());
const min=a=>a.reduce((x,y)=>cmp(x,y)<=0?x:y),max=a=>a.reduce((x,y)=>cmp(x,y)>=0?x:y);
const rec=a=>({numerator:a[0].toString(),denominator:a[1].toString(),decimal_display:Number(a[0])/Number(a[1])});
function decimal(s){if(!/^-?[0-9]+(\.[0-9]+)?$/.test(s))throw Error("decimal");const q=s.split(".");return F(BigInt(q.join("")),10n**BigInt(q[1]?.length??0));}
function fromFloat(x){
 if(!Number.isFinite(x))throw Error("nonfinite input");
 const b=new ArrayBuffer(8),v=new DataView(b);v.setFloat64(0,x,false);
 const hi=v.getUint32(0,false),lo=v.getUint32(4,false);
 const sign=(hi>>>31)?-1n:1n,exponent=(hi>>>20)&2047;
 let mantissa=(BigInt(hi&1048575)<<32n)+BigInt(lo),e;
 if(exponent===0)e=-1074;else{mantissa+=(1n<<52n);e=exponent-1023-52;}
 return e>=0?F(sign*(mantissa<<BigInt(e))):F(sign*mantissa,1n<<BigInt(-e));
}
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
function main(){
 const numbers=[
  .09599996014428179,-.006718093057120565,-.00041367333804088465,
  -8.163704447421332e-05,-3.249955389806626e-05,2.1154336872755326e-05,
  1.447778863436384e-05,-6.131388312117053e-06,-7.135535766629933e-07,
  -2.23899654214933e-06,-2.6764421496681754e-06,-6.719257621786248e-07,
  -5.688710875603695e-07,2.2406668284416053e-07,1.156214079792537e-07,
  -8.180817339803354e-09,4.704333485835285e-08,1.5324667477040568e-08,
  4.313421357991321e-09,3.326754781168885e-08,6.456814403875876e-09,
  -8.468662408593604e-09,3.0794386861890594e-09,1.6740527264404394e-08];
 const c=numbers.map(fromFloat),target=decimal("0.402"),muLo=decimal("0.7071067811865475"),muHi=decimal("0.7071067811865476");
 if(!(cmp(mul(muLo,muLo),F(1,2))<0&&cmp(mul(muHi,muHi),F(1,2))>0))throw Error("sqrt2 bracket");
 const mu=div(add(muLo,muHi),F(2)),oddTail=sum(c.filter((x,i)=>i+1>=3&&(i+1)%2));
 const highL1=sum(c.map((x,i)=>i>=2?mul(F(4*(i+1)**2-1),abs(x)):Z()));
 const epsilon=max([muLo,muHi].map(u=>abs(add(c[1],div(mul(c[0],u),F(10))))));
 const endpoints=[];
 for(const q of [c[0],target]){
  const current=c.slice();current[0]=q;current[1]=sub(c[1],div(mul(sub(q,c[0]),mu),F(10)));
  const c4err=div(mul(sub(q,c[0]),sub(muHi,muLo)),F(20)),rhoerr=mul(F(15),c4err);
  const gap=mul(F(2),add(q,oddTail)),diam=mul(F(5),gap),required=mul(F(3,100),diam);
  const cheb=[sub(sub(O(),required),rhoerr),...current.map((x,i)=>mul(F(-(4*(i+1)**2-1)),x))];
  const power=chebyshevPower(cheb),certificate=positiveCertificate(power);
  const axisMid=sub(O(),sum(current.map((x,i)=>mul(F((4*(i+1)**2-1)*(((i+1)%2)?-1:1)),x))));
  const axisUpper=add(axisMid,rhoerr),product=mul(mul(fromFloat(.45),gap),axisUpper);
  const simple=sub(sub(sub(O(),mul(mul(F(3),q),muHi)),mul(F(15),epsilon)),highL1);
  endpoints.push({actual_q:rec(q),c4_midpoint:rec(current[1]),c4_error_bound:rec(c4err),
   rho_uniform_error_from_sqrt2:rec(rhoerr),axial_support_gap:rec(gap),
   core_distance_diameter_budget:rec(diam),required_radius:rec(required),
   simple_l1_rho_lower:rec(simple),simple_l1_radius_surplus:rec(sub(simple,required)),
   short_axis_rho_upper:rec(axisUpper),R7_initial_witness_product_upper:rec(product),
   R7_less_than_one:cmp(product,O())<0,R7_less_than_point95:cmp(product,F(19,20))<0,
   polynomial_power_coefficients:power.map(rec),radius_surplus_certificate:certificate});
 }
 const evalPower=(power,x)=>power.reduceRight((acc,coef)=>add(mul(acc,x),coef),Z());
 const checkPoints=[F(-1),F(-3,4),F(-1,2),Z(),F(1,2),F(3,4),O()];
 let allCovered=true,endpointValuesPositive=true;
 for(const row of endpoints){
  const cert=row.radius_surplus_certificate;
  const parseRec=r=>F(r.numerator,r.denominator);
  let at=F(-1);
  for(const leaf of cert.positive_leaves){
   if(cmp(parseRec(leaf.lo),at)!==0||cmp(parseRec(leaf.lower),Z())<=0)allCovered=false;
   at=parseRec(leaf.hi);
  }
  if(cmp(at,O())!==0)allCovered=false;
  const power=row.polynomial_power_coefficients.map(parseRec);
  for(const x of checkPoints)if(cmp(evalPower(power,x),Z())<=0)endpointValuesPositive=false;
  const b=bernstein(power),n=power.length-1;
  for(const t of [Z(),F(1,4),F(1,2),F(3,4),O()]){
   const x=sub(mul(F(2),t),O());
   const pow=(v,k)=>{let z=O();for(let i=0;i<k;i++)z=mul(z,v);return z;};
   const atT=sum(b.map((v,i)=>mul(mul(mul(v,F(binom(n,i))),pow(t,i)),pow(sub(O(),t),n-i))));
   if(cmp(atT,evalPower(power,x))!==0)throw Error("Bernstein/power identity");
  }
 }
 if(!allCovered||!endpointValuesPositive)throw Error("certificate coverage/checkpoints");
 const arithmeticChecks={
  all_binary64_coefficients_roundtrip:numbers.every((x,i)=>Number(c[i][0])/Number(c[i][1])===x),
  complete_exact_leaf_partition:allCovered,
  endpoint_polynomials_positive_at_seven_rational_points:endpointValuesPositive,
  Bernstein_power_exact_agreement_at_five_rational_points:true,
  inverse_sqrt2_bracket_squared_exact:true
 };
 if(!Object.values(arithmeticChecks).every(Boolean))throw Error("exact arithmetic check");
 const end=endpoints.at(-1);
 return {arithmetic_checks:arithmeticChecks,
  scope:"Exact rational endpoint Bernstein check of an artificial planar-core path; no new prefix/tail/geometry solve.",
  input_summary:"notes/2026-11-12-strong-actual-q096-ci-actions-43302113873-1-strong-summary.json",
  input_summary_sha256:"c3291bbc2de37008f5a9272e762c628a3f4e95106b3382d6253bf4a5b14c3c2a",
  input_summary_lines:[675,825],coefficients_read_from_original_summary:true,
  source_solver_success:true,source_audit_pending:false,representation_gauge:.09,
  source_metric_sample:6.333190867485509e-7,source_actual_primary:numbers[0],
  exact_source_coefficients:c.map(rec),landing_q:rec(target),
  inverse_sqrt_two_interval:[rec(muLo),rec(muHi)],high_mode_weighted_l1:rec(highL1),
  endpoints,planar_corridor_radius_budget_certified:endpoints.every(r=>r.radius_surplus_certificate.certified_positive),
  planar_corridor_R7_less_than_one:end.R7_less_than_one,
  whole_path_reason:"For every fixed x=cos(2 phi), the lower polynomial rho(q,x)-.15*d(q) is affine in q; positive endpoint Bernstein enclosures prove the segment. d>0 and the positive short-axis rho upper increase with q, so the upper R7 product is maximal at the landing endpoint.",
  limitations:[
   "All actual coefficients with physical frequencies>=6 are artificially frozen along this planar path; a nonlinear continuation need not follow it.",
   "All 24 supplied binary64 coefficients are converted exactly to rational numbers; decimal displays are not proofs.",
   "D<=5d is a future whole-surface budget, not the measured diameter of this accepted prefix.",
   "No closed held, global reach, infinite tail, exact isometry family or C2 error certificate follows.",
   "New M28 core coefficients, once actually solved, require a fresh check."
  ]};
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module){
 console.log(JSON.stringify(main(),null,2));
}
