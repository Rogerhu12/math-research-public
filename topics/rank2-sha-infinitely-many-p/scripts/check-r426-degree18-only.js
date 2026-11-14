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
const fieldPrime=1009;
const md=x=>((x%fieldPrime)+fieldPrime)%fieldPrime;
function mpow(x,n){let r=1;while(n){if(n&1)r=md(r*x);x=md(x*x);n=Math.floor(n/2);}return r;}
const minv=x=>mpow(md(x),fieldPrime-2);
function reduceField(q){return md((Number(q[0]%1009n)+260*Number(q[1]%1009n))*minv(Number(q[2]%1009n)));}
function solveMod(A,b){
 const M=A.map((row,i)=>[...row,b[i]]),n=b.length;
 for(let j=0;j<n;j++){
  let k=j;while(k<n&&!M[k][j])k++;if(k===n)throw Error('singular interpolation');
  [M[j],M[k]]=[M[k],M[j]];const u=minv(M[j][j]);M[j]=M[j].map(x=>md(x*u));
  for(let i=0;i<n;i++)if(i!==j){const q=M[i][j];M[i]=M[i].map((x,k)=>md(x-q*M[j][k]));}
 }
 return M.map(row=>row[n]);
}
function matrix18(offset){
 const size=offset?3:4;
 const evaluation=Array.from({length:size},(_,i)=>Array.from({length:size},(_,j)=>mpow((i+1)**3,j)));
 const columns=[];
 for(let j=0;j<size;j++){
  const P=Array.from({length:size},(_,k)=>k===j?o:z);
  const values=Array.from({length:size},(_,i)=>md(reduceField(mul(norm,exactTrace(18,offset,i+1,P)))*minv(mpow(i+1,offset))));
  columns.push(solveMod(evaluation,values));
 }
 return Array.from({length:size},(_,i)=>columns.map(column=>column[i]));
}
function determinant(M){
 M=M.map(row=>row.slice());let d=1;
 for(let j=0;j<M.length;j++){
  let k=j;while(k<M.length&&!M[k][j])k++;if(k===M.length)return 0;
  if(k!==j){[M[j],M[k]]=[M[k],M[j]];d=md(-d);}
  const a=M[j][j];d=md(d*a);const u=minv(a);
  for(let i=j+1;i<M.length;i++){const q=md(M[i][j]*u);for(let k=j;k<M.length;k++)M[i][k]=md(M[i][k]-q*M[j][k]);}
 }
 return d;
}
const matrixG=matrix18(0),matrixF=matrix18(1),rootOmega=reduceField(omega);
const minorG=determinant(matrixG.slice(0,3).map((row,i)=>row.slice(0,3).map((x,j)=>md(x-(i===j?rootOmega:0)))));
const minorF=determinant(matrixF.slice(0,2).map((row,i)=>row.slice(0,2).map((x,j)=>md(x-(i===j?1:0)))));
if(minorG!==899||minorF!==450)throw Error('CM7 eigenspace uniqueness');
console.log(JSON.stringify({fieldPrime,delta:260,rootOmega,matrixG,matrixF,minorG,minorF}));
console.log('Both displayed degree18 CM7 eigenlines are unique in their full angular blocks.');
