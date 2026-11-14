#!/usr/bin/env node
// R503: exact original five-input frame and the positive-test mass coefficient.
// Uses only BigInt rational arithmetic; no sampling over target primes.
const certificate = (() => {

const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const neg=a=>[-a[0],a[1]], sub=(a,b)=>add(a,neg(b));
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]), div=(a,b)=>q(a[0]*b[1],a[1]*b[0]);
function pow(a,n){let r=q(1);for(;n;n>>=1,a=mul(a,a))if(n&1)r=mul(r,a);return r}
const eq=(a,b)=>a[0]===b[0]&&a[1]===b[1], qs=a=>a[1]===1n?String(a[0]):a[0]+"/"+a[1];
const c=(a=0,b=0)=>[Array.isArray(a)?a:q(a),Array.isArray(b)?b:q(b)];
const ca=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])], cn=a=>[neg(a[0]),neg(a[1])], cs=(a,b)=>ca(a,cn(b));
const cm=(a,b)=>[sub(mul(a[0],b[0]),mul(q(3),mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
const cc=a=>[a[0],neg(a[1])], norm=a=>add(mul(a[0],a[0]),mul(q(3),mul(a[1],a[1])));
const ci=a=>[div(a[0],norm(a)),neg(div(a[1],norm(a)))], cd=(a,b)=>cm(a,ci(b));
const ce=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]), cj=a=>({real:qs(a[0]),delta:qs(a[1])});
function cp(a,n){let r=c(1);for(;n;n>>=1,a=cm(a,a))if(n&1)r=cm(r,a);return r}
function dot(a,b){return a.map((x,i)=>cm(x,cc(b[i]))).reduce(ca,c())}
function mm(A,B){return A.map(row=>B[0].map((_,j)=>row.map((x,k)=>cm(x,B[k][j])).reduce(ca,c())))}
const alpha=c(37,3),z=[c(0,1),c(0,2),c(q(5,2),q(1,2)),c(1),c(2)];
const v=[c(q(63,2),q(17,2)),c(9,-10),c(-17,14),c(22,12),c(17,-3)];
const u=[c(1,1),c(0,1),c(1,1),c(q(3,2),q(1,2)),c(2)];
const per=[c(23,-1),c(q(9,2),q(-35,2)),c(-22,8),c(12,7),c(1,-3)];
const M=[[cd(alpha,c(54)),c(q(1,27))],[c(q(-137,27)),cd(cc(alpha),c(54))]];
const inv=[[cd(cc(alpha),c(36)),c(q(-1,18))],[c(q(137,18)),cd(alpha,c(36))]];
const I=[[c(1),c()],[c(),c(1)]];
if(JSON.stringify(mm(M,inv),(_,x)=>typeof x==="bigint"?String(x):x)!==JSON.stringify(I,(_,x)=>typeof x==="bigint"?String(x):x))throw Error("inverse");
for(let j=0;j<5;j++){
 if(!ce(ca(cm(M[0][0],z[j]),cm(M[0][1],v[j])),u[j]))throw Error("U coefficient");
 if(!ce(ca(cm(M[1][0],z[j]),cm(M[1][1],v[j])),per[j]))throw Error("P coefficient");
}
if(!ce(dot(u,u),c(18))||!ce(dot(per,per),c(2466))||!ce(dot(u,per),c()))throw Error("Gram");
const det=cs(cm(M[0][0],M[1][1]),cm(M[0][1],M[1][0]));
if(!ce(det,c(q(2,3))))throw Error("det");
const projector=mm(mm(inv,[[c(1),c()],[c(),c()]]),M);
const expected=[[cd(c(1396),c(1944)),cd(cm(c(2),cc(alpha)),c(1944))],[cd(cm(c(274),alpha),c(1944)),cd(c(548),c(1944))]];
for(let i=0;i<2;i++)for(let j=0;j<2;j++)if(!ce(projector[i][j],expected[i][j]))throw Error("projector");
const wp=[q(1),q(-1,7)];
for(let n=2;n<=5;n++){let s=q(0);for(let i=1;i<n;i++)s=add(s,mul(wp[i],wp[n-i]));wp[n]=div(s,q((6*n+1)*(n-1)))}
const logs=[q(0),...wp.slice(1).map((a,i)=>div(neg(a),q((6*(i+1))*(6*(i+1)-1))))];
const sig=[q(1)];
for(let n=1;n<=5;n++){let s=q(0);for(let j=1;j<=n;j++)s=add(s,mul(q(j),mul(logs[j],sig[n-j])));sig[n]=div(s,q(n))}
const L=43024169751465478338233979150199956512749200351148033743183443885006289024867517102817280n;
const nums=[
-669434980352778043509581310714866556317857825822326580693089728706624639467520n,
-119981363974691021171554991621708858631413799763774609514070383001600n,
-55342492105213394108340720066257765863550432453355110400n,
-42045915630443092877608745094656489256652800n,
5620340233791194124683811078144n,
1075621969600983023n];
function fact(n){let r=1n;for(let i=2;i<=n;i++)r*=BigInt(i);return r}
let mass=q(0);
for(let k=1;k<=6;k++)mass=add(mass,mul(q(nums[k-1],L),mul(q(fact(6*k)),mul(pow(q(-27),6*k-5),sig[k-1]))));
if(mass[0]===0n)throw Error("mass coefficient vanishes");
let rem=mass[0]%101n; if(rem<0n)rem+=101n;
let den=mass[1]%101n;let invden=1n;for(let i=0;i<99;i++)invden=(invden*den)%101n;
const mod101=(rem*invden)%101n;
const gamma=c(q(5,2),q(1,2));
return {
  status:"exact characteristic-zero identities checked",
  delta_squared:-3,
  source_Z:z.map(cj),source_V:v.map(cj),
  U_coefficients:u.map(cj),P_coefficients:per.map(cj),
  frame:M.map(r=>r.map(cj)),inverse:inv.map(r=>r.map(cj)),determinant:cj(det),
  gram:[[18,0],[0,2466]],W_prime_projector:projector.map(r=>r.map(cj)),
  sigma_series_A_b1:sig.map(qs),
  h_common_denominator:String(L),h_numerators:nums.map(String),
  mass_T5_rational_sum:qs(mass),mass_T5_rational_mod101:String(mod101),
  gamma6:cj(cp(gamma,6)),
  mass_T5_formula:"gamma^6/(7*b) * sum_k c_k (6k)! (-27)^(6k-5) a_(k-1) * (1-beta*kappa^(6k-5))/(1-lambda*kappa^(6k))",
  exact_small_domain:"V deep n, U valuation r -> U,P simultaneous depth r; after scaling 274U+alpha P deep n-r",
  annulus_identity:"(chi_V*lambda)^n beta^r (A(kappa^r)-beta A(kappa^(r+1))) for 1<=r<n",
  boundary_identity:"J_S'(0)=B_0+beta A(kappa)"
};

})();
process.stdout.write(JSON.stringify(certificate, null, 2) + "\n");
