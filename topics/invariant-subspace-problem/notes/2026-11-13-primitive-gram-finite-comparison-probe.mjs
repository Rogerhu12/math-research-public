// Exact rational finite primitive-Gram probe. No external packages.
// The refined inequality is false: the final default case is a known exact counterexample.
const exactPrimitiveGram = function(inputWeights,s,nmax=3,refined=true){
 function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
 class Q{constructor(n,d=1n){if(d===0n)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}add(v){return new Q(this.n*v.d+v.n*this.d,this.d*v.d);}sub(v){return new Q(this.n*v.d-v.n*this.d,this.d*v.d);}mul(v){return new Q(this.n*v.n,this.d*v.d);}div(v){return new Q(this.n*v.d,this.d*v.n);}neg(){return new Q(-this.n,this.d);}str(){return this.d===1n?String(this.n):String(this.n)+"/"+String(this.d);}}
 const zero=new Q(0n),one=new Q(1n),a=inputWeights.map(x=>BigInt(x)),N=a.length;
 function mat(r,c){return Array.from({length:r},()=>Array.from({length:c},()=>zero));}
 function subs(k){const out=[];function rec(st,x){if(x.length===k){out.push(x.slice());return;}for(let j=st;j<=N-k+x.length;j++){x.push(j);rec(j+1,x);x.pop();}}rec(0,[]);return out;}
 if(!Number.isInteger(s)||s<0||!Number.isInteger(nmax)||nmax<1||nmax>N-2*s||a.some(x=>x<=0n))throw Error("require positive integer weights and 0<=s, 1<=nmax<=N-2s");
 const basis=subs(s),low=s===0?[]:subs(s-1),M=basis.length,sets=basis.map(x=>new Set(x)),lowMap=new Map(low.map((x,i)=>[x.join(","),i])),D=mat(low.length,M);
 for(let j=0;j<M;j++)for(let t=0;t<s;t++){const x=basis[j].slice(),i=x.splice(t,1)[0];D[lowMap.get(x.join(","))][j]=new Q(a[i]);}
 const piv=[];let row=0;
 for(let j=0;j<M&&row<D.length;j++){let p=row;while(p<D.length&&D[p][j].n===0n)p++;if(p===D.length)continue;[D[p],D[row]]=[D[row],D[p]];const v=D[row][j];for(let k=j;k<M;k++)D[row][k]=D[row][k].div(v);for(let i=0;i<D.length;i++)if(i!==row&&D[i][j].n!==0n){const z=D[i][j];for(let k=j;k<M;k++)D[i][k]=D[i][k].sub(z.mul(D[row][k]));}piv.push(j);row++;}
 if(row!==low.length)throw Error("low rank");
 const free=Array.from({length:M},(_,i)=>i).filter(i=>!piv.includes(i)),d=free.length,K=mat(M,d);
 for(let j=0;j<d;j++){K[free[j]][j]=one;for(let i=0;i<piv.length;i++)K[piv[i]][j]=D[i][free[j]].neg();}
 function solve(A,B){const n=A.length,k=B[0].length,C=A.map((r,i)=>r.slice().concat(B[i]));
  for(let j=0;j<n;j++){let p=j;while(p<n&&C[p][j].n===0n)p++;if(p===n)throw Error("singular Gram");if(p!==j)[C[p],C[j]]=[C[j],C[p]];const v=C[j][j];for(let u=j;u<n+k;u++)C[j][u]=C[j][u].div(v);for(let i=0;i<n;i++)if(i!==j&&C[i][j].n!==0n){const z=C[i][j];for(let u=j;u<n+k;u++)C[i][u]=C[i][u].sub(z.mul(C[j][u]));}}
  return C.map(r=>r.slice(n));}
 function compress(X){const G=mat(d,d);for(let i=0;i<d;i++)for(let j=0;j<=i;j++){let z=zero;for(let k=0;k<M;k++)z=z.add(K[k][i].mul(X[k][j]));G[i][j]=G[j][i]=z;}return G;}
 const G=[compress(K)];
 for(let n=1;n<=nmax;n++){const F=mat(M,M);
  for(let i=0;i<M;i++)for(let j=0;j<=i;j++){const union=new Set([...basis[i],...basis[j]]),h=union.size-s;let z=0n;if(h<=n){let f=1n;for(const x of basis[i])if(!sets[j].has(x))f*=a[x];for(const x of basis[j])if(!sets[i].has(x))f*=a[x];const e=Array(n-h+1).fill(0n);e[0]=1n;for(let k=0;k<N;k++)if(!union.has(k))for(let t=e.length-1;t>=1;t--)e[t]+=a[k]*a[k]*e[t-1];z=f*e[n-h];}F[i][j]=F[j][i]=new Q(z);}
  G.push(compress(solve(F,K)));
 }
 const checks=[];
 for(let n=1;n<nmax;n++){
  const factor=refined?new Q(BigInt((s+n)*(N-2*s-n)),BigInt((s+n+1)*(N-2*s-n+1))):one;
  const X=solve(G[n+1],G[n]),A=mat(d,d);
  for(let i=0;i<d;i++)for(let j=0;j<=i;j++){let v=G[n-1][i][j].mul(factor);for(let k=0;k<d;k++)v=v.sub(G[n][i][k].mul(X[k][j]));A[i][j]=A[j][i]=v;}
  const L=mat(d,d);let status="positive";const pivots=[];
  for(let j=0;j<d;j++){let p=A[j][j];for(let k=0;k<j;k++)p=p.sub(L[j][k].mul(L[j][k]).mul(pivots[k]));pivots.push(p);L[j][j]=one;
   if(p.n<0n){status="negative";const v=Array.from({length:d},()=>zero);v[j]=one;for(let k=j-1;k>=0;k--){let z=zero;for(let t=k+1;t<=j;t++)z=z.add(L[t][k].mul(v[t]));v[k]=z.neg();}
    checks.push({n,factor:factor.str(),status,pivot:j,quadratic:p.str(),vector:v.map(x=>x.str())});break;}
   if(p.n===0n){status="zero_pivot";checks.push({n,factor:factor.str(),status,pivot:j});break;}
   for(let i=j+1;i<d;i++){let z=A[i][j];for(let k=0;k<j;k++)z=z.sub(L[i][k].mul(L[j][k]).mul(pivots[k]));L[i][j]=z.div(p);}
  }
  if(status==="positive")checks.push({n,factor:factor.str(),status,lastPivotDigits:pivots.at(-1).n.toString().length+"/"+pivots.at(-1).d.toString().length});
 }
 return {weights:inputWeights,s,nmax,sourceDimension:M,primitiveDimension:d,refined,checks};
};

const cases = [
 [[100,100,1,1,1,1,1],2,3],
 [[100,90,10,10,1,1,1],2,3],
 [[1000,100,10,1,1,1,1],2,3],
 [[100,97,31,7,3,2,1],2,3],
 [[100,1,1,1,1,1,1],1,4],
 [[3,3,3,3,3,1,1],2,3]
];
for (const [weights,s,nmax] of cases) {
 console.log(JSON.stringify(exactPrimitiveGram(weights,s,nmax,true)));
}
