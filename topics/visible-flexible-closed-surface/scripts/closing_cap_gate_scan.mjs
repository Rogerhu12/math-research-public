import fs from 'node:fs/promises';
import {createRecalibrationFactory,diagnosePhysicalMode} from './closing_recalibrated_tail.mjs';
const input=process.argv[2],output=process.argv[3],mode=+(process.argv[4]??3),steps=+(process.argv[5]??96),far=+(process.argv[6]??32),rows=[];
if(!input||!output)throw Error('Usage: config.json output.json [mode] [steps] [far]');
const config=JSON.parse(await fs.readFile(input,'utf8'));
for(const number of [1,2,3])for(const peak of [.04,.06,.08,.1,.12,.16,.2]){
 const c={...config,pulseCaps:Array.from({length:number},()=>[peak,peak]),valleyCaps:Array(number).fill(peak),maxCachedBetas:2};let row;
 try{const tail=createRecalibrationFactory(c).assemble(),z=diagnosePhysicalMode(tail,mode,steps,far);row={number,peak,threshold:z.linearTPositivityAmplitudeThreshold,gradientThreshold:z.gradientAmplitudeThreshold,cutSlope:z.cutSlope,where:z.thresholdLocation,cellThresholds:z.cellThresholds.slice(0,8).map(v=>v.threshold),stats:tail.stats,config:c};}
 catch(e){row={number,peak,error:e.message};}
 rows.push(row);console.log(JSON.stringify({...row,config:undefined,cellThresholds:undefined}));await fs.writeFile(output,JSON.stringify({scope:'Finite changed metrics; sampled physical mode gate scan. No nonlinear claim.',input,mode,steps,far,rows},null,2)+'\n');
}
