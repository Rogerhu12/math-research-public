// Actual full changed tail linear graph for a finite GC boundary initializer.
// Deep cells are appended from the unchanged source; no protectCell extension.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import v8 from 'node:v8';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {boundTailPointCaches} from './fd2d-bounded-tail-point-cache.mjs';
import {appendUnchangedDeepSource} from './fd2d-gc-tail-deep-extension.mjs';
import {subdividePhysical,buildStableStageGraphs,stageGraphStatistics} from './fd2d-gc-tail-stage-graphs.mjs';

const [input,output,modesArg='47',stepsArg='256']=process.argv.slice(2);
if(!input||!output)throw Error('config.json output.json [mode count] [linear steps]');
if(fs.existsSync(output))throw Error('Use an unused output path');
const modes=Number(modesArg),steps=Number(stepsArg),spacing=2,parts=2,far=196,began=Date.now();
const identity=file=>{const bytes=fs.readFileSync(file);return {file:String(file),bytes:bytes.length,sha256:crypto.createHash('sha256').update(bytes).digest('hex')};};
const cfg=JSON.parse(fs.readFileSync(input,'utf8'));
if(cfg.protectCell!==160)throw Error('This entry expects the declared 160 physically modified cells');
const factory=createRecalibrationFactory(cfg),cache=boundTailPointCaches(factory,cfg,{pointsPerEntry:8});
const finite=factory.assemble(),physical=appendUnchangedDeepSource(finite,far),stages=subdividePhysical(physical,160,parts);
console.log(JSON.stringify({event:'assembled',modes,spacing,raw_depth:160,far,stages:stages.cells.length,cache,
  memory:{...process.memoryUsage(),heap_size_limit:v8.getHeapStatistics().heap_size_limit}}));
const value=buildStableStageGraphs(physical,stages,{modes,spacing,linearFar:far,linearSteps:steps});
const cell=stages.cells[0],p=cell.profiles.at(-1)(1),w=Math.exp(p.logw),orientation=cfg.orientation??1;
const rows=Array.from({length:modes},(_,j)=>{
  const mode=spacing*(j+1),graph=value.graphs[0][j];
  const slope=mode*mode/p.r+orientation*Math.sqrt(12)*cell.mu*cell.portRatio*graph/(p.r**8*w);
  if(!Number.isFinite(slope))throw Error('Nonfinite actual cut slope for mode '+mode);
  return {mode,slope,cut_graph:graph};
});
const result={schema:'fd2d-full160-linear-tail-port-v1',scope:'Actual finite linear graph through every modified cell and unchanged source through195; a labelled GC initializer, not a nonlinear DN or infinite-tail certificate.',
  source:identity(new URL(import.meta.url)),config_input:identity(input),config:cfg,modes,spacing,steps,far,
  modified_cells:160,source_appended_without_modifying_g:true,parts,stats:finite.stats,
  cut:{r:p.r,w,wr:w*p.dlogwdx/p.drdx,E:1+w*w,mu:cell.mu,portRatio:cell.portRatio},
  rows,graph_statistics:stageGraphStatistics(),deep_extension:physical.deepExtension,
  source_dependencies:['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs','fd2d-bounded-tail-point-cache.mjs','fd2d-gc-tail-deep-extension.mjs','fd2d-gc-tail-stage-graphs.mjs','950f-tail-subdivision.mjs'].map(name=>identity(new URL('./'+name,import.meta.url))),
  completed:true,nonlinear_tail_solved:false,continuous_certificate:false,seconds:(Date.now()-began)/1000,
  memory:{...process.memoryUsage(),heap_size_limit:v8.getHeapStatistics().heap_size_limit}};
fs.mkdirSync(path.dirname(output),{recursive:true});fs.writeFileSync(output+'.tmp',JSON.stringify(result,null,2)+'\n');fs.renameSync(output+'.tmp',output);
console.log(JSON.stringify({event:'completed',output,rows:rows.length,first:rows[0],last:rows.at(-1),seconds:result.seconds,memory:result.memory}));
