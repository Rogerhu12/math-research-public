// Actual centered Cartesian geometry of the COMPUTED finite tail only.
// The deep nonlinear tail, continuous bounds and all-mode limit remain unpaid.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [topic,factoryFile,input,prefixEndpointFile,out,angularArg='128',partsArg='4']=process.argv.slice(2);
process.env.VISIBLE_FLEX_SOURCE_TOPIC=topic;
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
const hash=f=>createHash('sha256').update(fs.readFileSync(f)).digest('hex');
const record=JSON.parse(gunzipSync(fs.readFileSync(input))),cp=record.response.checkpoint;
const cfg={...record.config,quadrature:Number(angularArg)},N=cfg.quadrature,M=cfg.modes,parts=Number(partsArg);
if(cfg.steps%parts)throw Error('Sample parts must divide the integration step count');
const endpoint=JSON.parse(fs.readFileSync(prefixEndpointFile)),Z=endpoint.mean_height;
const {createRecalibrationFactory}=await import(pathToFileURL(factoryFile));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/78718-tail-tangent-split.mjs')));
const {createRelativeSpatialJetEvaluator}=await import(pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,'f6tail_relative_spatial_jets.mjs')));
const {relativeSurfaceGeometry}=await import(pathToFileURL(path.join(process.env.CLOSING_TAIL_CACHE,'f6tail_relative_development.mjs')));
const physical=createRecalibrationFactory(cfg).assemble(),dn=createSplitFluxCompactTailDN({...cfg,tail:physical});
const spans=[],innerMean=[],reflect=v=>[v[0],v[1],-v[2]];
let sum=0;
for(let n=0;n<dn.tail.cells.length;n++){
 const c=dn.tail.cells[n],p=c.profiles[0];let s=new Float64Array(2*M+2);s.set(cp.states[n+1]);
 for(let j=0;j<cfg.steps;j++)s=c.engine.rk4(s,p,j/cfg.steps,1/cfg.steps);
 const h=s[2*M]+s[2*M+1];spans.push(h);sum+=h;innerMean.push(Z+sum);
}
const result={scope:'Sampled actual Cartesian geometry of all computed finite tail stages. The rest of the infinite nonlinear tail and uniform parameter bounds are not certified.',input,input_sha256:hash(input),factory_sha256:hash(factoryFile),prefix_endpoint_sha256:hash(prefixEndpointFile),modes:M,rootAngular:N,steps:cfg.steps,samplesPerStage:parts+1,physicalDepth:cfg.depth,stages:dn.tail.cells.length,backgroundFullHeight:physical.stats.heightSpan,finiteMeanHeightIncrease:sum,maxMetric:0,maxFullTensor:0,maxCurvature:0,minSupport:Infinity,maxRadiusXY:0,maxNorm:0,minZ:Infinity,maxZ:-Infinity,minA:Infinity,minD:Infinity,where:{}};
for(let n=0;n<dn.tail.cells.length;n++){
 const c=dn.tail.cells[n],p=c.profiles[0],ev=createRelativeSpatialJetEvaluator(c.engine,{spacing:cfg.spacing,radialDifferenceStep:1e-4});
 let s=new Float64Array(2*M+2);s.set(cp.states[n+1]);
 for(let k=0;k<=cfg.steps;k++){
  if(k%(cfg.steps/parts)===0){
   const x=k/cfg.steps,v=ev.evaluate(s,p,x),g=v.g,mean=innerMean[n]-s[2*M]-s[2*M+1];
   result.minA=Math.min(result.minA,v.heightJets.minA);result.minD=Math.min(result.minD,v.heightJets.minD);
   for(const a of v.perAngle){
    const C=Math.cos(a.theta),S=Math.sin(a.theta),nonmean=a.V[2]-s[2*M];
    const X=[g.r*C+a.V[0],g.r*S+a.V[1],mean-nonmean];
    const Xr=reflect([C+a.Vr[0],S+a.Vr[1],g.w+a.Vr[2]]),Xt=reflect([-g.r*S+a.Vt[0],g.r*C+a.Vt[1],a.Vt[2]]);
    const normal=[Xr[1]*Xt[2]-Xr[2]*Xt[1],Xr[2]*Xt[0]-Xr[0]*Xt[2],Xr[0]*Xt[1]-Xr[1]*Xt[0]],area=Math.hypot(...normal),support=X.reduce((t,z,j)=>t+z*normal[j]/area,0);
    const geo=relativeSurfaceGeometry(g,a.theta,a.Vr,a.Vt,a.Vrr,a.Vrt,a.Vtt),where={stage:n,cell:c.rawCell,segment:c.rawSegment,x,u:a.theta,r:g.r,w:g.w};
    for(const [key,value]of [['maxMetric',geo.metric],['maxFullTensor',geo.fullTensorFrobeniusBound],['maxCurvature',geo.actualCurvature],['maxRadiusXY',Math.hypot(X[0],X[1])],['maxNorm',Math.hypot(...X)]])if(value>result[key]){result[key]=value;result.where[key]=where;}
    if(support<result.minSupport){result.minSupport=support;result.where.minSupport=where;}
    result.minZ=Math.min(result.minZ,X[2]);result.maxZ=Math.max(result.maxZ,X[2]);
   }
  }
  if(k<cfg.steps)s=c.engine.rk4(s,p,k/cfg.steps,1/cfg.steps);
 }
}
result.maxHeightAboveCut=result.maxZ-Z;
fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
