// Explicit complete-input stage persistence around the retained exact-raw worker.
// All original nonlinear residual, line search, full-H Jacobian and audit paths
// remain. The diagnostic request compares the full actual evaluate only and
// never returns a converged DN response.
import fs from 'node:fs';
import crypto from 'node:crypto';

const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
const templateURL=new URL('./strong_exact_raw_tail_worker.mjs',import.meta.url);
const original=fs.readFileSync(templateURL,'utf8');
const expected='ec69703a4b0786313c2506aae5f82ec8da39330876d15519225e2d4b7f7d2cc8';
if(sha(original)!==expected)throw Error('The original exact-raw worker changed');

const lowerEdits=[{
 before:' const prior=record.response?.checkpoint??record.seam?.tail_checkpoint??record.checkpoint??record;',
 after:' const prior=restoreExactInitialSeed(record.response?.checkpoint??record.seam?.tail_checkpoint??record.checkpoint??record,dn);'
},{
 before:"console.log(JSON.stringify({event:'ready',exactRawWarmAdapter:exactRawWarmAdapterManifest,",
 after:"console.log(JSON.stringify({event:'ready',exactStageCacheAdapter:stageCacheWorkerManifest,exactStageStorage:dn.tail.exactStagePersistence,exactRawWarmAdapter:exactRawWarmAdapterManifest,"
},{
 before:'const sol=dn.solve(req.height,',
 after:`const exactInitialSeed=saveExactInitialSeed({dn,height:req.height,states:initial,call,
    prefix:process.env.VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX,sourceIdentity:{...stageCacheWorkerManifest,
     engineSHA256:stageCacheWorkerManifest.stageEngineSHA256,helperSHA256:stageCacheWorkerManifest.seedHelperSHA256}});
  trace({event:'exact_initial_stage_seed_saved',call,...exactInitialSeed});
  if(req.exactStageDiagnostic===true){
   const check=compareCompleteStageEvaluation(dn,initial,req.height,row=>trace({...row,call}));
   console.log(JSON.stringify({exactStageDiagnostic:check,exactInitialSeed,
    prefixAccepted:false,tailConverged:false}));continue;
  }
  const sol=dn.solve(req.height,`
}];
const extraTemplateEdits=[{
 before:"const engineURL=new URL('./tail_resumable_engine.mjs',import.meta.url).href;",
 after:"const engineURL=new URL('./strong_exact_stage_engine.mjs',import.meta.url).href;"
},{
 before:"const rawWarmURL=new URL('./strong_exact_raw_tail_warm.mjs',import.meta.url).href;",
 after:`const rawWarmURL=new URL('./strong_exact_raw_tail_warm.mjs',import.meta.url).href;
const stageSeedURL=new URL('./strong_exact_stage_seed.mjs',import.meta.url).href;
const stageCheckURL=new URL('./strong_exact_stage_evaluation_check.mjs',import.meta.url).href;
const stageCacheWorkerManifest={name:'exact-input-persistent-actual-stage-worker-v1',
 workerSHA256:sha256(fs.readFileSync(new URL(import.meta.url))),
 exactRawWorkerSHA256:${JSON.stringify(expected)},
 stageEngineSHA256:sha256(fs.readFileSync(new URL(engineURL))),
 seedHelperSHA256:sha256(fs.readFileSync(new URL(stageSeedURL))),
 evaluationCheckSHA256:sha256(fs.readFileSync(new URL(stageCheckURL))),
 transformedExactRawHostSHA256:process.env.STRONG_EXACT_STAGE_HOST_SHA,
 sourceTransforms:JSON.parse(process.env.STRONG_EXACT_STAGE_SOURCE_TRANSFORMS),
 actualVariationalBackend:'fourier-root-and-product-moments-v1',
 scope:'Exact binary stage persistence and unaccepted initial-seed retention only. Every original full nonlinear solve, Jacobian, positivity, line search and final audit gate remains.'};`
},{
 before:'const dn=createSourceCompactTailDN(options),sourceSolve=dn.solve;',
 after:`if(backend!=='fourier-root')throw Error('The explicitly verified cache requires the actual Fourier-root backend');
  if(!process.env.VISIBLE_FLEX_EXACT_STAGE_CACHE||!process.env.VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX)
   throw Error('Exact-stage storage and initial-seed paths must be explicit');
  const dn=createSourceCompactTailDN({...options,exactStageCache:{
   directory:process.env.VISIBLE_FLEX_EXACT_STAGE_CACHE,
   identity:{worker:stageCacheWorkerManifest,actualVariationalBackend:backend,predictor,
    splitConstructorFollowedByOriginalFourierRootObjectAssign:true},
   event:row=>trace({event:'exact_stage_cache',...row})}}),sourceSolve=dn.solve;`
},{
 before:'const importRedirects=[];',
 after:'for(const {before,after} of '+JSON.stringify(lowerEdits)+')replaceOnce(before,after);\nconst importRedirects=[];'
},{
 before:'source=`import {preserveExactRawWarm,samePhysicalHeight,rawWarmGarbageCollection} from ${JSON.stringify(rawWarmURL)};\\n`+',
 after:'source=`import {saveExactInitialSeed,restoreExactInitialSeed} from ${JSON.stringify(stageSeedURL)};\\n`+\n'+
       '  `import {compareCompleteStageEvaluation} from ${JSON.stringify(stageCheckURL)};\\n`+\n'+
       '  `const stageCacheWorkerManifest=${JSON.stringify(stageCacheWorkerManifest)};\\n`+\n'+
       '  `import {preserveExactRawWarm,samePhysicalHeight,rawWarmGarbageCollection} from ${JSON.stringify(rawWarmURL)};\\n`+'
},{
 before:'  exactRawWarmAdapter:rawWarmAdapterManifest,',
 after:'  exactStageCacheAdapter:stageCacheWorkerManifest,\n  exactRawWarmAdapter:rawWarmAdapterManifest,'
}];
const hostEdits=[{
 before:'for(const {before,after} of templateEdits){',
 after:'templateEdits.push(...'+JSON.stringify(extraTemplateEdits)+');\nfor(const {before,after} of templateEdits){'
},{
 before:"const templateURL=new URL('./tail_frozen_worker.mjs',import.meta.url);",
 after:'const templateURL=new URL('+JSON.stringify(new URL('./tail_frozen_worker.mjs',import.meta.url).href)+');'
},{
 before:"source=source.replaceAll('import.meta.url',JSON.stringify(import.meta.url));",
 after:"source=source.replaceAll('import.meta.url',JSON.stringify("+JSON.stringify(import.meta.url)+'));'
}];
let transformed=original;
for(const {before,after} of hostEdits){
 if(transformed.split(before).length!==2)throw Error('Exact-stage host source anchor is not unique');
 transformed=transformed.replace(before,after);
}
process.env.STRONG_EXACT_STAGE_HOST_SHA=sha(transformed);
process.env.STRONG_EXACT_STAGE_SOURCE_TRANSFORMS=JSON.stringify({originalExactRawWorkerSHA256:expected,
 hostEdits,extraTemplateEdits,lowerEdits});
try{await import('data:text/javascript;base64,'+Buffer.from(transformed).toString('base64'));}
catch(error){
 console.error(String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<exact-stage-worker>'));
 process.exitCode=1;
}
