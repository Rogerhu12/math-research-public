"use strict";
// NEW whole correct Phi B=0: original Gram mean syzygy and weighted values.
// No first-head inverse, no N1 slope inverse, no old six-by-two replay.
// Coordinates are (x,lambda,f,t); only intrinsic parameter units inverted.
const began=Date.now(),BUDGET=120000;let products=0,fullDivisions=0;
const DIM=4,ZK="0,0,0,0";
function checkTime(){if(Date.now()-began>BUDGET)throw Error("new true B original input 120 second boundary")}
function C(n=0n){n=BigInt(n);return n===0n?new Map():new Map([[ZK,n]])}
function V(i){const e=[0,0,0,0];e[i]=1;return new Map([[e.join(","),1n]])}
function pa(a,b){const c=new Map(a);for(const[k,v]of b){const z=(c.get(k)||0n)+v;if(z)c.set(k,z);else c.delete(k)}return c}
function pn(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function ps(a,b){return pa(a,pn(b))}
function pm(a,b){checkTime();products++;if(!a.size||!b.size)return C();const c=new Map();for(const[ka,va]of a){const ea=ka.split(",").map(Number);for(const[kb,vb]of b){const eb=kb.split(",").map(Number),k=ea.map((x,i)=>x+eb[i]).join(","),v=(c.get(k)||0n)+va*vb;if(v)c.set(k,v);else c.delete(k)}}return c}
function gi(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r}return a}
function eqp(a,b){return !ps(a,b).size}
const Xp=V(0),Lp=V(1),Fp=V(2),Tp=V(3);
const H=ps(pm(C(2),Xp),C(1)),J=pa(ps(pm(C(7),pm(Xp,Xp)),pm(C(4),Xp)),C(1));
const beta=ps(pm(C(5),Xp),C(1)),xp=pa(Xp,C(1)),F0=pa(ps(pm(Xp,Xp),Xp),C(1));
const atoms=[Xp,H,J,beta,xp],coeffAtoms=[[0n,1n],[-1n,2n],[1n,-4n,7n],[-1n,5n],[1n,1n]];
function divAtom(p,idx){
 const q=coeffAtoms[idx],dq=q.length-1,groups=new Map();let max=-1;
 for(const[k,v]of p){const e=k.split(",").map(Number);max=Math.max(max,e[0]);const tail=e.slice(1).join(",");if(!groups.has(tail))groups.set(tail,[]);groups.get(tail)[e[0]]=v}
 if(max<dq)return null;const out=new Map();
 for(const[tail,arr]of groups){
  const r=Array.from({length:max+1},(_,i)=>arr[i]||0n),z=Array(Math.max(0,max-dq+1)).fill(0n);
  for(let i=max;i>=dq;i--){if(!r[i])continue;if(r[i]%q[dq])return null;const a=r[i]/q[dq];z[i-dq]=a;for(let j=0;j<=dq;j++)r[i-dq+j]-=a*q[j]}
  if(r.some(x=>x))return null;for(let i=0;i<z.length;i++)if(z[i])out.set(i+","+tail,z[i]);
 }
 if(!eqp(pm(out,atoms[idx]),p))throw Error("whole integer atom division return");fullDivisions++;return out;
}
const powCache=atoms.map(a=>[C(1),a]);
function atomPow(i,n){const c=powCache[i];while(c.length<=n)c.push(pm(c.at(-1),atoms[i]));return c[n]}
function mulDen(n,e){for(let i=0;i<5;i++)if(e[i])n=pm(n,atomPow(i,e[i]));return n}
function F(n=C(),e=[0,0,0,0,0],d=1n){
 d=BigInt(d);if(!d)throw Error("zero denominator");if(!n.size)return{n:C(),e:[0,0,0,0,0],d:1n};e=e.slice();
 if(d<0n){n=pn(n);d=-d}
 let g=d;for(const v of n.values())g=gi(g,v);if(g>1n){n=new Map([...n].map(([k,v])=>[k,v/g]));d/=g}
 for(let i=0;i<5;i++)while(e[i]>0){const q=divAtom(n,i);if(q===null)break;n=q;e[i]--}
 return{n,e,d};
}
function cf(n,d=1n){return F(C(n),undefined,d)}
function fa(a,b){
 if(!a.n.size)return b;if(!b.n.size)return a;
 const e=a.e.map((v,i)=>Math.max(v,b.e[i])),g=gi(a.d,b.d),d=a.d/g*b.d;
 return F(pa(pm(C(d/a.d),mulDen(a.n,e.map((v,i)=>v-a.e[i]))),pm(C(d/b.d),mulDen(b.n,e.map((v,i)=>v-b.e[i])))),e,d);
}
function fn(a){return{n:pn(a.n),e:a.e,d:a.d}}
function fs(a,b){return fa(a,fn(b))}
function fm(a,b){return F(pm(a.n,b.n),a.e.map((v,i)=>v+b.e[i]),a.d*b.d)}
function fc(a,n,d=1n){return fm(a,cf(n,d))}
function fq(a){return fm(a,a)}
function fp(a,n){let r=cf(1);while(n--)r=fm(r,a);return r}
function inv(i){const e=[0,0,0,0,0];e[i]=1;return F(C(1),e)}
function prod(...xs){return xs.reduce(fm,cf(1))}
function sum(...xs){return xs.reduce(fa,cf(0))}
const zero=cf(0),one=cf(1),x=F(Xp),lam=F(Lp),ff=F(Fp),tt=F(Tp),HH=F(H),JJ=F(J),BB=F(beta),XP=F(xp),FF=F(F0);
const u=fc(prod(fq(XP),inv(0)),1,3);
const Q=fc(FF,4,3),delta=fc(fq(HH),-1,3),s=fs(u,one);
const ell=fc(prod(XP,BB,fp(inv(0),2)),1,6),aw=fs(one,ell);
const m=fc(prod(XP,fs(x,one),HH,fp(inv(0),2)),1,6);
const bc=fc(prod(fq(XP),JJ,fp(inv(0),4)),1,36);
const K=fc(prod(FF,XP,inv(0)),4,3),T0=fn(K),P02=fc(prod(fq(FF),XP,BB,fp(inv(0),3)),4,27);
const Pf=fc(prod(fp(FF,3),XP,fp(inv(0),3)),16,27);
const T=sum(fc(prod(fs(XP,ff),inv(3)),3),fn(prod(XP,lam,inv(0))),fn(ell));
const A1=sum(fc(prod(FF,fs(ff,XP),fp(inv(0),2)),2,3),fc(prod(FF,XP,BB,lam,fp(inv(0),3)),2,9));
const Vmean=sum(ff,fc(A1,-1,2),fm(bc,tt));
const Wmean=fa(fc(u,2),zero); // overwritten exact E0 expression below
const W=fa(fc(K,-1,2),fc(fm(u,ff),2));
const minv=fc(prod(fp(x,4),fp(inv(4),2),inv(2),fp(inv(1),2)),-27);
const xmean=prod(fs(fm(fs(u,fm(ell,Q)),Vmean),fm(m,W)),minv);
const ymean=prod(fs(fm(ell,W),fm(u,Vmean)),minv);
function q(v=zero,w=zero){return[v,w]}
function qa(v,w){return[fa(v[0],w[0]),fa(v[1],w[1])]}
function qn(v){return[fn(v[0]),fn(v[1])]}
function qs(v,w){return qa(v,qn(w))}
function qm(v,w){return[fa(fm(v[0],w[0]),prod(delta,v[1],w[1])),fa(fm(v[0],w[1]),fm(v[1],w[0]))]}
function qc(v,n,d=1n){return[fc(v[0],n,d),fc(v[1],n,d)]}
function qt(v,w){return qm(q(v),w)}
function conj(v){return[v[0],fn(v[1])]}
const b=q(fc(ell,1,2),fc(prod(XP,fs(x,one),fp(inv(0),2),inv(1)),-1,4)),c=conj(b);
const p=q(one,one),qv=conj(p),unit=[q(one),q(),q(one),q(one)];
function vm(v,w){return[qm(v[0],w[0]),qa(qm(v[0],w[1]),qm(v[1],w[0])),qm(v[2],w[2]),qm(v[3],w[3])]}
function va(v,w){return v.map((a,i)=>qa(a,w[i]))}
function vs(a,v){return v.map(w=>qm(a,w))}
function tau(v){return[qt(aw,v[0]),v[1],qm(b,v[2]),qm(c,v[3])].reduce(qa,q())}
const X=q(xmean,ymean),Y=conj(X),r=qs(qs(X,qt(aw,p)),qt(tt,c)),sv=conj(r);
const rows=[[q(),q(),p,qv],[q(),q(A1),r,sv],[p,r,q(),q(tt)],[qv,sv,q(tt),q()]];
function DK(v){return rows.map(row=>tau(vm(row,v)))}
const dv=DK(unit),F2=tau(dv),Kd=DK(dv),dd=vm(dv,dv);
const checks=[];function ck(name,v){for(const a of (Array.isArray(v)?v:[v]))if(a.n.size)throw Error(name+": nonzero "+a.n.size+" terms");checks.push(name)}
function pure(name,v){ck(name+"_odd",v[1]);return v[0]}
function mean(j){const val=j===1?qc(tau(vm(rows[0],rows[1])),2):tau(vm(rows[j],rows[j]));
 return[val,qc(Kd[j],-2),qc(dd[j],-2),qc(qm(F2,dv[j]),2)].reduce(qa,q())}
function centered(v){return va(v,vs(qn(tau(v)),unit))}
function P2(v){const c0=centered(v);return tau(vm(vm(c0,c0),c0))}
function N4(v){const tv=tau(v),vv=vm(v,v);
 return[qc(tau(vm(dv,vv)),2),qn(qm(F2,tau(vv))),qc(qm(tv,tau(vm(dv,v))),-4),qc(qm(F2,qm(tv,tv)),2),tau(vm(v,DK(v)))].reduce(qa,q())}
ck("new_B_weight_sum",fs(fa(b[0],c[0]),ell));
ck("new_B_weight_u",qs(qa(qm(b,p),qm(c,qv)),q(u)));
ck("new_B_weight_product",qs(qm(b,c),q(bc)));
ck("new_B_M_inverse",fs(prod(minv,fc(prod(bc,delta),4)),one));
ck("new_B_actual_f",qs(F2,q(fc(ff,2))));
ck("new_B_E0",mean(0));
ck("new_B_P02",qs(P2(rows[0]),q(P02)));
const N0=N4(rows[0]),Pj=qc(tau(vm(vm(centered(rows[0]),centered(rows[0])),centered(rows[1]))),3),w=fs(fs(lam,one),T);
ck("new_B_N0",qs(N0,q(prod(cf(2),lam,P02))));
ck("new_B_Pjet",qs(Pj,q(prod(cf(3),w,P02))));
const E1=pure("new_B_E1",mean(1)),EB=mean(2),EC=mean(3);
ck("new_B_mean_conjugacy",qs(EC,conj(EB)));
const Nj=qs(qs(N4(va(rows[0],rows[1])),N0),N4(rows[1]));
const N1=pure("new_B_polar_N1",qs(Nj,q(prod(cf(4),lam,w,P02))));
const A2=sum(fc(fq(lam),2),fc(lam,-2),one),B3=sum(fc(fp(lam,3),4),fc(fq(lam),-6),fc(lam,3),cf(-1));
const NS=pure("new_B_NS",qs(qa(qm(b,N4(rows[2])),qm(c,N4(rows[3]))),q(prod(cf(2),lam,P02,sum(ell,fc(T,2),A2)))));
const PS=pure("new_B_PS",qs(qa(qm(b,P2(rows[2])),qm(c,P2(rows[3]))),q(prod(P02,sum(ell,fc(T,3),fc(A2,3),B3)))));
function inf(v){let deg=[-1,-1,-1,-1];for(const k of v.n.keys()){const e=k.split(",").map(Number);deg=deg.map((x,i)=>Math.max(x,e[i]))}return{degrees:deg,terms:v.n.size,denominatorConstant:String(v.d),denominatorPowers:v.e}}
function extract(v,i,j){const p=new Map();for(const[k,c0]of v.n){const e=k.split(",").map(Number);if(e[2]===i&&e[3]===j){e[2]=e[3]=0;p.set(e.join(","),c0)}}return F(p,v.e,v.d)}
const Qq=(function(){const started=began;let arithmetic=0,products=0,divisions=0;
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
return {P,add,sub,mul,scale,pow,sum,prod,divmod,xgcd,equal,textp,R,monic,stat:()=>({arithmetic,products,divisions})};})();


const phi=Qq.P(2,-11,23),Kzero=Qq.P(),Kone=Qq.P(1),Kx=Qq.P(0,1);
let kProducts=0,kInverses=0,lambdaDivisions=0,lambdaProducts=0;
function kr(a){return Qq.divmod(a,phi)[1]}
function kc(a){return Qq.P(a)}
function ka(a,b){return kr(Qq.add(a,b))}
function kn(a){return Qq.scale(a,-1)}
function ks(a,b){return ka(a,kn(b))}
function km(a,b){checkTime();kProducts++;return kr(Qq.mul(a,b))}
function kp(a,n){let z=Kone;while(n--)z=km(z,a);return z}
function ki(a){const[g,v,w]=Qq.xgcd(a,phi);if(g.length!==1)throw Error("whole C algebra nonunit");const z=kr(v);if(!Qq.equal(km(a,z),Kone))throw Error("whole C inverse return");kInverses++;return z}
function kd(a,b){return km(a,ki(b))}
const kAtoms=coeffAtoms.map(a=>kr(Qq.P(...a)));
for(const a of [...kAtoms,kr(Qq.P(1,-1,1))])ki(a);
const xcache=[Kone,Kx];function xpow(n){while(xcache.length<=n)xcache.push(km(xcache.at(-1),Kx));return xcache[n]}
function constantDen(v){let a=kc(v.d);for(let i=0;i<5;i++)if(v.e[i])a=km(a,kp(kAtoms[i],v.e[i]));return ki(a)}
function kraw(v){
 const invden=constantDen(v),out=new Map();
 for(const[k,c0]of v.n){const[i,l,f,t]=k.split(",").map(Number),key=l+","+f+","+t,val=km(km(kc(c0),xpow(i)),invden);
 const vv=ka(out.get(key)||Kzero,val);if(vv.length)out.set(key,vv);else out.delete(key)}
 return out;
}
function polyF(co){const p=C();for(let i=0;i<co.length;i++)if(co[i])p.set(i+",0,0,0",BigInt(co[i]));return F(p)}
const ksyzygy=[
 prod(cf(-18),fp(x,3),HH),
 polyF([2,-13,54,-79,68]),
 prod(HH,polyF([-2,15,-54,97,-48]))
];
const rawL=sum(...ksyzygy.map((a,i)=>fm(a,[E1,EB[0],EB[1]][i])));
for(const key of rawL.n.keys()){const e=key.split(",").map(Number);if(e[2]+e[3]>1||e[1]>2)throw Error("new original mean syzygy not degree (2,1,1)")}
const Lk=kraw(rawL),coef=(l,f,t)=>Lk.get([l,f,t].join(","))||Kzero;
const af=coef(1,1,0),bf=coef(0,1,0),ct=coef(1,0,1),dt=coef(0,0,1),p0=[coef(0,0,0),coef(1,0,0),coef(2,0,0)];
for(const key of Lk.keys()){if(!["0,0,0","1,0,0","2,0,0","0,1,0","1,1,0","0,0,1","1,0,1"].includes(key))throw Error("unexpected mean syzygy monomial")}
if(ks(km(af,dt),km(bf,ct)).length)throw Error("C slope relation");
const lam0=kn(kd(bf,af));
if(!Qq.equal(lam0,Qq.P(Qq.R(-1,4))))throw Error("exact -1/4 head value");
const pAt0=ka(ka(p0[0],km(p0[1],lam0)),km(p0[2],kp(lam0,2)));ki(pAt0);
const rf=kn(kd(ct,af)),rfExpected=kd(kr(Qq.P(1,-4,7)),km(kc(12),kp(Kx,2)));
if(!Qq.equal(rf,rfExpected))throw Error("original f/t ratio");
function tr(p){p=p.slice();while(p.length&&!p.at(-1).length)p.pop();return p}
function la(a,b){return tr(Array.from({length:Math.max(a.length,b.length)},(_,i)=>ka(a[i]||Kzero,b[i]||Kzero)))}
function ln(a){return a.map(kn)}
function ls(a,b){return la(a,ln(b))}
function lscale(a,c){return tr(a.map(v=>km(v,c)))}
function lm(a,b){checkTime();lambdaProducts++;if(!a.length||!b.length)return[];const out=Array.from({length:a.length+b.length-1},()=>Kzero);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)out[i+j]=ka(out[i+j],km(a[i],b[j]));return tr(out)}
function lp(a,n){let out=[Kone];while(n--)out=lm(out,a);return out}
function ld(a,b){
 if(!b.length)throw Error("zero lambda divisor");let r=a.slice(),q=[];
 const lcInv=ki(b.at(-1));while(r.length>=b.length){const d=r.length-b.length,c=km(r.at(-1),lcInv),v=Array.from({length:d},()=>Kzero).concat([c]);q=la(q,v);r=ls(r,lm(v,b))}
 if(ls(a,la(lm(q,b),r)).length)throw Error("whole K[lambda] division return");lambdaDivisions++;return[q,r];
}
function lgcd(a,b){
 let r0=a,r1=b,s0=[Kone],s1=[],t0=[],t1=[Kone];
 while(r1.length){const[q,r]=ld(r0,r1);[r0,r1]=[r1,r];[s0,s1]=[s1,ls(s0,lm(q,s1))];[t0,t1]=[t1,ls(t0,lm(q,t1))]}
 if(r0.length){const c=ki(r0.at(-1));r0=lscale(r0,c);s0=lscale(s0,c);t0=lscale(t0,c)}
 if(ls(la(lm(s0,a),lm(t0,b)),r0).length)throw Error("full K lambda Bezout return");
 return[r0,s0,t0];
}
function zpoly(a=Kzero){return a.length?new Map([["0,0",a]]):new Map()}
function za(a,b){const out=new Map(a);for(const[k,v]of b){const w=ka(out.get(k)||Kzero,v);if(w.length)out.set(k,w);else out.delete(k)}return out}
function zn(a){return new Map([...a].map(([k,v])=>[k,kn(v)]))}
function zs(a,b){return za(a,zn(b))}
function zm(a,b){const out=new Map();for(const[ka0,va]of a){const e=ka0.split(",").map(Number);for(const[kb0,vb]of b){const f=kb0.split(",").map(Number),key=[e[0]+f[0],e[1]+f[1]].join(","),v=ka(out.get(key)||Kzero,km(va,vb));if(v.length)out.set(key,v);else out.delete(key)}}return out}
function zp(a,n){let r=zpoly(Kone);while(n--)r=zm(r,a);return r}
function zscale(a,c){return new Map([...a].map(([k,v])=>[k,km(v,c)]).filter(([,v])=>v.length))}
const DL=new Map([["0,0",Kone],["1,0",kc(4)]]),zt=new Map([["0,1",Kone]]);
const hn=p0.map(v=>km(km(kc(-4),ki(af)),v));
const fnumer=za(zscale(zm(DL,zt),rf),new Map(hn.map((v,i)=>[i+",0",v]).filter(([,v])=>v.length)));
function evalRow(v){
 const p=kraw(v);let d=-1;for(const key of p.keys())d=Math.max(d,Number(key.split(",")[1]));if(d<0)return{p:new Map(),fDegree:0};
 let out=new Map();
 for(const[key,c0]of p){const[l,f,t]=key.split(",").map(Number),mon=new Map([[l+","+t,c0]]);
 out=za(out,zm(mon,zm(zp(fnumer,f),zp(DL,d-f))))}
 return{p:out,fDegree:d};
}
const checkLinear=evalRow(rawL);if(checkLinear.p.size)throw Error("whole original L after f recovery");
const vals=[E1,EB[0],EB[1],N1,NS,PS].map(evalRow);
function tcoeffs(p){let d=-1;for(const key of p.keys())d=Math.max(d,Number(key.split(",")[1]));const out=Array.from({length:d+1},()=>[]);
 for(const[key,v]of p){const[l,t]=key.split(",").map(Number);out[t][l]=v}
 return out.map(a=>tr(Array.from({length:a.length},(_,i)=>a[i]||Kzero)));
}
const trows=vals.map(a=>tcoeffs(a.p));let exactDeterminants=0;
function det(M){
 const n=M.length;if(!n)return[Kone];if(n===1)return M[0][0];
 let out=[];for(let j=0;j<n;j++){if(!M[0][j].length)continue;const B=M.slice(1).map(row=>row.filter((_,k)=>k!==j));const v=lm(M[0][j],det(B));out=la(out,j%2?ln(v):v)}return out;
}
function resultant(a,b){
 const m=a.length-1,n=b.length-1;if(m<0||n<0)return{poly:[],degrees:[m,n],size:m+n};
 if(!m)return{poly:lp(a[0],n),degrees:[m,n],size:n};
 if(!n)return{poly:lp(b[0],m),degrees:[m,n],size:m};
 const N=m+n,M=Array.from({length:N},()=>Array.from({length:N},()=>[]));
 for(let i=0;i<n;i++)for(let j=0;j<=m;j++)M[i][i+j]=a[j];
 for(let i=0;i<m;i++)for(let j=0;j<=n;j++)M[n+i][i+j]=b[j];
 exactDeterminants++;return{poly:det(M),degrees:[m,n],size:N};
}
const report=[],names=["E1","EBe","EBo","N1","NS","PS"];
let g=[];
for(const j of [0,1,2,4,5]){
 const r=resultant(trows[3],trows[j]),bez=lgcd(g,r.poly);g=bez[0];
 report.push({anchor:"N1",other:names[j],fixedTDegrees:r.degrees,fixedSylvesterSize:r.size,
  resultantLambdaDegree:r.poly.length-1,cumulativeGCDDegree:g.length-1,
  completeKBezoutReturned:true});
 if(g.length===1)break;
}
let remaining=g,removed=[];
for(const[name,p]of [["lambda",[Kzero,Kone]],["4lambda+1",[Kone,kc(4)]]]){
 let power=0;while(remaining.length>1){const[q,r]=ld(remaining,p);if(r.length)break;remaining=q;power++}if(power)removed.push({name,power})}
return{schema:"isp-true-Phi-Bzero-C2-original-fixed-t-return-v1",
 elapsedMilliseconds:Date.now()-began,integerProducts:products,fullIntegerDivisions:fullDivisions,
 phi:Qq.textp(phi),exactLambdaHeadValue:Qq.textp(lam0),
 wholeZeroLambdaHeadFiberExcluded:true,allIntrinsicWeightUnitsReturned:true,
 exactOriginalLinearRecoveryReturned:true,
 originalRowDegrees:trows.map((r,i)=>({name:names[i],t:r.length-1,lambda:r.reduce((a,p)=>Math.max(a,p.length-1),-1),clearedPower4lambda1:vals[i].fDegree})),
 projections:report,finalExactGCD:g.map(Qq.textp),removedKnownUnits:removed,
 exactRemainingPolynomial:remaining.map(Qq.textp),remainingLambdaDegree:remaining.length-1,
 kProducts,kInverses,lambdaProducts,lambdaDivisions,exactDeterminants,
 allParameterEmbeddingsKept:true,noPhysicalDInverted:true,
 entireCExcluded:remaining.length===1,entireBExcluded:false,ordinaryISPClaim:false};
