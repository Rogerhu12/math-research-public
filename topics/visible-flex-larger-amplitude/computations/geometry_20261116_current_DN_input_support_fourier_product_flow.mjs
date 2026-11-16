// R602: original Fourier-product local Jacobian and original717ac RK/grid.
// Only its complete A*T uses the published R523 actual-input support helper.
// Original root/rows/six moments/one Cholesky/all224 right sides already share;
// they are not new optimizations here. This module supplies a real factory,
// not a replacement finite-root-trace algorithm or a scientific acceptance gate.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {completeInputSupportLinear,newInputSupportLinearStatistics}
 from './geometry_20261116_finite_trace_actual_input_support_linear.mjs';

export const CURRENT_DN_INPUT_SUPPORT_SCHEMA=
 'R602-original-Fourier-product-current-DN-actual-input-support-v1';
const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC,
 sourceRoot=process.env.VISIBLE_FLEX_SOURCE_ROOT;
if(!topic||!sourceRoot)throw Error('Actual original public source topic/root required');

const hash=raw=>crypto.createHash('sha256').update(raw).digest('hex');
function bindSource(file,expected){
 const raw=fs.readFileSync(file),actual={file:path.resolve(file),
  bytes:raw.length,sha256:hash(raw)};
 if(expected&&(actual.bytes!==expected.bytes||actual.sha256!==expected.sha256))
  throw Error('Declared original/source implementation changed: '+file);
 return actual;
}
const helperPath=fileURLToPath(new URL(
 './geometry_20261116_finite_trace_actual_input_support_linear.mjs',import.meta.url));
const factoryPath=path.resolve(topic,'scripts/78718-tail-fourier-root-split-engine.mjs'),
 flowPath=path.resolve(topic,'scripts/78718-tail-fourier-product-flow.mjs'),
 jacobianPath=path.resolve(topic,'scripts/78718-tail-fourier-product-jacobian.mjs'),
 gridPath=path.resolve(sourceRoot,'topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs');
const sourceBinding={
 schema:CURRENT_DN_INPUT_SUPPORT_SCHEMA+'-actual-source-binding',
 current_source:bindSource(fileURLToPath(import.meta.url)),
 helper:bindSource(helperPath,{bytes:6246,
  sha256:'e16be66d2a7ab528a31cb643702864c6fae493bbfc3059f6c18419d9dec485f3'}),
 original_factory:bindSource(factoryPath,{bytes:2045,
  sha256:'a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372'}),
 original_flow_ancestor:bindSource(flowPath,{bytes:2400,
  sha256:'717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f'}),
 original_local_J:bindSource(jacobianPath,{bytes:3948,
  sha256:'205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25'}),
 original_integration_grid:bindSource(gridPath,{bytes:1805,
  sha256:'b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f'}),
 source_files_modified:false,
 local_J_is_original_Fourier_product_moments_not_finite_root_trace:true,
 original_primal_root_RHS_and_Cholesky_sharing_already_present:true,
 original_717ac_integrationGrid_and_RK_expressions_retained:true,
 full_size_by_K_output_and_both_mean_rows_retained:true,
 helper_support_rebuilt_from_current_T_per_field:true,
 original_nonfinite_input_complete_loop_retained:true,
 nonlinear_or_output_finiteness_gate_added:false,
 resource_frontier_and_whole_run_word_equality_claimed:false,
 numerical_run_or_speedup_prepaid:false
};
const {createFourierRootSplitFluxEngine:originalFactory}=
 await import(pathToFileURL(factoryPath));
const {integrationGrid}=await import(pathToFileURL(gridPath));

// Same signature as the original worker factory. OriginalFactory constructs
// exactly its original root/split/RHS/local-J objects, tables and cusp wrapper.
// Its original withJ closure is replaced; rhsWithJacobian itself is not rebuilt.
// Each actual engine gets one separate statistics object; original statistics
// and all existing function references except flowStateWithJacobian survive.
export function createFourierRootSplitFluxEngine(options={}){
 const base=originalFactory(options),{M,size,rhsWithJacobian}=base,Kdim=2*M,
  linearStatistics=newInputSupportLinearStatistics();
 function flowStateWithJacobian(initial,segments,opts={}){
  const steps=opts.stepsPerSegment??64;
  let state=Float64Array.from(initial),tangent=new Float64Array(size*Kdim),minA=Infinity,minD=Infinity,maxRootRelative=0;
  for(let j=0;j<Kdim;j++)tangent[j*Kdim+j]=1;
  function field(s,t,p,x){
   const f=rhsWithJacobian(s,p,x);
   minA=Math.min(minA,f.root.e.minA);minD=Math.min(minD,f.root.e.minD);maxRootRelative=Math.max(maxRootRelative,f.root.err/f.root.scale);
   const dt=completeInputSupportLinear(f.jacobian,t,size,Kdim,linearStatistics);
   return {ds:f.derivative,dt};
  }
  function increment(s,t,f,h){return {s:Float64Array.from(s,(v,j)=>v+h*f.ds[j]),t:Float64Array.from(t,(v,j)=>v+h*f.dt[j])};}
  for(const p of segments){
   const cuts=p.integrationBreakpoints??[],grid=cuts.length?integrationGrid(steps,cuts):null,count=grid?grid.length-1:steps,ordinaryH=1/steps;
   for(let n=0;n<count;n++){
    const h=grid?grid[n+1]-grid[n]:ordinaryH,x=grid?grid[n]:n*ordinaryH,
     a=field(state,tangent,p,x),ab=increment(state,tangent,a,h/2),b=field(ab.s,ab.t,p,x+h/2),
     bc=increment(state,tangent,b,h/2),c=field(bc.s,bc.t,p,x+h/2),cd=increment(state,tangent,c,h),d=field(cd.s,cd.t,p,x+h);
    for(let j=0;j<size;j++)state[j]+=h*(a.ds[j]+2*b.ds[j]+2*c.ds[j]+d.ds[j])/6;
    for(let j=0;j<tangent.length;j++)tangent[j]+=h*(a.dt[j]+2*b.dt[j]+2*c.dt[j]+d.dt[j])/6;
   }
  }
  return {state,tangent,shapeDimension:Kdim,minA,minD,maxRootRelative};
 }
 return {...base,flowStateWithJacobian,
  linearEvaluation:CURRENT_DN_INPUT_SUPPORT_SCHEMA,
  linearInputSupportStatistics:linearStatistics,
  linearInputSupportSourceBinding:sourceBinding};
}
