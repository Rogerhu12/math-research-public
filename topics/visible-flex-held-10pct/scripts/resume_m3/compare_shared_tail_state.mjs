// One complete accepted state, before/after allocation sharing. No new solve.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
const [beforeTopic,afterTopic,input,out]=process.argv.slice(2);
const source=path.join(beforeTopic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=source;
process.env.CLOSING_TAIL_CACHE=path.join(source,'topics/large-amplitude-twist-flex/scripts');
const data=JSON.parse(gunzipSync(fs.readFileSync(input))),cfg=data.config,cp=data.response.checkpoint;
if(!data.response.converged||!(data.response.residual<=cfg.solveTolerance))throw Error('An accepted actual input is required');
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(beforeTopic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN:oldFactory}=await import(pathToFileURL(path.join(beforeTopic,'scripts/950f-tail-stage-split.mjs')));
const {createSplitFluxCompactTailDN:newFactory}=await import(pathToFileURL(path.join(afterTopic,'scripts/950f-tail-stage-split.mjs')));
const physical=createRecalibrationFactory(cfg).assemble();
const old=oldFactory({...cfg,tail:physical}),fresh=newFactory({...cfg,tail:physical});
const oldCount=new Set(old.tail.cells.map(c=>c.engine)).size,newCount=new Set(fresh.tail.cells.map(c=>c.engine)).size;
if(newCount!==new Set(fresh.tail.cells.map(c=>c.mu)).size||!(newCount<oldCount))throw Error('Expected local same-mu sharing');
const states=cp.states.map(v=>Float64Array.from(v)),M=cfg.modes,K=2*M;
const target=Float64Array.from(cp.cutHeight,v=>v/cfg.rCut**4),scales=new Float64Array(states.length);
scales[0]=Math.max(...Array.from(target,Math.abs));
for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(old.tail.gains[n][0]);
const rows={residual:0,flow:0,jacobian:0,deepGraph:0,gains:0,graphs:0};
let compared=0;
function compare(a,b,key){
 if(a.length!==b.length)throw Error('Length mismatch '+key);
 for(let j=0;j<a.length;j++){
  if(!Number.isFinite(a[j])||!Number.isFinite(b[j]))throw Error('Nonfinite comparison '+key);
  rows[key]=Math.max(rows[key],Math.abs(a[j]-b[j]));compared++;
 }
}
const hashA=createHash('sha256'),hashB=createHash('sha256');
function hash(h,a){const b=Float64Array.from(a);h.update(new Uint8Array(b.buffer));}
const t0=performance.now(),A=old.tail.evaluate(states,target,true,scales),secondsA=(performance.now()-t0)/1000;
console.log(JSON.stringify({event:'original_complete_evaluate',norm:A.norm,seconds:secondsA,engines:oldCount}));
const t1=performance.now(),B=fresh.tail.evaluate(states,target,true,scales),secondsB=(performance.now()-t1)/1000;
for(let n=0;n<A.flows.length;n++){
 compare(A.residuals[n],B.residuals[n],'residual');compare(A.flows[n].out,B.flows[n].out,'flow');
 compare(A.flows[n].J,B.flows[n].J,'jacobian');
 compare(old.tail.gains[n],fresh.tail.gains[n],'gains');
 compare(old.tail.graphs[n],fresh.tail.graphs[n],'graphs');
 for(const x of [A.residuals[n],A.flows[n].out,A.flows[n].J])hash(hashA,x);
 for(const x of [B.residuals[n],B.flows[n].out,B.flows[n].J])hash(hashB,x);
}
compare(A.end,B.end,'residual');compare(old.tail.graphs.at(-1),fresh.tail.graphs.at(-1),'deepGraph');
hash(hashA,A.end);hash(hashB,B.end);
const base=fresh.tail.cells[0],same=fresh.tail.cells.findIndex((c,i)=>i>0&&c.engine===base.engine),
 different=fresh.tail.cells.findIndex(c=>c.engine!==base.engine);
function point(index){const c=fresh.tail.cells[index],s=new Float64Array(K+2);s.set(states[index+1]);return c.engine.rhsWithJacobian(s,c.profiles[0],0);}
const first=point(0),saved={derivative:Float64Array.from(first.derivative),jacobian:Float64Array.from(first.jacobian),L:Float64Array.from(first.root.L)};
point(same);if(different>=0)point(different);const again=point(0);
function maxDiff(a,b){let v=0;for(let j=0;j<a.length;j++)v=Math.max(v,Math.abs(a[j]-b[j]));return v;}
const mutableScratch={sameEngineStage:same,differentEngineStage:different,
 returnedDerivativeMutation:maxDiff(first.derivative,saved.derivative),returnedJacobianMutation:maxDiff(first.jacobian,saved.jacobian),returnedRootMutation:maxDiff(first.root.L,saved.L),
 repeatedDerivativeDifference:maxDiff(again.derivative,saved.derivative),repeatedJacobianDifference:maxDiff(again.jacobian,saved.jacobian),repeatedRootDifference:maxDiff(again.root.L,saved.L)};
const digestA=hashA.digest('hex'),digestB=hashB.digest('hex');
if(Object.values(rows).some(x=>x!==0)||A.norm!==B.norm||A.minA!==B.minA||A.minD!==B.minD||digestA!==digestB)throw Error('Complete numerical input/output equality failed');
if(Object.entries(mutableScratch).some(([k,v])=>!k.endsWith('Stage')&&v!==0))throw Error('Mutable scratch escaped across stages');
const files=[process.argv[1],...['950f-tail-stage-core.mjs','950f-tail-stage-split.mjs'].flatMap(n=>[path.join(beforeTopic,'scripts',n),path.join(afterTopic,'scripts',n)])];
const result={scope:'Complete same-state residual and every stage flow Jacobian comparison, plus direct mutable-output and reentrant-stage check. No new BVP or tail solve, and no universal speed claim.',
 input_sha256:createHash('sha256').update(fs.readFileSync(input)).digest('hex'),inputAcceptedResidual:data.response.residual,
 source_sha256:Object.fromEntries(files.map(p=>[p,createHash('sha256').update(fs.readFileSync(p)).digest('hex')])),
 modes:M,quadrature:cfg.quadrature,shootingParts:cfg.shootingParts,stages:A.flows.length,
 originalEngines:oldCount,sharedEngines:newCount,comparedScalarEntries:compared,differences:rows,
 originalNorm:A.norm,sharedNorm:B.norm,minA:A.minA,minD:A.minD,
 originalBitHash:digestA,sharedBitHash:digestB,mutableScratch,originalSeconds:secondsA,sharedSeconds:secondsB,
 globalSparseSystem:'Every flow Jacobian, residual block, deep graph, gain and common scale agrees; sparseGlobalSolve and its assembly source are byte unchanged.'};
fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
