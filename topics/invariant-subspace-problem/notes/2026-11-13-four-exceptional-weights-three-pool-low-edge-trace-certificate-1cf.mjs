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
function polyMul(a,b){const aa=exponentBounds(a),bb=exponentBounds(b);for(let i=0;i<4;i++){maximumInputExponent=Math.max(maximumInputExponent,aa[i]+bb[i]);if(aa[i]+bb[i]>24)throw Error("monomial exponent bound");}const c=zpoly();for(const[k,v]of a)for(const[l,w]of b)addTerm(c,k+l,v*w);return c;}
function polyAcc(a,b,s=1n){for(const[k,v]of b)addTerm(a,k,s*v);return a;}
function matMul(A,B){const C=zmatrix(A.length,B[0].length);for(let i=0;i<C.length;i++)for(let j=0;j<C[0].length;j++)for(let k=0;k<B.length;k++)polyAcc(C[i][j],polyMul(A[i][k],B[k][j]));return C;}

function q4ThreePoolFrames(){
 const steps=[1,32,1024,32768],pairs=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)pairs.push([i,j]);
 const F0=[],F1=[],F2=[];
 for(let mask=0;mask<16;mask++){
  const b=Array.from({length:4},(_,i)=>mask>>i&1),r=b.reduce((a,c)=>a+c,0),key=b.reduce((a,c,i)=>a+c*steps[i],0),f=pairs.map(([i,j])=>b[i]*b[j]);
  const common={mask,key,b,f};
  if(r>=2)F0.push({...common,v:f,w:BigInt([6,2,2][r-2])});
  if(r>=1)F1.push({...common,v:b,w:BigInt([6,2,2,6][r-1])});
  if(r<=3)F2.push({...common,v:[...f.map(x=>x-b[3]),1-b[3],...b.slice(0,3).map(x=>x-b[3])],w:BigInt([6,2,2,6][r])});
 }return{F0,F1,F2};
}

function verifyFourHeadThreePoolLowEdge(){
 const f=q4ThreePoolFrames(),aa=gramCB(f.F0,6),cc=middleCB(f.F1),gg=gramCB(f.F2,10),cAdj=gramCB(f.F1,4);
 const A=zmatrix(6),G=zmatrix(10),S=zmatrix(6),M=zmatrix(6,4),C=zmatrix(4);
 for(const v of f.F0)for(let i=0;i<6;i++)for(let j=0;j<6;j++)addTerm(A[i][j],v.key,v.w*BigInt(v.f[i]*v.f[j]));
 for(const v of f.F2)for(let i=0;i<10;i++)for(let j=0;j<10;j++)addTerm(G[i][j],v.key,v.w*BigInt(v.v[i]*v.v[j]));
 for(const v of f.F1){
  for(let i=0;i<6;i++)for(let j=0;j<6;j++)addTerm(S[i][j],v.key,v.w*BigInt(v.f[i]*v.f[j]));
  for(let i=0;i<6;i++)for(let j=0;j<4;j++)addTerm(M[i][j],v.key,v.w*BigInt(v.f[i]*v.b[j]));
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)addTerm(C[i][j],v.key,v.w*BigInt(v.b[i]*v.b[j]));
 }
 const same=(p,q)=>p.size===q.size&&[...p].every(([k,v])=>q.get(k)===v);
 for(const[B,adj,det]of[[A,aa.adj,aa.det],[C,cAdj.adj,cAdj.det],[G,gg.adj,gg.det]]){
  const check=matMul(B,adj);for(let i=0;i<B.length;i++)for(let j=0;j<B.length;j++)if(!same(check[i][j],i===j?det:zpoly()))throw Error("full adjugate identity");
 }
 const Mt=M[0].map((_,i)=>M.map(r=>r[i])),correction=matMul(matMul(M,cAdj.adj),Mt);
 for(let i=0;i<6;i++)for(let j=0;j<6;j++)if(!same(polyAcc(polyMul(cc.det,S[i][j]),correction[i][j],-1n),cc.K[i][j]))throw Error("middle Schur identity");
 const J=gg.adj.slice(0,6).map(r=>r.slice(0,6)),KJK=matMul(matMul(cc.K,J),cc.K),N=zpoly();
 for(let i=0;i<6;i++)for(let j=0;j<6;j++)polyAcc(N,polyMul(aa.adj[i][j],KJK[j][i]));
 const D=polyMul(polyMul(aa.det,polyMul(cc.det,cc.det)),gg.det);
 if(N.size!==D.size)throw Error("support mismatch");
 let min=null,minAt=null,maxExp=0,maxDegree=0;
 for(const[k,d]of D){
  const n=N.get(k);if(d<=0n||n===undefined||n<=0n)throw Error("positive coefficients");
  const gap=9n*d-4n*n;if(gap<=0n)throw Error("trace9/4 failed");
  const e=[1,32,1024,32768].map(s=>Math.floor(k/s)%32);
  if(min===null||gap<min){min=gap;minAt=e;}
  maxExp=Math.max(maxExp,...e);maxDegree=Math.max(maxDegree,e.reduce((a,b)=>a+b,0));
 }
 const counts=[aa.nd,aa.na,cc.nd,cc.nk,gg.nd,gg.na];
 if(D.size!==21202||min!==697143656448n||maxExp!==20||maxDegree!==67||counts.join(",")!=="303,423,940,2778,2068,4630")throw Error("certificate census changed");
 return{status:"PASS",scope:"four positive exceptional heads, three unit pool bits; fixed birth 2; n=1",
  conclusion:"trace(H0^-1 H1 H2^-1 H1)<9/4",
  coefficients:D.size,minimumGap:min.toString(),minimumAt:minAt,maxExp,maxDegree,maximumInputExponent,frameCounts:counts,
  identities:["A adjA=detA I","C adjC=detC I","G adjG=detG I","K=detC S-M adjC M^T"],
  trueNextConstraint:"F([4])=0, four affine lower parameters"};
}
const certificate=verifyFourHeadThreePoolLowEdge();
if(typeof console!=="undefined")console.log(JSON.stringify(certificate));
