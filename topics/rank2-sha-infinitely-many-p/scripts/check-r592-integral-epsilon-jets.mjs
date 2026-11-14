// R592: the actual integral epsilon jet, not an independent-column model.
// Exact rational sigma series; same p=17 analytic fibre as R589, b=1 and b=2.
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}const d=gcd(a,b);return[a/d,b/d]}
const qa=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const qm=(a,b)=>q(a[0]*b[0],a[1]*b[1]);
const qs=(a,n,d=1)=>qm(a,q(n,d));
const p=17,s=3,N=6*s;
const zero=()=>Array.from({length:N+1},()=>q(0));
const constant=c=>{const f=zero();f[0]=q(c);return f};
const add=(a,b)=>a.map((v,i)=>qa(v,b[i]));
const scale=(a,c,d=1)=>a.map(v=>qs(v,c,d));
function mul(a,b){const f=zero();for(let i=0;i<=N;i++)if(a[i][0])for(let j=0;j+i<=N;j++)if(b[j][0])f[i+j]=qa(f[i+j],qm(a[i],b[j]));return f}
function pow(a,n){let f=constant(1);for(;n;n>>=1,a=mul(a,a))if(n&1)f=mul(f,a);return f}
function inv(a){const f=zero();f[0]=q(a[0][1],a[0][0]);for(let n=1;n<=N;n++){let z=q(0);for(let j=1;j<=n;j++)z=qa(z,qm(a[j],f[n-j]));f[n]=qm(qs(z,-1),f[0])}return f}
function exp(a){const f=constant(1);for(let n=1;n<=N;n++){let z=q(0);for(let j=1;j<=n;j++)z=qa(z,qs(qm(a[j],f[n-j]),j));f[n]=qs(z,1,n)}return f}
const A=constant(1);A[1]=q(-1,7);
for(let n=2;n<=N;n++){let z=q(0);for(let j=1;j<n;j++)z=qa(z,qm(A[j],A[n-j]));A[n]=qs(z,1,(6*n+1)*(n-1))}
const L=zero();for(let n=1;n<=N;n++)L[n]=qs(A[n],-1,n*(6*n-1));
const AS=mul(A,exp(L)),ABS=mul(A.map((x,i)=>qs(x,1-3*i)),AS);
const theta=mul(A,exp(scale(L,1,3))),w=zero();w[1]=q(1);
const t=scale(mul(w,pow(inv(A),3)),-1),t2=mul(t,t),t3=mul(t2,t);
const radialS=scale(mul(mul(mul(t,add(t,constant(-1))),add(add(scale(t2,16),scale(t,4)),constant(7))),add(constant(1),scale(t,8))),1,7);
const radialV=mul(mul(add(constant(1),scale(t,-4)),add(add(constant(1),scale(t,-20)),scale(t2,-8))),add(add(add(constant(1),scale(t,96)),scale(t2,48)),scale(t3,-64)));
const F0=[mul(pow(theta,17),radialS),mul(mul(pow(theta,36),radialS),radialV)];
const labels=["S","T"];
for(const [name,source,cap]of [["W4",AS,1],["W1",ABS,4]])for(let h=0;h<=cap;h++){
 const f=zero();for(let k=1;k<=N;k++)f[k]=qs(source[k-1],1,6*k-h);
 F0.push(f);labels.push(name+","+h);
}
const mod=x=>Number((BigInt(x)%BigInt(p)+BigInt(p))%BigInt(p));
function mpow(a,n){a=mod(a);let r=1;for(;n;n>>=1,a=a*a%p)if(n&1)r=r*a%p;return r}
function reduce(a){if(a[1]%BigInt(p)===0n)throw Error("nonintegral actual row");return mod(a[0])*mpow(mod(a[1]),p-2)%p}
let checks=0;const check=(a,b,msg)=>{checks++;if(a!==b)throw Error(msg+": "+a+" != "+b)};
const epone=()=>[1,0,0,0,0,0,0];
function epmul(a,b){const f=Array(7).fill(0);for(let i=0;i<7;i++)for(let j=0;i+j<7;j++)f[i+j]=(f[i+j]+a[i]*b[j])%p;return f}
const frames=[];
for(const b of [1,2]){
 const F=F0.map(f=>f.map((x,k)=>qs(x,BigInt(b)**BigInt(Math.max(0,k-1)))));
 const am=reduce(qs(L[s],BigInt(p)*BigInt(b)**BigInt(s)));
 const c4=reduce(qs(AS[s-1],BigInt(b)**BigInt(s-1)));
 const c1=reduce(qs(ABS[s-1],BigInt(b)**BigInt(s-1)));
 const v=F.map(()=>Array(7).fill(0));
 v[3][1]=c4;
 for(let h=1;h<=4;h++){let fac=1;for(let j=1;j<=h;j++)fac=fac*j%p;v[4+h][h]=mpow(am,h-1)*c1%p*mpow(fac,p-2)%p}
 const first=F.map(f=>reduce(f[1]));
 const rho=F.map(f=>reduce(qs(f[p],BigInt(p)**6n)));
 const expectedRho=Array(9).fill(0);
 expectedRho[2]=mpow(am,5)*reduce(qs(AS[s-2],BigInt(b)**BigInt(s-2),720))%p;
 expectedRho[4]=mpow(am,5)*reduce(qs(ABS[s-2],BigInt(b)**BigInt(s-2),720))%p;
 for(let i=0;i<9;i++){
  check(rho[i],expectedRho[i],"actual residue "+labels[i]);
  for(let j=0;j<=6;j++)check(reduce(qs(F[i][j*s],BigInt(p)**BigInt(j))),v[i][j],"actual coordinate epsilon jet");
 }
 let monomials=0,nonzeroCorrections=0;
 function visit(actual,expected,indices,last,depth){
  if(depth){
   let correction=0;
   if(depth===2){const[i,j]=indices;correction=(rho[i]*first[j]+first[i]*rho[j])%p}
   const ex=expected.slice();ex[6]=(ex[6]+correction)%p;
   for(let j=0;j<=6;j++)check(reduce(qs(actual[j*s],BigInt(p)**BigInt(j))),ex[j],"full actual monomial "+indices+" epsilon "+j);
   if(correction)nonzeroCorrections++;
   monomials++;
  }
  if(depth===3)return;
  for(let i=last;i<9;i++)visit(mul(actual,F[i]),epmul(expected,v[i]),[...indices,i],i,depth+1);
 }
 visit(constant(1),epone(),[],0,0);
 const sixth=pow(F[3],6),expectedSixth=mpow(c4,6);
 check(reduce(qs(sixth[6*s],BigInt(p)**6n)),expectedSixth,"sixth degree actual monomial");
 const square=mul(F[2],F[2]);
 const firstDefect=reduce(qs(square[6*s],BigInt(p)**6n));
 check(firstDefect,2*rho[2]*first[2]%p,"actual first multiplication defect");
 frames.push({p,b,c4,c1,a:am,coordinate_epsilon_jets:v,first_w_rows:first,adjacent_pole_rows:rho,
  all_monomials_degree_at_most_3:monomials,nonzero_quadratic_corrections:nonzeroCorrections,
  W40_squared_sixth_integral_row:firstDefect});
}
let carryChecks=0;
for(let ss=3;ss<=30;ss++){
 const pp=6*ss-1;
 for(let r=1;r<ss;r++){const t=ss-r;
  for(let Q=0;Q<=5;Q++)for(let R=0;R<=5-Q;R++){
   const out=Q+R+1,ef=Q+6*r>=pp,eg=R+6*t>=pp;
   const survives=Number(ef)+Number(eg)>=1;
   const exceptional=out===6&&((r===ss-1&&Q===5&&t===1&&R===0)||(t===ss-1&&R===5&&r===1&&Q===0));
   check(Number(survives),Number(exceptional),"whole possible r-zero carry");
   carryChecks++;
  }
 }
}
console.log(JSON.stringify({status:"all exact checks passed",checks,actual_analytic_frames:frames,
 carry_positions_checked:carryChecks,
 theorem:"Psi5 is an actual algebra homomorphism; Psi6 has the displayed original quadratic correction",
 original_target:"O[w,epsilon]/(w^s-p epsilon,epsilon^p)",
 actual_prefix_only:true,
 c4_c1_nonvanishing_claim:false,
 original_arithmetic_zero_to_forcing_zero_claim:false,
 global_cutoff_claim:false,
 main_target_complete:false},null,2));

