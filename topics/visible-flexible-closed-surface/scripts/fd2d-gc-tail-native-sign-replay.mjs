// Recover native signed zeros by replaying the frozen Newton algebra against
// exact retained stage maps. Any unrecorded radial input is rejected.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import v8 from 'node:v8';
import {createHash} from 'node:crypto';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {appendUnchangedDeepSource} from './fd2d-gc-tail-deep-extension.mjs';
import {createSplitFluxCompactTailDN} from './fd2d-gc-tail-deep-cached-split.mjs';
import {geometricWarmRemesh} from './fd2d-gc-tail-normalized-warm-remesh.mjs';
import {createDeepSplitMomentumEngine} from './fd2d-gc-tail-deep-engine.mjs';
import {createGeometricTrialHook} from './fd2d-gc-tail-normalized-retraction.mjs';

const [runtime,responseFile,outPrefix]=process.argv.slice(2),started=Date.now(),
 hash=b=>createHash('sha256').update(b).digest('hex'),cfg=JSON.parse(fs.readFileSync(path.join(runtime,'config.json'))),
 responseBytes=fs.readFileSync(responseFile),response=JSON.parse(responseBytes),
 trace=fs.readFileSync(path.join(runtime,'outputs/actual-worker-trace.jsonl'),'utf8').trim().split('\n').map(JSON.parse),
 complete=trace.filter(x=>x.event==='stage_cache_evaluation_complete'),K=2*cfg.modes,
 loaded=new Map(),replayEvents=[];
if(!response.converged)throw Error('Only a complete successful response can be replay-bound');
function exactCache(record){
 if(loaded.has(record.key))return loaded.get(record.key);
 const index=fs.readFileSync(path.join(record.directory,'index.jsonl'),'utf8').trim().split('\n').map(JSON.parse),
  blocks=index.filter(x=>x.key===record.key&&x.withJac===record.withJac).sort((a,b)=>a.start-b.start),rows=[];
 let cursor=0;
 for(const b of blocks){
  const bytes=fs.readFileSync(b.file);if(hash(bytes)!==b.sha256)throw Error('Retained map SHA differs');
  const data=v8.deserialize(zlib.gunzipSync(bytes));
  if(data.key!==record.key||data.start!==cursor||data.end!==b.end||data.withJac!==record.withJac)throw Error('Retained map coverage/identity differs');
  for(let j=0;j<data.end-data.start;j++)rows.push({out:data.output.slice(j*K,(j+1)*K),
   J:record.withJac?data.jacobian.slice(j*K*K,(j+1)*K*K):null,meanHeight:data.scalar[3*j],
   minA:record.withJac?data.scalar[3*j+1]:undefined,minD:record.withJac?data.scalar[3*j+2]:undefined});
  cursor=data.end;
 }
 if(cursor!==record.count)throw Error('Retained map has missing stages');loaded.set(record.key,rows);return rows;
}
const stageEvaluationCache={begin(states,withJac){
 const packed=Float64Array.from(states.slice(1).flatMap(s=>Array.from(s))),inputHash=hash(Buffer.from(packed.buffer)),
  record=complete.find(x=>x.inputHash===inputHash&&x.withJac===withJac);
 if(!record)throw Error('No actual stored radial map for this exact native input '+inputHash+'/'+withJac);
 const rows=exactCache(record);replayEvents.push({key:record.key,inputHash,withJac,count:rows.length});
 return {has:()=>true,get:n=>rows[n],finish(){},flush(){}};
}},factory=createRecalibrationFactory(cfg);
boundTailPointCaches(factory,cfg,{pointsPerEntry:8});
const physical=appendUnchangedDeepSource(factory.assemble(),cfg.linearFar),
 dn=createSplitFluxCompactTailDN({...cfg,tail:physical,retainTangentPredictor:false,stageEvaluationCache}),
 originalWarm=JSON.parse(fs.readFileSync(cfg.initialCheckpoint)),prior=originalWarm.checkpoint,
 warm=geometricWarmRemesh(prior,dn,createDeepSplitMomentumEngine),trial=createGeometricTrialHook(dn.tail.cells,{spacing:cfg.spacing}),
 progress=[],sol=dn.solve(response.checkpoint.cutHeight,{initial:warm.states.map(Float64Array.from),
  maxIterations:cfg.maxIterations,tolerance:cfg.solveTolerance,jacobian:false,audit:false,
  retractTrial:trial.retractTrial,progress:row=>progress.push(row)});
if(!sol.converged)throw Error('Cached algebra did not reproduce accepted termination');
const values=Float64Array.from(sol.states.slice(1).flat()),actualHash=hash(Buffer.from(values.buffer)),
 finalComplete=complete.filter(x=>x.withJac).at(-1),jsonValues=Float64Array.from(response.checkpoint.states.slice(1).flat()),negativeZeroIndices=[];
if(actualHash!==finalComplete.inputHash)throw Error('Replayed native final input SHA differs');
for(let i=0;i<values.length;i++){
 if(values[i]!==jsonValues[i])throw Error('Nonzero numeric value differs at '+i);
 if(Object.is(values[i],-0))negativeZeroIndices.push(i);
}
const mask={schema:'fd2d-exact-native-input-negative-zero-mask-v1',source_response_sha256:hash(responseBytes),
 inputHash:actualHash,coordinate_count:values.length,node_start:1,node_count:sol.states.length-1,width:K,
 negativeZeroIndices,scope:'Exact original packed-input SHA reproduced from frozen Newton algebra and SHA-bound retained maps; no new radial stage map was evaluated.'},
 bytes=zlib.gzipSync(JSON.stringify(mask)+'\n'),maskFile=outPrefix+'-negative-zero-mask.json.gz';
fs.writeFileSync(maskFile,bytes,{flag:'wx'});
const report={source:{path:import.meta.filename,sha256:hash(fs.readFileSync(import.meta.filename))},
 runtime,response:{path:responseFile,bytes:responseBytes.length,sha256:hash(responseBytes)},
 actual_native_input_hash:actualHash,parsed_json_input_hash:hash(Buffer.from(jsonValues.buffer)),
 numeric_values_identical:true,negative_zero_count:negativeZeroIndices.length,coordinate_count:values.length,
 finalResidual:sol.normalizedResidual,originalResidual:response.residual,replayEvents,progress,
 mask:{path:maskFile,bytes:bytes.length,sha256:hash(bytes)},seconds:(Date.now()-started)/1000,
 scope:mask.scope};
fs.writeFileSync(outPrefix+'-report.json',JSON.stringify(report,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({negative_zero_count:negativeZeroIndices.length,actual_native_input_hash:actualHash,
 finalResidual:sol.normalizedResidual,replayEvents,seconds:report.seconds,mask:report.mask}));
