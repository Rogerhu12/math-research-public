// R607: exact integral target presentation, complete Euler images, and actual mixed Schur lattice.
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

function factMod(n){return mod(fact(n))}
function rankMod(input){
 const a=input.map(r=>r.slice());let rank=0;
 if(!a.length)return 0;
 for(let j=0;j<a[0].length&&rank<a.length;j++){
  let z=rank;while(z<a.length&&a[z][j]===0)z++;if(z===a.length)continue;
  [a[z],a[rank]]=[a[rank],a[z]];const inv=mi(a[rank][j]);
  a[rank]=a[rank].map(x=>mod(x*inv));
  for(let i=0;i<a.length;i++)if(i!==rank){const c=a[i][j];a[i]=a[i].map((x,k)=>mod(x-c*a[rank][k]))}
  rank++;
 }
 return rank;
}
const ringFrames=[];
for(const pp of [17,23]){
 const ss=(pp+1)/6,nn=pp*ss;
 const normal=n=>{const j=Math.floor(n/pp),v=n-j*pp,t=Math.floor(v/ss),r=v-t*ss;return{j,t,r}};
 function reduce(r,t,j){
  let exponent=0;
  for(let turns=0;turns<4*nn;turns++){
   if(j>=ss)return null;
   if(t>=6){t-=6;r++;j++;continue}
   if(r>=ss){r-=ss;t++;exponent++;continue}
   if(r===ss-1&&t===5){r=0;t=0;j++;exponent++;continue}
   return {r,t,j,exponent,n:j*pp+t*ss+r};
  }
  throw Error("normal form did not terminate");
 }
 const seen=new Set;
 for(let j=0;j<ss;j++)for(let t=0;t<=5;t++)for(let r=0;r<ss;r++){
  if(t===5&&r===ss-1)continue;
  const n=j*pp+t*ss+r;check(seen.has(n),false,"distinct physical normal form");seen.add(n);
  check(Math.floor(6*n/pp),6*j+t,"physical exponent in integral basis");
 }
 check(seen.size,nn,"full torsion-free basis cardinality");
 let multiplication=0;
 for(let n=0;n<nn;n++)for(let m=0;m<nn;m++){
  const a=normal(n),b=normal(m),out=reduce(a.r+b.r,a.t+b.t,a.j+b.j);
  if(n+m>=nn)check(out,null,"complete physical truncation");
  else{
   check(out.n,n+m,"all physical multiplication exponents");
   check(out.exponent,Math.floor(6*(n+m)/pp)-Math.floor(6*n/pp)-Math.floor(6*m/pp),"all actual p carries");
  }
  multiplication++;
 }
 ringFrames.push({p:pp,s:ss,rank:nn,all_ordered_basis_products:multiplication});
}
const sourceFrames=[];
for(const b0 of [1,17]){
 const am=mod(6*pc*mp(b0,s));
 const greens={4:data.AS.slice(0,s).map((x,r)=>red(qs(x,BigInt(b0)**BigInt(r)))),
               1:data.ABS.slice(0,s).map((x,r)=>red(qs(x,BigInt(b0)**BigInt(r))))};
 const sourceRows=[];
 for(const ell of [4,1])for(let h=0;h<=(ell===4?1:4);h++){
  const gg=greens[ell],tag=ell===4?"AS":"ABS";
  const actual=[],predicted=Array(p*s).fill(0),gamma=Array(s).fill(0);
  for(let n=0;n<p*s;n++){
   const value=n===0?q(0):qs(data[tag][n-1],BigInt(b0)**BigInt(n-1),6*n-h);
   actual.push(red(qs(value,BigInt(p)**BigInt(Math.floor(6*n/p)))));
  }
  for(let u=1;u<s;u++)for(let L=0;L+6*u<p;L++){
   const n=L*s+u;
   predicted[n]=mod(mp(am,L)*gg[u-1]*mi(factMod(L))*mi(L+6*u-h));
  }
  for(let j=(h===0?1:0);j<s;j++){
   const c=mod(mp(am,6*j+h-1)*gg[s-1-j]*mi(factMod(6*j+h)));
   gamma[j]=c;predicted[j*p+h*s]=mod(predicted[j*p+h*s]+c);
  }
  for(let n=0;n<p*s;n++)check(actual[n],predicted[n],"complete actual Euler source image");
  check(gamma[0],h===0?0:mod(mp(am,h-1)*gg[s-1]*mi(factMod(h))),"forcing is original resonant constant");
  sourceRows.push({ell,h,gamma,complete_integral_image:actual});
 }
 for(const ell of [4,1]){
  const tag=ell===4?"AS":"ABS",gg=greens[ell];
  for(let n=0;n<p*s;n++){
   const raw=n===0?q(0):qs(data[tag][n-1],BigInt(b0)**BigInt(n-1));
   const actual=red(qs(raw,BigInt(p)**BigInt(Math.floor(6*n/p))));
   let expected=0;
   const Q=Math.floor(n/s),r=n-Q*s;
   if(r>0&&Q+6*r<p)expected=mod(mp(am,Q)*gg[r-1]*mi(factMod(Q)));
   check(actual,expected,"complete actual numerator source image");
  }
 }
 const lowMatrix=Array.from({length:6*s},(_,i)=>sourceRows.map(x=>Math.floor(i/s)===x.h?x.gamma[i%s]:0));
 check(rankMod(lowMatrix),7,"entire low-weight seven-source rank");
 const fullPole=lowMatrix.map((row,i)=>i%s===0?row.map(()=>0):row);
 check(rankMod(fullPole),7,"old first-pole rank kept after restoring forcing constants");
 sourceFrames.push({p,b:b0,a:am,forcing:[greens[4][s-1],greens[1][s-1]],sourceRows});
}
// Actual p>7D mixed lattice, same source series, with every column retained.
const lowW=[],names=["S","T"];
for(const ell of [4,1])for(let h=0;h<=(ell===4?1:4);h++){
 const a=zero(),tag=ell===4?"AS":"ABS";
 for(let n=1;n<=M;n++)a[n]=qs(data[tag][n-1],1,6*n-h);
 lowW.push(a);names.push("W"+ell+","+h);
}
const sources=[S,T,...lowW],D=3,b0=17,cols=[];
function enumCols(poly,exps,last,depth){
 cols.push({P:poly,exps:exps.slice(),degree:depth});
 if(depth===D)return;
 for(let i=last;i<sources.length;i++){exps[i]++;enumCols(mul(poly,sources[i]),exps,i,depth+1);exps[i]--;}
}
enumCols(cst(1),Array(9).fill(0),0,0);
const rows=[];for(let q0=0;q0<=D;q0++)for(let h=0;h<=q0;h++)rows.push({q:q0,h,n:h*s+q0});
const mixed=rows.map(row=>cols.map(col=>{
 const raw=row.n<col.degree?q(0):qs(col.P[row.n],BigInt(b0)**BigInt(row.n-col.degree));
 const value=red(qs(raw,BigInt(p)**BigInt(row.h)*fact(row.h)));
 checks++;return value;
}));
const pure=[];
for(let d=0;d<=D;d++)for(let v=0;v<=d;v++){
 const idx=cols.findIndex(c=>c.degree===d&&c.exps[0]===d-v&&c.exps[1]===v&&c.exps.slice(2).every(x=>x===0));
 if(idx<0)throw Error("lost genuine pure source column");pure.push(idx);
}
const Vmat=mixed.map(row=>pure.map(j=>row[j]));
check(rankMod(Vmat),pure.length,"actual pure unit block inside all mixed columns");
check(rankMod(mixed),pure.length,"actual full mixed selected row rank");
const corrections=[];
for(let h=0;h<=4;h++){
 const den=mod(19*(6-h)*(7-h));
 const aa=mod((234-33*h)*mi(den)),bb=mod((14*h-101)*mi(den));
 check(mod(aa+bb),mi(6-h),"actual degree-one first-row correction");
 check(mod((17*mi(3))*aa+12*bb),mi(7-h),"actual degree-one Gaussian-row correction");
 corrections.push({h,alpha:aa,beta:bb});
}
return {status:"all exact checks passed",checks,ringFrames,sourceFrames,
 actual_mixed_integral_lattice:{p,b:b0,D,condition_p_gt_7D:p>7*D,
 source_names:names,actual_columns:cols.length,selected_rows:rows,pure_source_columns:pure,
 matrix_mod_p:mixed,degree_one_correction_reductions:corrections},
 ambient_generators_not_added_as_global_sources:true,
 actual_finite_source_images_only:true,all_true_prefix_rows_retained:true,
 no_central_nonvanishing_claim:true,main_target_complete:false};
}
console.log(JSON.stringify(certificate(build(90)),null,2));
