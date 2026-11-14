// Exact initial shooting-state persistence. This is never an accepted solution.
// No physical factory, RHS, Newton iteration, Jacobian or audit is called here.
// Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {preserveExactRawWarm} from './strong_exact_raw_tail_warm.mjs';

const SCHEMA='exact-initial-shooting-seed-v1';
const STATUS='initial-warm-only';
const LIMIT=5_000_000;
const sha=value=>crypto.createHash('sha256').update(value).digest('hex');
const helperSHA=()=>sha(fs.readFileSync(new URL(import.meta.url)));
const warmSHA=()=>sha(fs.readFileSync(new URL('./strong_exact_raw_tail_warm.mjs',import.meta.url)));
const isSHA=value=>typeof value==='string'&&/^[a-f0-9]{64}$/.test(value);
const plain=value=>value!==null&&typeof value==='object'&&Object.getPrototypeOf(value)===Object.prototype;
const own=(value,key)=>Object.prototype.hasOwnProperty.call(value,key);

function numberHex(value){
 if(!Number.isFinite(value))throw Error('An exact initial seed cannot contain a nonfinite number');
 const bytes=Buffer.allocUnsafe(8);bytes.writeDoubleLE(value);return bytes.toString('hex');
}
function encodeExact(value,depth=0){
 if(depth>64)throw Error('Exact seed metadata exceeds the nesting limit');
 if(value===undefined)return ['undefined'];
 if(value===null)return ['null'];
 if(typeof value==='number')return ['f64le',numberHex(value)];
 if(typeof value==='string')return ['string',value];
 if(typeof value==='boolean')return ['boolean',value];
 if(Array.isArray(value)){
  if(Object.keys(value).length!==value.length||
      Object.keys(value).some((key,i)=>key!==String(i)))
   throw Error('Exact seed metadata requires ordinary dense arrays');
  return ['array',value.map(item=>encodeExact(item,depth+1))];
 }
 if(plain(value)){
  if(Reflect.ownKeys(value).some(key=>typeof key!=='string'))
   throw Error('Exact seed metadata cannot contain symbolic properties');
  const descriptors=Object.getOwnPropertyDescriptors(value);
  return ['object',Object.keys(value).sort().map(key=>{
   if(!own(descriptors[key],'value'))throw Error('Exact seed metadata cannot contain accessors');
   return [key,encodeExact(descriptors[key].value,depth+1)];
  })];
 }
 throw Error('Exact seed metadata must be plain recorded values');
}
function decodeExact(encoded,depth=0){
 if(depth>64||!Array.isArray(encoded))throw Error('Invalid exact seed metadata encoding');
 const [kind,value]=encoded;
 if(kind==='null'&&encoded.length===1)return null;
 if(kind==='undefined'&&encoded.length===1)return undefined;
 if(encoded.length!==2)throw Error('Invalid exact metadata tag length');
 if(kind==='f64le'){
  if(typeof value!=='string'||!/^[a-f0-9]{16}$/.test(value))
   throw Error('Invalid exact metadata binary64');
  const number=Buffer.from(value,'hex').readDoubleLE(0);
  if(!Number.isFinite(number))throw Error('Nonfinite encoded seed metadata');
  return number;
 }
 if(kind==='string'&&typeof value==='string')return value;
 if(kind==='boolean'&&typeof value==='boolean')return value;
 if(kind==='array'&&Array.isArray(value))return value.map(item=>decodeExact(item,depth+1));
 if(kind==='object'&&Array.isArray(value)){
  const result={};let previous=null;
  for(const pair of value){
   if(!Array.isArray(pair)||pair.length!==2||typeof pair[0]!=='string'||
       (previous!==null&&!(previous<pair[0])))
    throw Error('Exact metadata object keys must be unique and sorted');
   previous=pair[0];
   Object.defineProperty(result,pair[0],{value:decodeExact(pair[1],depth+1),
    enumerable:true,writable:true,configurable:true});
  }
  return result;
 }
 throw Error('Invalid exact seed metadata tag');
}
function exactRecord(value){
 const encoded=encodeExact(value);
 return {encoding:'tagged-plain-values-and-Float64LE-hex-v1',
  encoded,sha256:sha(JSON.stringify(encoded))};
}
function recoverRecord(record){
 if(!plain(record)||record.encoding!=='tagged-plain-values-and-Float64LE-hex-v1'||
     !isSHA(record.sha256)||sha(JSON.stringify(record.encoded))!==record.sha256)
  throw Error('Exact seed metadata checksum mismatch');
 const result=decodeExact(record.encoded);
 if(sha(JSON.stringify(encodeExact(result)))!==record.sha256)
  throw Error('Exact seed metadata did not round-trip');
 return result;
}
function vector(value,length,label){
 if(!(Array.isArray(value)||value instanceof Float64Array)||value.length!==length)
  throw Error('Exact initial seed '+label+' has the wrong complete dimension');
 const bytes=Buffer.allocUnsafe(8*length);
 for(let j=0;j<length;j++){
  if(!Number.isFinite(value[j]))throw Error('Nonfinite initial '+label);
  bytes.writeDoubleLE(value[j],8*j);
 }
 return bytes;
}
function binaryRecord(bytes,shape){
 return {encoding:'Float64LE-base64',shape,byteLength:bytes.length,
  sha256:sha(bytes),base64:bytes.toString('base64')};
}
function recoverBinary(record,shape){
 if(!plain(record)||record.encoding!=='Float64LE-base64'||
     JSON.stringify(record.shape)!==JSON.stringify(shape)||!isSHA(record.sha256)||
     typeof record.base64!=='string')
  throw Error('Invalid complete initial seed binary descriptor');
 const expected=shape.reduce((a,b)=>a*b,1)*8;
 if(!Number.isSafeInteger(expected)||expected<0||expected>=LIMIT||
     record.byteLength!==expected)
  throw Error('Complete initial seed binary size differs');
 const bytes=Buffer.from(record.base64,'base64');
 if(bytes.length!==expected||bytes.toString('base64')!==record.base64||sha(bytes)!==record.sha256)
  throw Error('Complete initial seed binary checksum differs');
 for(let i=0;i<bytes.length;i+=8)
  if(!Number.isFinite(bytes.readDoubleLE(i)))throw Error('Nonfinite encoded initial state');
 return bytes;
}
function dimensions(dn){
 const tail=dn?.tail,parameters=tail?.parameters;
 const M=parameters?.modes,depth=parameters?.depth;
 if(!tail||!plain(parameters)||!Number.isSafeInteger(M)||M<1||
     !Number.isSafeInteger(depth)||depth<1||tail.cells?.length!==depth)
  throw Error('An explicit complete numerical tail is required for an initial seed');
 const stageIdentitySHA=tail.exactStagePersistence?.identitySHA;
 if(!isSHA(stageIdentitySHA))throw Error('An initial seed requires the complete exact-stage identity');
 const rawNode=Array.from(tail.rawNode??[]);
 if(rawNode.length<2||rawNode[0]!==0||rawNode.at(-1)!==depth||
     rawNode.some((value,j)=>!Number.isSafeInteger(value)||value<0||value>depth||
       (j&&value<=rawNode[j-1])))
  throw Error('The complete physical raw-node layout is required');
 if(parameters.physicalDepth!==undefined&&parameters.physicalDepth!==rawNode.length-1)
  throw Error('Physical depth and raw-node layout differ');
 return {tail,parameters,M,K:2*M,depth,N:depth+1,rawNode,stageIdentitySHA};
}
function sourceRecord(sourceIdentity){
 if(!plain(sourceIdentity))throw Error('Complete initial seed source identity is required');
 for(const key of ['workerSHA256','engineSHA256','helperSHA256'])
  if(!isSHA(sourceIdentity[key]))throw Error('Initial seed source identity lacks '+key);
 if(sourceIdentity.helperSHA256!==helperSHA())
  throw Error('Initial seed helper hash differs from the executing helper');
 return exactRecord(sourceIdentity);
}
function jsonEqual(a,b){
 // This is only the ordinary JSON view. Its unavoidable -0 -> +0 loss is
 // repaired from the checksummed authoritative binary/typed metadata above.
 if(a===b)return true;
 if(a===null||b===null||typeof a!=='object'||typeof b!=='object')return false;
 if(Array.isArray(a)!==Array.isArray(b))return false;
 const ka=Object.keys(a).sort(),kb=Object.keys(b).sort();
 return ka.length===kb.length&&ka.every((key,j)=>key===kb[j]&&jsonEqual(a[key],b[key]));
}
const jsonView=value=>JSON.parse(JSON.stringify(value));
function binding(marker){
 return {schema:marker.schema,status:marker.status,numericalSolutionAccepted:marker.numericalSolutionAccepted,
  fullOriginalAcceptanceRequired:marker.fullOriginalAcceptanceRequired,
  call:marker.call,modes:marker.modes,numericalDepth:marker.numericalDepth,
  nodeCount:marker.nodeCount,shapeDimension:marker.shapeDimension,
  stageIdentitySHA:marker.stageIdentitySHA,helperSHA256:marker.helperSHA256,
  originalRawWarmHelperSHA256:marker.originalRawWarmHelperSHA256,
  parametersSHA256:marker.parameters.sha256,sourceIdentitySHA256:marker.sourceIdentity.sha256,
  heightSHA256:marker.height.sha256,statesSHA256:marker.states.sha256,
  rawNodeSHA256:marker.rawNode.sha256};
}
function atomicCreate(file,bytes){
 fs.mkdirSync(path.dirname(file),{recursive:true});
 if(fs.existsSync(file)){
  if(!fs.readFileSync(file).equals(bytes))throw Error('An existing initial seed has different exact bytes');
  return true;
 }
 const temporary=file+'.tmp-'+process.pid+'-'+crypto.randomBytes(8).toString('hex');
 let fd;
 try{
  fd=fs.openSync(temporary,'wx',0o600);fs.writeFileSync(fd,bytes);fs.fsyncSync(fd);fs.closeSync(fd);fd=undefined;
  try{fs.linkSync(temporary,file);}
  catch(error){
   if(error.code!=='EEXIST'||!fs.readFileSync(file).equals(bytes))throw error;
   return true;
  }
  const directory=fs.openSync(path.dirname(file),'r');
  try{fs.fsyncSync(directory);}finally{fs.closeSync(directory);}
  return false;
 }finally{
  if(fd!==undefined)fs.closeSync(fd);
  if(fs.existsSync(temporary))fs.unlinkSync(temporary);
 }
}

export function saveExactInitialSeed({dn,height,states,call,prefix,sourceIdentity}){
 const d=dimensions(dn);
 if(!Number.isSafeInteger(call)||call<1||typeof prefix!=='string'||!prefix)
  throw Error('A positive call number and an explicit initial-seed prefix are required');
 if(!Array.isArray(states)||states.length!==d.N)
  throw Error('No complete initial state was supplied; this helper never constructs a warm guess');
 const heightBytes=vector(height,d.M,'height'),stateBytes=Buffer.allocUnsafe(d.N*d.K*8);
 for(let n=0;n<d.N;n++)vector(states[n],d.K,'state row').copy(stateBytes,n*d.K*8);
 const rawNodeBytes=vector(d.rawNode,d.rawNode.length,'rawNode');
 const marker={schema:SCHEMA,status:STATUS,numericalSolutionAccepted:false,
  fullOriginalAcceptanceRequired:true,call,modes:d.M,numericalDepth:d.depth,
  nodeCount:d.N,shapeDimension:d.K,stageIdentitySHA:d.stageIdentitySHA,
  helperSHA256:helperSHA(),originalRawWarmHelperSHA256:warmSHA(),
  parameters:exactRecord(d.parameters),sourceIdentity:sourceRecord(sourceIdentity),
  height:binaryRecord(heightBytes,[d.M]),states:binaryRecord(stateBytes,[d.N,d.K]),
  rawNode:binaryRecord(rawNodeBytes,[d.rawNode.length])};
 marker.bindingSHA256=sha(JSON.stringify(binding(marker)));
 const rows=states.map(row=>Array.from(row));
 const checkpoint={parameters:d.parameters,states:rows,rawNode:d.rawNode,
  rawStates:d.rawNode.map(n=>rows[n].slice()),cutHeight:Array.from(height),
  scope:'Exact initial warm state before the first complete evaluation. Not accepted, not a residual result, and not a geometric audit.',
  exactInitialSeed:marker};
 // This runs only the frozen complete parameter/raw-node data guard.
 // It neither evaluates a physical stage nor declares numerical convergence.
 preserveExactRawWarm(checkpoint,dn);
 const container={schema:'exact-initial-shooting-seed-container-v1',status:STATUS,
  converged:false,audit:null,numericalSolutionAccepted:false,checkpoint};
 const bytes=zlib.gzipSync(Buffer.from(JSON.stringify(container)+'\n'),{level:6,mtime:0});
 if(bytes.length>=LIMIT)throw Error('The complete initial seed exceeds the repository file limit');
 const file=path.resolve(prefix+'-call'+String(call).padStart(6,'0')+'-initial-seed.json.gz');
 const alreadyStored=atomicCreate(file,bytes);
 return {path:file,sha256:sha(bytes),bytes:bytes.length,call,status:STATUS,
  numericalSolutionAccepted:false,fullOriginalAcceptanceRequired:true,
  stageIdentitySHA:d.stageIdentitySHA,bindingSHA256:marker.bindingSHA256,
  heightSHA256:marker.height.sha256,statesSHA256:marker.states.sha256,
  nodeCount:d.N,shapeDimension:d.K,alreadyStored};
}

export function restoreExactInitialSeed(prior,dn){
 if(!prior||typeof prior!=='object'||!own(prior,'exactInitialSeed'))return prior;
 const marker=prior.exactInitialSeed,d=dimensions(dn);
 if(!plain(marker)||marker.schema!==SCHEMA||marker.status!==STATUS||
     marker.numericalSolutionAccepted!==false||marker.fullOriginalAcceptanceRequired!==true||
     !Number.isSafeInteger(marker.call)||marker.call<1||marker.modes!==d.M||
     marker.numericalDepth!==d.depth||marker.nodeCount!==d.N||marker.shapeDimension!==d.K||
     marker.stageIdentitySHA!==d.stageIdentitySHA||marker.helperSHA256!==helperSHA()||
     marker.originalRawWarmHelperSHA256!==warmSHA())
  throw Error('The marked initial seed has a different status, source, stage identity or dimension');
 if(!isSHA(marker.bindingSHA256)||sha(JSON.stringify(binding(marker)))!==marker.bindingSHA256)
  throw Error('Complete initial seed binding checksum mismatch');
 const parameters=recoverRecord(marker.parameters),sourceIdentity=recoverRecord(marker.sourceIdentity);
 sourceRecord(sourceIdentity);
 const heightBytes=recoverBinary(marker.height,[d.M]);
 const stateBytes=recoverBinary(marker.states,[d.N,d.K]);
 const nodeBytes=recoverBinary(marker.rawNode,[d.rawNode.length]);
 const cutHeight=Array.from({length:d.M},(_,j)=>heightBytes.readDoubleLE(j*8));
 const states=Array.from({length:d.N},(_,n)=>Array.from({length:d.K},
  (_,j)=>stateBytes.readDoubleLE(8*(n*d.K+j))));
 const rawNode=Array.from({length:d.rawNode.length},(_,j)=>nodeBytes.readDoubleLE(j*8));
 if(!rawNode.every((value,j)=>Object.is(value,d.rawNode[j])))
  throw Error('The exact raw-node layout changed');
 const rawStates=rawNode.map(n=>states[n].slice());
 for(const key of ['parameters','states','rawNode','rawStates','cutHeight']){
  const recovered={parameters,states,rawNode,rawStates,cutHeight}[key];
  if(!jsonEqual(jsonView(prior[key]),jsonView(recovered)))
   throw Error('Ordinary checkpoint data contradict authoritative exact initial bytes: '+key);
 }
 const restored={...prior,parameters,states,rawNode,rawStates,cutHeight};
 // Keep the original frozen full non-I/O parameter and raw-state equality gate.
 // The worker still calls its original warm loader and full solver afterwards.
 preserveExactRawWarm(restored,dn);
 return restored;
}
