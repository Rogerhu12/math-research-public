// Local algebra/performance experiment, not a replacement solver.
import fs from 'node:fs';import path from 'node:path';import zlib from 'node:zlib';import crypto from 'node:crypto';import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
import {geometricWarmRemesh} from './78718-tail-geometric-warm-remesh.mjs';
import {createFourierProductJacobianEngine} from './78718-tail-fourier-product-jacobian.mjs';
const srcRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(srcRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs')));
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.packet||!opt.out||fs.existsSync(opt.out))throw Error('input and fresh output required');
const started=Date.now(),buf=fs.readFileSync(opt.packet),packet=JSON.parse(zlib.gunzipSync(buf)),M=Number(opt.modes??22),N=Number(opt.quadrature??512),cfg={...packet.config,modes:M,quadrature:N};
const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),engines=new Map(),prototypes=new Map();
const cells=stages.cells.map(c=>{if(!engines.has(c.mu)){const o={modes:M,spacing:cfg.spacing,quadrature:N,mu:c.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05},b=createFastSplitFluxMomentumTailEngine(o);engines.set(c.mu,b);prototypes.set(c.mu,createFourierProductJacobianEngine(o,b));}return {...c,engine:engines.get(c.mu)};});
const dn={tail:{physical,cells,rawNode:stages.rawNode,parameters:{...physical.parameters,modes:M,quadrature:N,spacing:cfg.spacing,orientation:cfg.orientation,depth:cells.length,physicalDepth:cfg.depth,shootingParts:cfg.shootingParts,projectionFloor:cfg.projectionFloor??.05}}};
const converted=geometricWarmRemesh(packet.response.checkpoint,dn,createFastSplitFluxMomentumTailEngine),rows=[],repeat=Number(opt.repeat??20);
for(const node of [0,16,31,34,40,72,144,288,576,864]){
 const c=cells[node===0?0:node-1],p=node===0?c.profiles.at(-1):c.profiles[0],x=node===0?1:0,y=new Float64Array(2*M+2);y.set(converted.states[node]);if(node===0)for(let j=M;j<2*M;j++)y[j]*=c.portRatio;
 const original=c.engine.rhsWithJacobian,fast=prototypes.get(c.mu).rhsWithJacobian;
 for(let k=0;k<3;k++){original(y,p,x);fast(y,p,x);}
 const a=original(y,p,x),b=fast(y,p,x);let rhsGap=0,jacGap=0,scaledShape=0,scaledMean=0;
 for(let k=0;k<a.derivative.length;k++)rhsGap=Math.max(rhsGap,Math.abs(a.derivative[k]-b.derivative[k]));
 const qScale=Math.max(1e-250,...Array.from(y.slice(0,M),Math.abs)),piScale=Math.max(1e-250,...Array.from(y.slice(M,2*M),Math.abs));
 for(let i=0;i<2*M+2;i++){let err=0,size=0;for(let j=0;j<2*M;j++){const aa=a.jacobian[i*2*M+j],bb=b.jacobian[i*2*M+j],d=Math.abs(aa-bb),scale=j<M?qScale:piScale;jacGap=Math.max(jacGap,d);err+=d*scale;size+=Math.abs(aa)*scale;}const rel=err/Math.max(1e-300,size);if(i<2*M)scaledShape=Math.max(scaledShape,rel);else scaledMean=Math.max(scaledMean,rel);}
 const t0=performance.now();for(let k=0;k<repeat;k++)original(y,p,x);const t1=performance.now();for(let k=0;k<repeat;k++)fast(y,p,x);const t2=performance.now();
 const row={node,rawCell:c.rawCell,r:a.root.g.r,originalMilliseconds:(t1-t0)/repeat,fourierProductMilliseconds:(t2-t1)/repeat,speedup:(t1-t0)/(t2-t1),maxDerivativeAbsoluteDifference:rhsGap,maxJacobianAbsoluteDifference:jacGap,maxScaledShapeRowDifference:scaledShape,maxScaledMeanRowDifference:scaledMean};rows.push(row);console.log(JSON.stringify(row));
}
const report={scope:'Local prototype comparisons only. Original root and split RHS unchanged; no flow, DN, BVP, or production worker uses the prototype.',packet:{path:path.resolve(opt.packet),sha256:crypto.createHash('sha256').update(buf).digest('hex')},modes:M,quadrature:N,repeat,prototype:{path:path.resolve('scripts/78718-tail-fourier-product-jacobian.mjs'),sha256:crypto.createHash('sha256').update(fs.readFileSync(new URL('./78718-tail-fourier-product-jacobian.mjs',import.meta.url))).digest('hex')},rows,aggregateSpeedup:rows.reduce((s,v)=>s+v.originalMilliseconds,0)/rows.reduce((s,v)=>s+v.fourierProductMilliseconds,0),elapsedSeconds:(Date.now()-started)/1000};fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,aggregateSpeedup:report.aggregateSpeedup,elapsedSeconds:report.elapsedSeconds}));
