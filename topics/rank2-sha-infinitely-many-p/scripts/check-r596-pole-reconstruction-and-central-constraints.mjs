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

function certificate(data){
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b)[a,b]=[b,a%b];return a}
function q(a,b=1n){a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}const d=gcd(a,b);return[a/d,b/d]}
const qa=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const qm=(a,b)=>q(a[0]*b[0],a[1]*b[1]),qs=(a,n,d=1)=>qm(a,q(n,d));
const p=23,s=4,N=s-1,M=s;
const mod=x=>Number((BigInt(x)%BigInt(p)+BigInt(p))%BigInt(p));
function mpow(a,n){a=mod(a);let r=1;for(;n;n>>=1,a=a*a%p)if(n&1)r=r*a%p;return r}
const mi=x=>mpow(x,p-2);
function red(a){if(a[1]%BigInt(p)===0n)throw Error("nonintegral rational row");return mod(a[0])*mi(mod(a[1]))%p}
function binom(n,k){let a=1n;for(let j=1;j<=k;j++)a=a*BigInt(n-j+1)/BigInt(j);return a}
const Z=()=>Array(M+1).fill(0),C0=c=>{const a=Z();a[0]=mod(c);return a};
const sa=(a,b)=>a.map((x,i)=>mod(x+b[i])),sc=(a,c)=>a.map(x=>mod(x*c));
function sm(a,b){const f=Z();for(let i=0;i<=M;i++)for(let j=0;j+i<=M;j++)f[i+j]=mod(f[i+j]+a[i]*b[j]);return f}
function sp(a,n){let f=C0(1);for(;n;n>>=1,a=sm(a,a))if(n&1)f=sm(f,a);return f}
function si(a){const f=Z();f[0]=mi(a[0]);for(let n=1;n<=M;n++){let z=0;for(let j=1;j<=n;j++)z=mod(z+a[j]*f[n-j]);f[n]=mod(-z*f[0])}return f}
function se(a){const f=C0(1);for(let n=1;n<=M;n++){let z=0;for(let j=1;j<=n;j++)z=mod(z+j*a[j]*f[n-j]);f[n]=z*mi(n)%p}return f}
const t=Z();t[1]=1;
let checks=0;function check(a,b,msg){checks++;if(a!==b)throw Error(msg+": "+a+" != "+b)}
const CC=C0(1),H=C0(1),Q=C0(1),logK=Z();
for(let n=1;n<=N;n++){
 CC[n]=mod(-(2*n-1)*mi(2*n)*CC[n-1]);H[n]=CC[n]*mi(6*n+1)%p;
 Q[n]=mod(-(6*n-4)*mi(6*n-1)*Q[n-1]);logK[n]=Q[n]*mi(n)%p;
}
const K=se(logK);K[M]=0;
const PS=sc(sm(sm(sa(C0(1),t),sa(C0(1),sc(t,-8))),sa(sa(C0(7),sc(t,-4)),sc(sp(t,2),16))),mi(7));
const PT=sm(sm(sm(PS,sa(C0(1),sc(t,4))),sa(sa(sa(C0(1),sc(t,-96)),sc(sp(t,2),48)),sc(sp(t,3),64))),sa(sa(C0(1),sc(t,20)),sc(sp(t,2),-8)));
const U=sm(CC,sp(si(H),2));
const alpha=17*mi(3)%p;
const AS=k=>sm(sp(k,alpha),sm(PS,U))[N],AT=k=>sm(sp(k,12),sm(PT,U))[N];
const EE=k=>sm(k.map((x,j)=>mod(j*x)),si(k))[N];
const LL=k=>mod(36*AS(k)-17*AT(k));
const BB=k=>mod(5*mi(34)*AS(k)+EE(k));
const DD=k=>sm(k,sa(sp(H,3),sc(CC,-1)))[N];
// Independently build the actual original S/T z-series, not the u formulas.
const Az=data.A.slice(0,M+1).map(red);
const Lz=data.L.slice(0,M+1).map((x,j)=>j<s?red(x):0);
const theta=sm(Az,se(sc(Lz,mi(3))));
const tz=sc(sm(t,sp(si(Az),3)),-1),tz2=sp(tz,2),tz3=sp(tz,3);
const radial=sc(sm(sm(sm(tz,sa(tz,C0(-1))),sa(sa(sc(tz2,16),sc(tz,4)),C0(7))),sa(C0(1),sc(tz,8))),mi(7));
const angular=sm(sm(sa(C0(1),sc(tz,-4)),sa(sa(C0(1),sc(tz,-20)),sc(tz2,-8))),sa(sa(sa(C0(1),sc(tz,96)),sc(tz2,48)),sc(tz3,-64)));
const actualAS=sm(sp(theta,17),radial)[s],actualAT=sm(sm(sp(theta,36),radial),angular)[s];
check(AS(K),actualAS,"whole original S34 residue substitution");
check(AT(K),actualAT,"whole original T72 residue substitution");
const hp=mod(binom(3*s-1,2*s-1));
check(Q[N],mod(-hp*mi(3)),"true hypergeometric terminal unit");
const frames=[];
for(const b of [1,17]){
 const am=red(qs(data.L[s],BigInt(p)*BigInt(b)**BigInt(s)));
 const pole=[],gg=[];
 for(let r=0;r<=N-1;r++){
  const e=p-6-6*r,m=e+1,k=e*s+r+1;
  const value=red(qs(data.AS[k-1],BigInt(p)**BigInt(e+1)*BigInt(b)**BigInt(k-1),6*k));
  let fac=1;for(let j=1;j<=m;j++)fac=fac*j%p;
  const gr=mod(value*fac*mi(mpow(am,e)));
  const actual=red(qs(data.AS[r],BigInt(b)**BigInt(r)));
  check(gr,actual,"original high-pole row reconstructs forcing coefficient");
  pole.push({r,epsilon:e,w:r+1,physical_index:k,value});gg.push(gr);
 }
 const khat=Z();
 for(let r=0;r<=N-1;r++){
  const part=sp(H,4+6*r),coef=gg[r]*mi(mpow(b,r))%p;
  for(let j=r;j<=N-1;j++)khat[j]=mod(khat[j]+coef*part[j-r]);
 }
 for(let j=0;j<N;j++)check(khat[j],K[j],"unit triangular actual K reconstruction");
 const rawC4=red(qs(data.AS[N],BigInt(b)**BigInt(N)));
 const rawC1=red(qs(data.ABS[N],BigInt(b)**BigInt(N)));
 const normC4=rawC4*mi(mpow(b,N))%p,normC1=rawC1*mi(mpow(b,N))%p;
 let rawDiff=0;
 for(let j=1;j<=N;j++)rawDiff=mod(rawDiff+red(qs(data.A[j],BigInt(1-3*j)*BigInt(b)**BigInt(j)))*gg[N-j]);
 check(rawDiff,mod(rawC1-rawC4),"exact linear pole difference in original z frame");
 check(DD(khat),mod(normC1-normC4),"same difference in u frame");
 const missing=mod(2*mi(5)*hp+6*mi(5)*EE(khat));
 check(missing,K[N],"missing original top K coefficient from log connection");
 check(mod(missing+sm(khat,CC)[N]),normC4,"complete original c4 reconstruction");
 check(mod(missing+sm(khat,sp(H,3))[N]),normC1,"complete original c1 reconstruction");
 check(mod(alpha*missing+AS(khat)),actualAS,"complete original S34 diagonal reconstruction");
 check(mod(12*missing+AT(khat)),actualAT,"complete original T72 diagonal reconstruction");
 check(LL(khat),mod(36*actualAS-17*actualAT),"actual central combination from original pole");
 check(BB(khat),mod(-hp*mi(3)+5*mi(34)*actualAS),"nonhomogeneous unit pole constraint");
 const low=khat.slice();low[N-1]=0;
 check(mod(LL(khat)-LL(low)),mod(76024*mi(5)*khat[N-1]),"actual highest visible pole coefficient");
 check(mod(BB(khat)-BB(low)),mod(-2141*mi(252)*khat[N-1]),"actual nonhomogeneous highest coefficient");
 check(mod(DD(khat)-DD(low)),mod(2*mi(7)*khat[N-1]),"actual linear difference highest coefficient");
 let square=q(0);
 for(let i=1;i<2*p;i++)square=qa(square,qs(qm(data.AS[i-1],data.AS[2*p-i-1]),BigInt(b)**BigInt(2*p-2),36*i*(2*p-i)));
 const squareRow=red(qs(square,BigInt(p)**12n));
 check(squareRow,pole[pole.length-1].value**2%p,"actual quadratic source row, not product in J squared");
 frames.push({quadratic_W40_row_at_2p:squareRow,p,b,a:am,hp,full_R40_pole:pole,reconstructed_K:khat.slice(0,N),actual_K_top:K[N],
 forcing_normalized:[normC4,normC1],central_normalized:[actualAS,actualAT],
 original_linear_difference:rawDiff,L:LL(khat),B:BB(khat),E:EE(khat),
 lower_L:LL(low),lower_B:BB(low)});
}
return {status:"all exact checks passed",checks,actual_original_p23_frames:frames,
 previous_fibre_only:true,pole_rows_taken_from_exact_high_rational_coefficients:true,
 full_target_pole_polynomials_not_multiplied_in_square_zero_ideal:true,
 no_free_source_column:true,central_nonvanishing_claim:false,main_target_complete:false};
}

console.log(JSON.stringify(certificate(build(68)),null,2));
