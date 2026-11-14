// R604: exact original S/T staircase minor and genuine-prefix boundary.
// No external dependency. This is not a scan for arithmetic nonvanishing.
function build(N){

const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
const q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]};
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]),sc=(a,n,d=1)=>mul(a,q(n,d));
const A=Array.from({length:N+1},()=>q(0)),L=Array.from({length:N+1},()=>q(0)),S=Array.from({length:N+1},()=>q(0));A[0]=q(1);S[0]=q(1);if(N)A[1]=q(-1,7);
for(let n=2;n<=N;n++){let s=q(0);for(let j=1;j<n;j++)s=add(s,mul(A[j],A[n-j]));A[n]=sc(s,1,(6*n+1)*(n-1))}
for(let n=1;n<=N;n++)L[n]=sc(A[n],-1,n*(6*n-1));
for(let n=1;n<=N;n++){let s=q(0);for(let j=1;j<=n;j++)s=add(s,sc(mul(L[j],S[n-j]),j));S[n]=sc(s,1,n)}
const AS=Array.from({length:N+1},()=>q(0)),ABS=Array.from({length:N+1},()=>q(0));
for(let n=0;n<=N;n++)for(let j=0;j<=n;j++)AS[n]=add(AS[n],mul(A[j],S[n-j]));
for(let n=0;n<=N;n++)for(let j=0;j<=n;j++)ABS[n]=add(ABS[n],sc(mul(A[j],AS[n-j]),1-3*j));
return {A,L,S,AS,ABS};
}


function certificate(data) {
const p=23, s=4, M=15, maxDegree=6;
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const qa=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const qm=(a,b)=>q(a[0]*b[0],a[1]*b[1]);
const qs=(a,n,d=1n)=>qm(a,q(n,d));
const zero=()=>Array.from({length:M+1},()=>q(0));
const cst=c=>{const f=zero();f[0]=q(c);return f};
const add=(a,b)=>a.map((v,i)=>qa(v,b[i]));
const scale=(a,n,d=1n)=>a.map(v=>qs(v,n,d));
function mul(a,b){const f=zero();for(let i=0;i<=M;i++)if(a[i][0])for(let j=0;i+j<=M;j++)if(b[j][0])f[i+j]=qa(f[i+j],qm(a[i],b[j]));return f}
function pow(a,n){let f=cst(1);for(;n;n>>=1,a=mul(a,a))if(n&1)f=mul(f,a);return f}
function inv(a){const f=zero();f[0]=q(a[0][1],a[0][0]);for(let n=1;n<=M;n++){let v=q(0);for(let j=1;j<=n;j++)v=qa(v,qm(a[j],f[n-j]));f[n]=qs(qm(v,f[0]),-1)}return f}
function exp(a){const f=cst(1);for(let n=1;n<=M;n++){let v=q(0);for(let j=1;j<=n;j++)v=qa(v,qs(qm(a[j],f[n-j]),j));f[n]=qs(v,1,n)}return f}
const mod=x=>Number((BigInt(x)%BigInt(p)+BigInt(p))%BigInt(p));
function mp(a,n){a=mod(a);let r=1;for(;n;n>>=1,a=a*a%p)if(n&1)r=r*a%p;return r}
const mi=a=>mp(a,p-2);
function red(a){if(a[1]%BigInt(p)===0n)throw Error("nonintegral actual coefficient");return mod(a[0])*mi(mod(a[1]))%p}
function fact(n){let f=1n;for(let j=1;j<=n;j++)f*=BigInt(j);return f}
let checks=0;
function check(a,b,label){checks++;if(a!==b)throw Error(label+": "+a+" != "+b)}
const w=zero();w[1]=q(1);
const A=data.A,L=data.L;
const theta=mul(A,exp(scale(L,1,3)));
const t=scale(mul(w,pow(inv(A),3)),-1),t2=pow(t,2),t3=pow(t,3);
const f=scale(mul(mul(mul(t,add(t,cst(-1))),add(add(scale(t2,16),scale(t,4)),cst(7))),add(cst(1),scale(t,8))),1,7);
const V=mul(mul(add(cst(1),scale(t,-4)),add(add(cst(1),scale(t,-20)),scale(t2,-8))),add(add(add(cst(1),scale(t,96)),scale(t2,48)),scale(t3,-64)));
const S=mul(pow(theta,17),f),T=mul(pow(theta,36),mul(f,V));
check(red(S[1]),1,"actual S leading coefficient");
check(red(T[1]),1,"actual T leading coefficient");
const betaH=qa(T[2],qs(S[2],-1));
check(String(betaH),String(q(-1118,15)),"exact E1 three-row determinant");
const pc=red(qs(L[s],p,6));

function detMod(input) {
 const A=input.map(row=>row.slice());let det=1;
 for(let j=0;j<A.length;j++){
  let pivot=j;while(pivot<A.length&&A[pivot][j]===0)pivot++;
  if(pivot===A.length)return 0;
  if(pivot!==j){[A[pivot],A[j]]=[A[j],A[pivot]];det=mod(-det)}
  const v=A[j][j];det=mod(det*v);
  for(let i=j+1;i<A.length;i++){const c=mod(A[i][j]*mi(v));for(let k=j;k<A.length;k++)A[i][k]=mod(A[i][k]-c*A[j][k])}
 }
 return det;
}
function detRational(input){
 const A=input.map(row=>row.slice());let det=q(1);
 for(let j=0;j<A.length;j++){
  let pivot=j;while(pivot<A.length&&A[pivot][j][0]===0n)pivot++;
  if(pivot===A.length)return q(0);
  if(pivot!==j){[A[pivot],A[j]]=[A[j],A[pivot]];det=qs(det,-1)}
  const v=A[j][j];det=qm(det,v);
  for(let i=j+1;i<A.length;i++){
   const c=qm(A[i][j],q(v[1],v[0]));
   for(let k=j;k<A.length;k++)A[i][k]=qa(A[i][k],qs(qm(c,A[j][k]),-1));
  }
 }
 return det;
}
function valuation(qv){if(!qv[0])return null;let a=abs(qv[0]),b=qv[1],v=0;while(a%BigInt(p)===0n){a/=BigInt(p);v++}while(b%BigInt(p)===0n){b/=BigInt(p);v--}return v}
const frames=[];
for(const b0 of [1,17])for(let D=1;D<=3;D++){
 const cols=[],rows=[];
 for(let d=0;d<=D;d++)for(let v=0;v<=d;v++){
  cols.push({degree:d,mu:d-v,nu:v,P:mul(pow(S,d-v),pow(T,v))});
  rows.push({q:d,h:v,n:v*s+d});
 }
 const actual=(col,n)=>n<col.degree?q(0):qs(col.P[n],BigInt(b0)**BigInt(n-col.degree));
 const matrix=rows.map(row=>cols.map(col=>red(qs(actual(col,row.n),BigInt(p)**BigInt(row.h)*fact(row.h)))));
 const zeta=mod(pc*mp(b0,s)),beta=mod(38*zeta);
 for(let i=0;i<rows.length;i++)for(let j=0;j<cols.length;j++){
  const row=rows[i],col=cols[j];
  if(col.degree>row.q)check(matrix[i][j],0,"actual block triangular zero");
  if(col.degree===row.q){
   const gamma=mod(zeta*(34*row.q+38*col.nu));
   check(matrix[i][j],mp(gamma,row.h),"actual diagonal Vandermonde");
  }
 }
 const exponent=D*(D+1)*(D+2)/6;
 let expected=mp(beta,exponent);
 for(let j=1;j<=D;j++)expected=mod(expected*mp(Number(fact(j)%BigInt(p)),D-j+1));
 const determinant=detMod(matrix);
 check(determinant,expected,"full exact original staircase determinant");
 if(!determinant)throw Error("nonunit staircase determinant");
 const rawMinor=detRational(rows.map(row=>cols.map(col=>actual(col,row.n))));
 check(valuation(rawMinor),-exponent,"exact unscaled selected determinant valuation");
 const consecutiveMinor=detRational(Array.from({length:cols.length},(_,n)=>cols.map(col=>actual(col,n))));
 if(!consecutiveMinor[0])throw Error("chosen low-degree consecutive check singular");
 const rowCount=rows.filter(row=>row.n<D*(s+1)+1).length;
 check(rowCount,cols.length,"all selected rows occur before exact empty-prefix bound");
 frames.push({p,b:b0,D,columns:cols.map(({P,...col})=>col),selected_rows:rows,
 normalized_matrix:matrix,normalized_det:determinant,formula_det:expected,
 raw_selected_det_valuation:valuation(rawMinor),
 consecutive_prefix_size:cols.length,
 consecutive_prefix_det_valuation:valuation(consecutiveMinor),
 exact_prefix_bound:D*(s+1)+1});
}
return {status:"all exact checks passed",checks,previous_analytic_prime_only:true,frames,
 full_D_proof_uses_R600_actual_source_rows:true,
 exact_selected_minor_not_identified_with_saturated_flag_cost:true,
 all_noncentral_prefix_rows_preserved:true,no_central_nonvanishing_claim:true,main_target_complete:false};
}
console.log(JSON.stringify(certificate(build(15)),null,2));
