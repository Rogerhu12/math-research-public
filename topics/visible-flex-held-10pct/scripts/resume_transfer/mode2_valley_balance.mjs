// Rebalance six actual physical valley controls; linear design only.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
const [topic,inputFile,outDir]=process.argv.slice(2);
fs.mkdirSync(outDir,{recursive:true});
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const base=JSON.parse(fs.readFileSync(inputFile,'utf8'));
for(const k of ['initialCheckpoint','designInitialCheckpoint','secantCheckpoint','traceFile'])delete base[k];
const rows=[],cache=new Map();let best=null;
function evaluate(x,label,steps=64){
 const key=JSON.stringify([x,steps]);if(cache.has(key))return cache.get(key);
 const started=Date.now();let row;
 try{
  const cfg=structuredClone(base);x.forEach((v,j)=>cfg.valleyControls[j]=v);
  const tail=createRecalibrationFactory(cfg).assemble();
  const d=diagnosePhysicalMode(tail,2,steps,48,0),g=sampleTailGeometry(tail,24);
  row={controls:x.slice(),label,steps,threshold:d.linearTPositivityAmplitudeThreshold,cutSlope:d.cutSlope,bottleneck:d.thresholdLocation,background:g,seconds:(Date.now()-started)/1000};
  if(!best||row.threshold>best.threshold){best=row;fs.writeFileSync(path.join(outDir,'best-config.json'),JSON.stringify(cfg,null,2)+'\n');}
 }catch(e){row={controls:x.slice(),label,steps,error:String(e),threshold:0,seconds:(Date.now()-started)/1000};}
 rows.push(row);cache.set(key,row);console.log(JSON.stringify(row));
 fs.writeFileSync(path.join(outDir,'record.json'),JSON.stringify({scope:'New physical six-valley designs, globally recalibrated. Finite linear A thresholds and sampled background geometry do not establish nonlinear capacity, same-g refinement, or a closed surface.',source_sha256:createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex'),input_sha256:createHash('sha256').update(fs.readFileSync(inputFile)).digest('hex'),argv:process.argv.slice(2),rows,best},null,2)+'\n');
 return row;
}
for(const seed of [
 [4.5,4.5,5.5,6,6.5,5],
 [5,5,6,6.5,7,6],
 [6,6,7,7.5,8,7],
 [8,8,9,9.5,10,9],
 [6,5,5,5,5,5],
 [8,7,7,7,7,6],
])evaluate(seed,'new six-valley physical design');
for(const step of [1,.5]){
 for(let pass=0;pass<2;pass++){
  const x=best.controls.slice(),old=best.threshold;
  for(let j=0;j<6;j++)for(const sign of [-1,1]){
   const v=x.slice();v[j]+=sign*step;if(v[j]>=0&&v[j]<=14)evaluate(v,`coordinate step ${step}`);
  }
  if(best.threshold<=old*(1+1e-5))break;
 }
}
evaluate(best.controls.slice(),'selected finer physical propagation',192);
