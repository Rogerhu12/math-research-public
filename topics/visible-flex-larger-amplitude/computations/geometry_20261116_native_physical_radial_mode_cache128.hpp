// R515: reuse only the finite radial-mode word already formed in one
// physical128 query. All angular sums, original C solve, physical jets,
// cut rows and two means retain their original expressions and order.
// This independent header does not replace any published source or set
// native/fullDN acceptance. There is no cross-query or cross-state cache.
#ifndef VISIBLE_NATIVE_PHYSICAL_RADIAL_MODE_CACHE128_HPP
#define VISIBLE_NATIVE_PHYSICAL_RADIAL_MODE_CACHE128_HPP
#include "geometry_20261115_native_physical128.hpp"
namespace physical128 {

static Jets physical_jets_radial_mode_cache(const Problem &p,const PhysicalPacket &physical,
    const V &state,const Cell &cell,const PhysicalGeometry &geometry,
    const FieldTape &field){
  const auto &g=geometry.g;const Q k=geometry.k,W=g.w2,dW=2*W*k,dE=dW,
    sigma=g.dr/g.r,r2=g.r*g.r,r3=r2*g.r,r4=r2*r2,
    fac=static_cast<Q>(p.orientation)*p.sq12*cell.mu/(p.sq2*r4*W);
  const auto &root=field.root.returned;const V &rhs=field.primal.derivative;
  V right(p.J,0),Tdot(p.N,0);
  // Each cache is owned by this one immutable physical query. A nonfinite
  // word is never cached; its next use executes the complete original form.
  V radial_mode_words(p.M,0);
  std::vector<unsigned char> radial_mode_ready(p.M,0);
  for(int j=0;j<p.M;++j)right[j+1]=fac*(rhs[p.M+j]-(4*sigma+2*k)*state[p.M+j]);
  for(int n=0;n<p.N;++n){
    if((n&31)==0)time_check();
    const Q *cs=physical.cosine.data()+size_t(n)*p.J,*sn=physical.sine.data()+size_t(n)*p.M;
    Q dP=0,dPt=0;
    for(int j=0;j<p.M;++j){
      Q dp;
      if(radial_mode_ready[j]){
        dp=radial_mode_words[j];
      }else{
        dp=-p.frequency[j]*r3/(p.sq2*g.w)*(rhs[j]+(3*sigma-k)*state[j]);
        if(finiteq(dp)){radial_mode_words[j]=dp;radial_mode_ready[j]=1;}
      }
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

static CutReadout cut_readout_radial_mode_cache(const Problem &p,const PhysicalPacket &physical,
    const V &node,const Policy &policy,BatchStats &stats,std::ostream &trace,int label){
  V y(p.size,0);for(int j=0;j<p.K;++j)y[j]=node[j];
  for(int j=0;j<p.M;++j)y[p.M+j]*=physical.rho;
  auto field=capture_field(p,y,p.cells[0],physical.cut.g,policy,stats,trace,-1,label,0);
  auto jets=physical_jets_radial_mode_cache(p,physical,y,p.cells[0],physical.cut,field);
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
