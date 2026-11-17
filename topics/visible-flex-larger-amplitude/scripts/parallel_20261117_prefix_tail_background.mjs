// Explicit new metric joining the actual prefix cut jet to an outward cuff.
// The finite Hermite log-slope metric is fixed by the exported scalar jets.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
const argv=process.argv.slice(2),get=(key,fallback=null)=>{const i=argv.indexOf(key);return i<0?fallback:argv[i+1];};
const source=path.resolve(get('--source')),tracePath=path.resolve(get('--trace')),configPath=path.resolve(get('--config'));
const depth=Number(get('--depth','4')),steps=Number(get('--steps','64')),modes=Number(get('--modes','64'));
const width=Number(get('--width','.6')),bridgeWidth=Number(get('--bridge-width','.05')),out=path.resolve(get('--out'));
if(!(width>bridgeWidth&&bridgeWidth>0))throw Error('Need width > bridge-width > 0');
process.env.CLOSING_TAIL_CACHE=path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const weighted=await import(pathToFileURL(path.join(source,'scripts/closing_weighted_tail.mjs')).href);
const trace=JSON.parse(fs.readFileSync(tracePath,'utf8')),original=JSON.parse(fs.readFileSync(configPath,'utf8'));
const r0=trace.r,w0=trace.w,wr0=trace.w_r;
const config={...(original.parameters??original),rCut:r0+bridgeWidth,wCut:w0,width:width-bridgeWidth,orientation:-1,
 curvatureBound:Number(get('--curvature-bound','6'))};
const begin=performance.now(),factory=weighted.createRecalibrationFactory(config),tail=factory.assemble();
if(depth>tail.cells.length)throw Error('Depth exceeds available source');
const sourceRows=[];
for(let n=depth-1;n>=0;n--)for(let j=0;j<tail.cells[n].profiles.length;j++)for(let k=0;k<=steps;k++){
 const x=k/steps,g=tail.cells[n].profiles[j](x);
 sourceRows.push({r:g.r,logw:g.logw,dlogwdr:g.dlogwdx/g.drdx,cell:n,segment:j,x});
}
sourceRows.reverse();
const cut=sourceRows[0],h=cut.r-r0,c0=Math.log(w0),c1=h*wr0/w0,A=cut.logw-c0-c1,B=h*cut.dlogwdr-c1;
const coeff=[c0,c1,3*A-B,B-2*A];
const rows=[];
for(let k=0;k<=steps;k++){
 const x=k/steps,logw=coeff[0]+x*(coeff[1]+x*(coeff[2]+x*coeff[3]));
 const derivative=(coeff[1]+x*(2*coeff[2]+3*x*coeff[3]))/h;
 rows.push({r:r0+h*x,logw,dlogwdr:derivative,cell:-1,segment:0,x});
}
rows.push(...sourceRows.slice(1));
const inner=tail.cells[depth-1].profiles[0](0),mu=tail.cells[depth-1].mu;
const boundary=Array.from({length:modes},(_,i)=>{
 const m=2*(i+1),u=1,v=-weighted.idealModeGraph(m,config.R??64,config.a??2.75);
 const beta=Math.sqrt(12)*Math.exp(Math.log(mu)-7*Math.log(inner.r)-inner.logw)/m;
 const kp=u,pp=m*u+beta*v,norm=Math.hypot(kp,pp);
 return {frequency:m,p:pp/norm,k:kp/norm,ideal_column:[u,v],mu};
});
let maxMeridian=0,maxAngular=0,maxW=0;
for(const row of rows){const w=Math.exp(row.logw),E=1+w*w;maxMeridian=Math.max(maxMeridian,Math.abs(w*row.dlogwdr)/E**1.5);maxAngular=Math.max(maxAngular,w/(row.r*Math.sqrt(E)));maxW=Math.max(maxW,w);}
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const report={scope:'New fixed scalar Hermite background: actual prefix r,w,w_r jet, explicit C1 cubic logw bridge, orientation -1 oscillatory tail toward an outer cuff. The finite ideal deep boundary is not nonlinear infinite-tail DN.',
 source_recovery:JSON.parse(fs.readFileSync(path.join(source,'recovery.json'),'utf8')),
 source_sha256:sha(fs.readFileSync(new URL(import.meta.url))),trace_sha256:sha(fs.readFileSync(tracePath)),config_sha256:sha(fs.readFileSync(configPath)),
 parameters:tail.parameters,stats:tail.stats,depth,steps,modes,width,bridge_width:bridgeWidth,seconds:(performance.now()-begin)/1000,
 shallow_at:'left',deep_at:'right',cut:{r:r0,w:w0,w_r:wr0},bridge:{coefficients:coeff,r0,r1:cut.r},
 inner:{r:inner.r,logw:inner.logw,dlogwdr:inner.dlogwdx/inner.drdx},boundary,rows,
 sampled_background:{maxMeridian,maxAngular,maxW}};
fs.writeFileSync(out,JSON.stringify(report)+'\n');
process.stdout.write(JSON.stringify({depth,steps,rows:rows.length,seconds:report.seconds,cut:report.cut,inner:report.inner,sampled_background:report.sampled_background,stats:report.stats,output_sha256:sha(fs.readFileSync(out))})+'\n');
