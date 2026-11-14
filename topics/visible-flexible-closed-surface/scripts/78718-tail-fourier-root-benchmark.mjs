// Actual fixed-state and one short-stage comparison; no DN or BVP solve.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
import {geometricWarmRemesh} from './78718-tail-geometric-warm-remesh.mjs';
import {createFourierRootSplitFluxEngine} from './78718-tail-fourier-root-split-engine.mjs';
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs')));
const args=process.argv.slice(2),opt={};
for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.packet||!opt.out||fs.existsSync(opt.out))throw Error('input and fresh output required');
const started=Date.now(),buf=fs.readFileSync(opt.packet),packet=JSON.parse(zlib.gunzipSync(buf)),
 M=Number(opt.modes??22),N=Number(opt.quadrature??512),repeat=Number(opt.repeat??20),
 cfg={...packet.config,modes:M,quadrature:N},physical=createRecalibrationFactory(cfg).assemble(),
 stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),originalEngines=new Map(),fastEngines=new Map();
const cells=stages.cells.map(c=>{
 if(!originalEngines.has(c.mu)){
  const options={modes:M,spacing:cfg.spacing,quadrature:N,mu:c.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05};
  originalEngines.set(c.mu,createFastSplitFluxMomentumTailEngine(options));
  fastEngines.set(c.mu,createFourierRootSplitFluxEngine(options));
 }
 return {...c,engine:originalEngines.get(c.mu)};
});
const dn={tail:{physical,cells,rawNode:stages.rawNode,parameters:{...physical.parameters,
 modes:M,quadrature:N,spacing:cfg.spacing,orientation:cfg.orientation,depth:cells.length,
 physicalDepth:cfg.depth,shootingParts:cfg.shootingParts,projectionFloor:cfg.projectionFloor??.05}}};
const converted=geometricWarmRemesh(packet.response.checkpoint,dn,createFastSplitFluxMomentumTailEngine);
function maxGap(a,b){let err=0,mag=0;for(let k=0;k<a.length;k++){err=Math.max(err,Math.abs(a[k]-b[k]));mag=Math.max(mag,Math.abs(a[k]));}return {maxAbsolute:err,oldMaxMagnitude:mag,maxNormRelative:err/Math.max(1e-300,mag)};}
function scaledMatrixGap(a,b,y){
 const qScale=Math.max(1e-250,...Array.from(y.slice(0,M),Math.abs)),
  piScale=Math.max(1e-250,...Array.from(y.slice(M,2*M),Math.abs));
 let shape=0,mean=0;
 for(let i=0;i<2*M+2;i++){
  let err=0,mag=0;
  for(let j=0;j<2*M;j++){
   const aa=a[i*2*M+j],bb=b[i*2*M+j],scale=j<M?qScale:piScale;
   err+=Math.abs(aa-bb)*scale;mag+=Math.abs(aa)*scale;
  }
  const rel=err/Math.max(1e-300,mag);if(i<2*M)shape=Math.max(shape,rel);else mean=Math.max(mean,rel);
 }
 return {...maxGap(a,b),maxScaledShapeRow:shape,maxScaledMeanRow:mean};
}
const rows=[];
for(const node of [0,16,31,34,40,72,144,288,576,864]){
 const c=cells[node===0?0:node-1],p=node===0?c.profiles.at(-1):c.profiles[0],
  x=node===0?1:0,y=new Float64Array(2*M+2),old=c.engine,fast=fastEngines.get(c.mu);
 y.set(converted.states[node]);if(node===0)for(let j=M;j<2*M;j++)y[j]*=c.portRatio;
 for(let k=0;k<3;k++){old.rhsWithJacobian(y,p,x);fast.rhsWithJacobian(y,p,x);}
 const a=old.rhsWithJacobian(y,p,x),b=fast.rhsWithJacobian(y,p,x);
 const t0=performance.now();for(let k=0;k<repeat;k++)old.root(y,p,x);
 const t1=performance.now();for(let k=0;k<repeat;k++)fast.root(y,p,x);
 const t2=performance.now();for(let k=0;k<repeat;k++)old.rhsWithJacobian(y,p,x);
 const t3=performance.now();for(let k=0;k<repeat;k++)fast.rhsWithJacobian(y,p,x);
 const t4=performance.now();
 const row={node,rawCell:c.rawCell,r:a.root.g.r,
  root:{originalMilliseconds:(t1-t0)/repeat,fourierMilliseconds:(t2-t1)/repeat,
   speedup:(t1-t0)/(t2-t1),lambdaGap:maxGap(a.root.L,b.root.L),
   BGap:maxGap(a.root.e.B,b.root.e.B),
   oldIterations:a.root.iterations,newIterations:b.root.iterations,
   oldRelativeResidual:a.root.err/a.root.scale,newRelativeResidual:b.root.err/b.root.scale},
  completeJacobian:{originalMilliseconds:(t3-t2)/repeat,fourierMilliseconds:(t4-t3)/repeat,speedup:(t3-t2)/(t4-t3),
   rhsGap:maxGap(a.derivative,b.derivative),matrixGap:scaledMatrixGap(a.jacobian,b.jacobian,y)}};
 rows.push(row);
}
const stage=Number(opt.stage??31),c=cells[stage],y=new Float64Array(2*M+2);y.set(converted.states[stage+1]);
const t0=performance.now(),a=c.engine.flowStateWithJacobian(y,c.profiles,{stepsPerSegment:cfg.steps}),
 t1=performance.now(),b=fastEngines.get(c.mu).flowStateWithJacobian(y,c.profiles,{stepsPerSegment:cfg.steps}),t2=performance.now();
const flow={stage,rawCell:c.rawCell,rawSegment:c.rawSegment,steps:cfg.steps,
 originalMilliseconds:t1-t0,fourierMilliseconds:t2-t1,speedup:(t1-t0)/(t2-t1),
 stateGap:maxGap(a.state,b.state),tangentGap:scaledMatrixGap(a.tangent,b.tangent,y),
 oldGuards:{minA:a.minA,minD:a.minD,maxRootRelative:a.maxRootRelative},
 newGuards:{minA:b.minA,minD:b.minD,maxRootRelative:b.maxRootRelative}};
const sources={};
for(const name of ['78718-tail-fourier-root-momentum.mjs','78718-tail-fourier-root-split-engine.mjs','78718-tail-fourier-product-jacobian.mjs','78718-tail-fourier-product-flow.mjs']){
 const bytes=fs.readFileSync(new URL(name,import.meta.url));sources[name]={bytes:bytes.length,sha256:crypto.createHash('sha256').update(bytes).digest('hex')};
}
const report={scope:'Fixed geometric warm states, original root policy and physical equations; finite comparisons only, no new tail or BVP.',
 packet:{path:path.resolve(opt.packet),sha256:crypto.createHash('sha256').update(buf).digest('hex')},
 modes:M,quadrature:N,repeat,sources,rows,flow,
 aggregateRootSpeedup:rows.reduce((s,v)=>s+v.root.originalMilliseconds,0)/rows.reduce((s,v)=>s+v.root.fourierMilliseconds,0),
 aggregateCompleteJacobianSpeedup:rows.reduce((s,v)=>s+v.completeJacobian.originalMilliseconds,0)/rows.reduce((s,v)=>s+v.completeJacobian.fourierMilliseconds,0),
 elapsedSeconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,aggregateRootSpeedup:report.aggregateRootSpeedup,
 aggregateCompleteJacobianSpeedup:report.aggregateCompleteJacobianSpeedup,flow,elapsedSeconds:report.elapsedSeconds}));

