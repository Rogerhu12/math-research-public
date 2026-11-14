"use strict";
/*
  R595 direct r3 coefficient replay, reconstructed after environment loss.
  This is a new readable implementation of the recorded exact algorithm,
  not a claim to recover the old source bytes. It has NOT been executed
  during recovery. The historical p269 certificate was preserved separately.
*/
function r3Direct(p) {
  if (!Number.isInteger(p) || p < 41 || p > 269 || p % 6 !== 5)
    throw Error("This exact Number-dot implementation is bounded to 41<=p<=269,p=5 mod6.");
  for (let d=2;d*d<=p;d++) if(p%d===0) throw Error("p must be prime");
  const mod=x=>((x%p)+p)%p;
  const power=(a,n)=>{let r=1;while(n){if(n%2)r=mod(r*a);n=Math.floor(n/2);if(n)a=mod(a*a);}return r;};
  const inv=a=>{a=mod(a);if(!a)throw Error("nonunit");return power(a,p-2);};
  const n=(p-1)*(p-3),M=(n-2)/6,P=BigInt(p),z=new Array(M+1),inv4=inv(4);
  let binom=1n,pow4=1;
  for(let k=0;k<=M;k++){
    let num=binom,den=BigInt(6*k+1);
    while(den%P===0n){if(num%P!==0n)throw Error("nonintegral log coefficient");den/=P;num/=P;}
    z[k]=mod(Number(num%P)*inv(Number(den%P))*pow4);
    binom=binom*BigInt(2*(2*k+1))/BigInt(k+1);
    pow4=mod(pow4*inv4);
  }
  const A=new Array(M+1).fill(0),F=new Array(M+1);
  for(let k=0;k<=M;k++){
    const numerator=k===0?1:k===1?34:k===2?-8:0;
    A[k]=mod(numerator+228*(A[k-1]||0)-48*(A[k-2]||0)+64*(A[k-3]||0));
    F[k]=mod((2+6*k)*A[k]);
  }
  let maxDot=0,Q=F;
  for(let stage=0;stage<3;stage++){
    const out=new Array(M+1);
    for(let k=0;k<=M;k++){
      let sum=0;for(let i=1;i<=k;i++)sum+=z[i]*out[k-i];
      if(sum>=2**53)throw Error("integer precision bound");
      maxDot=Math.max(maxDot,sum);out[k]=mod(Q[k]-sum);
    }
    Q=out;
  }
  const cap=Math.floor(M/p),short=z.slice(0,cap+1);
  const product=(a,b)=>{const c=new Array(cap+1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length&&i+j<=cap;j++)c[i+j]=mod(c[i+j]+a[i]*b[j]);return c;};
  const z2=product(short,short),z4=product(z2,z2),summands=[];
  for(let j=0;j<=cap;j++)summands.push(mod(z4[j]*Q[M-p*j]));
  const raw=mod(summands.reduce((a,b)=>a+b,0));
  return {p,n,M,n_modp:mod(n),raw_sum_modp:raw,result:mod(raw*inv(n)),summands,largest_integer_dot:maxDot};
}
module.exports={r3Direct};
if(require.main===module)process.stdout.write(JSON.stringify(r3Direct(Number(process.argv[2]||269)),null,2)+"\n");
