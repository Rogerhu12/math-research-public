// Linear per-harmonic margins at a recorded H vector; no nonlinear claim.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,recordFile,outFile,...betas]=process.argv.slice(2);
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory,diagnosePhysicalMode}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const record=JSON.parse(gunzipSync(fs.readFileSync(recordFile))),rows=[];
if(!record.response?.converged)throw Error('Expected an accepted old source response');
const heights=record.response.checkpoint.cutHeight,cfg=record.config;
for(const beta0 of betas.map(Number)){
 const input={...cfg,valleyControls:[...cfg.valleyControls]};input.valleyControls[0]=beta0;
 const tail=createRecalibrationFactory(input).assemble(),harmonics=[];
 for(let j=0;j<heights.length;j++){
  const mode=cfg.spacing*(j+1),d=diagnosePhysicalMode(tail,mode,128,48,0);
  harmonics.push({mode,cutHeight:heights[j],cutSlope:d.cutSlope,
   linearAAmplitudeThreshold:d.linearTPositivityAmplitudeThreshold,
   amplitudeToThreshold:Math.abs(heights[j])/d.linearTPositivityAmplitudeThreshold,
   location:d.thresholdLocation});
 }
 const row={beta0,harmonics,triangleRatio:harmonics.reduce((sum,h)=>sum+h.amplitudeToThreshold,0)};
 rows.push(row);console.log(JSON.stringify(row));
 fs.writeFileSync(outFile,JSON.stringify({scope:'Sampled separate linear harmonic margins; triangleRatio < 1 is only a sufficient sampled condition for the linear height lift. Neither a nonlinear solution nor a nonlinear obstruction follows.',
  source_sha256:createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex'),
  input_sha256:createHash('sha256').update(fs.readFileSync(recordFile)).digest('hex'),steps:128,far:48,rows},null,2)+'\n');
}
