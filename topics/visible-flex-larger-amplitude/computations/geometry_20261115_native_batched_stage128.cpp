// Full finite-trace stage columns at an explicitly supplied persistent128
// state.  This executable supplies no endpoint or physical-audit acceptance.
#include "geometry_20261115_native_shared_trace128.hpp"
using namespace shared_trace128;

int main(int argc,char **argv){
  fs::path out;
  try{
    action_guard();
    if(argc!=10)throw std::runtime_error(
      "usage: packet current-state.f128 out seconds threads first-stage stages first-column columns");
    const int seconds=std::stoi(argv[4]),threads=std::stoi(argv[5]),
      first_stage=std::stoi(argv[6]),count=std::stoi(argv[7]),
      first_column=std::stoi(argv[8]),columns=std::stoi(argv[9]);
    if(seconds<1||seconds>20000||threads<1||threads>64)
      throw std::runtime_error("explicit-resource-bounds");
    deadline=Clock::now()+std::chrono::seconds(seconds);
    const auto started=Clock::now();Problem p(argv[1]);
    p.base=read128(argv[2],size_t(p.depth+1)*p.K);
    if(first_stage<0||count<1||first_stage+count>p.depth||
       first_column<0||columns<1||first_column+columns>p.K)
      throw std::runtime_error("explicit-column-stage-range");
    out=argv[3];
    if(fs::exists(out))throw std::runtime_error("fresh-output-required");
    fs::create_directories(out/"large-arrays");
    const Policy policy{"original-stop",p.original_stop,p.original_fallback};
    std::vector<BatchStats> stats(p.depth);
    std::vector<std::string> errors(p.depth,"not-requested");
    std::vector<unsigned char> complete(p.depth,0);
    std::vector<size_t> step_count(p.depth,0);
    // A stage payload is written only after every requested column and every
    // original atomic RK step in that stage has returned.  Incomplete stages
    // retain their primal root log and explicit progress, not fabricated J.
    #pragma omp parallel for schedule(dynamic,1) num_threads(threads)
    for(int n=first_stage;n<first_stage+count;++n){
      errors[n].clear();
      try{
        time_check();const fs::path dir=out/"large-arrays"/("stage-"+std::to_string(n));
        fs::create_directory(dir);
        std::ofstream trace(dir/"root-trace.jsonl",std::ios::binary|std::ios::trunc);
        if(!trace)throw std::runtime_error("root-trace-open");
        BatchPair y{V(p.size,0),V(size_t(p.size)*columns,0),columns};
        for(int j=0;j<p.K;++j)y.value[j]=p.base[size_t(n+1)*p.K+j];
        for(int col=0;col<columns;++col)y.direction[size_t(first_column+col)*columns+col]=1;
        for(size_t k=0;k<p.cells[n].steps.size();++k){
          y=rk4_batch(p,y,p.cells[n],p.cells[n].steps[k],policy,stats[n],trace,n,k);
          step_count[n]=k+1;
        }
        trace.flush();if(!trace)throw std::runtime_error("root-trace-flush");
        V shape(size_t(p.K)*columns),means(size_t(2)*columns),residual(p.K);
        for(int j=0;j<p.K;++j){
          const Q value=j<p.M?y.value[j]:y.value[j]/p.cells[n].ratio;
          residual[j]=value-p.base[size_t(n)*p.K+j];finite(residual[j],"stage-residual");
          for(int col=0;col<columns;++col){
            const Q v=y.direction[size_t(j)*columns+col];
            shape[size_t(j)*columns+col]=j<p.M?v:v/p.cells[n].ratio;
            finite_direction(shape[size_t(j)*columns+col],"post-port-stage-column");
          }
        }
        for(int j=0;j<2;++j)for(int col=0;col<columns;++col)
          means[size_t(j)*columns+col]=y.direction[size_t(p.K+j)*columns+col];
        raw128(dir/"primal-full-output.f128",y.value);
        raw128(dir/"full-columns-before-port.f128",y.direction);
        raw128(dir/"shape-columns-after-port.f128",shape);
        raw128(dir/"mean-columns.f128",means);
        raw128(dir/"stage-residual.f128",residual);
        complete[n]=1;
      }catch(const std::exception &e){errors[n]=e.what();}
    }
    V residual(size_t(p.depth+1)*p.K,nanq(""));
    for(int j=0;j<p.M;++j){
      residual[j]=p.base[j]-p.target[j];
      const size_t q=size_t(p.depth)*p.K+j,row=p.M+size_t(p.depth)*p.K+j;
      residual[row]=p.base[q+p.M]-p.far[j]*p.base[q];
    }
    size_t done=0;BatchStats total;
    bool budget=false;
    for(int n=0;n<p.depth;++n){
      total.join(stats[n]);if(errors[n]=="explicit-experiment-time-budget")budget=true;
      if(complete[n]){
        ++done;const V r=read128(out/"large-arrays"/("stage-"+std::to_string(n))/"stage-residual.f128",p.K);
        for(int j=0;j<p.K;++j)residual[p.M+size_t(n)*p.K+j]=r[j];
      }
    }
    raw128(out/"large-arrays"/"primal-residual.f128",residual);
    const bool full_primal=done==size_t(p.depth);
    const bool full_J=full_primal&&first_column==0&&columns==p.K;
    Q norm=0;size_t worst=0;std::string norm_error;
    if(full_primal)try{
      for(size_t row=0;row<residual.size();++row){
        const Q v=fabsq(residual[row])/p.scales[sigma_index(p,row)];
        finite(v,"normalized-primal-residual");if(v>norm){norm=v;worst=row;}
      }
    }catch(const std::exception &e){norm_error=e.what();}
    std::ostringstream report;
    report<<"{\"schema\":\"native-persistent128-batched-finite-trace-stage-maps-v1\""
      <<",\"complete_requested_range\":"<<(done==size_t(count)?"true":"false")
      <<",\"complete_576_stage_primal\":"<<(full_primal?"true":"false")
      <<",\"complete_224_stage_columns\":"<<(full_J?"true":"false")
      <<",\"modes\":"<<p.M<<",\"depth\":"<<p.depth<<",\"shape_dimension\":"<<p.K
      <<",\"complete_state_dimension\":"<<p.size<<",\"columns_requested\":"<<columns
      <<",\"first_column\":"<<first_column<<",\"first_stage\":"<<first_stage
      <<",\"stages_requested\":"<<count<<",\"stages_completed\":"<<done
      <<",\"original_root_policy\":"<<quoted(policy.label)
      <<",\"root_stop_decimal\":"<<quoted(qstr(policy.stop))
      <<",\"root_fallback_decimal\":"<<quoted(qstr(policy.fallback))
      <<",\"state_received_as_binary128\":true,\"state_cast_to_binary64\":false"
      <<",\"primal_branch_search_once_per_field\":true,\"primal_Cholesky_shared_across_columns\":true"
      <<",\"F_C_value_shadows_replayed_per_column\":true,\"C_is_assumed_F_e\":false"
      <<",\"fixed_trace_real_expression_variation\":true,\"derivative_of_IEEE_roundmap_claimed\":false"
      <<",\"branch_stability_proved\":false,\"new_RHS_profile_or_literal_tables\":false"
      <<",\"unrequested_columns_are_not_zero_columns\":true"
      <<",\"native_accepted\":false,\"endpoint338x112_supplied\":false,\"physical_audit_supplied\":false"
      <<",\"new_acceptance_gate\":false,\"seconds_budget\":"<<seconds<<",\"threads\":"<<threads
      <<",\"budget_exhausted\":"<<(budget?"true":"false")
      <<",\"elapsed_seconds\":"<<std::setprecision(17)<<std::chrono::duration<double>(Clock::now()-started).count()
      <<",\"primal_norm_decimal\":"<<(full_primal&&norm_error.empty()?quoted(qstr(norm)):"null")
      <<",\"primal_norm_binary128_hex\":"<<(full_primal&&norm_error.empty()?quoted(qhex(norm)):"null")
      <<",\"primal_worst_row\":"<<(full_primal&&norm_error.empty()?std::to_string(worst):"null")
      <<",\"norm_readback_error\":"<<(norm_error.empty()?"null":quoted(norm_error))
      <<",\"statistics\":";print_stats(report,total);
    report<<",\"stages\":[";
    for(int n=0;n<p.depth;++n){
      if(n)report<<',';
      report<<"{\"stage\":"<<n<<",\"input_node\":"<<n+1<<",\"output_node\":"<<n
        <<",\"requested\":"<<(n>=first_stage&&n<first_stage+count?"true":"false")
        <<",\"completed\":"<<(complete[n]?"true":"false")
        <<",\"atomic_steps_total\":"<<p.cells[n].steps.size()<<",\"atomic_steps_completed\":"<<step_count[n]
        <<",\"unfinished_step_suffix\":["<<step_count[n]<<','<<p.cells[n].steps.size()<<']'
        <<",\"error\":"<<(errors[n].empty()?"null":quoted(errors[n]))<<",\"statistics\":";
      print_stats(report,stats[n]);report<<'}';
    }
    report<<"]}";
    json_file(out/"summary.json",report.str());
    // The launcher emits a bounded scalar view; complete stage provenance
    // remains temporary and is included in its path/size/SHA manifest.
    std::cout<<"{\"event\":\"batched_stage128_complete\",\"summary\":\"summary.json\","
      <<"\"requested_complete\":"<<(done==size_t(count)?"true":"false")
      <<",\"all224columns\":"<<(full_J?"true":"false")<<",\"native_accepted\":false}\n";
    return done==size_t(count)&&norm_error.empty()?0:2;
  }catch(const std::exception &e){
    const std::string record="{\"schema\":\"native-persistent128-batched-finite-trace-stage-maps-v1\","
      "\"complete_requested_range\":false,\"native_accepted\":false,\"error\":"+quoted(e.what())+"}";
    std::cerr<<record<<'\n';
    if(!out.empty()&&fs::is_directory(out))try{json_file(out/"failure.json",record);}catch(...){}
    return 2;
  }
}
