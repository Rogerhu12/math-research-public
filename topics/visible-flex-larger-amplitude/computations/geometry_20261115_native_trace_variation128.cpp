// Independent R283 directional variation of a successful finite root trace.
// The frozen113 primal source is included unchanged.  This program supplies
// neither a native solve nor endpoint J / physical sensitivity / final audit.
#define main frozen_native_primal113_main_not_called
#include "geometry_20261115_native_primal128.cpp"
#undef main
#include <array>
#include <sstream>

namespace trace_variation {
static constexpr const char *original_cpp_sha256 =
    "1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d";

// The value operation is the original arithmetic primitive; the direction is
// a numerical chain-rule evaluation for its real-expression extension.  In
// particular no derivative of an IEEE rounding operation is asserted.
struct D {
  Q v, d;
  D(Q value=0, Q direction=0):v(value),d(direction){}
};
static D operator+(D a,D b){return {a.v+b.v,a.d+b.d};}
static D operator-(D a,D b){return {a.v-b.v,a.d-b.d};}
static D operator-(D a){return {-a.v,-a.d};}
static D operator*(D a,D b){return {a.v*b.v,a.d*b.v+a.v*b.d};}
static D operator/(D a,D b){
  const Q value=a.v/b.v;
  return {value,(a.d-value*b.d)/b.v};
}
static D &operator+=(D &a,D b){a=a+b;return a;}
static D dsqrt(D a){const Q value=sqrtq(a.v);return {value,a.d/(2*value)};}
using DV=std::vector<D>;
struct DAngular {D P,Pt,L,K,U,S,Dv,A,sd,quad;};
struct VariationStats {
  uint64_t F_direction_calls=0,C_direction_calls=0,factor_direction_calls=0,
    forward_direction_calls=0,backward_direction_calls=0,
    primal_returns_selected=0,joint_root_returns=0,zero_update_returns=0,
    accepted_updates_differentiated=0,shadow_words_checked=0,shadow_word_mismatches=0;
  std::array<uint64_t,30> returned_update_count{};
  std::array<uint64_t,20> accepted_backtrack_count{};
  void join(const VariationStats &s){
    F_direction_calls+=s.F_direction_calls;C_direction_calls+=s.C_direction_calls;
    factor_direction_calls+=s.factor_direction_calls;
    forward_direction_calls+=s.forward_direction_calls;
    backward_direction_calls+=s.backward_direction_calls;
    primal_returns_selected+=s.primal_returns_selected;joint_root_returns+=s.joint_root_returns;
    zero_update_returns+=s.zero_update_returns;
    accepted_updates_differentiated+=s.accepted_updates_differentiated;
    shadow_words_checked+=s.shadow_words_checked;shadow_word_mismatches+=s.shadow_word_mismatches;
    for(size_t i=0;i<returned_update_count.size();++i)returned_update_count[i]+=s.returned_update_count[i];
    for(size_t i=0;i<accepted_backtrack_count.size();++i)accepted_backtrack_count[i]+=s.accepted_backtrack_count[i];
  }
};
static void same_value(Q shadow,Q original,VariationStats &stats,const char *where){
  ++stats.shadow_words_checked;
  if(std::memcmp(&shadow,&original,sizeof(Q))!=0){
    ++stats.shadow_word_mismatches;
    throw std::runtime_error(std::string("primal-shadow-word-mismatch:")+where);
  }
}
static void finite_direction(Q x,const char *where){
  if(!finiteq(x))throw std::runtime_error(std::string("nonfinite-trace-direction:")+where);
}
struct FDirection {V residual;std::vector<Angular> rows;};

// Same finite angular expressions and accumulation order as root_evaluate.
// The authoritative domain tests and root choices remain in the included
// primal root_evaluate.  This shadow is evaluated only at an actually used
// root iterate and checked against every original returned row and F word.
static FDirection F_direction(const Problem &p,const V &e,const V &de,
    const V &target,const V &dt,const V &state,const V &direction,
    const Geometry &g,const RootEval &original,VariationStats &stats){
  time_check();++stats.F_direction_calls;
  DV L(p.J),momentum(p.M),pt(p.J,D(0));
  const Q r3=g.r*g.r*g.r;
  for(int j=0;j<p.J;++j)L[j]=D(target[j],dt[j])+D(e[j],de[j]);
  for(int j=0;j<p.M;++j){
    momentum[j]=-p.frequency[j]*r3*D(state[j],direction[j])/(p.sq2*g.w);
    pt[j+1]=p.frequency[j]*momentum[j];
  }
  DV residual(p.J,D(0));FDirection result;result.rows.resize(p.N);result.residual.resize(p.J);
  const Q invN=1/static_cast<Q>(p.N);
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();
    D P=0,Pt=0,Lv=L[0],U=0;
    const Q *cs=p.cosine.data()+size_t(n)*p.J;
    const Q *sn=p.sine.data()+size_t(n)*p.M;
    for(int j=0;j<p.M;++j){
      const Q m=p.frequency[j];
      P+=momentum[j]*sn[j];Pt+=pt[j+1]*cs[j+1];Lv+=L[j+1]*cs[j+1];
      U+=(-m*L[j+1]+(m*m-1)*momentum[j])*sn[j];
    }
    const D K=Lv-Pt,T=2*K+K*K+g.E*P*P,u=g.w2*T,
      DD=1-u,S=1-g.w2*P*P,A=1+Lv+g.w2*Pt;
    const D sd=dsqrt(DD),fc=u*(2+sd)/(2*sd*(1+sd)*(1+sd)),
      gc=g.w2*(P*P+S*T/(1+sd))/(S*sd),
      quad=(K*K+g.E*P*P)/2+K*Pt+T*fc+(1+K)*Pt*gc;
    const std::array<D,10> shadow={P,Pt,Lv,K,U,S,DD,A,sd,quad};
    const auto &v=original.rows[n];
    const std::array<Q,10> values={v.P,v.Pt,v.L,v.K,v.U,v.S,v.D,v.A,v.sd,v.quad};
    for(size_t i=0;i<shadow.size();++i){
      same_value(shadow[i].v,values[i],stats,"F-angular-row");
      finite_direction(shadow[i].d,"F-angular-row");
    }
    for(int i=0;i<p.J;++i)residual[i]+=quad*cs[i]*invN;
    result.rows[n]={P.d,Pt.d,Lv.d,K.d,U.d,S.d,DD.d,A.d,sd.d,quad.d};
  }
  for(int j=0;j<p.J;++j){
    residual[j]+=D(e[j],de[j]);
    same_value(residual[j].v,original.residual[j],stats,"F-residual");
    finite_direction(residual[j].d,"F-residual");result.residual[j]=residual[j].d;
  }
  return result;
}
static DAngular pair_row(const Angular &v,const Angular &d){
  return {{v.P,d.P},{v.Pt,d.Pt},{v.L,d.L},{v.K,d.K},{v.U,d.U},
    {v.S,d.S},{v.D,d.D},{v.A,d.A},{v.sd,d.sd},{v.quad,d.quad}};
}

// C is differentiated from root_matrix itself, with its independent gram
// table.  C is never substituted for F_e, nor rebuilt using cosine products.
static V C_direction(const Problem &p,const Geometry &g,
    const std::vector<Angular> &rows,const std::vector<Angular> &directions,
    const V &original,VariationStats &stats){
  ++stats.C_direction_calls;
  DV bm(2*p.M+1,D(0));V result(size_t(p.J)*p.J,0);
  const Q invN=1/static_cast<Q>(p.N);
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();
    const auto v=pair_row(rows[n],directions[n]);
    const D u=g.w2*(2*v.K+v.K*v.K+g.E*v.P*v.P),am=v.L+g.w2*v.Pt,
      dm=u*(v.sd+1/(1+v.sd))/(v.Dv*v.sd),value=am+(1+am)*dm;
    const Q *gc=p.gram.data()+size_t(n)*(2*p.M+1);
    for(int k=0;k<=2*p.M;++k)bm[k]+=value*gc[k]*invN;
  }
  for(int i=0;i<p.J;++i)for(int j=0;j<=i;++j){
    const D v=D(i==j?1:0)+(j==0?(i==0?bm[0]:p.sq2*bm[i]):bm[i-j]+bm[i+j]);
    same_value(v.v,original[size_t(i)*p.J+j],stats,"C-lower-triangle");
    same_value(v.v,original[size_t(j)*p.J+i],stats,"C-symmetric-entry");
    finite_direction(v.d,"C-entry");
    result[size_t(i)*p.J+j]=v.d;result[size_t(j)*p.J+i]=v.d;
  }
  return result;
}

struct SolveTape {V L,tmp,out;};
// Verbatim primal loops from frozen spd_solve, with only its return object
// extended to retain the actual factor and forward solution.  No second
// primal factorisation or implicit C^{-1}(dF-dC*s) replacement is performed.
static SolveTape spd_solve_taped(const V &B, const V &b, int n) {
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
  return {std::move(L),std::move(tmp),std::move(out)};
}
static V spd_solve_direction(const SolveTape &tape,const V &dB,const V &db,
    int n,VariationStats &stats){
  const V &L=tape.L,&tmp=tape.tmp,&out=tape.out;
  V dL(size_t(n)*n,0),dtmp(n),dout(n);
  ++stats.factor_direction_calls;
  for(int i=0;i<n;++i){
    if((i&15)==0)time_check();
    for(int j=0;j<=i;++j){
      Q dv=dB[size_t(i)*n+j];
      for(int k=0;k<j;++k)
        dv-=dL[size_t(i)*n+k]*L[size_t(j)*n+k]+L[size_t(i)*n+k]*dL[size_t(j)*n+k];
      if(i==j)dL[size_t(i)*n+j]=dv/(2*L[size_t(i)*n+i]);
      else dL[size_t(i)*n+j]=(dv-L[size_t(i)*n+j]*dL[size_t(j)*n+j])/L[size_t(j)*n+j];
      finite_direction(dL[size_t(i)*n+j],"Cholesky");
    }
  }
  ++stats.forward_direction_calls;
  for(int i=0;i<n;++i){
    Q dv=db[i];
    for(int j=0;j<i;++j)dv-=dL[size_t(i)*n+j]*tmp[j]+L[size_t(i)*n+j]*dtmp[j];
    dtmp[i]=(dv-tmp[i]*dL[size_t(i)*n+i])/L[size_t(i)*n+i];
    finite_direction(dtmp[i],"forward-substitution");
  }
  ++stats.backward_direction_calls;
  for(int i=n-1;i>=0;--i){
    Q dv=dtmp[i];
    for(int j=i+1;j<n;++j)dv-=dL[size_t(j)*n+i]*out[j]+L[size_t(j)*n+i]*dout[j];
    dout[i]=(dv-out[i]*dL[size_t(i)*n+i])/L[size_t(i)*n+i];
    finite_direction(dout[i],"back-substitution");
  }
  return dout;
}
struct RootVariation {RootSolution value;V dL;std::vector<Angular> drows;};

// The primal choices below are the original root choices.  A derivative is
// propagated only after an alpha has actually been accepted.  Rejected
// candidate evaluations are recorded but do not create derivative updates.
static RootVariation root_variation(const Problem &p,const V &state,const V &direction,
    const Cell &cell,const Geometry &g,const Policy &policy,RootStats &stats,
    VariationStats &variation,std::ostream &trace,int stage,size_t step,int field){
  ++stats.calls;
  V target(p.J,0),e(p.J,0),dt(p.J,0),de(p.J,0);
  const Q r2=g.r*g.r,r4=r2*r2,
          fac=static_cast<Q>(p.orientation)*p.sq12*cell.mu/(p.sq2*r4*g.w2);
  Q target_scale=static_cast<Q>(1e-300);
  for(int j=0;j<p.M;++j){
    target[j+1]=fac*state[p.M+j];target_scale=qmax(target_scale,fabsq(target[j+1]));
    dt[j+1]=fac*direction[p.M+j];finite_direction(dt[j+1],"root-target");
  }
  std::ostringstream record;
  record<<"{\"stage\":"<<stage<<",\"RK_step\":"<<step<<",\"field\":"<<field
    <<",\"root_call_in_stage\":"<<stats.calls<<",\"events\":[";
  bool first=true,original_seen=false,return_selected=false;int updates=0;
  const auto event=[&](const std::string &s){if(!first)record<<',';first=false;record<<s;};
  const auto write_record=[&](bool complete,const char *kind,const std::string &error){
    record<<"],\"accepted_update_count\":"<<updates<<",\"primal_return_selected\":"
      <<(return_selected?"true":"false")<<",\"complete_directional_return\":"<<(complete?"true":"false")
      <<",\"return_kind\":"<<quoted(kind)<<",\"error\":"<<(error.empty()?"null":quoted(error))<<"}";
    trace<<record.str()<<'\n';
    if(!trace)throw std::runtime_error("temporary-root-trace-write");
  };
  try{
    for(int it=0;it<30;++it){
      auto ev=root_evaluate(p,e,target,state,g,stats);
      const Q scale=qmax(target_scale,ev.max_quad),relative=ev.err/scale;
      stats.max_iterations=std::max(stats.max_iterations,it);
      if(!original_seen&&ev.err<=p.original_stop*scale){
        original_seen=true;++stats.original_threshold_reached;
        stats.max_original_stop_relative=qmax(stats.max_original_stop_relative,relative);
      }
      event("{\"kind\":\"iterate\",\"iteration\":"+std::to_string(it)+
        ",\"error\":"+quoted(qstr(ev.err))+",\"scale\":"+quoted(qstr(scale))+
        ",\"relative\":"+quoted(qstr(relative))+
        ",\"normal_stop_selected\":"+(ev.err<=policy.stop*scale?"true":"false")+"}");
      auto finish=[&](bool fallback){
        return_selected=true;++variation.primal_returns_selected;
        if(fallback)++stats.fallbacks;
        stats.max_returned_relative=qmax(stats.max_returned_relative,relative);
        stats.returned_minD=std::min(stats.returned_minD,ev.minD);
        stats.returned_minS=std::min(stats.returned_minS,ev.minS);
        stats.returned_minA=std::min(stats.returned_minA,ev.minA);
        V L(p.J),dL(p.J);
        for(int j=0;j<p.J;++j){L[j]=target[j]+e[j];dL[j]=dt[j]+de[j];finite_direction(dL[j],"returned-L");}
        auto fd=F_direction(p,e,de,target,dt,state,direction,g,ev,variation);
        ++variation.joint_root_returns;if(updates==0)++variation.zero_update_returns;
        if(updates<0||updates>29)throw std::runtime_error("successful-root-update-count");
        ++variation.returned_update_count[updates];
        write_record(true,fallback?"original-fallback":"normal","");
        return RootVariation{{std::move(L),std::move(ev)},std::move(dL),std::move(fd.rows)};
      };
      if(ev.err<=policy.stop*scale)return finish(false);
      const V C=root_matrix(p,g,ev.rows);
      const SolveTape tape=spd_solve_taped(C,ev.residual,p.J);const V &step_value=tape.out;
      ++stats.newton_steps;
      bool accepted=false;int accepted_k=-1;V accepted_trial;
      for(int k=0;k<20;++k){
        ++stats.line_trials;const Q alpha=scalbnq(1,-k);V trial(p.J);
        for(int j=0;j<p.J;++j)trial[j]=e[j]-alpha*step_value[j];
        try{
          auto value=root_evaluate(p,trial,target,state,g,stats);
          const bool chosen=value.err<ev.err||value.err<=policy.stop*scale;
          event("{\"kind\":\"trial\",\"iteration\":"+std::to_string(it)+
            ",\"backtrack\":"+std::to_string(k)+",\"error\":"+quoted(qstr(value.err))+
            ",\"current_scale\":"+quoted(qstr(scale))+",\"domain_returned\":true,\"accepted\":"+
            (chosen?"true":"false")+"}");
          if(chosen){accepted_trial=std::move(trial);accepted=true;accepted_k=k;break;}
        }catch(const std::runtime_error &error){
          if(std::string(error.what())=="explicit-experiment-time-budget")throw;
          if(std::string(error.what()).rfind("momentum-branch-D-S-A-rejected",0)!=0)throw;
          event("{\"kind\":\"trial\",\"iteration\":"+std::to_string(it)+
            ",\"backtrack\":"+std::to_string(k)+",\"domain_returned\":false,\"accepted\":false,\"error\":"+
            quoted(error.what())+"}");
        }
      }
      if(!accepted){
        if(ev.err<=policy.fallback*scale)return finish(true);
        throw std::runtime_error("momentum-Newton-line-search-failed");
      }
      // Differentiate the OLD actual F and C, then the actual taped solve.
      // No ideal implicit root response and no derivative through comparisons.
      const auto fd=F_direction(p,e,de,target,dt,state,direction,g,ev,variation);
      const V dC=C_direction(p,g,ev.rows,fd.rows,C,variation);
      const V dstep=spd_solve_direction(tape,dC,fd.residual,p.J,variation);
      const Q alpha=scalbnq(1,-accepted_k);
      for(int j=0;j<p.J;++j){de[j]=de[j]-alpha*dstep[j];finite_direction(de[j],"accepted-e-update");}
      e=std::move(accepted_trial);++updates;++variation.accepted_updates_differentiated;
      ++variation.accepted_backtrack_count[accepted_k];
    }
    throw std::runtime_error("momentum-Newton-iteration-limit");
  }catch(const std::exception &error){write_record(false,"failed",error.what());throw;}
}

struct RHSPrimal {V derivative,flux;};
// Original RHS after its root call.  Capturing flux extends only the return
// object; every primal arithmetic expression below is frozen113's expression.
static RHSPrimal rhs_from_root(const Problem &p, const V &state, const Cell &cell,
             const Geometry &g, const RootSolution &rt) {
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
  return {std::move(derivative),std::move(flux)};
}
struct Pair {V value,direction;};
static Pair rhs_variation(const Problem &p,const Pair &state,const Cell &cell,
    const Geometry &g,const Policy &policy,RootStats &stats,VariationStats &variation,
    std::ostream &trace,int stage,size_t step,int field){
  auto rt=root_variation(p,state.value,state.direction,cell,g,policy,stats,variation,trace,stage,step,field);
  auto primal=rhs_from_root(p,state.value,cell,g,rt.value);
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
    const D y(state.value[j],state.direction[j]),pi(state.value[p.M+j],state.direction[p.M+j]),
      L(rt.value.L[j+1],rt.dL[j+1]),pj=-m*r3*y/(p.sq2*g.w),linear=-m*L+(m*m-1)*pj;
    same_value(flux[j].v,primal.flux[j],variation,"RHS-flux");
    derivative[j]=sigma*((m*m-4)*y+p.sq2*g.w*L/r3);
    derivative[p.M+j]=4*sigma*pi+pref*m*(linear+flux[j]);
  }
  derivative[p.K]=g.dr*g.w*D(rt.value.L[0],rt.dL[0]);derivative[p.K+1]=D(g.dr*g.w,0);
  V result(p.size);
  for(int j=0;j<p.size;++j){
    same_value(derivative[j].v,primal.derivative[j],variation,"complete-RHS");
    finite_direction(derivative[j].d,"complete-RHS");result[j]=derivative[j].d;
  }
  return {std::move(primal.derivative),std::move(result)};
}
static Pair rk4_variation(const Problem &p,const Pair &state,const Cell &cell,const Step &s,
    const Policy &policy,RootStats &stats,VariationStats &variation,
    std::ostream &trace,int stage,size_t step){
  const auto a=rhs_variation(p,state,cell,s.g[0],policy,stats,variation,trace,stage,step,0);
  Pair t{V(p.size),V(p.size)};
  for(int j=0;j<p.size;++j){t.value[j]=state.value[j]+s.h*a.value[j]/2;t.direction[j]=state.direction[j]+s.h*a.direction[j]/2;}
  const auto b=rhs_variation(p,t,cell,s.g[1],policy,stats,variation,trace,stage,step,1);
  for(int j=0;j<p.size;++j){t.value[j]=state.value[j]+s.h*b.value[j]/2;t.direction[j]=state.direction[j]+s.h*b.direction[j]/2;}
  const auto c=rhs_variation(p,t,cell,s.g[1],policy,stats,variation,trace,stage,step,2);
  for(int j=0;j<p.size;++j){t.value[j]=state.value[j]+s.h*c.value[j];t.direction[j]=state.direction[j]+s.h*c.direction[j];}
  const auto d=rhs_variation(p,t,cell,s.g[2],policy,stats,variation,trace,stage,step,3);
  Pair out{V(p.size),V(p.size)};
  for(int j=0;j<p.size;++j){
    out.value[j]=state.value[j]+s.h*(a.value[j]+2*b.value[j]+2*c.value[j]+d.value[j])/6;
    out.direction[j]=state.direction[j]+s.h*(a.direction[j]+2*b.direction[j]+2*c.direction[j]+d.direction[j])/6;
    finite(out.value[j],"RK4-state");finite_direction(out.direction[j],"RK4-state");
  }
  return out;
}

struct JointEvaluation {
  V states,residual,action,stage_output,stage_direction;
  std::vector<std::string> errors,trace_files;
  std::string readback_error;
  std::vector<RootStats> root_by_stage;
  std::vector<VariationStats> variation_by_stage;
  RootStats root;VariationStats variation;
  size_t stages_completed=0,rows_completed=0,worst=0,action_worst=0,affine_worst=0;
  Q norm=0,action_norm=0,affine_norm=0,mean_total=0,mean_direction=0;
  bool complete=false,budget=false;
};
static size_t sigma_index(const Problem &p,size_t row){
  return row<size_t(p.M)?0:row>=size_t(p.M)+size_t(p.depth)*p.K?p.depth:(row-p.M)/p.K;
}
static JointEvaluation evaluate_direction(const Problem &p,Q alpha,const Policy &policy,
    int threads,const std::string &directory){
  const size_t dimension=size_t(p.depth+1)*p.K;
  JointEvaluation out;out.states.resize(dimension);
  for(size_t i=0;i<dimension;++i)out.states[i]=alpha==0?p.base[i]:p.base[i]+alpha*p.delta[i];
  out.residual.assign(dimension,nanq(""));out.action.assign(dimension,nanq(""));
  out.stage_output.assign(size_t(p.depth)*p.size,nanq(""));out.stage_direction=out.stage_output;
  out.errors.resize(p.depth);out.trace_files.resize(p.depth);
  out.root_by_stage.resize(p.depth);out.variation_by_stage.resize(p.depth);
  for(int j=0;j<p.M;++j){
    out.residual[j]=out.states[j]-p.target[j];out.action[j]=p.delta[j];
    const size_t farrow=p.M+size_t(p.depth)*p.K+j,farq=size_t(p.depth)*p.K+j;
    out.residual[farrow]=out.states[farq+p.M]-p.far[j]*out.states[farq];
    out.action[farrow]=p.delta[farq+p.M]-p.far[j]*p.delta[farq];
    finite_direction(out.action[farrow],"far-boundary");
  }
  #pragma omp parallel for schedule(dynamic,1) num_threads(threads)
  for(int n=0;n<p.depth;++n){
    try{
      time_check();
      const std::string name="root-trace-stage-"+std::to_string(n)+".jsonl";
      std::ofstream trace(directory+"/"+name,std::ios::binary|std::ios::trunc);
      if(!trace)throw std::runtime_error("temporary-root-trace-open");out.trace_files[n]=name;
      Pair y{V(p.size,0),V(p.size,0)};
      for(int j=0;j<p.K;++j){y.value[j]=out.states[size_t(n+1)*p.K+j];y.direction[j]=p.delta[size_t(n+1)*p.K+j];}
      for(size_t k=0;k<p.cells[n].steps.size();++k)
        y=rk4_variation(p,y,p.cells[n],p.cells[n].steps[k],policy,out.root_by_stage[n],out.variation_by_stage[n],trace,n,k);
      trace.flush();if(!trace)throw std::runtime_error("temporary-root-trace-flush");
      for(int j=0;j<p.size;++j){out.stage_output[size_t(n)*p.size+j]=y.value[j];out.stage_direction[size_t(n)*p.size+j]=y.direction[j];}
      for(int j=0;j<p.K;++j){
        const Q v=j<p.M?y.value[j]:y.value[j]/p.cells[n].ratio;
        const Q dv=j<p.M?y.direction[j]:y.direction[j]/p.cells[n].ratio;
        const size_t row=p.M+size_t(n)*p.K+j;
        out.residual[row]=v-out.states[size_t(n)*p.K+j];out.action[row]=dv-p.delta[size_t(n)*p.K+j];
        finite(out.residual[row],"shooting-stage");finite_direction(out.action[row],"shooting-stage");
      }
    }catch(const std::exception &error){out.errors[n]=error.what();}
  }
  out.rows_completed=2*p.M;
  for(int n=0;n<p.depth;++n){
    out.root.join(out.root_by_stage[n]);out.variation.join(out.variation_by_stage[n]);
    if(out.errors[n].empty()){
      ++out.stages_completed;out.rows_completed+=p.K;
      out.mean_total+=out.stage_output[size_t(n)*p.size+p.K]+out.stage_output[size_t(n)*p.size+p.K+1];
      out.mean_direction+=out.stage_direction[size_t(n)*p.size+p.K]+out.stage_direction[size_t(n)*p.size+p.K+1];
    }
    if(out.errors[n]=="explicit-experiment-time-budget")out.budget=true;
  }
  out.complete=out.stages_completed==size_t(p.depth);
  if(out.complete)try{
    for(size_t row=0;row<dimension;++row){
      const Q sigma=p.scales[sigma_index(p,row)],r=out.residual[row],a=out.action[row];
      const Q rn=fabsq(r)/sigma,an=fabsq(a)/sigma,en=fabsq(r+a)/sigma;
      finite(rn,"complete-primal-norm");finite_direction(an,"complete-direction-norm");finite_direction(en,"complete-affine-norm");
      if(rn>out.norm){out.norm=rn;out.worst=row;}if(an>out.action_norm){out.action_norm=an;out.action_worst=row;}
      if(en>out.affine_norm){out.affine_norm=en;out.affine_worst=row;}
    }
  }catch(const std::exception &error){
    // Keep all already computed original rows and trace files even when a
    // normalized scalar readback overflows.  That is not a native verdict.
    out.readback_error=error.what();out.complete=false;
  }
  return out;
}
static void print_root_stats(std::ostream &o,const RootStats &s){
  o<<"{\"calls\":"<<s.calls<<",\"angular_evaluations\":"<<s.evaluations
    <<",\"Newton_steps\":"<<s.newton_steps<<",\"line_search_trials\":"<<s.line_trials
    <<",\"fallback_returns\":"<<s.fallbacks<<",\"maximum_iterations\":"<<s.max_iterations
    <<",\"original_threshold_reached_count\":"<<s.original_threshold_reached
    <<",\"max_returned_relative_decimal\":"<<quoted(qstr(s.max_returned_relative))
    <<",\"min_D_over_returned_RHS_roots\":"<<(s.returned_minD==FLT128_MAX?"null":quoted(qstr(s.returned_minD)))
    <<",\"min_S_over_returned_RHS_roots\":"<<(s.returned_minS==FLT128_MAX?"null":quoted(qstr(s.returned_minS)))
    <<",\"min_A_over_returned_RHS_roots\":"<<(s.returned_minA==FLT128_MAX?"null":quoted(qstr(s.returned_minA)))<<"}";
}
static void print_variation_stats(std::ostream &o,const VariationStats &s){
  o<<"{\"F_direction_calls\":"<<s.F_direction_calls<<",\"C_direction_calls\":"<<s.C_direction_calls
    <<",\"factor_direction_calls\":"<<s.factor_direction_calls<<",\"forward_direction_calls\":"<<s.forward_direction_calls
    <<",\"backward_direction_calls\":"<<s.backward_direction_calls<<",\"primal_returns_selected\":"<<s.primal_returns_selected
    <<",\"joint_root_returns\":"<<s.joint_root_returns<<",\"zero_update_returns\":"<<s.zero_update_returns
    <<",\"accepted_updates_differentiated\":"<<s.accepted_updates_differentiated
    <<",\"shadow_words_checked\":"<<s.shadow_words_checked<<",\"shadow_word_mismatches\":"<<s.shadow_word_mismatches
    <<",\"successful_return_update_count_0_to_29\":[";
  for(size_t i=0;i<s.returned_update_count.size();++i){if(i)o<<',';o<<s.returned_update_count[i];}
  o<<"],\"accepted_backtrack_count_0_to_19\":[";
  for(size_t i=0;i<s.accepted_backtrack_count.size();++i){if(i)o<<',';o<<s.accepted_backtrack_count[i];}
  o<<"]}";
}
static void print_row(std::ostream &o,const Problem &p,const JointEvaluation &ev,size_t row){
  const size_t n=sigma_index(p,row);const Q r=ev.residual[row],a=ev.action[row],s=p.scales[n];
  o<<"{\"row\":"<<row<<",\"sigma_index\":"<<n<<",\"sigma_decimal\":"<<quoted(qstr(s));
  if(row<size_t(p.M))o<<",\"kind\":\"cut\",\"Q_mode_one_based\":"<<row+1;
  else if(row>=size_t(p.M)+size_t(p.depth)*p.K)
    o<<",\"kind\":\"far\",\"mode_one_based\":"<<row-p.M-size_t(p.depth)*p.K+1;
  else{
    const size_t c=(row-p.M)%p.K;
    o<<",\"kind\":\"stage\",\"stage\":"<<n<<",\"input_node\":"<<n+1<<",\"output_node\":"<<n
      <<",\"component\":"<<quoted(c<size_t(p.M)?"Q":"Pi")<<",\"mode_one_based\":"<<c%p.M+1;
  }
  o<<",\"primal_residual_decimal\":"<<quoted(qstr(r))<<",\"primal_residual_binary128_hex\":"<<quoted(qhex(r))
    <<",\"directional_action_decimal\":"<<quoted(qstr(a))<<",\"directional_action_binary128_hex\":"<<quoted(qhex(a))
    <<",\"primal_normalized_decimal\":"<<quoted(qstr(r/s))
    <<",\"directional_normalized_decimal\":"<<quoted(qstr(a/s))
    <<",\"unit_step_affine_normalized_decimal\":"<<quoted(qstr((r+a)/s))<<"}";
}
static std::string report(const Problem &p,const JointEvaluation &ev,Q alpha,const Policy &policy,
    int threads,int seconds,double elapsed){
  std::ostringstream o;
  o<<"{\"schema\":\"native-finite-root-trace-direction-binary128-v1\",\"original_cpp_sha256\":"<<quoted(original_cpp_sha256)
    <<",\"complete\":"<<(ev.complete?"true":"false")<<",\"experiment_budget_exhausted\":"<<(ev.budget?"true":"false")
    <<",\"policy\":"<<quoted(policy.label)<<",\"root_stop_decimal\":"<<quoted(qstr(policy.stop))
    <<",\"root_fallback_decimal\":"<<quoted(qstr(policy.fallback))<<",\"state_alpha_decimal\":"<<quoted(qstr(alpha))
    <<",\"state_alpha_binary128_hex\":"<<quoted(qhex(alpha))
    <<",\"direction\":\"the complete actual packet delta, lifted word by word\",\"modes\":"<<p.M
    <<",\"shape_dimension\":"<<p.K<<",\"complete_state_dimension\":"<<p.size<<",\"depth\":"<<p.depth
    <<",\"node_count\":"<<p.depth+1<<",\"quadrature\":"<<p.N<<",\"full_row_count\":"<<size_t(p.depth+1)*p.K
    <<",\"rows_completed\":"<<ev.rows_completed<<",\"stages_completed\":"<<ev.stages_completed
    <<",\"all_stage_rows_computed\":"<<(ev.stages_completed==size_t(p.depth)?"true":"false")
    <<",\"scalar_readback_error\":"<<(ev.readback_error.empty()?"null":quoted(ev.readback_error))
    <<",\"cut_rows\":"<<p.M<<",\"stage_rows\":"<<size_t(p.depth)*p.K<<",\"far_rows\":"<<p.M
    <<",\"threads\":"<<threads<<",\"experiment_seconds\":"<<seconds<<",\"elapsed_seconds\":"<<std::setprecision(17)<<elapsed
    <<",\"storage\":\"IEEE754-binary128-little-endian\",\"mantissa_bits\":"<<FLT128_MANT_DIG
    <<",\"compiler_version\":"<<quoted(__VERSION__)
    <<",\"geometry_and_tables_fixed_literal_binary64\":true,\"C_is_not_defined_as_F_e\":true"
    <<",\"actual_Cholesky_and_both_triangular_loops_differentiated\":true"
    <<",\"rejected_root_trials_not_differentiated\":true,\"fixed_trace_real_expression_numeric_variation\":true"
    <<",\"derivative_of_IEEE_rounding_map_claimed\":false,\"real_branch_stability_proved\":false"
    <<",\"full_224_column_stage_J_supplied\":false,\"new_QR_or_native_solve\":false"
    <<",\"native_accepted\":false,\"physical_fullDN_J_or_fresh_audit_supplied\":false"
    <<",\"original_native_acceptance_thresholds_changed\":false,\"new_acceptance_gate\":false"
    <<",\"normalized_affine_is_a_model_readout_not_a_nonlinear_trial\":true"
    <<",\"root_statistics\":";print_root_stats(o,ev.root);o<<",\"variation_statistics\":";print_variation_stats(o,ev.variation);
  o<<",\"arrays\":[";
  const auto arr=[&](const char *name,size_t rows,size_t cols,bool comma){
    if(comma)o<<',';o<<"{\"file\":"<<quoted(name)<<",\"bytes\":"<<rows*cols*sizeof(Q)
      <<",\"shape\":["<<rows<<','<<cols<<"],\"dtype\":\"IEEE754-binary128-little-endian\",\"order\":\"C\"}";
  };
  arr("current-states.f128",p.depth+1,p.K,false);arr("input-direction.f128",p.depth+1,p.K,true);
  arr("primal-residual.f128",size_t(p.depth+1)*p.K,1,true);arr("directional-residual.f128",size_t(p.depth+1)*p.K,1,true);
  arr("stage-full-output.f128",p.depth,p.size,true);arr("stage-full-direction.f128",p.depth,p.size,true);
  o<<"],\"stage_full_arrays_before_port\":true,\"only_stage_Pi_divided_by_original_port_in_residual_and_JVP\":true"
    <<",\"both_mean_rows_retained_without_port_scaling\":true,\"boundary_target_graph_geometry_variations_fixed_zero\":true";
  if(ev.complete){
    o<<",\"primal_norm_decimal\":"<<quoted(qstr(ev.norm))<<",\"primal_norm_binary128_hex\":"<<quoted(qhex(ev.norm))
      <<",\"directional_norm_decimal\":"<<quoted(qstr(ev.action_norm))
      <<",\"unit_step_affine_norm_decimal\":"<<quoted(qstr(ev.affine_norm))
      <<",\"mean_height_sum_decimal\":"<<quoted(qstr(ev.mean_total))
      <<",\"mean_height_direction_decimal\":"<<quoted(qstr(ev.mean_direction))
      <<",\"primal_worst_row\":";print_row(o,p,ev,ev.worst);
    o<<",\"directional_worst_row\":";print_row(o,p,ev,ev.action_worst);
    o<<",\"unit_step_affine_worst_row\":";print_row(o,p,ev,ev.affine_worst);
    o<<",\"historical_watch_rows\":[";
    const size_t watches[]={2539,2536,2762,2128};
    for(size_t i=0;i<4;++i){if(i)o<<',';print_row(o,p,ev,watches[i]);}o<<']';
  }else o<<",\"primal_norm_decimal\":null,\"directional_norm_decimal\":null,\"unit_step_affine_norm_decimal\":null";
  o<<",\"stage_reports\":[";
  for(int n=0;n<p.depth;++n){
    if(n)o<<',';o<<"{\"stage\":"<<n<<",\"input_node\":"<<n+1<<",\"output_node\":"<<n
      <<",\"RK_steps\":"<<p.cells[n].steps.size()<<",\"complete\":"<<(ev.errors[n].empty()?"true":"false")
      <<",\"error\":"<<(ev.errors[n].empty()?"null":quoted(ev.errors[n]))
      <<",\"trace_file\":"<<(ev.trace_files[n].empty()?"null":quoted(ev.trace_files[n]))
      <<",\"root\":";print_root_stats(o,ev.root_by_stage[n]);o<<",\"variation\":";print_variation_stats(o,ev.variation_by_stage[n]);o<<'}';
  }
  o<<"]}";return o.str();
}
} // namespace trace_variation

int main(int argc,char **argv){
  using namespace trace_variation;
  try{
    const char *ga=std::getenv("GITHUB_ACTIONS"),*repo=std::getenv("GITHUB_REPOSITORY");
    if(!ga||std::string(ga)!="true"||!repo||std::string(repo)!="Rogerhu12/math-research-public")
      throw std::runtime_error("public-repository-Actions-only");
    if(std::fegetround()!=FE_TONEAREST)throw std::runtime_error("round-to-nearest-required");
    if(argc!=7)throw std::runtime_error("usage: trace-variation packet output-directory seconds threads original|refined base|trial:0..9");
    const int seconds=std::stoi(argv[3]),threads=std::stoi(argv[4]);
    if(seconds<60||seconds>14400||threads<1||threads>4)throw std::runtime_error("explicit-experiment-budget");
    deadline=Clock::now()+std::chrono::seconds(seconds);const auto start=Clock::now();
    Problem p(argv[1]);Policy policy;
    if(std::string(argv[5])=="original")policy={"binary128-e-original-inner-stop",p.original_stop,p.original_fallback};
    else if(std::string(argv[5])=="refined")policy={"binary128-e-refined-inner-stop",strtoflt128("1e-28",nullptr),strtoflt128("5e-27",nullptr)};
    else throw std::runtime_error("explicit-original-or-refined-policy");
    const std::string point=argv[6];Q alpha=0;
    if(point!="base"){
      if(point.size()!=7||point.rfind("trial:",0)!=0||point[6]<'0'||point[6]>'9')throw std::runtime_error("explicit-base-or-original-ten-alpha-point");
      alpha=scalbnq(1,-(point[6]-'0'));
    }
    const std::string directory=argv[2];
    auto ev=evaluate_direction(p,alpha,policy,threads,directory);
    write_raw(directory+"/current-states.f128",ev.states);write_raw(directory+"/input-direction.f128",p.delta);
    write_raw(directory+"/primal-residual.f128",ev.residual);write_raw(directory+"/directional-residual.f128",ev.action);
    write_raw(directory+"/stage-full-output.f128",ev.stage_output);write_raw(directory+"/stage-full-direction.f128",ev.stage_direction);
    const double elapsed=std::chrono::duration<double>(Clock::now()-start).count();
    const std::string body=report(p,ev,alpha,policy,threads,seconds,elapsed);
    std::ofstream f(directory+"/trace-direction-report.json",std::ios::binary|std::ios::trunc);f<<body<<'\n';f.close();
    if(!f)throw std::runtime_error("temporary-report-write");
    std::cout<<"NATIVE_TRACE_VARIATION {\"event\":\"finite_trace_direction_returned\",\"complete\":"<<(ev.complete?"true":"false")
      <<",\"rows_completed\":"<<ev.rows_completed<<",\"report\":\"trace-direction-report.json\",\"budget_exhausted\":"<<(ev.budget?"true":"false")
      <<",\"native_accepted\":false}"<<std::endl;
    return ev.complete?0:(ev.budget?3:2);
  }catch(const std::exception &error){
    std::cout<<"NATIVE_TRACE_VARIATION {\"event\":\"finite_trace_direction_error\",\"error\":"<<quoted(error.what())<<",\"native_accepted\":false}"<<std::endl;
    return 2;
  }
}
