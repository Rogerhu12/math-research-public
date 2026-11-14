// Owned adapter: evaluate the immutable recorded tail worker in memory,
// replacing only its first-slope/mean endpoint derivative rows.
// Source equations, physical geometry, warm starts and acceptance stay intact.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const sourceTopic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!sourceTopic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC is required');
const workerPath=path.join(sourceTopic,'scripts/78718-prefix-tail-tangent-fourier-worker.mjs');
const modulePath=new URL('./numerical-tail-slope-jacobian.mjs',import.meta.url);
const sha256=data=>crypto.createHash('sha256').update(data).digest('hex');
const original=fs.readFileSync(workerPath,'utf8');
let source=original;
const replacements=[];
function replaceOnce(before,after) {
  const count=source.split(before).length-1;
  if(count!==1)throw Error(`Analytic-tail adapter source mismatch: expected one occurrence, found ${count}`);
  source=source.replace(before,after);replacements.push({before,after,count});
}
replaceOnce(
  "import {createSplitFluxCompactTailDN as createCompactTailDN} from './78718-tail-tangent-split.mjs';",
  "import {createSplitFluxCompactTailDN as createSourceCompactTailDN} from './78718-tail-tangent-split.mjs';"
);
replaceOnce(
  "amplitudeWarm:'physical-Q-L-amplitude-v1'",
  "amplitudeWarm:'physical-Q-L-amplitude-v1',endpointJacobianAdapter:adapterManifest"
);
replaceOnce(
  'jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,history:sol.history',
  'jets:sol.jets,heightJetJacobian:sol.heightJetJacobian??null,heightJetJacobianMethod:sol.heightJetJacobianMethod??null,endpointJacobianDiagnostics:sol.endpointJacobianDiagnostics??null,history:sol.history'
);
// Dynamic evaluation has a data: module URL, so preserve each source import's
// location explicitly. No source file is materialized or modified.
const importRedirects=[];
for(const relative of new Set([...source.matchAll(/['"]\.\/([^'"]+)['"]/g)].map(v=>v[1]))) {
  const absolute=pathToFileURL(path.join(sourceTopic,'scripts',relative)).href;
  source=source.replaceAll("'./"+relative+"'",JSON.stringify(absolute))
               .replaceAll('"./'+relative+'"',JSON.stringify(absolute));
  importRedirects.push({relative,absolute});
}
const wrapper=`
function createCompactTailDN(options) {
  const dn=createSourceCompactTailDN(options), sourceSolve=dn.solve;
  dn.solve=(height,opts={})=>{
    const sol=sourceSolve(height,opts);
    if(opts.jacobian && sol.converged) {
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
  sourceWorker:workerPath,sourceWorkerSHA256:sha256(original),
  slopeModule:modulePath.href,slopeModuleSHA256:sha256(fs.readFileSync(modulePath)),
  adapterSHA256:sha256(fs.readFileSync(new URL(import.meta.url))),
  sourceRevision:JSON.parse(fs.readFileSync(path.join(sourceTopic,'source-origin.json'),'utf8')).source_revision,
  replacements,importRedirects,
  scope:'In-memory endpoint derivative adapter only. Original worker and dependency files remain immutable.'
};
source=`import {actualSlopeJacobian,replaceFirstSlopeRows} from ${JSON.stringify(modulePath.href)};\n`+
       `const adapterManifest=${JSON.stringify(manifest)};\n`+source+wrapper;
try {
  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
} catch(error) {
  // Preserve the diagnostic and line numbers without dumping the complete
  // encoded source body when an initialization precondition is rejected.
  console.error(String(error?.stack??error).replace(
    /data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<in-memory-tail-worker>'));
  process.exitCode=1;
}
