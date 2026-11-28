#!/usr/bin/env node
/** Restore exact complete closed historical parameter documents. No scientific program is loaded. */
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {existsSync,mkdirSync,readFileSync,writeFileSync} from 'node:fs';
import {dirname,join,resolve} from 'node:path';
import {fileURLToPath} from 'node:url';

const here=dirname(fileURLToPath(import.meta.url));
const topic=dirname(here);
const repo=execFileSync('git',['-C',topic,'rev-parse','--show-toplevel'],{encoding:'utf8'}).trim();
const registry=JSON.parse(readFileSync(join(here,'ret100n-closed-actions-whole-parameter-recovery.json')));
if(process.argv.length!==3) throw Error('Supply the complete restoration output directory.');
const output=resolve(process.argv[2]);
function jsonWords(text) {
    const pieces = text.match(/[ \t\r\n]*(?:"(?:\\.|[^"\\])*"|true|false|null|-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?|[{}\[\],:])|[ \t\r\n]+$/g) || [];
    if (pieces.join('') !== text) throw Error('Unsupported original JSON spelling');
    return pieces;
}
function verify(bytes,row) {
    const sha=createHash('sha256').update(bytes).digest('hex');
    const blob=createHash('sha1').update('blob '+bytes.length+'\0').update(bytes).digest('hex');
    if(bytes.length!==row[1]||sha!==row[2]||blob!==row[3]) throw Error('Whole-file identity differs: '+row[0]);
}
const documents=new Map();
const restored=new Set();
for(const [id,...row] of registry.independent_parent_files) {
    const bytes=execFileSync('git',['-C',repo,'show',registry.before_commit+':'+registry.topic+'/'+row[0]],{maxBuffer:100000});
    verify(bytes,row);
    const text=bytes.toString('utf8');
    JSON.parse(text);
    documents.set(id,jsonWords(text));
}
const targets=new Map(registry.retired_documents.map(([id,branch,...row])=>[id,row]));
for(const group of registry.complete_edit_groups) {
    const bytes=readFileSync(join(topic,group[0]));
    verify(bytes,group);
    for(const [id,operations] of JSON.parse(bytes).documents) {
        const row=targets.get(id);
        if(!row||restored.has(id)) throw Error('Missing or repeated output document '+id);
        const text=[];
        for(const operation of operations) {
            if(typeof operation==='string') {text.push(operation);continue;}
            const [parent,start,count]=operation;
            const words=documents.get(parent);
            if(!words||parent>=id||!Number.isInteger(start)||!Number.isInteger(count)||
                    start<0||count<=0||start+count>words.length) throw Error('Invalid prior complete parameter range '+id);
            text.push(words.slice(start,start+count).join(''));
        }
        const complete=text.join('');
        JSON.parse(complete);
        const bytes=Buffer.from(complete,'utf8');
        verify(bytes,row);
        const path=join(output,row[0]);
        mkdirSync(dirname(path),{recursive:true});
        if(existsSync(path)) verify(readFileSync(path),row);
        else writeFileSync(path,bytes,{flag:'wx'});
        documents.set(id,jsonWords(complete));
        restored.add(id);
        process.stdout.write(JSON.stringify({id,path:row[0],bytes:row[1],sha256:row[2],git_blob_sha:row[3]})+'\n');
    }
}
if(restored.size!==targets.size) throw Error('The complete requested output set did not return.');
