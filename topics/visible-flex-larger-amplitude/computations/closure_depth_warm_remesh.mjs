// Physical-depth extension is an initial guess only. The pinned geometric
// Q/L embedding requires equal depths, so use the pinned older remesher only
// when angular modes, quadrature and the existing shooting grid are unchanged.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const sourceTopic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!sourceTopic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC is required');
const sourcePath=path.join(sourceTopic,'scripts/950f-tail-warm-remesh.mjs');
const sourceSHA256=crypto.createHash('sha256').update(fs.readFileSync(sourcePath)).digest('hex');
const {remeshCheckpoint}=await import(pathToFileURL(sourcePath).href);

export function depthWarmRemesh(prior,dn,engineFactory){
  const old=prior.parameters,now=dn.tail.parameters;
  const oldDepth=old.physicalDepth??old.depth,depth=now.physicalDepth??now.depth;
  if(!(Number.isInteger(oldDepth)&&Number.isInteger(depth)&&depth>oldDepth))
    throw Error('Depth-only warm extension requires a strict physical-depth increase');
  for(const key of ['modes','spacing','quadrature','shootingParts','orientation'])
    if(old[key]!==now[key])throw Error('Depth-only warm extension cannot also change '+key);
  if(!(old.shootingParts>0))throw Error('Depth-only adapter requires a saved subdivided state');
  if(!prior.rawNode||prior.rawNode.length!==oldDepth+1)
    throw Error('Depth-only adapter requires the old physical node map');
  for(let n=0;n<=oldDepth;n++)
    if(prior.rawNode[n]!==dn.tail.rawNode[n])throw Error('Depth extension changed an existing physical node');
  const states=remeshCheckpoint(prior,dn,engineFactory);
  let maxExistingStateDifference=0;
  if(prior.states.length!==dn.tail.rawNode[oldDepth]+1)
    throw Error('Old warm state length does not agree with its physical depth');
  for(let i=0;i<prior.states.length;i++)for(let j=0;j<prior.states[i].length;j++)
    maxExistingStateDifference=Math.max(maxExistingStateDifference,Math.abs(states[i][j]-prior.states[i][j]));
  if(maxExistingStateDifference!==0)
    throw Error('Depth-only warm extension changed an existing shooting state');
  return {states,diagnostics:{method:'pinned-depth-only-linear-initial-guess-v1',
    sourceSHA256,sourceModes:old.modes,targetModes:now.modes,
    sourceQuadrature:old.quadrature,targetQuadrature:now.quadrature,
    sourcePhysicalDepth:oldDepth,physicalDepth:depth,shootingParts:now.shootingParts,
    sourceNodeCount:prior.states.length,nodeCount:states.length,
    appendedNodeCount:states.length-prior.states.length,maxExistingStateDifference,
    scope:'All saved nodes remain exactly unchanged. Appended linear-graph nodes are only an initial guess; the full nonlinear residual is still solved.'}};
}
