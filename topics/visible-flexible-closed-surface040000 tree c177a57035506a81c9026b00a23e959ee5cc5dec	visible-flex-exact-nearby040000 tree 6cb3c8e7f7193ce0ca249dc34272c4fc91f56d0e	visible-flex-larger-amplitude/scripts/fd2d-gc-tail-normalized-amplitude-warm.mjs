// Exactly the physical Q/L amplitude initializer in normalized arithmetic.
// It is only a guess; the full nonlinear residual decides acceptance.
import {initializeNormalizedMean} from './fd2d-gc-tail-normalized-mean.mjs';
export function geometricAmplitudeWarm(inputStates,dn,scale){
 const tail=dn.tail,{modes:M,spacing}=tail.parameters,K=2*M,sq2=Math.sqrt(2);
 if(!(Number.isFinite(scale)&&scale>0))throw Error('Positive finite amplitude scale required');
 if(!Array.isArray(inputStates)||inputStates.length!==tail.cells.length+1)throw Error('Geometric amplitude warm node count mismatch');
 const states=new Array(inputStates.length),diagnostics={method:'same-physical-Q-L-amplitude-normalized-arithmetic-v1',
  scale,modes:M,quadrature:tail.parameters.quadrature,nodeCount:inputStates.length,
  maxQScalingError:0,maxNonconstantURScalingErrorFourierL1:0,maxMeanURDepartureFromLinearScaling:0,
  maxMomentumDepartureFromLinearScalingRelative:0,maxRootRelativeResidual:0,minLeading:Infinity,minD:Infinity,
  scope:'Warm guess only. Same nonmean physical Q/L scaling and complete mean root, without physical raw roundtrip. New Dirichlet boundary and full nonlinear F remain required.'};
 for(let node=0;node<inputStates.length;node++){
  const old=inputStates[node];if(old.length!==K)throw Error('Warm state width mismatch at node '+node);
  const cell=tail.cells[node===0?0:node-1],profile=node===0?cell.profiles.at(-1):cell.profiles[0],x=node===0?1:0,
   port=node===0?cell.portRatio:1,engine=cell.engine,y=new Float64Array(K+2);
  for(let j=0;j<M;j++){y[j]=old[j];y[M+j]=port*old[M+j];}
  let rt,initialized,nextRoot;
  try{
   rt=engine.root(y,profile,x);
   const Q=Float64Array.from(y.slice(0,M),v=>scale*v),L=Float64Array.from(rt.L,v=>scale*v);
   initialized=initializeNormalizedMean(engine,Q,L,profile,x,0);
   nextRoot=engine.root(initialized.state,profile,x);
  }catch(error){throw Error('Normalized amplitude warm failed at node '+node+': '+String(error));}
  const next=initialized.state,g=rt.g,ng=nextRoot.g,row=new Array(K);
  let slopeL1=0,piDifference=0,piScale=0;
  for(let j=0;j<M;j++){
   const ell=spacing*(j+1),before=sq2*g.w*rt.L[j+1]+ell*ell*g.r**3*y[j],after=sq2*ng.w*nextRoot.L[j+1]+ell*ell*ng.r**3*next[j];
   slopeL1+=Math.abs(after-scale*before);diagnostics.maxQScalingError=Math.max(diagnostics.maxQScalingError,Math.abs(next[j]-scale*y[j]));
   piDifference=Math.max(piDifference,Math.abs(next[M+j]-scale*y[M+j]));piScale=Math.max(piScale,Math.abs(scale*y[M+j]));
   row[j]=next[j];row[M+j]=next[M+j]/port;
  }
  diagnostics.maxNonconstantURScalingErrorFourierL1=Math.max(diagnostics.maxNonconstantURScalingErrorFourierL1,slopeL1);
  diagnostics.maxMeanURDepartureFromLinearScaling=Math.max(diagnostics.maxMeanURDepartureFromLinearScaling,Math.abs(ng.w*nextRoot.L[0]-scale*g.w*rt.L[0]));
  diagnostics.maxMomentumDepartureFromLinearScalingRelative=Math.max(diagnostics.maxMomentumDepartureFromLinearScalingRelative,piDifference/Math.max(1e-300,piScale));
  diagnostics.maxRootRelativeResidual=Math.max(diagnostics.maxRootRelativeResidual,nextRoot.err/nextRoot.scale);
  diagnostics.minLeading=Math.min(diagnostics.minLeading,nextRoot.e.minA);diagnostics.minD=Math.min(diagnostics.minD,nextRoot.e.minD);
  states[node]=row;
 }
 return {states,diagnostics};
}
