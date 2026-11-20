// Read the fixed factory's local quadrature/cache data. No nonlinear solve.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
const [sourceArg,portArg,outArg,rulesArg]=process.argv.slice(2);
if(!sourceArg||!portArg||!outArg)throw Error('SOURCE PORT OUTPUT');
const source=path.resolve(sourceArg),port=path.resolve(portArg);
process.env.CLOSING_TAIL_CACHE=path.join(source,'repro/source-root/topics/large-amplitude-twist-flex/scripts');
const record=JSON.parse(fs.readFileSync(port,'utf8'));
const cp=record.response?.checkpoint??record.checkpoint??record;
const factoryFile=path.join(source,'scripts/closing_weighted_tail.mjs');
const {createRecalibrationFactory}=await import(pathToFileURL(factoryFile));
const started=performance.now(),factory=createRecalibrationFactory(record.config??cp.parameters);
const physical=factory.assemble(),rows=[];
for(let n=0;n<32;n++){
 const row=factory.getEntries(n,physical.parameters.valleyControls[n]??0);
 rows.push({n,rStart:physical.cells[n].rStart,rEnd:physical.cells[n].rEnd,
  entries:row.entries.map(e=>({j:e.j,breakpoints:Array.from(e.breakpoints),total:Array.from(e.total),
    cumA:Array.from(e.cumA),cumB:Array.from(e.cumB),
    sourceStart:e.profileSource(0),sourceEnd:e.profileSource(1)}))});
}
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const out={scope:'Existing fixed-factory local integration data; no nonlinear states or new calibration parameters.',
 port_sha256:sha(port),factory_sha256:sha(factoryFile),local_source_sha256:sha(path.join(source,'scripts/closing_recalibrated_tail.mjs')),
 alpha:physical.stats.alpha,parameters:physical.parameters,rows,seconds:(performance.now()-started)/1000};
fs.writeFileSync(outArg,JSON.stringify(out)+'\n');
if(rulesArg){
 const local=fs.readFileSync(path.join(source,'scripts/closing_recalibrated_tail.mjs'),'utf8');
 const begin=local.indexOf('function gauss(n){'),end=local.indexOf('function quadrature(');
 if(begin<0||end<=begin)throw Error('The recorded local Gauss constructor was not found');
 const {G8,G16}=vm.runInNewContext(local.slice(begin,end)+';({G8,G16});');
 fs.writeFileSync(rulesArg,JSON.stringify({source_sha256:out.local_source_sha256,G8,G16})+'\n');
}
console.log(JSON.stringify({status:'dumped_existing_local_rules',cells:rows.length,alpha:out.alpha,
 critical_splits:rows.reduce((s,row)=>s+row.entries.reduce((a,e)=>a+e.breakpoints.length,0),0),
 seconds:out.seconds,output_sha256:sha(outArg)}));
