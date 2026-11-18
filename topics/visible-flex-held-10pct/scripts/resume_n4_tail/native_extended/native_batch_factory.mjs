// Installed next to the original stage factory in an independent owned copy.
// Construction remains original; the native cache is lazy until after split
// engine replacement. cutJets, physical jets, audit and FD stay original .05.
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {readNativeManifest,createNativeBatchEvaluator} from './native_batch_adapter.mjs';
import {createSplitFluxCompactTailDN} from './950f-tail-stage-split.mjs';

export function createNativeSplitFluxCompactTailDN(options={}){
  const loaded=readNativeManifest();
  if(options.nativeBatchFactory)throw Error('A second native batch factory is not supported');
  // Only metadata is read here. The original factory still constructs all
  // physical profiles, graphs, engines and boundary definitions.
  const gridAPI=options.nativeOriginalGridAPI;
  if(!gridAPI)throw Error('The original loaded cusp functions must be supplied');
  const dn=createSplitFluxCompactTailDN({...options,nativeBatchFactory:context=>
    createNativeBatchEvaluator(context,loaded,gridAPI)});
  dn.tail.parameters.shootingEvaluation='native-literal-LD-batch-v1';
  const mark=result=>{
    result.parameters.shootingEvaluation='native-literal-LD-batch-v1';
    result.parameters.nativeBatchManifestSHA256=loaded.binding.sha256;
    result.nativeBatchManifest=loaded.binding;return result;
  };
  const solveQ=dn.tail.solve;
  dn.tail.solve=(target,opts={})=>mark(solveQ(target,opts));
  const solve=dn.solve;
  dn.solve=(height,opts={})=>mark(solve(height,opts));
  return dn;
}

// Worker-compatible async module initialization loads the original pure cusp
// functions; it does not construct geometry or invoke an evaluator.
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!sourceRoot)throw Error('VISIBLE_FLEX_SOURCE_ROOT required');
const gridAPI=await import(pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));
export function createNativeCompactTailDN(options={}){
  return createNativeSplitFluxCompactTailDN({...options,nativeOriginalGridAPI:gridAPI});
}
