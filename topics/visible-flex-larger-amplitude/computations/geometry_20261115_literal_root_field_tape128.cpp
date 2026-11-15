// Independent temporary R314 evidence exporter. Never imported into request140.
// The two recorded direction functions below retain the R305 arithmetic text;
// their only extra operations write already formed values after the solve.
#include "geometry_20261115_native_operator_trace128.hpp"
using namespace operator_trace128;
using BatchStats=operator_trace128::BatchStats;
using BatchPair=shared_trace128::BatchPair;

static V recorded_L_direction(const Problem &p,const PreparedField &field,
    const InputDirection &input,const Geometry &g,const EnvironmentDirection &env,
    BatchStats &stats, const fs::path &column){
  V de(p.J,0);const Q invN=1/static_cast<Q>(p.N);
  for(size_t update=0;update<field.original.root.updates.size();++update){
    time_check();const auto &u=field.original.root.updates[update];
    const auto &rows=field.updates[update];V dL(p.J),dF(p.J,0),beta(2*p.M+1,0);
    for(int j=0;j<p.J;++j)dL[j]=input.target[j]+de[j];
    for(int n=0;n<p.N;++n){
      if((n&31)==0)time_check();
      const std::array<Q,6> x={input.P[n],input.Pt[n],angular_L_direction(p,dL,n),0,env.g.w2,env.g.E};
      const Q dq=apply_local(rows[n].quad,x),dc=apply_local(rows[n].rho,x),
        *cs=p.cosine.data()+size_t(n)*p.J,*gram=p.gram.data()+size_t(n)*(2*p.M+1);
      for(int j=0;j<p.J;++j)dF[j]+=dq*cs[j]*invN;
      for(int k=0;k<=2*p.M;++k)beta[k]+=dc*gram[k]*invN;
    }
    for(int j=0;j<p.J;++j)dF[j]+=de[j];
    const V action=structured_C_action(p,beta,u.solve.out);++stats.structured_C_products;
    V right(p.J);for(int j=0;j<p.J;++j)right[j]=dF[j]-action[j];
    const V ds=factor_direction_solve(u.solve,right,p.J);++stats.shared_factor_direction_solves;
    for(int i=0;i<p.J;++i){
      Q residual=0;for(int j=0;j<p.J;++j)residual+=u.C[size_t(i)*p.J+j]*ds[j];residual-=right[i];
      finite_direction(residual,"complete-C-direction-readback");
      stats.direction_C_solve_residual_max=qmax(stats.direction_C_solve_residual_max,fabsq(residual));
      ++stats.complete_C_linear_residual_rows;
    }
    const fs::path step=column/("update-"+std::to_string(update));
    fs::create_directory(step);
    raw128(step/"target-direction.f128",input.target);
    raw128(step/"incoming-e-direction.f128",de);
    raw128(step/"formed-F-direction.f128",dF);
    raw128(step/"formed-C-beta-direction.f128",beta);
    raw128(step/"formed-C-action.f128",action);
    raw128(step/"formed-direction-rhs.f128",right);
    raw128(step/"nominal-solve-direction.f128",ds);
    const Q alpha=scalbnq(1,-u.backtrack);
    for(int j=0;j<p.J;++j){de[j]=de[j]-alpha*ds[j];finite_direction(de[j],"operator-accepted-e-direction");}
    ++stats.accepted_operator_updates;
  }
  V result(p.J);for(int j=0;j<p.J;++j){result[j]=input.target[j]+de[j];finite_direction(result[j],"operator-returned-L-direction");}
  raw128(column/"returned-L-direction.f128",result);
  ++stats.root_operator_returns;
  // At a returned root only angular quantities are needed by RHS. The old
  // final complete dF reduction is not an output or an update input here.
  ++stats.final_unused_F_derivative_reductions_skipped;return result;
}
static V recorded_rhs_direction(const Problem &p,const PreparedField &field,
    const V &direction,const Cell &cell,const Geometry &g,
    const EnvironmentDirection &env,BatchStats &stats, const fs::path &column){
  const auto &root=field.original.root;const auto &primal=field.original.primal;
  const auto input=input_direction(p,root,direction,cell,g,env,stats);
  const V dL=recorded_L_direction(p,field,input,g,env,stats,column);
  const Q invN=1/static_cast<Q>(p.N);V dflux(p.M,0);
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();const Q *sn=p.sine.data()+size_t(n)*p.M;
    Q dU=0;for(int j=0;j<p.M;++j){const Q m=p.frequency[j];dU+=(-m*dL[j+1]+(m*m-1)*input.momentum[j])*sn[j];}
    const std::array<Q,6> x={input.P[n],input.Pt[n],angular_L_direction(p,dL,n),dU,env.g.w2,env.g.E};
    const Q value=apply_local(field.final_rows[n].flux,x);
    for(int j=0;j<p.M;++j)dflux[j]+=value*sn[j]*invN;
  }
  const D r(g.r,env.g.r),dr(g.dr,env.g.dr),w(g.w,env.g.w),w2(g.w2,env.g.w2),mu(cell.mu,env.mu),
    r3=r*r*r,sigma=dr/r,pref=static_cast<Q>(p.orientation)*p.sq2*r3*dr*w2/(p.sq12*mu);
  DV result(p.size,D(0));
  for(int j=0;j<p.M;++j){
    const Q m=p.frequency[j];const D y(root.state[j],direction[j]),pi(root.state[p.M+j],direction[p.M+j]),
      L(root.returned.L[j+1],dL[j+1]),pj=-m*r3*y/(p.sq2*w),linear=-m*L+(m*m-1)*pj;
    result[j]=sigma*((m*m-4)*y+p.sq2*w*L/r3);
    result[p.M+j]=4*sigma*pi+pref*m*(linear+D(primal.flux[j],dflux[j]));
  }
  result[p.K]=dr*w*D(root.returned.L[0],dL[0]);result[p.K+1]=dr*w;
  V out(p.size);
  for(int j=0;j<p.size;++j){
    same_value(result[j].v,primal.derivative[j],stats.variation,"operator-complete-RHS-value");
    finite_direction(result[j].d,"operator-complete-RHS-direction");out[j]=result[j].d;
  }
  return out;
}

static void copy_file_exact(const fs::path &a,const fs::path &b){
  fs::copy_file(a,b,fs::copy_options::none);
}
static FieldTape select_field(const Problem &p,const V &current,int stage,
    size_t wanted_step,int wanted_field,const Policy &policy,BatchStats &stats,
    std::ostream &trace){
  const Cell &cell=p.cells[stage];
  V y(p.size,0);for(int j=0;j<p.K;++j)y[j]=current[size_t(stage+1)*p.K+j];
  for(size_t k=0;k<=wanted_step;++k){
    time_check();const Step &s=cell.steps[k];V t(p.size);
    auto a=shared_trace128::capture_field(p,y,cell,s.g[0],policy,stats,trace,stage,k,0);
    if(k==wanted_step&&wanted_field==0)return a;
    for(int j=0;j<p.size;++j)t[j]=y[j]+s.h*a.primal.derivative[j]/2;
    auto b=shared_trace128::capture_field(p,t,cell,s.g[1],policy,stats,trace,stage,k,1);
    if(k==wanted_step&&wanted_field==1)return b;
    for(int j=0;j<p.size;++j)t[j]=y[j]+s.h*b.primal.derivative[j]/2;
    auto c=shared_trace128::capture_field(p,t,cell,s.g[1],policy,stats,trace,stage,k,2);
    if(k==wanted_step&&wanted_field==2)return c;
    for(int j=0;j<p.size;++j)t[j]=y[j]+s.h*c.primal.derivative[j];
    auto d=shared_trace128::capture_field(p,t,cell,s.g[2],policy,stats,trace,stage,k,3);
    if(k==wanted_step&&wanted_field==3)return d;
    for(int j=0;j<p.size;++j){
      y[j]=y[j]+s.h*(a.primal.derivative[j]+2*b.primal.derivative[j]+
                    2*c.primal.derivative[j]+d.primal.derivative[j])/6;
      finite(y[j],"selected-field-prefix-state");
    }
  }
  throw std::runtime_error("unreachable-selected-field");
}
int main(int argc,char **argv){
  fs::path out;bool tape_ready=false;int columns_ready=0,columns=0;
  int stage=-1,field=-1;size_t rk_step=0,updates=0;std::string error;
  std::string policy_name;bool fallback=false;const auto started=Clock::now();
  try{
    action_guard();
    if(!std::getenv("GITHUB_REPOSITORY")||
       std::string(std::getenv("GITHUB_REPOSITORY"))!="Rogerhu12/math-research-public")
      throw std::runtime_error("public-repository-only");
    if(argc!=10)throw std::runtime_error(
      "usage: packet current-state.f128 out seconds stage RK-step field original|refined state224|state224-plus-environment6");
    const int seconds=std::stoi(argv[4]);
    stage=std::stoi(argv[5]);rk_step=std::stoull(argv[6]);field=std::stoi(argv[7]);
    if(seconds<1||seconds>20000)throw std::runtime_error("explicit-export-budget");
    deadline=Clock::now()+std::chrono::seconds(seconds);
    Problem p(argv[1]);const V current=read128(argv[2],size_t(p.depth+1)*p.K);
    if(stage<0||stage>=p.depth||rk_step>=p.cells[stage].steps.size()||field<0||field>3)
      throw std::runtime_error("actual-stage-step-field-required");
    Policy policy;policy_name=argv[8];
    if(policy_name=="original")policy={"original-stop",p.original_stop,p.original_fallback};
    else if(policy_name=="refined")policy={"refined-stop",strtoflt128("1e-28",nullptr),strtoflt128("5e-27",nullptr)};
    else throw std::runtime_error("explicit-original-or-refined");
    const std::string mode=argv[9];
    if(mode=="state224")columns=224;
    else if(mode=="state224-plus-environment6")columns=230;
    else throw std::runtime_error("explicit-complete-column-family");
    out=argv[3];if(fs::exists(out))throw std::runtime_error("fresh-output-required");
    fs::create_directories(out/"large-arrays");
    std::ofstream trace(out/"root-trace.jsonl",std::ios::binary|std::ios::trunc);
    if(!trace)throw std::runtime_error("root-trace-open");
    BatchStats stats;
    auto original=select_field(p,current,stage,rk_step,field,policy,stats,trace);
    const auto &cell=p.cells[stage];
    const Geometry &g=cell.steps[rk_step].g[field==0?0:field==3?2:1];
    auto prepared=prepare_field(p,std::move(original),g,stats,trace,stage,rk_step,field);
    const fs::path arrays=out/"large-arrays";
    raw128(arrays/"frequency.f128",p.frequency);
    raw128(arrays/"cosine.f128",p.cosine);
    raw128(arrays/"sine.f128",p.sine);
    raw128(arrays/"independent-gram225.f128",p.gram);
    raw128(arrays/"constants.f128",{p.sq2,p.sq12,p.floor,p.outer_tol,p.original_stop,
      p.original_fallback,static_cast<Q>(p.orientation),g.r,g.dr,g.w,g.w2,g.E,
      cell.mu,cell.ratio,cell.steps[rk_step].h,policy.stop,policy.fallback});
    const auto &root=prepared.original.root;
    raw128(arrays/"field-input226.f128",root.state);
    raw128(arrays/"nominal-target113.f128",root.target);
    raw128(arrays/"nominal-final-e113.f128",root.final_e);
    raw128(arrays/"nominal-returned-L113.f128",root.returned.L);
    raw128(arrays/"nominal-returned-F113.f128",root.returned.evaluated.residual);
    raw128(arrays/"nominal-RHS226.f128",prepared.original.primal.derivative);
    raw128(arrays/"nominal-flux112.f128",prepared.original.primal.flux);
    updates=root.updates.size();fallback=root.fallback;
    std::ostringstream update_table;update_table<<'[';
    for(size_t k=0;k<updates;++k){
      const auto &u=root.updates[k];const fs::path d=arrays/("update-"+std::to_string(k));
      fs::create_directory(d);raw128(d/"e113.f128",u.e);
      raw128(d/"formed-F113.f128",u.evaluated.residual);raw128(d/"formed-C113x113.f128",u.C);
      raw128(d/"nominal-factor113x113.f128",u.solve.L);
      raw128(d/"nominal-forward113.f128",u.solve.tmp);raw128(d/"nominal-solve113.f128",u.solve.out);
      if(k)update_table<<',';update_table<<"{\"update\":"<<k<<",\"backtrack\":"<<u.backtrack<<'}';
    }
    update_table<<']';
    json_file(out/"tape.json","{\"schema\":\"literal-root-field-tape-v1\",\"stage\":"+std::to_string(stage)+
      ",\"RK_step\":"+std::to_string(rk_step)+",\"field\":"+std::to_string(field)+
      ",\"modes\":112,\"root_dimension\":113,\"state_dimension\":226,\"shape_dimension\":224,\"angles\":"+
      std::to_string(p.N)+",\"columns_requested\":"+std::to_string(columns)+
      ",\"original_policy\":"+quoted(policy_name)+",\"fallback\":"+(fallback?"true":"false")+
      ",\"updates\":"+update_table.str()+",\"field_input_is_actual_binary128_prefix_state\":true,"
      "\"field_input_uncertainty_from_earlier_RK_certified\":false,"
      "\"root_branch_selection_differentiated\":false,"
      "\"geometry_coordinates_independent\":true,\"C_is_assumed_F_e\":false}");
    tape_ready=true;
    for(int col=0;col<columns;++col){
      time_check();const fs::path d=arrays/("column-"+std::to_string(col));
      fs::create_directory(d);V seed(p.size,0);EnvironmentDirection env;
      if(col<p.K)seed[col]=1;
      else if(col==224)env.g.r=1;
      else if(col==225)env.g.dr=1;
      else if(col==226)env.g.w=1;
      else if(col==227)env.g.w2=1;
      else if(col==228)env.g.E=1;
      else if(col==229)env.mu=1;
      raw128(d/"input-seed226.f128",seed);
      raw128(d/"environment-seed6.f128",{env.g.r,env.g.dr,env.g.w,env.g.w2,env.g.E,env.mu});
      const V rhs=recorded_rhs_direction(p,prepared,seed,cell,g,env,stats,d);
      raw128(d/"nominal-RHS-direction226.f128",rhs);
      json_file(d/"complete.json","{\"column\":"+std::to_string(col)+",\"complete\":true}");
      ++columns_ready;
      std::cout<<"R314_FIELD_EXPORT {\"event\":\"column_returned\",\"column\":"<<col
               <<",\"rows\":226,\"native_accepted\":false}"<<std::endl;
    }
    trace.flush();if(!trace)throw std::runtime_error("root-trace-flush");
  }catch(const std::exception &e){error=e.what();}
  const bool complete=tape_ready&&columns>0&&columns_ready==columns;
  const bool budget=error=="explicit-experiment-time-budget";
  std::ostringstream report;
  report<<"{\"schema\":\"literal-root-field-export-result-v1\",\"complete\":"<<(complete?"true":"false")
    <<",\"tape_ready\":"<<(tape_ready?"true":"false")<<",\"stage\":"<<stage
    <<",\"RK_step\":"<<rk_step<<",\"field\":"<<field<<",\"updates\":"<<updates
    <<",\"columns_requested\":"<<columns<<",\"columns_completed\":"<<columns_ready
    <<",\"unvisited_column_suffix\":["<<columns_ready<<','<<columns<<']'
    <<",\"state_rows\":226,\"root_rows\":113,\"independent_gram_rows\":225"
    <<",\"elapsed_seconds\":"<<std::chrono::duration<double>(Clock::now()-started).count()
    <<",\"budget_exhausted\":"<<(budget?"true":"false")
    <<",\"error\":"<<(error.empty()?"null":quoted(error))
    <<",\"native_accepted\":false,\"complete_RK_stage_certified\":false"
    <<",\"complete_boundary112_response\":false,\"physical_audit_completed\":false}";
  if(!out.empty()&&fs::is_directory(out))json_file(out/"export-result.json",report.str());
  std::cout<<"R314_FIELD_EXPORT "<<report.str()<<std::endl;
  return complete?0:budget?3:2;
}
