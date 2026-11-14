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
function polyMul(a,b){const aa=exponentBounds(a),bb=exponentBounds(b);for(let i=0;i<4;i++){maximumInputExponent=Math.max(maximumInputExponent,aa[i]+bb[i]);if(aa[i]+bb[i]>30)throw Error("monomial exponent bound");}const c=zpoly();for(const[k,v]of a)for(const[l,w]of b)addTerm(c,k+l,v*w);return c;}
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
function q4BirthOneFrames(L){
 const steps=[1,32,1024,32768],pairs=[],triples=[];for(let mask=0;mask<16;mask++){const a=[];for(let i=0;i<4;i++)if(mask>>i&1)a.push(i);if(a.length===2)pairs.push(a);if(a.length===3)triples.push(a);}
 const F0=[],F1=[],F2=[];const d0=L,d1=L*(L-1),d2=d1*(L-2);
 for(let mask=0;mask<16;mask++){
  const b=Array.from({length:4},(_,i)=>mask>>i&1),r=b.reduce((a,c)=>a+c,0),key=b.reduce((a,c,i)=>a+c*steps[i],0);
  const f=triples.map(I=>I.every(i=>b[i])?1:0),quad=pairs.map(I=>I.every(i=>b[i])?1:0);
  if(r>=3)F0.push({mask,key,v:f,f,w:BigInt([L,1][r-3])});
  if(r>=2)F1.push({mask,key,v:quad,f,w:BigInt([d1,L-1,2][r-2])});
  if(r>=1)F2.push({mask,key,v:[...f,...b,...quad],f,w:BigInt([d2,(L-1)*(L-2),2*(L-2),6][r-1])});
 }return{F0,F1,F2,triples,pairs,d0,d1,d2};
}
const permutations=[];function permute4(a=[]){if(a.length===4){permutations.push([...a]);return;}for(let i=0;i<4;i++)if(!a.includes(i)){a.push(i);permute4(a);a.pop();}}permute4();
function symmetrizeGeneral(p,first,second,sets){
 const out=zpoly(),seen=new Set(),steps=[1,32,1024,32768],mon=[...p].map(([key,c])=>({e:steps.map(s=>Math.floor(key/s)%32),c}));
 const index=I=>{const s=I.slice().sort().join(",");return sets.findIndex(J=>J.join(",")===s);};
 for(const perm of permutations){const i=index(sets[first].map(a=>perm[a])),j=index(sets[second].map(a=>perm[a])),ij=i*sets.length+j;if(seen.has(ij))continue;seen.add(ij);
  for(const {e,c}of mon){let key=0;for(let a=0;a<4;a++)key+=e[a]*steps[perm[a]];addTerm(out,key,c);}
 }return{out,orbit:seen.size};
}
function evaluateBirthOneLowEdge(L){
 const f=q4BirthOneFrames(L),a=gramCB(f.F0,4),c=generalMiddleCB(f.F1,6,4),g=gramCB(f.F2,14,L===3?null:[0,1,2,3]);
 if(L===3){
  const A=zmatrix(4),G=zmatrix(14),S=zmatrix(4),M=zmatrix(4,6),C=zmatrix(6);
  for(const t of f.F0)for(let i=0;i<4;i++)for(let j=0;j<4;j++)addTerm(A[i][j],t.key,t.w*BigInt(t.f[i]*t.f[j]));
  for(const t of f.F2)for(let i=0;i<14;i++)for(let j=0;j<14;j++)addTerm(G[i][j],t.key,t.w*BigInt(t.v[i]*t.v[j]));
  for(const t of f.F1){
   for(let i=0;i<4;i++)for(let j=0;j<4;j++)addTerm(S[i][j],t.key,t.w*BigInt(t.f[i]*t.f[j]));
   for(let i=0;i<4;i++)for(let j=0;j<6;j++)addTerm(M[i][j],t.key,t.w*BigInt(t.f[i]*t.v[j]));
   for(let i=0;i<6;i++)for(let j=0;j<6;j++)addTerm(C[i][j],t.key,t.w*BigInt(t.v[i]*t.v[j]));
  }
  const ca=gramCB(f.F1,6),same=(x,y)=>x.size===y.size&&[...x].every(([k,v])=>y.get(k)===v);
  for(const[B,adj,det]of[[A,a.adj,a.det],[C,ca.adj,ca.det],[G,g.adj,g.det]]){
   const check=matMul(B,adj);for(let i=0;i<B.length;i++)for(let j=0;j<B.length;j++)if(!same(check[i][j],i===j?det:zpoly()))throw Error("full adjugate identity");
  }
  const Mt=M[0].map((_,i)=>M.map(r=>r[i])),corr=matMul(matMul(M,ca.adj),Mt);
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(!same(polyAcc(polyMul(c.det,S[i][j]),corr[i][j],-1n),c.K[i][j]))throw Error("six-parameter Schur identity");
 }
 const J=g.adj.slice(0,4).map(r=>r.slice(0,4));
 const KG=Array.from({length:4},zpoly);for(let j=0;j<4;j++)for(let k=0;k<4;k++)polyAcc(KG[j],polyMul(c.K[0][k],J[k][j]));
 const N=zpoly(),orbits=[];for(const j of [0,1]){const t=zpoly();for(let k=0;k<4;k++)polyAcc(t,polyMul(KG[k],c.K[k][j]));const z=symmetrizeGeneral(polyMul(a.adj[0][j],t),0,j,f.triples);polyAcc(N,z.out);orbits.push(z.orbit);}
 if(orbits.join(",")!=="4,12")throw Error("birth-one source orbits");
 
 if(L===3){
  const full=matMul(matMul(c.K,J),c.K),check=zpoly();
  for(let i=0;i<4;i++)for(let j=0;j<4;j++)polyAcc(check,polyMul(a.adj[i][j],full[j][i]));
  if(check.size!==N.size||[...check].some(([k,v])=>N.get(k)!==v))throw Error("S4 trace identity");
 }
 const D=polyMul(polyMul(a.det,polyMul(c.det,c.det)),g.det);
 let maxN=0n,maxD=1n,neg=0,missing=0;
 for(const[k,v]of N){const d=D.get(k)||0n;if(v<0n)neg++;if(!d&&v>0n)missing++;if(d&&v*BigInt(L-2)*maxD>maxN*d*BigInt(L-1)){maxN=v*BigInt(L-2);maxD=d*BigInt(L-1);}}
 return{N,D,metadata:{L,num:N.size,den:D.size,negative:neg,missing,maxRatio:Number(maxN)/Number(maxD),frames:[a.nd,a.na,c.nd,c.nk,g.nd,g.na]}};
}

function verifyBirthOneFirstLowEdge(){
 let keys=null;const columns=[],counts=[];let total=0,min=null,minAt=null;
 for(let order=0;order<=17;order++){
  const L=order+3,ll=BigInt(L),raw=evaluateBirthOneLowEdge(L);
  const nf=ll**8n*(ll-1n)**20n*(ll-2n)**12n;
  const df=ll**10n*(ll-1n)**19n*(ll-2n)**13n;
  const kk=[...new Set([...raw.N.keys(),...raw.D.keys()])].sort((a,b)=>a-b);
  if(keys===null)keys=kk;if(keys.length!==kk.length||keys.some((v,i)=>v!==kk[i]))throw Error("support");
  const col=keys.map(key=>{const n=raw.N.get(key)||0n,d=raw.D.get(key)||0n;if(n<0n||d<=0n)throw Error("raw positive coefficients");if(n%nf||d%df)throw Error("polynomial factor division");return 2n*ll*ll*(d/df)-n/nf;});
  for(let k=0;k<order;k++){
   let bin=1n;for(let j=1;j<=k;j++)bin=bin*BigInt(order+1-j)/BigInt(j);
   for(let i=0;i<col.length;i++)col[i]-=bin*columns[k][i];
  }
  let positive=0;
  for(let i=0;i<col.length;i++){
   if(col[i]<0n)throw Error("negative Newton coefficient");
   if(col[i]>0n){positive++;total++;if(min===null||col[i]<min){min=col[i];minAt={order,exponents:[1,32,1024,32768].map(s=>Math.floor(keys[i]/s)%32)};}}
  }
  if(order===0&&positive!==keys.length)throw Error("strict order zero");
  if(order>=16&&positive)throw Error("highest differences");
  columns.push(col);counts.push(positive);
 }
 const expected=[2286,2286,2286,1986,1650,1305,981,711,495,330,210,126,69,31,9,1,0,0];
 if(keys.length!==2286||total!==14762||min!==1536n||counts.join(",")!==expected.join(",")||maximumInputExponent!==24)throw Error("certificate census");
 return{status:"PASS",scope:"four positive exceptional heads, fixed birth one, first low edge n=1, all integer L>=3",
  conclusion:"trace(H0^-1 H1 H2^-1 H1)<2",
  degreeBound:16,headMonomials:keys.length,positiveNewtonCoefficients:total,counts,minimumPositive:min.toString(),minimumAt:minAt,
  maximumInputExponent,strictConstantTerms:2286,order16and17:"identically zero",
  fullIdentitiesAtL3:["A adjA=detA I","C adjC=detC I","G adjG=detG I","six-parameter middle Schur","S4 accelerated trace equals full matrix trace"]};
}
const certificate=verifyBirthOneFirstLowEdge();
if(typeof console!=="undefined")console.log(JSON.stringify(certificate));
