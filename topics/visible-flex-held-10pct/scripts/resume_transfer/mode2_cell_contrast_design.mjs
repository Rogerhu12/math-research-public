// New physical tail designs: vary the balanced-cell contrast, not merely valley controls.
// All reported thresholds are finite linear diagnostics, not nonlinear capacity.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';

const [topic,inputFile,outDir]=process.argv.slice(2);
if(!outDir)throw Error('usage: node mode2_cell_contrast_design.mjs SOURCE_TOPIC INPUT_CONFIG OUT_DIR');
fs.mkdirSync(outDir,{recursive:true});
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const base=JSON.parse(fs.readFileSync(inputFile,'utf8'));
for(const k of ['initialCheckpoint','designInitialCheckpoint','secantCheckpoint','traceFile'])delete base[k];
const rows=[];let best=null;
const hash=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
function save(){fs.writeFileSync(path.join(outDir,'record.json'),JSON.stringify({
  scope:'Distinct physical balanced-cell contrast designs. Full physical transfers and warp recalibration are recomputed. Finite linear thresholds and geometry samples do not prove a nonlinear tail or a closed flexible surface.',
  source_sha256:hash(process.argv[1]),input_sha256:hash(inputFile),argv:process.argv.slice(2),rows,best
},null,2)+'\n');}
function evaluate(contrast,steps,label){
  const started=Date.now();let row;
  try{
    const cfg={...structuredClone(base),prefixR:contrast};
    const tail=createRecalibrationFactory(cfg).assemble();
    const d=diagnosePhysicalMode(tail,2,steps,48,0),g=sampleTailGeometry(tail,32);
    row={contrast,steps,label,threshold:d.linearTPositivityAmplitudeThreshold,
      cutSlope:d.cutSlope,bottleneck:d.thresholdLocation,
      background:g,stats:tail.stats,seconds:(Date.now()-started)/1000};
    if(Number.isFinite(row.threshold)&&row.threshold>0&&(!best||row.threshold>best.threshold)){
      best=row;fs.writeFileSync(path.join(outDir,'best-config.json'),JSON.stringify(cfg,null,2)+'\n');
    }
  }catch(e){row={contrast,steps,label,error:String(e),threshold:0,seconds:(Date.now()-started)/1000};}
  rows.push(row);save();console.log(JSON.stringify(row));return row;
}
for(const contrast of [1.125,1.25,1.5,3,4,8,16])evaluate(contrast,96,'new contrast');
if(best){const chosen=best.contrast;evaluate(chosen,384,'fixed design finer propagation');}
