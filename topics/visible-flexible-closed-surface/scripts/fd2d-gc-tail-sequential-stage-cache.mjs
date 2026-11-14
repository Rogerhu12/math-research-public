// A serial adapter for the already used exact 32-stage output cache.
// It changes retention only. A cache hit never declares a solved DN response.
import {createStageMapCache} from './fd2d-stage-map-cache.mjs';

const runtimeKeys=new Set(['traceFile','iterationCheckpointFile','trialDiagnosticFile',
  'trialStatePrefix','initialCheckpoint','stageCacheRoot','pointCachePerEntry']);

export function createSequentialStageCache({cacheRoot,entryURL,tail,backend,
  dependencyBlobs,diagnostic=()=>{}}){
  const {modes:M,steps}=tail.parameters,K=2*M,count=tail.cells.length;
  const parameters=Object.fromEntries(Object.entries(tail.parameters)
    .filter(([key])=>!runtimeKeys.has(key)));
  // These are exact constructor inputs and actual stage coordinates, not a
  // sampled approximation replacing any physical profile. The dependency
  // blobs bind the verified CJS source as well as the MJS source closure.
  const definition={schema:'fd2d-exact-stage-function-definition-v1',parameters,
    physicalStats:tail.physical.stats,sourceParameters:tail.physical.source.parameters,
    stages:tail.cells.map(c=>({mu:c.mu,portRatio:c.portRatio,rawCell:c.rawCell,
      rawSegment:c.rawSegment,rawLeft:c.rawLeft,rawRight:c.rawRight,
      breakpoints:c.profiles.map(p=>Array.from(p.integrationBreakpoints??[]))}))};
  const cache=createStageMapCache({cacheRoot,entryURL,tables:definition,
    options:{backend,dependencyBlobs},stepsPerSegment:steps,count,K,diagnostic});
  if(!cache)return null;
  return {metadata:cache.metadata,begin(states,withJac){
    if(states.length!==count+1)throw Error('Cached evaluation node count differs');
    const input=new Float64Array(count*K),status=new Int32Array(new SharedArrayBuffer(4*count)),
      output=new Float64Array(count*K),scalar=new Float64Array(3*count),
      jacobian=withJac?new Float64Array(count*K*K):null;
    for(let n=0;n<count;n++)input.set(states[n+1],n*K);
    const saved=cache.begin(input,withJac,{status,output,jacobian,scalar});
    return {
      has:n=>Atomics.load(status,n)===1,
      get(n){return {out:output.slice(n*K,(n+1)*K),
        J:withJac?jacobian.slice(n*K*K,(n+1)*K*K):null,
        meanHeight:scalar[3*n],minA:withJac?scalar[3*n+1]:undefined,
        minD:withJac?scalar[3*n+2]:undefined};},
      set(n,flow){
        output.set(flow.out,n*K);if(withJac)jacobian.set(flow.J,n*K*K);
        scalar[3*n]=flow.meanHeight;scalar[3*n+1]=flow.minA;scalar[3*n+2]=flow.minD;
        Atomics.store(status,n,1);
        if((n+1)%32===0||n+1===count)saved.flush();
      },
      finish:()=>saved.finish(),flush:()=>saved.flush(),
    };
  }};
}
