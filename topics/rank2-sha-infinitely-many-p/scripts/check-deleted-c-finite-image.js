#!/usr/bin/env node
"use strict";

// R206: exact original-source calibration of the deleted-C finite image.
// No dependencies; all rational and modular arithmetic uses BigInt.
// The p19 D4 record is the existing source calibration, not a new prime scan.

function runRank2DeletedColumnCalibration() {
  "use strict";
  const size = 15;
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
  function solveCongruence(matrix,rhs,p,N){
    const modulus=p**BigInt(N);
    if(!matrix.length)return [];
    const ncols=matrix[0].length;
    if(!ncols){if(rhs.some(x=>mod(x,modulus)!==0n))throw Error("inconsistent empty system");return [];}
    if(!N)return Array(ncols).fill(0n);
    let a=matrix.map(row=>row.map(x=>mod(x,modulus))),b=rhs.map(x=>mod(x,modulus));
    let pi=-1,pj=-1;
    for(let i=0;i<a.length&&pi<0;i++)for(let j=0;j<ncols;j++)if(a[i][j]%p!==0n){pi=i;pj=j;break;}
    if(pi<0){
      if(b.some(x=>x%p!==0n))throw Error("inconsistent divisibility");
      return solveCongruence(a.map(row=>row.map(x=>x/p)),b.map(x=>x/p),p,N-1);
    }
    [a[0],a[pi]]=[a[pi],a[0]];[b[0],b[pi]]=[b[pi],b[0]];
    for(const row of a)[row[0],row[pj]]=[row[pj],row[0]];
    const inverse=inv(a[0][0],modulus);a[0]=a[0].map(x=>mod(x*inverse,modulus));b[0]=mod(b[0]*inverse,modulus);
    for(let i=1;i<a.length;i++){
      const factor=a[i][0];a[i]=a[i].map((x,j)=>mod(x-factor*a[0][j],modulus));b[i]=mod(b[i]-factor*b[0],modulus);
    }
    const tail=a.length===1?Array(ncols-1).fill(0n):solveCongruence(a.slice(1).map(row=>row.slice(1)),b.slice(1),p,N);
    let firstValue=b[0];for(let j=1;j<ncols;j++)firstValue-=a[0][j]*tail[j-1];
    const answer=[mod(firstValue,modulus),...tail];[answer[0],answer[pj]]=[answer[pj],answer[0]];
    return answer;
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
  const calibration=saturated(rows,19n),expected=[0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-1,-2];
  if(JSON.stringify(calibration.values)!==JSON.stringify(expected)||calibration.remaining)throw Error("known p19 saturated profile mismatch");
  const p=43n,N=3,r=11,modulus=p**3n;
  const matrix=rows.map((row,n)=>row.map(v=>reduce(mul(Q(p**BigInt(Math.floor(n/r))),v),modulus)));
  const cColumn=columns.findIndex(x=>x.m===1&&x.c===1),results=[];
  for(const k of [14,15]){
    const j=smithTruncated(matrix.slice(0,k),p,N);
    const j0=smithTruncated(matrix.slice(0,k).map(row=>row.filter((_,i)=>i!==cColumn)),p,N);
    const record={D:4,p:43,r,k,N,sourceDimension:15,CColumnIndex:cColumn,smithJBelowN:j.exponents,smithWithoutCBelowN:j0.exponents,imageLengthJ:j.imageLength,imageLengthWithoutC:j0.imageLength,aN:j.imageLength-j0.imageLength};
    if(k===14){
      const otherColumns=columns.map((_,i)=>i).filter(i=>i!==cColumn);
      const witnessOthers=solveCongruence(matrix.slice(0,k).map(row=>otherColumns.map(i=>row[i])),matrix.slice(0,k).map(row=>mod(-p*row[cColumn],modulus)),p,N);
      const witness=Array(columns.length).fill(0n);witness[cColumn]=p;otherColumns.forEach((j,i)=>witness[j]=witnessOthers[i]);
      const residues=matrix.slice(0,k).map(row=>mod(row.reduce((sum,v,i)=>sum+v*witness[i],0n),modulus));
      if(residues.some(x=>x!==0n)||!witness.some(x=>x%p!==0n))throw Error("primitive witness verification failed");
      record.witness={modulus:Number(modulus),C_coefficient:Number(p),terms:columns.map((col,i)=>({A:col.m-col.c,C:col.c,coefficient:Number(witness[i]>modulus/2n?witness[i]-modulus:witness[i])})).filter(x=>x.coefficient!==0),allNormalizedPrefixResidues:residues.map(Number),primitive:true};
    }
    results.push(record);
  }
  return {source:"R162 actual P,Q,W; parameter s=u^4",calibration:{D:4,p:19,rawSaturatedValues:calibration.values,matchedExistingRecord:true},results,scope:"This tests the original matrix and degree condition only. It does not assume or certify simultaneous complete central vanishing."};
}

console.log(JSON.stringify(runRank2DeletedColumnCalibration(), null, 2));
