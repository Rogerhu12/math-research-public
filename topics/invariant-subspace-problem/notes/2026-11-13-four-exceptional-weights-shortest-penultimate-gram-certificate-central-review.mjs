// Exact finite certificate: q=4, L=4, relative birth 3, n=1.
// Scope: the four-dimensional weak-pool-fixed primitive block.
// Variables z_i are the positive squared head weights.
// All coefficients and principal minors use BigInt; no samples or floats.
"use strict";

function verifyFourHeadShortestBlock() {
  const D = 4, BASE = 32;
  const STEP = [1,32,1024,32768];
  const zero = () => new Map();
  const constant = v => v ? new Map([[0,v]]) : zero();
  const matrix = () => Array.from({length:D}, () =>
    Array.from({length:D}, zero));
  let multiplicationCount = 0, maximumInputExponentSum = 0;

  function exponents(key) {
    if (!Number.isInteger(key) || key < 0 || key >= BASE**D)
      throw Error("invalid monomial key");
    return STEP.map(s => Math.floor(key/s)%BASE);
  }
  function bounds(p) {
    const b = [0,0,0,0];
    for (const key of p.keys()) {
      const e = exponents(key);
      for (let i=0;i<D;i++) b[i] = Math.max(b[i],e[i]);
    }
    return b;
  }
  function monomial(mask,value) {
    let key = 0;
    for (let i=0;i<D;i++) if ((mask>>i)&1) key += STEP[i];
    return value ? new Map([[key,value]]) : zero();
  }
  function accumulate(out,p,scale=1n) {
    for (const [key,value] of p) {
      const next = (out.get(key)||0n)+scale*value;
      if (next) out.set(key,next); else out.delete(key);
    }
    return out;
  }
  function scaled(p,c) {
    return c ? new Map([...p].map(([k,v])=>[k,c*v])) : zero();
  }
  function multiply(a,b) {
    multiplicationCount++;
    const x=bounds(a),y=bounds(b);
    for (let i=0;i<D;i++) {
      maximumInputExponentSum=Math.max(maximumInputExponentSum,x[i]+y[i]);
      // Seven original multi-affine factors suffice for every product here.
      // In particular there can be no base-32 carry between variable slots.
      if (x[i]+y[i]>7) throw Error("unexpected exponent growth");
    }
    const out=zero();
    for (const [k,v] of a) for (const [l,w] of b) {
      const key=k+l, next=(out.get(key)||0n)+v*w;
      if (next) out.set(key,next); else out.delete(key);
    }
    return out;
  }
  function equal(a,b) {
    if (a.size!==b.size) return false;
    for (const [k,v] of a) if (b.get(k)!==v) return false;
    return true;
  }
  function determinant(T) {
    const d=T.length;
    if (!d) return constant(1n);
    if (d===1) return T[0][0];
    const out=zero();
    for (let j=0;j<d;j++) {
      const minor=T.slice(1).map(row=>row.filter((_,k)=>k!==j));
      accumulate(out,multiply(T[0][j],determinant(minor)),j%2?-1n:1n);
    }
    return out;
  }
  function integerDeterminant(T) {
    const d=T.length;
    if (!d) return 1n;
    if (d===1) return T[0][0];
    let out=0n;
    for (let j=0;j<d;j++)
      out+=(j%2?-1n:1n)*T[0][j]*
        integerDeterminant(T.slice(1).map(row=>row.filter((_,k)=>k!==j)));
    return out;
  }
  function product(A,B) {
    const out=matrix();
    for (let i=0;i<D;i++) for (let j=0;j<D;j++)
      for (let k=0;k<D;k++) accumulate(out[i][j],multiply(A[i][k],B[k][j]));
    return out;
  }

  // A=12 H_0, B=12 H_2, Z=12 W_1, K=12 Z H_1.
  const A=matrix(),B=matrix(),S=matrix(),mean=Array.from({length:D},zero);
  const w0=[0,12,3,2,3], w1=[12,3,2,3,12], w2=[3,2,3,12,0];
  const Z=zero();
  for (let mask=0;mask<16;mask++) {
    const bit=Array.from({length:D},(_,i)=>(mask>>i)&1);
    const r=bit.reduce((x,y)=>x+y,0),w=monomial(mask,BigInt(w1[r]));
    accumulate(Z,w);
    for (let i=0;i<D;i++) {
      if (bit[i]) accumulate(mean[i],w);
      for (let j=0;j<D;j++) {
        if (bit[i]&&bit[j]) {
          accumulate(S[i][j],w);
          if (w0[r]) accumulate(A[i][j],monomial(mask,BigInt(w0[r])));
        }
        if (!bit[i]&&!bit[j]&&w2[r])
          accumulate(B[i][j],monomial(mask,BigInt(w2[r])));
      }
    }
  }
  const K=matrix();
  for (let i=0;i<D;i++) for (let j=0;j<D;j++)
    K[i][j]=accumulate(multiply(Z,S[i][j]),multiply(mean[i],mean[j]),-1n);
  const detB=determinant(B),adjB=matrix();
  for (let i=0;i<D;i++) for (let j=0;j<D;j++)
    adjB[i][j]=scaled(
      determinant(B.filter((_,r)=>r!==j).map(row=>row.filter((_,c)=>c!==i))),
      (i+j)%2?-1n:1n);
  const check=product(B,adjB);
  for (let i=0;i<D;i++) for (let j=0;j<D;j++)
    if (!equal(check[i][j],i===j?detB:zero()))
      throw Error("adjugate identity failed");

  const common=multiply(multiply(Z,Z),detB),KAK=product(product(K,adjB),K);
  const P=matrix(),keys=new Set();
  for (let i=0;i<D;i++) for (let j=0;j<D;j++) {
    P[i][j]=accumulate(scaled(multiply(common,A[i][j]),4n),KAK[i][j],-5n);
    for (const key of P[i][j].keys()) keys.add(key);
  }
  for (let i=0;i<D;i++) for (let j=0;j<D;j++)
    if (!equal(P[i][j],P[j][i])) throw Error("symmetry failed");

  const ranks=[0,0,0,0,0];
  let maximumFinalExponent=0,maximumFinalTotalDegree=0,principalChecks=0;
  for (const key of keys) {
    const ex=exponents(key);
    maximumFinalExponent=Math.max(maximumFinalExponent,...ex);
    maximumFinalTotalDegree=Math.max(maximumFinalTotalDegree,ex.reduce((a,b)=>a+b,0));
    const coefficient=P.map(row=>row.map(p=>p.get(key)||0n));
    let rank=0;
    for (let mask=1;mask<16;mask++) {
      const I=Array.from({length:D},(_,i)=>i).filter(i=>(mask>>i)&1);
      const value=integerDeterminant(I.map(i=>I.map(j=>coefficient[i][j])));
      principalChecks++;
      if (value<0n) throw Error("negative coefficient principal minor");
      if (value>0n) rank=Math.max(rank,I.length);
    }
    ranks[rank]++;
  }
  const anchorKey=STEP.reduce((a,b)=>a+b,0);
  const anchor=P.map(row=>row.map(p=>p.get(anchorKey)||0n));
  for (let i=0;i<D;i++) for (let j=0;j<D;j++)
    if (anchor[i][j]!== (i===j?165888n:77760n))
      throw Error("strict anchor changed");
  if (keys.size!==2156 || ranks.join(",")!=="0,77,356,598,1125" ||
      maximumFinalExponent!==6 || maximumFinalTotalDegree!==24)
    throw Error("certificate census changed");

  return {
    status:"PASS",
    scope:"q=4, L=4, weak-pool-fixed primitive birth 3, n=1",
    coefficient:"4/5",
    coefficientMatrices:keys.size,principalChecks,ranks,
    maximumInputExponentSum,maximumFinalExponent,maximumFinalTotalDegree,
    multiplicationCount,
    anchor:{monomial:"z1*z2*z3*z4",diagonal:"165888",offDiagonal:"77760",
      eigenvalueStandard:"88128",eigenvalueConstant:"399168"}
  };
}
const certificate=verifyFourHeadShortestBlock();
if (typeof console!=="undefined") console.log(JSON.stringify(certificate));
