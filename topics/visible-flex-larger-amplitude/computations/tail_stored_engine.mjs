// Opt-in evaluation of the original stable graphs on a shared physical grid.
// Nonlinear equations and finite-tail acceptance remain the pinned source.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
// This helper's legacy export name does not construct a rational metric.
import {buildRationalStableStageGraphs as buildSharedStableStageGraphs}
  from './closure_linear_stage_graphs.mjs';

const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!topic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC is required');
const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const corePath=path.join(topic,'scripts/78718-tail-tangent-core.mjs');
const splitPath=path.join(topic,'scripts/78718-tail-tangent-split.mjs');
const originalCore=fs.readFileSync(corePath,'utf8'),originalSplit=fs.readFileSync(splitPath,'utf8');
const before='const wholeGraph=buildStableStageGraphs(physical,stages,{modes:M,spacing,linearFar,linearSteps});';
const after='const wholeGraph=(options.stableGraphFactory??buildStableStageGraphs)(physical,stages,{modes:M,spacing,linearFar,linearSteps});';
if(originalCore.split(before).length!==2)throw Error('Pinned core graph insertion is not unique');
function redirect(source){
  for(const relative of new Set([...source.matchAll(/['"]\.\/([^'"]+)['"]/g)].map(x=>x[1]))){
    const absolute=pathToFileURL(path.join(topic,'scripts',relative)).href;
    source=source.replaceAll("'./"+relative+"'",JSON.stringify(absolute))
      .replaceAll('"./'+relative+'"',JSON.stringify(absolute));
  }
  return source;
}
const coreURL='data:text/javascript;base64,'+Buffer.from(redirect(originalCore.replace(before,after))).toString('base64');
const split=originalSplit.replace("'./78718-tail-tangent-core.mjs'",JSON.stringify(coreURL));
if(split===originalSplit)throw Error('Pinned split core import missing');
const splitModule=await import('data:text/javascript;base64,'+Buffer.from(redirect(split)).toString('base64'));
export const storedEngineManifest={
  name:'tail-original-stored-shared-stable-graphs-v1',
  coreSHA256:sha256(originalCore),splitSHA256:sha256(originalSplit),
  adapterSHA256:sha256(fs.readFileSync(new URL(import.meta.url))),
  graphSHA256:sha256(fs.readFileSync(new URL('./closure_linear_stage_graphs.mjs',import.meta.url))),
  replacement:{before,after},
  scope:'Shared evaluation of identical physical grid coefficients, original per-mode RK4 operation order and cusp splits. The nonlinear finite DN and acceptance thresholds are unchanged. The caller supplies the original stored metric.'
};
export function createStoredFiniteTailDN(options){
  if(options.tail.parameters.orientation!==1)
    throw Error('Original stored shared-graph adapter requires orientation +1');
  return splitModule.createSplitFluxCompactTailDN({...options,stableGraphFactory:buildSharedStableStageGraphs});
}
