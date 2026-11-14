import fs from 'node:fs/promises';
import {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry} from './closing_recalibrated_tail.mjs';
const input=process.argv[2],output=process.argv[3],steps=+(process.argv[4]??256),modes=(process.argv[5]??'2,3').split(',').map(Number),farArg=process.argv[6],testAmplitude=+(process.argv[7]??0);
if(!input||!output)throw Error('Usage: config-or-report.json output.json [steps] [mode list] [far]');
const raw=JSON.parse(await fs.readFile(input,'utf8')),config=raw.config??raw,factory=createRecalibrationFactory(config),tail=factory.assemble(),rows=[];
for(const mode of modes){
 const z=diagnosePhysicalMode(tail,mode,steps,farArg===undefined?tail.cells.length:+farArg,testAmplitude);rows.push(z);
 await fs.writeFile(output,JSON.stringify({scope:'True finite-profile physical Fourier diagnostics. No nonlinear or infinite-tail theorem.',config,stats:tail.stats,rows},null,2)+'\n');
 console.log(JSON.stringify({mode,cutSlope:z.cutSlope,threshold:z.linearTPositivityAmplitudeThreshold,gradientThreshold:z.gradientAmplitudeThreshold,where:z.thresholdLocation,formalGeometry:z.formalLinearHeightGeometry,far:z.far,steps}));
}
