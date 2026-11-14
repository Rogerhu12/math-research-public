// Actual two-jets of the height evolving under the finite projected momentum ODE.
// Differentiate the angular root implicitly, including its explicit r,w dependence.
// This avoids assuming a diagnostic evolution in another set of variables is identical.
export function createMomentumPhysicalJetEvaluator(engine,{spacing=2}={}){
 const M=engine.M,N=engine.N,J=M+1,Kdim=2*M,sq2=Math.sqrt(2),sq12=Math.sqrt(12),freq=Float64Array.from({length:M},(_,j)=>spacing*(j+1));
 const cs=Array.from({length:N},(_,n)=>Float64Array.from({length:J},(_,j)=>j?sq2*Math.cos(freq[j-1]*2*Math.PI*n/N):1));
 const sn=Array.from({length:N},(_,n)=>Float64Array.from({length:M},(_,j)=>sq2*Math.sin(freq[j]*2*Math.PI*n/N)));
 function spd(B,b){const L=new Float64Array(J*J),t=new Float64Array(J),z=new Float64Array(J);for(let i=0;i<J;i++)for(let j=0;j<=i;j++){let a=B[i*J+j];for(let k=0;k<j;k++)a-=L[i*J+k]*L[j*J+k];if(i===j){if(!(a>0))throw Error('physical jet root Jacobian not positive');L[i*J+j]=Math.sqrt(a);}else L[i*J+j]=a/L[j*J+j];}for(let i=0;i<J;i++){let a=b[i];for(let j=0;j<i;j++)a-=L[i*J+j]*t[j];t[i]=a/L[i*J+i];}for(let i=J-1;i>=0;i--){let a=t[i];for(let j=i+1;j<J;j++)a-=L[j*J+i]*z[j];z[i]=a/L[i*J+i];}return z;}
 return function evaluate(state,profile,x,{compareLegacy=false}={}){
  const root=engine.root(state,profile,x),g=root.g,field=engine.rhs(state,profile,x,false,root),sigma=g.drdx/g.r,k=g.dlogwdx,W=g.w2,dW=2*W*k,dE=dW,right=new Float64Array(J),Pdot=new Float64Array(N),Tdot=new Float64Array(N),fac=engine.orientation*sq12*engine.mu/(sq2*g.r**4*W);
  for(let j=0;j<M;j++)right[j+1]=fac*(field[M+j]-(4*sigma+2*k)*state[M+j]);
  for(let n=0;n<N;n++){
   let dP=0,dPt=0;for(let j=0;j<M;j++){const dp=-freq[j]*g.r**3/(sq2*g.w)*(field[j]+(3*sigma-k)*state[j]);dP+=dp*sn[n][j];dPt+=freq[j]*dp*cs[n][j+1];}
   Pdot[n]=dP;Tdot[n]=dPt;
   const v=root.e.rows[n],{P,Pt,K,S,sd}=v,dK=-dPt,T=2*K+K*K+g.E*P*P,dT=2*(1+K)*dK+dE*P*P+2*g.E*P*dP,u=W*T,du=dW*T+W*dT,dS=-dW*P*P-2*W*P*dP,dsd=-du/(2*sd),ff=(2+sd)/(2*sd*(1+sd)**2),fc=u*ff,dfc=du*ff+u*ff*dsd*(1/(2+sd)-1/sd-2/(1+sd)),gn=P*P+S*T/(1+sd),dgn=2*P*dP+(dS*T+S*dT)/(1+sd)-S*T*dsd/(1+sd)**2,gc=W*gn/(S*sd),dgc=(dW*gn+W*dgn)/(S*sd)-gc*(dS/S+dsd/sd);
   const dq=K*dK+.5*dE*P*P+g.E*P*dP+dK*Pt+K*dPt+dT*fc+T*dfc+dK*Pt*gc+(1+K)*dPt*gc+(1+K)*Pt*dgc;
   for(let j=0;j<J;j++)right[j]-=dq*cs[n][j]/N;
  }
  const Ldot=spd(root.e.B,right),perAngle=[];let maxDarboux=0,formalHeightCurvature=0,peak=-Infinity,valley=Infinity,maxLegacySecondDifference=0,maxLegacyDarbouxDifference=0,hol=0;
  const legacy=compareLegacy?engine.rhs(state,profile,x,true,root).legacy:null;
  for(let n=0;n<N;n++){
   const v=root.e.rows[n];let ld=0,h=state[Kdim]+state[Kdim+1];for(let j=0;j<J;j++)ld+=Ldot[j]*cs[n][j];for(let j=0;j<M;j++)h+=g.r**4*state[j]*cs[n][j+1]/sq2;
   const b=k*v.K+ld-Tdot[n],G=g.drdx*g.E/g.r*v.U*v.U-k*v.L+k*W*(v.K*v.Pt-v.P*v.P),darboux=W*(v.A*b-G)/(g.E*g.E*g.r*g.drdx),urr=g.w*(k+b)/g.drdx,ur=g.w*(1+v.K),ut=g.r*g.w*v.P,urt=g.w*(v.U+v.P),utt=g.r*g.w*v.Pt;
   const a=(urr-W*k*ur/(g.E*g.drdx))/(Math.sqrt(g.E)*v.sd),bc=g.w*v.U/(g.r*v.sd),c=g.w/g.r*(v.Pt+(1+v.K)/g.E)*Math.sqrt(g.E)/v.sd,disc=Math.hypot(a-c,2*bc);
   maxDarboux=Math.max(maxDarboux,Math.abs(darboux));formalHeightCurvature=Math.max(formalHeightCurvature,Math.abs((a+c+disc)/2),Math.abs((a+c-disc)/2));peak=Math.max(peak,h);valley=Math.min(valley,h);hol+=W*((2*v.K+v.K*v.K+g.E*v.P*v.P)/(v.sd*(1+v.sd))+(1+v.K)*v.Pt/(v.S*v.sd))/N;
   if(legacy){maxLegacySecondDifference=Math.max(maxLegacySecondDifference,Math.abs(urr-legacy.perAngle[n].urr));maxLegacyDarbouxDifference=Math.max(maxLegacyDarbouxDifference,Math.abs(darboux-legacy.perAngle[n].darboux));}
   perAngle.push({theta:2*Math.PI*n/N,ur,ut,urr,urt,utt,darboux,height:h});
  }
  return {perAngle,maxDarboux,formalHeightCurvature,peakValley:peak-valley,physicalHolonomyResidual:hol,minA:root.e.minA,minD:root.e.minD,Ldot:Array.from(Ldot),rootRelativeResidual:root.err/root.scale,...(compareLegacy?{maxLegacySecondDifference,maxLegacyDarbouxDifference}:{}),scope:'Two-jets differentiated from the finite momentum root and its actual ODE; no infinite-tail certificate.'};
 };
}
