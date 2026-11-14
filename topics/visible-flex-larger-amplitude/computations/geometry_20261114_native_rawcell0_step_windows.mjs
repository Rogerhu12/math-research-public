// Original withJac RK state path, with an independent tangent origin at every
// original step. This changes the finite variational representation, not the
// state RHS, x/h schedule, profile, complete mean state, or original exit port.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

const FLOW_SHA='717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f';
const GRID_SHA='b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f';
const GRID_KEY='topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs';
const sha=value=>crypto.createHash('sha256').update(value).digest('hex');

function actionsOnly(){
 if(process.env.GITHUB_ACTIONS!=='true'||
    (process.env.GITHUB_REPOSITORY??'').toLowerCase()!=='rogerhu12/math-research-public')
  throw Error('Original native per-step calculations belong only to public repository Actions');
}
export function numberRecord(value){
 const raw=Buffer.allocUnsafe(8);raw.writeDoubleLE(value);
 return {value:Number.isFinite(value)?value:null,float64le_hex:raw.toString('hex'),
  classification:Number.isNaN(value)?'NaN':value===Infinity?'positive-infinity':
   value===-Infinity?'negative-infinity':Object.is(value,-0)?'negative-zero':'finite'};
}

/** Import the same immutable source URL as the original Fourier-product flow.
 * The caller has already verified the complete live constructor/source chain. */
export async function loadOriginalIntegrationGrid({sourceRoot,originalSourceSHA256}){
 actionsOnly();
 if(!sourceRoot||originalSourceSHA256?.[GRID_KEY]!==GRID_SHA)
  throw Error('Original consumed integrationGrid identity is required');
 const file=path.join(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs');
 if(sha(fs.readFileSync(file))!==GRID_SHA)throw Error('Original integrationGrid source bytes changed');
 const imported=await import(pathToFileURL(file).href);
 if(typeof imported.integrationGrid!=='function')throw Error('Original integrationGrid export is missing');
 return {integrationGrid:imported.integrationGrid,identity:{
  source_key:GRID_KEY,source_sha256:GRID_SHA,
  function_sha256:sha(imported.integrationGrid.toString()),
  original_module_URL:pathToFileURL(file).href,
  source_matches_consumed_native_source:true,rewritten_grid:false}};
}

/** Pure, reversible source insertion. Original RK arithmetic remains literal.
 * The reset is deliberately a new local-J representation, not an assertion
 * that products of these rounded local matrices reproduce the old long J. */
export function preparePerStepFlowSource(original){
 if(sha(original)!==FLOW_SHA)throw Error('Original Fourier-product flow source bytes changed');
 const begin=' function flowStateWithJacobian(initial,segments,opts={}){';
 const end='\n return {...base,rhsWithJacobian,flowStateWithJacobian,variationalEvaluation:';
 if(original.split(begin).length!==2||original.split(end).length!==2)
  throw Error('Unique original variational function boundaries required');
 const start=original.indexOf(begin),stop=original.indexOf(end,start);
 if(stop<start)throw Error('Original function boundaries are out of order');
 const originalFunction=original.slice(start,stop).trim();
 const changes=[
  {before:'  function field(s,t,p,x){\n',
   after:'  function field(s,t,p,x){\n   opts.beforeField?.(s,p,x);\n'},
  {before:'   minA=Math.min(minA,f.root.e.minA);minD=Math.min(minD,f.root.e.minD);maxRootRelative=Math.max(maxRootRelative,f.root.err/f.root.scale);\n',
   after:'   minA=Math.min(minA,f.root.e.minA);minD=Math.min(minD,f.root.e.minD);maxRootRelative=Math.max(maxRootRelative,f.root.err/f.root.scale);\n   opts.afterField?.(s,p,x,f,{minA,minD,maxRootRelative});\n'},
  {before:'   const cuts=p.integrationBreakpoints??[],grid=cuts.length?integrationGrid(steps,cuts):null,count=grid?grid.length-1:steps,ordinaryH=1/steps;\n',
   after:'   const cuts=p.integrationBreakpoints??[],grid=cuts.length?integrationGrid(steps,cuts):null,count=grid?grid.length-1:steps,ordinaryH=1/steps;\n   opts.profileSchedule?.(p,cuts,grid,count,ordinaryH);\n'},
  {before:'    const h=grid?grid[n+1]-grid[n]:ordinaryH,x=grid?grid[n]:n*ordinaryH,\n     a=field',
   after:'    tangent.fill(0);for(let j=0;j<Kdim;j++)tangent[j*Kdim+j]=1;\n    const h=grid?grid[n+1]-grid[n]:ordinaryH,x=grid?grid[n]:n*ordinaryH;\n    opts.beforeStep?.(p,n,count,grid,x,h,state,tangent);\n    const a=field'},
  {before:'    for(let j=0;j<tangent.length;j++)tangent[j]+=h*(a.dt[j]+2*b.dt[j]+2*c.dt[j]+d.dt[j])/6;\n',
   after:'    for(let j=0;j<tangent.length;j++)tangent[j]+=h*(a.dt[j]+2*b.dt[j]+2*c.dt[j]+d.dt[j])/6;\n    opts.afterStep?.(p,n,count,grid,x,h,state,tangent,{minA,minD,maxRootRelative});\n'}
 ];
 let transformed=originalFunction;
 for(const change of changes){
  if(transformed.split(change.before).length!==2)throw Error('Unique original per-step insertion anchor required');
  transformed=transformed.replace(change.before,change.after);
 }
 let restored=transformed;
 for(const change of [...changes].reverse()){
  if(restored.split(change.after).length!==2)throw Error('Unique local-J source change required');
  restored=restored.replace(change.after,change.before);
 }
 if(restored!==originalFunction)throw Error('Per-step access changed the original numerical body');
 return {source:transformed,identity:{
  schema:'original-native-RK-per-step-source-v1',original_flow_module_sha256:FLOW_SHA,
  original_function_sha256:sha(originalFunction),per_step_function_sha256:sha(transformed),
  changes_sha256:sha(JSON.stringify(changes)),changes,exact_source_roundtrip_verified:true,
  original_state_RHS_RK_increment_and_state_update_expressions_retained:true,
  original_tangent_RK_expressions_retained_between_identity_resets:true,
  original_profile_loop_and_integrationGrid_branch_retained:true,
  tangent_identity_reset_before_every_original_step:true,
  readonly_observers_added:true,additional_ODE_steps:0,
  no_product_of_local_J_claimed_equal_to_original_long_J:true}};
}

/** Full226 state continues unchanged through all original profiles/steps.
 * Observers synchronously persist each completed local block before the next
 * tangent reset. They must not mutate any supplied live array or profile. */
export function createNativeRawCell0StepWindows({engine,cell,sourceTopic,stageIndex,
                                                originalGrid,steps=12}){
 actionsOnly();
 if(steps!==12||!Number.isInteger(stageIndex)||stageIndex<0||stageIndex>=72||
    cell.rawCell!==0||engine!==cell.engine||engine.M!==112||engine.size!==226||
    typeof engine.rhsWithJacobian!=='function'||!Array.isArray(cell.profiles)||
    cell.profiles.length===0||typeof originalGrid?.integrationGrid!=='function'||
    originalGrid.identity?.source_sha256!==GRID_SHA)
  throw Error('Use the unchanged original rawCell0 complete112-mode RK12 engine');
 if(!(Number.isFinite(cell.portRatio)&&cell.portRatio!==0))
  throw Error('Finite original nonzero stage port required');
 const file=path.join(sourceTopic,'scripts/78718-tail-fourier-product-flow.mjs');
 const prepared=preparePerStepFlowSource(fs.readFileSync(file,'utf8'));
 const rawFlow=new Function('rhsWithJacobian','size','Kdim','integrationGrid',
  'return ('+prepared.source+');')(engine.rhsWithJacobian,engine.size,2*engine.M,
   originalGrid.integrationGrid);
 const M=engine.M,K=2*M,profiles=cell.profiles;
 const identity={schema:'original-native-rawcell0-step-window-v1',source:prepared.identity,
  integration_grid:originalGrid.identity,stage:stageIndex,rawCell:cell.rawCell,
  rawSegment:cell.rawSegment,part:cell.part,parts:cell.parts,
  rawLeft:numberRecord(cell.rawLeft),rawRight:numberRecord(cell.rawRight),mu:numberRecord(cell.mu),
  original_port_ratio:numberRecord(cell.portRatio),steps,profiles:profiles.length,
  profile_function_sha256:profiles.map(p=>sha(p.toString())),
  profile_hashes_do_not_replace_complete_closure_source_binding:true,
  original_rhs_with_J_function_sha256:sha(engine.rhsWithJacobian.toString()),
  original_flow_function_object_sha256:sha(engine.flowStateWithJacobian.toString()),
  input_shape_dimension:K,full_state_dimension:engine.size,
  ordinary_schedule:'x=n*(1/12), h=1/12 in original pinned body',
  cusp_schedule:'original integrationGrid(12,cuts); original x=grid[n], h=grid[n+1]-grid[n]',
  separate_original_no_J_schedule_not_evaluated_or_equated:true,
  no_profile_reparameterization:true,no_mean_state_reset_between_steps:true,
  original_port_division_only_at_original_exit:true,additional_ODE_steps:0,
  no_changes_to_original_graphs_gains_far_sigma_or_acceptance:true};

 function run(initial,observers={}){
  actionsOnly();
  if(!(initial instanceof Float64Array)||initial.length!==engine.size)
   throw Error('Keep the complete original226-entry state');
  let completedSteps=0,active=null,profileIndex=-1,profileCount=0;
  function locate(p){const index=profiles.indexOf(p);
   if(index<0)throw Error('Do not substitute an original profile object');return index;}
  const result=rawFlow(initial,profiles,{stepsPerSegment:steps,
   profileSchedule(p,cuts,grid,count,ordinaryH){
    profileIndex=locate(p);
    if(profileIndex!==profileCount++)throw Error('Keep the original profile order');
    observers.profileSchedule?.({profile_index:profileIndex,cuts,grid,count,ordinaryH});
   },
   beforeStep(p,n,count,grid,x,h,state,tangent){
    const index=locate(p);
    if(index!==profileIndex)throw Error('Original profile/step order changed');
    active={global_step:completedSteps,profile_index:index,grid_index:n,
     grid_branch:grid?'integrationGrid':'ordinary',profile_step_count:count,x,h,
     final_original_step:index===profiles.length-1&&n===count-1,field_calls:0};
    observers.beforeStep?.({...active,state,tangent});
   },
   beforeField(state,p,x){
    if(!active||locate(p)!==active.profile_index)throw Error('Original field is outside its recorded step');
    observers.beforeField?.({...active,field_index:active.field_calls,x,state});
   },
   afterField(state,p,x,f,cumulative){
    if(!active||locate(p)!==active.profile_index||active.field_calls>=4)
     throw Error('Original RK field-call order changed');
    observers.afterField?.({...active,field_index:active.field_calls,x,state,
     root:f.root,cumulative});
    active.field_calls++;
   },
   afterStep(p,n,count,grid,x,h,state,tangent,cumulative){
    if(!active||active.field_calls!==4||locate(p)!==active.profile_index||
       n!==active.grid_index)throw Error('Keep exactly four original fields per completed RK step');
    const final=active.final_original_step;
    // These final-row port expressions are the original cellFlow expressions.
    const out=final?Float64Array.from(state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio):state.slice(0,K);
    let J;
    if(final){
     J=new Float64Array(K*K);
     for(let i=0;i<K;i++)for(let j=0;j<K;j++)J[i*K+j]=tangent[i*K+j]/(i<M?1:cell.portRatio);
    }else J=tangent.slice(0,K*K);
    observers.afterStep?.({...active,state,tangent,out,J,
     mean_tangent_rows:tangent.slice(K*K),cumulative,
     port_applied:final,port_ratio:final?cell.portRatio:1});
    completedSteps++;active=null;
   }});
  if(profileCount!==profiles.length||active!==null)
   throw Error('Every original profile and started RK step must complete');
  return {...result,step_count:completedSteps,meanHeight:result.state[K]+result.state[K+1],
   out:Float64Array.from(result.state.slice(0,K),(v,j)=>j<M?v:v/cell.portRatio),
   original_port_applied_once:true,no_J_product_formed:true};
 }
 return {identity,run};
}
