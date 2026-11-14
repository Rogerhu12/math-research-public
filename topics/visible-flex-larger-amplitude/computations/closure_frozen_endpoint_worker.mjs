// Original endpoint worker SHA256 b3be6397e951ddbaab021e6f2d31670d8d4f2f2d7ee30c623cb6d8cfe2c8b4c7
// Explicit new-g worker. The old analytic worker and its fixed-g chains remain
// untouched. All changes below are source-checked, opt-in in-memory adapters.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const sourceTopic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!sourceTopic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC is required');
const workerPath=path.join(sourceTopic,'scripts/78718-prefix-tail-tangent-fourier-worker.mjs');
const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const original=fs.readFileSync(workerPath,'utf8');
let source=original;
const replacements=[];
function replaceOnce(before,after){
  const count=source.split(before).length-1;
  if(count!==1)throw Error('Rational worker source replacement is not unique: '+count);
  source=source.replace(before,after);replacements.push({before,after,count});
}
const modelURL=new URL('./strong_frozen_rational_model.mjs',import.meta.url).href;
const engineURL=new URL('./closure_scaled_endpoint_engine.mjs',import.meta.url).href;
const slopeURL=new URL('./numerical-tail-slope-jacobian.mjs',import.meta.url).href;
const cacheURL=new URL('./closure_bounded_point_cache.mjs',import.meta.url).href;
const depthWarmURL=new URL('./closure_depth_warm_remesh.mjs',import.meta.url).href;
replaceOnce(
  "import {createSplitFluxCompactTailDN as createCompactTailDN} from './78718-tail-tangent-split.mjs';",
  `import {createRationalFiniteTailDN as createSourceCompactTailDN,rationalEngineManifest} from ${JSON.stringify(engineURL)};`
);
replaceOnce('const physical=createRecalibrationFactory(cfg).assemble();',`
const rationalModel=await createRationalDeepTail(cfg,{sourceTopic:process.env.VISIBLE_FLEX_SOURCE_TOPIC,
  frozenWarpAlpha:cfg.rationalFrozenWarpAlpha??null,pointCacheLimit:cfg.rationalPointCacheLimit??96});
if(!(cfg.linearFar>rationalModel.start))throw Error('New-g worker requires linearFar beyond the rational-source start');
const physical={...rationalModel.head,
  cells:Array.from({length:cfg.linearFar},(_,n)=>rationalModel.cell(n)),
  parameters:{...rationalModel.head.parameters,rationalDeepExtension:{start:rationalModel.start,alpha:'65/64',
    headFingerprint:rationalModel.manifest.headFingerprint,frozenWarpAlpha:rationalModel.manifest.frozenWarpAlpha}}};
`);
replaceOnce("amplitudeWarm:'physical-Q-L-amplitude-v1'",
  "amplitudeWarm:'physical-Q-L-amplitude-v1',endpointJacobianAdapter:adapterManifest,rationalEngine:rationalEngineManifest,rationalDeepModel:rationalModel.manifest,shallowHeadPreserved:dn.rationalHeadPreserved,deepLinearBridge:dn.deepLinearBridge,postGraphCacheReclamation:dn.postGraphCacheReclamation,shallowSourceParameters:dn.shallowSourceParameters");
replaceOnce('jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,history:sol.history',
  'jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,heightJetJacobianMethod:sol.heightJetJacobianMethod??null,endpointCanonicalTrace:sol.endpointCanonicalTrace??null,history:sol.history');
replaceOnce('const embedded=geometricWarmRemesh(prior,dn,createFastSplitFluxMomentumTailEngine);',
  'const embedded=(old.physicalDepth??old.depth)===cfg.depth?geometricWarmRemesh(prior,dn,createFastSplitFluxMomentumTailEngine):depthWarmRemesh(prior,dn,createFastSplitFluxMomentumTailEngine);');
const importRedirects=[];
for(const relative of new Set([...source.matchAll(/['"]\.\/([^'"]+)['"]/g)].map(x=>x[1]))){
  const absolute=pathToFileURL(path.join(sourceTopic,'scripts',relative)).href;
  source=source.replaceAll("'./"+relative+"'",JSON.stringify(absolute)).replaceAll('"./'+relative+'"',JSON.stringify(absolute));
  importRedirects.push({relative,absolute});
}
const manifest={name:'closure-frozen-calibration-endpoint-worker-v1',
  sourceWorker:workerPath,sourceWorkerSHA256:sha256(original),
  ownHashes:Object.fromEntries(['closure_frozen_endpoint_worker.mjs','strong_frozen_rational_model.mjs','strong_frozen_calibration_factory.mjs','closure_scaled_endpoint_worker.mjs','closure_rational_tail_model.mjs',
    'closure_scaled_endpoint_engine.mjs','closure_scaled_endpoint_graphs.mjs','closure_linear_stage_graphs.mjs',
    'closure_bounded_point_cache.mjs','closure_depth_warm_remesh.mjs','numerical-tail-slope-jacobian.mjs']
    .map(n=>[n,sha256(fs.readFileSync(new URL('./'+n,import.meta.url)))])),
  replacements,importRedirects,
  scope:'A NEW fixed rational-deep metric. Original shallow cell objects/global warp are retained. Finite nonlinear DN only; no infinite nonlinear existence or closed-shape claim.'};
const wrapper=`
function createCompactTailDN(options){
  const dn=createSourceCompactTailDN(options),sourceSolve=dn.solve;
  dn.rationalHeadPreserved=rationalModel.assertFrozenHead();
  const beforeReclamation=process.memoryUsage();
  installBoundedPointCache(rationalModel.factory,{count:rationalModel.start,
    controls:cfg.valleyControls??[],limit:cfg.rationalPointCacheLimit??96});
  dn.rationalHeadPreserved=rationalModel.assertFrozenHead();
  const gcAvailable=typeof global.gc==='function';
  if(gcAvailable)global.gc();
  dn.postGraphCacheReclamation={before:beforeReclamation,after:process.memoryUsage(),gcAvailable,
    scope:'Only point memoization is reset after the far graph. Source formula, frozen metric and all nonlinear data are unchanged.'};
  dn.shallowSourceParameters={interpretation:'Saved binary cell parameters, not certified exact calibration roots.',
    cells:rationalModel.head.source.cells.map(c=>({n:c.physicalIndex,delta:c.delta,R:c.R,
      c:c.c,lengthScale:c.lengthScale,alpha:c.cal.alpha}))};
  dn.solve=(height,opts={})=>{
    const sol=sourceSolve(height,opts);
    if(sol.converged&&sol.states){
      const stage=dn.tail.cells.at(-1),M=dn.tail.parameters.modes;
      const state=new Float64Array(2*M+2);state.set(sol.states.at(-1));
      const root=stage.engine.root(state,stage.profiles[0],0),g=root.g;
      const factor=Math.sqrt(2)*g.r**4*g.w2/(Math.sqrt(12)*stage.mu);
      const canonicalXi=Array.from({length:M},(_,j)=>factor*root.L[j+1]);
      const connectionMomentum=Array.from(state.slice(M,2*M));
      sol.endpointCanonicalTrace={physicalNode:dn.tail.parameters.physicalDepth,
        sourceCell:dn.tail.parameters.physicalDepth-1,radius:g.r,w:g.w,mu:stage.mu,
        Q:Array.from(state.slice(0,M)),canonicalXi,connectionMomentum,
        connectionMinusCanonical:connectionMomentum.map((v,j)=>v-canonicalXi[j]),
        meanSlopeCorrection:g.w*root.L[0],rootRelativeResidual:root.err/root.scale,
        minLeading:root.e.minA,minD:root.e.minD,
        formula:'Xi = sqrt(2)*r^4*w^2/(sqrt(12)*mu) * L_nonmean; Pi is the nonlinear connection momentum.',
        scope:'Actual finite-root coordinate conversion at the nonlinear endpoint. No complete-angle root or omitted radial flow certificate.'};
    }
    if(opts.jacobian&&sol.converged){
      const actual=actualSlopeJacobian(dn,sol);
      sol.heightJetJacobian=Array.from(replaceFirstSlopeRows(sol.heightJetJacobian,actual));
      sol.heightJetJacobianMethod={slope:'analytic actual shooting tangent',meanSlopeCorrection:'analytic actual shooting tangent',
        second:'source symmetric difference',meanSecondCorrection:'source symmetric difference',height:'source symmetric difference; exact map is identity'};
    }
    return sol;
  };
  return dn;
}
`;
source=`import {createRationalDeepTail} from ${JSON.stringify(modelURL)};\n`+
  `import {installBoundedPointCache} from ${JSON.stringify(cacheURL)};\n`+
  `import {depthWarmRemesh} from ${JSON.stringify(depthWarmURL)};\n`+
  `import {actualSlopeJacobian,replaceFirstSlopeRows} from ${JSON.stringify(slopeURL)};\n`+
  `const adapterManifest=${JSON.stringify(manifest)};\n`+source+wrapper;
try{
  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
}catch(error){
  console.error(String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<in-memory-rational-tail-worker>'));
  process.exitCode=1;
}
