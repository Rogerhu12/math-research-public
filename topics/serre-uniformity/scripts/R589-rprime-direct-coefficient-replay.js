"use strict";
/* Reconstructed exact coefficient recipe for R589. This NEW wrapper was not
   executed during recovery. Historical records are in the accompanying JSON.
   It is not a recovered copy of a lost executable and does not claim a rerun. */
function rprimeDirect(p) {
  if(!Number.isInteger(p)||p<41||p>383||p%6!==5) throw Error("41<=p<=383, p=5 mod6 required");
  for(let d=2;d*d<=p;d++)if(p%d===0)throw Error("p must be prime");
  const mod=x=>((x%p)+p)%p;
  const pow=(a,n)=>{let r=1;while(n){if(n%2)r=mod(r*a);n=Math.floor(n/2);if(n)a=mod(a*a);}return r;};
  const inv=a=>{a=mod(a);if(!a)throw Error("nonunit");return pow(a,p-2);};
  const n=(p-1)**2,M=(n-4)/6,P=BigInt(p),z=new Array(M+1);
  let binom=1n,pow4=1,cancellations=0;
  for(let k=0;k<=M;k++){
    let num=binom,den=BigInt(6*k+1);
    while(den%P===0n){if(num%P!==0n)throw Error("nonintegral log coefficient");den/=P;num/=P;cancellations++;}
    z[k]=mod(Number(num%P)*inv(Number(den%P))*pow4);
    binom=binom*BigInt(2*(2*k+1))/BigInt(k+1);pow4=mod(pow4*inv(4));
  }
  const a=new Array(M+1),q=new Array(M+1);let maxDot=0;
  for(let k=0;k<=M;k++){
    const top=k===0?7:k===1?4:k===2?16:0;
    a[k]=mod(top+228*(a[k-1]||0)-48*(a[k-2]||0)+64*(a[k-3]||0));
    let dot=0;for(let i=1;i<=k;i++)dot+=z[i]*q[k-i];
    if(dot>=2**53)throw Error("integer precision bound");maxDot=Math.max(maxDot,dot);
    q[k]=mod((4+6*k)*a[k]-dot);
  }
  const cap=Math.floor(M/p),zp2=new Array(cap+1).fill(0),summands=[];
  for(let i=0;i<=cap;i++)for(let j=0;i+j<=cap;j++)zp2[i+j]=mod(zp2[i+j]+z[i]*z[j]);
  for(let j=0;j<=cap;j++)summands.push(mod(zp2[j]*q[M-p*j]));
  const raw=mod(summands.reduce((a,b)=>a+b,0));
  return{p,n,M,n_modp:mod(n),rprime:mod(raw*inv(n)),raw_sum_modp:raw,summands,
    cancelled_log_denominator_p_factors:cancellations,largest_integer_dot:maxDot,
    method:"exact BigInt binomial; direct Q*Z=F; sparse Z(w^p)^2 convolution"};
}
module.exports={rprimeDirect};
if(require.main===module)process.stdout.write(JSON.stringify(rprimeDirect(Number(process.argv[2]||269)),null,2)+"\n");
