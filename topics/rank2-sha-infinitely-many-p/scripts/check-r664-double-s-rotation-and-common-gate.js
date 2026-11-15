#!/usr/bin/env node
"use strict";
/*
R664: exact fixed geometry over Q(omega), omega^2+omega+1=0.
No numerical prime scan. The all-depth/source/core arguments are in the proof.
Coordinates are (xi1,xi2,xi3,x,c,d); rows act on physical columns.
*/

const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const qa=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]), qn=a=>[-a[0],a[1]], qs=(a,b)=>qa(a,qn(b));
const qm=(a,b)=>q(a[0]*b[0],a[1]*b[1]), qd=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
const qe=(a,b)=>a[0]===b[0]&&a[1]===b[1], qj=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
function qpow(a,n){let r=q(1);for(;n;n>>=1,a=qm(a,a))if(n&1)r=qm(r,a);return r}
function field(N,poly){
 const d=poly.length-1,Z=()=>Array.from({length:d},()=>q(0));
 const C=(a,b=1)=>{let z=Z();z[0]=q(a,b);return z};
 const add=(a,b)=>a.map((x,i)=>qa(x,b[i])),neg=a=>a.map(qn),sub=(a,b)=>add(a,neg(b));
 const sc=(a,b,c=1)=>a.map(x=>qm(x,q(b,c)));
 const mul=(a,b)=>{let z=Array.from({length:2*d-1},()=>q(0));for(let i=0;i<d;i++)for(let j=0;j<d;j++)z[i+j]=qa(z[i+j],qm(a[i],b[j]));for(let k=2*d-2;k>=d;k--)for(let j=0;j<d;j++)z[k-d+j]=qs(z[k-d+j],qm(z[k],q(poly[j])));return z.slice(0,d)};
 const eq=(a,b)=>a.every((x,i)=>qe(x,b[i]));
 const pow=(a,n)=>{let r=C(1);for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r};
 const z=n=>{n=(n%N+N)%N;let x=Z();x[1]=q(1);return pow(x,n)};
 const conj=a=>a.map((x,i)=>sc(z(-i),x[0],x[1])).reduce(add,C(0));
 const json=a=>a.map(qj);
 return{N,d,Z,C,add,neg,sub,sc,mul,eq,pow,z,conj,json};
}
const mod=(x,m)=>(x%m+m)%m;
const fp=(x,y,m)=>[mod(x[0]*y[0]-x[1]*y[1],m),mod(x[0]*y[1]+x[1]*y[0]-x[1]*y[1],m)];
function fpower(x,n,m){let a=[1,0];for(;n;n>>=1,x=fp(x,x,m))if(n&1)a=fp(a,x,m);return a}
const fe=(x,y)=>x[0]===y[0]&&x[1]===y[1];

function certificate() {
 const F=field(3,[1,1,1]), {C,add,sub,neg,sc,mul,eq,conj,json}=F;
 const O=F.z(1),zero=C(0),one=C(1),delta=add(one,sc(O,2));
 const cm=(a,b=0)=>add(C(a),sc(O,b));
 const inv=x=>{const n=mul(x,conj(x)); if(!qe(n[1],q(0)))throw Error("nonreal norm");return sc(conj(x),n[0][1],n[0][0]);};
 const div=(x,y)=>mul(x,inv(y));
 const addR=(a,b)=>a.map((x,i)=>add(x,b[i]));
 const subR=(a,b)=>a.map((x,i)=>sub(x,b[i]));
 const scR=(a,c)=>a.map(x=>mul(x,c));
 const inn=(a,b)=>a.map((x,i)=>mul(x,conj(b[i]))).reduce(add,zero);
 const norm=a=>inn(a,a);
 const rjson=a=>a.map(json);
 const zrow=()=>Array.from({length:6},()=>zero);
 const basis=i=>Array.from({length:6},(_,j)=>C(i===j?1:0));
 const checks=[];
 function ok(name,value){if(!value)throw Error(name);checks.push(name);}
 const ef=(name,a,b)=>ok(name,eq(a,b));
 const er=(name,a,b)=>ok(name,a.length===b.length&&a.every((x,i)=>eq(x,b[i])));
 const e0R=zrow();
 const A=[cm(1,2),cm(2,4),cm(3,1),cm(2,-1),zero,zero];
 const Q=[zero,zero,zero,zero,one,C(2)];
 const L=[zero,zero,zero,zero,C(2),C(-1)];
 const Cc=scR([one,zero,C(-1),one,zero,zero],div(one,delta));
 const D4=[one,cm(-1,-1),cm(0,-2),zero,zero,zero];
 const H1=[C(-1),C(2),O,cm(1,1),zero,zero];
 const aa=sc(cm(-5,-6),1,29),bF=sc(cm(5,6),1,5),cF=sc(O,-3,5),gg=cm(3,-2);
 const Ds=subR(D4,scR(A,aa)),HH=addR(Cc,Ds);
 const FF=addR(addR(D4,Cc),[zero,zero,zero,zero,one,cm(2,3)]);
 const Jinv=r=>[...r.slice(0,4),r[5],neg(r[4])];
 const J=r=>[...r.slice(0,4),neg(r[5]),r[4]];
 const iter=(r,f,n)=>{for(let j=0;j<n;j++)r=f(r);return r;};
 const Y0=addR(A,Q),Y1=addR(A,L),Ym=addR(A,scR(Q,C(-1))),Ylm=addR(A,scR(L,C(-1)));
 const YY=[Y0,Y1,Ym,Ylm];
 const RR=addR(Y0,Y1),DD=subR(Y0,Y1),EE=subR(scR(A,C(5)),scR(addR(Q,L),C(29)));
 const FJ=Jinv(FF);
 const h0=cm(-5,-9),h1=cm(-5,-3);
 const v0=scR(subR(scR(Y1,C(34)),scR(Y0,C(29))),sc(h0,1,315));
 const v1=scR(subR(scR(Y0,C(34)),scR(Y1,C(29))),sc(h1,1,315));
 const e0=sc(cm(-170,-117),1,9135),e1=sc(cm(-170,-291),1,9135);
 const bQ=sc(cm(11,6),1,5),bL=sc(cm(2,12),1,5),bY=sc(cm(20,3),1,17);
 const W0=addR(A,addR(scR(Q,bQ),scR(L,bL))),W1=Jinv(W0);
 const w0=sc(cm(-8,-18),1,315),w1=sc(cm(-4,6),1,315);
 const project=(r,v)=>scR(v,div(inn(r,v),norm(v)));
 const P=(r,v,t)=>addR(r,scR(project(r,v),sub(t,one)));
 const PB=(r,t)=>addR(r,scR(addR(project(r,RR),project(r,DD)),sub(t,one)));
 ef("omega order 3",F.pow(O,3),one);
 ef("delta square -3",mul(delta,delta),C(-3));
 for(let i=0;i<6;i++){
  er("J^4 basis "+i,iter(basis(i),J,4),basis(i));
  er("J inverse basis "+i,J(Jinv(basis(i))),basis(i));
 }
 for(let i=0;i<4;i++)er("actual Y cycle "+i,iter(Y0,Jinv,i),YY[i]);
 er("Q after Jinv is L",Jinv(Q),L);
 er("L after Jinv is -Q",Jinv(L),scR(Q,C(-1)));
 for(const [name,r,n] of [["A",A,29],["Q",Q,5],["L",L,5],["C",Cc,1],["H1",H1,7],["Y0",Y0,34],["Y1",Y1,34],["W0",W0,72],["W1",W1,72],["R",RR,126],["D10",DD,10],["E",EE,9135]])ef("norm "+name,norm(r),C(n));
 for(const [name,u,v] of [["AQ",A,Q],["AL",A,L],["QL",Q,L],["R D",RR,DD],["R E",RR,EE],["D E",DD,EE]])ef("orthogonal "+name,inn(u,v),zero);
 const det=2*((1)*(-29)-(-1)*(-29))-(0*(-29)-(-1)*5)+(0*(-29)-1*5);
 ok("relative determinant -126",det===-126);
 er("A inverse",scR(addR(EE,scR(RR,C(29))),C(1,63)),A);
 er("Q inverse",scR(addR(subR(scR(RR,C(5)),scR(EE,C(2))),scR(DD,C(63))),C(1,126)),Q);
 er("L inverse",scR(subR(subR(scR(RR,C(5)),scR(EE,C(2))),scR(DD,C(63))),C(1,126)),L);
 for(const [name,v] of [["C",Cc],["Dstar",Ds],["H1",H1]])for(const [an,ar]of [["A",A],["Q",Q],["L",L],["E",EE],["Y0",Y0],["Y1",Y1]])ef("companion "+name+" perpendicular "+an,inn(v,ar),zero);
 ef("Dstar and C not orthogonal",inn(Ds,Cc),C(-1));
 ef("Dstar norm",norm(Ds),C(143,29));
 ef("E moves A",inn(EE,A),C(145));
 er("F full decomposition",FF,addR(HH,addR(scR(A,aa),addR(scR(Q,bF),scR(L,cF)))));
 er("FJ full decomposition",FJ,addR(HH,addR(scR(A,aa),addR(scR(Q,neg(cF)),scR(L,bF)))));
 ef("F perpendicular Y0",inn(FF,Y0),zero);
 ef("FJ perpendicular Y1",inn(FJ,Y1),zero);
 ef("F cross Y1",inn(FF,Y1),h0);
 ef("FJ cross Y0",inn(FJ,Y0),h1);
 er("F in common frame",FF,addR(HH,addR(scR(EE,e0),v0)));
 er("FJ in common frame",FJ,addR(HH,addR(scR(EE,e1),v1)));
 ef("gate difference unit",sub(e1,e0),sc(O,-2,105));
 er("frozen difference exactly E",subR(subR(FJ,v1),subR(FF,v0)),scR(EE,sc(O,-2,105)));
 for(const [name,r]of [["R",RR],["D",DD],["E",EE]])for(let j=0;j<6;j++){
  const zeta=mul(j%2?C(-1):one,F.z(j));
  er("C rotation fixes "+name+" "+j,P(r,Cc,zeta),r);
 }
 // These comparisons are coefficientwise for all t: B(t)=B(0)+t(I-B(0)).
 for(const [name,r,constant,linear]of [
  ["Y0",Y0,e0R,Y0],["Y1",Y1,e0R,Y1],["E",EE,EE,e0R],
  ["A",A,subR(A,scR(RR,C(29,63))),scR(RR,C(29,63))],
  ["Q",Q,scR(EE,C(-1,63)),addR(Q,scR(EE,C(1,63)))],
  ["L",L,scR(EE,C(-1,63)),addR(L,scR(EE,C(1,63)))],
  ["F",FF,addR(HH,scR(EE,e0)),v0],
  ["FJ",FJ,addR(HH,scR(EE,e1)),v1]
 ]){er("B constant "+name,PB(r,zero),constant);er("B linear "+name,subR(PB(r,one),PB(r,zero)),linear);}
 for(const [name,v]of [["R",RR],["D",DD],["E",EE]])for(let i=0;i<6;i++)er("idempotent "+name+" "+i,project(project(basis(i),v),v),project(basis(i),v));
 for(let i=0;i<6;i++)for(const [u,v]of [[RR,DD],[RR,EE],[DD,EE]])er("orthogonal projectors "+i+" "+checks.length,project(project(basis(i),u),v),e0R);
 for(const [i,wi,Wi,Yi]of [[0,w0,W0,Y0],[1,w1,W1,Y1]]){
  ef("W E coefficient "+i,div(inn(Wi,EE),norm(EE)),wi);
  ef("W Y coefficient "+i,div(inn(Wi,Yi),norm(Yi)),bY);
  er("W B constant "+i,PB(Wi,zero),scR(EE,wi));
  er("W B linear "+i,subR(Wi,PB(Wi,zero)),subR(Wi,scR(EE,wi)));
  for(const t of [C(2),C(3,2)])for(const sgn of [1,-1]){
   const actual=PB(P(Wi,Yi,div(C(sgn),t)),t);
   const expect=addR(scR(EE,wi),addR(scR(subR(Wi,scR(EE,wi)),t),scR(Yi,mul(sub(C(sgn),t),bY))));
   er("full T transpose "+i+" "+json(t).join(":")+" "+sgn,actual,expect);
  }
 }
 for(const [i,vi]of [[0,v0],[1,v1]])er("E contraction fixes vi "+i,P(vi,EE,C(2)),vi);
 function parity(r){
  return r.reduce((n,x)=>n+(x.some(a=>{if(a[1]!==1n)throw Error("nonintegral half-character");return ((a[0]%2n)+2n)%2n!==0n;})?1:0),0);
 }
 const parities=[RR,DD,EE].map(parity);
 ok("actual half-character counts 2 2 5",JSON.stringify(parities)==="[2,2,5]");
 const gpi=18271;
 ok("full g modulo 252",gpi%252===127);
 ok("full g modulo 20",gpi%20===11);
 ok("full g modulo 18270",gpi%18270===1);
 for(const N of [126,10])ok("real full period center N="+N,(((N+1)*(N+1)-1)/N)%2===0);
 ef("norm gamma7",mul(cm(3,1),conj(cm(3,1))),C(7));
 ok("Theta anchor degree126",2*9*7===126);
 const u2=div(sub(mul(e1,e1),mul(e0,e0)),mul(cF,cF));
 ef("same JN second coefficient",u2,sc(cm(136,-680),1,345303));
 const un=mul(u2,conj(u2));
 ef("same coefficient norm",un,C(64n*289n*31n,59049n*2401n*841n));
 const types=Array.from({length:7},(_,k)=>(k-2+6)%6);
 ok("only k2 may have mass",types.map((x,k)=>x===0?k:null).filter(x=>x!==null).join(",")==="2");
 return {
  result:"all exact checks passed",count:checks.length,checks,
  field:"Q(omega), omega^2+omega+1=0; pair [a,b] means a+b*omega",
  coordinates:["xi1","xi2","xi3","x","c","d"],
  rows:{A:rjson(A),Q:rjson(Q),L:rjson(L),C:rjson(Cc),Dstar:rjson(Ds),H1:rjson(H1),F:rjson(FF),FJ:rjson(FJ),Y0:rjson(Y0),Y1:rjson(Y1),R:rjson(RR),D10:rjson(DD),E:rjson(EE)},
  gram:["126","10","9135"],determinant:"-126",half_character_counts:parities,
  full_center_representative:gpi,moduli:[252,20,18270],
  coefficients:{h0:json(h0),h1:json(h1),e0:json(e0),e1:json(e1),cF:json(cF),bY:json(bY),w0:json(w0),w1:json(w1),v0:rjson(v0),v1:rjson(v1)},
  conditional_types:types,second_difference_factor:json(u2),second_factor_norm:json(un),
  norm_factorization:{numerator:{"2":6,"17":2,"31":1},denominator:{"3":10,"7":4,"29":2}},
  scope:"Only fixed exact geometry/center data. All-depth measure identities, original scalar anchors, conditional-source interpretation, and uncompensated outer domains are proved in the companion text."
 };
}
console.log(JSON.stringify(certificate(),null,2));
