// Share identical engine closures across numerical stages of each cell.
// Optional complete-RHS factory. It leaves the published default factory
// untouched and changes only the arithmetic evaluation of identical equations.
import {createCompactTailDN} from './78718-tail-parallel-stage-core.mjs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const sourceURL=name=>pathToFileURL(path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts',name));
const {createFastSplitFluxMomentumTailEngine}=await import(sourceURL('f6tail_fast_split_flux_engine.mjs'));
const {withCuspAwareRK}=await import(sourceURL('f6tail_cusp_grid.mjs'));

export function createSplitFluxCompactTailDN(options={}){
  const dn=createCompactTailDN({...options,fastJacobian:true}),p=dn.tail.parameters;
  const replaced=new Set();
  for(const cell of dn.tail.cells){
    if(replaced.has(cell.engine))continue;
    replaced.add(cell.engine);
    let engine=createFastSplitFluxMomentumTailEngine({modes:p.modes,spacing:p.spacing,quadrature:p.quadrature,
      mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor});
    if(options.cuspAwareFlow===true)engine=withCuspAwareRK(engine);
    // Preserve object identity: cutJets and the implicit physical jet evaluator
    // retain this object and dereference its root/rhs methods at call time.
    Object.assign(cell.engine,engine);
  }
  dn.tail.parameters.rhsEvaluation='split-linear-flux-v1';
  const solveQ=dn.tail.solve;
  dn.tail.solve=(target,opts={})=>{
    const result=solveQ(target,opts);result.parameters.rhsEvaluation='split-linear-flux-v1';
    result.rhsEvaluation='split-linear-flux-v1';return result;
  };
  const solve=dn.solve;
  dn.solve=(height,opts={})=>{
    const result=solve(height,opts);
    result.parameters.rhsEvaluation='split-linear-flux-v1';
    result.rhsEvaluation='split-linear-flux-v1';
    return result;
  };
  return dn;
}
