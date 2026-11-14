// Independent short-window access to the original finite RK12 arithmetic.
// No source file, profile, original step size, stage port or native gate is
// replaced. This is a building block for a separately identified split probe.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const FLOW_SHA='717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f';
const sha=value=>crypto.createHash('sha256').update(value).digest('hex');

function actionsOnly(){
 if(process.env.GITHUB_ACTIONS!=='true'||
    (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('Same-schedule native RK calculations belong only to public repository Actions');
}
function numberRecord(value){
 const raw=Buffer.allocUnsafe(8);raw.writeDoubleLE(value);
 return {value:Number.isFinite(value)?value:null,float64le_hex:raw.toString('hex'),
  classification:Number.isNaN(value)?'NaN':value===Infinity?'positive-infinity':
   value===-Infinity?'negative-infinity':Object.is(value,-0)?'negative-zero':'finite'};
}
function rowsSHA(rows){
 const h=crypto.createHash('sha256');
 for(const row of rows){
  const raw=Buffer.allocUnsafe(row.length*8);
  for(let j=0;j<row.length;j++)raw.writeDoubleLE(row[j],j*8);
  h.update(raw);
 }
 return h.digest('hex');
}

/** Pure source transform; callers must separately bind the actual engine,
 * original complete configuration, physical profile and live stage layout.
 * Only the loop bounds and a read-only x/h observation are added. */
export function prepareWindowedFlowSource(original){
 if(sha(original)!==FLOW_SHA)throw Error('Original Fourier-product RK source bytes changed');
 const begin=' function flowStateWithJacobian(initial,segments,opts={}){';
 const end='\n return {...base,rhsWithJacobian,flowStateWithJacobian,variationalEvaluation:';
 if(original.split(begin).length!==2||original.split(end).length!==2)
  throw Error('Unique original RK function boundaries required');
 const start=original.indexOf(begin),stop=original.indexOf(end,start);
 if(stop<start)throw Error('Original RK source boundaries are out of order');
 const originalFunction=original.slice(start,stop).trim();
 const changes=[
  {before:'for(let n=0;n<count;n++){',
   after:'for(let n=opts.firstStep;n<opts.lastStep;n++){'},
  {before:'    const h=grid?grid[n+1]-grid[n]:ordinaryH,x=grid?grid[n]:n*ordinaryH,\n     a=field',
   after:'    const h=grid?grid[n+1]-grid[n]:ordinaryH,x=grid?grid[n]:n*ordinaryH;\n    opts.scheduleObserver?.(p,n,x,h);\n    const a=field'}
 ];
 let transformed=originalFunction;
 for(const item of changes){
  if(transformed.split(item.before).length!==2)throw Error('Unique original RK range/observation anchor required');
  transformed=transformed.replace(item.before,item.after);
 }
 let restored=transformed;
 for(const item of [...changes].reverse()){
  if(restored.split(item.after).length!==2)throw Error('Unique independent RK source change required');
  restored=restored.replace(item.after,item.before);
 }
 if(restored!==originalFunction)throw Error('Window access changed the original RK arithmetic');
 return {source:transformed,identity:{schema:'original-native-RK-window-source-v1',
  original_flow_module_sha256:FLOW_SHA,original_function_sha256:sha(originalFunction),
  window_function_sha256:sha(transformed),changes_sha256:sha(JSON.stringify(changes)),
  exact_source_roundtrip_verified:true,changes,
  all_original_RK_field_increment_state_and_tangent_expressions_retained:true,
  only_loop_range_and_readonly_schedule_observer_added:true}};
}

/** No import of a replacement RHS/J. The object is the original live engine.
 * The scope is one original profile without cusp cuts, as in stages43/58.
 * Mean integrals are kept in the full size=226 intermediate state. */
export function createNativeSameScheduleWindows({engine,cell,sourceTopic,stageIndex,steps=12,split=6}){
 actionsOnly();
 if(steps!==12||split!==6||!Number.isInteger(stageIndex)||stageIndex<0)
  throw Error('This first candidate preserves the original12-step6+6 grouping');
 if(engine!==cell.engine||engine.M!==112||engine.size!==226||
    typeof engine.rhsWithJacobian!=='function'||typeof engine.rk4!=='function'||
    !Array.isArray(cell.profiles)||cell.profiles.length!==1)
  throw Error('Use the actual complete112-mode original engine and single profile');
 const profile=cell.profiles[0],cuts=profile.integrationBreakpoints??[];
 if(cuts.length!==0)throw Error('This same-schedule wrapper is explicitly restricted to original no-cusp stages');
 if(!(Number.isFinite(cell.portRatio)&&cell.portRatio!==0))throw Error('Finite original nonzero stage port required');
 const file=path.join(sourceTopic,'scripts/78718-tail-fourier-product-flow.mjs');
 const prepared=prepareWindowedFlowSource(fs.readFileSync(file,'utf8'));
 // The original function closes over these exact original engine functions.
 // integrationGrid is unreachable in this deliberately no-cusp interface.
 const rawFlow=new Function('rhsWithJacobian','size','Kdim','integrationGrid',
  'return ('+prepared.source+');')(engine.rhsWithJacobian,engine.size,2*engine.M,
    ()=>{throw Error('No cusp-grid substitution is allowed in this no-cusp window interface');});
 const M=engine.M,K=2*M;
 const identity={schema:'original-native-RK12-six-plus-six-stage-v1',
  source:prepared.identity,stage:stageIndex,rawCell:cell.rawCell,rawSegment:cell.rawSegment,
  part:cell.part,parts:cell.parts,rawLeft:numberRecord(cell.rawLeft),rawRight:numberRecord(cell.rawRight),
  mu:numberRecord(cell.mu),original_port_ratio:numberRecord(cell.portRatio),steps,split,
  original_profile_function_sha256:sha(profile.toString()),
  profile_function_hash_is_not_a_complete_closure_identity:true,
  original_rhs_with_J_function_sha256:sha(engine.rhsWithJacobian.toString()),
  original_no_J_rk4_function_sha256:sha(engine.rk4.toString()),
  input_shape_dimension:K,full_state_dimension:engine.size,
  profile_object_not_reparameterized:true,additional_ODE_steps:0,
  withJac_schedule:'x=n*(1/12), h=1/12 from original pinned RK body',
  noJ_schedule:'x=k/12, h=1/12 through original live engine.rk4',
  same_profile_object_and_independent_original_schedules:true,
  original_port_division_only_at_original_exit:true,
  whole_mean_state_retained_across_probe_windows:true,
  no_changes_to_original_graphs_gains_far_sigma_or_native_acceptance:true};

 function check(initial,first,last){
  if(!(initial instanceof Float64Array)||initial.length!==engine.size)
   throw Error('Keep the original full226-entry RK state, including both mean integrals');
  if(!((first===0&&last===6)||(first===6&&last===12)||(first===0&&last===12)))
   throw Error('Only original half windows or the original full12-step reference are defined');
 }
 function withJac(initial,first,last){
  actionsOnly();check(initial,first,last);const schedule=[];
  const result=rawFlow(initial,[profile],{stepsPerSegment:steps,firstStep:first,lastStep:last,
   scheduleObserver(p,n,x,h){
    if(p!==profile)throw Error('The actual original profile object changed');
    schedule.push({step:n,x:numberRecord(x),h:numberRecord(h),
     RK_abscissae:[numberRecord(x),numberRecord(x+h/2),numberRecord(x+h/2),numberRecord(x+h)]});
   }});
  return {...result,window:{kind:'withJac',firstStep:first,lastStep:last,schedule,
   state_float64le_sha256:rowsSHA([result.state]),tangent_float64le_sha256:rowsSHA([result.tangent]),
   tangent_restarted_at_identity_for_this_short_block:true,
   profile_object_unchanged:true,port_ratio_not_yet_applied:true}};
 }
 function noJac(initial,first,last){
  actionsOnly();check(initial,first,last);let state=Float64Array.from(initial);const schedule=[];
  for(let k=first;k<last;k++){
   const x=k/steps,h=1/steps;
   schedule.push({step:k,x:numberRecord(x),h:numberRecord(h),
    RK_abscissae:[numberRecord(x),numberRecord(x+h/2),numberRecord(x+h/2),numberRecord(x+h)]});
   state=engine.rk4(state,profile,x,h);
  }
  return {state,window:{kind:'noJ',firstStep:first,lastStep:last,schedule,
   state_float64le_sha256:rowsSHA([state]),profile_object_unchanged:true,port_ratio_not_yet_applied:true}};
 }
 function originalExit(result,withJacFlag){
  const out=Float64Array.from(result.state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio);
  let J=null;
  if(withJacFlag){
   J=new Float64Array(K*K);
   for(let i=0;i<K;i++)for(let j=0;j<K;j++)J[i*K+j]=result.tangent[i*K+j]/(i<M?1:cell.portRatio);
  }
  return {out,J,meanHeight:result.state[K]+result.state[K+1],
   original_port_ratio:cell.portRatio,original_port_division_applied_exactly_once:true};
 }
 function splitPropagation(initial,{withJac:withJacFlag=true}={}){
  actionsOnly();
  const run=withJacFlag?withJac:noJac,inner=run(initial,0,6),outer=run(inner.state,6,12);
  const exit=originalExit(outer,withJacFlag);
  const innerShapeJ=withJacFlag?inner.tangent.slice(0,K*K):null;
  return {identity,inner,outer,exit,innerShapeJ,
   outerShapeJWithOriginalPort:exit.J,
   original_input_float64le_sha256:rowsSHA([initial]),
   intermediate_full_state_float64le_sha256:rowsSHA([inner.state]),
   local_J_blocks_are_not_the_original_long_J_bytes:true,
   local_J_blocks_have_not_been_multiplied_into_a_long_matrix:true,
   reordered_shooting_parts:[{kind:'outer',firstStep:6,lastStep:12,portRatio:cell.portRatio},
    {kind:'inner',firstStep:0,lastStep:6,portRatio:1}],
   native_accepted:false,task_completed:false};
 }
 return {identity,withJac,noJac,originalExit,splitPropagation};
}

/** Only layout/weight selection. It never constructs new graphs/gains or
 * claims that a low split residual already satisfies the old whole-stage gate.
 * The caller supplies and binds the actual original sigma array. */
export function originalNodeSplitLayout(originalDepth,splitStages,originalScales){
 actionsOnly();
 if(!Number.isInteger(originalDepth)||originalDepth<1||originalScales.length!==originalDepth+1)
  throw Error('Complete original node and sigma layout required');
 const selected=[...splitStages].sort((a,b)=>a-b);
 if(new Set(selected).size!==selected.length||selected.some(n=>!Number.isInteger(n)||n<0||n>=originalDepth))
  throw Error('Explicit distinct original split stages required');
 const keep=new Set(selected),oldToNew=[],cells=[],newScales=[];
 for(let n=0;n<originalDepth;n++){
  oldToNew[n]=cells.length;newScales.push(originalScales[n]);
  if(keep.has(n)){
   cells.push({newStage:cells.length,originalStage:n,window:[6,12],port:'original'});
   newScales.push(originalScales[n]);
   cells.push({newStage:cells.length,originalStage:n,window:[0,6],port:'one'});
  }else cells.push({newStage:cells.length,originalStage:n,window:[0,12],port:'original'});
 }
 oldToNew[originalDepth]=cells.length;newScales.push(originalScales[originalDepth]);
 return {schema:'original-native-shooting-same-schedule-split-layout-v1',
  originalDepth,newDepth:cells.length,selectedOriginalStages:selected,oldToNew,cells,
  originalScalesFloat64LESHA256:rowsSHA([originalScales]),
  explicitNewScales:Float64Array.from(newScales),
  internalScaleRule:'The inserted node uses the actual original parent-stage sigma; every old-node sigma is preserved',
  no_new_gains_or_graphs_used_for_scales:true,
  original_full_flow_readback_on_old_nodes_still_required:true,
  new_local_jacobians_and_new_augmented_system_have_separate_identity:true,
  new_convergence_or_acceptance_claimed:false};
}
