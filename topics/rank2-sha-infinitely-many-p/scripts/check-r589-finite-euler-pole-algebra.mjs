// R589 exact certificate: one complete analytic fibre and full finite-target arithmetic.
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
function sourceCertificate(data){

const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
const q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]};
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]),sc=(a,n,d=1)=>mul(a,q(n,d));
const vp0=(a,p)=>{a=BigInt(a);if(!a)return Infinity;p=BigInt(p);let v=0;while(a%p===0n){v++;a/=p}return v};
const vp=(a,p)=>vp0(a[0],p)-vp0(a[1],p);
const mod=(a,p)=>{a=BigInt(a);a%=BigInt(p);return a<0?a+BigInt(p):a};
const mpow=(a,n,p)=>{let r=1n;a=mod(a,p);for(n=BigInt(n);n;n>>=1n,a=a*a%BigInt(p))if(n&1n)r=r*a%BigInt(p);return r};
const mq=(a,p)=>{if(vp0(a[1],p))throw Error("nonintegral reduction");return Number(mod(a[0],p)*mpow(a[1],p-2,p)%BigInt(p))};
const p=17,s=3,N=p*s-1;
const Z=()=>Array.from({length:N+1},()=>q(0)),ONE=()=>{const f=Z();f[0]=q(1);return f};
const sa=(a,b)=>a.map((x,i)=>add(x,b[i])),ss=(a,c)=>a.map(x=>sc(x,c));
const sm=(a,b)=>{const f=Z();for(let i=0;i<=N;i++)if(a[i][0])for(let j=0;j+i<=N;j++)if(b[j][0])f[i+j]=add(f[i+j],mul(a[i],b[j]));return f};
const sp=(a,n)=>{let r=ONE();for(;n;n>>=1,a=sm(a,a))if(n&1)r=sm(r,a);return r};
const si=a=>{const f=Z();f[0]=q(a[0][1],a[0][0]);for(let n=1;n<=N;n++){let z=q(0);for(let j=1;j<=n;j++)z=add(z,mul(a[j],f[n-j]));f[n]=mul(sc(z,-1),f[0])}return f};
const se=a=>{const f=ONE();for(let n=1;n<=N;n++){let z=q(0);for(let j=1;j<=n;j++)z=add(z,sc(mul(a[j],f[n-j]),j));f[n]=sc(z,1,n)}return f};
const D=Object.fromEntries(Object.entries(data).map(([k,v])=>[k,v.slice(0,N+1).map(a=>a.map(BigInt))]));
const theta=sm(D.A,se(D.L.map(a=>sc(a,1,3))));
const w=Z();w[1]=q(1);const t=ss(sm(w,sp(si(D.A),3)),-1),t2=sm(t,t),t3=sm(t2,t);
const C=c=>{const a=Z();a[0]=q(c);return a};
const f=ss(sm(sm(sm(t,sa(t,C(-1))),sa(sa(ss(t2,16),ss(t,4)),C(7))),sa(C(1),ss(t,8))),1);
for(let i=0;i<=N;i++)f[i]=sc(f[i],1,7);
const v=sm(sm(sa(C(1),ss(t,-4)),sa(sa(C(1),ss(t,-20)),ss(t2,-8))),sa(sa(sa(C(1),ss(t,96)),ss(t2,48)),ss(t3,-64)));
const S=sm(sp(theta,17),f),T=sm(sm(sp(theta,36),f),v);
const W=[],labels=[];
for(const tag of ["AS","ABS"])for(let h=0;h<=(tag==="AS"?1:4);h++){
 const a=Z();for(let k=1;k<=N;k++)a[k]=sc(D[tag][k-1],1,6*k-h);
 W.push(a);labels.push((tag==="AS"?"W4,":"W1,")+h);
}
const F=[S,T,...W];
let checks=0;const check=(ok,label)=>{checks++;if(!ok)throw Error(label)};
function toResidue(a,b=1,withP=true){
 const r=[];
 for(let k=0;k<=N;k++){
  const Q=Math.floor(k/s),rem=k-Q*s;
  const norm=sc(a[k],BigInt(p)**BigInt(Q+(withP?1:0))*BigInt(b)**BigInt(Math.max(0,k-1)));
  check(vp(norm,p)>=0,"whole finite target integrality");
  r[k]=mq(norm,p);
  if(withP&&Q+6*rem<p)check(r[k]===0,"full polynomial high-weight pole support");
 }
 return r;
}
function rank(A){
 A=A.map(x=>x.slice());let r=0;
 for(let col=0;col<A[0].length;col++){
  let i=r;while(i<A.length&&!A[i][col])i++;if(i===A.length)continue;
  [A[r],A[i]]=[A[i],A[r]];const inv=Number(mpow(A[r][col],p-2,p));A[r]=A[r].map(x=>x*inv%p);
  for(let j=0;j<A.length;j++)if(j!==r){const x=A[j][col];A[j]=A[j].map((v,k)=>(v-x*A[r][k]%p+p)%p)}
  r++;if(r===A.length)break;
 }return r;
}
const residues=F.map(a=>toResidue(a));
check(residues[0].every(x=>x===0)&&residues[1].every(x=>x===0),"old S/T integral columns");
check(rank(Array.from({length:N+1},(_,k)=>residues.map(a=>a[k])))===7,"complete first-pole rank seven");
let monomials=0;
function monomialTest(a,last,depth){
 if(depth){toResidue(a);monomials++}
 if(depth===3)return;
 for(let i=last;i<F.length;i++)monomialTest(sm(a,F[i]),i,depth+1);
}
monomialTest(ONE(),0,0);
let powerTests=0;
for(const a of W){toResidue(sp(a,p),1,false);powerTests++}
const nonlin=sa(sa(S,sm(W[0],W[3])),sp(W[6],3));
toResidue(sp(nonlin,p),1,false);powerTests++;
// Unit homothety on the same analytic sources; p=17 excludes b=17.
for(const a of F)toResidue(a,2);
const gaussian=sc(D.L[s],p),am=mq(gaussian,p);
for(let j=0;j<W.length;j++){
 const h=Number(labels[j].split(",")[1]),tag=labels[j][1]==="4"?"AS":"ABS",R=Array(N+1).fill(0);
 for(let r=0;r<=s-2;r++){
  const e=p+h-6-6*r,m=e+1,k=e*s+r+1;
  let factorial=1n;for(let n=2;n<=m;n++)factorial*=BigInt(n);
  const coeff=Number(mpow(am,e,p))*mq(D[tag][r],p)%p*Number(mpow(factorial,p-2,p))%p;
  R[k]=coeff;
 }
 check(R.every((x,k)=>x===residues[j+2][k]),"whole original residue polynomial "+labels[j]);
}
const top=(p*p-1)/6,Q=Math.floor(top/s);
check(Q===p-1,"height-two distinguished row");
for(const a of F)check(vp(a[top],p)>=-(p-1),"actual source height-two improvement");
return {checks,p,b_frames:[1,2],target_rank:p*s,source_rank:9,first_pole_rank:7,
 all_monomials_degree_at_most_3:monomials,complete_frobenius_power_tests:powerTests,
 residue_labels:labels,residue_columns:residues.slice(2),
 source_first_coefficients:{S:S[1].map(String),T:T[1].map(String)},
 finite_certificate_only:true,first_c4_c1_observation_claim:false,
 saturated_nonzero_claim:false};

}
function parameterCertificate(){

let checks=0,allDegreeRows=0,pairChecks=0,powerChecks=0;
const check=(ok,label)=>{checks++;if(!ok)throw Error(label)};
for(let s=3;s<=20;s++){
 const p=6*s-1,N=p*s-1,local=Array(N+1).fill(0),dp=Array(N+1).fill(0);
 for(let k=1;k<=N;k++){
  const L=Math.floor((k-1)/s),u=k-L*s,weight=L+6*u;
  check(weight>=6&&weight<=2*p-1,"actual individual noncanonical weight");
  let e=0;
  for(let h=0;h<=4;h++)if((6*k-h)%p===0){
   check((6*k-h)%(p*p)!==0,"no second short-denominator multiple in first square target");
   check(weight===p+h,"actual pole weight");e=1;
  }
  local[k]=L+e;
  for(let j=1;j<=k;j++)dp[k]=Math.max(dp[k],dp[k-j]+local[j]);
  const Q=Math.floor(k/s),r=k-Q*s;
  check(dp[k]<=Q+(Q+6*r>=p?1:0),"all source labels and all composition lengths");allDegreeRows++;
 }
 const top=(p*p-1)/6;check(dp[top]<=p-1,"actual height-two all-degree bound");
}
for(const p of [17,29,71]){
 const s=(p+1)/6,J=[];
 for(let r=0;r<s;r++)for(let Q=0;Q<p;Q++)if(6*r+Q>=p){
  J.push([r,Q]);check(Q>=5,"actual high-weight ideal epsilon floor");
 }
 check(J.length===3*s*(s-1),"exact square-zero ideal dimension");
 for(const [r,Q]of J)for(const[t,L]of J){
  check(r+t>=s||Q+L>=p,"whole square-zero ideal product");pairChecks++;
 }
 for(let j=1;j<=20;j++)for(let A=j;A<=j*(s-1);A++)for(let B=5*j;B<p;B++){
  if(6*A+B<j*p)continue;
  const carry=Math.floor(A/s);
  if(B+carry>=p)continue;
  check(carry>=j-1,"all possible lifted ideal power carries");powerChecks++;
 }
}
return {checks,all_degree_rows:allDegreeRows,square_zero_pairs:pairChecks,lift_power_checks:powerChecks};

}
const source=sourceCertificate(build(50)),parameters=parameterCertificate();
const result={status:'all exact checks passed',checks:source.checks+parameters.checks,actual_full_source_certificate:source,all_parameter_combinatorics:parameters,
actual_target:"O[w,epsilon]/(w^s-p epsilon,epsilon^p)",whole_polynomial_bound:"v_p [w^n] P >= -Q - 1_{Q+6r>=p}, n=Qs+r<ps, all degrees D",whole_frobenius_integrality:"F^p belongs to the actual finite integral target for every original source polynomial F",first_pole_rank:7,first_pole_ideal:"weight(6,1)>=p, square zero",exact_linear_integral_preimage:"O<1,S,T> + p O<W4,0,W4,1,W1,0,...,W1,4>",selected_height_two_row_gain:"k=(p^2-1)/6: norm <=p^(p-1), all D",central_rows_c4_c1_not_observed:true,ordinary_negative_moment_nonvanishing_claim:false,full_cutoff_claim:false,main_target_complete:false};
console.log(JSON.stringify(result,null,2));
