#!/usr/bin/env node
// R549: exact Cartier/Verschiebung and same-source negative-moment checks.
// node check-r549-original-cartier-verschiebung-negative-moments.mjs
// Three existing finite rows cross-check the universal proof; no nonvanishing extrapolation.
const result=(()=>{
function calc(p){
 const mod=x=>(x%p+p)%p,pow=(a,n)=>{let r=1;for(a=mod(a);n;n=Math.floor(n/2),a=a*a%p)if(n%2)r=r*a%p;return r;},iv=a=>{if(mod(a)===0)throw Error("zero denominator");return pow(a,p-2);};
 const n=(p-1)/6-1,A=Array(n+1).fill(0),S=Array(n+1).fill(0),L=Array(n+1).fill(0),B=Array(n+1).fill(0);
 A[0]=S[0]=B[0]=1;if(n>=1)A[1]=mod(-iv(7));
 for(let k=2;k<=n;k++){let t=0;for(let j=1;j<k;j++)t=mod(t+A[j]*A[k-j]);A[k]=mod(t*iv((6*k+1)*(k-1)));}
 for(let k=1;k<=n;k++){L[k]=mod(-A[k]*iv(k*(6*k-1)));B[k]=mod(-(3*k-1)*A[k]);let t=0;for(let j=1;j<=k;j++)t=mod(t+j*L[j]*S[k-j]);S[k]=mod(t*iv(k));}
 const mul=(x,y)=>{const o=Array(n+1).fill(0);for(let i=0;i<=n;i++)for(let j=0;j<=n-i;j++)o[i+j]=mod(o[i+j]+x[i]*y[j]);return o;};
 const F4=mul(A,S),F1=mul(F4,B);
 return {p,n,c4:F4[n],c1:F1[n],ratio:F4[n]?mod(F1[n]*iv(F4[n])):null};
}

function modRing(p){
 const mod=x=>(x%p+p)%p,pow=(a,n)=>{let r=1;for(a=mod(a);n;n=Math.floor(n/2),a=a*a%p)if(n%2)r=r*a%p;return r};
 return {mod,pow,inv:a=>{if(mod(a)===0)throw Error("zero denominator");return pow(a,p-2);}};
}
function verifyPrime(p,b=17){
 const {mod,pow,inv}=modRing(p),s=(p-1)/6,r=s-1;
 if(!Number.isInteger(s)||p<=7||mod(b)===0)throw Error("input outside proved range");
 const ck=(name,ok)=>{if(!ok)throw Error(p+": "+name);checks.push(name)},checks=[];
 const mul=(A,B,n=r)=>{const R=Array(n+1).fill(0);for(let i=0;i<A.length&&i<=n;i++)for(let j=0;j<B.length&&i+j<=n;j++)R[i+j]=mod(R[i+j]+A[i]*B[j]);return R;};
 const pw=(A,e)=>{let R=[1];for(;e;e>>=1,A=mul(A,A))if(e&1)R=mul(R,A);return R};
 const C=Array(2*s).fill(0),Sq=Array(2*s).fill(0);C[0]=Sq[0]=1;
 for(let n=1;n<2*s;n++){C[n]=mod(-C[n-1]*(2*n-1)*inv(2*n));Sq[n]=mod(Sq[n-1]*(3-2*n)*inv(2*n));}
 const H0=C[s],Ha=mod(H0*pow(b,s));
 let cb=1;for(let j=1;j<=s;j++)cb=mod(cb*(2*s+j)*inv(j));
 ck("Hasse binomial C_s=binom(3s,s)",H0===cb&&H0!==0);
 const zeta=Array(s).fill(0);zeta[0]=mod(-inv(4*b));
 for(let j=1;j<s;j++)zeta[j]=mod(-(6*j+1)*zeta[j-1]*inv((6*j+4)*b));
 ck("D zeta_p=-x, first coefficient",mod(4*b*zeta[0])===p-1);
 for(let j=1;j<s;j++)ck("D zeta_p middle "+j,mod((6*j+1)*zeta[j-1]+(6*j+4)*b*zeta[j])===0);
 ck("D zeta_p last coefficient vanishes",mod((6*(s-1)+7)*zeta[s-1])===0);
 ck("absolute leading Laurent coefficient",mod(Ha*zeta[s-1])===1);
 const rev=Array.from({length:s},(_,k)=>mod(zeta[s-1-k]*pow(inv(b),k)));
 ck("reversed zeta polynomial = Hasse^-1 C_<s",rev.every((x,k)=>x===mod(inv(Ha)*C[k])));
 const aux=mul(rev,Sq,2*s-1);
 ck("AS at O constant",aux[0]===inv(Ha));
 for(let k=1;k<s;k++)ck("AS at O intermediate pole "+k,aux[k]===0);
 const H=Array(s).fill(0),Z=Array(s).fill(0);H[0]=Z[0]=1;
 for(let n=1;n<s;n++){H[n]=mod(C[n]*inv(6*n+1));Z[n]=mod(-C[n]*inv(6*n-1));}
 for(let n=0;n<s;n++)ck("AS regular jet "+n,aux[s+n]===mod(-pow(inv(b),s)*Z[n]));
 const Q=mul(Z,C),log=Array(s).fill(0),Sw=Array(s).fill(0);Sw[0]=1;
 let mid=H0,prod=1;
 for(let n=0;n<s;n++){
  if(n){mid=mod(mid*(2*s-n+1)*inv(s+n));prod=mod(-prod*(6*n-4)*inv(6*n-1));}
  ck("middle binomial/logarithmic coefficient "+n,Q[n]===mod(mid*inv(H0))&&Q[n]===prod);
  if(n){log[n]=mod(Q[n]*inv(n));let v=0;for(let j=1;j<=n;j++)v=mod(v+Q[j]*Sw[n-j]);Sw[n]=mod(v*inv(n));}
 }
 const c4=mul(mul(mul(H,H),C),Sw)[r],c1=mul(pw(H,5),Sw)[r];
 const o=calc(p);
 ck("original AS diagonal equals Cartier-Hermite formula",c4===o.c4);
 ck("original ABS diagonal equals Cartier-Hermite formula",c1===o.c1);
 let f=1;for(let j=1;j<=p-1;j++)f=f*j%p;ck("Wilson",(f+1)%p===0);
 const fact=n=>{let a=1;for(let j=1;j<=n;j++)a=a*j%p;return a};
 ck("(p-3)!=-1/2",fact(p-3)===mod(-inv(2)));
 ck("(p-6)!=1/120",fact(p-6)===inv(120));
 return {p,b,s,H0,Ha,zeta_coefficients:zeta,logarithmic_coefficients:Q,Sw_coefficients:Sw,
 c4,c1,normalized_I4:"-c4/(2*b*H0*Omega^2)",normalized_I1:"c1/(120*b*H0*Omega^5)",
 checks:checks.length,status:"PASS"};
}
const rows=[13,19,61].map(p=>verifyPrime(p));
const unipotent=[2,5].map(r=>({rank:r+1,connection:"D-N",restricted_derivation:"D^[p]=Ha*D",
 p_curvature:"Ha*N",p_curvature_rank:r,N_nilpotence:r+1,p_gt_rank:true}));
return {status:"PASS",scope:"Exact certificates for the universal identities proved in R549. Three existing primes only; no claim of nonvanishing from samples.",
rows,unipotent,first_layer_character:"the same xi of conductor (6) as R540",
curve:"y^2=x^3+17",polynomial_system:["6t H'+H=(1+t)^(-1/2)","6t(1+t)L''+(5+8t)L'+2=0","L=log(Sw)"],
all_prime_proof:"R549 sections 2-7; finite rows check implementation and the p=61 zero in the second observation."};

})();
console.log(JSON.stringify(result,null,2));
