#!/usr/bin/env node
// Exact complete-source identity repair only. No scientific imports or calls.
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
const SPEC={
  "schema": "complete-fixed-fejer-geometry-meridian-source-constant-repair-v1",
  "parent": {
    "name": "so3_fixed_fejer_batched_missing_angle_geometry.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py",
    "bytes": 88163,
    "sha256": "c1dad273c31eacfd25e245927e35b07f0010441f95bc71a3dd56082c665c0e98",
    "git_blob_sha": "372e9da72b43c41b8c004d6e514ee8e83723415a"
  },
  "child": {
    "name": "so3_fixed_fejer_batched_missing_angle_geometry.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/so3_fixed_fejer_batched_missing_angle_geometry.py",
    "bytes": 88163,
    "sha256": "5730b1792d58c1c695592aaea8a229d76b68f8bd1fefe8ded6016afba9566135",
    "git_blob_sha": "c5325d3da8329547ad81e74a5da479323bfccd21"
  },
  "actual_helper": {
    "name": "fixed_fejer_detached_meridian_values.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_values.py",
    "bytes": 41126,
    "sha256": "eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de",
    "git_blob_sha": "2b547c08dcaeb55701f5c68ba56d405f595f5b9e"
  },
  "unchanged_actual_normal": {
    "name": "fixed_fejer_detached_meridian_normal_lift.py",
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_detached_meridian_normal_lift.py",
    "bytes": 96276,
    "sha256": "76185c2184bd9b29eaec1177b540d1d549ea8b6b6e57befe3c2840618051407d",
    "git_blob_sha": "fc51c16b6dbd53abf04fe9175e5421f77e25c49c"
  },
  "patch": {
    "before": "DETACHED_MERIDIAN_VALUES_SOURCE_SHA256 = '7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd'",
    "after": "DETACHED_MERIDIAN_VALUES_SOURCE_SHA256 = 'eaeaf274bf0e74e63afbaa92588ea48d8ea75316f602882f49e71fa7453cb1de'",
    "occurrences": 1
  }
};
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const options={};const words=process.argv.slice(2);
for(let i=0;i<words.length;i+=2){
 if(!['--parent-source','--meridian-values','--output'].includes(words[i])||!words[i+1]||words[i] in options)throw Error('Use each complete path option exactly once');
 options[words[i]]=path.resolve(words[i+1]);
}
if(Object.keys(options).length!==3)throw Error('Required: --parent-source FILE --meridian-values FILE --output FILE');
if(options['--output']===options['--parent-source']||options['--output']===options['--meridian-values'])throw Error('Retain the original complete input files');
async function read(filename,record){
 const raw=await fs.readFile(filename);
 if(raw.length!==record.bytes||hash(raw)!==record.sha256)throw Error('Whole source mismatch: '+filename);
 const s=raw.toString('utf8');if(!Buffer.from(s,'utf8').equals(raw))throw Error('Use the complete valid UTF-8 source');
 return s;
}
const parent=await read(options['--parent-source'],SPEC.parent);
await read(options['--meridian-values'],SPEC.actual_helper);
if(parent.split(SPEC.patch.before).length-1!==SPEC.patch.occurrences)throw Error('The unique original identity declaration changed');
const result=parent.replace(SPEC.patch.before,SPEC.patch.after);
if(result.replace(SPEC.patch.after,SPEC.patch.before)!==parent)throw Error('The complete original source was not recovered');
const raw=Buffer.from(result,'utf8');
if(raw.length!==SPEC.child.bytes||hash(raw)!==SPEC.child.sha256)throw Error('The entire repaired source differs');
await fs.mkdir(path.dirname(options['--output']),{recursive:true});
try {
 const old=await fs.readFile(options['--output']);
 if(!old.equals(raw))throw Error('Refuse a different existing output');
}catch(error){
 if(error.code!=='ENOENT')throw error;
 await fs.writeFile(options['--output'],raw,{flag:'wx'});
}
process.stdout.write(JSON.stringify({complete_source:SPEC.child,changed_literal_only:true,
 guard_and_all_function_bodies_unchanged:true,scientific_execution:false},null,2)+'\n');
