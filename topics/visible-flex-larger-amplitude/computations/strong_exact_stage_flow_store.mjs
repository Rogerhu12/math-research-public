// Optional exact-input persistence for a completed full-Jacobian stage map.
// This generic store does not construct a physical tail or alter any solver.
// A production caller must supply and verify its complete mathematical identity.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const MAGIC=Buffer.from('VFXJAC01','ascii');
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
function numberBytes(value){const b=Buffer.allocUnsafe(8);b.writeDoubleLE(value);return b;}
function canonical(value){
 if(value===null)return 'null';
 if(value===undefined)return 'undefined';
 if(typeof value==='number'){
  if(!Number.isFinite(value))throw Error('Nonfinite stage identity');
  return 'f64:'+numberBytes(value).toString('hex');
 }
 if(typeof value==='string')return 'str:'+JSON.stringify(value);
 if(typeof value==='boolean')return value?'true':'false';
 if(Array.isArray(value))return '['+value.map(canonical).join(',')+']';
 if(typeof value==='object'&&Object.getPrototypeOf(value)===Object.prototype)
  return '{'+Object.keys(value).sort().map(k=>JSON.stringify(k)+':'+canonical(value[k])).join(',')+'}';
 throw Error('Stage identity must contain plain recorded data only');
}
function vectorBytes(values,length){
 if(values.length!==length)throw Error('Stage vector dimension differs');
 const b=Buffer.allocUnsafe(length*8);
 for(let j=0;j<length;j++){
  if(!Number.isFinite(values[j]))throw Error('Nonfinite stage vector');
  b.writeDoubleLE(values[j],8*j);
 }
 return b;
}
function outputBytes(value,K){
 const keys=Object.keys(value).sort();
 if(JSON.stringify(keys)!==JSON.stringify(['J','meanHeight','minA','minD','out']))
  throw Error('Stage result contains an unrecorded field');
 return Buffer.concat([vectorBytes(value.out,K),vectorBytes(value.J,K*K),
  vectorBytes([value.meanHeight,value.minA,value.minD],3)]);
}
function decodeOutput(payload,K){
 const read=(first,length)=>Float64Array.from({length},(_,j)=>payload.readDoubleLE(8*(first+j)));
 const out=read(0,K),J=read(K,K*K),v=read(K+K*K,3);
 if(![...out,...J,...v].every(Number.isFinite))throw Error('Nonfinite cached stage output');
 return {out,J,meanHeight:v[0],minA:v[1],minD:v[2]};
}
export function createExactStageFlowStore({directory,identity,dimension,event=()=>{}}){
 if(!directory||!Number.isInteger(dimension)||dimension<1)
  throw Error('Explicit cache directory and full stage dimension are required');
 const K=dimension;
 const runtime={node:process.versions.node,v8:process.versions.v8,arch:process.arch,platform:process.platform};
 const identityText=canonical({schema:'exact-full-Jacobian-stage-v1',dimension:K,runtime,identity});
 const identitySHA=sha(identityText),root=path.join(path.resolve(directory),identitySHA);
 fs.mkdirSync(root,{recursive:true});
 const identityFile=path.join(root,'identity.txt');
 if(fs.existsSync(identityFile)){
  if(fs.readFileSync(identityFile,'utf8')!==identityText+'\n')throw Error('Stage-cache identity file mismatch');
 }else fs.writeFileSync(identityFile,identityText+'\n',{flag:'wx'});
 const stats={hits:0,misses:0,uncachedNonJacobian:0,storedBytes:0,loadedBytes:0};
 function evaluate(stage,input,withJac,compute){
  if(typeof compute!=='function')throw Error('The original exact stage callback is required');
  if(!withJac){stats.uncachedNonJacobian++;return compute();}
  if(!Number.isSafeInteger(stage)||stage<0)throw Error('Invalid physical numerical-stage index');
  const bytes=vectorBytes(input,K),inputSHA=sha(bytes);
  const key=sha(Buffer.concat([Buffer.from(identitySHA+':'+stage+':true:'),bytes]));
  const file=path.join(root,String(stage).padStart(6,'0')+'-'+key+'.bin');
  const expected={schema:'exact-full-Jacobian-stage-v1',identitySHA,stage,dimension:K,inputSHA,withJac:true};
  const payloadLength=(K+K*K+3)*8;
  if(fs.existsSync(file)){
   const record=fs.readFileSync(file);
   if(record.length<12||!record.subarray(0,8).equals(MAGIC))throw Error('Invalid cached stage magic');
   const headerLength=record.readUInt32LE(8);
   if(headerLength<1||headerLength>16384||record.length!==12+headerLength+payloadLength)
    throw Error('Incomplete cached stage payload');
   const header=JSON.parse(record.subarray(12,12+headerLength).toString('utf8'));
   for(const [name,value] of Object.entries(expected))if(header[name]!==value)
    throw Error('Exact stage cache header mismatch: '+name);
   const payload=record.subarray(12+headerLength);
   if(header.payloadSHA256!==sha(payload))throw Error('Exact stage cache payload checksum mismatch');
   stats.hits++;stats.loadedBytes+=record.length;
   event({kind:'restored-exact-stage',stage,key,identitySHA,inputSHA,
    payloadSHA256:header.payloadSHA256,source:'previously completed identical-input stage',
    independentRecomputation:false});
   return decodeOutput(payload,K);
  }
  const value=compute();
  const payload=outputBytes(value,K);
  const header=Buffer.from(JSON.stringify({...expected,payloadSHA256:sha(payload)}),'utf8');
  const size=Buffer.alloc(4);size.writeUInt32LE(header.length);
  const record=Buffer.concat([MAGIC,size,header,payload]);
  if(record.length>=5_000_000)throw Error('A stage checkpoint exceeds the file limit');
  const temporary=file+'.tmp-'+process.pid+'-'+crypto.randomBytes(8).toString('hex');
  fs.writeFileSync(temporary,record,{flag:'wx'});
  fs.renameSync(temporary,file);
  stats.misses++;stats.storedBytes+=record.length;
  event({kind:'stored-completed-stage',stage,key,identitySHA,inputSHA,
   payloadSHA256:sha(payload),bytes:record.length});
  return value;
 }
 return {evaluate,identitySHA,root,stats,
  scope:'Exact full-state binary key and full-source identity only. Every cached stage is an explicitly identified prior computation; all global residuals and original solve/audit gates remain the caller responsibility. Numerical engine diagnostic call counters are not replayed.'};
}
