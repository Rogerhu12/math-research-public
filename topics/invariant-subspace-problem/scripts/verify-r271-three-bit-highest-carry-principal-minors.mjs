// Author: Astra-ISP-b2a9acde-20261120 / r271_cost with root.
// AI-assisted GPT-6 Astra Pro. 2026-11-20 UTC.
// R271 exact finite check for the three-bit N head, r = 3.
// Parameters: b0 = 1, b1 = 1/4, b2 = 1/9; s = 1; tail J_l;
// l in {1,3,5,7,9}; integer scale Cbar = 36 C, Vbar = 36 V.
// A finite-field computation selects candidates only. Every certificate is then
// reconstructed by BigInt fraction-free elimination and checked over Z/Q.
// No elimination arrays or determinant tables are emitted or saved.

import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
const suiteStarted = performance.now();

const run = (() => {
const MOD = 1000003;
const mod = (x) => ((x % MOD) + MOD) % MOD;
function inv(a) {
  let exponent = MOD - 2, result = 1;
  while (exponent) {
    if (exponent & 1) result = mod(result * a);
    a = mod(a * a);
    exponent = Math.floor(exponent / 2);
  }
  return result;
}
function zero(n, m = n) {
  return Array.from({length: n}, () => Array(m).fill(0));
}
function identity(n) {
  const a = zero(n);
  for (let i = 0; i < n; ++i) a[i][i] = 1;
  return a;
}

function tr(a){return a[0].map((_,j)=>a.map(row=>row[j]));}
function mm(a,b){let z=zero(a.length,b[0].length);for(let i=0;i<a.length;i++)for(let k=0;k<b.length;k++)if(a[i][k])for(let j=0;j<b[0].length;j++)if(b[k][j])z[i][j]=mod(z[i][j]+a[i][k]*b[k][j]);return z;}
function rr(a){a=a.map(row=>row.map(mod));let k=0,piv=[];for(let j=0;j<a[0].length&&k<a.length;j++){let p=k;while(p<a.length&&!a[p][j])p++;if(p===a.length)continue;[a[p],a[k]]=[a[k],a[p]];let z=inv(a[k][j]);for(let q=j;q<a[0].length;q++)a[k][q]=mod(a[k][q]*z);for(let i=0;i<a.length;i++)if(i!==k&&a[i][j]){let v=a[i][j];for(let q=j;q<a[0].length;q++)a[i][q]=mod(a[i][q]-v*a[k][q]);}piv.push(j);k++;}return{a,piv,rank:k};}
function kernel(a){let r=rr(a),free=Array.from({length:a[0].length},(_,i)=>i).filter(i=>!r.piv.includes(i)),K=zero(a[0].length,free.length);for(let j=0;j<free.length;j++){K[free[j]][j]=1;for(let i=0;i<r.rank;i++)K[r.piv[i]][j]=mod(-r.a[i][free[j]]);}return{K,free,piv:r.piv};}
function sympiv(M){let ids=Array.from({length:M.length},(_,i)=>i),A=M.map(x=>x.slice()),out=[];while(ids.length){let p=A.findIndex((row,i)=>row[i]);if(p>=0){let rest=ids.map((_,i)=>i).filter(i=>i!==p),a=inv(A[p][p]);out.push(ids[p]);A=rest.map(i=>rest.map(j=>mod(A[i][j]-A[i][p]*a%MOD*A[p][j])));ids=rest.map(i=>ids[i]);}else{let p=-1,q=-1;outer:for(let i=0;i<A.length;i++)for(let j=i+1;j<A.length;j++)if(A[i][j]){p=i;q=j;break outer;}if(p<0)break;let rest=ids.map((_,i)=>i).filter(i=>i!==p&&i!==q),a=inv(A[p][q]);out.push(ids[p],ids[q]);A=rest.map(i=>rest.map(j=>mod(A[i][j]-mod(A[i][p]*a)*A[q][j]-mod(A[i][q]*a)*A[p][j])));ids=rest.map(i=>ids[i]);}}return out;}
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b];}return a;}
function rat(a,b=1n){if(!a)return[0n,1n];if(b<0n){a=-a;b=-b;}let g=gcd(a,b);return[a/g,b/g];}
const sub=(a,b)=>rat(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
const muli=(a,b)=>rat(a[0]*b,a[1]);
const divi=(a,b)=>rat(a[0],a[1]*b);
function bareiss(A,B=null){let n=A.length,m=n+(B?B[0].length:0),a=A.map((row,i)=>row.map(BigInt).concat(B?B[i].map(BigInt):[])),old=1n,sign=1n;for(let k=0;k<n-1;k++){let p=k;while(p<n&&!a[p][k])p++;if(p===n)throw Error("singular");if(p!==k){[a[p],a[k]]=[a[k],a[p]];sign=-sign;}let v=a[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<m;j++){let num=v*a[i][j]-a[i][k]*a[k][j];if(num%old)throw Error("nonexact");a[i][j]=num/old;}a[i][k]=0n;}old=v;}let det=sign*a[n-1][n-1];if(!B)return{det};let sol=Array.from({length:n},()=>Array(B[0].length));for(let i=n-1;i>=0;i--)for(let j=0;j<B[0].length;j++){let z=rat(a[i][n+j]);for(let k=i+1;k<n;k++)z=sub(z,muli(sol[k][j],a[i][k]));sol[i][j]=divi(z,a[i][i]);}return{det,sol};}
function pop(x){let n=0;while(x){x&=x-1;n++;}return n;}
function run(l){let N=8*l,c=[],v=[],at=(h,j)=>h*l+j;for(let j=0;j<l;j++){for(let b=0;b<2;b++){let o=4*b;c.push([at(o,j),at(o+1,j),36],[at(o,j),at(o+2,j),9],[at(o+1,j),at(o+2,j),36],[at(o+1,j),at(o+3,j),9],[at(o+2,j),at(o+3,j),36]);}for(let h=0;h<4;h++)c.push([at(h,j),at(h+4,j),4]);v.push([at(2,j),at(4,j),9],[at(3,j),at(4,j),36],[at(3,j),at(5,j),9]);for(let h=0;h<8;h++)if(j)c.push([at(h,j-1),at(h,j),36]);}
function isparse(e,x){let y=zero(N);for(let [a,b,c]of e)for(let j=0;j<N;j++)y[a][j]+=c*x[b][j];return y;}
let X=identity(N),Y=zero(N);for(let r=1;r<=3;r++){let ny=isparse(c,Y),vx=isparse(v,X);for(let i=0;i<N;i++)for(let j=0;j<N;j++)ny[i][j]+=vx[i][j];X=isparse(c,X);Y=ny;}
for (const row of X.concat(Y)) for (const entry of row) if (!Number.isSafeInteger(entry)) throw Error("unsafe integer matrix entry");
let grade=Array.from({length:N},(_,i)=>pop(Math.floor(i/l))+i%l),cut=(l+1)/2,cols=grade.map((g,i)=>[g,i]).filter(z=>z[0]>=cut).map(z=>z[1]),A=X.map(row=>cols.map(j=>row[j])),kr=kernel(A),Kfull=zero(N,kr.free.length);for(let i=0;i<cols.length;i++)Kfull[cols[i]]=kr.K[i];let M=mm(tr(Kfull),mm(Y,Kfull).reverse()),p=sympiv(M),free=p.map(j=>kr.free[j]),rows=rr(tr(A)).piv;
let BB=rows.map(i=>kr.piv.map(j=>A[i][j])),rhs=rows.map(i=>free.map(j=>A[i][j])),sol=bareiss(BB,rhs).sol,cert=[];
for(let j=0;j<free.length;j++){let vec=Array.from({length:N},()=>rat(0n));vec[cols[free[j]]]=rat(1n);for(let i=0;i<kr.piv.length;i++)vec[cols[kr.piv[i]]]=rat(-sol[i][j][0],sol[i][j][1]);let den=1n;for(let v of vec)den=den/gcd(den,v[1])*v[1];let ints=vec.map(v=>v[0]*(den/v[1])),g=0n;for(let v of ints)g=gcd(g,v);ints=ints.map(v=>v/g);let fst=ints.find(v=>v);if(fst<0n)ints=ints.map(v=>-v);for(let i=0;i<N;i++){let val=0n;for(let k=0;k<N;k++)val+=BigInt(X[i][k])*ints[k];if(val)throw Error("kernel fail");}cert.push(ints);}
let BM=cert.map(u=>cert.map(w=>{let z=0n;for(let i=0;i<N;i++)if(u[i])for(let j=0;j<N;j++)if(w[j])z+=u[i]*BigInt(Y[N-1-i][j])*w[j];return z;})),det=bareiss(BM).det;
return{l,N,cut,rank:p.length,det:det.toString(),vectors:cert.map(w=>w.map((x,i)=>[i,x.toString()]).filter(x=>x[1]!=="0")),B:BM.map(row=>row.map(String))};}
return run;

})();

function chainRank(a, b, r) {
  let result = 0;
  for (let j = 0; j < Math.min(a, b); ++j)
    result += Math.max(a + b - 1 - 2*j - r, 0);
  return result;
}
function popcount(value) {
  let result = 0;
  while (value) { value &= value - 1; ++result; }
  return result;
}
const aggregate = createHash("sha256");
for (const l of [1, 3, 5, 7, 9]) {
  const result = run(l);
  const expectedRank = chainRank(8, l, 3)
    - chainRank(5, l, 3) - chainRank(3, l, 3);
  if (result.rank !== expectedRank || result.rank > 7)
    throw new Error("rank certificate does not cover the full Jordan rank gain");
  if (BigInt(result.det) === 0n)
    throw new Error("singular Schur certificate");
  for (const vector of result.vectors) {
    if (vector.length > 12)
      throw new Error("sparse coefficient bound exceeded");
    for (const [index, entry] of vector) {
      const coefficient = BigInt(entry);
      if (coefficient < -128n || coefficient > 128n)
        throw new Error("integer coefficient bound exceeded");
      const grade = popcount(Math.floor(index / l)) + index % l;
      if (grade < (l + 1)/2)
        throw new Error("high-grade support condition failed");
    }
  }
  for (let i = 0; i < result.B.length; ++i)
    for (let j = 0; j < result.B.length; ++j)
      if (result.B[i][j] !== result.B[j][i])
        throw new Error("Schur form is not symmetric");

  const digest = createHash("sha256")
    .update(JSON.stringify(result)).digest("hex");
  aggregate.update(digest);
  console.log(JSON.stringify({
    check: "r271_three_bit_high_pole_minor",
    tail_length: l,
    grade_threshold: (l + 1)/2,
    complete_rank_gain: expectedRank,
    exact_kernel_equations: true,
    exact_schur_nonsingularity: true,
    support_and_coefficient_bounds: true,
    certificate_sha256: digest
  }));
}
console.log(JSON.stringify({
  check: "r271_three_bit_high_pole_minor_suite",
  passed: true,
  reconstruction_sha256: aggregate.digest("hex")
}));

console.log(JSON.stringify({check:"r271_exact_run_identity",source_sha256:createHash("sha256").update(readFileSync(new URL(import.meta.url))).digest("hex"),node_version:process.versions.node,elapsed_seconds:(performance.now()-suiteStarted)/1000}));
