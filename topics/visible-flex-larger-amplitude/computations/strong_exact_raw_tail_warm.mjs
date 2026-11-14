// Exact same-discretization raw shooting warm restoration only.
// No residual, Newton, full variational pass or final audit is bypassed.
import crypto from 'node:crypto';

const IO=new Set(['traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint']);
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
function exact(a,b){
  if(typeof a==='number'||typeof b==='number')return typeof a==='number'&&typeof b==='number'&&Object.is(a,b);
  if(a===null||b===null||typeof a!=='object'||typeof b!=='object')return a===b;
  if(Array.isArray(a)!==Array.isArray(b))return false;
  const ka=Object.keys(a).sort(),kb=Object.keys(b).sort();
  return ka.length===kb.length&&ka.every((key,j)=>key===kb[j]&&exact(a[key],b[key]));
}
function numericBytes(rows){
  const values=rows.flat(),buffer=Buffer.allocUnsafe(values.length*8);
  values.forEach((value,j)=>buffer.writeDoubleLE(value,j*8));return buffer;
}
export function samePhysicalHeight(a,b){
  return Array.isArray(a)&&Array.isArray(b)&&a.length===b.length&&
    a.every((v,j)=>Number.isFinite(v)&&Object.is(v,b[j]));
}
export function preserveExactRawWarm(prior,dn){
  const old=prior?.parameters,now=dn?.tail?.parameters;
  if(!old||!now)throw Error('Exact raw warm requires both complete parameter objects');
  const keys=[...new Set([...Object.keys(old),...Object.keys(now)])].filter(k=>!IO.has(k)).sort();
  for(const key of keys)if(!exact(old[key],now[key]))
    throw Error('Exact raw warm changed a physical/discretization parameter: '+key);
  const M=now.modes,K=2*M,depth=now.depth;
  if(!Number.isInteger(M)||M<1||!Number.isInteger(depth)||depth!==dn.tail.cells.length)
    throw Error('Exact raw warm target grid dimensions are inconsistent');
  const rows=prior.states,rawNode=Array.from(dn.tail.rawNode);
  if(!Array.isArray(rows)||rows.length!==depth+1||rows.some(row=>
      !Array.isArray(row)||row.length!==K||row.some(v=>!Number.isFinite(v))))
    throw Error('Exact raw warm lacks the complete finite state array');
  if(!exact(prior.rawNode,rawNode)||!Array.isArray(prior.rawStates)||
      prior.rawStates.length!==rawNode.length||rawNode.some((n,j)=>
      !Number.isInteger(n)||n<0||n>depth||!exact(prior.rawStates[j],rows[n])))
    throw Error('Exact raw warm raw-node state copies do not match');
  if(!samePhysicalHeight(prior.cutHeight,prior.cutHeight)||prior.cutHeight.length!==M)
    throw Error('Exact raw warm requires all finite physical H coefficients');
  // Copy every scalar without any Q/L conversion, interpolation or scaling.
  // The original solver will copy these arrays into its own Float64 storage.
  const states=rows.map(row=>row.slice());
  const stateSHA=sha(numericBytes(states));
  if(stateSHA!==sha(numericBytes(rows)))throw Error('Exact raw state copy changed bytes');
  return {states,diagnostics:{
    method:'same-discretization-exact-raw-shooting-warm-v1',
    scope:'Warm guess only. The original complete nonlinear residual, full variational pass, Newton, positivity, line search and audit determine acceptance.',
    modes:M,nodeCount:states.length,shapeDimension:K,physicalDepth:now.physicalDepth??now.depth,
    shootingParts:now.shootingParts,quadrature:now.quadrature,steps:now.steps,
    allNonIOParametersExactlyEqual:true,checkedParameterKeys:keys,
    rawNodeExactlyEqual:true,rawStatesExactlyEqual:true,
    fullStateFloat64LESHA256:stateSHA,
    noQ_LRemesh:true,noAmplitudeRescaleAtLoad:true,priorNormNotUsedForAcceptance:true,
    numericalSolutionAccepted:false}};
}
export function rawWarmGarbageCollection(stage,trace){
  const before=process.memoryUsage();
  if(typeof globalThis.gc!=='function')throw Error('Exact raw storage mode requires explicit GC');
  globalThis.gc();
  trace({event:'exact_raw_storage_gc',stage,before,after:process.memoryUsage(),
    scope:'Only unreachable storage is collected; live mathematical state is retained.'});
}
