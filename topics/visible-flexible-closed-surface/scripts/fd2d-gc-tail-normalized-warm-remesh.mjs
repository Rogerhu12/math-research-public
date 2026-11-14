// Same spectral physical Q/L prolongation; no physical slope underflow.
// Spectral prolongation through physical Q/L coordinates, not by zero-padding
// the nonlinear connection momentum. This only prepares a numerical guess.
// The caller must keep the original physical-geometry compatibility checks.
import {initializeNormalizedMean} from './fd2d-gc-tail-normalized-mean.mjs';

function gcd(a,b){while(b){const r=a%b;a=b;b=r;}return a;}

export function geometricWarmRemesh(prior,dn,engineFactory){
 const old=prior.parameters,now=dn.tail.parameters,oldM=old.modes,M=now.modes,
  oldN=old.quadrature,N=now.quadrature,oldDepth=old.physicalDepth??old.depth,
  depth=now.physicalDepth??now.depth;
 if(!(Number.isInteger(oldM)&&M>=oldM))throw Error('Geometric warm embedding requires nondecreasing Fourier modes');
 if(oldDepth!==depth||old.shootingParts!==now.shootingParts)
  throw Error('Geometric warm embedding currently requires identical physicalDepth and shootingParts');
 if(old.spacing!==now.spacing||old.orientation!==now.orientation)
  throw Error('Geometric warm embedding requires the same angular spacing and orientation');
 if(prior.states.length!==dn.tail.cells.length+1)throw Error('Geometric warm node count mismatch');
 if(prior.rawNode&&(prior.rawNode.length!==dn.tail.rawNode.length||prior.rawNode.some((v,i)=>v!==dn.tail.rawNode[i])))
  throw Error('Geometric warm raw-cell node indices mismatch');
 const states=prior.states.map(row=>{if(row.length!==2*oldM)throw Error('Source warm width mismatch');const out=Array(2*M).fill(0);for(let j=0;j<oldM;j++){out[j]=row[j];out[M+j]=row[oldM+j];}return out;}),oldEngines=new Map(),
  commonAngles=gcd(oldN,N),spacing=old.spacing,sq2=Math.sqrt(2);
 const diagnostics={method:'same-physical-Q-L-prolongation-normalized-arithmetic-v1',scope:'Initial guess conversion only; no new shooting solve or high-mode trajectory is asserted.',
  sourceModes:oldM,targetModes:M,sourceQuadrature:oldN,targetQuadrature:N,
  physicalDepth:depth,shootingParts:now.shootingParts,nodeCount:states.length,
  commonAngularNodes:commonAngles,quadratureChanged:oldN!==N,
  maxQChange:0,maxNonconstantHeightChange:0,maxNormalizedNonmeanLGap:0,maxURGapCommonAngles:0,
  maxURGapFloatingFourierL1:0,maxMeanSlopeChange:0,maxLowMomentumRelativeChange:0,
  maxNewHighMomentumRelativeSize:0,maxRootRelativeResidual:0,
  minLeading:Infinity,minD:Infinity,worstURNode:null};
 for(let i=0;i<states.length;i++){
  const cell=dn.tail.cells[i===0?0:i-1],profile=i===0?cell.profiles.at(-1):cell.profiles[0],x=i===0?1:0,
   ratio=i===0?cell.portRatio:1;
  if(!(ratio>0&&Number.isFinite(ratio)))throw Error('Invalid port normalization');
  let oldEngine=oldEngines.get(cell.mu);
  if(!oldEngine){oldEngine=engineFactory({modes:oldM,spacing,quadrature:oldN,mu:cell.mu,
    orientation:old.orientation,projectionFloor:old.projectionFloor??.05});oldEngines.set(cell.mu,oldEngine);}
  const y=new Float64Array(2*oldM+2);
  for(let j=0;j<oldM;j++){y[j]=states[i][j];y[oldM+j]=states[i][M+j]*ratio;}
  const oldRoot=oldEngine.root(y,profile,x),Q=new Float64Array(M),L=new Float64Array(M+1);
  for(let j=0;j<oldM;j++){Q[j]=y[j];L[j+1]=oldRoot.L[j+1];}
  const nextEngine=cell.engine,initialized=initializeNormalizedMean(nextEngine,Q,L,profile,x,0),
   next=initialized.state,nextRoot=nextEngine.root(next,profile,x),g=oldRoot.g,ng=nextRoot.g;
  const meanGap=ng.w*(1+nextRoot.L[0])-g.w*(1+oldRoot.L[0]),delta=new Float64Array(M);
  let l1=Math.abs(meanGap),qChange=0,piScale=0,lowPiChange=0,highPiSize=0;
  for(let j=0;j<M;j++){
   const m=spacing*(j+1),oldCoefficient=j<oldM?sq2*g.w*oldRoot.L[j+1]+m*m*g.r**3*y[j]:0,
    newCoefficient=sq2*ng.w*nextRoot.L[j+1]+m*m*ng.r**3*next[j];
   delta[j]=newCoefficient-oldCoefficient;l1+=Math.abs(delta[j]);
   diagnostics.maxNormalizedNonmeanLGap=Math.max(diagnostics.maxNormalizedNonmeanLGap,Math.abs(nextRoot.L[j+1]-(j<oldM?oldRoot.L[j+1]:0)));
   qChange=Math.max(qChange,Math.abs(next[j]-states[i][j]));
   if(j<oldM){piScale=Math.max(piScale,Math.abs(y[oldM+j]));lowPiChange=Math.max(lowPiChange,Math.abs(next[M+j]-y[oldM+j]));}
   else highPiSize=Math.max(highPiSize,Math.abs(next[M+j]));
  }
  let urGap=0;
  for(let a=0;a<commonAngles;a++){const theta=2*Math.PI*a/commonAngles;let value=meanGap;for(let j=0;j<M;j++)value+=delta[j]*Math.cos(spacing*(j+1)*theta);urGap=Math.max(urGap,Math.abs(value));}
  if(urGap>diagnostics.maxURGapCommonAngles){diagnostics.maxURGapCommonAngles=urGap;diagnostics.worstURNode=i;}
  diagnostics.maxURGapFloatingFourierL1=Math.max(diagnostics.maxURGapFloatingFourierL1,l1);
  diagnostics.maxMeanSlopeChange=Math.max(diagnostics.maxMeanSlopeChange,Math.abs(meanGap));
  diagnostics.maxQChange=Math.max(diagnostics.maxQChange,qChange);
  diagnostics.maxNonconstantHeightChange=Math.max(diagnostics.maxNonconstantHeightChange,M*ng.r**4*qChange);
  diagnostics.maxLowMomentumRelativeChange=Math.max(diagnostics.maxLowMomentumRelativeChange,lowPiChange/Math.max(piScale,1e-300));
  diagnostics.maxNewHighMomentumRelativeSize=Math.max(diagnostics.maxNewHighMomentumRelativeSize,highPiSize/Math.max(piScale,1e-300));
  diagnostics.maxRootRelativeResidual=Math.max(diagnostics.maxRootRelativeResidual,nextRoot.err/nextRoot.scale);
  diagnostics.minLeading=Math.min(diagnostics.minLeading,nextRoot.e.minA);diagnostics.minD=Math.min(diagnostics.minD,nextRoot.e.minD);
  const row=Array(2*M);for(let j=0;j<M;j++){row[j]=next[j];row[M+j]=next[M+j]/ratio;}states[i]=row;
 }
 return {states,diagnostics};
}
