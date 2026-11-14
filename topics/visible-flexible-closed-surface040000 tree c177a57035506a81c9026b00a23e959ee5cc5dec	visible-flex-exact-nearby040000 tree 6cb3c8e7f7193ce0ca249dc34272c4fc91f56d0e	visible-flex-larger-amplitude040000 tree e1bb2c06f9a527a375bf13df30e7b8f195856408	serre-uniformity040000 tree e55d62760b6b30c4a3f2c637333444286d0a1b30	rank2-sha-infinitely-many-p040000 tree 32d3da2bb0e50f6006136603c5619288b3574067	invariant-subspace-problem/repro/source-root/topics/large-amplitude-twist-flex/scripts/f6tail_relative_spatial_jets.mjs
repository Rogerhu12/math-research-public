import {createMomentumPhysicalJetEvaluator} from './f6tail_momentum_physical_jets.mjs';
import {relativeActualDevelopment,periodicDerivative} from './f6tail_relative_development.mjs';

export function createRelativeSpatialJetEvaluator(engine,{spacing=6,radialDifferenceStep=1e-4}={}){
  const M=engine.M,N=engine.N,K=2*M,ev=createMomentumPhysicalJetEvaluator(engine,{spacing});
  function point(state,profile,x){
    const rt=engine.root(state,profile,x),g=rt.g,j=ev(state,profile,x),development=relativeActualDevelopment(g,rt.e.rows,j.perAngle);
    return {rt,g,j,development};
  }
  function evaluate(state,profile,x){
    const q=point(state,profile,x),{rt,g,j,development:d}=q,field=engine.rhs(state,profile,x,false,rt),sigma=g.drdx/g.r,
      hc=new Float64Array(M),hrrc=new Float64Array(M),meanRR=g.w*(j.Ldot[0]+g.dlogwdx*rt.L[0])/g.drdx,
      dxRR=new Float64Array(N),dyRR=new Float64Array(N),h=radialDifferenceStep;
    for(let i=0;i<M;i++){const m=spacing*(i+1);hc[i]=g.r**4*state[i];hrrc[i]=(m*m*g.r**3*(field[i]+3*sigma*state[i])+Math.sqrt(2)*g.w*(j.Ldot[i+1]+g.dlogwdx*rt.L[i+1]))/g.drdx;}
    let offsets,weights;
    if(x>=2*h&&x<=1-2*h){offsets=[-2,-1,1,2];weights=[1,-8,8,-1];}
    else if(x<2*h){offsets=[0,1,2,3,4];weights=[-25,48,-36,16,-3];}
    else{offsets=[0,-1,-2,-3,-4];weights=[25,-48,36,-16,3];}
    for(let i=0;i<offsets.length;i++){
      const dt=h*offsets[i],v=offsets[i]===0?d:point(engine.rk4(state,profile,x,dt),profile,x+dt).development;
      for(let k=0;k<N;k++){dxRR[k]+=weights[i]*v.dxR[k]/(12*h*g.drdx);dyRR[k]+=weights[i]*v.dyR[k]/(12*h*g.drdx);}
    }
    const dxRT=periodicDerivative(d.dxR),dyRT=periodicDerivative(d.dyR),dxTT=periodicDerivative(d.dxT),dyTT=periodicDerivative(d.dyT),perAngle=[];
    for(let n=0;n<N;n++){
      const theta=2*Math.PI*n/N,v=rt.e.rows[n];let height=state[K],second=meanRR;
      for(let i=0;i<M;i++){const c=Math.cos(spacing*(i+1)*theta);height+=hc[i]*c;second+=hrrc[i]*c;}
      perAngle.push({theta,V:[d.dx[n],d.dy[n],height],Vr:[d.dxR[n],d.dyR[n],g.w*v.K],Vt:[d.dxT[n],d.dyT[n],g.r*g.w*v.P],
        Vrr:[dxRR[n],dyRR[n],second],Vrt:[dxRT[n],dyRT[n],g.w*(v.U+v.P)],Vtt:[dxTT[n],dyTT[n],g.r*g.w*v.Pt]});
    }
    return {g,root:rt,field,perAngle,development:d,heightJets:j,scope:'Actual centered R16 Cartesian perturbation jets; planar radial second derivative is a fourth-order finite difference of the cancellation-free actual first derivative.'};
  }
  return {point,evaluate};
}
