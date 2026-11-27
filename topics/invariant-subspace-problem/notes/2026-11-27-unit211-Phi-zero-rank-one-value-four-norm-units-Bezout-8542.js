"use strict";
// New exact small input: the true residual mod32 versus the complete
// squarefree factor support of four QQ norm-zero image covers.
// QQ cover identities come from f66e913c..., actual run46003172567.
// This source supplies the NEW full modular Bezout needed to pay norm units.
const started=Date.now();
const p=1009;
const g=[722,278,731,355,485,40,431,879,886,775,986,900,350,67,972,697,900,306,248,789,718,976,181,674,177,210,486,428,438,486,520,1003,1];
const factors=[
 ["c_half_quadratic",[1,-2,3]],
 ["ell_image_head12",[9,-108,654,-2580,7329,-15720,26056,-33600,33456,-25088,13440,-4608,768]],
 ["lambda_half",[-1,2]],
 ["B3_quadratic",[1,-2,4]],
 ["B3_linear",[-1,1]],
 ["A2",[1,-2,2]],
 ["b_image_head12",[2,-24,147,-590,1719,-3816,6612,-9000,9528,-7616,4320,-1536,256]]
];
const mod=x=>((x%p)+p)%p;
const trim=a=>{while(a.length&&a[a.length-1]===0)a.pop();return a;};
const norm=a=>trim(a.map(mod));
const add=(a,b)=>{let c=Array(Math.max(a.length,b.length)).fill(0);for(let i=0;i<c.length;i++)c[i]=mod((a[i]||0)+(b[i]||0));return trim(c);};
const neg=a=>a.map(x=>mod(-x));
const sub=(a,b)=>add(a,neg(b));
const scale=(a,s)=>trim(a.map(x=>mod(x*s)));
const mul=(a,b)=>{if(!a.length||!b.length)return [];let c=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=mod(c[i+j]+a[i]*b[j]);return trim(c);};
const equal=(a,b)=>a.length===b.length&&a.every((x,i)=>x===b[i]);
function pow(a,n){let out=1;while(n){if(n&1)out=mod(out*a);a=mod(a*a);n=Math.floor(n/2);}return out;}
function divide(a,b){
 if(!b.length)throw Error("zero divisor polynomial");
 let r=a.slice(),q=Array(Math.max(0,a.length-b.length+1)).fill(0),inv=pow(b[b.length-1],p-2);
 if(mod(inv*b[b.length-1])!==1)throw Error("scalar inverse failure");
 while(r.length>=b.length){
  const d=r.length-b.length,c=mod(r[r.length-1]*inv);q[d]=c;
  for(let i=0;i<b.length;i++)r[d+i]=mod(r[d+i]-c*b[i]);
  trim(r);
 }
 q=trim(q);if(!equal(add(mul(q,b),r),a))throw Error("division return failure");
 return [q,r];
}
let z=[1];
for(const [,f]of factors)z=mul(z,norm(f));
if(g.length!==33||z.length!==33)throw Error("fixed degree mismatch");
let r0=norm(g),r1=z,s0=[1],s1=[],t0=[],t1=[1],steps=0;
while(r1.length){
 const [q,r]=divide(r0,r1);
 [r0,r1]=[r1,r];[s0,s1]=[s1,sub(s0,mul(q,s1))];[t0,t1]=[t1,sub(t0,mul(q,t1))];steps++;
 if(!equal(add(mul(s0,norm(g)),mul(t0,z)),r0))throw Error("Bezout stage return failure");
}
const lcInv=pow(r0[r0.length-1],p-2);
r0=scale(r0,lcInv);s0=scale(s0,lcInv);t0=scale(t0,lcInv);
if(!equal(r0,[1])||!equal(add(mul(s0,norm(g)),mul(t0,z)),[1]))throw Error("Bezout is not one");
return {
 schema:"isp-actual-four-norm-zero-cover-modular-Bezout-v1",
 prime:p,priorQQImageSourceSha256:"f66e913c9508536a4213b6164bd133a0404f048ad9fbb9b72114f686542c84a3",
 priorActualRun:46003172567,priorActualJob:140519731590,
 inputNames:["true_residual_g32","all_QQ_norm_image_factor_support_Z32"],
 inputDegrees:[32,32],factorCoefficientsAscending:factors,
 gCoefficientsAscending:norm(g),zCoefficientsAscending:z,
 BezoutTagCoefficientsAscending:[s0,t0],BezoutTagDegrees:[s0.length-1,t0.length-1],
 gcd:[1],allScalarInversesMultipliedBack:true,
 allPolynomialDivisionsMultipliedBack:true,allBezoutStagesMultipliedBack:true,
 completeFinalProductEqualsOne:true,euclidSteps:steps,
 actualElapsedMilliseconds:Date.now()-started,
 newPaidOriginalNorms:["Norm(ell)","Norm(u)","Norm(u-ell)","Norm(b)"],
 QQInferenceRequiresPriorMonic1069AndOriginalImageIdentities:true,
 claimEntirePhiFaceExcluded:false,ordinaryISPClaim:false
};
