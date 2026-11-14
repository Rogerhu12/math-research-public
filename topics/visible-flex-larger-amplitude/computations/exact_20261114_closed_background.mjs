// Same frozen source primitives for the new refined-tail assembly interface.
// No recalibration, tail ODE or new shooting solve is performed.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';

const opt={};for(let i=2;i<process.argv.length;i+=2)opt[process.argv[i]]=process.argv[i+1];
for(const key of ['--repo-root','--source-topic','--config','--plan','--out'])if(!opt[key])throw Error('Missing '+key);
const started=performance.now(),sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const selfHash=sha(fileURLToPath(import.meta.url));
const repo=path.resolve(opt['--repo-root']),source=path.resolve(opt['--source-topic']);
const topic=path.join(repo,'topics/visible-flex-larger-amplitude'),comp=path.join(topic,'computations'),notes=path.join(topic,'notes');
const config=JSON.parse(fs.readFileSync(opt['--config'],'utf8')),plan=JSON.parse(fs.readFileSync(opt['--plan'],'utf8'));
if(plan.inputs.config.sha256!==sha(opt['--config']))throw Error('Plan and config differ');
Object.assign(process.env,{
 VISIBLE_FLEX_SOURCE_TOPIC:source,VISIBLE_FLEX_SOURCE_ROOT:path.join(source,'repro/source-root'),
 VISIBLE_FLEX_FROZEN_LEDGER_READY:path.join(notes,'2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'),
 VISIBLE_FLEX_FROZEN_STORED_READY:path.join(notes,'2026-11-13-strong-m28-recovered-full-audit-r1-ready.json'),
 VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT:'8',
 CLOSING_TAIL_CACHE:path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts')
});
const {createStoredPhysical}=await import(pathToFileURL(path.join(comp,'tail_frozen_geometry.mjs')).href);
const {physical,factory,manifest}=await createStoredPhysical(config),alpha=physical.stats.alpha;
if(manifest.profileFingerprintAfter!==plan.profile_fingerprint)throw Error('Plan belongs to different background');
const cut=physical.cells[0].profiles.at(-1)(1).r,cuff=physical.parameters.rCuff;
if(cut!==plan.cut||cuff!==plan.cuff)throw Error('Physical closing anchors differ');
const radii=plan.background_radii;
if(!radii.includes(cut)||!radii.includes(cuff)||radii.some(r=>r<cuff||r>cut))throw Error('Invalid requested source radii');
let sum=0,correction=0;
const add=v=>{const y=v-correction,t=sum+y;correction=(t-sum)-y;sum=t;};
const pieces=[];
for(let n=0;n<physical.cells.length;n++){
 const entries=factory.getEntries(n,config.valleyControls?.[n]??0).entries;
 for(let j=entries.length-1;j>=0;j--){
  const entry=entries[j],profile=physical.cells[n].profiles[j];
  const outer=profile(1).r,inner=profile(0).r,heightAtOuter=sum;
  const gain=entry.total[4]+alpha*entry.total[5];add(gain);
  if(outer>inner)pieces.push({n,j,entry,profile,outer,inner,heightAtOuter});
 }
}
const totalHeight=sum;
const jet=g=>{const w=Math.exp(g.logw);return{w,wr:w*g.dlogwdx/g.drdx,E:1+w*w};};
const rows=[];
for(const r of radii){
 if(r===cut){rows.push({r,heightFromRToCut:0,...jet(physical.cells[0].profiles.at(-1)(1)),source:'exact stored cut',radialResidual:0,splitPrimitiveDifference:0});continue;}
 if(r===cuff){rows.push({r,heightFromRToCut:totalHeight,w:0,wr:0,E:1,source:'flat source limit; finite160-cell primitive representative',radialResidual:0,splitPrimitiveDifference:0});continue;}
 const piece=pieces.find(p=>p.inner<=r&&r<=p.outer);
 if(!piece)throw Error('No stored source profile covers requested radius '+r);
 let x;
 if(r===piece.outer)x=1;
 else if(r===piece.inner)x=0;
 else{
  let lo=0,hi=1;
  for(let k=0;k<48;k++){const mid=(lo+hi)/2;if(piece.profile(mid).r<r)lo=mid;else hi=mid;}
  x=(lo+hi)/2;
 }
 const integral=piece.entry.integrate(x,1),mid=(x+1)/2;
 const left=piece.entry.integrate(x,mid),right=piece.entry.integrate(mid,1);
 const height=integral[4]+alpha*integral[5],split=left[4]+right[4]+alpha*(left[5]+right[5]);
 const g=piece.profile(x);
 rows.push({r,heightFromRToCut:piece.heightAtOuter+height,...jet(g),source:'unchanged stored source function',
  cell:piece.n,segment:piece.j,sourceX:x,radialResidual:g.r-r,splitPrimitiveDifference:split-height});
}
const p=physical.parameters,n=160;
const W=p.epsilonScale*p.R*(p.delta0*2**(-n))**(7/4)/cuff**7;
const logWidth=6*p.delta0*2**(-n)+6*p.etaRatioAtN0*p.delta0*2**(-p.etaPower*n)/(1-2**(-p.etaPower));
const deepWidth=cuff*Math.expm1(logWidth/Math.sqrt(12));
const report={schema:'refined-tail-closed-source-background-v1',finished:true,
 source_sha256_at_start:selfHash,inputs:{config:{file:path.resolve(opt['--config']),sha256:sha(opt['--config'])},plan:{file:path.resolve(opt['--plan']),sha256:sha(opt['--plan'])}},
 profile_fingerprint:manifest.profileFingerprintAfter,original_factory_alpha:alpha,
 source_revision:manifest.sourceRevision,source_adapter:manifest,
 cut,cuff,finiteHeightFromCuffToCut:totalHeight,rows,
 maximumInverseRadiusResidual:Math.max(...rows.map(x=>Math.abs(x.radialResidual))),
 maximumSplitPrimitiveDifference:Math.max(...rows.map(x=>Math.abs(x.splitPrimitiveDifference))),
 conditional_rotational_deep_omission:{start:n,formula:'unchanged-source R28: W_n * r_cuff * expm1(remaining_log_radius_n/sqrt(12))',
  slopeRepresentative:W,widthRepresentative:deepWidth,heightRepresentative:W*deepWidth,intervalCertificate:false},
 definition:'The original background is retained as a source function. heightFromRToCut is its native primitive from r to the cut. The flat-cuff value uses all160 saved source cells and records the conditional omitted rotational tail.',
 limitations:['Floating source evaluation and primitives, not interval-certified values.','The nonzero finite nonaxisymmetric collar is separate; no infinite nonlinear solution is implied.'],
 seconds:(performance.now()-started)/1000};
fs.writeFileSync(opt['--out'],JSON.stringify(report)+'\n',{flag:'wx'});
console.log(JSON.stringify({output:opt['--out'],queries:rows.length,totalHeight,
 maximumInverseRadiusResidual:report.maximumInverseRadiusResidual,seconds:report.seconds}));
