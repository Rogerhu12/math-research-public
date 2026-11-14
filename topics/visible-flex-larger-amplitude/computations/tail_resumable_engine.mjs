// Original-g shared graph engine with accepted-trial recovery checkpoints.
// No solver state, numerical operation, acceptance gate, or iteration history
// is changed. The original progress recorder receives one additional copy of
// an already accepted trial before the next expensive variational evaluation.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {buildRationalStableStageGraphs as buildSharedStableStageGraphs}
  from './closure_linear_stage_graphs.mjs';

const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!topic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC is required');
const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const corePath=path.join(topic,'scripts/78718-tail-tangent-core.mjs');
const splitPath=path.join(topic,'scripts/78718-tail-tangent-split.mjs');
const originalCore=fs.readFileSync(corePath,'utf8'),originalSplit=fs.readFileSync(splitPath,'utf8');
const replacements=[{
  before:'const wholeGraph=buildStableStageGraphs(physical,stages,{modes:M,spacing,linearFar,linearSteps});',
  after:'const wholeGraph=(options.stableGraphFactory??buildStableStageGraphs)(physical,stages,{modes:M,spacing,linearFar,linearSteps});'
},{
  before:"opts.trialDiagnostic?.({...diagnostic,kind:'accepted',trialNorm:test.norm},null);break;",
  after:"opts.trialDiagnostic?.({...diagnostic,kind:'accepted',trialNorm:test.norm},null);\n"+
    "     opts.progress?.({iteration:it+1,norm:test.norm,phase:'accepted-trial-recovery-only',acceptedFromIteration:it,acceptedTrial:k,acceptedStep:lambda},states.map(v=>Array.from(v)));break;"
}];
let core=originalCore;
for(const {before,after} of replacements){
  if(core.split(before).length!==2)throw Error('Pinned source replacement is not unique');
  core=core.replace(before,after);
}
// A direct source check ensures this adapter is just the previously validated
// graph insertion plus a progress callback, not an alternative convergence path.
const recordedOnly="\n     opts.progress?.({iteration:it+1,norm:test.norm,phase:'accepted-trial-recovery-only',acceptedFromIteration:it,acceptedTrial:k,acceptedStep:lambda},states.map(v=>Array.from(v)));";
if(core.replace(recordedOnly,'')!==originalCore.replace(replacements[0].before,replacements[0].after))
  throw Error('Recovery insertion changed code outside the accepted-trial progress callback');
function redirect(source){
  for(const relative of new Set([...source.matchAll(/['"]\.\/([^'"]+)['"]/g)].map(x=>x[1]))){
    const absolute=pathToFileURL(path.join(topic,'scripts',relative)).href;
    source=source.replaceAll("'./"+relative+"'",JSON.stringify(absolute))
      .replaceAll('"./'+relative+'"',JSON.stringify(absolute));
  }
  return source;
}
const coreURL='data:text/javascript;base64,'+Buffer.from(redirect(core)).toString('base64');
const split=originalSplit.replace("'./78718-tail-tangent-core.mjs'",JSON.stringify(coreURL));
if(split===originalSplit)throw Error('Pinned split core import missing');
const splitModule=await import('data:text/javascript;base64,'+Buffer.from(redirect(split)).toString('base64'));
export const storedEngineManifest={
  name:'tail-original-stored-shared-stable-graphs-v1',
  acceptedTrialCheckpoints:'recovery-only-before-full-variational-recheck-v1',
  coreSHA256:sha256(originalCore),splitSHA256:sha256(originalSplit),
  adapterSHA256:sha256(fs.readFileSync(new URL(import.meta.url))),
  graphSHA256:sha256(fs.readFileSync(new URL('./closure_linear_stage_graphs.mjs',import.meta.url))),
  replacements,
  solverChangeBeyondProgressCallback:false,
  scope:'Original stored metric and shared stable graph arithmetic. An already accepted trial is copied to the existing recovery-only progress recorder before the next variational pass. The pass, solve tolerance, positivity guard, line search and success definition remain unchanged.'
};
export function createStoredFiniteTailDN(options){
  if(options.tail.parameters.orientation!==1)
    throw Error('Original stored shared-graph adapter requires orientation +1');
  return splitModule.createSplitFluxCompactTailDN({...options,stableGraphFactory:buildSharedStableStageGraphs});
}
