// Export a fixed physical cell and independent original-momentum traces.
// Regenerated states and angular jets are scratch-only data.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const [topicArg,inputArg,outArg,intervalsArg='8',referenceStepsArg='128',rawCellArg='0']=process.argv.slice(2);
const topic=path.resolve(topicArg),input=path.resolve(inputArg),out=path.resolve(outArg);
const intervals=Number(intervalsArg),referenceSteps=Number(referenceStepsArg),rawCell=Number(rawCellArg);
if(!(Number.isInteger(intervals)&&intervals>0&&Number.isInteger(referenceSteps)&&referenceSteps>0))throw Error('Invalid resolution');
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const original=process.env.CLOSING_TAIL_CACHE;
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-subdivision.mjs')));
const {createMomentumTailEngine}=await import(pathToFileURL(path.join(original,'general_root_tail_momentum.mjs')));
const {createMomentumPhysicalJetEvaluator}=await import(pathToFileURL(path.join(original,'f6tail_momentum_physical_jets.mjs')));
const {withCuspAwareRK}=await import(pathToFileURL(path.join(original,'f6tail_cusp_grid.mjs')));
const digest=file=>createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const rec=JSON.parse(gunzipSync(fs.readFileSync(input))),cp=rec.response?.checkpoint??rec.checkpoint??rec;
const cfg=rec.config??cp.parameters,M=cp.parameters.modes,N=cp.parameters.quadrature,spacing=cp.parameters.spacing;
const physical=createRecalibrationFactory(cfg).assemble();
if(cp.parameters.constructor!=='closing_weighted_tail_v1')throw Error('This exporter is for the original physical constructor');
const stages=subdividePhysical(physical,cp.parameters.physicalDepth??cfg.depth,cfg.shootingParts??1);
if(JSON.stringify(stages.rawNode)!==JSON.stringify(cp.rawNode))throw Error('Physical stage indexing differs from checkpoint');
const first=cp.rawNode[rawCell],last=cp.rawNode[rawCell+1],cell=physical.cells[rawCell];
const engine=withCuspAwareRK(createMomentumTailEngine({modes:M,quadrature:N,spacing,mu:cell.mu,orientation:1,projectionFloor:cp.parameters.projectionFloor}));
const jets=createMomentumPhysicalJetEvaluator(engine,{spacing}),rOuter=stages.cells[first].profiles[0](1).r;
function checkpointState(n,stage,outer){
 const y=new Float64Array(2*M+2);y.set(cp.states[n]);
 if(outer)for(let j=0;j<M;j++)y[M+j]*=stage.portRatio;
 return y;
}
function mixed(y,root){
 const g=root.g,v=Array.from(y.slice(0,M),a=>g.r**3*a/(Math.SQRT2*g.w));
 const t=Array.from(y.slice(M,2*M),a=>Math.sqrt(12)*cell.mu*a/(Math.SQRT2*g.r**4*g.w2));
 return [...v,...t,...root.L];
}
function invertRadius(p,r){
 const a=p(0).r,b=p(1).r;
 if(r<=a)return 0;if(r>=b)return 1;
 let lo=0,hi=1;
 for(let k=0;k<54;k++){const m=(lo+hi)/2;if(p(m).r<r)lo=m;else hi=m;}
 return (lo+hi)/2;
}
const nodes=[],stageReports=[],links=[];
for(let n=first;n<last;n++){
 const stage=stages.cells[n],p=stage.profiles[0];
 if(stage.mu!==cell.mu)throw Error('Unexpected mu change inside a physical cell');
 const target=[];
 for(let j=0;j<intervals;j++){
  const l=p(j/intervals).r,r=p((j+1)/intervals).r;
  if(j===0)target.push({r:l,t:j/intervals});
  target.push({r:(l+r)/2,t:invertRadius(p,(l+r)/2)},{r,t:(j+1)/intervals});
 }
 let y=checkpointState(n+1,stage,false),previous=0;
 const trace=[];let maxFlowResidual=0;
 for(let j=0;j<target.length;j++){
  const a=target[j],parts=Math.max(1,Math.ceil((a.t-previous)*referenceSteps));
  if(a.t>previous)for(let k=0;k<parts;k++)y=engine.rk4(y,p,previous+(a.t-previous)*k/parts,(a.t-previous)/parts);
  previous=a.t;
  let selected=y;
  if(j===target.length-1){
   selected=checkpointState(n,stage,true);
   const re=engine.root(y,p,1),ce=engine.root(selected,p,1),fy=mixed(y,re),cy=mixed(selected,ce);
   maxFlowResidual=Math.max(...fy.map((v,k)=>Math.abs(v-cy[k])));
  }
  const rt=engine.root(selected,p,a.t),g=rt.g,jt=jets(selected,p,a.t),Y=mixed(selected,rt);
  trace.push({x:rOuter-g.r,r:g.r,w:g.w,wr:g.w*g.dlogwdx/g.drdx,
    local_parameter:a.t,stage:n,raw_segment:stage.rawSegment,Y,
    Lr:jt.Ldot.map(v=>v/g.drdx),
    height_jets:jt.perAngle.map(v=>[v.height-selected[2*M]-selected[2*M+1],v.ur,v.ut,v.urr,v.urt,v.utt]),
    reference_audit:{root_relative:jt.rootRelativeResidual,minA:jt.minA,minD:jt.minD,minS:rt.e.minS,
      gauss_defect:jt.maxDarboux,formal_curvature:jt.formalHeightCurvature,holonomy:jt.physicalHolonomyResidual}});
 }
 trace.reverse();
 if(nodes.length){
  const l=nodes.at(-1),r=trace[0];
  if(Math.abs(l.r-r.r)>1e-13)throw Error('Nonmatching physical profile radii');
  links.push({stage:n,r:l.r,position_error:Math.abs(l.r-r.r),w_error:Math.abs(l.w-r.w),wr_error:Math.abs(l.wr-r.wr),
    mixed_state_error:Math.max(...l.Y.map((v,j)=>Math.abs(v-r.Y[j]))),
    height_second_error:Math.max(...l.height_jets.map((v,j)=>Math.abs(v[3]-r.height_jets[j][3])))});
  trace.shift();
 }
 nodes.push(...trace);
 stageReports.push({stage:n,raw_segment:stage.rawSegment,part:stage.part,mu:stage.mu,portRatio:stage.portRatio,
  r_inner:p(0).r,r_outer:p(1).r,reference_endpoint_state_error:maxFlowResidual,
  minA:Math.min(...trace.map(v=>v.reference_audit.minA)),minD:Math.min(...trace.map(v=>v.reference_audit.minD)),
  gauss_defect:Math.max(...trace.map(v=>v.reference_audit.gauss_defect)),formal_curvature:Math.max(...trace.map(v=>v.reference_audit.formal_curvature))});
 console.log(JSON.stringify({event:'stage_exported',...stageReports.at(-1)}));
}
const sources=['scripts/closing_weighted_tail.mjs','scripts/950f-tail-subdivision.mjs',
 'repro/source-root/topics/large-amplitude-twist-flex/scripts/general_root_tail_momentum.mjs',
 'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_momentum_physical_jets.mjs',
 'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs'];
const doc={scope:'One complete fixed physical cell of the accepted finite tail; original momentum flow is an independent reference, not a continuous geometric certificate.',
 input,checkpoint_sha256:digest(input),source_sha256:Object.fromEntries(sources.map(f=>[f,digest(path.join(topic,f))])),
 exporter_sha256:digest(process.argv[1]),parameters:{M,N,spacing,rawCell,firstStage:first,lastStageExclusive:last,mu:cell.mu,intervalsPerStage:intervals,referenceStepsPerStage:referenceSteps,
  originalProjectionFloor:cp.parameters.projectionFloor,mixedProjectionFloor:.01,coordinate:'x = outer radius - r; r_x=-1',boundary:'outer v and inner t from the accepted complete checkpoint'},
 stages:stageReports,joins:links,nodes};
fs.mkdirSync(path.dirname(out),{recursive:true});fs.writeFileSync(out,gzipSync(JSON.stringify(doc)));
console.log(JSON.stringify({event:'completed',out,sha256:digest(out),nodes:nodes.length,stages:stageReports.length}));
