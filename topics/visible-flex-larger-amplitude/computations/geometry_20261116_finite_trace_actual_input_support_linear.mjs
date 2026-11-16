// R523: use the same actual finite-input scan to index each used T row's
// nonzero columns. Every retained product/add and each output's j order is
// unchanged. The complete output and the original nonfinite fallback remain.
// No root, field, RK, mean, finite-output gate, clock or retry is added here.
export const INPUT_SUPPORT_LINEAR_SCHEMA=
 'original64-finite-input-row-support-linear-v1';

export function newInputSupportLinearStatistics(){
 return {schema:INPUT_SUPPORT_LINEAR_SCHEMA,
  calls_started:0,calls_completed:0,finite_input_calls:0,
  original_complete_loop_calls:0,actual_A_entries_checked:0,
  actual_used_T_entries_checked:0,zero_j_terms_skipped:0,
  scalar_products_skipped:0,retained_j_terms_completed:0,
  actual_nonzero_T_words_indexed:0,actual_zero_T_words_seen:0,
  T_rows_indexed:0,zero_T_products_skipped_after_nonzero_A:0,
  retained_scalar_products_completed:0,
  fallback_reason_counts:{},last_observation:null,
  actual_used_T_is_only_first_K_rows:true,
  support_is_rebuilt_from_actual_T_for_every_call:true,
  no_support_reused_across_fields_steps_or_calls:true,
  no_block_structure_or_zero_H_assumption:true,
  both_mean_output_rows_retained:true,
  original_nonzero_product_then_add_and_j_order_retained:true,
  no_output_finiteness_gate_added:true,
  nonfinite_output_class_only_not_NaN_payload:true,
  resource_or_other_exception_caught_for_retry:false,
  whole_run_word_or_runtime_equivalence_claimed:false};
}

// Internal caller contract: ordinary numeric typed arrays, no concurrent
// mutation, original compatible dimensions and binary64 product then RN add.
// Numeric values are never cached in the support; only current column indices
// are stored. Array indices are ordinary JS numbers, without narrowing casts.
export function completeInputSupportLinear(A,T,size,Kdim,stats){
 const dt=new Float64Array(size*Kdim);
 stats.calls_started++;
 const seen=stats.last_observation={rows:size,shape_columns:Kdim,
  phase:'actual-A-finiteness',input_index:null,
  finite_input_qualification:null,first_nonfinite_input:null,
  support_rows_completed:0,support_entries_completed:0,
  row:null,shape_index:null,j_action:null,j_completed:null,
  selected_T_row_nonzero_columns:null,
  current_inner_columns_not_individually_recorded:false,
  decision:null,completed:false};
 let reason=null,rowStarts=null,columns=null;
 for(let index=0;index<size*Kdim;index++){
  seen.input_index=index;stats.actual_A_entries_checked++;
  if(!Number.isFinite(A[index])){
   reason='actual-A-entry-nonfinite';
   seen.first_nonfinite_input={array:'A',index,value:String(A[index])};
   break;
  }
 }
 if(reason===null){
  seen.phase='actual-used-T-finiteness-and-row-support';seen.input_index=null;
  rowStarts=new Array(Kdim+1);columns=[];rowStarts[0]=0;
  // This is the same row-major used-T scan. T's two final mean rows are
  // not read by the original multiplication and impose no new condition.
  for(let j=0;j<Kdim&&reason===null;j++){
   rowStarts[j]=columns.length;
   for(let k=0;k<Kdim;k++){
    const index=j*Kdim+k,value=T[index];
    seen.input_index=index;stats.actual_used_T_entries_checked++;
    if(!Number.isFinite(value)){
     reason='actual-used-T-entry-nonfinite';
     seen.first_nonfinite_input={array:'T',index,value:String(value)};
     break;
    }
    if(value!==0){
     columns.push(k);stats.actual_nonzero_T_words_indexed++;
     seen.support_entries_completed++;
    }else stats.actual_zero_T_words_seen++;
   }
   if(reason===null){
    rowStarts[j+1]=columns.length;stats.T_rows_indexed++;
    seen.support_rows_completed++;
   }
  }
 }
 if(reason!==null){
  stats.original_complete_loop_calls++;
  stats.fallback_reason_counts[reason]=(stats.fallback_reason_counts[reason]??0)+1;
  seen.finite_input_qualification=false;seen.decision='original-complete-i-j-k-loop';
  seen.phase='original-complete-i-j-k-loop';
  seen.current_inner_columns_not_individually_recorded=true;
  // Full original fallback. No support, zero decision, per-column observer,
  // finite-output check, exception catch or restarted budget is inserted.
   for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
    const z=A[i*Kdim+j];for(let k=0;k<Kdim;k++)dt[i*Kdim+k]+=z*T[j*Kdim+k];
   }
  stats.calls_completed++;seen.completed=true;
  seen.current_inner_columns_not_individually_recorded=false;
  seen.phase='original-complete-loop-returned';
  return dt;
 }
 stats.finite_input_calls++;seen.finite_input_qualification=true;
 seen.input_index=null;seen.decision='actual-finite-input-row-support';
 seen.phase='original-j-order-with-actual-input-support';
 for(let i=0;i<size;i++)for(let j=0;j<Kdim;j++){
  seen.row=i;seen.shape_index=j;seen.j_completed=false;
  seen.current_inner_columns_not_individually_recorded=false;
  seen.selected_T_row_nonzero_columns=null;
  const z=A[i*Kdim+j];
  if(z===0){
   seen.j_action='skip-actual-zero-coefficient';
   stats.zero_j_terms_skipped++;stats.scalar_products_skipped+=Kdim;
   seen.j_completed=true;
   continue;
  }
  const begin=rowStarts[j],end=rowStarts[j+1],count=end-begin;
  seen.selected_T_row_nonzero_columns=count;
  seen.j_action='original-product-add-on-actual-nonzero-T-columns';
  seen.current_inner_columns_not_individually_recorded=true;
  // columns[begin:end] is the ascending actual nonzero support of T[j,:].
  // Each remaining expression is the original product then add. No terms
  // from different j are combined; different output columns never alias.
  for(let entry=begin;entry<end;entry++){
   const k=columns[entry];dt[i*Kdim+k]+=z*T[j*Kdim+k];
  }
  // Inner-loop counts are committed only after that whole original-order
  // support loop returned; an interruption does not invent its partial k.
  stats.retained_scalar_products_completed+=count;
  stats.zero_T_products_skipped_after_nonzero_A+=Kdim-count;
  stats.scalar_products_skipped+=Kdim-count;
  stats.retained_j_terms_completed++;seen.j_completed=true;
  seen.current_inner_columns_not_individually_recorded=false;
 }
 // Finite inputs do not imply finite products or sums. Original overflow,
 // infinity and NaN classes remain for original downstream consumers.
 stats.calls_completed++;seen.completed=true;
 seen.phase='input-support-complete-loop-returned';
 return dt;
}
