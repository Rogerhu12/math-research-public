// R402 recorded-coefficient / nominal-factor operator preassembly.
// This is a NEW binary128 operation graph. Literal sine/cosine/gram words,
// the full primal/root trace, all224 state columns and original final gates
// remain. No bitwise equivalence with R305/186 or derivative error bound is
// asserted. The ideal real operator uses the actual recorded Cholesky factor,
// not an unproved exact inverse of C. The optional integer-digit kernel from
// R402 is NOT implemented here.
#ifndef VISIBLE_NATIVE_PREASSEMBLED_OPERATOR_TRACE128_HPP
#define VISIBLE_NATIVE_PREASSEMBLED_OPERATOR_TRACE128_HPP
#include "geometry_20261115_native_hoisted_operator_trace128.hpp"
#include <cstdint>

namespace preassembled_trace128 {
using namespace shared_trace128;
using shared_trace128::BatchPair;
using EnvironmentDirection=hoisted_trace128::EnvironmentDirection;
using StepDirections=hoisted_trace128::StepDirections;

struct BatchStats : hoisted_trace128::BatchStats {
  uint64_t root_map_builds_started=0,root_map_builds_completed=0,
    flux_map_builds_started=0,flux_map_builds_completed=0,
    root_map_angular_rows=0,flux_map_angular_rows=0,
    gram_action_rows_preassembled=0,complete_matrix_entries_checked=0,
    small_input_columns=0,preassembled_root_map_actions=0,
    preassembled_flux_map_actions=0,coefficient_matrices_hashed=0;
  double completed_preassembly_seconds=0;
  void join(const BatchStats &b){
    hoisted_trace128::BatchStats::join(b);
    root_map_builds_started+=b.root_map_builds_started;
    root_map_builds_completed+=b.root_map_builds_completed;
    flux_map_builds_started+=b.flux_map_builds_started;
    flux_map_builds_completed+=b.flux_map_builds_completed;
    root_map_angular_rows+=b.root_map_angular_rows;
    flux_map_angular_rows+=b.flux_map_angular_rows;
    gram_action_rows_preassembled+=b.gram_action_rows_preassembled;
    complete_matrix_entries_checked+=b.complete_matrix_entries_checked;
    small_input_columns+=b.small_input_columns;
    preassembled_root_map_actions+=b.preassembled_root_map_actions;
    preassembled_flux_map_actions+=b.preassembled_flux_map_actions;
    coefficient_matrices_hashed+=b.coefficient_matrices_hashed;
    completed_preassembly_seconds+=b.completed_preassembly_seconds;
  }
};

// SHA256 is metadata only: row-major IEEE754 binary128 little-endian matrix
// bytes, with dimensions/dtype recorded separately. It never decides science.
struct MatrixSHA256 {
  uint32_t h[8]={0x6a09e667u,0xbb67ae85u,0x3c6ef372u,0xa54ff53au,
    0x510e527fu,0x9b05688cu,0x1f83d9abu,0x5be0cd19u};
  unsigned char block[64]{};size_t used=0;uint64_t bytes=0;
  static uint32_t rr(uint32_t x,unsigned n){return (x>>n)|(x<<(32-n));}
  void compress(){
    static constexpr uint32_t k[64]={
      0x428a2f98u,0x71374491u,0xb5c0fbcfu,0xe9b5dba5u,0x3956c25bu,0x59f111f1u,0x923f82a4u,0xab1c5ed5u,
      0xd807aa98u,0x12835b01u,0x243185beu,0x550c7dc3u,0x72be5d74u,0x80deb1feu,0x9bdc06a7u,0xc19bf174u,
      0xe49b69c1u,0xefbe4786u,0x0fc19dc6u,0x240ca1ccu,0x2de92c6fu,0x4a7484aau,0x5cb0a9dcu,0x76f988dau,
      0x983e5152u,0xa831c66du,0xb00327c8u,0xbf597fc7u,0xc6e00bf3u,0xd5a79147u,0x06ca6351u,0x14292967u,
      0x27b70a85u,0x2e1b2138u,0x4d2c6dfcu,0x53380d13u,0x650a7354u,0x766a0abbu,0x81c2c92eu,0x92722c85u,
      0xa2bfe8a1u,0xa81a664bu,0xc24b8b70u,0xc76c51a3u,0xd192e819u,0xd6990624u,0xf40e3585u,0x106aa070u,
      0x19a4c116u,0x1e376c08u,0x2748774cu,0x34b0bcb5u,0x391c0cb3u,0x4ed8aa4au,0x5b9cca4fu,0x682e6ff3u,
      0x748f82eeu,0x78a5636fu,0x84c87814u,0x8cc70208u,0x90befffau,0xa4506cebu,0xbef9a3f7u,0xc67178f2u};
    uint32_t w[64];
    for(int i=0;i<16;++i)w[i]=(uint32_t(block[4*i])<<24)|(uint32_t(block[4*i+1])<<16)|
      (uint32_t(block[4*i+2])<<8)|uint32_t(block[4*i+3]);
    for(int i=16;i<64;++i){
      const uint32_t a=rr(w[i-15],7)^rr(w[i-15],18)^(w[i-15]>>3);
      const uint32_t b=rr(w[i-2],17)^rr(w[i-2],19)^(w[i-2]>>10);
      w[i]=w[i-16]+a+w[i-7]+b;
    }
    uint32_t a=h[0],b=h[1],c=h[2],d=h[3],e=h[4],f=h[5],g=h[6],z=h[7];
    for(int i=0;i<64;++i){
      const uint32_t s1=rr(e,6)^rr(e,11)^rr(e,25),ch=(e&f)^((~e)&g);
      const uint32_t t1=z+s1+ch+k[i]+w[i],s0=rr(a,2)^rr(a,13)^rr(a,22);
      const uint32_t maj=(a&b)^(a&c)^(b&c),t2=s0+maj;
      z=g;g=f;f=e;e=d+t1;d=c;c=b;b=a;a=t1+t2;
    }
    h[0]+=a;h[1]+=b;h[2]+=c;h[3]+=d;h[4]+=e;h[5]+=f;h[6]+=g;h[7]+=z;
  }
  void add(const void *raw,size_t n){
    const auto *p=static_cast<const unsigned char*>(raw);bytes+=n;
    while(n){
      const size_t take=std::min(n,size_t(64-used));
      std::memcpy(block+used,p,take);used+=take;p+=take;n-=take;
      if(used==64){compress();used=0;}
    }
  }
  std::string finish(){
    const uint64_t bits=bytes*8;const unsigned char one=0x80,zero=0;
    add(&one,1);while(used!=56)add(&zero,1);
    unsigned char tail[8];for(int i=0;i<8;++i)tail[i]=static_cast<unsigned char>(bits>>(56-8*i));
    add(tail,8);std::ostringstream out;
    out<<std::hex<<std::setfill('0');for(uint32_t x:h)out<<std::setw(8)<<x;
    return out.str();
  }
};
struct DenseMap {
  int rows=0,columns=0;V values;
  DenseMap()=default;
  DenseMap(int r,int c):rows(r),columns(c),values(size_t(r)*c,0){}
  Q &at(int i,int j){return values[size_t(i)*columns+j];}
  Q at(int i,int j)const{return values[size_t(i)*columns+j];}
  V apply(const V &x)const{
    if(x.size()!=size_t(columns))throw std::runtime_error("preassembled-map-column-shape");
    V out(rows,0);
    for(int i=0;i<rows;++i){
      if((i&15)==0)time_check();
      for(int j=0;j<columns;++j)out[i]+=at(i,j)*x[j];
      finite_direction(out[i],"preassembled-complete-matrix-action");
    }
    return out;
  }
  void check(BatchStats &stats)const{
    for(Q x:values){finite_direction(x,"preassembled-complete-matrix-coefficient");++stats.complete_matrix_entries_checked;}
  }
  void identity(std::ostream &out,BatchStats &stats)const{
    MatrixSHA256 digest;digest.add(values.data(),values.size()*sizeof(Q));
    out<<"{\"shape\":["<<rows<<','<<columns<<"],\"bytes\":"<<values.size()*sizeof(Q)
      <<",\"dtype\":\"IEEE754-binary128-little-endian\",\"order\":\"C\",\"sha256\":"
      << ::quoted(digest.finish())<<'}';
    ++stats.coefficient_matrices_hashed;
  }
};
struct RootMaps {DenseMap momentum,L;};
struct FluxMaps {DenseMap momentum,L;};
struct PreparedField : hoisted_trace128::PreparedField {
  std::vector<RootMaps> root_maps;
  FluxMaps flux_maps;
};

// One ORIGINAL literal-gram row is acted on by the ORIGINAL C layout and s.
// No cosine-product identity, FFT, ideal theta, or Toeplitz substitution occurs.
static V gram_step_action(const Problem &p,const Q *gram,const V &step,
    BatchStats &stats){
  V out(p.J,0);out[0]=gram[0]*step[0];
  for(int j=1;j<p.J;++j)out[0]+=(p.sq2*gram[j])*step[j];
  for(int i=1;i<p.J;++i){
    out[i]=(p.sq2*gram[i])*step[0];
    for(int j=1;j<p.J;++j)out[i]+=(gram[std::abs(i-j)]+gram[i+j])*step[j];
  }
  for(Q v:out)finite_direction(v,"preassembled-literal-gram-step-action");
  stats.gram_action_rows_preassembled+=p.J;return out;
}
static RootMaps assemble_root(const Problem &p,const UpdateTape &update,
    const std::vector<hoisted_trace128::PointOperator> &rows,BatchStats &stats){
  ++stats.root_map_builds_started;const auto began=Clock::now();
  RootMaps out{DenseMap(p.J,p.M),DenseMap(p.J,p.J)};
  const Q invN=1/static_cast<Q>(p.N);
  for(int n=0;n<p.N;++n){
    if((n&3)==0)time_check();
    const Q *cs=p.cosine.data()+size_t(n)*p.J,*sn=p.sine.data()+size_t(n)*p.M,
      *gram=p.gram.data()+size_t(n)*(2*p.M+1);
    const V hg=gram_step_action(p,gram,update.solve.out,stats);
    const auto &q=rows[n].quad,&rho=rows[n].rho;
    for(int i=0;i<p.J;++i){
      // Deliberately NEW association relative to per-column R305.
      const Q wP=(cs[i]*q[0]-hg[i]*rho[0])*invN,
        wPt=(cs[i]*q[1]-hg[i]*rho[1])*invN,
        wL=(cs[i]*q[2]-hg[i]*rho[2])*invN;
      finite_direction(wP,"preassembled-wP");finite_direction(wPt,"preassembled-wPt");
      finite_direction(wL,"preassembled-wL");
      for(int j=0;j<p.M;++j)
        out.momentum.at(i,j)+=wP*sn[j]+wPt*(p.frequency[j]*cs[j+1]);
      out.L.at(i,0)+=wL; // angular_L_direction uses explicit 1, NOT cs[0].
      for(int j=1;j<p.J;++j)out.L.at(i,j)+=wL*cs[j];
    }
    ++stats.root_map_angular_rows;
  }
  out.momentum.check(stats);out.L.check(stats);
  ++stats.root_map_builds_completed;
  stats.completed_preassembly_seconds+=std::chrono::duration<double>(Clock::now()-began).count();
  return out;
}
static FluxMaps assemble_flux(const Problem &p,
    const std::vector<hoisted_trace128::PointOperator> &rows,BatchStats &stats){
  ++stats.flux_map_builds_started;const auto began=Clock::now();
  FluxMaps out{DenseMap(p.M,p.M),DenseMap(p.M,p.J)};
  const Q invN=1/static_cast<Q>(p.N);
  for(int n=0;n<p.N;++n){
    if((n&3)==0)time_check();
    const Q *cs=p.cosine.data()+size_t(n)*p.J,*sn=p.sine.data()+size_t(n)*p.M;
    const auto &f=rows[n].flux;V a(p.M),b(p.J);
    b[0]=f[2]; // separate actual angular L mean basis.
    for(int j=0;j<p.M;++j){
      const Q m=p.frequency[j];
      a[j]=f[0]*sn[j]+f[1]*(m*cs[j+1])+f[3]*(sn[j]*(m*m-1));
      b[j+1]=f[2]*cs[j+1]-f[3]*(sn[j]*m);
      finite_direction(a[j],"preassembled-final-momentum-coefficient");
      finite_direction(b[j+1],"preassembled-final-L-coefficient");
    }
    finite_direction(b[0],"preassembled-final-mean-coefficient");
    for(int i=0;i<p.M;++i){
      const Q left=sn[i]*invN;
      for(int j=0;j<p.M;++j)out.momentum.at(i,j)+=left*a[j];
      for(int j=0;j<p.J;++j)out.L.at(i,j)+=left*b[j];
    }
    ++stats.flux_map_angular_rows;
  }
  out.momentum.check(stats);out.L.check(stats);
  ++stats.flux_map_builds_completed;
  stats.completed_preassembly_seconds+=std::chrono::duration<double>(Clock::now()-began).count();
  return out;
}
static PreparedField capture_prepared(const Problem &p,const V &state,
    const Cell &cell,const Geometry &g,const Policy &policy,BatchStats &stats,
    std::ostream &trace,int stage,size_t step,int field){
  PreparedField out;
  static_cast<hoisted_trace128::PreparedField&>(out)=
    hoisted_trace128::capture_prepared(p,state,cell,g,policy,stats,trace,stage,step,field);
  for(size_t i=0;i<out.original.root.updates.size();++i){
    out.root_maps.push_back(assemble_root(p,out.original.root.updates[i],out.updates[i],stats));
    trace<<"{\"kind\":\"recorded-root-preassembled-map-identity\",\"stage\":"<<stage
      <<",\"RK_step\":"<<step<<",\"field\":"<<field<<",\"accepted_update\":"<<i
      <<",\"original_backtrack\":"<<out.original.root.updates[i].backtrack
      <<",\"momentum_map\":";out.root_maps.back().momentum.identity(trace,stats);
    trace<<",\"L_map\":";out.root_maps.back().L.identity(trace,stats);
    trace<<",\"all_literal_angular_nodes\":"<<p.N
      <<",\"nominal_factor_exactly_equals_C_not_assumed\":true"
      <<",\"reassociated_binary128_formation\":true,\"error_enclosure_supplied\":false}\n";
    if(!trace)throw std::runtime_error("preassembled-root-identity-write");
  }
  out.flux_maps=assemble_flux(p,out.final_rows,stats);
  trace<<"{\"kind\":\"recorded-final-flux-preassembled-map-identity\",\"stage\":"<<stage
    <<",\"RK_step\":"<<step<<",\"field\":"<<field<<",\"momentum_map\":";
  out.flux_maps.momentum.identity(trace,stats);
  trace<<",\"L_map\":";out.flux_maps.L.identity(trace,stats);
  trace<<",\"reassociated_binary128_formation\":true,\"error_enclosure_supplied\":false}\n";
  if(!trace)throw std::runtime_error("preassembled-flux-identity-write");
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
static V returned_L_direction(const Problem &p,const PreparedField &field,
    const InputDirection &input,BatchStats &stats){
  if(field.root_maps.size()!=field.original.root.updates.size())
    throw std::runtime_error("complete-original-root-update-map-count");
  V de(p.J,0);
  for(size_t k=0;k<field.original.root.updates.size();++k){
    time_check();const auto &u=field.original.root.updates[k];
    const auto &maps=field.root_maps[k];V dL(p.J);
    for(int j=0;j<p.J;++j)dL[j]=input.target[j]+de[j];
    const V ym=maps.momentum.apply(input.momentum),yl=maps.L.apply(dL);
    V right(p.J);
    for(int j=0;j<p.J;++j){right[j]=de[j]+ym[j]+yl[j];finite_direction(right[j],"preassembled-root-right");}
    ++stats.preassembled_root_map_actions;
    const V ds=hoisted_trace128::factor_direction_solve(u.solve,right,p.J);
    ++stats.shared_factor_direction_solves;
    for(int i=0;i<p.J;++i){
      Q residual=0;for(int j=0;j<p.J;++j)residual+=u.C[size_t(i)*p.J+j]*ds[j];
      residual-=right[i];finite_direction(residual,"complete-C-direction-readback");
      stats.direction_C_solve_residual_max=qmax(stats.direction_C_solve_residual_max,fabsq(residual));
      ++stats.complete_C_linear_residual_rows;
    }
    const Q alpha=scalbnq(1,-u.backtrack);
    for(int j=0;j<p.J;++j){de[j]=de[j]-alpha*ds[j];finite_direction(de[j],"operator-accepted-e-direction");}
    ++stats.accepted_operator_updates;
  }
  V result(p.J);
  for(int j=0;j<p.J;++j){result[j]=input.target[j]+de[j];finite_direction(result[j],"operator-returned-L-direction");}
  ++stats.root_operator_returns;++stats.final_unused_F_derivative_reductions_skipped;
  return result;
}
static V rhs_direction_operator(const Problem &p,const PreparedField &field,
    const V &direction,const Cell &cell,const Geometry &g,
    const EnvironmentDirection &env,BatchStats &stats){
  if(!hoisted_trace128::is_zero_environment(env))
    throw std::runtime_error("nonzero-environment-must-use-complete-original-fallback");
  const auto &root=field.original.root;const auto &primal=field.original.primal;
  const auto input=input_direction(p,root,direction,cell,g,env,stats);
  const V dL=returned_L_direction(p,field,input,stats);
  const V fm=field.flux_maps.momentum.apply(input.momentum),fl=field.flux_maps.L.apply(dL);
  V dflux(p.M);
  for(int j=0;j<p.M;++j){dflux[j]=fm[j]+fl[j];finite_direction(dflux[j],"preassembled-complete-flux");}
  ++stats.preassembled_flux_map_actions;
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

static void compare_requested_field(const Problem &p,const PreparedField &field,
    const V &seed,const V &actual,const Cell &cell,const Geometry &g,
    const EnvironmentDirection &env,BatchStats &stats,std::ostream &trace,
    int stage,size_t step,int field_index,int column){
  hoisted_trace128::compare_requested_field(p,field,seed,actual,cell,g,env,stats,
    trace,stage,step,field_index,column);
}
static EnvironmentDirection column_environment(const StepDirections *parameters,
    int field,int column,int columns){
  return hoisted_trace128::column_environment(parameters,field,column,columns);
}
static BatchPair rk4_batch_parameters(const Problem &p,const BatchPair &state,
    const Cell &cell,const Step &s,const Policy &policy,BatchStats &stats,
    std::ostream &trace,int stage,size_t step,const StepDirections *parameters){
  // The complete stage caller passes nullptr. Preserve the original
  // general parameter implementation rather than silently zeroing it.
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
    <<",\"integer_digit_matmul_implemented\":false"
    <<",\"full_root_derivative_error_enclosure_supplied\":false"
    <<",\"acceptance_gate\":false}";
}
} // namespace preassembled_trace128
#endif
