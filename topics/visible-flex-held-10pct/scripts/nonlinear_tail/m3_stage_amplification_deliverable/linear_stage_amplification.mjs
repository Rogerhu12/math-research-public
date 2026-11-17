// Numerical subdivision screen on the unchanged rotational background.
// This is not a nonlinear capacity bound or an acceptance certificate.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
const [topic,config,out]=process.argv.slice(2);process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const cfg=JSON.parse(fs.readFileSync(config)),{createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs'))),{subdividePhysical,linearColumn}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-subdivision.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),rows=[];
for(const parts of [2,4,8,16]){
 const stages=subdividePhysical(physical,cfg.depth,parts).cells,steps=128/parts,byLimit={8:{norm:0},12:{norm:0},16:{norm:0}};
 for(let n=0;n<stages.length;n++){
  const c=stages[n];
  for(let j=1;j<=16;j++){
   const mode=3*j,a=linearColumn(c.profiles,c.mu,mode,steps,[1,0]),b=linearColumn(c.profiles,c.mu,mode,steps,[0,1]);
   const norm=Math.max(Math.abs(a[0])+Math.abs(b[0]),(Math.abs(a[1])+Math.abs(b[1]))/c.portRatio);
   for(const lim of [8,12,16])if(j<=lim&&norm>byLimit[lim].norm)byLimit[lim]={norm,stage:n,cell:c.rawCell,segment:c.rawSegment,rawLeft:c.rawLeft,rawRight:c.rawRight,mode};
  }
 }
 rows.push({shootingParts:parts,stepsPerStage:steps,totalStepsPerRawSegment:128,stages:stages.length,maxBackgroundJacobianInfinityNorm:byLimit});
}
const hash=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const res={scope:'Background first-variation stage amplification under purely numerical subdivision at fixed physical parameters and fixed total RK step count per raw segment. No nonlinear, metric, convergence or capacity claim.',config_sha256:hash(config),source_sha256:hash(path.join(topic,'scripts/950f-tail-subdivision.mjs')),factory_sha256:hash(path.join(topic,'scripts/closing_weighted_tail.mjs')),rows};fs.writeFileSync(out,JSON.stringify(res,null,2)+'\n');console.log(JSON.stringify(res));
