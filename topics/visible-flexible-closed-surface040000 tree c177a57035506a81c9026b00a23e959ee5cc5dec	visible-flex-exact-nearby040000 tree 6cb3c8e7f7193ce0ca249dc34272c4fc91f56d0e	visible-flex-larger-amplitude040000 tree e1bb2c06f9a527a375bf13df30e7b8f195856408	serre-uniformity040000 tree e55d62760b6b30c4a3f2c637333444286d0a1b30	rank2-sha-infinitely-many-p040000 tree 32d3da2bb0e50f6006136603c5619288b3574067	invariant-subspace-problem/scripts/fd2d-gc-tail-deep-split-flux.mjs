// Algebraically identical finite momentum RHS with the linear angular flux
// projected exactly. The original engine and published sources are untouched.
// This module currently exports the nonlinear state engine, not its Jacobian.
import {createMomentumTailEngine} from './fd2d-gc-tail-deep-root.mjs';

export function createSplitFluxMomentumTailEngine(options={}){
  const base=createMomentumTailEngine(options),{M,N,size,mu,orientation}=base,
    spacing=options.spacing??2,sq2=Math.sqrt(2),sq12=Math.sqrt(12),
    frequency=Float64Array.from({length:M},(_,j)=>spacing*(j+1)),
    sine=Array.from({length:N},(_,n)=>{
      const theta=2*Math.PI*n/N;return Float64Array.from(frequency,m=>sq2*Math.sin(m*theta));
    }),statistics={evaluations:0,maximumRootRelativeResidual:0,roundoffFallbacks:0};
  function rhsWithComponents(state,profile,x,knownRoot=null){
    const rt=knownRoot??base.root(state,profile,x),g=rt.g,d=new Float64Array(size),
      sigma=g.drdx/g.r,nonlinearFlux=new Float64Array(M),
      pref=g.momentumFluxFactor,momentumFlux=new Float64Array(M);
    statistics.evaluations++;statistics.maximumRootRelativeResidual=Math.max(statistics.maximumRootRelativeResidual,rt.err/rt.scale);
    if(rt.roundoffFallback)statistics.roundoffFallbacks++;
    for(let n=0;n<N;n++){
      const v=rt.e.rows[n],wp=g.w*v.P,wk=g.w*v.K,
        u=g.deepScaled?2*g.w*wk+wk*wk+g.E*wp*wp:g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),
        wP2=g.deepScaled?wp*wp:g.w2*v.P*v.P,
        factor=(v.K+u/(1+v.sd)+wP2*v.sd)/(v.S*v.sd),
        f=v.U*factor;
      for(let j=0;j<M;j++)nonlinearFlux[j]+=f*sine[n][j]/N;
    }
    for(let j=0;j<M;j++){
      const m=frequency[j],p=g.deepScaled?-m*g.momentumPFactor*state[j]:-m*g.r**3*state[j]/(sq2*g.w),
        linearFlux=-m*rt.L[j+1]+(m*m-1)*p;
      d[j]=sigma*((m*m-4)*state[j]+sq2*g.w*rt.L[j+1]/g.r**3);
      momentumFlux[j]=linearFlux+nonlinearFlux[j];
      d[M+j]=4*sigma*state[M+j]+pref*m*momentumFlux[j];
    }
    d[2*M]=g.drdx*g.w*rt.L[0];d[2*M+1]=g.drdx*g.w;
    return {derivative:d,momentumFlux,nonlinearFlux,root:rt};
  }
  function rhs(state,profile,x,detail=false,knownRoot=null){
    const f=rhsWithComponents(state,profile,x,knownRoot);
    if(!detail)return f.derivative;
    if(f.root.g.deepScaled)return {...f,splitFlux:true,legacyUnavailable:true};
    return {...base.rhs(state,profile,x,true,f.root),derivative:f.derivative,
      nonlinearFlux:Array.from(f.nonlinearFlux),momentumFlux:f.momentumFlux,splitFlux:true};
  }
  function rk4(state,profile,x,h){
    const a=rhs(state,profile,x),t=new Float64Array(size);
    for(let j=0;j<size;j++)t[j]=state[j]+h*a[j]/2;
    const b=rhs(t,profile,x+h/2);for(let j=0;j<size;j++)t[j]=state[j]+h*b[j]/2;
    const c=rhs(t,profile,x+h/2);for(let j=0;j<size;j++)t[j]=state[j]+h*c[j];
    const d=rhs(t,profile,x+h);return Float64Array.from(state,(v,j)=>v+h*(a[j]+2*b[j]+2*c[j]+d[j])/6);
  }
  return {...base,rhs,rhsWithComponents,rk4,statistics};
}
