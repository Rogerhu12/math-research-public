// Disk retention of actual independent finite stage outputs. The key includes
// exact binary inputs, exact tabulated profiles, engine options, source closure,
// architecture and V8 version. A hit is the already computed same map value,
// never an inferred DN solve. Partial/missing/corrupt blocks are recomputed.
import fs from 'node:fs';
import path from 'node:path';
import v8 from 'node:v8';
import zlib from 'node:zlib';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';

const SCHEMA='visible-flex-actual-stage-output-cache-v1',BLOCK=32;
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
function sourceClosure(entry){
 const sourceScripts=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,
  'topics/large-amplitude-twist-flex/scripts');
 const seen=new Set(),todo=[path.resolve(entry)],rows=[];
 while(todo.length){
  const file=todo.pop();if(seen.has(file))continue;seen.add(file);
  const bytes=fs.readFileSync(file),text=bytes.toString();
  rows.push({path:file,sha256:digest(bytes)});
  for(const match of text.matchAll(/['"]([^'"\n]+\.mjs)['"]/g)){
   const name=match[1],candidates=[path.resolve(path.dirname(file),name),
    path.resolve(sourceScripts,name)];
   const found=candidates.find(p=>fs.existsSync(p)&&fs.statSync(p).isFile());
   if(found&&!seen.has(found))todo.push(found);
  }
 }
 rows.sort((a,b)=>a.path.localeCompare(b.path));return rows;
}
function atomic(file,bytes){
 const temporary=file+'.tmp-'+process.pid;
 fs.writeFileSync(temporary,bytes);fs.renameSync(temporary,file);
}

export function createStageMapCache({cacheRoot,entryURL,tables,options,
 stepsPerSegment,count,K,diagnostic=()=>{}}){
 if(!cacheRoot)return null;
 const observe=row=>{try{diagnostic(row);}catch{}};
 let root,context,sources;
 try{
  root=path.resolve(cacheRoot);fs.mkdirSync(root,{recursive:true});
  sources=sourceClosure(fileURLToPath(entryURL));
  context=digest(v8.serialize({schema:SCHEMA,options,stepsPerSegment,tables,
   sources,arch:process.arch,v8:process.versions.v8}));
  const manifest={schema:SCHEMA,context,sources,options,stepsPerSegment,count,K,
   blockSize:BLOCK,arch:process.arch,v8:process.versions.v8,
   scope:'Exact finite stage map cache only. No nonlinear response is inferred.'};
  const file=path.join(root,context+'-context.json');
  if(!fs.existsSync(file))atomic(file,JSON.stringify(manifest,null,2)+'\n');
 }catch(error){observe({event:'stage_cache_unavailable',error:String(error)});return null;}

 return {
  metadata:{schema:SCHEMA,root,context,blockSize:BLOCK,sourceCount:sources.length},
  begin(input,withJac,{status,output,jacobian,scalar}){
   const inputHash=digest(Buffer.from(input.buffer,input.byteOffset,input.byteLength));
   const key=digest(context+'|'+inputHash+'|'+String(withJac));
   const directory=path.join(root,key),saved=new Set();
   let loadedStages=0,newlySavedStages=0,disabled=false;
   const blockFile=start=>path.join(directory,'block-'+String(start).padStart(5,'0')+'.v8.gz');
   const dimensions=(row,start,end)=>row?.schema===SCHEMA&&row.key===key&&
    row.start===start&&row.end===end&&row.withJac===withJac&&
    row.output instanceof Float64Array&&row.output.length===(end-start)*K&&
    row.scalar instanceof Float64Array&&row.scalar.length===3*(end-start)&&
    (!withJac||(row.jacobian instanceof Float64Array&&row.jacobian.length===(end-start)*K*K));
   try{
    fs.mkdirSync(directory,{recursive:true});
    for(let start=0;start<count;start+=BLOCK){
     const end=Math.min(count,start+BLOCK),file=blockFile(start);
     if(!fs.existsSync(file))continue;
     try{
      const row=v8.deserialize(zlib.gunzipSync(fs.readFileSync(file)));
      if(!dimensions(row,start,end))throw new Error('Cached stage block identity/dimensions differ');
      output.set(row.output,start*K);scalar.set(row.scalar,3*start);
      if(withJac)jacobian.set(row.jacobian,start*K*K);
      for(let i=start;i<end;i++)Atomics.store(status,i,1);
      saved.add(start);loadedStages+=end-start;
     }catch(error){observe({event:'stage_cache_block_ignored',key,start,end,error:String(error)});}
    }
   }catch(error){disabled=true;observe({event:'stage_cache_unavailable',key,error:String(error)});}
   observe({event:'stage_cache_evaluation_start',context,key,inputHash,withJac,
    count,loadedStages,directory});
   function flush(){
    if(disabled)return;
    for(let start=0;start<count;start+=BLOCK){
     if(saved.has(start))continue;
     const end=Math.min(count,start+BLOCK);let complete=true;
     for(let i=start;i<end;i++)if(Atomics.load(status,i)!==1){complete=false;break;}
     if(!complete)continue;
     try{
      const record={schema:SCHEMA,key,start,end,withJac,
       output:output.slice(start*K,end*K),scalar:scalar.slice(3*start,3*end),
       jacobian:withJac?jacobian.slice(start*K*K,end*K*K):null};
      const bytes=zlib.gzipSync(v8.serialize(record));
      if(bytes.length>=5_000_000)throw new Error('Stage cache block exceeds file size limit');
      const file=blockFile(start);atomic(file,bytes);saved.add(start);newlySavedStages+=end-start;
      const row={event:'stage_cache_block_saved',time:new Date().toISOString(),
       context,key,withJac,start,end,bytes:bytes.length,sha256:digest(bytes),file};
      fs.appendFileSync(path.join(directory,'index.jsonl'),JSON.stringify(row)+'\n');
      observe(row);
     }catch(error){disabled=true;observe({event:'stage_cache_write_failed',key,start,end,error:String(error)});return;}
    }
   }
   return {flush,finish(){flush();observe({event:'stage_cache_evaluation_complete',context,key,
    inputHash,withJac,count,loadedStages,newlySavedStages,directory});}};
  },
 };
}
