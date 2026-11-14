// Pure storage fixture: no physical source, engine, RHS, Jacobian or solve.
// Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import zlib from 'node:zlib';
import {saveExactInitialSeed,restoreExactInitialSeed} from './strong_exact_stage_seed.mjs';

const sha=value=>crypto.createHash('sha256').update(value).digest('hex');
const helperSHA=sha(fs.readFileSync(new URL('./strong_exact_stage_seed.mjs',import.meta.url)));
const stageSHA=sha('pure fixture exact mathematical stage identity');
const sourceIdentity={workerSHA256:sha('fixture worker'),engineSHA256:sha('fixture engine'),
 helperSHA256:helperSHA,scope:'Pure storage fixture only',nested:{negativeZero:-0,unused:undefined}};
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--out')throw Error('Use --out fresh-fixture-report.json');
const reportPath=path.resolve(args[1]);
if(fs.existsSync(reportPath))throw Error('Fixture report already exists');
const directory=fs.mkdtempSync(path.join(os.tmpdir(),'visible-flex-exact-seed-fixture-'));
const checks=[];
function assert(value,message){if(!value)throw Error(message);}
function reject(fn,message){let failed=false;try{fn();}catch{failed=true;}assert(failed,message);}
function check(name,fn){fn();checks.push({name,passed:true});}
function makeDN(M=2,depth=3,rawNode=[0,3]){
 const parameters={modes:M,depth,physicalDepth:rawNode.length-1,shootingParts:1,
  spacing:2,quadrature:16,steps:8,orientation:1,negativeZero:-0,
  valleyControls:[0,-0],nullable:null,unused:undefined,
  nested:{real:0.125,signed:-0},traceFile:'fixture-a',initialCheckpoint:'fixture-in'};
 return {tail:{parameters,cells:Array.from({length:depth},()=>({})),rawNode,
  exactStagePersistence:{identitySHA:stageSHA}}};
}
const unpack=record=>JSON.parse(zlib.gunzipSync(fs.readFileSync(record.path)).toString());
const clone=value=>JSON.parse(JSON.stringify(value));
const equalRows=(a,b)=>a.length===b.length&&a.every((row,n)=>row.length===b[n].length&&
 row.every((v,j)=>Object.is(v,b[n][j])));
let primary,full;
try{
 const dn=makeDN();
 const height=[-0,Number.MIN_VALUE];
 const states=[
  Float64Array.from([-0,0,Number.MIN_VALUE,-Number.MIN_VALUE]),
  Float64Array.from([0.125,-0,-0.25,1]),
  Float64Array.from([1e-300,-1e-300,Number.MAX_VALUE,-Number.MAX_VALUE]),
  Float64Array.from([-0,2,-3,4])];
 const input={dn,height,states,call:1,prefix:path.join(directory,'small'),sourceIdentity};
 check('unmarked prior is returned by identity',()=>{
  const prior={old:true};assert(restoreExactInitialSeed(prior,{})===prior,'Unmarked prior was modified');
 });
 check('complete initial warm saved atomically',()=>{
  primary=saveExactInitialSeed(input);
  assert(fs.existsSync(primary.path)&&primary.bytes<5_000_000&&!primary.alreadyStored,'Seed did not save');
  assert(primary.status==='initial-warm-only'&&primary.numericalSolutionAccepted===false,'Wrong status');
  assert(sha(fs.readFileSync(primary.path))===primary.sha256,'File SHA mismatch');
 });
 const container=unpack(primary),prior=container.checkpoint;
 check('plain checkpoint is explicitly unaccepted',()=>{
  assert(container.converged===false&&container.audit===null&&container.numericalSolutionAccepted===false,
   'Storage fixture was declared accepted');
  assert(prior.exactInitialSeed.status==='initial-warm-only','Missing seed marker');
 });
 check('all state and height Float64 bits including negative zero restore',()=>{
  const restored=restoreExactInitialSeed(prior,dn);
  assert(equalRows(restored.states,states),'A state bit changed');
  assert(height.every((v,j)=>Object.is(v,restored.cutHeight[j])),'A complete H bit changed');
  assert(equalRows(restored.rawStates,[states[0],states[3]]),'Raw-state copies changed');
 });
 check('complete nested parameter encoding preserves negative zero and undefined',()=>{
  const restored=restoreExactInitialSeed(prior,dn),p=restored.parameters;
  assert(Object.is(p.negativeZero,-0)&&Object.is(p.valleyControls[1],-0)&&Object.is(p.nested.signed,-0),
   'Parameter -0 was lost');
  assert(Object.hasOwn(p,'unused')&&p.unused===undefined,'An explicit undefined parameter was lost');
 });
 check('marked restoration is idempotent without changing exact bytes',()=>{
  const a=restoreExactInitialSeed(prior,dn),b=restoreExactInitialSeed(a,dn);
  assert(equalRows(a.states,b.states)&&b.exactInitialSeed.bindingSHA256===a.exactInitialSeed.bindingSHA256,
   'Repeated restoration changed exact state');
 });
 check('the original guard permits only original I/O differences',()=>{
  const next=makeDN();next.tail.parameters.traceFile='fixture-b';next.tail.parameters.initialCheckpoint='other';
  const restored=restoreExactInitialSeed(prior,next);
  assert(equalRows(restored.states,states),'Valid I/O-only change was rejected');
  const wrong=makeDN();wrong.tail.parameters.steps=9;
  reject(()=>restoreExactInitialSeed(prior,wrong),'Changed physical/discretization parameter was accepted');
 });
 check('the complete stage identity is mandatory and verified',()=>{
  const wrong=makeDN();wrong.tail.exactStagePersistence.identitySHA=sha('another actual source tree');
  reject(()=>restoreExactInitialSeed(prior,wrong),'Changed stage identity was accepted');
  const absent=makeDN();delete absent.tail.exactStagePersistence;
  reject(()=>saveExactInitialSeed({...input,dn:absent,prefix:path.join(directory,'no-stage')}),
   'Missing stage identity was accepted');
 });
 check('tampered authoritative binary payload is rejected',()=>{
  const wrong=clone(prior),bytes=Buffer.from(wrong.exactInitialSeed.states.base64,'base64');
  bytes[0]^=1;wrong.exactInitialSeed.states.base64=bytes.toString('base64');
  reject(()=>restoreExactInitialSeed(wrong,dn),'Corrupt binary state was accepted');
 });
 check('tampered exact parameter encoding is rejected',()=>{
  const wrong=clone(prior);wrong.exactInitialSeed.parameters.encoded[1][0][1]=['number','bad'];
  reject(()=>restoreExactInitialSeed(wrong,dn),'Corrupt parameter encoding was accepted');
 });
 check('ordinary JSON contradictions are rejected',()=>{
  const wrong=clone(prior);wrong.states[0][0]=1;
  reject(()=>restoreExactInitialSeed(wrong,dn),'Contradictory JSON state was ignored');
  const node=clone(prior);node.rawStates[1][1]=123;
  reject(()=>restoreExactInitialSeed(node,dn),'Contradictory JSON raw state was ignored');
 });
 check('marked incomplete or accepted metadata is rejected',()=>{
  const wrong=clone(prior);wrong.exactInitialSeed.numericalSolutionAccepted=true;
  reject(()=>restoreExactInitialSeed(wrong,dn),'Accepted marker was permitted');
  reject(()=>restoreExactInitialSeed({exactInitialSeed:null},dn),'Null marker was treated as unmarked');
 });
 check('missing initial states never construct a different warm guess',()=>{
  reject(()=>saveExactInitialSeed({...input,states:undefined,prefix:path.join(directory,'missing')}),
   'Missing initial states were manufactured');
  reject(()=>saveExactInitialSeed({...input,states:states.slice(1),prefix:path.join(directory,'partial')}),
   'Incomplete shooting grid was accepted');
 });
 check('nonfinite complete input and invalid source manifests are rejected',()=>{
  reject(()=>saveExactInitialSeed({...input,height:[NaN,0],prefix:path.join(directory,'nan')}),
   'Nonfinite H was accepted');
  reject(()=>saveExactInitialSeed({...input,sourceIdentity:{},prefix:path.join(directory,'source')}),
   'Incomplete source identity was accepted');
 });
 check('repeated identical seed is retained and a conflicting seed is not overwritten',()=>{
  const again=saveExactInitialSeed(input);
  assert(again.alreadyStored&&again.sha256===primary.sha256,'Identical initial seed did not match');
  reject(()=>saveExactInitialSeed({...input,height:[1,2]}),'Different initial state overwrote a seed');
  assert(sha(fs.readFileSync(primary.path))===primary.sha256,'Conflicting write changed the primary seed');
 });
 check('actual-size 577 by 48 byte layout round-trips completely',()=>{
  const M=24,depth=576,largeDN=makeDN(M,depth,Array.from({length:9},(_,j)=>72*j));
  largeDN.tail.parameters.shootingParts=8;
  const largeStates=Array.from({length:577},(_,n)=>Float64Array.from({length:48},
   (_,j)=>(n+j)%17===0?-0:(n*48+j-1000)/1024));
  const largeHeight=Array.from({length:M},(_,j)=>j===0?-0:(j+1)/65536);
  full=saveExactInitialSeed({dn:largeDN,height:largeHeight,states:largeStates,call:2,
   prefix:path.join(directory,'full'),sourceIdentity});
  const restored=restoreExactInitialSeed(unpack(full).checkpoint,largeDN);
  assert(equalRows(restored.states,largeStates),'A full-size shooting scalar changed');
  assert(largeHeight.every((v,j)=>Object.is(v,restored.cutHeight[j])),'A full-size height scalar changed');
  assert(full.nodeCount===577&&full.shapeDimension===48&&full.bytes<5_000_000,'Wrong full-size file');
 });
 const report={author:'tail_refinement (GPT-6 Astra Pro, AI-assisted)',
  scope:'Pure exact initial-seed storage fixture; no physical source, RHS, Newton, stage map, Jacobian or audit',
  finished:true,all_checks_passed:true,checks,checked_full_states:577,checked_full_dimension:48,
  small_seed_bytes:primary.bytes,full_seed_bytes:full.bytes,
  helper_sha256:helperSHA,fixture_sha256:sha(fs.readFileSync(new URL(import.meta.url))),
  original_warm_helper_sha256:sha(fs.readFileSync(new URL('./strong_exact_raw_tail_warm.mjs',import.meta.url))),
  runtime:{node:process.versions.node,v8:process.versions.v8,arch:process.arch,platform:process.platform},
  memory:process.memoryUsage(),physical_computation_started:false,numerical_solution_accepted:false};
 fs.mkdirSync(path.dirname(reportPath),{recursive:true});
 fs.writeFileSync(reportPath,JSON.stringify(report,null,2)+'\n',{flag:'wx'});
 console.log(JSON.stringify({out:reportPath,checks:checks.length,all_checks_passed:true,
  full_seed_bytes:full.bytes,helper_sha256:helperSHA}));
}finally{
 fs.rmSync(directory,{recursive:true,force:true});
}
