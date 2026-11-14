// Original state RK formulas and all four full local A, from saved actual41
// full226 inputs. The discarded binary64 tangent multiplication is skipped;
// no placeholder tangent is exposed as a Jacobian. A separate pinned worker
// applies actual50's direct longdouble RK formula to the four returned A.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {preparePerStepFlowSource,numberRecord}
 from './geometry_20261114_native_rawcell0_step_windows.mjs';

const FLOW_SHA='717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f';
const PREPARED_SHA='447590785c402226adef6af880a44f8da6e2831786724d2762ab6c2c0addf5ab';
const sha=x=>crypto.createHash('sha256').update(x).digest('hex');
const stable=v=>Array.isArray(v)?v.map(stable):v&&typeof v==='object'?
 Object.fromEntries(Object.keys(v).sort().map(k=>[k,stable(v[k])])):v;
const equal=(a,b,label)=>{if(JSON.stringify(stable(a))!==JSON.stringify(stable(b)))
 throw Error('Original per-step identity differs: '+label);};
function actionsOnly(){
 if(process.env.GITHUB_ACTIONS!=='true'||
    (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('Original per-step local A belongs only to this public repository Actions');
}

export function prepareDirectLDStateSource(original){
 if(sha(original)!==FLOW_SHA)throw Error('Original complete product-flow source changed');
 const parent=preparePerStepFlowSource(original);
 if(sha(parent.source)!==PREPARED_SHA)throw Error('Actual41 original-step preparation changed');
 const changes=[
  {before:'   for(let n=0;n<count;n++){\n',
   after:'   for(let n=0;n<count;n++){\n    if(p!==opts.selectedProfile||n!==opts.selectedGridIndex)continue;\n'},
  {before:'   for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){const z=f.jacobian[i*Kdim+j];for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*t[j*Kdim+k];}\n',
   after:'   // The old binary64 tangent product is intentionally not formed.\n   // dt is an internal zero placeholder, never an exported derivative.\n'}
 ];
 let source=parent.source;
 for(const row of changes){
  if(source.split(row.before).length!==2)throw Error('Unique original selection/tangent-product anchor required');
  source=source.replace(row.before,row.after);
 }
 let restored=source;
 for(const row of [...changes].reverse()){
  if(restored.split(row.after).length!==2)throw Error('Unique reversible local-A change required');
  restored=restored.replace(row.after,row.before);
 }
 if(restored!==parent.source)throw Error('Source roundtrip did not restore the literal original state/RK body');
 return {source,identity:{schema:'original-native-saved-step-local-A-only-source-v1',
  original_flow_module_sha256:FLOW_SHA,actual41_per_step_function_sha256:PREPARED_SHA,
  selected_state_function_sha256:sha(source),parent:parent.identity,changes,
  exact_source_roundtrip:true,original_complete226_state_expressions_retained:true,
  original_four_rhsWithJacobian_calls_retained:true,
  old_binary64_tangent_matrix_products_skipped:true,
  internal_unused_zero_tangent_not_exported_as_any_J:true,
  prior_steps_not_evaluated_before_saved_input:true,additional_ODE_steps:0}};
}

export function createDirectLDLocalAWindow({engine,cell,sourceTopic,stageIndex,originalGrid}){
 actionsOnly();
 if(engine!==cell.engine||cell.rawCell!==0||engine.M!==112||engine.size!==226||
    !Number.isInteger(stageIndex)||stageIndex<0||stageIndex>=72||
    !Array.isArray(cell.profiles)||!cell.profiles.length||
    typeof engine.rhsWithJacobian!=='function'||typeof originalGrid?.integrationGrid!=='function'||
    !(Number.isFinite(cell.portRatio)&&cell.portRatio!==0))
  throw Error('Use the unchanged original rawCell0 complete112-mode engine and port');
 const prepared=prepareDirectLDStateSource(fs.readFileSync(
  path.join(sourceTopic,'scripts/78718-tail-fourier-product-flow.mjs'),'utf8'));
 const K=224,size=226,profiles=cell.profiles;
 const rawFlow=new Function('rhsWithJacobian','size','Kdim','integrationGrid',
  'return ('+prepared.source+');')(engine.rhsWithJacobian,size,K,originalGrid.integrationGrid);
 const identity={...prepared.identity,stage:stageIndex,rawCell:cell.rawCell,
  rawSegment:cell.rawSegment,part:cell.part,parts:cell.parts,
  rawLeft:numberRecord(cell.rawLeft),rawRight:numberRecord(cell.rawRight),mu:numberRecord(cell.mu),
  original_port_ratio:numberRecord(cell.portRatio),steps:12,profiles:profiles.length,
  profile_function_sha256:profiles.map(p=>sha(p.toString())),
  original_rhs_with_J_function_sha256:sha(engine.rhsWithJacobian.toString()),
  original_flow_function_object_sha256:sha(engine.flowStateWithJacobian.toString()),
  original_grid_identity:originalGrid.identity,
  full226_saved_input_including_both_means:true,no_profile_reparameterization:true,
  original_no_J_schedule_not_evaluated_or_equated:true};

 function run(initial,schedule,originalProfileSchedules,observer={}){
  actionsOnly();
  if(!(initial instanceof Float64Array)||initial.length!==size||
     !Number.isInteger(schedule.global_step)||!Number.isInteger(schedule.profile_index)||
     !Number.isInteger(schedule.grid_index)||!profiles[schedule.profile_index])
   throw Error('Select a saved actual41 full226 input and its actual original schedule');
  let seenProfiles=0,seenSteps=0,fields=0,active=null;
  const selected=profiles[schedule.profile_index];
  const result=rawFlow(initial,profiles,{stepsPerSegment:12,
   selectedProfile:selected,selectedGridIndex:schedule.grid_index,
   profileSchedule(p,cuts,grid,count,ordinaryH){
    const index=profiles.indexOf(p);
    if(index!==seenProfiles++)throw Error('Preserve the complete original profile order');
    const current={profile_index:index,grid_branch:grid?'integrationGrid':'ordinary',step_count:count,
     cuts:Array.from(cuts,numberRecord),grid:grid?Array.from(grid,numberRecord):null,
     ordinary_h:numberRecord(ordinaryH),ordinary_h_not_reconstructed_from_neighboring_grid_values:true};
    equal(current,originalProfileSchedules[index],'original profile/cusp schedule');
   },
   beforeStep(p,n,count,grid,x,h,state,_unusedTangent){
    if(active||seenSteps!==0||p!==selected||n!==schedule.grid_index)
     throw Error('Evaluate only the requested saved original step');
    const profileIndex=profiles.indexOf(p);
    active={global_step:schedule.global_step,profile_index:profileIndex,grid_index:n,
     grid_branch:grid?'integrationGrid':'ordinary',profile_step_count:count,x,h,field_calls:0,
     final_original_step:profileIndex===profiles.length-1&&n===count-1};
    equal(numberRecord(x),schedule.x,'original x bits');
    equal(numberRecord(h),schedule.h,'original h bits');
    equal(active.grid_branch,schedule.grid_branch,'original ordinary/cusp branch');
    equal(active.final_original_step,schedule.final_original_step,'original exit location');
    observer.beforeStep?.({...active,state});
   },
   beforeField(state,p,x){
    if(!active||p!==selected||active.field_calls>=4)
     throw Error('Keep the original four-field sequence');
    observer.beforeField?.({...active,field_index:active.field_calls,x,state});
   },
   afterField(state,p,x,f,cumulative){
    if(!active||p!==selected||active.field_calls>=4||
       f.jacobian.length!==size*K||f.derivative.length!==size)
     throw Error('Retain every original local-A row/column and state derivative');
    observer.afterField?.({...active,field_index:active.field_calls,x,state,
     derivative:f.derivative,jacobian:f.jacobian,root:f.root,cumulative});
    active.field_calls++;fields++;
   },
   afterStep(p,n,count,grid,x,h,state,_unusedTangent,cumulative){
    if(!active||p!==selected||n!==schedule.grid_index||active.field_calls!==4)
     throw Error('Complete exactly one original four-field state step');
    const final=active.final_original_step;
    const out=final?Float64Array.from(state.slice(0,K),(v,j)=>j<112?v:v/cell.portRatio):state.slice(0,K);
    observer.afterStep?.({...active,state,out,cumulative,
     port_applied:final,port_ratio:final?cell.portRatio:1});
    seenSteps++;active=null;
   }});
  if(seenProfiles!==profiles.length||seenSteps!==1||fields!==4||active!==null)
   throw Error('Every requested original profile/step/field must be accounted for');
  return {state:result.state,selected_steps:seenSteps,returned_local_J:fields,
   complete_mean_state_preserved:true,old_binary64_tangent_not_formed:true,
   additional_ODE_steps:0};
 }
 return {identity,run};
}
