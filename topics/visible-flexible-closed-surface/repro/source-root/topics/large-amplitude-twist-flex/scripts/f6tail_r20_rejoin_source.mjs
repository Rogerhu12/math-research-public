// Optional fixed-source rejoin to the literal R20 delta/eta sequence.
// Alpha is defined mathematically by the same exact canonical mode2 zero;
// this evaluator approximates it with the stated calibrationSteps.
// Source agreement alone does not certify any nonlinear trace or full DN.
import {calibrateBalancedCell} from './tailnext_balanced_tail.mjs';
import cells from './general_root_smooth_tail_cells.cjs';
const {cellSegments,cellSmooth,cellSmoothDerivative}=cells;
export function rejoinedTailLength({delta0=.006,etaRatioAtN0=.05,etaPower=1.5,rejoinR20At=48,rejoinIndexOffset=4}={}){
 const q=2**(-etaPower),deepDelta0=.08*2**(-rejoinIndexOffset),deepC0=.05*2**(-rejoinIndexOffset/2),oldFrom=n=>6*delta0*2**(-n)+6*etaRatioAtN0*delta0*q**n/(1-q),newFrom=n=>6*deepDelta0*2**(-n)+6*deepC0*deepDelta0*q**n/(1-q);
 const tailFrom=n=>n>=rejoinR20At?newFrom(n):oldFrom(n)-oldFrom(rejoinR20At)+newFrom(rejoinR20At);
 return {total:tailFrom(0),tailFrom,deepDelta0,deepC0,oldTotal:oldFrom(0),tailLengthChange:newFrom(rejoinR20At)-oldFrom(rejoinR20At)};
}
export function createRejoinedBalancedTail(options={}){
 const {depth=80,delta0=.006,R=64,a=2.75,etaPower=1.5,etaRatioAtN0=.05,epsilonScale=.1,rCuff=1,orientation=1,calibrationSteps=1024,prefixEnd=15,prefixR=8,prefixRByCell=null,rejoinR20At=48,rejoinIndexOffset=4}=options;
 if(!(R===64&&a===2.75&&etaPower===1.5&&Number.isInteger(rejoinR20At)&&rejoinR20At>prefixEnd&&Number.isInteger(rejoinIndexOffset)&&rejoinIndexOffset>=0))throw Error('literal R20 source rejoin requires R64,a11/4,etaPower3/2 and a fixed deep integer index');
 const lengths=rejoinedTailLength({delta0,etaRatioAtN0,etaPower,rejoinR20At,rejoinIndexOffset}),A=a*Math.log(2),logMu0=Math.log(epsilonScale)+a*Math.log(delta0);
 function physicalCell(n){const joined=n>=rejoinR20At,delta=(joined?lengths.deepDelta0:delta0)*2**(-n),c=(joined?lengths.deepC0:etaRatioAtN0)*2**(-n/2),Rn=n<=prefixEnd?(prefixRByCell?.[n]??prefixR):R,cal=calibrateBalancedCell({delta,R:Rn,c,A,steps:calibrationSteps}),logMu=logMu0-a*n*Math.log(2),mu=Math.exp(logMu),after=lengths.tailFrom(n+1),rOuter=rCuff*Math.exp(orientation*after/Math.sqrt(12));let offset=0;
  const profiles=cellSegments(delta,Rn,cal.alpha,A,c).map(seg=>{const len=seg.lengthRatio*delta,start=offset;offset+=len;return x=>{const s=seg.transition?cellSmooth(x):0,ds=seg.transition?cellSmoothDerivative(x):0,logRadius=Math.log(rOuter)+orientation*(start+len*x)/Math.sqrt(12),r=Math.exp(logRadius);return {r,drdx:orientation*len*r/Math.sqrt(12),logw:logMu+seg.lo+(seg.hi-seg.lo)*s-Math.log(delta)-7*logRadius,dlogwdx:(seg.hi-seg.lo)*ds-7*orientation*len/Math.sqrt(12)};};});
  return {n,physicalIndex:joined?n+rejoinIndexOffset:n,delta,c,R:Rn,mu,logMu,rOuter,cal,profiles,length:offset,joinedLiteralR20:joined};
 }
 const actual=Array.from({length:depth},(_,n)=>physicalCell(n)),deepEpsilon=epsilonScale*(delta0/lengths.deepDelta0)**a;
 return {cells:actual,physicalCell,parameters:{...options,depth,delta0,R,a,etaPower,etaRatioAtN0,epsilonScale,rCuff,orientation,calibrationSteps,prefixEnd,prefixR,prefixRByCell,rejoinR20At,rejoinIndexOffset,deepDelta0:lengths.deepDelta0,deepEtaRatioAtN0:lengths.deepC0,deepEpsilon,deepEpsilonAfterRadiusScaling:deepEpsilon/rCuff**7,sourceLengthChange:lengths.tailLengthChange,sourceDefinition:'For n>=rejoinR20At, literal R20 delta/eta sequence at index n+offset, unchanged mu ports and rescaled epsilon; numerical alpha evaluation remains an approximation to its exact defining zero. Outer direction and nonlinear trace applicability remain separate.'}};
}
