// First-mode zero-momentum cell calibration; design aid, not nonlinear capacity.
import fs from 'node:fs';import path from 'node:path';import readline from 'node:readline';import {pathToFileURL}from'node:url';
const [topic,factoryFile,configFile,stepsArg='128']=process.argv.slice(2),steps=Number(stepsArg);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;process.env.CLOSING_TAIL_CACHE=path.join(topic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(factoryFile));
const {physicalModeColumn}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const cfg=JSON.parse(fs.readFileSync(configFile)),factory=createRecalibrationFactory(cfg);
for await(const line of readline.createInterface({input:process.stdin,crlfDelay:Infinity})){
 try{
  const controls=JSON.parse(line),tail=factory.assemble(controls),rows=tail.cells.slice(0,controls.length).map(c=>{
   const v=physicalModeColumn(c,2,steps),[u,z]=v.column;
   return{residual:z/Math.hypot(u,z),gain:u,momentum:z,beta:c.beta,rInner:c.rStart,rOuter:c.rEnd};
  });
  console.log(JSON.stringify({controls,rows,residual:rows.map(r=>r.residual),height:tail.stats.heightSpan,alpha:tail.stats.blockAlpha??tail.stats.alpha,minWidth:tail.stats.blockMinimumWidth??tail.stats.minimumWarpWidth}));
 }catch(e){console.log(JSON.stringify({error:String(e)}));}
}
