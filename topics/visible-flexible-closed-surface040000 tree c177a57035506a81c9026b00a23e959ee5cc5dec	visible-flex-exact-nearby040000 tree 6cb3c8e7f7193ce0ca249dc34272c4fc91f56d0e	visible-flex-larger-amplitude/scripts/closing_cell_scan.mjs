import fs from 'node:fs/promises';
import {createRecalibrationFactory,physicalM2Column} from './closing_recalibrated_tail.mjs';
const input=process.argv[2],output=process.argv[3],n=+(process.argv[4]??0),steps=+(process.argv[5]??128),mode=process.argv[6]??'original';
if(!input||!output)throw Error('Usage: config.json output.json [cell] [steps] [capMode]');
const config={...JSON.parse(await fs.readFile(input,'utf8')),capMode:mode},factory=createRecalibrationFactory(config),baseline=factory.assemble(),rows=[];
for(let beta=-12;beta<=12;beta+=1){
 try{
  const controls=Array.from({length:factory.parameters.protectCell},(_,i)=>i===n?beta:config.valleyControls?.[i]??0),tail=factory.assemble(controls),z=physicalM2Column(tail.cells[n],steps),row={beta,...z,alpha:tail.stats.alpha,heightSpan:tail.stats.heightSpan,minimumWarpWidth:tail.stats.minimumWarpWidth,rStart:tail.cells[n].rStart,rEnd:tail.cells[n].rEnd};rows.push(row);console.log(JSON.stringify(row));
 }catch(e){const row={beta,error:e.message};rows.push(row);console.log(JSON.stringify(row));}
 await fs.writeFile(output,JSON.stringify({scope:'Single-cell true physical transfer scan, not a calibrated nonlinear tail.',config,baselineStats:baseline.stats,cell:n,steps,rows},null,2)+'\n');
}
