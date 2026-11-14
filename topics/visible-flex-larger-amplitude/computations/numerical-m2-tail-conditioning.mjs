// Finite linear stable-line conditioning on alternative physical tail designs.
// This is a screening diagnostic, never an actual nonlinear tail response.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
const [sourceTopic,portFile,heightFile,outputFile,variantFile]=process.argv.slice(2);
const sourceRoot=path.join(sourceTopic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(sourceTopic,'scripts/closing_weighted_tail.mjs')));
const {subdividePhysical,buildStableStageGraphs,linearColumn}=await import(pathToFileURL(path.join(sourceTopic,'scripts/950f-tail-subdivision.mjs')));
const base=JSON.parse(fs.readFileSync(portFile,'utf8')).parameters,report=JSON.parse(fs.readFileSync(heightFile,'utf8'));
const h=(report.full_prefix_target_height??report.full_target_height)[0],depth=24,parts=4,linearSteps=512,linearFar=48;
const variants=variantFile?JSON.parse(fs.readFileSync(variantFile,'utf8')):[...[2,4,8,16,32,64].map(prefixR=>({prefixR,label:'prefixR'+prefixR})),...[1,2,4].map(add=>({prefixR:8,addValley:add,label:'prefixR8-valleyplus'+add}))];
const out={scope:'Finite linear stable-line conditioning only. Does not solve nonlinear equations or certify a closing tail.',height:h,depth,parts,linearSteps,linearFar,source_sha256:{},rows:[]};
for(const file of [portFile,heightFile,path.join(sourceTopic,'scripts/closing_weighted_tail.mjs'),path.join(sourceTopic,'scripts/950f-tail-subdivision.mjs')])out.source_sha256[file]=crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
for(const v of variants){const start=Date.now();let row={variant:v};
 try{
  const cfg={...base,prefixR:v.prefixR??base.prefixR,...v.parameters};if(v.addValley)cfg.valleyControls=Array.from({length:base.protectCell},(_,j)=>(base.valleyControls[j]??0)+(j<16?v.addValley:0));
  const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,depth,parts),{graphs,gains}=buildStableStageGraphs(physical,stages,{modes:1,spacing:2,linearFar,linearSteps});
  const states=[[h/base.rCut**4,graphs[0][0]*h/base.rCut**4]];
  for(let n=0;n<stages.cells.length;n++){const q=states[n][0]/gains[n][0];states.push([q,graphs[n+1][0]*q]);}
  let maxL=0,maxP=0,maxQ=0,atL=null,atP=null,cutSlope=null;const byRaw=[];
  function record(y,c,n,x){const g=c.profiles[0](x),w=Math.exp(g.logw),P=Math.abs(2*g.r**3*y[0]/w),L=Math.abs(Math.sqrt(12)*c.mu*y[1]/(g.r**4*w*w));const at={stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,x,r:g.r,w,Q:y[0],momentum:y[1]};if(L>maxL){maxL=L;atL=at;}if(P>maxP){maxP=P;atP=at;}maxQ=Math.max(maxQ,Math.abs(y[0]));byRaw[c.rawCell]??={rawCell:c.rawCell,maxL:0,maxP:0,maxQ:0};const a=byRaw[c.rawCell];a.maxL=Math.max(a.maxL,L);a.maxP=Math.max(a.maxP,P);a.maxQ=Math.max(a.maxQ,Math.abs(y[0]));}
  for(let n=0;n<stages.cells.length;n++){
   const c=stages.cells[n],profile=c.profiles[0];let y=states[n+1].slice();record(y,c,n,0);
   for(let j=0;j<8;j++){const lo=j/8,part=x=>{const g=profile(lo+x/8);return {...g,drdx:g.drdx/8,dlogwdx:g.dlogwdx/8};};part.integrationBreakpoints=(profile.integrationBreakpoints??[]).filter(x=>x>lo&&x<lo+1/8).map(x=>(x-lo)*8);y=linearColumn([part],c.mu,2,8,y);record(y,c,n,(j+1)/8);}
  }
  const cut=physical.cells[0].profiles.at(-1)(1),wcut=Math.exp(cut.logw);cutSlope=4/cut.r+Math.sqrt(12)*physical.cells[0].mu*states[0][1]*2**physical.parameters.a/(cut.r**8*wcut*states[0][0]);
  row={...row,cutSlope,stats:physical.stats,maxL,maxP,maxQ,atL,atP,byRaw,linearSeedLmaxQuarterScale:.25/maxL,config:cfg};
 }catch(error){row.error=String(error);}
 row.seconds=(Date.now()-start)/1000;out.rows.push(row);fs.writeFileSync(outputFile,JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({variant:v,...Object.fromEntries(['cutSlope','maxL','maxP','linearSeedLmaxQuarterScale','seconds','error'].map(k=>[k,row[k]]))}));
}
