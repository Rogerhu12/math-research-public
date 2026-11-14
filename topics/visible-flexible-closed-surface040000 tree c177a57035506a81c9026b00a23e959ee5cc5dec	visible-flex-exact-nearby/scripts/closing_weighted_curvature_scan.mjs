// Each row is a distinct actual background metric, with recomputed warp and DN.
import fs from 'node:fs/promises';
import {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry} from './closing_weighted_tail.mjs';
const input=process.argv[2],output=process.argv[3],steps=+(process.argv[4]??96),far=+(process.argv[5]??32),amplitude=+(process.argv[6]??.00114),ks=(process.argv[7]??'4.5,5,6,7,8,9').split(',').map(Number);
if(!input||!output)throw Error('Usage: config.json out.json [steps] [far] [amplitude] [K list]');
const config=JSON.parse(await fs.readFile(input,'utf8')),rows=[];
for(const curvatureBound of ks){
 const candidate={...config,curvatureBound};let row;
 try{const tail=createRecalibrationFactory(candidate).assemble(),z=diagnosePhysicalMode(tail,3,steps,far,amplitude);row={curvatureBound,config:candidate,cutSlope:z.cutSlope,threshold:z.linearTPositivityAmplitudeThreshold,where:z.thresholdLocation,cellThresholds:z.cellThresholds.slice(0,10).map(v=>v.threshold),stats:tail.stats,formalGeometry:z.formalLinearHeightGeometry,backgroundGeometry:sampleTailGeometry(tail,64)};}
 catch(e){row={curvatureBound,error:e.message};}
 rows.push(row);console.log(JSON.stringify({...row,config:undefined,cellThresholds:undefined,backgroundGeometry:undefined}));
 await fs.writeFile(output,JSON.stringify({scope:'Different fixed backgrounds; finite sampled linear and formal curvature diagnostics only. No nonlinear surface or reach certificate.',input,steps,far,amplitude,rows},null,2)+'\n');
}
