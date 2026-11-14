// One selected-stage serial/pool experiment on the actual successful checkpoint.
// Does not build the far stable graph, solve shooting, or start a prefix BVP.
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {performance} from 'node:perf_hooks';
import {runStageParityBenchmark} from './78718-tail-stage-parity-benchmark.mjs';

const args=process.argv.slice(2),opt={};
if(args.length===0||args.includes('--help')){
 console.log('node scripts/fd2d-tail-stage-pool-benchmark.mjs --packet ACTUAL.json.gz --out NEW.json [--stages 0,12,74,1440] [--workers 2|4] [--pool-module PATH] [--source-root PATH]');
 process.exit(0);
}
for(let i=0;i<args.length;i+=2){
 if(!args[i].startsWith('--')||args[i+1]===undefined)throw Error('key/value arguments required');
 opt[args[i].slice(2)]=args[i+1];
}
if(!opt.packet||!opt.out)throw Error('--packet and fresh --out required');
const here=path.dirname(fileURLToPath(import.meta.url)),out=path.resolve(opt.out);
if(fs.existsSync(out))throw Error('fresh --out required');
const sourceRoot=path.resolve(opt['source-root']??process.env.VISIBLE_FLEX_SOURCE_ROOT??path.join(here,'../repro/source-root'));
process.env.VISIBLE_FLEX_SOURCE_ROOT=sourceRoot;
process.env.CLOSING_TAIL_CACHE=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts');
const poolPath=path.resolve(opt['pool-module']??path.join(here,'fd2d-tail-parallel-stage-pool.mjs'));
const {createStagePool,serialStageFlow}=await import(pathToFileURL(poolPath));
const {createRecalibrationFactory}=await import('./closing_weighted_tail.mjs');
const {subdividePhysical}=await import('./950f-tail-subdivision.mjs');
const {createFourierRootSplitFluxEngine}=await import('./78718-tail-fourier-root-split-engine.mjs');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const identity=p=>{const b=fs.readFileSync(p);return {path:path.resolve(p),bytes:b.length,sha256:sha(b)};};
const began=performance.now(),packetBytes=fs.readFileSync(opt.packet);
const packet=JSON.parse(packetBytes[0]===31&&packetBytes[1]===139?zlib.gunzipSync(packetBytes):packetBytes);
const cfg=packet.config,cp=packet.response?.checkpoint;
if(!cfg||!cp||packet.response.converged!==true)throw Error('actual converged packet with config/checkpoint required');
const selected=(opt.stages??'0,12,74,1440').split(',').map(Number);
if(selected.length<2||selected.length>4||new Set(selected).size!==selected.length||
 selected.some(n=>!Number.isInteger(n)||n<0)||selected.some((n,i)=>i>0&&n<=selected[i-1])){
 throw Error('Choose two to four distinct stages in increasing original index order');
}
const M=cfg.modes,N=cfg.quadrature,K=2*M,steps=cfg.steps;
const geometryBegin=performance.now();
const physical=createRecalibrationFactory(cfg).assemble();
const tail=subdividePhysical(physical,cfg.depth,cfg.shootingParts);
if(cp.states.length!==tail.cells.length+1||selected.some(n=>n>=tail.cells.length)||
 cp.states.some(v=>v.length!==K))throw Error('checkpoint/config stage dimensions differ');
const engines=new Map();
const stages=selected.map(n=>{
 const c=tail.cells[n];
 if(!engines.has(c.mu))engines.set(c.mu,createFourierRootSplitFluxEngine({
  modes:M,quadrature:N,spacing:cfg.spacing,mu:c.mu,orientation:cfg.orientation,
  projectionFloor:cfg.projectionFloor??.05,cuspAwareFlow:cfg.cuspAwareFlow===true,
 }));
 return {index:n,cell:{...c,engine:engines.get(c.mu)}};
});
const geometryPreparationMilliseconds=performance.now()-geometryBegin;
const sourceFiles=[fileURLToPath(import.meta.url),poolPath,
 ...['78718-tail-stage-parity-benchmark.mjs','closing_weighted_tail.mjs',
 'closing_recalibrated_tail.mjs','950f-tail-subdivision.mjs',
 '78718-tail-fourier-root-split-engine.mjs','78718-tail-fourier-root-momentum.mjs',
 '78718-tail-fourier-product-flow.mjs','78718-tail-fourier-product-jacobian.mjs'].map(f=>path.join(here,f)),
 ...['f6tail_momentum_split_flux.mjs','f6tail_cusp_grid.mjs'].map(f=>path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts',f))];
const report={
 scope:'Only selected actual successful stages, serial and selected-worker state/Jacobian parity and local timing; no new shooting or prefix BVP, no global speed or geometry claim.',
 packet:{path:path.resolve(opt.packet),bytes:packetBytes.length,sha256:sha(packetBytes)},
 sourceIdentities:sourceFiles.map(identity),
 config:{modes:M,quadrature:N,spacing:cfg.spacing,physicalDepth:cfg.depth,shootingParts:cfg.shootingParts,
  stepsPerSegment:steps,orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05,cuspAwareFlow:cfg.cuspAwareFlow===true},
 savedResponseResidual:packet.response.residual,
 requestHeightSHA256:sha(JSON.stringify(packet.request?.height??null)),
 selectedStages:selected,geometryPreparationMilliseconds,
 stableGraphConstructed:false,actualShootingSolves:0,actualBVPCalls:0,
};
let pool;
try{
 const startupBegin=performance.now();
 pool=await createStagePool({stages,modes:M,quadrature:N,spacing:cfg.spacing,
  orientation:cfg.orientation,projectionFloor:cfg.projectionFloor??.05,
  cuspAwareFlow:cfg.cuspAwareFlow===true,stepsPerSegment:steps,workers:Number(opt.workers??4)});
 report.poolStartupMilliseconds=performance.now()-startupBegin;
 report.poolMetadata=pool.metadata??null;
 report.benchmark=await runStageParityBenchmark({
  stages:stages.map(({index:n,cell:c})=>({stage:n,input:cp.states[n+1],target:cp.states[n],
   metadata:{rawCell:c.rawCell,rawSegment:c.rawSegment,part:c.part,profiles:c.profiles.length,
    portRatio:c.portRatio,mu:c.mu,inputNode:n+1,targetNode:n}})),
  serialFlow:(n,input,withJac)=>serialStageFlow(stages.find(v=>v.index===n).cell,input,{withJac,stepsPerSegment:steps}),
  parallelFlows:(tasks,withJac)=>pool.evaluate(tasks.map(v=>v.input),withJac),
 });
 report.success=true;
}catch(error){
 report.success=false;
 report.error={name:error.name??'Error',message:String(error.message??error)};
 process.exitCode=2;
}finally{
 if(pool){const closeBegin=performance.now();await pool.close();report.poolCloseMilliseconds=performance.now()-closeBegin;}
}
report.sourcesUnchanged=sourceFiles.every((p,i)=>identity(p).sha256===report.sourceIdentities[i].sha256);
report.elapsedSeconds=(performance.now()-began)/1000;
const encoded=Buffer.from(JSON.stringify(report,null,2)+'\n');
if(encoded.length>=5_000_000)throw Error('report exceeds repository file-size limit');
fs.writeFileSync(out,encoded);
console.log(JSON.stringify({out,bytes:encoded.length,sha256:sha(encoded),success:report.success,
 selectedStages:selected,poolStartupMilliseconds:report.poolStartupMilliseconds,
 blocks:report.benchmark?.blocks.map(b=>({withJac:b.withJac,
  serialMilliseconds:b.serialMilliseconds,parallelMilliseconds:b.parallelMilliseconds,
  selectedBlockSpeedRatio:b.selectedBlockSpeedRatio,allFlowsBitwiseEqual:b.allFlowsBitwiseEqual})),
 sourcesUnchanged:report.sourcesUnchanged,seconds:report.elapsedSeconds,error:report.error}));
