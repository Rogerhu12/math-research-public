#!/usr/bin/env node
// R661: complete odd-five finite types and the original logarithmic rows.
// Run: node check-r661-odd-five-all-types-and-original-log-rows.mjs
// Exact rational cyclotomic arithmetic; no packages, network, or L-value samples.
const result=(()=>{

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

const cert={status:"PASS",checks:[],profiles:[]};
const ck=(n,v)=>{if(!v)throw Error(n);cert.checks.push(n)};
const B=field(15,[1,-1,0,1,-1,1,0,-1,1]),om=B.z(5),r6=B.add(B.C(1),om);
const rt5=B.add(B.C(1),B.sc(B.add(B.z(3),B.z(-3)),2));
const mv=(M,v)=>M.map(row=>row.map((x,j)=>B.mul(x,v[j])).reduce(B.add,B.C(0)));
const mm=(M,N)=>M.map(row=>N[0].map((_,j)=>row.map((x,k)=>B.mul(x,N[k][j])).reduce(B.add,B.C(0))));
const roots6=Array.from({length:6},(_,i)=>fpower([1,1],i,5));
const labels={1:["Sigma5",5,"E80"],2:["D5",0,"E10000"],3:["Z5",1,"E80"],4:["-y*sigma5",2,"E10000"],5:["x*sigma5",3,"E80"]};
function chi2(n){const a=mod(n,8);return a===1||a===3?1:a===5||a===7?-1:0}
for(let r=1;r<=5;r++){
 const M=Array.from({length:5},(_,a)=>Array.from({length:5},(_,b)=>B.sc(B.mul(B.pow(om,r),B.mul(rt5,B.z(-6*(a*a+4*a*b+b*b)))),1,5)));
 const M2=mm(M,M),M3=mm(M2,M);
 ck("M cube I r="+r,M3.every((row,a)=>row.every((x,b)=>B.eq(x,B.C(a===b?1:0)))));
 ck("M unitary r="+r,mm(M,M[0].map((_,j)=>M.map(row=>B.conj(row[j])))).every((row,a)=>row.every((x,b)=>B.eq(x,B.C(a===b?1:0)))));
 const seed=Array.from({length:5},(_,i)=>B.C(r%2?(i===0?1:0):(i===1?1:i===4?-1:0)));
 const Mseed=mv(M,seed),M2seed=mv(M2,seed);
 const v=seed.map((x,i)=>B.sc(B.add(B.add(x,Mseed[i]),M2seed[i]),1,3));
 const norm=v.map(x=>B.mul(x,B.conj(x))).reduce(B.add,B.C(0));
 ck("invariant r="+r,mv(M,v).every((x,i)=>B.eq(x,v[i])));
 ck("real r="+r,v.every(x=>B.eq(x,B.conj(x))));
 ck("parity r="+r,v.every((x,i)=>B.eq(x,B.sc(v[mod(-i,5)],r%2?1:-1))));
 ck("nonzero r="+r,!B.eq(norm,B.C(0)));
 const ev=v.map((x,i)=>B.mul(x,seed[i])).reduce(B.add,B.C(0));
 ck("projection norm r="+r,B.eq(norm,ev));
 let Gauss=B.C(0);
 for(let a=0;a<5;a++)for(let b=0;b<5;b++)if(a||b){
   const e=roots6.findIndex(x=>fe(x,fpower([a,b],4,5))),tr=mod(2*a-b,5);
   Gauss=B.add(Gauss,B.mul(B.pow(r6,mod(r*e,6)),B.z(-3*tr)));
 }
 ck("full F25 Gauss r="+r,B.eq(Gauss,B.C(r%2?-5:5)));
 const an=n=>B.sc(v[mod(n,5)],chi2(n));
 for(let n=0;n<40;n++){
  ck("period r,n="+r+","+n,B.eq(an(n+20),B.neg(an(n))));
  ck("parity Fourier r,n="+r+","+n,B.eq(an(-n),B.sc(an(n),r%2?-1:1)));
  if(n%2)ck("shift r,n="+r+","+n,B.eq(an(n+10),B.sc(an(n),mod((n-1)/2,2)?-1:1)));
 }
 const j=labels[r][1];
 ck("dyadic unit cancellation r="+r,mod(r+2*j+1,3)===0);
 ck("triadic full uniformizer r="+r,mod(r+j,2)===0);
 ck("true CM angle r="+r,mod(j+2-r,6)===0);
 cert.profiles.push({r,source:labels[r][0],angle:j,curve:labels[r][2],matrix:M.map(row=>row.map(B.json)),vector:v.map(B.json),norm:B.json(norm),gauss:B.json(Gauss)});
}
const Leg=x=>mod(x,5)===0?0:[1,4].includes(mod(x,5))?1:-1;
for(let a=0;a<5;a++)for(let b=0;b<5;b++)if(a||b){
 const e=roots6.findIndex(x=>fe(x,fpower([a,b],4,5)));
 ck("chi cubed is quadratic5 "+a+","+b,(e%2?-1:1)===Leg(a*a-a*b+b*b));
}
const Nz=cert.profiles.find(x=>x.r===3).norm;
ck("Z norm exact formula",B.eq(Nz.map(x=>{const t=x.split("/");return q(t[0],t[1]??1)}),B.sc(B.add(B.C(1),B.sc(rt5,2,5)),1,3)));
cert.actual_rows={
D:{source:"-x*y*sigma_17^5",character:"chi^2 psi0^(m+1) barpsi0^(-m), m=(p-1)u",curve:"y^2+y=x^3+156 (E10000)",mass:"1-beta",period_factor:"c_D theta Omega_p",log_identity:"2 ell_D/(1-beta)=L_D'(0)/((p-1)L_D(0))+log<5>"},
Z:{source:"x^2*sigma_17^5",character:"chi^3 psi0^(m+1) barpsi0^(-m), m=1+(p-1)u",curve:"E80, positive angular weight3",moment1:"Omega_p(1-beta*kappa)",period_factor:"c_Z theta^3 Omega_p/5",log_identity:"2 ell_Z,1/[Omega_p(1-beta*kappa)]=L_Z'(0)/((p-1)L_Z(0))+log<5>"}};
cert.check_count=cert.checks.length;
cert.checks=cert.checks.filter(x=>!/^period |^parity Fourier |^shift |^chi cubed/.test(x));
return cert;

})();
console.log(JSON.stringify(result,null,2));
