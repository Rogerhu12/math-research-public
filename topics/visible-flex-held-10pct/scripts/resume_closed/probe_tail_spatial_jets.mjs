// Locate and separate the physical-r second-jet finite-difference error.
// No BVP/Newton equation or checkpoint value is changed.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';
const {values}=parseArgs({options:{'source-topic':{type:'string'},'checkpoint':{type:'string'},'radii':{type:'string'},'out':{type:'string'},'dump-jets':{type:'string'},'steps':{type:'string',default:'64'},'difference-steps':{type:'string',default:'.0002,.0001,.00005,.000025,.0000125,.00000625'}}});
for(const x of ['source-topic','checkpoint','radii','out'])if(!values[x])throw Error('Missing '+x);
const topic=path.resolve(values['source-topic']),src=path.join(topic,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
process.env.CLOSING_TAIL_CACHE=src;process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
const read=f=>JSON.parse(f.endsWith('.gz')?gunzipSync(fs.readFileSync(f)):fs.readFileSync(f));
const raw=read(values.checkpoint),cp=raw.response?.checkpoint??raw.checkpoint??raw,p=cp.parameters,M=p.modes,K=2*M,N=p.quadrature??256;
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-subdivision.mjs')));
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(src,'f6tail_fast_split_flux_engine.mjs')));
const {withCuspAwareRK}=await import(pathToFileURL(path.join(src,'f6tail_cusp_grid.mjs')));
const {createRelativeSpatialJetEvaluator}=await import(pathToFileURL(path.join(src,'f6tail_relative_spatial_jets.mjs')));
const {relativeSurfaceGeometry}=await import(pathToFileURL(path.join(src,'f6tail_relative_development.mjs')));
const factory=createRecalibrationFactory(raw.config??p),physical=factory.assemble(),stages=subdividePhysical(physical,p.physicalDepth??p.depth,p.shootingParts??1),steps=+values.steps;
const hs=values['difference-steps'].split(',').map(Number),reports=[],jetDump=[];
for(const radius of values.radii.split(',').map(Number)){
 const n=stages.cells.findIndex(c=>radius>=c.profiles[0](0).r&&radius<=c.profiles[0](1).r);
 if(n<0)throw Error('No source stage for radius '+radius);
 const cell=stages.cells[n],profile=cell.profiles[0];let lo=0,hi=1;
 for(let k=0;k<50;k++){const mid=(lo+hi)/2;if(profile(mid).r<radius)lo=mid;else hi=mid;}
 const x=(lo+hi)/2,engine=withCuspAwareRK(createFastSplitFluxMomentumTailEngine({modes:M,spacing:p.spacing,quadrature:N,mu:cell.mu,orientation:p.orientation,projectionFloor:p.projectionFloor}));
 let state=new Float64Array(K+2);state.set(cp.states[n+1]);
 const xs=[0,...Array.from({length:Math.floor(x*steps)},(_,j)=>(j+1)/steps).filter(y=>y<x),...(profile.integrationBreakpoints??[]).filter(y=>y>0&&y<x),x].sort((a,b)=>a-b);
 for(let k=1;k<xs.length;k++)if(xs[k]>xs[k-1])state=engine.rk4(state,profile,xs[k-1],xs[k]-xs[k-1]);
 const jets=hs.map(h=>createRelativeSpatialJetEvaluator(engine,{spacing:p.spacing,radialDifferenceStep:h}).evaluate(state,profile,x));
 jetDump.push({radius,sourceRadius:profile(x).r,differenceStep:hs[0],jets:jets[0].perAngle.map(q=>({theta:q.theta,Vr:q.Vr,Vrr:q.Vrr}))});
 const rows=[];
 for(let i=0;i<hs.length;i++){
  let tensor=0,metric=0,curvature=0,second=0,diff=0;
  for(let j=0;j<N;j++){
   const q=jets[i].perAngle[j],g=relativeSurfaceGeometry(jets[i].g,q.theta,q.Vr,q.Vt,q.Vrr,q.Vrt,q.Vtt);
   tensor=Math.max(tensor,g.fullTensorFrobeniusBound);metric=Math.max(metric,g.metric);curvature=Math.max(curvature,g.actualCurvature);
   second=Math.max(second,Math.hypot(...q.Vrr));
   if(i)diff=Math.max(diff,Math.hypot(...q.Vrr.map((v,k)=>v-jets[i-1].perAngle[j].Vrr[k])));
  }
  rows.push({differenceStep:hs[i],metric,fullTensor:tensor,curvature,secondPerturbationNorm:second,secondDifferenceFromPrevious:i?diff:null});
 }
 const out={radius,stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,rawLeft:cell.rawLeft,rawRight:cell.rawRight,x,sourceRadius:profile(x).r,integrationBreakpoints:profile.integrationBreakpoints,sourceDrdx:profile(x).drdx,rows};reports.push(out);console.log(JSON.stringify(out));
}
if(values['dump-jets'])fs.writeFileSync(values['dump-jets'],JSON.stringify(jetDump)+'\n');
const sha=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
fs.writeFileSync(values.out,JSON.stringify({scope:'Same accepted checkpoint and reconstructed physical stage state; only source finite-difference step changes. Numerical diagnostic, not a new solution.',command:process.argv,checkpoint_sha256:sha(values.checkpoint),source_sha256:sha(new URL(import.meta.url)),source_files:Object.fromEntries(['f6tail_relative_spatial_jets.mjs','f6tail_relative_development.mjs','f6tail_momentum_physical_jets.mjs'].map(f=>[f,sha(path.join(src,f))])),steps,rows:reports},null,2)+'\n');
