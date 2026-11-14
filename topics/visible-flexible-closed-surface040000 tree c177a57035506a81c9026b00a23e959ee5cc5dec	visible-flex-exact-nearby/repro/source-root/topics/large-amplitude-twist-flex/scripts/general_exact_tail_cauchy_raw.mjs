import {createRelativeTailEngine} from "./general_exact_tail_cauchy.mjs";

// Physical raw-coordinate implementation of the SAME full Galerkin equation.
// Author: exact_construction, GPT-6 Astra Pro, AI-assisted, 2026-11-07.
// It removes coordinate-induced large linear growth of relative states.
// No infinite-tail certification or actual embedding follows from this tool.
// State = [Q_1..Q_M, eta_1..eta_M, mean(v_r), mean(Z)].
// Q=C/r^4, eta=(C'/r^3-m^2 Q)/sqrt(12), physical y=sqrt(12)log r.
export function createRawTailEngine(options={}) {
 const relative=createRelativeTailEngine(options), M=relative.M,N=relative.N;
 const frequencies=relative.frequencies,J=M+1,size=2*M+2,mi=2*M,zi=mi+1;
 const sq2=Math.sqrt(2),sq12=Math.sqrt(12),floor=options.projectionFloor??.1;
 const cs=Array.from({length:N},()=>new Float64Array(J));
 const sn=Array.from({length:N},()=>new Float64Array(M));
 for(let n=0;n<N;n++){const theta=2*Math.PI*n/N;cs[n][0]=1;
  for(let j=0;j<M;j++){cs[n][j+1]=sq2*Math.cos(frequencies[j]*theta);sn[n][j]=sq2*Math.sin(frequencies[j]*theta);}}
 function profileData(profile,x) {
  const g=profile(x),w=Math.exp(g.logw),w2=w*w;
  if(!(g.r>0&&w>0)||!Number.isFinite(w2)||!Number.isFinite(g.drdx)||g.drdx===0||!Number.isFinite(g.dlogwdx))
   throw new Error("Raw coordinates require finite r>0,w>0,w^2 and nonzero drdx.");
  return {...g,w,w2,E:1+w2};
 }
 function toRelative(state,profile,x) {
  const g=profileData(profile,x),y=new Float64Array(size),fac=g.r**3/(sq2*g.w);
  for(let j=0;j<M;j++){
   const m=frequencies[j];y[j]=-m*fac*state[j];
   y[M+j+1]=fac*(sq12*state[M+j]+m*m*state[j]);
  }
  y[M]=state[mi]/g.w;y[zi]=state[zi];return y;
 }
 function fromRelative(state,profile,x) {
  const raw=relative.stateToRaw(state,profile,x),g=profileData(profile,x);
  const y=new Float64Array(size);y.set(raw);y[mi]=g.w*state[M];y[zi]=state[zi];return y;
 }
 function initialize(raw,profile,x=0,meanHeight=0) {
  const root=relative.rawToState(raw,profile,x,meanHeight);
  const state=fromRelative(root.state,profile,x);
  // Preserve specified raw Cauchy input exactly through the mean lift.
  state.set(raw);
  return {...root,state,meanRelative:root.state[M]};
 }
 function solveSPD(B,b) {
  const L=new Float64Array(J*J);
  for(let i=0;i<J;i++)for(let j=0;j<=i;j++){
   let z=B[i*J+j];for(let k=0;k<j;k++)z-=L[i*J+k]*L[j*J+k];
   if(i===j){if(!(z>0))throw new Error("Compressed matrix not SPD.");L[i*J+j]=Math.sqrt(z);}
   else L[i*J+j]=z/L[j*J+j];
  }
  const tmp=new Float64Array(J),out=new Float64Array(J);
  for(let i=0;i<J;i++){let z=b[i];for(let k=0;k<i;k++)z-=L[i*J+k]*tmp[k];tmp[i]=z/L[i*J+i];}
  for(let i=J-1;i>=0;i--){let z=tmp[i];for(let k=i+1;k<J;k++)z-=L[k*J+i]*out[k];out[i]=z/L[i*J+i];}
  return out;
 }
 function rhs(state,profile,x,detail=false) {
  if(state.length!==size)throw new Error("Wrong raw state length.");
  const g=profileData(profile,x),fac=g.r**3/(sq2*g.w);
  const pc=new Float64Array(M),kc=new Float64Array(J),lc=new Float64Array(J),uc=new Float64Array(M);
  kc[0]=lc[0]=state[mi]/g.w;
  for(let j=0;j<M;j++){
   const m=frequencies[j],Q=state[j],eta=state[M+j];
   pc[j]=-m*fac*Q;kc[j+1]=fac*(sq12*eta+m*m*Q);
   lc[j+1]=sq12*fac*eta;uc[j]=-m*fac*(sq12*eta+(m*m-1)*Q);
  }
  const B=new Float64Array(J*J),bb=new Float64Array(J),rows=new Array(N);
  let minD=Infinity,minS=Infinity,minA=Infinity;
  for(let n=0;n<N;n++){
   let P=0,Pt=0,K=kc[0],L=lc[0],U=0;
   for(let j=0;j<M;j++){
    P+=pc[j]*sn[n][j];Pt+=frequencies[j]*pc[j]*cs[n][j+1];
    K+=kc[j+1]*cs[n][j+1];L+=lc[j+1]*cs[n][j+1];U+=uc[j]*sn[n][j];
   }
   const S=1-g.w2*P*P,T=2*K+K*K+g.E*P*P,D=1-g.w2*T;
   const A=1+L+g.w2*Pt,sqrtD=Math.sqrt(D),rho=1/(D*sqrtD);
   if(!(D>floor&&S>floor&&A>floor))throw new Error("Projection or radial leading coefficient outside positive branch.");
   minD=Math.min(minD,D);minS=Math.min(minS,S);minA=Math.min(minA,A);
   const G=g.drdx*g.E/g.r*U*U-g.dlogwdx*L+g.dlogwdx*g.w2*(K*Pt-P*P);
   for(let i=0;i<J;i++){bb[i]+=rho*G*cs[n][i]/N;
    for(let j=0;j<=i;j++)B[i*J+j]+=rho*A*cs[n][i]*cs[n][j]/N;}
   rows[n]={P,Pt,K,L,U,S,T,D,A,sqrtD,G};
  }
  for(let i=0;i<J;i++)for(let j=0;j<i;j++)B[j*J+i]=B[i*J+j];
  const b=solveSPD(B,bb),out=new Float64Array(size),sr=g.drdx/g.r;
  for(let j=0;j<M;j++){
   const m=frequencies[j],m2=m*m;
   out[j]=sr*((m2-4)*state[j]+sq12*state[M+j]);
   out[M+j]=sq2*g.w/(sq12*g.r**3)*b[j+1]
       -sr*((m2+3)*state[M+j]+m2*(m2-1)/sq12*state[j]);
  }
  out[mi]=g.w*b[0];out[zi]=g.drdx*(g.w+state[mi]);
  if(!detail)return out;
  let maxDarboux=0,maxFormalCurvature=0,hol=0,maxHeight=0,minHeight=Infinity,maxHeightValue=-Infinity;
  const perAngle=new Array(N);
  for(let n=0;n<N;n++){
   const v=rows[n];let bv=0,hv=0;
   for(let j=0;j<J;j++)bv+=b[j]*cs[n][j];
   for(let j=0;j<M;j++)hv+=g.r**4*state[j]*cs[n][j+1]/sq2;
   const defect=v.A*bv-v.G,darboux=g.w2*defect/(g.E*g.E*g.r*g.drdx);
   const urr=g.w*g.dlogwdx/g.drdx+g.w*bv/g.drdx;
   const ur=g.w*(1+v.K),ut=g.r*g.w*v.P,urt=g.w*(v.U+v.P),utt=g.r*g.w*v.Pt;
   const hrr=(urr-(g.w*g.w*g.dlogwdx/(g.E*g.drdx))*ur)/g.E;
   const a=hrr*Math.sqrt(g.E)/v.sqrtD;
   const bc=g.w*v.U/(g.r*v.sqrtD);
   const c=g.w/g.r*(v.Pt+(1+v.K)/g.E)*Math.sqrt(g.E)/v.sqrtD;
   const disc=Math.hypot(a-c,2*bc);
   maxDarboux=Math.max(maxDarboux,Math.abs(darboux));
   maxFormalCurvature=Math.max(maxFormalCurvature,Math.abs((a+c+disc)/2),Math.abs((a+c-disc)/2));
   hol+=v.T/(v.sqrtD*(1+v.sqrtD))+(1+v.K)*v.Pt/(v.S*v.sqrtD);
   maxHeight=Math.max(maxHeight,Math.abs(hv));minHeight=Math.min(minHeight,hv);maxHeightValue=Math.max(maxHeightValue,hv);
   perAngle[n]={theta:2*Math.PI*n/N,ur,ut,urr,urt,utt,darboux,height:state[zi]+hv};
  }
  return {derivative:out,minD,minS,minA,normalizedHolonomyResidual:hol/N,
   physicalHolonomyResidual:g.w2*hol/N,maxDarboux,formalHeightCurvature:maxFormalCurvature,
   curvatureIsActualOnlyIfExactDarboux:true,maxHeightOscillation:maxHeight,peakValley:maxHeightValue-minHeight,
   backgroundCurvature:Math.max(Math.abs(g.w*g.dlogwdx/g.drdx)/(g.E**1.5),g.w/(g.r*Math.sqrt(g.E))),
   perAngle};
 }
 function rk4(state,profile,x,h) {
  const y=Float64Array.from(state),tmp=new Float64Array(size),a=rhs(y,profile,x);
  for(let i=0;i<size;i++)tmp[i]=y[i]+h*a[i]/2;const b=rhs(tmp,profile,x+h/2);
  for(let i=0;i<size;i++)tmp[i]=y[i]+h*b[i]/2;const c=rhs(tmp,profile,x+h/2);
  for(let i=0;i<size;i++)tmp[i]=y[i]+h*c[i];const d=rhs(tmp,profile,x+h);
  for(let i=0;i<size;i++)y[i]+=h*(a[i]+2*b[i]+2*c[i]+d[i])/6;
  return y;
 }
 function toPort(state,profile,x) {
  const g=profileData(profile,x),height=new Float64Array(M),radial=new Float64Array(M);
  for(let j=0;j<M;j++){height[j]=g.r**4*state[j];radial[j]=g.r**3*(sq12*state[M+j]+frequencies[j]**2*state[j]);}
  return {r:g.r,w:g.w,logw:g.logw,heightCos:height,radialCos:radial,meanHeight:state[zi],meanRadial:g.w+state[mi]};
 }
 function integrate(state,profile,opts={}) {
  const x0=opts.x0??0,x1=opts.x1??1,steps=opts.steps??64,h=(x1-x0)/steps;
  if(!Number.isInteger(steps)||steps<1)throw new Error("Positive integer steps required.");
  let y=Float64Array.from(state),maxD=0,maxPhi=0,minD=Infinity,minA=Infinity,maxKap=0,maxPV=0,maxPVx=x0;
  function check(x){const z=rhs(y,profile,x,true);maxD=Math.max(maxD,z.maxDarboux);
   maxPhi=Math.max(maxPhi,Math.abs(z.physicalHolonomyResidual));minD=Math.min(minD,z.minD);minA=Math.min(minA,z.minA);
   maxKap=Math.max(maxKap,z.formalHeightCurvature);if(z.peakValley>maxPV){maxPV=z.peakValley;maxPVx=x;}
   if(opts.sample)opts.sample({x,state:Float64Array.from(y),diagnostics:z});}
  check(x0);
  for(let n=0;n<steps;n++){y=rk4(y,profile,x0+n*h,h);if(opts.auditEveryStep!==false||n===steps-1)check(x0+(n+1)*h);}
  return {state:y,steps,maxDarboux:maxD,maxPhysicalHolonomyResidual:maxPhi,minD,minA,
   formalHeightCurvature:maxKap,maxPeakValley:maxPV,maxPeakValleyX:maxPVx};
 }
 function flowRawCell(raw,segments,opts={}) {
  if(!Array.isArray(segments)||!segments.length)throw new Error("Nonempty fixed profile segments required.");
  const root=initialize(raw,segments[0],0,opts.meanHeight??0);
  let state=root.state,maxD=0,maxPhi=0,minD=Infinity,minA=Infinity,maxKap=0,maxPV=0,maxPVx=0;
  let maxJoinPositionError=0,maxJoinLogwError=0,maxJoinLogSlopeError=0;
  for(let k=0;k<segments.length;k++){
   if(k){const a=profileData(segments[k-1],1),b=profileData(segments[k],0),tol=opts.joinTolerance??1e-10;
    const er=Math.abs(a.r-b.r),ew=Math.abs(a.logw-b.logw),es=Math.abs(a.dlogwdx/a.drdx-b.dlogwdx/b.drdx);
    maxJoinPositionError=Math.max(maxJoinPositionError,er);maxJoinLogwError=Math.max(maxJoinLogwError,ew);
    maxJoinLogSlopeError=Math.max(maxJoinLogSlopeError,es);
    if(er>tol*Math.max(1,a.r,b.r)||ew>tol||es>tol*Math.max(1,Math.abs(a.dlogwdx/a.drdx),Math.abs(b.dlogwdx/b.drdx)))
     throw new Error("Profile segment jets mismatch.");}
   const z=integrate(state,segments[k],{steps:opts.stepsPerSegment??64,auditEveryStep:opts.auditEveryStep,sample:opts.sample});
   state=z.state;maxD=Math.max(maxD,z.maxDarboux);maxPhi=Math.max(maxPhi,z.maxPhysicalHolonomyResidual);
   minD=Math.min(minD,z.minD);minA=Math.min(minA,z.minA);maxKap=Math.max(maxKap,z.formalHeightCurvature);
   if(z.maxPeakValley>maxPV){maxPV=z.maxPeakValley;maxPVx=k+z.maxPeakValleyX;}
  }
  return {raw:state.slice(0,2*M),state,port:toPort(state,segments.at(-1),1),
   initialMean:root.meanRelative,maxDarboux:maxD,maxPhi,minD,minA,formalHeightCurvature:maxKap,
   maxPeakValley:maxPV,maxPeakValleyX:maxPVx,maxJoinPositionError,maxJoinLogwError,maxJoinLogSlopeError};
 }
 return {M,N,size,frequencies,meanIndex:mi,heightIndex:zi,relative,
  toRelative,fromRelative,initialize,rhs,rk4,integrate,toPort,flowRawCell};
}
