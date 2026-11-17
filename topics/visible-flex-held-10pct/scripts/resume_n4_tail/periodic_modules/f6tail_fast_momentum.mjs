// Optional exact periodic quadrature reuse; declared N and all original guards retained.
// Batched variational derivative of the unchanged finite momentum equations.
// The pointwise root and nonlinear RHS are imported unchanged; only their
// linearization is assembled with matrix products and one Cholesky factorization.
import {createMomentumTailEngine} from './general_root_tail_momentum.mjs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const periodicSourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!periodicSourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const {integrationGrid}=await import(pathToFileURL(path.join(periodicSourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));

export function createFastMomentumTailEngine(options={}){
  const base=createMomentumTailEngine(options),{M,N,size,mu,orientation}=base,
    nq=base.quadratureIndependentNodes,
    spacing=options.spacing??2,J=M+1,Kdim=2*M,sq2=Math.sqrt(2),sq12=Math.sqrt(12),
    freq=Float64Array.from({length:M},(_,j)=>spacing*(j+1)),
    cs=Array.from({length:nq},(_,n)=>Float64Array.from({length:J},(_,j)=>j?sq2*Math.cos(freq[j-1]*2*Math.PI*n/N):1)),
    sn=Array.from({length:nq},(_,n)=>Float64Array.from({length:M},(_,j)=>sq2*Math.sin(freq[j]*2*Math.PI*n/N)));
  if(N<=2*spacing*M)throw Error('batched Fourier Jacobian requires resolved basis orthogonality');
  function solveManySPD(B,R){
    const L=new Float64Array(J*J),X=Float64Array.from(R);
    for(let i=0;i<J;i++)for(let j=0;j<=i;j++){
      let v=B[i*J+j];for(let k=0;k<j;k++)v-=L[i*J+k]*L[j*J+k];
      if(i===j){if(!(v>0))throw Error('batched momentum Jacobian not positive');L[i*J+j]=Math.sqrt(v);}else L[i*J+j]=v/L[j*J+j];
    }
    for(let i=0;i<J;i++)for(let col=0;col<Kdim;col++){
      let v=X[i*Kdim+col];for(let k=0;k<i;k++)v-=L[i*J+k]*X[k*Kdim+col];X[i*Kdim+col]=v/L[i*J+i];
    }
    for(let i=J-1;i>=0;i--)for(let col=0;col<Kdim;col++){
      let v=X[i*Kdim+col];for(let k=i+1;k<J;k++)v-=L[k*J+i]*X[k*Kdim+col];X[i*Kdim+col]=v/L[i*J+i];
    }
    return X;
  }
  function rhsWithJacobian(state,profile,x){
    const rt=base.root(state,profile,x),g=rt.g,derivative=base.rhs(state,profile,x,false,rt),sigma=g.drdx/g.r,
      pref=orientation*sq2*g.r**3*g.drdx*g.w2/(sq12*mu),
      targetFac=orientation*sq12*mu/(sq2*g.r**4*g.w2),pFac=g.r**3/(sq2*g.w),
      right=new Float64Array(J*Kdim),FL=new Float64Array(M*J),FQ=new Float64Array(M*M),
      pc=new Float64Array(M),tc=new Float64Array(M),ql=new Float64Array(J),qq=new Float64Array(M);
    for(let n=0;n<nq;n++){
      const v=rt.e.rows[n],omega=1+g.w2*(v.L+v.quad),rho=1/(v.D*v.sd),
        FP=g.E*v.P*omega/v.D+2*g.w2*(1+v.K)*v.Pt*v.P/(v.S*v.S*v.sd),
        FT=-(g.E*v.Pt+g.w2*(1+v.K)*(g.w2*v.P*v.P+2*v.K+v.K*v.K)/v.S)*rho,
        flux=(1+v.K)*v.U/(v.S*v.sd),
        CK=v.U/(v.S*v.sd)+flux*g.w2*(1+v.K)/v.D,
        u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),
        CUminus=(v.K+u/(1+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd),
        CP=flux*(2*g.w2*v.P/v.S+g.w2*g.E*v.P/v.D),
        am=v.L+g.w2*v.Pt,bm=am+(1+am)*Math.expm1(-1.5*Math.log1p(-u));
      ql[0]=CK;
      for(let j=0;j<M;j++){
        pc[j]=-freq[j]*pFac*sn[n][j];tc[j]=-freq[j]*freq[j]*pFac*cs[n][j+1];
        const q=FP*pc[j]+FT*tc[j];
        for(let i=0;i<J;i++){
          right[i*Kdim+j]-=q*cs[n][i]/nq;
          right[i*Kdim+M+j]-=targetFac*bm*cs[n][i]*cs[n][j+1]/nq;
        }
        ql[j+1]=CK*cs[n][j+1]-CUminus*freq[j]*sn[n][j];
        qq[j]=(CP+CUminus*(freq[j]*freq[j]-1))*pc[j]-CK*tc[j];
      }
      for(let i=0;i<M;i++){
        const factor=sn[n][i]/nq;
        for(let j=0;j<J;j++)FL[i*J+j]+=factor*ql[j];
        for(let j=0;j<M;j++)FQ[i*M+j]+=factor*qq[j];
      }
    }
    // dL is the deviation from the exact linear diagonal target response.
    const dL=solveManySPD(rt.e.B,right),jacobian=new Float64Array(size*Kdim);
    for(let j=0;j<M;j++)for(let col=0;col<Kdim;col++){
      let df=-freq[j]*dL[(j+1)*Kdim+col]+(col<M?FQ[j*M+col]:FL[j*J+col-M+1]*targetFac);
      for(let i=0;i<J;i++)df+=FL[j*J+i]*dL[i*Kdim+col];
      jacobian[j*Kdim+col]=sigma*((col===j?freq[j]*freq[j]-4:0)+sq2*g.w*(dL[(j+1)*Kdim+col]+(col===M+j?targetFac:0))/g.r**3);
      jacobian[(M+j)*Kdim+col]=(col===M+j?(4-freq[j]*freq[j])*sigma:0)
        +(col===j?-pref*freq[j]*freq[j]*(freq[j]*freq[j]-1)*pFac:0)+pref*freq[j]*df;
    }
    for(let col=0;col<Kdim;col++)jacobian[2*M*Kdim+col]=g.drdx*g.w*dL[col];
    return {derivative,jacobian,root:rt};
  }
  function flowStateWithJacobian(initial,segments,opts={}){
    const steps=opts.stepsPerSegment??64;
    let state=Float64Array.from(initial),tangent=new Float64Array(size*Kdim),minA=Infinity,minD=Infinity,maxRootRelative=0;
    for(let j=0;j<Kdim;j++)tangent[j*Kdim+j]=1;
    function field(s,t,p,x){
      const f=rhsWithJacobian(s,p,x),dt=new Float64Array(size*Kdim);
      minA=Math.min(minA,f.root.e.minA);minD=Math.min(minD,f.root.e.minD);maxRootRelative=Math.max(maxRootRelative,f.root.err/f.root.scale);
      for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){const z=f.jacobian[i*Kdim+j];for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*t[j*Kdim+k];}
      return {ds:f.derivative,dt};
    }
    function increment(s,t,f,h){return {s:Float64Array.from(s,(v,j)=>v+h*f.ds[j]),t:Float64Array.from(t,(v,j)=>v+h*f.dt[j])};}
    for(const p of segments){const ordinaryH=1/steps,cuts=p.integrationBreakpoints??[],grid=cuts.length?integrationGrid(steps,cuts):null,
      count=grid?grid.length-1:steps;
      for(let n=0;n<count;n++){
        const h=grid?grid[n+1]-grid[n]:ordinaryH,x=grid?grid[n]:n*ordinaryH,
          a=field(state,tangent,p,x),ab=increment(state,tangent,a,h/2),b=field(ab.s,ab.t,p,x+h/2),
          bc=increment(state,tangent,b,h/2),c=field(bc.s,bc.t,p,x+h/2),cd=increment(state,tangent,c,h),d=field(cd.s,cd.t,p,x+h);
        for(let j=0;j<size;j++)state[j]+=h*(a.ds[j]+2*b.ds[j]+2*c.ds[j]+d.ds[j])/6;
        for(let j=0;j<tangent.length;j++)tangent[j]+=h*(a.dt[j]+2*b.dt[j]+2*c.dt[j]+d.dt[j])/6;
      }
    }
    return {state,tangent,shapeDimension:Kdim,minA,minD,maxRootRelative};
  }
  return {...base,rhsWithJacobian,flowStateWithJacobian};
}
