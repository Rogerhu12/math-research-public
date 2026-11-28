// Preload only: the original exporter, arguments, math and output bytes stay intact.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';

const root=path.resolve(process.env.HELD10_GEOMETRY_DISK_ROOT??'');
const floor=BigInt(process.env.HELD10_GEOMETRY_DISK_FLOOR??'0');
if(floor<16777216n||!fs.statSync(root).isDirectory())throw Error('A real geometry disk reserve is required');
const write=fs.writeFileSync,sourcePath=fileURLToPath(import.meta.url);
const source={path:sourcePath,sha256:createHash('sha256').update(fs.readFileSync(sourcePath)).digest('hex')};
const status=path.join(root,`disk-guard-node-${process.pid}.json`),sleep=new Int32Array(new SharedArrayBuffer(4));
function freeBytes(){const s=fs.statfsSync(root,{bigint:true});return s.bavail*s.bsize;}
function note(event,file,needed,free){
 const value={event,source,pid:process.pid,utc_unix_time:Date.now()/1000,pending_path:file,
  pending_bytes:Number(needed),free_bytes:Number(free),reserve_bytes:Number(floor),geometry_bytes_changed:false};
 write(status,JSON.stringify(value,null,2)+'\n');
 if(event!=='disk_write_gate_resumed')console.error(JSON.stringify(value));
}
fs.writeFileSync=function(file,data,...options){
 if(typeof file==='string'||file instanceof URL){
  const target=path.resolve(file instanceof URL?fileURLToPath(file):file);
  if(target===root||target.startsWith(root+path.sep)){
   const encoding=typeof options[0]==='string'?options[0]:options[0]?.encoding??'utf8';
   const needed=BigInt(typeof data==='string'?Buffer.byteLength(data,encoding):data.byteLength);
   let waiting=false,last=0;
   while(true){
    const free=freeBytes();
    if(free>=floor+needed){if(waiting)note('disk_write_gate_resumed',target,needed,free);break;}
    if(!waiting||Date.now()-last>=30000){note('disk_write_gate_waiting',target,needed,free);last=Date.now();}
    waiting=true;Atomics.wait(sleep,0,0,5000);
   }
  }
 }
 return write.call(fs,file,data,...options);
};
