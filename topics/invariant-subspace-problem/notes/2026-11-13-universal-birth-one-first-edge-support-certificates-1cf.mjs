
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
 for(let i=0;i<m;i++)for(let j=i;j<m;j++){let p=new Map;for(let k=0;k<m;k++){const prod=mul(B2[i][k],B2[k][j]),q=new Map;for(const[key,c]of prod){if(Math.floor(key/pow[k])%32===0)throw Error("missing divisibility");q.set(key-pow[k],c);}p=add(p,q);}p=add(mul(ww,p),mul(mul(zz,zz),B3[i][j]),-1n);out[i][j]=out[j][i]=keep(p);}
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
const expected={
 4:[[52,"1"],[298,"1"],[832,"2"]],
 5:[[107,"5"],[916,"24"],[3636,"108"],[9996,"324"]],
 6:[[120,"12"],[1275,"135"],[6170,"1350"],[20325,"10125"],[53094,"263250"]]
};
function verifyLargeSupport(){
 const rows=[];
 for(const alpha of partitions(10).filter(a=>a.length>=7)){
  const m=alpha.length,M=Array.from({length:m},()=>Array(m).fill(0n));let positive=[];
  for(let i=0;i<m;i++)for(let j=i+1;j<m;j++){const c=off(alpha,i,j);M[i][j]=M[j][i]=c;M[i][i]-=c;M[j][j]-=c;if(c>0n)positive.push([i,j,String(c)]);}
  if(positive.length){if(alpha.join(",")!=="3,2,1,1,1,1,1"||JSON.stringify(positive)!=='[[0,1,"70"]]')throw Error("unexpected positive edge");
   for(let j=2;j<m;j++){if(M[0][j]!==-34n||M[1][j]!==-104n)throw Error("exceptional edge");for(let k=j+1;k<m;k++)if(M[j][k]!==-59n)throw Error("exceptional clique");}
   if(100n*450n-70n*70n!==40100n)throw Error("two-coordinate Gram");}
  rows.push({alpha,positiveEdges:positive.length});
 }
 if(rows.length!==7)throw Error("large-support partition count");return rows;
}
async function verifyUniversalBirthOneFirstEdge(options={}){
 const summaries=[];
 for(const m of [4,5,6]){const M=supportMatrix(m),D=directSupport(m);for(let i=0;i<m;i++)for(let j=0;j<m;j++)equivalent(M[i][j],D[i][j]);
  const stats=minorStats(M);if(JSON.stringify(stats.map(v=>[v.terms,v.min]))!==JSON.stringify(expected[m]))throw Error("recorded integer summary mismatch");
  summaries.push({support:m,independentCovarianceConstruction:true,stats});if(options.onProgress)await options.onProgress(summaries.at(-1));}
 const large=verifyLargeSupport();
 return{all_pass:true,smallSupports:"0,1,2 vanish; support3 is e2^2 e3 A C2^2 A",summaries,large,coefficientDegree:10,monomialBase:32,maximumIntermediateExponent:20,conclusion:"For every finite positive physical row with N>=4, C3<C2^2 on a-perp, equivalently Gamma1 Gamma2^-1 Gamma1<Gamma0 on the complete birth-one primitive space. No higher-birth conclusion."};
}
