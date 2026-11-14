// In-memory opt-in: inject a batched linear graph constructor into the immutable
// finite nonlinear DN. The actual nonlinear ODE, Newton steps and gates remain
// those of the pinned source. The caller supplies the separately named new g.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {buildScaledEndpointGraphs,getDeepLinearBridge} from './closure_scaled_endpoint_graphs.mjs';

const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!topic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC required');
const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const corePath=path.join(topic,'scripts/78718-tail-tangent-core.mjs');
const splitPath=path.join(topic,'scripts/78718-tail-tangent-split.mjs');
const originalCore=fs.readFileSync(corePath,'utf8'),originalSplit=fs.readFileSync(splitPath,'utf8');
const before='const wholeGraph=buildStableStageGraphs(physical,stages,{modes:M,spacing,linearFar,linearSteps});';
const after='const wholeGraph=(options.stableGraphFactory??buildStableStageGraphs)(physical,stages,{modes:M,spacing,linearFar,linearSteps});';
if(originalCore.split(before).length!==2)throw Error('Pinned core graph injection no longer unique');
const acceptedBefore="opts.trialDiagnostic?.({...diagnostic,kind:'accepted',trialNorm:test.norm},null);break;";
const recoveryCallback="\n     opts.progress?.({iteration:it+1,norm:test.norm,phase:'accepted-trial-recovery-only',acceptedFromIteration:it,acceptedTrial:k,acceptedStep:lambda},states.map(v=>Array.from(v)));";
const acceptedAfter="opts.trialDiagnostic?.({...diagnostic,kind:'accepted',trialNorm:test.norm},null);"+recoveryCallback+'break;';
if(originalCore.split(acceptedBefore).length!==2)throw Error('Pinned accepted-trial callback insertion no longer unique');
const graphPatched=originalCore.replace(before,after);
const patchedCore=graphPatched.replace(acceptedBefore,acceptedAfter);
if(patchedCore.replace(recoveryCallback,'')!==graphPatched)
  throw Error('Recovery recording changed solver code outside its extra callback');
function redirect(source){
  for(const relative of new Set([...source.matchAll(/['"]\.\/([^'"]+)['"]/g)].map(x=>x[1]))){
    const absolute=pathToFileURL(path.join(topic,'scripts',relative)).href;
    source=source.replaceAll("'./"+relative+"'",JSON.stringify(absolute)).replaceAll('"./'+relative+'"',JSON.stringify(absolute));
  }
  return source;
}
const coreURL='data:text/javascript;base64,'+Buffer.from(redirect(patchedCore)).toString('base64');
let split=originalSplit.replace("'./78718-tail-tangent-core.mjs'",JSON.stringify(coreURL));
if(split===originalSplit)throw Error('Pinned split factory import missing');
const splitModule=await import('data:text/javascript;base64,'+Buffer.from(redirect(split)).toString('base64'));
export const rationalEngineManifest={
  coreSHA256:sha256(originalCore),splitSHA256:sha256(originalSplit),
  adapterSHA256:sha256(fs.readFileSync(new URL(import.meta.url))),
  graphSHA256:sha256(fs.readFileSync(new URL('./closure_scaled_endpoint_graphs.mjs',import.meta.url))),
  sharedGridSHA256:sha256(fs.readFileSync(new URL('./closure_linear_stage_graphs.mjs',import.meta.url))),
  replacement:{before,after},
  acceptedTrialRecovery:{before:acceptedBefore,after:acceptedAfter},
  scope:'Shared graph evaluation plus copying accepted trials to the existing recovery-only progress recorder. The nonlinear equations, next complete variational pass and acceptance thresholds are unchanged.'
};
export function createRationalFiniteTailDN(options){
  const dn=splitModule.createSplitFluxCompactTailDN({...options,stableGraphFactory:buildScaledEndpointGraphs});
  dn.deepLinearBridge=getDeepLinearBridge();
  return dn;
}
