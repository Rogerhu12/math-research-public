"use strict";
async function integerRightKernel(A,report){
 const abs=a=>a<0n?-a:a,gcd=(a,b)=>{a=abs(a);b=abs(b);while(b){const c=a%b;a=b;b=c;}return a;};
 const B=A.map(r=>r.map(BigInt)),n=B.length,m=B[0].length,piv=[];let r=0,last=Date.now(),maxDigits=0;
 const primitive=(row,c)=>{let g=0n;for(let j=c;j<m;j++)if(row[j]){g=gcd(g,row[j]);if(g===1n)break;}if(g>1n)for(let j=c;j<m;j++)row[j]/=g;let j=c;while(j<m&&!row[j])j++;if(j<m&&row[j]<0n)for(;j<m;j++)row[j]=-row[j];};
 for(const row of B)primitive(row,0);
 for(let c=0;c<m&&r<n;c++){
  let k=-1,best=Infinity;for(let i=r;i<n;i++)if(B[i][c]){const d=abs(B[i][c]).toString().length;if(d<best){best=d;k=i;}}
  if(k<0)continue;[B[k],B[r]]=[B[r],B[k]];const q=B[r],pv=q[c];
  for(let i=r+1;i<n;i++)if(B[i][c]){const f=B[i][c],g=gcd(pv,f),aa=pv/g,bb=f/g,row=B[i];row[c]=0n;for(let j=c+1;j<m;j++)row[j]=aa*row[j]-bb*q[j];primitive(row,c+1);}
  piv.push(c);r++;
  maxDigits=Math.max(maxDigits,...q.map(x=>abs(x).toString().length));
  if(report&&Date.now()-last>10000){await report({stage:"echelon",pivot:r,column:c,maxDigits});last=Date.now();}
 }
 const free=Array.from({length:m},(_,i)=>i).filter(i=>!piv.includes(i));
 const kernels=[];
 for(const f of free){
  let nums=Array(m).fill(0n),den=1n;nums[f]=1n;
  for(let i=r-1;i>=0;i--){
   const c=piv[i],q=B[i];let sum=0n;for(let j=c+1;j<m;j++)sum+=q[j]*nums[j];const g=gcd(sum,q[c]),aa=q[c]/g,bb=-sum/g;
   if(aa!==1n){for(let j=0;j<m;j++)nums[j]*=aa;den*=aa;}
   nums[c]=bb;
   let gg=den;for(const v of nums){gg=gcd(gg,v);if(gg===1n)break;}if(gg>1n){den/=gg;nums=nums.map(v=>v/gg);}
  }
  let g=0n;for(const v of nums)g=gcd(g,v);if(g)nums=nums.map(v=>v/g);if(nums[f]<0n)nums=nums.map(v=>-v);
  for(const row of A){let s=0n;for(let j=0;j<m;j++)s+=BigInt(row[j])*nums[j];if(s)throw new Error("Exact kernel substitution failed");}
  kernels.push(nums.map(String));
  if(report&&Date.now()-last>10000){await report({stage:"kernel",done:kernels.length,total:free.length});last=Date.now();}
 }
 return {rows:n,columns:m,rank:r,pivots:piv,free,kernels,maxEchelonDigits:maxDigits};
}
if(typeof module!=="undefined")module.exports={integerRightKernel};
