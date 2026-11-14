import fs from 'node:fs/promises';
import {createRecalibrationFactory,diagnosePhysicalM2,sampleTailGeometry,physicalM2Column} from './closing_recalibrated_tail.mjs';
const input=process.argv[2],output=process.argv[3],steps=+(process.argv[4]??256),betas=(process.argv[5]??'original').split(',').map(v=>v==='original'?null:+v);
if(!input||!output)throw Error('Usage: config-or-report.json output.json [steps] [beta0 list or original]');
const raw=JSON.parse(await fs.readFile(input,'utf8')),config=raw.config??raw,factory=createRecalibrationFactory(config),rows=[];
for(const beta0 of betas){
 const controls=Array.from({length:factory.parameters.protectCell},(_,n)=>n===0&&beta0!==null?beta0:config.valleyControls?.[n]??0),tail=factory.assemble(controls),diagnostics=diagnosePhysicalM2(tail,steps),geometry=sampleTailGeometry(tail,64),cell0=physicalM2Column(tail.cells[0],steps),row={beta0:controls[0],stats:tail.stats,cell0,diagnostics,geometry,config:{...config,valleyControls:controls}};
 rows.push(row);await fs.writeFile(output,JSON.stringify({scope:'True finite-profile linear m2 diagnostics after changing finite controls. No nonlinear closure or rigorous lower bound.',input,steps,rows},null,2)+'\n');
 console.log(JSON.stringify({beta0:row.beta0,stats:tail.stats,cell0,cutSlope:diagnostics.cutSlope,threshold:diagnostics.linearTPositivityAmplitudeThreshold,where:diagnostics.thresholdLocation,geometry}));
}
