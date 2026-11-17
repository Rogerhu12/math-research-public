// Locate the local A bottleneck in an already accepted actual finite tail.
// No solve, physical parameter, local root guard or state is changed.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,recordFile,outFile]=process.argv.slice(2);
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const record=JSON.parse(gunzipSync(fs.readFileSync(recordFile))),cfg=record.config;
if(record.response?.converged!==true||!(record.response.residual<=cfg.solveTolerance))throw new Error('Expected an accepted original-gate tail');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical}),K=2*cfg.modes;
const states=record.response.checkpoint.states,rows=[];
for(let n=0;n<dn.tail.cells.length;n++){
 const c=dn.tail.cells[n],state=new Float64Array(K+2);state.set(states[n+1]);
 const f=c.engine.flowStateWithJacobian(state,c.profiles,{stepsPerSegment:cfg.steps});
 rows.push({stage:n,rawCell:c.rawCell,rawSegment:c.rawSegment,rawLeft:c.rawLeft,rawRight:c.rawRight,
            minA:f.minA,minD:f.minD,
            innerRadius:c.profiles[0](0).r,outerRadius:c.profiles.at(-1)(1).r});
}
rows.sort((a,b)=>a.minA-b.minA);
const output={scope:'Finite numerical stage localization, not a continuous bound or an amplitude limit.',
              source_sha256:createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex'),
              input_sha256:createHash('sha256').update(fs.readFileSync(recordFile)).digest('hex'),
              stages:rows.length,lowest:rows.slice(0,12)};
fs.writeFileSync(outFile,JSON.stringify(output,null,2)+'\n');
console.log(JSON.stringify(output));
