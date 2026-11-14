// Geometry-only check against archived five- and seven-fraction fingerprints.
// The constructor retains its original auxiliary one-mode source graphs.
// No physical-tail stable graph, nonlinear DN, BVP or accepted surface is computed.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {parseArgs} from 'node:util';
import {pathToFileURL} from 'node:url';
import {createFrozenCalibrationFactory,profileFingerprint} from './strong_frozen_calibration_factory.mjs';

const {values}=parseArgs({options:{'source-topic':{type:'string'},config:{type:'string'},
  'ledger-ready':{type:'string'},'stored-ready':{type:'string',multiple:true},
  out:{type:'string'},'compare-original':{type:'boolean',default:false}}});
for(const key of ['source-topic','config','ledger-ready','out'])
  if(!values[key])throw Error('Missing --'+key);
if(fs.existsSync(values.out))throw Error('Refusing to replace '+values.out);
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const sourceSHA=sha(fs.readFileSync(new URL(import.meta.url)));
const configBytes=fs.readFileSync(values.config),config=JSON.parse(configBytes);
const started=Date.now();
const result={scope:'Geometry-only frozen-calibration reuse check; no nonlinear solve or accepted surface.',
  finished:false,nonlinearSolution:false,configFile:path.resolve(values.config),
  configSHA256:sha(configBytes),checkSHA256:sourceSHA,compareOriginal:values['compare-original']};
function save(){
  const file=path.resolve(values.out),temp=file+'.tmp';
  fs.writeFileSync(temp,JSON.stringify(result,null,2)+'\n');fs.renameSync(temp,file);
}
try{
  console.log('frozen-calibration-check: loading saved 160-cell alpha table',new Date().toISOString());
  const adapted=await createFrozenCalibrationFactory(config,{
    sourceTopic:values['source-topic'],ledgerReadyFile:values['ledger-ready'],
    storedReadyFiles:values['stored-ready']??[]});
  console.log('frozen-calibration-check: source complete; original physical assembly begins',new Date().toISOString());
  const physical=adapted.factory.assemble();
  result.manifest=adapted.manifest;
  result.stats=physical.stats;
  result.geometryOnlySourceConstructorStillBuiltOriginalFarGraphs=true;
  let missingRejected=0;
  for(const key of adapted.manifest.missingCalibrationDiagnostics){
    try{void physical.source.cells[0].cal[key];}
    catch(error){
      if(!String(error).includes('Frozen alpha-only record'))throw error;
      missingRejected++;continue;
    }
    throw Error('Unavailable calibration diagnostic did not reject access: '+key);
  }
  result.unavailableCalibrationDiagnosticReadsRejected=missingRejected;
  if(values['compare-original']){
    console.log('frozen-calibration-check: optional original full recalibration begins',new Date().toISOString());
    const originalModule=await import(pathToFileURL(path.join(path.resolve(values['source-topic']),
      'scripts/closing_weighted_tail.mjs')).href);
    const originalFactory=originalModule.createRecalibrationFactory(config);
    const original=originalFactory.assemble();
    if(!Object.is(original.stats.alpha,adapted.reference.frozenWarpAlpha))
      throw Error('Original global warp alpha differs from the archived binary value');
    let binaryComparisons=0;
    for(let n=0;n<160;n++){
      if(!Object.is(original.source.cells[n].cal.alpha,adapted.reference.rows[n].alpha))
        throw Error('Original alpha differs at cell '+n);
      for(let j=0;j<physical.cells[n].profiles.length;j++)
        for(const x of [0,.125,.25,.5,.75,.875,1]){
          const a=physical.cells[n].profiles[j](x),b=original.cells[n].profiles[j](x);
          for(const key of ['r','drdx','logw','dlogwdx']){
            if(!Object.is(a[key],b[key]))throw Error('Direct binary profile mismatch: '+[n,j,x,key]);
            binaryComparisons++;
          }
        }
    }
    result.originalComparison={binaryComparisons,allProfileValuesObjectIsEqual:true,
      calibrationBinaryEqualCount:160,globalWarpAlphaObjectIsEqual:true,
      fingerprints:adapted.reference.fingerprints.map(item=>({kind:item.kind,
        fractions:item.fractions,expected:item.expected,
        original:profileFingerprint(original,item.fractions)}))};
  }
  result.finished=true;result.wallSeconds=(Date.now()-started)/1000;
  result.memory=process.memoryUsage();save();
  console.log(JSON.stringify({finished:true,nonlinearSolution:false,
    calibrationCount:160,fingerprints:result.manifest.profileVerification.map(v=>({kind:v.kind,match:v.exactFingerprintMatch})),
    wallSeconds:result.wallSeconds,memory:result.memory}));
}catch(error){
  result.wallSeconds=(Date.now()-started)/1000;
  result.error=String(error?.stack??error).replace(/data:text\/javascript;base64,[A-Za-z0-9+/=]+/g,'<frozen-calibration-module>');
  save();console.error(result.error);process.exitCode=1;
}
