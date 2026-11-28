"use strict";
// NEW correct Phi f=u, entire u=3/2 head fiber.
// Coordinates are (Q,unused,unused,t); all original Gram values returned.
// Only intrinsic units and the already proved t!=0, lambda!=0 are removed.
const began=Date.now(),BUDGET=120000;let products=0,fullDivisions=0;
const DIM=4,ZK="0,0,0,0";
function checkTime(){if(Date.now()-began>BUDGET)throw Error("new true Phi fu u=3/2 input 120 second boundary")}
function C(n=0n){n=BigInt(n);return n===0n?new Map():new Map([[ZK,n]])}
function V(i){const e=[0,0,0,0];e[i]=1;return new Map([[e.join(","),1n]])}
function pa(a,b){const c=new Map(a);for(const[k,v]of b){const z=(c.get(k)||0n)+v;if(z)c.set(k,z);else c.delete(k)}return c}
function pn(a){return new Map([...a].map(([k,v])=>[k,-v]))}
function ps(a,b){return pa(a,pn(b))}
function pm(a,b){checkTime();products++;if(!a.size||!b.size)return C();const c=new Map();for(const[ka,va]of a){const ea=ka.split(",").map(Number);for(const[kb,vb]of b){const eb=kb.split(",").map(Number),k=ea.map((x,i)=>x+eb[i]).join(","),v=(c.get(k)||0n)+va*vb;if(v)c.set(k,v);else c.delete(k)}}return c}
function gi(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const r=a%b;a=b;b=r}return a}
function eqp(a,b){return !ps(a,b).size}
const Xp=V(0),Lp=V(1),Fp=V(2),Tp=V(3);
const H=ps(C(1),Xp),J=pa(pm(C(2),Xp),C(1));
const beta=pa(pm(C(4),Xp),C(5)),xp=pa(Xp,C(2));
const atoms=[Xp,H,J,beta,xp],coeffAtoms=[[0n,1n],[1n,-1n],[1n,2n],[5n,4n],[2n,1n]];
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

const zero=cf(0),one=cf(1),Q=F(Xp),tt=F(Tp),delta=F(H),PP=F(J),BB=F(beta);
const u=cf(3,2),ff=u,ell=fc(prod(PP,inv(0)),1,2),aw=fs(one,ell);
const bc=fc(prod(BB,inv(0)),1,16),T=cf(-3,4);
const lam=fc(prod(fs(fc(Q,2),cf(5)),inv(2)),1,4);
const P02=fc(PP,1,2),T0=fn(F(xp)),Pf=F(xp);
const A1=fc(prod(PP,inv(0)),-1,4);
const xm=fa(u,fc(tt,1,4)),ym=fc(prod(sum(cf(10),fc(Q,-4),fc(tt,-3)),inv(1)),1,8);
function q(v=zero,w=zero){return[v,w]}
function qa(a,b){return[fa(a[0],b[0]),fa(a[1],b[1])]}
function qn(a){return[fn(a[0]),fn(a[1])]}
function qs(a,b){return qa(a,qn(b))}
function qm(a,b){return[fa(fm(a[0],b[0]),prod(delta,a[1],b[1])),fa(fm(a[0],b[1]),fm(a[1],b[0]))]}
function qc(a,n,d=1n){return[fc(a[0],n,d),fc(a[1],n,d)]}
function qt(v,a){return qm(q(v),a)}
function conj(a){return[a[0],fn(a[1])]}
const b=q(fc(prod(PP,inv(0)),1,4),fc(inv(0),-1,4)),c=conj(b);
const p=q(one,one),qp=conj(p),unit=[q(one),q(),q(one),q(one)];
const X=q(xm,ym),Y=conj(X),r=qs(qs(X,qt(aw,p)),qt(tt,c)),ss=conj(r);
const rows=[[q(),q(),p,qp],[q(),q(A1),r,ss],[p,r,q(),q(tt)],[qp,ss,q(tt),q()]];
function vm(a,b){return[qm(a[0],b[0]),qa(qm(a[0],b[1]),qm(a[1],b[0])),qm(a[2],b[2]),qm(a[3],b[3])]}
function va(a,b){return a.map((v,i)=>qa(v,b[i]))}
function vs(a,b){return b.map(v=>qm(a,v))}
function qsum(...xs){return xs.reduce(qa,q())}
function tau(v){return qsum(qt(aw,v[0]),v[1],qm(b,v[2]),qm(c,v[3]))}
function DK(v){return rows.map(row=>tau(vm(row,v)))}
const dv=DK(unit),F2=tau(dv),Kd=DK(dv),dd=vm(dv,dv);
const checks=[];function ck(name,a){for(const v of (Array.isArray(a)?a:[a]))if(v.n.size)throw Error(name+": nonzero "+v.n.size+" terms");checks.push(name)}
function pure(name,a){ck(name+"_odd",a[1]);return a[0]}
function mean(j){const v=j===1?qc(tau(vm(rows[0],rows[1])),2):tau(vm(rows[j],rows[j]));
 return qsum(v,qc(Kd[j],-2),qc(dd[j],-2),qc(qm(F2,dv[j]),2))}
function centered(v){return va(v,vs(qn(tau(v)),unit))}
function P2(v){const z=centered(v);return tau(vm(vm(z,z),z))}
function N4(v){const tv=tau(v),vv=vm(v,v);
 return qsum(qc(tau(vm(dv,vv)),2),qn(qm(F2,tau(vv))),qc(qm(tv,tau(vm(dv,v))),-4),qc(qm(F2,qm(tv,tv)),2),tau(vm(v,DK(v))))}
ck("new_half_u_weights",qs(qa(qm(b,p),qm(c,qp)),q(u)));
ck("new_half_u_bc",qs(qm(b,c),q(bc)));
ck("new_half_u_E0",mean(0));
ck("new_half_u_actual_f",qs(F2,q(cf(3))));
ck("new_half_u_P02",qs(P2(rows[0]),q(P02)));
const N0=N4(rows[0]),ww=fs(fs(lam,one),T);
const pj=qc(tau(vm(vm(centered(rows[0]),centered(rows[0])),centered(rows[1]))),3);
ck("new_half_u_N0",qs(N0,q(prod(cf(2),lam,P02))));
ck("new_half_u_P1",qs(pj,q(prod(cf(3),ww,P02))));
const EB=mean(2),EC=mean(3);
ck("new_half_u_E_conjugacy",qs(EC,conj(EB)));
ck("new_half_u_true_E1_minus_EW",qs(mean(1),qa(qm(b,EB),qm(c,EC))));
const nj=qs(qs(N4(va(rows[0],rows[1])),N0),N4(rows[1]));
const N1=pure("new_half_u_N1",qs(nj,q(prod(cf(4),lam,ww,P02))));
const A2=sum(fc(fq(lam),2),fc(lam,-2),one),B3=sum(fc(fp(lam,3),4),fc(fq(lam),-6),fc(lam,3),cf(-1));
const NS=pure("new_half_u_NS",qs(qsum(qm(b,N4(rows[2])),qm(c,N4(rows[3]))),q(prod(cf(2),lam,P02,sum(ell,fc(T,2),A2)))));
const PS=pure("new_half_u_PS",qs(qsum(qm(b,P2(rows[2])),qm(c,P2(rows[3]))),q(prod(P02,sum(ell,fc(T,3),fc(A2,3),B3)))));
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


function coeffs(p){
 let d=-1;for(const key of p.keys())d=Math.max(d,Number(key.split(",")[3]));const out=Array.from({length:d+1},()=>Qq.P());
 for(const[key,a]of p){const[i,j,k,n]=key.split(",").map(Number);if(j||k)throw Error("free unwanted coordinate");const cs=Array(i+1).fill(0n);cs[i]=a;out[n]=Qq.add(out[n],Qq.P(...cs))}
 return out;
}
const units=[["Q",Qq.P(0,1)],["1-Q",Qq.P(1,-1)],["2Q+1",Qq.P(1,2)],["4Q+5",Qq.P(5,4)],["Q+2",Qq.P(2,1)],["2Q-5",Qq.P(-5,2)]];
const raw=[EB[0],EB[1],N1,NS,PS],names=["EBe","EBo","N1","NS","PS"],prepared=[];
for(let i=0;i<raw.length;i++){
 let row=coeffs(raw[i].n),tRemoved=0,divisor=Qq.P(1),removals=[];
 while(row.length&&!row[0].length){row.shift();tRemoved++}
 let content=Qq.P();for(const c0 of row)content=Qq.xgcd(content,c0)[0];
 for(const[name,p]of units){let power=0;while(content.length>1){const[q,r]=Qq.divmod(content,p);if(r.length)break;content=q;divisor=Qq.mul(divisor,p);power++}if(power)removals.push({name,power})}
 row=row.map(p=>{const[q,r]=Qq.divmod(p,divisor);if(r.length)throw Error("whole original unit-content division");return q});
 prepared.push({row,tRemoved,removals,tDegree:row.length-1,QDegree:row.reduce((d,a)=>Math.max(d,a.length-1),-1)});
}
let detDivisions=0;
function det(M){
 const n=M.length,A=M.map(r=>r.map(p=>p.slice()));if(!n)return Qq.P(1);if(n===1)return A[0][0];
 let prev=Qq.P(1),sign=1;
 for(let k=0;k<n-1;k++){
  let j=k;while(j<n&&!A[j][k].length)j++;
  if(j===n)return Qq.P();if(j!==k){[A[j],A[k]]=[A[k],A[j]];sign=-sign}
  const pivot=A[k][k];
  for(let i=k+1;i<n;i++)for(let j2=k+1;j2<n;j2++){
   const numerator=Qq.sub(Qq.mul(pivot,A[i][j2]),Qq.mul(A[i][k],A[k][j2])),[q,r]=Qq.divmod(numerator,prev);
   if(r.length||!Qq.equal(Qq.mul(q,prev),numerator))throw Error("complete fixed Sylvester division");detDivisions++;A[i][j2]=q;
  }
  for(let i=k+1;i<n;i++)A[i][k]=Qq.P();prev=pivot;
 }
 return Qq.scale(A[n-1][n-1],sign);
}
function resultant(a,b){
 const m=a.length-1,n=b.length-1,N=m+n;if(m<0||n<0)return{p:Qq.P(),degrees:[m,n],size:N};
 if(!m)return{p:Qq.pow(a[0],n),degrees:[m,n],size:n};if(!n)return{p:Qq.pow(b[0],m),degrees:[m,n],size:m};
 const M=Array.from({length:N},()=>Array.from({length:N},()=>Qq.P()));
 for(let i=0;i<n;i++)for(let j=0;j<=m;j++)M[i][i+j]=a[j];
 for(let i=0;i<m;i++)for(let j=0;j<=n;j++)M[n+i][i+j]=b[j];
 return{p:det(M),degrees:[m,n],size:N};
}
const projections=[];let gcd=Qq.P(),remaining=Qq.P(),finalRemoved=[];
for(const j of [0,1,3,4]){
 const r=resultant(prepared[2].row,prepared[j].row),[g,a,b]=Qq.xgcd(gcd,r.p);gcd=g;
 remaining=g;finalRemoved=[];
 for(const[name,p]of units){let power=0;while(remaining.length>1){const[q,r]=Qq.divmod(remaining,p);if(r.length)break;remaining=q;power++}if(power)finalRemoved.push({name,power})}
 projections.push({anchor:"N1",other:names[j],fixedTDegrees:r.degrees,fixedSize:r.size,resultantQDegree:r.p.length-1,cumulativeGCDDegree:g.length-1,remainingDegree:remaining.length-1,completeQQBezoutReturned:true});
 if(remaining.length===1)break;
}
return{schema:"isp-true-Phi-fu-whole-u-three-half-original-return-v1",
 elapsedMilliseconds:Date.now()-began,integerProducts:products,fullIntegerDivisions:fullDivisions,checks:checks.length,
 actualOriginalParameter:"u=f=3/2, lambda=(2Q-5)/(4(2Q+1)), T=-3/4",
 originalRows:prepared.map((r,i)=>({name:names[i],tDegree:r.tDegree,QDegree:r.QDegree,tRemoved:r.tRemoved,originalPaidContent:r.removals})),
 fixedProjections:projections,exactGCD:Qq.textp(gcd),finalPaidRemovals:finalRemoved,
 remaining:Qq.textp(Qq.monic(remaining)),remainingDegree:remaining.length-1,
 fixedSylvesterFullDivisions:detDivisions,rationalStatistics:Qq.stat(),
 everyQLeadingAndFiniteTRootKept:true,noPhysicalDInverted:true,
 wholeFuHalfHeadExcluded:remaining.length===1,wholeFuExcluded:false,wholePhiExcluded:false,ordinaryISPClaim:false};
