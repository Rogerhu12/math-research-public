// R550: one accepted complete finite RootEval, reused only at the next
// iteration of the same original root invocation. No cross-root cache.
#ifndef VISIBLE_R550_ACCEPTED_ROOT_EVALUATION_REUSE_HPP
#define VISIBLE_R550_ACCEPTED_ROOT_EVALUATION_REUSE_HPP
#include <utility>

struct R550ReusePathStats {
  uint64_t iteration_sites=0,original_main_evaluations_started=0,
    original_main_evaluations_returned=0,reused_complete_evaluations=0,
    accepted_results_offered=0,qualified_results=0,
    shape_declined_results=0,nonfinite_declined_results=0,
    no_next_iteration_results=0,summary_words_visited=0,
    residual_words_visited=0,angular_rows_visited=0,angular_words_visited=0;
  bool last_present=false;
  const char *last_phase="absent";
  int last_iteration=-1,last_row=-1,last_component=-1;
  void mark(const char *phase,int iteration,int row=-1,int component=-1){
    last_present=true;last_phase=phase;last_iteration=iteration;
    last_row=row;last_component=component;
  }
  void join(const R550ReusePathStats &s){
    iteration_sites+=s.iteration_sites;
    original_main_evaluations_started+=s.original_main_evaluations_started;
    original_main_evaluations_returned+=s.original_main_evaluations_returned;
    reused_complete_evaluations+=s.reused_complete_evaluations;
    accepted_results_offered+=s.accepted_results_offered;
    qualified_results+=s.qualified_results;
    shape_declined_results+=s.shape_declined_results;
    nonfinite_declined_results+=s.nonfinite_declined_results;
    no_next_iteration_results+=s.no_next_iteration_results;
    summary_words_visited+=s.summary_words_visited;
    residual_words_visited+=s.residual_words_visited;
    angular_rows_visited+=s.angular_rows_visited;
    angular_words_visited+=s.angular_words_visited;
    if(s.last_present){
      last_present=true;last_phase=s.last_phase;last_iteration=s.last_iteration;
      last_row=s.last_row;last_component=s.last_component;
    }
  }
};
struct R550RootReuseStats {
  R550ReusePathStats primal,trace_variation;
  void join(const R550RootReuseStats &s){
    primal.join(s.primal);trace_variation.join(s.trace_variation);
  }
};

// No numerical comparison with a second evaluation is performed. The
// candidate is the complete value actually returned at an accepted trial.
// Eligibility only selects reuse; declining it follows the original call.
template<class Eval>
static void r550_offer_accepted(Eval &saved,bool &ready,Eval &candidate,
    const Problem &p,int accepted_iteration,R550ReusePathStats &s){
  ready=false;++s.accepted_results_offered;
  s.mark("accepted-result-offered",accepted_iteration);
  if(accepted_iteration>=29){
    ++s.no_next_iteration_results;
    s.mark("original-iteration-limit-has-no-next-site",accepted_iteration);
    return;
  }
  time_check();
  if(candidate.residual.size()!=size_t(p.J)||candidate.rows.size()!=size_t(p.N)){
    ++s.shape_declined_results;
    s.mark("shape-declined-original-next-evaluation",accepted_iteration);
    return;
  }
  const Q summary[]={candidate.err,candidate.max_quad,
    candidate.minD,candidate.minS,candidate.minA};
  for(int i=0;i<5;++i){
    ++s.summary_words_visited;s.mark("qualifying-summary",accepted_iteration,-1,i);
    if(!finiteq(summary[i])){
      ++s.nonfinite_declined_results;
      s.mark("nonfinite-summary-original-next-evaluation",accepted_iteration,-1,i);
      return;
    }
  }
  for(int i=0;i<p.J;++i){
    if((i&31)==0)time_check();
    ++s.residual_words_visited;s.mark("qualifying-residual",accepted_iteration,i);
    if(!finiteq(candidate.residual[size_t(i)])){
      ++s.nonfinite_declined_results;
      s.mark("nonfinite-residual-original-next-evaluation",accepted_iteration,i);
      return;
    }
  }
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();
    ++s.angular_rows_visited;
    const auto &v=candidate.rows[size_t(n)];
    const Q words[]={v.P,v.Pt,v.L,v.K,v.U,v.S,v.D,v.A,v.sd,v.quad};
    for(int i=0;i<10;++i){
      ++s.angular_words_visited;s.mark("qualifying-angular-row",accepted_iteration,n,i);
      if(!finiteq(words[i])){
        ++s.nonfinite_declined_results;
        s.mark("nonfinite-angular-original-next-evaluation",accepted_iteration,n,i);
        return;
      }
    }
  }
  saved=std::move(candidate);ready=true;++s.qualified_results;
  s.mark("complete-finite-accepted-result-ready",accepted_iteration);
}

template<class Eval,class OriginalEvaluation>
static Eval r550_original_or_accepted(Eval &saved,bool &ready,
    int iteration,R550ReusePathStats &s,OriginalEvaluation original){
  // Keep a check at every original iteration evaluation boundary. Work
  // saved and added checks can change resource frontiers; no equality of
  // wall time, fenv sticky flags or allocation behaviour is asserted.
  time_check();++s.iteration_sites;s.mark("iteration-evaluation-site",iteration);
  if(ready){
    ready=false;++s.reused_complete_evaluations;
    s.mark("reused-complete-accepted-result",iteration);
    return std::move(saved);
  }
  ++s.original_main_evaluations_started;
  s.mark("executing-original-main-evaluation",iteration);
  Eval value=original();
  ++s.original_main_evaluations_returned;
  s.mark("original-main-evaluation-returned",iteration);
  return value;
}

static void r550_print_path_stats(std::ostream &o,const R550ReusePathStats &s){
  o<<"{\"iteration_sites\":"<<s.iteration_sites
   <<",\"original_main_evaluations_started\":"<<s.original_main_evaluations_started
   <<",\"original_main_evaluations_returned\":"<<s.original_main_evaluations_returned
   <<",\"reused_complete_evaluations\":"<<s.reused_complete_evaluations
   <<",\"accepted_results_offered\":"<<s.accepted_results_offered
   <<",\"qualified_results\":"<<s.qualified_results
   <<",\"shape_declined_results\":"<<s.shape_declined_results
   <<",\"nonfinite_declined_results\":"<<s.nonfinite_declined_results
   <<",\"no_next_iteration_results\":"<<s.no_next_iteration_results
   <<",\"summary_words_visited\":"<<s.summary_words_visited
   <<",\"residual_words_visited\":"<<s.residual_words_visited
   <<",\"angular_rows_visited\":"<<s.angular_rows_visited
   <<",\"angular_words_visited\":"<<s.angular_words_visited
   <<",\"last_present\":"<<(s.last_present?"true":"false")<<",\"last\":";
  if(!s.last_present)o<<"null";
  else o<<"{\"phase\":"<<quoted(s.last_phase)
    <<",\"iteration_zero_based\":"<<s.last_iteration
    <<",\"row_zero_based\":"<<(s.last_row<0?"null":std::to_string(s.last_row))
    <<",\"component_zero_based\":"<<(s.last_component<0?"null":std::to_string(s.last_component))<<"}";
  o<<"}";
}
static void r550_print_reuse_stats(std::ostream &o,const R550RootReuseStats &s){
  o<<"{\"schema\":\"R550-same-root-next-iteration-complete-evaluation-reuse-v1\",\"primal\":";
  r550_print_path_stats(o,s.primal);
  o<<",\"trace_variation\":";r550_print_path_stats(o,s.trace_variation);
  o<<",\"original_angular_evaluations_count_only_executed_calls\":true"
   <<",\"original_R535_word_counters_count_only_executed_calls\":true"
   <<",\"skipped_work_is_not_added_to_original_counters\":true"
   <<",\"merge_order\":\"original-stage-index-order\""
   <<",\"root_iteration_and_trial_limits_unchanged\":true"
   <<",\"complete_scientific_evaluation_not_inferred_from_counters\":true"
   <<",\"cross_root_state_or_geometry_cache\":false}";
}
#endif
