"use strict";
// Exact finite scalar certificate; no external packages or floating-point decisions.
function exactCertificate() {
  const K = [
    [0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
    [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]
  ].map(r=>r.map(BigInt));
  const zmat=(n,m)=>Array.from({length:n},()=>Array(m).fill(0n));
  const J=zmat(11,11);
  for(let i=0;i<6;i++)for(let j=0;j<6;j++)
  for(let p=0;p<6;p++)for(let q=0;q<6;q++)
    J[i+p][j+q]+=K[i][j]*K[p][q];
  // Independent trace construction of the same Hankel Hessian.
  for(let m=0;m<11;m++)for(let n=0;n<11;n++){
    let t=0n;
    for(let i=0;i<6;i++)for(let j=0;j<6;j++)
    for(let p=0;p<6;p++)for(let q=0;q<6;q++)
      if(j+p===m && q+i===n)t+=K[i][j]*K[p][q];
    if(t!==J[m][n])throw Error("trace/convolution mismatch");
  }
  function bareiss(M){
    const A=M.map(r=>r.slice()),pivots=[],swaps=[];
    let old=1n,sign=1n;
    for(let k=0;k<A.length-1;k++){
      let p=k;while(p<A.length && !A[p][k])p++;
      if(p===A.length)return{det:0n,pivots,swaps};
      if(p!==k){[A[p],A[k]]=[A[k],A[p]];sign=-sign;swaps.push([k,p]);}
      const v=A[k][k];pivots.push(v);
      for(let i=k+1;i<A.length;i++){
        for(let j=k+1;j<A.length;j++){
          const numerator=v*A[i][j]-A[i][k]*A[k][j];
          if(numerator%old)throw Error("nonintegral Bareiss division");
          A[i][j]=numerator/old;
        }
        A[i][k]=0n;
      }
      old=v;
    }
    return{det:sign*A.at(-1).at(-1),pivots,swaps};
  }
  const abs=x=>x<0n?-x:x;
  function gcd(a,b){a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a;}
  function rat(a,b=1n){
    if(!b)throw Error("zero denominator");
    if(b<0n){a=-a;b=-b;}if(!a)return[0n,1n];
    const g=gcd(a,b);return[a/g,b/g];
  }
  const add=(x,y)=>rat(x[0]*y[1]+y[0]*x[1],x[1]*y[1]);
  const mul=(x,y)=>rat(x[0]*y[0],x[1]*y[1]);
  const neg=x=>[-x[0],x[1]];
  const div=(x,y)=>rat(x[0]*y[1],x[1]*y[0]);
  const A=J.map((r,i)=>[...r.map(x=>rat(x)),...r.map((_,j)=>rat(i===j?1n:0n))]);
  for(let k=0;k<11;k++){
    let p=k;while(p<11 && !A[p][k][0])p++;
    if(p===11)throw Error("singular J");
    [A[p],A[k]]=[A[k],A[p]];
    const pivot=A[k][k];A[k]=A[k].map(x=>div(x,pivot));
    for(let i=0;i<11;i++)if(i!==k && A[i][k][0]){
      const c=A[i][k];A[i]=A[i].map((x,j)=>add(x,neg(mul(c,A[k][j]))));
    }
  }
  const Ji=A.map(r=>r.slice(11));
  for(let i=0;i<11;i++)for(let j=0;j<11;j++){
    let s=rat(0n);for(let k=0;k<11;k++)s=add(s,mul(rat(J[i][k]),Ji[k][j]));
    if(s[0]!==BigInt(i===j)||s[1]!==1n)throw Error("inverse check failed");
  }
  const e2=[];
  for(let i=0;i<6;i++)for(let j=i;j<6;j++){
    const e=Array(6).fill(0);e[i]++;e[j]++;e2.push(e);
  }
  const indices=e=>e.flatMap((v,i)=>Array(v).fill(i));
  const Fc=e2.map(e=>{const[i,j]=indices(e);return rat(K[i][j],i===j?2n:1n);});
  const B=Array.from({length:11},()=>e2.map(()=>rat(0n)));
  for(let m=0;m<11;m++)for(let t=0;t<21;t++){
    const[i,j]=indices(e2[t]);let c=0n;
    for(let a=0;a<6;a++)for(let b=0;b<6;b++)
      if(a+b===m)c+=K[a][i]*K[b][j]*(i===j?1n:2n);
    B[m][t]=rat(c);
  }
  const T=Ji.map(row=>e2.map((_,t)=>row.reduce((s,x,n)=>add(s,mul(x,B[n][t])),rat(0n))));
  const R=new Map();
  for(let a=0;a<21;a++)for(let b=0;b<21;b++){
    let c=mul(Fc[a],Fc[b]),s=rat(0n);
    for(let m=0;m<11;m++)s=add(s,mul(B[m][a],T[m][b]));
    c=add(c,neg(mul(rat(1n,2n),s)));
    const e=e2[a].map((v,i)=>v+e2[b][i]).join(",");
    R.set(e,add(R.get(e)||rat(0n),c));
  }
  const terms=[...R].filter(([e,c])=>c[0]).map(([e,c])=>({exponents:e.split(",").map(Number),coefficient:c}));
  const value=new Map(),gradient=Array.from({length:6},()=>new Map());
  for(const{exponents:e,coefficient:c}of terms){
    const p=e.reduce((s,v,i)=>s+v*i,0);
    value.set(p,add(value.get(p)||rat(0n),c));
    for(let i=0;i<6;i++)if(e[i]){
      const k=p-i,v=mul(c,rat(BigInt(e[i])));
      gradient[i].set(k,add(gradient[i].get(k)||rat(0n),v));
    }
  }
  if([...value.values()].some(c=>c[0]) || gradient.some(g=>[...g.values()].some(c=>c[0])))
    throw Error("RNC coefficient check failed");
  const d=bareiss(J),dk=bareiss(K);
  if(d.det!==-64701092257700249600n || dk.det!==-25600n)throw Error("unexpected determinant");
  return {
    coordinateConvention:"original x_j = i^j y_j, j=0,...,5; W_m = i^m W'_m",
    Kprime:K,Jprime:J,detKprime:dk.det,detJprime:d.det,
    bareissPivots:d.pivots,bareissRowSwaps:d.swaps,inverseJprime:Ji,
    quadraticExponents:e2,Fcoeff:Fc,Bcoeff:B,SchurH2coeff:T,Rterms:terms,
    verified:{traceEqualsConvolution:true,inverseExact:true,RNCValueAndAllGradientsZero:true},
    scope:"Finite ordinary scalar elimination only. No claim that the full critical locus equals the RNC, or that an actual Bell inverse or invariant-subspace conclusion follows."
  };
}
if(typeof module!=="undefined")module.exports={exactCertificate};
if(typeof require!=="undefined" && require.main===module)
  console.log(JSON.stringify(exactCertificate(),(_,v)=>typeof v==="bigint"?v.toString():v,2));
