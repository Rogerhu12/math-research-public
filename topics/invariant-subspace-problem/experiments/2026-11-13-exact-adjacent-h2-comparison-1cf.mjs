// Author: Astra-ISP-1cf8c51d; 2026-11-13. Diagnostic only; no universal bound is asserted.
function exactH2Comparison(weights0,gFloat){
const w=weights0.map(BigInt),n=w.length,s=2;
const abs=x=>x<0n?-x:x;function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;}
function R(a,b=1n){if(b===0n)throw Error("zero denominator");if(a===0n)return{n:0n,d:1n};if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return{n:a/g,d:b/g};}
const add=(a,b)=>R(a.n*b.d+b.n*a.d,a.d*b.d),sub=(a,b)=>R(a.n*b.d-b.n*a.d,a.d*b.d),mulI=(a,b)=>R(a.n*b,a.d);
function solve(A,b){const N=A.length,M=A.map((r,i)=>r.concat(b[i]));let prev=1n;for(let k=0;k<N-1;k++){if(!M[k][k]){let p=k+1;while(p<N&&!M[p][k])p++;if(p===N)throw Error("singular");[M[p],M[k]]=[M[k],M[p]];}const p=M[k][k];for(let i=k+1;i<N;i++){for(let j=k+1;j<=N;j++){const x=M[i][j]*p-M[i][k]*M[k][j];if(x%prev)throw Error("Bareiss remainder");M[i][j]=x/prev;}M[i][k]=0n;}prev=p;}const x=Array(N);for(let i=N-1;i>=0;i--){let q=R(M[i][N]);for(let j=i+1;j<N;j++)q=sub(q,mulI(x[j],M[i][j]));x[i]=R(q.n,q.d*M[i][i]);}return x;}
function sets(k){let a=[];function rec(m,i,left){if(!left){a.push(m);return;}for(let j=i;j<=n-left;j++)rec(m|1<<j,j+1,left-1);}rec(0,0,k);return a;}
const lev=[sets(1),sets(2),sets(3),sets(4)],idx=new Map(lev[1].map((m,i)=>[m,i])),g=Array(lev[1].length).fill(0n),P=w[1]*w[2];let sum=0n;
for(let i=1;i<n;i++)for(let j=i+1;j<n;j++)if(!(i===1&&j===2)){const at=idx.get((1<<i)|(1<<j)),b=BigInt(Math.round(gFloat[at]*1e15));g[at]=w[0]*P*b;sum+=w[i]*w[j]*b;}
g[idx.get(6)]=-w[0]*sum;
for(let i=1;i<n;i++){let v=0n;for(let j=1;j<n;j++)if(i!==j)v+=w[j]*g[idx.get((1<<i)|(1<<j))];if(v%w[0])throw Error("g denominator");g[idx.get(1|(1<<i))]=-v/w[0];}
const D=lev[0].map(I=>lev[1].map(J=>((I&J)===I)?w[Math.log2(I^J)]:0n)),dot=(a,b)=>a.reduce((z,x,i)=>z+x*b[i],0n),mv=(A,x)=>A.map(r=>dot(r,x)),tr=A=>A[0].map((_,j)=>A.map(r=>r[j])),mm=(A,B)=>{const T=tr(B);return A.map(r=>T.map(c=>dot(r,c)));};
if(mv(D,g).some(x=>x!==0n))throw Error("not primitive");
function gram(k){const A=Array.from({length:g.length},()=>Array(g.length).fill(0n));for(const J of lev[k+1]){let v=[];for(let i=0;i<g.length;i++){const I=lev[1][i];if((I&J)!==I)continue;let x=k===2?2n:1n;for(let j=0;j<n;j++)if((I^J)&1<<j)x*=w[j];v.push([i,x]);}for(const[i,x]of v)for(const[j,y]of v)A[i][j]+=x*y;}return A;}
const G1=gram(1),G2=gram(2),a=solve(G1,g);let den=1n;for(const q of a)den=den/gcd(den,q.d)*q.d;const av=a.map(q=>q.n*(den/q.d)),t=mv(G2,av),c=mv(D,t),B=mm(D,mm(G2,tr(D))),z=solve(B,c);let numerator=R(dot(av,t));for(let i=0;i<c.length;i++)numerator=sub(numerator,mulI(z[i],c[i]));
const denominator=den*den*dot(g,g),ratio=R(numerator.n,numerator.d*denominator);
function decimal(q){const a=abs(q.n).toString(),b=q.d.toString(),sign=q.n<0n?-1:1;const na=Math.min(a.length,16),nb=Math.min(b.length,16);return sign*Number(a.slice(0,na))/Number(b.slice(0,nb))*10**(a.length-na-b.length+nb);}
return{weights:weights0,ratio:decimal(ratio),comparisonTo4:ratio.n-4n*ratio.d>0n?"greater":ratio.n-4n*ratio.d===0n?"equal":"less",primitiveExact:true,ratioNumeratorDigits:ratio.n.toString().length,ratioDenominatorDigits:ratio.d.toString().length,g:g.map(String),ratioExact:{n:ratio.n.toString(),d:ratio.d.toString()}};
}
const report=exactH2Comparison(["1000000000000000000000000","0000649015592822944000000","0065669688263362040000000","0000835427294402596100000","0000333825094014337760000","0000950438917976352100000","0293269860935943870000000","0000269341732553237240000"],[-0.02876194970023078,0.00003247615548196235,-0.037027462679459944,-0.014791470479221965,-0.04216938303782512,0.00032645164819293055,-0.01207974434201543,0.4282577144950549,0.02059338650117397,0.008228000786223709,0.023436999032653522,0.002026724638255133,0.00666591585704923,0.5513613477044034,0.22023258818071564,0.628097335505439,-0.005080991343627271,0.18032679905414883,0.010591767121690871,0.030170055381845015,0.002631867770667565,0.008581407605814793,0.012054318421465447,0.0010307787855228494,0.0034271302626521297,0.0031537569492852144,-0.17418372489853812,0.0013320535630476497]);
if(!report.primitiveExact||report.comparisonTo4!=="less")throw new Error("Certificate verification failed");
console.log(JSON.stringify({ratio:report.ratio,comparisonTo4:report.comparisonTo4,primitiveExact:report.primitiveExact,ratioNumeratorDigits:report.ratioNumeratorDigits,ratioDenominatorDigits:report.ratioDenominatorDigits},null,2));
