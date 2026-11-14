// Bounded equivalence check for the optional memory-sharing implementation.
// Compares actual cut jets and variational stage flows, not source text alone.
import fs from 'node:fs';
import zlib from 'node:zlib';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {createSplitFluxCompactTailDN as original} from './950f-tail-stage-split.mjs';
import {createSplitFluxCompactTailDN as shared} from './db6f-prefix-tail-shared-split.mjs';
const args=process.argv.slice(2),get=name=>args[args.indexOf(name)+1];
const checkpoint=get('--checkpoint'),config=get('--config'),output=get('--out');
const bytes=fs.readFileSync(checkpoint),record=JSON.parse((checkpoint.endsWith('.gz')?zlib.gunzipSync(bytes):bytes).toString()),
  cp=record.response?.checkpoint??record.checkpoint??record,cfg=JSON.parse(fs.readFileSync(config,'utf8'));
if(cp.parameters.modes!==cfg.modes)throw Error('Use one unchanged checkpoint configuration');
const physical=createRecalibrationFactory(cfg).assemble(),a=original({...cfg,tail:physical}),b=shared({...cfg,tail:physical});
function compare(x,y){
  if(x.length!==y.length)throw Error('Different vector dimensions');
  let maximum=0,bitwise=true;
  for(let k=0;k<x.length;k++){maximum=Math.max(maximum,Math.abs(x[k]-y[k]));if(!Object.is(x[k],y[k]))bitwise=false;}
  return {maximum,bitwise};
}
const ja=a.cutJets(cp.states[0]),jb=b.cutJets(cp.states[0]),jetRows=[];
for(const k of Object.keys(ja))jetRows.push({name:k,...compare(Array.isArray(ja[k])?ja[k]:[ja[k]],Array.isArray(jb[k])?jb[k]:[jb[k]])});
const indices=[0,Math.floor(a.tail.cells.length/3),a.tail.cells.length-1],stageRows=[];
for(const n of indices){
  const v=new Float64Array(2*cfg.modes+2);v.set(cp.states[n+1]);
  const x=a.tail.cells[n].engine.flowStateWithJacobian(v,a.tail.cells[n].profiles,{stepsPerSegment:cfg.steps}),
    y=b.tail.cells[n].engine.flowStateWithJacobian(v,b.tail.cells[n].profiles,{stepsPerSegment:cfg.steps});
  stageRows.push({stage:n,state:compare(x.state,y.state),tangent:compare(x.tangent,y.tangent),
    minA:compare([x.minA],[y.minA]),minD:compare([x.minD],[y.minD])});
}
const out={scope:'Actual jet and variational-flow equivalence at representative saved states. Allocation only is changed.',
  checkpoint,config,stages:a.tail.cells.length,oldEngineObjects:new Set(a.tail.cells.map(c=>c.engine)).size,
  sharedEngineObjects:new Set(b.tail.cells.map(c=>c.engine)).size,jetRows,stageRows};
out.all_bitwise_equal=jetRows.every(r=>r.bitwise)&&stageRows.every(r=>['state','tangent','minA','minD'].every(k=>r[k].bitwise));
fs.writeFileSync(output,JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({output,all_bitwise_equal:out.all_bitwise_equal,stages:out.stages,
  oldEngineObjects:out.oldEngineObjects,sharedEngineObjects:out.sharedEngineObjects}));
if(!out.all_bitwise_equal)process.exitCode=1;
