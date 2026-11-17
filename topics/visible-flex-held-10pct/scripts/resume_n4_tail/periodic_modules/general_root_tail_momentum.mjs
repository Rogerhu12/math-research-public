// Optional exact periodic quadrature reuse; declared N and all original guards retained.
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const periodicSourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!periodicSourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const {createRawTailEngine}=await import(pathToFileURL(path.join(periodicSourceRoot,'topics/large-amplitude-twist-flex/scripts/general_exact_tail_cauchy_raw.mjs')));
// Root: exact projected angular-connection momentum coordinates.
// Depends on createRawTailEngine only for independent legacy diagnostics.
// pi = orientation*r^4*(omega_theta-1)/(sqrt(12)*mu), mu fixed per cell.
// Unknowns Q_j, pi_j use plain cosine coefficients. L=K+P_theta uses orthonormal cosines.
// FULL finite-M momentum roots are solved; no pointwise-k projection substitutes for the actual jet.
export function createMomentumTailEngine(options={}) {
 const M=options.modes??4,N=options.quadrature??128,spacing=options.spacing??2;
 const mu=options.mu??1,orientation=options.orientation??1,floor=options.projectionFloor??.1;
 if(!(M>=1&&M<=64&&Number.isInteger(M)&&Number.isInteger(N)&&Number.isInteger(spacing)&&spacing>=1&&N>4*M*spacing&&mu>0&&(orientation===1||orientation===-1)))throw new Error("invalid momentum engine options");
 let ga=N,gb=spacing;while(gb!==0){const t=ga%gb;ga=gb;gb=t;}
 const periodicMultiplicity=ga,nq=N/periodicMultiplicity;
 const J=M+1,size=2*M+2,sq2=Math.sqrt(2),sq12=Math.sqrt(12);
 const cs=Array.from({length:nq},()=>new Float64Array(J)),sn=Array.from({length:nq},()=>new Float64Array(M));
 const freq=Float64Array.from({length:M},(_,j)=>(j+1)*spacing);
 for(let n=0;n<nq;n++){cs[n][0]=1;const theta=2*Math.PI*n/N;
  for(let j=0;j<M;j++){cs[n][j+1]=sq2*Math.cos(freq[j]*theta);sn[n][j]=sq2*Math.sin(freq[j]*theta);}}
 const legacy=createRawTailEngine({modes:M,quadrature:N,spacing,projectionFloor:floor});
 function geometry(profile,x){
  const g=profile(x),w=Math.exp(g.logw),w2=Math.exp(2*g.logw);
  if(!(g.r>0&&w>0&&w2>0&&Number.isFinite(g.drdx)&&g.drdx!==0))throw new Error("momentum profile out of float range");
  return {...g,w,w2,E:1+w2};
 }
 function data(Q,g){
  const p=new Float64Array(M),pt=new Float64Array(J);
  for(let j=0;j<M;j++){p[j]=-freq[j]*g.r**3*Q[j]/(sq2*g.w);pt[j+1]=freq[j]*p[j];}
  return {p,pt};
 }
 function evaluateL(L,Q,g,needJac=true){
  const d=data(Q,g),quad=new Float64Array(J),B=new Float64Array(J*J),rows=[];
  if(needJac)for(let i=0;i<J;i++)B[i*J+i]=1;
  let minD=Infinity,minA=Infinity,minS=Infinity,maxQuad=0;
  for(let n=0;n<nq;n++){
   let P=0,Pt=0,Lv=L[0],U=0;
   for(let j=0;j<M;j++){
    P+=d.p[j]*sn[n][j];Pt+=d.pt[j+1]*cs[n][j+1];Lv+=L[j+1]*cs[n][j+1];
    U+=(-freq[j]*L[j+1]+(freq[j]*freq[j]-1)*d.p[j])*sn[n][j];
   }
   const K=Lv-Pt,T=2*K+K*K+g.E*P*P,u=g.w2*T,D=1-u,S=1-g.w2*P*P,A=1+Lv+g.w2*Pt;
   if(!(D>floor&&S>floor&&A>floor))throw new Error("momentum branch D/S/A rejected");
   const sd=Math.sqrt(D),fc=u*(2+sd)/(2*sd*(1+sd)*(1+sd));
   const gc=g.w2*(P*P+S*T/(1+sd))/(S*sd);
   const q=.5*(K*K+g.E*P*P)+K*Pt+T*fc+(1+K)*Pt*gc;
   maxQuad=Math.max(maxQuad,Math.abs(q));minD=Math.min(minD,D);minA=Math.min(minA,A);minS=Math.min(minS,S);
   for(let i=0;i<J;i++)quad[i]+=q*cs[n][i]/nq;
   if(needJac){
    const am=Lv+g.w2*Pt,bm=am+(1+am)*Math.expm1(-1.5*Math.log1p(-u));
    for(let i=0;i<J;i++)for(let j=0;j<=i;j++)B[i*J+j]+=bm*cs[n][i]*cs[n][j]/nq;
   }
   rows.push({P,Pt,L:Lv,K,U,S,D,A,sd,quad:q});
  }
  for(let n=nq;n<N;n++)rows.push({...rows[n%nq]});
  if(needJac)for(let i=0;i<J;i++)for(let j=0;j<i;j++)B[j*J+i]=B[i*J+j];
  return {moments:Float64Array.from(L,(v,j)=>v+quad[j]),quad,B,rows,minD,minS,minA,maxQuad};
 }
 function solveSPD(B,b){
  const L=new Float64Array(J*J),out=new Float64Array(J),tmp=new Float64Array(J);
  for(let i=0;i<J;i++)for(let j=0;j<=i;j++){
   let v=B[i*J+j];for(let k=0;k<j;k++)v-=L[i*J+k]*L[j*J+k];
   if(i===j){if(!(v>0))throw new Error("momentum Newton matrix not SPD");L[i*J+j]=Math.sqrt(v);}
   else L[i*J+j]=v/L[j*J+j];
  }
  for(let i=0;i<J;i++){let v=b[i];for(let j=0;j<i;j++)v-=L[i*J+j]*tmp[j];tmp[i]=v/L[i*J+i];}
  for(let i=J-1;i>=0;i--){let v=tmp[i];for(let j=i+1;j<J;j++)v-=L[j*J+i]*out[j];out[i]=v/L[i*J+i];}
  return out;
 }
 function root(state,profile,x,guess){
  const g=geometry(profile,x),Q=state.slice(0,M),target=new Float64Array(J);
  const f=orientation*sq12*mu/(sq2*g.r**4*g.w2);
  for(let j=0;j<M;j++)target[j+1]=f*state[M+j];
  let L=guess?Float64Array.from(guess):Float64Array.from(target);
  let last;
  for(let it=0;it<30;it++){
   const e=evaluateL(L,Q,g,true),res=Float64Array.from(e.moments,(v,j)=>v-target[j]);
   const err=Math.max(...Array.from(res,Math.abs)),scale=Math.max(1e-300,e.maxQuad,...Array.from(target,Math.abs));
   last={L,e,g,err,scale,iterations:it};
   if(err<=8e-14*scale)return last;
   const step=solveSPD(e.B,res);let accepted=false;
   for(let k=0;k<20;k++){
    const fac=2**(-k),trial=Float64Array.from(L,(v,j)=>v-fac*step[j]);
    try{const v=evaluateL(trial,Q,g,false),er=Math.max(...Array.from(v.moments,(z,j)=>Math.abs(z-target[j])));
     if(er<err||er<=8e-14*scale){L=trial;accepted=true;break;}}
    catch(_){}
   }
   if(!accepted){if(err<=5e-12*scale)return {...last,roundoffFallback:true};throw new Error("momentum Newton line search failed");}
  }
  throw new Error("momentum Newton iteration limit");
 }
 function initializeFromRaw(raw,profile,x=0){
  const g=geometry(profile,x),Q=Float64Array.from(raw.slice(0,M)),L=new Float64Array(J);
  for(let j=0;j<M;j++)L[j+1]=sq12*g.r**3*raw[M+j]/(sq2*g.w);
  let e;
  for(let it=0;it<30;it++){
   e=evaluateL(L,Q,g,true);const err=e.moments[0],scale=Math.max(1e-300,e.maxQuad,Math.abs(L[0]));
   if(Math.abs(err)<=8e-14*scale)break;
   const step=err/e.B[0];let accepted=false;
   for(let k=0;k<20;k++){const trial=Float64Array.from(L);trial[0]-=step*2**(-k);
    try{const d=evaluateL(trial,Q,g,false);if(Math.abs(d.moments[0])<Math.abs(err)){L.set(trial);accepted=true;break;}}catch(_){}
   }
   if(!accepted)throw new Error("initial full mean root failed");
   if(it===29)throw new Error("initial mean iteration limit");
  }
  e=evaluateL(L,Q,g,true);const state=new Float64Array(size);state.set(Q);
  const f=orientation*sq2*g.r**4*g.w2/(sq12*mu);
  for(let j=0;j<M;j++)state[M+j]=f*e.moments[j+1];
  return {state,L,meanPhysical:g.w*L[0],normalizedMeanResidual:e.moments[0]};
 }
 function toRaw(state,profile,x=0,solved){
  const r=solved??root(state,profile,x),g=r.g,raw=new Float64Array(2*M);
  raw.set(state.slice(0,M));for(let j=0;j<M;j++)raw[M+j]=sq2*g.w*r.L[j+1]/(sq12*g.r**3);
  return {raw,meanPhysical:g.w*r.L[0],meanHeight:state[2*M]+state[2*M+1],root:r};
 }
 function rhs(state,profile,x,detail=false,knownRoot=null){
  const r=knownRoot??root(state,profile,x),g=r.g,d=new Float64Array(size),sigma=g.drdx/g.r,flux=new Float64Array(M);
  for(let n=0;n<nq;n++){
   const v=r.e.rows[n],f=(1+v.K)*v.U/(v.S*v.sd);
   for(let j=0;j<M;j++)flux[j]+=f*sn[n][j]/nq;
  }
  const pref=orientation*sq2*g.r**3*g.drdx*g.w2/(sq12*mu);
  for(let j=0;j<M;j++){
   d[j]=sigma*((freq[j]*freq[j]-4)*state[j]+sq2*g.w*r.L[j+1]/g.r**3);
   d[M+j]=4*sigma*state[M+j]+pref*freq[j]*flux[j];
  }
  d[2*M]=g.drdx*g.w*r.L[0];d[2*M+1]=g.drdx*g.w;
  if(!detail)return d;
  const rr=toRaw(state,profile,x,r),old=new Float64Array(size);old.set(rr.raw);old[2*M]=rr.meanPhysical;old[2*M+1]=rr.meanHeight;
  const diag=legacy.rhs(old,profile,x,true);
  return {derivative:d,raw:rr.raw,meanPhysical:rr.meanPhysical,rootResidual:r.err,rootRelativeResidual:r.err/r.scale,
   rootIterations:r.iterations,minD:r.e.minD,minA:r.e.minA,legacy:diag};
 }
 function rk4(state,profile,x,h){
  const a=rhs(state,profile,x),t=new Float64Array(size);
  for(let j=0;j<size;j++)t[j]=state[j]+h*a[j]/2;
  const b=rhs(t,profile,x+h/2);for(let j=0;j<size;j++)t[j]=state[j]+h*b[j]/2;
  const c=rhs(t,profile,x+h/2);for(let j=0;j<size;j++)t[j]=state[j]+h*c[j];
  const d=rhs(t,profile,x+h);return Float64Array.from(state,(v,j)=>v+h*(a[j]+2*b[j]+2*c[j]+d[j])/6);
 }
 function flowRawCell(raw,segments,opts={}){
  const init=initializeFromRaw(raw,segments[0]),steps=opts.stepsPerSegment??64;
  let maxJoinPositionError=0,maxJoinLogwError=0,maxJoinLogSlopeError=0;
  let state=init.state,maxDarboux=0,maxNormalizedDefect=0,maxRootRelativeResidual=0,maxMeanResidual=0,minD=Infinity,minA=Infinity,maxPV=0,maxCurvature=0,maxIterations=0;
  for(let k=0;k<segments.length;k++){
   const profile=segments[k],h=1/steps;
   if(k>0){const left=segments[k-1](1),right=profile(0);
    maxJoinPositionError=Math.max(maxJoinPositionError,Math.abs(left.r-right.r));
    maxJoinLogwError=Math.max(maxJoinLogwError,Math.abs(left.logw-right.logw));
    const slopeError=Math.abs(left.dlogwdx/left.drdx-right.dlogwdx/right.drdx);maxJoinLogSlopeError=Math.max(maxJoinLogSlopeError,slopeError);
    if(Math.abs(left.r-right.r)>1e-11*Math.max(1,left.r,right.r)||Math.abs(left.logw-right.logw)>1e-10||slopeError>1e-10*Math.max(1,Math.abs(left.dlogwdx/left.drdx),Math.abs(right.dlogwdx/right.drdx)))throw new Error('Momentum profile segment join mismatch');
   }
   const audit=x=>{
    const a=rhs(state,profile,x,true),g=geometry(profile,x),ld=a.legacy;
    maxDarboux=Math.max(maxDarboux,ld.maxDarboux);
    for(const v of ld.perAngle)maxNormalizedDefect=Math.max(maxNormalizedDefect,Math.abs(v.darboux*g.E*g.E*g.r*g.drdx/g.w2));
    maxRootRelativeResidual=Math.max(maxRootRelativeResidual,a.rootRelativeResidual);
    maxMeanResidual=Math.max(maxMeanResidual,Math.abs(ld.normalizedHolonomyResidual));
    minD=Math.min(minD,a.minD);minA=Math.min(minA,a.minA);maxPV=Math.max(maxPV,ld.peakValley);maxCurvature=Math.max(maxCurvature,ld.formalHeightCurvature);maxIterations=Math.max(maxIterations,a.rootIterations);
    if(opts.sample)opts.sample({segment:k,x,state:Float64Array.from(state),diagnostics:a});
   };
   audit(0);
   for(let n=0;n<steps;n++){state=rk4(state,profile,n*h,h);if(opts.auditEveryStep!==false||n===steps-1)audit((n+1)*h);}
  }
  const end=toRaw(state,segments.at(-1),1);
  return {raw:end.raw,state,meanPhysical:end.meanPhysical,meanHeight:end.meanHeight,maxDarboux,maxNormalizedDefect,maxRootRelativeResidual,maxMeanResidual,minD,minA,maxPV,formalHeightCurvature:maxCurvature,maxIterations,maxJoinPositionError,maxJoinLogwError,maxJoinLogSlopeError,
   scope:"Full finite-M projected momentum system, not an infinite tail or actual developed closed surface."};
 }
 function rhsWithJacobian(state,profile,x){
  const rt=root(state,profile,x),g=rt.g,Kdim=2*M,sigma=g.drdx/g.r;
  const derivative=rhs(state,profile,x,false,rt),jacobian=new Float64Array(size*Kdim);
  const pref=orientation*sq2*g.r**3*g.drdx*g.w2/(sq12*mu);
  const targetFac=orientation*sq12*mu/(sq2*g.r**4*g.w2),pFac=g.r**3/(sq2*g.w);
  for(let col=0;col<Kdim;col++){
   const dp=new Float64Array(M),dpt=new Float64Array(J),right=new Float64Array(J);
   if(col<M){dp[col]=-freq[col]*pFac;dpt[col+1]=freq[col]*dp[col];}
   else right[col-M+1]=targetFac;
   for(let n=0;n<nq;n++){
    const v=rt.e.rows[n],omega=1+g.w2*(v.L+v.quad),rho=1/(v.D*v.sd);
    const FP=g.E*v.P*omega/v.D+2*g.w2*(1+v.K)*v.Pt*v.P/(v.S*v.S*v.sd);
    const FT=-(g.E*v.Pt+g.w2*(1+v.K)*(g.w2*v.P*v.P+2*v.K+v.K*v.K)/v.S)*rho;
    let P1=0,T1=0;for(let j=0;j<M;j++){P1+=dp[j]*sn[n][j];T1+=dpt[j+1]*cs[n][j+1];}
    const q=FP*P1+FT*T1;for(let i=0;i<J;i++)right[i]-=q*cs[n][i]/nq;
   }
   const dL=solveSPD(rt.e.B,right),df=new Float64Array(M);
   for(let n=0;n<nq;n++){
    const v=rt.e.rows[n];let P1=0,T1=0,L1=dL[0],U1=0;
    for(let j=0;j<M;j++){P1+=dp[j]*sn[n][j];T1+=dpt[j+1]*cs[n][j+1];L1+=dL[j+1]*cs[n][j+1];
     U1+=(-freq[j]*dL[j+1]+(freq[j]*freq[j]-1)*dp[j])*sn[n][j];}
    const K1=L1-T1,f=(1+v.K)*v.U/(v.S*v.sd);
    const F1=(K1*v.U+(1+v.K)*U1)/(v.S*v.sd)
      +f*(2*g.w2*v.P*P1/v.S+g.w2*((1+v.K)*K1+g.E*v.P*P1)/v.D);
    for(let j=0;j<M;j++)df[j]+=F1*sn[n][j]/nq;
   }
   for(let j=0;j<M;j++){
    jacobian[j*Kdim+col]=sigma*((col===j?freq[j]*freq[j]-4:0)+sq2*g.w*dL[j+1]/g.r**3);
    jacobian[(M+j)*Kdim+col]=(col===M+j?4*sigma:0)+pref*freq[j]*df[j];
   }
   jacobian[2*M*Kdim+col]=g.drdx*g.w*dL[0];
  }
  return {derivative,jacobian,root:rt};
 }
 function flowStateWithJacobian(initial,segments,opts={}){
  const Kdim=2*M,steps=opts.stepsPerSegment??64;
  let state=Float64Array.from(initial),tangent=new Float64Array(size*Kdim),minA=Infinity,minD=Infinity,maxRootRelative=0;
  for(let j=0;j<Kdim;j++)tangent[j*Kdim+j]=1;
  function field(s,t,p,x){
   const f=rhsWithJacobian(s,p,x),dt=new Float64Array(size*Kdim);
   minA=Math.min(minA,f.root.e.minA);minD=Math.min(minD,f.root.e.minD);maxRootRelative=Math.max(maxRootRelative,f.root.err/f.root.scale);
   for(let i=0;i<size;i++)for(let k=0;k<Kdim;k++)for(let j=0;j<Kdim;j++)dt[i*Kdim+k]+=f.jacobian[i*Kdim+j]*t[j*Kdim+k];
   return {ds:f.derivative,dt};
  }
  function increment(s,t,f,h){return {s:Float64Array.from(s,(v,j)=>v+h*f.ds[j]),t:Float64Array.from(t,(v,j)=>v+h*f.dt[j])};}
  for(const p of segments){
   const h=1/steps;
   for(let n=0;n<steps;n++){
    const x=n*h,a=field(state,tangent,p,x),ab=increment(state,tangent,a,h/2),b=field(ab.s,ab.t,p,x+h/2);
    const bc=increment(state,tangent,b,h/2),c=field(bc.s,bc.t,p,x+h/2),cd=increment(state,tangent,c,h),d=field(cd.s,cd.t,p,x+h);
    for(let j=0;j<size;j++)state[j]+=h*(a.ds[j]+2*b.ds[j]+2*c.ds[j]+d.ds[j])/6;
    for(let j=0;j<tangent.length;j++)tangent[j]+=h*(a.dt[j]+2*b.dt[j]+2*c.dt[j]+d.dt[j])/6;
   }
  }
  return {state,tangent,shapeDimension:Kdim,minA,minD,maxRootRelative};
 }
 return {M,N,size,mu,orientation,quadratureIndependentNodes:nq,quadraturePeriodMultiplicity:periodicMultiplicity,root,evaluateL,geometry,initializeFromRaw,toRaw,rhs,rhsWithJacobian,rk4,flowRawCell,flowStateWithJacobian};
}
