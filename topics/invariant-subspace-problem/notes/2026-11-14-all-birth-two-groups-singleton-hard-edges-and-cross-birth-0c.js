'use strict';
/* Exact complete hard-edge and cross-birth identities; no sampled parameters. */
function kernel(names) {
 const dim=names.length, zk=Array(dim).fill(0).join(',');
 const C=a=>BigInt(a)===0n?new Map:new Map([[zk,BigInt(a)]]);
 const add=(...ps)=>{const o=new Map;for(const p of ps)for(const[k,a]of p){const v=(o.get(k)||0n)+a;if(v)o.set(k,v);else o.delete(k)}return o};
 const neg=p=>new Map([...p].map(([k,a])=>[k,-a]));
 const sub=(p,q)=>add(p,neg(q));
 const mul=(...ps)=>{let p=C(1);for(const q of ps){const o=new Map;for(const[k,a]of p){const e=k.split(',').map(Number);for(const[l,b]of q){const f=l.split(',').map(Number),ex=e.map((v,i)=>v+f[i]);if(ex.some(v=>!Number.isSafeInteger(v)))throw Error('unsafe exponent');const key=ex.join(','),v=(o.get(key)||0n)+a*b;if(v)o.set(key,v);else o.delete(key)}}p=o}return p};
 const pow=(p,n)=>{if(n<0){if(p.size!==1)throw Error('nonmonomial inverse');const[[k,a]]=p;if(a!==1n&&a!==-1n)throw Error('nonunit inverse');return new Map([[k.split(',').map(v=>Number(v)*n).join(','),a===-1n&&(-n)%2?-1n:1n]])}let o=C(1);for(let i=0;i<n;i++)o=mul(o,p);return o};
 const div=(p,q)=>mul(p,pow(q,-1));
 const subs=(p,i,q)=>{let o=new Map;for(const[k,a]of p){const e=k.split(',').map(Number),v=e[i];if(v<0)throw Error('uncleared substitution');e[i]=0;o=add(o,mul(new Map([[e.join(','),a]]),pow(q,v)))}return o};
 const vars=names.map((_,i)=>{const e=Array(dim).fill(0);e[i]=1;return new Map([[e.join(','),1n]])});
 const check=(name,p)=>{if(p.size)throw Error(name+': '+p.size+' nonzero terms');console.log(name+'_PASS')};
 return{C,add,neg,sub,mul,pow,div,subs,vars,check};
}
{
 const{C,add,neg,sub,mul,pow,div,subs,vars,check}=kernel(['R','r','T','c','f']);
 const[R,r,T,c,f]=vars,o=C(1),two=C(2),four=C(4);
 const e=sub(o,r),d=sub(r,T),A=sub(o,mul(R,r));
 const R2twice=sub(mul(two,r),div(mul(c,d,A),mul(R,T)));
 const Base=add(div(mul(T,e,sub(o,R)),r),sub(o,mul(R,T)),mul(R,r,sub(o,T)));
 const E4=add(div(mul(two,T,sub(o,R),sub(two,R2twice)),r),
  mul(four,sub(o,mul(R,T))),mul(four,R,r,sub(o,T)),
  neg(div(mul(f,d,pow(A,2)),mul(r,R))),
  neg(mul(two,f,d,add(mul(two,R),div(R2twice,r)))),
  div(mul(four,f,d,A,add(r,o)),r),
  neg(div(mul(pow(f,2),pow(d,2),pow(A,2)),mul(r,T,R))));
 const expansion4=add(mul(four,Base),
  div(mul(four,f,d,sub(o,mul(R,r,add(r,two)))),r),
  div(mul(A,d,sub(mul(two,c,sub(o,R)),mul(f,A))),mul(R,r)),
  div(mul(f,A,pow(d,2),sub(mul(two,c),mul(f,A))),mul(R,r,T)));
 check('HARD_GENERAL_EXPANSION',sub(E4,expansion4));
 const Fn4=subs(E4,4,mul(two,c));
 const Fn0=add(div(mul(four,T,e),r),four,
  div(mul(two,c,d,add(C(3),r)),r),div(mul(four,pow(c,2),pow(d,2)),T));
 const Fn1=add(mul(four,add(o,r),sub(o,T)),
  div(mul(two,c,d,add(C(3),neg(mul(C(6),r)),neg(mul(C(5),pow(r,2))))),r),
  div(mul(four,pow(c,2),e,pow(d,2)),T));
 check('HARD_FN_R0',sub(subs(Fn4,0,C(0)),Fn0));
 check('HARD_FN_R1',sub(subs(Fn4,0,o),Fn1));
 check('HARD_FN_AFFINE',sub(Fn4,add(mul(sub(o,R),Fn0),mul(R,Fn1))));
 check('HARD_FN_LAST_LINEAR_BOUND',sub(add(mul(four,r,add(o,r)),C(3),neg(mul(C(6),r)),neg(mul(C(5),pow(r,2)))),mul(e,add(r,C(3)))));
 const Fg4=subs(E4,4,div(o,r));
 const FgClaim4=add(mul(four,Base),
  div(mul(four,d,sub(o,mul(R,r,add(r,two)))),pow(r,2)),
  div(mul(A,d,sub(mul(two,c,r,sub(o,R)),A)),mul(R,pow(r,2))),
  div(mul(A,pow(d,2),sub(mul(two,c,r),A)),mul(R,pow(r,3),T)));
 check('HARD_FG_EXPANSION',sub(Fg4,FgClaim4));
 const L4=add(mul(four,Base),
  div(mul(four,d,sub(o,mul(R,r,add(r,two)))),pow(r,2)),
  neg(div(mul(A,d,e),pow(r,2))),div(mul(A,pow(d,2)),mul(pow(r,2),T)));
 const rem=div(mul(A,d,sub(mul(two,c,r),o),add(sub(o,R),div(d,mul(r,T)))),mul(R,pow(r,2)));
 check('HARD_FG_CAP_REMAINDER',sub(sub(Fg4,L4),rem));
 const L0=add(div(mul(four,T,e),r),four,
  div(mul(d,add(C(3),r)),pow(r,2)),div(pow(d,2),mul(pow(r,2),T)));
 const coeff=add(mul(four,pow(r,3)),neg(pow(r,2)),neg(mul(C(6),r)),C(3));
 const L1=add(mul(four,add(o,r),e),div(mul(d,coeff),pow(r,2)),div(mul(e,pow(d,2)),mul(pow(r,2),T)));
 check('HARD_FG_R0',sub(subs(L4,0,C(0)),L0));
 check('HARD_FG_R1',sub(subs(L4,0,o),L1));
 check('HARD_FG_AFFINE',sub(L4,add(mul(sub(o,R),L0),mul(R,L1))));
 check('HARD_FG_LAST_LINEAR_BOUND',sub(add(mul(four,r,add(o,r),e),coeff),mul(e,add(r,C(3)))));
}
{
 const{C,add,neg,sub,mul,pow,vars,check}=kernel(['n','m','R','T','U','V']);
 const[n,m,R,T,U,V]=vars,o=C(1),M1=add(m,o),N1=add(n,o),M=add(m,C(2));
 const F=sub(mul(n,M1),mul(R,sub(mul(N1,M),U)));
 const G=sub(mul(m,N1),mul(T,sub(mul(add(n,C(2)),M1),V)));
 const D=sub(G,mul(T,F));
 const rhs=add(D,mul(N1,sub(mul(T,add(m,mul(M,sub(o,R)))),m)));
 check('CROSS_BIRTH_UPPER_DIFFERENCE',sub(mul(T,sub(V,mul(R,U))),rhs));
}
{
 const{C,add,neg,sub,mul,pow,vars,check}=kernel(['n','m','R','T','alpha','G']);
 const[n,m,R,T,alpha,G]=vars,o=C(1),M1=add(m,o),N1=add(n,o),M=add(m,C(2));
 const F=sub(mul(n,M1),mul(M,alpha,R));
 const E0=sub(F,G),D=sub(G,mul(T,F)),A0=sub(F,mul(R,G));
 const NB=sub(mul(sub(o,R),add(mul(R,T,pow(E0,2),m,pow(M1,2),N1),mul(n,pow(m,2),M1,D,A0))),
  mul(D,add(mul(pow(m,2),pow(A0,2)),neg(mul(C(2),R,E0,m,M1,A0)),mul(R,pow(E0,2),pow(M1,2)))));
 const positive=add(mul(sub(o,R),T,m,pow(M1,2),N1,pow(E0,2)),
  mul(D,E0,sub(mul(sub(o,R),m,M,G),E0)),
  mul(sub(o,R),D,pow(m,2),M,alpha,A0));
 check('GENERAL_BAD_P1_POSITIVE_REGROUPING',sub(NB,mul(R,positive)));
}
console.log('ALL_PASS: exact hard-edge and cross-birth identities');
