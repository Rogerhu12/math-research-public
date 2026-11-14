// Exact certificate: four positive exceptional weights, two unit pool bits.
// Relative primitive birth 2, full inverse before fixed-block compression.
// The six-dimensional fixed block satisfies H1 H2^{-1} H1 < H0.
// Every arithmetic sign decision uses BigInt. No numerical samples.
"use strict";

function verifyFourHeadTwoPoolBlock() {
  const STEP=[1,32,1024,32768],zero=()=>new Map();
  const matrix=(r,c=r)=>Array.from({length:r},()=>Array.from({length:c},zero));
  const transpose=A=>A[0].map((_,j)=>A.map(row=>row[j]));
  let multiplications=0,maxInputExponentSum=0;
  function exponents(key) {
    if (!Number.isInteger(key)||key<0||key>=32**4) throw Error("bad monomial");
    return STEP.map(s=>Math.floor(key/s)%32);
  }
  function bounds(p) {
    const out=[0,0,0,0];
    for (const key of p.keys()) {
      const e=exponents(key);
      for (let i=0;i<4;i++) out[i]=Math.max(out[i],e[i]);
    }
    return out;
  }
  function keyOf(mask) {
    return STEP.reduce((s,e,i)=>s+(((mask>>i)&1)?e:0),0);
  }
  function accumulate(out,p,c=1n) {
    for (const [k,v] of p) {
      const z=(out.get(k)||0n)+c*v;
      if(z)out.set(k,z);else out.delete(k);
    }
    return out;
  }
  function multiply(a,b) {
    const x=bounds(a),y=bounds(b);multiplications++;
    for(let i=0;i<4;i++){
      maxInputExponentSum=Math.max(maxInputExponentSum,x[i]+y[i]);
      if(x[i]+y[i]>13)throw Error("exponent budget exceeded");
    }
    const out=zero();
    for(const[k,v]of a)for(const[l,w]of b){
      const z=(out.get(k+l)||0n)+v*w;
      if(z)out.set(k+l,z);else out.delete(k+l);
    }
    return out;
  }
  function product(A,B) {
    const out=matrix(A.length,B[0].length);
    for(let i=0;i<A.length;i++)for(let j=0;j<B[0].length;j++)
      for(let k=0;k<B.length;k++)accumulate(out[i][j],multiply(A[i][k],B[k][j]));
    return out;
  }
  function equal(a,b) {
    if(a.size!==b.size)return false;
    for(const[k,v]of a)if(b.get(k)!==v)return false;
    return true;
  }
  function integerDeterminant(T) {
    const n=T.length;
    if(!n)return 1n;if(n===1)return T[0][0];
    let z=0n;
    for(let j=0;j<n;j++)z+=(j%2?-1n:1n)*T[0][j]*
      integerDeterminant(T.slice(1).map(row=>row.filter((_,k)=>k!==j)));
    return z;
  }
  function combinations(N,k,callback) {
    const a=[];
    function rec(start) {
      if(a.length===k){callback([...a]);return;}
      for(let j=start;j<=N-(k-a.length);j++){
        a.push(j);rec(j+1);a.pop();
      }
    }
    rec(0);
  }

  // Cauchy--Binet determinant and adjugate of sum w_j v_j v_j^T.
  // All selected-frame minors are exact constant integer determinants.
  function gramDetAdj(frames,D) {
    const det=zero(),adj=matrix(D);
    let determinantFrames=0,adjugateFrames=0;
    combinations(frames.length,D,I=>{
      const T=Array.from({length:D},(_,r)=>I.map(j=>BigInt(frames[j].v[r])));
      const d=integerDeterminant(T);if(!d)return;
      let key=0,w=d*d;
      for(const j of I){key+=frames[j].key;w*=frames[j].weight;}
      if(Math.max(...exponents(key))>D)throw Error("frame exponent");
      accumulate(det,new Map([[key,w]]));determinantFrames++;
    });
    combinations(frames.length,D-1,I=>{
      const v=Array.from({length:D},(_,r)=>(r%2?-1n:1n)*
        integerDeterminant(Array.from({length:D},(_,j)=>j)
          .filter(j=>j!==r).map(j=>I.map(t=>BigInt(frames[t].v[j])))));
      if(v.every(x=>!x))return;
      let key=0,w=1n;
      for(const j of I){key+=frames[j].key;w*=frames[j].weight;}
      if(Math.max(...exponents(key))>D-1)throw Error("cofactor exponent");
      for(let i=0;i<D;i++)for(let j=0;j<D;j++)if(v[i]&&v[j])
        accumulate(adj[i][j],new Map([[key,w*v[i]*v[j]]]));
      adjugateFrames++;
    });
    return{det,adj,determinantFrames,adjugateFrames};
  }

  const pairs=[];
  for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)pairs.push([i,j]);
  const A=matrix(6),B=matrix(6),S=matrix(6),M=matrix(6,3),C=matrix(3);
  const framesB=[],framesC=[];
  for(let mask=0;mask<16;mask++){
    const bit=Array.from({length:4},(_,i)=>(mask>>i)&1);
    const r=bit.reduce((a,b)=>a+b,0),key=keyOf(mask);
    const f=pairs.map(([i,j])=>bit[i]*bit[j]);
    const fc=pairs.map(([i,j])=>(1-bit[i])*(1-bit[j]));
    const w0=r>=2?[2,1,2][r-2]:0;
    const w2=r<=2?[2,1,2][r]:0;
    const w1=r>=1&&r<=3?[2,1,2][r-1]:0;
    if(w0)for(let i=0;i<6;i++)for(let j=0;j<6;j++)if(f[i]&&f[j])
      accumulate(A[i][j],new Map([[key,BigInt(w0)]]));
    if(w2){
      framesB.push({v:fc,key,weight:BigInt(w2)});
      for(let i=0;i<6;i++)for(let j=0;j<6;j++)if(fc[i]&&fc[j])
        accumulate(B[i][j],new Map([[key,BigInt(w2)]]));
    }
    if(w1){
      // F(R)=f(R)-f(all)*1_(4 in R)+sum_{i<4} b_i(1_i-1_4).
      // Thus constant=0 and sum of four linear coefficients=-f(all).
      const v=f.map(x=>x-bit[3]),u=bit.slice(0,3).map(x=>x-bit[3]);
      const weight=BigInt(w1);
      framesC.push({v:u,key,weight});
      for(let i=0;i<6;i++)for(let j=0;j<6;j++)if(v[i]&&v[j])
        accumulate(S[i][j],new Map([[key,weight*BigInt(v[i]*v[j])]]));
      for(let i=0;i<6;i++)for(let j=0;j<3;j++)if(v[i]&&u[j])
        accumulate(M[i][j],new Map([[key,weight*BigInt(v[i]*u[j])]]));
      for(let i=0;i<3;i++)for(let j=0;j<3;j++)if(u[i]&&u[j])
        accumulate(C[i][j],new Map([[key,weight*BigInt(u[i]*u[j])]]));
    }
  }
  const cb=gramDetAdj(framesB,6),cc=gramDetAdj(framesC,3);
  for(const [G,t]of [[B,cb],[C,cc]]){
    const check=product(G,t.adj);
    for(let i=0;i<G.length;i++)for(let j=0;j<G.length;j++)
      if(!equal(check[i][j],i===j?t.det:zero()))throw Error("adjugate identity");
  }
  const correction=product(product(M,cc.adj),transpose(M)),K=matrix(6);
  for(let i=0;i<6;i++)for(let j=0;j<6;j++)
    K[i][j]=accumulate(multiply(cc.det,S[i][j]),correction[i][j],-1n);
  const common=multiply(multiply(cc.det,cc.det),cb.det);
  const KAK=product(product(K,cb.adj),K),P=matrix(6),keys=new Set();
  for(let i=0;i<6;i++)for(let j=0;j<6;j++){
    P[i][j]=accumulate(multiply(common,A[i][j]),KAK[i][j],-1n);
    for(const key of P[i][j].keys())keys.add(key);
  }
  for(let i=0;i<6;i++)for(let j=0;j<6;j++)
    if(!equal(P[i][j],P[j][i]))throw Error("nonsymmetric coefficient matrix");

  // Exact symmetric fraction-free elimination.
  // At each stage T/previous is the remaining Schur complement.
  // A positive diagonal pivot is a legal congruence.
  // If every remaining diagonal is zero, PSD requires the full block zero.
  function positiveSemidefinite(T) {
    T=T.map(row=>[...row]);let previous=1n,rank=0;
    for(let k=0;k<T.length;k++){
      for(let i=k;i<T.length;i++)if(T[i][i]<0n)return{pass:false,rank};
      let j=k;while(j<T.length&&!T[j][j])j++;
      if(j===T.length){
        for(let i=k;i<T.length;i++)for(let t=k;t<T.length;t++)
          if(T[i][t])return{pass:false,rank};
        return{pass:true,rank};
      }
      if(j!==k){
        [T[k],T[j]]=[T[j],T[k]];
        for(const row of T)[row[k],row[j]]=[row[j],row[k]];
      }
      const pivot=T[k][k];
      for(let i=k+1;i<T.length;i++)for(let j2=i;j2<T.length;j2++){
        const numerator=pivot*T[i][j2]-T[i][k]*T[k][j2];
        if(numerator%previous)throw Error("inexact fraction-free division");
        T[i][j2]=T[j2][i]=numerator/previous;
      }
      previous=pivot;rank++;
    }
    return{pass:true,rank};
  }
  const ranks=Array(7).fill(0);
  let maximumFinalExponent=0,maximumTotalDegree=0;
  for(const key of keys){
    const e=exponents(key);
    maximumFinalExponent=Math.max(maximumFinalExponent,...e);
    maximumTotalDegree=Math.max(maximumTotalDegree,e.reduce((a,b)=>a+b,0));
    const coefficient=P.map(row=>row.map(p=>p.get(key)||0n));
    const result=positiveSemidefinite(coefficient);
    if(!result.pass)throw Error("negative coefficient matrix");
    ranks[result.rank]++;
  }
  const anchorKey=4*STEP.reduce((a,b)=>a+b,0);
  const anchor=P.map(row=>row.map(p=>p.get(anchorKey)||0n));
  for(let i=0;i<6;i++)for(let j=0;j<6;j++){
    const shared=pairs[i].some(x=>pairs[j].includes(x));
    const expected=i===j?266240n:shared?-24064n:-86016n;
    if(anchor[i][j]!==expected)throw Error("strict anchor changed");
  }
  if(keys.size!==7689||ranks.join(",")!=="0,994,276,828,706,720,4165"||
     maximumFinalExponent!==10||maximumTotalDegree!==34||
     framesB.length!==11||framesC.length!==14||
     cb.determinantFrames!==303||cb.adjugateFrames!==423||
     cc.determinantFrames!==232||cc.adjugateFrames!==84)
    throw Error("certificate census changed");
  return{
    status:"PASS",
    scope:"q=4, L=2, fixed primitive birth 2, n=1; coefficient 1",
    coefficientMatrices:keys.size,ranks,
    maximumFinalExponent,maximumTotalDegree,maxInputExponentSum,multiplications,
    frameCounts:[cb.determinantFrames,cb.adjugateFrames,cc.determinantFrames,cc.adjugateFrames],
    anchor:{monomial:"(z1*z2*z3*z4)^4",diagonal:"266240",
      adjacent:"-24064",opposite:"-86016",
      eigenvalueDimensions1_3_2:["83968","352256","228352"]}
  };
}
const certificate=verifyFourHeadTwoPoolBlock();
if(typeof console!=="undefined")console.log(JSON.stringify(certificate));
