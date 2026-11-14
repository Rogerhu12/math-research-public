// Local Jacobian prototype. No flow/solver entry is exported: the live workers
// retain their original code. Products of resolved sine/cosine basis functions
// are assembled from six sets of discrete Fourier moments.
export function createFourierProductJacobianEngine(options,base){
 const M=options.modes,N=options.quadrature,spacing=options.spacing??2,J=M+1,K=2*M,
  size=2*M+2,mu=options.mu,orientation=options.orientation??1,sq2=Math.sqrt(2),sq12=Math.sqrt(12);
 if(base.M!==M||base.N!==N||N<=4*spacing*M)throw Error('Resolved original base required');
 const freq=Float64Array.from({length:M},(_,j)=>spacing*(j+1)),
  cos=Array.from({length:N},(_,n)=>Float64Array.from({length:2*M+1},(_,j)=>Math.cos(spacing*j*2*Math.PI*n/N))),
  sin=Array.from({length:N},(_,n)=>Float64Array.from({length:2*M+1},(_,j)=>Math.sin(spacing*j*2*Math.PI*n/N)));
 const CC=(v,i,j)=>i===0?(j===0?v[0]:sq2*v[j]):j===0?sq2*v[i]:v[Math.abs(i-j)]+v[i+j];
 const SS=(v,i,j)=>v[Math.abs(i-j)]-v[i+j];
 const odd=(v,k)=>k<0?-v[-k]:v[k];
 const CS=(v,i,j)=>i===0?sq2*v[j]:v[i+j]+odd(v,j-i);
 const SC=(v,i,j)=>j===0?sq2*v[i]:v[i+j]+odd(v,i-j);
 function solveMany(B,R){
  const L=new Float64Array(J*J),X=Float64Array.from(R);
  for(let i=0;i<J;i++)for(let j=0;j<=i;j++){let v=B[i*J+j];for(let k=0;k<j;k++)v-=L[i*J+k]*L[j*J+k];if(i===j){if(!(v>0))throw Error('Fourier-product Jacobian not positive');L[i*J+j]=Math.sqrt(v);}else L[i*J+j]=v/L[j*J+j];}
  for(let i=0;i<J;i++)for(let col=0;col<K;col++){let v=X[i*K+col];for(let k=0;k<i;k++)v-=L[i*J+k]*X[k*K+col];X[i*K+col]=v/L[i*J+i];}
  for(let i=J-1;i>=0;i--)for(let col=0;col<K;col++){let v=X[i*K+col];for(let k=i+1;k<J;k++)v-=L[k*J+i]*X[k*K+col];X[i*K+col]=v/L[i*J+i];}return X;
 }
 function rhsWithJacobian(state,profile,x){
  const rt=base.root(state,profile,x),g=rt.g,derivative=base.rhs(state,profile,x,false,rt),sigma=g.drdx/g.r,
   pref=g.momentumFluxFactor,targetFac=g.momentumTargetFactor,pFac=g.momentumPFactor,
   FPm=new Float64Array(2*M+1),FTm=new Float64Array(2*M+1),CKm=new Float64Array(2*M+1),
   CUm=new Float64Array(2*M+1),CPm=new Float64Array(2*M+1),bmM=new Float64Array(2*M+1);
  for(let n=0;n<N;n++){
   const v=rt.e.rows[n];let FP,FT,CK,CU,CP,bm;
   if(!g.deepScaled){
    const omega=1+g.w2*(v.L+v.quad),rho=1/(v.D*v.sd);
    FP=g.E*v.P*omega/v.D+2*g.w2*(1+v.K)*v.Pt*v.P/(v.S*v.S*v.sd);
    FT=-(g.E*v.Pt+g.w2*(1+v.K)*(g.w2*v.P*v.P+2*v.K+v.K*v.K)/v.S)*rho;
    const flux=(1+v.K)*v.U/(v.S*v.sd);CK=v.U/(v.S*v.sd)+flux*g.w2*(1+v.K)/v.D;
    const u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P);CU=(v.K+u/(1+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd);
    CP=flux*(2*g.w2*v.P/v.S+g.w2*g.E*v.P/v.D);
    const am=v.L+g.w2*v.Pt;bm=am+(1+am)*Math.expm1(-1.5*Math.log1p(-u));
   }else{
    const wp=g.w*v.P,wk=g.w*v.K,wpt=g.w*v.Pt,
     omega=1+g.w*(g.w*(v.L+v.quad)),rho=1/(v.D*v.sd),
     u=2*g.w*wk+wk*wk+g.E*wp*wp;
    FP=g.E*v.P*omega/v.D+2*(1+v.K)*wpt*wp/(v.S*v.S*v.sd);
    FT=-(g.E*v.Pt+(1+v.K)*(g.w*(g.w*wp*wp)+2*g.w*wk+wk*wk)/v.S)*rho;
    const flux=(1+v.K)*v.U/(v.S*v.sd);
    CK=v.U/(v.S*v.sd)+flux*g.w*(g.w*(1+v.K))/v.D;
    CU=(v.K+u/(1+v.sd)+wp*wp*v.sd)/(v.S*v.sd);
    CP=flux*(2*g.w*wp/v.S+g.w*g.E*wp/v.D);
    const am=v.L+g.w*wpt;bm=am+(1+am)*Math.expm1(-1.5*Math.log1p(-u));
   }
   for(let k=0;k<=2*M;k++){const c=cos[n][k]/N,s=sin[n][k]/N;FPm[k]+=FP*s;CKm[k]+=CK*s;FTm[k]+=FT*c;CUm[k]+=CU*c;CPm[k]+=CP*c;bmM[k]+=bm*c;}
  }
  // For a deep cell solve B*(pref*dL)=pref*right directly.
  // pref*targetFac=dr/r; no vanishing pref or enormous dL is formed separately.
  const pf=g.deepScaled?g.momentumFluxTimesP:pFac,tf=g.deepScaled?sigma:targetFac;
  const right=new Float64Array(J*K),FL=new Float64Array(M*J),FQ=new Float64Array(M*M);
  for(let i=0;i<J;i++)for(let j=0;j<M;j++){const f=freq[j];right[i*K+j]=pf*(f*CS(FPm,i,j+1)+f*f*CC(FTm,i,j+1));right[i*K+M+j]=-tf*CC(bmM,i,j+1);}
  for(let i=0;i<M;i++){FL[i*J]=SC(CKm,i+1,0);for(let j=0;j<M;j++){const f=freq[j],ck=SC(CKm,i+1,j+1),cu=SS(CUm,i+1,j+1);FL[i*J+j+1]=ck-f*cu;FQ[i*M+j]=pf*(-f*(SS(CPm,i+1,j+1)+(f*f-1)*cu)+f*f*ck);}}
  const dL=solveMany(rt.e.B,right),jacobian=new Float64Array(size*K);
  if(g.deepScaled){
   for(let j=0;j<M;j++)for(let col=0;col<K;col++){
    const f=freq[j];
    let pdf=-f*dL[(j+1)*K+col]+(col<M?FQ[j*M+col]:FL[j*J+col-M+1]*sigma);
    for(let i=0;i<J;i++)pdf+=FL[j*J+i]*dL[i*K+col];
    jacobian[j*K+col]=(col===j?(f*f-4)*sigma:0)+g.momentumScaledQFactor*dL[(j+1)*K+col]+(col===M+j?g.momentumLinearPiQFactor:0);
    jacobian[(M+j)*K+col]=(col===M+j?(4-f*f)*sigma:0)+(col===j?-g.momentumFluxTimesP*f*f*(f*f-1):0)+f*pdf;
   }
   for(let col=0;col<K;col++)jacobian[2*M*K+col]=g.momentumScaledMeanFactor*dL[col];
   if(!jacobian.every(Number.isFinite))throw Error('Combined momentum Jacobian outside binary64 range');
   return {derivative,jacobian,root:rt};
  }
  for(let j=0;j<M;j++)for(let col=0;col<K;col++){
   let df=-freq[j]*dL[(j+1)*K+col]+(col<M?FQ[j*M+col]:FL[j*J+col-M+1]*targetFac);
   for(let i=0;i<J;i++)df+=FL[j*J+i]*dL[i*K+col];
   jacobian[j*K+col]=sigma*((col===j?freq[j]*freq[j]-4:0)+sq2*g.w*(dL[(j+1)*K+col]+(col===M+j?targetFac:0))/g.r**3);
   jacobian[(M+j)*K+col]=(col===M+j?(4-freq[j]*freq[j])*sigma:0)+(col===j?-pref*freq[j]*freq[j]*(freq[j]*freq[j]-1)*pFac:0)+pref*freq[j]*df;
  }
  for(let col=0;col<K;col++)jacobian[2*M*K+col]=g.drdx*g.w*dL[col];
  return {derivative,jacobian,root:rt};
 }
 return {rhsWithJacobian,scope:'local prototype only; no flow entry'};
}
