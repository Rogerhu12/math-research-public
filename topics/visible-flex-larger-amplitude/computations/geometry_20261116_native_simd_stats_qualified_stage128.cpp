// Full SIMD-exact-dyadic recorded-coefficient stage columns at an explicitly supplied persistent128
// state.  This executable supplies no endpoint or physical-audit acceptance.
#include "geometry_20261115_native_simd_digit_operator_trace128.hpp"
using namespace simd_digit_trace128;
using BatchStats=simd_digit_trace128::BatchStats;
using BatchPair=shared_trace128::BatchPair;

int main(int argc,char **argv){
  fs::path out;
  try{
    action_guard();
    if(argc!=11)throw std::runtime_error(
      "usage: packet current-state.f128 out seconds threads first-stage stages first-column columns reference-columns-or-none");
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
    std::vector<int> reference_columns;
    const std::string reference_argument=argv[10];
    if(reference_argument!="none"){
      std::istringstream input(reference_argument);std::string item;
      while(std::getline(input,item,',')){
        if(item.empty()||item.find_first_not_of("0123456789")!=std::string::npos)
          throw std::runtime_error("explicit-reference-column-format");
        const int column=std::stoi(item);
        if(column<first_column||column>=first_column+columns||
           std::find(reference_columns.begin(),reference_columns.end(),column-first_column)!=reference_columns.end())
          throw std::runtime_error("reference-column-not-in-requested-range-or-duplicate");
        reference_columns.push_back(column-first_column);
      }
      if(reference_columns.empty())throw std::runtime_error("empty-reference-column-list");
    }
    simd_digit_trace128::BatchStats literal_stats;const auto literal_started=Clock::now();
    const LiteralBases basis(p,literal_stats);
    const double literal_basis_elapsed_seconds=
      std::chrono::duration<double>(Clock::now()-literal_started).count();
    std::ostringstream literal_record;basis.identity(literal_record,literal_stats);
    json_file(out/"literal-bases-identity.json",literal_record.str());
    std::vector<simd_digit_trace128::BatchStats> stats(p.depth);
    for(auto &s:stats){s.requested_reference_columns=reference_columns;s.first_requested_state_column=first_column;}
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
          y=simd_digit_trace128::rk4_batch(p,y,p.cells[n],p.cells[n].steps[k],policy,basis,stats[n],trace,n,k);
          step_count[n]=k+1;
        }
        trace.flush();if(!trace)throw std::runtime_error("root-trace-flush");
        V shape(size_t(p.K)*columns),means(size_t(2)*columns),residual(p.K);
        for(int j=0;j<p.K;++j){
          const Q value=j<p.M?y.value[j]:y.value[j]/p.cells[n].ratio;
          residual[j]=value-p.base[size_t(n)*p.K+j];finite(residual[j],"stage-residual");
          for(int col=0;col<columns;++col){
            const Q v=y.direction[size_t(j)*columns+col];
            shape[size_t(j)*columns+col]=j<p.M?v:simd_digit_trace128::post_port_direction(y.value[j],v,p.cells[n].ratio,0);
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
    size_t done=0;simd_digit_trace128::BatchStats total;total.join(literal_stats);
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
    report<<"{\"schema\":\"native-persistent128-complete-simd-dyadic-recorded-stage-maps-v1\""
      <<",\"complete_requested_range\":"<<(done==size_t(count)?"true":"false")
      <<",\"complete_576_stage_primal\":"<<(full_primal?"true":"false")
      <<",\"complete_224_stage_columns\":"<<(full_J?"true":"false")
      <<",\"modes\":"<<p.M<<",\"depth\":"<<p.depth<<",\"shape_dimension\":"<<p.K
      <<",\"complete_state_dimension\":"<<p.size<<",\"columns_requested\":"<<columns
      <<",\"first_column\":"<<first_column<<",\"first_stage\":"<<first_stage
      <<",\"stages_requested\":"<<count<<",\"stages_completed\":"<<done
      <<",\"original_root_policy\":"<< ::quoted(policy.label)
      <<",\"root_stop_decimal\":"<< ::quoted(qstr(policy.stop))
      <<",\"root_fallback_decimal\":"<< ::quoted(qstr(policy.fallback))
      <<",\"state_received_as_binary128\":true,\"state_cast_to_binary64\":false"
      <<",\"primal_branch_search_once_per_field\":true,\"primal_Cholesky_shared_across_columns\":true"
      <<",\"F_C_value_shadows_replayed_per_column\":false,\"C_is_assumed_F_e\":false"
      <<",\"fixed_recorded_coefficient_real_operator\":true,\"accurate_finite_root_derivative_certified\":false,\"derivative_of_IEEE_roundmap_claimed\":false"
      <<",\"branch_stability_proved\":false,\"new_RHS_profile_or_literal_tables\":false"
      <<",\"cached_angular_partial_operator\":true,\"literal_gram_C_layout_retained_in_preassembly\":true"
      <<",\"independent_preassembled_state_column_implementation\":true"
      <<",\"frozen_R305_primitive_and_reduction_order_preserved\":false"
      <<",\"whole_stage_bitwise_comparison_independently_run\":false"
      <<",\"shared_six_partial_value_program\":true,\"state_angle_actions_replaced_by_full_recorded_maps\":true"
      <<",\"ideal_trigonometric_product_identities_substituted\":false"
      <<",\"invN_multiplication_reassociated\":true"
      <<",\"general_geometry_batches_use_original_R305_fallback\":true"
      <<",\"factor_and_triangular_loop_direction_arithmetic_changed\":true"
      <<",\"recorded_coefficient_nominal_factor_real_equivalence_only\":true,\"old_C_exact_inverse_assumed\":false,\"integer_digit_matmul_implemented\":true,\"old_dL_graph_word_equality_claimed\":false"
      <<",\"nominal_factor_residual_derivatives_proved_zero\":false,\"direction_error_bound_supplied\":false"
      <<",\"geometry_parameter_interface_implemented\":true,\"this_stage_request_geometry_directions_are_zero\":true"
      <<",\"complete_mean_and_port_direction_included\":true"
      <<",\"optional_reference_columns_global_argument\":"<< ::quoted(reference_argument)
      <<",\"optional_reference_scope\":\"same field/tape/current supplied tangent; not independently propagated old whole-stage map\""
      <<",\"unrequested_columns_are_not_zero_columns\":true"
      <<",\"complete_dyadic_dot_then_once_RN113\":true"
      <<",\"full_significand_exponent_and_subnormal_bits_retained\":true"
      <<",\"wide_exponent_fallback_same_exact_dot_contract\":true"
      <<",\"each_fast_integer_reduction_has_at_most_2048_terms\":true"
      <<",\"fixed_six_limb_quantization_used\":false"
      <<",\"literal_basis_elapsed_seconds\":"<<std::setprecision(17)<<literal_basis_elapsed_seconds
      <<",\"literal_basis_identity_file\":\"literal-bases-identity.json\""
      <<",\"all_state_columns_batched_per_field\":"<<columns
      <<",\"small_recorded_H_coefficients_reassociated_relative_to190\":true"
      <<",\"factor_direction_triangular_primitives_unchanged_from190\":true"
      <<",\"old190_word_equality_claimed\":false"
      <<",\"native_accepted\":false,\"endpoint338x112_supplied\":false,\"physical_audit_supplied\":false"
      <<",\"new_acceptance_gate\":false,\"seconds_budget\":"<<seconds<<",\"threads\":"<<threads
      <<",\"budget_exhausted\":"<<(budget?"true":"false")
      <<",\"elapsed_seconds\":"<<std::setprecision(17)<<std::chrono::duration<double>(Clock::now()-started).count()
      <<",\"primal_norm_decimal\":"<<(full_primal&&norm_error.empty()? ::quoted(qstr(norm)):"null")
      <<",\"primal_norm_binary128_hex\":"<<(full_primal&&norm_error.empty()? ::quoted(qhex(norm)):"null")
      <<",\"primal_worst_row\":"<<(full_primal&&norm_error.empty()?std::to_string(worst):"null")
      <<",\"norm_readback_error\":"<<(norm_error.empty()?"null": ::quoted(norm_error))
      <<",\"statistics\":";simd_digit_trace128::print_stats(report,total);
    report<<",\"stages\":[";
    for(int n=0;n<p.depth;++n){
      if(n)report<<',';
      report<<"{\"stage\":"<<n<<",\"input_node\":"<<n+1<<",\"output_node\":"<<n
        <<",\"requested\":"<<(n>=first_stage&&n<first_stage+count?"true":"false")
        <<",\"completed\":"<<(complete[n]?"true":"false")
        <<",\"atomic_steps_total\":"<<p.cells[n].steps.size()<<",\"atomic_steps_completed\":"<<step_count[n]
        <<",\"unfinished_step_suffix\":["<<step_count[n]<<','<<p.cells[n].steps.size()<<']'
        <<",\"error\":"<<(errors[n].empty()?"null": ::quoted(errors[n]))<<",\"statistics\":";
      simd_digit_trace128::print_stats(report,stats[n]);report<<'}';
    }
    report<<"]}";
    json_file(out/"summary.json",report.str());
    // The launcher emits a bounded scalar view; complete stage provenance
    // remains temporary and is included in its path/size/SHA manifest.
    std::cout<<"{\"event\":\"operator_stage128_complete\",\"summary\":\"summary.json\","
      <<"\"requested_complete\":"<<(done==size_t(count)?"true":"false")
      <<",\"all224columns\":"<<(full_J?"true":"false")<<",\"native_accepted\":false}\n";
    return done==size_t(count)&&norm_error.empty()?0:2;
  }catch(const std::exception &e){
    const std::string record="{\"schema\":\"native-persistent128-complete-simd-dyadic-recorded-stage-maps-v1\","
      "\"complete_requested_range\":false,\"native_accepted\":false,\"error\":"+ ::quoted(e.what())+"}";
    std::cerr<<record<<'\n';
    if(!out.empty()&&fs::is_directory(out))try{json_file(out/"failure.json",record);}catch(...){}
    return 2;
  }
}
