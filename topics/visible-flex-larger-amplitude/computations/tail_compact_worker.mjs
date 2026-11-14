// Original-g compact memory adapter with accepted-trial recovery and explicit GC.
// The immutable worker and its dependencies are evaluated in memory unchanged
// except for the explicit, recorded substitutions below.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!topic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC is required');
const workerPath=path.join(topic,'scripts/78718-prefix-tail-tangent-fourier-worker.mjs');
const slopeURL=new URL('./numerical-tail-slope-jacobian.mjs',import.meta.url).href;
const geometryURL=new URL('./tail_compact_geometry.mjs',import.meta.url).href;
const engineURL=new URL('./tail_resumable_engine.mjs',import.meta.url).href;
const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const original=fs.readFileSync(workerPath,'utf8');
let source=original;
const replacements=[];
function replaceOnce(before,after){
  const count=source.split(before).length-1;
  if(count!==1)throw Error('Stored-tail adapter source mismatch, count='+count);
  source=source.replace(before,after);replacements.push({before,after,count});
}
replaceOnce(
  "import {createSplitFluxCompactTailDN as createCompactTailDN} from './78718-tail-tangent-split.mjs';",
  `import {createStoredFiniteTailDN as createSourceCompactTailDN,storedEngineManifest} from ${JSON.stringify(engineURL)};`
);
replaceOnce('const physical=createRecalibrationFactory(cfg).assemble();',
  'const storedGeometry=await createStoredPhysical(cfg),physical=storedGeometry.physical;');
replaceOnce("amplitudeWarm:'physical-Q-L-amplitude-v1'",
  "amplitudeWarm:'physical-Q-L-amplitude-v1',endpointJacobianAdapter:adapterManifest,storedMetricAdapter:storedGeometry.manifest,stableGraphAdapter:storedEngineManifest");
replaceOnce('jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,history:sol.history',
  'jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,heightJetJacobianMethod:sol.heightJetJacobianMethod??null,endpointJacobianDiagnostics:sol.endpointJacobianDiagnostics??null,history:sol.history');
replaceOnce('const sol=dn.solve(req.height,',
  "   const gcBefore=process.memoryUsage(); if(typeof globalThis.gc==='function')globalThis.gc(); trace({event:'compact_storage_gc_before_solve',call,before:gcBefore,after:process.memoryUsage()});\n   const sol=dn.solve(req.height,");
const importRedirects=[];
for(const relative of new Set([...source.matchAll(/['"]\.\/([^'"]+)['"]/g)].map(x=>x[1]))){
  const absolute=pathToFileURL(path.join(topic,'scripts',relative)).href;
  source=source.replaceAll("'./"+relative+"'",JSON.stringify(absolute))
    .replaceAll('"./'+relative+'"',JSON.stringify(absolute));
  importRedirects.push({relative,absolute});
}
const wrapper=`
function createCompactTailDN(options){
  const dn=createSourceCompactTailDN(options),sourceSolve=dn.solve;
  dn.solve=(height,opts={})=>{
    const sol=sourceSolve(height,opts);
    if(opts.jacobian&&sol.converged){
      const actual=actualSlopeJacobian(dn,sol);
      sol.heightJetJacobian=Array.from(replaceFirstSlopeRows(sol.heightJetJacobian,actual));
      sol.heightJetJacobianMethod={
        slope:'analytic actual shooting tangent plus exact cut chain rule',
        meanSlopeCorrection:'analytic actual shooting tangent plus exact cut chain rule',
        second:'source symmetric difference on actual tangent graph',
        meanSecondCorrection:'source symmetric difference on actual tangent graph',
        height:'source symmetric difference; mathematically identity',
        sourceSecondDifferenceStep:1e-4
      };
      sol.endpointJacobianDiagnostics={cut:actual.cut,root:actual.root};
    }
    return sol;
  };
  return dn;
}
`;
const manifest={
  name:'numerical-analytic-first-slope-and-mean-v1',
  storageAdapter:'tail-original-stored-bounded-shared-graphs-v1',
  recoveryAdapter:'accepted-trial-recovery-only-v1',
  sourceWorker:workerPath,sourceWorkerSHA256:sha256(original),
  slopeModule:slopeURL,slopeModuleSHA256:sha256(fs.readFileSync(new URL(slopeURL))),
  adapterSHA256:sha256(fs.readFileSync(new URL(import.meta.url))),
  sourceRevision:JSON.parse(fs.readFileSync(path.join(topic,'source-origin.json'),'utf8')).source_revision,
  replacements,importRedirects,
  scope:'Original stored metric with bounded point memoization and shared linear graph grid, analytic endpoint rows, and immediate recovery-only recording of already accepted trials. No rational deep model or acceptance change.'
};
source=`import {actualSlopeJacobian,replaceFirstSlopeRows} from ${JSON.stringify(slopeURL)};\n`+
  `import {createStoredPhysical} from ${JSON.stringify(geometryURL)};\n`+
  `const adapterManifest=${JSON.stringify(manifest)};\n`+source+wrapper;
try{
  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
}catch(error){
  console.error(String(error?.stack??error).replace(
    /data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<in-memory-stored-tail-worker>'));
  process.exitCode=1;
}
