// Genuine same-mode warm-state conversion to finer multiple-shooting nodes.
// Uses the immutable source remeshCheckpoint to integrate inserted nodes.
// All old nodes must be preserved exactly; no new node is asserted solved.
// This prepares a valid-shape input for the source geometricWarmRemesh,
// whose own entry point intentionally requires identical shootingParts.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const [sourceTopic,configFile,priorFile,outputFile]=process.argv.slice(2);
if(!sourceTopic || !configFile || !priorFile || !outputFile || !outputFile.endsWith('.json.gz'))
  throw Error('Usage: node numerical-tail-subdivide-warm.mjs SOURCE_TOPIC NEW_CONFIG.json PRIOR.json.gz OUTPUT.json.gz');
if(fs.existsSync(outputFile))throw Error('Output already exists');
const started=Date.now(),sourceRoot=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const url=name=>pathToFileURL(path.join(sourceTopic,'scripts',name));
const {createRecalibrationFactory}=await import(url('closing_weighted_tail.mjs'));
const {createSplitFluxCompactTailDN}=await import(url('78718-tail-tangent-split.mjs'));
const {createFourierRootSplitFluxEngine}=await import(url('78718-tail-fourier-root-split-engine.mjs'));
const {remeshCheckpoint}=await import(url('950f-tail-warm-remesh.mjs'));
const config=JSON.parse(fs.readFileSync(configFile,'utf8')),bytes=fs.readFileSync(priorFile),
  record=JSON.parse(zlib.gunzipSync(bytes)),prior=record.response?.checkpoint??record.checkpoint??record,
  physical=createRecalibrationFactory(config).assemble(),
  dn=createSplitFluxCompactTailDN({...config,tail:physical}),
  old=prior.parameters,now=dn.tail.parameters;
if(!old || !prior.states || !prior.cutHeight)throw Error('Complete warm checkpoint required');
// Only numerical subdivision, its audit grid, iteration cap and recording
// paths may differ. depth is the resulting numerical stage count;
// physicalDepth, modes, quadrature, tolerances and every metric field stay fixed.
const allowed=new Set(['shootingParts','steps','depth','auditSteps','maxIterations',
  'traceFile','trialDiagnosticFile','iterationCheckpointFile','initialCheckpoint']);
const nonphysicalChanges={};
for(const key of new Set([...Object.keys(old),...Object.keys(now)])) {
  if(allowed.has(key)) {
    if(JSON.stringify(old[key]??null)!==JSON.stringify(now[key]??null))
      nonphysicalChanges[key]={old:old[key]??null,new:now[key]??null};
    continue;
  }
  if(JSON.stringify(old[key]??null)!==JSON.stringify(now[key]??null))
    throw Error('Warm subdivision changes an unauthorized parameter: '+key);
}
const factor=now.shootingParts/old.shootingParts;
if(!(Number.isInteger(factor) && factor>1))throw Error('Integral strict shooting refinement required');
if(now.steps*now.shootingParts!==old.steps*old.shootingParts)
  throw Error('This diagnostic requires identical total RK steps per original profile');
if(old.modes!==now.modes || old.quadrature!==now.quadrature ||
   old.physicalDepth!==now.physicalDepth)
  throw Error('Angular discretization and physical depth must remain fixed');
const engineFactory=options=>createFourierRootSplitFluxEngine({...options,cuspAwareFlow:false});
const states=remeshCheckpoint(prior,dn,engineFactory);
let maxCommonChange=0;
if(states.length!==(prior.states.length-1)*factor+1)throw Error('Unexpected refined node count');
for(let n=0;n<prior.states.length;n++)for(let j=0;j<2*now.modes;j++)
  maxCommonChange=Math.max(maxCommonChange,Math.abs(states[factor*n][j]-prior.states[n][j]));
if(maxCommonChange!==0)throw Error('Original shooting nodes were not preserved exactly');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const diagnostics={
  scope:'Warm guess only. Every original node is copied exactly; inserted nodes are computed by the same finite nonlinear RK field on the original grid. A new actual shooting solve and audit are still required.',
  source_revision:JSON.parse(fs.readFileSync(path.join(sourceTopic,'source-origin.json'))).source_revision,
  source_checkpoint:priorFile,source_checkpoint_sha256:hash(bytes),
  source_checkpoint_converged:record.response?.converged===true,
  source_checkpoint_status:record.status??record.response?.failed??'not separately declared',
  original_parts:old.shootingParts,refined_parts:now.shootingParts,
  original_steps:old.steps,refined_steps:now.steps,
  original_node_count:prior.states.length,refined_node_count:states.length,
  total_steps_per_original_profile:now.steps*now.shootingParts,
  nonphysical_parameter_changes:nonphysicalChanges,
  common_nodes_max_state_change:maxCommonChange,
  physical_metric_unchanged:true,physical_cut_height_unchanged:true,
  source_sha256:{
    'numerical-tail-subdivide-warm.mjs':hash(fs.readFileSync(new URL(import.meta.url))),
    '950f-tail-warm-remesh.mjs':hash(fs.readFileSync(path.join(sourceTopic,'scripts/950f-tail-warm-remesh.mjs'))),
    '950f-tail-subdivision.mjs':hash(fs.readFileSync(path.join(sourceTopic,'scripts/950f-tail-subdivision.mjs'))),
    new_config:hash(fs.readFileSync(configFile))
  },seconds:(Date.now()-started)/1000
};
const checkpoint={parameters:now,states,rawNode:dn.tail.rawNode,
  rawStates:dn.tail.rawNode.map(n=>states[n]),cutHeight:prior.cutHeight,
  scope:diagnostics.scope};
const output=zlib.gzipSync(JSON.stringify({status:'warm-remesh-only',checkpoint,diagnostics})+'\n');
if(output.length>=5_000_000)throw Error('Warm checkpoint exceeds repository size limit');
fs.writeFileSync(outputFile,output,{flag:'wx'});
console.log(JSON.stringify({output:outputFile,diagnostics}));
