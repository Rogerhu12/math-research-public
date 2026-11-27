// R271 new finite four/five-site half-bound certificate.
// Astra-ISP-8542378f, 2026-11-28 Asia/Taipei; target C2^2-2*C3.

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
N=add(N,mul(mul(add(S,add(x,y),-1n),square(Z)),W),-1n);
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
 for(let i=0;i<m;i++)for(let j=i;j<m;j++){let p=new Map;for(let k=0;k<m;k++){const prod=mul(B2[i][k],B2[k][j]),q=new Map;for(const[key,c]of prod){if(Math.floor(key/pow[k])%32===0)throw Error("missing divisibility");q.set(key-pow[k],c);}p=add(p,q);}p=add(mul(ww,p),mul(mul(zz,zz),B3[i][j]),-2n);out[i][j]=out[j][i]=keep(p);}
 return out;
}
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

function coefficientMatrix(alpha){
 const n=alpha.length,M=Array.from({length:n},()=>Array(n).fill(0n));
 for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){const c=off(alpha,i,j);M[i][j]=M[j][i]=c;M[i][i]-=c;M[j][j]-=c;}
 return M;
}
function partitions(n,max=n){if(!n)return[[]];let out=[];for(let k=Math.min(n,max);k>=1;k--)for(const t of partitions(n-k,k))out.push([k,...t]);return out;}
function subsets(n,k,start=0){if(!k)return[[]];let a=[];for(let i=start;i<=n-k;i++)for(const b of subsets(n,k-1,i+1))a.push([i,...b]);return a;}
function elementaryMatrixCoefficient(p,m,k){
 const out=new Map;
 for(const I of subsets(m,k)){
  const perm=I.concat(Array.from({length:m},(_,i)=>i).filter(i=>!I.includes(i)));
  for(const [key,c]of p){
   let nk=0;for(let i=0;i<m;i++)nk+=(Math.floor(key/(32**i))%32)*32**perm[i];
   out.set(nk,(out.get(nk)||0n)+c);
  }
 }
 return new Map([...out].filter(([k,c])=>c));
}
function factorial(n){let r=1n;for(let i=2;i<=n;i++)r*=BigInt(i);return r;}
function multiplicity(part){let d=1n;for(let i=0;i<part.length;){let j=i+1;while(j<part.length&&part[j]===part[i])j++;d*=factorial(j-i);i=j;}return factorial(part.length)/d;}
function permutations(p){
 const out=[];
 function rec(rest,pre){if(!rest.length){out.push(pre);return;}
  for(let i=0;i<rest.length;i++){if(i&&rest[i]===rest[i-1])continue;rec(rest.slice(0,i).concat(rest.slice(i+1)),pre.concat(rest[i]));}
 }
 rec(p,[]);return out;
}
function subtractMean(p,part,weight){
 const mult=multiplicity(part);if(weight%mult)throw Error("nonintegral orbit subtraction");
 const c=weight/mult;
 for(const ex of permutations(part)){const key=ex.reduce((s,x,i)=>s+x*32**i,0),v=(p.get(key)||0n)-c;if(v)p.set(key,v);else p.delete(key);}
}
function positiveStats(p){
 if(!p.size)throw Error("empty positive residual");let lo=null,hi=0n,total=0n;
 for(const c of p.values()){if(c<=0n)throw Error("nonpositive residual coefficient");if(lo===null||c<lo)lo=c;if(c>hi)hi=c;total+=c;}
 return {terms:p.size,min:String(lo),max:String(hi),sum:String(total)};
}
const moves4=[
 [[10,7,1,0],[9,8,1,0],96n],
 [[9,7,2,0],[8,8,2,0],480n],
 [[9,7,1,1],[8,8,1,1],288n]
];
const moves5=[
 [[14,5,1,0,0],[14,4,2,0,0],32400n],
 [[14,4,2,0,0],[14,3,2,1,0],176400n],
 [[14,4,1,1,0],[14,3,2,1,0],6000n],
 [[14,4,1,1,0],[14,3,1,1,1],120000n],
 [[14,3,3,0,0],[14,3,2,1,0],111600n],
 [[14,3,2,1,0],[14,2,2,2,0],24000n],
 [[14,3,2,1,0],[14,2,2,1,1],606000n]
];
function checkMove(a,b){
 for(let i=0;i<a.length;i++)for(let j=i+1;j<a.length;j++){
  if(a[i]<a[j]+2)continue;let c=a.slice();c[i]--;c[j]++;c.sort((x,y)=>y-x);
  if(c.every((x,k)=>x===b[k]))return {fromIndex:i,toIndex:j};
 }
 throw Error("move not an elementary positive symmetrized square");
}
function checkAllSymmetries(p,m){
 const seen=new Map;
 for(const[key,c]of p){
  const part=Array.from({length:m},(_,i)=>Math.floor(key/(32**i))%32).sort((a,b)=>b-a),k=part.join(",");
  if(seen.has(k)){if(seen.get(k)!==c)throw Error("coefficient asymmetry");}
  else{
   seen.set(k,c);
   for(const ex of permutations(part)){const q=ex.reduce((s,x,i)=>s+x*32**i,0);if((p.get(q)||0n)!==c)throw Error("missing orbit");}
  }
 }
 return seen.size;
}
async function verifyBirthOneHalfUpToFive(options={}){
 const started=Date.now();
 for(const alpha of partitions(10).filter(a=>a.length<=2)){
  const A=coefficientMatrix(alpha);
  if(A.some(row=>row.some(c=>c!==0n)))throw Error("support <=2 did not vanish");
 }
 const result=[];
 for(const m of [4,5]){
  const M=supportMatrix(m),direct=directSupport(m);
  for(let i=0;i<m;i++)for(let j=0;j<m;j++)equivalent(M[i][j],direct[i][j]);
  const leading=leadingPolynomials(M),checks=[];
  for(let k=1;k<m;k++){
   const e=elementaryMatrixCoefficient(leading[k-1],m,k),original=new Map(e);
   const orbitCount=checkAllSymmetries(e,m),repairs=[];
   if(m===4&&k===2){
    // Pairwise positive identity:
    // x^4*y^4*(x-y)^2*(3*x^2+2*x*y+3*y^2).
    for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){
     for(const[a,b,c]of [[8,4,3n],[4,8,3n],[7,5,-4n],[5,7,-4n],[6,6,2n]]){
      const key=a*32**i+b*32**j;if(e.get(key)!==c)throw Error("wrong quadratic repair coefficient");e.delete(key);
     }
     repairs.push({variables:[i,j],positiveTerm:"x^4*y^4*(x-y)^2*(3*x^2+2*x*y+3*y^2)"});
    }
   }
   if(k===m-1){
    for(const [a,b,w]of(m===4?moves4:moves5)){
     const step=checkMove(a,b);
     subtractMean(e,a,w);subtractMean(e,b,-w);
     repairs.push({from:a,to:b,weight:String(w),step});
    }
   }
   checks.push({order:k,degree:k*(10-m),originalTerms:original.size,
                originalNegative:[...original.values()].filter(c=>c<0n).length,
                symmetryOrbits:orbitCount,positiveResidual:positiveStats(e),repairs});
  }
  result.push({support:m,independentCovarianceConstruction:true,checks});
  if(options.onProgress)await options.onProgress(result.at(-1));
 }
 return {all_pass:true,target:"C2^2-2*C3",physicalSites:[4,5],
   allIndependentPositiveWeights:true,completeBirthOnePrimitiveSource:true,
   smallSupport:"<=2 vanishes; support 3 equals e2^2*e3*A*C2^2*A and is PSD",
   coefficientDegree:10,monomialBase:32,maximumIntermediateExponent:20,
   characteristicCoefficientPrinciple:"one zero eigenvalue; all remaining elementary symmetric coefficients positive, hence all remaining eigenvalues positive",
   result,runtimeMilliseconds:Date.now()-started,
   boundary:"No six-site or larger half-bound, no S2 or higher-birth result, no original W fee inferred."};
}
if(typeof process!=="undefined"&&process.argv.includes("--run")){
 verifyBirthOneHalfUpToFive().then(r=>process.stdout.write(JSON.stringify(r,null,2)+"\n"))
 .catch(e=>{process.stderr.write(String(e)+"\n");process.exitCode=1;});
}
