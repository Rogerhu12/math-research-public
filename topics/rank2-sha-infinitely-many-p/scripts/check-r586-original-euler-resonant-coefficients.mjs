// Exact original coefficients and full integer identities for R586.
// Run with Node.js; no dependency and no broadened prime scan.
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
function checkOriginal(data){

const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
const q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]};
const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]),sc=(a,n,d=1n)=>mul(a,q(n,d));
const vp0=(a,p)=>{a=BigInt(a);if(!a)return Infinity;p=BigInt(p);let v=0;while(a%p===0n){v++;a/=p}return v};
const vp=(a,p)=>vp0(a[0],p)-vp0(a[1],p);
const mp=(a,p)=>{p=BigInt(p);a%=p;return a<0?a+p:a};
const pow=(a,e,p)=>{let z=1n;a=mp(a,p);p=BigInt(p);for(e=BigInt(e);e;e>>=1n,a=a*a%p)if(e&1n)z=z*a%p;return z};
const modq=(a,p)=>{if(vp0(a[1],p))throw Error("nonintegral rational");return mp(a[0],p)*pow(a[1],p-2,p)%BigInt(p)};
const fact=n=>{let a=1n;for(let j=2;j<=n;j++)a*=BigInt(j);return a};
const D=Object.fromEntries(Object.entries(data).map(([key,v])=>[key,v.map(a=>a.map(BigInt))]));
let checks=0;const check=(ok,label)=>{checks++;if(!ok)throw Error(label)};const rows=[];
for(const p of [11,23]){
 const s=(p+1)/6,a=sc(D.L[s],p);
 check(vp(a,p)===0,"actual Gaussian leading unit "+p);
 for(const b of [1,17]){
  const ab=sc(a,BigInt(b)**BigInt(s)),abmod=modq(ab,p);
  for(const tag of ["AS","ABS"])for(let h=0;h<=(tag==="AS"?1:4);h++){
   let exact=0;
   for(let k=1;k<=D[tag].length;k++){
    const L=Math.floor((k-1)/s),r=k-1-L*s,n=6*k-h,e=vp0(n,p),u=BigInt(n)/BigInt(p)**BigInt(e);
    const coeff=sc(D[tag][k-1],BigInt(b)**BigInt(k-1),BigInt(n));
    const norm=sc(coeff,BigInt(p)**BigInt(L+e)*fact(L));
    check(vp(norm,p)>=0,"all-k integral normalization");
    const gr=sc(D[tag][r],BigInt(b)**BigInt(r));
    const right=pow(abmod,L,p)*modq(gr,p)%BigInt(p)*pow(u,p-2,p)%BigInt(p);
    check(modq(norm,p)===right,"whole original coefficient congruence "+[p,b,tag,h,k]);
    if(right!==0n){check(vp(coeff,p)===-L-vp0(fact(L),p)-e,"exact actual coefficient valuation");exact++}
   }
   rows.push({p,b,source:tag==="AS"?"f4":"f1",h,coefficients:D[tag].length,certified_exact_valuations:exact});
  }
 }
}
return {checks,rows};
}
function checkParameters(){

let checks=0;const check=(ok,label)=>{checks++;if(!ok)throw Error(label)};
let tailChecks=0,windowChecks=0;
for(let s=2;s<=30;s++){
 const p=6*s-1;
 for(let r=0;r<s;r++)for(let d=1;d<=120;d++){
  check(d*p-3*(d*s+r)>0,"unique lowest Gaussian term");
  check(Math.floor(3*(d*s+r)/p)<=d-1,"complete lower term floor");tailChecks++;
 }
 for(let h=0;h<=4;h++)for(let t=0;t<s;t++){
  const m=h+6*t;if(m<1||m>=p)continue;
  const k=m*s-t,L=m-1,r=s-t-1;
  check(6*k-h===m*p&&k-1===L*s+r,"actual resonant index");
  check(r>=0&&r<s&&6*k<p*p,"complete first square window");
  if(t===s-1){
   check(m===p+h-5&&r===0,"specified unit endpoint");
   check(Math.floor(6*k*p/(p*p-1))===m,"Gaussian bound attained at endpoint");
  }
  windowChecks++;
 }
}
check(6-(-4)===10&&10*7===2*35,"two forcing determinant 2b/7");
return {checks,tail_checks:tailChecks,window_checks:windowChecks};

}
const original=checkOriginal(build(80)),parameters=checkParameters();
const result={status:'all exact checks passed',checks:original.checks+parameters.checks,actual_coefficient_checks:original,parameter_checks:parameters,
theorem:"p^(L+e) L! [w^k] W_l,h = a^L g_l,r / u mod p, k-1=Ls+r, 6k-h=p^e u",first_window:"m=h+6t in [1,p-1], k=ms-t, p^m[w^k]W_l,h = a^(m-1)g_l,s-t-1/m! mod p",exact_unit_endpoint:"t=s-1, m=p+h-5, r=0, valuation exactly -m",
original_saturated_prefix_preserved_but_coefficient_not_assumed_in_kernel:true,first_resonant_c4_c1_unconditional_nonvanishing_claim:false,ordinary_negative_moment_nonvanishing_claim:false,main_target_complete:false};
console.log(JSON.stringify(result,null,2));
