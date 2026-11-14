// Actual two-jets of the SAME finite momentum equations. Normal-range
// arithmetic follows the frozen evaluator. In the deep branch only
// algebraic ordering changes: no w^2 denominator is formed separately.
// No DN or radial flow is started by this module.

function scaled(logFactor, value) {
  if(value===0)return value;
  const answer=Math.sign(value)*Math.exp(logFactor+Math.log(Math.abs(value)));
  if(!Number.isFinite(answer))throw Error('deep physical-jet final scaled value exceeds Number range');
  return answer;
}

export function createMomentumPhysicalJetEvaluator(engine,{spacing=2}={}) {
  const M=engine.M,N=engine.N,J=M+1,Kdim=2*M,sq2=Math.sqrt(2),sq12=Math.sqrt(12),
    freq=Float64Array.from({length:M},(_,j)=>spacing*(j+1)),
    cs=Array.from({length:N},(_,n)=>Float64Array.from({length:J},(_,j)=>j?sq2*Math.cos(freq[j-1]*2*Math.PI*n/N):1)),
    sn=Array.from({length:N},(_,n)=>Float64Array.from({length:M},(_,j)=>sq2*Math.sin(freq[j]*2*Math.PI*n/N)));
  function spd(B,b) {
    const L=new Float64Array(J*J),t=new Float64Array(J),z=new Float64Array(J);
    for(let i=0;i<J;i++)for(let j=0;j<=i;j++) {
      let a=B[i*J+j];for(let k=0;k<j;k++)a-=L[i*J+k]*L[j*J+k];
      if(i===j){if(!(a>0))throw Error('physical jet root Jacobian not positive');L[i*J+j]=Math.sqrt(a);}
      else L[i*J+j]=a/L[j*J+j];
    }
    for(let i=0;i<J;i++){let a=b[i];for(let j=0;j<i;j++)a-=L[i*J+j]*t[j];t[i]=a/L[i*J+i];}
    for(let i=J-1;i>=0;i--){let a=t[i];for(let j=i+1;j<J;j++)a-=L[j*J+i]*z[j];z[i]=a/L[i*J+i];}
    return z;
  }

  return function evaluate(state,profile,x,{compareLegacy=false}={}) {
    const root=engine.root(state,profile,x),g=root.g,deep=!!g.deepScaled,
      sigma=g.drdx/g.r,k=g.dlogwdx,W=g.w2,dW=2*W*k,dE=dW,
      right=new Float64Array(J),Pdot=new Float64Array(N),Tdot=new Float64Array(N);
    let field,components=null;
    if(deep) {
      if(typeof engine.rhsWithComponents!=='function')throw Error('deep jets require the same engine rhsWithComponents');
      components=engine.rhsWithComponents(state,profile,x,root);
      field=components.derivative;
      if(!components.momentumFlux||components.momentumFlux.length!==M)throw Error('missing complete unscaled angular momentum flux');
      const logT=Math.log(sq12/sq2)+Math.log(engine.mu)-4*Math.log(g.r)-2*g.logw;
      for(let j=0;j<M;j++) {
        const target=root.target?.[j+1]??
          (Number.isFinite(g.momentumTargetFactor)&&g.momentumTargetFactor!==0
            ?g.momentumTargetFactor*state[M+j]
            :engine.orientation*scaled(logT,state[M+j]));
        right[j+1]=sigma*freq[j]*components.momentumFlux[j]-2*k*target;
      }
      const pdot=new Float64Array(M),logC=3*Math.log(g.r)-g.logw-Math.log(sq2);
      for(let j=0;j<M;j++) {
        const p=Number.isFinite(g.momentumPFactor)&&g.momentumPFactor!==0
          ?-freq[j]*g.momentumPFactor*state[j]:scaled(logC,-freq[j]*state[j]);
        pdot[j]=((freq[j]*freq[j]-1)*sigma-k)*p-freq[j]*sigma*root.L[j+1];
      }
      for(let n=0;n<N;n++) {
        const v=root.e.rows[n];let dPt=0;
        for(let j=0;j<M;j++)dPt+=freq[j]*pdot[j]*cs[n][j+1];
        const dP=sigma*v.U-k*v.P,dK=-dPt,wp=g.w*v.P,wk=g.w*v.K,wpt=g.w*v.Pt,
          w1k=g.w+wk,wdP=g.w*dP,wdK=g.w*dK,
          u=2*g.w*wk+wk*wk+g.E*wp*wp,
          du=2*k*u+2*w1k*wdK+2*g.E*wp*wdP+2*k*(g.w*wp)*(g.w*wp),
          dS=-2*k*wp*wp-2*wp*wdP,dsd=-du/(2*v.sd),
          ff=(2+v.sd)/(2*v.sd*(1+v.sd)**2),
          ffLogDerivative=1/(2+v.sd)-1/v.sd-2/(1+v.sd),
          gc=(wp*wp+v.S*u/(1+v.sd))/(v.S*v.sd),
          numeratorDot=2*wp*(k*wp+wdP)+(dS*u+v.S*du)/(1+v.sd)-v.S*u*dsd/(1+v.sd)**2,
          dgc=numeratorDot/(v.S*v.sd)-gc*(dS/v.S+dsd/v.sd),
          wT=2*wk+v.K*wk+g.E*v.P*wp,
          wTdot=k*wT+2*w1k*dK+2*k*g.w*wp*wp+2*g.E*wp*dP,
          derivativeTfc=2*wT*wTdot*ff+wT*wT*ff*ffLogDerivative*dsd,
          dq=g.E*v.P*dP-v.Pt*dPt+k*wp*wp+derivativeTfc
            +dK*v.Pt*gc+(1+v.K)*dPt*gc+(1+v.K)*v.Pt*dgc;
        Pdot[n]=dP;Tdot[n]=dPt;
        if(!Number.isFinite(dq))throw Error('deep physical-jet implicit derivative exceeds Number range');
        for(let j=0;j<J;j++)right[j]-=dq*cs[n][j]/N;
      }
    } else {
      // Preserve the frozen ordinary evaluator's operation ordering.
      field=engine.rhs(state,profile,x,false,root);
      const fac=engine.orientation*sq12*engine.mu/(sq2*g.r**4*W);
      for(let j=0;j<M;j++)right[j+1]=fac*(field[M+j]-(4*sigma+2*k)*state[M+j]);
      for(let n=0;n<N;n++) {
        let dP=0,dPt=0;
        for(let j=0;j<M;j++){const dp=-freq[j]*g.r**3/(sq2*g.w)*(field[j]+(3*sigma-k)*state[j]);dP+=dp*sn[n][j];dPt+=freq[j]*dp*cs[n][j+1];}
        Pdot[n]=dP;Tdot[n]=dPt;
        const v=root.e.rows[n],{P,Pt,K,S,sd}=v,dK=-dPt,T=2*K+K*K+g.E*P*P,
          dT=2*(1+K)*dK+dE*P*P+2*g.E*P*dP,u=W*T,du=dW*T+W*dT,
          dS=-dW*P*P-2*W*P*dP,dsd=-du/(2*sd),ff=(2+sd)/(2*sd*(1+sd)**2),
          fc=u*ff,dfc=du*ff+u*ff*dsd*(1/(2+sd)-1/sd-2/(1+sd)),
          gn=P*P+S*T/(1+sd),dgn=2*P*dP+(dS*T+S*dT)/(1+sd)-S*T*dsd/(1+sd)**2,
          gc=W*gn/(S*sd),dgc=(dW*gn+W*dgn)/(S*sd)-gc*(dS/S+dsd/sd),
          dq=K*dK+.5*dE*P*P+g.E*P*dP+dK*Pt+K*dPt+dT*fc+T*dfc+dK*Pt*gc+(1+K)*dPt*gc+(1+K)*Pt*dgc;
        for(let j=0;j<J;j++)right[j]-=dq*cs[n][j]/N;
      }
    }
    const Ldot=spd(root.e.B,right),perAngle=[];
    let maxDarboux=0,maxNormalizedDarboux=0,formalHeightCurvature=0,peak=-Infinity,valley=Infinity,
      maxLegacySecondDifference=0,maxLegacyDarbouxDifference=0,hol=0,normalizedHol=0,
      physicalDarbouxUnderflowCount=0;
    const legacy=compareLegacy?engine.rhs(state,profile,x,true,root).legacy:null;
    const logWOverRx=2*g.logw-Math.log(Math.abs(g.drdx)),
      logWOverRxMetric=logWOverRx-Math.log(g.r)-2*Math.log(g.E),
      logwOverRx=g.logw-Math.log(Math.abs(g.drdx)),rxSign=Math.sign(g.drdx);
    for(let n=0;n<N;n++) {
      const v=root.e.rows[n];let ld=0,h=state[Kdim]+state[Kdim+1];
      for(let j=0;j<J;j++)ld+=Ldot[j]*cs[n][j];
      for(let j=0;j<M;j++)h+=g.r**4*state[j]*cs[n][j+1]/sq2;
      const b=k*v.K+ld-Tdot[n];
      let G,darboux,urr,ur,ut,urt,utt,a,bc,c;
      if(deep) {
        const wp=g.w*v.P,wk=g.w*v.K,wpt=g.w*v.Pt,wU=g.w*v.U,
          wr=rxSign*scaled(logwOverRx,k),u=2*g.w*wk+wk*wk+g.E*wp*wp;
        G=sigma*g.E*v.U*v.U-k*v.L+k*(wk*wpt-wp*wp);
        const normalized=v.A*b-G;
        darboux=rxSign*scaled(logWOverRxMetric,normalized);
        if(darboux===0&&normalized!==0)physicalDarbouxUnderflowCount++;
        urr=rxSign*scaled(logwOverRx,k+b);ur=g.w+wk;ut=g.r*wp;urt=wU+wp;utt=g.r*wpt;
        a=(urr-g.w*wr*ur/g.E)/(Math.sqrt(g.E)*v.sd);
        bc=wU/(g.r*v.sd);c=(wpt+(g.w+wk)/g.E)*Math.sqrt(g.E)/(g.r*v.sd);
        hol+=(u/(v.sd*(1+v.sd))+(g.w+wk)*wpt/(v.S*v.sd))/N;
      } else {
        G=g.drdx*g.E/g.r*v.U*v.U-k*v.L+k*W*(v.K*v.Pt-v.P*v.P);
        darboux=W*(v.A*b-G)/(g.E*g.E*g.r*g.drdx);
        urr=g.w*(k+b)/g.drdx;ur=g.w*(1+v.K);ut=g.r*g.w*v.P;urt=g.w*(v.U+v.P);utt=g.r*g.w*v.Pt;
        a=(urr-W*k*ur/(g.E*g.drdx))/(Math.sqrt(g.E)*v.sd);
        bc=g.w*v.U/(g.r*v.sd);c=g.w/g.r*(v.Pt+(1+v.K)/g.E)*Math.sqrt(g.E)/v.sd;
        hol+=W*((2*v.K+v.K*v.K+g.E*v.P*v.P)/(v.sd*(1+v.sd))+(1+v.K)*v.Pt/(v.S*v.sd))/N;
      }
      const normalizedDarboux=v.A*b-G,disc=Math.hypot(a-c,2*bc);
      normalizedHol+=(v.L+v.quad)/N;
      maxNormalizedDarboux=Math.max(maxNormalizedDarboux,Math.abs(normalizedDarboux));
      maxDarboux=Math.max(maxDarboux,Math.abs(darboux));
      formalHeightCurvature=Math.max(formalHeightCurvature,Math.abs((a+c+disc)/2),Math.abs((a+c-disc)/2));
      peak=Math.max(peak,h);valley=Math.min(valley,h);
      if(legacy){maxLegacySecondDifference=Math.max(maxLegacySecondDifference,Math.abs(urr-legacy.perAngle[n].urr));maxLegacyDarbouxDifference=Math.max(maxLegacyDarbouxDifference,Math.abs(darboux-legacy.perAngle[n].darboux));}
      if(![ur,ut,urr,urt,utt,darboux,normalizedDarboux,h].every(Number.isFinite))throw Error('nonfinite actual physical jet');
      perAngle.push({theta:2*Math.PI*n/N,ur,ut,urr,urt,utt,darboux,normalizedDarboux,height:h});
    }
    return {perAngle,maxDarboux,maxNormalizedDarboux,formalHeightCurvature,peakValley:peak-valley,
      physicalHolonomyResidual:hol,normalizedHolonomyResidual:normalizedHol,
      minA:root.e.minA,minD:root.e.minD,Ldot:Array.from(Ldot),rootRelativeResidual:root.err/root.scale,
      ...(compareLegacy?{maxLegacySecondDifference,maxLegacyDarbouxDifference}:{}),
      deepScaledArithmetic:deep,physicalDarbouxUnderflowCount,finiteMomentumEquationsUnchanged:true,
      scope:'Actual two-jets from the finite momentum root and its own complete flux; deep-range arithmetic regrouping, no DN/ODE solve or infinite-tail certificate.'};
  };
}

export const createDeepMomentumPhysicalJetEvaluator=createMomentumPhysicalJetEvaluator;
