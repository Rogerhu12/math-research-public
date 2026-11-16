// R535: finite words shared only within one actual root invocation/evaluation.
// This is a source library, not an alternate stopping rule or scientific test.
#ifndef VISIBLE_R535_ROOT_FINITE_WORDS_HPP
#define VISIBLE_R535_ROOT_FINITE_WORDS_HPP

struct R535WordStats {
  uint64_t fixed_requests=0,fixed_builds_started=0,fixed_builds_completed=0,
    fixed_qualified_builds=0,fixed_nonfinite_mode_fallbacks=0,
    fixed_nonfinite_angular_fallbacks=0,fixed_mode_pairs_formed=0,
    fixed_angular_pairs_formed=0,fixed_evaluations_used=0,
    fixed_evaluations_fallback=0,fixed_evaluations_without_local_cache=0,
    u_builds_started=0,u_builds_completed=0,u_qualified_builds=0,
    u_nonfinite_mode_fallbacks=0,u_mode_words_formed=0,
    u_angular_rows_used=0,u_angular_rows_fallback=0;
  bool last_present=false,last_fixed_used=false,last_u_used=false;
  const char *last_phase="absent";
  int last_mode=-1,last_angle=-1;
  void mark(const char *phase,int mode=-1,int angle=-1){
    last_present=true;last_phase=phase;last_mode=mode;last_angle=angle;
  }
  void join(const R535WordStats &s){
    fixed_requests+=s.fixed_requests;
    fixed_builds_started+=s.fixed_builds_started;
    fixed_builds_completed+=s.fixed_builds_completed;
    fixed_qualified_builds+=s.fixed_qualified_builds;
    fixed_nonfinite_mode_fallbacks+=s.fixed_nonfinite_mode_fallbacks;
    fixed_nonfinite_angular_fallbacks+=s.fixed_nonfinite_angular_fallbacks;
    fixed_mode_pairs_formed+=s.fixed_mode_pairs_formed;
    fixed_angular_pairs_formed+=s.fixed_angular_pairs_formed;
    fixed_evaluations_used+=s.fixed_evaluations_used;
    fixed_evaluations_fallback+=s.fixed_evaluations_fallback;
    fixed_evaluations_without_local_cache+=s.fixed_evaluations_without_local_cache;
    u_builds_started+=s.u_builds_started;
    u_builds_completed+=s.u_builds_completed;
    u_qualified_builds+=s.u_qualified_builds;
    u_nonfinite_mode_fallbacks+=s.u_nonfinite_mode_fallbacks;
    u_mode_words_formed+=s.u_mode_words_formed;
    u_angular_rows_used+=s.u_angular_rows_used;
    u_angular_rows_fallback+=s.u_angular_rows_fallback;
    if(s.last_present){
      last_present=true;last_phase=s.last_phase;last_mode=s.last_mode;
      last_angle=s.last_angle;last_fixed_used=s.last_fixed_used;
      last_u_used=s.last_u_used;
    }
  }
};

// Created as an automatic object in the one original root() call. No static,
// thread_local, global, cross-state or cross-RK cache exists.
struct R535FixedRootWords {
  const Problem *problem;
  const V *state;
  const Geometry *geometry;
  bool attempted=false,qualified=false;
  V momentum,pt,P,Pt;
  R535FixedRootWords(const Problem &p,const V &s,const Geometry &g):
    problem(&p),state(&s),geometry(&g){}
};

static void r535_build_fixed_words(R535FixedRootWords &c,
    const Problem &p,const V &state,const Geometry &g,R535WordStats &s){
  // This is a closed caller/source identity check, not a new BVP condition.
  if(c.problem!=&p||c.state!=&state||c.geometry!=&g)
    throw std::runtime_error("R535-local-root-cache-source-scope-mismatch");
  if(c.attempted)return;
  c.attempted=true;++s.fixed_builds_started;s.mark("fixed-mode-build");
  c.momentum.assign(p.M,0);c.pt.assign(p.J,0);
  const Q r3=g.r*g.r*g.r;
  for(int j=0;j<p.M;++j){
    s.mark("fixed-mode-build",j);
    c.momentum[j]=-p.frequency[j]*r3*state[j]/(p.sq2*g.w);
    c.pt[j+1]=p.frequency[j]*c.momentum[j];
    ++s.fixed_mode_pairs_formed;
    if(!finiteq(c.momentum[j])||!finiteq(c.pt[j+1])){
      ++s.fixed_nonfinite_mode_fallbacks;
      ++s.fixed_builds_completed;s.mark("fixed-nonfinite-mode-fallback",j);
      return;
    }
  }
  c.P.assign(p.N,0);c.Pt.assign(p.N,0);
  for(int n=0;n<p.N;++n){
    s.mark("fixed-angular-build",-1,n);
    if((n&31)==0)time_check();
    Q P=0,Pt=0;
    const Q *cs=p.cosine.data()+size_t(n)*p.J;
    const Q *sn=p.sine.data()+size_t(n)*p.M;
    for(int j=0;j<p.M;++j){
      P+=c.momentum[j]*sn[j];Pt+=c.pt[j+1]*cs[j+1];
    }
    c.P[n]=P;c.Pt[n]=Pt;++s.fixed_angular_pairs_formed;
    if(!finiteq(P)||!finiteq(Pt)){
      ++s.fixed_nonfinite_angular_fallbacks;
      ++s.fixed_builds_completed;s.mark("fixed-nonfinite-angular-fallback",-1,n);
      return;
    }
  }
  c.qualified=true;++s.fixed_qualified_builds;++s.fixed_builds_completed;
  s.mark("fixed-complete-finite-words");
}

static bool r535_build_u_words(const Problem &p,const V &L,
    const V &momentum,V &words,R535WordStats &s){
  ++s.u_builds_started;s.mark("u-mode-build");
  words.resize(p.M);
  for(int j=0;j<p.M;++j){
    s.mark("u-mode-build",j);
    const Q m=p.frequency[j];
    // Preserve this complete parenthesized word before its original *sn[j].
    words[j]=-m*L[j+1]+(m*m-1)*momentum[j];
    ++s.u_mode_words_formed;
    if(!finiteq(m)||!finiteq(L[j+1])||!finiteq(momentum[j])||!finiteq(words[j])){
      ++s.u_nonfinite_mode_fallbacks;++s.u_builds_completed;
      s.mark("u-nonfinite-mode-fallback",j);return false;
    }
  }
  ++s.u_qualified_builds;++s.u_builds_completed;
  s.mark("u-complete-finite-words");return true;
}

static void r535_print_word_stats(std::ostream &o,const R535WordStats &s){
  o<<"{\"schema\":\"R535-native-root-local-finite-words-statistics-v1\""
   <<",\"fixed_requests\":"<<s.fixed_requests
   <<",\"fixed_builds_started\":"<<s.fixed_builds_started
   <<",\"fixed_builds_completed\":"<<s.fixed_builds_completed
   <<",\"fixed_qualified_builds\":"<<s.fixed_qualified_builds
   <<",\"fixed_nonfinite_mode_fallbacks\":"<<s.fixed_nonfinite_mode_fallbacks
   <<",\"fixed_nonfinite_angular_fallbacks\":"<<s.fixed_nonfinite_angular_fallbacks
   <<",\"fixed_mode_pairs_formed\":"<<s.fixed_mode_pairs_formed
   <<",\"fixed_angular_pairs_formed\":"<<s.fixed_angular_pairs_formed
   <<",\"fixed_evaluations_used\":"<<s.fixed_evaluations_used
   <<",\"fixed_evaluations_fallback\":"<<s.fixed_evaluations_fallback
   <<",\"fixed_evaluations_without_local_cache\":"<<s.fixed_evaluations_without_local_cache
   <<",\"u_builds_started\":"<<s.u_builds_started
   <<",\"u_builds_completed\":"<<s.u_builds_completed
   <<",\"u_qualified_builds\":"<<s.u_qualified_builds
   <<",\"u_nonfinite_mode_fallbacks\":"<<s.u_nonfinite_mode_fallbacks
   <<",\"u_mode_words_formed\":"<<s.u_mode_words_formed
   <<",\"u_angular_rows_used\":"<<s.u_angular_rows_used
   <<",\"u_angular_rows_fallback\":"<<s.u_angular_rows_fallback
   <<",\"last_present\":"<<(s.last_present?"true":"false")<<",\"last\":";
  if(!s.last_present){o<<"null";}else{
    o<<"{\"phase\":"<<quoted(s.last_phase)
     <<",\"mode_zero_based\":"<<(s.last_mode<0?"null":std::to_string(s.last_mode))
     <<",\"angle_zero_based\":"<<(s.last_angle<0?"null":std::to_string(s.last_angle))
     <<",\"fixed_words_used_in_evaluation\":"<<(s.last_fixed_used?"true":"false")
     <<",\"u_words_used_in_evaluation\":"<<(s.last_u_used?"true":"false")<<"}";
  }
  o<<",\"counter_scope\":\"actual-original-root-and-evaluation-calls\""
   <<",\"last_merge_order\":\"original-stage-index-order\""
   <<",\"complete_scientific_evaluation_not_inferred_from_counters\":true"
   <<",\"cross_root_state_or_geometry_cache\":false}";
}
#endif
