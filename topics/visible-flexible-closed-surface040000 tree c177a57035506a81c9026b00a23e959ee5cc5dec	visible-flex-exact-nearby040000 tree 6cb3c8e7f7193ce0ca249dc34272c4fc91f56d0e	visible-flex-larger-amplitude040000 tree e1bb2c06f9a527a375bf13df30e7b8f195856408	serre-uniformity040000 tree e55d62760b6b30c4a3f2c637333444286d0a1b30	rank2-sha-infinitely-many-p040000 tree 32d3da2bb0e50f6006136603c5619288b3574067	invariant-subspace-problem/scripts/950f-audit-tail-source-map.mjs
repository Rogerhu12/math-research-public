// Read-only audit of the physical/deep source interface; no optimization.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [input,out,sourceRoot]=process.argv.slice(2);
if(!input||!out||!sourceRoot)throw Error('checkpoint out sourceRoot required');
if(fs.existsSync(out))throw Error('refusing to overwrite existing record');
const here=path.dirname(fileURLToPath(import.meta.url));
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.resolve(sourceRoot);
process.env.CLOSING_TAIL_CACHE=path.join(path.resolve(sourceRoot),'topics/large-amplitude-twist-flex/scripts');
const record=JSON.parse(gunzipSync(fs.readFileSync(input)).toString()),p=record.response.checkpoint.parameters;
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const factory=createRecalibrationFactory(record.config??p),tail=factory.assemble();
const rows=[];
for(const n of [6,7,8,9,16,31,79,158,159]){
 const cell=tail.cells[n],old=factory.source.cells[n],row={n,R:old.R,mu:old.mu,rOuter:cell.rEnd,rInner:cell.rStart,ports:[]};
 for(const [segment,x] of [[0,0],[4,.5],[8,1]]){
  const g=cell.profiles[segment](x),s=old.profiles[segment](x);
  row.ports.push({segment,x,r:g.r,sourceR:s.r,drdx:g.drdx,sourceDrdx:s.drdx,radialDerivativeRatio:g.drdx/s.drdx,w:Math.exp(g.logw),logw:g.logw,sourceLogw:s.logw,chi:g.chi});
 }
 rows.push(row);
}
const sha=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const sources=[fileURLToPath(import.meta.url),input,...['closing_recalibrated_tail.mjs','closing_weighted_tail.mjs','closing_tail_sources.mjs'].map(f=>path.join(here,f)),...['tailnext_balanced_tail.mjs','general_root_smooth_tail_cells.cjs','f6tail_infinite_profile.mjs'].map(f=>path.join(process.env.CLOSING_TAIL_CACHE,f))];
const r={scope:'Floating source/interface diagnostics only. Exact source formulas and parameter compatibility are discussed in the independent tail-extension audit. Positive radial warp persists through raw cell159; raw source starts at160. No nonlinear tail or global certificate.',sourceSHA256:Object.fromEntries(sources.map(f=>[path.resolve(f),sha(f)])),inputPhysicalParameters:{delta0:p.delta0,etaRatioAtN0:p.etaRatioAtN0,etaPower:p.etaPower,a:p.a,R:p.R,rCuff:p.rCuff,rCut:p.rCut,wCut:p.wCut,width:p.width,protectCell:p.protectCell,linearFar:p.linearFar},stats:tail.stats,unitCuffEpsilon:tail.parameters.epsilonScale/tail.parameters.rCuff**7,rows};
fs.writeFileSync(out,JSON.stringify(r,null,2)+'\n');
console.log(JSON.stringify({alpha:tail.stats.alpha,unitCuffEpsilon:r.unitCuffEpsilon,cell31midRadialWarp:rows.find(x=>x.n===31).ports[1].radialDerivativeRatio,rawStartsAt:p.protectCell}));
