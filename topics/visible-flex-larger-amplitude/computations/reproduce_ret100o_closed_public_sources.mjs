#!/usr/bin/env node
/** Recreate the complete original source files for closed public Actions.
 * Run from any directory with --out DESTINATION, optionally --topic TOPIC.
 * Input consists of independent, complete retained source files and whole-line
 * replacements. This entry reads local published text only and runs no science.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

export function restoreWhole(parent, edits) {
  const lines=parent.match(/[^\n]*\n|[^\n]+$/g)||[];
  const output=[];
  let cursor=0;
  for (const [first,remove,insert] of edits) {
    if (!Number.isSafeInteger(first)||!Number.isSafeInteger(remove)||first<cursor||
        remove<0||first+remove>lines.length||typeof insert!=='string') {
      throw new Error('Invalid original-line replacement');
    }
    output.push(...lines.slice(cursor,first),insert);
    cursor=first+remove;
  }
  output.push(...lines.slice(cursor));
  return output.join('');
}

function digest(raw,algo) {return crypto.createHash(algo).update(raw).digest('hex');}
function verify(raw,item) {
  const [name,size,sha256,git]=item;
  const head=Buffer.from('blob '+raw.length+'\0','utf8');
  if (raw.length!==size||digest(raw,'sha256')!==sha256||
      digest(Buffer.concat([head,raw]),'sha1')!==git) throw new Error('Wrong complete file '+name);
  return raw;
}
function guardedName(root,relative) {
  if(typeof relative!=='string'||path.isAbsolute(relative)||
     relative.split('/').some(part=>!part||part==='.'||part==='..'))throw new Error('Invalid source path');
  return path.join(root,relative);
}

function main(argv) {
  const here=path.dirname(fileURLToPath(import.meta.url));
  let topic=path.resolve(here,'..'),out;
  for(let k=0;k<argv.length;k+=2) {
    if(!argv[k+1])throw new Error('Every option takes a directory');
    if(argv[k]==='--topic')topic=path.resolve(argv[k+1]);
    else if(argv[k]==='--out')out=path.resolve(argv[k+1]);
    else throw new Error('Unknown argument '+argv[k]);
  }
  if(!out)throw new Error('Supply --out DESTINATION');
  const manifestPath=path.join(topic,'computations','ret100o-closed-public-source-recovery.json');
  const manifest=JSON.parse(fs.readFileSync(manifestPath,'utf8'));
  const read=item=>verify(fs.readFileSync(guardedName(topic,item[0])),item);
  const originals=manifest.retained_whole_parents.map(item=>read(item).toString('utf8'));
  const completed=new Map();
  for(const item of manifest.complete_edit_documents) {
    const group=JSON.parse(read(item));
    for(const [index,parentIndex,edits] of group.members) {
      const identity=manifest.original_files[index];
      if(!identity||!Number.isSafeInteger(parentIndex)||parentIndex<0||parentIndex>=originals.length||
         completed.has(index)||manifest.parent_for_original[index]!==parentIndex)throw new Error('Invalid member '+index);
      const raw=Buffer.from(restoreWhole(originals[parentIndex],edits),'utf8');
      completed.set(index,verify(raw,identity));
    }
  }
  if(completed.size!==manifest.original_files.length)throw new Error('Incomplete historical source family');
  for(const [i,raw] of completed) {
    const target=guardedName(out,manifest.original_files[i][0]);
    if(fs.existsSync(target)&&!fs.readFileSync(target).equals(raw))throw new Error('Different existing output '+target);
  }
  for(const [i,raw] of completed) {
    const target=guardedName(out,manifest.original_files[i][0]);
    if(!fs.existsSync(target)) {
      fs.mkdirSync(path.dirname(target),{recursive:true});
      fs.writeFileSync(target,raw,{flag:'wx'});
    }
  }
  process.stdout.write(JSON.stringify({original_complete_sources:completed.size,independent_parents:originals.length,
    original_source_bytes:[...completed.values()].reduce((n,x)=>n+x.length,0),out})+'\n');
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))main(process.argv.slice(2));
