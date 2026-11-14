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

const headPermutations=[];function getPerms(a=[]){if(a.length===4){headPermutations.push([...a]);return;}for(let i=0;i<4;i++)if(!a.includes(i)){a.push(i);getPerms(a);a.pop();}}getPerms();
function symmetrizeEdgeTerm(p,first,second){
 const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]],pairIndex=p=>pairs.findIndex(q=>q[0]===Math.min(...p)&&q[1]===Math.max(...p)),seen=new Set(),out=zpoly(),steps=[1,32,1024,32768];
 const monomials=[...p].map(([key,c])=>({e:steps.map(s=>Math.floor(key/s)%32),c}));
 for(const perm of headPermutations){
  const i=pairIndex(pairs[first].map(x=>perm[x])),j=pairIndex(pairs[second].map(x=>perm[x])),ij=i*6+j;
  if(seen.has(ij))continue;seen.add(ij);
  for(const {e,c} of monomials){let key=0;for(let a=0;a<4;a++)key+=e[a]*steps[perm[a]];addTerm(out,key,c);}
 }
 return{out,orbit:seen.size};
}
function evaluateQ4TraceSymmetric(L){
 const f=q4CertificateFrames(L),a=gramCB(f.F0,6),c=middleCB(f.F1),g=gramCB(f.F2,11,[0,1,2,3,4,5]);
 const KG=Array.from({length:6},zpoly);
 for(let j=0;j<6;j++)for(let k=0;k<6;k++)polyAcc(KG[j],polyMul(c.K[0][k],g.adj[k][j]));
 const N=zpoly(),orbits=[];
 for(const j of [0,1,5]){
  const t=zpoly();for(let k=0;k<6;k++)polyAcc(t,polyMul(KG[k],c.K[k][j]));
  const p=polyMul(a.adj[0][j],t),sym=symmetrizeEdgeTerm(p,0,j);polyAcc(N,sym.out);orbits.push(sym.orbit);
 }
 if(orbits.join(",")!=="6,24,6")throw Error("S4 ordered edge orbits");
 const D=polyMul(polyMul(a.det,polyMul(c.det,c.det)),g.det);
 
 if(L===4){
  const full=matMul(matMul(c.K,g.adj),c.K),Nfull=zpoly();
  for(let i=0;i<6;i++)for(let j=0;j<6;j++)polyAcc(Nfull,polyMul(a.adj[i][j],full[j][i]));
  if(N.size!==Nfull.size||[...N].some(([k,v])=>Nfull.get(k)!==v))throw Error("S4 trace disagrees with full trace");
 }
 return{N,D};

}

function binomialBig(n,k){let z=1n;for(let j=1;j<=k;j++)z=z*BigInt(n+1-j)/BigInt(j);return z;}

// The loop is finite because the independently proved degree bound is 37.
// n=38 is a redundant exact consistency check, not a substitute for that bound.
async function verifyFourHeadAllPoolsLowEdge(options={}){
 const progress=options.onProgress??(async()=>{}),columns=[],counts=[];
 let keys=null,totalPositive=0,minPositive=null,minAt=null;
 for(let order=0;order<=38;order++){
  const L=order+4,ll=BigInt(L),raw=evaluateQ4TraceSymmetric(L);
  const nf=ll*(ll-1n)**4n*(ll-2n)**13n*(ll-3n)**9n;
  const df=ll**2n*(ll-1n)**5n*(ll-2n)**12n*(ll-3n)**10n;
  const thisKeys=[...new Set([...raw.N.keys(),...raw.D.keys()])].sort((a,b)=>a-b);
  if(keys===null)keys=thisKeys;
  if(keys.length!==thisKeys.length||keys.some((k,i)=>k!==thisKeys[i]))throw Error("head monomial support changed");
  const column=keys.map(k=>{
   const n=raw.N.get(k)||0n,d=raw.D.get(k)||0n;
   if(n<=0n||d<=0n)throw Error("positive raw coefficients");
   if(n%nf||d%df)throw Error("inexact common polynomial factor");
   return 3n*ll*(ll-1n)*(d/df)-n/nf;
  });
  for(let k=0;k<order;k++){
   const c=binomialBig(order,k);
   for(let j=0;j<keys.length;j++)column[j]-=c*columns[k][j];
  }
  let positive=0,zero=0;
  for(let j=0;j<column.length;j++){
   const c=column[j];if(c<0n)throw Error("negative Newton coefficient");
   if(c===0n){zero++;continue;}
   positive++;if(order<=37){totalPositive++;if(minPositive===null||c<minPositive){minPositive=c;minAt={order,exponents:[1,32,1024,32768].map(s=>Math.floor(keys[j]/s)%32)};}}
  }
  if(order===0&&positive!==keys.length)throw Error("strict constant term");
  if(order>=37&&positive!==0)throw Error("unexpected highest differences");
  columns.push(column);counts.push(positive);
  await progress({pool:L,order,positive,zero});
 }
 const expected=[21251,21251,21251,21171,21031,20815,20506,20086,19536,18836,17965,16961,15841,14625,13336,12000,10646,9306,8015,6811,5705,4705,3816,3040,2376,1820,1365,1001,715,495,330,210,126,69,31,5,1,0,0];
 if(keys.length!==21251||counts.join(",")!==expected.join(",")||totalPositive!==357050||minPositive!==36691771392n||maximumInputExponent!==21)throw Error("certificate census changed");
 return{status:"PASS",scope:"q=4, relative birth 2, all integer unit-pool lengths L>=4, low edge n=1",
  conclusion:"trace(H0^-1 H1 H2^-1 H1)<3",
  degreeBound:37,headMonomials:keys.length,positiveNewtonCoefficients:totalPositive,
  positiveCounts:counts,minimumPositive:minPositive.toString(),minimumAt:minAt,
  maximumInputExponent,strictConstantTerms:21251,order37and38:"identically zero",
  symmetryCheck:"S4 orbit evaluation equals full matrix trace at L=4"};
}

// Standalone Node usage: node this-file.mjs
// Tool use: obtain verifyFourHeadAllPoolsLowEdge via Function, then await it;
// onProgress may yield after each finite sample.
if(typeof process!=="undefined"&&process.versions?.node&&typeof console!=="undefined"){
 verifyFourHeadAllPoolsLowEdge({onProgress:async v=>{if(v.order%5===0)console.log(JSON.stringify(v));}})
 .then(v=>console.log(JSON.stringify(v))).catch(e=>{console.error(e);process.exitCode=1;});
}
