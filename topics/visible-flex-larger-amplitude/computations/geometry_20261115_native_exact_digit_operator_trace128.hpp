// R405 independent complete dyadic-dot R402 operator.
// Every passed finite-Q dot is exact before one RN113. Matrix coefficient
// formation is still actual binary128 arithmetic, so no complete derivative
// enclosure or old graph word equality is asserted.
#ifndef VISIBLE_NATIVE_EXACT_DIGIT_OPERATOR_TRACE128_HPP
#define VISIBLE_NATIVE_EXACT_DIGIT_OPERATOR_TRACE128_HPP
#include "geometry_20261115_native_preassembled_operator_trace128.hpp"
#include "geometry_20261115_native_exact_digit128.hpp"

namespace exact_digit_trace128 {
using namespace shared_trace128;
using shared_trace128::BatchPair;
using EnvironmentDirection=hoisted_trace128::EnvironmentDirection;
using StepDirections=hoisted_trace128::StepDirections;

struct BatchStats:preassembled_trace128::BatchStats {
  exact_digit128::Stats digits;
  uint64_t literal_basis_caches=0,gram_coefficient_entries=0,
    gram_exact_dot_outputs=0,batch_matrix_products=0,
    complete_rhs_column_batches=0,full_rhs_columns=0,
    entire_RK_column_batches=0;
  void join(const BatchStats &b){
    preassembled_trace128::BatchStats::join(b);digits.join(b.digits);
    literal_basis_caches+=b.literal_basis_caches;
    gram_coefficient_entries+=b.gram_coefficient_entries;
    gram_exact_dot_outputs+=b.gram_exact_dot_outputs;
    batch_matrix_products+=b.batch_matrix_products;
    complete_rhs_column_batches+=b.complete_rhs_column_batches;
    full_rhs_columns+=b.full_rhs_columns;
    entire_RK_column_batches+=b.entire_RK_column_batches;
  }
};
struct DenseMap:preassembled_trace128::DenseMap {
  using preassembled_trace128::DenseMap::DenseMap;
  V apply_batch(const V &x,int count,BatchStats &stats)const{
    if(count<1||x.size()!=size_t(columns)*count)
      throw std::runtime_error("exact-digit-map-complete-batch-shape");
    V out=exact_digit128::multiply(values.data(),x.data(),rows,columns,count,
        stats.digits,time_check);
    for(Q value:out)finite_direction(value,"exact-digit-complete-matrix-action");
    ++stats.batch_matrix_products;return out;
  }
};
// An immutable right matrix's exact words/digits may be shared by all stages.
// Only metadata counters are stage-local. There is no cache keyed by an
// address whose lifetime or contents could later change.
struct RightCache {
  size_t rows=0,columns=0,row_reserve=0;
  std::vector<exact_digit128::PackedVector> packed_columns;
  RightCache()=default;
  RightCache(const DenseMap &matrix,BatchStats &stats):
      rows(matrix.rows),columns(matrix.columns){
    row_reserve=std::min(
      exact_digit128::checked_product(exact_digit128::checked_product(
        exact_digit128::FAST_LIMB_LIMIT,rows),sizeof(int32_t)),
      exact_digit128::PACKING_BYTES_LIMIT);
    size_t available=exact_digit128::PACKING_BYTES_LIMIT-row_reserve;
    packed_columns.reserve(columns);
    for(size_t j=0;j<columns;++j){
      time_check();
      packed_columns.push_back(exact_digit128::prepare(
        {matrix.values.data()+j,rows,columns},available,stats.digits,time_check));
    }
  }
  DenseMap left_multiply(const DenseMap &a,BatchStats &stats)const{
    if(size_t(a.columns)!=rows)throw std::runtime_error("exact-digit-cached-product-shape");
    DenseMap out(a.rows,static_cast<int>(columns));
    for(int i=0;i<a.rows;++i){
      time_check();size_t available=row_reserve;
      const auto row=exact_digit128::prepare(
        {a.values.data()+size_t(i)*a.columns,rows,1},available,stats.digits,time_check);
      for(size_t j=0;j<columns;++j)
        out.at(i,static_cast<int>(j))=exact_digit128::dot(row,packed_columns[j],stats.digits,time_check);
    }
    out.check(stats);++stats.batch_matrix_products;return out;
  }
};
struct LiteralBases {
  DenseMap gram_transpose,momentum_basis,L_basis,sine_over_N_transpose;
  RightCache gram_right,momentum_right,L_right;
  LiteralBases(const Problem &p,BatchStats &stats):
      gram_transpose(2*p.M+1,p.N),momentum_basis(2*p.N,p.M),
      L_basis(p.N,p.J),sine_over_N_transpose(p.M,p.N){
    const Q invN=1/static_cast<Q>(p.N);
    for(int n=0;n<p.N;++n){
      if((n&15)==0)time_check();
      const Q *cs=p.cosine.data()+size_t(n)*p.J,
        *sn=p.sine.data()+size_t(n)*p.M,
        *gr=p.gram.data()+size_t(n)*(2*p.M+1);
      for(int j=0;j<2*p.M+1;++j)gram_transpose.at(j,n)=gr[j];
      L_basis.at(n,0)=1;
      for(int j=1;j<p.J;++j)L_basis.at(n,j)=cs[j];
      for(int j=0;j<p.M;++j){
        momentum_basis.at(n,j)=sn[j];
        momentum_basis.at(p.N+n,j)=p.frequency[j]*cs[j+1];
        sine_over_N_transpose.at(j,n)=sn[j]*invN;
      }
    }
    gram_transpose.check(stats);momentum_basis.check(stats);
    L_basis.check(stats);sine_over_N_transpose.check(stats);
    gram_right=RightCache(gram_transpose,stats);
    momentum_right=RightCache(momentum_basis,stats);
    L_right=RightCache(L_basis,stats);
    ++stats.literal_basis_caches;
  }
  void identity(std::ostream &out,BatchStats &stats)const{
    out<<"{\"schema\":\"complete-literal-binary128-bases-for-exact-digit-stage-v1\","
      "\"gram_transpose\":";gram_transpose.identity(out,stats);
    out<<",\"momentum_basis\":";momentum_basis.identity(out,stats);
    out<<",\"L_basis\":";L_basis.identity(out,stats);
    out<<",\"sine_over_N_transpose\":";sine_over_N_transpose.identity(out,stats);
    out<<",\"all_input_tables_original_literal_words\":true,"
      "\"frequency_and_invN_products_still_binary128\":true,"
      "\"ideal_trigonometric_identities_used\":false,"
      "\"immutable_cache_shared_across_stage_threads\":true}";
  }
};
struct RootMaps{DenseMap momentum,L;};
struct FluxMaps{DenseMap momentum,L;};
struct PreparedField:hoisted_trace128::PreparedField{
  std::vector<RootMaps> root_maps;FluxMaps flux_maps;
};
static DenseMap gram_coefficient_matrix(const Problem &p,const V &step,BatchStats &stats){
  if(step.size()!=size_t(p.J))throw std::runtime_error("exact-digit-recorded-step-shape");
  DenseMap H(p.J,2*p.M+1);H.at(0,0)=step[0];
  for(int j=1;j<p.J;++j)H.at(0,j)=p.sq2*step[j];
  for(int i=1;i<p.J;++i){
    H.at(i,i)=p.sq2*step[0];
    for(int j=1;j<p.J;++j){
      H.at(i,std::abs(i-j))+=step[j];
      H.at(i,i+j)+=step[j];
    }
  }
  H.check(stats);stats.gram_coefficient_entries+=H.values.size();
  return H;
}
static RootMaps assemble_root(const Problem &p,const UpdateTape &update,
    const std::vector<hoisted_trace128::PointOperator> &rows,
    const LiteralBases &basis,BatchStats &stats){
  ++stats.root_map_builds_started;const auto began=Clock::now();
  // This H forms the R402 accurate-real coefficient pattern from the actual
  // recorded solve.out. Its small coefficient sums/products are explicitly
  // binary128 and reassociated relative to190. No coefficient error enclosure
  // is invented. All original 2M+1 literal gram columns are retained.
  const DenseMap H=gram_coefficient_matrix(p,update.solve.out,stats);
  const DenseMap HG=basis.gram_right.left_multiply(H,stats);
  stats.gram_exact_dot_outputs+=HG.values.size();
  stats.gram_action_rows_preassembled+=HG.values.size();
  DenseMap WM(p.J,2*p.N),WL(p.J,p.N);
  const Q invN=1/static_cast<Q>(p.N);
  for(int n=0;n<p.N;++n){
    if((n&3)==0)time_check();
    const Q *cs=p.cosine.data()+size_t(n)*p.J;
    const auto &q=rows[n].quad,&rho=rows[n].rho;
    for(int i=0;i<p.J;++i){
      const Q hg=HG.at(i,n),
        wP=(cs[i]*q[0]-hg*rho[0])*invN,
        wPt=(cs[i]*q[1]-hg*rho[1])*invN,
        wL=(cs[i]*q[2]-hg*rho[2])*invN;
      finite_direction(wP,"exact-digit-wP");finite_direction(wPt,"exact-digit-wPt");
      finite_direction(wL,"exact-digit-wL");
      WM.at(i,n)=wP;WM.at(i,p.N+n)=wPt;WL.at(i,n)=wL;
    }
    ++stats.root_map_angular_rows;
  }
  RootMaps out{basis.momentum_right.left_multiply(WM,stats),
    basis.L_right.left_multiply(WL,stats)};
  ++stats.root_map_builds_completed;
  stats.completed_preassembly_seconds+=std::chrono::duration<double>(Clock::now()-began).count();
  return out;
}
static FluxMaps assemble_flux(const Problem &p,
    const std::vector<hoisted_trace128::PointOperator> &rows,
    const LiteralBases &basis,BatchStats &stats){
  ++stats.flux_map_builds_started;const auto began=Clock::now();
  DenseMap A(p.N,p.M),B(p.N,p.J);
  for(int n=0;n<p.N;++n){
    if((n&3)==0)time_check();
    const Q *cs=p.cosine.data()+size_t(n)*p.J,*sn=p.sine.data()+size_t(n)*p.M;
    const auto &f=rows[n].flux;B.at(n,0)=f[2];
    for(int j=0;j<p.M;++j){
      const Q m=p.frequency[j];
      A.at(n,j)=f[0]*sn[j]+f[1]*(m*cs[j+1])+f[3]*(sn[j]*(m*m-1));
      B.at(n,j+1)=f[2]*cs[j+1]-f[3]*(sn[j]*m);
    }
    ++stats.flux_map_angular_rows;
  }
  A.check(stats);B.check(stats);
  const RightCache ar(A,stats),br(B,stats);
  FluxMaps out{ar.left_multiply(basis.sine_over_N_transpose,stats),
    br.left_multiply(basis.sine_over_N_transpose,stats)};
  ++stats.flux_map_builds_completed;
  stats.completed_preassembly_seconds+=std::chrono::duration<double>(Clock::now()-began).count();
  return out;
}
static PreparedField capture_prepared(const Problem &p,const V &state,
    const Cell &cell,const Geometry &g,const Policy &policy,const LiteralBases &basis,
    BatchStats &stats,std::ostream &trace,int stage,size_t step,int field){
  PreparedField out;
  static_cast<hoisted_trace128::PreparedField&>(out)=
    hoisted_trace128::capture_prepared(p,state,cell,g,policy,stats,trace,stage,step,field);
  for(size_t i=0;i<out.original.root.updates.size();++i){
    out.root_maps.push_back(assemble_root(p,out.original.root.updates[i],out.updates[i],basis,stats));
    trace<<"{\"kind\":\"recorded-root-exact-digit-map-identity\",\"stage\":"<<stage
      <<",\"RK_step\":"<<step<<",\"field\":"<<field<<",\"accepted_update\":"<<i
      <<",\"original_backtrack\":"<<out.original.root.updates[i].backtrack
      <<",\"momentum_map\":";out.root_maps.back().momentum.identity(trace,stats);
    trace<<",\"L_map\":";out.root_maps.back().L.identity(trace,stats);
    trace<<",\"all_literal_angular_nodes\":"<<p.N
      <<",\"complete_dyadic_dot_then_once_RN113\":true"
      <<",\"small_H_and_weight_coefficients_still_binary128\":true"
      <<",\"nominal_factor_exactly_equals_C_not_assumed\":true"
      <<",\"error_enclosure_supplied\":false}\n";
    if(!trace)throw std::runtime_error("exact-digit-root-identity-write");
  }
  out.flux_maps=assemble_flux(p,out.final_rows,basis,stats);
  trace<<"{\"kind\":\"recorded-final-flux-exact-digit-map-identity\",\"stage\":"<<stage
    <<",\"RK_step\":"<<step<<",\"field\":"<<field<<",\"momentum_map\":";
  out.flux_maps.momentum.identity(trace,stats);
  trace<<",\"L_map\":";out.flux_maps.L.identity(trace,stats);
  trace<<",\"complete_dyadic_dot_then_once_RN113\":true,\"error_enclosure_supplied\":false}\n";
  if(!trace)throw std::runtime_error("exact-digit-flux-identity-write");
  return out;
}
struct InputDirection {V target,momentum;};
static InputDirection input_direction(const Problem &p,const RootTape &root,
    const V &direction,const Cell &cell,const Geometry &g,
    const EnvironmentDirection &env,BatchStats &stats){
  if(direction.size()!=size_t(p.size))throw std::runtime_error("complete226-direction-required");
  InputDirection result{V(p.J,0),V(p.M)};
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
  ++stats.small_input_columns;return result;
}

struct InputBatch{V target,momentum;int columns=0;};
static InputBatch input_batch(const Problem &p,const RootTape &root,
    const V &directions,int columns,const Cell &cell,const Geometry &g,BatchStats &stats){
  if(columns<1||directions.size()!=size_t(p.size)*columns)
    throw std::runtime_error("exact-digit-complete226-input-batch-required");
  InputBatch out{V(size_t(p.J)*columns,0),V(size_t(p.M)*columns),columns};
  const EnvironmentDirection env{};
  for(int col=0;col<columns;++col){
    time_check();V seed(p.size);
    for(int j=0;j<p.size;++j)seed[j]=directions[size_t(j)*columns+col];
    const InputDirection in=input_direction(p,root,seed,cell,g,env,stats);
    for(int j=0;j<p.J;++j)out.target[size_t(j)*columns+col]=in.target[j];
    for(int j=0;j<p.M;++j)out.momentum[size_t(j)*columns+col]=in.momentum[j];
  }
  return out;
}
static V returned_L_batch(const Problem &p,const PreparedField &field,
    const InputBatch &input,BatchStats &stats){
  if(field.root_maps.size()!=field.original.root.updates.size())
    throw std::runtime_error("complete-original-root-update-map-count");
  const int columns=input.columns;V de(size_t(p.J)*columns,0);
  for(size_t k=0;k<field.original.root.updates.size();++k){
    time_check();const auto &u=field.original.root.updates[k];
    const auto &maps=field.root_maps[k];V dL(de.size());
    for(size_t j=0;j<de.size();++j)dL[j]=input.target[j]+de[j];
    const V ym=maps.momentum.apply_batch(input.momentum,columns,stats),
      yl=maps.L.apply_batch(dL,columns,stats);
    const Q alpha=scalbnq(1,-u.backtrack);
    for(int col=0;col<columns;++col){
      time_check();V right(p.J);
      for(int j=0;j<p.J;++j){
        const size_t at=size_t(j)*columns+col;
        right[j]=de[at]+ym[at]+yl[at];finite_direction(right[j],"exact-digit-root-right");
      }
      const V ds=hoisted_trace128::factor_direction_solve(u.solve,right,p.J);
      ++stats.shared_factor_direction_solves;
      // Original C multiplication/accumulation and original nominal-factor
      // triangular solve remain; this is an actual diagnostic, not a new gate.
      for(int i=0;i<p.J;++i){
        Q residual=0;for(int j=0;j<p.J;++j)residual+=u.C[size_t(i)*p.J+j]*ds[j];
        residual-=right[i];finite_direction(residual,"complete-C-direction-readback");
        stats.direction_C_solve_residual_max=qmax(stats.direction_C_solve_residual_max,fabsq(residual));
        ++stats.complete_C_linear_residual_rows;
      }
      for(int j=0;j<p.J;++j){
        const size_t at=size_t(j)*columns+col;
        de[at]=de[at]-alpha*ds[j];finite_direction(de[at],"operator-accepted-e-direction");
      }
      ++stats.accepted_operator_updates;++stats.preassembled_root_map_actions;
    }
  }
  V result(de.size());
  for(size_t j=0;j<de.size();++j){
    result[j]=input.target[j]+de[j];finite_direction(result[j],"operator-returned-L-direction");
  }
  stats.root_operator_returns+=columns;stats.final_unused_F_derivative_reductions_skipped+=columns;
  return result;
}
static V rhs_direction_batch(const Problem &p,const PreparedField &field,
    const V &directions,int columns,const Cell &cell,const Geometry &g,BatchStats &stats){
  const auto &root=field.original.root;const auto &primal=field.original.primal;
  const auto input=input_batch(p,root,directions,columns,cell,g,stats);
  const V dL=returned_L_batch(p,field,input,stats);
  const V fm=field.flux_maps.momentum.apply_batch(input.momentum,columns,stats),
    fl=field.flux_maps.L.apply_batch(dL,columns,stats);
  V out(size_t(p.size)*columns);
  const EnvironmentDirection env{};
  for(int col=0;col<columns;++col){
    time_check();V direction(p.size),dflux(p.M);
    for(int j=0;j<p.size;++j)direction[j]=directions[size_t(j)*columns+col];
    for(int j=0;j<p.M;++j){
      const size_t at=size_t(j)*columns+col;
      dflux[j]=fm[at]+fl[at];finite_direction(dflux[j],"exact-digit-complete-flux");
    }
    const D r(g.r,env.g.r),dr(g.dr,env.g.dr),w(g.w,env.g.w),w2(g.w2,env.g.w2),mu(cell.mu,env.mu),
      r3=r*r*r,sigma=dr/r,pref=static_cast<Q>(p.orientation)*p.sq2*r3*dr*w2/(p.sq12*mu);
    DV result(p.size,D(0));
    for(int j=0;j<p.M;++j){
      const Q m=p.frequency[j];const D y(root.state[j],direction[j]),pi(root.state[p.M+j],direction[p.M+j]),
        L(root.returned.L[j+1],dL[size_t(j+1)*columns+col]),pj=-m*r3*y/(p.sq2*w),linear=-m*L+(m*m-1)*pj;
      result[j]=sigma*((m*m-4)*y+p.sq2*w*L/r3);
      result[p.M+j]=4*sigma*pi+pref*m*(linear+D(primal.flux[j],dflux[j]));
    }
    result[p.K]=dr*w*D(root.returned.L[0],dL[col]);result[p.K+1]=dr*w;
    for(int j=0;j<p.size;++j){
      same_value(result[j].v,primal.derivative[j],stats.variation,"operator-complete-RHS-value");
      finite_direction(result[j].d,"operator-complete-RHS-direction");
      out[size_t(j)*columns+col]=result[j].d;
    }
    ++stats.full_rhs_columns;++stats.preassembled_flux_map_actions;
  }
  ++stats.complete_rhs_column_batches;return out;
}
static void compare_requested_batch(const Problem &p,const PreparedField &field,
    const V &seed,const V &actual,int columns,const Cell &cell,const Geometry &g,
    BatchStats &stats,std::ostream &trace,int stage,size_t step,int field_index){
  const EnvironmentDirection env{};
  for(int col=0;col<columns;++col){
    V a(p.size),b(p.size);
    for(int j=0;j<p.size;++j){a[j]=seed[size_t(j)*columns+col];b[j]=actual[size_t(j)*columns+col];}
    hoisted_trace128::compare_requested_field(p,field,a,b,cell,g,env,stats,
      trace,stage,step,field_index,col);
  }
}
static BatchPair rk4_batch_parameters(const Problem &p,const BatchPair &state,
    const Cell &cell,const Step &s,const Policy &policy,const LiteralBases &basis,
    BatchStats &stats,std::ostream &trace,int stage,size_t step,const StepDirections *parameters){
  if(parameters){
    ++stats.general_parameter_RK_fallbacks;
    operator_trace128::StepDirections original_parameters;
    original_parameters.h=parameters->h;
    for(int field=0;field<3;++field){
      original_parameters.environment[field].reserve(parameters->environment[field].size());
      for(const auto &e:parameters->environment[field])
        original_parameters.environment[field].push_back({e.g,e.mu});
    }
    return operator_trace128::rk4_batch_parameters(p,state,cell,s,policy,stats,
        trace,stage,step,&original_parameters);
  }

  ++stats.state_only_RK_batches;
  const auto a=capture_prepared(p,state.value,cell,s.g[0],policy,basis,stats,trace,stage,step,0);
  V t(p.size);
  for(int j=0;j<p.size;++j)t[j]=state.value[j]+s.h*a.original.primal.derivative[j]/2;
  const auto b=capture_prepared(p,t,cell,s.g[1],policy,basis,stats,trace,stage,step,1);
  for(int j=0;j<p.size;++j)t[j]=state.value[j]+s.h*b.original.primal.derivative[j]/2;
  const auto c=capture_prepared(p,t,cell,s.g[1],policy,basis,stats,trace,stage,step,2);
  for(int j=0;j<p.size;++j)t[j]=state.value[j]+s.h*c.original.primal.derivative[j];
  const auto d=capture_prepared(p,t,cell,s.g[2],policy,basis,stats,trace,stage,step,3);
  BatchPair out{V(p.size),V(size_t(p.size)*state.columns),state.columns};
  for(int j=0;j<p.size;++j){
    out.value[j]=state.value[j]+s.h*(a.original.primal.derivative[j]+2*b.original.primal.derivative[j]+2*c.original.primal.derivative[j]+d.original.primal.derivative[j])/6;
    finite(out.value[j],"operator-original-RK-primal");
  }
  const int columns=state.columns;
  const V da=rhs_direction_batch(p,a,state.direction,columns,cell,s.g[0],stats);
  compare_requested_batch(p,a,state.direction,da,columns,cell,s.g[0],stats,trace,stage,step,0);
  V tb(state.direction.size());
  for(int j=0;j<p.size;++j)for(int col=0;col<columns;++col){
    const size_t at=size_t(j)*columns+col;
    tb[at]=(D(state.value[j],state.direction[at])+D(s.h,0)*D(a.original.primal.derivative[j],da[at])/2).d;
  }
  const V db=rhs_direction_batch(p,b,tb,columns,cell,s.g[1],stats);
  compare_requested_batch(p,b,tb,db,columns,cell,s.g[1],stats,trace,stage,step,1);
  V tc(state.direction.size());
  for(int j=0;j<p.size;++j)for(int col=0;col<columns;++col){
    const size_t at=size_t(j)*columns+col;
    tc[at]=(D(state.value[j],state.direction[at])+D(s.h,0)*D(b.original.primal.derivative[j],db[at])/2).d;
  }
  const V dc=rhs_direction_batch(p,c,tc,columns,cell,s.g[1],stats);
  compare_requested_batch(p,c,tc,dc,columns,cell,s.g[1],stats,trace,stage,step,2);
  V td(state.direction.size());
  for(int j=0;j<p.size;++j)for(int col=0;col<columns;++col){
    const size_t at=size_t(j)*columns+col;
    td[at]=(D(state.value[j],state.direction[at])+D(s.h,0)*D(c.original.primal.derivative[j],dc[at])).d;
  }
  const V dd=rhs_direction_batch(p,d,td,columns,cell,s.g[2],stats);
  compare_requested_batch(p,d,td,dd,columns,cell,s.g[2],stats,trace,stage,step,3);
  for(int col=0;col<columns;++col){
    time_check();
    for(int j=0;j<p.size;++j){
      const size_t at=size_t(j)*columns+col;
      const D result=D(state.value[j],state.direction[at])+D(s.h,0)*
        (D(a.original.primal.derivative[j],da[at])+2*D(b.original.primal.derivative[j],db[at])+
         2*D(c.original.primal.derivative[j],dc[at])+D(d.original.primal.derivative[j],dd[at]))/6;
      same_value(result.v,out.value[j],stats.variation,"operator-RK-value");
      finite_direction(result.d,"operator-RK-direction");out.direction[at]=result.d;
    }
    ++stats.completed_column_steps;
  }
  ++stats.entire_RK_column_batches;++stats.RK_steps;return out;
}
static BatchPair rk4_batch(const Problem &p,const BatchPair &state,const Cell &cell,
    const Step &s,const Policy &policy,const LiteralBases &basis,
    BatchStats &stats,std::ostream &trace,int stage,size_t step){
  return rk4_batch_parameters(p,state,cell,s,policy,basis,stats,trace,stage,step,nullptr);
}
static Q post_port_direction(Q before,Q derivative,Q ratio,Q ratio_direction){
  return preassembled_trace128::post_port_direction(before,derivative,ratio,ratio_direction);
}
static void print_digit_stats(std::ostream &o,const exact_digit128::Stats &s){
  o<<"{\"decoded_values\":"<<s.decoded_values
    <<",\"zero_input_words\":"<<s.zero_input_words
    <<",\"negative_zero_input_words\":"<<s.negative_zero_input_words
    <<",\"subnormal_input_words\":"<<s.subnormal_input_words
    <<",\"nonfinite_input_failures\":"<<s.nonfinite_input_failures
    <<",\"packed_vectors\":"<<s.packed_vectors
    <<",\"wide_span_vectors\":"<<s.wide_span_vectors
    <<",\"packing_budget_vectors\":"<<s.packing_budget_vectors
    <<",\"complete_digit_planes\":"<<s.complete_digit_planes
    <<",\"zero_digit_planes\":"<<s.zero_digit_planes
    <<",\"exact_dot_calls\":"<<s.exact_dot_calls
    <<",\"zero_dot_calls\":"<<s.zero_dot_calls
    <<",\"packed_dot_calls\":"<<s.packed_dot_calls
    <<",\"wide_dot_calls\":"<<s.wide_dot_calls
    <<",\"complete_scalar_products\":"<<s.complete_scalar_products
    <<",\"digit_products\":"<<s.digit_products
    <<",\"integer_partial_sums\":"<<s.integer_partial_sums
    <<",\"exact_zero_outputs\":"<<s.exact_zero_outputs
    <<",\"inexact_roundings\":"<<s.inexact_roundings
    <<",\"subnormal_outputs\":"<<s.subnormal_outputs
    <<",\"rounded_zero_outputs\":"<<s.rounded_zero_outputs
    <<",\"overflow_outputs\":"<<s.overflow_outputs
    <<",\"max_observed_span_bits\":"<<s.max_observed_span_bits
    <<",\"max_observed_limb_count\":"<<s.max_observed_limb_count
    <<",\"max_positive_words\":"<<s.max_positive_words
    <<",\"max_negative_words\":"<<s.max_negative_words
    <<",\"digit_bits\":20,\"reduction_block_max\":2048,\"fast_limb_limit\":12"
    <<",\"six_limb_truncation_used\":false,\"packing_budget_bytes\":67108864"
    <<",\"wide_integer_fallback_complete\":true,\"BLAS_or_Boost_used\":false}";
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
    <<",\"nominal_LLtranspose_minus_C_max_abs\":"<< ::quoted(qstr(s.nominal_factor_residual_max))
    <<",\"nominal_Ltmp_minus_F_max_abs\":"<< ::quoted(qstr(s.nominal_forward_residual_max))
    <<",\"nominal_Ltranspose_step_minus_tmp_max_abs\":"<< ::quoted(qstr(s.nominal_backward_residual_max))
    <<",\"nominal_C_step_minus_F_max_abs\":"<< ::quoted(qstr(s.nominal_C_step_residual_max))
    <<",\"computed_C_direction_solve_max_abs_residual\":"<< ::quoted(qstr(s.direction_C_solve_residual_max))
    <<",\"reference_field_columns\":"<<s.reference_field_columns
    <<",\"reference_field_failures\":"<<s.reference_field_failures
    <<",\"reference_field_not_applicable\":"<<s.reference_field_not_applicable
    <<",\"reference_complete226_difference_max_abs\":"<< ::quoted(qstr(s.reference_field_difference_max))
    <<",\"nominal_residual_derivative_bound_provided\":false"
    <<",\"reference_difference_is_error_bound\":false"
    <<",\"shared_six_axis_point_value_programs\":"<<s.shared_six_axis_point_programs
    <<",\"momentum_frequency_vectors_formed_once\":"<<s.momentum_weight_vectors
    <<",\"flux_modal_vectors_formed_once\":"<<s.flux_coefficient_vectors
    <<",\"cached_momentum_frequency_products\":"<<s.cached_momentum_frequency_products
    <<",\"cached_flux_modal_coefficients\":"<<s.cached_flux_modal_coefficients
    <<",\"state_only_RK_batches\":"<<s.state_only_RK_batches
    <<",\"original_general_parameter_RK_fallbacks\":"<<s.general_parameter_RK_fallbacks
    <<",\"used_Q_primitive_and_reduction_order_preserved_relative_to_R305\":false"
    <<",\"independent_runtime_word_comparison_performed\":false"
    <<",\"preassembly_root_builds_started\":"<<s.root_map_builds_started
    <<",\"preassembly_root_builds_completed\":"<<s.root_map_builds_completed
    <<",\"preassembly_flux_builds_started\":"<<s.flux_map_builds_started
    <<",\"preassembly_flux_builds_completed\":"<<s.flux_map_builds_completed
    <<",\"preassembly_root_angular_rows\":"<<s.root_map_angular_rows
    <<",\"preassembly_flux_angular_rows\":"<<s.flux_map_angular_rows
    <<",\"literal_gram_step_rows_preassembled\":"<<s.gram_action_rows_preassembled
    <<",\"complete_preassembled_matrix_entries_checked\":"<<s.complete_matrix_entries_checked
    <<",\"preassembled_coefficient_matrices_hashed\":"<<s.coefficient_matrices_hashed
    <<",\"original_small_input_columns\":"<<s.small_input_columns
    <<",\"preassembled_root_actions\":"<<s.preassembled_root_map_actions
    <<",\"preassembled_final_flux_actions\":"<<s.preassembled_flux_map_actions
    <<",\"completed_preassembly_seconds\":"<<std::setprecision(17)<<s.completed_preassembly_seconds
    <<",\"recorded_factor_real_operator_only\":true"
    <<",\"angular_reduction_and_invN_reassociated\":true"
    <<",\"eliminated_intermediates_not_claimed_individually_formed\":true"
    <<",\"integer_digit_matmul_implemented\":true"
    <<",\"full_root_derivative_error_enclosure_supplied\":false"
    <<",\"whole_recorded_H_coefficient_matrix_formed_binary128\":true"
    <<",\"same_small_coefficient_graph_as190_claimed\":false"
    <<",\"complete_dyadic_dot_then_once_RN113\":true"
    <<",\"exact_zero_sum_convention_positive_zero\":true"
    <<",\"negative_nonzero_underflow_retains_negative_zero\":true"
    <<",\"literal_basis_caches\":"<<s.literal_basis_caches
    <<",\"gram_coefficient_entries\":"<<s.gram_coefficient_entries
    <<",\"gram_exact_dot_outputs\":"<<s.gram_exact_dot_outputs
    <<",\"batch_matrix_products\":"<<s.batch_matrix_products
    <<",\"complete_rhs_column_batches\":"<<s.complete_rhs_column_batches
    <<",\"full_rhs_columns\":"<<s.full_rhs_columns
    <<",\"entire_RK_column_batches\":"<<s.entire_RK_column_batches
    <<",\"exact_digit_statistics\":";print_digit_stats(o,s.digits);
  o
    <<",\"acceptance_gate\":false}";
}

} // namespace exact_digit_trace128
#endif
