// Preserve actual stage outputs when their byte-identical source/input tree is
// copied outside git. Verify the complete old context from the copied inputs;
// only logical source paths in that context change. No stage flow is rerun.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import v8 from 'node:v8';
import {createHash} from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';

const argv=process.argv.slice(2),args={};
for(let i=0;i<argv.length;i+=2){
 if(!argv[i].startsWith('--')||argv[i+1]===undefined)throw Error('key/value arguments required');
 args[argv[i].slice(2)]=argv[i+1];
}
for(const key of ['config','warm','cache-root','old-context','original-topic','out'])
 if(!args[key])throw Error('Missing --'+key);
if(fs.existsSync(args.out))throw Error('Choose a new closed migration report');
const here=path.dirname(fileURLToPath(import.meta.url)),topic=path.dirname(here),
 sourceRoot=path.join(topic,'repro/source-root'),cacheRoot=path.resolve(args['cache-root']);
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
const read=file=>{
 const bytes=fs.readFileSync(file);
 return JSON.parse(bytes[0]===31&&bytes[1]===139?zlib.gunzipSync(bytes):bytes);
};
const cfg=read(args.config),warm=read(args.warm),cp=warm.response?.checkpoint??warm.checkpoint??warm;
const old=read(path.join(cacheRoot,args['old-context']+'-context.json'));
if(old.context!==args['old-context'])throw Error('Old context identity differs');
const movedSources=old.sources.map(row=>{
 const relative=path.relative(path.resolve(args['original-topic']),row.path);
 if(relative.startsWith('..')||path.isAbsolute(relative))throw Error('Old source lies outside its declared topic');
 const file=path.join(topic,relative),sha256=digest(fs.readFileSync(file));
 if(sha256!==row.sha256)throw Error('Copied source bytes differ: '+relative);
 return {path:file,sha256};
}).sort((a,b)=>a.path.localeCompare(b.path));

const {createRecalibrationFactory}=await import('./closing_weighted_tail.mjs');
const {subdividePhysical}=await import('./950f-tail-subdivision.mjs');
const {createStageMapCache}=await import('./fd2d-stage-map-cache.mjs');
const {splitIntegrationInterval,integrationGrid}=await import(pathToFileURL(path.join(
 sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));
const poolFile=path.join(here,'fd2d-cached-tail-stage-pool.mjs'),poolSource=fs.readFileSync(poolFile,'utf8');
const begin=poolSource.indexOf('function tabulateProfile('),
 end=poolSource.indexOf('\nfunction restoreProfile(',begin);
if(begin<0||end<0)throw Error('Actual pool tabulation definition was not found');
// This is the exact saved tabulation routine, with its own original imports.
// Reconstructing the old context hash below checks all resulting profile bits.
const tabulateProfile=new Function('splitIntegrationInterval','integrationGrid','infrastructure',
 poolSource.slice(begin,end)+'\nreturn tabulateProfile;')(
 splitIntegrationInterval,integrationGrid,message=>new Error(message));
const physical=createRecalibrationFactory(cfg).assemble(),
 stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts);
const options={modes:cfg.modes,quadrature:cfg.quadrature,spacing:cfg.spacing,
 orientation:physical.parameters.orientation,projectionFloor:cfg.projectionFloor??.05,
 cuspAwareFlow:cfg.cuspAwareFlow===true};
const stepsPerSegment=cfg.steps,count=stages.cells.length,K=2*cfg.modes;
if(cp.states.length!==count+1||cp.states.some(row=>row.length!==K))
 throw Error('Actual warm dimensions differ from the copied finite stages');
const tables=stages.cells.map((cell,index)=>({index,mu:cell.mu,portRatio:cell.portRatio,
 profiles:cell.profiles.map(p=>tabulateProfile(p,stepsPerSegment,options.cuspAwareFlow))}));
const oldReconstructed=digest(v8.serialize({schema:old.schema,options,stepsPerSegment,tables,
 sources:old.sources,arch:process.arch,v8:process.versions.v8}));
if(oldReconstructed!==old.context)
 throw Error('Copied inputs/profiles/options/runtime did not reproduce the old exact cache context');
const cache=createStageMapCache({cacheRoot,entryURL:pathToFileURL(poolFile),tables,options,
 stepsPerSegment,count,K,diagnostic:row=>process.stderr.write(JSON.stringify(row)+'\n')});
if(!cache)throw Error('New source-path context could not be created');
const current=read(path.join(cacheRoot,cache.metadata.context+'-context.json'));
if(JSON.stringify(current.sources)!==JSON.stringify(movedSources))
 throw Error('New dependency closure is not exactly the path relocation of the old closure');
const input=new Float64Array(count*K);
for(let n=0;n<count;n++)input.set(cp.states[n+1],n*K);
const inputHash=digest(Buffer.from(input.buffer)),migrations=[];
for(const withJac of [true,false]){
 const oldKey=digest(old.context+'|'+inputHash+'|'+String(withJac)),
  newKey=digest(current.context+'|'+inputHash+'|'+String(withJac));
 const sourceDirectory=path.join(cacheRoot,oldKey),destination=path.join(cacheRoot,newKey);
 if(!fs.existsSync(sourceDirectory))continue;
 fs.mkdirSync(destination,{recursive:true});
 for(const name of fs.readdirSync(sourceDirectory).filter(n=>/^block-\d+\.v8\.gz$/.test(n)).sort()){
  const source=path.join(sourceDirectory,name),originalBytes=fs.readFileSync(source),
   record=v8.deserialize(zlib.gunzipSync(originalBytes));
  if(record.schema!==old.schema||record.key!==oldKey||record.withJac!==withJac||
   record.start<0||record.end>count||record.output.length!==(record.end-record.start)*K||
   record.scalar.length!==3*(record.end-record.start)||
   (withJac&&record.jacobian.length!==(record.end-record.start)*K*K))
   throw Error('Actual old block identity/dimensions differ');
  // Preserve these same typed arrays; only the path-sensitive context key is relabelled.
  record.key=newKey;
  const bytes=zlib.gzipSync(v8.serialize(record)),file=path.join(destination,name);
  if(bytes.length>=5_000_000)throw Error('Relocated cache block exceeds file size limit');
  if(fs.existsSync(file)){
   if(digest(fs.readFileSync(file))!==digest(bytes))throw Error('Destination cache block conflicts');
  }else{
   fs.writeFileSync(file+'.tmp',bytes);fs.renameSync(file+'.tmp',file);
  }
  const row={event:'stage_cache_block_relocated',withJac,start:record.start,end:record.end,
   original_context:old.context,context:current.context,original_key:oldKey,key:newKey,
   original_file:source,original_sha256:digest(originalBytes),file,sha256:digest(bytes),
   bytes:bytes.length,typed_array_values_unchanged:true};
  migrations.push(row);
 }
 const rows=migrations.filter(row=>row.key===newKey);
 fs.writeFileSync(path.join(destination,'relocated-index.jsonl'),rows.map(row=>JSON.stringify(row)).join('\n')+'\n');
}
const report={scope:'Exact relocation of already computed stage outputs; zero new stage flows, DN solves or BVP calls',
 old_context:old.context,new_context:current.context,old_context_reconstructed_exactly:true,
 all_dependency_source_bytes_equal:true,changed_context_content:'source paths only',
 source_count:old.sources.length,input_hash:inputHash,stages:count,K,
 original_warm_file:path.resolve(args.warm),original_warm_sha256:digest(fs.readFileSync(args.warm)),
 retained_blocks:migrations.length,retained_stages:migrations.reduce((n,row)=>n+row.end-row.start,0),migrations};
const bytes=Buffer.from(JSON.stringify(report,null,2)+'\n');
if(bytes.length>=1_000_000)throw Error('Unexpectedly large relocation metadata');
fs.writeFileSync(args.out,bytes,{flag:'wx'});
console.log(JSON.stringify({out:args.out,bytes:bytes.length,sha256:digest(bytes),
 retained_blocks:report.retained_blocks,retained_stages:report.retained_stages,
 old_context:old.context,new_context:current.context,input_hash:inputHash}));
