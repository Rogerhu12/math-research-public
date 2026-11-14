import fs from 'node:fs/promises';
import {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry} from './closing_recalibrated_tail.mjs';
const input=process.argv[2],output=process.argv[3],mode=+(process.argv[4]??3),steps=+(process.argv[5]??96),far=+(process.argv[6]??32),rows=[];
if(!input||!output)throw Error('Usage: config.json output.json [mode] [steps] [far]');
const config=JSON.parse(await fs.readFile(input,'utf8'));let best=null;
for(const cell of [0,1,2,3,4,5,6,8,10])for(const slope of [.02,.05,.1,.2]){
 const c={...config,flatOuterThroughCell:cell,flatOuterStartSegment:2,flatSlope:slope,maxCachedBetas:1};let row;
 try{const tail=createRecalibrationFactory(c).assemble(),z=diagnosePhysicalMode(tail,mode,steps,far);row={cell,slope,threshold:z.linearTPositivityAmplitudeThreshold,gradientThreshold:z.gradientAmplitudeThreshold,cutSlope:z.cutSlope,where:z.thresholdLocation,cellThresholds:z.cellThresholds.slice(0,Math.max(cell+2,10)).map(v=>v.threshold),stats:tail.stats,config:c};
  if(!best||Math.min(row.threshold,row.gradientThreshold)>Math.min(best.threshold,best.gradientThreshold)){
   best={...row,geometry:sampleTailGeometry(tail,64)};await fs.writeFile(output.replace(/\.json$/,'_best_config.json'),JSON.stringify(c,null,2)+'\n');
  }
 }catch(e){row={cell,slope,error:e.message};}
 rows.push(row);console.log(JSON.stringify({cell,slope,threshold:row.threshold,gradientThreshold:row.gradientThreshold,cutSlope:row.cutSlope,where:row.where?{cell:row.where.cell,segment:row.where.segment,x:row.where.x,r:row.where.r,w:row.where.w}:undefined,heightSpan:row.stats?.heightSpan,minimumWidth:row.stats?.minimumWarpWidth,error:row.error}));
 await fs.writeFile(output,JSON.stringify({scope:'Actual finite splice: source first high plateau to constant-slope sleeve, then exact cut recovery. Different fixed metrics; linear sampled diagnostics only.',input,mode,steps,far,best,rows},null,2)+'\n');
}
