// Same stored metric as accepted A: retain h0'(r)=w(r) as a source function.
// Only scalar background primitives and jets are evaluated here. No point-root,
// nonlinear ODE, shooting solve, or recalibration is performed.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const opt={};
for(let i=2;i<process.argv.length;i+=2)opt[process.argv[i]]=process.argv[i+1];
for(const k of ['--repo-root','--source-topic','--out'])if(!opt[k])throw Error('Missing '+k);
const repo=path.resolve(opt['--repo-root']),source=path.resolve(opt['--source-topic']);
const topic=path.join(repo,'topics/visible-flex-larger-amplitude'),comp=path.join(topic,'computations'),notes=path.join(topic,'notes');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const configPath=path.join(notes,'2026-11-13-strong-q126-m32-tail2-actual-r1-config.json');
const configBytes=fs.readFileSync(configPath),config=JSON.parse(configBytes);
if(sha(configBytes)!=='3b0deaaf0cdc65a34a8e4652e0a04d96a840db354ccada71d9cba5e4cd228e23')throw Error('Original A config required');
const ledger=path.join(notes,'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json');
const stored=path.join(notes,'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json');
Object.assign(process.env,{
  VISIBLE_FLEX_SOURCE_TOPIC:source,
  VISIBLE_FLEX_SOURCE_ROOT:path.join(source,'repro/source-root'),
  VISIBLE_FLEX_FROZEN_LEDGER_READY:ledger,
  VISIBLE_FLEX_FROZEN_STORED_READY:stored,
  VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT:'8',
  CLOSING_TAIL_CACHE:path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts')
});
const {createStoredPhysical}=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')).href);
const {subdividePhysical}=await import(pathToFileURL(path.join(source,'scripts/950f-tail-subdivision.mjs')).href);
const {integrationGrid}=await import(pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,'f6tail_cusp_grid.mjs')).href);
const start=performance.now(),{physical,factory,manifest}=await createStoredPhysical(config);
const stages=subdividePhysical(physical,config.depth,config.shootingParts);
if(stages.cells.length!==576)throw Error('Expected original 576 stages');
const alpha=physical.stats.alpha;
const primitive=(entry,a,b)=>{const v=entry.integrate(a,b);return v[4]+alpha*v[5];};
const geom=(profile,x)=>{
  const g=profile(x),w=Math.exp(g.logw),w2=Math.exp(2*g.logw);
  if(!(g.r>0&&g.drdx>0&&w>0))throw Error('Invalid background');
  return {x,r:g.r,w,w2,E:1+w2,wr:w*g.dlogwdx/g.drdx,drdx:g.drdx,dlogwdx:g.dlogwdx};
};
function rkBackground(profile,steps){
  const cuts=profile.integrationBreakpoints??[],grid=cuts.length?integrationGrid(steps,cuts):null;
  const f=x=>{const q=profile(x);return Math.exp(q.logw)*q.drdx;};
  let total=0;
  const ordinaryH=1/steps,count=grid?grid.length-1:steps;
  for(let i=0;i<count;i++){
    const a=grid?grid[i]:i*ordinaryH,h=grid?grid[i+1]-grid[i]:ordinaryH;
    const A=f(a),B=f(a+h/2),D=f(a+h);
    total+=h*(A+2*B+2*B+D)/6;
  }
  return total;
}
const rows=[];
for(let si=0;si<576;si++){
  const c=stages.cells[si],p=c.profiles[0];
  const entry=factory.getEntries(c.rawCell,config.valleyControls?.[c.rawCell]??0).entries[c.rawSegment];
  const a=c.rawLeft,b=c.rawRight,m=(a+b)/2;
  const native=primitive(entry,a,b),split=primitive(entry,a,m)+primitive(entry,m,b);
  rows.push({stage:si,rawCell:c.rawCell,rawSegment:c.rawSegment,rawLeft:a,rawRight:b,
    nativeHeightIncrement:native,splitHeightIncrement:split,nativeSplitDifference:split-native,
    rk12HeightIncrement:rkBackground(p,12),rk24HeightIncrement:rkBackground(p,24),
    integrationBreakpoints:p.integrationBreakpoints??[],
    points:Array.from({length:17},(_,j)=>geom(p,j/16))});
}
const nodeHeight=new Float64Array(577),nodeRK12=new Float64Array(577),nodeRK24=new Float64Array(577);
for(let i=575;i>=0;i--){
  nodeHeight[i]=nodeHeight[i+1]+rows[i].nativeHeightIncrement;
  nodeRK12[i]=nodeRK12[i+1]+rows[i].rk12HeightIncrement;
  nodeRK24[i]=nodeRK24[i+1]+rows[i].rk24HeightIncrement;
}
const out={schema:'accepted-A-source-background-preserving-data-v1',finished:true,
  source_sha256:sha(fs.readFileSync(new URL(import.meta.url))),original_config_sha256:sha(configBytes),
  ledger_sha256:sha(fs.readFileSync(ledger)),stored_reference_sha256:sha(fs.readFileSync(stored)),
  original_profile_fingerprint:manifest.profileFingerprintAfter,
  original_factory_alpha:alpha,stages:576,samples_per_stage:17,
  nodeHeightInnerAnchor:Array.from(nodeHeight),nodeRK12HeightInnerAnchor:Array.from(nodeRK12),
  nodeRK24HeightInnerAnchor:Array.from(nodeRK24),rows,
  maximumNativeSplitDifference:Math.max(...rows.map(r=>Math.abs(r.nativeSplitDifference))),
  nativeMinusRK12AtCut:nodeHeight[0]-nodeRK12[0],nativeMinusRK24AtCut:nodeHeight[0]-nodeRK24[0],
  seconds:(performance.now()-start)/1000,
  definition:'h0(r)=integral from the original node576 radius to r of w(s) ds. w and wr use unchanged source profiles. Native primitives use original entry.integrate; split differences are numerical diagnostics.',
  limitations:['All primitives and profile jets are floating evaluations, not interval bounds.',
    'No new nonlinear tail or closed surface is claimed.']};
fs.writeFileSync(opt['--out'],JSON.stringify(out)+'\n',{flag:'wx'});
console.log(JSON.stringify({file:opt['--out'],stages:576,seconds:out.seconds,
  maximumNativeSplitDifference:out.maximumNativeSplitDifference,
  nativeMinusRK12AtCut:out.nativeMinusRK12AtCut,nativeMinusRK24AtCut:out.nativeMinusRK24AtCut}));
