// Independent audit input export only; does not change the constructed metric.
import fs from 'node:fs/promises';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {createCutPreservingTail} from './root_cut_preserving_tail.mjs';
const [input,output]=process.argv.slice(2);
if(!input||!output)throw Error('config.json output.json.gz');
const config=JSON.parse(await fs.readFile(input,'utf8'));
const tail=createCutPreservingTail(config);
const source=tail.source.cells.map((c,n)=>({n,mu:c.mu,delta:c.delta,R:c.R,calibratedAlpha:c.cal.alpha,
 profiles:c.profiles.map(p=>{const a=p(0),b=p(.5),k=a.drdx/a.r;return {r0:a.r,k,logw0:a.logw,
 logSmoothCoefficient:(b.dlogwdx+7*k)/(15/8)};})}));
const samples=[];
for(const n of [0,1,7,15,31,tail.cells.length-1])for(let j=0;j<tail.cells[n].profiles.length;j++)
 for(const x of [0,.13,.25,.5,.77,1])samples.push({n,j,x,...tail.cells[n].profiles[j](x)});
const hashes={};
for(const name of ['root_cut_preserving_tail.mjs','root_cut_tail_linear.mjs','root_cut_tail_general_linear.mjs']){
 const url=new URL(name,import.meta.url);hashes[name]=crypto.createHash('sha256').update(await fs.readFile(url)).digest('hex');
}
const out={scope:'Raw source coefficients and frozen metric comparison samples for independent audit; not a solution certificate',config,parameters:tail.parameters,source,rootStats:tail.stats,samples,hashes};
await fs.writeFile(output,zlib.gzipSync(JSON.stringify(out)));
console.log(JSON.stringify({output,sourceCells:source.length,comparisonSamples:samples.length,hashes}));
