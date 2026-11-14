// Exact certificate for R398. Run with: node check-e24-original-degree72-cm7-source.js
// Uses only built-in BigInt arithmetic; no network, file access, or external package.
"use strict";

function exactCM7(a0){
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
const U=rm([z,z,z,o],rp(Nb,3)),W=pc(rp(qb,6),pow(gb,6));
const R=[1024,-1920,-1632,104,-1128,87,7].map(x=>f(x)),Q=[256,256,-336,-92,1].map(x=>f(x));
const P=pm([z,o],pm(Q,R));while(P.length<13)P.push(z);
let E=[P[12]],Wp=[o];for(let i=11;i>=0;i--){Wp=rm(Wp,W);E=pa(rm(E,U),pc(Wp,P[i]));}
const Eout=pc(rm(rp(ri(q),72),E),pow(iv(gam),72));
const tr=[f(7)];for(let k=1;k<=6;k++){let v=mul(f(k),F[7-k]);for(let j=1;j<k;j++)v=add(v,mul(F[7-j],tr[k-j]));tr[k]=neg(v);}
let got=z;for(let i=0;i<Eout.length;i++)got=add(got,mul(Eout[i],tr[i]));
let X=pow(a,3),v=z;for(let i=P.length-1;i>=0;i--)v=add(mul(v,X),P[i]);let expected=neg(mul(gam,v));
return {a:a0,pass:eq(got,expected),got:got.map(String),expected:expected.map(String),polynomial:P.map(c=>c.map(String))};
}


function compute(p,ds,verbose=false){
const mod=x=>((x%p)+p)%p, add=(a,b)=>mod(a+b), sub=(a,b)=>mod(a-b), mul=(a,b)=>mod(a*b);
function pow(a,n){let r=1;while(n){if(n%2)r=mul(r,a);a=mul(a,a);n=Math.floor(n/2);}return r;} const inv=a=>pow(mod(a),p-2);
const gam=mul(5+ds,inv(2)), gb=mul(5-ds,inv(2)), r=mul(2-6*ds,inv(7)), rb=mul(2+6*ds,inv(7));
function trim(v){while(v.length>1&&v.at(-1)===0)v.pop();return v;}
function pa(a,b){let c=Array(Math.max(a.length,b.length)).fill(0);for(let i=0;i<c.length;i++)c[i]=add(a[i]||0,b[i]||0);return trim(c);}
function ps(a,b){let c=Array(Math.max(a.length,b.length)).fill(0);for(let i=0;i<c.length;i++)c[i]=sub(a[i]||0,b[i]||0);return trim(c);}
function pm(a,b){let c=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=add(c[i+j],mul(a[i],b[j]));return trim(c);}
const pc=(a,c)=>trim(a.map(x=>mul(x,c)));
function div(a,b){a=a.slice();let q=Array(Math.max(1,a.length-b.length+1)).fill(0), ib=inv(b.at(-1));while(a.length>=b.length&&!(a.length===1&&a[0]===0)){let k=a.length-b.length,v=mul(a.at(-1),ib);q[k]=v;for(let j=0;j<b.length;j++)a[j+k]=sub(a[j+k],mul(v,b[j]));trim(a);}return [trim(q),trim(a)];}
function ring(f){
const red=a=>div(a,f)[1], m=(a,b)=>red(pm(a,b));
function pw(a,n){let v=[1];while(n){if(n%2)v=m(v,a);a=m(a,a);n=Math.floor(n/2);}return v;}
function iv(a){let r0=f,r1=a,s0=[0],s1=[1];while(!(r1.length===1&&r1[0]===0)){let [q,r2]=div(r0,r1),s2=ps(s0,pm(q,s1));[r0,r1,s0,s1]=[r1,r2,s1,s2];}if(r0.length!==1)throw Error("notinvertible");return red(pc(s0,inv(r0[0])));}
return {m,pw,iv,red};
}
function fib(a){
const ga=mul(mul(gam,gam),a);const f=[mod(-mul(ga,mul(r,r))),mul(7*r+24,r),0,mul(2*ga,r),mod(28*r+12),0,mod(-ga),1];
const {m,pw,iv,red}=ring(f);let q=[mod(-r),0,0,1], qb=[mod(-rb),0,0,1];
let rat=m(qb,iv(q)), factor=pc(pw(rat,72),pow(mul(gb,inv(gam)),72));
let num=[mod((7*rb+24)*rb),0,0,mod(28*rb+12),0,0,1];
let xb=pc(m(m([0,1],num),pw(iv(qb),2)),inv(mul(gb,gb))), Xb=pw(xb,3);
let Qb=m(pa(Xb,[4]),pa(pa(ps(pw(Xb,3),pc(pw(Xb,2),96)),pc(Xb,48)),[64]));
let P=m(m(factor,Xb),Qb);const tr=[7];for(let k=1;k<=6;k++){let v=mul(k,f[7-k]);for(let j=1;j<k;j++)v=add(v,mul(f[7-j],tr[k-j]));tr[k]=mod(-v);}
const trace=a=>a.reduce((v,x,i)=>add(v,mul(x,tr[i])),0);let out=[];for(let j=0;j<=6;j++){out.push(trace(P));P=m(P,Xb);}return out;
}
function solve(A,b){let n=b.length,M=A.map((r,i)=>[...r,b[i]]);for(let j=0;j<n;j++){let k=j;while(k<n&&!M[k][j])k++;if(k===n)throw Error("singular");[M[j],M[k]]=[M[k],M[j]];let c=inv(M[j][j]);M[j]=M[j].map(x=>mul(x,c));for(let i=0;i<n;i++)if(i!==j){let t=M[i][j];M[i]=M[i].map((x,k)=>sub(x,mul(t,M[j][k])));}}return M.map(r=>r[n]);}
const sam=[],ev=[],rows=[];for(let a=1;sam.length<7;a++){const X=pow(a,3),Q=mul(X+4,mod(pow(X,3)-mul(96,pow(X,2))+48*X+64));if(X&&Q&&!sam.some(z=>pow(z,3)===X)){sam.push(a);ev.push(Array.from({length:7},(_,j)=>pow(X,j)));rows.push(fib(a).map(x=>mul(x,inv(mul(X,Q)))));}}
let columns=[];for(let j=0;j<7;j++)columns.push(solve(ev,rows.map(r=>r[j])));
const matrix=Array.from({length:7},(_,i)=>columns.map(c=>c[i]));
const candidateCheck=[];const checks=[];for(let a=8;checks.length<3;a++){let X=pow(a,3),Q=mul(X+4,mod(pow(X,3)-mul(96,pow(X,2))+48*X+64));if(!X||!Q)continue;let actual=fib(a);candidateCheck.push({a,actual,basis:Array.from({length:7},(_,j)=>mul(mul(X,Q),pow(X,j)))});checks.push(actual.every((z,j)=>z===mul(mul(X,Q),columns[j].reduce((v,c,i)=>add(v,mul(c,pow(X,i))),0))));}
function nullspace(A){let M=A.map(r=>r.slice()), piv=[], k=0;for(let j=0;j<7;j++){let i=k;while(i<7&&!M[i][j])i++;if(i===7)continue;[M[k],M[i]]=[M[i],M[k]];const iv=inv(M[k][j]);M[k]=M[k].map(x=>mul(x,iv));for(let i2=0;i2<7;i2++)if(i2!==k){let v=M[i2][j];M[i2]=M[i2].map((x,l)=>sub(x,mul(v,M[k][l])));}piv.push(j);k++;}let free=Array.from({length:7},(_,i)=>i).filter(i=>!piv.includes(i));return free.map(j=>{let v=Array(7).fill(0);v[j]=1;piv.forEach((c,i)=>v[c]=mod(-M[i][j]));return v;});}
const eig=[];for(let sign of [1,-1])for(let j=0;j<3;j++){let om=mul(ds-1,inv(2)),lambda=mul(sign*gam,pow(om,j)),ker=nullspace(matrix.map((r,i)=>r.map((v,k)=>sub(v,k===i?lambda:0))));if(ker.length)eig.push({sign,j,lambda,ker});}
return {p,ds,gam,gb,r,rb,matrix,checks,eig,candidateCheck,samples:sam};
}


const fibers=Array.from({length:13},(_,i)=>exactCM7(i+1));
if(!fibers.every(x=>x.pass))throw Error("Exact CM7 fiber failure");
const mf=compute(1009,260),p=1009,mod=x=>((x%p)+p)%p;
function mpow(a,n){let v=1;while(n){if(n%2)v=mod(v*a);a=mod(a*a);n=Math.floor(n/2);}return v;}
function det(M){M=M.map(r=>r.slice());let d=1;for(let j=0;j<M.length;j++){let i=j;while(i<M.length&&!M[i][j])i++;if(i===M.length)return 0;if(i!==j){[M[i],M[j]]=[M[j],M[i]];d=mod(-d);}const v=M[j][j],iv=mpow(v,p-2);d=mod(d*v);for(let k=j+1;k<M.length;k++){const q=mod(M[k][j]*iv);for(let l=j;l<M.length;l++)M[k][l]=mod(M[k][l]-q*M[j][l]);}}return d;}
const lambda=mod(-mf.gam),A=mf.matrix.map((r,i)=>r.map((v,j)=>mod(v-(i===j?lambda:0))));
const minor=det(A.slice(0,6).map(r=>r.slice(0,6)));
if(minor!==85)throw Error("Uniqueness minor failure");
const imul=(a,b)=>{let c=Array(a.length+b.length-1).fill(0);a.forEach((x,i)=>b.forEach((y,j)=>c[i+j]+=x*y));return c;};
const P6=imul(imul([16,-4,7],[1,1]),imul([-8,1],[-8,20,1]));
const expected=[1024,-1920,-1632,104,-1128,87,7];
if(JSON.stringify(P6)!==JSON.stringify(expected))throw Error("Original P6 factor failure");
const Q4=imul([4,1],[64,48,-96,1]);
if(JSON.stringify(Q4)!==JSON.stringify([256,256,-336,-92,1]))throw Error("Original Q4 factor failure");
if((-109)*(-2)*81+19*270*3*81/45!==56*270*3)throw Error("Third-torsion h5 reduction failure");
if(3024n**3n*(-72n)!==(-6048n)**3n*9n)throw Error("Actual scalar cube failure");
const report={
 scope:"Exact Q(sqrt(-3)) fibers and one exact finite reduction proving characteristic-zero uniqueness; no target-prime scan.",
 exact_fibers:fibers.map(({a,pass,got})=>({a,pass,trace:got})),
 uniqueness:{prime:1009,delta:260,lambda,matrix:A,minor_rows:[0,1,2,3,4,5],minor_columns:[0,1,2,3,4,5],minor},
 P6_ascending:expected,Q4_ascending:Q4,
 scalar:"a24 = -6048*b*real_cuberoot(9)",
 central_scope:"No deduction of infinitely many nonzero central derivatives."
};
console.log(JSON.stringify(report,null,2));
