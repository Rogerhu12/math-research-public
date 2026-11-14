// Pure storage fixtures only: no physical factory, RHS, variational engine or solver.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {createExactStageFlowStore} from './strong_exact_stage_flow_store.mjs';

const directory=fs.mkdtempSync(path.join(os.tmpdir(),'strong-stage-store-check-'));
const events=[],checks=[];
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const sourceURL=new URL('./strong_exact_stage_flow_store.mjs',import.meta.url);
const identity={source:{fixture:'no-physical-source'},parameters:{modes:2,steps:12},warp:[.3,-0]};
const input=Float64Array.from([1,-0,Number.MIN_VALUE,-3.5]);
const value=()=>({out:Float64Array.from([-.25,-0,Number.MIN_VALUE,1e150]),
 J:Float64Array.from({length:16},(_,i)=>i===3?-0:(i-7)/17),
 meanHeight:-0,minA:.87,minD:.999});
let computed=0;
const compute=()=>{computed++;return value();};
const binary=x=>{
 const all=[...x.out,...x.J,x.meanHeight,x.minA,x.minD],b=Buffer.alloc(all.length*8);
 all.forEach((v,i)=>b.writeDoubleLE(v,i*8));return b;
};
function check(name,f){f();checks.push({name,passed:true});}
try{
 const store=createExactStageFlowStore({directory,identity,dimension:4,event:x=>events.push(x)});
 let first;
 check('initial-miss-calls-original-map-once',()=>{
  first=store.evaluate(0,input,true,compute);
  assert.equal(computed,1);assert.equal(store.stats.misses,1);
 });
 check('same-input-hit-restores-every-Float64-byte',()=>{
  const hit=store.evaluate(0,input,true,()=>{throw Error('Original callback must not run on exact hit');});
  assert.ok(binary(first).equals(binary(hit)));assert.equal(store.stats.hits,1);
  assert.ok(Object.is(hit.out[1],-0));assert.ok(Object.is(hit.meanHeight,-0));
 });
 check('second-store-instance-restores-complete-payload',()=>{
  const other=createExactStageFlowStore({directory,identity,dimension:4});
  assert.ok(binary(first).equals(binary(other.evaluate(0,input,true,()=>{throw Error('unexpected recomputation');}))));
 });
 check('one-ULP-in-one-input-component-misses',()=>{
  const next=Float64Array.from(input),b=Buffer.alloc(8);b.writeDoubleLE(next[0]);
  b.writeBigUInt64LE(b.readBigUInt64LE()+1n);next[0]=b.readDoubleLE();
  store.evaluate(0,next,true,compute);assert.equal(computed,2);
 });
 check('signed-zero-input-is-part-of-binary-key',()=>{
  const next=Float64Array.from(input);next[1]=0;
  store.evaluate(0,next,true,compute);assert.equal(computed,3);
 });
 check('different-stage-misses',()=>{
  store.evaluate(1,input,true,compute);assert.equal(computed,4);
 });
 check('different-source-and-parameter-identities-miss',()=>{
  for(const changed of [
   {...identity,source:{fixture:'different-no-physical-source'}},
   {...identity,parameters:{...identity.parameters,steps:24}},
   {...identity,warp:[.3,0]}]){
   const other=createExactStageFlowStore({directory,identity:changed,dimension:4});
   assert.notEqual(other.identitySHA,store.identitySHA);other.evaluate(0,input,true,compute);
  }
  assert.equal(computed,7);
 });
 check('non-Jacobian-path-calls-original-without-storage',()=>{
  const result={out:Float64Array.from(input),J:null};
  assert.equal(store.evaluate(0,input,false,()=>result),result);
  assert.equal(store.stats.uncachedNonJacobian,1);
 });
 check('orphan-temporary-file-never-counts-as-hit',()=>{
  fs.writeFileSync(path.join(store.root,'000002-orphan.bin.tmp-interrupted'),'incomplete');
  store.evaluate(2,input,true,compute);assert.equal(computed,8);
 });
 check('nonfinite-input-and-unrecorded-output-are-rejected',()=>{
  assert.throws(()=>store.evaluate(3,[1,NaN,0,0],true,compute),/Nonfinite/);
  assert.throws(()=>store.evaluate(3,input,true,()=>({...value(),unrecorded:1})),/unrecorded/);
 });
 check('checksum-corruption-is-rejected-without-recomputation',()=>{
  const key=events.find(x=>x.kind==='stored-completed-stage'&&x.stage===0).key;
  const file=path.join(store.root,'000000-'+key+'.bin'),bytes=fs.readFileSync(file);
  bytes[bytes.length-1]^=1;fs.writeFileSync(file,bytes);
  assert.throws(()=>store.evaluate(0,input,true,compute),/checksum/);assert.equal(computed,8);
 });
 check('truncated-payload-is-rejected-without-recomputation',()=>{
  const key=events.find(x=>x.kind==='stored-completed-stage'&&x.stage===1).key;
  const file=path.join(store.root,'000001-'+key+'.bin'),bytes=fs.readFileSync(file);
  fs.writeFileSync(file,bytes.subarray(0,bytes.length-1));
  assert.throws(()=>store.evaluate(1,input,true,compute),/Incomplete/);assert.equal(computed,8);
 });
 check('identity-manifest-corruption-is-rejected',()=>{
  fs.writeFileSync(path.join(store.root,'identity.txt'),'different');
  assert.throws(()=>createExactStageFlowStore({directory,identity,dimension:4}),/identity file mismatch/);
 });
 console.log(JSON.stringify({scope:'Pure binary storage fixtures only; no numerical-tail equivalence claim',
  physicalFactories:0,physicalRHS:0,physicalJacobian:0,nonlinearSolves:0,
  sourceSHA256:sha(fs.readFileSync(sourceURL)),checkSHA256:sha(fs.readFileSync(new URL(import.meta.url))),
  checks,passed:checks.every(x=>x.passed),computedFixtureMaps:computed,events:events.length,
  realPhysicalStageComparisonRequired:true,fullEvaluationComparisonRequired:true},null,2));
}finally{
 fs.rmSync(directory,{recursive:true,force:true});
}
