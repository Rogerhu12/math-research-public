// Exact actual Moore--Penrose low-edge certificate. All sign decisions use BigInt.
"use strict";

function q4CertificateFrames(L) {
 const STEPS=[1,32,1024,32768],pairs=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)pairs.push([i,j]);
 const pop=m=>{let n=0;for(;m;m&=m-1)n++;return n}, key=m=>STEPS.reduce((s,v,i)=>s+((m>>i&1)?v:0),0);
 const d0=L*(L-1),d1=d0*(L-2),d2=d1*(L-3);
 const F0=[],F1=[],F2=[];
 for(let m=0;m<16;m++){const b=Array.from({length:4},(_,i)=>(m>>i)&1),r=pop(m),f=pairs.map(([i,j])=>b[i]*b[j]);
  const common={mask:m,key:key(m),f,b};
  if(r>=2)F0.push({...common,v:f,w:BigInt([d0,L-1,2][r-2])});
  if(r>=1)F1.push({...common,v:b,w:BigInt([d1,(L-1)*(L-2),2*(L-2),6][r-1])});
  F2.push({...common,v:[...f,1,...b],w:BigInt([d2,(L-1)*(L-2)*(L-3),2*(L-2)*(L-3),6*(L-3),24][r])});
 }
 return{STEPS,pairs,F0,F1,F2,d0,d1,d2};
}
function biDet(A){
 const n=A.length;if(!n)return 1n;
 let a=A.map(r=>r.map(BigInt)),den=1n,sign=1n;
 for(let k=0;k<n-1;k++){let p=k;while(p<n&&!a[p][k])p++;if(p===n)return 0n;
  if(p!==k){[a[p],a[k]]=[a[k],a[p]];sign=-sign;}
  const z=a[k][k];for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){const v=z*a[i][j]-a[i][k]*a[k][j];if(v%den)throw Error("Bareiss");a[i][j]=v/den;}den=z;
 } return sign*a[n-1][n-1];
}
function eachComb(N,k,cb){const a=[];function rec(s){if(a.length===k){cb(a);return;}for(let j=s;j<=N-k+a.length;j++){a.push(j);rec(j+1);a.pop();}}rec(0);}
const zpoly=()=>new Map(),zmatrix=(m,n=m)=>Array.from({length:m},()=>Array.from({length:n},zpoly));
function addTerm(P,k,v){if(!v)return;v+=(P.get(k)||0n);if(v)P.set(k,v);else P.delete(k);}
function gramCB(frames,D,rows=null){
 rows=rows??Array.from({length:D},(_,i)=>i);const det=zpoly(),adj=zmatrix(rows.length);
 let nd=0,na=0;
 eachComb(frames.length,D,I=>{const d=biDet(Array.from({length:D},(_,r)=>I.map(j=>frames[j].v[r])));if(!d)return;let k=0,w=d*d;for(const j of I){k+=frames[j].key;w*=frames[j].w;}addTerm(det,k,w);nd++;});
 eachComb(frames.length,D-1,I=>{
  const u=rows.map(r=>(r%2?-1n:1n)*biDet(Array.from({length:D},(_,s)=>s).filter(s=>s!==r).map(s=>I.map(j=>frames[j].v[s]))));
  if(u.every(v=>!v))return;let k=0,w=1n;for(const j of I){k+=frames[j].key;w*=frames[j].w;}for(let i=0;i<rows.length;i++)for(let j=0;j<rows.length;j++)addTerm(adj[i][j],k,w*u[i]*u[j]);na++;
 });return{det,adj,nd,na};
}
function middleCB(frames){
 const det=zpoly(),K=zmatrix(6);let nd=0,nk=0;
 eachComb(frames.length,4,I=>{const d=biDet(Array.from({length:4},(_,r)=>I.map(j=>frames[j].b[r])));if(!d)return;let k=0,w=d*d;for(const j of I){k+=frames[j].key;w*=frames[j].w;}addTerm(det,k,w);nd++;});
 eachComb(frames.length,5,I=>{
  const u=I.map((_,r)=>(r%2?-1n:1n)*biDet(Array.from({length:4},(_,s)=>I.filter((_,j)=>j!==r).map(j=>frames[j].b[s]))));
  const v=Array.from({length:6},(_,r)=>I.reduce((z,j,i)=>z+u[i]*BigInt(frames[j].f[r]),0n));if(v.every(x=>!x))return;
  let k=0,w=1n;for(const j of I){k+=frames[j].key;w*=frames[j].w;}for(let i=0;i<6;i++)for(let j=0;j<6;j++)addTerm(K[i][j],k,w*v[i]*v[j]);nk++;
 });return{det,K,nd,nk};
}
function jsonPol(P){return [...P].map(([k,v])=>[k,v.toString()]);}
function jsonMat(A){return A.map(r=>r.map(jsonPol));}
function fromPol(P){return new Map(P.map(([k,v])=>[k,BigInt(v)]));}
function fromMat(A){return A.map(r=>r.map(fromPol));}

const boundCache=new WeakMap();
function exponentBounds(p){if(boundCache.has(p))return boundCache.get(p);const z=[0,0,0,0];for(const k of p.keys())for(let i=0;i<4;i++)z[i]=Math.max(z[i],Math.floor(k/[1,32,1024,32768][i])%32);boundCache.set(p,z);return z;}
let maximumInputExponent=0;
function polyMul(a,b){const aa=exponentBounds(a),bb=exponentBounds(b);for(let i=0;i<4;i++){maximumInputExponent=Math.max(maximumInputExponent,aa[i]+bb[i]);if(aa[i]+bb[i]>25)throw Error("monomial exponent bound");}const c=zpoly();for(const[k,v]of a)for(const[l,w]of b)addTerm(c,k+l,v*w);return c;}
function polyAcc(a,b,s=1n){for(const[k,v]of b)addTerm(a,k,s*v);return a;}
function matMul(A,B){const C=zmatrix(A.length,B[0].length);for(let i=0;i<C.length;i++)for(let j=0;j<C[0].length;j++)for(let k=0;k<B.length;k++)polyAcc(C[i][j],polyMul(A[i][k],B[k][j]));return C;}

function verifyFourHeadFourPoolLowEdge(){
 const data=q4CertificateFrames(4);
 const aa=gramCB(data.F0,6),cc=middleCB(data.F1),gg=gramCB(data.F2,11);
 const A=zmatrix(6),G=zmatrix(11),S=zmatrix(6),M=zmatrix(6,4),C=zmatrix(4);
 for(const f of data.F0)for(let i=0;i<6;i++)for(let j=0;j<6;j++)addTerm(A[i][j],f.key,f.w*BigInt(f.f[i]*f.f[j]));
 for(const f of data.F2)for(let i=0;i<11;i++)for(let j=0;j<11;j++)addTerm(G[i][j],f.key,f.w*BigInt(f.v[i]*f.v[j]));
 for(const f of data.F1){
  for(let i=0;i<6;i++)for(let j=0;j<6;j++)addTerm(S[i][j],f.key,f.w*BigInt(f.f[i]*f.f[j]));
  for(let i=0;i<6;i++)for(let j=0;j<4;j++)addTerm(M[i][j],f.key,f.w*BigInt(f.f[i]*f.b[j]));
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)addTerm(C[i][j],f.key,f.w*BigInt(f.b[i]*f.b[j]));
 }
 const cAdj=gramCB(data.F1,4);
 const same=(p,q)=>p.size===q.size&&[...p].every(([k,v])=>q.get(k)===v);
 for(const [matrix,adj,det] of [[A,aa.adj,aa.det],[C,cAdj.adj,cAdj.det],[G,gg.adj,gg.det]]){
  const test=matMul(matrix,adj);for(let i=0;i<test.length;i++)for(let j=0;j<test.length;j++)if(!same(test[i][j],i===j?det:zpoly()))throw Error("full adjugate identity");
 }
 if(!same(cc.det,cAdj.det))throw Error("middle determinant");
 const Mt=M[0].map((_,i)=>M.map(r=>r[i])),correction=matMul(matMul(M,cAdj.adj),Mt);
 for(let i=0;i<6;i++)for(let j=0;j<6;j++){
  const p=polyAcc(polyMul(cc.det,S[i][j]),correction[i][j],-1n);
  if(!same(p,cc.K[i][j]))throw Error("middle Schur identity");
 }
 const topAdj=gg.adj.slice(0,6).map(r=>r.slice(0,6));
 const KGK=matMul(matMul(cc.K,topAdj),cc.K);
 const N=zpoly();for(let i=0;i<6;i++)for(let j=0;j<6;j++)polyAcc(N,polyMul(aa.adj[i][j],KGK[j][i]));
 const D=polyMul(polyMul(aa.det,polyMul(cc.det,cc.det)),gg.det);
 if(N.size!==D.size)throw Error("supports differ");
 let minimum=null,minimumAt=null,maxExponent=0,maxTotalDegree=0;
 for(const[k,v]of D){
  if(v<=0n||!N.has(k)||N.get(k)<=0n)throw Error("positive coefficient support");
  const gap=5n*v-N.get(k);if(gap<=0n)throw Error("trace bound failed");
  const exponents=[1,32,1024,32768].map(s=>Math.floor(k/s)%32);
  maxExponent=Math.max(maxExponent,...exponents);maxTotalDegree=Math.max(maxTotalDegree,exponents.reduce((a,b)=>a+b,0));
  if(minimum===null||gap<minimum){minimum=gap;minimumAt=exponents;}
 }
 const counts=[aa.nd,aa.na,cc.nd,cc.nk,gg.nd,gg.na];
 if(D.size!==21251||minimum!==511284864104792064n||counts.join(",")!=="303,423,940,2778,3008,7408"||maxExponent!==21)throw Error("certificate census");
 return{status:"PASS",scope:"four positive exceptional weights, four unit pool bits; birth 2 fixed block; n=1",
  conclusion:"tr(H0^-1 H1 H2^-1 H1)<5/2, hence H1 H2^-1 H1 < (5/2) H0",
  coefficients:D.size,minimumGap:minimum.toString(),minimumAt,frameCounts:counts,
  maximumInputExponent,maxExponent,maxTotalDegree,
  identities:["A adjA=detA I","C adjC=detC I","G adjG=detG I","K=detC S-M adjC M^T"]};
}
const certificate=verifyFourHeadFourPoolLowEdge();
if(typeof console!=="undefined")console.log(JSON.stringify(certificate));
