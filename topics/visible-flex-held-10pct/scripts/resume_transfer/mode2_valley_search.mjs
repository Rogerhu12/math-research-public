// Finite physical mode-two design. No nonlinear capacity or closure assertion.
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
const rows=[];let best=null;const cache=new Map();
function cfgFor(x){const c=structuredClone(base);for(let j=0;j<3;j++)c.valleyControls[j]=x[j];return c;}
function evaluate(x,label,steps=48){
 const key=JSON.stringify([x,steps]);if(cache.has(key))return cache.get(key);
 const start=Date.now();let row;
 try{const c=cfgFor(x),tail=createRecalibrationFactory(c).assemble(),d=diagnosePhysicalMode(tail,2,steps,48,0);
 row={controls:x.slice(),label,steps,threshold:d.linearTPositivityAmplitudeThreshold,cutSlope:d.cutSlope,bottleneck:d.thresholdLocation,seconds:(Date.now()-start)/1000};
 if(!best||row.threshold>best.threshold){const g=sampleTailGeometry(tail,24);row.background=g;best=row;fs.writeFileSync(path.join(outDir,'best-config.json'),JSON.stringify(c,null,2)+'\n');}
 }catch(e){row={controls:x.slice(),label,steps,error:String(e),threshold:0,seconds:(Date.now()-start)/1000};}
 rows.push(row);cache.set(key,row);console.log(JSON.stringify(row));
 fs.writeFileSync(path.join(outDir,'record.json'),JSON.stringify({scope:'Actual mode-two linear design under new physical first-three-valley controls. All candidate metrics differ. No nonlinear-tail or amplitude claim.',source_sha256:createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex'),input_sha256:createHash('sha256').update(fs.readFileSync(inputFile)).digest('hex'),argv:process.argv.slice(2),rows,best},null,2)+'\n');
 return row;
}
const initial=base.valleyControls.slice(0,3);
for(const seed of [initial,[4.125,1,0],[5.125,2,1],[6.125,3,2],[7.125,4,3],[5.125,4,1],[4.125,-1,0]])evaluate(seed,'new physical seed');
for(const step of [1,.5,.25,.125]){
 for(let round=0;round<3;round++){
  const old=best.threshold;const x=best.controls.slice();
  for(let j=0;j<3;j++)for(const sign of [-1,1]){const y=x.slice();y[j]+=sign*step;if(y[j]>=-3&&y[j]<=12)evaluate(y,`coordinate ${step}`);}
  for(const sign of [-1,1])evaluate(x.map(v=>v+sign*step),`joint ${step}`);
  if(best.threshold<=old*(1+1e-5))break;
 }
}
const selected=best.controls.slice();evaluate(selected,'selected finer physical propagation',128);
