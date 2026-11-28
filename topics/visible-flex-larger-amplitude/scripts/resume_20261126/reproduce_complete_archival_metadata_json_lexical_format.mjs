#!/usr/bin/env node
/** Complete lexical JSON whitespace formatting, with original whole recovery.
 * Does not parse/reserialize scientific values or run a scientific module.
 * node reproduce_complete_archival_metadata_json_lexical_format.mjs
 *   --manifest FILE --source-directory ROOT --output-directory NEW_ROOT
 */
import {readFile,writeFile,mkdir,access} from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
const hash=(bytes,algorithm='sha256')=>createHash(algorithm).update(bytes).digest('hex');
const blob=bytes=>hash(Buffer.concat([Buffer.from('blob '+bytes.length+'\0'),bytes]),'sha1');
function lexicalCompactJSON(body){
 let out="",inside=false,escaped=false;
 for(let i=0;i<body.length;i++){
  const ch=body[i];
  if(inside){out+=ch;if(escaped){escaped=false;}else if(ch==="\\"){escaped=true;}else if(ch==='"'){inside=false;}}
  else if(ch==='"'){inside=true;out+=ch;}
  else if(ch!==" "&&ch!=="\t"&&ch!=="\r"&&ch!=="\n"){out+=ch;}
 }
 if(inside||escaped)throw Error("unfinished JSON string");
 return out+"\n";
}
const args={};
for(let i=2;i<process.argv.length;i+=2){
 const key=process.argv[i],value=process.argv[i+1];
 if(!['--manifest','--source-directory','--output-directory'].includes(key)
    ||value===undefined||value.startsWith('--')||Object.hasOwn(args,key))
   throw Error('Supply the three complete path options once');
 args[key]=path.resolve(value);
}
if(Object.keys(args).length!==3)throw Error('All three complete path options are required');
if(args['--source-directory']===args['--output-directory'])
 throw Error('Keep the original whole checkout separate from generated files');
const manifestBytes=await readFile(args['--manifest']);
const manifest=JSON.parse(manifestBytes.toString('utf8'));
if(manifest.schema!=='complete-archival-metadata-JSON-lexical-whitespace-format-v1'
    ||!Array.isArray(manifest.complete_file_map))
 throw Error('Use the complete recorded formatting map');
const completed=[];
for(const r of manifest.complete_file_map){
 if(!r.path.startsWith('topics/visible-flex-larger-amplitude/computations/')
      ||r.path.split('/').includes('..')||!r.path.endsWith('.json'))
   throw Error('Unexpected mapped path');
 const input=path.join(args['--source-directory'],r.path);
 const output=path.join(args['--output-directory'],r.path);
 const original=await readFile(input);
 if(original.length!==r.original.bytes||hash(original)!==r.original.sha256
      ||blob(original)!==r.original.sha)
   throw Error('Restore the entire original recorded Git body before formatting '+r.path);
 const text=original.toString('utf8');
 if(!Buffer.from(text,'utf8').equals(original))throw Error('Original must be lossless UTF-8');
 const formatted=Buffer.from(lexicalCompactJSON(text),'utf8');
 if(formatted.length!==r.current.bytes||hash(formatted)!==r.current.sha256
      ||blob(formatted)!==r.current.sha)
   throw Error('Complete expected formatted body differs '+r.path);
 await mkdir(path.dirname(output),{recursive:true});
 try{
   await access(output);
   if(!(await readFile(output)).equals(formatted))
     throw Error('Refusing to replace a different existing output '+r.path);
 }catch(error){if(error.code!=='ENOENT')throw error;}
 await writeFile(output,formatted);
 completed.push({path:r.path,bytes:formatted.length,sha256:hash(formatted),git_blob_sha:blob(formatted)});
}
console.log(JSON.stringify({
 schema:'complete-archival-metadata-JSON-lexical-whitespace-format-run-v1',
 manifest_sha256:hash(manifestBytes),preformat_fixed_commit:manifest.preformat_fixed_commit,
 files:completed,scientific_calculation:false,
 numeric_tokens_or_string_bytes_changed:false,
 git_ref_or_active_queue_written:false
},null,2));
