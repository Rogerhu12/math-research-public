import fs from 'node:fs/promises';
import {createRecalibrationFactory,solvePhysicalCell,diagnosePhysicalM2,sampleTailGeometry} from './closing_recalibrated_tail.mjs';
const input=process.argv[2],output=process.argv[3],steps=+(process.argv[4]??128),mode=process.argv[5]??'original',maxOuter=+(process.argv[6]??12);
if(!input||!output)throw Error('Usage: config.json output.json [steps] [capMode] [maxOuter]');
const config={...JSON.parse(await fs.readFile(input,'utf8')),capMode:mode},factory=createRecalibrationFactory(config),baseline=factory.assemble(),N=factory.parameters.protectCell,history=[],controls=Array.from({length:N},(_,n)=>config.valleyControls?.[n]??2*Math.log(baseline.stats.alpha));
let alpha=baseline.stats.alpha,tail=baseline;
for(let outer=0;outer<maxOuter;outer++){
 let r=factory.deepSource.r;const rows=[];
 for(let n=N-1;n>=0;n--){
  const cellSteps=n>=60?Math.min(steps,16):n>=40?Math.min(steps,32):n>=24?Math.min(steps,64):steps;
  const z=solvePhysicalCell(factory,n,r,alpha,{steps:cellSteps,tolerance:1e-9,initialBeta:controls[n]});controls[n]=z.beta;r=z.cell.rEnd;
  rows.push({cell:n,beta:z.beta,gain:z.gain,residual:z.zeroResidual,rStart:z.cell.rStart,rEnd:z.cell.rEnd,evaluations:z.evaluations,steps:cellSteps});
  if(n%16===0)console.log(JSON.stringify({outer,cell:n,beta:z.beta,gain:z.gain,residual:z.zeroResidual,r}));
 }
 tail=factory.assemble(controls,alpha);const next=factory.assemble(controls),error=tail.stats.cutRadiusError;
 const row={outer,alpha,newAlpha:next.stats.alpha,cutRadiusError:error,heightSpan:tail.stats.heightSpan,minimumWarpWidth:tail.stats.minimumWarpWidth,rows};history.push(row);
 console.log(JSON.stringify({outer,alpha,newAlpha:next.stats.alpha,cutRadiusError:error,heightSpan:tail.stats.heightSpan}));
 const checkpoint={scope:'Numerical true physical m2 finite-cell recalibration. Not nonlinear closure.',config:{...config,valleyControls:controls},steps,baselineStats:baseline.stats,history,stats:tail.stats};
 await fs.writeFile(output,JSON.stringify(checkpoint,null,2)+'\n');
 if(Math.abs(error)<2e-11){
  const diagnostics=diagnosePhysicalM2(tail,Math.max(steps,256)),geometry=sampleTailGeometry(tail,128);
  await fs.writeFile(output,JSON.stringify({...checkpoint,converged:true,diagnostics,geometry},null,2)+'\n');
  await fs.writeFile(output.replace(/\.json$/,'_config.json'),JSON.stringify({...config,valleyControls:controls},null,2)+'\n');
  console.log(JSON.stringify({converged:true,stats:tail.stats,cutSlope:diagnostics.cutSlope,threshold:diagnostics.linearTPositivityAmplitudeThreshold,where:diagnostics.thresholdLocation,geometry}));break;
 }
 alpha=next.stats.alpha;
}
