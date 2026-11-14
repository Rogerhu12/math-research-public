// Resource envelope only. The actual numerical worker retains its original
// stdin/stdout protocol and creates the same independent stage maps.
// No process-wide V8 heap flag is set: such a flag overrides Worker limits.
import {Worker} from 'node:worker_threads';
import path from 'node:path';
import {pathToFileURL} from 'node:url';

const [entry,configuration,heapText]=process.argv.slice(2),oldHeap=Number(heapText);
if(!entry||!configuration||!Number.isInteger(oldHeap)||oldHeap<64)
 throw new Error('Expected numerical worker, configuration, and main old-heap MiB');
if((process.env.NODE_OPTIONS??'').trim())
 throw new Error('Bounded launcher requires no global NODE_OPTIONS');

const limits={maxOldGenerationSizeMb:oldHeap,maxYoungGenerationSizeMb:16,stackSizeMb:4};
const worker=new Worker(pathToFileURL(path.resolve(entry)),{
 argv:[configuration],stdin:true,stdout:true,stderr:true,execArgv:[],
 env:{...process.env,NODE_OPTIONS:''},resourceLimits:limits,
 workerData:{kind:'visible-flex-bounded-numerical-host-v1'},
});
process.stdin.pipe(worker.stdin);
worker.stdout.pipe(process.stdout,{end:false});
worker.stderr.pipe(process.stderr,{end:false});
worker.on('error',error=>{
 process.stderr.write(JSON.stringify({event:'numerical_host_worker_error',
  code:error.code??null,error:String(error),resourceLimits:limits})+'\n');
 process.exitCode=2;
});
worker.on('exit',code=>{
 process.stdin.unpipe(worker.stdin);process.stdin.destroy();
 process.exitCode=code===0?(process.exitCode??0):2;
 if(code!==0)process.stderr.write(JSON.stringify({event:'numerical_host_worker_exit',
  code,resourceLimits:limits})+'\n');
});
