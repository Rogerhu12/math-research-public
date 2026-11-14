// Persist already computed full shooting-flow Jacobians for warm prediction.
// Storage and identity checks only: this module does not import a tail engine,
// evaluate a root/ODE/Jacobian, create a predictor, or accept a new solution.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';

const SCHEMA='full-shooting-flow-tangent-storage-v1';
const FORMAT='Float64LE-row-major-gzip-v1';
const MAX_FILE_BYTES=5_000_000;
const DEFAULT_RAW_CHUNK_BYTES=2_000_000;
// The exact same four output/warm path keys are excluded by the existing
// preserveExactRawWarm adapter. Every other parameter remains bound.
const IO_KEYS=new Set(['traceFile','iterationCheckpointFile','trialDiagnosticFile','initialCheckpoint']);
const HELPER_SHA256=crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex');
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
const fail=message=>{throw Error('Full-flow tangent storage: '+message);};
const numericArray=value=>Array.isArray(value)||(ArrayBuffer.isView(value)&&!(value instanceof DataView));

function finiteVector(value,length,name){
  if(!numericArray(value)||value.length!==length)fail(name+' has the wrong complete dimension');
  for(let j=0;j<length;j++)if(typeof value[j]!=='number'||!Number.isFinite(value[j]))
    fail(name+' contains a nonfinite/non-numeric entry at '+j);
  return value;
}

function numberHex(value){
  if(!Number.isFinite(value))fail('nonfinite identity number');
  const bytes=Buffer.allocUnsafe(8);bytes.writeDoubleLE(value);return bytes.toString('hex');
}

// An injective typed JSON-data encoding with the exact binary64 number bits.
// Undefined object properties are absent, as in the existing JSON checkpoints;
// undefined array entries and all executable/non-JSON values are rejected.
function identityTree(value){
  if(value===null)return ['null'];
  if(typeof value==='number')return ['f64le',numberHex(value)];
  if(typeof value==='string')return ['string',value];
  if(typeof value==='boolean')return ['boolean',value];
  if(numericArray(value))return ['array',Array.from(value,identityTree)];
  if(typeof value==='object'){
    const proto=Object.getPrototypeOf(value);
    if(proto!==Object.prototype&&proto!==null)fail('identity must contain only plain JSON data');
    return ['object',Object.keys(value).sort().filter(key=>value[key]!==undefined)
      .map(key=>[key,identityTree(value[key])])];
  }
  fail('unsupported identity value of type '+typeof value);
}

const canonical=value=>JSON.stringify(identityTree(value));

function equationParameters(parameters){
  if(!parameters||typeof parameters!=='object'||Array.isArray(parameters))
    fail('complete original tail parameters required');
  return Object.fromEntries(Object.entries(parameters).filter(([key])=>!IO_KEYS.has(key)));
}

function sourceMap(sourceSha256){
  if(!sourceSha256||typeof sourceSha256!=='object'||Array.isArray(sourceSha256))
    fail('a complete frozen-source SHA map is required');
  const result={};
  for(const key of Object.keys(sourceSha256).sort()){
    if(typeof sourceSha256[key]!=='string'||!/^[a-f0-9]{64}$/.test(sourceSha256[key]))
      fail('invalid frozen-source SHA for '+key);
    result[key]=sourceSha256[key];
  }
  for(const name of ['78718-tail-tangent-core.mjs','78718-tail-tangent-split.mjs',
                     '78718-tail-tangent-predictor.mjs'])
    if(!Object.keys(result).some(key=>key.endsWith(name)))fail('missing frozen source '+name);
  return result;
}

function nonemptyData(value,name){
  if(value===undefined||value===null||(typeof value==='object'&&!Object.keys(value).length))
    fail(name+' must explicitly identify the original physical/backend data');
  canonical(value);return value;
}

function dimensions(identity){
  const M=identity?.parameters?.modes,depth=identity?.parameters?.depth,K=2*M;
  if(!Number.isSafeInteger(M)||M<1||!Number.isSafeInteger(depth)||depth<1||
     !Number.isSafeInteger(depth*K*K))fail('invalid complete tail dimensions');
  if(!Number.isFinite(identity.radius)||identity.radius<=0)fail('invalid physical cut radius');
  finiteVector(identity.farGraph,M,'farGraph');
  const raw=identity.rawNode;
  if(!numericArray(raw)||raw.length<2||raw[0]!==0||raw.at(-1)!==depth||
     Array.from(raw).some((n,j)=>!Number.isSafeInteger(n)||n<0||n>depth||(j&&n<=raw[j-1])))
    fail('complete strictly ordered rawNode map required');
  if(identity.parameters.physicalDepth!==undefined&&raw.length!==identity.parameters.physicalDepth+1)
    fail('rawNode count differs from original physical depth');
  if(!Array.isArray(identity.stageLayout)||identity.stageLayout.length!==depth)
    fail('complete original stage layout required');
  sourceMap(identity.sourceSha256);
  nonemptyData(identity.physicalIdentity,'physicalIdentity');
  nonemptyData(identity.backendIdentity,'backendIdentity');
  canonical(identity);
  return {M,K,depth,nodes:depth+1};
}

/** Read numerical metadata only; do not call any engine/profile function. */
export function describeTailTangentIdentity({dn,radius,sourceSha256,physicalIdentity,backendIdentity}){
  const tail=dn?.tail;
  if(!tail?.parameters||!Array.isArray(tail.cells)||!tail.graphs?.length||!tail.rawNode)
    fail('the original complete DN tail metadata is required');
  const keys=['rawCell','rawSegment','rawLeft','rawRight','part','parts','portRatio','mu'];
  const stageLayout=tail.cells.map((cell,index)=>{
    const row={stage:index};
    for(const key of keys){
      if(typeof cell[key]!=='number'||!Number.isFinite(cell[key]))fail('stage '+index+' lacks '+key);
      row[key]=cell[key];
    }
    if(!Array.isArray(cell.profiles)||!cell.profiles.length)fail('missing original stage profiles');
    row.profileIntegrationBreakpoints=cell.profiles.map(profile=>{
      const points=profile.integrationBreakpoints??[];
      finiteVector(points,points.length,'stage integration breakpoints');
      return Array.from(points);
    });
    return row;
  });
  const identity={parameters:equationParameters(tail.parameters),rawNode:Array.from(tail.rawNode),stageLayout,
    farGraph:Array.from(tail.graphs.at(-1)),radius,sourceSha256:sourceMap(sourceSha256),
    physicalIdentity:nonemptyData(physicalIdentity,'physicalIdentity'),
    backendIdentity:nonemptyData(backendIdentity,'backendIdentity')};
  dimensions(identity);return identity;
}

function completeStates(states,{nodes,K},name){
  if(!Array.isArray(states)||states.length!==nodes)fail(name+' must retain every shooting node');
  for(let n=0;n<nodes;n++)finiteVector(states[n],K,name+'['+n+']');
  return states;
}

function checkpointNumericJSON(states,height,rawNode){
  // This is precisely the finite-number representation used by the original
  // JSON checkpoint. Signed zero is restored separately from the binary seed.
  return JSON.stringify({states:states.map(row=>Array.from(row)),
    cutHeight:Array.from(height),rawNode:Array.from(rawNode)});
}

function encodeVectors(vectors){
  const count=vectors.reduce((sum,row)=>sum+row.length,0);
  if(!Number.isSafeInteger(count)||count<1)fail('invalid binary payload length');
  const bytes=Buffer.allocUnsafe(count*8);let at=0;
  for(const row of vectors)for(const value of row){
    if(typeof value!=='number'||!Number.isFinite(value))fail('binary payload contains a nonfinite value');
    bytes.writeDoubleLE(value,at);at+=8;
  }
  return bytes;
}

function writeDataFile(filename,raw,extra={}){
  const compressed=zlib.gzipSync(raw,{level:6});
  if(compressed.length>=MAX_FILE_BYTES)fail('compressed data file exceeds the strict per-file limit');
  fs.writeFileSync(filename,compressed,{flag:'wx'});
  return {file:path.basename(filename),encoding:FORMAT,bytes:compressed.length,
    rawBytes:raw.length,sha256:sha(compressed),rawSha256:sha(raw),...extra};
}

function readDataFile(directory,record,expectedBytes){
  if(!record||record.encoding!==FORMAT||typeof record.file!=='string'||
     path.basename(record.file)!==record.file||record.file==='.'||record.file==='..'||
     !record.file.endsWith('.f64le.gz'))fail('invalid binary sidecar reference');
  if(!Number.isSafeInteger(expectedBytes)||expectedBytes<8||record.rawBytes!==expectedBytes||
     !Number.isSafeInteger(record.bytes)||record.bytes<1||record.bytes>=MAX_FILE_BYTES)
    fail('binary sidecar dimensions or size limit differ');
  const filename=path.join(directory,record.file),stat=fs.statSync(filename);
  if(!stat.isFile()||stat.size!==record.bytes)fail('binary sidecar file size differs');
  const compressed=fs.readFileSync(filename);
  if(sha(compressed)!==record.sha256)fail('compressed sidecar SHA differs');
  const raw=zlib.gunzipSync(compressed,{maxOutputLength:expectedBytes});
  if(raw.length!==expectedBytes||sha(raw)!==record.rawSha256)fail('complete Float64LE payload differs');
  return raw;
}

/** Save existing converged-solution flows; no new numerical evaluation. */
export function writeFullFlowTangentSnapshot({outPrefix,solution,cutHeight,identity,
    solveTolerance,maxRawChunkBytes=DEFAULT_RAW_CHUNK_BYTES}){
  const d=dimensions(identity),{M,K,depth,nodes}=d;
  if(solution?.converged!==true||!Number.isFinite(solution.normalizedResidual)||
     !Number.isFinite(solveTolerance)||solveTolerance<=0||!(solution.normalizedResidual<solveTolerance))
    fail('only a response passing the original strict solve tolerance can seed a predictor');
  if(canonical(equationParameters(solution.parameters))!==canonical(identity.parameters))
    fail('solution parameters differ from the live original DN');
  completeStates(solution.states,d,'solution states');finiteVector(cutHeight,M,'complete physical H');
  const flows=solution.linearizedFlowJacobians;
  if(!Array.isArray(flows)||flows.length!==depth)fail('all original variational stage flows must already exist');
  for(let n=0;n<depth;n++)finiteVector(flows[n],K*K,'flow Jacobian '+n);
  if(!Number.isSafeInteger(maxRawChunkBytes)||maxRawChunkBytes<K*K*8||maxRawChunkBytes>4_000_000)
    fail('chunk size must fit one full stage and remain at most4,000,000 raw bytes');
  if(typeof outPrefix!=='string'||!outPrefix.length)fail('fresh output prefix required');
  const prefix=path.resolve(outPrefix),directory=path.dirname(prefix);
  const manifestPath=prefix+'-manifest.json.gz',seedPath=prefix+'-base.f64le.gz';
  const stagesPerChunk=Math.floor(maxRawChunkBytes/(K*K*8));
  const count=Math.ceil(depth/stagesPerChunk);
  const chunkPaths=Array.from({length:count},(_,j)=>prefix+'-flow-'+String(j).padStart(4,'0')+'.f64le.gz');
  fs.mkdirSync(directory,{recursive:true});
  for(const filename of [manifestPath,seedPath,...chunkPaths])
    if(fs.existsSync(filename))fail('refusing to overwrite existing snapshot file '+filename);
  // A small binary seed preserves every base state/H bit, including -0.
  // The original JSON checkpoint remains independently bound in full.
  const seed=encodeVectors([...solution.states,cutHeight,identity.farGraph,[identity.radius],identity.rawNode]);
  const seedRecord=writeDataFile(seedPath,seed,{layout:['states[node][Q_then_pi]','physical_H',
    'farGraph','radius','rawNode'],counts:{states:nodes*K,physicalH:M,farGraph:M,radius:1,rawNode:identity.rawNode.length}});
  const chunks=[];
  for(let j=0,first=0;first<depth;j++,first+=stagesPerChunk){
    const stop=Math.min(depth,first+stagesPerChunk);
    const raw=encodeVectors(flows.slice(first,stop));
    chunks.push(writeDataFile(chunkPaths[j],raw,{firstStage:first,stageCount:stop-first,
      shape:[stop-first,K,K],matrixLayout:'row-major',components:'all Q and pi inputs/outputs'}));
  }
  const identityCanonical=canonical(identity);
  const manifest={schema:SCHEMA,complete:true,helperSha256:HELPER_SHA256,
    createdUTC:new Date().toISOString(),dimensions:{modes:M,stateDimension:K,stages:depth,nodes},
    identityEncoding:'typed-JSON-with-exact-Float64LE-numbers-v1',identityCanonical,
    identitySha256:sha(Buffer.from(identityCanonical)),
    checkpointNumericJSONSha256:sha(Buffer.from(checkpointNumericJSON(solution.states,cutHeight,identity.rawNode))),
    checkpointZeroConvention:'Original finite-number JSON comparison; all original signed-zero bits are restored from base binary seed.',
    convergedBaseResidual:solution.normalizedResidual,originalSolveTolerance:solveTolerance,
    baseHadAudit:solution.audit!==undefined&&solution.audit!==null,
    base:seedRecord,chunks,rawFlowBytes:depth*K*K*8,
    allStageFlowJacobiansRetained:true,allBaseStatesAndHeightsRetained:true,
    nonlinearSolvePerformedByStorage:false,newTargetAccepted:false,
    scope:'Warm predictor storage only. Original full nonlinear residual, Newton, positivity, full Jacobian and requested audit remain authoritative.'};
  const bytes=zlib.gzipSync(Buffer.from(JSON.stringify(manifest)+'\n'),{level:6});
  if(bytes.length>=MAX_FILE_BYTES)fail('snapshot manifest exceeds the strict per-file limit');
  // Publish complete manifest last. A partial failure leaves diagnostics and
  // never creates a manifest claiming that missing chunks are complete.
  fs.writeFileSync(manifestPath,bytes,{flag:'wx'});
  return {schema:SCHEMA,manifestPath,manifestSha256:sha(bytes),manifestBytes:bytes.length,
    chunks:chunks.length,rawFlowBytes:manifest.rawFlowBytes,baseRawBytes:seed.length,
    helperSha256:HELPER_SHA256,newTargetAccepted:false};
}

/** Restore exact prior bits and flows for the unchanged original factory. */
export function readFullFlowTangentSnapshot({manifestPath,checkpoint,identity,manifestSha256}){
  const d=dimensions(identity),{M,K,depth,nodes}=d;
  if(typeof manifestPath!=='string'||!manifestPath.length)fail('snapshot manifest path required');
  const filename=path.resolve(manifestPath),stat=fs.statSync(filename);
  if(!stat.isFile()||stat.size<1||stat.size>=MAX_FILE_BYTES)fail('manifest file size limit differs');
  const compressed=fs.readFileSync(filename),manifestHash=sha(compressed);
  if(typeof manifestSha256!=='string'||!/^[a-f0-9]{64}$/.test(manifestSha256)||manifestHash!==manifestSha256)
    fail('the enclosing checkpoint must supply the exact snapshot manifest SHA');
  const manifest=JSON.parse(zlib.gunzipSync(compressed,{maxOutputLength:32_000_000}).toString('utf8'));
  if(manifest.schema!==SCHEMA||manifest.complete!==true||manifest.helperSha256!==HELPER_SHA256||
     manifest.identityEncoding!=='typed-JSON-with-exact-Float64LE-numbers-v1'||
     manifest.nonlinearSolvePerformedByStorage!==false||manifest.newTargetAccepted!==false)
    fail('manifest schema/source/scope differs');
  const actualCanonical=canonical(identity);
  if(manifest.identityCanonical!==actualCanonical||manifest.identitySha256!==sha(Buffer.from(actualCanonical)))
    fail('full original tail/physical/backend/source identity differs');
  const md=manifest.dimensions;
  if(md?.modes!==M||md.stateDimension!==K||md.stages!==depth||md.nodes!==nodes||
     !Number.isFinite(manifest.convergedBaseResidual)||!Number.isFinite(manifest.originalSolveTolerance)||
     !(manifest.originalSolveTolerance>0)||!(manifest.convergedBaseResidual<manifest.originalSolveTolerance))
    fail('base dimensions or original convergence evidence differ');
  if(!checkpoint||canonical(equationParameters(checkpoint.parameters))!==canonical(identity.parameters)||
     canonical(checkpoint.rawNode)!==canonical(identity.rawNode))
    fail('checkpoint parameters or complete raw-node map differ');
  completeStates(checkpoint.states,d,'checkpoint states');finiteVector(checkpoint.cutHeight,M,'checkpoint complete H');
  if(sha(Buffer.from(checkpointNumericJSON(checkpoint.states,checkpoint.cutHeight,identity.rawNode)))!==manifest.checkpointNumericJSONSha256)
    fail('complete checkpoint base states/H differ');
  if(checkpoint.rawStates!==undefined){
    if(!Array.isArray(checkpoint.rawStates)||checkpoint.rawStates.length!==identity.rawNode.length)
      fail('checkpoint raw-state copy dimensions differ');
    for(let j=0;j<identity.rawNode.length;j++)
      if(canonical(checkpoint.rawStates[j])!==canonical(checkpoint.states[identity.rawNode[j]]))
        fail('checkpoint raw-state copy differs from the full node array');
  }
  const count=nodes*K+M+M+1+identity.rawNode.length;
  const counts=manifest.base?.counts;
  if(!counts||counts.states!==nodes*K||counts.physicalH!==M||counts.farGraph!==M||
     counts.radius!==1||counts.rawNode!==identity.rawNode.length)
    fail('binary base-seed layout differs');
  const directory=path.dirname(filename),seed=readDataFile(directory,manifest.base,count*8);
  let at=0;
  const take=length=>{
    const out=new Float64Array(length);
    for(let j=0;j<length;j++){
      const value=seed.readDoubleLE(at);at+=8;
      if(!Number.isFinite(value))fail('nonfinite original base binary value');out[j]=value;
    }
    return out;
  };
  const states=Array.from({length:nodes},()=>Array.from(take(K)));
  const baseHeight=Array.from(take(M)),farGraph=take(M),radius=take(1)[0],rawNode=Array.from(take(identity.rawNode.length));
  if(at!==seed.length||canonical(farGraph)!==canonical(identity.farGraph)||
     !Object.is(radius,identity.radius)||canonical(rawNode)!==canonical(identity.rawNode)||
     sha(Buffer.from(checkpointNumericJSON(states,baseHeight,rawNode)))!==manifest.checkpointNumericJSONSha256)
    fail('binary base seed is not bound to the same full checkpoint/identity');
  if(!Array.isArray(manifest.chunks)||!manifest.chunks.length||manifest.rawFlowBytes!==depth*K*K*8||
     manifest.allStageFlowJacobiansRetained!==true||manifest.allBaseStatesAndHeightsRetained!==true)
    fail('complete variational-flow manifest required');
  const flows=Array(depth);let first=0;
  for(const chunk of manifest.chunks){
    if(chunk.firstStage!==first||!Number.isSafeInteger(chunk.stageCount)||chunk.stageCount<1||
       first+chunk.stageCount>depth||canonical(chunk.shape)!==canonical([chunk.stageCount,K,K])||
       chunk.matrixLayout!=='row-major')fail('gap, overlap or changed dimensions in complete flow chunks');
    const raw=readDataFile(directory,chunk,chunk.stageCount*K*K*8);let offset=0;
    for(let n=0;n<chunk.stageCount;n++){
      const matrix=new Float64Array(K*K);
      for(let j=0;j<K*K;j++){
        const value=raw.readDoubleLE(offset);offset+=8;
        if(!Number.isFinite(value))fail('nonfinite original flow Jacobian');matrix[j]=value;
      }
      flows[first+n]=matrix;
    }
    if(offset!==raw.length)fail('unconsumed flow binary values');first+=chunk.stageCount;
  }
  if(first!==depth)fail('missing variational stages');
  return {solution:{converged:true,states,linearizedFlowJacobians:flows,
      parameters:identity.parameters,normalizedResidual:manifest.convergedBaseResidual},
    farGraph:Array.from(farGraph),radius,baseHeight,manifest,
    diagnostics:{schema:SCHEMA,manifestPath:filename,manifestSha256:manifestHash,
      completeFrozenIdentityMatched:true,completeCheckpointNumericJSONMatched:true,
      allOriginalBaseFloat64BitsRestored:true,allOriginalFlowFloat64BitsRestored:true,
      modes:M,stages:depth,rawFlowBytes:manifest.rawFlowBytes,
      noNewRootODEJacobianOrPredictorEvaluation:true,newTargetAccepted:false}};
}
