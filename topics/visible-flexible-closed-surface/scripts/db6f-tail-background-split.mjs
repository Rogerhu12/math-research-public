// Numerical bookkeeping only; no rigorous quadrature claim.
import fs from 'node:fs';
import path from 'node:path';
import {gunzipSync} from 'node:zlib';
import {pathToFileURL,fileURLToPath} from 'node:url';
const [input,out,sourceRoot]=process.argv.slice(2);
if(!sourceRoot)throw Error('input output sourceRoot required');
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.resolve(sourceRoot);process.env.CLOSING_TAIL_CACHE=path.join(path.resolve(sourceRoot),'topics/large-amplitude-twist-flex/scripts');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(path.dirname(fileURLToPath(import.meta.url)),'closing_weighted_tail.mjs')));
const read=JSON.parse((input.endsWith('.gz')?gunzipSync(fs.readFileSync(input)):fs.readFileSync(input)).toString()),r=read.response??read,cp=r.checkpoint??r,fac=createRecalibrationFactory(read.config??cp.parameters),tail=fac.assemble(),rows=[];
for(let n=0;n<tail.parameters.protectCell;n++){
 const e=fac.getEntries(n,tail.parameters.valleyControls[n]??0),v=e.total;
 rows.push({n,A:v[0],B:v[1],AH:v[4],BH:v[5],width:v[0]+tail.stats.alpha*v[1],height:v[4]+tail.stats.alpha*v[5],calibrationAlpha:fac.source.cells[n].cal.alpha,segments:n===0?e.entries.map(x=>({j:x.j,A:x.total[0],B:x.total[1],AH:x.total[4],BH:x.total[5]})):undefined});
}
const rest=rows.slice(1).reduce((s,v)=>{for(const k of ['A','B','AH','BH','width','height'])s[k]+=v[k];return s;},{A:0,B:0,AH:0,BH:0,width:0,height:0});
const report={scope:'Numerical source-integral bookkeeping, not rigorous quadrature',input:path.resolve(input),stats:tail.stats,first:rows[0],rest,rows};fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({alpha:tail.stats.alpha,first:rows[0],rest}));
