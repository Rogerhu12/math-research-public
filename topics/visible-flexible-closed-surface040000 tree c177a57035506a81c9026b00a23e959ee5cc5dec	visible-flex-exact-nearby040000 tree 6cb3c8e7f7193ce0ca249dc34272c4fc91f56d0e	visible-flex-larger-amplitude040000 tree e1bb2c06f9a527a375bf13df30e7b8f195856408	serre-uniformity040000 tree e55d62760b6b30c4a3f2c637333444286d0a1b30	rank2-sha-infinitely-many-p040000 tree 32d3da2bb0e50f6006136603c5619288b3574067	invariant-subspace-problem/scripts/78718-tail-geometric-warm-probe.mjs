// Exercise all saved warm nodes without stable-graph construction or a solve.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {createRecalibrationFactory} from './closing_weighted_tail.mjs';
import {subdividePhysical} from './950f-tail-subdivision.mjs';
import {geometricWarmRemesh} from './78718-tail-geometric-warm-remesh.mjs';
const srcRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
const {createFastSplitFluxMomentumTailEngine}=await import(pathToFileURL(path.join(srcRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs')));
const args=process.argv.slice(2),opt={};for(let k=0;k<args.length;k+=2)opt[args[k].replace(/^--/,'')]=args[k+1];
if(!opt.packet||!opt.out||fs.existsSync(opt.out))throw Error('packet and fresh out required');
const started=Date.now(),buf=fs.readFileSync(opt.packet),packet=JSON.parse(zlib.gunzipSync(buf)),prior=packet.response.checkpoint,rows=[];
for(const N of String(opt.quadratures??'512,1024').split(',').map(Number)){
 const M=Number(opt.modes??22),cfg={...packet.config,modes:M,quadrature:N},physical=createRecalibrationFactory(cfg).assemble(),stages=subdividePhysical(physical,cfg.depth,cfg.shootingParts),engines=new Map();
 const cells=stages.cells.map(c=>{if(!engines.has(c.mu))engines.set(c.mu,createFastSplitFluxMomentumTailEngine({modes:M,spacing:cfg.spacing,quadrature:N,mu:c.mu,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05}));return {...c,engine:engines.get(c.mu)};});
 const dn={tail:{physical,cells,rawNode:stages.rawNode,parameters:{...physical.parameters,modes:M,quadrature:N,spacing:cfg.spacing,orientation:cfg.orientation,depth:cells.length,physicalDepth:cfg.depth,shootingParts:cfg.shootingParts,projectionFloor:cfg.projectionFloor??.05}}};
 const t=Date.now(),result=geometricWarmRemesh(prior,dn,createFastSplitFluxMomentumTailEngine);
 rows.push({...result.diagnostics,convertedStateSHA256:crypto.createHash('sha256').update(JSON.stringify(result.states)).digest('hex'),seconds:(Date.now()-t)/1000});console.log(JSON.stringify({modes:M,quadrature:N,...result.diagnostics,seconds:(Date.now()-t)/1000}));
}
const report={scope:'All-node numerical initial-guess conversion, no stable graph, true DN, BVP, or new tail solution.',packet:{path:path.resolve(opt.packet),bytes:buf.length,sha256:crypto.createHash('sha256').update(buf).digest('hex')},program:{path:path.resolve(process.argv[1]),sha256:crypto.createHash('sha256').update(fs.readFileSync(process.argv[1])).digest('hex')},converter:{path:path.resolve('scripts/78718-tail-geometric-warm-remesh.mjs'),sha256:crypto.createHash('sha256').update(fs.readFileSync(new URL('./78718-tail-geometric-warm-remesh.mjs',import.meta.url))).digest('hex')},rows,elapsedSeconds:(Date.now()-started)/1000};fs.writeFileSync(opt.out,JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({out:path.resolve(opt.out),bytes:fs.statSync(opt.out).size,elapsedSeconds:report.elapsedSeconds}));
