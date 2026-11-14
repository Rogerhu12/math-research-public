// Same canonical cell momentum coordinates. Only products/quotients whose
// separate factors underflow are combined before binary64 evaluation.
// Normal-range arithmetic retains the archived order of operations.
export function momentumGeometry(profile,x,{mu,orientation}){
 const a=profile(x),w=Math.exp(a.logw),w2=Math.exp(2*a.logw);
 if(!(a.r>0&&w>0&&Number.isFinite(a.drdx)&&a.drdx!==0&&mu>0))
  throw Error('Momentum geometry or cell normalization is outside binary64 range');
 const g={...a,w,w2,E:1+w2,deepScaled:a.logw< -250},sq2=Math.sqrt(2),sq12=Math.sqrt(12);
 if(!g.deepScaled){
  g.momentumTargetFactor=orientation*sq12*mu/(sq2*g.r**4*w2);
  g.momentumInverseFactor=orientation*sq2*g.r**4*w2/(sq12*mu);
  g.momentumFluxFactor=orientation*sq2*g.r**3*g.drdx*w2/(sq12*mu);
  g.momentumPFactor=g.r**3/(sq2*w);
 }else{
  const lr=Math.log(g.r),lm=Math.log(mu),lx=Math.log(Math.abs(g.drdx)),sx=Math.sign(g.drdx),
   lambda=lm-2*g.logw;
  g.momentumTargetFactor=orientation*Math.sqrt(6)*Math.exp(lambda-4*lr);
  g.momentumInverseFactor=orientation/Math.sqrt(6)*Math.exp(-lambda+4*lr);
  g.momentumFluxFactor=orientation*sx/Math.sqrt(6)*Math.exp(-lambda+3*lr+lx);
  g.momentumPFactor=Math.exp(3*lr-g.logw)/sq2;
  // P*C, sigma*sqrt(2)*w/(r^3*P), and dr*w/P. P is the flux factor.
  g.momentumFluxTimesP=orientation*sx/Math.sqrt(12)*Math.exp(6*lr+lx+g.logw-lm);
  g.momentumScaledQFactor=orientation*Math.sqrt(12)*Math.exp(lm-7*lr-g.logw);
  g.momentumLinearPiQFactor=orientation*sx*Math.sqrt(12)*Math.exp(lm+lx-8*lr-g.logw);
  g.momentumScaledMeanFactor=orientation*Math.sqrt(6)*Math.exp(lm-3*lr-g.logw);
 }
 for(const key of ['momentumTargetFactor','momentumInverseFactor','momentumFluxFactor','momentumPFactor'])
  if(!Number.isFinite(g[key]))throw Error('Combined momentum factor outside binary64 range: '+key);
 return g;
}

// Values needed by the true angular root and its analytic first variation.
// Multiplication by w occurs before squaring; w^2 itself may be zero.
export function deepWeightedTerms(g,K,P,Pt,L=0){
 const wp=g.w*P,wk=g.w*K,wpt=g.w*Pt,
  u=2*g.w*wk+wk*wk+g.E*wp*wp,
  S=1-wp*wp,A=1+L+g.w*wpt;
 return {wp,wk,wpt,u,S,A};
}
