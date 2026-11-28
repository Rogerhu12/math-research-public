"use strict";
// NEW exact one-variable original Phi t=0,f=u,ell=1/2,w=0 branch.
// Uses the newly returned complete weighted N/P equations, not the frozen
// two-variable Buchberger ideal. All removed factors have explicit branch proofs.
const started=Date.now();let arithmetic=0,products=0,divisions=0;
function gcdI(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r}return a}
function R(n=0n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d}if(!n)return{n:0n,d:1n};const g=gcdI(n,d);return{n:n/g,d:d/g}}
const ZERO=R(),ONE=R(1n);
function rat(x){return typeof x==="object"&&"n" in x?x:R(x)}
function ra(a,b){arithmetic++;a=rat(a);b=rat(b);return R(a.n*b.d+b.n*a.d,a.d*b.d)}
function rn(a){a=rat(a);return{n:-a.n,d:a.d}}
function rs(a,b){return ra(a,rn(b))}
function rm(a,b){arithmetic++;a=rat(a);b=rat(b);return R(a.n*b.n,a.d*b.d)}
function rd(a,b){a=rat(a);b=rat(b);if(!b.n)throw Error("zero division");return R(a.n*b.d,a.d*b.n)}
function rz(a){return !a.n}
function trim(p){p=p.slice();while(p.length&&rz(p[p.length-1]))p.pop();return p}
function P(...xs){return trim(xs.map(rat))}
function add(a,b){return trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>ra(a[i]||ZERO,b[i]||ZERO)))}
function neg(a){return a.map(rn)}
function sub(a,b){return add(a,neg(b))}
function scale(a,c){return trim(a.map(x=>rm(x,c)))}
function mul(a,b){if(Date.now()-started>120000)throw Error("new one-variable input 120 second boundary");products++;if(!a.length||!b.length)return[];const c=Array.from({length:a.length+b.length-1},()=>ZERO);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=ra(c[i+j],rm(a[i],b[j]));return trim(c)}
function pow(a,n){let x=P(1n),y=a;while(n){if(n&1)x=mul(x,y);n>>=1;if(n)y=mul(y,y)}return x}
function sum(...a){return a.reduce(add,[])}
function prod(...a){return a.reduce(mul,P(1n))}
function shift(a,n){return Array(n).fill(ZERO).concat(a)}
function equal(a,b){return sub(a,b).length===0}
function divmod(a,b){if(!b.length)throw Error("division by zero polynomial");let r=a.slice(),q=[];while(r.length>=b.length){const k=r.length-b.length,c=rd(r.at(-1),b.at(-1)),t=shift(P(c),k);q=add(q,t);r=sub(r,mul(t,b))}if(!equal(a,add(mul(q,b),r)))throw Error("full division return");divisions++;return[q,r]}
function monic(a){return a.length?scale(a,rd(ONE,a.at(-1))):[]}
function xgcd(a,b){
 let r0=a,r1=b,s0=P(1n),s1=[],t0=[],t1=P(1n);
 while(r1.length){const[q,r]=divmod(r0,r1);[r0,r1]=[r1,r];[s0,s1]=[s1,sub(s0,mul(q,s1))];[t0,t1]=[t1,sub(t0,mul(q,t1))]}
 if(r0.length){const inv=rd(ONE,r0.at(-1));r0=scale(r0,inv);s0=scale(s0,inv);t0=scale(t0,inv)}
 if(!equal(sum(mul(s0,a),mul(t0,b)),r0))throw Error("whole QQ Bezout return");
 return[r0,s0,t0];
}
function textp(p){return p.map(x=>x.d===1n?String(x.n):String(x.n)+"/"+String(x.d))}
const u=P(0n,1n),s=P(-1n,1n),r=P(-2n,1n),head=P(-3n,2n);
const Q=scale(mul(s,r),4n),L=scale(mul(s,r),2n),K=scale(pow(s,2),4n);
const delta=sub(P(1n),Q),Mn=scale(prod(pow(s,3),r),-8n),mnum=sub(mul(u,Q),L);
const A=scale(s,4n),N=P(6n,-6n,1n),Den=scale(mul(head,r),2n);
if(!equal(sub(scale(N,2n),Den),scale(mul(u,s),-2n)))throw Error("actual n numerator");
const [,headRemainder]=divmod(N,head);
if(!equal(headRemainder,P(R(-3n,4n))))throw Error("entire head-zero branch");
const v0=sub(mul(Q,P(-1n,2n)),scale(pow(s,3),4n)),v1=scale(mul(s,L),-2n);
const VN=sum(mul(v0,Den),mul(v1,N));
const NN=sub(prod(Q,add(neg(K),scale(pow(u,2),4n)),Den),scale(VN,2n));
const SN=sub(scale(prod(L,delta,VN),2n),mul(mnum,NN));
const DN=sum(scale(mul(mnum,VN),-2n),mul(L,NN));
const Pw=sum(scale(prod(Q,Mn,L,K,pow(Den,2)),-2n),
 scale(prod(L,delta,pow(VN,2)),-4n),neg(mul(L,pow(NN,2))),
 scale(prod(mnum,VN,NN),4n),scale(prod(Q,Mn,u,VN,Den),8n));
const Po=sum(scale(prod(Q,pow(Mn,2),sub(Q,L),s,pow(Den,2)),2n),
 scale(prod(pow(Q,2),pow(Mn,2),u,pow(Den,2)),-4n),
 prod(Q,Mn,SN,Den),scale(prod(Q,pow(Mn,2),VN,Den),2n),
 prod(Q,Mn,add(u,P(1n)),DN,Den),neg(mul(SN,DN)));
const P02=mul(s,Q);
const Ep=sum(neg(prod(P02,pow(sub(scale(N,2n),Den),2),add(N,Den))),
 scale(prod(pow(u,3),pow(Den,3)),-2n));
const original=[Pw,Po,Ep],paid=[u,s,r,delta,head],normalized=[],removed=[];
for(const f of original){
 let a=f,record=[];
 for(let j=0;j<paid.length;j++){
  let n=0;while(a.length){const[q,rem]=divmod(a,paid[j]);if(rem.length)break;if(!equal(mul(q,paid[j]),a))throw Error("paid divisor return");a=q;n++}
  if(n)record.push({factor:j,power:n});
 }
 const lc=a.length?a.at(-1):ONE;
 const q=monic(a);if(!equal(scale(q,lc),a))throw Error("rational constant return");
 normalized.push(q);removed.push({factors:record,constant:lc.d===1n?String(lc.n):String(lc.n)+"/"+String(lc.d)});
}
let g=[],comb=normalized.map(()=>[]);
const gcdStages=[];
for(let i=0;i<normalized.length;i++){
 const[next,a,b]=xgcd(g,normalized[i]);comb=comb.map(x=>mul(a,x));comb[i]=add(comb[i],b);g=next;
 if(!equal(sum(...comb.map((x,j)=>mul(x,normalized[j]))),g))throw Error("full combined original QQ return");
 gcdStages.push({input:i,degree:g.length-1});
 if(g.length===1)break;
}
return {schema:"isp-true-Phi-tzero-fu-halfweight-original-return-v1",
 elapsed_milliseconds:Date.now()-started,exactRationalOperations:arithmetic,
 polynomialProducts:products,fullPolynomialDivisionReturns:divisions,
 physicalBranch:["Phi=0","t=0","f=u","ell=1/2","lambda!=1/2","w=0","Q*(1-Q)*Pf*P02*bc!=0"],
 originalRows:["Den^2*Q*W4","Den^2*Q^2*(1-Q)*Obar","Den^3*weighted_PS"],
 originalDegrees:original.map(p=>p.length-1),
 paidFactors:["u from (2lambda-1)!=0 and exact 2N-Den=-2u(u-1)","u-1","u-2","1-Q","2u-3 from exact P1 head-zero incompatibility"],
 removedContents:removed,normalizedDegrees:normalized.map(p=>p.length-1),
 originalRecovery:"Q=4(u-1)(u-2), T=lambda-1, Den*lambda=u^2-6u+6",
 noNewUnpaidHeadInverse:true,headZeroRemainder:textp(headRemainder),
 combinedWholeQQBezoutReturned:true,gcdStages,gcd:textp(g),
 combinationDegrees:comb.map(p=>p.length-1),
 branchExcluded:g.length===1,allComplexEmbeddingsKept:true,
 noOldGroebnerGateRepeated:true,originalPhiExcluded:false,ordinaryISPClaim:false};
