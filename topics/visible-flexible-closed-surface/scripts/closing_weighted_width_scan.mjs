import fs from 'node:fs/promises';
import {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry} from './closing_weighted_tail.mjs';
const input=process.argv[2],output=process.argv[3],steps=+(process.argv[4]??96),far=+(process.argv[5]??32),rows=[];
const config=JSON.parse(await fs.readFile(input,'utf8'));let best=null;
for(const width of [.25,.3,.35,.375,.4,.425,.45,.475,.5]){
 const c={...config,width};let row;
 try{const tail=createRecalibrationFactory(c).assemble(),z=diagnosePhysicalMode(tail,3,steps,far);row={width,threshold:z.linearTPositivityAmplitudeThreshold,cutSlope:z.cutSlope,where:z.thresholdLocation,cellThresholds:z.cellThresholds.slice(0,10).map(v=>v.threshold),stats:tail.stats,config:c};
  if(!best||row.threshold>best.threshold){best={...row,geometry:sampleTailGeometry(tail,64)};await fs.writeFile(output.replace(/\.json$/,'_best_config.json'),JSON.stringify(c,null,2)+'\n');}
 }catch(e){row={width,error:e.message};}
 rows.push(row);console.log(JSON.stringify({width,T:row.threshold,DN:row.cutSlope,H:row.stats?.heightSpan,where:row.where?.cell,error:row.error}));await fs.writeFile(output,JSON.stringify({scope:'Different true weighted profiles over tail widths; m3 linear sampled gates only.',input,steps,far,best,rows},null,2)+'\n');
}
