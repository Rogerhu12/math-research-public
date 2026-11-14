import fs from 'node:fs/promises';
import {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry} from './closing_weighted_tail.mjs';
const input=process.argv[2],output=process.argv[3],mode=+(process.argv[4]??3),steps=+(process.argv[5]??96),far=+(process.argv[6]??32),rows=[];
if(!input||!output)throw Error('Usage: config.json output.json [mode] [steps] [far]');
const config=JSON.parse(await fs.readFile(input,'utf8'));let best=null;
const firsts=(process.argv[7]??'1,1.5,2,3,4').split(',').map(Number),valleys=(process.argv[8]??'.5,1,2').split(',').map(Number),seconds=(process.argv[9]??'.05,.2,1').split(',').map(Number);
for(const first of firsts)for(const valley of valleys)for(const second of seconds){
 const c={...config,warpWeightLevels:[[1,first,valley,second,1]],maxCachedBetas:1};let row;
 try{const tail=createRecalibrationFactory(c).assemble(),z=diagnosePhysicalMode(tail,mode,steps,far);row={first,valley,second,threshold:z.linearTPositivityAmplitudeThreshold,cutSlope:z.cutSlope,where:z.thresholdLocation,cellThresholds:z.cellThresholds.slice(0,9).map(v=>v.threshold),stats:tail.stats,config:c};
  if(!best||row.threshold>best.threshold){best={...row,geometry:sampleTailGeometry(tail,64)};await fs.writeFile(output.replace(/\.json$/,'_best_config.json'),JSON.stringify(c,null,2)+'\n');console.log(JSON.stringify({best:true,first,valley,second,T:row.threshold,DN:row.cutSlope,H:row.stats.heightSpan,where:row.where.cell}));}
 }catch(e){row={first,valley,second,error:e.message};}
 rows.push(row);await fs.writeFile(output,JSON.stringify({scope:'Actual fixed profiles with positive C2-compatible free-warp weights. Different metrics; linear sampled diagnostics only.',input,mode,steps,far,best,rows},null,2)+'\n');
}
