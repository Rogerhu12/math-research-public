// Finite linear physical-tail diagnostic. No nonlinear amplitude upper bound.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const [sourceTopic,configFile,outFile,stepsArg='64',farArg='32']=process.argv.slice(2);
if(!outFile)throw Error('Usage: source-topic config.json output.json [steps=64] [far=32]');
process.env.CLOSING_TAIL_CACHE=path.join(sourceTopic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory,diagnosePhysicalMode,sampleTailGeometry}=await import(pathToFileURL(path.join(sourceTopic,'scripts/closing_weighted_tail.mjs')));
const config=JSON.parse(fs.readFileSync(configFile));
if (Number.isInteger(config.valleyControlsPadTo)) {
  while (config.valleyControls.length < config.valleyControlsPadTo) config.valleyControls.push(0);
  delete config.valleyControlsPadTo;
}
const tail=createRecalibrationFactory(config).assemble();
const steps=Number(stepsArg),far=Number(farArg),linear=diagnosePhysicalMode(tail,2,steps,far),geometry=sampleTailGeometry(tail,steps);
const result={scope:'Sampled finite linear first-mode positive-leading-branch diagnostic; not a nonlinear existence or amplitude bound.',config,steps,far,physicalDepth:config.protectCell,stats:tail.stats,linear,geometry};
fs.writeFileSync(outFile,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({D2:linear.cutSlope,linearTThreshold:linear.linearTPositivityAmplitudeThreshold,height:tail.stats.heightSpan,kappa:geometry.maxMeridian}));
