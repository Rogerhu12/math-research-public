// Direct finite-profile linear gate optimization. The selected mode need not
// have zero momentum at cell boundaries. Each candidate is a different metric.
import fs from 'node:fs/promises';
import {createRecalibrationFactory,diagnosePhysicalMode} from './closing_recalibrated_tail.mjs';
const input=process.argv[2],output=process.argv[3],mode=+(process.argv[4]??3),steps=+(process.argv[5]??128),far=+(process.argv[6]??32),number=+(process.argv[7]??4);
if(!input||!output)throw Error('Usage: config.json output.json [mode] [steps] [far] [number of outer valley controls]');
const config=JSON.parse(await fs.readFile(input,'utf8')),factory=createRecalibrationFactory({...config,maxCachedBetas:4}),N=factory.parameters.protectCell,history=[],memo=new Map();let best=null,iteration=0;
const base=Array.from({length:N},(_,n)=>config.valleyControls?.[n]??0);
function value(z){const vals=[z.gradientAmplitudeThreshold,...z.cellThresholds.map(v=>v.threshold)].filter(v=>v>0&&Number.isFinite(v)),logs=vals.map(Math.log),m=Math.min(...logs),p=4;return m-Math.log(logs.reduce((s,l)=>s+Math.exp(p*(m-l)),0))/p;}
async function evaluate(x,label){
 const key=JSON.stringify(x);if(memo.has(key))return memo.get(key);const controls=base.slice();for(let n=0;n<number;n++)controls[n]=x[n];let row;
 try{const tail=factory.assemble(controls),z=diagnosePhysicalMode(tail,mode,steps,far);row={iteration:iteration++,label,x:Array.from(x),score:value(z),threshold:z.linearTPositivityAmplitudeThreshold,gradientThreshold:z.gradientAmplitudeThreshold,cutSlope:z.cutSlope,where:z.thresholdLocation,cellThresholds:z.cellThresholds.slice(0,Math.max(number+3,10)).map(v=>v.threshold),stats:tail.stats};}
 catch(e){row={iteration:iteration++,label,x:Array.from(x),score:-1e300,error:e.message};}
 history.push(row);memo.set(key,row);
 if(!best||row.score>best.score){best=row;console.log(JSON.stringify({best:true,...row,cellThresholds:undefined,stats:{alpha:row.stats?.alpha,heightSpan:row.stats?.heightSpan,minimumWarpWidth:row.stats?.minimumWarpWidth}}));const bestControls=base.slice();for(let n=0;n<number;n++)bestControls[n]=best.x[n];await fs.writeFile(output.replace(/\.json$/,'_config.json'),JSON.stringify({...config,valleyControls:bestControls},null,2)+'\n');}
 await fs.writeFile(output,JSON.stringify({scope:'Direct physical Fourier linear gate optimization over distinct finite metrics; samples, not nonlinear existence.',input,mode,steps,far,number,best,history},null,2)+'\n');return row;
}
await evaluate(base.slice(0,number),'input');
for(const v of [1,2,3,4,5,6,8])await evaluate(Array(number).fill(v),'uniform seed '+v);
for(const step of [2,1,.5,.25,.125,.0625]){
 for(let pass=0;pass<5;pass++){
  const start=best.score;
  for(let n=0;n<number;n++){
   const current=best.x.slice();for(const sign of [-1,1]){const x=current.slice();x[n]+=sign*step;if(x[n]>=-12&&x[n]<=18)await evaluate(x,'coordinate '+n+' step '+step);}
  }
  // Joint direction helps pass balanced minima where several cells are active.
  const current=best.x.slice();for(const sign of [-1,1]){const x=current.map(v=>v+sign*step);if(x.every(v=>v>=-12&&v<=18))await evaluate(x,'joint step '+step);}
  if(best.score-start<1e-5)break;
 }
}
console.log(JSON.stringify({finished:true,evaluations:history.length,best}));
