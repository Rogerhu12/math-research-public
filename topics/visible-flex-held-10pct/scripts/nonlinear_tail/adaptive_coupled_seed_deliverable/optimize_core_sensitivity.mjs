// Direct physical design search. The smooth objective is a first-variation
// screening quantity, not a nonlinear amplitude or nonexistence criterion.
import fs from'node:fs';import path from'node:path';import{pathToFileURL}from'node:url';
const[topic,input,out,surrogateFile,stepsArg='128']=process.argv.slice(2),steps=Number(stepsArg);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;process.env.CLOSING_TAIL_CACHE=path.join(topic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const{createRecalibrationFactory}=await import('./hybrid_outer_factory.mjs');
const{diagnosePhysicalMode}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const config=JSON.parse(fs.readFileSync(input)),surrogate=JSON.parse(fs.readFileSync(surrogateFile)),factory=createRecalibrationFactory(config),N=config.outerCellDesign.count,history=[],memo=new Map();let best=null;
const initial=[...config.outerCellDesign.valleyControls,...config.outerCellDesign.pulseCaps.map(p=>Math.log(p[1])),Math.log(config.outerCellDesign.pulseCaps[0][0]),Math.log(config.outerCellDesign.warpWeights[0][2])];
function physicalConfig(x){const c=structuredClone(config);c.outerCellDesign.valleyControls=x.slice(0,N);c.outerCellDesign.pulseCaps=c.outerCellDesign.pulseCaps.map((p,j)=>[p[0],Math.exp(x[N+j])]);c.outerCellDesign.pulseCaps[0][0]=Math.exp(x[2*N]);c.outerCellDesign.warpWeights[0][2]=Math.exp(x[2*N+1]);return c;}
function evaluate(x,label){
 const key=JSON.stringify(x);if(memo.has(key))return memo.get(key);let row;
 try{
  const c=physicalConfig(x),tail=factory.assemble(c.outerCellDesign.valleyControls,c.outerCellDesign.pulseCaps,c.outerCellDesign.warpWeights),d=diagnosePhysicalMode(tail,2,steps,48);
  const HperQ=Math.abs(surrogate.C/(d.cutSlope-surrogate.D0));
  const sensitivities=d.cellThresholds.map(r=>1/r.threshold).concat([1/d.gradientAmplitudeThreshold]);
  const logs=sensitivities.filter(v=>v>0&&Number.isFinite(v)).map(v=>Math.log(v*HperQ)),max=Math.max(...logs),power=24;
  const logObjective=max+Math.log(logs.reduce((s,v)=>s+Math.exp(power*(v-max)),0))/power;
  row={iteration:history.length,label,x:Array.from(x),score:-logObjective,coreLeadingSlope:Math.exp(max),mode:2,steps,far:48,cutD:d.cutSlope,approximateHperQ:HperQ,worst:d.thresholdLocation,firstEightSensitivities:d.cellThresholds.slice(0,8).map(v=>1/v.threshold),height:tail.stats.heightSpan,alpha:tail.stats.blockAlpha,minWidth:tail.stats.blockMinimumWidth};
  if(!(row.height<.25&&Number.isFinite(row.score)))throw Error('Invalid geometry or objective');
 }catch(e){row={iteration:history.length,label,x:Array.from(x),score:-1e300,error:String(e)};}
 history.push(row);memo.set(key,row);
 if(!best||row.score>best.score){best=row;console.log(JSON.stringify({best:true,...row,firstEightSensitivities:undefined}));fs.writeFileSync(out.replace(/\.json$/,'_config.json'),JSON.stringify(physicalConfig(best.x),null,2)+'\n');}
 fs.writeFileSync(out,JSON.stringify({scope:'Full first-mode stage sensitivity times a declared approximate prefix core-line transfer. Distinct physical metrics; only screening. Selected candidate must have exact prefix root, all-frequency audit and nonlinear solve.',input,surrogateFile,steps,far:48,best,history},null,2)+'\n');return row;
}
evaluate(initial,'initial');
for(const shift of [-2,-1,1,2])evaluate(initial.map((v,j)=>j<N?v+shift:v),'joint beta seed '+shift);
for(const step of [1,.5,.25,.125,.0625,.03125]){
 for(let pass=0;pass<5;pass++){
  const start=best.score;
  for(let n=0;n<2*N+2;n++){
   const current=best.x.slice();for(const sign of [-1,1]){const x=current.slice();x[n]+=sign*step;const ok=n<N?(x[n]>=-8&&x[n]<=12):n<2*N?(x[n]>=Math.log(1e-4)&&x[n]<=Math.log(.3)):n===2*N?(x[n]>=Math.log(.15)&&x[n]<=Math.log(1.4)):(x[n]>=Math.log(.25)&&x[n]<=Math.log(40));if(ok)evaluate(x,'coordinate '+n+' step '+step);}
  }
  const current=best.x.slice();for(const sign of [-1,1]){const x=current.map((v,j)=>j<N?v+sign*step:v);if(x.slice(0,N).every(v=>v>=-8&&v<=12))evaluate(x,'joint beta step '+step);}
  if(best.score-start<1e-5)break;
 }
}
console.log(JSON.stringify({finished:true,evaluations:history.length,best}));
