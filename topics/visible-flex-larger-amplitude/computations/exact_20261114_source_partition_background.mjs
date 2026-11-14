// Original source background on a uniform refinement plus retained source knots.
// No new metric, interpolation of the background, tail solve or ODE flow.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';
import{pathToFileURL,fileURLToPath}from'node:url';
const opt={};for(let i=2;i<process.argv.length;i+=2)opt[process.argv[i]]=process.argv[i+1];
for(const k of ['--repo-root','--source-topic','--config','--complete','--out'])if(!opt[k])throw Error('Missing '+k);
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const repo=path.resolve(opt['--repo-root']),source=path.resolve(opt['--source-topic']),topic=path.join(repo,'topics/visible-flex-larger-amplitude');
const notes=path.join(topic,'notes'),comp=path.join(topic,'computations'),config=JSON.parse(fs.readFileSync(opt['--config'],'utf8')),
  complete=JSON.parse(fs.readFileSync(opt['--complete'],'utf8')),samples=Number(opt['--samples-per-span']??17);
if(!complete.finished||!Number.isInteger(samples)||samples<3||!complete.input_sha256||!Object.values(complete.input_sha256).includes(sha(opt['--config'])))throw Error('Completed matching readout/config required');
Object.assign(process.env,{VISIBLE_FLEX_SOURCE_TOPIC:source,VISIBLE_FLEX_SOURCE_ROOT:path.join(source,'repro/source-root'),
 VISIBLE_FLEX_FROZEN_LEDGER_READY:path.join(notes,'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'),
 VISIBLE_FLEX_FROZEN_STORED_READY:path.join(notes,'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json'),
 VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT:'8',CLOSING_TAIL_CACHE:path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts')});
const sourceHashes=Object.fromEntries([fileURLToPath(import.meta.url),path.join(comp,'tail_frozen_geometry.mjs'),path.join(source,'scripts/950f-tail-subdivision.mjs')].map(p=>[p,sha(p)]));
const inputs=Object.fromEntries(['--config','--complete'].map(k=>[path.resolve(opt[k]),sha(opt[k])])),started=performance.now();
const{createStoredPhysical}=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')));
const{subdividePhysical}=await import(pathToFileURL(path.join(source,'scripts/950f-tail-subdivision.mjs')));
const{physical,factory,manifest}=await createStoredPhysical(config),stages=subdividePhysical(physical,config.depth,config.shootingParts),factor=complete.refinement;
if(manifest.profileFingerprintAfter!==complete.original_profile_fingerprint||!Number.isInteger(factor)||factor<1)throw Error('Source fingerprint/refinement differs');
const additions=complete.source_knot_refinement?.additions??[],rows=[],radii=[];
const geom=(p,x)=>{const q=p(x),w=Math.exp(q.logw),w2=Math.exp(2*q.logw);return{r:q.r,w,w2,E:1+w2,wr:w*q.dlogwdx/q.drdx,drdx:q.drdx,dlogwdx:q.dlogwdx};};
for(let si=0;si<stages.cells.length;si++){
 const c=stages.cells[si],p=c.profiles[0],extra=additions.filter(q=>q.stage===si).map(q=>q.x);
 if(extra.some(x=>!(p.integrationBreakpoints??[]).some(y=>Math.abs(x-y)<1e-13)))throw Error('An added knot is not an original source integration breakpoint');
 const grid=Array.from({length:factor+1},(_,j)=>j/factor).concat(extra).sort((a,b)=>a-b);
 if(grid.some((x,j)=>j&&!(x>grid[j-1])))throw Error('Repeated partition point');
 const entry=factory.getEntries(c.rawCell,config.valleyControls?.[c.rawCell]??0).entries[c.rawSegment];
 if(si===0)radii.push(p(1).r);
 for(let j=grid.length-2;j>=0;j--){
  const a=grid[j],b=grid[j+1],primitive=entry.integrate(c.rawLeft+(c.rawRight-c.rawLeft)*a,c.rawLeft+(c.rawRight-c.rawLeft)*b);
  rows.push({stage:rows.length,originalStage:si,uniformBaselineRefinement:factor,sourceProfileLeft:a,sourceProfileRight:b,
   nativeHeightIncrement:primitive[4]+physical.stats.alpha*primitive[5],
   points:Array.from({length:samples},(_,k)=>({...geom(p,a+(b-a)*k/(samples-1)),x:k/(samples-1)}))});
  radii.push(p(a).r);
 }
}
if(rows.length+1!==complete.rows.length)throw Error('Partition has another node count');
let maximumNodeRadiusDiscrepancy=0;
for(let i=0;i<radii.length;i++)maximumNodeRadiusDiscrepancy=Math.max(maximumNodeRadiusDiscrepancy,Math.abs(radii[i]-complete.rows[i].geometry.r));
if(maximumNodeRadiusDiscrepancy>16*Number.EPSILON)throw Error('Readout node radii differ from declared source partition');
const native=new Float64Array(rows.length+1);for(let i=rows.length-1;i>=0;i--)native[i]=native[i+1]+rows[i].nativeHeightIncrement;
const result={schema:'same-source-background-on-retained-cusp-partition-v1',finished:true,original_profile_fingerprint:manifest.profileFingerprintAfter,
 stages:rows.length,samples_per_stage:samples,nodeHeightInnerAnchor:Array.from(native),rows,uniform_baseline_refinement:factor,
 retained_source_knots:additions,maximumNodeRadiusDiscrepancy,source_sha256_at_start:sourceHashes,input_sha256:inputs,
 unchanged_source_function:true,background_interpolated:false,seconds:(performance.now()-started)/1000};
fs.writeFileSync(opt['--out'],JSON.stringify(result)+'\n',{flag:'wx'});
console.log(JSON.stringify({event:'complete',out:opt['--out'],stages:rows.length,sourceKnots:additions.length,maximumNodeRadiusDiscrepancy,seconds:result.seconds}));
