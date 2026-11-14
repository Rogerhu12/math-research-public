// Opt-in reuse of the saved binary alpha_n, with the pinned physical formulas.
// This is not a recalibration, a new deep source, or a nonlinear-tail solve.
// The original files are read and hash checked; only in-memory copies change.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {gunzipSync} from 'node:zlib';
import {pathToFileURL} from 'node:url';

const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const SELF_SHA=sha(fs.readFileSync(new URL(import.meta.url)));
const REVISION='869436630c99aa5a68afb55bd8877c826034d117';
const PINNED={
  balanced:'928567418f411b70c4040be9ee08be2a78b65e147b8d0c5728f4cf6766a28888',
  base:'4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6',
  weighted:'740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e',
  cells:'d074799099e27401456449343c8f490ec60cdec7eb0d02758f024f541d409575'
};
const DEFAULTS={rCut:1.03,wCut:.05,width:.04,curvatureBound:210,delta0:.006,
  R:64,a:2.75,etaPower:1.5,etaRatioAtN0:.05,orientation:-1,prefixR:8,
  prefixEnd:15,prefixReturnStart:8,protectCell:80,calibrationSteps:1024,
  warpSteps:16,quadratureTolerance:2e-11,slopeCap:0,capTransition:2,
  capMode:'original',cuspAwareQuadrature:true,valleyControls:[],
  rejoinR20At:null,rejoinIndexOffset:4};
const GEOMETRY_KEYS=[...Object.keys(DEFAULTS),'pulseCaps','valleyCaps',
  'warpWeightLevels','flatOuterThroughCell','flatOuterStartSegment','flatSlope'];
const DERIVED_KEYS=['rCuff','oldCut','epsilonScale','prefixRByCell'];
const FIVE=[0,.25,.5,.75,1],SEVEN=[0,.125,.25,.5,.75,.875,1];
const FIELDS=['r','drdx','logw','dlogwdx'];
const MISSING_CAL=['matrix','alphaDerivative','determinant','iterations',
  'gain','targetLowerEntry'];

function equal(a,b){
  if(typeof a==='number'||typeof b==='number')return Object.is(a,b);
  if(a===b)return true;
  if(!a||!b||typeof a!=='object'||typeof b!=='object')return false;
  if(Array.isArray(a)!==Array.isArray(b))return false;
  const ak=Object.keys(a).sort(),bk=Object.keys(b).sort();
  return ak.length===bk.length&&ak.every((k,i)=>k===bk[i]&&equal(a[k],b[k]));
}
function insist(ok,message){if(!ok)throw Error(message);}
function jsonFile(file){
  file=path.resolve(file);const bytes=fs.readFileSync(file);
  const text=(bytes[0]===31&&bytes[1]===139?gunzipSync(bytes):bytes).toString();
  return {file,sha256:sha(bytes),data:JSON.parse(text)};
}
function ready(record){return record.ready??record;}
function normal(input){
  const p={...DEFAULTS,...input};
  p.warpWeightLevels??=[];
  return p;
}
function assertGeometry(candidate,reference,label){
  const a=normal(candidate),b=normal(reference);
  for(const key of GEOMETRY_KEYS)
    insist(equal(a[key],b[key]),label+': frozen geometry differs at '+key);
}

// Read-only preparation. This does not import or construct any tail engine.
export function readFrozenCalibrationReferences(options={}){
  insist(options.ledgerReadyFile,'A saved ready file with all 160 alpha_n is required');
  const ledgerInput=jsonFile(options.ledgerReadyFile),r=ready(ledgerInput.data);
  const model=r.rationalDeepModel,table=r.shallowSourceParameters;
  insist(model?.sourceRevision===REVISION&&model.start===160,
    'The calibration ledger is not the pinned 160-cell head');
  insist(table?.cells?.length===160,'The frozen calibration table must have 160 rows');
  const rows=table.cells.map((v,n)=>{
    insist(v.n===n,'Noncontiguous calibration table at '+n);
    for(const key of ['delta','R','c','lengthScale','alpha'])
      insist(Number.isFinite(v[key])&&v[key]>0,'Invalid saved '+key+' at '+n);
    return {n,delta:v.delta,R:v.R,c:v.c,lengthScale:v.lengthScale,alpha:v.alpha};
  });
  const parameters=model.physicalParameters;
  insist(parameters?.protectCell===160&&parameters.orientation===1&&
    parameters.rejoinR20At===null,'Only the reviewed unrejoined 160-cell head is supported');
  insist(Number.isFinite(model.frozenWarpAlpha)&&model.frozenWarpAlpha>0,
    'The saved global warp alpha is missing');
  insist(model.sourceHashes?.weighted===PINNED.weighted&&
    model.sourceHashes?.cells===PINNED.cells,'The ledger source hashes differ');
  const fingerprints=[{kind:'rational-head',fractions:FIVE,
    expected:model.headFingerprint,input:{file:ledgerInput.file,sha256:ledgerInput.sha256}}];
  const inputs=[{kind:'calibration-ledger',file:ledgerInput.file,sha256:ledgerInput.sha256}];
  for(const file of options.storedReadyFiles??[]){
    const input=jsonFile(file),old=ready(input.data).storedMetricAdapter;
    insist(old?.sourceRevision===REVISION&&old.cellCount===160,
      'Stored ready reference is not the reviewed 160-cell geometry: '+file);
    insist(equal(old.fingerprintFractions,SEVEN)&&equal(old.fingerprintFields,FIELDS),
      'Unexpected stored fingerprint convention: '+file);
    insist(old.profileFingerprintBefore===old.profileFingerprintAfter,
      'The stored reference did not preserve its own original fingerprint');
    insist(Object.is(old.frozenWarpAlpha,model.frozenWarpAlpha),
      'Stored and rational-head references have different global warp alpha');
    insist(old.sourceSHA256?.weighted===PINNED.weighted,'Stored weighted source mismatch');
    assertGeometry(old.physicalParameters,parameters,'Stored reference');
    for(const key of DERIVED_KEYS)
      insist(equal(old.physicalParameters[key],parameters[key]),
        'Stored and rational-head derived parameter differs: '+key);
    fingerprints.push({kind:'stored-head',fractions:SEVEN,
      expected:old.profileFingerprintBefore,input:{file:input.file,sha256:input.sha256}});
    inputs.push({kind:'stored-ready',file:input.file,sha256:input.sha256});
  }
  for(const item of fingerprints)
    insist(/^[0-9a-f]{64}$/.test(item.expected),'Missing historical head fingerprint');
  return {rows,parameters,frozenWarpAlpha:model.frozenWarpAlpha,fingerprints,inputs,
    interpretation:table.interpretation,calibrationTableSHA256:sha(JSON.stringify(rows))};
}

export function profileFingerprint(physical,fractions){
  const hash=crypto.createHash('sha256');
  for(const cell of physical.cells)for(const profile of cell.profiles)
    for(const x of fractions){
      const z=profile(x),values=FIELDS.map(k=>z[k]);
      insist(values.every(Number.isFinite),'A nonfinite profile value cannot be fingerprinted');
      hash.update(JSON.stringify(values)+'\n');
    }
  return hash.digest('hex');
}

// The factory still creates all original far cells, true transfers and graphs.
// Only n<160 calibration calls read saved alpha; n>=160 is the original code.
export async function createFrozenCalibrationFactory(config={},options={}){
  const reference=readFrozenCalibrationReferences(options);
  assertGeometry(config,reference.parameters,'Requested configuration');
  if(config.rationalFrozenWarpAlpha!==undefined)
    insist(Object.is(config.rationalFrozenWarpAlpha,reference.frozenWarpAlpha),
      'Requested rationalFrozenWarpAlpha differs from the saved binary value');
  const topic=path.resolve(options.sourceTopic??process.env.VISIBLE_FLEX_SOURCE_TOPIC??'');
  const origin=JSON.parse(fs.readFileSync(path.join(topic,'source-origin.json'),'utf8'));
  insist(origin.source_revision===REVISION,'Source revision differs from the pinned revision');
  const sourceDir=path.join(topic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
  if(process.env.CLOSING_TAIL_CACHE)
    insist(path.resolve(process.env.CLOSING_TAIL_CACHE)===sourceDir,
      'An existing CLOSING_TAIL_CACHE points to a different source');
  else process.env.CLOSING_TAIL_CACHE=sourceDir;
  const files={balanced:path.join(sourceDir,'tailnext_balanced_tail.mjs'),
    cells:path.join(sourceDir,'general_root_smooth_tail_cells.cjs'),
    base:path.join(topic,'scripts/closing_recalibrated_tail.mjs'),
    weighted:path.join(topic,'scripts/closing_weighted_tail.mjs')};
  const original={},sourceSHA256={};
  for(const [name,file] of Object.entries(files)){
    const bytes=fs.readFileSync(file);sourceSHA256[name]=sha(bytes);
    insist(sourceSHA256[name]===PINNED[name],'Pinned source mismatch: '+file);
    original[name]=bytes.toString();
  }
  // Keep the original complete Git-blob dependency check, including dependencies
  // untouched by this adapter. A different selected cache is refused.
  const loaderFile=path.join(topic,'scripts/closing_tail_sources.mjs');
  const loader=await import(pathToFileURL(loaderFile).href);
  insist(path.resolve(loader.closingTailSourceDirectory)===sourceDir,
    'The original verified loader selected a different dependency directory');
  sourceSHA256.loader=sha(fs.readFileSync(loaderFile));
  const transforms=[];
  function replace(source,module,before,after,recordAfter=after,count=1){
    const actual=source.split(before).length-1;
    insist(actual===count,'Source substitution count differs in '+module+': '+actual);
    transforms.push({module,before,after:recordAfter,count});
    return source.replaceAll(before,after);
  }
  const dataURL=text=>'data:text/javascript;base64,'+Buffer.from(text).toString('base64');
  const helper=`
const __frozenRows=${JSON.stringify(reference.rows)};
const __frozenA=${JSON.stringify(reference.parameters.a)}*Math.log(2);
const __frozenSteps=${JSON.stringify(reference.parameters.calibrationSteps)};
const __frozenReads=[];
function __readFrozenCalibration(index,p,A,steps){
 const row=__frozenRows[index];
 if(!row||row.n!==index||!Object.is(A,__frozenA)||steps!==__frozenSteps)
  throw Error('Frozen calibration identity mismatch at '+index);
 for(const key of ['delta','R','c','lengthScale'])
  if(!Object.is(p[key],row[key]))throw Error('Frozen calibration '+key+' mismatch at '+index);
 const cal={alpha:row.alpha};
 for(const key of ${JSON.stringify(MISSING_CAL)})Object.defineProperty(cal,key,{
  enumerable:false,get(){throw Error('Frozen alpha-only record has no original calibration diagnostic '+key);}});
 __frozenReads.push(index);return Object.freeze(cal);
}
export function __frozenCalibrationReadTrace(){return __frozenReads.slice();}
`;
  let balanced=original.balanced;
  balanced=replace(balanced,'balanced',
    'cal=calibrateBalancedCell({...p,A,steps:calibrationSteps})',
    'cal=(index<160?__readFrozenCalibration(index,p,A,calibrationSteps):calibrateBalancedCell({...p,A,steps:calibrationSteps}))');
  for(const name of ['general_root_smooth_tail_cells.cjs','general_root_tail_momentum.mjs'])
    balanced=replace(balanced,'balanced',"'./"+name+"'",JSON.stringify(pathToFileURL(path.join(sourceDir,name)).href));
  balanced=helper+balanced;
  transforms.push({module:'balanced',operation:'prepend alpha-only checked lookup',
    helperSHA256:sha(helper),tableSHA256:reference.calibrationTableSHA256,
    unavailableDiagnostics:MISSING_CAL});
  const balancedURL=dataURL(balanced),balancedSHA=sha(balanced);
  let base=original.base;
  base=replace(base,'base',
    "const {createBalancedTail}=await loadClosingTailSource('tailnext_balanced_tail.mjs');",
    'import {createBalancedTail} from '+JSON.stringify(balancedURL)+';',
    'import {createBalancedTail} from <transformed-balanced:'+balancedSHA+'>;');
  base=replace(base,'base',"'./closing_tail_sources.mjs'",JSON.stringify(pathToFileURL(loaderFile).href));
  const baseURL=dataURL(base),baseSHA=sha(base);
  let weighted=replace(original.weighted,'weighted',"'./closing_recalibrated_tail.mjs'",
    JSON.stringify(baseURL),'<transformed-base:'+baseSHA+'>',2);
  const weightedURL=dataURL(weighted);
  const balancedModule=await import(balancedURL),before=balancedModule.__frozenCalibrationReadTrace().length;
  const weightedModule=await import(weightedURL),inner=weightedModule.createRecalibrationFactory(config);
  const readTrace=balancedModule.__frozenCalibrationReadTrace().slice(before);
  insist(equal(readTrace,Array.from({length:160},(_,n)=>n)),
    'The adapted factory did not reuse every original shallow cell exactly once');
  insist(inner.source.cells.length===160,'The source head was truncated or extended');
  for(const key of DERIVED_KEYS)
    insist(equal(inner.parameters[key],reference.parameters[key]),
      'Regenerated derived source parameter differs: '+key);
  for(let n=0;n<160;n++)
    insist(Object.is(inner.source.cells[n].cal.alpha,reference.rows[n].alpha),
      'Saved alpha was not retained at '+n);
  const manifest={name:'frozen-binary-calibration-lookup-v1',sourceRevision:REVISION,
    adapterSHA256:SELF_SHA,sourceSHA256,sourceFiles:files,
    transformedSHA256:{balanced:balancedSHA,base:baseSHA,weighted:sha(weighted)},transforms,
    inputs:reference.inputs,calibrationTableSHA256:reference.calibrationTableSHA256,
    reusedCellIndices:readTrace,reusedCalibrationCount:160,
    sourceLinearFarIndex:inner.source.parameters.linearFarIndex,
    originalFarCalibrationCodeRetained:true,originalTransferGraphCodeRetained:true,
    missingCalibrationDiagnostics:MISSING_CAL,frozenWarpAlpha:reference.frozenWarpAlpha,
    matchedGeometryKeys:GEOMETRY_KEYS,matchedDerivedKeys:DERIVED_KEYS,
    profileVerification:[],
    scope:'Saved binary alpha_n only for n<160. All original source cells, far transfers, graphs, physical quadrature and arithmetic order are retained. Global warp alpha is the saved binary datum. No recalibration, truncated head, new deep metric or nonlinear solution.'};
  function verify(physical){
    insist(physical.cells.length===160,'A head fingerprint needs all 160 cells');
    insist(Object.is(physical.stats.alpha,reference.frozenWarpAlpha),'Global warp alpha changed');
    const results=reference.fingerprints.map(item=>{
      const actual=profileFingerprint(physical,item.fractions);
      insist(actual===item.expected,'Historical '+item.kind+' profile fingerprint mismatch');
      return {...item,actual,exactFingerprintMatch:true,cellCount:160,fields:FIELDS};
    });
    manifest.profileVerification=results;return results;
  }
  function assemble(controls=config.valleyControls??[],overrideAlpha=reference.frozenWarpAlpha){
    insist(equal(controls,reference.parameters.valleyControls),
      'Frozen assembly requires the original complete valley controls');
    insist(Object.is(overrideAlpha,reference.frozenWarpAlpha),
      'Frozen assembly requires the saved global warp alpha, including an explicit non-null override');
    const physical=inner.assemble(controls,overrideAlpha);
    verify(physical);return physical;
  }
  return {factory:{...inner,assemble},manifest,reference,verify,
    physicalModeColumn:weightedModule.physicalModeColumn,
    idealModeGraph:weightedModule.idealModeGraph};
}
