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
const modelURL=new URL('./closure_rational_tail_model.mjs',import.meta.url).href;
const engineURL=new URL('./closure_rational_tail_engine.mjs',import.meta.url).href;
const slopeURL=new URL('./numerical-tail-slope-jacobian.mjs',import.meta.url).href;
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
  "amplitudeWarm:'physical-Q-L-amplitude-v1',endpointJacobianAdapter:adapterManifest,rationalEngine:rationalEngineManifest,rationalDeepModel:rationalModel.manifest,shallowHeadPreserved:dn.rationalHeadPreserved");
replaceOnce('jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,history:sol.history',
  'jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,heightJetJacobianMethod:sol.heightJetJacobianMethod??null,history:sol.history');
const importRedirects=[];
for(const relative of new Set([...source.matchAll(/['"]\.\/([^'"]+)['"]/g)].map(x=>x[1]))){
  const absolute=pathToFileURL(path.join(sourceTopic,'scripts',relative)).href;
  source=source.replaceAll("'./"+relative+"'",JSON.stringify(absolute)).replaceAll('"./'+relative+'"',JSON.stringify(absolute));
  importRedirects.push({relative,absolute});
}
const manifest={name:'closure-rational-deep-worker-v1',
  sourceWorker:workerPath,sourceWorkerSHA256:sha256(original),
  ownHashes:Object.fromEntries(['closure_rational_tail_worker.mjs','closure_rational_tail_model.mjs',
    'closure_rational_tail_engine.mjs','closure_linear_stage_graphs.mjs','numerical-tail-slope-jacobian.mjs']
    .map(n=>[n,sha256(fs.readFileSync(new URL('./'+n,import.meta.url)))])),
  replacements,importRedirects,
  scope:'A NEW fixed rational-deep metric. Original shallow cell objects/global warp are retained. Finite nonlinear DN only; no infinite nonlinear existence or closed-shape claim.'};
const wrapper=`
function createCompactTailDN(options){
  const dn=createSourceCompactTailDN(options),sourceSolve=dn.solve;
  dn.rationalHeadPreserved=rationalModel.assertFrozenHead();
  dn.solve=(height,opts={})=>{
    const sol=sourceSolve(height,opts);
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
  `import {actualSlopeJacobian,replaceFirstSlopeRows} from ${JSON.stringify(slopeURL)};\n`+
  `const adapterManifest=${JSON.stringify(manifest)};\n`+source+wrapper;
try{
  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
}catch(error){
  console.error(String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<in-memory-rational-tail-worker>'));
  process.exitCode=1;
}
