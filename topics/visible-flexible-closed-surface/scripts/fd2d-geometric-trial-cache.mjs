// Retain actual complete geometric trial constructions across external exits.
// A saved trial is not accepted and is not a nonlinear response. The original
// complete residual and acceptance test still decide whether it is usable.
import fs from 'node:fs';
import path from 'node:path';
import v8 from 'node:v8';
import zlib from 'node:zlib';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {createGeometricTrialHook} from './78718-tail-geometric-newton-retraction-centered-v3.mjs';

const SCHEMA='visible-flex-complete-geometric-trial-cache-v1';
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
function sourceClosure(entries){
 const root=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,
  'topics/large-amplitude-twist-flex/scripts'),seen=new Set(),todo=[...entries],rows=[];
 while(todo.length){
  const file=todo.pop();if(seen.has(file))continue;seen.add(file);
  const bytes=fs.readFileSync(file);rows.push({path:file,sha256:digest(bytes)});
  for(const match of bytes.toString().matchAll(/['"]([^'"\n]+\.mjs)['"]/g)){
   const found=[path.resolve(path.dirname(file),match[1]),path.resolve(root,match[1])]
    .find(candidate=>fs.existsSync(candidate)&&fs.statSync(candidate).isFile());
   if(found&&!seen.has(found))todo.push(found);
  }
 }
 return rows.sort((a,b)=>a.path.localeCompare(b.path));
}
function atomic(file,bytes){
 const temporary=file+'.tmp-'+process.pid;
 fs.writeFileSync(temporary,bytes);fs.renameSync(temporary,file);
}

export function createCachedGeometricTrialHook(cells,{spacing,parameters,cacheRoot,
 diagnostic=()=>{}}={}){
 const observe=row=>{try{diagnostic({...row,hostMemory:process.memoryUsage()});}catch{}};
 const M=cells[0].engine.M,K=2*M,count=cells.length+1;
 const statistics={preparations:0,trialCalls:0,lastPreparation:null,
  cacheHits:0,cacheMisses:0,
  scope:'Actual complete trial constructions only; every returned trial still needs the original residual and acceptance.'};
 let root=null,context=null;
 try{
  if(cacheRoot){
   root=path.join(path.resolve(cacheRoot),'geometric-trials');fs.mkdirSync(root,{recursive:true});
   const here=path.dirname(fileURLToPath(import.meta.url)),
    sources=sourceClosure([fileURLToPath(import.meta.url),
     path.join(here,'78718-tail-fourier-root-split-engine.mjs')]);
   // These are exact fixed-node inputs to every root/conversion in the original
   // helper. No flow or root is evaluated to build this identity.
   const points=Array.from({length:count},(_,i)=>{
    const cell=cells[i===0?0:i-1],profile=i===0?cell.profiles.at(-1):cell.profiles[0],
     x=i===0?1:0,value=profile(x);
    if(Object.values(value).some(v=>typeof v!=='number'||!Number.isFinite(v)))
     throw Error('Original fixed-node profile contains nonfinite/nonnumeric data');
    return {M:cell.engine.M,N:cell.engine.N,mu:cell.mu,
     orientation:cell.engine.orientation,portRatio:i===0?cell.portRatio:1,x,value};
   });
   context=digest(v8.serialize({schema:SCHEMA,spacing,parameters,points,sources,
    arch:process.arch,v8:process.versions.v8}));
   const metadata={schema:SCHEMA,context,spacing,parameters,count,K,sources,
    arch:process.arch,v8:process.versions.v8,
    scope:'Exact fixed-node profile values and helper sources; a hit is an actual previously constructed trial, not acceptance.'};
   const file=path.join(root,context+'-context.json');
   if(!fs.existsSync(file))atomic(file,JSON.stringify(metadata,null,2)+'\n');
   observe({event:'geometric_trial_cache_ready',context,root,count,K,sourceCount:sources.length});
  }
 }catch(error){root=context=null;observe({event:'geometric_trial_cache_unavailable',error:String(error)});}

 function flatten(rows){
  if(rows.length!==count||rows.some(row=>row.length!==K))throw Error('Original trial dimensions differ');
  const result=new Float64Array(count*K);
  for(let n=0;n<count;n++)result.set(rows[n],n*K);
  return result;
 }
 function hashValues(values){return digest(Buffer.from(values.buffer,values.byteOffset,values.byteLength));}
 function retractTrial(states,delta,lambda){
  statistics.trialCalls++;
  let key=null,file=null,stateHash=null,deltaHash=null;
  if(root&&context){
   try{
    stateHash=hashValues(flatten(states));deltaHash=hashValues(flatten(delta));
    key=digest(context+'|'+stateHash+'|'+deltaHash+'|'+String(lambda));
    file=path.join(root,key+'.v8.gz');
    if(fs.existsSync(file)){
     const bytes=fs.readFileSync(file),record=v8.deserialize(zlib.gunzipSync(bytes));
     if(record.schema!==SCHEMA||record.key!==key||record.context!==context||
      record.stateHash!==stateHash||record.deltaHash!==deltaHash||record.lambda!==lambda||
      !(record.values instanceof Float64Array)||record.values.length!==count*K||
      record.valuesHash!==hashValues(record.values))throw Error('Complete trial cache identity/dimensions differ');
     statistics.cacheHits++;
     observe({event:'geometric_trial_cache_hit',context,key,stateHash,deltaHash,lambda,
      file,bytes:bytes.length,sha256:digest(bytes),scope:'Complete construction only; not accepted.'});
     return Array.from({length:count},(_,n)=>Array.from(record.values.subarray(n*K,(n+1)*K)));
    }
   }catch(error){observe({event:'geometric_trial_cache_ignored',key,error:String(error)});file=null;}
  }
  statistics.cacheMisses++;
  // The original helper is stateless across independently chosen states/delta.
  // Keep its preparation only during this actual construction, then release its
  // closures. A later uncached backtrack recomputes the same original helper.
  const actual=createGeometricTrialHook(cells,{spacing}),trial=actual.retractTrial(states,delta,lambda);
  statistics.preparations+=actual.statistics.preparations;
  statistics.lastPreparation=actual.statistics.lastPreparation;
  if(file&&context&&key){
   try{
    const values=flatten(trial),record={schema:SCHEMA,context,key,stateHash,deltaHash,lambda,
     valuesHash:hashValues(values),values,
     scope:'Actual complete UNACCEPTED geometric trial; no residual or convergence is inferred.'};
    const bytes=zlib.gzipSync(v8.serialize(record));
    if(bytes.length>=5_000_000)throw Error('Complete trial cache exceeds file size limit');
    atomic(file,bytes);
    observe({event:'geometric_trial_cache_saved',context,key,stateHash,deltaHash,lambda,
     file,bytes:bytes.length,sha256:digest(bytes),scope:'Complete construction only; not accepted.'});
   }catch(error){observe({event:'geometric_trial_cache_write_failed',key,error:String(error)});}
  }
  return trial;
 }
 return {retractTrial,statistics};
}
