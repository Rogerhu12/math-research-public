// R471: eligibility for retaining the original +0 nonlinear dFlux array.
// The authoritative primal/root and finiteRootDirection have already run.
// This helper never changes those values, a branch, a coefficient, a matrix
// entry, or a scientific gate. A false return selects the original complete
// angular loop. No thrown error (including resource exhaustion) is caught.
// All arithmetic below belongs to the public Actions science invocation.
export const ZERO_NONLINEAR_SPLIT_FLUX_SCHEMA=
 'original64-zero-nonlinear-split-flux-eligibility-v1';

export function newZeroNonlinearFluxStatistics(){
 return {schema:ZERO_NONLINEAR_SPLIT_FLUX_SCHEMA,
  calls_started:0,calls_completed:0,actual_zero_trace_candidates:0,
  certified_zero_dflux_calls:0,original_angular_fallback_calls:0,
  sparse_direction_entries_checked:0,complete_angular_rows_checked:0,
  complete_shape_direction_pairs_checked:0,fallback_reason_counts:{},
  last_observation:null,
  actual_primal_and_finiteRootDirection_always_retained:true,
  same_original_angularPartials_factor_evaluated:true,
  unused_q_or_bm_not_eligibility_gates:true,
  literal_trigonometric_orthogonality_not_assumed:true,
  original_complete_final_assembly_and_both_mean_rows_retained:true,
  resource_or_other_exception_caught_for_retry:false,
  whole_run_word_or_runtime_equivalence_claimed:false,
  continuous_or_IEEE_rounding_map_derivative_certificate_claimed:false};
}

// Called only after the unchanged finiteRootDirection entry returns. The
// sparse-word check below also makes the needed initial-direction premise
// explicit rather than trusting a shape label or a caller's zero flag.
// angularPartials is the exact original function, not a closed-form shadow.
export function certifyZeroNonlinearSplitFlux(rt,state,dL,tables,dims,
 pCoefficient,angularPartials,resourceCheck,stats){
 const {M,N,J,K}=dims,trace=rt.finiteTrace;
 stats.calls_started++;
 const seen=stats.last_observation={mode_count:M,angular_rows:N,shape_columns:K,
  phase:'actual-trace',angle:null,direction_pair:null,sparse_row:null,
  decision:null,reason:null,detail:null,completed:false};
 const ordinary=(reason,detail={})=>{
  stats.original_angular_fallback_calls++;
  stats.fallback_reason_counts[reason]=(stats.fallback_reason_counts[reason]??0)+1;
  stats.calls_completed++;
  seen.decision='original-complete-angular-loop';seen.reason=reason;
  seen.detail=detail;seen.completed=true;
  return false;
 };
 if(!Number.isInteger(M)||M<1||!Number.isInteger(N)||N<=0||
    J!==M+1||K!==2*M||state.length!==K+2||dL.length!==J*K||
    pCoefficient.length!==M||rt.L.length!==J||rt.e.rows.length!==N||
    tables.freq.length!==M||tables.cs.length!==N||tables.sn.length!==N)
  return ordinary('actual-shape-or-positive-angular-count-unavailable');
 if(trace?.initial_guess_supplied!==false||!Array.isArray(trace?.accepted_updates)||
    trace.accepted_updates.length!==0||trace.iterations!==0||
    !['normal-stop','original-roundoff-fallback'].includes(trace.return_reason))
  return ordinary('actual-empty-unsupplied-successful-trace-unavailable');
 const ell=trace.target_factor;
 if(!Number.isFinite(ell))
  return ordinary('actual-target-factor-nonfinite',{value:String(ell)});
 seen.phase='actual-zero-state';
 for(let i=0;i<K;i++)if(state[i]!==0)
  return ordinary('actual-shape-state-not-zero',{index:i,value:String(state[i])});
 for(let i=0;i<J;i++)if(rt.L[i]!==0)
  return ordinary('actual-returned-root-not-zero',{index:i,value:String(rt.L[i])});
 // Means need not be zero. Their primal values and complete derivative rows
 // are left to the original caller and its unchanged final assembly.
 stats.actual_zero_trace_candidates++;
 seen.phase='actual-sparse-initial-direction';
 for(let i=0;i<J;i++){
  if((i&15)===0)resourceCheck();
  seen.sparse_row=i;
  const offset=i*K;
  for(let col=0;col<K;col++){
   const expected=i>0&&col===M+i-1?ell:0;
   stats.sparse_direction_entries_checked++;
   if(!Object.is(dL[offset+col],expected))
    return ordinary('actual-direction-is-not-original-sparse-initial-word',
     {row:i,column:col,value:String(dL[offset+col]),expected:String(expected)});
  }
 }
 for(let j=0;j<M;j++){
  if(!Number.isFinite(tables.freq[j])||!Number.isFinite(pCoefficient[j]))
   return ordinary('actual-frequency-or-formed-p-coefficient-nonfinite',
    {index:j,frequency:String(tables.freq[j]),coefficient:String(pCoefficient[j])});
 }
 seen.sparse_row=null;seen.phase='original-angular-factor-and-sparse-directions';
 for(let n=0;n<N;n++){
  if((n&31)===0)resourceCheck();
  seen.angle=n;seen.direction_pair=null;
  const cs=tables.cs[n],sn=tables.sn[n],v=rt.e.rows[n];
  if(!cs||!sn||cs.length!==J||sn.length!==M||!v)
   return ordinary('actual-angular-row-shape-unavailable',{angle:n});
  for(const name of ['P','Pt','L','K','U'])if(v[name]!==0)
   return ordinary('actual-angular-primal-row-not-zero',
    {angle:n,component:name,value:String(v[name])});
  // Keep the original AD computation, including its actual parentheses.
  // Only factor enters the original split loop. Its unused q is not a gate.
  const a=angularPartials(v,rt.g,false),f=a.factor;
  if(!f||f.length!==4||!Number.isFinite(f[0])||!Number.isFinite(f[1])||
     !Number.isFinite(f[2])||!Number.isFinite(f[3])||f[0]!==0)
   return ordinary('original-factor-not-finite-zero-with-finite-partials',{angle:n});
  for(let j=0;j<M;j++){
   seen.direction_pair=j;
   const c=cs[j+1],sine=sn[j],m=tables.freq[j],pc=pCoefficient[j];
   if(!Number.isFinite(c)||!Number.isFinite(sine))
    return ordinary('used-literal-cosine-or-sine-nonfinite',{angle:n,index:j});
   // There is at most one nonzero contribution to each actual direction.
   // All other original terms are signed zeros. The explicit leading +0
   // is essential: a unique product rounding to -0 accumulates to +0.
   // Retain the original (-m*0+q)*sine and (-m*ell+0)*sine parentheses.
   const q=(m*m-1)*pc,
    dlPi=0+ell*c,
    duQ=0+(-m*0+q)*sine,
    duPi=0+(-m*ell+0)*sine,
    p=pc*sine,
    pt=m*pc*c,
    dFactorQ=f[1]*p+f[2]*pt+f[3]*0,
    dFactorPi=f[1]*0+f[2]*0+f[3]*dlPi;
   if(!Number.isFinite(q)||!Number.isFinite(dlPi)||!Number.isFinite(duQ)||
      !Number.isFinite(duPi)||!Number.isFinite(p)||!Number.isFinite(pt)||
      !Number.isFinite(dFactorQ)||!Number.isFinite(dFactorPi))
    return ordinary('original-sparse-angular-direction-nonfinite',{angle:n,index:j});
   stats.complete_shape_direction_pairs_checked++;
  }
  stats.complete_angular_rows_checked++;
 }
 // Each original df is now a sum of products of finite numbers with signed
 // zeros, hence a signed zero. Multiplication by every used finite sine and
 // division by N>0 preserves a signed zero. RN addition to the original
 // +0-initialized dFlux keeps +0 at every original n. No trig identity or
 // pref*ell=sigma replacement is used. The caller retains that same array.
 stats.certified_zero_dflux_calls++;stats.calls_completed++;
 seen.phase='original-positive-zero-dflux-retained';seen.angle=null;
 seen.direction_pair=null;seen.decision='retain-original-positive-zero-dflux';
 seen.completed=true;
 return true;
}
