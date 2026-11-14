// Exact actual Moore--Penrose low-edge certificate. All sign decisions use BigInt.
"use strict";

function q4CertificateFrames(L) {
 const STEPS=[1,64,4096,262144],pairs=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)pairs.push([i,j]);
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
function exponentBounds(p){if(boundCache.has(p))return boundCache.get(p);const z=[0,0,0,0];for(const k of p.keys())for(let i=0;i<4;i++)z[i]=Math.max(z[i],Math.floor(k/[1,64,4096,262144][i])%64);boundCache.set(p,z);return z;}
let maximumInputExponent=0;
function polyMul(a,b){const aa=exponentBounds(a),bb=exponentBounds(b);for(let i=0;i<4;i++){maximumInputExponent=Math.max(maximumInputExponent,aa[i]+bb[i]);if(aa[i]+bb[i]>44)throw Error("monomial exponent bound");}const c=zpoly();for(const[k,v]of a)for(const[l,w]of b)addTerm(c,k+l,v*w);return c;}
function polyAcc(a,b,s=1n){for(const[k,v]of b)addTerm(a,k,s*v);return a;}
function matMul(A,B){const C=zmatrix(A.length,B[0].length);for(let i=0;i<C.length;i++)for(let j=0;j<C[0].length;j++)for(let k=0;k<B.length;k++)polyAcc(C[i][j],polyMul(A[i][k],B[k][j]));return C;}

function generalMiddleCB(frames,p,q){
 const det=zpoly(),K=zmatrix(q);let nd=0,nk=0;
 eachComb(frames.length,p,I=>{const d=biDet(Array.from({length:p},(_,r)=>I.map(j=>frames[j].v[r])));if(!d)return;let key=0,w=d*d;for(const j of I){key+=frames[j].key;w*=frames[j].w;}addTerm(det,key,w);nd++;});
 eachComb(frames.length,p+1,I=>{
  const u=I.map((_,r)=>(r%2?-1n:1n)*biDet(Array.from({length:p},(_,s)=>I.filter((_,j)=>j!==r).map(j=>frames[j].v[s]))));
  const v=Array.from({length:q},(_,r)=>I.reduce((z,j,i)=>z+u[i]*BigInt(frames[j].f[r]),0n));if(v.every(x=>!x))return;
  let key=0,w=1n;for(const j of I){key+=frames[j].key;w*=frames[j].w;}for(let i=0;i<q;i++)for(let j=0;j<q;j++)addTerm(K[i][j],key,w*v[i]*v[j]);nk++;
 });return{det,K,nd,nk};
}
function q4BirthOneShortFrames(L,k){
 const sets={pairs:[],triples:[]};for(let mask=0;mask<16;mask++){const I=[];for(let i=0;i<4;i++)if(mask>>i&1)I.push(i);if(I.length===2)sets.pairs.push(I);if(I.length===3)sets.triples.push(I);}
 const steps=[1,64,4096,262144],frames=[];
 function choose(n,r){if(r<0||r>n)return 0;let z=1;for(let j=1;j<=r;j++)z=z*(n+1-j)/j;return z;}
 for(let mask=0;mask<16;mask++){
  const b=Array.from({length:4},(_,i)=>mask>>i&1),r=b.reduce((a,c)=>a+c,0),t=k+r-3;if(t<0||t>L)continue;
  const bc=b.map(x=>1-x),f=sets.triples.map(I=>I.every(i=>b[i])?1:0),q=sets.pairs.map(I=>I.every(i=>b[i])?1:0),fc=sets.triples.map(I=>I.every(i=>bc[i])?1:0),qc=sets.pairs.map(I=>I.every(i=>bc[i])?1:0);
  let v,u;
  if(k===0){v=f;u=[];}
  else if(k===1&&L>=2){v=f;u=q;}
  else if(k===1&&L===1){v=f.map(x=>x-q[5]);u=q.slice(0,5).map(x=>x-q[5]);}
  else if(k===2&&L>=3){v=f;u=[...b,...q];}
  else if(k===2&&L===2){v=f.map(x=>x-b[3]);u=[...b.slice(0,3).map(x=>x-b[3]),...q.map(x=>x-b[3])];}
  else if(k===2&&L===1){v=fc.map(x=>-x+qc[5]);u=qc.slice(0,5).map(x=>-x+qc[5]);}
  else if(k===3&&L===3){v=f.map(x=>x-b[3]);u=[1-b[3],...b.slice(0,3).map(x=>x-b[3]),...q.map(x=>x-b[3])];}
  else if(k===3&&L===2){v=fc.map(x=>-x);u=qc.map(x=>-x);}
  else if(k===3&&L===1){v=fc.map(x=>-x);u=[];}
  else throw Error("not a short case");
  frames.push({mask,key:b.reduce((s,x,i)=>s+x*steps[i],0),v:[...v,...u],f:v,low:u,w:BigInt(L/choose(L,t))});
 }return{frames,low:frames[0].low.length,sets};
}
function evaluateShortBirthOne(L,n){
 const prev=q4BirthOneShortFrames(L,n-1),mid=q4BirthOneShortFrames(L,n),next=q4BirthOneShortFrames(L,n+1);
 const a=gramCB(prev.frames,4+prev.low),c=generalMiddleCB(mid.frames.map(t=>({...t,v:t.low})),mid.low,4),g=gramCB(next.frames,4+next.low);
 const ca=gramCB(mid.frames.map(t=>({...t,v:t.low})),mid.low);
 const A=zmatrix(4+prev.low),G=zmatrix(4+next.low),S=zmatrix(4),M=zmatrix(4,mid.low),C=zmatrix(mid.low);
 for(const t of prev.frames)for(let i=0;i<A.length;i++)for(let j=0;j<A.length;j++)addTerm(A[i][j],t.key,t.w*BigInt(t.v[i]*t.v[j]));
 for(const t of next.frames)for(let i=0;i<G.length;i++)for(let j=0;j<G.length;j++)addTerm(G[i][j],t.key,t.w*BigInt(t.v[i]*t.v[j]));
 for(const t of mid.frames){
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)addTerm(S[i][j],t.key,t.w*BigInt(t.f[i]*t.f[j]));
  for(let i=0;i<4;i++)for(let j=0;j<mid.low;j++)addTerm(M[i][j],t.key,t.w*BigInt(t.f[i]*t.low[j]));
  for(let i=0;i<mid.low;i++)for(let j=0;j<mid.low;j++)addTerm(C[i][j],t.key,t.w*BigInt(t.low[i]*t.low[j]));
 }
 const same=(p,q)=>p.size===q.size&&[...p].every(([k,v])=>q.get(k)===v);
 for(const[B,adj,det]of[[A,a.adj,a.det],[C,ca.adj,ca.det],[G,g.adj,g.det]]){
  const check=matMul(B,adj);for(let i=0;i<B.length;i++)for(let j=0;j<B.length;j++)if(!same(check[i][j],i===j?det:zpoly()))throw Error("full adjugate identity");
 }
 const Mt=M[0].map((_,i)=>M.map(r=>r[i])),corr=matMul(matMul(M,ca.adj),Mt);
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(!same(polyAcc(polyMul(c.det,S[i][j]),corr[i][j],-1n),c.K[i][j]))throw Error("middle constrained Schur identity");
 const Jprev=a.adj.slice(0,4).map(r=>r.slice(0,4)),Jnext=g.adj.slice(0,4).map(r=>r.slice(0,4));
 const KJK=matMul(matMul(c.K,Jnext),c.K),N=zpoly();for(let i=0;i<4;i++)for(let j=0;j<4;j++)polyAcc(N,polyMul(Jprev[i][j],KJK[j][i]));
 const D=polyMul(polyMul(a.det,polyMul(c.det,c.det)),g.det);
 let maxN=0n,maxD=1n,neg=0,missing=0,minGap=null,negativeGap=0,zeroGap=0,maxExp=0,maxTotal=0;
 for(const k of new Set([...N.keys(),...D.keys()])){
  const v=N.get(k)||0n,d=D.get(k)||0n;if(v<0n)neg++;if(!d&&v>0n)missing++;if(d&&v*maxD>maxN*d){maxN=v;maxD=d;}
  const gap=3n*d-v;if(gap<0n)negativeGap++;else if(gap===0n)zeroGap++;else if(minGap===null||gap<minGap)minGap=gap;
  const ex=[1,64,4096,262144].map(s=>Math.floor(k/s)%64);maxExp=Math.max(maxExp,...ex);maxTotal=Math.max(maxTotal,ex.reduce((a,b)=>a+b,0));
 }
 return{N,D,summary:{L,n,low:[prev.low,mid.low,next.low],frames:[a.nd,a.na,c.nd,c.nk,g.nd,g.na],num:N.size,den:D.size,neg,missing,maxRatio:Number(maxN)/Number(maxD),negativeGap,zeroGap,minGap:minGap?.toString(),maxExp,maxTotal}};
}

function verifyBirthOneShortPools(){
 const cases=[[1,1,1980,9n],[2,1,2285,589824n],[2,2,5949,9437184n],[3,2,6254,1594323n]],results=[];
 for(const[L,n,count,minimum]of cases){
  const raw=evaluateShortBirthOne(L,n);let min=null,minAt=null,positive=0;
  for(const[k,d]of raw.D){
   const v=raw.N.get(k)||0n;if(d<=0n||v<0n)throw Error("raw coefficient signs");
   const gap=9n*d-4n*v;if(gap<=0n)throw Error("9/4 trace coefficient");
   positive++;if(min===null||gap<min){min=gap;minAt=[1,64,4096,262144].map(s=>Math.floor(k/s)%64);}
  }
  if([...raw.N.keys()].some(k=>!raw.D.has(k))||positive!==count||min!==minimum)throw Error("short certificate census");
  results.push({L,n,positiveCoefficients:positive,minimumGap:min.toString(),minimumAt:minAt,
   parameterDimensions:raw.summary.low,frameCounts:raw.summary.frames,maxExponent:raw.summary.maxExp,totalDegree:raw.summary.maxTotal});
 }
 if(maximumInputExponent!==28)throw Error("input exponent bound");
 return{status:"PASS",scope:"four exceptional positive heads; fixed birth one; all remaining short-pool edges",
  conclusion:"trace(H_(n-1)^-1 H_n H_(n+1)^-1 H_n)<9/4 for the four cases",
  results,maximumInputExponent,identities:"all full previous/middle-low/next adjugates and every exact constrained middle Schur"};
}
const certificate=verifyBirthOneShortPools();
if(typeof console!=="undefined")console.log(JSON.stringify(certificate));
