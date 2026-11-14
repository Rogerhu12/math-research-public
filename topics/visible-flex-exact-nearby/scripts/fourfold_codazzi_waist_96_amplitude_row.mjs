#!/usr/bin/env node
/** Complete physical waist amplitude row, all 96 head columns and the mean. */
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
function calculate(){
const data={"candidate_sha256":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413","alpha":"6890507429876859/9007199254740992","radius":["53436641/50000000","1068732841/1000000000"],"V":["1270129564654771/158456325028528675187087900672","2864496691872449/2251799813685248","1624098663981119/144115188075855872","-5192475905313877/1152921504606846976","3207928299402237/18446744073709551616","8478816635014769/147573952589676412928","-2368231246518113/1180591620717411303424","-241215380024263/295147905179352825856","-7488681247664523/302231454903657293676544","1680147733147791/302231454903657293676544","2508528725620295/9671406556917033397649408","-3887138776749025/77371252455336267181195264","-1066351861434367/309485009821345068724781056","8296177205370157/19807040628566084398385987584","5629761606212273/158456325028528675187087900672","-4861405037374475/633825300114114700748351602688","-6979762178234097/10141204801825835211973625643008","1843513710930941/20282409603651670423947251286016","5718599097241473/649037107316853453566312041152512","-40196755016835/324518553658426726783156020576256","-15433068265181/5192296858534827628530496329220096","1656983633614179/10384593717069655257060992658440192","-265068066504897/649037107316853453566312041152512","185919756031151/2596148429267413814265248164610048","7413412059233215/20769187434139310514121985316880384","-286349145547645/324518553658426726783156020576256","-8537671162694723/10384593717069655257060992658440192","-4276107853106963/10384593717069655257060992658440192","88795069357391/1298074214633706907132624082305024","-41329815694417/2596148429267413814265248164610048","-2699806148147159/1298074214633706907132624082305024","-147053166086193/162259276829213363391578010288128","53994010478195/1298074214633706907132624082305024"],"reference_cos4_interval":["-0.627611118976129017","-0.609577561809481048"],"reference_mean_interval":["-1.276033052468980174799328","-1.276014207147490866328027"],"waist_input_sha256":"8066f501acc87d42e7d58f30377680aaa317be500471fa71bcceef336fc9357b","mean_input_sha256":"63986d47452a34f0b52a70ebfa40aad7630eba2e0f47ec39274ac6e83f0b5b56"};
const scale=2n**384n;
const floorDiv=(a,b)=>a<0n?-((-a+b-1n)/b):a/b;
const ceilDiv=(a,b)=>-floorDiv(-a,b);
const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;};
function q(n,d=1n){if(typeof n==='string'){if(n.includes('/')){const t=n.split('/');n=t[0];d=t[1];}
 else if(n.includes('.')){let sign=1n;if(n[0]==='-'){sign=-1n;n=n.slice(1);}const t=n.split('.');d=10n**BigInt(t[1].length);n=sign*BigInt(t[0]+t[1]);}}
 n=BigInt(n);d=BigInt(d);if(d<0n){n=-n;d=-d;}if(!d)throw Error('zero rational denominator');const g=gcd(n,d);return {n:n/g,d:d/g};}
const qa=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),qn=a=>q(-a.n,a.d),qs=(a,b)=>qa(a,qn(b));
const qm=(a,b)=>q(a.n*b.n,a.d*b.d),qd=(a,b)=>q(a.n*b.d,a.d*b.n);
const qabs=a=>a.n<0n?qn(a):a,qcmp=(a,b)=>a.n*b.d-b.n*a.d;
const fixed=a=>[floorDiv(a.n*scale,a.d),ceilDiv(a.n*scale,a.d)];
const hull=(a,b)=>[a[0]<b[0]?a[0]:b[0],a[1]>b[1]?a[1]:b[1]];
const zero=()=>[0n,0n],one=()=>[scale,scale];
const add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[1],-a[0]],sub=(a,b)=>add(a,neg(b));
const rawProduct=(a,b)=>{const z=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]];let lo=z[0],hi=z[0];for(const x of z){if(x<lo)lo=x;if(x>hi)hi=x;}return [lo,hi];};
const mul=(a,b)=>{const z=rawProduct(a,b);return [floorDiv(z[0],scale),ceilDiv(z[1],scale)];};
const divInteger=(a,n)=>[floorDiv(a[0],BigInt(n)),ceilDiv(a[1],BigInt(n))];
const mulDiv=(a,b,n)=>{const z=rawProduct(a,b),den=scale*BigInt(n);return [floorDiv(z[0],den),ceilDiv(z[1],den)];};
const absUpper=a=>{const x=a[0]<0n?-a[0]:a[0],y=a[1]<0n?-a[1]:a[1];return x>y?x:y;};
const strFixed=x=>{const a=q(x,scale);return a.n+'/'+a.d;};
function dec(x,up,d=72){const S=10n**BigInt(d),r=up?ceilDiv(x*S,scale):floorDiv(x*S,scale);
 const sign=r<0n?'-':'',a=(r<0n?-r:r).toString().padStart(d+1,'0');return sign+a.slice(0,-d)+'.'+a.slice(-d);}
const interval=a=>({lower:dec(a[0],false),upper:dec(a[1],true)});
const alpha=q(data.alpha),V=data.V.map(x=>q(x)),al=q(data.radius[0]),au=q(data.radius[1]);
if(V.length!==33)throw Error('the complete actual waist vector is required');
const g0=qs(al,qm(alpha,V[0])),g1=qs(au,qm(alpha,V[0]));
if(qcmp(g0,q(1))<=0)throw Error('actual mean gap');
const inv2=hull(fixed(qd(q(1),qm(g0,g0))),fixed(qd(q(1),qm(g1,g1))));
const tau=hull(fixed(qd(qm(alpha,V[1]),g0)),fixed(qd(qm(alpha,V[1]),g1)));
const fullPhase=new Map(),epsilon=[];
let epsBound=0n;
for(let j=1;j<=32;j++){
 const numerator=qm(alpha,V[j]);
 const a=qd(qn(numerator),qm(q(2*j),g0)),b=qd(qn(numerator),qm(q(2*j),g1));
 const p=hull(fixed(a),fixed(b));
 fullPhase.set(j,p);fullPhase.set(-j,neg(p));
 if(j>=2){epsilon.push([j,p],[-j,neg(p)]);epsBound+=2n*absUpper(p);}
}
const K=26,degree=32*K,termLimit=32;
let term=[one()],termDegree=0;
const E=Array.from({length:2*degree+1},zero);E[degree]=one();
for(let n=1;n<=K;n++){
 const nd=termDegree+32,L=Array(2*nd+1).fill(0n),U=Array(2*nd+1).fill(0n);
 for(let i=0;i<term.length;i++){
  const a=term[i];if(a[0]===0n&&a[1]===0n)continue;
  for(const [j,p] of epsilon){
   const z=rawProduct(a,p),dest=i+32+j;
   L[dest]+=z[0];U[dest]+=z[1];
  }
 }
 const den=scale*BigInt(n);
 term=L.map((x,i)=>[floorDiv(x,den),ceilDiv(U[i],den)]);termDegree=nd;
 for(let i=0;i<term.length;i++)E[degree-nd+i]=add(E[degree-nd+i],term[i]);
}
let tailTerm=scale;
for(let n=1;n<=K+1;n++)tailTerm=ceilDiv(tailTerm*epsBound,scale*BigInt(n));
const expRatio=ceilDiv(epsBound,BigInt(K+2));
if(expRatio>=scale)throw Error('complete higher phase remainder ratio failed');
const expTail=ceilDiv(tailTerm*scale,scale-expRatio);
const coefficientTail=3n*expTail; // exp(tau)<=e<3, because actual 0<tau<1.
const qTau=divInteger(mul(tau,tau),4);
const maxBessel=degree+97,J=[];
let pref=one(),largestBesselTail=0n;
for(let n=0;n<=maxBessel;n++){
 let t=pref,sum=pref;
 for(let l=1;l<=termLimit;l++){t=mulDiv(t,qTau,l*(n+l));sum=l%2?sub(sum,t):add(sum,t);}
 const next=mulDiv(t,qTau,(termLimit+1)*(n+termLimit+1));
 const ratio=ceilDiv(qTau[1],BigInt((termLimit+2)*(n+termLimit+2)));
 if(ratio>=scale)throw Error('complete Bessel ratio failed');
 const fee=ceilDiv(next[1]*scale,scale-ratio);
 if(fee>largestBesselTail)largestBesselTail=fee;
 const out=[sum[0]-fee,sum[1]+fee];
 if(out[1]<0n)throw Error('the positive true Bessel range was lost');
 if(out[0]<0n)out[0]=0n; // Alternating decreasing series for 0<tau<1.
 J.push(out);
 pref=mulDiv(pref,tau,2*(n+1));
}
function mainCoefficient(n){
 const x=J[Math.abs(n)];
 return n>=0&&n%2?neg(x):x;
}
const A=new Map();
for(let n=-97;n<=95;n++){
 let L=0n,U=0n;
 for(let l=-degree;l<=degree;l++){
  const e=E[l+degree];if(e[0]===0n&&e[1]===0n)continue;
  const z=rawProduct(e,mainCoefficient(n-l));L+=z[0];U+=z[1];
 }
 A.set(n,[floorDiv(L,scale)-coefficientTail,ceilDiv(U,scale)+coefficientTail]);
}
const rows=[];let largestWidth=0n;
for(let j=1;j<=96;j++){
 const d=neg(divInteger(mul(inv2,sub(A.get(j-1),A.get(-j-1))),j));
 if(d[1]-d[0]>largestWidth)largestWidth=d[1]-d[0];
 rows.push({moving_index:j,physical_frequency:4*j,
   physical_cosine_amplitude_derivative:interval(d),
   exact_interval_numerator_at_scale:[d[0].toString(),d[1].toString()]});
}
let meanIntegrand=neg(A.get(-1));
for(const [j,p] of fullPhase)meanIntegrand=sub(meanIntegrand,mul(p,A.get(-j-1)));
const meanColumn=mul(inv2,meanIntegrand).map(x=>2n*x);
const gates=[];
function g(name,ok,details={}){if(!ok)throw Error(name);gates.push({name,passed:true,...details});}
g('complete actual 33-term waist input',V.length===33);
g('true mean gap greater than one',qcmp(g0,q(1))>0);
g('actual primary Bessel phase positive and below one',tau[0]>0n&&tau[1]<scale,{phase_interval:interval(tau)});
g('all j2..32 phase terms including tiny stored values retained',epsilon.length===62);
g('complete higher phase bound',epsBound*500n<3n*scale,{upper:strFixed(epsBound)});
g('complete higher phase exponential tail',expTail*10n**80n<scale,{upper:strFixed(expTail)});
g('all Bessel indices and complete radial series tail',J.length===maxBessel+1&&largestBesselTail*10n**80n<scale,{maximum_index:maxBessel,upper:strFixed(largestBesselTail)});
g('complete 96 physical cosine derivative columns',rows.length===96);
const first=[BigInt(rows[0].exact_interval_numerator_at_scale[0]),BigInt(rows[0].exact_interval_numerator_at_scale[1])];
const oldFirst=data.reference_cos4_interval.map(x=>q(x));
g('actual first cosine column lies strictly in previous whole-ball certificate',
 qcmp(q(first[0],scale),oldFirst[0])>0&&qcmp(q(first[1],scale),oldFirst[1])<0);
const oldMean=data.reference_mean_interval.map(x=>q(x));
g('actual mean column lies strictly in previous full mean certificate',
 qcmp(q(meanColumn[0],scale),oldMean[0])>0&&qcmp(q(meanColumn[1],scale),oldMean[1])<0);
g('all actual cosine column widths below 1e-5',largestWidth*100000n<scale,{upper:strFixed(largestWidth)});
g('full current mean column width below 1e-5',(meanColumn[1]-meanColumn[0])*100000n<scale);
return {kind:'actual_final_complete_96_physical_waist_amplitude_Jacobi_row',
 complete:true,executed:true,arithmetic:'signed outward fixed-point BigInt intervals at denominator 2^384, complete Bessel and exponential tails',
 candidate_sha256:data.candidate_sha256,whole_original_eta:true,exact_inputs:data,
 exact_interval_denominator:scale.toString(),actual_mean_abs_interval:{lower:g0.n+'/'+g0.d,upper:g1.n+'/'+g1.d},
 actual_phase_interval:interval(tau),higher_phase_A0_upper:strFixed(epsBound),
 complete_higher_phase_polynomial_degree:degree,higher_phase_exponential_order:K,
 complete_higher_phase_A0_tail:strFixed(expTail),complete_convolution_coefficient_tail:strFixed(coefficientTail),
 maximum_Bessel_order:maxBessel,Bessel_terms:termLimit+1,complete_Bessel_tail_upper:strFixed(largestBesselTail),
 complete_actual_mean_amplitude_derivative:interval(meanColumn),
 exact_mean_interval_numerator_at_scale:meanColumn.map(x=>x.toString()),
 complete_odd_u_derivative_columns:'all exactly zero',
 physical_even_column_coordinates:'h2=z+sum_j a_j cos(4j phi), unnormalized physical moving variation; entries are D A[cos(4j phi)], not gradient cosine amplitudes',
 rows,all_96_head_columns_retained:true,
 full_unknown_high_L2_dual_tail_reference:{path:'notes/2026-11-14-R133-final-waist-high-amplitude-tail-rational.json',sha256:'19fc31617d033a4dcdc92153498592290da23ae58b545f3c5f64dc0ca343a3d9',current_centre_upper:'1e-42'},
 new_centre_row_not_transferred_to_unknown_Wiener_ball:true,
 gate_count:gates.length,gates,actual_full_radial_trial_present:false,
 actual_nu_Schur_nonzero_proved:false,complete_BVP_inverse_proved:false};
}
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('usage: node this.mjs --out NEW_REPORT.json');
const report=calculate();
report.producer_sha256=createHash('sha256').update(await readFile(fileURLToPath(import.meta.url))).digest('hex');
await writeFile(args[1],JSON.stringify(report,null,2)+'\n',{flag:'wx'});
if(!report.complete)process.exitCode=1;
console.log(JSON.stringify({complete:report.complete,gate_count:report.gate_count,out:args[1]}));
