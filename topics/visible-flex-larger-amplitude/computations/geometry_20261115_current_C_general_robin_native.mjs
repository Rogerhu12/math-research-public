// Independent current-C native shooting owner; no old graphs or gains.
// Author: geometry agent (AI), 2026-11-15.
// Scientific calls are restricted to this repository's public Actions.
// Geometry production and the complete linear child are explicit dependencies.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {pathToFileURL} from 'node:url';

export const SCHEMA='current-C-full112-general-Robin-native-owner-v1';
export const MODEL='R286-original-stored-continuous-model-convention-C-v1';
const M=112,K=224,SIZE=226,DEPTH=576;
const hash=raw=>crypto.createHash('sha256').update(raw).digest('hex');
const finite=(v,label)=>{if(!Number.isFinite(v))throw Error('Nonfinite '+label);return v;};
const raw=view=>Buffer.from(view.buffer,view.byteOffset,view.byteLength);
const digest=view=>hash(raw(view));
function actions(){
 if(process.env.GITHUB_ACTIONS!=='true'||process.env.GITHUB_REPOSITORY!=='Rogerhu12/math-research-public')
  throw Error('Current-C scientific execution belongs to this public repository Actions');
}
function array(value,n,label){
 const out=Float64Array.from(value??[]);
 if(out.length!==n)throw Error('Complete '+label+' length differs');
 for(const v of out)finite(v,label);
 return out;
}
function positive(v,label){finite(v,label);if(!(v>0))throw Error('Positive '+label+' required');return v;}
function plain(value){return JSON.parse(JSON.stringify(value));}
function multiply(A,B,rows,inner,cols){
 const C=new Float64Array(rows*cols);
 for(let i=0;i<rows;i++)for(let j=0;j<inner;j++){
  const a=A[i*inner+j];for(let k=0;k<cols;k++)C[i*cols+k]+=a*B[j*cols+k];
 }
 return C;
}
function sameWords(a,b,label){
 if(a.length!==b.length||!raw(a).equals(raw(b)))throw Error('Actual byte identity differs: '+label);
}
export function constantReferenceScales(target,referenceFloor){
 actions();positive(referenceFloor,'declared reference floor');
 const t=array(target,M,'cut Q target');
 const scale=Math.max(referenceFloor,...t.map(Math.abs));
 return {values:new Float64Array(DEPTH+1).fill(scale),identity:{
  name:'current-C-constant-positive-reference-scale-v1',
  reference_floor:referenceFloor,scale,scales_sha256:digest(new Float64Array(DEPTH+1).fill(scale)),
  old_graphs_or_gains_used:false,
  original_old_metric_sigma_reused:false,
  original_old_weighted_norm_equivalence_claimed:false}};
}
export function physicalRobinToMomentum(column,r,w,mu,orientation=1){
 actions();positive(r,'radius');positive(w,'w');positive(mu,'mu');
 if(orientation!==1&&orientation!==-1)throw Error('Original radial orientation required');
 const u=array(column.u,M,'complete physical far height column');
 const k=array(column.k,M,'complete physical far derivative column');
 const matrix=new Float64Array(M*K),rowPowers=[];
 for(let j=0;j<M;j++){
  const m=2*(j+1);
  // (-k,u) applied to H=r^4 Q, H_r=m^2 r^3 Q+orientation sqrt(12)mu Pi/(r^4 w).
  let a=-k[j]*r**4+u[j]*m*m*r**3;
  let b=u[j]*orientation*Math.sqrt(12)*mu/(r**4*w);
  finite(a,'unscaled far Q coefficient');finite(b,'unscaled far Pi coefficient');
  const norm=Math.max(Math.abs(a),Math.abs(b));
  if(!(norm>0))throw Error('A complete far row is zero; no graph is fabricated');
  let exponent=Math.floor(Math.log2(norm));
  if(!Number.isSafeInteger(exponent)||exponent<-1074||exponent>1023)throw Error('Far row power outside finite range');
  // Exact-power normalization only; no division by a physical height coordinate.
  const factor=2**exponent;
  if(factor===0||!Number.isFinite(factor))throw Error('Far normalization power unavailable');
  const aa=a/factor,bb=b/factor;
  finite(aa,'normalized far Q coefficient');finite(bb,'normalized far Pi coefficient');
  if(!(Math.abs(aa)>0||Math.abs(bb)>0))throw Error('Both far coefficients were lost');
  matrix[j*K+j]=aa;matrix[j*K+M+j]=bb;rowPowers.push(exponent);
 }
 return {matrix,row_powers:rowPowers,
  rule:'complete (-k,u) physical row then disclosed binary64 coordinate map and exact-power row normalization',
  original_unscaled_column:{u_sha256:digest(u),k_sha256:digest(k)},
  divided_by_height:false,
  finite_normalized_row_is_not_an_exact_Robin_certificate:true};
}
export async function loadOriginalRuntime(sourceTopic,computationDirectory,expected){
 actions();
 const files={
  engine:path.join(sourceTopic,'scripts/78718-tail-fourier-root-split-engine.mjs'),
  product:path.join(sourceTopic,'scripts/78718-tail-fourier-product-jacobian.mjs'),
  root:path.join(sourceTopic,'scripts/78718-tail-fourier-root-momentum.mjs'),
  cusp:path.join(sourceTopic,'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs'),
  physicalJet:path.join(sourceTopic,'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_momentum_physical_jets.mjs'),
  metric:path.join(sourceTopic,'repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_actual_metric.mjs'),
  noJ:path.join(computationDirectory,'geometry_20261114_noj_matched_variational_engine.mjs')
 };
 const pinned={
  engine:'a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372',
  product:'205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25',
  root:'cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88',
  cusp:'b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f',
  physicalJet:expected.physicalJet,metric:expected.metric,noJ:expected.noJ
 };
 const receipts={};
 for(const [name,file] of Object.entries(files)){
  const b=fs.readFileSync(file),h=hash(b);
  if(!/^[0-9a-f]{64}$/.test(pinned[name]??'')||h!==pinned[name])throw Error('Pinned native dependency differs: '+name);
  receipts[name]={file,bytes:b.length,sha256:h};
 }
 // Existing pinned capacity loader must have been installed by the actual launcher.
 const engine=await import(pathToFileURL(files.engine));
 const product=await import(pathToFileURL(files.product));
 const cusp=await import(pathToFileURL(files.cusp));
 const jets=await import(pathToFileURL(files.physicalJet));
 const metric=await import(pathToFileURL(files.metric));
 const noJ=await import(pathToFileURL(files.noJ));
 return {...engine,...product,...cusp,...jets,...metric,...noJ,
  receipts,owner_source_sha256:hash(fs.readFileSync(new URL(import.meta.url)))};
}
export function createCurrentCNative(options){
 actions();
 const {runtime,geometry,linearChild}=options;
 if(!runtime||typeof runtime.createFourierRootSplitFluxEngine!=='function'||
    typeof runtime.createNoJMatchedVariationalEngine!=='function'||
    typeof runtime.createMomentumPhysicalJetEvaluator!=='function'||
    typeof runtime.actualMetricFromDarbouxJets!=='function'||typeof linearChild!=='function')
  throw Error('Actual pinned original runtime and current general-chain child required');
 if(geometry?.model_schema!==MODEL||geometry?.schema!=='current-C-native-radial-geometry-bundle-v1'||
    geometry.modes!==M||geometry.spacing!==2||geometry.stage_count!==DEPTH||
    geometry.native_old_graphs_or_gains_used!==false||
    !geometry.original_C_input_binding||!geometry.numeric_geometry_identity)
  throw Error('An explicit current-C geometry realization is required');
 if(!Array.isArray(geometry.cells)||geometry.cells.length!==DEPTH||
    !Array.isArray(geometry.rawNode)||geometry.rawNode.length!==9)
  throw Error('All 576 current stages and the nine actual physical boundaries are required');
 if(geometry.rawNode.some((x,i)=>x!==72*i))throw Error('Current 8 by 9 by 8 stage layout differs');
 const quadrature=options.quadrature,steps=options.steps,projectionFloor=options.projectionFloor;
 if(!Number.isSafeInteger(quadrature)||quadrature<=4*M*2||
    !Number.isSafeInteger(steps)||steps<=0||
    !(projectionFloor>0&&projectionFloor<1))
  throw Error('Actual original resolved quadrature, positive steps and branch floor required');
 const orientation=geometry.orientation;
 if(orientation!==1)throw Error('The current-C source has outward orientation +1');
 const farMatrix=array(geometry.far_matrix,M*K,'current complete general far matrix');
 for(let i=0;i<M;i++){
  let norm=0;for(let j=0;j<K;j++)norm=Math.max(norm,Math.abs(farMatrix[i*K+j]));
  if(!(norm>0))throw Error('Current complete far row '+i+' is zero');
 }
 // Each engine owns large deterministic angular tables. Keep only two complete
 // engines alive; construction has no evolving mathematical state. The original
 // root/RHS/RK methods and their arguments are unchanged on every actual use.
 const engineCache=new Map(),engineCacheCapacity=2;
 function engineFor(mu){
  const cacheKey=String(mu);
  if(engineCache.has(cacheKey)){
   const value=engineCache.get(cacheKey);engineCache.delete(cacheKey);engineCache.set(cacheKey,value);return value;
  }
  const args={modes:M,spacing:2,quadrature,mu,orientation,projectionFloor,cuspAwareFlow:false};
  const original=runtime.createFourierRootSplitFluxEngine(args);
  const engine=runtime.createNoJMatchedVariationalEngine(args,original,{
   createFourierProductJacobianEngine:runtime.createFourierProductJacobianEngine,
   splitIntegrationInterval:runtime.splitIntegrationInterval});
  engineCache.set(cacheKey,engine);
  while(engineCache.size>engineCacheCapacity)engineCache.delete(engineCache.keys().next().value);
  return engine;
 }
 const cells=geometry.cells.map((cell,n)=>{
  if(cell.stage!==n||cell.rawCell!==Math.floor(n/72)||!Array.isArray(cell.profiles)||
     cell.profiles.length!==1||typeof cell.profiles[0]!=='function')throw Error('Complete ordered current stage differs');
  const mu=positive(cell.mu,'current stage mu');
  positive(cell.portRatio,'current stage port ratio');
  return {...cell,get engine(){return engineFor(mu);}};
 });
 const cutProfile=cells[0].profiles[0],cutRadius=positive(cutProfile(1).r,'actual current cut radius');
 if(!Object.is(cutRadius,geometry.cut_radius))throw Error('Actual numerical cut and provider cut differ');
 const cutPort=positive(cells[0].portRatio,'actual cut port');
 const nodeR=array(geometry.node_radii,DEPTH+1,'complete node radii');
 if(!Object.is(nodeR[0],cutRadius))throw Error('Current node0 radius differs');
 const parameterRecord={modes:M,spacing:2,depth:DEPTH,physicalDepth:8,shootingParts:8,
  steps,quadrature,projectionFloor,orientation,cut_radius:cutRadius,engine_cache_capacity:engineCacheCapacity,
  method:'same-C-sampled-geometry-general-Robin-noJ-matched-full-chain',
  old_graphs_or_gains_used:false};
 const identity={schema:SCHEMA,source_sha256:hash(fs.readFileSync(new URL(import.meta.url))),
  original_runtime:plain(runtime.receipts),original_C_input_binding:plain(geometry.original_C_input_binding),
  numeric_geometry_identity:plain(geometry.numeric_geometry_identity),
  far_matrix_sha256:digest(farMatrix),far_identity:plain(geometry.far_identity),
  same_C_numerical_realization_is_not_an_exact_infinite_nonlinear_DN:true,
  parameter_record:parameterRecord};
 let call=0,lastCompleteSensitivity=null;
 function initial(){return Array.from({length:DEPTH+1},()=>new Float64Array(K));}
 function cellFlow(n,input,withJac){
  const c=cells[n],s=new Float64Array(SIZE);s.set(input);
  let f;
  if(withJac)f=c.engine.flowStateWithJacobian(s,c.profiles,{stepsPerSegment:steps});
  else{
   let state=s;
   for(const profile of c.profiles)for(let k=0;k<steps;k++)state=c.engine.rk4(state,profile,k/steps,1/steps);
   f={state};
  }
  const out=Float64Array.from(f.state.slice(0,K),(v,j)=>j<M?v:v/c.portRatio);
  let J=null,meanRows=null;
  if(withJac){
   J=new Float64Array(K*K);meanRows=new Float64Array(2*K);
   for(let i=0;i<K;i++)for(let j=0;j<K;j++)J[i*K+j]=f.tangent[i*K+j]/(i<M?1:c.portRatio);
   meanRows.set(f.tangent.slice(K*K,(K+2)*K));
  }
  return {out,J,meanRows,meanHeight:f.state[K]+f.state[K+1],
   completeMeanState:Float64Array.from(f.state.slice(K)),minA:withJac?f.minA:Infinity,minD:withJac?f.minD:Infinity};
 }
 function evaluate(states,target,withJac,scales){
  const flows=[],residuals=[];let norm=0,minA=Infinity,minD=Infinity;
  for(let n=0;n<DEPTH;n++){
   let f;
   try{f=cellFlow(n,states[n+1],withJac);}
   catch(error){if(error&&typeof error==='object')Object.assign(error,{
    tailStage:n,tailRawCell:cells[n].rawCell,tailRawSegment:cells[n].rawSegment});throw error;}
   const r=Float64Array.from(f.out,(v,j)=>v-states[n][j]);
   norm=Math.max(norm,...Array.from(r,v=>Math.abs(v)/scales[n]));flows.push(f);residuals.push(r);
   if(withJac){minA=Math.min(minA,f.minA);minD=Math.min(minD,f.minD);}
  }
  const end=new Float64Array(M),cut=new Float64Array(M);
  for(let i=0;i<M;i++){
   let v=0;for(let j=0;j<K;j++)v+=farMatrix[i*K+j]*states[DEPTH][j];
   end[i]=v;norm=Math.max(norm,Math.abs(v)/scales[DEPTH]);
   cut[i]=states[0][i]-target[i];norm=Math.max(norm,Math.abs(cut[i])/scales[0]);
  }
  return {flows,residuals,end,cut,norm,minA,minD};
 }
 function child(ev,states,target,scales,kind,iteration){
  // This callback must snapshot the actual current arrays and run the independent child.
  // No original matrix, state, weight, or boundary is reconstructed from a prior response.
  const request={kind,call,iteration,identity,states,target,scales,farMatrix,ev,cutRadius,
   cutHeightDenominator:cutRadius**4,
   full_shape:[DEPTH+1,K],modes:M,stage_count:DEPTH,
   eta:kind==='correction'?options.eta:0,all_node_and_boundary_rows_required:true};
  const before={state:states.map(digest),target:digest(target),scales:digest(scales),far:digest(farMatrix)};
  const result=linearChild(request);
  if(!result||typeof result.then==='function')throw Error('Use a completed synchronous current-chain child');
  if(states.some((s,i)=>digest(s)!==before.state[i])||digest(target)!==before.target||
     digest(scales)!==before.scales||digest(farMatrix)!==before.far)
   throw Error('Child mutated the actual native input arrays');
  return result;
 }
 function cutJets(node){
  const engine=cells[0].engine,y=new Float64Array(SIZE);y.set(node);
  for(let j=0;j<M;j++)y[M+j]*=cutPort;
  const jetsEvaluator=runtime.createMomentumPhysicalJetEvaluator(engine,{spacing:2});
  const rt=engine.root(y,cutProfile,1),jets=jetsEvaluator(y,cutProfile,1),g=rt.g;
  const field=engine.rhs(y,cutProfile,1,false,rt),slope=new Float64Array(M),second=new Float64Array(M);
  const sigma=g.drdx/g.r,k=g.dlogwdx;
  for(let j=0;j<M;j++){
   const m2=(2*(j+1))**2;
   slope[j]=m2*g.r**3*y[j]+Math.sqrt(2)*g.w*rt.L[j+1];
   second[j]=(m2*g.r**3*(field[j]+3*sigma*y[j])+Math.sqrt(2)*g.w*(jets.Ldot[j+1]+k*rt.L[j+1]))/g.drdx;
  }
  const meanSlopeCorrection=g.w*rt.L[0],meanSecondCorrection=g.w*(k*rt.L[0]+jets.Ldot[0])/g.drdx;
  const backgroundSecond=g.w*k/g.drdx;
  return {radius:g.r,backgroundSlope:g.w,backgroundSecond,E:g.E,Ep:2*g.w2*k/g.drdx,
   height:Array.from(node.slice(0,M),v=>g.r**4*v),slope:Array.from(slope),second:Array.from(second),
   meanSlope:g.w+meanSlopeCorrection,meanSecond:backgroundSecond+meanSecondCorrection,
   meanSlopeCorrection,meanSecondCorrection,minLeading:jets.minA,minD:jets.minD,
   endpointFullD:jets.maxDarboux,endpointPhi:jets.physicalHolonomyResidual,
   formalCurvature:jets.formalHeightCurvature};
 }
 function audit(states){
  let fullD=0,normalizedFullDefect=0,minLeading=Infinity,minD=Infinity,
   formalCurvature=0,maxPhysicalPV=0,actualMetric=0,holonomy=0;
  for(let n=0;n<DEPTH;n++){
   const c=cells[n],ev=runtime.createMomentumPhysicalJetEvaluator(c.engine,{spacing:2});
   let y=new Float64Array(SIZE);y.set(states[n+1]);
   for(const p of c.profiles)for(let k=0;k<=steps;k++){
    const x=k/steps,g=c.engine.geometry(p,x),j=ev(y,p,x),metric=runtime.actualMetricFromDarbouxJets(g,j.perAngle);
    fullD=Math.max(fullD,j.maxDarboux);minLeading=Math.min(minLeading,j.minA);minD=Math.min(minD,j.minD);
    formalCurvature=Math.max(formalCurvature,j.formalHeightCurvature);maxPhysicalPV=Math.max(maxPhysicalPV,j.peakValley);
    actualMetric=Math.max(actualMetric,metric.actualMetricRelativeOperatorError);
    holonomy=Math.max(holonomy,Math.abs(j.physicalHolonomyResidual));
    for(const t of j.perAngle)normalizedFullDefect=Math.max(normalizedFullDefect,Math.abs(t.darboux*g.E*g.E*g.r*g.drdx/g.w2));
    if(k<steps)y=c.engine.rk4(y,p,x,1/steps);
   }
  }
  return {fullD,normalizedFullDefect,minLeading,minD,formalCurvature,maxPhysicalPV,actualMetric,holonomy,
   actual_all_stage_finite_audit:true,continuous_C_or_closed_surface_audit:false};
 }
 function endpointJacobian(states,ev,target,scales){
  const response=child(ev,states,target,scales,'sensitivity',null);
  if(response.kind!=='sensitivity'||response.eta!==0||response.columns!==M)
   throw Error('Endpoint derivatives require the complete non-damped 112 RHS system');
  const cutSensitivity=array(response.cut_sensitivity,K*M,'actual complete cut sensitivities');
  const allSensitivity=array(response.complete_all_node_sensitivity,(DEPTH+1)*K*M,
   'actual complete all-node sensitivities');
  sameWords(allSensitivity.subarray(0,K*M),cutSensitivity,'complete node0/cut sensitivities');
  lastCompleteSensitivity={call,values:allSensitivity,receipt:response.receipt};
  const graph=new Float64Array(M*M);
  for(let i=0;i<M;i++)for(let j=0;j<M;j++)graph[i*M+j]=cutSensitivity[(M+i)*M+j]*cutRadius**4;
  // Source symmetric differences retain all second and mean-second rows; no old G is reused.
  const base=Float64Array.from(states[0]),scale=Math.max(1e-250,...base.slice(0,M).map(Math.abs));
  const differenceStep=1e-4,J=new Float64Array((3*M+2)*M);
  for(let k=0;k<M;k++){
   const h=differenceStep*Math.max(Math.abs(base[k]),.1*scale),plus=Float64Array.from(base),minus=Float64Array.from(base);
   plus[k]+=h;minus[k]-=h;
   for(let j=0;j<M;j++){plus[M+j]+=h*graph[j*M+k];minus[M+j]-=h*graph[j*M+k];}
   const a=cutJets(plus),b=cutJets(minus);
   const av=[...a.slope,...a.second,a.meanSlopeCorrection,a.meanSecondCorrection,...a.height];
   const bv=[...b.slope,...b.second,b.meanSlopeCorrection,b.meanSecondCorrection,...b.height];
   for(let j=0;j<av.length;j++)J[j*M+k]=(av[j]-bv[j])/(2*h*cutRadius**4);
  }
  // The actual local derivative and complete cut sensitivity, not a damped solve, give first slopes.
  const y=new Float64Array(SIZE);y.set(base);for(let j=0;j<M;j++)y[M+j]*=cutPort;
  const field=cells[0].engine.rhsWithJacobian(y,cutProfile,1),g=field.root.g;
  const transformed=Float64Array.from(cutSensitivity,(v,i)=>i<M*M?v:v*cutPort);
  const dF=multiply(field.jacobian,transformed,SIZE,K,M);
  for(let i=0;i<M;i++)for(let j=0;j<M;j++)
   J[i*M+j]=g.r**4*dF[i*M+j]/g.drdx+4*g.r**3*cutSensitivity[i*M+j];
  for(let j=0;j<M;j++)J[2*M*M+j]=dF[K*M+j]/g.drdx;
  for(const v of J)finite(v,'complete 338 endpoint derivative');
  return {matrix:J,graph,complete_current_cut_sensitivity:cutSensitivity,
   source_second_difference_step:differenceStep,linear_response_receipt:response.receipt,
   rows:['slope[m]','second[m]','meanSlopeCorrection','meanSecondCorrection','height[m]'],
   source_scope:'Current finite root and complete current-stage tangent system; no validated infinite nonlinear DN claim',
   exact_saved_matrix_nonresonance_certified:response.exact_saved_matrix_nonresonance_certified===true};
 }
 function solve(height,opts={}){
  actions();call++;
  const H=array(height,M,'current requested physical height'),target=Float64Array.from(H,v=>v/cutRadius**4);
  const scaleRecord=opts.scales?{values:array(opts.scales,DEPTH+1,'declared current scales'),identity:opts.scaleIdentity}:
   constantReferenceScales(target,options.referenceFloor);
  const scales=scaleRecord.values;for(const s of scales)positive(s,'current node scale');
  let states=opts.initial?opts.initial.map((s,n)=>array(s,K,'actual initial node '+n)):initial();
  if(states.length!==DEPTH+1)throw Error('Keep the complete 577-node current initial state');
  const history=[],trialRecords=[];let last;
  const maxIterations=opts.maxIterations??32,tolerance=opts.tolerance??2e-9;
  if(maxIterations!==32||tolerance!==2e-9)throw Error('This independent owner retains the declared 32/10/2e-9 nonlinear policy');
  positive(options.eta,'explicit nonlinear damping eta');
  const record=(v)=>{trialRecords.push(v);opts.trialDiagnostic?.(plain(v));};
  try{
   for(let it=0;it<maxIterations;it++){
    const ev=evaluate(states,target,true,scales);last=ev;
    history.push({iteration:it,norm:ev.norm,minA:ev.minA,minD:ev.minD});
    opts.progress?.(plain(history.at(-1)),states.map(v=>Array.from(v)));
    if(ev.norm<tolerance)break;
    const cor=child(ev,states,target,scales,'correction',it);
    if(cor.kind!=='correction'||cor.eta!==options.eta||!Array.isArray(cor.delta)||cor.delta.length!==DEPTH+1)
     throw Error('A complete current eta direction is required');
    const delta=cor.delta.map((s,n)=>array(s,K,'complete current direction '+n));
    let accepted=false;
    for(let k=0;k<10;k++){
     const lambda=2**(-k),trial=states.map((s,n)=>Float64Array.from(s,(v,j)=>v+lambda*delta[n][j]));
     let test=null,failure=null;
     try{test=evaluate(trial,target,false,scales);}catch(error){failure=error;}
     const diagnostic={iteration:it,trial:k,step:lambda,baseNorm:ev.norm};
     if(failure){
      const message=String(failure);
      const kind=message.includes('momentum branch D/S/A rejected')?'momentum-guard-rejection':
       (message.includes('momentum Newton')?'momentum-root-solver-rejection':'other-evaluation-rejection');
      record({...diagnostic,kind,error:message,stage:failure.tailStage,rawCell:failure.tailRawCell,rawSegment:failure.tailRawSegment});
      continue;
     }
     if(test.norm<ev.norm){states=trial;history.at(-1).step=lambda;accepted=true;
      record({...diagnostic,kind:'accepted',trialNorm:test.norm});break;}
     record({...diagnostic,kind:'residual-not-decreasing',trialNorm:test.norm});
    }
    if(!accepted)throw Error('multiple-shooting line search failed at '+ev.norm);
   }
   if(!last||last.norm>=tolerance)last=evaluate(states,target,true,scales);
   const converged=last.norm<tolerance;
   const result={schema:SCHEMA,identity,call,parameters:parameterRecord,
    requested_height:Array.from(H),target:Array.from(target),scale_identity:scaleRecord.identity,
    states:states.map(s=>Array.from(s)),state_sha256:states.map(digest),scales:Array.from(scales),
    normalizedResidual:last.norm,converged,history,trialRecords,minA:last.minA,minD:last.minD,
    meanHeightToCut:last.flows.reduce((sum,f)=>sum+f.meanHeight,0),nodeRadius:Array.from(nodeR),
    jets:cutJets(states[0]),nonlinear_finite_response_computed:true,
    old_graphs_or_gains_used:false,old_finite_tail_output_relabelled:false,
    complete_infinite_C_nonlinear_DN_certified:false};
   if(converged&&opts.jacobian){
    const j=endpointJacobian(states,last,target,scales);
    result.heightJetJacobian=Array.from(j.matrix);result.heightJetJacobianRows=j.rows;
    result.graphJacobian=Array.from(j.graph);result.endpointLinearReceipt=j.linear_response_receipt;
    result.heightJetJacobianMethod={first_slope:'analytic local derivative times full non-damped current sensitivity',
     mean_slope:'analytic local derivative times full non-damped current sensitivity',
     second:'original symmetric difference along the current cut tangent',mean_second:'same original symmetric difference',
     height:'same original symmetric difference',differenceStep:j.source_second_difference_step};
    result.exact_saved_matrix_nonresonance_certified=j.exact_saved_matrix_nonresonance_certified;
   }
   result.audit=opts.audit?audit(states):null;
   opts.completed?.(result);
   return result;
  }catch(error){
   opts.failed?.({schema:SCHEMA,identity,call,error:String(error),history,trialRecords,
    states:states.map(s=>Array.from(s)),state_sha256:states.map(digest),target:Array.from(target),
    scales:Array.from(scales),scale_identity:scaleRecord.identity,
    last_withJ_norm:last?.norm??null,current_native_completed:false});
   throw error;
  }
 }
 return {identity,parameters:parameterRecord,cells,initial,evaluate,cutJets,audit,solve,
  farMatrix,rawNode:[...geometry.rawNode],old_graphs_or_gains:null,
  currentCompleteSensitivity:()=>lastCompleteSensitivity};
}
