"use strict";
// NEW true Phi A=0: actual full Gram on the two linear true-germ branches.
// Explicitly localized only at 2,u,u-1,2u-1,2u-3.  No old compact E1.
const began=Date.now();let products=0;const DIM=3,ZK="0,0,0";
function C(n=0n){n=BigInt(n);return n===0n?new Map():new Map([[ZK,n]])}
function V(i){let e=[0,0,0];e[i]=1;return new Map([[e.join(","),1n]])}
function pa(a,b){const c=new Map(a);for(const[k,v]of b){const z=(c.get(k)||0n)+v;if(z)c.set(k,z);else c.delete(k)}return c}
function pn(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function ps(a,b){return pa(a,pn(b))}
function pm(a,b){if(Date.now()-began>120000)throw Error("new A-curve 120 second budget");products++;if(!a.size||!b.size)return C();const c=new Map();for(const[ka,va]of a){const ea=ka.split(",").map(Number);for(const[kb,vb]of b){const eb=kb.split(",").map(Number),k=ea.map((x,i)=>x+eb[i]).join(","),v=(c.get(k)||0n)+va*vb;if(v)c.set(k,v);else c.delete(k)}}return c}
const PU=V(0),PL=V(1),PA=V(2),PS=ps(PU,C(1)),PB=ps(pm(C(2),PU),C(1)),PH=ps(pm(C(2),PU),C(3));
const atoms=[C(2),PU,PS,PB,PH],powerCaches=atoms.map(p=>[C(1),p]);
function pp(i,n){const a=powerCaches[i];while(a.length<=n)a.push(pm(a.at(-1),atoms[i]));return a[n]}
function mulDen(n,e){for(let i=0;i<5;i++)if(e[i])n=pm(n,pp(i,e[i]));return n}
function F(n=C(),e=[0,0,0,0,0]){if(!n.size)return{n:C(),e:[0,0,0,0,0]};return{n,e:e.slice()}}
function cf(n){return F(C(n))}
function fa(a,b){if(!a.n.size)return b;if(!b.n.size)return a;const e=a.e.map((x,i)=>Math.max(x,b.e[i]));return F(pa(mulDen(a.n,e.map((x,i)=>x-a.e[i])),mulDen(b.n,e.map((x,i)=>x-b.e[i]))),e)}
function fn(a){return F(pn(a.n),a.e)}
function fs(a,b){return fa(a,fn(b))}
function fm(a,b){return F(pm(a.n,b.n),a.e.map((x,i)=>x+b.e[i]))}
function fc(a,n){return fm(a,cf(n))}
function fq(a){return fm(a,a)}
function fp(a,n){let v=cf(1);while(n--)v=fm(v,a);return v}
function inv(i){const e=[0,0,0,0,0];e[i]=1;return F(C(1),e)}
function sum(xs){return xs.reduce(fa,cf(0))}
function prod(xs){return xs.reduce(fm,cf(1))}
const U=F(PU),Lam=F(PL),AA=F(PA),S=F(PS),B=F(PB),H=F(PH),one=cf(1),zero=cf(0);
const half=inv(0),ell=prod([U,half,inv(2)]),aw=fs(one,ell),Q=fc(fq(S),4),delta=fs(one,Q);
const bc=prod([fq(U),fq(half),inv(2),inv(3)]);
function q(v=zero,w=zero){return[v,w]}
function qa(v,w){return[fa(v[0],w[0]),fa(v[1],w[1])]}
function qn(v){return[fn(v[0]),fn(v[1])]}
function qs(v,w){return qa(v,qn(w))}
function qm(v,w){return[fa(fm(v[0],w[0]),prod([delta,v[1],w[1]])),fa(fm(v[0],w[1]),fm(v[1],w[0]))]}
function qc(v,n){return[v[0]&&fc(v[0],n),fc(v[1],n)]}
function qt(v,w){return qm(q(v),w)}
function conj(v){return[v[0],fn(v[1])]}
const bp=q(prod([U,fq(half),inv(2)]),fn(prod([U,fq(half),inv(2),inv(3)]))),cp=conj(bp);
const ppair=q(one,one),qpair=conj(ppair),unit=[q(one),q(),q(one),q(one)];
function vm(v,w){return[qm(v[0],w[0]),qa(qm(v[0],w[1]),qm(v[1],w[0])),qm(v[2],w[2]),qm(v[3],w[3])]}
function va(v,w){return v.map((x,i)=>qa(x,w[i]))}
function vs(v,w){return w.map(x=>qm(v,x))}
function tau(v){return[qt(aw,v[0]),v[1],qm(bp,v[2]),qm(cp,v[3])].reduce(qa,q())}
const checks=[];function ck(name,v){for(const p of (Array.isArray(v)?v:[v]))if(p.n.size)throw Error(name+": "+p.n.size+" nonzero terms");checks.push(name)}
function pure(name,v){ck(name+"_odd",v[1]);return v[0]}
function info(v){let deg=[-1,-1,-1];for(const k of v.n.keys()){const e=k.split(",").map(Number);deg=deg.map((a,i)=>Math.max(a,e[i]))}return{degrees:deg,terms:v.n.size,denominatorPowers:v.e}}
function rawTerms(v,max=150){return v.n.size<=max?[...v.n].map(([k,n])=>[k,String(n)]):null}
const output=[],realRows=[];
for(const branch of [1]){
 const f=branch===1?fa(U,fm(half,AA)):fs(fs(U,fm(U,Lam)),fm(half,AA));
 const T=branch===1?fn(prod([half,inv(2),fa(fm(U,fa(fc(Lam,2),one)),AA)])):prod([half,inv(2),fs(AA,U)]);
 const xx=branch===1?fs(fa(U,AA),fm(S,Lam)):fs(U,fm(B,Lam));
 const yy=branch===1?fm(fs(fs(U,cf(2)),fm(S,Lam)),inv(4)):fm(sum([U,cf(-2),Lam,AA]),inv(4));
 const X=q(xx,yy),Y=conj(X),tt=prod([cf(2),B,AA,inv(1)]);
 const A1=branch===1?fa(AA,fc(fm(U,Lam),2)):fn(AA);
 const rr=qs(qs(X,qt(aw,ppair)),qt(tt,cp)),ss=conj(rr);
 const rows=[[q(),q(),ppair,qpair],[q(),q(A1),rr,ss],[ppair,rr,q(),q(tt)],[qpair,ss,q(tt),q()]];
 function DK(v){return rows.map(row=>tau(vm(row,v)))}
 const dv=DK(unit),F2=tau(dv),Kd=DK(dv),dd=vm(dv,dv);
 ck("b"+branch+"_actual_f",qs(F2,q(fc(f,2))));
 function mean(j){const v=j===1?qc(tau(vm(rows[0],rows[1])),2):tau(vm(rows[j],rows[j]));
  return [v,qc(Kd[j],-2),qc(dd[j],-2),qc(qm(F2,dv[j]),2)].reduce(qa,q())}
 function centered(v){return va(v,vs(qn(tau(v)),unit))}
 function P2(v){const z=centered(v);return tau(vm(vm(z,z),z))}
 function N4(v){const tv=tau(v),vv=vm(v,v);
  return[qc(tau(vm(dv,vv)),2),qn(qm(F2,tau(vv))),qc(qm(tv,tau(vm(dv,v))),-4),
   qc(qm(F2,qm(tv,tv)),2),tau(vm(v,DK(v)))].reduce(qa,q())}
 const P02=pure("b"+branch+"_P02",P2(rows[0]));
 ck("b"+branch+"_P02_identity",fs(P02,prod([cf(4),U,fq(S)])));
 const N0=N4(rows[0]),Pj=qc(tau(vm(vm(centered(rows[0]),centered(rows[0])),centered(rows[1]))),3);
 const ww=fs(fs(Lam,one),T);
 ck("b"+branch+"_E0",mean(0));
 ck("b"+branch+"_true_germ_minus_weighted_mean",qs(mean(1),qa(qm(bp,mean(2)),qm(cp,mean(3)))));
 ck("b"+branch+"_N0",qs(N0,q(prod([cf(2),Lam,P02]))));
 ck("b"+branch+"_Pjet",qs(Pj,q(prod([cf(3),ww,P02]))));
 const EB=mean(2),EC=mean(3);ck("b"+branch+"_mean_conjugacy",qs(EC,conj(EB)));
 const Nj=qs(qs(N4(va(rows[0],rows[1])),N4(rows[0])),N4(rows[1]));
 const n1=pure("b"+branch+"_N1",qs(Nj,q(prod([cf(4),Lam,ww,P02]))));
 const NW=qa(qm(bp,N4(rows[2])),qm(cp,N4(rows[3])));
 const PW=qa(qm(bp,P2(rows[2])),qm(cp,P2(rows[3])));
 const A2=sum([fc(fq(Lam),2),fc(Lam,-2),one]);
 const B3=sum([fc(fp(Lam,3),4),fc(fq(Lam),-6),fc(Lam,3),cf(-1)]);
 const ns=pure("b"+branch+"_NS",qs(NW,q(prod([cf(2),Lam,P02,sum([ell,fc(T,2),A2])]))));
 const ps=pure("b"+branch+"_PS",qs(PW,q(prod([P02,sum([ell,fc(T,3),fc(A2,3),B3])]))));
 const meanCombo=fs(EB[0],fm(B,EB[1])); // EB=Econst+Ecoef*p, and B=2u-1: Econst-2s Ecoef = EB_even-B EB_odd
 if(branch===1)ck("b1_exact_mean_linear_product",
   fs(meanCombo,prod([cf(8),fq(S),inv(4),fa(Lam,one),fa(AA,fm(U,Lam))])));
 realRows.push([EB[0],EB[1],n1,ns,ps]);
 output.push({branch,rows:[EB[0],EB[1],n1,ns,ps].map(info),meanComboInfo:info(meanCombo),meanComboTerms:rawTerms(meanCombo)});
}

function gi(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r}return a}
let returnedLinearDivisions=0;
function prim(p){if(!p.size)return{p:C(),content:1n};let g=0n;for(const v of p.values())g=gi(g,v);return{p:new Map([...p].map(([k,v])=>[k,v/g])),content:g}}
function du(p,aa,bb){
 if(!p.size)return null;let d=0;for(const k of p.keys())d=Math.max(d,Number(k.split(",")[0]));if(!d)return null;
 const groups=new Map();for(const[k,v]of p){const[e,l,a]=k.split(",").map(Number),z=l+","+a;if(!groups.has(z))groups.set(z,Array(d+1).fill(0n));groups.get(z)[e]=v}
 const scale=aa**BigInt(d),quo=new Map();for(const[k,v]of groups){const co=Array(d).fill(0n);co[d-1]=scale*v[d]/aa;if(co[d-1]*aa!==scale*v[d])throw Error("integer leading division");
 for(let i=d-1;i>0;i--){const n=scale*v[i]-bb*co[i];if(n%aa)throw Error("integer linear division");co[i-1]=n/aa}
 if(scale*v[0]-bb*co[0])return null;
 for(let i=0;i<d;i++)if(co[i])quo.set(i+","+k,co[i]);}
 const lp=pa(pm(C(aa),PU),C(bb));ck("exact_linear_content_return",F(ps(pm(lp,quo),pm(C(scale),p))));returnedLinearDivisions++;return quo;
}
function dm(p,idx){if(!p.size)return null;if([...p.keys()].some(k=>Number(k.split(",")[idx])===0))return null;
 const q=new Map([...p].map(([k,v])=>{let e=k.split(",").map(Number);e[idx]--;return[e.join(","),v]}));
 ck("exact_monomial_content_return",F(ps(pm(V(idx),q),p)));returnedLinearDivisions++;return q;
}
const primitiveRows=[];
for(let j=0;j<1;j++){
 const rows=[];
 for(let i=0;i<5;i++){let p=prim(realRows[j][i].n).p;const removed=[];
  for(const[name,A,B]of [["u",1n,0n],["u-1",1n,-1n],["2u-1",2n,-1n],["2u-3",2n,-3n]]){
   let power=0;while(p.size){const q=du(p,A,B);if(q===null)break;p=prim(q).p;power++}if(power)removed.push({factor:name,power});}
  for(const[name,k]of [["lambda",1],["a",2]]){let power=0;while(p.size){const q=dm(p,k);if(q===null)break;p=prim(q).p;power++}if(power)removed.push({factor:name,power});}
  rows.push({name:["EBe","EBo","N1","NS","PS"][i],removed,terms:rawTerms(F(p),300),info:info(F(p))});
 }primitiveRows.push({branch:j+1,rows});
}
const Qq=(function(){const started=Date.now();let arithmetic=0,products=0,divisions=0;
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
return {P,add,sub,mul,scale,pow,sum,prod,divmod,xgcd,equal,textp,R,rd,monic,stat:()=>({arithmetic,products,divisions})};})();

const actualP=primitiveRows[0].rows.map(row=>new Map(row.terms.map(([k,v])=>[k,BigInt(v)])));
function mpow(p,n){let v=C(1);while(n--)v=pm(v,p);return v}
function substA(p,z){let out=C();for(const[k,v]of p){const[i,j,n]=k.split(",").map(Number);out=pa(out,pm(pm(C(v),new Map([[i+","+j+",0",1n]])),mpow(z,n)))}return out}
function assertp(name,p){ck(name,F(p))}
function toQq(p,l,a,den=Qq.P(1n)){
 let D=0;for(const k of p.keys()){const e=k.split(",").map(Number);D=Math.max(D,e[1]+e[2])}
 let out=Qq.P();const u=Qq.P(0n,1n);
 for(const[k,v]of p){const[i,j,m]=k.split(",").map(Number);
  out=Qq.add(out,Qq.prod(...[Qq.P(v),Qq.pow(u,i),Qq.pow(l,j),Qq.pow(a,m),Qq.pow(den,D-j-m)]));}
 return{p:out,denPower:D};
}
const uq=Qq.P(0n,1n),sq=Qq.P(-1n,1n),hq=Qq.P(-3n,2n);
const c1A=Qq.P(-3n,4n);
const firstRows=actualP.map(p=>toQq(p,Qq.P(-1n),c1A));
if(firstRows[2].p.length)throw Error("lambda minus one N1 recovery");
const meanExpected=Qq.prod(...[hq,sq,Qq.P(-9n,7n)]);
if(!Qq.equal(firstRows[1].p,meanExpected))throw Error("lambda minus one remaining mean");
const v97=Qq.R(9n,7n);function ev(p,x){let v=Qq.R();for(let i=p.length-1;i>=0;i--)v=Qq.add(Qq.P(Qq.R(p[i].n,p[i].d)),Qq.mul(Qq.P(x),Qq.P(v)))[0]||Qq.R();return v}
const nAt97=ev(firstRows[3].p,v97);if(!nAt97.n)throw Error("new NS constant vanishes");
const case1={lambda:"-1",a:"4u-3",remainingOriginalMean:"(2u-3)(u-1)(7u-9)",u:"9/7",
  exactNSNonzero:Qq.textp([nAt97]),excluded:true};
const apl=pn(pm(PU,PL));
const pe=substA(actualP[1],apl),pn1=substA(actualP[2],apl);
const qU=dm(pe,0);if(!qU)throw Error("known u division");const EE=pn(qU);
const Lpoly=pa(pm(pa(ps(pm(C(2),pm(PU,PU)),pm(C(7),PU)),C(4)),PL),ps(pm(C(3),PU),C(4)));
assertp("new_same_point_N1_plus_s_mean_linear",ps(pa(pn1,pm(PS,EE)),pm(pm(PH,PL),Lpoly)));
const den=Qq.P(4n,-7n,2n),num=Qq.P(4n,-3n),aq=Qq.scale(Qq.mul(uq,num),-1n);
const headGcd=Qq.xgcd(den,num);if(headGcd[0].length!==1)throw Error("entire lambda head zero not covered");
const eq=toQq(EE,num,Qq.P(),den);
const F4=Qq.P(16n,-24n,9n,-4n,2n);
if(!Qq.equal(eq.p,Qq.scale(Qq.mul(sq,F4),2n)))throw Error("quartic original mean return");
const secondRows=actualP.map(p=>toQq(p,num,aq,den));
let g=F4;const stages=[];
for(const i of [3,4]){const rr=Qq.xgcd(g,secondRows[i].p);g=rr[0];stages.push({originalRow:i,originalDegree:secondRows[i].p.length-1,gcdDegree:g.length-1,bezoutDegrees:[rr[1].length-1,rr[2].length-1]});if(g.length===1)break}
return {schema:"isp-true-Phi-Azero-first-linear-branch-complete-original-return-v1",
 elapsedMilliseconds:Date.now()-began,integerPolynomialProducts:products,fullOriginalChecks:checks.filter(x=>!x.startsWith("exact_")),
 returnedLinearDivisions,case1,case2:{a:"-u*lambda",linear:"(2u^2-7u+4)lambda+3u-4",entireHeadZeroQQBezout1:true,
 exactRemainingQuartic:[16,-24,9,-4,2],wholeQuarticIdentityReturned:true,stages,remainingGCD:Qq.textp(g),excluded:g.length===1},
 rationalStatistics:Qq.stat(),firstLinearBranchExcluded:g.length===1,secondLinearBranchNotYetExcluded:true,ordinaryISPClaim:false};
