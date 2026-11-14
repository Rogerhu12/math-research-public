// Experimental, explicitly requested persistence of complete identical-input
// variational stage maps. This file is not used by the exact-raw production plan.
// The original residual assembly, correction, line search, tolerance and audit
// are kept byte-for-byte except for the explicitly listed map wrapper.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const originalURL=new URL('./tail_resumable_engine.mjs',import.meta.url);
const original=fs.readFileSync(originalURL,'utf8');
if(sha(original)!=='1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8')
 throw Error('Pinned resumable engine template differs before stage persistence');
const storeURL=new URL('./strong_exact_stage_flow_store.mjs',import.meta.url).href;
const originalSHA=sha(original),storeSHA=sha(fs.readFileSync(new URL(storeURL)));
const ioKeys=new Set(['traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint']);

// Hash all executable MJS sources in the two explicitly owned source trees.
// The conservative extra hashes can cause misses, but cannot cause a false hit.
function sourceTree(root){
 const out={};
 function visit(directory){
  for(const item of fs.readdirSync(directory,{withFileTypes:true}).sort((a,b)=>a.name.localeCompare(b.name))){
   if(item.isSymbolicLink())throw Error('Exact-stage source snapshot does not follow symbolic links');
   const file=path.join(directory,item.name);
   if(item.isDirectory())visit(file);
   else if(item.isFile()&&item.name.endsWith('.mjs'))out[path.relative(root,file)]=sha(fs.readFileSync(file));
  }
 }
 visit(root);return out;
}
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
const sourceTopic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!sourceRoot||!sourceTopic)throw Error('Explicit pinned source root and topic are required');
const sourceOrigin=JSON.parse(fs.readFileSync(path.join(sourceTopic,'source-origin.json'),'utf8'));
const staticIdentity={schema:'strict-complete-stage-identity-v1',
 pinnedSourceRevision:sourceOrigin.source_revision,pinnedSourceManifest:sourceOrigin.manifest_sha256,
 pinnedMjs:sourceTree(path.resolve(sourceRoot)),
 pinnedTopicMjs:sourceTree(path.resolve(sourceTopic)),
 adapterMjs:sourceTree(path.dirname(new URL(import.meta.url).pathname)),
 templateSHA256:originalSHA,storeSHA256:storeSHA};
for(const [key,env] of [['calibrationLedger','VISIBLE_FLEX_FROZEN_LEDGER_READY'],
 ['storedReferenceReady','VISIBLE_FLEX_FROZEN_STORED_READY']]){
 const file=process.env[env];if(!file)throw Error('Exact stage identity requires '+env);
 staticIdentity[key+'SHA256']=sha(fs.readFileSync(file));
}

const stageEdits=[{
 before:' function cellFlow(n,input,withJac){',
 after:' function uncachedCellFlow(n,input,withJac){'
},{
 before:' const nodeR=Array.from({length:depth+1},',
 after:` const stageStore=options.exactStageCache?createExactStageFlowStore({
  directory:options.exactStageCache.directory,dimension:K,event:options.exactStageCache.event,
  identity:{...options.exactStageCache.identity,
   physicalParameters:Object.fromEntries(Object.entries(physical.parameters).filter(([key])=>!${JSON.stringify([...ioKeys])}.includes(key))),
   globalWarpAlpha:physical.stats.alpha,
   resolved:{modes:M,spacing,physicalDepth,numericalDepth:depth,steps,quadrature,
    linearFar,linearSteps,linearMethod,projectionFloor,fastJacobian,cuspAwareFlow,shootingParts:stages.parts,
    resolvedEngine:'split-linear-flux-v1'},
   stageGeometry:cells.map(c=>({mu:c.mu,portRatio:c.portRatio,rawCell:c.rawCell,rawSegment:c.rawSegment,
    profiles:c.profiles.map(profile=>({integrationBreakpoints:profile.integrationBreakpoints??[]}))})),
   rawNode:stages.rawNode
  }}):null;
 function cellFlow(n,input,withJac){
  return stageStore?stageStore.evaluate(n,input,withJac,()=>uncachedCellFlow(n,input,withJac)):
   uncachedCellFlow(n,input,withJac);
 }
 const nodeR=Array.from({length:depth+1},`
},{
 before:' return {solve,initial,evaluate,cells,graphs,gains,physical,',
 after:' return {exactStagePersistence:stageStore?{identitySHA:stageStore.identitySHA,root:stageStore.root,stats:stageStore.stats}:null,exactStageDiagnostic:stageStore?{uncachedCellFlow,cellFlow}:null,solve,initial,evaluate,cells,graphs,gains,physical,'
}];
const injection=`
const exactStageEdits=${JSON.stringify(stageEdits)};
for(const {before,after} of exactStageEdits){
 if(core.split(before).length!==2)throw Error('Exact-stage map wrapper anchor is not unique');
 core=core.replace(before,after);
}
core=${JSON.stringify('import {createExactStageFlowStore} from '+JSON.stringify(storeURL)+';\n')}+core;
`;
let transformed=original;
const edits=[
 {before:"from './closure_linear_stage_graphs.mjs';",after:'from '+JSON.stringify(new URL('./closure_linear_stage_graphs.mjs',import.meta.url).href)+';'},
 {before:'function redirect(source){',after:injection+'\nfunction redirect(source){'},
 {before:'  replacements,',after:'  replacements,\n  exactStagePersistence:{name:"exact-input-completed-variational-stage-v1",replacements:exactStageEdits,originalTemplateSHA256:'+JSON.stringify(originalSHA)+',storeSHA256:'+JSON.stringify(storeSHA)+',diagnosticCountersReplayed:false,fullResidualAssemblyAndOriginalAcceptanceUnchanged:true},'}
];
for(const {before,after} of edits){
 if(transformed.split(before).length!==2)throw Error('Resumable stage adapter anchor is not unique');
 transformed=transformed.replace(before,after);
}
// Relative imports still resolve to the actual adapter directory; its recorded
// adapter hash identifies this wrapper, and the old template hash is explicit.
transformed=transformed.replaceAll('import.meta.url',JSON.stringify(import.meta.url));
const virtual=await import('data:text/javascript;base64,'+Buffer.from(transformed).toString('base64'));
export const storedEngineManifest={...virtual.storedEngineManifest,
 exactStageHost:{templateSHA256:originalSHA,transformedSHA256:sha(transformed),
  sourceTransform:edits,sourceIdentity:staticIdentity,
  status:'experimental-requires-real-stage-and-complete-evaluation-comparison'}};

export function createStoredFiniteTailDN(options){
 if(!options.exactStageCache?.directory)
  throw Error('An explicit exactStageCache directory is required; this adapter is never enabled implicitly');
 if(typeof options.tail?.stats?.alpha!=='number'||!Number.isFinite(options.tail.stats.alpha))
  throw Error('Exact-stage identity requires the actual frozen global warp alpha');
 const supplied=options.exactStageCache;
 const dn=virtual.createStoredFiniteTailDN({...options,exactStageCache:{...supplied,
  identity:{staticIdentity,callerIdentity:supplied.identity??null}}});
 if(dn.tail.parameters.rhsEvaluation!=='split-linear-flux-v1')
  throw Error('The actual final stage engine is not the pinned split-flux factory');
 return dn;
}
