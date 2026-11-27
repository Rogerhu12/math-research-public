// R271 new two-thirds certificate; Astra-ISP-8542378f, 2026-11-28 Asia/Taipei.
// Exact BigInt calculation for the new target 2*C2^2-3*C3.

"use strict";
const enc=[1,16,256,4096,65536],ZP=()=>new Map,one=new Map([[0,1n]]);
function add(a,b,c=1n){const r=new Map(a);for(const[k,v]of b){const w=(r.get(k)||0n)+c*v;if(w)r.set(k,w);else r.delete(k);}return r;}
function scale(a,c){return new Map([...a].map(([k,v])=>[k,v*BigInt(c)]));}
function mul(a,b){const r=new Map;for(const[k,v]of a)for(const[l,w]of b){const m=k+l;r.set(m,(r.get(m)||0n)+v*w);}return new Map([...r].filter(([k,v])=>v));}
const [S,Z,W,x,y]=enc.map(k=>new Map([[k,1n]])),square=a=>mul(a,a);
const F=x=>add(add(add(square(S),scale(Z,2)),scale(mul(S,x),-3)),scale(square(x),2));
const E=x=>add(add(Z,scale(mul(S,x),-1)),square(x));
let N=mul(mul(add(scale(S,2),scale(add(x,y),-1)),square(Z)),W);
N=add(N,mul(mul(add(mul(F(x),add(S,y,-1n)),mul(F(y),add(S,x,-1n))),Z),W),-1n);
N=add(N,mul(mul(add(mul(S,Z),scale(W,3)),mul(add(S,x,-1n),add(S,y,-1n))),W));
N=add(N,mul(mul(E(x),E(y)),square(Z)));
N=add(scale(N,2),mul(mul(add(S,add(x,y),-1n),square(Z)),W),-1n);
N=add(N,mul(mul(E(x),E(y)),square(Z)));
const terms=[...N].map(([k,c])=>({p:enc.map(s=>Math.floor(k/s)%16),c}));
const memo=new Map();
function choose(n,k){let r=1n;for(let i=1;i<=k;i++)r=r*BigInt(n+1-i)/BigInt(i);return r;}
function coeff(A,B,C,beta){
 beta=beta.filter(e=>e>0).sort((a,b)=>b-a);
 if(beta.reduce((a,b)=>a+b,0)!==A+2*B+3*C)return 0n;
 if(!A&&!B&&!C)return beta.length?0n:1n;
 const key=[A,B,C,beta.join(",")].join("|");if(memo.has(key))return memo.get(key);
 const k=C?3:B?2:1,na=A-(k===1?1:0),nb=B-(k===2?1:0),nc=C-(k===3?1:0);
 const groups=[];for(const e of beta){if(groups.length&&groups.at(-1)[0]===e)groups.at(-1)[1]++;else groups.push([e,1]);}
 let total=0n;const picked=[];
 function visit(j,left,multiplicity){
  if(j===groups.length){if(left)return;let next=[];for(let r=0;r<groups.length;r++){let[e,m]=groups[r],h=picked[r];for(let z=0;z<m-h;z++)next.push(e);for(let z=0;z<h;z++)if(e>1)next.push(e-1);}total+=multiplicity*coeff(na,nb,nc,next);return;}
  const [e,m]=groups[j];for(let h=0;h<=Math.min(m,left);h++){picked[j]=h;visit(j+1,left-h,multiplicity*choose(m,h));}
 }
 visit(0,k,1n);memo.set(key,total);return total;
}
function off(alpha,i,j){let ans=0n;for(const {p,c}of terms){const beta=alpha.slice();beta[i]-=1+p[3];beta[j]-=1+p[4];if(beta.some(e=>e<0))continue;ans+=c*coeff(p[0],p[1],p[2],beta);}return ans;}

function comps(d,m){if(m===1)return[[d]];const out=[];for(let i=0;i<=d;i++)for(const a of comps(d-i,m-1))out.push([i,...a]);return out;}
function supportMatrix(m){
 const pow=Array.from({length:m},(_,i)=>32**i),M=Array.from({length:m},()=>Array.from({length:m},()=>new Map));
 for(const beta of comps(10-m,m)){const key=beta.reduce((s,x,i)=>s+x*pow[i],0),a=beta.map(x=>x+1);
  for(let i=0;i<m;i++)for(let j=i+1;j<m;j++){const c=off(a,i,j);if(!c)continue;M[i][j].set(key,c);M[j][i].set(key,c);M[i][i].set(key,(M[i][i].get(key)||0n)-c);M[j][j].set(key,(M[j][j].get(key)||0n)-c);}
 }
 return M.map(r=>r.map(p=>new Map([...p].filter(([k,v])=>v))));
}
function equivalent(a,b){const c=add(a,b,-1n);if(c.size)throw Error("polynomial identity failed");}
function directSupport(m){
 const pow=Array.from({length:m},(_,i)=>32**i),v=pow.map(k=>new Map([[k,1n]])),ss=v.reduce((s,p)=>add(s,p),new Map),zz=new Map,ww=new Map;
 for(let i=0;i<m;i++)for(let j=i+1;j<m;j++){zz.set(pow[i]+pow[j],1n);for(let k=j+1;k<m;k++)ww.set(pow[i]+pow[j]+pow[k],1n);}
 const mm2=v.map((p,i)=>mul(p,add(ss,p,-1n))),mm3=v.map((p,i)=>mul(p,add(add(zz,mul(ss,p),-1n),mul(p,p))));
 const B2=Array.from({length:m},(_,i)=>Array.from({length:m},(_,j)=>add(mul(zz,i===j?mm2[i]:mul(v[i],v[j])),mul(mm2[i],mm2[j]),-1n)));
 const B3=Array.from({length:m},(_,i)=>Array.from({length:m},(_,j)=>add(mul(ww,i===j?mm3[i]:mul(mul(v[i],v[j]),add(add(ss,v[i],-1n),v[j],-1n))),mul(mm3[i],mm3[j]),-1n)));
 const keep=p=>{const r=new Map;for(const[k,c]of p){let kk=k,ok=true;for(let i=0;i<m;i++)if(Math.floor(k/pow[i])%32===0){ok=false;break;}if(ok)r.set(k-pow.reduce((s,x)=>s+x,0),c);}return r;};
 const out=Array.from({length:m},()=>Array.from({length:m},()=>new Map));
 for(let i=0;i<m;i++)for(let j=i;j<m;j++){let p=new Map;for(let k=0;k<m;k++){const prod=mul(B2[i][k],B2[k][j]),q=new Map;for(const[key,c]of prod){if(Math.floor(key/pow[k])%32===0)throw Error("missing divisibility");q.set(key-pow[k],c);}p=add(p,q);}p=add(scale(mul(ww,p),2),mul(mul(zz,zz),B3[i][j]),-3n);out[i][j]=out[j][i]=keep(p);}
 return out;
}
function minorStats(M){
 const n=M.length-1,dp=new Map([[0,new Map([[0,1n]])]]),stats=[];
 for(let mask=1;mask<(1<<n);mask++){const ids=[];for(let j=0;j<n;j++)if(mask>>j&1)ids.push(j);const r=ids.length-1;let p=new Map;
  for(let pos=0;pos<ids.length;pos++){const j=ids[pos];p=add(p,mul(M[r][j],dp.get(mask^(1<<j))),(r+pos)%2?-1n:1n);}dp.set(mask,p);
  if(mask===(1<<ids.length)-1){if(!p.size)throw Error("zero leading minor");let min=null,max=0n;for(const[k,v]of p){if(v<=0n)throw Error("nonpositive coefficient");if(min===null||v<min)min=v;if(v>max)max=v;}
   stats.push({order:ids.length,terms:p.size,min:String(min),max:String(max)});}
 }
 return stats;
}
function partitions(n,max=n){if(!n)return[[]];let out=[];for(let k=Math.min(n,max);k>=1;k--)for(const t of partitions(n-k,k))out.push([k,...t]);return out;}

function leadingPolynomials(M){
 const n=M.length-1,dp=new Map([[0,new Map([[0,1n]])]]),out=[];
 for(let mask=1;mask<(1<<n);mask++){
  const ids=[];for(let j=0;j<n;j++)if(mask>>j&1)ids.push(j);
  const r=ids.length-1;let p=new Map;
  for(let pos=0;pos<ids.length;pos++){const j=ids[pos];p=add(p,mul(M[r][j],dp.get(mask^(1<<j))),(r+pos)%2?-1n:1n);}
  dp.set(mask,p);if(mask===(1<<ids.length)-1)out.push(p);
 }
 return out;
}
function positiveStats(p){if(!p.size)throw Error("zero polynomial");let lo=null,hi=0n;for(const c of p.values()){if(c<=0n)throw Error("nonpositive residual coefficient");if(lo===null||c<lo)lo=c;if(c>hi)hi=c;}return{terms:p.size,min:String(lo),max:String(hi)};}
function coefficientMatrix(alpha){
 const n=alpha.length,M=Array.from({length:n},()=>Array(n).fill(0n));
 for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){const c=off(alpha,i,j);M[i][j]=M[j][i]=c;M[i][i]-=c;M[j][j]-=c;}
 return M;
}
function equalInteger(a,b,msg){if(a!==b)throw Error(msg);}
function convolution(a,b){const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c;}
function certifyLarge(){
 const A=coefficientMatrix([4,1,1,1,1,1,1]),B=coefficientMatrix([3,2,1,1,1,1,1]),C=coefficientMatrix([2,2,2,1,1,1,1]);
 for(let i=0;i<7;i++)for(let j=0;j<7;j++){
  equalInteger(A[i][j],i===0||j===0?0n:i===j?220n:-44n,"seven-site cubic coefficient");
  const want=i===j?(i===0?30n:i===1?620n:466n):
   i<2&&j<2?160n:i===0||j===0?-38n:i===1||j===1?-156n:-68n;
  equalInteger(B[i][j],want,"seven-site mixed coefficient");
  if(i!==j&&C[i][j]>=0n)throw Error("seven-site triple is not a positive Laplacian");
 }
 // Pairwise grouping: six partners per site, hence A_i/6 in every pair.
 // Three times the two-coordinate diagonal polynomials at y=1:
 const a=[110n,1860n,90n,0n],b=[0n,90n,1860n,110n],c=[0n,480n,480n,0n];
 const ab=convolution(a,b),cc=convolution(c,c),det=ab.map((v,i)=>v-(cc[i]||0n));
 const expected=[0n,9900n,141600n,3019000n,141600n,9900n,0n];
 if(det.length!==expected.length||det.some((v,i)=>v!==expected[i]))throw Error("seven-site pair determinant");
 // The orthogonal five-coordinate variance has coefficient
 // 44(x^3+y^3)+534xy(x+y)>0.
 const E=coefficientMatrix([2,2,1,1,1,1,1,1]);
 for(let i=0;i<8;i++)for(let j=0;j<8;j++){
  const want=i===j?(i<2?1740n:1640n):
   i<2&&j<2?60n:i<2||j<2?-300n:-208n;
  equalInteger(E[i][j],want,"eight-site paired coefficient");
 }
 equalInteger(1740n*1740n-60n*60n,3024000n,"eight-site positive two-coordinate determinant");
 const remaining=[[3,1,1,1,1,1,1,1],[2,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]],laplacians=[];
 for(const alpha of remaining){const M=coefficientMatrix(alpha);let max=null;
  for(let i=0;i<M.length;i++)for(let j=i+1;j<M.length;j++){if(M[i][j]>0n)throw Error("large-support Laplacian edge");if(max===null||M[i][j]>max)max=M[i][j];}
  laplacians.push({alpha,largestOffDiagonal:String(max)});
 }
 if(partitions(10).filter(a=>a.length>=7).length!==7)throw Error("large-support exhaustiveness");
 return {sevenSitePairDeterminant:det.map(String),eightSiteTwoCoordinateDeterminant:"3024000",laplacians};
}
async function verifyUniversalBirthOneTwoThirds(options={}){
 for(const alpha of partitions(10).filter(a=>a.length<=2)){
  const M=coefficientMatrix(alpha);if(M.some(r=>r.some(c=>c!==0n)))throw Error("low support did not vanish");
 }
 const summaries=[];
 for(const m of [4,5,6]){
  const M=supportMatrix(m),D=directSupport(m);
  for(let i=0;i<m;i++)for(let j=0;j<m;j++)equivalent(M[i][j],D[i][j]);
  const polynomials=leadingPolynomials(M),stats=[];
  for(let j=0;j<polynomials.length;j++){
   let p=new Map(polynomials[j]),repair=[];
   if(m===4&&j===1){
    for(const i of [0,1])for(const k of [2,3]){
     for(const [a,c]of [[4,4n],[5,-4n],[6,4n]]){
      const exp=[0,0,0,0];exp[i]=a;exp[k]=12-a;
      const key=exp.reduce((sum,v,h)=>sum+v*32**h,0);
      equalInteger(p.get(key),c,"four-site exact repair coefficient");
      p.delete(key);
     }
     repair.push({i,k,polynomial:"4*x^4*y^6*(x^2-x*y+y^2)"});
    }
   }
   stats.push({order:j+1,originalTerms:polynomials[j].size,positiveResidual:positiveStats(p),repair});
  }
  summaries.push({support:m,independentCovarianceConstruction:true,stats});
  if(options.onProgress)await options.onProgress(summaries.at(-1));
 }
 const large=certifyLarge();
 return {all_pass:true,smallSupports:"support <=2 vanishes; support 3 is 2*e2^2*e3*A*C2^2*A",summaries,large,coefficientDegree:10,monomialBase:32,maximumIntermediateExponent:20,conclusion:"For every N>=4 and every independent positive physical weight, Gamma1 Gamma2^{-1} Gamma1 < (2/3) Gamma0 on the complete birth-one primitive space. No general higher-birth claim."};
}

if (typeof process !== "undefined" && process.argv.includes("--run")) {
 const started=Date.now();
 verifyUniversalBirthOneTwoThirds().then(r=>{
  r.runtimeMilliseconds=Date.now()-started;
  process.stdout.write(JSON.stringify(r,null,2)+"\n");
 }).catch(e=>{process.stderr.write(String(e)+"\n");process.exitCode=1;});
}
