// One root/split/product engine per physical cell. Unlike the old wrapper,
// construction does not allocate unused raw and fast Jacobian engine copies.
import {createSplitFluxMomentumTailEngine} from './fd2d-gc-tail-deep-split-flux.mjs';
import {createFourierProductVariationalEngine} from './fd2d-gc-tail-deep-product-flow.mjs';
export function createDeepSplitMomentumEngine(options={}){
 const base=createSplitFluxMomentumTailEngine(options);
 return createFourierProductVariationalEngine(options,base);
}
