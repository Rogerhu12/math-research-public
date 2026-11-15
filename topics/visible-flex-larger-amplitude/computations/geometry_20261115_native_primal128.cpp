// Request113: full finite native primal evaluation in IEEE binary128.
// Original binary64 inputs/tables/profile samples are lifted exactly.  No
// scientific acceptance or native final-J/audit is supplied by this program.
#include <quadmath.h>
#include <algorithm>
#include <atomic>
#include <chrono>
#include <cfenv>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>
#include <omp.h>

using Q = __float128;
using V = std::vector<Q>;
using Clock = std::chrono::steady_clock;
static_assert(sizeof(Q) == 16 && FLT128_MANT_DIG == 113,
              "Request113 requires genuine IEEE binary128, not long double.");
static_assert(sizeof(double) == 8 && std::numeric_limits<double>::digits == 53,
              "Input words must be binary64.");
static Clock::time_point deadline;
struct TeeBuffer : std::streambuf {
  std::streambuf *a,*b;
  TeeBuffer(std::streambuf *aa,std::streambuf *bb):a(aa),b(bb){}
  int overflow(int c) override {
    if(c==traits_type::eof())return traits_type::not_eof(c);
    return a->sputc(c)==traits_type::eof()||b->sputc(c)==traits_type::eof()?traits_type::eof():c;
  }
  std::streamsize xsputn(const char *s,std::streamsize n) override {
    const auto x=a->sputn(s,n),y=b->sputn(s,n);return std::min(x,y);
  }
  int sync() override {return a->pubsync()||b->pubsync()?-1:0;}
};
static std::string qstr(Q x) {
  char b[192];
  if (quadmath_snprintf(b, sizeof b, "%.36Qg", x) < 0)
    throw std::runtime_error("binary128 decimal formatting failed");
  return std::string(b);
}
static std::string qhex(Q x) {
  char b[192];
  if (quadmath_snprintf(b, sizeof b, "%Qa", x) < 0)
    throw std::runtime_error("binary128 hex formatting failed");
  return std::string(b);
}
static std::string quoted(const std::string &x) {
  std::string r = "\"";
  for (unsigned char c : x) {
    if (c == '"' || c == '\\') { r += '\\'; r += char(c); }
    else if (c == '\n') r += "\\n";
    else if (c == '\r') r += "\\r";
    else if (c == '\t') r += "\\t";
    else if (c >= 32 && c < 127) r += char(c);
    else r += '?';
  }
  return r + '"';
}
static void time_check() {
  if (Clock::now() >= deadline) throw std::runtime_error("explicit-experiment-time-budget");
}
static void finite(Q x, const char *where) {
  if (!finiteq(x)) throw std::runtime_error(std::string("nonfinite-") + where);
}
static Q qmax(Q a, Q b) { return a > b ? a : b; }

struct Input {
  std::ifstream file;
  explicit Input(const std::string &name) : file(name, std::ios::binary) {
    if (!file) throw std::runtime_error("input-open");
    const uint32_t x = 1;
    if (*reinterpret_cast<const unsigned char *>(&x) != 1)
      throw std::runtime_error("little-endian-input-required");
  }
  void bytes(void *p, size_t n) {
    if (!file.read(static_cast<char *>(p), n)) throw std::runtime_error("input-short");
  }
  uint32_t u32() { uint32_t x; bytes(&x, 4); return x; }
  double f64() {
    double x; bytes(&x, 8);
    if (!std::isfinite(x)) throw std::runtime_error("nonfinite-input-word");
    return x;
  }
  V words(size_t n) {
    V r(n);
    for (size_t i = 0; i < n; ++i) r[i] = static_cast<Q>(f64());
    return r;
  }
};
struct Geometry { Q r, dr, w, w2, E; };
struct Step { Q h; Geometry g[3]; };
struct Cell { Q mu, ratio; std::vector<Step> steps; };
struct Problem {
  int M, J, K, size, N, depth, orientation;
  Q sq2, sq12, floor, outer_tol, original_stop, original_fallback;
  V frequency, cosine, sine, gram, base, delta, target, scales, far;
  std::vector<Cell> cells;
  explicit Problem(const std::string &filename) {
    Input in(filename); char magic[8]; in.bytes(magic, 8);
    if (std::memcmp(magic, "QPR11301", 8)) throw std::runtime_error("packet-magic");
    M = in.u32(); N = in.u32(); depth = in.u32();
    const int flag = in.u32(); orientation = flag == 1 ? 1 : flag == 2 ? -1 : 0;
    if (M != 112 || depth != 576 || N <= 4*M*2 || N > 65536 || orientation == 0)
      throw std::runtime_error("actual-complete-112-by576-layout");
    J=M+1; K=2*M; size=K+2;
    sq2=in.f64(); sq12=in.f64(); floor=in.f64(); outer_tol=in.f64();
    original_stop=in.f64(); original_fallback=in.f64();
    if (!(sq2>0 && sq12>0 && floor>0 && outer_tol>0 &&
          original_stop>0 && original_fallback>=original_stop))
      throw std::runtime_error("positive-original-constants");
    frequency=in.words(M); cosine=in.words(size_t(N)*J);
    sine=in.words(size_t(N)*M); gram=in.words(size_t(N)*(2*M+1));
    base=in.words(size_t(depth+1)*K); delta=in.words(size_t(depth+1)*K);
    target=in.words(M); scales=in.words(depth+1); far=in.words(M);
    for (Q s:scales) if (!(s>0)) throw std::runtime_error("positive-original-scales");
    for (int n=0;n<depth;++n) {
      Cell c; c.mu=in.f64(); c.ratio=in.f64(); const uint32_t count=in.u32();
      if (!(c.mu>0 && c.ratio>0) || count==0 || count>100000)
        throw std::runtime_error("actual-cell-layout");
      for (uint32_t k=0;k<count;++k) {
        Step s; s.h=in.f64();
        if (s.h==0) throw std::runtime_error("zero-original-RK-step");
        for (auto &g:s.g) {
          g={in.f64(),in.f64(),in.f64(),in.f64(),in.f64()};
          if (!(g.r>0 && g.dr!=0 && g.w>0 && g.w2>0 && g.E>0))
            throw std::runtime_error("original-profile-range");
        }
        c.steps.push_back(s);
      }
      cells.push_back(std::move(c));
    }
    char extra;
    if (in.file.read(&extra,1)) throw std::runtime_error("unparsed-packet-suffix");
  }
};
struct RootStats {
  uint64_t calls=0, evaluations=0, newton_steps=0, line_trials=0,
           fallbacks=0, original_threshold_reached=0;
  int max_iterations=0;
  Q max_returned_relative=0, max_original_stop_relative=0;
  Q minD=FLT128_MAX, minS=FLT128_MAX, minA=FLT128_MAX;
  Q returned_minD=FLT128_MAX, returned_minS=FLT128_MAX, returned_minA=FLT128_MAX;
  void join(const RootStats &s) {
    calls+=s.calls; evaluations+=s.evaluations; newton_steps+=s.newton_steps;
    line_trials+=s.line_trials; fallbacks+=s.fallbacks;
    original_threshold_reached+=s.original_threshold_reached;
    max_iterations=std::max(max_iterations,s.max_iterations);
    max_returned_relative=qmax(max_returned_relative,s.max_returned_relative);
    max_original_stop_relative=qmax(max_original_stop_relative,s.max_original_stop_relative);
    minD=std::min(minD,s.minD); minS=std::min(minS,s.minS); minA=std::min(minA,s.minA);
    returned_minD=std::min(returned_minD,s.returned_minD);
    returned_minS=std::min(returned_minS,s.returned_minS);
    returned_minA=std::min(returned_minA,s.returned_minA);
  }
};
struct Angular { Q P, Pt, L, K, U, S, D, A, sd, quad; };
struct RootEval { V residual; std::vector<Angular> rows; Q err=0, max_quad=0,
  minD=FLT128_MAX,minS=FLT128_MAX,minA=FLT128_MAX; };
struct RootSolution { V L; RootEval evaluated; };
struct Policy { const char *label; Q stop, fallback; };

// e is the unknown L-target.  F(e)=e+quad(target+e,Qstate).
// This change is algebraic; no cancellation-prone (L+quad)-target is formed.
static RootEval root_evaluate(const Problem &p, const V &e, const V &target,
                             const V &Qstate, const Geometry &g,
                             RootStats &stats) {
  time_check(); ++stats.evaluations;
  V L(p.J), momentum(p.M), pt(p.J,0);
  const Q r3=g.r*g.r*g.r;
  for (int j=0;j<p.J;++j) L[j]=target[j]+e[j];
  for (int j=0;j<p.M;++j) {
    momentum[j]=-p.frequency[j]*r3*Qstate[j]/(p.sq2*g.w);
    pt[j+1]=p.frequency[j]*momentum[j];
  }
  RootEval result; result.residual.assign(p.J,0); result.rows.resize(p.N);
  const Q invN=1/static_cast<Q>(p.N);
  for (int n=0;n<p.N;++n) {
    if ((n&31)==0) time_check();
    Q P=0,Pt=0,Lv=L[0],U=0;
    const Q *cs=p.cosine.data()+size_t(n)*p.J;
    const Q *sn=p.sine.data()+size_t(n)*p.M;
    for (int j=0;j<p.M;++j) {
      const Q m=p.frequency[j];
      P+=momentum[j]*sn[j]; Pt+=pt[j+1]*cs[j+1]; Lv+=L[j+1]*cs[j+1];
      U+=(-m*L[j+1]+(m*m-1)*momentum[j])*sn[j];
    }
    const Q K=Lv-Pt, T=2*K+K*K+g.E*P*P, u=g.w2*T,
            D=1-u, S=1-g.w2*P*P, A=1+Lv+g.w2*Pt;
    if (!(D>p.floor && S>p.floor && A>p.floor))
      throw std::runtime_error("momentum-branch-D-S-A-rejected angle="+std::to_string(n)+
        " D="+qstr(D)+" S="+qstr(S)+" A="+qstr(A));
    const Q sd=sqrtq(D), fc=u*(2+sd)/(2*sd*(1+sd)*(1+sd)),
            gc=g.w2*(P*P+S*T/(1+sd))/(S*sd),
            quad=(K*K+g.E*P*P)/2+K*Pt+T*fc+(1+K)*Pt*gc;
    finite(quad,"root-quadratic");
    result.max_quad=qmax(result.max_quad,fabsq(quad));
    stats.minD=std::min(stats.minD,D); stats.minS=std::min(stats.minS,S); stats.minA=std::min(stats.minA,A);
    result.minD=std::min(result.minD,D);result.minS=std::min(result.minS,S);result.minA=std::min(result.minA,A);
    for (int i=0;i<p.J;++i) result.residual[i]+=quad*cs[i]*invN;
    result.rows[n]={P,Pt,Lv,K,U,S,D,A,sd,quad};
  }
  for (int j=0;j<p.J;++j) {
    result.residual[j]+=e[j];
    finite(result.residual[j],"root-residual"); result.err=qmax(result.err,fabsq(result.residual[j]));
  }
  return result;
}
static V root_matrix(const Problem &p,const Geometry &g,const std::vector<Angular> &rows){
  // The root Gram matrix is needed only after a failed residual stop.  Reuse
  // exactly those binary128 angular rows; do not re-run the nonlinear field.
  V bm(2*p.M+1,0),B(size_t(p.J)*p.J,0);
  const Q invN=1/static_cast<Q>(p.N);
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();
    const auto &v=rows[n];
    const Q u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),am=v.L+g.w2*v.Pt,
      dm=u*(v.sd+1/(1+v.sd))/(v.D*v.sd),value=am+(1+am)*dm;
    const Q *gc=p.gram.data()+size_t(n)*(2*p.M+1);
    for(int k=0;k<=2*p.M;++k)bm[k]+=value*gc[k]*invN;
  }
  for(int i=0;i<p.J;++i)for(int j=0;j<=i;++j){
    const Q v=(i==j?1:0)+(j==0?(i==0?bm[0]:p.sq2*bm[i]):bm[i-j]+bm[i+j]);
    B[size_t(i)*p.J+j]=v;B[size_t(j)*p.J+i]=v;
  }
  return B;
}
static V spd_solve(const V &B, const V &b, int n) {
  V L(size_t(n)*n,0),tmp(n),out(n);
  for (int i=0;i<n;++i) for (int j=0;j<=i;++j) {
    Q v=B[size_t(i)*n+j];
    for (int k=0;k<j;++k) v-=L[size_t(i)*n+k]*L[size_t(j)*n+k];
    if (i==j) {
      if (!(v>0)) throw std::runtime_error("momentum-Newton-matrix-not-SPD");
      L[size_t(i)*n+j]=sqrtq(v);
    } else L[size_t(i)*n+j]=v/L[size_t(j)*n+j];
  }
  for (int i=0;i<n;++i) {
    Q v=b[i]; for (int j=0;j<i;++j) v-=L[size_t(i)*n+j]*tmp[j];
    tmp[i]=v/L[size_t(i)*n+i];
  }
  for (int i=n-1;i>=0;--i) {
    Q v=tmp[i]; for (int j=i+1;j<n;++j) v-=L[size_t(j)*n+i]*out[j];
    out[i]=v/L[size_t(i)*n+i]; finite(out[i],"root-Newton-step");
  }
  return out;
}
static RootSolution root(const Problem &p, const V &state, const Cell &cell,
                         const Geometry &g, const Policy &policy, RootStats &stats) {
  ++stats.calls;
  V target(p.J,0),e(p.J,0);
  const Q r2=g.r*g.r,r4=r2*r2,
          fac=static_cast<Q>(p.orientation)*p.sq12*cell.mu/(p.sq2*r4*g.w2);
  Q target_scale=static_cast<Q>(1e-300);
  for (int j=0;j<p.M;++j) {
    target[j+1]=fac*state[p.M+j]; target_scale=qmax(target_scale,fabsq(target[j+1]));
  }
  bool original_seen=false;
  for (int it=0;it<30;++it) {
    auto ev=root_evaluate(p,e,target,state,g,stats);
    const Q scale=qmax(target_scale,ev.max_quad),relative=ev.err/scale;
    stats.max_iterations=std::max(stats.max_iterations,it);
    if (!original_seen && ev.err<=p.original_stop*scale) {
      original_seen=true; ++stats.original_threshold_reached;
      stats.max_original_stop_relative=qmax(stats.max_original_stop_relative,relative);
    }
    auto finish=[&](bool fallback) {
      if (fallback) ++stats.fallbacks;
      stats.max_returned_relative=qmax(stats.max_returned_relative,relative);
      stats.returned_minD=std::min(stats.returned_minD,ev.minD);
      stats.returned_minS=std::min(stats.returned_minS,ev.minS);
      stats.returned_minA=std::min(stats.returned_minA,ev.minA);
      V L(p.J); for(int j=0;j<p.J;++j) L[j]=target[j]+e[j];
      return RootSolution{std::move(L),std::move(ev)};
    };
    if (ev.err<=policy.stop*scale) return finish(false);
    const V step=spd_solve(root_matrix(p,g,ev.rows),ev.residual,p.J); ++stats.newton_steps;
    bool accepted=false;
    for (int k=0;k<20;++k) {
      ++stats.line_trials; const Q alpha=scalbnq(1,-k); V trial(p.J);
      for (int j=0;j<p.J;++j) trial[j]=e[j]-alpha*step[j];
      try {
        auto value=root_evaluate(p,trial,target,state,g,stats);
        if (value.err<ev.err || value.err<=policy.stop*scale) {
          e=std::move(trial); accepted=true; break;
        }
      } catch (const std::runtime_error &error) {
        if (std::string(error.what())=="explicit-experiment-time-budget") throw;
        if (std::string(error.what()).rfind("momentum-branch-D-S-A-rejected",0)!=0) throw;
      }
    }
    if (!accepted) {
      if (ev.err<=policy.fallback*scale) return finish(true);
      throw std::runtime_error("momentum-Newton-line-search-failed");
    }
  }
  throw std::runtime_error("momentum-Newton-iteration-limit");
}
static V rhs(const Problem &p, const V &state, const Cell &cell,
             const Geometry &g, const Policy &policy, RootStats &stats) {
  auto rt=root(p,state,cell,g,policy,stats);
  V derivative(p.size,0),flux(p.M,0);
  const Q invN=1/static_cast<Q>(p.N), r3=g.r*g.r*g.r,
          sigma=g.dr/g.r, pref=static_cast<Q>(p.orientation)*p.sq2*r3*g.dr*g.w2/(p.sq12*cell.mu);
  for (int n=0;n<p.N;++n) {
    if((n&31)==0)time_check();
    const auto &v=rt.evaluated.rows[n];
    const Q u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),
            factor=(v.K+u/(1+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd), f=v.U*factor;
    const Q *sn=p.sine.data()+size_t(n)*p.M;
    for (int j=0;j<p.M;++j) flux[j]+=f*sn[j]*invN;
  }
  for (int j=0;j<p.M;++j) {
    const Q m=p.frequency[j], pj=-m*r3*state[j]/(p.sq2*g.w),
            linear=-m*rt.L[j+1]+(m*m-1)*pj;
    derivative[j]=sigma*((m*m-4)*state[j]+p.sq2*g.w*rt.L[j+1]/r3);
    derivative[p.M+j]=4*sigma*state[p.M+j]+pref*m*(linear+flux[j]);
  }
  derivative[2*p.M]=g.dr*g.w*rt.L[0]; derivative[2*p.M+1]=g.dr*g.w;
  for(Q x:derivative) finite(x,"complete-RHS");
  return derivative;
}
static V rk4(const Problem &p,const V &state,const Cell &cell,const Step &s,
             const Policy &policy,RootStats &stats) {
  const auto a=rhs(p,state,cell,s.g[0],policy,stats); V t(p.size);
  for(int j=0;j<p.size;++j)t[j]=state[j]+s.h*a[j]/2;
  const auto b=rhs(p,t,cell,s.g[1],policy,stats);
  for(int j=0;j<p.size;++j)t[j]=state[j]+s.h*b[j]/2;
  const auto c=rhs(p,t,cell,s.g[1],policy,stats);
  for(int j=0;j<p.size;++j)t[j]=state[j]+s.h*c[j];
  const auto d=rhs(p,t,cell,s.g[2],policy,stats);
  V out(p.size);
  for(int j=0;j<p.size;++j){out[j]=state[j]+s.h*(a[j]+2*b[j]+2*c[j]+d[j])/6;finite(out[j],"RK4-state");}
  return out;
}
struct Evaluation {
  V residual; std::vector<std::string> errors; RootStats stats;
  size_t stages_completed=0, rows_completed=0, worst=0;
  Q norm=0, worst_residual=0, mean_total=0;
  bool complete=false,budget=false;
};
static Evaluation evaluate(const Problem &p,Q alpha,const Policy &policy,int threads) {
  const size_t dimension=size_t(p.depth+1)*p.K;
  V states(dimension);
  // No binary64 rounding of either the step or the updated node state.
  for(size_t i=0;i<dimension;++i) states[i]=alpha==0?p.base[i]:p.base[i]+alpha*p.delta[i];
  Evaluation out; out.residual.assign(dimension,nanq("")); out.errors.resize(p.depth);
  std::vector<RootStats> per_stage(p.depth); V means(p.depth,0);
  for(int j=0;j<p.M;++j) {
    out.residual[j]=states[j]-p.target[j];
    out.residual[p.M+size_t(p.depth)*p.K+j]=states[size_t(p.depth)*p.K+p.M+j]-p.far[j]*states[size_t(p.depth)*p.K+j];
  }
  #pragma omp parallel for schedule(dynamic,1) num_threads(threads)
  for(int n=0;n<p.depth;++n) {
    try {
      time_check(); V y(p.size,0);
      for(int j=0;j<p.K;++j)y[j]=states[size_t(n+1)*p.K+j];
      for(const auto &s:p.cells[n].steps)y=rk4(p,y,p.cells[n],s,policy,per_stage[n]);
      for(int j=0;j<p.K;++j){
        const Q v=j<p.M?y[j]:y[j]/p.cells[n].ratio;
        out.residual[p.M+size_t(n)*p.K+j]=v-states[size_t(n)*p.K+j];
      }
      means[n]=y[p.K]+y[p.K+1];
    }catch(const std::exception &error){out.errors[n]=error.what();}
  }
  out.rows_completed=2*p.M;
  for(int n=0;n<p.depth;++n){
    out.stats.join(per_stage[n]);out.mean_total+=means[n];
    if(out.errors[n].empty()){++out.stages_completed;out.rows_completed+=p.K;}
    if(out.errors[n]=="explicit-experiment-time-budget")out.budget=true;
  }
  out.complete=out.stages_completed==size_t(p.depth);
  if(out.complete)for(size_t row=0;row<dimension;++row){
    const size_t stage=row<size_t(p.M)?0:row>=size_t(p.M)+size_t(p.depth)*p.K?p.depth:(row-p.M)/p.K;
    const Q r=out.residual[row],v=fabsq(r)/p.scales[stage];finite(v,"complete-shooting-residual");
    if(v>out.norm){out.norm=v;out.worst=row;out.worst_residual=r;}
  }
  return out;
}
static void write_raw(const std::string &file,const V &values){
  std::ofstream f(file,std::ios::binary|std::ios::trunc);
  if(!f || !f.write(reinterpret_cast<const char*>(values.data()),values.size()*sizeof(Q)))
    throw std::runtime_error("temporary-binary128-output-write");
}
static void print_result(const Problem &p,const Evaluation &ev,const Policy &policy,
                         int trial,Q alpha,Q base_norm,bool base_valid,
                         const std::string &raw,double seconds){
  std::cout<<"NATIVE113 {\"event\":\"native113_complete_primal_evaluation\",\"policy\":"<<quoted(policy.label)
   <<",\"trial\":"<<trial<<",\"alpha\":"<<quoted(qstr(alpha))
   <<",\"all_rows\":"<<(size_t(p.depth+1)*p.K)<<",\"rows_completed\":"<<ev.rows_completed
   <<",\"stages_completed\":"<<ev.stages_completed<<",\"complete\":"<<(ev.complete?"true":"false")
   <<",\"experiment_budget_exhausted\":"<<(ev.budget?"true":"false")
   <<",\"root_stop\":"<<quoted(qstr(policy.stop))<<",\"root_fallback\":"<<quoted(qstr(policy.fallback))
   <<",\"temporary_residual_file\":"<<quoted(raw)<<",\"temporary_residual_bytes\":"<<ev.residual.size()*sizeof(Q)
   <<",\"elapsed_seconds\":"<<std::setprecision(17)<<seconds;
  if(ev.complete){
    std::cout<<",\"norm_decimal\":"<<quoted(qstr(ev.norm))<<",\"norm_binary128_hex\":"<<quoted(qhex(ev.norm))
     <<",\"worst_original_row\":"<<ev.worst<<",\"worst_residual_decimal\":"<<quoted(qstr(ev.worst_residual))
     <<",\"worst_residual_binary128_hex\":"<<quoted(qhex(ev.worst_residual))
     <<",\"below_original_native_tolerance\":"<<(ev.norm<p.outer_tol?"true":"false")
     <<",\"strict_decrease_from_same_policy_base\":"<<(trial>=0&&base_valid?(ev.norm<base_norm?"true":"false"):"null")
     <<",\"mean_height_sum_decimal\":"<<quoted(qstr(ev.mean_total));
  }else std::cout<<",\"norm_decimal\":null,\"strict_decrease_from_same_policy_base\":null";
  const auto &s=ev.stats;
  std::cout<<",\"root_statistics\":{\"calls\":"<<s.calls<<",\"angular_evaluations\":"<<s.evaluations
   <<",\"Newton_steps\":"<<s.newton_steps<<",\"line_search_trials\":"<<s.line_trials
   <<",\"fallback_returns\":"<<s.fallbacks<<",\"maximum_iterations\":"<<s.max_iterations
   <<",\"max_returned_relative_decimal\":"<<quoted(qstr(s.max_returned_relative))
   <<",\"original_threshold_reached_count\":"<<s.original_threshold_reached
   <<",\"max_first_original_stop_relative_decimal\":"<<quoted(qstr(s.max_original_stop_relative))
   <<",\"min_D_over_all_valid_root_evaluations\":"<<quoted(qstr(s.minD))
   <<",\"min_S_over_all_valid_root_evaluations\":"<<quoted(qstr(s.minS))
   <<",\"min_A_over_all_valid_root_evaluations\":"<<quoted(qstr(s.minA))
   <<",\"min_D_over_returned_RHS_roots\":"<<quoted(qstr(s.returned_minD))
   <<",\"min_S_over_returned_RHS_roots\":"<<quoted(qstr(s.returned_minS))
   <<",\"min_A_over_returned_RHS_roots\":"<<quoted(qstr(s.returned_minA))<<"},\"failed_stages\":[";
  bool first=true;size_t failures=0;
  for(size_t n=0;n<ev.errors.size();++n)if(!ev.errors[n].empty()){
    if(failures<8){if(!first)std::cout<<',';first=false;std::cout<<"["<<n<<","<<quoted(ev.errors[n])<<"]";}
    ++failures;
  }
  std::cout<<"],\"failed_stage_detail_limit\":8,\"failed_stage_count\":"<<failures<<",\"all_failed_stage_indices\":[";
  first=true;
  for(size_t n=0;n<ev.errors.size();++n)if(!ev.errors[n].empty()){
    if(!first)std::cout<<',';first=false;std::cout<<n;
  }
  std::cout<<"],\"native_accepted\":false,\"new_final_J_or_audit_supplied\":false}"<<std::endl;
}
int main(int argc,char **argv){
  const auto previous_buffer=std::cout.rdbuf();
  std::unique_ptr<std::ofstream> report;
  std::unique_ptr<TeeBuffer> tee;
  int status=0;
  try{
    const char *ga=std::getenv("GITHUB_ACTIONS"),*repo=std::getenv("GITHUB_REPOSITORY");
    if(!ga||std::string(ga)!="true"||!repo||std::string(repo)!="Rogerhu12/math-research-public")
      throw std::runtime_error("public-repository-Actions-only");
    if(std::fegetround()!=FE_TONEAREST)throw std::runtime_error("round-to-nearest-required");
    if(argc!=5)throw std::runtime_error("usage: evaluator packet output-directory seconds threads");
    report=std::make_unique<std::ofstream>(std::string(argv[2])+"/evaluation-records.jsonl",std::ios::binary|std::ios::trunc);
    if(!*report)throw std::runtime_error("temporary-evaluation-report-open");
    tee=std::make_unique<TeeBuffer>(previous_buffer,report->rdbuf());std::cout.rdbuf(tee.get());
    const int seconds=std::stoi(argv[3]),threads=std::stoi(argv[4]);
    if(seconds<60||seconds>14400||threads<1||threads>4)throw std::runtime_error("explicit-experiment-budget");
    deadline=Clock::now()+std::chrono::seconds(seconds);
    Problem p(argv[1]);
    const Policy policies[]={
      {"binary128-e-original-inner-stop",p.original_stop,p.original_fallback},
      {"binary128-e-refined-inner-stop",strtoflt128("1e-28",nullptr),strtoflt128("5e-27",nullptr)}};
    std::cout<<"NATIVE113 {\"event\":\"native113_binary128_implementation\",\"storage_bytes\":"<<sizeof(Q)
     <<",\"mantissa_bits\":"<<FLT128_MANT_DIG<<",\"threads\":"<<threads
     <<",\"experiment_seconds\":"<<seconds<<",\"node_state_trial_root_rhs_RK_residual_binary128\":true,"
     <<"\"geometry_angular_graph_scale_inputs_are_lifted_original_binary64\":true,"
     <<"\"original64_J_is_only_direction_producer_not_new128_exact_J\":true,"
     <<"\"native_accepted\":false}"<<std::endl;
    int done=0;bool exhausted=false;
    Q baseline[2]={0,0};bool baseline_valid[2]={false,false};
    // Interleave policies so both full baselines precede later trial costs.
    for(int trial=-1;trial<10&&!exhausted;++trial){
      for(int pi=0;pi<2;++pi){
        if(Clock::now()>=deadline){exhausted=true;break;}
        const Q alpha=trial<0?0:scalbnq(1,-trial);
        auto started=Clock::now();auto ev=evaluate(p,alpha,policies[pi],threads);
        const std::string name=std::string(argv[2])+"/policy-"+std::to_string(pi)+"-trial-"+std::to_string(trial)+".f128";
        write_raw(name,ev.residual);
        print_result(p,ev,policies[pi],trial,alpha,baseline[pi],baseline_valid[pi],name,
          std::chrono::duration<double>(Clock::now()-started).count());
        ++done;
        if(trial<0){baseline[pi]=ev.norm;baseline_valid[pi]=ev.complete;}
        if(ev.budget){exhausted=true;break;}
      }
    }
    std::cout<<"NATIVE113 {\"event\":\"native113_binary128_finished\",\"evaluations_reported\":"<<done
     <<",\"all22_requested_evaluations_reported\":"<<(done==22?"true":"false")
     <<",\"experiment_budget_exhausted\":"<<(exhausted?"true":"false")
     <<",\"budget_expiry_is_not_a_scientific_failure\":true,\"native_accepted\":false}"<<std::endl;
  }catch(const std::exception &error){
    std::cout<<"NATIVE113 {\"event\":\"native113_evaluator_error\",\"error\":"<<quoted(error.what())
     <<",\"native_accepted\":false}"<<std::endl;status=2;
  }
  std::cout.flush();std::cout.rdbuf(previous_buffer);
  return status;
}
