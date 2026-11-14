// Relative-gradient, full Galerkin Cauchy engine for a fixed rotational metric.
// Author: exact_construction, GPT-6 Astra Pro, AI-assisted, 2026-11-07.
// A numerical local-cell tool; NOT a certified R465 infinite-tail implementation.
// No array printing. E=1+w^2, Z_r=w(1+K), Z_theta=r*w*P.
// State: [P_1,...,P_M, K_0,K_1,...,K_M, mean(Z)].
// P uses sqrt(2)sin(j*spacing*theta); K uses 1,sqrt(2)cos(...).

export function createRelativeTailEngine(options = {}) {
  const M = options.modes ?? 4;
  const spacing = options.spacing ?? 2;
  const N = options.quadrature ?? Math.max(64, 16*M*spacing);
  const floor = options.projectionFloor ?? 0.1;
  if (!Number.isInteger(M)||M<1||M>64||!Number.isInteger(spacing)||spacing<1
      ||!Number.isInteger(N)||N<=4*M*spacing)
    throw new Error("Require 1<=modes<=64, integer spacing, quadrature>4*modes*spacing.");
  const J=M+1, size=2*M+2, ki=M, zi=size-1, rt2=Math.sqrt(2);
  const cs=Array.from({length:N},()=>new Float64Array(J));
  const sn=Array.from({length:N},()=>new Float64Array(M));
  const freq=Float64Array.from({length:M},(_,j)=>(j+1)*spacing);
  for(let n=0;n<N;n++){
    const th=2*Math.PI*n/N;cs[n][0]=1;
    for(let j=0;j<M;j++){cs[n][j+1]=rt2*Math.cos(freq[j]*th);sn[n][j]=rt2*Math.sin(freq[j]*th);}
  }
  function profileData(profile,x) {
    const g=profile(x);
    if(!(g.r>0)||!Number.isFinite(g.drdx)||g.drdx===0
       ||!Number.isFinite(g.logw)||!Number.isFinite(g.dlogwdx))
      throw new Error("Profile requires r>0, finite nonzero drdx, finite logw and dlogwdx.");
    if(g.logw>300)throw new Error("Profile exceeds float64 w^2 range reserved by this prototype.");
    const w=Math.exp(g.logw),w2=Math.exp(2*g.logw);
    return {...g,w,w2,E:1+w2,underflow:(w===0||w2===0)};
  }
  function angles(state,g) {
    if(state.length!==size)throw new Error("Wrong state length.");
    const rows=new Array(N);
    let minD=Infinity,minS=Infinity,minA=Infinity,maxRel=0;
    for(let n=0;n<N;n++){
      let P=0,Pt=0,K=state[ki],Kt=0;
      for(let j=0;j<M;j++){
        P+=state[j]*sn[n][j];Pt+=freq[j]*state[j]*cs[n][j+1];
        K+=state[ki+j+1]*cs[n][j+1];
        Kt-=freq[j]*state[ki+j+1]*sn[n][j];
      }
      const S=1-g.w2*P*P,T=2*K+K*K+g.E*P*P,D=1-g.w2*T;
      const A=1+K+g.E*Pt;
      minD=Math.min(minD,D);minS=Math.min(minS,S);minA=Math.min(minA,A);
      maxRel=Math.max(maxRel,Math.abs(P),Math.abs(K));
      if(!(D>floor&&S>floor&&A>floor))throw new Error("Projection or radial leading coefficient left the certified algebraic branch.");
      const q=Math.sqrt(D),rho=1/(D*q);
      rows[n]={P,Pt,K,Kt,S,T,D,A,q,rho};
    }
    return {rows,minD,minS,minA,maxRel};
  }
  function meanRoot(state,profile,x,opts={}) {
    const y=Float64Array.from(state),g=profileData(profile,x);
    const tol=opts.tolerance??2e-14,limit=opts.maxIterations??30;
    function value(y0) {
      y[ki]=y0;const d=angles(y,g);let f=0,df=0;
      for(const v of d.rows){
        f+=v.T/(v.q*(1+v.q))+(1+v.K)*v.Pt/(v.S*v.q);
        df+=v.A*v.rho;
      }
      return {f:f/N,df:df/N,diagnostics:d};
    }
    let v=value(y[ki]),it=0;
    while(Math.abs(v.f)>tol&&it<limit){
      const old=y[ki],step=-v.f/v.df;
      let next=null;
      for(let k=0;k<24;k++){
        try { const z=value(old+step*Math.pow(0.5,k));
          if(Math.abs(z.f)<Math.abs(v.f)){next=z;break;}
        } catch(e) {}
      }
      if(!next){y[ki]=old;throw new Error("Mean root failed to descend on the positive branch.");}
      v=next;it++;
    }
    if(Math.abs(v.f)>tol)throw new Error("Mean root iteration limit.");
    return {state:y,iterations:it,normalizedHolonomyResidual:v.f,
      physicalHolonomyResidual:g.w2*v.f,derivative:v.df,
      minD:v.diagnostics.minD,minA:v.diagnostics.minA,underflow:g.underflow};
  }
  function choleskySolve(B,b) {
    const L=new Float64Array(J*J);
    for(let i=0;i<J;i++)for(let j=0;j<=i;j++){
      let z=B[i*J+j];for(let k=0;k<j;k++)z-=L[i*J+k]*L[j*J+k];
      if(i===j){if(!(z>0))throw new Error("Galerkin compressed matrix is not SPD.");L[i*J+j]=Math.sqrt(z);}
      else L[i*J+j]=z/L[j*J+j];
    }
    const x=new Float64Array(J),tmp=new Float64Array(J);
    for(let i=0;i<J;i++){let z=b[i];for(let k=0;k<i;k++)z-=L[i*J+k]*tmp[k];tmp[i]=z/L[i*J+i];}
    for(let i=J-1;i>=0;i--){let z=tmp[i];for(let k=i+1;k<J;k++)z-=L[k*J+i]*x[k];x[i]=z/L[i*J+i];}
    return x;
  }
  function rhs(state,profile,x,detail=false) {
    const g=profileData(profile,x),ad=angles(state,g);
    const B=new Float64Array(J*J),b=new Float64Array(J),G=new Float64Array(N);
    for(let n=0;n<N;n++){
      const v=ad.rows[n],lambda=g.dlogwdx;
      const rhsval=g.drdx*g.E/g.r*(v.Kt-v.P)**2
        -lambda*(v.K+v.Pt)+lambda*g.w2*(v.K*v.Pt-v.P*v.P);
      G[n]=rhsval;
      const a=v.rho*v.A/N,c=v.rho*rhsval/N;
      for(let i=0;i<J;i++){b[i]+=c*cs[n][i];for(let j=0;j<=i;j++)B[i*J+j]+=a*cs[n][i]*cs[n][j];}
    }
    for(let i=0;i<J;i++)for(let j=0;j<i;j++)B[j*J+i]=B[i*J+j];
    const kk=choleskySolve(B,b),out=new Float64Array(size);
    for(let j=0;j<M;j++)
      out[j]=g.drdx/g.r*(-freq[j]*state[ki+j+1]-state[j])-g.dlogwdx*state[j];
    for(let j=0;j<J;j++)out[ki+j]=kk[j]-g.dlogwdx*state[ki+j];
    out[zi]=g.drdx*g.w*(1+state[ki]);
    if(!detail)return out;
    let maxD=0,maxFormalCurvature=0,hol=0;
    const perAngle=new Array(N);
    for(let n=0;n<N;n++){
      const v=ad.rows[n];let Kx=0;
      for(let j=0;j<J;j++)Kx+=out[ki+j]*cs[n][j];
      const defect=v.A*(Kx+g.dlogwdx*v.K)-G[n];
      const darboux=g.w2*defect/(g.E*g.E*g.r*g.drdx);
      maxD=Math.max(maxD,Math.abs(darboux));
      hol+=v.T/(v.q*(1+v.q))+(1+v.K)*v.Pt/(v.S*v.q);
      const Kr=Kx/g.drdx,wp=g.w*g.dlogwdx/g.drdx;
      const a=(wp*(1+v.K)/(g.E*g.E)+g.w*Kr/g.E)*Math.sqrt(g.E)/v.q;
      const bcur=g.w*(v.Kt-v.P)/(g.r*v.q);
      const c=g.w/g.r*(v.Pt+(1+v.K)/g.E)*Math.sqrt(g.E)/v.q;
      const dis=Math.hypot(a-c,2*bcur);
      maxFormalCurvature=Math.max(maxFormalCurvature,Math.abs((a+c+dis)/2),Math.abs((a+c-dis)/2));
      perAngle[n]={theta:2*Math.PI*n/N,ur:g.w*(1+v.K),ut:g.r*g.w*v.P,
        urr:wp*(1+v.K)+g.w*Kr,urt:g.w*v.Kt,utt:g.r*g.w*v.Pt,darboux};
    }
    return {derivative:out,minD:ad.minD,minS:ad.minS,minA:ad.minA,
      normalizedHolonomyResidual:hol/N,physicalHolonomyResidual:g.w2*hol/N,
      maxDarboux:maxD,formalHeightCurvature:maxFormalCurvature,
      curvatureIsActualOnlyIfExactDarboux:true,underflow:g.underflow,
      backgroundCurvature:Math.max(Math.abs(g.w*g.dlogwdx/g.drdx)/(g.E**1.5),g.w/(g.r*Math.sqrt(g.E))),
      perAngle};
  }
  function rk4(state,profile,x,h) {
    const y=Float64Array.from(state),tmp=new Float64Array(size),a=rhs(y,profile,x);
    for(let i=0;i<size;i++)tmp[i]=y[i]+h*a[i]/2;
    const b=rhs(tmp,profile,x+h/2);
    for(let i=0;i<size;i++)tmp[i]=y[i]+h*b[i]/2;
    const c=rhs(tmp,profile,x+h/2);
    for(let i=0;i<size;i++)tmp[i]=y[i]+h*c[i];
    const d=rhs(tmp,profile,x+h);
    for(let i=0;i<size;i++)y[i]+=h*(a[i]+2*b[i]+2*c[i]+d[i])/6;
    return y;
  }
  function integrate(state,profile,opts={}) {
    const x0=opts.x0??0,x1=opts.x1??1,steps=opts.steps??64;
    if(!Number.isInteger(steps)||steps<1)throw new Error("steps must be positive integer.");
    let y=Float64Array.from(state),maxD=0,maxHol=0,minD=Infinity,minA=Infinity,maxKap=0,underflow=false;
    const h=(x1-x0)/steps;
    function check(x){const z=rhs(y,profile,x,true);maxD=Math.max(maxD,z.maxDarboux);
      maxHol=Math.max(maxHol,Math.abs(z.physicalHolonomyResidual));
      minD=Math.min(minD,z.minD);minA=Math.min(minA,z.minA);
      maxKap=Math.max(maxKap,z.formalHeightCurvature);underflow ||= z.underflow;}
    check(x0);
    for(let n=0;n<steps;n++){y=rk4(y,profile,x0+n*h,h);if(opts.auditEveryStep!==false||n===steps-1)check(x0+(n+1)*h);}
    return {state:y,steps,maxDarboux:maxD,maxPhysicalHolonomyResidual:maxHol,minD,minA,
      formalHeightCurvature:maxKap,underflow};
  }
  function fromHeightCos(profile,x,cosCoefficients,radialCoefficients,meanHeight=0) {
    const g=profileData(profile,x),y=new Float64Array(size);
    if(!(g.w>0))throw new Error("Physical-to-relative conversion underflow; provide relative state directly.");
    for(let j=0;j<M;j++){
      const c=cosCoefficients[j]??0,d=radialCoefficients[j]??0;
      y[j]=-freq[j]*c/(rt2*g.r*g.w);y[ki+j+1]=d/(rt2*g.w);
    }
    y[zi]=meanHeight;
    return meanRoot(y,profile,x);
  }
  function toPort(state,profile,x) {
    const g=profileData(profile,x),height=new Float64Array(M),radial=new Float64Array(M);
    for(let j=0;j<M;j++){height[j]=-rt2*g.r*g.w*state[j]/freq[j];radial[j]=rt2*g.w*state[ki+j+1];}
    return {r:g.r,w:g.w,logw:g.logw,heightCos:height,radialCos:radial,
      meanHeight:state[zi],meanRadial:g.w*(1+state[ki]),underflow:g.underflow};
  }

  function rawToState(raw,profile,x,meanHeight=0) {
    if(raw.length!==2*M)throw new Error("Raw state requires M Q coefficients followed by M eta coefficients.");
    const g=profileData(profile,x),cc=new Float64Array(M),dd=new Float64Array(M);
    for(let j=0;j<M;j++){cc[j]=g.r**4*raw[j];dd[j]=g.r**3*(Math.sqrt(12)*raw[M+j]+freq[j]**2*raw[j]);}
    return fromHeightCos(profile,x,cc,dd,meanHeight);
  }
  function stateToRaw(state,profile,x) {
    const p=toPort(state,profile,x),raw=new Float64Array(2*M);
    for(let j=0;j<M;j++){
      raw[j]=p.heightCos[j]/p.r**4;
      raw[M+j]=(p.radialCos[j]/p.r**3-freq[j]**2*raw[j])/Math.sqrt(12);
    }
    return raw;
  }
  function flowRawCell(raw,segments,opts={}) {
    if(!Array.isArray(segments)||segments.length===0)throw new Error("At least one fixed profile segment required.");
    const root=rawToState(raw,segments[0],0,opts.meanHeight??0);
    let state=root.state,maxD=0,maxPhi=0,minD=Infinity,minA=Infinity,underflow=false;
    let maxJoinPositionError=0,maxJoinLogwError=0,maxJoinLogSlopeError=0;
    for(let k=0;k<segments.length;k++){
      if(k){
        const a=profileData(segments[k-1],1),b=profileData(segments[k],0);
        const er=Math.abs(a.r-b.r),ew=Math.abs(a.logw-b.logw);
        const es=Math.abs(a.dlogwdx/a.drdx-b.dlogwdx/b.drdx);
        maxJoinPositionError=Math.max(maxJoinPositionError,er);
        maxJoinLogwError=Math.max(maxJoinLogwError,ew);
        maxJoinLogSlopeError=Math.max(maxJoinLogSlopeError,es);
        const tol=opts.joinTolerance??1e-10;
        if(er>tol*Math.max(1,a.r,b.r)||ew>tol||es>tol*Math.max(1,Math.abs(a.dlogwdx/a.drdx),Math.abs(b.dlogwdx/b.drdx)))
          throw new Error("Cell profile pieces do not match r, log w and physical first derivative.");
      }
      const rr=integrate(state,segments[k],{steps:opts.stepsPerSegment??64,auditEveryStep:opts.auditEveryStep});
      state=rr.state;maxD=Math.max(maxD,rr.maxDarboux);maxPhi=Math.max(maxPhi,rr.maxPhysicalHolonomyResidual);
      minD=Math.min(minD,rr.minD);minA=Math.min(minA,rr.minA);underflow ||= rr.underflow;
    }
    return {raw:stateToRaw(state,segments.at(-1),1),state,
      port:toPort(state,segments.at(-1),1),initialMean:root.state[ki],
      maxDarboux:maxD,maxPhi,minD,minA,underflow,
      maxJoinPositionError,maxJoinLogwError,maxJoinLogSlopeError};
  }

  return {M,spacing,N,size,meanIndex:ki,heightIndex:zi,frequencies:freq,
    meanRoot,rhs,rk4,integrate,fromHeightCos,toPort,rawToState,stateToRaw,flowRawCell};
}

export function constantSlopeProfile(r0,r1,w) {
  if(!(r0>0&&r1>0&&r0!==r1&&w>0))throw new Error("Invalid constant-slope profile.");
  return x=>({r:r0+(r1-r0)*x,drdx:r1-r0,logw:Math.log(w),dlogwdx:0});
}
export function constantPProfile(r0,r1,logP) {
  if(!(r0>0&&r1>0&&r0!==r1&&Number.isFinite(logP)))throw new Error("Invalid constant-P profile.");
  return x=>{const r=r0+(r1-r0)*x,drdx=r1-r0;return {r,drdx,logw:logP-7*Math.log(r),dlogwdx:-7*drdx/r};};
}

// General dependency recursion. map(n, raw) must be the same fixed actual
// nonlinear cell map (including the complete mean lift) at every depth.
export function composeTailAtCut(cut,depth,q,targetAt,map) {
  if(!Number.isInteger(cut)||!Number.isInteger(depth)||depth<0)throw new Error("Invalid cut/depth.");
  let raw=Float64Array.from(targetAt(cut+depth),x=>q*x);
  for(let n=cut+depth;n>cut;n--)raw=Float64Array.from(map(n,raw));
  const linear=targetAt(cut);
  if(raw.length!==linear.length)throw new Error("Raw dimension mismatch.");
  return {raw,correction:Float64Array.from(raw,(x,j)=>x-q*linear[j])};
}
export function contractionRemainder(kappa,ballRadius,depth,weightAtCut=1,physicalJetLipschitz=1) {
  if(!(kappa>=0&&kappa<1&&ballRadius>=0&&Number.isInteger(depth)&&depth>=0
      &&weightAtCut>=0&&physicalJetLipschitz>=0))throw new Error("Invalid certified contraction inputs.");
  return {weightedError:ballRadius*kappa**depth,
    rawError:weightAtCut*ballRadius*kappa**depth,
    physicalJetError:physicalJetLipschitz*weightAtCut*ballRadius*kappa**depth};
}
