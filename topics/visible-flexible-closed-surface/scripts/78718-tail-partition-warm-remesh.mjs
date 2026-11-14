// Same-state, same-equation shooting refinement. All inserted nodes are warm
// data from actual partial RK flows, not converged responses. Existing nodes
// are copied without a root, amplitude change or momentum reprojection.
import {remeshCheckpoint} from './950f-tail-warm-remesh.mjs';

export function partitionWarmRemesh(prior,dn){
 const old=prior.parameters,now=dn.tail.parameters,
  oldParts=old.shootingParts,newParts=now.shootingParts,
  oldDepth=old.physicalDepth??old.depth,depth=now.physicalDepth??now.depth,
  M=now.modes,K=2*M;
 if(!(Number.isInteger(oldParts)&&oldParts>0&&Number.isInteger(newParts)&&
      newParts>oldParts&&newParts%oldParts===0))
  throw Error('Partition warm requires an integral refinement of shootingParts');
 if(old.modes!==M||old.quadrature!==now.quadrature||oldDepth!==depth||
    old.spacing!==now.spacing||old.orientation!==now.orientation)
  throw Error('Partition warm requires the same M/N, physical depth, spacing and orientation');
 const factor=newParts/oldParts;
 if(!(Number.isInteger(old.steps)&&Number.isInteger(now.steps)&&old.steps>0&&now.steps>0&&
      old.steps===factor*now.steps))
  throw Error('Partition warm must retain the original raw-profile RK density');
 if(!Array.isArray(prior.rawNode)||prior.rawNode.length!==dn.tail.rawNode.length||
    prior.rawNode.some((v,n)=>v*factor!==dn.tail.rawNode[n])||
    prior.states.length!==prior.rawNode.at(-1)+1||
    prior.states.some(row=>row.length!==K||!row.every(Number.isFinite)))
  throw Error('Partition warm has incompatible saved node layout');
 // Use the actual selected engine objects. In the current branch these have
 // already been replaced by the original-precision Fourier-root factory.
 // The old remesher constructs the partial physical profile and executes
 // old.steps*oldParts*partialWidth RK steps, including its actual cusp splits.
 const engines=new Map(dn.tail.cells.map(cell=>[cell.mu,cell.engine]));
 const factory=options=>{
  if(options.modes!==M||options.quadrature!==now.quadrature||
     options.spacing!==now.spacing||options.orientation!==now.orientation||
     options.projectionFloor!==now.projectionFloor||!engines.has(options.mu))
   throw Error('Partition warm engine options differ from the selected actual engine');
  return engines.get(options.mu);
 };
 const start=Date.now(),states=remeshCheckpoint(prior,dn,factory);
 let maximumRetainedNodeChange=0,retainedNodesBitwiseEqual=true,insertedNodes=0;
 for(let n=0;n<prior.states.length;n++)for(let j=0;j<K;j++){
  const a=states[factor*n][j],b=prior.states[n][j];
  maximumRetainedNodeChange=Math.max(maximumRetainedNodeChange,Math.abs(a-b));
  retainedNodesBitwiseEqual&&=Object.is(a,b);
 }
 for(let n=0;n<states.length;n++){
  if(states[n].length!==K||!states[n].every(Number.isFinite))
   throw Error('Partition warm produced a nonfinite or malformed node');
  if(n%factor!==0)insertedNodes++;
 }
 if(!retainedNodesBitwiseEqual)throw Error('Partition warm changed an existing saved node');
 const oldStages=prior.states.length-1;
 return {states,diagnostics:{method:'actual-partial-RK-partition-warm-v1',
  scope:'UNCONVERGED initial guess only. The new full shooting residual must be actually solved; no equality of nonzero old/new normalized residuals is asserted.',
  sourceModes:old.modes,targetModes:M,sourceQuadrature:old.quadrature,targetQuadrature:now.quadrature,
  physicalDepth:depth,sourceShootingParts:oldParts,targetShootingParts:newParts,
  sourceStepsPerStage:old.steps,targetStepsPerStage:now.steps,
  nominalRKStepsPerRawProfile:newParts*now.steps,refinementFactor:factor,
  sourceNodeCount:prior.states.length,nodeCount:states.length,insertedNodes,
  retainedNodesBitwiseEqual,maximumRetainedNodeChange,
  partialFlowNominalRKSteps:oldStages*now.steps*factor*(factor-1)/2,
  midpointEngine:'actual selected cell.engine; original root precision and original physical RHS',
  actualCriticalPointSplits:true,partialPhysicalCoordinateRoundingMayDiffer:true,
  noMomentumReprojection:true,knownConvergenceNotInferred:true,sourceScope:prior.scope,
  seconds:(Date.now()-start)/1000}};
}
