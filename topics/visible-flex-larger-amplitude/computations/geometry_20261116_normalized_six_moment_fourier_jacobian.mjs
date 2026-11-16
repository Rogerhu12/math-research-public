// R611: same-engine normalization of the actual original trigonometric tables.
// Every cached word is produced by that table element's original /N operation.
// No multiplication/division reassociation, Fourier orthogonality assumption,
// alternative root, or scientific acceptance condition is introduced.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

export const NORMALIZED_MOMENT_SCHEMA=
 'R611-current-Fourier-product-six-moment-original-normalization-v1';
const topic=process.env.VISIBLE_FLEX_SOURCE_TOPIC;
if(!topic)throw Error('Actual original public source topic required');
const originalPath=path.resolve(topic,'scripts/78718-tail-fourier-product-jacobian.mjs');
const sha=raw=>crypto.createHash('sha256').update(raw).digest('hex');
function sourceIdentity(file){
 const raw=fs.readFileSync(file);
 return {file:path.resolve(file),bytes:raw.length,sha256:sha(raw)};
}
const originalSource=sourceIdentity(originalPath);
if(originalSource.bytes!==3948||originalSource.sha256!==
 '205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25')
 throw Error('Declared original Fourier-product Jacobian source changed');
const moduleSource=sourceIdentity(fileURLToPath(import.meta.url));
const sourceBinding={
 schema:NORMALIZED_MOMENT_SCHEMA+'-actual-source-binding',
 current_source:moduleSource,original_local_J:originalSource,
 source_files_modified:false,
 original_trigonometric_call_order_and_argument_expressions_retained:true,
 each_cached_word_is_the_original_table_element_divided_by_actual_N:true,
 division_not_replaced_by_reciprocal_multiplication:true,
 original_six_moment_n_k_and_addition_order_retained:true,
 original_root_RHS_solveMany_assembly_and_mean_rows_retained:true,
 normalized_tables_owned_by_one_actual_engine:true,
 cross_engine_or_cross_field_value_cache:false,
 nonfinite_table_or_invalid_N_uses_original_runtime_divisions:true,
 new_scientific_acceptance_condition:false,
 resource_frontier_whole_run_or_wall_clock_equivalence_claimed:false
};

// This eligibility branch only chooses the expression representation. A false
// result preserves both complete raw tables and the original runtime divisions.
// Scan both complete tables before mutating either one. No exception is caught.
function normalizeActualTables(cos,sin,N,M,statistics){
 const observation={phase:'table-eligibility',actual_N:N,actual_M:M,
  scanned_elements:0,first_nonfinite:null,normalization_complete:false};
 statistics.last_observation=observation;
 if(!(Number.isInteger(N)&&Number.isFinite(N)&&N>=1)){
  statistics.normalization_reason='actual-N-is-not-a-finite-positive-integer';
  return false;
 }
 for(let n=0;n<N;n++)for(let k=0;k<=2*M;k++){
  const c=cos[n][k],s=sin[n][k];
  statistics.table_elements_scanned+=2;observation.scanned_elements+=2;
  if(!Number.isFinite(c)||!Number.isFinite(s)){
   statistics.normalization_reason='actual-original-trigonometric-table-nonfinite';
   observation.first_nonfinite={n,k,cosine_nonfinite:!Number.isFinite(c),
    sine_nonfinite:!Number.isFinite(s)};
   return false;
  }
 }
 observation.phase='table-normalization';
 for(let n=0;n<N;n++)for(let k=0;k<=2*M;k++){
  observation.current_element={n,k};
  cos[n][k]=cos[n][k]/N;
  statistics.normalization_divisions_completed++;
  sin[n][k]=sin[n][k]/N;
  statistics.normalization_divisions_completed++;
 }
 observation.phase='table-normalization-complete';
 observation.normalization_complete=true;
 statistics.normalization_reason='complete-actual-tables-normalized-by-original-division';
 return true;
}

// Local Jacobian prototype. No flow/solver entry is exported: the live workers
// retain their original code. Products of resolved sine/cosine basis functions
// are assembled from six sets of discrete Fourier moments.
export function createFourierProductJacobianEngine(options,base){
 const M=options.modes,N=options.quadrature,spacing=options.spacing??2,J=M+1,K=2*M,
  size=2*M+2,mu=options.mu,orientation=options.orientation??1,sq2=Math.sqrt(2),sq12=Math.sqrt(12);
 if(base.M!==M||base.N!==N||N<=4*spacing*M)throw Error('Resolved original base required');
 const freq=Float64Array.from({length:M},(_,j)=>spacing*(j+1)),
  cos=Array.from({length:N},(_,n)=>Float64Array.from({length:2*M+1},(_,j)=>Math.cos(spacing*j*2*Math.PI*n/N))),
  sin=Array.from({length:N},(_,n)=>Float64Array.from({length:2*M+1},(_,j)=>Math.sin(spacing*j*2*Math.PI*n/N)));

 const normalizedMomentStatistics={
  schema:NORMALIZED_MOMENT_SCHEMA+'-statistics',
  actual_N:N,actual_M:M,actual_spacing:spacing,
  table_elements_scanned:0,normalization_divisions_completed:0,
  rhs_calls_started:0,rhs_calls_returned:0,
  cached_moment_rows_completed:0,fallback_moment_rows_completed:0,
  cached_normalized_table_reads_in_complete_rows:0,
  fallback_normalization_divisions_in_complete_rows:0,
  normalization_qualified:false,normalization_reason:null,last_observation:null,
  scope:{
   integer_counts_are_actual_source_operations_not_timing_or_acceptance:true,
   row_counts_only_advance_after_the_complete_original_inner_k_loop:true,
   an_unreturned_rhs_call_is_not_inferred_to_have_completed_assembly:true,
   inner_k_progress_is_not_recorded_or_inferred:true,
   all_original_failures_and_resource_exceptions_propagate:true
  }
 };
 const normalized=normalizeActualTables(cos,sin,N,M,normalizedMomentStatistics);
 normalizedMomentStatistics.normalization_qualified=normalized;
 const normalizedMomentSourceBinding={...sourceBinding,
  actual_engine_parameters:{M,N,spacing,size,J,K,mu,orientation},
  actual_table_normalization_qualified:normalized};
 const CC=(v,i,j)=>i===0?(j===0?v[0]:sq2*v[j]):j===0?sq2*v[i]:v[Math.abs(i-j)]+v[i+j];
 const SS=(v,i,j)=>v[Math.abs(i-j)]-v[i+j];
 const odd=(v,k)=>k<0?-v[-k]:v[k];
 const CS=(v,i,j)=>i===0?sq2*v[j]:v[i+j]+odd(v,j-i);
 const SC=(v,i,j)=>j===0?sq2*v[i]:v[i+j]+odd(v,i-j);
 function solveMany(B,R){
  const L=new Float64Array(J*J),X=Float64Array.from(R);
  for(let i=0;i<J;i++)for(let j=0;j<=i;j++){let v=B[i*J+j];for(let k=0;k<j;k++)v-=L[i*J+k]*L[j*J+k];if(i===j){if(!(v>0))throw Error('Fourier-product Jacobian not positive');L[i*J+j]=Math.sqrt(v);}else L[i*J+j]=v/L[j*J+j];}
  for(let i=0;i<J;i++)for(let col=0;col<K;col++){let v=X[i*K+col];for(let k=0;k<i;k++)v-=L[i*J+k]*X[k*K+col];X[i*K+col]=v/L[i*J+i];}
  for(let i=J-1;i>=0;i--)for(let col=0;col<K;col++){let v=X[i*K+col];for(let k=i+1;k<J;k++)v-=L[k*J+i]*X[k*K+col];X[i*K+col]=v/L[i*J+i];}return X;
 }
 function rhsWithJacobian(state,profile,x){
  normalizedMomentStatistics.rhs_calls_started++;
  const momentObservation={phase:'original-root-and-RHS',
   call_number:normalizedMomentStatistics.rhs_calls_started,
   table_normalization_qualified:normalized,current_row:null,
   moment_rows_completed:0,inner_k_progress_recorded:false};
  normalizedMomentStatistics.last_observation=momentObservation;
  const rt=base.root(state,profile,x),g=rt.g,derivative=base.rhs(state,profile,x,false,rt),sigma=g.drdx/g.r,
   pref=orientation*sq2*g.r**3*g.drdx*g.w2/(sq12*mu),targetFac=orientation*sq12*mu/(sq2*g.r**4*g.w2),pFac=g.r**3/(sq2*g.w),
   FPm=new Float64Array(2*M+1),FTm=new Float64Array(2*M+1),CKm=new Float64Array(2*M+1),
   CUm=new Float64Array(2*M+1),CPm=new Float64Array(2*M+1),bmM=new Float64Array(2*M+1);
  for(let n=0;n<N;n++){
   momentObservation.phase='original-row-coefficients';momentObservation.current_row=n;
   const v=rt.e.rows[n],omega=1+g.w2*(v.L+v.quad),rho=1/(v.D*v.sd),
    FP=g.E*v.P*omega/v.D+2*g.w2*(1+v.K)*v.Pt*v.P/(v.S*v.S*v.sd),
    FT=-(g.E*v.Pt+g.w2*(1+v.K)*(g.w2*v.P*v.P+2*v.K+v.K*v.K)/v.S)*rho,
    flux=(1+v.K)*v.U/(v.S*v.sd),CK=v.U/(v.S*v.sd)+flux*g.w2*(1+v.K)/v.D,
    u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),CU=(v.K+u/(1+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd),
    CP=flux*(2*g.w2*v.P/v.S+g.w2*g.E*v.P/v.D),am=v.L+g.w2*v.Pt,
    bm=am+(1+am)*Math.expm1(-1.5*Math.log1p(-u));
   momentObservation.phase='original-six-moment-inner-loop';
   for(let k=0;k<=2*M;k++){const c=normalized?cos[n][k]:cos[n][k]/N,s=normalized?sin[n][k]:sin[n][k]/N;FPm[k]+=FP*s;CKm[k]+=CK*s;FTm[k]+=FT*c;CUm[k]+=CU*c;CPm[k]+=CP*c;bmM[k]+=bm*c;}
   momentObservation.moment_rows_completed++;
   if(normalized){normalizedMomentStatistics.cached_moment_rows_completed++;
    normalizedMomentStatistics.cached_normalized_table_reads_in_complete_rows+=2*(2*M+1);
   }else{normalizedMomentStatistics.fallback_moment_rows_completed++;
    normalizedMomentStatistics.fallback_normalization_divisions_in_complete_rows+=2*(2*M+1);}
  }
  momentObservation.phase='original-complete-right-FL-FQ-and-Cholesky-assembly';
  const right=new Float64Array(J*K),FL=new Float64Array(M*J),FQ=new Float64Array(M*M);
  for(let i=0;i<J;i++)for(let j=0;j<M;j++){const f=freq[j];right[i*K+j]=pFac*(f*CS(FPm,i,j+1)+f*f*CC(FTm,i,j+1));right[i*K+M+j]=-targetFac*CC(bmM,i,j+1);}
  for(let i=0;i<M;i++){FL[i*J]=SC(CKm,i+1,0);for(let j=0;j<M;j++){const f=freq[j],ck=SC(CKm,i+1,j+1),cu=SS(CUm,i+1,j+1);FL[i*J+j+1]=ck-f*cu;FQ[i*M+j]=pFac*(-f*(SS(CPm,i+1,j+1)+(f*f-1)*cu)+f*f*ck);}}
  const dL=solveMany(rt.e.B,right),jacobian=new Float64Array(size*K);
  for(let j=0;j<M;j++)for(let col=0;col<K;col++){
   let df=-freq[j]*dL[(j+1)*K+col]+(col<M?FQ[j*M+col]:FL[j*J+col-M+1]*targetFac);
   for(let i=0;i<J;i++)df+=FL[j*J+i]*dL[i*K+col];
   jacobian[j*K+col]=sigma*((col===j?freq[j]*freq[j]-4:0)+sq2*g.w*(dL[(j+1)*K+col]+(col===M+j?targetFac:0))/g.r**3);
   jacobian[(M+j)*K+col]=(col===M+j?(4-freq[j]*freq[j])*sigma:0)+(col===j?-pref*freq[j]*freq[j]*(freq[j]*freq[j]-1)*pFac:0)+pref*freq[j]*df;
  }
  for(let col=0;col<K;col++)jacobian[2*M*K+col]=g.drdx*g.w*dL[col];
  normalizedMomentStatistics.rhs_calls_returned++;
  momentObservation.phase='original-complete-local-J-return';
  return {derivative,jacobian,root:rt};
 }
 return {rhsWithJacobian,scope:'local prototype only; no flow entry',
  normalizedMomentStatistics,normalizedMomentSourceBinding,
  momentEvaluation:NORMALIZED_MOMENT_SCHEMA};
}
