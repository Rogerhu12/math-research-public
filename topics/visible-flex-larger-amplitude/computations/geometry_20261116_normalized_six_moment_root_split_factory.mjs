// R615/request253: originala47df full constructor, one actual R611 local-J.
// The original root module path is preserved for the real capacity loader.
// Complete optional engine: same momentum root policy and split state RHS,
// with finite Fourier-product Gram and variational projection assembly.
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createFourierProductVariationalEngine} from './geometry_20261116_normalized_six_moment_fourier_product_flow.mjs';
const sourceTopic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!sourceTopic)throw Error('Actual original public source topic required');
const {createFourierRootMomentumTailEngine}=await import(pathToFileURL(
 path.join(sourceTopic,'scripts/78718-tail-fourier-root-momentum.mjs')));
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const sourceURL=name=>pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',name));
const {createSplitFluxMomentumTailEngine}=await import(sourceURL('f6tail_momentum_split_flux.mjs'));
const {withCuspAwareRK}=await import(sourceURL('f6tail_cusp_grid.mjs'));

export function createFourierRootSplitFluxEngine(options={}){
 const rootBase=createFourierRootMomentumTailEngine(options),
  originalSplit=createSplitFluxMomentumTailEngine(options),{size}=rootBase;
 function rhs(state,profile,x,detail=false,knownRoot=null){
  const rt=knownRoot??rootBase.root(state,profile,x);
  return originalSplit.rhs(state,profile,x,detail,rt);
 }
 function rk4(state,profile,x,h){
  const a=rhs(state,profile,x),t=new Float64Array(size);
  for(let j=0;j<size;j++)t[j]=state[j]+h*a[j]/2;
  const b=rhs(t,profile,x+h/2);for(let j=0;j<size;j++)t[j]=state[j]+h*b[j]/2;
  const c=rhs(t,profile,x+h/2);for(let j=0;j<size;j++)t[j]=state[j]+h*c[j];
  const d=rhs(t,profile,x+h);return Float64Array.from(state,(v,j)=>v+h*(a[j]+2*b[j]+2*c[j]+d[j])/6);
 }
 const unavailable=()=>{throw Error('This optional split engine does not expose legacy flowRawCell; use its explicit rk4 or flowStateWithJacobian.');};
 let engine=createFourierProductVariationalEngine(options,{
  ...rootBase,rhs,rk4,statistics:originalSplit.statistics,flowRawCell:unavailable,
  rhsEvaluation:'split-linear-flux-v1',
  rootEvaluation:'fourier-product-gram-v1'
 });
 if(options.cuspAwareFlow===true)engine=withCuspAwareRK(engine);
 return engine;
}

