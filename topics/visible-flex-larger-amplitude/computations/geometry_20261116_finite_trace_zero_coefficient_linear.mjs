// R474: actual finite-input zero-coefficient elision in the original complete
// i/j/k linear product. R473 proves finite output words and nonfinite classes,
// not NaN payloads, whole-run words, timing or a derivative of IEEE rounding.
// This helper adds no finite-output throw, scientific gate or retry. The
// caller's original root, local Jacobian, RK and deadline remain authoritative.
export const ZERO_COEFFICIENT_LINEAR_SCHEMA=
 'original64-finite-input-zero-coefficient-linear-v1';

export function newZeroCoefficientLinearStatistics(){
 return {schema:ZERO_COEFFICIENT_LINEAR_SCHEMA,
  calls_started:0,calls_completed:0,finite_input_calls:0,
  original_complete_loop_calls:0,actual_A_entries_checked:0,
  actual_used_T_entries_checked:0,zero_j_terms_skipped:0,
  scalar_products_skipped:0,retained_j_terms_completed:0,
  fallback_reason_counts:{},last_observation:null,
  actual_used_T_is_only_first_K_rows:true,
  both_mean_output_rows_retained:true,
  original_nonzero_product_then_add_and_j_order_retained:true,
  no_output_finiteness_gate_added:true,
  nonfinite_output_class_only_not_NaN_payload:true,
  resource_or_other_exception_caught_for_retry:false,
  whole_run_word_or_runtime_equivalence_claimed:false};
}

// Internal caller: A and T are the original ordinary typed numeric arrays,
// without concurrent mutation, and size/K have the original flow dimensions.
// Only stats is changed besides the newly allocated original output array.
export function completeZeroElidingLinear(A,T,size,Kdim,stats){
 const dt=new Float64Array(size*Kdim);
 stats.calls_started++;
 const seen=stats.last_observation={rows:size,shape_columns:Kdim,
  phase:'actual-A-finiteness',input_index:null,
  finite_input_qualification:null,first_nonfinite_input:null,
  row:null,shape_index:null,j_action:null,j_completed:null,
  current_inner_columns_not_individually_recorded:false,
  decision:null,completed:false};
 let reason=null;
 for(let index=0;index<size*Kdim;index++){
  seen.input_index=index;stats.actual_A_entries_checked++;
  if(!Number.isFinite(A[index])){
   reason='actual-A-entry-nonfinite';
   seen.first_nonfinite_input={array:'A',index,value:String(A[index])};
   break;
  }
 }
 if(reason===null){
  seen.phase='actual-used-T-finiteness';seen.input_index=null;
  // Original linear reads T[j*Kdim+k] only for j,k<Kdim. The two mean
  // tangent input rows are not inspected or imposed as a new condition.
  for(let index=0;index<Kdim*Kdim;index++){
   seen.input_index=index;stats.actual_used_T_entries_checked++;
   if(!Number.isFinite(T[index])){
    reason='actual-used-T-entry-nonfinite';
    seen.first_nonfinite_input={array:'T',index,value:String(T[index])};
    break;
   }
  }
 }
 if(reason!==null){
  stats.original_complete_loop_calls++;
  stats.fallback_reason_counts[reason]=(stats.fallback_reason_counts[reason]??0)+1;
  seen.finite_input_qualification=false;seen.decision='original-complete-i-j-k-loop';
  seen.phase='original-complete-i-j-k-loop';
  seen.current_inner_columns_not_individually_recorded=true;
  // This is the complete original fallback body. No per-column observer,
  // finite-output check, zero test, catch or restarted budget is inserted.
   for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
    const z=A[i*Kdim+j];for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*T[j*Kdim+k];
   }
  stats.calls_completed++;seen.completed=true;
  seen.current_inner_columns_not_individually_recorded=false;
  seen.phase='original-complete-loop-returned';
  return dt;
 }
 stats.finite_input_calls++;seen.finite_input_qualification=true;
 seen.input_index=null;seen.decision='actual-zero-coefficient-elision';
 seen.phase='original-order-with-actual-zero-elision';
 for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
  seen.row=i;seen.shape_index=j;seen.j_completed=false;
  seen.current_inner_columns_not_individually_recorded=false;
  const z=A[i*Kdim+j];
  if(z===0){
   // Both signs of zero qualify. Each omitted product would be a signed
   // zero because every actually used T word was finite. The original +0
   // accumulator cannot become -0; R473 also treats overflow/NaN classes.
   seen.j_action='skip-actual-zero-coefficient';
   stats.zero_j_terms_skipped++;stats.scalar_products_skipped+=Kdim;
   seen.j_completed=true;
   continue;
  }
  seen.j_action='original-nonzero-product-then-add';
  seen.current_inner_columns_not_individually_recorded=true;
  for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*T[j*Kdim+k];
  stats.retained_j_terms_completed++;seen.j_completed=true;
  seen.current_inner_columns_not_individually_recorded=false;
 }
 // A normal return is not a finite-output assertion. Infinities or NaNs
 // formed by original retained products/sums remain for original consumers.
 stats.calls_completed++;seen.completed=true;
 seen.phase='zero-eliding-complete-loop-returned';
 return dt;
}
