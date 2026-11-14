'use strict';
/* Complete exact Laurent identities for the two curvature endpoints of P2.
   BigInt coefficients; full signed exponent vectors; no sampled parameters. */
const names=['n','m','R','T','r','M1','N1','xi','upsilon','B','F'],dim=names.length,zkey=Array(dim).fill(0).join(',');
const cp=a=>BigInt(a)===0n?new Map:new Map([[zkey,BigInt(a)]]);
const add=(...ps)=>{const o=new Map;for(const p of ps)for(const[k,a]of p){const v=(o.get(k)||0n)+a;if(v)o.set(k,v);else o.delete(k)}return o};
const neg=p=>new Map([...p].map(([k,a])=>[k,-a])),sub=(p,q)=>add(p,neg(q));
const mul=(...ps)=>{let p=cp(1);for(const q of ps){const o=new Map;for(const[k,a]of p){const e=k.split(',').map(Number);for(const[l,b]of q){const f=l.split(',').map(Number),ex=e.map((v,i)=>v+f[i]);if(ex.some(v=>!Number.isSafeInteger(v)))throw Error('unsafe exponent');const key=ex.join(','),v=(o.get(key)||0n)+a*b;if(v)o.set(key,v);else o.delete(key)}}p=o}return p};
const pow=(p,n)=>{if(n<0){if(p.size!==1)throw Error('inverse of nonmonomial');const[[k,a]]=p;if(a!==1n&&a!==-1n)throw Error('nonunit inverse');return new Map([[k.split(',').map(v=>Number(v)*n).join(','),a===-1n&&(-n)%2?-1n:1n]])}return mul(...Array(n).fill(p))};
const div=(p,q)=>mul(p,pow(q,-1));
const subs=(p,i,q)=>{let o=new Map;for(const[k,a]of p){const e=k.split(',').map(Number),v=e[i];if(v<0)throw Error('uncleared substitution');e[i]=0;o=add(o,mul(new Map([[e.join(','),a]]),pow(q,v)))}return o};
const vs=names.map((_,i)=>{const e=Array(dim).fill(0);e[i]=1;return new Map([[e.join(','),1n]])});
const[n,m,R,T,r,M,N,xi,y,B,Z]=vs,o=cp(1),two=cp(2),ep=sub(o,r),A=sub(o,mul(R,r)),d=sub(r,T),P=sub(add(o,T),mul(two,R,T)),Q=sub(add(o,R),mul(two,R,T)),C=add(sub(o,mul(R,T)),div(mul(T,sub(o,R)),r)),c=mul(xi,y);
function ks(F){return{
 kp:sub(mul(n,xi,P),mul(R,add(o,T),F,pow(xi,2))),
 km:sub(div(mul(m,y,Q),r),div(mul(T,add(o,R),F,pow(y,2)),r)),
 k0:add(div(mul(ep,sub(mul(T,sub(o,R)),mul(R,r,sub(o,T)))),r),neg(div(mul(n,m,sub(o,mul(R,T)),c),r)),div(mul(R,m,F,pow(xi,2),y),r),div(mul(T,n,F,xi,pow(y,2)),r),div(mul(two,R,T,add(r,o),F,c),r),neg(div(mul(R,T,pow(F,2),pow(c,2)),r)))}}
function S(F){return add(mul(ep,C),div(mul(T,c,add(mul(n,m,sub(o,R)),neg(mul(R,m,F,xi)),mul(n,F,y),mul(two,R,add(r,o),F),neg(mul(R,pow(F,2),c)))),r),neg(div(mul(T,add(o,R),F,ep,y),m)))}
function actualXY(p){return subs(subs(p,7,div(A,mul(R,M))),8,div(d,mul(N,T)))}
function check(p,name){if(p.size)throw Error(name+': '+p.size+' remaining terms');console.log(name+'_PASS')}
{
 const k=ks(Z);
 const lhs=add(k.k0,div(mul(k.kp,m,y),r),mul(ep,sub(Q,div(mul(T,add(o,R),Z,y),m))));
 check(sub(lhs,S(Z)),'FULL_S_BRIDGE');
}
{
 const F=mul(n,M),C1=sub(mul(two,add(r,o)),div(mul(m,ep),M));
 const BB=add(neg(div(mul(add(o,R),ep,M),m)),div(mul(A,C1),r));
 const target=add(mul(ep,C),div(mul(n,d,BB),N),div(mul(n,A,d,F,div(d,mul(N,T))),mul(M,N)));
 check(sub(actualXY(S(F)),target),'FN_ENDPOINT');
 const bpos=add(div(mul(two,ep,sub(m,o)),m),div(mul(pow(ep,2),add(m,two)),mul(M,r)),mul(sub(o,R),add(div(mul(ep,M),m),C1)));
 check(subs(mul(m,M,r,sub(BB,bpos)),5,add(m,o)),'FN_POSITIVE_B');
 const aa=div(m,M);
 const btail=add(mul(ep,add(sub(sub(cp(4),aa),div(two,aa)),div(mul(sub(two,aa),ep),r))),mul(sub(o,R),add(div(ep,aa),sub(mul(two,add(r,o)),aa))));
 check(sub(sub(BB,mul(aa,A)),btail),'FN_BAD_B_MINUS_aA');
 const Delta=sub(mul(two,T),mul(r,add(o,T)));
 check(add(actualXY(ks(F).kp),div(mul(n,A,Delta),M)),'FN_KPLUS_DELTA');
 const constdiff=sub(sub(sub(mul(cp(4),m,M),pow(m,2)),mul(two,pow(M,2))),sub(pow(m,2),two));
 check(subs(constdiff,5,add(m,o)),'M_GE_3_BAD_CONSTANT');
}
{
 const F=div(mul(m,N),r),aa=div(m,M),cc=div(n,N),b0=div(mul(m,N),mul(n,M,r));
 const rough=add(div(mul(ep,sub(mul(two,T),mul(R,r,add(o,T)))),r),div(mul(aa,A,d,sub(div(mul(two,add(r,o)),r),ep)),r));
 const rem1=div(mul(T,c,n,A,sub(o,b0),add(m,mul(F,y))),r);
 const rem2=div(mul(aa,A,d,add(mul(sub(o,cc),ep),div(mul(cc,d),T))),r);
 check(sub(actualXY(S(F)),add(rough,actualXY(rem1),rem2)),'FG_POSITIVE_REMAINDERS');
 const Bg=add(mul(ep,sub(R,div(two,r))),div(mul(aa,A,sub(div(mul(two,add(r,o)),r),ep)),r));
 const bgpos=add(div(mul(ep,add(mul(add(o,aa),pow(r,2)),mul(sub(two,aa),ep),sub(mul(cp(3),aa),two))),pow(r,2)),mul(sub(o,R),add(sub(mul(cp(3),aa),o),mul(add(aa,o),r),div(mul(two,aa,ep),r))));
 check(sub(Bg,bgpos),'FG_POSITIVE_Bg');
 check(sub(rough,add(mul(ep,sub(two,mul(R,add(o,r)))),mul(d,Bg))),'FG_ROUGH_REWRITE');
 const bgtail=add(div(mul(ep,add(pow(r,2),mul(sub(two,aa),ep),sub(mul(cp(3),aa),two))),pow(r,2)),mul(sub(o,R),add(sub(mul(cp(3),aa),o),r,div(mul(two,aa,ep),r))));
 check(sub(sub(Bg,mul(aa,A)),bgtail),'FG_BAD_Bg_MINUS_aA');
}
function tight(RR,TT,rr,Rlo,Tlo,xx,yy,xy){return add(div(mul(TT,sub(o,RR),sub(o,Rlo)),rr),mul(sub(o,mul(RR,TT)),sub(o,mul(Rlo,Tlo))),mul(RR,rr,sub(o,TT),sub(o,Tlo)),neg(mul(RR,add(TT,mul(rr,Tlo)),xx)),neg(div(mul(TT,add(RR,div(Rlo,rr)),yy),rr)),neg(div(mul(two,RR,TT,add(rr,o),xy),rr)),neg(div(mul(RR,TT,xx,yy),rr)))}
{
 // n,m are independent lower ratios here; xi,upsilon,Z are shear products.
 const lhs=tight(R,T,r,n,m,xi,y,Z);
 const rhs=tight(T,R,pow(r,-1),m,n,div(y,r),div(xi,r),div(Z,r));
 check(sub(lhs,rhs),'COMPLETE_MIDDLE_RHO_REFLECTION');
}
console.log('ALL_PASS: complete general middle coefficient endpoint and reflection identities');
