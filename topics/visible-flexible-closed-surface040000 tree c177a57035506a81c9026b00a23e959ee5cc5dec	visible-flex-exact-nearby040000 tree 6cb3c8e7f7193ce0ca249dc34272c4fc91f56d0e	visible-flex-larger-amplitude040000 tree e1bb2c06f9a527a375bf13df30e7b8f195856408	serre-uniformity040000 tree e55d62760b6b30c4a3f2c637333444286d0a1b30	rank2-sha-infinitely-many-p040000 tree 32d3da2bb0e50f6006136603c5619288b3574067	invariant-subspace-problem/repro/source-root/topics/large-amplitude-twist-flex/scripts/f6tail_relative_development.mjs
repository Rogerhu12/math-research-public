// Cancellation-free R16 development relative to the fixed centered round map.
// Even, pi-periodic height branch: phase and center gauges are fixed for all r.
import {periodicPrimitiveReal} from './f6tail_actual_metric.mjs';

export function periodicDerivative(values){
  const n=values.length,re=Float64Array.from(values),im=new Float64Array(n);
  function fft(inverse){
    for(let i=1,j=0;i<n;i++){let bit=n>>1;for(;j&bit;bit>>=1)j^=bit;j^=bit;if(i<j){[re[i],re[j]]=[re[j],re[i]];[im[i],im[j]]=[im[j],im[i]];}}
    for(let len=2;len<=n;len*=2){const a=(inverse?2:-2)*Math.PI/len,wr=Math.cos(a),wi=Math.sin(a);for(let p=0;p<n;p+=len){let ur=1,ui=0;for(let j=0;j<len/2;j++){const k=p+j,l=k+len/2,vr=re[l]*ur-im[l]*ui,vi=re[l]*ui+im[l]*ur,x=re[k],y=im[k];re[k]=x+vr;im[k]=y+vi;re[l]=x-vr;im[l]=y-vi;const z=ur*wr-ui*wi;ui=ur*wi+ui*wr;ur=z;}}}
    if(inverse)for(let j=0;j<n;j++){re[j]/=n;im[j]/=n;}
  }
  fft(false);re[0]=im[0]=0;
  for(let j=1;j<n;j++){if(j===n/2){re[j]=im[j]=0;continue;}const k=j<n/2?j:j-n,x=re[j],y=im[j];re[j]=-k*y;im[j]=k*x;}
  fft(true);return re;
}

export function relativeActualDevelopment(g,rows,perAngle){
  const {r,w,w2:W,E}=g,N=rows.length,omegaCorrection=new Float64Array(N),Omega=new Float64Array(N);
  let zeta=0;
  for(let j=0;j<N;j++){const v=rows[j];omegaCorrection[j]=W*(v.L+v.quad);zeta+=omegaCorrection[j]/N;Omega[j]=perAngle[j].darboux*E*E*r/(v.D*v.sd);}
  const phase=periodicPrimitiveReal(omegaCorrection),pOmega=periodicPrimitiveReal(Omega),
    dxT=new Float64Array(N),dyT=new Float64Array(N),dxR0=new Float64Array(N),dyR0=new Float64Array(N),cx=new Float64Array(N),cy=new Float64Array(N);
  let txMean=0,tyMean=0,phaseRMean=0;
  for(let j=0;j<N;j++){
    const v=rows[j],theta=2*Math.PI*j/N,c=Math.cos(theta),s=Math.sin(theta),
      sp=Math.sin(phase[j]),cpMinus=-2*Math.sin(phase[j]/2)**2,
      ds=s*cpMinus+c*sp,dc=c*cpMinus-s*sp,cos=c+dc,sin=s+ds,
      sqrtS=Math.sqrt(v.S),rho=r*sqrtS,drho=-r*W*v.P*v.P/(1+sqrtS),
      alpha=v.sd/sqrtS,dalpha=-W*(2*v.K+v.K*v.K+W*v.P*v.P)/(v.S*(1+alpha)),
      beta=-W*(1+v.K)*v.P/sqrtS;
    dxT[j]=-drho*s-rho*ds;dyT[j]=drho*c+rho*dc;
    dxR0[j]=dalpha*c+alpha*dc-beta*sin;dyR0[j]=dalpha*s+alpha*ds+beta*cos;
    const ax=c+dxR0[j],ay=s+dyR0[j];cx[j]=-rho*pOmega[j]*cos-zeta*ay;cy[j]=-rho*pOmega[j]*sin+zeta*ax;
    txMean+=dxT[j]/N;tyMean+=dyT[j]/N;
    phaseRMean+=w*w*(1+v.K)*v.U/(r*v.S*v.sd)/N;
  }
  const dx=periodicPrimitiveReal(dxT),dy=periodicPrimitiveReal(dyT),pcx=periodicPrimitiveReal(cx),pcy=periodicPrimitiveReal(cy),dxR=new Float64Array(N),dyR=new Float64Array(N);
  let metric=0,radial=0,angular=0,position=0;
  for(let j=0;j<N;j++){
    dxR[j]=dxR0[j]+pcx[j];dyR[j]=dyR0[j]+pcy[j];dxT[j]-=txMean;dyT[j]-=tyMean;
    const v=rows[j],theta=2*Math.PI*j/N,c=Math.cos(theta),s=Math.sin(theta),hr=w*v.K,ht=r*w*v.P,
      A=(2*(c*dxR[j]+s*dyR[j])+dxR[j]**2+dyR[j]**2+2*w*hr+hr*hr)/E,
      B=(c*dxT[j]+s*dyT[j]+r*(-s*dxR[j]+c*dyR[j])+dxR[j]*dxT[j]+dyR[j]*dyT[j]+(w+hr)*ht)/(r*Math.sqrt(E)),
      C=(2*r*(-s*dxT[j]+c*dyT[j])+dxT[j]**2+dyT[j]**2+ht*ht)/(r*r);
    metric=Math.max(metric,(Math.abs(A+C)+Math.hypot(A-C,2*B))/2);
    position=Math.max(position,Math.hypot(dx[j],dy[j]));radial=Math.max(radial,Math.hypot(dxR[j],dyR[j]));angular=Math.max(angular,Math.hypot(dxT[j],dyT[j]));
  }
  return {dx,dy,dxR,dyR,dxT,dyT,phase,actualMetricRelativeOperatorError:metric,positionBound:position,radialBound:radial,angularBound:angular,
    angularHolonomyResidual:Math.abs(zeta),translationPeriod:2*Math.PI*Math.hypot(txMean,tyMean),angularPhaseMeanDerivative:phaseRMean};
}

// Actual metric, full vector Darboux tensor and principal curvature from
// Cartesian perturbation two-jets. The round background tensor cancels exactly.
export function relativeSurfaceGeometry(g,theta,Vr,Vt,Vrr,Vrt,Vtt){
  const {r,w,E}=g,wr=w*g.dlogwdx/g.drdx,Ep=2*w*wr,K=w*wr/(r*E*E),c=Math.cos(theta),s=Math.sin(theta),sqE=Math.sqrt(E),
    U0=[c/sqE,s/sqE,w/sqE],V0=[-s,c,0],dU=Vr.map(x=>x/sqE),dV=Vt.map(x=>x/r),
    H10=[-w*wr*c/(E*E),-w*wr*s/(E*E),wr/(E*E)],H30=[-w*w*c/(E*r),-w*w*s/(E*r),w/(E*r)],
    dH1=Vrr.map((x,j)=>(x-Ep*Vr[j]/(2*E))/E),dH2=Vrt.map((x,j)=>(x-Vt[j]/r)/(r*sqE)),dH3=Vtt.map((x,j)=>x/(r*r)+Vr[j]/(E*r)),
    dot=(a,b)=>a.reduce((v,x,j)=>v+x*b[j],0),U=U0.map((x,j)=>x+dU[j]),V=V0.map((x,j)=>x+dV[j]),
    A=2*dot(U0,dU)+dot(dU,dU),B=dot(U0,dV)+dot(V0,dU)+dot(dU,dV),C=2*dot(V0,dV)+dot(dV,dV),
    metric=(Math.abs(A+C)+Math.hypot(A-C,2*B))/2,T=new Float64Array(9);
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)T[i*3+j]=.5*(H10[i]*dH3[j]+dH3[i]*H10[j]+dH1[i]*H30[j]+H30[i]*dH1[j]+dH1[i]*dH3[j]+dH3[i]*dH1[j])-dH2[i]*dH2[j]
    +K*(U0[i]*dU[j]+dU[i]*U0[j]+dU[i]*dU[j]+V0[i]*dV[j]+dV[i]*V0[j]+dV[i]*dV[j]);
  const cross=[U[1]*V[2]-U[2]*V[1],U[2]*V[0]-U[0]*V[2],U[0]*V[1]-U[1]*V[0]],area=Math.hypot(...cross),n=cross.map(x=>x/area),
    H1=H10.map((x,j)=>x+dH1[j]),H3=H30.map((x,j)=>x+dH3[j]),b11=dot(n,H1),b12=dot(n,dH2),b22=dot(n,H3),
    detG=area*area,tr=(1+C)*b11+(1+A)*b22-2*B*b12,detB=b11*b22-b12*b12,
    curvature=(Math.abs(tr)+Math.sqrt(Math.max(0,tr*tr-4*detG*detB)))/(2*detG);
  return {metric,fullTensorFrobeniusBound:Math.hypot(...T),actualCurvature:curvature,areaNormalized:area,
    tangentNorms:[Math.hypot(...U),Math.hypot(...V)],hessianNorms:[Math.hypot(...H1),Math.hypot(...dH2),Math.hypot(...H3)],targetGaussCurvature:K,
    metricEntries:[A,B,C],fullTensor:Array.from(T)};
}
