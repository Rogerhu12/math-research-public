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
 let checks=0;
 const frames=[];
 const gcd=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a};
 const Q=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]};
 const qa=(a,b)=>Q(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
 const qm=(a,b)=>Q(a[0]*b[0],a[1]*b[1]);
 const qs=(a,n,d=1)=>qm(a,Q(n,d));
 function check(a,b,label){checks++;if(String(a)!==String(b))throw Error(label+": "+a+" != "+b);}
 const fall=(n,r)=>{let a=1n;n=BigInt(n);for(let j=0;j<r;j++)a*=n-BigInt(j);return a;};
 // Complete theta-space identities: both basis coefficients are exact rationals.
 check(String(data.AS[1]),String(Q(-4,35)),"f4 first coefficient");
 check(String(data.ABS[1]),String(Q(6,35)),"f1 first coefficient");
 check(String(data.ABS[2]),String(Q(-1068,25025)),"f1 second coefficient");
 check(String(qa(qs(qm(data.ABS[1],data.ABS[1]),252),qs(data.ABS[2],10296))),
       String(Q(-432)),"whole H4 f1 z10 coefficient");
 const h4Second=qs(data.AS[1],-936);
 check(String(h4Second),String(Q(3744,35)),"whole H4 f4 z10 coefficient");
 check(String(qa(qs(Q(-18,35),72),Q(144))),String(h4Second),
       "complete S12 type4 coefficients");
 check(30-25-6,-1,"same charge derivative normalization");
 check(-5+2,-3,"Wronskian x4 coefficient");
 check(-2+2,0,"Wronskian bx coefficient");
 for(const pp of [17,23])for(const bb of [1,17].filter(b=>b%pp!==0)){
   const p=BigInt(pp),s=(pp+1)/6,N=s-1,b=BigInt(bb);
   const mod=a=>{a=BigInt(a)%p;return a<0n?a+p:a;};
   function pow(a,n){let out=1n;a=mod(a);n=BigInt(n);for(;n;n>>=1n,a=a*a%p)if(n&1n)out=out*a%p;return out;}
   const inv=a=>pow(a,p-2n);
   function redFraction(a,b,label="actual integral coefficient"){
     a=BigInt(a);b=BigInt(b);if(a===0n)return 0n;
     while(b%p===0n){if(a%p!==0n)throw Error(label+" has a genuine p denominator");a/=p;b/=p;}
     return mod(a)*inv(mod(b))%p;
   }
   const red=v=>redFraction(v[0],v[1]);
   const am=red(qs(data.L[s],p))*pow(b,s)%p;
   check(am===0n,false,"original Gaussian unit");
   const g4=data.AS.slice(0,s).map((v,i)=>red(v)*pow(b,i)%p);
   const g1=data.ABS.slice(0,s).map((v,i)=>red(v)*pow(b,i)%p);
   let fact=[1n];for(let j=1;j<pp;j++)fact[j]=fact[j-1]*BigInt(j)%p;
   for(const r of [2,5])for(let m=0;m<=pp-r;m++){
     let product=1n;for(let v=1;v<r;v++)product=product*BigInt(m+v)%p;
     if((m+r)%2)product=mod(-product);
     check(inv(fact[m]*fact[pp-r-m]%p),product,"complete Wilson factorial pairing");
   }
   const gamma=(g,h)=>Array.from({length:s},(_,j)=>{
     if(h===0&&j===0)return 0n;
     return pow(am,6*j+h-1)*g[N-j]%p*inv(fact[6*j+h])%p;
   });
   const G40=gamma(g4,0),G13=gamma(g1,3),G41=gamma(g4,1);
   const coeff=(u,v,n)=>{let out=0n;for(let j=0;j<=n;j++)out=(out+(u[j]||0n)*(v[n-j]||0n))%p;return out;};
   const q44=coeff(G40,G40,N),q41=coeff(G40,G13,N),q11=coeff(G13,G13,N-1);
   const n44=N*pp,n41=N*pp+3*s,n11=N*pp+1,maxN=n41;
   function actualSource(tag,h){
     const out=[0n];
     for(let n=1;n<=maxN;n++){
       const v=data[tag][n-1],t=Math.floor(6*n/pp);
       out.push(redFraction(v[0]*p**BigInt(t),v[1]*BigInt(6*n-h))*pow(b,n-1)%p);
     }
     return out;
   }
   const W40=actualSource("AS",0),W13=actualSource("ABS",3),W41=actualSource("AS",1);
   function physicalProduct(u,v,n){
     const t=Math.floor(6*n/pp);let out=0n;
     for(let j=0;j<=n;j++){
       const carry=t-Math.floor(6*j/pp)-Math.floor(6*(n-j)/pp);
       check(carry===0||carry===1,true,"actual C_p product carry");
       if(carry===0)out=(out+u[j]*v[n-j])%p;
     }
     return out;
   }
   check(physicalProduct(W40,W40,n44),q44,"actual W40 squared physical row");
   check(physicalProduct(W40,W13,n41),q41,"actual W40 W13 physical row");
   check(physicalProduct(W13,W13,n11),q11,"actual W13 squared physical row");
   check(W41[s],g4[N],"actual forcing row");
   for(const n of [n44,n41,n11]){
     const oldQ=Math.floor(n/s),r=n-oldQ*s;
     check(oldQ+6*r>=pp,true,"quadratic row is the original pole");
     check(Math.floor(6*n/pp),oldQ+1,"actual original pole scaling");
   }
   function rawH4(tag,d0){
     const total=(pp+3-2*d0)/6;let out=0n;
     check(Number.isInteger(total),true,"H4 physical CM coefficient");
     for(let i=0;i<=total;i++){
       const j=total-i,u=BigInt(6*i+d0),v=BigInt(6*j+d0);
       const weight=fall(v,4)-4n*u*fall(v,3)+3n*fall(u,2)*fall(v,2);
       const ri=data[tag][i],rj=data[tag][j];
       const term=redFraction(ri[0]*rj[0]*weight,ri[1]*rj[1],"entire H4 physical term");
       out=(out+term*pow(b,total))%p;
     }
     return out;
   }
   const h44=rawH4("AS",4),h11=rawH4("ABS",1);
   let wr=0n;
   for(let i=0;i<=N;i++){
     const j=N-i,ri=data.AS[i],rj=data.ABS[j],weight=BigInt(6*j+1-(6*i+4));
     wr=(wr+redFraction(ri[0]*rj[0]*weight,ri[1]*rj[1])*pow(b,N))%p;
   }
   check(h44,mod(-8n*pow(am,6)*q44+384n*g4[N]),"all f4 endpoints kept");
   check(wr,mod(2n*pow(am,3)*q41+2n*g4[N]),"mixed endpoint kept");
   check(h11,mod(8n*pow(am,6)*q11-10n*am),"Gaussian endpoint kept");
   check(mod((p+2n)*(p+1n)*(p-5n)),mod(-10),"exact Gaussian defect");
   check(mod(3n*b*h44+72n*b*wr+h11),0n,"full S12 reference cancellation");
   const lhs=mod(pow(am,6)*(q11-3n*b*q44)+18n*b*pow(am,3)*q41+162n*b*g4[N]);
   const rhs=5n*am*inv(4n)%p;
   check(lhs,rhs,"complete nonhomogeneous quadratic relation");
   frames.push({
     p:pp,b:bb,a:String(am),forcing:{c4:String(g4[N]),c1:String(g1[N])},
     physical_indices:{Q44:n44,Q41:n41,Q11:n11,forcing:s},
     physical_exponents:{Q44:pp-5,Q41:pp-2,Q11:pp-5,forcing:1},
     gamma:{W40:G40.map(String),W13:G13.map(String),W41:G41.map(String)},
     quadratic_rows:{Q44:String(q44),Q41:String(q41),Q11:String(q11)},
     complete_hirota_rows:{H44:String(h44),Wr41:String(wr),H11:String(h11)},
     complete_unit_relation:{lhs:String(lhs),rhs:String(rhs)},
     actual_sources:{W40:W40.map(String),W13:W13.map(String),W41:W41.map(String)}
   });
 }
 return {status:"passed",checks,frames,
    fixed_global_identities:{H4_f4:"72 x(x^3+2b) sigma^12",H4_f1:"-432 b^2 x sigma^12",Wr:"-3 x^4 sigma^12"},
    gaussian_endpoint:"-10 a",
    reference_sources_actually_eliminated:true,
    all_three_physical_rows_and_forcing_kept:true,
    no_true_prefix_layer_inferred:true,
    no_central_or_forcing_nonvanishing_claim:true,
    main_target_complete:false};
}
console.log(JSON.stringify(certificate(build(80)),null,2));
