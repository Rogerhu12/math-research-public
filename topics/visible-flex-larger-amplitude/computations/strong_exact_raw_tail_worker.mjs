// Strict same-discretization raw warm adapter over the unchanged frozen worker.
// The source transform and all mathematical source hashes are retained in ready.
import fs from 'node:fs';
import crypto from 'node:crypto';
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
const templateURL=new URL('./tail_frozen_worker.mjs',import.meta.url);
const original=fs.readFileSync(templateURL,'utf8');
const expected="3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054";
if(sha(original)!==expected)throw Error('Frozen worker template changed before exact-raw transformation');
let source=original;
const templateEdits=[
  {
    "before": "const original=fs.readFileSync(workerPath,'utf8');",
    "after": "const rawWarmURL=new URL('./strong_exact_raw_tail_warm.mjs',import.meta.url).href;\nconst rawWarmAdapterManifest={name:'same-discretization-exact-raw-shooting-warm-v1',templateSHA256:\"3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054\",workerAdapterSHA256:sha256(fs.readFileSync(new URL(import.meta.url))),warmHelperSHA256:sha256(fs.readFileSync(new URL(rawWarmURL))),transformedTemplateSHA256:process.env.STRONG_EXACT_RAW_WORKER_TRANSFORM_SHA,scope:'Only same-discretization raw warm storage and explicit GC. The original full residual, variational pass, Newton, line search, positivity and full audit remain unchanged.'};\nconst original=fs.readFileSync(workerPath,'utf8');"
  },
  {
    "before": "replaceOnce(\n  \"import {createSplitFluxCompactTailDN as createCompactTailDN} from './78718-tail-tangent-split.mjs';\",",
    "after": "for(const {before,after} of [{\"before\": \"let last=null,call=0,progressStates=null,progressRow=null,currentHeight=null,warmEmbeddingDiagnostics=null;\", \"after\": \"let exactRawPending=null;\\nlet last=null,call=0,progressStates=null,progressRow=null,currentHeight=null,warmEmbeddingDiagnostics=null;\"}, {\"before\": \"if(cfg.initialCheckpoint){\\n\", \"after\": \"rawWarmGarbageCollection('before-checkpoint-warm',trace);\\nif(cfg.initialCheckpoint){\\n\"}, {\"before\": \" const embedded=geometricWarmRemesh(prior,dn,createFastSplitFluxMomentumTailEngine);\\n const states=embedded.states;warmEmbeddingDiagnostics=embedded.diagnostics;\\n trace({event:'geometric_warm_embedding',source:cfg.initialCheckpoint,...warmEmbeddingDiagnostics});\", \"after\": \" const embedded=preserveExactRawWarm(prior,dn);\\n const states=embedded.states;warmEmbeddingDiagnostics=embedded.diagnostics;\\n exactRawPending={height:prior.cutHeight.slice(),states};\\n trace({event:'exact_raw_warm_loaded',source:cfg.initialCheckpoint,checkpointSHA256:createHash('sha256').update(raw).digest('hex'),...warmEmbeddingDiagnostics});\"}, {\"before\": \"console.log(JSON.stringify({event:'ready',\", \"after\": \"rawWarmGarbageCollection('before-ready',trace);\\nconsole.log(JSON.stringify({event:'ready',exactRawWarmAdapter:exactRawWarmAdapterManifest,\"}, {\"before\": \"  let initial,predicted=false;\\n  if(tangentPredictor){\", \"after\": \"  rawWarmGarbageCollection('before-request-warm',trace);\\n  let initial,predicted=false;\\n  if(exactRawPending&&samePhysicalHeight(req.height,exactRawPending.height)){\\n   initial=exactRawPending.states.map(row=>Float64Array.from(row));predicted=true;\\n   trace({event:'exact_raw_same_H_initial',call,complete_H_bitwise_equal:true,all_original_raw_values_preserved:true,warm_Q_L_remesh_bypassed:true,warm_ratio_one_rescale_bypassed:true,warm_only_boundary_correction_bypassed:true,full_original_residual_Newton_Jacobian_audit_required:true});\\n  }\\n  exactRawPending=null;\\n  if(!predicted&&tangentPredictor){\"}])replaceOnce(before,after);\nreplaceOnce(\n  \"import {createSplitFluxCompactTailDN as createCompactTailDN} from './78718-tail-tangent-split.mjs';\","
  },
  {
    "before": "source=`import {actualSlopeJacobian,replaceFirstSlopeRows} from ${JSON.stringify(slopeURL)};\\n`+",
    "after": "source=`import {preserveExactRawWarm,samePhysicalHeight,rawWarmGarbageCollection} from ${JSON.stringify(rawWarmURL)};\\n`+\n  `const exactRawWarmAdapterManifest=${JSON.stringify(rawWarmAdapterManifest)};\\n`+\n  `import {actualSlopeJacobian,replaceFirstSlopeRows} from ${JSON.stringify(slopeURL)};\\n`+"
  },
  {
    "before": "  sourceRevision:JSON.parse",
    "after": "  exactRawWarmAdapter:rawWarmAdapterManifest,\n  sourceRevision:JSON.parse"
  }
];
for(const {before,after} of templateEdits){
 if(source.split(before).length!==2)throw Error('Exact-raw worker source anchor is not unique');
 source=source.replace(before,after);
}
// The virtual module resolves relative adapters and records this actual wrapper.
source=source.replaceAll('import.meta.url',JSON.stringify(import.meta.url));
process.env.STRONG_EXACT_RAW_WORKER_TRANSFORM_SHA=sha(source);
try{await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));}
catch(error){
 console.error(String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<exact-raw-frozen-worker>'));
 process.exitCode=1;
}
