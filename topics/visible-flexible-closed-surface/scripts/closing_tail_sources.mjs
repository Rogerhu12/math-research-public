// Reproducible source lookup: adjacent checked-in topic first, optional verified cache second.
import fs from 'node:fs/promises';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import path from 'node:path';
const manifest=JSON.parse(await fs.readFile(new URL('../notes/closing_tail_dependency_blobs.json',import.meta.url),'utf8'));
const preferred=fileURLToPath(new URL('../../large-amplitude-twist-flex/scripts/',import.meta.url));
const candidates=[preferred,...(process.env.CLOSING_TAIL_CACHE?[process.env.CLOSING_TAIL_CACHE]:[]),'/workspace/scratch/f6f33987b45e/math-research/topics/large-amplitude-twist-flex/scripts'];
let selected;
for(const dir of candidates){try{await fs.access(path.join(dir,'f6tail_compact_controlled_tail.mjs'));selected=dir;break;}catch{}}
if(!selected)throw Error('Missing verified adjacent-topic sources; use a full repository checkout or set CLOSING_TAIL_CACHE to its scripts directory.');
for(const [name,sha] of Object.entries(manifest)){
 const bytes=await fs.readFile(path.join(selected,name));
 const got=crypto.createHash('sha1').update(Buffer.from('blob '+bytes.length+'\0')).update(bytes).digest('hex');
 if(got!==sha)throw Error('Dependency Git blob mismatch: '+name+' expected '+sha+' got '+got);
}
export async function loadClosingTailSource(name){
 if(!(name in manifest))throw Error('Unlisted dependency '+name);
 return import(pathToFileURL(path.join(selected,name)).href);
}
export const closingTailSourceDirectory=selected;
