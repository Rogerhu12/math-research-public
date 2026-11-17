// One-dimensional physical design screen, not a nonlinear-tail certificate.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
const [topic,configFile,outFile,...betaStrings]=process.argv.slice(2);
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const cfg=JSON.parse(fs.readFileSync(configFile,'utf8'));
delete cfg.initialCheckpoint;delete cfg.traceFile;delete cfg.secantCheckpoint;
const betas=betaStrings.length?betaStrings.map(Number):[2.625,3.125,3.375,3.625,3.875,4.125,4.625];
const rows=[];
for(const beta0 of betas){
 const input={...cfg,valleyControls:[...cfg.valleyControls]};input.valleyControls[0]=beta0;
 const started=Date.now();let row;
 try{
  const tail=createRecalibrationFactory(input).assemble(),d=diagnosePhysicalMode(tail,3,128,48,0),g=sampleTailGeometry(tail,16);
  row={beta0,cutSlope:d.cutSlope,linearAAmplitudeThreshold:d.linearTPositivityAmplitudeThreshold,
       bottleneck:d.thresholdLocation,geometry:g,physicalStatistics:tail.stats,
       seconds:(Date.now()-started)/1000};
 }catch(error){row={beta0,error:String(error),seconds:(Date.now()-started)/1000};}
 rows.push(row);console.log(JSON.stringify(row));
 fs.writeFileSync(outFile,JSON.stringify({scope:'Mode-three linear first-valley physical design screen; not actual nonlinear capacity, closure or fixed-metric convergence.',
     source_sha256:createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex'),
     config_sha256:createHash('sha256').update(fs.readFileSync(configFile)).digest('hex'),
     steps:128,far:48,rows},null,2)+'\n');
}
