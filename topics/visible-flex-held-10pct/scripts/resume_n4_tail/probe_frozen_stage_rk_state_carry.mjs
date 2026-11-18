// One read-only arithmetic comparison on three prescribed original stages.
// Only each final state-plus-RK-increment addition may use a Kahan carry.
// In real arithmetic the carry is identically zero, so the RK formula is unchanged.
// RHS and intermediate stages read only the current Float64 state, never the carry.
// Carry variables are numerical bookkeeping, not extra physical unknowns.
// This is not an end-to-end higher-precision flow or an ODE error certificate.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {gunzipSync,gzipSync} from 'node:zlib';
import {createHash} from 'node:crypto';

const [topicArg,input,locator,runSummary,inheritedFixture,prefixArg]=process.argv.slice(2);
if(!prefixArg)throw Error('Need original source topic, failed state, locator, run summary, frozen first-comparison fixture, new output prefix');
const topic=path.resolve(topicArg),prefix=path.resolve(prefixArg);
const sha=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const digest=x=>createHash('sha256').update(x).digest('hex');
const load=p=>JSON.parse(p.endsWith('.gz')?gunzipSync(fs.readFileSync(p)):fs.readFileSync(p,'utf8'));
const record=load(input),located=load(locator),run=load(runSummary),cfg=record.config;
const originalConfig=JSON.stringify(cfg);
const frozen=load(inheritedFixture);
if(frozen.input_sha256!==sha(input)||JSON.stringify(frozen.config)!==originalConfig)
  throw Error('The inherited original fixture differs');
for(const [name,value] of Object.entries(frozen.source_sha256))
  if(sha(name)!==value)throw Error('The inherited comparison source changed: '+name);
if(!record.response?.failed||located.inputAccepted||located.input_sha256!==sha(input))
  throw Error('Exact complete failed input and its original locator required');
if(located.replayNormalizedResidual!==record.response.lastIteration.norm||
   located.originalGate!==2e-9||cfg.solveTolerance!==2e-9)
  throw Error('Original stopping-state/gate identity differs');
const sources={...located.source_sha256};
for(const [name,value] of Object.entries(record.source_sha256))
  sources[path.resolve(topic,'scripts',name)]=value;
for(const [name,value] of Object.entries(run.periodic_engine_sha256))
  sources[path.resolve(topic,'scripts/periodic-quadrature',name)]=value;
for(const name of fs.readdirSync(path.join(topic,'scripts/periodic-quadrature')))
  if(name.endsWith('.mjs')&&!sources[path.resolve(topic,'scripts/periodic-quadrature',name)])
    throw Error('Unbound actual periodic module: '+name);
for(const [name,value] of Object.entries(sources))if(sha(name)!==value)
  throw Error('Bound original source changed: '+name);
const root=path.join(topic,'repro/source-root');
process.env.VISIBLE_FLEX_SOURCE_ROOT=root;
process.env.CLOSING_TAIL_CACHE=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const rootScripts=path.join(root,'topics/large-amplitude-twist-flex/scripts');
const additionalSources={};
for(const name of fs.readdirSync(rootScripts))
  if(/\.(mjs|cjs)$/.test(name))additionalSources[path.join(rootScripts,name)]=sha(path.join(rootScripts,name));
sources[path.resolve(process.argv[1])]=sha(process.argv[1]);
const {createRecalibrationFactory}=await import(pathToFileURL(path.join(topic,'scripts/closing_weighted_tail.mjs')));
const {createSplitFluxCompactTailDN}=await import(pathToFileURL(path.join(topic,'scripts/950f-tail-stage-split.mjs')));
const {integrationGrid}=await import(pathToFileURL(path.join(rootScripts,'f6tail_cusp_grid.mjs')));
const physical=createRecalibrationFactory(cfg).assemble();
const dn=createSplitFluxCompactTailDN({...cfg,tail:physical}),cp=record.response.checkpoint;
const M=cfg.modes,K=2*M,size=K+2,stages=dn.tail.cells.length;
if(cp.states.length!==stages+1||cp.states.some(row=>row.length!==K))throw Error('Complete original state shape required');
const namedStages=[43,38,175];
if(M!==20||cfg.spacing!==4||cfg.shootingParts!==32||cfg.steps!==16)
  throw Error('This predeclared experiment is only the recorded n4 M20/parts32/RK16 state');
const paths=Object.fromEntries(['inputs','original','kahan','summary'].map(name=>
  [name,prefix+'-'+name+(name==='summary'?'.json':'.json.gz')]));
for(const file of Object.values(paths))if(fs.existsSync(file))throw Error('A frozen output already exists: '+file);
fs.mkdirSync(path.dirname(prefix),{recursive:true});
function bytes(values){
  const b=Buffer.alloc(8*values.length);
  for(let j=0;j<values.length;j++){
    if(!Number.isFinite(values[j]))throw Error('Non-finite frozen numeric value');
    b.writeDoubleLE(values[j],8*j);
  }
  return b;
}
const hashNumbers=values=>digest(bytes(values));
const originalStateIdentity=hashNumbers(cp.states.flat());
const radius=dn.tail.cells[0].profiles.at(-1)(1).r;
const target=cp.cutHeight.map(v=>v/radius**4),scales=new Float64Array(stages+1);
scales[0]=Math.max(1e-250,...target.map(Math.abs));
for(let n=0;n<stages;n++)scales[n+1]=scales[n]/Math.abs(dn.tail.gains[n][0]);
function grids(cell){
  return cell.profiles.map(profile=>{
    const cuts=profile.integrationBreakpoints??[];
    const g=cuts.length?integrationGrid(cfg.steps,cuts):null;
    const count=g?g.length-1:cfg.steps,h0=1/cfg.steps;
    return Array.from({length:count},(_,n)=>({x:g?g[n]:n*h0,h:g?g[n+1]-g[n]:h0}));
  });
}
function manualFlow(cell,initial,grid,useStateCarry){
  let state=Float64Array.from(initial),minA=Infinity,minD=Infinity;
  const carry=new Float64Array(size);
  let maximumRootRelativeResidual=0,rootEvaluations=0,changedStateUpdates=0,maximumCarry=0,maximumStateUpdateDifference=0;
  function field(s,p,x){
    const value=cell.engine.rhsWithJacobian(s,p,x);
    // Copy before any subsequent engine invocation; do not retain mutable views.
    const derivative=Float64Array.from(value.derivative);
    minA=Math.min(minA,value.root.e.minA);minD=Math.min(minD,value.root.e.minD);
    maximumRootRelativeResidual=Math.max(maximumRootRelativeResidual,value.root.err/value.root.scale);
    rootEvaluations++;
    return derivative;
  }
  const increment=(s,f,h)=>Float64Array.from(s,(v,j)=>v+h*f[j]);
  for(let i=0;i<cell.profiles.length;i++){
    const p=cell.profiles[i];
    for(const {x,h} of grid[i]){
      const a=field(state,p,x),b=field(increment(state,a,h/2),p,x+h/2),
        c=field(increment(state,b,h/2),p,x+h/2),d=field(increment(state,c,h),p,x+h);
      for(let j=0;j<size;j++){
        const sum=a[j]+2*b[j]+2*c[j]+d[j],stepIncrement=h*sum/6;
        if(useStateCarry){
          const previous=state[j],ordinary=previous+stepIncrement;
          const corrected=stepIncrement-carry[j],next=previous+corrected;
          carry[j]=(next-previous)-corrected;
          state[j]=next;
          if(!Object.is(next,ordinary))changedStateUpdates++;
          maximumStateUpdateDifference=Math.max(maximumStateUpdateDifference,Math.abs(next-ordinary));
          maximumCarry=Math.max(maximumCarry,Math.abs(carry[j]));
        }else state[j]+=stepIncrement;
      }
    }
  }
  return {state:Float64Array.from(state),minA,minD,maximumRootRelativeResidual,
    rootEvaluations,changedStateUpdates,maximumCarry,maximumStateUpdateDifference,carry:Array.from(carry)};
}
function residual(cell,state,node,scale){
  const out=Float64Array.from(state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio);
  const signed=Float64Array.from(out,(v,j)=>v-node[j]);
  let norm=0,component=0;
  for(let j=0;j<K;j++)if(Math.abs(signed[j])/scale>norm){norm=Math.abs(signed[j])/scale;component=j;}
  return {out:Array.from(out),signed:Array.from(signed),normalizedResidual:norm,component};
}
const nq=dn.tail.cells[0].engine.quadratureIndependentNodes,N=cfg.quadrature,sq2=Math.sqrt(2);
const frequency=Array.from({length:M},(_,j)=>(j+1)*cfg.spacing);
const trig={state_cos:[],state_sin:[],jacobian_cos:[],jacobian_sin:[]};
for(let n=0;n<nq;n++){
  const theta=2*Math.PI*n/N;
  trig.state_cos.push([1,...frequency.map(m=>sq2*Math.cos(m*theta))]);
  trig.state_sin.push(frequency.map(m=>sq2*Math.sin(m*theta)));
  trig.jacobian_cos.push([1,...frequency.map(m=>sq2*Math.cos(m*2*Math.PI*n/N))]);
  trig.jacobian_sin.push(frequency.map(m=>sq2*Math.sin(m*2*Math.PI*n/N)));
}
for(const [name,values] of Object.entries(trig))
  if(hashNumbers(values.flat())!==hashNumbers(frozen.trig[name].flat()))
    throw Error('The inherited trigonometric constants changed: '+name);
const originalRows=[],newRows=[],fixtures=[],summaries=[];
const began=performance.now();
for(const n of namedStages){
  const cell=dn.tail.cells[n],initial=new Float64Array(size);initial.set(cp.states[n+1]);
  const targetNode=Array.from(cp.states[n]),grid=grids(cell);
  const geometry=[];
  for(let i=0;i<cell.profiles.length;i++)for(const {x,h} of grid[i])
    for(const xx of [x,x+h/2,x+h])geometry.push({profile:i,x:xx,
      values:cell.engine.geometry(cell.profiles[i],xx)});
  const inherited=frozen.fixtures.find(row=>row.stage===n);
  if(!inherited||!bytes(initial).equals(bytes(inherited.initial42))||
     !bytes(targetNode).equals(bytes(inherited.targetNode40))||
     digest(JSON.stringify(grid))!==inherited.grid_sha256||
     digest(JSON.stringify(geometry))!==inherited.sampled_original_geometry_sha256)
    throw Error('Original input/grid/profile fixture changed at stage '+n);
  const referenceRaw=cell.engine.flowStateWithJacobian(initial,cell.profiles,{stepsPerSegment:cfg.steps});
  const reference=Float64Array.from(referenceRaw.state);
  const referenceMinA=referenceRaw.minA,referenceMinD=referenceRaw.minD;
  const plain=manualFlow(cell,initial,grid,false);
  const equal=bytes(reference).equals(bytes(plain.state));
  const baselineDiff=Array.from(plain.state,(v,j)=>v-reference[j]);
  if(!equal){
    fs.writeFileSync(prefix+'-baseline-mismatch.json',JSON.stringify({stage:n,reference:Array.from(reference),plain:Array.from(plain.state),baselineDiff})+'\n');
    throw Error('The unchanged RK baseline does not reproduce all 42 original state outputs at stage '+n);
  }
  const rr=residual(cell,reference,targetNode,scales[n]);
  const named=located.largestResidual.find(row=>row.stage===n);
  if(!named||rr.normalizedResidual!==named.normalizedResidual||rr.component!==named.component)
    throw Error('The original named full-Jacobian row no longer matches its locator');
  const compensated=manualFlow(cell,initial,grid,true);
  if(!bytes(reference).equals(bytes(Float64Array.from(referenceRaw.state))))
    throw Error('A later engine call mutated the saved original reference view');
  const nr=residual(cell,compensated.state,targetNode,scales[n]);
  const inputIdentity=hashNumbers(initial),referenceIdentity=hashNumbers(reference);
  const basic={stage:n,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
    rawLeft:cell.rawLeft,rawRight:cell.rawRight,portRatio:cell.portRatio,mu:cell.mu,
    normalizationScale:scales[n],inputNode:n+1,input42_sha256:inputIdentity,
    targetNode40_sha256:hashNumbers(targetNode),grid_sha256:digest(JSON.stringify(grid)),
    sampled_original_geometry_sha256:digest(JSON.stringify(geometry))};
  fixtures.push({...basic,initial42:Array.from(initial),targetNode40:targetNode,grid,geometry});
  originalRows.push({...basic,reference42:Array.from(reference),manualPlain42:Array.from(plain.state),
    reference42_sha256:referenceIdentity,baseline42_bitwise_identical:true,
    referenceMinA,referenceMinD,...plain,state:Array.from(plain.state),residual:rr});
  newRows.push({...basic,arithmetic_change:'Restore the ordinary four-term RK slope sum; only final state-plus-increment uses a per-component Kahan carry, zero at the beginning of this stage. RHS/intermediate formulas read Float64 state only. Carries are not physical unknowns.',
    ...compensated,state:Array.from(compensated.state),output42_sha256:hashNumbers(compensated.state),residual:nr});
  const diffs=Array.from(compensated.state,(v,j)=>v-reference[j]);
  const normalizedOutDifference=Math.max(...nr.out.map((v,j)=>Math.abs(v-rr.out[j])/scales[n]));
  const j=named.component;
  summaries.push({...basic,baseline_all42_bitwise_identical:true,
    original_output42_sha256:referenceIdentity,compensated_output42_sha256:hashNumbers(compensated.state),
    original_normalized_residual:rr.normalizedResidual,compensated_normalized_residual:nr.normalizedResidual,
    original_peak_component:rr.component,compensated_peak_component:nr.component,
    original_peak_physical_mode:(rr.component%M+1)*cfg.spacing,
    compensated_peak_physical_mode:(nr.component%M+1)*cfg.spacing,
    original_named_component_signed_residual:rr.signed[j],
    compensated_same_component_signed_residual:nr.signed[j],
    original_named_component_ulp:named.componentUlp,
    original_flow_change_at_named_component:nr.out[j]-rr.out[j],
    flow_change_at_named_component_over_recorded_ulp:(nr.out[j]-rr.out[j])/named.componentUlp,
    maximum_original_normalized_flow_change:normalizedOutDifference,
    changed_output42_components:diffs.filter(v=>v!==0).length,
    maximum_output42_absolute_change:Math.max(...diffs.map(Math.abs)),
    maximum_mean2_absolute_change:Math.max(...diffs.slice(K).map(Math.abs)),
    original_minA:referenceMinA,original_minD:referenceMinD,
    compensated_minA:compensated.minA,compensated_minD:compensated.minD,
    original_maximum_point_root_relative_residual:plain.maximumRootRelativeResidual,
    compensated_maximum_point_root_relative_residual:compensated.maximumRootRelativeResidual,
    changed_local_state_updates:compensated.changedStateUpdates,
    maximum_auxiliary_carry:compensated.maximumCarry,
    maximum_final_auxiliary_carry:Math.max(...compensated.carry.map(Math.abs)),
    final_carry42_sha256:hashNumbers(compensated.carry),
    maximum_local_state_update_difference:compensated.maximumStateUpdateDifference,
    original_point_root_evaluations:plain.rootEvaluations,
    compensated_point_root_evaluations:compensated.rootEvaluations});
  console.log(JSON.stringify({event:'named_stage_arithmetic_complete',...summaries.at(-1)}));
}
if(originalConfig!==JSON.stringify(cfg)||originalStateIdentity!==hashNumbers(cp.states.flat()))
  throw Error('Input configuration or state was mutated');
const context={input: path.resolve(input),input_sha256:sha(input),locator_sha256:sha(locator),
  inherited_fixture:{path:path.resolve(inheritedFixture),sha256:sha(inheritedFixture)},
  inherited_probe_sha256:'d6312e79aa156f116f8673e0eb76b9b02711b689091759b1c69e6e05534d5023',
  original_run_summary_sha256:sha(runSummary),config:cfg,named_stages:namedStages,
  source_sha256:sources,additional_current_root_source_sha256:additionalSources,
  additional_source_scope:'These root-module hashes bind this read-only comparison; they do not retroactively add hashes to an earlier execution.',
  command:process.argv,modes:M,spacing:cfg.spacing,quadrature:N,independent_quadrature_nodes:nq,
  steps:cfg.steps,originalGate:cfg.solveTolerance,stage_count:stages,
  complete_input_states_sha256:originalStateIdentity,complete_cut_height_sha256:hashNumbers(cp.cutHeight)};
function saveGz(file,value){fs.writeFileSync(file,gzipSync(JSON.stringify(value)+'\n'));return {path:file,sha256:sha(file)};}
const inputs=saveGz(paths.inputs,{...context,scope:'Frozen three-stage inputs, original RK grid, sampled original geometry and original state/analytic-Jacobian trigonometric constant formulas. No continuous profile certificate.',trig,fixtures});
const old=saveGz(paths.original,{...context,scope:'Unchanged original full-Jacobian flow and its bitwise-identical 42-component manual RK state replay.',rows:originalRows});
const changed=saveGz(paths.kahan,{...context,scope:'Only final state-plus-RK-increment additions carry per-component Kahan errors across the original steps. Ordinary four-term slope sums and RHS/intermediate formulas stay unchanged. This is not an end-to-end higher-precision algorithm, an exact ODE flow or a nonlinear-tail solution.',rows:newRows});
const result={...context,scope:'Read-only three-stage arithmetic comparison using the prior frozen fixtures. Only final state-plus-increment addition gets a zero-initialized per-component Kahan carry; RHS reads the rounded Float64 state, not the carry. In real arithmetic the carry remains zero. No complete-tail replay, DN/Newton solve, state checkpoint update, physical change or acceptance is performed.',
  fixtures:inputs,original:old,compensated:changed,
  trig_float64_le_sha256:Object.fromEntries(Object.entries(trig).map(([k,v])=>[k,hashNumbers(v.flat())])),
  named_results:summaries,states_changed:false,checkpoint_written:false,
  full_tail_replay_performed:false,nonlinear_solver_invoked:false,
  seconds:(performance.now()-began)/1000};
fs.writeFileSync(paths.summary,JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({event:'terminal',summary:paths.summary,sha256:sha(paths.summary),seconds:result.seconds}));
