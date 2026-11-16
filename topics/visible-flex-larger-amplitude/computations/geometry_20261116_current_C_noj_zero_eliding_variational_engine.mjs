// R494: current-C captured-product Jacobian with R474 finite-input linear zero elision.
// Author: amplitude agent (AI), 2026-11-16. This independent caller does not
// replace the product Jacobian by a finite-root-trace derivative. The original
// root, split RHS, captured product formulas, RK and cusp schedule remain below.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {completeZeroElidingLinear,newZeroCoefficientLinearStatistics} from './geometry_20261116_finite_trace_zero_coefficient_linear.mjs';

export const CURRENT_C_ZERO_ELIDING_SCHEMA='R494-current-C-noJ-captured-product-zero-eliding-linear-v1';

const originalGeometryKeys=['r','drdx','w','w2','E'];
const originalRowKeys=['P','Pt','L','K','U','S','D','A','sd','quad'];

function copiedOriginalRoot(rt){
 const g={};for(const key of originalGeometryKeys)g[key]=rt.g[key];
 const rows=rt.e.rows.map(row=>{
  const value={};for(const key of originalRowKeys)value[key]=row[key];return value;
 });
 return {g,L:Float64Array.from(rt.L),err:rt.err,scale:rt.scale,
  e:{B:Float64Array.from(rt.e.B),rows,minA:rt.e.minA,minD:rt.e.minD}};
}

// The partial derivatives are the unmodified original product-moment
// formula at the *captured* root. This avoids a second numerical root/RHS
// call and prevents a later profile/cache access from changing that root.
export function createNoJMatchedZeroElidingVariationalEngine(options,base,dependencies){
 const {createFourierProductJacobianEngine,splitIntegrationInterval}=dependencies,
  {M,N,size}=base,Kdim=2*M,
  rootValue=base.root,stateRhs=base.rhs,originalRk4=base.rk4;
 const linearStatistics=dependencies.zeroCoefficientLinearStatistics??newZeroCoefficientLinearStatistics();
 if(M!==options.modes||N!==options.quadrature||size!==2*M+2||
    typeof rootValue!=='function'||typeof stateRhs!=='function'||typeof originalRk4!=='function'||
    typeof createFourierProductJacobianEngine!=='function'||typeof splitIntegrationInterval!=='function')
  throw Error('Bind the actual original Fourier-root split backend and its two original dependencies');
 let activeCapture=null;
 const feed={...base,
  root(state,profile,x){
   const a=activeCapture;
   if(!a||state!==a.state||profile!==a.profile||!Object.is(x,a.x))
    throw Error('The original local Jacobian must consume exactly the captured original field');
   a.rootFeedCalls++;return a.root;
  },
  rhs(state,profile,x,detail=false,knownRoot=null){
   const a=activeCapture;
   if(!a||state!==a.state||profile!==a.profile||!Object.is(x,a.x)||detail!==false||knownRoot!==a.root)
    throw Error('The local Jacobian may only read the stored derivative and root');
   a.rhsFeedCalls++;return a.derivative;
  }};
 const {rhsWithJacobian:capturedLocalJacobian}=createFourierProductJacobianEngine(options,feed);

 function flowStateWithJacobian(initial,segments,opts={}){
  // Original core.cellFlow supplies exactly one fresh Float64Array(size)
  // per stage, including both complete mean-state entries.
  if(!(initial instanceof Float64Array)||initial.length!==size)
   throw Error('Use the complete original typed stage state');
  const steps=opts.stepsPerSegment??64;
  if(!Number.isInteger(steps)||steps<=0)throw Error('The original positive integer step count is required');
  let state=initial,tangent=new Float64Array(size*Kdim),
   minA=Infinity,minD=Infinity,maxRootRelative=0,
   originalRootCalls=0,originalRhsCalls=0,capturedJacobianCalls=0;
  const schedule=[];
  for(let j=0;j<Kdim;j++)tangent[j*Kdim+j]=1;

  function field(s,p,x){
   // These are the same two calls inside original no-J rhs: root first,
   // then the same split RHS with that known root, detail=false.
   const rt=rootValue(s,p,x);originalRootCalls++;
   const ds=stateRhs(s,p,x,false,rt);originalRhsCalls++;
   // Copy only after both original calls, before no-J reuses its t buffer.
   const capture={state:Float64Array.from(s),profile:p,x,
    root:copiedOriginalRoot(rt),derivative:Float64Array.from(ds),
    rootFeedCalls:0,rhsFeedCalls:0};
   minA=Math.min(minA,rt.e.minA);minD=Math.min(minD,rt.e.minD);
   maxRootRelative=Math.max(maxRootRelative,rt.err/rt.scale);
   return {ds,capture};
  }

  function fromCaptured(capture){
   if(activeCapture!==null)throw Error('No overlapping local-J capture scopes');
   activeCapture=capture;
   try{
    const f=capturedLocalJacobian(capture.state,capture.profile,capture.x);
    if(f.derivative!==capture.derivative||f.root!==capture.root||capture.rootFeedCalls!==1||capture.rhsFeedCalls!==1)
     throw Error('Original local-J source no longer has its single known-root/value read');
    capturedJacobianCalls++;return f.jacobian;
   }finally{activeCapture=null;}
  }

  function linear(A,T){
   return completeZeroElidingLinear(A,T,size,Kdim,linearStatistics);
  }

  function oneOriginalStep(p,x,h,position){
   const entered=state,enteredTangent=tangent;
   // Preserve every original no-J state expression and its reusable t
   // buffer. In particular h*a/2 is NOT rewritten as (h/2)*a.
   const a=field(state,p,x),t=new Float64Array(size);
   for(let j=0;j<size;j++)t[j]=state[j]+h*a.ds[j]/2;
   const b=field(t,p,x+h/2);for(let j=0;j<size;j++)t[j]=state[j]+h*b.ds[j]/2;
   const c=field(t,p,x+h/2);for(let j=0;j<size;j++)t[j]=state[j]+h*c.ds[j];
   const d=field(t,p,x+h);
   const nextState=Float64Array.from(state,(v,j)=>v+h*(a.ds[j]+2*b.ds[j]+2*c.ds[j]+d.ds[j])/6);
   // Complete the original primal before applying any of its four local
   // Jacobians. No original root/RHS/profile call occurs in this phase.
   const Aa=fromCaptured(a.capture),Ab=fromCaptured(b.capture),
    Ac=fromCaptured(c.capture),Ad=fromCaptured(d.capture),
    ta=linear(Aa,tangent),tbState=Float64Array.from(tangent,(v,j)=>v+h*ta[j]/2),
    tb=linear(Ab,tbState),tcState=Float64Array.from(tangent,(v,j)=>v+h*tb[j]/2),
    tc=linear(Ac,tcState),tdState=Float64Array.from(tangent,(v,j)=>v+h*tc[j]),
    td=linear(Ad,tdState),
    nextTangent=Float64Array.from(tangent,(v,j)=>v+h*(ta[j]+2*tb[j]+2*tc[j]+td[j])/6);
   state=nextState;tangent=nextTangent;
   const record={...position,x,h,field_x:[x,x+h/2,x+h/2,x+h]};
   schedule.push(record);
   if(typeof opts.onStep==='function'){
    // No returned observer object aliases numerical state, tangent,
    // original profile or any root/RHS cache. An observer may serialize
    // these copies but cannot change later primal/covariant arithmetic.
    opts.onStep({...record,input_state:Float64Array.from(entered),output_state:Float64Array.from(state),
     input_tangent:Float64Array.from(enteredTangent),output_tangent:Float64Array.from(tangent),
     fields:[a,b,c,d].map((f,i)=>({index:i,x:f.capture.x,
      state:Float64Array.from(f.capture.state),derivative:Float64Array.from(f.capture.derivative),
      geometry:{...f.capture.root.g},err:f.capture.root.err,scale:f.capture.root.scale,
      minA:f.capture.root.e.minA,minD:f.capture.root.e.minD,
      local_jacobian:Float64Array.from([Aa,Ab,Ac,Ad][i])}))});
   }
  }

  for(let profileIndex=0;profileIndex<segments.length;profileIndex++){
   const p=segments[profileIndex];
   for(let k=0;k<steps;k++){
    // Match core.cellFlow's exact ordinary arguments. Do not replace
    // division by reciprocal multiplication or build a global grid.
    const x=k/steps,h=1/steps;
    if(options.cuspAwareFlow===true){
     const grid=splitIntegrationInterval(x,x+h,p.integrationBreakpoints);
     if(grid.length===2){
      // Same original branch: retain h, rather than recomputing b-a.
      oneOriginalStep(p,x,h,{profile_index:profileIndex,ordinary_index:k,sub_index:0,
       branch:'original-local-cusp-wrapper-unsplit',original_ordinary_x:x,original_ordinary_h:h});
     }else{
      // Keep duplicates, endpoint comparisons, sort/reversal, and the
      // original per-interval endpoint rounding from the imported helper.
      for(let j=0;j<grid.length-1;j++)oneOriginalStep(p,grid[j],grid[j+1]-grid[j],{
       profile_index:profileIndex,ordinary_index:k,sub_index:j,
       branch:'original-local-cusp-wrapper-split',original_ordinary_x:x,original_ordinary_h:h});
     }
    }else{
     oneOriginalStep(p,x,h,{profile_index:profileIndex,ordinary_index:k,sub_index:0,
      branch:'original-cusp-disabled',original_ordinary_x:x,original_ordinary_h:h});
    }
   }
  }
  return {state,tangent,shapeDimension:Kdim,minA,minD,maxRootRelative,
   implementation:'R494-original-noJ-captured-product-zero-eliding-linear-v1',schedule,
   originalRootCalls,originalRhsCalls,capturedJacobianCalls,
   root_or_RHS_reexecuted_during_tangent_phase:false,
   two_mean_state_entries_preserved:true,primal_modified_by_tangent:false};
 }
 return {...base,flowStateWithJacobian,
  variationalEvaluation:'R494-original-noJ-captured-product-zero-eliding-linear-v1',
  zeroCoefficientLinearStatistics:linearStatistics,
  capturedOriginalProductJacobianUnchanged:true,
  finiteRootTraceDerivativeInstalled:false,
  originalNoJRk4Reference:originalRk4,
  noJRk4FunctionUnchanged:true,originalRhsFunctionUnchanged:true,
  originalRootFunctionUnchanged:true};
}

const BASELINE_NOJ='f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9';
const BASELINE_PRODUCT='205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25';
const HELPER_NAME='geometry_20261116_finite_trace_zero_coefficient_linear.mjs';
const HELPER_SHA='eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02';
const CALLER_NAME='geometry_20261116_current_C_noj_zero_eliding_variational_engine.mjs';
const copyMetadata=value=>JSON.parse(JSON.stringify(value));
function sourceReceipt(file){
 const b=fs.readFileSync(file);
 return {file:path.basename(file),bytes:b.length,sha256:crypto.createHash('sha256').update(b).digest('hex')};
}

// Call only after the original owner has loaded and verified its full original
// runtime. Both fae2's 112 owner and fb951's general-M owner use the same factory
// signature. This API is the actual substitution point; it does not register
// a worker/client/checkpoint tuple or mutate the supplied original runtime.
export function bindCurrentCNoJZeroElidingRuntime(originalRuntime,sourceSha256){
 if(process.env.GITHUB_ACTIONS!=='true'||process.env.GITHUB_REPOSITORY!=='Rogerhu12/math-research-public')
  throw Error('Current-C scientific execution belongs to the named public Actions');
 if(!originalRuntime||typeof originalRuntime.createNoJMatchedVariationalEngine!=='function'||
    typeof originalRuntime.createFourierProductJacobianEngine!=='function'||
    originalRuntime.receipts?.noJ?.sha256!==BASELINE_NOJ||
    originalRuntime.receipts?.product?.sha256!==BASELINE_PRODUCT)
  throw Error('Bind the complete original captured-product runtime, not a finite-root-trace runtime');
 const callerPath=fileURLToPath(import.meta.url),directory=path.dirname(callerPath),
  caller=sourceReceipt(callerPath),helper=sourceReceipt(path.join(directory,HELPER_NAME));
 if(caller.file!==CALLER_NAME||sourceSha256?.[CALLER_NAME]!==caller.sha256||
    helper.sha256!==HELPER_SHA||sourceSha256?.[HELPER_NAME]!==helper.sha256)
  throw Error('Actual R494 caller and unchanged R474 helper source identities differ');
 const originalNoJ=copyMetadata(originalRuntime.receipts.noJ),
  statistics=newZeroCoefficientLinearStatistics();
 let enginesStarted=0,enginesConstructed=0;
 const actualNoJ={...caller,
  original_loaded_noJ_source:originalNoJ,
  original_loaded_factory_replaced_by_explicit_caller:true,
  unchanged_R474_linear_helper:helper,
  original_product_source:copyMetadata(originalRuntime.receipts.product),
  finite_root_trace_derivative_installed:false};
 function factory(options,base,dependencies){
  enginesStarted++;
  const engine=createNoJMatchedZeroElidingVariationalEngine(options,base,
   {...dependencies,zeroCoefficientLinearStatistics:statistics});
  enginesConstructed++;return engine;
 }
 function readback(){
  return {schema:CURRENT_C_ZERO_ELIDING_SCHEMA+'-actual-statistics',
   actual_variational_source:copyMetadata(actualNoJ),
   engines_started:enginesStarted,engines_constructed:enginesConstructed,
   complete_linear_statistics:copyMetadata(statistics),
   statistics_scope:'cumulative actual linear calls across this runtime owner and all its engine-cache generations',
   counts_are_not_unique_fields_or_complete_J_or_a_timing_certificate:true,
   original_noJ_root_RHS_product_RK_and_cusp_arithmetic_unchanged:true,
   finite_output_words_and_nonfinite_classes_only_not_NaN_payload:true,
   finite_root_trace_derivative_installed:false,
   whole_run_identity_or_performance_claimed:false};
 }
 return {...originalRuntime,
  createNoJMatchedVariationalEngine:factory,
  receipts:{...originalRuntime.receipts,noJ:actualNoJ},
  currentCNoJZeroElisionReadback:readback,
  currentCNoJZeroElisionSchema:CURRENT_C_ZERO_ELIDING_SCHEMA};
}
