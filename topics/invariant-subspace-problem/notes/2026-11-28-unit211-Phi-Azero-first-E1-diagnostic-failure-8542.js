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
const output=[];
for(const branch of [1,2]){
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
 ck("b"+branch+"_E0",mean(0));ck("b"+branch+"_true_E1",mean(1));
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
 output.push({branch,rows:[EB[0],EB[1],n1,ns,ps].map(info),meanComboInfo:info(meanCombo),meanComboTerms:rawTerms(meanCombo)});
}
return{schema:"isp-true-Phi-Azero-two-original-Gram-branches-v1",milliseconds:Date.now()-began,integerPolynomialProducts:products,fullOriginalChecks:checks,output,
 originalBranches:"a-2(f-u)=0 or a+2(f-u)+2u*lambda=0; a=u*t/(2(2u-1))",
 wholeAExcluded:false,ordinaryISPClaim:false};
