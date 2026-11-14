// Original full mean root with given dimensionless nonmean L coefficients.
// This is initializeFromRaw after the exact fixed-node linear coordinate
// substitution raw_j=w*L_j/(sqrt(6)*r^3), without forming tiny physical raw_j.
export function initializeNormalizedMean(engine,Q,nonmeanL,profile,x=0,meanGuess=0){
 const {M}=engine,g=engine.geometry(profile,x),L=Float64Array.from(nonmeanL);
 if(Q.length!==M||L.length!==M+1||!Number.isFinite(meanGuess))throw Error('Normalized mean input dimensions or guess invalid');
 L[0]=meanGuess;let e,iterations;
 for(let it=0;it<30;it++){
  iterations=it;e=engine.evaluateL(L,Q,g,true);
  const error=e.moments[0],scale=Math.max(1e-300,e.maxQuad,Math.abs(L[0]));
  if(Math.abs(error)<=8e-14*scale)break;
  const correction=error/e.B[0];let accepted=false;
  for(let k=0;k<20;k++){
   const trial=Float64Array.from(L);trial[0]-=correction*2**(-k);
   try{const v=engine.evaluateL(trial,Q,g,false);if(Math.abs(v.moments[0])<Math.abs(error)){L.set(trial);accepted=true;break;}}catch(_){}
  }
  if(!accepted)throw Error('Normalized initial full mean root failed');
  if(it===29)throw Error('Normalized initial mean iteration limit');
 }
 e=engine.evaluateL(L,Q,g,true);
 const state=new Float64Array(2*M+2);state.set(Q);
 for(let j=0;j<M;j++)state[M+j]=g.momentumInverseFactor*e.moments[j+1];
 if(!state.every(Number.isFinite))throw Error('Normalized initial momentum outside binary64 range');
 return {state,L,g,meanPhysical:g.w*L[0],normalizedMeanResidual:e.moments[0],meanIterations:iterations,minA:e.minA,minD:e.minD,minS:e.minS};
}
