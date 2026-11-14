// Recover the actual finite mean-height integral already computed by the last
// completed F/J. No radial equation or numerical integration is repeated.
import fs from 'node:fs';
import path from 'node:path';
import v8 from 'node:v8';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
const [runtime,responseFile,outPrefix]=process.argv.slice(2),
 trace=fs.readFileSync(path.join(runtime,'outputs/actual-worker-trace.jsonl'),'utf8').trim().split('\n').map(JSON.parse),
 complete=trace.filter(r=>r.event==='stage_cache_evaluation_complete'&&r.withJac).at(-1),
 responseBytes=fs.readFileSync(responseFile),response=JSON.parse(responseBytes),hash=x=>crypto.createHash('sha256').update(x).digest('hex');
if(!response.converged||!complete||complete.count!==response.checkpoint.states.length-1)throw Error('Missing matching closed successful finite response/full-J');
const index=fs.readFileSync(path.join(complete.directory,'index.jsonl'),'utf8').trim().split('\n').map(JSON.parse),
 blocks=index.filter(r=>r.key===complete.key&&r.withJac).sort((a,b)=>a.start-b.start),means=[],inputs=[];
let next=0,sum=0,minA=Infinity,minD=Infinity;
for(const b of blocks){
 const bytes=fs.readFileSync(b.file);if(hash(bytes)!==b.sha256)throw Error('Actual block SHA differs');
 const r=v8.deserialize(zlib.gunzipSync(bytes));
 if(r.key!==complete.key||r.start!==next||r.end!==b.end||r.scalar.length!==3*(r.end-r.start))throw Error('Actual stage coverage differs');
 for(let i=0;i<r.end-r.start;i++){
  const h=r.scalar[3*i];if(!Number.isFinite(h))throw Error('Nonfinite retained mean');
  means.push(h);sum+=h;minA=Math.min(minA,r.scalar[3*i+1]);minD=Math.min(minD,r.scalar[3*i+2]);
 }
 next=r.end;inputs.push({start:r.start,end:r.end,sha256:b.sha256,bytes:bytes.length});
}
if(next!==complete.count)throw Error('Incomplete retained mean coverage');
const data={source_response_sha256:hash(responseBytes),context:complete.context,key:complete.key,inputHash:complete.inputHash,
 stage_count:means.length,mean_heights:means,scope:'Actual stored finite stage integrals, zero mean-height anchor at node160. The original unchanged infinite tail beyond160 still needs its stated flat-tail completion.'},
 bytes=zlib.gzipSync(JSON.stringify(data)+'\n'),dataFile=outPrefix+'-data.json.gz';
fs.writeFileSync(dataFile,bytes);
const report={response:{path:responseFile,bytes:responseBytes.length,sha256:hash(responseBytes)},
 complete_evaluation:complete,blocks:inputs,meanHeightToCut:sum,minA,minD,
 data:{path:dataFile,bytes:bytes.length,sha256:hash(bytes)},stage_count:means.length,
 scope:'Exactly the original ordered sum of already computed stage meanHeight scalars; no new solve. This is the finite160 value, not an infinite-tail certificate.'};
fs.writeFileSync(outPrefix+'-report.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({meanHeightToCut:sum,minA,minD,stage_count:means.length,data:report.data}));
