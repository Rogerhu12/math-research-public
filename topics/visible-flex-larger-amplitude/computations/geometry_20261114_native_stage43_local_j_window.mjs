// One existing actual41 RK step, with all four actual local Jacobians exposed.
// The original complete226 state formulas and original tangent formulas remain
// literal. No preceding step is replayed and no additional ODE step is added.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {preparePerStepFlowSource,numberRecord}
 from './geometry_20261114_native_rawcell0_step_windows.mjs';

const FLOW_SHA='717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f';
const PREPARED_SHA='447590785c402226adef6af880a44f8da6e2831786724d2762ab6c2c0addf5ab';
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
function actionsOnly(){
 if(process.env.GITHUB_ACTIONS!=='true'||
    (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('Original local-J computations belong only to the public repository Actions');
}
export function prepareStage43Step11Source(original){
 if(sha(original)!==FLOW_SHA)throw Error('Original product-flow source changed');
 const parent=preparePerStepFlowSource(original);
 if(sha(parent.source)!==PREPARED_SHA)throw Error('Actual41 per-step function source changed');
 const before='   for(let n=0;n<count;n++){\n';
 const after=before+'    if(n!==11)continue;\n';
 if(parent.source.split(before).length!==2)throw Error('One original RK loop required');
 const source=parent.source.replace(before,after);
 if(source.replace(after,before)!==parent.source)throw Error('Exact single-step selection roundtrip failed');
 return {source,identity:{
  schema:'same-original-stage43-step11-local-J-function-v1',
  original_flow_module_sha256:FLOW_SHA,actual41_per_step_function_sha256:PREPARED_SHA,
  selected_function_sha256:sha(source),parent:parent.identity,
  added_selection:{before,after},exact_source_selection_roundtrip:true,
  selected_original_stage:43,selected_flow_step:11,
  complete226_state_RK_and_tangent_arithmetic_retained:true,
  earlier_steps_skipped_without_evaluation:true,additional_ODE_steps:0,
  original_four_rhsWithJacobian_calls_retained:true,
  output_port_only_at_original_exit:true}};
}
export function createStage43Step11Window({engine,cell,sourceTopic,originalGrid}){
 actionsOnly();
 if(cell.rawCell!==0||cell.rawSegment!==3||cell.part!==4||cell.parts!==8||
    engine!==cell.engine||engine.M!==112||engine.size!==226||
    !Array.isArray(cell.profiles)||cell.profiles.length!==1||
    (cell.profiles[0].integrationBreakpoints??[]).length!==0||
    typeof engine.rhsWithJacobian!=='function'||
    typeof originalGrid?.integrationGrid!=='function'||
    !(Number.isFinite(cell.portRatio)&&cell.portRatio===1))
  throw Error('Use the exact original old43 ordinary RK12 stage, complete112 modes, and port1');
 const original=fs.readFileSync(path.join(sourceTopic,'scripts/78718-tail-fourier-product-flow.mjs'),'utf8');
 const prepared=prepareStage43Step11Source(original),K=224,size=226;
 const rawFlow=new Function('rhsWithJacobian','size','Kdim','integrationGrid',
  'return ('+prepared.source+');')(engine.rhsWithJacobian,size,K,originalGrid.integrationGrid);
 const p=cell.profiles[0];
 const identity={...prepared.identity,
  mu:numberRecord(cell.mu),original_port_ratio:numberRecord(cell.portRatio),
  profile_function_sha256:sha(p.toString()),
  original_rhs_with_J_function_sha256:sha(engine.rhsWithJacobian.toString()),
  original_flow_function_object_sha256:sha(engine.flowStateWithJacobian.toString()),
  original_grid_identity:originalGrid.identity,
  complete_mean_state_not_reset:true,no_profile_reparameterization:true,
  original_no_J_schedule_not_evaluated_or_equated:true};
 function run(initial,observer={}){
  actionsOnly();
  if(!(initial instanceof Float64Array)||initial.length!==size)
   throw Error('Use the saved actual41 full226 step input including both means');
  let profiles=0,steps=0,fields=0,active=null;
  const result=rawFlow(initial,cell.profiles,{stepsPerSegment:12,
   profileSchedule(profile,cuts,grid,count,ordinaryH){
    if(profile!==p||cuts.length!==0||grid!==null||count!==12||profiles++)
     throw Error('Keep the single original ordinary12-step schedule');
    observer.profileSchedule?.({profile_index:0,cuts,grid,count,ordinaryH});
   },
   beforeStep(profile,n,count,grid,x,h,state,tangent){
    if(profile!==p||n!==11||count!==12||grid!==null||active||steps!==0)
     throw Error('Only original flow step11 may execute');
    active={global_step:n,profile_index:0,grid_index:n,grid_branch:'ordinary',
     x,h,field_calls:0,final_original_step:true};
    observer.beforeStep?.({...active,state,tangent});
   },
   beforeField(state,profile,x){
    if(!active||profile!==p||active.field_calls>=4)
     throw Error('Field belongs to the single original selected step');
    observer.beforeField?.({...active,field_index:active.field_calls,x,state});
   },
   afterField(state,profile,x,f,cumulative){
    if(!active||profile!==p||active.field_calls>=4||
       f.jacobian.length!==size*K||f.derivative.length!==size)
     throw Error('Retain all226 rows and224 local derivative columns');
    observer.afterField?.({...active,field_index:active.field_calls,x,state,
     derivative:f.derivative,jacobian:f.jacobian,root:f.root,cumulative});
    active.field_calls++;fields++;
   },
   afterStep(profile,n,count,grid,x,h,state,tangent,cumulative){
    if(!active||profile!==p||n!==11||active.field_calls!==4)
     throw Error('Exactly four original fields must finish before the stored exit');
    const out=Float64Array.from(state.slice(0,K),(v,j)=>j<112?v:v/cell.portRatio);
    const J=new Float64Array(K*K);
    for(let i=0;i<K;i++)for(let j=0;j<K;j++)
     J[i*K+j]=tangent[i*K+j]/(i<112?1:cell.portRatio);
    observer.afterStep?.({...active,state,tangent,out,J,
     mean_tangent_rows:tangent.slice(K*K),cumulative,
     port_applied:true,port_ratio:cell.portRatio});
    steps++;active=null;
   }});
  if(profiles!==1||steps!==1||fields!==4||active!==null)
   throw Error('Only the one complete original step with four local A was requested');
  return {...result,selected_steps:steps,returned_local_J:fields,
   all_original_mean_values_carried:true,additional_ODE_steps:0};
 }
 return {identity,run};
}
