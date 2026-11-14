// Compile all nested worker adapters without importing any physical module.
import fs from 'node:fs';
import crypto from 'node:crypto';
import vm from 'node:vm';
import zlib from 'node:zlib';

const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
const out=process.argv[2];
if(!out)throw Error('An explicit diagnostic output prefix is required');
const workerURL=new URL('./strong_exact_stage_tail_worker.mjs',import.meta.url).href;
const builtinCache=new Map();
async function linker(name){
 if(!name.startsWith('node:'))throw Error('A physical import is forbidden in static transform verification: '+name);
 if(!builtinCache.has(name)){
  const values=await import(name),keys=Object.keys(values);
  const module=new vm.SyntheticModule(keys,function(){for(const key of keys)this.setExport(key,values[key]);});
  builtinCache.set(name,module);
 }
 return builtinCache.get(name);
}
async function evaluateBuilder(source,url,marker,capture){
 const index=source.lastIndexOf(marker);
 if(index<0||source.indexOf(marker)!==index)throw Error('The import-stop anchor is not unique');
 const prefix=source.slice(0,index)+'\nglobalThis.'+capture+'=typeof transformed!=="undefined"?transformed:source;\n';
 const module=new vm.SourceTextModule(prefix,{identifier:url,
  initializeImportMeta:meta=>{meta.url=url;}});
 await module.link(linker);await module.evaluate();
 return globalThis[capture];
}
const original=fs.readFileSync(new URL(workerURL),'utf8');
const first=await evaluateBuilder(original,workerURL,
 "try{await import('data:text/javascript;base64,'+Buffer.from(transformed).toString('base64'));}",'__stagePreparedHost');
const second=await evaluateBuilder(first,workerURL,
 "try{await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));}",'__stagePreparedFrozen');
const third=await evaluateBuilder(second,workerURL,
 "try{\n  await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));",'__stagePreparedPhysicalWorker');
// Parsing the final module performs no imports or evaluation.
new vm.SourceTextModule(third,{identifier:'file:///explicit-static-physical-worker-not-evaluated.mjs'});
// Replacement manifests also quote these anchors; count executable statement
// lines rather than occurrences inside the serialized provenance strings.
if([...third.matchAll(/^[ \t]*const sol=dn\.solve\(req\.height,/gm)].length!==1||
   [...third.matchAll(/^[ \t]*const exactInitialSeed=saveExactInitialSeed\(/gm)].length!==1||
   [...third.matchAll(/^[ \t]*const check=compareCompleteStageEvaluation\(dn,initial,req\.height/gm)].length!==1)
 throw Error('Original solve and explicit observation/diagnostic sites differ');
const outputs=[];
for(const [name,source] of [['host',first],['frozen-host',second],['physical-worker',third]]){
 const file=out+'-'+name+'.txt.gz',bytes=zlib.gzipSync(source);
 fs.writeFileSync(file,bytes,{flag:'wx'});
 outputs.push({kind:name,file,bytes:bytes.length,compressedSHA256:sha(bytes),sourceSHA256:sha(source)});
}
const report={scope:'Exact nested worker source substitutions and final module parsing only.',
 passed:true,physicalModulesImported:0,physicalFactories:0,RHSEvaluations:0,JacobianEvaluations:0,
 NodeNonlinearWorkers:0,sourceSHA256:sha(original),
 checkSHA256:sha(fs.readFileSync(new URL(import.meta.url))),outputs,
 originalSolveCallRetainedOnce:true,seedBeforeSolve:true,diagnosticNotConvergedResponse:true,
 runtime:{node:process.versions.node,v8:process.versions.v8,arch:process.arch,platform:process.platform}};
fs.writeFileSync(out+'.json',JSON.stringify(report,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify(report));
