// Pure JSON/source audit of a prepared diagnostic; no numerical module imports.
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {gunzipSync} from 'node:zlib';
import {fileURLToPath} from 'node:url';
import {parseArgs} from 'node:util';
const {values}=parseArgs({options:{out:{type:'string'}}});
if(!values.out||fs.existsSync(values.out))throw Error('New --out required');
const topic=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const note=x=>path.join(topic,'notes','2026-11-09-db6f-'+x);
const read=p=>JSON.parse((p.endsWith('.gz')?gunzipSync(fs.readFileSync(p)):fs.readFileSync(p)).toString());
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const binding=p=>({path:p,bytes:fs.statSync(p).size,sha256:sha(p)});
const need=(b,s)=>{if(!b)throw Error(s);};
const canonical=x=>Array.isArray(x)?'['+x.map(canonical).join(',')+']':
 x!==null&&typeof x==='object'?'{'+Object.keys(x).sort().map(k=>JSON.stringify(k)+':'+canonical(x[k])).join(',')+'}':JSON.stringify(x);
const pins={
 'prefix-continuation03-call002-direction-launch.json':'4f3bb8268e74c9a57e095649bb97c5689f7a666831f0d0e01c21a82a715ad03f',
 'prefix-continuation03-call002-direction-bindings.json':'4f161641ccf73a79388f674dfcc48eea5f599237ab3bdd2e867507640e8b87fe',
 'prefix-continuation03-call002-direction-interface.md':'c51ba48eff5dfe6d1bc013582007c468f51b4aeaf4e96d307307ce5b864c15a3',
};
for(const [name,h] of Object.entries(pins))need(sha(note(name))===h,'Pinned identity '+name);
const launch=read(note('prefix-continuation03-call002-direction-launch.json'));
const source=read(launch.bindings.path);need(source.files.length===98,'98 sources');
for(const b of source.files)need(canonical(binding(b.path))===canonical(b),'Source '+b.path);
need(canonical(binding(launch.bindings.path))===canonical(launch.bindings),'Source ledger binding');
need(canonical(binding(launch.method.path))===canonical(launch.method),'Method binding');
const [base,small]=launch.stages;need(base.id==='base'&&small.id==='small_trials','Stage order');
function opts(argv){const out={};for(let j=2;j<argv.length;j+=2){need(argv[j].startsWith('--')&&j+1<argv.length,'argv pair');need(!(argv[j] in out),'duplicate flag');out[argv[j].slice(2)]=argv[j+1];}return out;}
const a=opts(base.command),b=opts(small.command);
for(const k of ['source-root','config','checkpoint'])need(a[k]===b[k],'Same input '+k);
need(!('direction' in a)&&!('lambdas' in a),'Base recomputes original direction');
need(b.lambdas==='0.000244140625,0.0001220703125,0.00006103515625','Only three dyadic steps');
const lambdas=b.lambdas.split(',').map(Number);need(lambdas.every((v,j)=>v===2**(-12-j)),'Exact dyadic parse');
const direction=a.out.replace(/\.json$/,'')+'-direction.json.gz';need(b.direction===direction,'Direction path');
const expectedOut=[a.out,direction,b.out,base.stdout_log,small.stdout_log];
need(new Set(expectedOut).size===5&&canonical([...expectedOut].sort())===canonical([...launch.future_outputs].sort()),'Output set');
const cfg=read(a.config),rec=read(a.checkpoint),cp=rec.response.checkpoint;
need(canonical(rec.config)===canonical(cfg),'Typed config identity');
need(canonical(Object.keys(rec.response).sort())===canonical(['checkpoint','failed','lastIteration']),'Failed response schema');
need(rec.request.jacobian===false&&rec.request.audit===false,'Original unaudited request');
need(canonical(cp.cutHeight)===canonical(rec.request.height),'Requested physical H label');
need(cfg.modes===15&&cfg.spacing===3&&cfg.quadrature===256&&cfg.depth===12&&cfg.shootingParts===8&&cfg.steps===32,'Original numerical problem');
need(cp.parameters.modes===15&&cp.parameters.physicalDepth===12&&cp.parameters.depth===864&&cp.parameters.shootingParts===8,'Stored problem');
const finite=x=>typeof x==='number'&&Number.isFinite(x);
need(cp.states.length===865&&cp.states.every(x=>x.length===30&&x.every(finite)),'Finite state shape');
need(cp.rawNode.length===13&&cp.rawStates.length===13,'Raw node lengths');
for(let j=0;j<13;j++){need(Number.isInteger(cp.rawNode[j])&&cp.rawNode[j]===72*j,'Raw node identity');need(canonical(cp.rawStates[j])===canonical(cp.states[cp.rawNode[j]]),'Raw state exact copy');}
let copyChecks=13;
for(let n=0;n<12;n++)for(let k=1;k<72;k++){
 const segment=8-Math.floor((k-1)/8),rawLeft=(7-(k-1)%8)/8;
 const z=rawLeft*8,nearest=Math.round(z),oldBase=cp.rawNode[n]+(8-segment)*8;
 need(z===nearest&&oldBase+8-nearest===cp.rawNode[n]+k,'Same-grid remesh copy');copyChecks++;
}
need(copyChecks===865,'All stored nodes copied');
const closedOne=a.checkpoint.replace('_0002.json.gz','_0001.json.gz');
const oneBinding=source.files.find(x=>x.path===closedOne);need(!!oneBinding,'Closed cut-radius control bound');
const one=read(closedOne);need(one.response.jets.radius===cp.parameters.rCut,'Same binary radius from actual prior response');
const r4=one.response.jets.radius**4;
const differences=cp.cutHeight.map((h,j)=>h/r4-cp.states[0][j]);need(differences.every(x=>x===0),'Exact JS boundary delta zero');
const oldIO=['traceFile','iterationCheckpointFile','trialDiagnosticFile','trialStatePrefix','initialCheckpoint'];
for(const output of expectedOut){
 need(!source.files.some(x=>path.resolve(x.path)===path.resolve(output)),'Output/input collision');
 for(const k of oldIO)if(typeof cfg[k]==='string')need(output!==cfg[k]&&!output.startsWith(cfg[k]+'.')&&!output.startsWith(cfg[k]+'-'),'Protected path '+k);
}
const core=p=>fs.readFileSync(path.join(topic,'scripts',p),'utf8');
need(core('db6f-prefix-tail-direction-core.mjs').replace('return {solve,initial,evaluate,correction,scaleFor,cells,graphs,gains,physical,rawNode:',
 'return {solve,initial,evaluate,cells,graphs,gains,physical,rawNode:')===core('db6f-prefix-tail-trial-core.mjs'),'Core only exports two existing functions');
need(core('db6f-prefix-tail-direction-split.mjs').replace('./db6f-prefix-tail-direction-core.mjs','./db6f-prefix-tail-trial-core.mjs')===core('db6f-prefix-tail-trial-split.mjs'),'Split only import changes');
const probe=core('db6f-prefix-tail-direction-probe.mjs');
need(!probe.includes('shared-worker')&&!probe.includes('tail.solve(')&&!probe.includes('dn.solve('),'No worker or solver calls');
for(const k of oldIO)need(!probe.includes(k),'Probe does not consume old I/O '+k);
const gate=small.base_gate;
need(small.requires_reviewed_base===true&&gate.actual_tool_exit===0,'Explicit second-stage gate');
need(gate['stateOnly.norm']===2.604516507642326&&gate['variational.norm']===2.604516507642326,'Same base norm gate');
need(gate.maximumNormalizedResidualDifference===0&&gate.chartCondition===46758.07673463052,'Residual and chart gate');
const report={status:'PASS_STATIC_INPUT_AND_OUTPUT_ISOLATION_ONLY',script:binding(fileURLToPath(import.meta.url)),
 launch:binding(note('prefix-continuation03-call002-direction-launch.json')),ledger:binding(launch.bindings.path),method:binding(launch.method.path),
 verified_bound_files:98,closed_checkpoint:binding(a.checkpoint),closed_cut_radius_control:oneBinding,
 state_shape:[865,30],raw_state_shape:[13,30],same_grid_remesh_copy_checks:copyChecks,
 javascript_boundary_delta_max:Math.max(...differences.map(Math.abs)),
 exact_three_lambdas:lambdas,protected_config_paths:Object.fromEntries(oldIO.map(k=>[k,cfg[k]])),
 independent_output_paths:expectedOut,all_outputs_disjoint_from_inputs_and_old_IO:true,
 core_source_diff:'Only exposes correction and scaleFor',split_source_diff:'Only changes core import',
 worker_imported:false,numerical_modules_imported:false,root_RK_flow_solver_calls:0,
 base_result_or_direction_read:false,output_absence_now_asserted:false,
 stage2_authorized_by_this_static_report:false,
 remaining_runtime_gate:'Root must observe actual base exit0 and completed output; exact two norms/stage residual agreement/chart, saved direction hash and its CP/config identity, finite linear residual. No stage2 until all pass.',
 scope:'Prepared diagnostic input only. Existing base execution belongs to root; no runtime gate result is inferred here.'};
const data=JSON.stringify(report,null,2)+'\n';need(Buffer.byteLength(data)<100000,'Small report');
fs.writeFileSync(values.out,data,{flag:'wx'});fs.chmodSync(values.out,0o444);
console.log(JSON.stringify({status:report.status,verified_sources:98,copyChecks,boundaryDifference:0,solverCalls:0,report:binding(path.resolve(values.out))}));
