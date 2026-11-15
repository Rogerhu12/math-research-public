// Three independent components: declared cut forcing; complete 338x112 cut
// response; full original physical-query audit, all in binary128 arithmetic.
// Their successful execution is not the original worker/full-DN acceptance.
#include "geometry_20261115_native_physical128.hpp"
using namespace physical128;

static void common(std::ostream &s){
  s<<",\"native_accepted\":false,\"fullDN_accepted\":false"
   <<",\"state_cast_to_binary64\":false,\"new_acceptance_gate\":false"
   <<",\"literal_geometry_and_independent_tables_lifted_from_binary64\":true"
   <<",\"physical_radial_jet_formula\":\"original-C-based-finite-program-lifted-to-binary128\""
   <<",\"C_equals_F_e_claimed\":false,\"physical_Ldot_is_finite_root_trace_radial_derivative_claimed\":false"
   <<",\"physical_jets_are_continuous_ODE_certificates\":false"
   <<",\"IEEE_original_worker_bitwise_equivalence_claimed\":false";
}
static int forcing(const Problem &p,const PhysicalPacket &physical,const fs::path &out){
  fs::create_directories(out/"large-arrays");
  const Q r=physical.cut.g.r,r2=r*r,r4=r2*r2;V f(size_t(p.M)*p.M,0);
  for(int i=0;i<p.M;++i)f[size_t(i)*p.M+i]=1/r4;
  raw128(out/"large-arrays"/"cut-Q-per-height.f128",f);
  std::ostringstream s;s<<"{\"schema\":\"native-persistent128-local-height-forcing-v1\",\"complete\":true"
    <<",\"physical_height_extension\":\"saved_target+(H-saved_H)/binary128((r*r)*(r*r))\""
    <<",\"physical_H_IEEE_division_roundmap_derivative_claimed\":false"
    <<",\"input_saved_target_is_not_recomputed\":true"
    <<",\"cut_and_terminal_RK_geometry_words_equal\":"<<(physical.cut_terminal_geometry_words_equal?"true":"false")
    <<",\"cut_r4_binary128_decimal\":"<<quoted(qstr(r4))
    <<",\"original_binary64_r_pow4_literal_decimal\":"<<quoted(qstr(physical.original_r4_literal))
    <<",\"shape\":["<<p.M<<','<<p.M<<']';
  common(s);s<<'}';json_file(out/"summary.json",s.str());std::cout<<s.str()<<'\n';return 0;
}
static int endpoint(const Problem &p,const PhysicalPacket &physical,const fs::path &state_file,
    const fs::path &boundary,const fs::path &out){
  fs::create_directories(out/"large-arrays");const fs::path arrays=out/"large-arrays";
  const V states=read128(state_file,size_t(p.depth+1)*p.K);
  V node(p.K);for(int j=0;j<p.K;++j)node[j]=states[j];
  const V G=read128(boundary/"large-arrays"/"cut-Pi-graph-per-Q.f128",size_t(p.M)*p.M);
  const Policy policy{"original-stop",p.original_stop,p.original_fallback};
  const Geometry &g=physical.cut.g;const Q r2=g.r*g.r,r3=r2*g.r,r4=r2*r2;
  const int rows=3*p.M+2;V symmetric(size_t(rows)*p.M,nanq("")),J=symmetric;
  BatchStats stats;int columns=0,analytic_columns=0;bool base_complete=false;
  std::string error,base_scalars="null";
  std::ofstream trace(arrays/"cut-root-traces.jsonl",std::ios::binary|std::ios::trunc);
  if(!trace)throw std::runtime_error("cut-root-log-open");
  std::vector<std::string> column_records;
  try{
    auto base=cut_readout(p,physical,node,policy,stats,trace,0);base_complete=true;
    raw128(arrays/"cut-original-program-jets.f128",base.rows);
    raw128(arrays/"cut-C-based-Ldot.f128",base.jets.Ldot);
    std::ostringstream bs;
    bs<<"{\"radius\":"<<quoted(qstr(g.r))<<",\"backgroundSlope\":"<<quoted(qstr(g.w))
      <<",\"backgroundSecond\":"<<quoted(qstr(g.w*physical.cut.k/g.dr))
      <<",\"E\":"<<quoted(qstr(g.E))<<",\"Ep\":"<<quoted(qstr(2*g.w2*physical.cut.k/g.dr))
      <<",\"meanSlope\":"<<quoted(qstr(g.w+base.rows[2*p.M]))
      <<",\"meanSecond\":"<<quoted(qstr(g.w*physical.cut.k/g.dr+base.rows[2*p.M+1]))
      <<",\"minLeading\":"<<quoted(qstr(base.jets.minA))<<",\"minD\":"<<quoted(qstr(base.jets.minD))
      <<",\"endpointFullD\":"<<quoted(qstr(base.jets.maxDarboux))
      <<",\"endpointPhi\":"<<quoted(qstr(base.jets.holonomy))
      <<",\"formalCurvature\":"<<quoted(qstr(base.jets.curvature))
      <<",\"original_C_radial_solve_readback\":"<<quoted(qstr(base.jets.radial_solve_readback))<<"}";
    base_scalars=bs.str();
    V alternative_slope(p.M),slope_identity_difference(p.M);
    for(int j=0;j<p.M;++j){
      alternative_slope[j]=r4*base.field.primal.derivative[j]/g.dr+4*r3*node[j];
      slope_identity_difference[j]=alternative_slope[j]-base.rows[j];
    }
    raw128(arrays/"first-slope-RHS-identity-readback.f128",slope_identity_difference);
    const Q mean_identity=base.field.primal.derivative[p.K]/g.dr-base.rows[2*p.M];
    raw128(arrays/"mean-first-slope-RHS-identity-readback.f128",V{mean_identity});
    Q scale=physical.scale_floor;for(int j=0;j<p.M;++j)scale=qmax(scale,fabsq(node[j]));
    for(int col=0;col<p.M;++col){
      time_check();
      const Q h=physical.difference_step*qmax(fabsq(node[col]),physical.relative_step_floor*scale);
      if(!(h>0&&finiteq(h)))throw std::runtime_error("cut-difference-step");
      V plus=node,minus=node;plus[col]+=h;minus[col]-=h;
      for(int j=0;j<p.M;++j){plus[p.M+j]+=h*G[size_t(j)*p.M+col];minus[p.M+j]-=h*G[size_t(j)*p.M+col];}
      const auto a=cut_readout(p,physical,plus,policy,stats,trace,1+2*col);
      const auto b=cut_readout(p,physical,minus,policy,stats,trace,2+2*col);
      V pairrows(size_t(2)*rows);
      for(int row=0;row<rows;++row){
        pairrows[row]=a.rows[row];pairrows[rows+row]=b.rows[row];
        const Q v=(a.rows[row]-b.rows[row])/(2*h*r4);
        finite_direction(v,"complete-cut-symmetric-column");symmetric[size_t(row)*p.M+col]=v;J[size_t(row)*p.M+col]=v;
      }
      raw128(arrays/("cut-plus-minus-node-"+std::to_string(col)+".f128"),[&](){V v=plus;v.insert(v.end(),minus.begin(),minus.end());return v;}());
      raw128(arrays/("cut-plus-minus-jets-"+std::to_string(col)+".f128"),pairrows);
      ++columns;
      // Original analytic first-slope formula, with the actual finite-trace
      // root/RHS variation replacing the old implicit-root local matrix.
      V direction(p.size,0);direction[col]=1;
      for(int j=0;j<p.M;++j)direction[p.M+j]=physical.rho*G[size_t(j)*p.M+col];
      const V dy=rhs_direction(p,base.field,direction,p.cells[0],g,stats);
      for(int row=0;row<p.M;++row){
        J[size_t(row)*p.M+col]=dy[row]/g.dr+(row==col?4/g.r:0);
        finite_direction(J[size_t(row)*p.M+col],"first-slope-column");
      }
      J[size_t(2*p.M)*p.M+col]=dy[p.K]/(g.dr*r4);
      finite_direction(J[size_t(2*p.M)*p.M+col],"mean-first-slope-column");++analytic_columns;
      std::ostringstream c;
      c<<"{\"column\":"<<col<<",\"Q_difference_step_decimal\":"<<quoted(qstr(h))
        <<",\"Q_difference_step_binary128_hex\":"<<quoted(qhex(h))
        <<",\"symmetric_full338_returned\":true,\"matched_trace_first_slope_returned\":true}";
      column_records.push_back(c.str());
    }
  }catch(const std::exception &e){error=e.what();}
  trace.flush();
  raw128(arrays/"complete-symmetric-cut-J.f128",symmetric);
  raw128(arrays/"complete-mixed-cut-J.f128",J);
  raw128(arrays/"actual-cut-Pi-per-Q-graph.f128",G);
  const bool complete=base_complete&&columns==p.M&&analytic_columns==p.M&&error.empty();
  std::ostringstream s;s<<"{\"schema\":\"native-persistent128-endpoint338x112-readout-v1\",\"complete\":"<<(complete?"true":"false")
    <<",\"matrix_shape\":["<<rows<<','<<p.M<<"],\"symmetric_columns_completed\":"<<columns
    <<",\"finite_trace_first_slope_columns_completed\":"<<analytic_columns
    <<",\"unfinished_symmetric_column_suffix\":["<<columns<<','<<p.M<<']'
    <<",\"unfinished_first_slope_column_suffix\":["<<analytic_columns<<','<<p.M<<']'
    <<",\"rows\":[\"slope[112]\",\"second[112]\",\"meanSlopeCorrection\",\"meanSecondCorrection\",\"height[112]\"]"
    <<",\"first_slope_method\":\"finite-root-trace-RHS-variation-on-complete-current-Pi-per-Q-graph\""
    <<",\"second_and_mean_second_method\":\"original-symmetric-difference-of-C-based-physical-jet-program\""
    <<",\"all338rows_are_an_exact_analytic_Jacobian_claimed\":false"
    <<",\"original_difference_step_decimal\":"<<quoted(qstr(physical.difference_step))
    <<",\"physical_columns\":\"declared-local-cut-height-extension\""
    <<",\"cut_and_terminal_RK_geometry_words_equal\":"<<(physical.cut_terminal_geometry_words_equal?"true":"false")
    <<",\"cut_original_jet_scalars\":"<<base_scalars
    <<",\"endpoint_matrix_does_not_itself_pay_fullDN_or_fresh_audit\":true"
    <<",\"error\":"<<(error.empty()?"null":quoted(error))
    <<",\"resource_partial\":"<<(error=="explicit-experiment-time-budget"?"true":"false")
    <<",\"statistics\":";print_stats(s,stats);common(s);s<<",\"column_records\":[";
  for(size_t i=0;i<column_records.size();++i){if(i)s<<',';s<<column_records[i];}s<<"]}";
  json_file(out/"summary.json",s.str());std::cout<<s.str()<<'\n';return complete?0:2;
}
struct AuditStage {
  uint64_t queries=0,advances=0,active_query=0,active_advance=0,active_advance_count=0;
  bool complete=false;std::string error,phase="not-started";
  Q fullD=0,normalized=0,minA=FLT128_MAX,minD=FLT128_MAX,curvature=0,PV=0,
    metric=0,holonomy=0,radial_solve_readback=0;
  BatchStats stats;
};
static int audit(const Problem &p,const PhysicalPacket &physical,const fs::path &state_file,
    const fs::path &out,int threads){
  fs::create_directories(out/"large-arrays");const fs::path arrays=out/"large-arrays";
  const V states=read128(state_file,size_t(p.depth+1)*p.K);
  const Policy policy{"original-stop",p.original_stop,p.original_fallback};
  std::vector<AuditStage> stages(p.depth);
  #pragma omp parallel for schedule(dynamic,1) num_threads(threads)
  for(int n=0;n<p.depth;++n){
    auto &s=stages[n];
    try{
      time_check();const fs::path stage=arrays/("stage-"+std::to_string(n));fs::create_directory(stage);
      std::ofstream trace(stage/"root-traces.jsonl",std::ios::binary|std::ios::trunc),
        rows(stage/"query-scalars.jsonl",std::ios::binary|std::ios::trunc),
        angles(stage/"all-angle-jets.f128",std::ios::binary|std::ios::trunc),
        query_states(stage/"all-query-states.f128",std::ios::binary|std::ios::trunc);
      if(!trace||!rows||!angles||!query_states)throw std::runtime_error("audit-stage-output-open");
      V y(p.size,0);for(int j=0;j<p.K;++j)y[j]=states[size_t(n+1)*p.K+j];
      for(size_t qi=0;qi<physical.stages[n].size();++qi){
        time_check();const auto &q=physical.stages[n][qi];
        s.active_query=qi;s.active_advance=0;s.active_advance_count=q.advance.size();s.phase="physical-query";
        auto field=capture_field(p,y,p.cells[n],q.geometry.g,policy,s.stats,trace,n,qi,9);
        auto jets=physical_jets(p,physical,y,p.cells[n],q.geometry,field);
        const auto metric=physical_metric(q.geometry.g,jets,physical);
        s.fullD=qmax(s.fullD,jets.maxDarboux);s.minA=std::min(s.minA,jets.minA);s.minD=std::min(s.minD,jets.minD);
        s.curvature=qmax(s.curvature,jets.curvature);s.PV=qmax(s.PV,jets.peak_valley);
        s.metric=qmax(s.metric,metric.relative);s.holonomy=qmax(s.holonomy,fabsq(jets.holonomy));
        s.radial_solve_readback=qmax(s.radial_solve_readback,jets.radial_solve_readback);
        V full(size_t(p.N)*7);
        const auto &g=q.geometry.g;
        for(int j=0;j<p.N;++j){
          const auto &a=jets.angles[j];
          s.normalized=qmax(s.normalized,fabsq(a.darboux*g.E*g.E*g.r*g.dr/g.w2));
          const std::array<Q,7> v={a.ur,a.ut,a.urr,a.urt,a.utt,a.darboux,a.height};
          for(int k=0;k<7;++k)full[size_t(j)*7+k]=v[k];
        }
        if(!angles.write(reinterpret_cast<const char*>(full.data()),full.size()*sizeof(Q))||
           !query_states.write(reinterpret_cast<const char*>(y.data()),y.size()*sizeof(Q)))
          throw std::runtime_error("audit-complete-angle-state-write");
        rows<<"{\"query\":"<<qi<<",\"segment\":"<<q.segment<<",\"k\":"<<q.index
          <<",\"x_decimal\":"<<quoted(qstr(q.x))<<",\"fullD\":"<<quoted(qstr(jets.maxDarboux))
          <<",\"minA\":"<<quoted(qstr(jets.minA))<<",\"minD\":"<<quoted(qstr(jets.minD))
          <<",\"curvature\":"<<quoted(qstr(jets.curvature))<<",\"peakValley\":"<<quoted(qstr(jets.peak_valley))
          <<",\"physicalHolonomy\":"<<quoted(qstr(jets.holonomy))
          <<",\"actualMetricRelativeOperatorError\":"<<quoted(qstr(metric.relative))
          <<",\"actualMetricRR\":"<<quoted(qstr(metric.RR))<<",\"actualMetricRT\":"<<quoted(qstr(metric.RT))
          <<",\"actualMetricTT\":"<<quoted(qstr(metric.TT))<<",\"angularHolonomy\":"<<quoted(qstr(metric.holonomy))
          <<",\"translationPeriod\":"<<quoted(qstr(metric.translation))<<",\"radialGaugeMeanError\":"<<quoted(qstr(metric.gauge))
          <<",\"angularPhaseMeanDerivative\":"<<quoted(qstr(metric.phase_mean_derivative))
          <<",\"minProjectedDelta\":"<<quoted(qstr(metric.min_delta))
          <<",\"radialCurlCorrection\":"<<quoted(qstr(metric.curl_correction))
          <<",\"original_C_radial_solve_readback\":"<<quoted(qstr(jets.radial_solve_readback))<<"}\n";
        if(!rows)throw std::runtime_error("audit-query-scalar-write");++s.queries;s.phase="primal-advance";
        for(size_t k=0;k<q.advance.size();++k){
          BatchPair value{y,V{},0};
          y=rk4_batch(p,value,p.cells[n],q.advance[k],policy,s.stats,trace,n,qi*100000+k).value;
          ++s.advances;s.active_advance=k+1;
        }
      }
      trace.flush();rows.flush();angles.flush();query_states.flush();
      if(!trace||!rows||!angles||!query_states)throw std::runtime_error("audit-flush");
      s.complete=true;s.phase="completed";
    }catch(const std::exception &e){s.error=e.what();}
  }
  AuditStage total;size_t complete=0,total_queries=0,requested_queries=0;
  for(int n=0;n<p.depth;++n){
    const auto &s=stages[n];if(s.complete)++complete;total_queries+=s.queries;
    requested_queries+=physical.stages[n].size();total.stats.join(s.stats);
    total.fullD=qmax(total.fullD,s.fullD);total.normalized=qmax(total.normalized,s.normalized);
    total.minA=std::min(total.minA,s.minA);total.minD=std::min(total.minD,s.minD);
    total.curvature=qmax(total.curvature,s.curvature);total.PV=qmax(total.PV,s.PV);
    total.metric=qmax(total.metric,s.metric);total.holonomy=qmax(total.holonomy,s.holonomy);
    total.radial_solve_readback=qmax(total.radial_solve_readback,s.radial_solve_readback);
  }
  const bool done=complete==size_t(p.depth);
  std::ostringstream s;s<<"{\"schema\":\"native-persistent128-original-physical-program-audit-v1\",\"complete\":"<<(done?"true":"false")
    <<",\"stages_completed\":"<<complete<<",\"queries_completed\":"<<total_queries<<",\"queries_requested\":"<<requested_queries
    <<",\"audit_steps_per_profile\":"<<physical.audit_steps<<",\"threads\":"<<threads
    <<",\"all_angular_rows_saved\":"<<(done?"true":"false")<<",\"angle_jet_columns\":[\"ur\",\"ut\",\"urr\",\"urt\",\"utt\",\"Darboux\",\"height\"]"
    <<",\"fullD\":"<<quoted(qstr(total.fullD))<<",\"normalizedFullDefect\":"<<quoted(qstr(total.normalized))
    <<",\"minLeading\":"<<(total.minA==FLT128_MAX?"null":quoted(qstr(total.minA)))
    <<",\"minD\":"<<(total.minD==FLT128_MAX?"null":quoted(qstr(total.minD)))
    <<",\"formalCurvature\":"<<quoted(qstr(total.curvature))<<",\"maxPhysicalPV\":"<<quoted(qstr(total.PV))
    <<",\"actualMetric\":"<<quoted(qstr(total.metric))<<",\"holonomy\":"<<quoted(qstr(total.holonomy))
    <<",\"C_radial_solve_readback_max\":"<<quoted(qstr(total.radial_solve_readback))
    <<",\"extrema_are_partial_if_complete_false\":true"
    <<",\"independent_audit_replay_starts_at_each_actual_binary128_node\":true"
    <<",\"audit_query_schedule_and_cusp_advances_exported_from_original_live_configuration\":true"
    <<",\"state_dependent_development_transcendentals\":\"libquadmath-cosq-sinq\""
    <<",\"statistics\":";print_stats(s,total.stats);common(s);s<<",\"stages\":[";
  for(int n=0;n<p.depth;++n){
    if(n)s<<',';const auto &a=stages[n];
    s<<"{\"stage\":"<<n<<",\"complete\":"<<(a.complete?"true":"false")<<",\"queries_completed\":"<<a.queries
      <<",\"queries_requested\":"<<physical.stages[n].size()
      <<",\"unfinished_query_suffix\":["<<a.queries<<','<<physical.stages[n].size()<<']'
      <<",\"atomic_advances_completed\":"<<a.advances<<",\"active_phase\":"<<quoted(a.phase)
      <<",\"active_query\":"<<a.active_query<<",\"active_query_advance_completed\":"<<a.active_advance
      <<",\"active_query_advance_count\":"<<a.active_advance_count
      <<",\"error\":"<<(a.error.empty()?"null":quoted(a.error))<<"}";
  }
  s<<"]}";json_file(out/"summary.json",s.str());
  std::cout<<"{\"event\":\"physical128_audit_returned\",\"complete\":"<<(done?"true":"false")
    <<",\"queries_completed\":"<<total_queries<<",\"native_accepted\":false}\n";return done?0:2;
}
int main(int argc,char **argv){
  fs::path out;
  try{
    action_guard();
    if(argc<6)throw std::runtime_error(
      "forcing packet physical out seconds | endpoint packet physical state boundary out seconds | audit packet physical state out seconds threads");
    const std::string mode=argv[1];Problem p(argv[2]);PhysicalPacket physical(argv[3],p);
    int seconds=0;
    if(mode=="forcing"&&argc==6){out=argv[4];seconds=std::stoi(argv[5]);}
    else if(mode=="endpoint"&&argc==8){out=argv[6];seconds=std::stoi(argv[7]);}
    else if(mode=="audit"&&argc==8){out=argv[5];seconds=std::stoi(argv[6]);}
    else throw std::runtime_error("physical-component-CLI");
    if(seconds<1||seconds>20000||fs::exists(out))throw std::runtime_error("fresh-output-and-explicit-resource-required");
    deadline=Clock::now()+std::chrono::seconds(seconds);
    if(mode=="forcing")return forcing(p,physical,out);
    if(mode=="endpoint")return endpoint(p,physical,argv[4],argv[5],out);
    const int threads=std::stoi(argv[7]);if(threads<1||threads>64)throw std::runtime_error("audit-thread-bound");
    return audit(p,physical,argv[4],out,threads);
  }catch(const std::exception &e){
    const std::string record="{\"schema\":\"native-persistent128-physical-component-failure-v1\","
      "\"complete\":false,\"native_accepted\":false,\"error\":"+quoted(e.what())+"}";
    std::cerr<<record<<'\n';
    if(!out.empty()&&fs::is_directory(out))try{json_file(out/"failure.json",record);}catch(...){}
    return 2;
  }
}
