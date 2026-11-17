// Finite complete linear propagation used only to rank physical designs.
// Its first variation of A is NOT a nonlinear amplitude or existence bound.
import fs from'node:fs';import path from'node:path';import{pathToFileURL}from'node:url';import{createHash}from'node:crypto';
const[topic,factoryFile,configFile,out,stepsArg='128',modesArg='8']=process.argv.slice(2),steps=Number(stepsArg),M=Number(modesArg);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;process.env.CLOSING_TAIL_CACHE=path.join(topic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const{createRecalibrationFactory}=await import(pathToFileURL(factoryFile));
const{diagnosePhysicalMode}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const cfg=JSON.parse(fs.readFileSync(configFile)),physical=createRecalibrationFactory(cfg).assemble(),rows=[],hash=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
for(let k=1;k<=M;k++){
 const mode=2*k,d=diagnosePhysicalMode(physical,mode,steps,48),sensitivity=1/d.linearTPositivityAmplitudeThreshold;
 rows.push({mode,cutD:d.cutSlope,leadingSensitivityPerUnitCutHeight:sensitivity,worst:d.thresholdLocation,firstEightCells:d.cellThresholds.slice(0,8).map((r,n)=>({cell:n,sensitivity:1/r.threshold,where:r.where})),heightSensitivity:d.normalizedHeightMax,radialDerivativeSensitivity:d.normalizedDerivativeMax});
 fs.writeFileSync(out,JSON.stringify({scope:'Sampled finite full-stage linear first variation of A. Used for ranking only, not as a nonlinear capacity or nonexistence criterion.',steps,far:48,baseMode:2,config:configFile,config_sha256:hash(configFile),factory:factoryFile,factory_sha256:hash(factoryFile),stats:physical.stats,rows},null,2)+'\n');
 console.log(JSON.stringify({mode,D:d.cutSlope,sensitivity,worstCell:d.thresholdLocation.cell,worstSegment:d.thresholdLocation.segment}));
}
