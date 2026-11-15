// Independent R305 implementation of the exact-real successful root trace.
// The primal and all literal tables are supplied by the frozen R302 header.
// Its derivative arithmetic is deliberately a NEW implementation: cached
// angular partials and C^{-1}(dF-dC*s), using the actual nominal factor.
// No derivative of IEEE rounding, bitwise equality with the old dL graph,
// or bound for that graph's residual derivatives is claimed.
#ifndef VISIBLE_NATIVE_OPERATOR_TRACE128_HPP
#define VISIBLE_NATIVE_OPERATOR_TRACE128_HPP
#include "geometry_20261115_native_shared_trace128.hpp"

namespace operator_trace128 {
using namespace shared_trace128;
using shared_trace128::BatchPair;

// The five geometry packet words are independent coordinates here. A caller
// differentiating a profile must supply its own true chain rule; in particular
// w2 and E are NOT silently replaced by formulas in w. Literal frequency,
// cosine, sine, gram, sqrt constants, and orientation have zero directions.
struct EnvironmentDirection {
  Geometry g{0,0,0,0,0};
  Q mu=0;
};
struct StepDirections {
  V h;
  std::array<std::vector<EnvironmentDirection>,3> environment;
};
struct BatchStats : shared_trace128::BatchStats {
  uint64_t local_partial_rows=0, local_partial_basis_evaluations=0,
    structured_C_products=0, shared_factor_direction_solves=0,
    root_operator_returns=0, accepted_operator_updates=0,
    complete_C_linear_residual_rows=0, reference_field_columns=0,
    reference_field_failures=0, reference_field_not_applicable=0,
    final_unused_F_derivative_reductions_skipped=0;
  Q nominal_factor_residual_max=0, nominal_forward_residual_max=0,
    nominal_backward_residual_max=0, nominal_C_step_residual_max=0,
    direction_C_solve_residual_max=0, reference_field_difference_max=0;
  std::vector<int> requested_reference_columns;
  int first_requested_state_column=0;
  void join(const BatchStats &b){
    shared_trace128::BatchStats::join(b);
    local_partial_rows+=b.local_partial_rows;
    local_partial_basis_evaluations+=b.local_partial_basis_evaluations;
    structured_C_products+=b.structured_C_products;
    shared_factor_direction_solves+=b.shared_factor_direction_solves;
    root_operator_returns+=b.root_operator_returns;
    accepted_operator_updates+=b.accepted_operator_updates;
    complete_C_linear_residual_rows+=b.complete_C_linear_residual_rows;
    reference_field_columns+=b.reference_field_columns;
    reference_field_failures+=b.reference_field_failures;
    reference_field_not_applicable+=b.reference_field_not_applicable;
    final_unused_F_derivative_reductions_skipped+=b.final_unused_F_derivative_reductions_skipped;
    nominal_factor_residual_max=qmax(nominal_factor_residual_max,b.nominal_factor_residual_max);
    nominal_forward_residual_max=qmax(nominal_forward_residual_max,b.nominal_forward_residual_max);
    nominal_backward_residual_max=qmax(nominal_backward_residual_max,b.nominal_backward_residual_max);
    nominal_C_step_residual_max=qmax(nominal_C_step_residual_max,b.nominal_C_step_residual_max);
    direction_C_solve_residual_max=qmax(direction_C_solve_residual_max,b.direction_C_solve_residual_max);
    reference_field_difference_max=qmax(reference_field_difference_max,b.reference_field_difference_max);
  }
};

// Coordinates of one angular expression: P, Pt, L, U, w2, E. These
// coefficients are prepared once per actually used primal root evaluation,
// not once per direction column. Five geometry words and mu subsequently
// enter the original momentum/target/prefactor formulas explicitly.
struct PointOperator {
  std::array<Q,6> quad{},rho{},flux{};
  Q rho_value=0,flux_value=0;
};
static PointOperator prepare_point(const Angular &original,const Geometry &g,
    BatchStats &stats){
  PointOperator result;
  for(int axis=0;axis<6;++axis){
    const D P(original.P,axis==0?1:0),Pt(original.Pt,axis==1?1:0),
      Lv(original.L,axis==2?1:0),U(original.U,axis==3?1:0),
      w2(g.w2,axis==4?1:0),E(g.E,axis==5?1:0);
    const D K=Lv-Pt,T=2*K+K*K+E*P*P,u=w2*T,
      DD=1-u,S=1-w2*P*P,A=1+Lv+w2*Pt;
    const D sd=dsqrt(DD),fc=u*(2+sd)/(2*sd*(1+sd)*(1+sd)),
      gc=w2*(P*P+S*T/(1+sd))/(S*sd),
      quad=(K*K+E*P*P)/2+K*Pt+T*fc+(1+K)*Pt*gc;
    const D am=Lv+w2*Pt,
      dm=u*(sd+1/(1+sd))/(DD*sd),rho=am+(1+am)*dm,
      factor=(K+u/(1+sd)+w2*P*P*sd)/(S*sd),flux=U*factor;
    if(axis==0){
      same_value(K.v,original.K,stats.variation,"operator-K");
      same_value(S.v,original.S,stats.variation,"operator-S");
      same_value(DD.v,original.D,stats.variation,"operator-D");
      same_value(A.v,original.A,stats.variation,"operator-A");
      same_value(sd.v,original.sd,stats.variation,"operator-sqrt-D");
      same_value(quad.v,original.quad,stats.variation,"operator-quad");
      result.rho_value=rho.v;result.flux_value=flux.v;
    }
    finite_direction(quad.d,"quad-partial");
    finite_direction(rho.d,"C-angular-partial");
    finite_direction(flux.d,"RHS-angular-partial");
    result.quad[axis]=quad.d;result.rho[axis]=rho.d;result.flux[axis]=flux.d;
    ++stats.local_partial_basis_evaluations;
  }
  ++stats.local_partial_rows;return result;
}
static std::vector<PointOperator> prepare_rows(const RootEval &value,
    const Geometry &g,BatchStats &stats){
  std::vector<PointOperator> rows;rows.reserve(value.rows.size());
  for(size_t n=0;n<value.rows.size();++n){
    if((n&31)==0)time_check();rows.push_back(prepare_point(value.rows[n],g,stats));
  }
  return rows;
}
static Q apply_local(const std::array<Q,6> &a,const std::array<Q,6> &x){
  Q result=0;for(int k=0;k<6;++k)result+=a[k]*x[k];
  finite_direction(result,"cached-local-linear-operator");return result;
}

// Direct action of dC on the ORIGINAL accepted Newton solution s.
// beta uses the independent literal gram table. This formula is exactly
// the symmetric matrix layout in root_matrix; it is not cosine outer products.
static V structured_C_action(const Problem &p,const V &beta,const V &s){
  if(beta.size()!=size_t(2*p.M+1)||s.size()!=size_t(p.J))
    throw std::runtime_error("structured-C-shape");
  V result(p.J,0);
  result[0]=beta[0]*s[0];
  for(int j=1;j<p.J;++j)result[0]+=(p.sq2*beta[j])*s[j];
  for(int i=1;i<p.J;++i){
    result[i]=(p.sq2*beta[i])*s[0];
    for(int j=1;j<p.J;++j)result[i]+=(beta[std::abs(i-j)]+beta[i+j])*s[j];
  }
  for(Q x:result)finite_direction(x,"structured-C-action");return result;
}

// This reuses the NOMINAL recorded Cholesky factor. It is a numerical
// implementation of the exact-real identity, not the original dL operation
// graph. All rows of C*answer-rhs are read back below, without acceptance gates.
static V factor_direction_solve(const SolveTape &tape,const V &rhs,int n){
  V temporary(n),out(n);
  for(int i=0;i<n;++i){
    Q value=rhs[i];for(int j=0;j<i;++j)value-=tape.L[size_t(i)*n+j]*temporary[j];
    temporary[i]=value/tape.L[size_t(i)*n+i];finite_direction(temporary[i],"operator-forward");
  }
  for(int i=n-1;i>=0;--i){
    Q value=temporary[i];for(int j=i+1;j<n;++j)value-=tape.L[size_t(j)*n+i]*out[j];
    out[i]=value/tape.L[size_t(i)*n+i];finite_direction(out[i],"operator-backward");
  }
  return out;
}
struct NominalDefects {Q factor=0,forward=0,backward=0,full_step=0;};
static NominalDefects read_nominal_defects(const UpdateTape &u,int n){
  NominalDefects r;
  for(int i=0;i<n;++i){
    if((i&15)==0)time_check();
    for(int j=0;j<n;++j){
      Q value=0;for(int k=0;k<=std::min(i,j);++k)value+=u.solve.L[size_t(i)*n+k]*u.solve.L[size_t(j)*n+k];
      value-=u.C[size_t(i)*n+j];finite(value,"nominal-factor-defect");r.factor=qmax(r.factor,fabsq(value));
    }
    Q forward=0,backward=0,full=0;
    for(int j=0;j<=i;++j)forward+=u.solve.L[size_t(i)*n+j]*u.solve.tmp[j];
    for(int j=i;j<n;++j)backward+=u.solve.L[size_t(j)*n+i]*u.solve.out[j];
    for(int j=0;j<n;++j)full+=u.C[size_t(i)*n+j]*u.solve.out[j];
    forward-=u.evaluated.residual[i];backward-=u.solve.tmp[i];full-=u.evaluated.residual[i];
    finite(forward,"nominal-forward-defect");finite(backward,"nominal-backward-defect");finite(full,"nominal-C-step-defect");
    r.forward=qmax(r.forward,fabsq(forward));r.backward=qmax(r.backward,fabsq(backward));r.full_step=qmax(r.full_step,fabsq(full));
  }
  return r;
}
struct PreparedField {
  FieldTape original;
  std::vector<std::vector<PointOperator>> updates;
  std::vector<PointOperator> final_rows;
};
static PreparedField prepare_field(const Problem &p,FieldTape &&original,
    const Geometry &g,BatchStats &stats,std::ostream &trace,int stage,size_t step,int field){
  PreparedField result;result.original=std::move(original);
  const Q invN=1/static_cast<Q>(p.N);
  for(size_t update=0;update<result.original.root.updates.size();++update){
    const auto &u=result.original.root.updates[update];
    auto rows=prepare_rows(u.evaluated,g,stats);V beta(2*p.M+1,0);
    for(int n=0;n<p.N;++n){
      if((n&31)==0)time_check();const Q *gram=p.gram.data()+size_t(n)*(2*p.M+1);
      for(int k=0;k<=2*p.M;++k)beta[k]+=rows[n].rho_value*gram[k]*invN;
    }
    for(int i=0;i<p.J;++i)for(int j=0;j<=i;++j){
      const Q value=(i==j?1:0)+(j==0?(i==0?beta[0]:p.sq2*beta[i]):beta[i-j]+beta[i+j]);
      same_value(value,u.C[size_t(i)*p.J+j],stats.variation,"operator-literal-C-lower");
      same_value(value,u.C[size_t(j)*p.J+i],stats.variation,"operator-literal-C-symmetric");
    }
    const auto defects=read_nominal_defects(u,p.J);
    stats.nominal_factor_residual_max=qmax(stats.nominal_factor_residual_max,defects.factor);
    stats.nominal_forward_residual_max=qmax(stats.nominal_forward_residual_max,defects.forward);
    stats.nominal_backward_residual_max=qmax(stats.nominal_backward_residual_max,defects.backward);
    stats.nominal_C_step_residual_max=qmax(stats.nominal_C_step_residual_max,defects.full_step);
    trace<<"{\"kind\":\"operator-nominal-factor-readback\",\"stage\":"<<stage
      <<",\"RK_step\":"<<step<<",\"field\":"<<field<<",\"accepted_update\":"<<update
      <<",\"LLt_minus_C_max_abs\":"<<quoted(qstr(defects.factor))
      <<",\"Ltmp_minus_F_max_abs\":"<<quoted(qstr(defects.forward))
      <<",\"Lt_step_minus_tmp_max_abs\":"<<quoted(qstr(defects.backward))
      <<",\"C_step_minus_F_max_abs\":"<<quoted(qstr(defects.full_step))
      <<",\"residual_derivatives_not_proved_zero\":true,\"acceptance_gate\":false}\n";
    if(!trace)throw std::runtime_error("operator-nominal-readback-write");
    result.updates.push_back(std::move(rows));
  }
  result.final_rows=prepare_rows(result.original.root.returned.evaluated,g,stats);
  V flux(p.M,0);
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();const Q *sine=p.sine.data()+size_t(n)*p.M;
    for(int j=0;j<p.M;++j)flux[j]+=result.final_rows[n].flux_value*sine[j]*invN;
  }
  for(int j=0;j<p.M;++j)same_value(flux[j],result.original.primal.flux[j],stats.variation,"operator-final-primal-flux");
  return result;
}
static PreparedField capture_prepared(const Problem &p,const V &state,
    const Cell &cell,const Geometry &g,const Policy &policy,BatchStats &stats,
    std::ostream &trace,int stage,size_t step,int field){
  auto value=shared_trace128::capture_field(p,state,cell,g,policy,stats,trace,stage,step,field);
  return prepare_field(p,std::move(value),g,stats,trace,stage,step,field);
}

struct InputDirection {V target,momentum,P,Pt;};
static InputDirection input_direction(const Problem &p,const RootTape &root,
    const V &direction,const Cell &cell,const Geometry &g,
    const EnvironmentDirection &env,BatchStats &stats){
  if(direction.size()!=size_t(p.size))throw std::runtime_error("complete226-direction-required");
  InputDirection result{V(p.J,0),V(p.M),V(p.N,0),V(p.N,0)};
  const D r(g.r,env.g.r),w(g.w,env.g.w),w2(g.w2,env.g.w2),mu(cell.mu,env.mu),
    r2=r*r,r4=r2*r2,r3=r*r*r,
    factor=static_cast<Q>(p.orientation)*p.sq12*mu/(p.sq2*r4*w2);
  for(int j=0;j<p.M;++j){
    const D target=factor*D(root.state[p.M+j],direction[p.M+j]),
      momentum=-p.frequency[j]*r3*D(root.state[j],direction[j])/(p.sq2*w);
    same_value(target.v,root.target[j+1],stats.variation,"operator-target-value");
    result.target[j+1]=target.d;result.momentum[j]=momentum.d;
    finite_direction(target.d,"operator-target-direction");finite_direction(momentum.d,"operator-momentum-direction");
  }
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();const Q *sn=p.sine.data()+size_t(n)*p.M,*cs=p.cosine.data()+size_t(n)*p.J;
    for(int j=0;j<p.M;++j){
      result.P[n]+=result.momentum[j]*sn[j];
      result.Pt[n]+=(p.frequency[j]*result.momentum[j])*cs[j+1];
    }
    finite_direction(result.P[n],"operator-P-direction");finite_direction(result.Pt[n],"operator-Pt-direction");
  }
  return result;
}
static Q angular_L_direction(const Problem &p,const V &dL,int n){
  const Q *cs=p.cosine.data()+size_t(n)*p.J;Q value=dL[0];
  for(int j=0;j<p.M;++j)value+=dL[j+1]*cs[j+1];return value;
}
static V returned_L_direction(const Problem &p,const PreparedField &field,
    const InputDirection &input,const Geometry &g,const EnvironmentDirection &env,
    BatchStats &stats){
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
    const Q alpha=scalbnq(1,-u.backtrack);
    for(int j=0;j<p.J;++j){de[j]=de[j]-alpha*ds[j];finite_direction(de[j],"operator-accepted-e-direction");}
    ++stats.accepted_operator_updates;
  }
  V result(p.J);for(int j=0;j<p.J;++j){result[j]=input.target[j]+de[j];finite_direction(result[j],"operator-returned-L-direction");}
  ++stats.root_operator_returns;
  // At a returned root only angular quantities are needed by RHS. The old
  // final complete dF reduction is not an output or an update input here.
  ++stats.final_unused_F_derivative_reductions_skipped;return result;
}
static V rhs_direction_operator(const Problem &p,const PreparedField &field,
    const V &direction,const Cell &cell,const Geometry &g,
    const EnvironmentDirection &env,BatchStats &stats){
  const auto &root=field.original.root;const auto &primal=field.original.primal;
  const auto input=input_direction(p,root,direction,cell,g,env,stats);
  const V dL=returned_L_direction(p,field,input,g,env,stats);
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
static bool is_zero_environment(const EnvironmentDirection &e){
  return e.g.r==0&&e.g.dr==0&&e.g.w==0&&e.g.w2==0&&e.g.E==0&&e.mu==0;
}
static void compare_requested_field(const Problem &p,const PreparedField &field,
    const V &seed,const V &actual,const Cell &cell,const Geometry &g,
    const EnvironmentDirection &env,BatchStats &stats,std::ostream &trace,
    int stage,size_t step,int field_index,int column){
  if(std::find(stats.requested_reference_columns.begin(),stats.requested_reference_columns.end(),column)==stats.requested_reference_columns.end())return;
  std::string failure;Q error=0;bool completed=false;
  if(!is_zero_environment(env)){
    failure="old-reference-has-no-geometry-direction-interface";
    ++stats.reference_field_not_applicable;
  }else try{
    const V reference=shared_trace128::rhs_direction(p,field.original,seed,cell,g,stats);
    for(int j=0;j<p.size;++j)error=qmax(error,fabsq(actual[j]-reference[j]));
    finite_direction(error,"requested-old-graph-difference");
    stats.reference_field_difference_max=qmax(stats.reference_field_difference_max,error);
    ++stats.reference_field_columns;completed=true;
  }catch(const std::exception &e){
    if(std::string(e.what())=="explicit-experiment-time-budget")throw;
    failure=e.what();++stats.reference_field_failures;
  }
  trace<<"{\"kind\":\"requested-old-dL-graph-field-comparison\",\"stage\":"<<stage
    <<",\"RK_step\":"<<step<<",\"field\":"<<field_index<<",\"column_in_requested_block\":"<<column
    <<",\"state_column\":"<<stats.first_requested_state_column+column
    <<",\"comparison_complete\":"<<(completed?"true":"false")
    <<",\"error\":"<<(failure.empty()?"null":quoted(failure))
    <<",\"complete226_max_abs_difference\":"<<(completed?quoted(qstr(error)):"null")
    <<",\"same_actual_tape_and_supplied_tangent\":true,\"independent_original_whole_stage_comparison\":false,\"acceptance_gate\":false}\n";
  if(!trace)throw std::runtime_error("operator-reference-log-write");
}
static EnvironmentDirection column_environment(const StepDirections *parameters,int field,int column,int columns){
  if(!parameters)return {};
  if(parameters->h.size()!=size_t(columns)||parameters->environment[field].size()!=size_t(columns))
    throw std::runtime_error("complete-parameter-direction-columns-required");
  return parameters->environment[field][column];
}
static BatchPair rk4_batch_parameters(const Problem &p,const BatchPair &state,
    const Cell &cell,const Step &s,const Policy &policy,BatchStats &stats,
    std::ostream &trace,int stage,size_t step,const StepDirections *parameters){
  const auto a=capture_prepared(p,state.value,cell,s.g[0],policy,stats,trace,stage,step,0);
  V t(p.size);
  for(int j=0;j<p.size;++j)t[j]=state.value[j]+s.h*a.original.primal.derivative[j]/2;
  const auto b=capture_prepared(p,t,cell,s.g[1],policy,stats,trace,stage,step,1);
  for(int j=0;j<p.size;++j)t[j]=state.value[j]+s.h*b.original.primal.derivative[j]/2;
  const auto c=capture_prepared(p,t,cell,s.g[1],policy,stats,trace,stage,step,2);
  for(int j=0;j<p.size;++j)t[j]=state.value[j]+s.h*c.original.primal.derivative[j];
  const auto d=capture_prepared(p,t,cell,s.g[2],policy,stats,trace,stage,step,3);
  BatchPair out{V(p.size),V(size_t(p.size)*state.columns),state.columns};
  for(int j=0;j<p.size;++j){
    out.value[j]=state.value[j]+s.h*(a.original.primal.derivative[j]+2*b.original.primal.derivative[j]+2*c.original.primal.derivative[j]+d.original.primal.derivative[j])/6;
    finite(out.value[j],"operator-original-RK-primal");
  }
  for(int col=0;col<state.columns;++col){
    time_check();V seed(p.size),tangent(p.size);
    for(int j=0;j<p.size;++j)seed[j]=state.direction[size_t(j)*state.columns+col];
    const auto e0=column_environment(parameters,0,col,state.columns),
      em=column_environment(parameters,1,col,state.columns),e1=column_environment(parameters,2,col,state.columns);
    if(parameters&&(e0.mu!=em.mu||em.mu!=e1.mu))
      throw std::runtime_error("one-cell-mu-has-one-parameter-direction");
    const Q dh=parameters?parameters->h[col]:0;
    const V da=rhs_direction_operator(p,a,seed,cell,s.g[0],e0,stats);
    compare_requested_field(p,a,seed,da,cell,s.g[0],e0,stats,trace,stage,step,0,col);
    for(int j=0;j<p.size;++j)tangent[j]=(D(state.value[j],seed[j])+D(s.h,dh)*D(a.original.primal.derivative[j],da[j])/2).d;
    const V db=rhs_direction_operator(p,b,tangent,cell,s.g[1],em,stats);
    compare_requested_field(p,b,tangent,db,cell,s.g[1],em,stats,trace,stage,step,1,col);
    for(int j=0;j<p.size;++j)tangent[j]=(D(state.value[j],seed[j])+D(s.h,dh)*D(b.original.primal.derivative[j],db[j])/2).d;
    const V dc=rhs_direction_operator(p,c,tangent,cell,s.g[1],em,stats);
    compare_requested_field(p,c,tangent,dc,cell,s.g[1],em,stats,trace,stage,step,2,col);
    for(int j=0;j<p.size;++j)tangent[j]=(D(state.value[j],seed[j])+D(s.h,dh)*D(c.original.primal.derivative[j],dc[j])).d;
    const V dd=rhs_direction_operator(p,d,tangent,cell,s.g[2],e1,stats);
    compare_requested_field(p,d,tangent,dd,cell,s.g[2],e1,stats,trace,stage,step,3,col);
    for(int j=0;j<p.size;++j){
      const D result=D(state.value[j],seed[j])+D(s.h,dh)*
        (D(a.original.primal.derivative[j],da[j])+2*D(b.original.primal.derivative[j],db[j])+
         2*D(c.original.primal.derivative[j],dc[j])+D(d.original.primal.derivative[j],dd[j]))/6;
      same_value(result.v,out.value[j],stats.variation,"operator-RK-value");
      finite_direction(result.d,"operator-RK-direction");out.direction[size_t(j)*state.columns+col]=result.d;
    }
    ++stats.completed_column_steps;
  }
  ++stats.RK_steps;return out;
}
static BatchPair rk4_batch(const Problem &p,const BatchPair &state,const Cell &cell,
    const Step &s,const Policy &policy,BatchStats &stats,std::ostream &trace,int stage,size_t step){
  return rk4_batch_parameters(p,state,cell,s,policy,stats,trace,stage,step,nullptr);
}
static Q post_port_direction(Q before,Q derivative,Q ratio,Q ratio_direction){
  const D mapped=D(before,derivative)/D(ratio,ratio_direction);
  finite_direction(mapped.d,"operator-port-direction");return mapped.d;
}
static void print_stats(std::ostream &o,const BatchStats &s){
  o<<"{\"actual_shared_primal_and_reference_statistics\":";
  shared_trace128::print_stats(o,s);
  o<<",\"local_partial_rows\":"<<s.local_partial_rows
    <<",\"local_six_basis_evaluations\":"<<s.local_partial_basis_evaluations
    <<",\"structured_C_products\":"<<s.structured_C_products
    <<",\"shared_factor_direction_solves\":"<<s.shared_factor_direction_solves
    <<",\"root_operator_returns\":"<<s.root_operator_returns
    <<",\"accepted_operator_updates\":"<<s.accepted_operator_updates
    <<",\"all_C_direction_residual_rows_read\":"<<s.complete_C_linear_residual_rows
    <<",\"final_unused_dF_reductions_skipped\":"<<s.final_unused_F_derivative_reductions_skipped
    <<",\"nominal_LLtranspose_minus_C_max_abs\":"<<quoted(qstr(s.nominal_factor_residual_max))
    <<",\"nominal_Ltmp_minus_F_max_abs\":"<<quoted(qstr(s.nominal_forward_residual_max))
    <<",\"nominal_Ltranspose_step_minus_tmp_max_abs\":"<<quoted(qstr(s.nominal_backward_residual_max))
    <<",\"nominal_C_step_minus_F_max_abs\":"<<quoted(qstr(s.nominal_C_step_residual_max))
    <<",\"computed_C_direction_solve_max_abs_residual\":"<<quoted(qstr(s.direction_C_solve_residual_max))
    <<",\"reference_field_columns\":"<<s.reference_field_columns
    <<",\"reference_field_failures\":"<<s.reference_field_failures
    <<",\"reference_field_not_applicable\":"<<s.reference_field_not_applicable
    <<",\"reference_complete226_difference_max_abs\":"<<quoted(qstr(s.reference_field_difference_max))
    <<",\"nominal_residual_derivative_bound_provided\":false"
    <<",\"reference_difference_is_error_bound\":false,\"acceptance_gate\":false}";
}
} // namespace operator_trace128
#endif
