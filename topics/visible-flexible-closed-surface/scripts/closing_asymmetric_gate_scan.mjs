import fs from 'node:fs/promises';
import {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry} from './closing_recalibrated_tail.mjs';
const input=process.argv[2],output=process.argv[3],mode=+(process.argv[4]??3),steps=+(process.argv[5]??96),far=+(process.argv[6]??32),rows=[];
if(!input||!output)throw Error('Usage: config.json output.json [mode] [steps] [far]');
const config=JSON.parse(await fs.readFile(input,'utf8'));let best=null,bestShort=null;
for(const K of [8,9])for(const first of [.1,.2,.4,.6,.8,1,1.2]){
 const c={...config,curvatureBound:K,pulseCaps:[[first,.02]],valleyCaps:[.1],maxCachedBetas:3};
 let factory;try{factory=createRecalibrationFactory(c);}catch(e){rows.push({K,first,error:e.message});continue;}
 for(const beta0 of [0,1,2,3,4,5,6]){
  const controls=Array.from({length:factory.parameters.protectCell},(_,n)=>n===0?beta0:c.valleyControls?.[n]??0);let row;
  try{const tail=factory.assemble(controls),z=diagnosePhysicalMode(tail,mode,steps,far);row={K,first,beta0,threshold:z.linearTPositivityAmplitudeThreshold,gradientThreshold:z.gradientAmplitudeThreshold,cutSlope:z.cutSlope,where:z.thresholdLocation,cellThresholds:z.cellThresholds.slice(0,8).map(v=>v.threshold),stats:tail.stats,config:{...c,valleyControls:controls}};
   const gate=Math.min(row.threshold,row.gradientThreshold);
   if(!best||gate>Math.min(best.threshold,best.gradientThreshold)){best={...row,geometry:sampleTailGeometry(tail,64)};await fs.writeFile(output.replace(/\.json$/,'_best_config.json'),JSON.stringify(row.config,null,2)+'\n');console.log(JSON.stringify({newBest:true,K,first,beta0,gate,DN:z.cutSlope,height:tail.stats.heightSpan,where:{cell:z.thresholdLocation.cell,segment:z.thresholdLocation.segment,x:z.thresholdLocation.x}}));}
   if(tail.stats.heightSpan<=.08&&(!bestShort||gate>Math.min(bestShort.threshold,bestShort.gradientThreshold))){bestShort=row;await fs.writeFile(output.replace(/\.json$/,'_short_config.json'),JSON.stringify(row.config,null,2)+'\n');}
  }catch(e){row={K,first,beta0,error:e.message};}
  rows.push(row);await fs.writeFile(output,JSON.stringify({scope:'Asymmetric shallow pulse and valley control, actual changed metrics. Linear sampled gates only.',input,mode,steps,far,best,bestShort,rows},null,2)+'\n');
 }
 console.log(JSON.stringify({completed:{K,first},bestGate:best?Math.min(best.threshold,best.gradientThreshold):null}));
}
