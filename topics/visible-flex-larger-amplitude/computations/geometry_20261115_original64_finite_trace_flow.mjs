// Matched actual original64 noJ primal with a numerical finite-root-trace tangent.
// No implicit product-moment Jacobian is called by this new variational path.
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {completeFiniteRootTraceJacobian,newFiniteTraceStatistics} from './geometry_20261115_original64_finite_trace_variation.mjs';
const sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!sourceRoot)throw Error('The original public source root is required');
const {splitIntegrationInterval}=await import(pathToFileURL(path.join(sourceRoot,
 'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs')));

const originalGeometryKeys=['r','drdx','w','w2','E'];
const originalRowKeys=['P','Pt','L','K','U','S','D','A','sd','quad'];

function copiedOriginalRoot(rt){
 const g={};for(const key of originalGeometryKeys)g[key]=rt.g[key];
 const rows=rt.e.rows.map(row=>{
  const value={};for(const key of originalRowKeys)value[key]=row[key];return value;
 });
 return {g,L:Float64Array.from(rt.L),err:rt.err,scale:rt.scale,finiteTrace:rt.finiteTrace,
  e:{B:Float64Array.from(rt.e.B),rows,minA:rt.e.minA,minD:rt.e.minD,minS:rt.e.minS}};
}

// Original noJ root/RHS calls finish before this tangent consumes their tape.
// The existing f9b RK and cusp schedule below remains the arithmetic baseline.
export function createOriginal64FiniteTraceVariationalEngine(options,base){
 const {M,N,size}=base,Kdim=2*M,
  rootValue=base.root,stateRhs=base.rhs,originalRk4=base.rk4,tables=base.finiteTraceTables,
  statistics=newFiniteTraceStatistics();
 if(M!==options.modes||N!==options.quadrature||size!==2*M+2||
    typeof rootValue!=='function'||typeof stateRhs!=='function'||typeof originalRk4!=='function'||
    base.finiteRootTraceSchema!=='original64-root-primal-tape-v1'||!tables)
  throw Error('Bind the actual original Fourier-root tape and literal tables');
 function noteFailure(error){
  statistics.incomplete_field_evaluations=(statistics.incomplete_field_evaluations??0)+1;
  statistics.last_failure={message:String(error),resource_budget:
   error?.finiteTraceVariation?.resource_budget===true,
   root_trace_available:!!error?.finiteRootTrace,
   original_return_reason:error?.finiteRootTrace?.return_reason??null,
   original_completed_updates:error?.finiteRootTrace?.accepted_updates?.length??null};
 }
 function rhsWithJacobian(state,profile,x){
  try{
   const rt=rootValue(state,profile,x,undefined,true),
    derivative=stateRhs(state,profile,x,false,rt),
    jacobian=completeFiniteRootTraceJacobian(rt,state,options,tables,statistics);
   return {root:rt,derivative,jacobian,
    scope:'complete local fixed finite-root trace numerical variation'};
  }catch(error){noteFailure(error);throw error;}
 }
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
   const rt=rootValue(s,p,x,undefined,true);originalRootCalls++;
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
   // No root, RHS or profile is re-executed here.
   const jacobian=completeFiniteRootTraceJacobian(capture.root,capture.state,options,tables,statistics);
   capturedJacobianCalls++;return jacobian;
  }

  function linear(A,T){
   const dt=new Float64Array(size*Kdim);
   // The two mean rows are retained; only the original K shape columns
   // enter this multiplication, so mean tangents never feed shape.
   for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
    const z=A[i*Kdim+j];for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*T[j*Kdim+k];
   }
   return dt;
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
   implementation:'original64-noJ-primal-finite-root-loop-variation-v1',schedule,
   originalRootCalls,originalRhsCalls,capturedJacobianCalls,
   root_or_RHS_reexecuted_during_tangent_phase:false,
   two_mean_state_entries_preserved:true,primal_modified_by_tangent:false};
 }
 const completeFlow=(...args)=>{
  try{return flowStateWithJacobian(...args);}catch(error){noteFailure(error);throw error;}
 };
 return {...base,rhsWithJacobian,flowStateWithJacobian:completeFlow,
  finiteTraceStatistics:statistics,
  finiteTraceVariationScope:'fixed successful real trace numerical linearisation; not IEEE roundmap derivative',
  variationalEvaluation:'original64-noJ-primal-finite-root-loop-variation-v1',
  originalNoJRk4Reference:originalRk4,
  noJRk4FunctionUnchanged:true,originalRhsFunctionUnchanged:true,
  originalRootPrimalArithmeticRecovered:true,originalRootFunctionUnchanged:false,
  originalRootObserverSourceExplicitlyBound:true};
}
