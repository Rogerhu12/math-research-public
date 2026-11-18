// Frozen finite momentum equations: original formed-moment root and ordinary RK.
// The only precision candidate is native long double; no shifted root/carry.
#include "frozen_flow.h"
#include <algorithm>
#include <array>
#include <cfenv>
#include <cfloat>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <initializer_list>
#include <iostream>
#include <limits>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <type_traits>
#include <vector>

static_assert(LDBL_MANT_DIG == 64, "This reviewed candidate is x87 extended64-significand precision");
static_assert(sizeof(long double) == 16, "Unexpected long double storage ABI");
static_assert(sizeof(double) == 8, "Unexpected binary64 ABI");
#if __BYTE_ORDER__ != __ORDER_LITTLE_ENDIAN__
#error This exact encoding protocol currently requires little endian.
#endif

namespace vf {
struct DomainError : std::runtime_error { using std::runtime_error::runtime_error; };
struct CallbackError : std::runtime_error { using std::runtime_error::runtime_error; };
struct LiteralJacobianError : std::runtime_error { using std::runtime_error::runtime_error; };

template<class R> constexpr int scalar_mode() { return std::is_same_v<R,double> ? 0 : 1; }
template<class R> constexpr size_t scalar_bytes() { return std::is_same_v<R,double> ? 8 : 10; }

template<class R> void canonical(const R *values, size_t n, unsigned char *out) {
    if (!out) return;
    for (size_t i=0;i<n;i++) std::memcpy(out+i*scalar_bytes<R>(), values+i, scalar_bytes<R>());
}

template<class R> class Math {
    const VFCallbacks &cb;
public:
    explicit Math(const VFCallbacks &callbacks) : cb(callbacks) {}
    R sqrt(R x) const {
        if constexpr (std::is_same_v<R,double>) {
            double out=0;
            if (!cb.double_sqrt || cb.double_sqrt(x,&out,cb.user))
                throw CallbackError("exact V8 sqrt callback failed");
            return out;
        } else return std::sqrt(x);
    }
    void root_trans(const std::vector<R> &D,const std::vector<R> &u,bool need_jac,
                    std::vector<R> &sd,std::vector<R> &bm) const {
        sd.resize(D.size());
        bm.resize(need_jac ? D.size() : 0);
        if constexpr (std::is_same_v<R,double>) {
            if (!cb.double_trans || cb.double_trans(D.size(),D.data(),u.data(),need_jac,
                    sd.data(),need_jac?bm.data():nullptr,cb.user))
                throw CallbackError("exact V8 root-transcendental callback failed");
        } else {
            for (size_t n=0;n<D.size();n++) sd[n]=std::sqrt(D[n]);
            if (need_jac) for (size_t n=0;n<D.size();n++)
                bm[n]=std::expm1(-R(1.5)*std::log1p(-u[n]));
        }
    }
};

template<class R, size_t D> struct Dual {
    R v;
    std::array<R,D> d{};
    Dual() : v(0) {}
    explicit Dual(R x) : v(x) {}
    static Dual variable(R x,size_t i) { Dual a(x);a.d[i]=R(1);return a; }
};
template<class R,size_t D> Dual<R,D> operator+(const Dual<R,D>&a,const Dual<R,D>&b) {
    Dual<R,D> z(a.v+b.v);for(size_t j=0;j<D;j++)z.d[j]=a.d[j]+b.d[j];return z;
}
template<class R,size_t D> Dual<R,D> operator-(const Dual<R,D>&a,const Dual<R,D>&b) {
    Dual<R,D> z(a.v-b.v);for(size_t j=0;j<D;j++)z.d[j]=a.d[j]-b.d[j];return z;
}
template<class R,size_t D> Dual<R,D> operator*(const Dual<R,D>&a,const Dual<R,D>&b) {
    Dual<R,D> z(a.v*b.v);for(size_t j=0;j<D;j++)z.d[j]=a.d[j]*b.v+a.v*b.d[j];return z;
}
template<class R,size_t D> Dual<R,D> operator/(const Dual<R,D>&a,const Dual<R,D>&b) {
    Dual<R,D> z(a.v/b.v);for(size_t j=0;j<D;j++)z.d[j]=(a.d[j]-z.v*b.d[j])/b.v;return z;
}
template<class R,size_t D> Dual<R,D> dual_sqrt(const Dual<R,D>&a,const Math<R>&math) {
    Dual<R,D> z(math.sqrt(a.v));for(size_t j=0;j<D;j++)z.d[j]=a.d[j]/(R(2)*z.v);return z;
}

template<class R> struct Coeff {
    R r3,r4,sqrt2,sqrt12,E,w2,pden,target,sigma,pref,qlnum,mean;
    std::vector<R> pnum;
    Coeff(const double *p,int M) : r3(p[0]),r4(p[1]),sqrt2(p[2]),sqrt12(p[3]),
        E(p[4]),w2(p[5]),pden(p[6]),target(p[7]),sigma(p[8]),pref(p[9]),qlnum(p[10]),mean(p[11]),pnum(M) {
        for(int j=0;j<M;j++)pnum[j]=R(p[12+j]);
    }
};
template<class R> struct Row { R P,Pt,L,K,U,T,u,D,S,A,sd,quad; };
template<class R> struct Evaluation {
    std::vector<R> moments,quad,B;
    std::vector<Row<R>> rows;
    R minD=std::numeric_limits<R>::infinity(), minS=minD, minA=minD, maxQuad=0;
};
template<class R> struct Root {
    std::vector<R> L;
    Evaluation<R> e;
    R err=0,scale=0;
    int iteration=0;
    bool fallback=false;
};
template<class R> struct Field { std::vector<R> ds,dt; };

template<class R> class Engine {
    int M,J,K,size,nq;
    const VFConfig &cfg;
    const VFCallbacks &cb;
    Math<R> math;
    std::vector<R> cs,sn,halves;
    std::vector<int> frequency;
    std::vector<Coeff<R>> coeff;
    R floor,tolerance,fallback_tolerance,scale_floor;
    bool tracing;
    uint64_t trace_events=0,root_calls=0,root_updates=0,root_fallbacks=0;
    R minA=std::numeric_limits<R>::infinity(),minD=minA,maxRootRelative=0,minLiteralPivot=minA;

    void emit(int code,std::initializer_list<int64_t> integers,std::vector<R> values,
              const char *message=nullptr) {
        if(!tracing)return;
        std::vector<unsigned char> bytes(values.size()*scalar_bytes<R>());
        canonical(values.data(),values.size(),bytes.data());
        trace_events++;
        if(cb.trace(code,integers.begin(),integers.size(),bytes.data(),values.size(),
                    scalar_mode<R>(),message,cb.user))throw CallbackError("trace callback failed");
    }
    static void append(std::vector<R>&a,const std::vector<R>&b) { a.insert(a.end(),b.begin(),b.end()); }
    static R max_abs(const std::vector<R>&values) {
        R result=0;for(R v:values)result=std::max(result,std::abs(v));return result;
    }
    Evaluation<R> evaluate(const std::vector<R>&L,const std::vector<R>&Q,const Coeff<R>&g,bool need_jac) {
        if(tracing){std::vector<R>v=L;append(v,Q);emit(3,{need_jac},std::move(v));}
        std::vector<R> p(M),pt(J,R(0));
        for(int j=0;j<M;j++){p[j]=g.pnum[j]*Q[j]/g.pden;pt[j+1]=frequency[j]*p[j];}
        Evaluation<R> e;
        e.quad.assign(J,R(0));e.B.assign(J*J,R(0));e.rows.reserve(nq);
        if(need_jac)for(int i=0;i<J;i++)e.B[i*J+i]=R(1);
        std::vector<R> Ds,us;Ds.reserve(nq);us.reserve(nq);
        for(int n=0;n<nq;n++){
            R P=0,Pt=0,U=0,Lv=L[0];const R *co=&cs[n*J],*si=&sn[n*M];
            for(int j=0;j<M;j++){
                int m=frequency[j];
                P+=p[j]*si[j];Pt+=pt[j+1]*co[j+1];Lv+=L[j+1]*co[j+1];
                U+=(-m*L[j+1]+(m*m-1)*p[j])*si[j];
            }
            R kv=Lv-Pt,T=R(2)*kv+kv*kv+g.E*P*P,u=g.w2*T;
            R D=R(1)-u,S=R(1)-g.w2*P*P,A=R(1)+Lv+g.w2*Pt;
            bool dp=D>floor,sp=dp&&(S>floor),ac=dp&&sp,ap=ac&&(A>floor);
            if(tracing)emit(4,{n,dp,dp,dp?int(sp):-1,ac,ac?int(ap):-1},{D,S,A,floor});
            if(!(dp&&sp&&ap))throw DomainError("momentum branch D/S/A rejected");
            e.rows.push_back({P,Pt,Lv,kv,U,T,u,D,S,A,R(0),R(0)});Ds.push_back(D);us.push_back(u);
        }
        std::vector<R>sd,bmn;math.root_trans(Ds,us,need_jac,sd,bmn);
        for(int n=0;n<nq;n++){
            auto &v=e.rows[n];const R *co=&cs[n*J];v.sd=sd[n];
            R fc=v.u*(R(2)+v.sd)/(R(2)*v.sd*(R(1)+v.sd)*(R(1)+v.sd));
            R gc=g.w2*(v.P*v.P+v.S*v.T/(R(1)+v.sd))/(v.S*v.sd);
            R q=R(.5)*(v.K*v.K+g.E*v.P*v.P)+v.K*v.Pt+v.T*fc+(R(1)+v.K)*v.Pt*gc;
            v.quad=q;e.maxQuad=std::max(e.maxQuad,std::abs(q));
            e.minD=std::min(e.minD,v.D);e.minA=std::min(e.minA,v.A);e.minS=std::min(e.minS,v.S);
            for(int i=0;i<J;i++)e.quad[i]+=q*co[i]/nq;
            if(need_jac){
                R am=v.L+g.w2*v.Pt,bm=am+(R(1)+am)*bmn[n];
                for(int i=0;i<J;i++)for(int j=0;j<=i;j++)e.B[i*J+j]+=bm*co[i]*co[j]/nq;
            }
        }
        if(need_jac)for(int i=0;i<J;i++)for(int j=0;j<i;j++)e.B[j*J+i]=e.B[i*J+j];
        e.moments.resize(J);for(int i=0;i<J;i++)e.moments[i]=L[i]+e.quad[i];
        if(tracing){auto v=e.moments;v.insert(v.end(),{e.minD,e.minS,e.minA,e.maxQuad});emit(5,{},std::move(v));}
        return e;
    }
    std::vector<R> factor(const std::vector<R>&B,bool original_newton) {
        std::vector<R>L(J*J,R(0));
        for(int i=0;i<J;i++)for(int j=0;j<=i;j++){
            R v=B[i*J+j];for(int k=0;k<j;k++)v-=L[i*J+k]*L[j*J+k];
            if(i==j){
                if(original_newton){
                    if(tracing)emit(6,{i,v>R(0)},{v});
                    if(!(v>R(0)))throw DomainError("momentum Newton matrix not SPD");
                }else{
                    // Literal B_exact has its own checked pivots. Positivity is
                    // never borrowed from the original B or the D/S/A floor.
                    if(!(v>R(0))||!std::isfinite(v))
                        throw LiteralJacobianError("literal implicit Jacobian pivot not positive finite");
                    minLiteralPivot=std::min(minLiteralPivot,v);
                }
                L[i*J+j]=math.sqrt(v);
            }else L[i*J+j]=v/L[j*J+j];
        }
        return L;
    }
    std::vector<R> solve_factored(const std::vector<R>&L,const std::vector<R>&b,int columns) {
        std::vector<R>X=b;
        for(int i=0;i<J;i++)for(int col=0;col<columns;col++){
            R v=X[i*columns+col];for(int k=0;k<i;k++)v-=L[i*J+k]*X[k*columns+col];
            X[i*columns+col]=v/L[i*J+i];
        }
        for(int i=J-1;i>=0;i--)for(int col=0;col<columns;col++){
            R v=X[i*columns+col];for(int k=i+1;k<J;k++)v-=L[k*J+i]*X[k*columns+col];
            X[i*columns+col]=v/L[i*J+i];
        }
        return X;
    }
    Root<R> root(const std::vector<R>&state,const Coeff<R>&g,double x) {
        std::vector<R>target(J,R(0));for(int j=0;j<M;j++)target[j+1]=g.target*state[M+j];
        std::vector<R>L=target,Q(state.begin(),state.begin()+M);
        if(tracing){auto v=state;v.push_back(R(x));append(v,target);append(v,L);emit(2,{},std::move(v));}
        for(int it=0;it<cfg.root_iterations;it++){
            auto e=evaluate(L,Q,g,true);std::vector<R>residual(J);
            for(int i=0;i<J;i++)residual[i]=e.moments[i]-target[i];
            R err=max_abs(residual),scale=std::max(scale_floor,e.maxQuad);
            for(R v:target)scale=std::max(scale,std::abs(v));
            R threshold=tolerance*scale;bool accepted=err<=threshold;
            if(tracing)emit(7,{it,accepted},{err,scale,tolerance,threshold});
            auto finish=[&](bool fallback)->Root<R>{
                if(tracing)emit(8,{it,fallback},{err,scale});
                root_calls++;root_updates+=it;root_fallbacks+=fallback;
                maxRootRelative=std::max(maxRootRelative,err/scale);
                return Root<R>{std::move(L),std::move(e),err,scale,it,fallback};
            };
            if(accepted)return finish(false);
            auto step=solve_factored(factor(e.B,true),residual,1);
            accepted=false;
            for(int k=0;k<cfg.n_halves;k++){
                R fac=halves[k];std::vector<R>trial(J);
                for(int j=0;j<J;j++)trial[j]=L[j]-fac*step[j];
                if(tracing){std::vector<R>v{fac};append(v,trial);emit(9,{k},std::move(v));}
                try{
                    auto v=evaluate(trial,Q,g,false);R er=0;
                    for(int j=0;j<J;j++)er=std::max(er,std::abs(v.moments[j]-target[j]));
                    bool improves=er<err,compared=!improves,within=compared&&(er<=threshold);
                    accepted=improves||within;
                    if(tracing)emit(10,{k,improves,compared,compared?int(within):-1,accepted},{er,err,scale,threshold});
                    if(accepted){L=std::move(trial);break;}
                }catch(const DomainError &error){
                    if(tracing)emit(11,{k},{},error.what());
                }
            }
            if(!accepted){
                threshold=fallback_tolerance*scale;accepted=err<=threshold;
                if(tracing)emit(12,{accepted},{err,scale,fallback_tolerance,threshold});
                if(accepted)return finish(true);
                throw DomainError("momentum Newton line search failed");
            }
        }
        throw DomainError("momentum Newton iteration limit");
    }

    std::array<R,3> q_partials(const Row<R>&v,const Coeff<R>&g) {
        using D=Dual<R,3>;
        D Lv=D::variable(v.L,0),P=D::variable(v.P,1),Pt=D::variable(v.Pt,2);
        D one(R(1)),two(R(2)),half(R(.5)),E(g.E),W(g.w2);
        D k=Lv-Pt,T=two*k+k*k+E*P*P,u=W*T,den=one-u,S=one-W*P*P;
        D sd=dual_sqrt(den,math),fc=u*(two+sd)/(two*sd*(one+sd)*(one+sd));
        D gc=W*(P*P+S*T/(one+sd))/(S*sd);
        D q=half*(k*k+E*P*P)+k*Pt+T*fc+(one+k)*Pt*gc;
        return q.d;
    }
    std::array<R,2> flux_partials(const Row<R>&v,const Coeff<R>&g) {
        using D=Dual<R,2>;
        D k=D::variable(v.K,0),P=D::variable(v.P,1),one(R(1)),two(R(2)),E(g.E),W(g.w2);
        D T=two*k+k*k+E*P*P,u=W*T,sd=dual_sqrt(one-u,math),S=one-W*P*P;
        D f=(k+u/(one+sd)+W*P*P*sd)/(S*sd);
        return f.d;
    }
    std::vector<R> literal_jacobian(const Root<R>&rt,const Coeff<R>&g,const std::vector<R>&factors) {
        std::vector<R>B(J*J,R(0)),right(J*K,R(0)),a(M);
        std::vector<std::array<R,2>> fpartial(nq);
        for(int i=0;i<J;i++)B[i*J+i]=R(1);
        for(int j=0;j<M;j++){a[j]=g.pnum[j]/g.pden;right[(j+1)*K+M+j]=g.target;}
        for(int n=0;n<nq;n++){
            auto q=q_partials(rt.e.rows[n],g);fpartial[n]=flux_partials(rt.e.rows[n],g);
            const R *co=&cs[n*J],*si=&sn[n*M];
            for(int i=0;i<J;i++)for(int k=0;k<=i;k++)B[i*J+k]+=q[0]*co[i]*co[k]/nq;
            for(int j=0;j<M;j++){
                R chain=q[1]*a[j]*si[j]+q[2]*frequency[j]*a[j]*co[j+1];
                for(int i=0;i<J;i++)right[i*K+j]-=chain*co[i]/nq;
            }
        }
        for(int i=0;i<J;i++)for(int j=0;j<i;j++)B[j*J+i]=B[i*J+j];
        // This is the literal moment equation's implicit Jacobian, evaluated at
        // the returned approximate root, not AD through Newton stopping rules.
        auto dL=solve_factored(factor(B,false),right,K);
        std::vector<R>dN(M*K,R(0));
        for(int n=0;n<nq;n++){
            const R *co=&cs[n*J],*si=&sn[n*M];const auto &v=rt.e.rows[n];
            for(int col=0;col<K;col++){
                R dP=0,dPt=0,dLv=dL[col],dU=0;
                if(col<M){dP=a[col]*si[col];dPt=frequency[col]*a[col]*co[col+1];}
                for(int j=0;j<M;j++){
                    int m=frequency[j];R lj=dL[(j+1)*K+col];dLv+=lj*co[j+1];
                    dU+=(-m*lj+(col==j?(m*m-1)*a[j]:R(0)))*si[j];
                }
                R dK=dLv-dPt;
                R df=dU*factors[n]+v.U*(fpartial[n][0]*dK+fpartial[n][1]*dP);
                for(int j=0;j<M;j++)dN[j*K+col]+=df*si[j]/nq;
            }
        }
        std::vector<R>out(size*K,R(0));
        for(int j=0;j<M;j++)for(int col=0;col<K;col++){
            int m=frequency[j];R lj=dL[(j+1)*K+col];
            out[j*K+col]=g.sigma*((col==j?R(m*m-4):R(0))+g.qlnum*lj/g.r3);
            out[(M+j)*K+col]=(col==M+j?R(4)*g.sigma:R(0))+
                g.pref*m*(-m*lj+(col==j?(m*m-1)*a[j]:R(0))+dN[j*K+col]);
        }
        for(int col=0;col<K;col++)out[K*K+col]=g.mean*dL[col];
        // Last mean RHS is the fixed g.mean, so its40 derivatives remain zero.
        return out;
    }
    std::pair<std::vector<R>,std::vector<R>> rhs(const std::vector<R>&state,const Coeff<R>&g,double x,bool with_jac) {
        auto rt=root(state,g,x);std::vector<R>flux(M,R(0)),factors(nq);
        minA=std::min(minA,rt.e.minA);minD=std::min(minD,rt.e.minD);
        for(int n=0;n<nq;n++){
            const auto &v=rt.e.rows[n];R u=g.w2*(R(2)*v.K+v.K*v.K+g.E*v.P*v.P);
            R f=(v.K+u/(R(1)+v.sd)+g.w2*v.P*v.P*v.sd)/(v.S*v.sd);
            factors[n]=f;R product=v.U*f;
            for(int j=0;j<M;j++)flux[j]+=product*sn[n*M+j]/nq;
        }
        std::vector<R>out(size,R(0));
        for(int j=0;j<M;j++){
            int m=frequency[j];R p=g.pnum[j]*state[j]/g.pden;
            R linear=-m*rt.L[j+1]+(m*m-1)*p;
            out[j]=g.sigma*((m*m-4)*state[j]+g.qlnum*rt.L[j+1]/g.r3);
            out[M+j]=R(4)*g.sigma*state[M+j]+g.pref*m*(linear+flux[j]);
        }
        out[K]=g.mean*rt.L[0];out[K+1]=g.mean;
        auto jac=with_jac?literal_jacobian(rt,g,factors):std::vector<R>{};
        return {std::move(out),std::move(jac)};
    }
public:
    Engine(const VFConfig &c,const VFStage &s,const VFCallbacks &callbacks) :
        M(c.M),J(M+1),K(2*M),size(K+2),nq(c.nq),cfg(c),cb(callbacks),math(cb),
        cs(nq*J),sn(nq*M),halves(c.n_halves),frequency(M),
        floor(c.floor),tolerance(c.tolerance),fallback_tolerance(c.fallback_tolerance),
        scale_floor(c.scale_floor),tracing(cb.trace!=nullptr) {
        for(int i=0;i<nq*J;i++)cs[i]=R(c.cosine[i]);
        for(int i=0;i<nq*M;i++)sn[i]=R(c.sine[i]);
        for(int i=0;i<c.n_halves;i++)halves[i]=R(c.halves[i]);
        for(int j=0;j<M;j++)frequency[j]=(j+1)*c.spacing;
        coeff.reserve(s.npoints);for(int i=0;i<s.npoints;i++)coeff.emplace_back(s.coefficients+i*(M+12),M);
    }
    void flow(const VFStage&s,bool with_jac,std::vector<R>&state,std::vector<R>&tangent) {
        state.resize(size);for(int i=0;i<size;i++)state[i]=R(s.initial42[i]);
        tangent.assign(with_jac?size*K:0,R(0));if(with_jac)for(int j=0;j<K;j++)tangent[j*K+j]=R(1);
        auto field=[&](const std::vector<R>&v,const std::vector<R>&t,const VFStep&step,
                       int label,int point,double x)->Field<R>{
            if(tracing)emit(1,{step.profile,step.step,label},{R(x)});
            auto result=rhs(v,coeff[point],x,with_jac);Field<R>f;f.ds=std::move(result.first);
            if(with_jac){
                f.dt.assign(size*K,R(0));
                for(int i=0;i<size;i++)for(int j=0;j<K;j++){
                    R z=result.second[i*K+j];for(int k=0;k<K;k++)f.dt[i*K+k]+=z*t[j*K+k];
                }
            }
            return f;
        };
        auto increment=[&](const Field<R>&f,R h){
            std::pair<std::vector<R>,std::vector<R>>z{state,tangent};
            for(int j=0;j<size;j++)z.first[j]=state[j]+h*f.ds[j];
            if(with_jac)for(size_t j=0;j<tangent.size();j++)z.second[j]=tangent[j]+h*f.dt[j];
            return z;
        };
        for(int k=0;k<s.nsteps;k++){
            const auto &step=s.steps[k];R h=R(step.h);
            auto a=field(state,tangent,step,0,step.point_a,step.x);
            auto ab=increment(a,h/R(2));auto b=field(ab.first,ab.second,step,1,step.point_mid,step.x+step.h/2);
            auto bc=increment(b,h/R(2));auto c=field(bc.first,bc.second,step,2,step.point_mid,step.x+step.h/2);
            auto cd=increment(c,h);auto d=field(cd.first,cd.second,step,3,step.point_end,step.x+step.h);
            for(int j=0;j<size;j++)state[j]+=h*(a.ds[j]+R(2)*b.ds[j]+R(2)*c.ds[j]+d.ds[j])/R(6);
            if(with_jac)for(size_t j=0;j<tangent.size();j++)
                tangent[j]+=h*(a.dt[j]+R(2)*b.dt[j]+R(2)*c.dt[j]+d.dt[j])/R(6);
        }
    }
    void diagnostics(VFDiagnostics &d) const {
        d.root_calls=root_calls;d.root_updates=root_updates;d.root_fallbacks=root_fallbacks;d.trace_events=trace_events;
        d.minA=double(minA);d.minD=double(minD);d.max_root_relative_residual=double(maxRootRelative);
        d.min_literal_Jacobian_pivot=double(minLiteralPivot);d.scalar_bytes=scalar_bytes<R>();
    }
};

void validate(const VFConfig &c,const VFStage&s,int mode,int with_jac,const VFCallbacks&cb) {
    if(c.abi_version!=1 || (mode!=0&&mode!=1) || (with_jac!=0&&with_jac!=1))throw std::runtime_error("invalid ABI/arithmetic mode");
    if(!(c.M>=1&&c.M<=64&&c.spacing>=1&&c.N>4*c.M*c.spacing&&
         c.nq==c.N/std::gcd(c.N,c.spacing)))throw std::runtime_error("original Fourier guard rejected");
    if(c.root_iterations!=30||c.n_halves!=20||!c.cosine||!c.sine||!c.halves||c.floor!=.1||
       c.tolerance!=8e-14||c.fallback_tolerance!=5e-12||c.scale_floor!=1e-300)
        throw std::runtime_error("original point-root rules changed");
    if(!(s.nsteps>0&&s.npoints>0)||!s.steps||!s.coefficients||!s.initial42)throw std::runtime_error("invalid frozen stage payload");
    if(std::fegetround()!=FE_TONEAREST)throw std::runtime_error("runtime rounding mode is not nearest");
    if(mode==1){
        unsigned short control=0;
        __asm__ __volatile__("fnstcw %0" : "=m"(control));
        if(((control>>8)&3)!=3)throw std::runtime_error("x87 precision control is not64-significand extended");
    }
    if(mode==0&&(!cb.double_trans||!cb.double_sqrt))throw std::runtime_error("double baseline requires original V8 math callbacks");
    for(int k=0;k<c.n_halves;k++)if(c.halves[k]!=std::ldexp(1.0,-k))throw std::runtime_error("original halving list changed");
    for(int k=0;k<s.nsteps;k++){
        const auto &p=s.steps[k];
        if(p.point_a<0||p.point_mid<0||p.point_end<0||p.point_a>=s.npoints||p.point_mid>=s.npoints||p.point_end>=s.npoints||
           !std::isfinite(p.x)||!std::isfinite(p.h)||!(p.h>0))throw std::runtime_error("invalid original grid/index");
    }
    for(int i=0;i<s.npoints*(c.M+12);i++)if(!std::isfinite(s.coefficients[i]))throw std::runtime_error("nonfinite frozen coefficient");
    for(int i=0;i<2*c.M+2;i++)if(!std::isfinite(s.initial42[i]))throw std::runtime_error("nonfinite input state");
}
template<class R> void run(const VFConfig&c,const VFStage&s,int with_jac,const VFCallbacks&cb,
    double*out,double*jac,unsigned char*native_out,unsigned char*native_jac,VFDiagnostics&d) {
    Engine<R>e(c,s,cb);std::vector<R>state,tangent;
    auto start=std::chrono::steady_clock::now();
    try{e.flow(s,with_jac,state,tangent);}catch(...){e.diagnostics(d);throw;}
    d.kernel_seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    e.diagnostics(d);
    // The original Node physical-port conversion/subtraction/scales stay outside.
    for(size_t j=0;j<state.size();j++){
        out[j]=double(state[j]);if(!std::isfinite(out[j]))throw DomainError("nonfinite binary64 output conversion");
    }
    if(with_jac)for(size_t j=0;j<tangent.size();j++){
        jac[j]=double(tangent[j]);if(!std::isfinite(jac[j]))throw LiteralJacobianError("nonfinite binary64 tangent conversion");
    }
    canonical(state.data(),state.size(),native_out);
    if(with_jac)canonical(tangent.data(),tangent.size(),native_jac);
}
} // namespace vf

extern "C" int vf_abi_version(void){return 1;}
extern "C" int vf_long_double_significand_bits(void){return LDBL_MANT_DIG;}
extern "C" int vf_runtime_info(char*out,size_t cap){
    if(!out||cap==0)return 1;
    unsigned short control=0;
#if defined(__x86_64__) || defined(__i386__)
    __asm__ __volatile__("fnstcw %0" : "=m"(control));
#endif
    std::ostringstream s;s<<"{\"abi\":1,\"long_double_significand_bits\":"<<LDBL_MANT_DIG
        <<",\"long_double_storage_bytes\":"<<sizeof(long double)<<",\"rounding_mode\":"<<std::fegetround()
        <<",\"round_to_nearest\":"<<(std::fegetround()==FE_TONEAREST?"true":"false")
        <<",\"x87_control_word\":"<<control<<",\"config_size\":"<<sizeof(VFConfig)
        <<",\"step_size\":"<<sizeof(VFStep)<<",\"stage_size\":"<<sizeof(VFStage)
        <<",\"callbacks_size\":"<<sizeof(VFCallbacks)<<",\"diagnostics_size\":"<<sizeof(VFDiagnostics)<<"}";
    if(s.str().size()+1>cap)return 2;std::memcpy(out,s.str().c_str(),s.str().size()+1);return 0;
}
extern "C" int vf_run_stage(const VFConfig*c,const VFStage*s,int mode,int with_jac,const VFCallbacks*callbacks,
    double*out,double*jac,unsigned char*native_out,unsigned char*native_jac,VFDiagnostics*d,char*error,size_t cap){
    if(d)std::memset(d,0,sizeof(*d));
    try{
        if(!c||!s||!d||!out||(with_jac&&!jac))throw std::runtime_error("missing required ABI pointer");
        VFCallbacks empty{};const auto &cb=callbacks?*callbacks:empty;
        vf::validate(*c,*s,mode,with_jac,cb);
        if(mode==0)vf::run<double>(*c,*s,with_jac,cb,out,jac,native_out,native_jac,*d);
        else vf::run<long double>(*c,*s,with_jac,cb,out,jac,native_out,native_jac,*d);
        if(error&&cap)error[0]=0;return 0;
    }catch(const std::exception&e){
        if(error&&cap){size_t n=std::min(cap-1,std::strlen(e.what()));std::memcpy(error,e.what(),n);error[n]=0;}
        return 1;
    }
}

#ifdef VF_BUILD_MAIN
// Whole-evaluate ABI1 wire protocol. This CLI uses the identical kernel above.
// No per-stage process creation, JSON dependency or Node addon is required.
namespace {
template<class T>T read_one(std::istream&s){T x{};s.read(reinterpret_cast<char*>(&x),sizeof(x));if(!s)throw std::runtime_error("truncated batch payload");return x;}
template<class T>void write_one(std::ostream&s,const T&x){s.write(reinterpret_cast<const char*>(&x),sizeof(x));if(!s)throw std::runtime_error("batch output failed");}
std::vector<double> read_doubles(std::istream&s,size_t n){std::vector<double>v(n);s.read(reinterpret_cast<char*>(v.data()),n*sizeof(double));if(!s)throw std::runtime_error("truncated coefficient/state array");return v;}
void write_doubles(std::ostream&s,const std::vector<double>&v){s.write(reinterpret_cast<const char*>(v.data()),v.size()*sizeof(double));if(!s)throw std::runtime_error("batch output array failed");}
}
int main(int argc,char**argv){
    if(argc!=3){std::cerr<<"usage: frozen_flow_batch INPUT.bin OUTPUT.bin\n";return 2;}
    try{
        std::ifstream input(argv[1],std::ios::binary);if(!input)throw std::runtime_error("cannot open batch input");
        std::ifstream existing(argv[2],std::ios::binary);if(existing.good())throw std::runtime_error("refusing to overwrite existing batch output");
        char magic[8];input.read(magic,8);if(!input||std::memcmp(magic,"VFN4LD01",8))throw std::runtime_error("invalid batch magic");
        VFConfig c{};c.abi_version=read_one<int32_t>(input);c.M=read_one<int32_t>(input);c.N=read_one<int32_t>(input);
        c.spacing=read_one<int32_t>(input);c.nq=read_one<int32_t>(input);c.root_iterations=read_one<int32_t>(input);
        c.n_halves=read_one<int32_t>(input);int32_t stages=read_one<int32_t>(input),with_jac=read_one<int32_t>(input);
        if(!(c.M>=1&&c.M<=64&&c.nq>0&&c.nq<=1048576&&c.n_halves==20&&stages>0&&stages<=1048576&&(with_jac==0||with_jac==1)))
            throw std::runtime_error("invalid batch dimensions");
        // An opaque64-byte input/source identity token is returned unchanged;
        // the caller verifies its SHA manifest before starting this executable.
        char identity[64];input.read(identity,64);if(!input)throw std::runtime_error("truncated manifest token");
        c.floor=read_one<double>(input);c.tolerance=read_one<double>(input);
        c.fallback_tolerance=read_one<double>(input);c.scale_floor=read_one<double>(input);
        auto halves=read_doubles(input,c.n_halves),cosine=read_doubles(input,size_t(c.nq)*(c.M+1)),sine=read_doubles(input,size_t(c.nq)*c.M);
        c.halves=halves.data();c.cosine=cosine.data();c.sine=sine.data();
        std::ofstream output(argv[2],std::ios::binary);if(!output)throw std::runtime_error("cannot create batch output");
        output.write("VFN4OUT1",8);write_one(output,c.abi_version);write_one(output,c.M);write_one(output,stages);write_one(output,with_jac);output.write(identity,64);
        for(int n=0;n<stages;n++){
            VFStage s{};s.nsteps=read_one<int32_t>(input);s.npoints=read_one<int32_t>(input);
            if(!(s.nsteps>0&&s.nsteps<=1048576&&s.npoints>0&&s.npoints<=1048576))throw std::runtime_error("invalid stage dimensions");
            auto initial=read_doubles(input,2*c.M+2),coefficients=read_doubles(input,size_t(s.npoints)*(c.M+12));
            std::vector<VFStep> steps(s.nsteps);
            for(auto&p:steps){p.profile=read_one<int32_t>(input);p.step=read_one<int32_t>(input);p.point_a=read_one<int32_t>(input);
                p.point_mid=read_one<int32_t>(input);p.point_end=read_one<int32_t>(input);p.x=read_one<double>(input);p.h=read_one<double>(input);}
            s.initial42=initial.data();s.coefficients=coefficients.data();s.steps=steps.data();
            std::vector<double>state(2*c.M+2),tangent(with_jac?(2*c.M+2)*(2*c.M):0);VFDiagnostics d{};char error[4096];
            int status=vf_run_stage(&c,&s,1,with_jac,nullptr,state.data(),with_jac?tangent.data():nullptr,nullptr,nullptr,&d,error,sizeof(error));
            write_one(output,int32_t(n));write_one(output,int32_t(status));
            if(status){uint32_t length=std::strlen(error);write_one(output,length);output.write(error,length);output.flush();std::cerr<<"stage "<<n<<": "<<error<<"\n";return 3;}
            write_doubles(output,state);if(with_jac)write_doubles(output,tangent);
            write_one(output,d.root_calls);write_one(output,d.root_updates);write_one(output,d.root_fallbacks);
            write_one(output,d.minA);write_one(output,d.minD);write_one(output,d.max_root_relative_residual);
            write_one(output,d.min_literal_Jacobian_pivot);write_one(output,d.kernel_seconds);
        }
        if(input.peek()!=std::char_traits<char>::eof())throw std::runtime_error("unexpected trailing batch bytes");
        output.flush();if(!output)throw std::runtime_error("batch flush failed");return 0;
    }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}
}
#endif
