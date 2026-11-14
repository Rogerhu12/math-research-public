// Local algebra/performance experiment, not a replacement solver.
import fs from 'node:fs';import path from 'node:path';import zlib from 'node:zlib';import crypto from 'node:crypto';import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
import {geometricWarmRemesh} from './78718-tail-geometric-warm-remesh.mjs';
import {createFourierProductJacobianEngine} from './78718-tail-fourier-product-jacobian.mjs';
import {createFourierProductVariationalEngine} from './78718-tail-fourier-product-flow.mjs';
const srcRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(srcRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs')));
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.packet||!opt.out||fs.existsSync(opt.out))throw Error('input and fresh output required');
const started=Date.now(),buf=fs.readFileSync(opt.packet),packet=JSON.parse(zlib.gunzipSync(buf)),M=Number(opt.modes??22),N=Number(opt.quadrature??512),cfg={...packet.config,modes:M,quadrature:N};
const physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),engines=new Map(),prototypes=new Map();
const cells=stages.cells.map(c=>{if(!engines.has(c.mu)){const o={modes:M,spacing:cfg.spacing,quadrature:N,mu:c.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05},b=createFastSplitFluxMomentumTailEngine(o);engines.set(c.mu,b);prototypes.set(c.mu,createFourierProductJacobianEngine(o,b));}return {...c,engine:engines.get(c.mu)};});
const dn={tail:{physical,cells,rawNode:stages.rawNode,parameters:{...physical.parameters,modes:M,quadrature:N,spacing:cfg.spacing,orientation:cfg.orientation,depth:cells.length,physicalDepth:cfg.depth,shootingParts:cfg.shootingParts,projectionFloor:cfg.projectionFloor??.05}}};
const converted=geometricWarmRemesh(packet.response.checkpoint,dn,createFastSplitFluxMomentumTailEngine),rows=[],repeat=Number(opt.repeat??20);

const stage=Number(opt.stage??31),cell=cells[stage],y=new Float64Array(2*M+2);y.set(converted.states[stage+1]);
const accelerated=createFourierProductVariationalEngine({modes:M,spacing:cfg.spacing,quadrature:N,mu:cell.mu,orientation:cfg.orientation},cell.engine);
const t0=performance.now(),a=cell.engine.flowStateWithJacobian(y,cell.profiles,{stepsPerSegment:cfg.steps}),t1=performance.now(),b=accelerated.flowStateWithJacobian(y,cell.profiles,{stepsPerSegment:cfg.steps}),t2=performance.now();
let stateGap=0,tangentGap=0,tangentSize=0,scaledRows=0;
for(let j=0;j<a.state.length;j++)stateGap=Math.max(stateGap,Math.abs(a.state[j]-b.state[j]));
const qScale=Math.max(1e-250,...Array.from(y.slice(0,M),Math.abs)),piScale=Math.max(1e-250,...Array.from(y.slice(M,2*M),Math.abs));
for(let i=0;i<2*M+2;i++){let err=0,size=0;for(let j=0;j<2*M;j++){const aa=a.tangent[i*2*M+j],bb=b.tangent[i*2*M+j],d=Math.abs(aa-bb),scale=j<M?qScale:piScale;tangentGap=Math.max(tangentGap,d);tangentSize=Math.max(tangentSize,Math.abs(aa));err+=d*scale;size+=Math.abs(aa)*scale;}scaledRows=Math.max(scaledRows,err/Math.max(1e-300,size));}
const report={scope:'One actual short-stage RK/variational comparison, no multiple shooting or BVP.',packet:{path:path.resolve(opt.packet),sha256:crypto.createHash('sha256').update(buf).digest('hex')},modes:M,quadrature:N,stage,rawCell:cell.rawCell,rawSegment:cell.rawSegment,steps:cfg.steps,originalMilliseconds:t1-t0,fourierProductMilliseconds:t2-t1,speedup:(t1-t0)/(t2-t1),stateMaxAbsoluteDifference:stateGap,tangentMaxAbsoluteDifference:tangentGap,tangentMaxMagnitude:tangentSize,tangentMaxScaledRowRelativeDifference:scaledRows,originalGuards:{minA:a.minA,minD:a.minD,maxRootRelative:a.maxRootRelative},fourierProductGuards:{minA:b.minA,minD:b.minD,maxRootRelative:b.maxRootRelative},elapsedSeconds:(Date.now()-started)/1000};
fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
