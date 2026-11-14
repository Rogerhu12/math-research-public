// No root, ODE, DN, BVP, physical factory or candidate input is constructed.
// Exercises the exact shared-progress and bounded-close helpers with tiny
// intentionally exiting/waiting workers, not the numerical stage engine.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {Worker} from 'node:worker_threads';
import {performance} from 'node:perf_hooks';
const here=path.dirname(fileURLToPath(import.meta.url));
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('Use --out FRESH.json');
const out=path.resolve(args[1]);if(fs.existsSync(out))throw Error('Fresh output required');
process.env.VISIBLE_FLEX_SOURCE_ROOT??=path.resolve(here,'../repro/source-root');
const source=path.join(here,'78718-tail-parallel-stage-pool.mjs');
const {waitForSharedCompletion,closeStageWorkers}=await import(pathToFileURL(source));
const sha=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const cases=[],began=performance.now();
for(const mode of ['native-exit','ignore-stop','continues-progress']){
 const shared=new SharedArrayBuffer(4*4),control=new Int32Array(shared);
 const worker=new Worker(`
  const {workerData}=require('node:worker_threads');
  const a=new Int32Array(workerData.shared);
  Atomics.store(a,0,1);
  if(workerData.mode==='native-exit')process.exit(23);
  if(workerData.mode==='ignore-stop')for(;;)Atomics.wait(a,3,0);
  if(workerData.mode==='continues-progress'){
   for(let k=0;k<8;k++){Atomics.add(a,2,1);Atomics.wait(a,3,0,10);}
   Atomics.store(a,1,1);Atomics.notify(a,1);
  }
 `,{eval:true,workerData:{mode,shared},execArgv:[]});
 const errors=[],exitPromise=new Promise(resolve=>worker.once('exit',resolve));
 worker.on('error',e=>errors.push(String(e)));
 while(!Atomics.load(control,0))await new Promise(r=>setTimeout(r,1));
 const start=performance.now();let error=null;
 try{waitForSharedCompletion({control,doneIndex:1,doneCount:1,progressIndex:2,
  noProgressMilliseconds:mode==='continues-progress'?30:120});}
 catch(e){error={message:String(e.message),code:e.code};}
 const waitMilliseconds=performance.now()-start,closeStart=performance.now();
 const close=await closeStageWorkers([worker],[exitPromise],{
  closeGraceMilliseconds:20,terminateGraceMilliseconds:1000});
 const exitCode=await exitPromise;
 const passed=mode==='continues-progress'?error===null&&exitCode===0:
  error?.code==='TAIL_STAGE_POOL_INFRASTRUCTURE'&&
  (mode==='native-exit'?exitCode===23:close.forcedTermination&&exitCode===1);
 cases.push({mode,passed,waitMilliseconds,error,closeMilliseconds:performance.now()-closeStart,
  close,actualWorkerExitCode:exitCode,workerErrors:errors});
}
const report={scope:'Worker infrastructure only; no numerical candidate, root or flow.',
 source:{path:source,sha256:sha(source)},script:{path:fileURLToPath(import.meta.url),sha256:sha(fileURLToPath(import.meta.url))},
 productionLimits:{noProgressMilliseconds:120000,closeGraceMilliseconds:2000,terminateGraceMilliseconds:5000},
 shortenedProbeLimits:true,cases,success:cases.every(c=>c.passed),seconds:(performance.now()-began)/1000,
 actualRoots:0,actualFlows:0,actualDN:0,actualBVP:0};
fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({out,sha256:sha(out),success:report.success,seconds:report.seconds,
 cases:cases.map(c=>({mode:c.mode,passed:c.passed,actualWorkerExitCode:c.actualWorkerExitCode,
  forcedTermination:c.close.forcedTermination,waitMilliseconds:c.waitMilliseconds}))}));
if(!report.success)process.exitCode=2;
