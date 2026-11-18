// One complete SAME-STATE original lexical evaluate through the owned native
// provider. Before it runs, the static producer is checked against all saved
// coefficients/trig/inputs in the three original fixtures. No nonlinear DN
// solve, correction, new physical target, cutJets or audit is called here.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {gzipSync,gunzipSync} from 'node:zlib';
import {isDeepStrictEqual} from 'node:util';

const digest=b=>createHash('sha256').update(b).digest('hex');
const ref=p=>({path:path.resolve(p),sha256:digest(fs.readFileSync(p))});
const load=p=>JSON.parse(p.endsWith('.gz')?gunzipSync(fs.readFileSync(p)):fs.readFileSync(p,'utf8'));
const assert=(ok,message)=>{if(!ok)throw Error(message);};
function bytes(a){const b=Buffer.alloc(a.length*8);a.forEach((v,j)=>b.writeDoubleLE(v,8*j));return b;}
function saveJSON(p,x){fs.writeFileSync(p,JSON.stringify(x,null,2)+'\n',{flag:'wx'});return ref(p);}
const args=process.argv.slice(2);
assert(args.length===2&&args[0]==='--plan','Usage: probe_native_adapter_entry.mjs --plan PLAN');
const planPath=path.resolve(args[1]),plan=load(planPath);
assert(plan.schema==='n4-native-adapter-entry-v1'&&plan.native_evaluate_count===1&&plan.withJac===true,'Unexpected fixed entry plan');
for(const item of Object.values(plan.files))assert(ref(item.path).sha256===item.sha256,'Plan reference changed: '+item.path);
assert(ref(process.argv[1]).sha256===plan.files.probe.sha256,'Entry probe source changed');
for(const p of Object.values(plan.outputs))assert(!fs.existsSync(p),'Refusing to overwrite entry output');
process.env.VISIBLE_FLEX_SOURCE_ROOT=path.join(plan.source_topic,'repro/source-root');
process.env.CLOSING_TAIL_CACHE=path.join(process.env.VISIBLE_FLEX_SOURCE_ROOT,'topics/large-amplitude-twist-flex/scripts');
process.env.VISIBLE_FLEX_NATIVE_MANIFEST=plan.files.manifest.path;
process.env.VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=plan.files.manifest.sha256;
process.env.VISIBLE_FLEX_NATIVE_RUN_DIR=plan.run_directory;
const summary={schema:'n4-native-adapter-entry-terminal-v1',plan:ref(planPath),source:ref(process.argv[1]),
  input:plan.files.production_CP,manifest:plan.files.manifest,original_input_was_accepted:false,
  requested_complete_evaluates:1,Newton_or_DN_solve:false,cutJets_or_audit:false,
  scope:'Finite same-state transport/evaluate only. Neither completion nor a residual below2e-9 is a completed actual DN/Jac/audit acceptance.'};
const begin=performance.now();
try{
  const record=load(plan.files.production_CP.path),checkpoint=record.response.checkpoint,cfg=record.config;
  assert(cfg.modes===20&&cfg.spacing===4&&cfg.shootingParts===32&&cfg.steps===16&&cfg.solveTolerance===2e-9,'Original finite problem differs');
  assert(checkpoint?.states&&checkpoint?.cutHeight&&checkpoint?.parameters,'Complete original failed checkpoint required');
  const {createRecalibrationFactory}=await import(pathToFileURL(path.join(plan.source_topic,'scripts/closing_weighted_tail.mjs')));
  const {createNativeCompactTailDN}=await import(pathToFileURL(path.join(plan.source_topic,'scripts/native_batch_factory.mjs')));
  const physical=createRecalibrationFactory(cfg).assemble(),dn=createNativeCompactTailDN({...cfg,tail:physical});
  summary.physical_and_linear_graph_construction_seconds=(performance.now()-begin)/1000;
  for(const [key,value] of Object.entries(checkpoint.parameters))
    assert(isDeepStrictEqual(dn.tail.parameters[key],value),'Original physical/numerical parameter differs: '+key);
  const M=cfg.modes,K=2*M,states=checkpoint.states.map(row=>Float64Array.from(row));
  assert(states.length===dn.tail.cells.length+1&&states.every(row=>row.length===K),'Original complete node grid required');
  const inputHash=digest(bytes(states.flatMap(row=>Array.from(row))));
  const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
  const target=Float64Array.from(checkpoint.cutHeight,v=>v/radius**4),scales=new Float64Array(states.length);
  scales[0]=Math.max(1e-250,...Array.from(target,Math.abs));
  for(let n=0;n<scales.length-1;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
  const backend=dn.tail.nativeBatch(),prepared=backend.prepare(states,true),capsule=load(plan.files.capsule_coefficients.path);
  const fixtureIdentity=[];
  const coefficientOrder=['r3','r4','sqrt2','sqrt12','E','w2','pDenominator','targetFactor','sigma','fluxPrefactor','qLNumerator','meanFactor'];
  for(const old of capsule.fixtures){
    const actual=backend.inspectStage(prepared,old.stage);
    assert(bytes([actual.mu,actual.portRatio,scales[old.stage]]).equals(bytes([old.mu,old.portRatio,old.normalizationScale])),'Original mu/port/scale differs');
    assert(actual.initialBytes.equals(bytes(old.initial42)),'Original all42 initial bytes differ');
    assert(actual.cosineBytes.equals(bytes(capsule.trig.state_cos.flat()))&&actual.sineBytes.equals(bytes(capsule.trig.state_sin.flat())),'Original state trig differs');
    assert(actual.profileGrids.length===old.grid.length,'Original profile count differs');
    for(let i=0;i<old.grid.length;i++)
      assert(bytes(actual.profileGrids[i].flatMap(p=>[p.x,p.h])).equals(bytes(old.grid[i].flatMap(p=>[p.x,p.h]))),'Original literal cusp grid differs');
    const table=new Map(actual.points.map(p=>[p.profile+':'+bytes([p.x]).toString('hex'),p.values]));
    for(const p of old.points){
      const values=table.get(p.profile+':'+bytes([p.x]).toString('hex'));
      assert(values&&bytes(values).equals(bytes([...coefficientOrder.map(key=>p.coefficients[key]),...p.coefficients.pNumerator])),'Original complete coefficient point differs');
    }
    fixtureIdentity.push({stage:old.stage,all42_input_equal:true,state_trig_equal:true,mu_port_and_scale_equal:true,
      all_literal_grid_bytes_equal:true,all_original_coefficient_points_equal:true,coefficient_points:old.points.length,
      input_sha256:digest(actual.initialBytes),coefficient_bytes_sha256:digest(actual.coefficientBytes),
      grid_bytes_sha256:digest(actual.stepBytes)});
  }
  assert(backend.callCount===0,'A native call occurred before producer identity checks');
  summary.fixtureIdentity=fixtureIdentity;summary.static_metadata=backend.staticMetadataRef;
  summary.actual_grid_and_wire_counts=backend.staticMetadata.counts;
  summary.production_projectionFloor=dn.tail.parameters.projectionFloor;
  summary.original_state_sha256=inputHash;summary.target_sha256=digest(bytes(Array.from(target)));
  summary.scales_sha256=digest(bytes(Array.from(scales)));
  console.log(JSON.stringify({event:'original_static_producer_identity_passed',fixtureIdentity,
    counts:summary.actual_grid_and_wire_counts,complete_native_evaluates_so_far:backend.callCount}),'\n');
  const evaluateBegin=performance.now();
  const value=dn.tail.evaluate(states,target,true,scales);
  summary.complete_evaluate_seconds=(performance.now()-evaluateBegin)/1000;
  assert(backend.callCount===1,'Entry invoked other than one whole-evaluate native process');
  assert(digest(bytes(states.flatMap(row=>Array.from(row))))===inputHash,'Original input nodes were mutated');
  const peaks=value.residuals.map((r,n)=>{
    let j=0;for(let k=1;k<K;k++)if(Math.abs(r[k])>Math.abs(r[j]))j=k;
    return {stage:n,component:j,physicalMode:cfg.spacing*(j%M+1),kind:j<M?'Q':'pi',
      difference:r[j],flow:value.flows[n].out[j],target:states[n][j],scale:scales[n],normalized:Math.abs(r[j])/scales[n],
      minA:value.flows[n].minA,minD:value.flows[n].minD};
  });
  const raw={schema:'n4-native-adapter-complete-evaluate-v1',scope:summary.scope,input:plan.files.production_CP,
    config:cfg,manifest:plan.files.manifest,target:Array.from(target),scales:Array.from(scales),
    residuals:value.residuals.map(r=>Array.from(r)),end:Array.from(value.end),
    flows:value.flows.map(f=>({out:Array.from(f.out),J:Array.from(f.J),meanHeight:f.meanHeight,minA:f.minA,minD:f.minD})),
    norm:value.norm,minA:value.minA,minD:value.minD};
  fs.writeFileSync(plan.outputs.raw,gzipSync(JSON.stringify(raw)+'\n'),{flag:'wx'});
  Object.assign(summary,{status:'complete',raw:ref(plan.outputs.raw),native_evaluate_count:backend.callCount,
    original_normalizedResidual:value.norm,original_gate:cfg.solveTolerance,
    same_state_below_residual_gate:value.norm<cfg.solveTolerance,minA:value.minA,minD:value.minD,
    far_Robin_normalized_max:Math.max(...Array.from(value.end,v=>Math.abs(v)/scales.at(-1))),
    left_target_normalized_max:Math.max(...Array.from(target,(v,j)=>Math.abs(states[0][j]-v)/scales[0])),
    largestResidual:peaks.toSorted((a,b)=>b.normalized-a.normalized).slice(0,12),
    original_input_nodes_unchanged:true,production_J_shape:[K,K],saved_native_J_shape:[K+2,K],
    meanHeightToCut:value.flows.reduce((sum,f)=>sum+f.meanHeight,0),
    original_DN_acceptance_performed:false});
}catch(e){
  summary.status='failure';summary.error={name:e.name,message:String(e.message),stack:String(e.stack)};
  process.exitCode=1;
}
summary.seconds=(performance.now()-begin)/1000;
const output=saveJSON(plan.outputs.summary,summary);
console.log(JSON.stringify({event:'entry_terminal',status:summary.status,summary:output,
  original_normalizedResidual:summary.original_normalizedResidual,native_evaluate_count:summary.native_evaluate_count,
  error:summary.error??null}));
