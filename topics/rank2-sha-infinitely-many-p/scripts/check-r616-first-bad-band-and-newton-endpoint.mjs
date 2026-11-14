// R615: the original Weierstrass-zeta finite Cartier correspondence.
// Exact rational arithmetic; no external dependency or new prime scan.
function buildX(N){
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]};
 const add=(a,b)=>q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const mul=(a,b)=>q(a[0]*b[0],a[1]*b[1]);
 const A=Array.from({length:N+1},()=>q(0));A[0]=q(1);A[1]=q(-1,7);
 for(let n=2;n<=N;n++){let v=q(0);for(let j=1;j<n;j++)v=add(v,mul(A[j],A[n-j]));A[n]=q(v[0],v[1]*BigInt((6*n+1)*(n-1)))}
 return A;
}
function certificate(A) {
 let checks=0;const frames=[];
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const Q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]};
 function check(a,b,label){checks++;if(String(a)!==String(b))throw Error(label+": "+a+" != "+b)}
 for(const pp of [17,23]){
  const p=BigInt(pp),s=(pp+1)/6,L=(pp*pp-1)/6,maxN=pp*s-1;
  const precision=Math.floor(maxN/pp)+1,modulus=p**BigInt(precision);
  const mod=(a,M=modulus)=>{a=BigInt(a)%M;return a<0n?a+M:a};
  function inv(a,M=modulus){let oldr=M,r=mod(a,M),olds=0n,t=1n;while(r){const q=oldr/r;[oldr,r]=[r,oldr-q*r];[olds,t]=[t,olds-q*t];}if(oldr!==1n)throw Error("nonunit denominator");return mod(olds,M);}
  function pow(a,n,M=modulus){let out=1n;a=mod(a,M);n=BigInt(n);for(;n;n>>=1n,a=a*a%M)if(n&1n)out=out*a%M;return out;}
  function redFraction(a,b,M=modulus){
   a=BigInt(a);b=BigInt(b);if(a===0n)return 0n;
   while(b%p===0n){if(a%p!==0n)throw Error("uncanceled p denominator");a/=p;b/=p;}
   return mod(a,M)*inv(b,M)%M;
  }
  let fact=[1n];for(let n=1;n<=maxN;n++)fact[n]=fact[n-1]*BigInt(n);
  const vp=n=>{let v=0;while(n&&n%p===0n){v++;n/=p;}return v};
  const binom=Array.from({length:maxN+1},(_,n)=>Array(n+1).fill(0n));
  for(let n=0;n<=maxN;n++){binom[n][0]=binom[n][n]=1n;for(let j=1;j<n;j++)binom[n][j]=(binom[n-1][j-1]+binom[n-1][j])%modulus;}
  // Exact original H, independent of sigma or the desired band theorem.
  const C=[Q(1)],H=[Q(1)];
  for(let n=1;n<=maxN;n++){
   C[n]=Q(-C[n-1][0]*BigInt(2*n-1),C[n-1][1]*BigInt(2*n));
   H[n]=Q(C[n][0],C[n][1]*BigInt(6*n+1));
  }
  for(let n=0;n<=maxN;n++){
   const v=vp(H[n][0])-vp(H[n][1]);
   check(n===L?v===-1:v>=0,true,"unique original H denominator");
  }
  check(redFraction(p*H[L][0],H[L][1],p),p-1n,"absolute H endpoint");
  const fibers=[];
  for(const bb of [1,17].filter(b=>b%pp!==0)){
   const b=BigInt(bb),bL=pow(b,L,p);
   // Hurwitz logarithm j! (6F-6cw^s)_j is integral. Recover actual
   // ordinary coefficients only after preserving sufficient p-adic precision.
   const ah=[],yh=[],lh=[0n];
   for(let n=0;n<=maxN;n++){
    ah[n]=redFraction(fact[n]*A[n][0],A[n][1])*pow(b,n)%modulus;
    yh[n]=mod(BigInt(1-3*n)*ah[n]);
    if(n>0)lh[n]=n===s?0n:mod(-redFraction(fact[n-1]*A[n][0],A[n][1]*BigInt(6*n-1))*pow(b,n));
   }
   const gh=[1n];
   for(let n=1;n<=maxN;n++){
    let value=0n;for(let j=1;j<=n;j++)value=(value+binom[n-1][j-1]*lh[j]*gh[n-j])%modulus;
    gh[n]=value;
   }
   function product(u,v){const out=[];for(let n=0;n<=maxN;n++){let value=0n;for(let j=0;j<=n;j++)value=(value+binom[n][j]*u[j]*v[n-j])%modulus;out[n]=value;}return out;}
   const g4h=product(ah,gh),g1h=product(yh,g4h);
   function low(u,n){check(vp(fact[n]),0,"low original factorial unit");return mod(u[n],p)*inv(mod(fact[n],p),p)%p;}
   function residue(u,n){
    const v=vp(fact[n]);check(v>=1,true,"bad-band factorial valuation");
    const pv=p**BigInt(v-1),unit=fact[n]/p**BigInt(v);
    check(u[n]%pv,0n,"full high-order cancellation before ordinary coefficient");
    return mod(u[n]/pv,p)*inv(mod(unit,p),p)%p;
   }
   const rows=[];
   for(let r=0;r<s;r++){
    const n=L+r;
    const xr=redFraction(A[r][0],A[r][1],p)*pow(b,r,p)%p;
    const prx=redFraction(p*A[n][0],A[n][1],p)*pow(b,n,p)%p;
    const pry=mod(BigInt(1-3*n)*prx,p);
    check(prx,mod(bL*BigInt(6*r-2)*xr,p),"complete original x residue band");
    check(pry,mod(bL*BigInt(6*r-3)*BigInt(1-3*r)*xr,p),"complete original y residue band");
    const prf=mod(-redFraction(p*A[n][0],A[n][1]*BigInt(6*n)*BigInt(6*n-1),p)*pow(b,n,p),p);
    const zr=mod(-xr*inv(6*r-1,p),p);
    check(prf,bL*zr%p,"complete log-sigma residue band");
    const g6=low(gh,r),g4=low(g4h,r),g1=low(g1h,r);
    const rg6=residue(gh,n),rg4=residue(g4h,n),rg1=residue(g1h,n);
    check(rg6,mod(bL*BigInt(6*r+6)*g6,p),"actual sigma6 Gaussian band");
    check(rg4,mod(bL*BigInt(6*r+4)*g4,p),"actual f4 Gaussian band");
    check(rg1,mod(bL*BigInt(6*r+1)*g1,p),"actual f1 Gaussian band");
    rows.push({r,index:n,pX:String(prx),pY:String(pry),pF:String(prf),
      low:{sigma6:String(g6),f4:String(g4),f1:String(g1)},
      actual_gaussian_residues:{sigma6:String(rg6),f4:String(rg4),f1:String(rg1)}});
   }
   const c4=low(g4h,s-1),c1=low(g1h,s-1),last=rows[rows.length-1];
   check(BigInt(last.actual_gaussian_residues.f4),mod(-bL*c4,p),"last f4 forcing return");
   check(BigInt(last.actual_gaussian_residues.f1),mod(-4n*bL*c1,p),"last f1 forcing return");
   check(rows[0].actual_gaussian_residues.f4,String(4n*bL%p),"first f4 bad coefficient unit");
   check(rows[0].actual_gaussian_residues.f1,String(bL),"first f1 bad coefficient unit");
   fibers.push({b:bb,bL:String(bL),forcing:{c4:String(c4),c1:String(c1)},rows});
  }
  frames.push({p:pp,s,L,maxN,hurwitz_modulus_exponent:precision,fibers});
 }
 return {status:"passed",checks,frames,
  actual_hurwitz_recurrence_used_before_unscaling:true,
  no_gaussian_endpoint_beyond_r_less_than_s:true,
  original_ST_factor_w_kept:true,
  Newton_endpoint_uses_original_first_central_coefficient:true,
  no_nonvanishing_of_designated_forcings_claimed:true,main_target_complete:false};
}
console.log(JSON.stringify(certificate(buildX(91)),null,2));
