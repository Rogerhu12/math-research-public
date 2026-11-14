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
function certificate(A){
 let checks=0;const frames=[];
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const Q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]};
 function check(a,b,label){checks++;if(String(a)!==String(b))throw Error(label+": "+a+" != "+b);}
 for(const pp of [17,23]){
  const p=BigInt(pp),s=(pp+1)/6,N=s-1,M=pp*N,L=(pp*pp-1)/6,m=(pp-1)/2,r0=pp-s;
  const mod=x=>{x=BigInt(x)%p;return x<0n?x+p:x};
  function pow(x,n){x=mod(x);n=BigInt(n);let out=1n;for(;n;n>>=1n,x=x*x%p)if(n&1n)out=out*x%p;return out}
  const inv=x=>pow(x,p-2n);
  function red(v){let a=v[0],b=v[1];if(a===0n)return 0n;while(b%p===0n){if(a%p!==0n)throw Error("actual denominator not canceled");a/=p;b/=p;}return mod(a)*inv(mod(b))%p;}
  const C=[Q(1)],H=[Q(1)];
  for(let n=1;n<=M;n++){
   C[n]=Q(-C[n-1][0]*BigInt(2*n-1),C[n-1][1]*BigInt(2*n));
   H[n]=Q(C[n][0],C[n][1]*BigInt(6*n+1));
  }
  const cm=C.map(red),hm=H.map(red),J=cm.slice(0,s).map((c,n)=>c*inv(1-6*n)%p);
  let fact=[1n];for(let n=1;n<pp;n++)fact[n]=fact[n-1]*BigInt(n)%p;
  const delta=mod(-pow(-1,r0)*inv(pow(4,r0))*fact[2*r0-pp]*inv(fact[r0]*fact[r0]%p));
  check(delta*cm[s]%p,3n,"complete carry constant");
  const P=Array(m+1).fill(0n);
  for(let r=0;r<=m;r++)P[r]=cm[r]*inv(6*r+1)%p;
  const B=Array(s-1).fill(0n);
  for(let j=0;j<=s-2;j++)B[j]=BigInt(2*j+1)*cm[j]%p*inv(6*j+5)%p;
  for(let n=0;n<=M;n++){
   const aa=Math.floor(n/pp),r=n-aa*pp;
   let expected=0n;
   if(r<=m)expected=P[r]*cm[aa]%p;
   if(r===r0)expected=delta*B[aa]%p;
   check(hm[n],expected,"complete original H digit block");
   check(6*n+1<pp*pp,true,"exact denominator window");
  }
  for(let j=1;j<s;j++)check(mod(3n*B[j-1]),mod(J[j]-cm[j]),"J-C equals 3tB");
  const coeff=(a,b,n)=>{let out=0n;for(let j=0;j<=n;j++)out=(out+a[j]*b[n-j])%p;return out;};
  const target=[];
  for(let k=0;k<s;k++){
   const wanted=coeff(cm,J,k);
   check(coeff(cm,hm,pp*k),wanted,"C_p(CH)=CJ full output window");
   check(coeff(hm,hm,pp*k),wanted,"C_p(H^2)=CJ full output window");
   target.push(String(wanted));
  }
  const fibers=[];
  for(const bb of [1,17].filter(b=>b%pp!==0)){
   const b=BigInt(bb),rows=[];
   for(let k=1;k<s;k++){
    const xlow=red(A[k])*pow(b,k)%p;
    const xhigh=red(A[pp*k])*pow(b,pp*k)%p;
    const rhs=mod(-pow(xlow,p)*inv(6*k-1));
    check(xhigh,rhs,"all original p-multiple Weierstrass coefficients");
    check(pp*k<L,true,"original height-two window retained");
    rows.push({k,original_index:pp*k,X_k:String(xlow),X_pk:String(xhigh),rhs:String(rhs)});
   }
   fibers.push({b:bb,rows});
  }
  frames.push({p:pp,s,N,M,L,m,r0,delta:String(delta),C_s:String(cm[s]),
    complete_H_mod_p:hm.map(String),complete_C_mod_p:cm.map(String),
    carry_polynomial:B.map(String),common_Cartier_output:target,fibers});
 }
 return {status:"passed",checks,frames,
   proof_independent_of_sigma_integrality:true,
   all_original_residue_factors_kept:true,
   no_extension_beyond_k_less_than_s:true,
   no_central_nonvanishing_claim:true,main_target_complete:false};
}
console.log(JSON.stringify(certificate(buildX(69)),null,2));
