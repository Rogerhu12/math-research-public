// Independent batched variation of the successful frozen finite-root trace.
// Include generated from the pinned R283 source, not an approximate implicit
// root Jacobian.  This file does not set native/full-DN/audit acceptance.
#ifndef VISIBLE_NATIVE_SHARED_TRACE128_HPP
#define VISIBLE_NATIVE_SHARED_TRACE128_HPP
#include "native_frozen_trace128_prefix.inc"
#include <filesystem>
#include <utility>

namespace shared_trace128 {
using namespace trace_variation;
namespace fs=std::filesystem;

struct UpdateTape {
  V e,C;
  RootEval evaluated;
  SolveTape solve;
  int backtrack;
};
struct RootTape {
  V state,target,final_e;
  RootSolution returned;
  std::vector<UpdateTape> updates;
  bool fallback=false;
};
struct BatchStats {
  RootStats primal;
  VariationStats variation;
  uint64_t tapes=0,column_returns=0,shared_primal_factorizations=0,
    RK_steps=0,completed_column_steps=0;
  void join(const BatchStats &b){
    primal.join(b.primal);variation.join(b.variation);
    tapes+=b.tapes;column_returns+=b.column_returns;
    shared_primal_factorizations+=b.shared_primal_factorizations;
    RK_steps+=b.RK_steps;completed_column_steps+=b.completed_column_steps;
  }
};
static V read128(const fs::path &name,size_t words){
  if(fs::file_size(name)!=words*sizeof(Q))throw std::runtime_error("binary128-input-size");
  std::ifstream f(name,std::ios::binary);
  V v(words);if(!f.read(reinterpret_cast<char*>(v.data()),words*sizeof(Q)))
    throw std::runtime_error("binary128-input-read");
  for(Q x:v)finite(x,"binary128-input");
  return v;
}
static void raw128(const fs::path &name,const V &v){
  std::ofstream f(name,std::ios::binary|std::ios::trunc);
  if(!f.write(reinterpret_cast<const char*>(v.data()),v.size()*sizeof(Q)))
    throw std::runtime_error("binary128-output-write");
}
static void json_file(const fs::path &name,const std::string &v){
  std::ofstream f(name,std::ios::binary|std::ios::trunc);
  if(!(f<<v<<'\n'))throw std::runtime_error("JSON-output-write");
}
static void action_guard(){
  if(!std::getenv("GITHUB_ACTIONS")||std::string(std::getenv("GITHUB_ACTIONS"))!="true")
    throw std::runtime_error("public-Actions-science-only");
  uint32_t word=1;
  if(*reinterpret_cast<unsigned char*>(&word)!=1||std::fegetround()!=FE_TONEAREST)
    throw std::runtime_error("little-endian-round-to-nearest-required");
}

// Exactly one authoritative primal root branch search per field.  Only
// actually accepted updates are retained.  Their F, C and Cholesky/forward
// solve values precede the accepted e update, as in the frozen R283 loop.
static RootTape capture_root(const Problem &p,const V &state,const Cell &cell,
    const Geometry &g,const Policy &policy,BatchStats &stats,
    std::ostream &trace,int stage,size_t step,int field){
  ++stats.primal.calls;++stats.tapes;
  RootTape tape;tape.state=state;tape.target.assign(p.J,0);
  V e(p.J,0);
  const Q r2=g.r*g.r,r4=r2*r2,
    fac=static_cast<Q>(p.orientation)*p.sq12*cell.mu/(p.sq2*r4*g.w2);
  Q target_scale=static_cast<Q>(1e-300);
  for(int j=0;j<p.M;++j){
    tape.target[j+1]=fac*state[p.M+j];
    target_scale=qmax(target_scale,fabsq(tape.target[j+1]));
  }
  std::ostringstream record;
  record<<"{\"stage\":"<<stage<<",\"RK_step\":"<<step<<",\"field\":"<<field
    <<",\"root_call_in_stage\":"<<stats.primal.calls<<",\"events\":[";
  bool first=true,original_seen=false;
  const auto event=[&](const std::string &s){if(!first)record<<',';first=false;record<<s;};
  const auto finish_record=[&](bool returned,bool fallback,const std::string &error){
    record<<"],\"accepted_update_count\":"<<tape.updates.size()
      <<",\"primal_return_selected\":"<<(returned?"true":"false")
      <<",\"fallback\":"<<(fallback?"true":"false")<<",\"error\":"
      <<(error.empty()?"null":quoted(error))<<"}";
    trace<<record.str()<<'\n';if(!trace)throw std::runtime_error("root-tape-log-write");
  };
  try{
    for(int it=0;it<30;++it){
      auto ev=root_evaluate(p,e,tape.target,state,g,stats.primal);
      const Q scale=qmax(target_scale,ev.max_quad),relative=ev.err/scale;
      stats.primal.max_iterations=std::max(stats.primal.max_iterations,it);
      if(!original_seen&&ev.err<=p.original_stop*scale){
        original_seen=true;++stats.primal.original_threshold_reached;
        stats.primal.max_original_stop_relative=qmax(stats.primal.max_original_stop_relative,relative);
      }
      event("{\"kind\":\"iterate\",\"iteration\":"+std::to_string(it)+
        ",\"error\":"+quoted(qstr(ev.err))+",\"scale\":"+quoted(qstr(scale))+
        ",\"relative\":"+quoted(qstr(relative))+
        ",\"normal_stop_selected\":"+(ev.err<=policy.stop*scale?"true":"false")+"}");
      const auto finish=[&](bool fallback){
        if(tape.updates.size()>29)throw std::runtime_error("successful-root-update-count");
        if(fallback)++stats.primal.fallbacks;
        stats.primal.max_returned_relative=qmax(stats.primal.max_returned_relative,relative);
        stats.primal.returned_minD=std::min(stats.primal.returned_minD,ev.minD);
        stats.primal.returned_minS=std::min(stats.primal.returned_minS,ev.minS);
        stats.primal.returned_minA=std::min(stats.primal.returned_minA,ev.minA);
        V L(p.J);for(int j=0;j<p.J;++j)L[j]=tape.target[j]+e[j];
        tape.final_e=e;tape.returned={std::move(L),std::move(ev)};tape.fallback=fallback;
        finish_record(true,fallback,"");return std::move(tape);
      };
      if(ev.err<=policy.stop*scale)return finish(false);
      V C=root_matrix(p,g,ev.rows);
      SolveTape solve=spd_solve_taped(C,ev.residual,p.J);
      ++stats.primal.newton_steps;++stats.shared_primal_factorizations;
      bool accepted=false;int accepted_k=-1;V accepted_trial;
      for(int k=0;k<20;++k){
        ++stats.primal.line_trials;const Q alpha=scalbnq(1,-k);V trial(p.J);
        for(int j=0;j<p.J;++j)trial[j]=e[j]-alpha*solve.out[j];
        try{
          auto value=root_evaluate(p,trial,tape.target,state,g,stats.primal);
          const bool chosen=value.err<ev.err||value.err<=policy.stop*scale;
          event("{\"kind\":\"trial\",\"iteration\":"+std::to_string(it)+
            ",\"backtrack\":"+std::to_string(k)+",\"error\":"+quoted(qstr(value.err))+
            ",\"current_scale\":"+quoted(qstr(scale))+
            ",\"domain_returned\":true,\"accepted\":"+(chosen?"true":"false")+"}");
          if(chosen){accepted_trial=std::move(trial);accepted=true;accepted_k=k;break;}
        }catch(const std::runtime_error &error){
          if(std::string(error.what())=="explicit-experiment-time-budget")throw;
          if(std::string(error.what()).rfind("momentum-branch-D-S-A-rejected",0)!=0)throw;
          event("{\"kind\":\"trial\",\"iteration\":"+std::to_string(it)+
            ",\"backtrack\":"+std::to_string(k)+
            ",\"domain_returned\":false,\"accepted\":false,\"error\":"+quoted(error.what())+"}");
        }
      }
      if(!accepted){
        if(ev.err<=policy.fallback*scale)return finish(true);
        throw std::runtime_error("momentum-Newton-line-search-failed");
      }
      tape.updates.push_back({e,std::move(C),std::move(ev),std::move(solve),accepted_k});
      e=std::move(accepted_trial);
    }
    throw std::runtime_error("momentum-Newton-iteration-limit");
  }catch(const std::exception &error){finish_record(false,false,error.what());throw;}
}

// Each column reuses the recorded branch, root values and Cholesky tape.
// F/C shadows still repeat their literal value expressions to retain R283's
// word checks.  We therefore claim shared root searches/factorizations, not
// elimination of every repeated value operation.
static RootVariation replay_root(const Problem &p,const RootTape &tape,
    const V &direction,const Cell &cell,const Geometry &g,BatchStats &stats){
  V dt(p.J,0),de(p.J,0);
  const Q r2=g.r*g.r,r4=r2*r2,
    fac=static_cast<Q>(p.orientation)*p.sq12*cell.mu/(p.sq2*r4*g.w2);
  for(int j=0;j<p.M;++j){dt[j+1]=fac*direction[p.M+j];finite_direction(dt[j+1],"root-target");}
  for(const auto &u:tape.updates){
    time_check();
    auto fd=F_direction(p,u.e,de,tape.target,dt,tape.state,direction,g,u.evaluated,stats.variation);
    const V dC=C_direction(p,g,u.evaluated.rows,fd.rows,u.C,stats.variation);
    const V dstep=spd_solve_direction(u.solve,dC,fd.residual,p.J,stats.variation);
    const Q alpha=scalbnq(1,-u.backtrack);
    for(int j=0;j<p.J;++j){de[j]=de[j]-alpha*dstep[j];finite_direction(de[j],"accepted-e-update");}
    ++stats.variation.accepted_updates_differentiated;
    ++stats.variation.accepted_backtrack_count[u.backtrack];
  }
  V dL(p.J);
  for(int j=0;j<p.J;++j){dL[j]=dt[j]+de[j];finite_direction(dL[j],"returned-L");}
  auto fd=F_direction(p,tape.final_e,de,tape.target,dt,tape.state,direction,g,tape.returned.evaluated,stats.variation);
  ++stats.variation.primal_returns_selected;++stats.variation.joint_root_returns;
  ++stats.variation.returned_update_count[tape.updates.size()];
  if(tape.updates.empty())++stats.variation.zero_update_returns;
  ++stats.column_returns;
  return {tape.returned,std::move(dL),std::move(fd.rows)};
}

struct FieldTape {RootTape root;RHSPrimal primal;};
static FieldTape capture_field(const Problem &p,const V &state,const Cell &cell,
    const Geometry &g,const Policy &policy,BatchStats &stats,std::ostream &trace,
    int stage,size_t step,int field){
  RootTape rt=capture_root(p,state,cell,g,policy,stats,trace,stage,step,field);
  auto value=rhs_from_root(p,state,cell,g,rt.returned);
  return {std::move(rt),std::move(value)};
}
static V rhs_direction(const Problem &p,const FieldTape &tape,const V &direction,
    const Cell &cell,const Geometry &g,BatchStats &stats){
  const auto rt=replay_root(p,tape.root,direction,cell,g,stats);
  const auto &state=tape.root.state;const auto &primal=tape.primal;
  DV derivative(p.size,D(0)),flux(p.M,D(0));
  const Q invN=1/static_cast<Q>(p.N),r3=g.r*g.r*g.r,
    sigma=g.dr/g.r,pref=static_cast<Q>(p.orientation)*p.sq2*r3*g.dr*g.w2/(p.sq12*cell.mu);
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();
    const auto v=pair_row(rt.value.evaluated.rows[n],rt.drows[n]);
    const D u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),
      factor=(v.K+u/(1+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd),f=v.U*factor;
    const Q *sn=p.sine.data()+size_t(n)*p.M;
    for(int j=0;j<p.M;++j)flux[j]+=f*sn[j]*invN;
  }
  for(int j=0;j<p.M;++j){
    const Q m=p.frequency[j];
    const D y(state[j],direction[j]),pi(state[p.M+j],direction[p.M+j]),
      L(rt.value.L[j+1],rt.dL[j+1]),pj=-m*r3*y/(p.sq2*g.w),linear=-m*L+(m*m-1)*pj;
    same_value(flux[j].v,primal.flux[j],stats.variation,"RHS-flux");
    derivative[j]=sigma*((m*m-4)*y+p.sq2*g.w*L/r3);
    derivative[p.M+j]=4*sigma*pi+pref*m*(linear+flux[j]);
  }
  derivative[p.K]=g.dr*g.w*D(rt.value.L[0],rt.dL[0]);derivative[p.K+1]=D(g.dr*g.w,0);
  V result(p.size);
  for(int j=0;j<p.size;++j){
    same_value(derivative[j].v,primal.derivative[j],stats.variation,"complete-RHS");
    finite_direction(derivative[j].d,"complete-RHS");result[j]=derivative[j].d;
  }
  return result;
}

// Derivatives are row-major [226, columns].  The four primal field inputs
// follow the original RK parentheses before any derivative is replayed.
struct BatchPair {V value,direction;int columns;};
static BatchPair rk4_batch(const Problem &p,const BatchPair &state,const Cell &cell,
    const Step &s,const Policy &policy,BatchStats &stats,std::ostream &trace,
    int stage,size_t step){
  const auto a=capture_field(p,state.value,cell,s.g[0],policy,stats,trace,stage,step,0);
  V t(p.size);
  for(int j=0;j<p.size;++j)t[j]=state.value[j]+s.h*a.primal.derivative[j]/2;
  const auto b=capture_field(p,t,cell,s.g[1],policy,stats,trace,stage,step,1);
  for(int j=0;j<p.size;++j)t[j]=state.value[j]+s.h*b.primal.derivative[j]/2;
  const auto c=capture_field(p,t,cell,s.g[1],policy,stats,trace,stage,step,2);
  for(int j=0;j<p.size;++j)t[j]=state.value[j]+s.h*c.primal.derivative[j];
  const auto d=capture_field(p,t,cell,s.g[2],policy,stats,trace,stage,step,3);
  BatchPair out{V(p.size),V(size_t(p.size)*state.columns),state.columns};
  for(int j=0;j<p.size;++j){
    out.value[j]=state.value[j]+s.h*(a.primal.derivative[j]+2*b.primal.derivative[j]+2*c.primal.derivative[j]+d.primal.derivative[j])/6;
    finite(out.value[j],"RK4-state");
  }
  for(int col=0;col<state.columns;++col){
    time_check();V seed(p.size),tangent(p.size);
    for(int j=0;j<p.size;++j)seed[j]=state.direction[size_t(j)*state.columns+col];
    const V da=rhs_direction(p,a,seed,cell,s.g[0],stats);
    for(int j=0;j<p.size;++j)tangent[j]=seed[j]+s.h*da[j]/2;
    const V db=rhs_direction(p,b,tangent,cell,s.g[1],stats);
    for(int j=0;j<p.size;++j)tangent[j]=seed[j]+s.h*db[j]/2;
    const V dc=rhs_direction(p,c,tangent,cell,s.g[1],stats);
    for(int j=0;j<p.size;++j)tangent[j]=seed[j]+s.h*dc[j];
    const V dd=rhs_direction(p,d,tangent,cell,s.g[2],stats);
    for(int j=0;j<p.size;++j){
      const Q v=seed[j]+s.h*(da[j]+2*db[j]+2*dc[j]+dd[j])/6;
      finite_direction(v,"RK4-state");out.direction[size_t(j)*state.columns+col]=v;
    }
    ++stats.completed_column_steps;
  }
  ++stats.RK_steps;return out;
}

static void print_stats(std::ostream &o,const BatchStats &s){
  o<<"{\"root_tapes\":"<<s.tapes<<",\"direction_column_returns\":"<<s.column_returns
    <<",\"shared_primal_factorizations\":"<<s.shared_primal_factorizations
    <<",\"completed_RK_steps\":"<<s.RK_steps<<",\"completed_column_steps\":"<<s.completed_column_steps
    <<",\"primal\":";print_root_stats(o,s.primal);
  o<<",\"variation\":";print_variation_stats(o,s.variation);o<<'}';
}
} // namespace shared_trace128
#endif
