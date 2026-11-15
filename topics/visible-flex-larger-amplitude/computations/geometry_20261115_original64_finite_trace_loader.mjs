// Literal-source observer and original64 finite-trace tangent installation.
// Loaded after the existing 07d45 capacity loader and before the independent
// current-H correction hook. Only the exact declared modules are intercepted.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {registerHooks} from 'node:module';

if(process.env.GITHUB_ACTIONS!=='true'||
 (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
 throw Error('Original64 finite-trace execution belongs to public Actions');
const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC,
 record=process.env.VISIBLE_FINITE_TRACE_SOURCE_RECORD,
 capacity=Number(process.env.VISIBLE_FLEX_TAIL_MODE_CAPACITY),
 here=path.dirname(fileURLToPath(import.meta.url)),
 sha=v=>crypto.createHash('sha256').update(v).digest('hex');
if(!topic||!record||!Number.isSafeInteger(capacity)||capacity<1)
 throw Error('Explicit current original trace source paths and capacity required');
const rootPath=path.resolve(topic,'scripts/78718-tail-fourier-root-momentum.mjs'),
 splitPath=path.resolve(topic,'scripts/78718-tail-fourier-root-split-engine.mjs'),
 flowPath=path.join(here,'geometry_20261115_original64_finite_trace_flow.mjs'),
 rootSHA='cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88',
 splitSHA='a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372';
const originalRoot=fs.readFileSync(rootPath,'utf8'),originalSplit=fs.readFileSync(splitPath,'utf8');
if(sha(originalRoot)!==rootSHA||sha(originalSplit)!==splitSHA)
 throw Error('The original root or split-engine source differs');
const capBefore='M>=1&&M<=64&&Number.isInteger(M)',
 capAfter='M>=1&&M<='+Math.max(64,capacity)+'&&Number.isInteger(M)';
if(originalRoot.split(capBefore).length!==2)throw Error('Original constructor ceiling anchor differs');
const capacityRoot=originalRoot.replace(capBefore,capAfter);
const changes=[];
function once(source,before,after,label){
 const count=source.split(before).length-1;
 if(count!==1)throw Error('Unique original finite-trace source anchor required: '+label+' count='+count);
 changes.push({label,before,after,count});return source.replace(before,after);
}
let transformed=capacityRoot;
transformed=once(transformed,' function solveSPD(B,b){',
 ' function solveSPD(B,b,capture=null){','optional-solve-observer');
const solveStart=transformed.indexOf(' function solveSPD('),
 solveEnd=transformed.indexOf('\n function root(',solveStart);
if(solveStart<0||solveEnd<=solveStart)throw Error('Original Cholesky source boundaries differ');
let solve=transformed.slice(solveStart,solveEnd);
const solveBefore=solve;
solve=once(solve,'  return out;',
 '  if(capture)capture({factor:L,forward:tmp,solution:out});\n  return out;',
 'observe-completed-original-factor-and-two-substitutions');
transformed=transformed.slice(0,solveStart)+solve+transformed.slice(solveEnd);
const rootStart=transformed.indexOf(' function root('),
 rootEnd=transformed.indexOf('\n function initializeFromRaw(',rootStart);
if(rootStart<0||rootEnd<=rootStart)throw Error('Original root source boundaries differ');
let root=transformed.slice(rootStart,rootEnd),rootBefore=root;
root=once(root,' function root(state,profile,x,guess){',
 ' function root(state,profile,x,guess,captureTrace=false){','optional-root-trace');
root=once(root,'  let L=guess?Float64Array.from(guess):Float64Array.from(target);',
 '  const finiteTrace=captureTrace?{schema:"original64-root-primal-tape-v1",'+
 'shape_dimension:2*M,root_dimension:J,geometry:g,target,target_factor:f,'+
 'initial_guess_supplied:!!guess,accepted_updates:[],line_decisions:[],'+
 'root_evaluations:0,line_trials:0,iterations:null,return_reason:null,'+
 'primal_word_mutation:false}:null;\n  try{\n'+
 '  let L=guess?Float64Array.from(guess):Float64Array.from(target);',
 'begin-observer-scope');
root=once(root,'   const e=evaluateL(L,Q,g,true),res=Float64Array.from(e.moments,(v,j)=>v-target[j]);',
 '   if(finiteTrace)finiteTrace.root_evaluations++;\n'+
 '   const e=evaluateL(L,Q,g,true),res=Float64Array.from(e.moments,(v,j)=>v-target[j]);',
 'count-authoritative-iteration-evaluation');
root=once(root,'   if(err<=8e-14*scale)return last;',
 '   if(err<=8e-14*scale){if(finiteTrace){finiteTrace.iterations=it;'+
 'finiteTrace.return_reason="normal-stop";last.finiteTrace=finiteTrace;}return last;}',
 'observe-original-normal-return');
root=once(root,'   const step=solveSPD(e.B,res);let accepted=false;',
 '   let finiteSolve=null;\n'+
 '   const step=solveSPD(e.B,res,finiteTrace?v=>{finiteSolve=v;}:null);let accepted=false;',
 'retain-actual-solve-values');
root=once(root,'    try{const v=evaluateL(trial,Q,g,false),er=Math.max(...Array.from(v.moments,(z,j)=>Math.abs(z-target[j])));',
 '    if(finiteTrace){finiteTrace.line_trials++;finiteTrace.root_evaluations++;}\n'+
 '    try{const v=evaluateL(trial,Q,g,false),er=Math.max(...Array.from(v.moments,(z,j)=>Math.abs(z-target[j])));\n'+
 '     if(finiteTrace)finiteTrace.line_decisions.push({iteration:it,backtrack:k,alpha:fac,error:er});',
 'observe-every-original-backtrack');
root=once(root,'     if(er<err||er<=8e-14*scale){L=trial;accepted=true;break;}}',
 '     if(er<err||er<=8e-14*scale){if(finiteTrace)finiteTrace.accepted_updates.push({'+
 'L,e,res,solve:finiteSolve,iteration:it,backtrack:k,alpha:fac});L=trial;accepted=true;break;}}',
 'retain-only-actually-accepted-root-updates');
root=once(root,'    catch(_){}',
 '    catch(_){if(finiteTrace)finiteTrace.line_decisions.push({iteration:it,backtrack:k,'+
 'alpha:fac,error:String(_),original_catch_preserved:true});}',
 'observe-original-caught-root-trial-error');
root=once(root,'   if(!accepted){if(err<=5e-12*scale)return {...last,roundoffFallback:true};throw new Error("momentum Newton line search failed");}',
 '   if(!accepted){if(err<=5e-12*scale){if(finiteTrace){finiteTrace.iterations=it;'+
 'finiteTrace.return_reason="original-roundoff-fallback";last.finiteTrace=finiteTrace;}'+
 'return {...last,roundoffFallback:true};}throw new Error("momentum Newton line search failed");}',
 'observe-original-fallback-without-a-new-update');
root=once(root,'  throw new Error("momentum Newton iteration limit");\n }',
 '  throw new Error("momentum Newton iteration limit");\n'+
 '  }catch(error){if(finiteTrace&&error&&typeof error==="object")error.finiteRootTrace=finiteTrace;throw error;}\n }',
 'preserve-original-failure-with-private-trace');
transformed=transformed.slice(0,rootStart)+root+transformed.slice(rootEnd);
const tableAnchor=' return {M,N,size,mu,orientation,root,evaluateL,geometry,initializeFromRaw,toRaw,rhs,rhsWithJacobian,rk4,flowRawCell,flowStateWithJacobian};';
transformed=once(transformed,tableAnchor,
 ' return {M,N,size,mu,orientation,root,evaluateL,geometry,initializeFromRaw,toRaw,rhs,rhsWithJacobian,rk4,flowRawCell,flowStateWithJacobian,'+
 'finiteTraceTables:{cs,sn,gramCos,freq,sq2,sq12},finiteRootTraceSchema:"original64-root-primal-tape-v1"};',
 'expose-exact-original-literal-tables-read-only');
let recovered=transformed;
for(const change of [...changes].reverse()){
 if(recovered.split(change.after).length!==2)throw Error('Original finite-trace observer reversal is not unique: '+change.label);
 recovered=recovered.replace(change.after,change.before);
}
if(recovered!==capacityRoot)throw Error('Observer reversal did not recover the exact original capacity-adapted source');
const flowURL=new URL('./geometry_20261115_original64_finite_trace_flow.mjs',import.meta.url).href;
const splitChanges=[
 {before:"import path from 'node:path';",after:"import {createOriginal64FiniteTraceVariationalEngine} from "+JSON.stringify(flowURL)+";\nimport path from 'node:path';"},
 {before:' return engine;',after:' return createOriginal64FiniteTraceVariationalEngine(options,engine);'}
];
let splitTransformed=originalSplit;
for(const c of splitChanges){
 if(splitTransformed.split(c.before).length!==2)throw Error('Original split wrapper anchor differs');
 splitTransformed=splitTransformed.replace(c.before,c.after);
}
let splitRecovered=splitTransformed;
for(const c of [...splitChanges].reverse())splitRecovered=splitRecovered.replace(c.after,c.before);
if(splitRecovered!==originalSplit)throw Error('Original split wrapper reversal failed');
const manifest={
 schema:'original64-finite-root-trace-loader-v1',
 loader_source_sha256:sha(fs.readFileSync(new URL(import.meta.url))),
 flow_source_sha256:sha(fs.readFileSync(flowPath)),
 kernel_source_sha256:sha(fs.readFileSync(path.join(here,'geometry_20261115_original64_finite_trace_variation.mjs'))),
 original_root_source_sha256:rootSHA,capacity_root_source_sha256:sha(capacityRoot),
 observed_root_source_sha256:sha(transformed),
 original_split_source_sha256:splitSHA,matched_split_source_sha256:sha(splitTransformed),
 original_root_and_rhs_primal_arithmetic_recovered:true,original_capacity_source_unchanged:true,
 original_root_policy:{iterations:30,backtracks:20,stop:8e-14,fallback:5e-12},
 changes,split_changes:splitChanges,loaded_root:false,loaded_split:false,
 no_original_disk_source_modified:true,
 tangent_scope:'numerical explicit factor-loop variation of the forced successful real root trace; not an IEEE roundmap derivative',
 no_implicit_root_or_IEEE_derivative_equivalence_claim:true
};
fs.writeFileSync(record,JSON.stringify(manifest,null,2)+'\n',{flag:'wx'});
function save(){fs.writeFileSync(record,JSON.stringify(manifest,null,2)+'\n');}
registerHooks({load(url,context,nextLoad){
 const loaded=nextLoad(url,context);
 if(!url.startsWith('file:'))return loaded;
 const file=path.resolve(fileURLToPath(url));
 if(file!==rootPath&&file!==splitPath)return loaded;
 const text=typeof loaded.source==='string'?loaded.source:Buffer.from(loaded.source).toString('utf8');
 if(file===rootPath){
  if(text!==capacityRoot)throw Error('Finite trace must follow the exact original capacity loader');
  manifest.loaded_root=true;save();return {...loaded,source:transformed};
 }
 if(text!==originalSplit)throw Error('Actual original split-wrapper source differs');
 manifest.loaded_split=true;save();return {...loaded,source:splitTransformed};
}});
