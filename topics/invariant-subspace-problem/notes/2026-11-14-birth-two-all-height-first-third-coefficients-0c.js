'use strict';
/* Exact universal polynomial identities used in the all-height birth-two P1/P3 proof. */
function setup(names){
 const c=a=>BigInt(a)===0n?new Map:new Map([[0,BigInt(a)]]);
 const add=(...ps)=>{const o=new Map;for(const p of ps)for(const[e,a]of p){const v=(o.get(e)||0n)+a;if(v)o.set(e,v);else o.delete(e)}return o};
 const neg=p=>new Map([...p].map(([e,a])=>[e,-a])),sub=(p,q)=>add(p,neg(q));
 const mul=(...ps)=>{let p=c(1);for(const q of ps){const o=new Map;for(const[e,a]of p)for(const[f,b]of q){
  for(let i=0;i<names.length;i++){const base=16**i;if(Math.floor(e/base)%16+Math.floor(f/base)%16>=16)throw Error('degree overflow');}
  const k=e+f;if(!Number.isSafeInteger(k))throw Error('unsafe exponent encoding');
  const v=(o.get(k)||0n)+a*b;if(v)o.set(k,v);else o.delete(k)
 }p=o}return p};
 const pow=(p,a)=>mul(...Array(a).fill(p));
 const vars=names.map((_,i)=>new Map([[16**i,1n]]));
 return{c,add,neg,sub,mul,pow,vars};
}
{
 const{c,add,neg,sub,mul,pow,vars}=setup(['n','m','R','T','rho','sigma','F','M1','N1']);
 const[n,m,R,T,rho,s,F,M,N]=vars,one=c(1),two=c(2);
 const A=sub(one,mul(R,rho)),d=sub(rho,T);
 const Ln=sub(mul(R,M),mul(n,s,A)),Wn=sub(mul(rho,s,N,T),mul(m,d));
 const D=mul(R,pow(M,2),pow(N,2),T,s);
 const direct=add(mul(T,sub(one,R),sub(mul(rho,D),mul(Ln,Wn,M,N))),mul(sub(one,mul(R,T)),sub(mul(pow(rho,2),D),mul(Wn,R,pow(M,2),N))),neg(mul(F,T,s,N,Wn,pow(A,2))),neg(mul(F,R,pow(M,2),pow(d,2))),mul(two,F,R,M,N,T,s,rho,A,d));
 const reduced=add(mul(pow(T,2),rho,A,pow(N,2),pow(s,2),sub(mul(n,M,sub(one,R)),mul(F,A))),mul(R,pow(M,2),d,sub(mul(m,N,sub(add(one,T),mul(two,R,T))),mul(F,d))),mul(R,pow(M,2),pow(N,2),T,s,sub(one,mul(R,T)),rho,sub(rho,one)),mul(N,T,s,A,d,add(neg(mul(n,m,M,sub(one,R))),mul(F,m,A),mul(two,F,rho,R,M))));
 if(sub(direct,reduced).size)throw Error('P1 Laurent identity');
 if(direct.size!==38)throw Error('P1 term count');
 console.log('P1_ALL_PARAMETERS_LAURENT_IDENTITY_PASS');
}
{
 const{c,add,neg,sub,mul,pow,vars}=setup(['n','m','R','T','h','sigma','F','xi','upsilon']);
 const[n,m,R,T,h,s,F,x,y]=vars,one=c(1),two=c(2);
 const A=sub(one,mul(n,x,s)),B=sub(mul(h,s),mul(m,pow(h,2),y));
 const direct=add(mul(h,s,T,sub(one,R),sub(h,A)),mul(sub(one,mul(R,T)),sub(mul(h,s),mul(A,B))),mul(R,sub(one,T),sub(s,B)),neg(mul(R,F,s,pow(x,2),add(mul(T,h,s),B))),neg(mul(T,pow(h,2),F,pow(y,2),add(R,A))),mul(two,R,T,add(one,h),F,x,y,h,s),neg(mul(R,T,pow(h,2),s,pow(F,2),pow(x,2),pow(y,2))));
 const kp=sub(mul(n,x,sub(add(one,T),mul(two,R,T))),mul(R,add(one,T),F,pow(x,2)));
 const km=sub(mul(m,h,y,sub(add(one,R),mul(two,R,T))),mul(T,h,add(one,R),F,pow(y,2)));
 const hk0=add(mul(h,sub(h,one),T,sub(one,R)),neg(mul(R,sub(h,one),sub(one,T))),neg(mul(m,n,pow(h,2),sub(one,mul(R,T)),x,y)),mul(R,m,pow(h,2),F,pow(x,2),y),mul(T,n,pow(h,2),F,x,pow(y,2)),mul(two,R,T,h,add(one,h),F,x,y),neg(mul(R,T,pow(h,2),pow(F,2),pow(x,2),pow(y,2))));
 const reduced=add(mul(h,kp,pow(s,2)),mul(hk0,s),mul(h,km));
 if(sub(direct,reduced).size)throw Error('P2 Laurent identity');
 if(direct.size!==24)throw Error('P2 term count');
 console.log('P2_ALL_PARAMETERS_LAURENT_IDENTITY_PASS');
}
/* Independent signed-exponent Laurent ring: exact direct quartic bridges.
   Tuple keys avoid any encoding collision or denominator specialization. */
function laurent(names){
 const zero=Array(names.length).fill(0).join(',');
 const c=a=>BigInt(a)===0n?new Map:new Map([[zero,BigInt(a)]]);
 const mon=o=>{const e=Array(names.length).fill(0);for(const[k,v]of Object.entries(o)){const i=names.indexOf(k);if(i<0)throw Error(k);e[i]=v;}return new Map([[e.join(','),1n]]);};
 const add=(...ps)=>{const out=new Map;for(const p of ps)for(const[k,v]of p){const w=(out.get(k)||0n)+v;if(w)out.set(k,w);else out.delete(k);}return out;};
 const neg=p=>new Map([...p].map(([k,v])=>[k,-v])),sub=(p,q)=>add(p,neg(q));
 const mul=(...ps)=>{let out=c(1);for(const p of ps){const next=new Map;for(const[k,v]of out)for(const[l,w]of p){const e=k.split(',').map(Number),f=l.split(',').map(Number),key=e.map((a,i)=>a+f[i]).join(','),z=(next.get(key)||0n)+v*w;if(z)next.set(key,z);else next.delete(key);}out=next;}return out;};
 return{c,mon,add,neg,sub,mul};
}
{
 const{c,mon,add,neg,sub,mul}=laurent(['R','T','h','u','R2','T2','xx','yy','xy']);
 const one=c(1),two=c(2),R=mon({R:1}),T=mon({T:1}),h=mon({h:1}),u=mon({u:1}),rr=mon({R2:1}),tt=mon({T2:1});
 const a=mon({u:-1,R:-1}),d=mon({u:2,T:-1}),v=mul(u,h),p=mon({u:-1,h:-1,R2:-1}),sv=mon({u:2,h:2,T2:-1});
 const xx=mon({xx:1}),yy=mon({yy:1}),xy=mon({xy:1});
 const la=[sub(mul(a,u),one),sub(mul(a,d),u),sub(d,mul(u,u))];
 const ph=[mul(p,sub(sv,mul(v,v))),mul(v,sub(mul(p,sv),v)),mul(v,sv,sub(mul(p,v),one))];
 const p2=add(mul(la[0],ph[2]),mul(la[1],ph[1]),mul(la[2],ph[0]),
  neg(mul(p,v,add(mul(u,sv),mul(d,v)),xx)),
  neg(mul(v,v,sv,add(a,p),yy)),neg(mul(two,p,v,sv,add(u,v),xy)),
  neg(mul(p,v,v,sv,xx,yy)));
 const compact=add(mul(h,T,sub(one,R),sub(one,rr)),mul(sub(one,mul(R,T)),sub(one,mul(rr,tt))),
  mul(mon({R:1,h:-1}),sub(one,T),sub(one,tt)),
  neg(mul(R,add(T,mon({T2:1,h:-1})),xx)),
  neg(mul(T,h,add(R,mul(h,rr)),yy)),neg(mul(two,R,T,add(one,h),xy)),
  neg(mul(R,T,h,xx,yy)));
 if(sub(mul(p2,mon({R:1,R2:1,T:1,T2:1,u:-3,h:-2})),compact).size)throw Error('P2 direct quartic bridge');
 console.log('P2_DIRECT_COMPLETE_QUARTIC_BRIDGE_PASS');
}
{
 const{c,mon,add,neg,sub,mul}=laurent(['R','T','rho','u','L','W','xx','yy','xy']);
 const one=c(1),two=c(2),R=mon({R:1}),T=mon({T:1}),rho=mon({rho:1}),u=mon({u:1}),L=mon({L:1}),W=mon({W:1});
 const a=mon({u:-1,R:-1}),d=mon({u:2,T:-1}),p=mon({u:-1,L:-1}),r=mon({u:1,rho:-1}),sv=mon({u:2,W:-1});
 const xx=mon({xx:1}),yy=mon({yy:1}),xy=mon({xy:1});
 const la0=sub(mul(a,u),one),la1=sub(mul(a,d),u);
 const ph0=mul(p,sub(sv,mul(r,r))),ph1=mul(r,sub(mul(p,sv),r));
 const p1=add(mul(la0,ph1),mul(la1,ph0),neg(mul(p,r,u,r,xx)),
  neg(mul(r,r,sv,a,p,yy)),neg(mul(two,p,r,sv,xy)));
 const compact=add(mul(T,sub(one,R),sub(rho,mul(L,W))),mul(sub(one,mul(R,T)),sub(mul(rho,rho),W)),
  neg(mul(R,T,W,xx)),neg(mul(T,yy)),neg(mul(two,R,T,rho,xy)));
 if(sub(mul(p1,mon({R:1,T:1,L:1,W:1,rho:2,u:-2})),compact).size)throw Error('P1 direct quartic bridge');
 console.log('P1_DIRECT_COMPLETE_QUARTIC_BRIDGE_PASS');
}


/* Exact positive boundary decomposition used for the nonpositive-Cplus sector. */
{
 const{c,add,neg,sub,mul,pow,vars}=setup(['n','m','R','T','G','alpha']);
 const[n,m,R,T,G,alpha]=vars,one=c(1),two=c(2),M=add(m,two),M1=add(m,one),N1=add(n,one);
 const F=sub(mul(n,M1),mul(M,alpha,R)),D=sub(G,mul(T,F)),A0=sub(F,mul(R,G)),E0=sub(F,G);
 const nb=sub(mul(sub(one,R),add(mul(R,T,pow(E0,2),m,pow(M1,2),N1),mul(n,pow(m,2),M1,D,A0))),
  mul(D,add(mul(pow(m,2),pow(A0,2)),neg(mul(two,R,E0,m,M1,A0)),mul(R,pow(E0,2),pow(M1,2)))));
 const positive=mul(R,add(mul(pow(E0,2),sub(mul(sub(one,R),T,m,pow(M1,2),N1),D)),
  mul(sub(one,R),D,m,M,add(mul(E0,G),mul(m,alpha,A0)))));
 if(sub(nb,positive).size)throw Error('P1 boundary positive decomposition');
 console.log('P1_EXACT_BOUNDARY_DECOMPOSITION_PASS');
}
{
 const{c,add,sub,mul,pow,vars}=setup(['x']);const[x]=vars,m=add(x,c(4)),M=add(m,c(2));
 const p=sub(mul(c(2),pow(m,2),pow(add(m,c(1)),2)),mul(pow(M,2),sub(mul(c(3),M),c(1))));
 const claimed=add(mul(c(2),pow(x,4)),mul(c(33),pow(x,3)),mul(c(189),pow(x,2)),mul(c(408),x),c(188));
 if(sub(p,claimed).size||[...p.values()].some(v=>v<=0n))throw Error('P1 m>=4 positive bracket');
 console.log('P1_HEIGHT_BOUND_POSITIVE_POLYNOMIAL_PASS');
}

/* The two remaining positive-Cplus curvature endpoints. */
{
 const{c,add,neg,sub,mul,pow,vars}=setup(['n','m','R','T','r']);
 const[n,m,R,T,r]=vars,o=c(1),two=c(2),M=add(m,o),N=add(n,o),ep=sub(o,r),A=sub(o,mul(R,r)),d=sub(r,T);
 const lhs=add(neg(mul(sub(o,mul(R,T)),r,ep,m,N,A)),mul(two,n,sub(o,R),r,d,m,A),mul(r,ep,A,m,N,sub(add(o,T),mul(two,R,T))),neg(mul(r,ep,n,M,sub(o,R),d)));
 const rhs=add(mul(r,sub(o,R),ep,T,m,N,A),mul(r,sub(o,R),n,d,sub(mul(two,m,A),mul(ep,M))));
 if(sub(lhs,rhs).size)throw Error('critical F boundary');
 if(lhs.size!==24)throw Error('critical F term count');
 const cpl=add(neg(mul(sub(o,mul(R,T)),r,ep,M)),mul(two,m,A,d),mul(T,ep,sub(add(r,o),mul(two,R,r)),M));
 const cpr=add(mul(pow(r,2),ep,sub(o,R),M),mul(d,sub(mul(two,m,A),mul(ep,add(o,r,neg(mul(R,r))),M))));
 if(sub(cpl,cpr).size)throw Error('cap F boundary');
 const bl=sub(mul(two,m,A),mul(ep,M,add(o,r,neg(mul(R,r)))));
 const br=add(mul(ep,sub(m,o)),mul(r,sub(o,R),sub(mul(two,m),mul(ep,M))));
 if(sub(bl,br).size)throw Error('cap positive bracket');
 if(cpl.size!==13)throw Error('cap F term count');
 console.log('P1_FCRIT_AND_FCAP_ENDPOINT_IDENTITIES_PASS');
}
{
 const{c,add,neg,sub,mul,pow,vars}=setup(['n','m','R','T','r','F']);
 const[n,m,R,T,r,F]=vars,o=c(1),two=c(2),M=add(m,o),N=add(n,o),e=sub(o,r),A=sub(o,mul(R,r)),d=sub(r,T);
 const direct=add(
  mul(pow(m,2),A,d,sub(mul(n,M,sub(o,R)),mul(F,A))),
  neg(mul(R,pow(e,2),m,pow(M,2),N,sub(o,mul(R,T)),r)),
  mul(e,m,A,d,add(neg(mul(n,m,M,sub(o,R))),mul(F,m,A),mul(two,F,r,R,M))),
  mul(R,pow(e,2),pow(M,2),r,sub(mul(m,N,sub(add(o,T),mul(two,R,T))),mul(F,d)))
 );
 const scaled=mul(r,sub(mul(sub(o,R),add(mul(R,T,pow(e,2),m,pow(M,2),N),mul(n,pow(m,2),M,d,A))),
  mul(F,d,add(mul(pow(m,2),pow(A,2)),neg(mul(two,R,e,m,M,A)),mul(R,pow(e,2),pow(M,2))))));
 if(sub(direct,scaled).size)throw Error('generic T2=1 endpoint bridge');
 console.log('P1_GENERIC_UPPER_ENDPOINT_BRIDGE_PASS');
}
{
 const{c,add,neg,sub,mul,pow,vars}=setup(['a','b','c','d','p','Q','r','s','x','y']);
 const[a,b,cc,d,p,Q,r,s,x,y]=vars,zero=c(0),two=c(2);
 function quartic(a,b,cc,d,p,Q,r,s,x,y){
  const L=[sub(mul(a,cc),mul(b,b)),sub(mul(a,d),mul(b,cc)),sub(mul(b,d),mul(cc,cc))];
  const Ph=[mul(p,Q,sub(mul(Q,s),mul(r,r))),mul(Q,r,sub(mul(p,s),mul(Q,r))),mul(r,s,sub(mul(p,r),mul(Q,Q)))];
  const out=Array.from({length:5},()=>zero);
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)out[i+j]=add(out[i+j],mul(Q,L[i],Ph[j]));
  const xr=[mul(cc,r),add(mul(cc,s),mul(d,r)),mul(d,s)];
  const yr=[mul(a,p),add(mul(a,Q),mul(b,p)),mul(b,Q)];
  const cr=[mul(b,Q),add(mul(b,r),mul(cc,Q)),mul(cc,r)];
  for(let j=0;j<3;j++)out[j+1]=add(out[j+1],
   neg(mul(p,pow(Q,3),r,xr[j],pow(x,2))),
   neg(mul(pow(Q,2),pow(r,2),s,yr[j],pow(y,2))),
   neg(mul(two,p,pow(Q,2),r,s,cr[j],x,y)));
  out[2]=sub(out[2],mul(p,pow(Q,3),pow(r,2),s,pow(x,2),pow(y,2)));
  return out;
 }
 const P=quartic(a,b,cc,d,p,Q,r,s,x,y),D=quartic(d,cc,b,a,s,r,Q,p,y,x);
 for(let i=0;i<5;i++)if(sub(mul(Q,D[4-i]),mul(r,P[i])).size)throw Error('quartic reflection coefficient '+i);
 console.log('P1_P3_COMPLETE_QUARTIC_REFLECTION_PASS');
}
if(!(175n*5n<144n*9n))throw Error('m=3 constants');
console.log('ALL_PASS: all-parameter identities for complete birth-two P1/P3; P2 positivity remains open');
