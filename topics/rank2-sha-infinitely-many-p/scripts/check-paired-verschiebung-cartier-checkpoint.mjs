#!/usr/bin/env node
// Exact check of the paired Verschiebung checkpoint. No dependencies.
const certificate=(function(){

const ring=(function(){
function ring(p,b=1){
 const mod=a=>(a%p+p)%p,pow=(a,n)=>{let r=1;for(a=mod(a);n;n=Math.floor(n/2),a=a*a%p)if(n&1)r=r*a%p;return r},iv=a=>pow(a,p-2);
 const trim=a=>{while(a.length>1&&!a[a.length-1])a.pop();return a},
 add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>mod((a[i]||0)+(b[i]||0)))),
 sc=(a,c)=>trim(a.map(v=>mod(v*c))),neg=a=>sc(a,-1),sub=(a,b)=>add(a,neg(b)),
 mul=(a,b)=>{let r=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)if(a[i])for(let j=0;j<b.length;j++)if(b[j])r[i+j]=mod(r[i+j]+a[i]*b[j]);return trim(r)},
 pp=(a,n)=>{let r=[1];for(;n;n=Math.floor(n/2),a=mul(a,a))if(n&1)r=mul(r,a);return r},
 der=a=>trim(a.slice(1).map((v,i)=>mod(v*(i+1)))),xp=n=>{let a=Array(n+1).fill(0);a[n]=1;return a};
 const X=xp(1),Y=add(xp(3),[b]),Y2=mul(Y,Y);
 const memo={0:[0],1:[1],2:[1],3:add(sc(xp(4),3),sc(X,12*b)),4:add(add(sc(xp(6),2),sc(xp(3),40*b)),[-16*b*b])};
 const psi=n=>{if(memo[n])return memo[n];const m=Math.floor(n/2);let r;
 if(n&1){let a=mul(psi(m+2),pp(psi(m),3)),c=mul(psi(m-1),pp(psi(m+1),3));r=(m&1)?sub(a,sc(mul(Y2,c),16)):sub(sc(mul(Y2,a),16),c)}
 else r=mul(psi(m),sub(mul(psi(m+2),pp(psi(m-1),2)),mul(psi(m-2),pp(psi(m+1),2))));
 return memo[n]=r};
 const rootP=a=>{let r=Array(Math.floor((a.length-1)/p)+1).fill(0);a.forEach((v,i)=>{if(v&&i%p)throw Error("not p power at "+i);if(i%p===0)r[i/p]=v});return trim(r)};
 const r=rootP(psi(p)),N=rootP(sub(mul(X,pp(psi(p),2)),sc(mul(Y,mul(psi(p-1),psi(p+1))),4)));
 const Ha=r[r.length-1],M=sc(sub(mul(der(N),r),sc(mul(N,der(r)),2)),iv(Ha));
 const q4=mul(pp(r,4),N),q1=neg(mul(mul(r,N),M));
 const D=(f,odd)=>odd?add(sc(mul(xp(2),f),3),sc(mul(Y,der(f)),2)):sc(der(f),2);
 const Dn=(f,odd,n)=>{for(let j=0;j<n;j++){f=D(f,odd);odd=!odd}return {f,odd}};
 const R4=Dn(q4,false,p-3).f,R1=Dn(q1,true,p-6).f;
 const E4=sub(Dn(R4,false,2).f,sc(q4,Ha)),E1=sub(Dn(R1,false,5).f,sc(q1,Ha));
 return {p,b,mod,pow,iv,add,sub,sc,mul,pp,der,xp,Y,psi,r,N,M,Ha,q4,q1,R4,R1,E4,E1,Dn};
}
return ring;
})();
const calc=(function(){function calc(p){
 const mod=x=>(x%p+p)%p,pow=(a,n)=>{let r=1;for(a=mod(a);n;n=Math.floor(n/2),a=a*a%p)if(n%2)r=r*a%p;return r;},iv=a=>{if(mod(a)===0)throw Error("zero denominator");return pow(a,p-2);};
 const n=(p-1)/6-1,A=Array(n+1).fill(0),S=Array(n+1).fill(0),L=Array(n+1).fill(0),B=Array(n+1).fill(0);
 A[0]=S[0]=B[0]=1;if(n>=1)A[1]=mod(-iv(7));
 for(let k=2;k<=n;k++){let t=0;for(let j=1;j<k;j++)t=mod(t+A[j]*A[k-j]);A[k]=mod(t*iv((6*k+1)*(k-1)));}
 for(let k=1;k<=n;k++){L[k]=mod(-A[k]*iv(k*(6*k-1)));B[k]=mod(-(3*k-1)*A[k]);let t=0;for(let j=1;j<=k;j++)t=mod(t+j*L[j]*S[k-j]);S[k]=mod(t*iv(k));}
 const mul=(x,y)=>{const o=Array(n+1).fill(0);for(let i=0;i<=n;i++)for(let j=0;j<=n-i;j++)o[i+j]=mod(o[i+j]+x[i]*y[j]);return o;};
 const F4=mul(A,S),F1=mul(F4,B);
 return {p,n,c4:F4[n],c1:F1[n],ratio:F4[n]?mod(F1[n]*iv(F4[n])):null};
}
;return calc})();
function checkPrime(p){
 const a=ring(p),{mod,pow,iv,sc,sub,add,mul,pp,xp,Y,Ha:h,r,N,M,q4,q1,R4,R1,E4,E1,Dn}=a;
 const checks=[];const eq=(A,B)=>{for(let i=0;i<Math.max(A.length,B.length);i++)if(mod((A[i]||0)-(B[i]||0)))return false;return true};
 const ck=(name,v)=>{if(!v)throw Error(p+": "+name);checks.push(name)};
 const xi=pow(2,2*(p-1)/3),s=(p-1)/6,low=calc(p);
 ck("r constant is the full inverse cubic-2 character",r[0]===xi);
 ck("V curve equation",eq(add(pp(N,3),pp(r,6)),mul(Y,pp(M,2))));
 ck("q4 unique pole 6p-4",q4.length-1===3*p-2);
 ck("q1 unique pole 6p-1",q1.length-1===3*p-2);
 ck("complete first Frobenius remainder",eq(E4,sc(xp(p),-xi)));
 ck("complete second Frobenius remainder",eq(E1,sc(mul(xp(p),pp(Y,(p-1)/2)),xi)));
 for(const [label,R]of[["R4",R4],["R1",R1]]){
  ck(label+" complete D^(p-1) eigen-normalization",eq(Dn(R,false,p-1).f,sc(R,h)));
  ck(label+" whole mu6 type zero",R.every((v,i)=>!v||i%3===0));
  const C=mul(R,pp(Y,3*s));
  ck(label+" bottom Cartier component",(C[p-1]||0)===0);
  ck(label+" top Cartier component",(C[4*p-1]||0)===0);
 }
 ck("R4 target is original c4", (R4[3*p]||0)===mod(-low.c4*iv(2*pow(h,2))));
 ck("R1 target is original c1", (R1[3*p]||0)===mod(low.c1*iv(120*pow(h,5))));
 ck("R4 forced unit next coefficient",R4[3*p-3]===mod(pow(h,5)*iv(30)));
 ck("R1 forced unit next coefficient",R1[3*p-3]===mod(pow(h,2)*iv(720)));
 const Z=sub(R4,sc(R1,24*pow(h,3)));
 ck("same-source six-jet exact cancellation",(Z[3*p-3]||0)===0);
 ck("same-source twelve-jet forced unit",Z[3*p-6]===mod(-pow(h,11)*iv(1100)));
 const dr=Dn(r,false,1).f,dq=Dn(q4,false,1).f;
 const nonlin=add(sub(mul(mul(r,q4),dq),sc(mul(dr,pp(q4,2)),6)),sc(mul(pp(r,7),q1),2*h));
 ck("whole nonlinear identity with actual differential h",eq(nonlin,[0]));
 const sp=f=>f.map((v,i)=>[i,v]).filter(([i,v])=>v);
 return {p,h,xi,c4:low.c4,c1:low.c1,r:sp(r),N:sp(N),M:sp(M),R4:sp(R4),R1:sp(R1),
 highest:[R4[3*p]||0,R1[3*p]||0],next:[R4[3*p-3],R1[3*p-3]],Z_next2:Z[3*p-6],
 checks:checks.length,status:"PASS"};
}
return {status:"PASS",scope:"Complete polynomial identities and normalization; three existing primes, no nonvanishing theorem inferred from samples.",
 rows:[13,19,61].map(checkPrime),
 unresolved:"Whether the two highest coefficients can simultaneously vanish for infinitely many allowed primes.",
 known_nonzero:"The common-source twelve-jet is -h^11/1100 for p>11."};

})();
console.log(JSON.stringify(certificate,null,2));
