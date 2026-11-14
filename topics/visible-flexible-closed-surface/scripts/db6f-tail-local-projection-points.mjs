// Standalone extraction of three closed moment inputs. Exactly one original
// root call, no RHS/RK/flow/DN solve, no active worker or frozen-source edit.
import fs from 'node:fs';
import path from 'node:path';
import {gzipSync,gunzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';
import {parseArgs} from 'node:util';
import {fileURLToPath,pathToFileURL} from 'node:url';

const names=['source-root','config','diagnostic','stage-input','control-checkpoint','control-report','out'];
const {values:a}=parseArgs({options:Object.fromEntries(names.map(k=>[k,{type:'string'}]))});
for(const k of names)if(!a[k])throw Error('Missing --'+k);
if(fs.existsSync(a.out))throw Error('Refusing to overwrite output');
const here=path.dirname(fileURLToPath(import.meta.url)),root=path.resolve(a['source-root']);
process.env.VISIBLE_FLEX_SOURCE_ROOT=root;
process.env.CLOSING_TAIL_CACHE=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const source=n=>path.join(process.env.CLOSING_TAIL_CACHE,n);
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const read=p=>{const b=fs.readFileSync(p);return JSON.parse((b[0]===31&&b[1]===139?gunzipSync(b):b).toString());};
const {createMomentumTailEngine}=await import(pathToFileURL(source('general_root_tail_momentum.mjs')));
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(here,'closing_weighted_tail.mjs')));
const {subdividePhysical}=await import(pathToFileURL(path.join(here,'950f-tail-subdivision.mjs')));
const config=read(a.config),diag=read(a.diagnostic),input=read(a['stage-input']),control=read(a['control-checkpoint']);
const priorControl=read(a['control-report']),p=input.parameters,M=p.modes,dim=2*M;
if(M!==15||p.quadrature!==256||p.projectionFloor!==.05||input.stage!==35||
   input.rawCell!==0||input.rawSegment!==4||input.trial.step!==.0625)throw Error('Wrong frozen point');
const failure=diag.cases.find(c=>c.inputSHA256===sha(a['stage-input']))?.firstFailure;
if(!failure||failure.sourceX!==0||failure.substage!==0||failure.ordinaryStep!==0)
  throw Error('Wrong closed failure record');
const physical=createRecalibrationFactory(config).assemble(),
  stages=subdividePhysical(physical,p.physicalDepth,p.shootingParts),cell=stages.cells[input.stage],profile=cell.profiles[0];
const options={modes:M,spacing:p.spacing,quadrature:p.quadrature,mu:cell.mu,
  orientation:p.orientation,projectionFloor:.05};
const engine=createMomentumTailEngine(options),g=engine.geometry(profile,0);
for(const k of ['r','logw','w','w2','E','drdx','dlogwdx'])
  if(g[k]!==failure.geometry[k])throw Error('Changed physical snapshot '+k);
const failureState=new Float64Array(dim+2);failureState.set(input.inputState);
if(JSON.stringify(Array.from(failureState))!==JSON.stringify(failure.state))throw Error('Changed stage input');
const target=s=>{const z=new Float64Array(M+1),f=p.orientation*Math.sqrt(12)*cell.mu/(Math.sqrt(2)*g.r**4*g.w2);
  for(let j=0;j<M;j++)z[j+1]=f*s[M+j];return z;};
if(JSON.stringify(Array.from(target(failureState)))!==JSON.stringify(failure.target))throw Error('Changed target');
function point(id,state,L,origin,rootDiagnostic=null){
  const Q=state.slice(0,M),e=engine.evaluateL(Float64Array.from(L),Q,g,true),tar=target(state);
  return {id,origin,options,stage:input.stage,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
    sourceX:0,rawSourceX:cell.rawLeft,state:Array.from(state),Q:Array.from(Q),L:Array.from(L),
    geometry:g,target:Array.from(tar),rootDiagnostic,
    sourceEvaluation:{moments:Array.from(e.moments),quad:Array.from(e.quad),B:Array.from(e.B),
      minA:e.minA,minD:e.minD,minS:e.minS,maxQuad:e.maxQuad,
      residual:Math.max(...Array.from(e.moments,(v,j)=>Math.abs(v-tar[j]))),
      scale:Math.max(1e-300,e.maxQuad,...Array.from(tar,Math.abs))}};
}
const points=[
  point('m15-failed-trial-default-legal',failureState,failure.target,
    {file:path.resolve(a.diagnostic),sha256:sha(a.diagnostic),pointer:'cases[4].firstFailure.target',
     status:'NOT A ROOT; legal default iterate of the closed lambda=1/16 failed trial'}),
  point('m15-failed-trial-last-accepted',failureState,failure.rootTrace.lastL,
    {file:path.resolve(a.diagnostic),sha256:sha(a.diagnostic),pointer:'cases[4].firstFailure.rootTrace.lastL',
     status:'NOT A ROOT; last accepted iterate before the closed root line-search failure'})];
const cp=control.checkpoint??control.response?.checkpoint??control,cs=new Float64Array(dim+2);
if(cp.parameters.modes!==M||cp.parameters.quadrature!==256||cp.states[input.stage+1].length!==dim)
  throw Error('Wrong successful-control input');
cs.set(cp.states[input.stage+1]);
// The single new original root calculation authorized for this extractor.
const rt=engine.root(cs,profile,0),previous=priorControl.controlResult.root;
for(const [k,z]of Object.entries({minA:rt.e.minA,minD:rt.e.minD,minS:rt.e.minS,
  residual:rt.err,scale:rt.scale}))if(z!==previous[k])throw Error('Successful control changed '+k);
points.push(point('m15-base-success-control',cs,rt.L,
  {file:path.resolve(a['control-checkpoint']),sha256:sha(a['control-checkpoint']),pointer:'checkpoint.states[36]',
   status:'One original local moment root; not a complete stage or DN solution'},
  {iterations:rt.iterations,residual:rt.err,scale:rt.scale,relativeResidual:rt.err/rt.scale,
   roundoffFallback:!!rt.roundoffFallback,agreesWithPreviouslyClosedControl:true}));
const files=[source('general_root_tail_momentum.mjs'),source('general_exact_tail_cauchy_raw.mjs'),
  ...['closing_weighted_tail.mjs','closing_recalibrated_tail.mjs','950f-tail-subdivision.mjs'].map(n=>path.join(here,n))];
const report={status:'THREE-closed-local-moment-inputs-NO-FLOW',
  scope:'Two saved legal nonroot iterates and one single original root control. No lower-floor scan, flow, RHS, DN, variational flow, or active worker modification.',
  scriptSHA256:sha(fileURLToPath(import.meta.url)),originalRootCalls:1,
  inputSHA256:Object.fromEntries(names.filter(k=>!['source-root','out'].includes(k)).map(k=>
    [k,{file:path.resolve(a[k]),sha256:sha(a[k])}])),
  sourceSHA256:Object.fromEntries(files.map(f=>[f,sha(f)])),points};
const bytes=gzipSync(JSON.stringify(report)+'\n');if(bytes.length>=5_000_000)throw Error('File too large');
fs.writeFileSync(a.out,bytes,{flag:'wx'});
console.log(JSON.stringify({finished:true,originalRootCalls:1,points:points.map(p=>({id:p.id,
  minA:p.sourceEvaluation.minA,residual:p.sourceEvaluation.residual,root:!!p.rootDiagnostic})),
  bytes:bytes.length,sha256:sha(a.out)}));
