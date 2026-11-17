// Export scalar jets from the verified 13-file smallcut background source.
// The Python solver defines its separately named fixed Hermite approximant;
// this exporter does not claim that interpolant equals the original metric.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
const a=process.argv.slice(2),get=(name,fallback=null)=>{const i=a.indexOf(name);return i<0?fallback:a[i+1];};
const source=path.resolve(get('--source')),configPath=path.resolve(get('--config'));
const depth=Number(get('--depth','4')),steps=Number(get('--steps','64')),modes=Number(get('--modes','32'));
const out=path.resolve(get('--out'));
process.env.CLOSING_TAIL_CACHE=path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const file=path.join(source,'scripts/closing_weighted_tail.mjs');
const weighted=await import(pathToFileURL(file).href);
const input=JSON.parse(fs.readFileSync(configPath,'utf8')),config=input.parameters??input;
const begin=performance.now(),factory=weighted.createRecalibrationFactory(config),tail=factory.assemble();
if(depth>tail.cells.length)throw Error('Requested depth exceeds recovered finite source');
const rows=[];
for(let n=depth-1;n>=0;n--)for(let j=0;j<tail.cells[n].profiles.length;j++){
 const f=tail.cells[n].profiles[j];
 for(let k=0;k<=steps;k++){
  const x=k/steps,g=f(x);
  rows.push({r:g.r,logw:g.logw,dlogwdr:g.dlogwdx/g.drdx,cell:n,segment:j,x});
 }
}
const inner=tail.cells[depth-1].profiles[0](0),mu=tail.cells[depth-1].mu;
const boundary=Array.from({length:modes},(_,i)=>{
 const m=2*(i+1),u=1,v=config.orientation*weighted.idealModeGraph(m,config.R??64,config.a??2.75);
 const beta=Math.sqrt(12)*Math.exp(Math.log(mu)-7*Math.log(inner.r)-inner.logw)/m;
 const kp=u,pp=m*u+beta*v,norm=Math.hypot(kp,pp);
 return {frequency:m,p:pp/norm,k:kp/norm,ideal_column:[u,v],mu};
});
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const report={scope:'Actual scalar samples from recovered verified source. The downstream fixed Hermite approximant is a new metric. Inner ideal graph is a finite design boundary, not nonlinear infinite-tail DN.',
 source_recovery:JSON.parse(fs.readFileSync(path.join(source,'recovery.json'),'utf8')),
 source_sha256:sha(fs.readFileSync(new URL(import.meta.url))),config_sha256:sha(fs.readFileSync(configPath)),
 parameters:tail.parameters,stats:tail.stats,depth,steps,modes,seconds:(performance.now()-begin)/1000,
 inner:{r:inner.r,logw:inner.logw,dlogwdr:inner.dlogwdx/inner.drdx},boundary,rows};
fs.writeFileSync(out,JSON.stringify(report)+'\n');
process.stdout.write(JSON.stringify({depth,steps,modes,rows:rows.length,seconds:report.seconds,inner:report.inner,stats:report.stats,output_sha256:sha(fs.readFileSync(out))})+'\n');
