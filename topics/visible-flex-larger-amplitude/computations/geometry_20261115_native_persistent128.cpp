// Persistent binary128 shooting state, with a labelled frozen64 chord model.
// The launcher generates this include from the complete frozen R283 source:
// only its standalone main is excluded, with the exact prefix SHA recorded.
// Original113 and R283 numerical function bodies are not edited.
#include "native_frozen_trace_variation128.inc"
#include <filesystem>
#include <cstring>

namespace persistent128 {
namespace fs = std::filesystem;
using namespace trace_variation;
static const char *schema="native-persistent128-original-stop-chord-state-v1";
struct OwnedEvaluation : Evaluation { std::string evaluation_error; };
static OwnedEvaluation value_evaluation(const Problem&p,Q alpha,const Policy&policy,int threads,V&stage_output){
  OwnedEvaluation out;
  try{evaluate_full(p,alpha,policy,threads,stage_output,out);}
  catch(const std::exception &error){
    // This is the original native trial caller's exception scope. Keep any
    // already computed rows/outputs and let the next original alpha run;
    // no fictitious failing stage is assigned to a global norm error.
    out.evaluation_error=error.what();out.complete=false;
    if(out.evaluation_error=="explicit-experiment-time-budget")out.budget=true;
  }
  return out;
}

static void text_file(const fs::path &file,const std::string &body){
  std::ofstream out(file,std::ios::binary|std::ios::trunc);
  if(!out||!out.write(body.data(),body.size())||!out.flush())
    throw std::runtime_error("persistent128-metadata-write");
}
static void event(const std::string &body){ std::cout<<body<<std::endl; }
static std::string qr(Q q){
  return std::string("{\"decimal\":")+quoted(qstr(q))+",\"binary128_hex\":"+quoted(qhex(q))+"}";
}
static bool equal_words(const V&a,const V&b){
  return a.size()==b.size()&&std::memcmp(a.data(),b.data(),a.size()*sizeof(Q))==0;
}
static V read_q(const fs::path &file,size_t count){
  if(fs::file_size(file)!=count*sizeof(Q))throw std::runtime_error("persistent128-state-byte-count");
  V v(count);std::ifstream f(file,std::ios::binary);
  if(!f.read(reinterpret_cast<char*>(v.data()),count*sizeof(Q)))throw std::runtime_error("persistent128-state-read");
  for(Q q:v)finite(q,"persistent128-state-input");return v;
}
static std::vector<double> read_d(const fs::path &file,size_t count){
  if(fs::file_size(file)!=count*sizeof(double))throw std::runtime_error("persistent128-z-byte-count");
  std::vector<double> v(count);std::ifstream f(file,std::ios::binary);
  if(!f.read(reinterpret_cast<char*>(v.data()),count*sizeof(double)))throw std::runtime_error("persistent128-z-read");
  for(double q:v)if(!std::isfinite(q))throw std::runtime_error("persistent128-nonfinite-z");return v;
}
static std::string norm_row(const Problem&p,size_t row,Q r){
  const size_t n=sigma_index(p,row);std::ostringstream o;
  o<<"{\"global_row\":"<<row<<",\"sigma_index\":"<<n<<",\"sigma\":"<<qr(p.scales[n]);
  if(row<size_t(p.M))o<<",\"kind\":\"cut\",\"node\":0,\"mode_one_based\":"<<row+1;
  else if(row>=size_t(p.M)+size_t(p.depth)*p.K)
    o<<",\"kind\":\"far\",\"node\":"<<p.depth<<",\"mode_one_based\":"<<row-p.M-size_t(p.depth)*p.K+1;
  else{
    const size_t c=(row-p.M)%p.K;
    o<<",\"kind\":\"stage\",\"stage\":"<<n<<",\"input_node\":"<<n+1<<",\"output_node\":"<<n
     <<",\"component\":"<<quoted(c<size_t(p.M)?"Q":"Pi")<<",\"mode_one_based\":"<<c%p.M+1;
  }
  o<<",\"residual\":"<<qr(r)<<",\"normalized_signed\":"<<qr(r/p.scales[n])<<"}";return o.str();
}
static std::string ev_record(const Problem&p,const OwnedEvaluation&e){
  std::ostringstream o;o<<"{\"complete\":"<<(e.complete?"true":"false")
   <<",\"budget_exhausted\":"<<(e.budget?"true":"false")<<",\"stages_completed\":"<<e.stages_completed
   <<",\"rows_completed\":"<<e.rows_completed<<",\"expected_rows\":"<<size_t(p.depth+1)*p.K
   <<",\"norm\":"<<(e.complete?qr(e.norm):"null")
   <<",\"below_original_tolerance\":"<<(e.complete?(e.norm<p.outer_tol?"true":"false"):"null")
   <<",\"mean_height_sum\":"<<(e.complete?qr(e.mean_total):"null")
   <<",\"evaluation_error\":"<<(e.evaluation_error.empty()?"null":quoted(e.evaluation_error))<<",\"worst_row\":";
  if(e.complete)o<<norm_row(p,e.worst,e.residual[e.worst]);else o<<"null";
  o<<",\"root_statistics\":";print_root_stats(o,e.stats);o<<",\"failed_stages\":[";bool comma=false;
  for(size_t n=0;n<e.errors.size();++n)if(!e.errors[n].empty()){
    if(comma)o<<',';comma=true;o<<"{\"stage\":"<<n<<",\"error\":"<<quoted(e.errors[n])<<"}";
  }o<<"]}";return o.str();
}
static void await_command(const char *expected){
  std::string line;if(!std::getline(std::cin,line))throw std::runtime_error("persistent128-owner-protocol-EOF");
  if(line!=expected)throw std::runtime_error("persistent128-owner-protocol-unexpected-command:"+line);
}
static std::string form_rhs64(const Problem&p,const V&r,const fs::path&file){
  std::vector<double>d(r.size());Q maximum=0;size_t changed=0,underflow=0,worst=0;
  for(size_t i=0;i<r.size();++i){
    d[i]=static_cast<double>(r[i]);if(!std::isfinite(d[i]))throw std::runtime_error("persistent128-rhs64-overflow");
    const Q error=static_cast<Q>(d[i])-r[i],scaled=fabsq(error)/p.scales[sigma_index(p,i)];
    if(error!=0)++changed;if(r[i]!=0&&d[i]==0)++underflow;
    if(scaled>maximum){maximum=scaled;worst=i;}
  }
  std::ofstream f(file,std::ios::binary|std::ios::trunc);
  if(!f.write(reinterpret_cast<const char*>(d.data()),d.size()*sizeof(double)))throw std::runtime_error("persistent128-rhs64-write");
  std::ostringstream o;o<<"{\"operation\":\"one RN binary128-to-binary64 cast for approximate QR only\",\"changed_entries\":"
   <<changed<<",\"nonzero_to_zero\":"<<underflow<<",\"max_original_sigma_scaled_conversion_error\":"<<qr(maximum)
   <<",\"worst_conversion_row\":"<<worst<<",\"original_r128_not_replaced\":true}";return o.str();
}
static std::string recover_direction(Problem&p,const fs::path&directory){
  auto z=read_d(directory/"scaled-z.f64",p.base.size());
  auto rounded=read_d(directory/"original-R273-rounded-delta.f64",p.base.size());
  Q maximum=0,scale_norm=0;size_t changed=0,nonzero_recovered=0,worst=0;
  for(size_t i=0;i<p.base.size();++i){
    // Both operands originate as literal binary64.  Their product is formed
    // in binary128 here, rather than taking the already-rounded delta64.
    p.delta[i]=p.scales[i/p.K]*static_cast<Q>(z[i]);finite(p.delta[i],"persistent128-recovery");
    const Q error=p.delta[i]-static_cast<Q>(rounded[i]);
    if(error!=0)++changed;if(p.delta[i]!=0&&rounded[i]==0)++nonzero_recovered;
    const Q v=fabsq(error)/p.scales[i/p.K];if(v>maximum){maximum=v;worst=i;}
    scale_norm=qmax(scale_norm,fabsq(static_cast<Q>(z[i])));
  }
  write_raw((directory/"chosen-direction.f128").string(),p.delta);
  std::ostringstream o;o<<"{\"coordinates\":\"delta128[node,j] = lifted original sigma[node] times lifted solved z64[node,j]\","
   <<"\"complete_nodes\":577,\"complete_columns\":224,\"cut_far_projection\":false,\"state_roundtrip_through_binary64\":false,"
   <<"\"different_from_R273_delta64_entries\":"<<changed<<",\"nonzero128_from_zero64_recovery_entries\":"<<nonzero_recovered
   <<",\"maximum_scaled_recovery_difference\":"<<qr(maximum)<<",\"worst_recovery_difference_index\":"<<worst
   <<",\"scaled_z_infinity_norm\":"<<qr(scale_norm)<<"}";return o.str();
}
static std::string trace_record(const Problem&p,const JointEvaluation&t,const Evaluation&base){
  std::ostringstream o;o<<"{\"complete\":"<<(t.complete?"true":"false")<<",\"budget_exhausted\":"<<(t.budget?"true":"false")
   <<",\"rows_completed\":"<<t.rows_completed<<",\"stages_completed\":"<<t.stages_completed
   <<",\"primal_exact_words_match_current_residual\":"<<(t.complete?(equal_words(t.residual,base.residual)?"true":"false"):"null")
   <<",\"finite_trace_real_expression_variation\":true,\"IEEE_roundmap_derivative_claimed\":false,\"C_equals_F_e_assumed\":false,"
   <<"\"preconditioner_is_this_derivative\":false,\"direction_rejected_by_affine_diagnostic\":false,\"root_statistics\":";
  print_root_stats(o,t.root);o<<",\"variation_statistics\":";print_variation_stats(o,t.variation);
  o<<",\"primal_norm\":"<<(t.complete?qr(t.norm):"null")<<",\"action_norm\":"<<(t.complete?qr(t.action_norm):"null")
   <<",\"unit_affine_norm\":"<<(t.complete?qr(t.affine_norm):"null")<<",\"all_ten_affine_diagnostics\":[";
  if(t.complete)for(int k=0;k<10;++k){
    Q alpha=scalbnq(Q(1),-k),norm=0;size_t worst=0;
    for(size_t row=0;row<t.residual.size();++row){
      const Q v=fabsq(t.residual[row]+alpha*t.action[row])/p.scales[sigma_index(p,row)];
      finite_direction(v,"persistent128-affine-readback");if(v>norm){norm=v;worst=row;}
    }
    if(k)o<<',';o<<"{\"trial\":"<<k<<",\"alpha\":"<<qr(alpha)<<",\"norm\":"<<qr(norm)
     <<",\"worst_row\":"<<worst<<",\"strict_linear_decrease\":"<<(norm<base.norm?"true":"false")<<"}";
  }
  o<<"],\"failed_stages\":[";bool comma=false;
  for(size_t n=0;n<t.errors.size();++n)if(!t.errors[n].empty()){
    if(comma)o<<',';comma=true;o<<"{\"stage\":"<<n<<",\"error\":"<<quoted(t.errors[n])<<"}";
  }o<<"],\"scalar_readback_error\":"<<(t.readback_error.empty()?"null":quoted(t.readback_error))<<"}";return o.str();
}

static int solve(Problem&p,const fs::path&out,const Policy&policy,int threads,bool trace_each){
  const size_t dimension=p.base.size();int accepted=0,directions=0,trials=0;std::string reason="not-started";
  std::vector<int> requested_directions;std::vector<std::pair<int,int>> attempted_trials;
  V current_stage_output;OwnedEvaluation current=value_evaluation(p,0,policy,threads,current_stage_output);
  event(std::string("{\"event\":\"persistent128_initial\",\"evaluation\":")+ev_record(p,current)+"}");
  if(!current.complete)reason=current.budget?"resource-partial-initial":"initial-primal-failure";
  else for(int it=0;it<32;++it){
    if(current.norm<p.outer_tol){reason="shooting-tolerance-reached";break;}
    if(Clock::now()>=deadline){reason="resource-partial-before-direction";break;}
    char name[32];std::snprintf(name,sizeof(name),"iteration-%03d",it);const fs::path dir=out/name;
    if(!fs::create_directory(dir))throw std::runtime_error("persistent128-iteration-directory-exists");
    write_raw((dir/"current-state.f128").string(),p.base);write_raw((dir/"current-residual.f128").string(),current.residual);
    write_raw((dir/"current-stage-full-output.f128").string(),current_stage_output);
    const std::string conversion=form_rhs64(p,current.residual,dir/"rhs-for-R273.f64");
    const std::string request=std::string("{\"event\":\"persistent128_need_direction\",\"iteration\":")+std::to_string(it)+
     ",\"directory\":"+quoted(name)+",\"current\":"+ev_record(p,current)+",\"rhs_conversion\":"+conversion+
     ",\"state_encoding\":\"IEEE754-binary128-little-endian\",\"state_owner_retains_original_128_words\":true}";
    requested_directions.push_back(it);text_file(dir/"direction-request.json",request);event(request);
    std::string reply;if(!std::getline(std::cin,reply))throw std::runtime_error("persistent128-direction-protocol-EOF");
    if(reply=="STOP_RESOURCE"){reason="resource-partial-current-QR";break;}
    if(reply=="STOP_LINEAR_FAILED"){reason="current-approximate-QR-failed";break;}
    if(reply!="DIRECTION_READY")throw std::runtime_error("persistent128-direction-protocol-unexpected-command:"+reply);
    const std::string recovery=recover_direction(p,dir);++directions;
    event(std::string("{\"event\":\"persistent128_direction_lifted\",\"iteration\":")+std::to_string(it)+",\"recovery\":"+recovery+"}");
    if(trace_each){
      const fs::path trace_dir=dir/"matched-trace";fs::create_directory(trace_dir);
      JointEvaluation t=evaluate_direction(p,0,policy,threads,trace_dir.string());
      write_raw((trace_dir/"current-state.f128").string(),t.states);write_raw((trace_dir/"input-direction.f128").string(),p.delta);
      write_raw((trace_dir/"residual.f128").string(),t.residual);write_raw((trace_dir/"action.f128").string(),t.action);
      write_raw((trace_dir/"stage-full-output.f128").string(),t.stage_output);write_raw((trace_dir/"stage-full-direction.f128").string(),t.stage_direction);
      const std::string record=trace_record(p,t,current);text_file(trace_dir/"summary.json",record);
      event(std::string("{\"event\":\"persistent128_matched_trace\",\"iteration\":")+std::to_string(it)+",\"directory\":"+quoted(name)+",\"report\":"+record+"}");
      await_command("TRACE_RECORDED");
      if(t.budget){reason="resource-partial-matched-trace";break;}
      // Failure of a variation is not a new nonlinear acceptance test. The
      // original primal trials may proceed, with the missing JVP explicit.
      if(t.complete&&!equal_words(t.residual,current.residual)){
        reason="finite-trace-primal-word-identity-failure";break;
      }
    }
    bool took=false,resource=false;
    for(int k=0;k<10;++k){
      attempted_trials.emplace_back(it,k);
      const Q alpha=scalbnq(Q(1),-k);V candidate(dimension);size_t changed=0,below64=0;
      for(size_t i=0;i<dimension;++i){
        candidate[i]=p.base[i]+alpha*p.delta[i];
        if(std::memcmp(&candidate[i],&p.base[i],sizeof(Q))!=0){++changed;
          if(static_cast<double>(candidate[i])==static_cast<double>(p.base[i]))++below64;}
      }
      const auto begin=Clock::now();V trial_stage_output;OwnedEvaluation trial=value_evaluation(p,alpha,policy,threads,trial_stage_output);++trials;
      const bool decrease=trial.complete&&trial.norm<current.norm;
      char tname[32];std::snprintf(tname,sizeof(tname),"trial-%02d",k);const fs::path trial_dir=dir/tname;fs::create_directory(trial_dir);
      write_raw((trial_dir/"actual-trial-state.f128").string(),candidate);write_raw((trial_dir/"actual-trial-residual.f128").string(),trial.residual);
      write_raw((trial_dir/"actual-trial-stage-full-output.f128").string(),trial_stage_output);
      std::ostringstream o;o<<"{\"event\":\"persistent128_trial\",\"iteration\":"<<it<<",\"trial\":"<<k
       <<",\"directory\":"<<quoted((fs::path(name)/tname).string())<<",\"alpha\":"<<qr(alpha)<<",\"base_norm\":"<<qr(current.norm)
       <<",\"evaluation\":"<<ev_record(p,trial)<<",\"accepted\":"<<(decrease?"true":"false")
       <<",\"reason\":"<<quoted(trial.budget?"resource-partial":!trial.complete?"original-primal-failure":decrease?"strict-original-norm-decrease":"residual-not-decreasing")
       <<",\"changed128_state_words\":"<<changed<<",\"changed128_with_same64_cast_values\":"<<below64
       <<",\"elapsed_seconds\":"<<std::setprecision(17)<<std::chrono::duration<double>(Clock::now()-begin).count()<<"}";
      text_file(trial_dir/"summary.json",o.str());event(o.str());await_command("TRIAL_RECORDED");
      if(trial.budget){resource=true;reason="resource-partial-trial";break;}
      if(decrease){p.base=std::move(candidate);current=std::move(trial);current_stage_output=std::move(trial_stage_output);++accepted;took=true;break;}
    }
    event(std::string("{\"event\":\"persistent128_iteration_closed\",\"iteration\":")+std::to_string(it)+
      ",\"directory\":"+quoted(name)+",\"accepted\":"+(took?"true":"false")+",\"current\":"+ev_record(p,current)+"}");
    await_command("ITERATION_RECORDED");
    if(resource)break;if(!took){reason="complete-ten-trial-line-search-failure";break;}
    reason=current.norm<p.outer_tol?"shooting-tolerance-reached":"original-32-direction-budget";
  }
  write_raw((out/"final-state.f128").string(),p.base);write_raw((out/"final-residual.f128").string(),current.residual);
  write_raw((out/"final-stage-full-output.f128").string(),current_stage_output);
  std::ostringstream final;final<<"{\"event\":\"persistent128_owner_final\",\"schema\":"<<quoted(schema)
   <<",\"stop_reason\":"<<quoted(reason)<<",\"directions_computed\":"<<directions<<",\"trial_evaluations\":"<<trials
   <<",\"accepted_steps\":"<<accepted<<",\"final\":"<<ev_record(p,current)
   <<",\"root_stop\":"<<qr(policy.stop)<<",\"root_fallback\":"<<qr(policy.fallback)<<",\"outer_tolerance\":"<<qr(p.outer_tol)
   <<",\"original32_by10_bounds\":true,\"persistent_binary128_state\":true,\"state_roundtrip_through_binary64\":false,"
   <<"\"direction_model\":\"fixed fresh64 J chord matrix and current128 RHS with explicit QR conversion\","
   <<"\"fixed64_J_is_current128_derivative\":false,\"finite_trace_JVP_is_nonlinear_acceptance_gate\":false,"
   <<"\"native_accepted\":false,\"fullDN_completed\":false,\"endpoint338_by112_sensitivity_complete\":false,"
   <<"\"original_geometric_final_audit_complete\":false,\"requested_direction_indices\":[";
  for(size_t i=0;i<requested_directions.size();++i){if(i)final<<',';final<<requested_directions[i];}
  final<<"],\"attempted_trial_addresses\":[";
  for(size_t i=0;i<attempted_trials.size();++i){if(i)final<<',';final<<'['<<attempted_trials[i].first<<','<<attempted_trials[i].second<<']';}
  final<<"],\"unvisited_direction_indices\":[";bool comma=false;
  for(int it=0;it<32;++it)if(std::find(requested_directions.begin(),requested_directions.end(),it)==requested_directions.end()){
    if(comma)final<<',';comma=true;final<<it;
  }
  final<<"],\"unvisited_trials_in_last_requested_direction\":[";comma=false;
  if(!requested_directions.empty())for(int k=0;k<10;++k){
    const auto address=std::make_pair(requested_directions.back(),k);
    if(std::find(attempted_trials.begin(),attempted_trials.end(),address)==attempted_trials.end()){
      if(comma)final<<',';comma=true;final<<k;
    }
  }
  final<<"],\"unvisited_suffix_scope\":\"not evaluated; preceding acceptance, mathematical stop, or explicit wall limit as separately recorded\","
   <<"\"no_deleted128_state_resume_claimed\":true}";
  text_file(out/"owner-summary.json",final.str());event(final.str());
  return reason=="shooting-tolerance-reached"?0:reason.find("resource-partial")==0?3:4;
}
static int replay(Problem&p,const fs::path&out,const fs::path&state,const Policy&policy,int threads){
  p.base=read_q(state,p.base.size());std::fill(p.delta.begin(),p.delta.end(),Q(0));
  V stage_output;OwnedEvaluation e=value_evaluation(p,0,policy,threads,stage_output);write_raw((out/"independent-residual.f128").string(),e.residual);
  write_raw((out/"independent-stage-full-output.f128").string(),stage_output);
  const std::string row=std::string("{\"event\":\"persistent128_independent_fresh_replay\",\"scope\":")+
   quoted("all original cut/stage/far rows and both complete mean accumulators, independent process; not geometric audit")+
   ",\"evaluation\":"+ev_record(p,e)+",\"input_state_not_converted_to_binary64\":true,\"native_accepted\":false}";
  text_file(out/"summary.json",row);event(row);return e.complete?0:e.budget?3:2;
}
static int column(Problem&p,const fs::path&out,const fs::path&state,int column,const Policy&policy,int threads){
  if(column<0||column>=p.K)throw std::runtime_error("complete-stage-column-index");
  p.base=read_q(state,p.base.size());std::fill(p.delta.begin(),p.delta.end(),Q(0));
  // Every independent stage receives the same basis column at its own
  // node n+1. The saved full stage direction is before output subtraction
  // and before port; it is the actual 226-by224 local map column.
  for(int n=1;n<=p.depth;++n)p.delta[size_t(n)*p.K+column]=1;
  JointEvaluation t=evaluate_direction(p,0,policy,threads,out.string());
  write_raw((out/"stage-full-column-before-port.f128").string(),t.stage_direction);
  write_raw((out/"primal-residual.f128").string(),t.residual);
  V shape(size_t(p.depth)*p.K),means(size_t(p.depth)*2);
  for(int n=0;n<p.depth;++n){
    for(int j=0;j<p.K;++j){Q v=t.stage_direction[size_t(n)*p.size+j];shape[size_t(n)*p.K+j]=j<p.M?v:v/p.cells[n].ratio;}
    means[2*n]=t.stage_direction[size_t(n)*p.size+p.K];means[2*n+1]=t.stage_direction[size_t(n)*p.size+p.K+1];
  }
  write_raw((out/"stage-shape-column-after-port.f128").string(),shape);write_raw((out/"stage-mean-column.f128").string(),means);
  std::ostringstream o;o<<"{\"event\":\"persistent128_final_stage_column\",\"column\":"<<column
   <<",\"complete\":"<<(t.complete?"true":"false")<<",\"budget_exhausted\":"<<(t.budget?"true":"false")
   <<",\"stages_completed\":"<<t.stages_completed<<",\"rows_completed\":"<<t.rows_completed
   <<",\"root_statistics\":";print_root_stats(o,t.root);o<<",\"variation_statistics\":";print_variation_stats(o,t.variation);
  o<<",\"boundary_row_action_not_substituted_for_local_map_column\":true,\"all_two_mean_rows_retained\":true,"
   <<"\"endpoint_sensitivity_complete\":false,\"native_accepted\":false}";
  text_file(out/"summary.json",o.str());event(o.str());return t.complete?0:t.budget?3:2;
}
} // namespace persistent128

int main(int argc,char **argv){
  using namespace persistent128;
  try{
    const char *ga=std::getenv("GITHUB_ACTIONS"),*repo=std::getenv("GITHUB_REPOSITORY");
    if(!ga||std::string(ga)!="true"||!repo||std::string(repo)!="Rogerhu12/math-research-public")throw std::runtime_error("public-Actions-only");
    if(argc<7)throw std::runtime_error("packet mode out seconds threads option [state]");
    uint16_t little=1;if(*reinterpret_cast<unsigned char*>(&little)!=1||sizeof(Q)!=16||FLT128_MANT_DIG!=113)
      throw std::runtime_error("actual-little-endian-binary128-required");
    if(std::fesetround(FE_TONEAREST)!=0)throw std::runtime_error("round-to-nearest-mode-unavailable");
    const int seconds=std::stoi(argv[4]),threads=std::stoi(argv[5]);
    if(seconds<1||seconds>21600||threads<1||threads>4)throw std::runtime_error("explicit-resource-parameters");
    deadline=Clock::now()+std::chrono::seconds(seconds);Problem p(argv[1]);const fs::path out=argv[3];
    if(!fs::is_directory(out))throw std::runtime_error("existing-owned-output-directory-required");
    Policy policy{"original-stop-literal64-lifted-to128",p.original_stop,p.original_fallback};
    const std::string mode=argv[2];
    if(mode=="solve"&&argc==7)return solve(p,out,policy,threads,std::string(argv[6])=="trace-each-direction");
    if(mode=="replay"&&argc==8)return replay(p,out,argv[7],policy,threads);
    if(mode=="stage-column"&&argc==8)return column(p,out,argv[7],std::stoi(argv[6]),policy,threads);
    throw std::runtime_error("explicit-persistent128-mode-required");
  }catch(const std::exception&e){
    event(std::string("{\"event\":\"persistent128_owner_error\",\"error\":")+quoted(e.what())+",\"native_accepted\":false}");
    return std::string(e.what()).find("explicit-experiment-time-budget")!=std::string::npos?3:2;
  }
}
