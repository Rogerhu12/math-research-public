// fd2d complete modified-prefix consumer; original solver retained below.
// Share identical engine closures across numerical stages of each cell.
// Optional complete-RHS factory. It leaves the published default factory
// untouched and changes only the arithmetic evaluation of identical equations.
import {createCompactTailDN} from './fd2d-gc-tail-deep-cached-core.mjs';
export function createSplitFluxCompactTailDN(options={}){
  const dn=createCompactTailDN({...options,fastJacobian:true});
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
