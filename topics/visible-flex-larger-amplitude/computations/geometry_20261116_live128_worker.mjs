// R493 live128 protocol for the unchanged stored finite original geometry.
// Original warm choices remain. Every requested H uses its actual same-call128
// result, and no old64 endpoint wrapper overwrites those returned component rows.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';

if(process.env.GITHUB_ACTIONS!=='true'||
 (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('R493 live worker belongs only to public repository Actions');
const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!topic)throw Error('VISIBLE_FLEX_SOURCE_TOPIC is required');
const spec=JSON.parse(fs.readFileSync(process.env.VISIBLE_FLEX_LIVE128_SPEC,'utf8'));
const workerPath=path.join(topic,'scripts/78718-prefix-tail-tangent-fourier-worker.mjs');
const geometryURL=new URL('./tail_frozen_geometry.mjs',import.meta.url).href;
const engineURL=new URL('./tail_resumable_engine.mjs',import.meta.url).href;
const liveURL=new URL('./geometry_20261116_live128_current_call.mjs',import.meta.url).href;
const sha256=x=>crypto.createHash('sha256').update(x).digest('hex');
const original=fs.readFileSync(workerPath,'utf8');
if(sha256(original)!=='36cf8235d42dfdb2477e6e709dfb721633ac39259b45aeadff2e13491e64864a')
 throw Error('The actual original complete protocol worker source differs');
if(sha256(fs.readFileSync(new URL(engineURL)))!=='1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8')
 throw Error('The unchanged stored/shared original engine differs');
let source=original;
const replacements=[];
function replaceOnce(before,after){
 const count=source.split(before).length-1;
 if(count!==1)throw Error('Unique original live protocol source anchor required, count='+count);
 source=source.replace(before,after);replacements.push({before,after,count});
}
replaceOnce("import {createSplitFluxCompactTailDN as createCompactTailDN} from './78718-tail-tangent-split.mjs';",
 'import {createStoredFiniteTailDN as createCompactTailDN,storedEngineManifest} from '+JSON.stringify(engineURL)+';');
replaceOnce('const physical=createRecalibrationFactory(cfg).assemble();',
 'const storedGeometry=await createStoredPhysical(cfg),physical=storedGeometry.physical;');
replaceOnce('let tangentPredictor=null;',
 'let tangentPredictor=null;\n'+
 'const live128=createLive128Session(dn,zero,cfg,{\n'+
 ' storedMetricAdapter:storedGeometry.manifest,stableGraphAdapter:storedEngineManifest,\n'+
 ' actual_original64_capture_backend:backendLabel,\n'+
 ' actual_live_worker:live128AdapterManifest},splitIntegrationInterval);');
const seedStart='if(cfg.initialCheckpoint){',seedEnd='\nconst D=[];';
if(source.split(seedStart).length!==2||source.split(seedEnd).length!==2)
 throw Error('Unique original optional imported-checkpoint block required');
const seedBlock=source.slice(source.indexOf(seedStart),source.indexOf(seedEnd));
replaceOnce(seedBlock,
 "if(cfg.initialCheckpoint)throw Error('The live128 seed has its own exact raw binding, not a remeshed initialCheckpoint');\n"+
 'last=live128.initialSeed();\n'+
 "warmEmbeddingDiagnostics={kind:'actual91-complete-failed-state-initial-guess',\n"+
 ' source:last.source,completed_parent:false,old_J_or_response_cache_imported:false,\n'+
 ' original_warm_amplitude_and_boundary_choices_follow:true};\n'+
 "trace({event:'live128_initial_guess',...warmEmbeddingDiagnostics});");
const solveLine=original.split('\n').filter(x=>x.startsWith('  const sol=dn.solve(req.height,'))[0];
if(!solveLine)throw Error('Original solve request line is unavailable');
const suffix=solveLine.slice('  const sol=dn.solve(req.height,'.length,-2);
if(!suffix.startsWith('{')||!suffix.endsWith('}'))throw Error('Original request options remain a complete literal source object');
replaceOnce(solveLine,
 '  const liveResponse=await live128.solve(req.height,'+suffix+',call,{'+
 "original_tangent_prediction_selected:predicted,original_initial_argument_supplied:!!initial,"+
 "cold_initialization_selected:!initial,first_seed_available:call===1});\n"+
 '  const sol=liveResponse.sol;');
replaceOnce("maxChartCondition:Math.max(...sol.history.map(x=>x.chartCondition??0))",
 "maxChartCondition:null,original64_chart_condition_not_formed:true,actual_response_arithmetic:sol.arithmetic_schema");
const responseLine=original.split('\n').filter(x=>x.startsWith('  console.log(JSON.stringify({converged:sol.converged,residual:sol.normalizedResidual'))[0];
if(!responseLine)throw Error('Original response protocol writer is unavailable');
replaceOnce(responseLine,
 '  await new Promise((resolve,reject)=>process.stdout.write(liveResponse.responseText,error=>error?reject(error):resolve()));\n'+
 '  liveResponse.markReturned();');
replaceOnce("tailJacobian:backendLabel,tailPredictor:predictorLabel,amplitudeWarm:'physical-Q-L-amplitude-v1'",
 "tailJacobian:'binary128-live-recorded-factor-simd-mixed338-v1',"+
 "tailPredictor:'full-shooting-projected128-tangent-v1',"+
 "freshOriginal64CaptureBackend:backendLabel,amplitudeWarm:'physical-Q-L-amplitude-v1',"+
 "storedMetricAdapter:storedGeometry.manifest,stableGraphAdapter:storedEngineManifest,"+
 "liveResponseArithmetic:'R493-current-H-live128-with-explicit-binary64-protocol-projection-v1',"+
 "liveResponseSource:live128AdapterManifest");
// These source transformations establish the actual call path. They never
// run an extra primal-shadow comparison or add a scientific acceptance gate.
let inverse=source;
for(const change of [...replacements].reverse()){
 if(inverse.split(change.after).length!==2)throw Error('Unique inverse current-worker source patch');
 inverse=inverse.replace(change.after,change.before);
}
if(inverse!==original)throw Error('Whole original worker source inverse differs');
const importRedirects=[];
for(const relative of new Set([...source.matchAll(/['"]\.\/([^'"]+)['"]/g)].map(x=>x[1]))){
 const absolute=pathToFileURL(path.join(topic,'scripts',relative)).href;
 source=source.replaceAll("'./"+relative+"'",JSON.stringify(absolute))
              .replaceAll('"./'+relative+'"',JSON.stringify(absolute));
 importRedirects.push({relative,absolute});
}
const manifest={
 schema:'R493-original-worker-to-live128-protocol-source-composition-v1',
 sourceWorker:workerPath,sourceWorkerSHA256:sha256(original),
 adapter:fs.realpathSync(fileURLToPath(import.meta.url)),
 adapterSHA256:sha256(fs.readFileSync(fileURLToPath(import.meta.url))),
 actualCallModule:liveURL,actualCallModuleSHA256:sha256(fs.readFileSync(new URL(liveURL))),
 originalStoredEngine:engineURL,originalStoredEngineSHA256:sha256(fs.readFileSync(new URL(engineURL))),
 actualOriginalSourceOrigin:JSON.parse(fs.readFileSync(path.join(topic,'source-origin.json'),'utf8')),
 replacements,importRedirects,complete_original_source_inverse_verified:true,
 original_nonlin_solve_is_not_called_as_an_extra_probe:true,
 no_old64_endpoint_J_overwrite:true,
 original_warm_predictor_amplitude_boundary_choices_retained:true,
 same_current_H128_primal_component_audit_contract_explicit:true,
 arbitrary_current_height_not_restricted_to_fixed_actual91:true,
 new_128_interface_projection_is_not_old64_word_equality:true,
 native_accepted:false,fullDN_accepted:false
};
const cuspPath=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,
 'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs');
source='import {createStoredPhysical} from '+JSON.stringify(geometryURL)+';\n'+
 'import {createLive128Session} from '+JSON.stringify(liveURL)+';\n'+
 'import {splitIntegrationInterval} from '+JSON.stringify(pathToFileURL(cuspPath).href)+';\n'+
 'const live128AdapterManifest='+JSON.stringify(manifest)+';\n'+source;
const output=path.join(spec.output,'worker-source-composition.json');
fs.writeFileSync(output,JSON.stringify({...manifest,actual_compiled_worker_sha256:sha256(source)},null,2)+'\n',{flag:'wx'});
try{
 await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
}catch(error){
 console.error(String(error?.stack??error).replace(
  /data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<actual-R493-live128-worker-source>'));
 process.exitCode=1;
}
