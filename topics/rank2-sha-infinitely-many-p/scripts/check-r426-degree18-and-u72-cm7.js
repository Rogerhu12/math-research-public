// Exact Q(sqrt(-3)) finite-fiber certificate for R426.
// Built-in BigInt only; no target-prime scan.
"use strict";

function exactTrace(N,offset,a0,coeff){
const abs=a=>a<0n?-a:a;function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b];}return a;}
function f(a,b=0n,c=1n){if(typeof a==="number")a=BigInt(a);if(typeof b==="number")b=BigInt(b);if(typeof c==="number")c=BigInt(c);if(c<0n){a=-a;b=-b;c=-c;}let g=gcd(gcd(a,b),c);return [a/g,b/g,c/g];}
const z=f(0),o=f(1),D=f(0,1),add=(x,y)=>f(x[0]*y[2]+y[0]*x[2],x[1]*y[2]+y[1]*x[2],x[2]*y[2]),neg=x=>[-x[0],-x[1],x[2]],sub=(x,y)=>add(x,neg(y)),mul=(x,y)=>f(x[0]*y[0]-3n*x[1]*y[1],x[0]*y[1]+x[1]*y[0],x[2]*y[2]),iv=x=>f(x[2]*x[0],-x[2]*x[1],x[0]*x[0]+3n*x[1]*x[1]);
function pow(a,n){let v=o;while(n){if(n%2)v=mul(v,a);a=mul(a,a);n=Math.floor(n/2);}return v;}
const eq=(x,y)=>x.every((v,i)=>v===y[i]),zero=x=>x[0]===0n&&x[1]===0n;
const gam=f(5,1,2),gb=f(5,-1,2),r=f(2,-6,7),rb=f(2,6,7),a=f(a0),ga=mul(pow(gam,2),a);
const F=[neg(mul(ga,pow(r,2))),mul(r,add(mul(f(7),r),f(24))),z,mul(f(2),mul(ga,r)),add(mul(f(28),r),f(12)),z,neg(ga),o];
function trim(A){while(A.length>1&&zero(A.at(-1)))A.pop();return A;}
function pa(A,B){let C=Array.from({length:Math.max(A.length,B.length)},()=>z);for(let i=0;i<C.length;i++)C[i]=add(A[i]||z,B[i]||z);return trim(C);}
function pn(A){return A.map(neg);}
function pc(A,c){return trim(A.map(x=>mul(x,c)));}
function pm(A,B){let C=Array.from({length:A.length+B.length-1},()=>z);for(let i=0;i<A.length;i++)for(let j=0;j<B.length;j++)C[i+j]=add(C[i+j],mul(A[i],B[j]));return trim(C);}
function div(A,B){A=A.slice();let Q=Array.from({length:Math.max(1,A.length-B.length+1)},()=>z);const ib=iv(B.at(-1));while(A.length>=B.length&&!(A.length===1&&zero(A[0]))){let k=A.length-B.length,v=mul(A.at(-1),ib);Q[k]=v;for(let j=0;j<B.length;j++)A[k+j]=sub(A[k+j],mul(v,B[j]));trim(A);}return [trim(Q),trim(A)];}
function red(A){A=A.slice();for(let i=A.length-1;i>=7;i--){let v=A[i];if(!zero(v))for(let j=0;j<7;j++)A[i-7+j]=sub(A[i-7+j],mul(v,F[j]));}return trim(A.slice(0,7));}
const rm=(A,B)=>red(pm(A,B));
function rp(A,n){let V=[o];while(n){if(n%2)V=rm(V,A);A=rm(A,A);n=Math.floor(n/2);}return V;}
function ri(A){let r0=F,r1=A,s0=[z],s1=[o];while(!(r1.length===1&&zero(r1[0]))){let [q,r2]=div(r0,r1),s2=pa(s0,pn(pm(q,s1)));[r0,r1,s0,s1]=[r1,r2,s1,s2];}if(r0.length!==1)throw Error("nonunit");return red(pc(s0,iv(r0[0])));}
const q=[neg(r),z,z,o],qb=[neg(rb),z,z,o];
const Nb=[mul(rb,add(mul(f(7),rb),f(24))),z,z,add(mul(f(28),rb),f(12)),z,z,o];
const T1=rm([z,o],Nb),V1=pc(rp(qb,2),pow(gb,2));
const U=rp(T1,3),W=rp(V1,3);
const d=Math.floor((N/2-offset)/3),rem=N/2-offset-3*d;
const P=coeff.map(x=>f(...x));while(P.length<d+1)P.push(z);
let E=[P[d]],Wp=[o];for(let i=d-1;i>=0;i--){Wp=rm(Wp,W);E=pa(rm(E,U),pc(Wp,P[i]));}
E=rm(E,rm(rp(T1,offset),rp(V1,rem)));
const Eout=pc(rm(rp(ri(q),N),E),pow(iv(gam),N));
const tr=[f(7)];for(let k=1;k<=6;k++){let v=mul(f(k),F[7-k]);for(let j=1;j<k;j++)v=add(v,mul(F[7-j],tr[k-j]));tr[k]=neg(v);}
let got=z;for(let i=0;i<Eout.length;i++)got=add(got,mul(Eout[i],tr[i]));
globalThis.ops={f,add,sub,mul,iv,neg,pm,pc,pa,z,o,pow,eq};
return got;
}

exactTrace(18,0,1,[[0n,0n,1n]]);
const {f,add,sub,mul,iv,pm,pc,z,o,pow,eq}=ops;
const gamma=f(5,1,2),omega=f(-1,1,2),omega2=f(-1,-1,2),norm=iv(mul(omega,gamma));
const evalpoly=(P,x)=>P.reduceRight((v,c)=>add(mul(v,x),c),z);
const G=[-32,-144,-30,1].map(x=>f(x));
const F=[f(16,0,7),f(-4,0,7),o];
for(let a=1;a<=4;a++)if(!eq(exactTrace(18,0,a,G),mul(mul(omega2,gamma),evalpoly(G,f(a**3)))))throw Error('G18 exact fiber');
for(let a=1;a<=3;a++)if(!eq(exactTrace(18,1,a,F),mul(mul(omega,gamma),mul(f(a),evalpoly(F,f(a**3))))))throw Error('F18 exact fiber');
console.log('Exact degree18 CM7 eigenfunctions passed: G eigen omega^2*gamma; F eigen omega*gamma.');
let U=[[0,1],[1,1],[-8,1],[-8,1],[-8,20,1]].map(a=>a.map(x=>f(x))).reduce(pm,[o]);
U=pm(pm(U,F),G);while(U.length<13)U.push(z);
function interpolate(values){
 let out=Array.from({length:13},()=>z);
 for(let i=0;i<13;i++){
  let poly=[o],den=o;const xi=BigInt((i+1)**3);
  for(let j=0;j<13;j++)if(i!==j){let xj=BigInt((j+1)**3);poly=pm(poly,[f(-xj),o]);den=mul(den,f(xi-xj));}
  poly=pc(poly,mul(values[i],iv(den)));
  for(let j=0;j<13;j++)out[j]=add(out[j],poly[j]||z);
 }
 return out;
}
let orbit=[U];const started=Date.now();
for(let n=1;n<=4;n++){
 const values=Array.from({length:13},(_,i)=>exactTrace(72,0,i+1,orbit[n-1]));
 orbit.push(interpolate(values).map(x=>mul(norm,x)));
 console.log('Exact U72 power',n,'elapsed_ms',Date.now()-started);
}
const residual=orbit[4].map((x,i)=>add(sub(x,mul(add(o,omega),orbit[2][i])),mul(omega,U[i])));
if(!residual.every(x=>eq(x,z)))throw Error('U72 exact quartic identity');
const q1=orbit[2].map((x,i)=>mul(iv(sub(o,omega)),sub(x,mul(omega,U[i]))));
const q1n=orbit[3].map((x,i)=>mul(iv(sub(o,omega)),sub(x,mul(omega,orbit[1][i]))));
const qo=U.map((x,i)=>sub(x,q1[i])),qon=orbit[1].map((x,i)=>sub(x,q1n[i]));
const parts=[
 ['1',q1.map((x,i)=>mul(f(1,0,2),add(x,q1n[i])))],
 ['-1',q1.map((x,i)=>mul(f(1,0,2),sub(x,q1n[i])))],
 ['omega2',qo.map((x,i)=>mul(f(1,0,2),add(x,mul(omega,qon[i]))))],
 ['-omega2',qo.map((x,i)=>mul(f(1,0,2),sub(x,mul(omega,qon[i]))))]
];
for(const [label,P]of parts){
 const expected=label.includes('omega')?f(-1,0,12):f(1,0,12);
 if(!eq(P[12],expected))throw Error('U72 component mass '+label);
 console.log('U72 component',label,'exact_mass',P[12].map(String));
}
console.log('Exact identity: (N^2-1)(N^2-omega) U72=0; all four spectral components nonzero.');
