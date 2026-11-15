// Literal-query extension of the original physical-jet/audit programs.
// This preserves their C-based radial-jet formula as a diagnostic.  It does
// not assert C=F_e or that this formula differentiates a finite root trace.
#ifndef VISIBLE_NATIVE_PHYSICAL128_HPP
#define VISIBLE_NATIVE_PHYSICAL128_HPP
#include "geometry_20261115_native_shared_trace128.hpp"
namespace physical128 {
using namespace shared_trace128;
struct PhysicalGeometry {Geometry g;Q k;};
struct Query {int segment,index;Q x;PhysicalGeometry geometry;std::vector<Step> advance;};
struct PhysicalPacket {
  int M,N,depth,audit_steps;
  Q rho,difference_step,scale_floor,relative_step_floor,original_r4_literal,two_pi;
  bool cut_terminal_geometry_words_equal=true;
  PhysicalGeometry cut;
  V cosine,sine,theta,twiddles;
  std::vector<std::vector<Query>> stages;
  static PhysicalGeometry geometry(Input &in){
    PhysicalGeometry p{{in.f64(),in.f64(),in.f64(),in.f64(),in.f64()},in.f64()};
    if(!(p.g.r>0&&p.g.dr!=0&&p.g.w>0&&p.g.w2>0&&p.g.E>0))
      throw std::runtime_error("physical-geometry-range");
    return p;
  }
  explicit PhysicalPacket(const std::string &file,const Problem &p){
    Input in(file);char magic[8];in.bytes(magic,8);
    if(std::memcmp(magic,"QPFI1281",8))throw std::runtime_error("physical-packet-magic");
    M=in.u32();N=in.u32();depth=in.u32();audit_steps=in.u32();
    if(M!=p.M||N!=p.N||depth!=p.depth||audit_steps<1||audit_steps>100000||
       (N&(N-1))!=0)throw std::runtime_error("physical-packet-layout");
    rho=in.f64();difference_step=in.f64();scale_floor=in.f64();relative_step_floor=in.f64();
    if(!(rho>0&&difference_step>0&&scale_floor>0&&relative_step_floor>0))
      throw std::runtime_error("physical-positive-constants");
    cut=geometry(in);original_r4_literal=in.f64();two_pi=in.f64();
    const Q physical_sq2=in.f64(),physical_sq12=in.f64();
    if(std::memcmp(&physical_sq2,&p.sq2,sizeof(Q))||std::memcmp(&physical_sq12,&p.sq12,sizeof(Q)))
      throw std::runtime_error("independent-physical-root-literal-constant-identity");
    const V physical_frequency=in.words(p.M);
    for(int j=0;j<p.M;++j)if(std::memcmp(&physical_frequency[j],&p.frequency[j],sizeof(Q)))
      throw std::runtime_error("independent-physical-root-frequency-identity");
    if(!(original_r4_literal>0))throw std::runtime_error("original-cut-r4-literal");
    const Geometry &last=p.cells[0].steps.back().g[2];
    const std::array<Q,5> a={last.r,last.dr,last.w,last.w2,last.E},
      b={cut.g.r,cut.g.dr,cut.g.w,cut.g.w2,cut.g.E};
    for(size_t j=0;j<a.size();++j)if(std::memcmp(&a[j],&b[j],sizeof(Q)))
      cut_terminal_geometry_words_equal=false;
    // The original cut evaluates profile(1); the terminal RK field has its
    // own literal x+h. Equality is reported, never imposed as a new gate.
    cosine=in.words(size_t(N)*(M+1));sine=in.words(size_t(N)*M);theta=in.words(N);
    int logn=0;for(int n=N;n>1;n/=2)++logn;
    twiddles=in.words(size_t(logn)*4);
    stages.resize(depth);
    for(int n=0;n<depth;++n){
      const uint32_t count=in.u32();
      if(!count||count>1000000)throw std::runtime_error("physical-stage-query-count");
      for(uint32_t q=0;q<count;++q){
        Query item;item.segment=in.u32();item.index=in.u32();item.x=in.f64();item.geometry=geometry(in);
        const uint32_t steps=in.u32();if(steps>100000)throw std::runtime_error("physical-query-step-count");
        if(item.index<0||item.index>audit_steps||item.x<0||item.x>1||
           (item.index==audit_steps&&steps!=0)||(item.index<audit_steps&&steps==0))
          throw std::runtime_error("physical-query-original-loop-layout");
        for(uint32_t k=0;k<steps;++k){
          Step s;s.h=in.f64();if(s.h==0)throw std::runtime_error("physical-zero-RK-step");
          for(auto &g:s.g){
            g={in.f64(),in.f64(),in.f64(),in.f64(),in.f64()};
            if(!(g.r>0&&g.dr!=0&&g.w>0&&g.w2>0&&g.E>0))
              throw std::runtime_error("physical-RK-geometry-range");
          }
          item.advance.push_back(s);
        }
        stages[n].push_back(std::move(item));
      }
    }
    char extra;if(in.file.read(&extra,1))throw std::runtime_error("physical-packet-suffix");
  }
};
struct AngleJet {Q ur,ut,urr,urt,utt,darboux,height;};
struct Jets {
  V Ldot;
  std::vector<AngleJet> angles;
  Q maxDarboux=0,curvature=0,peak_valley=0,holonomy=0,minA=0,minD=0,
    radial_solve_readback=0;
};

// Complete formula port of the original C-based physical-jet evaluator,
// using independently captured physical cs/sn words, not root-table aliases.
static Jets physical_jets(const Problem &p,const PhysicalPacket &physical,
    const V &state,const Cell &cell,const PhysicalGeometry &geometry,
    const FieldTape &field){
  const auto &g=geometry.g;const Q k=geometry.k,W=g.w2,dW=2*W*k,dE=dW,
    sigma=g.dr/g.r,r2=g.r*g.r,r3=r2*g.r,r4=r2*r2,
    fac=static_cast<Q>(p.orientation)*p.sq12*cell.mu/(p.sq2*r4*W);
  const auto &root=field.root.returned;const V &rhs=field.primal.derivative;
  V right(p.J,0),Tdot(p.N,0);
  for(int j=0;j<p.M;++j)right[j+1]=fac*(rhs[p.M+j]-(4*sigma+2*k)*state[p.M+j]);
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();
    const Q *cs=physical.cosine.data()+size_t(n)*p.J,*sn=physical.sine.data()+size_t(n)*p.M;
    Q dP=0,dPt=0;
    for(int j=0;j<p.M;++j){
      const Q dp=-p.frequency[j]*r3/(p.sq2*g.w)*(rhs[j]+(3*sigma-k)*state[j]);
      dP+=dp*sn[j];dPt+=p.frequency[j]*dp*cs[j+1];
    }
    Tdot[n]=dPt;const auto &v=root.evaluated.rows[n];
    const Q P=v.P,Pt=v.Pt,K=v.K,S=v.S,sd=v.sd,dK=-dPt,
      T=2*K+K*K+g.E*P*P,dT=2*(1+K)*dK+dE*P*P+2*g.E*P*dP,
      u=W*T,du=dW*T+W*dT,dS=-dW*P*P-2*W*P*dP,dsd=-du/(2*sd),
      one=1+sd,ff=(2+sd)/(2*sd*one*one),fc=u*ff,
      dfc=du*ff+u*ff*dsd*(1/(2+sd)-1/sd-2/(1+sd)),
      gn=P*P+S*T/(1+sd),
      dgn=2*P*dP+(dS*T+S*dT)/(1+sd)-S*T*dsd/(one*one),
      gc=W*gn/(S*sd),dgc=(dW*gn+W*dgn)/(S*sd)-gc*(dS/S+dsd/sd),
      dq=K*dK+static_cast<Q>(.5)*dE*P*P+g.E*P*dP+dK*Pt+K*dPt+dT*fc+T*dfc+
        dK*Pt*gc+(1+K)*dPt*gc+(1+K)*Pt*dgc;
    for(int j=0;j<p.J;++j)right[j]-=dq*cs[j]/p.N;
  }
  const V C=root_matrix(p,g,root.evaluated.rows);
  Jets out;out.Ldot=spd_solve(C,right,p.J);out.angles.resize(p.N);
  for(int i=0;i<p.J;++i){
    Q r=-right[i];for(int j=0;j<p.J;++j)r+=C[size_t(i)*p.J+j]*out.Ldot[j];
    finite(r,"physical-C-solve-readback");out.radial_solve_readback=qmax(out.radial_solve_readback,fabsq(r));
  }
  Q peak=-FLT128_MAX,valley=FLT128_MAX;
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();
    const Q *cs=physical.cosine.data()+size_t(n)*p.J;const auto &v=root.evaluated.rows[n];
    Q ld=0,height=state[p.K]+state[p.K+1];
    for(int j=0;j<p.J;++j)ld+=out.Ldot[j]*cs[j];
    for(int j=0;j<p.M;++j)height+=r4*state[j]*cs[j+1]/p.sq2;
    const Q b=k*v.K+ld-Tdot[n],G=g.dr*g.E/g.r*v.U*v.U-k*v.L+k*W*(v.K*v.Pt-v.P*v.P),
      darboux=W*(v.A*b-G)/(g.E*g.E*g.r*g.dr),urr=g.w*(k+b)/g.dr,
      ur=g.w*(1+v.K),ut=g.r*g.w*v.P,urt=g.w*(v.U+v.P),utt=g.r*g.w*v.Pt,
      a=(urr-W*k*ur/(g.E*g.dr))/(sqrtq(g.E)*v.sd),bc=g.w*v.U/(g.r*v.sd),
      c=g.w/g.r*(v.Pt+(1+v.K)/g.E)*sqrtq(g.E)/v.sd,disc=hypotq(a-c,2*bc);
    out.maxDarboux=qmax(out.maxDarboux,fabsq(darboux));
    out.curvature=qmax(out.curvature,qmax(fabsq((a+c+disc)/2),fabsq((a+c-disc)/2)));
    peak=std::max(peak,height);valley=std::min(valley,height);
    out.holonomy+=W*((2*v.K+v.K*v.K+g.E*v.P*v.P)/(v.sd*(1+v.sd))+
      (1+v.K)*v.Pt/(v.S*v.sd))/p.N;
    for(Q value:{ur,ut,urr,urt,utt,darboux,height})finite(value,"physical-angle-jet");
    out.angles[n]={ur,ut,urr,urt,utt,darboux,height};
  }
  out.peak_valley=peak-valley;out.minA=root.evaluated.minA;out.minD=root.evaluated.minD;
  return out;
}

static void fft(V &re,V &im,bool inverse,const PhysicalPacket &p){
  const int n=re.size();if(n!=p.N||im.size()!=re.size()||(n&(n-1)))throw std::runtime_error("physical-FFT-shape");
  for(int i=1,j=0;i<n;++i){
    int bit=n>>1;for(;j&bit;bit>>=1)j^=bit;j^=bit;
    if(i<j){std::swap(re[i],re[j]);std::swap(im[i],im[j]);}
  }
  int level=0;
  for(int len=2;len<=n;len*=2,++level){
    time_check();const size_t offset=size_t(level)*4+(inverse?2:0);
    const Q wr=p.twiddles[offset],wi=p.twiddles[offset+1];
    for(int start=0;start<n;start+=len){
      Q ur=1,ui=0;
      for(int j=0;j<len/2;++j){
        const int a=start+j,b=a+len/2;
        const Q vr=re[b]*ur-im[b]*ui,vi=re[b]*ui+im[b]*ur,ar=re[a],ai=im[a];
        re[a]=ar+vr;im[a]=ai+vi;re[b]=ar-vr;im[b]=ai-vi;
        const Q nr=ur*wr-ui*wi;ui=ur*wi+ui*wr;ur=nr;
      }
    }
  }
  if(inverse)for(int i=0;i<n;++i){re[i]/=n;im[i]/=n;}
}
static V periodic_primitive(const V &values,const PhysicalPacket &p){
  V re=values,im(values.size(),0);fft(re,im,false,p);re[0]=im[0]=0;
  for(int j=1;j<p.N;++j){
    if(j==p.N/2){re[j]=im[j]=0;continue;}
    const int k=j<=p.N/2?j:j-p.N;const Q a=re[j],b=im[j];re[j]=b/k;im[j]=-a/k;
  }
  fft(re,im,true,p);return re;
}
struct Metric {
  Q relative=0,RR=0,RT=0,TT=0,holonomy=0,translation=0,gauge=0,
    phase_mean_derivative=0,min_delta=FLT128_MAX,curl_correction=0;
};
// The original Fourier-development formulas and base FFT twiddles are
// preserved. sin/cos of the state-dependent developed angle are genuine
// binary128 calls, an explicitly new finite arithmetic implementation.
static Metric physical_metric(const Geometry &g,const Jets &jets,const PhysicalPacket &p){
  const int n=p.N;const Q r=g.r,E=g.E;
  V omega(n),Omega(n),rho(n),alpha(n),beta(n);Q phi=0,omegaRMean=0,minDelta=FLT128_MAX;
  for(int j=0;j<n;++j){
    if((j&31)==0)time_check();
    const auto &v=jets.angles[j];
    const Q S=r*r-v.ut*v.ut,Delta=E*S-r*r*v.ur*v.ur,sd=sqrtq(Delta),
      C=r+v.ur*v.utt-v.ut*v.ut/r;
    if(!(S>0&&Delta>0))throw std::runtime_error("actual-development-projection-failed");
    rho[j]=sqrtq(S);alpha[j]=sd/rho[j];beta[j]=-v.ur*v.ut/rho[j];
    omega[j]=r*r*C/(S*sd);phi+=omega[j]/n;
    omegaRMean+=r*r*v.ur*(v.urt-v.ut/r)/(S*sd)/n;
    const Q r2=r*r,r4=r2*r2;
    Omega[j]=v.darboux*E*E*r4/(Delta*sd);minDelta=std::min(minDelta,Delta/(r*r));
  }
  const V pOmega=periodic_primitive(Omega,p),pOmegaTheta=periodic_primitive(omega,p);
  V ax(n),ay(n),tx(n),ty(n),cx(n),cy(n);const Q zeta=phi-1;
  Q mx=0,my=0,maX=0,maY=0;
  for(int j=0;j<n;++j){
    const Q psi=p.theta[j]+pOmegaTheta[j],c=cosq(psi),s=sinq(psi);
    ax[j]=alpha[j]*c-beta[j]*s;ay[j]=alpha[j]*s+beta[j]*c;
    tx[j]=-rho[j]*s;ty[j]=rho[j]*c;
    cx[j]=-rho[j]*pOmega[j]*c-zeta*ay[j];cy[j]=-rho[j]*pOmega[j]*s+zeta*ax[j];
    mx+=tx[j]/n;my+=ty[j]/n;maX+=ax[j]/n;maY+=ay[j]/n;
  }
  const V pcx=periodic_primitive(cx,p),pcy=periodic_primitive(cy,p);
  Metric out;
  for(int j=0;j<n;++j){
    const auto &v=jets.angles[j];const Q rx=ax[j]+pcx[j],ry=ay[j]+pcy[j],
      sx=tx[j]-mx,sy=ty[j]-my,A=(rx*rx+ry*ry+v.ur*v.ur)/E-1,
      B=(rx*sx+ry*sy+v.ur*v.ut)/(r*sqrtq(E)),C=(sx*sx+sy*sy+v.ut*v.ut)/(r*r)-1;
    out.RR=qmax(out.RR,fabsq(A));out.RT=qmax(out.RT,fabsq(B));out.TT=qmax(out.TT,fabsq(C));
    out.relative=qmax(out.relative,qmax(fabsq((A+C+hypotq(A-C,2*B))/2),fabsq((A+C-hypotq(A-C,2*B))/2)));
    out.curl_correction=qmax(out.curl_correction,hypotq(pcx[j],pcy[j]));
  }
  out.holonomy=fabsq(zeta);out.translation=p.two_pi*hypotq(mx,my);
  out.gauge=hypotq(maX,maY);out.phase_mean_derivative=omegaRMean;out.min_delta=minDelta;
  for(Q x:{out.relative,out.RR,out.RT,out.TT,out.holonomy,out.translation,out.gauge,
           out.phase_mean_derivative,out.min_delta,out.curl_correction})finite(x,"physical-metric-readback");
  return out;
}
struct CutReadout {V rows;Jets jets;FieldTape field;};
static CutReadout cut_readout(const Problem &p,const PhysicalPacket &physical,
    const V &node,const Policy &policy,BatchStats &stats,std::ostream &trace,int label){
  V y(p.size,0);for(int j=0;j<p.K;++j)y[j]=node[j];
  for(int j=0;j<p.M;++j)y[p.M+j]*=physical.rho;
  auto field=capture_field(p,y,p.cells[0],physical.cut.g,policy,stats,trace,-1,label,0);
  auto jets=physical_jets(p,physical,y,p.cells[0],physical.cut,field);
  const Geometry &g=physical.cut.g;const Q k=physical.cut.k,sigma=g.dr/g.r,
    r2=g.r*g.r,r3=r2*g.r,r4=r2*r2;
  V rows(3*p.M+2,0);
  for(int j=0;j<p.M;++j){
    const Q m2=p.frequency[j]*p.frequency[j];
    rows[j]=m2*r3*y[j]+p.sq2*g.w*field.root.returned.L[j+1];
    rows[p.M+j]=(m2*r3*(field.primal.derivative[j]+3*sigma*y[j])+
      p.sq2*g.w*(jets.Ldot[j+1]+k*field.root.returned.L[j+1]))/g.dr;
    rows[2*p.M+2+j]=r4*node[j];
  }
  rows[2*p.M]=g.w*field.root.returned.L[0];
  rows[2*p.M+1]=g.w*(k*field.root.returned.L[0]+jets.Ldot[0])/g.dr;
  for(Q v:rows)finite(v,"cut-physical-readout");
  return {std::move(rows),std::move(jets),std::move(field)};
}
} // namespace physical128
#endif
