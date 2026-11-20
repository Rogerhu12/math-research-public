// Author: Astra-ISP-b2a9acde-20261120 / root; AI-assisted GPT-6 Astra Pro.
// Exact BigInt source; arrays stay in memory. Run with node on this file.
function verifyPolarCubeCorrection() {
  const trim=a=>{a=a.slice();while(a.length>1&&a[a.length-1]===0n)a.pop();return a;};
  const add=(a,b)=>{const z=Array(Math.max(a.length,b.length)).fill(0n);a.forEach((v,i)=>z[i]+=v);b.forEach((v,i)=>z[i]+=v);return trim(z);};
  const scale=(a,c)=>trim(a.map(v=>v*c));
  const mul=(a,b)=>{const z=Array(a.length+b.length-1).fill(0n);a.forEach((v,i)=>b.forEach((w,j)=>z[i+j]+=v*w));return trim(z);};
  const pow=(a,k)=>{let z=[1n];for(let i=0;i<k;i++)z=mul(z,a);return z;};
  const value=(a,t)=>a.reduceRight((v,c)=>v*t+c,0n);
  function sylvester(a,b) {
    const m=a.length-1,n=b.length-1,N=m+n;
    const z=Array.from({length:N},()=>Array(N).fill(0n));
    const aa=a.slice().reverse(),bb=b.slice().reverse();
    for(let i=0;i<n;i++)for(let j=0;j<=m;j++)z[i][i+j]=aa[j];
    for(let i=0;i<m;i++)for(let j=0;j<=n;j++)z[n+i][i+j]=bb[j];
    return z;
  }
  function bareiss(a) {
    a=a.map(row=>row.slice());let sign=1n,previous=1n,divisions=0;
    for(let k=0;k<a.length-1;k++) {
      let pivotRow=k;while(pivotRow<a.length&&a[pivotRow][k]===0n)pivotRow++;
      if(pivotRow===a.length)return {determinant:0n,divisions};
      if(pivotRow!==k){[a[k],a[pivotRow]]=[a[pivotRow],a[k]];sign=-sign;}
      const pivot=a[k][k];
      for(let i=k+1;i<a.length;i++)for(let j=k+1;j<a.length;j++) {
        const numerator=a[i][j]*pivot-a[i][k]*a[k][j];
        if(numerator%previous!==0n)throw Error("Nonintegral Bareiss division");
        a[i][j]=numerator/previous;divisions++;
      }
      for(let i=k+1;i<a.length;i++)a[i][k]=0n;
      previous=pivot;
    }
    return {determinant:sign*a.at(-1).at(-1),divisions};
  }
  const A=[1n,1n],B=[-5n,-3n,-3n],C=[0n,22n,-3n,1n],D=[0n,0n,-5n,1n];
  const P=add(pow(B,2),scale(mul(A,C),-3n));
  const Q=add(pow(B,3),scale(mul(pow(A,2),D),-27n));
  if(P.toString()!=="25,-36,-18,24,6")throw Error("Original P");
  if(Q.toString()!=="-125,-225,-225,-54,-135,-108,-27")throw Error("Correct original Q");
  const matrix=sylvester(P,Q);
  if(matrix.length!==10||matrix.some(row=>row.length!==10))throw Error("Full Sylvester dimensions");
  const result=bareiss(matrix);
  if(result.determinant!==260758295153015625n)throw Error("Correct full integer resultant");
  if((result.determinant%103n+103n)%103n!==56n)throw Error("Resultant residue control");
  if(value(A,-1n)!==0n||value(B,-1n)!==-5n)throw Error("Finite leading-zero exception");
  return {allPassed:true,sourceScope:"Correct pure-cube necessary condition only; other closed geometry is not rerun",
    sylvesterDimension:10,exactIntegerDivisions:result.divisions,
    resultant:result.determinant.toString(),resultantMod103:56,
    finiteLeadingZeroExceptionChecked:true,
    infinityBinaryFiber:"X^2(X+Y), two distinct roots",
    characteristicZeroNoPureCubeVerified:true};
}
if (typeof module !== 'undefined' && require.main === module) console.log(JSON.stringify(verifyPolarCubeCorrection()));
