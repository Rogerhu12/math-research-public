#!/usr/bin/env node
"use strict";

// R216: exact original-source finite quotient with nonunit low kernel.
// No dependencies; all rational and modular arithmetic uses BigInt.
// Reuses the previously calibrated p19 D4 k15 case; no prime scan.

function runRank2NonunitKernelCalibration() {
  "use strict";
  const size = 18;
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
  function Q(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}if(!n)return {n:0n,d:1n};const g=gcd(n,d);return {n:n/g,d:d/g};}
  const zero=Q(0),one=Q(1);
  function add(a,b){return Q(a.n*b.d+b.n*a.d,a.d*b.d);}
  function neg(a){return {n:-a.n,d:a.d};}
  function sub(a,b){return add(a,neg(b));}
  function mul(a,b){return Q(a.n*b.n,a.d*b.d);}
  function div(a,b){if(!b.n)throw Error("division by zero");return Q(a.n*b.d,a.d*b.n);}
  function series(values){const a=Array(size).fill(zero);values.forEach((v,i)=>{if(i<size)a[i]=typeof v==="object"?v:Q(v);});return a;}
  function sa(a,b){return a.map((x,i)=>add(x,b[i]));}
  function sn(a){return a.map(neg);}
  function sm(a,b){const c=series([]);for(let i=0;i<size;i++)if(a[i].n)for(let j=0;i+j<size;j++)if(b[j].n)c[i+j]=add(c[i+j],mul(a[i],b[j]));return c;}
  function sc(a,c){return a.map(x=>mul(x,c));}
  function si(a){const b=series([]);b[0]=div(one,a[0]);for(let n=1;n<size;n++){let s=zero;for(let i=1;i<=n;i++)s=add(s,mul(a[i],b[n-i]));b[n]=neg(div(s,a[0]));}return b;}
  function se(a){if(a[0].n)throw Error("exponential must have zero constant");const b=series([1]);for(let n=1;n<size;n++){let s=zero;for(let i=1;i<=n;i++)s=add(s,mul(Q(i),mul(a[i],b[n-i])));b[n]=div(s,Q(n));}return b;}
  function vpInt(a,p){if(!a)return 1000000;a=a<0n?-a:a;let n=0;while(a%p===0n){a/=p;n++;}return n;}
  function vp(a,p){return !a.n?1000000:vpInt(a.n,p)-vpInt(a.d,p);}
  function saturated(rows,p){
    const a=rows.map(r=>r.slice()),remaining=Array.from({length:a[0].length},(_,i)=>i),answer=[];
    for(let n=0;n<a.length&&remaining.length;n++){
      let pivot=remaining[0];for(const j of remaining)if(vp(a[n][j],p)<vp(a[n][pivot],p))pivot=j;
      const value=vp(a[n][pivot],p);if(value===1000000)continue;
      answer.push(value);remaining.splice(remaining.indexOf(pivot),1);
      const ratios=remaining.filter(j=>a[n][j].n).map(j=>[j,div(a[n][j],a[n][pivot])]);
      if(ratios.some(([,x])=>vp(x,p)<0))throw Error("nonintegral saturated elimination");
      for(let m=n+1;m<a.length;m++)if(a[m][pivot].n){
        const v=a[m][pivot];for(const[j,x]of ratios)a[m][j]=sub(a[m][j],mul(v,x));
      }
    }
    return {values:answer,remaining:remaining.length};
  }
  function mod(a,m){const b=a%m;return b<0n?b+m:b;}
  function inv(a,m){a=mod(a,m);let u=1n,v=0n,b=m;while(b){const q=a/b;[a,b]=[b,a-q*b];[u,v]=[v,u-q*v];}if(a!==1n)throw Error("nonunit inverse");return mod(u,m);}
  function reduce(a,m){return mod(a.n*inv(a.d,m),m);}
  function smithTruncated(matrix,p,N){
    let a=matrix.map(r=>r.slice()),modulus=p**BigInt(N),level=0;const exponents=[];
    while(a.length&&a[0].length&&level<N){
      let pi=-1,pj=-1;
      for(let i=0;i<a.length&&pi<0;i++)for(let j=0;j<a[i].length;j++)if(a[i][j]%p!==0n){pi=i;pj=j;break;}
      if(pi<0){a=a.map(row=>row.map(x=>x/p));modulus/=p;level++;continue;}
      [a[0],a[pi]]=[a[pi],a[0]];for(const row of a)[row[0],row[pj]]=[row[pj],row[0]];
      const inverse=inv(a[0][0],modulus);a[0]=a[0].map(x=>mod(x*inverse,modulus));
      for(let i=1;i<a.length;i++){const factor=a[i][0];a[i]=a[i].map((x,j)=>mod(x-factor*a[0][j],modulus));}
      exponents.push(level);a=a.slice(1).map(row=>row.slice(1));
    }
    return {exponents,imageLength:exponents.reduce((s,e)=>s+N-e,0)};
  }
  const s=series([0,1]),h1=series([1,4,70,4,1]),h2=series([1,20,-26,20,1]);
  const q8=series([1,0,364,-1088,1190,-1088,364,0,1]);
  const minus=series([1,-1]),plus=series([1,1]);
  let polynomial=s;
  for(const factor of [minus,minus,plus,series([1,-2,5]),series([5,-2,1]),h1,h2])polynomial=sm(polynomial,factor);
  polynomial=sc(polynomial,Q(1,5));
  const ratio=sa(sm(sm(plus,q8),si(sm(sm(minus,h1),h2))),series([-1]));
  const logarithm=series([]);let derivative=Q(17,3);
  for(let m=1;m<size;m++){logarithm[m]=div(derivative,Q(m));derivative=mul(derivative,Q(4*m+1,4*m+3));}
  const first=sm(polynomial,se(logarithm));
  if(first[1].n!==1n||first[1].d!==1n||first[2].n!==394n||first[2].d!==15n||ratio[1].n!==-22n||ratio[1].d!==1n)throw Error("actual source calibration failed");
  const powersA=[series([1])],powersV=[series([1])];
  for(let i=1;i<=4;i++){powersA.push(sm(powersA[i-1],first));powersV.push(sm(powersV[i-1],ratio));}
  const columns=[],values=[];
  for(let m=0;m<=4;m++)for(let c=0;c<=m;c++){columns.push({m,c});values.push(sm(powersA[m],powersV[c]));}
  const rows=Array.from({length:size},(_,n)=>values.map(v=>v[n]));

  const outputSize=15, originalC=sm(first,ratio), v0=Q(-22);
  function compose(a,b){let result=series([]),power=series([1]);for(let n=0;n<size;n++){if(a[n].n)result=sa(result,sc(power,a[n]));power=sm(power,b);}return result;}
  const rootInput=series([]);for(let n=0;n+2<size;n++)rootInput[n]=div(originalC[n+2],v0);
  if(rootInput[0].n!==1n||rootInput[0].d!==1n)throw Error("square-root leading coefficient");
  const root=series([1]);
  for(let n=1;n<size;n++){let cross=zero;for(let j=1;j<n;j++)cross=add(cross,mul(root[j],root[n-j]));root[n]=div(sub(rootInput[n],cross),Q(2));}
  const parameter=sm(s,root), inverse=series([0,1]);
  for(let n=2;n<=outputSize;n++){inverse[n]=zero;inverse[n]=neg(compose(parameter,inverse)[n]);}
  const inverseCheck=compose(parameter,inverse);
  if(inverseCheck.slice(0,outputSize).some((x,n)=>x.n!==BigInt(n===1)||x.d!==1n))throw Error("compositional inverse mismatch");
  const alpha=compose(first,inverse), originalCInV=compose(originalC,inverse);
  if(originalCInV.slice(0,outputSize).some((x,n)=>x.n!==(n===2?-22n:0n)||x.d!==1n))throw Error("C(v) is not v0 v^2");
  const even=series([]),odd=series([]);
  for(let n=0;2*n<outputSize;n++)even[n]=div(alpha[2*n],Q((-22n)**BigInt(n)));
  for(let n=0;2*n+1<outputSize;n++)odd[n]=div(alpha[2*n+1],Q((-22n)**BigInt(n)));
  const T=sc(even,Q(2)), Norm=subSeries(sm(even,even),sc(sm(s,sm(odd,odd)),Q(1,-22)));
  function subSeries(a,b){return sa(a,sn(b));}
  if(Norm[1].n!==1n||Norm[1].d!==22n)throw Error("norm leading coefficient");
  const Up=[series([1])],Vp=[series([])];
  for(let a=0;a<4;a++){Up.push(sn(sm(Norm,Vp[a])));Vp.push(sa(Up[a],sm(T,Vp[a])));}
  const p=19n,r=5,D=4,k=15,ell=2*D+1;
  function weight(n){const h=Math.floor(n/r);return h===0?0:h+Math.floor((h-1)/(Number(p)-1));}
  function coefficient(a,b,row){const n=Math.floor(row/2)-b;return n<0?zero:(row%2?Vp[a][n]:Up[a][n]);}
  const residualColumns=[];for(let m=0;m<=D-2;m++)for(let b=0;b<=m;b++)residualColumns.push({a:m-b,b});
  const cColumn=columns.findIndex(x=>x.m===1&&x.c===1),results=[];
  function same(a,b,message){if(JSON.stringify(a)!==JSON.stringify(b))throw Error(message);}
  const rawPrefix=saturated(rows.slice(0,k),p).values;
  same(rawPrefix,[0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-2],"previous p19 true prefix calibration");
  for(const N of [1,2,3]){
    const modulus=p**BigInt(N);
    function normalized(value,row){return reduce(mul(Q(p**BigInt(weight(row))),value),modulus);}
    const original=rows.slice(0,k).map((row,n)=>row.map(x=>normalized(x,n)));
    const paired=Array.from({length:k},(_,n)=>columns.map(col=>normalized(coefficient(col.m-col.c,col.c,n),n)));
    // Exact source splitting K_D plus A^2 E_(D-2), no rational Schur section.
    const remainder=Array.from({length:k},(_,n)=>residualColumns.map(col=>normalized(coefficient(col.a+2,col.b,n),n)));
    const b=Array.from({length:k},(_,j)=>j<ell?Math.min(N,weight(j)):N);
    // Embed O/p^b_j into O/p^N by multiplication by p^(N-b_j).
    const quotient=remainder.map((row,j)=>row.map(x=>mod(x*p**BigInt(N-b[j]),modulus)));
    const all=smithTruncated(original,p,N),pair=smithTruncated(paired,p,N);
    const deleted=smithTruncated(original.map(row=>row.filter((_,j)=>j!==cColumn)),p,N);
    const q=smithTruncated(quotient,p,N),qDeleted=smithTruncated(quotient.map(row=>row.slice(1)),p,N);
    const high=smithTruncated(remainder.slice(ell),p,N);
    const lowKernelLength=Array.from({length:ell},(_,j)=>Math.max(N-weight(j),0)).reduce((a,b)=>a+b,0);
    const lowTorsionLength=b.slice(0,ell).reduce((a,b)=>a+b,0);
    same(all,pair,"raw and pair images differ");
    if(all.imageLength!==lowKernelLength+q.imageLength)throw Error("nonunit low quotient formula");
    if(deleted.imageLength!==lowKernelLength+qDeleted.imageLength)throw Error("deleted-C finite quotient formula");
    if(all.imageLength-deleted.imageLength!==q.imageLength-qDeleted.imageLength)throw Error("cyclic image order");
    results.push({p:Number(p),r,D,k,N,lowKernelWeights:Array.from({length:ell},(_,j)=>weight(j)),lowKernelImageLength:lowKernelLength,lowTorsionLength,originalSmithBelowN:all.exponents,originalImageLength:all.imageLength,deletedCImageLength:deleted.imageLength,quotientImageLength:q.imageLength,quotientDeletedConstantImageLength:qDeleted.imageLength,highTailAloneImageLength:high.imageLength,extraInformationInLowTorsion:q.imageLength-high.imageLength,constantColumnOrderExponent:q.imageLength-qDeleted.imageLength,verified:true});
  }
  const final=results[2];
  const fullSmithSum=final.originalSmithBelowN.reduce((a,b)=>a+b,0);
  if(final.originalSmithBelowN.length!==15)throw Error("full original rank not observed");
  const high3=smithTruncated(Array.from({length:k-ell},(_,i)=>{const n=i+ell;return residualColumns.map(col=>reduce(mul(Q(p**BigInt(weight(n))),coefficient(col.a+2,col.b,n)),p**3n));}),p,3);
  if(high3.exponents.length!==6)throw Error("full high-tail rank not observed");
  const highSmithSum=high3.exponents.reduce((a,b)=>a+b,0),lowDetCost=Array.from({length:ell},(_,j)=>weight(j)).reduce((a,b)=>a+b,0);
  if(fullSmithSum!==lowDetCost+highSmithSum)throw Error("full-column minor factorization");
  return {source:"Same original P,Q and exact rational double component; s-to-w is a proved common integral triangular change on this old p19 prefix",rawSaturatedPrefixValues:rawPrefix,results,fullMinorCheck:{fullSmithSum,lowDetCost,highSmithSum,verified:true},scope:"Only the existing p19 D4 k15 case. Here r=5<=2D, so the low kernel is genuinely nonunit. No simultaneous central vanishing or infinite-prime nonvanishing is asserted."};

}

console.log(JSON.stringify(runRank2NonunitKernelCalibration(),null,2));
