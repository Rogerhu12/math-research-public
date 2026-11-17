// Geometry of one explicitly changed first cell; no nonlinear capacity claim.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
const [topic,factoryFile,configFile,out] = process.argv.slice(2);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;
process.env.CLOSING_TAIL_CACHE=path.join(topic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(factoryFile));
const cfg=JSON.parse(fs.readFileSync(configFile));
const hash=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
let report;
try {
 const tail=createRecalibrationFactory(cfg).assemble();
 let maxK=0,minR=Infinity,maxW=0,minWidth=Infinity,where=null;
 for (let n=0;n<Math.min(8,tail.cells.length);n++) {
  const cell=tail.cells[n];minWidth=Math.min(minWidth,cell.localWidth);
  for(let j=0;j<cell.profiles.length;j++)for(let k=0;k<=256;k++){
   const x=k/256,g=cell.profiles[j](x),w=Math.exp(g.logw),wr=w*g.dlogwdx/g.drdx,E=1+w*w;
   const K=Math.max(Math.abs(wr)/E**1.5,Math.abs(w)/(g.r*Math.sqrt(E)));
   if(K>maxK){maxK=K;where={n,j,x,r:g.r,w,wr};}
   minR=Math.min(minR,g.r);maxW=Math.max(maxW,w);
  }
 }
 report={scope:'Sampled axisymmetric physical metric geometry; finite first cell only changed, no nonlinear solve or closed-surface certificate.',config:configFile,config_sha256:hash(configFile),factory:factoryFile,factory_sha256:hash(factoryFile),stats:tail.stats,maxK,where,minR,maxW,minWidth,firstCells:tail.cells.slice(0,8).map(c=>({width:c.localWidth,height:c.heightSpan,rStart:c.rStart,rEnd:c.rEnd}))};
} catch(e) {report={config:configFile,error:String(e)};}
fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out,error:report.error,height:report.stats?.heightSpan,minWidth:report.stats?.outerCellMinimumWidth,alpha:report.stats?.outerCellAlpha,maxK:report.maxK,maxW:report.maxW}));
