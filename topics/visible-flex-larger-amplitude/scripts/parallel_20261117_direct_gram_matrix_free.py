#!/usr/bin/env python3
"""Full polynomial Gram constraints with one globally shared variable core rho.

This changes the finite objective, not the currently running Frenet LM budget.
All Y/U variables, actual cubic midpoints, original BC and all quadratic angular
modes remain. This probe does not solve a linear or nonlinear system, enforce
new mirror velocity conditions, or claim a continuous metric certificate.
"""
import argparse,hashlib,importlib.util,json,resource,time
from pathlib import Path
import numpy as np

MATRIX_SHA='ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def maximum(x):return float(np.max(np.abs(x)))

def factory(base):
 class GramFourier(base.FourierBatch):
  def __init__(self,M,N):
   super().__init__(M,N)
   if N<=12*M:raise ValueError('Complete coefficient-adjoint products must fit below Nyquist')
   self.out_n=6*M+2;self.out_modes=2*M;self.out_freq=2*np.arange(2*M+1)
  def first_jet(self,y):
   z=self.state_spec(y);v=np.fft.irfft(z,n=self.N,axis=-1)
   d=np.fft.irfft(z*self.imul,n=self.N,axis=-1);d[:,0]-=v[:,1];d[:,1]+=v[:,0]
   return v,d
  def rho(self,core,constant=1.):
   z=np.zeros(self.N//2+1,complex);z[0]=self.N*constant
   z[self.freq[1:]]=self.N/2*(1-self.freq[1:]**2)*core[1:self.M+1]
   return np.fft.irfft(z,n=self.N)
  def rho_transpose(self,beta):
   z=np.fft.rfft(beta)/self.N
   return (1-self.freq[1:]**2)*z[self.freq[1:]].real
  def project_constraints(self,r):
   z=np.fft.rfft(r,axis=-1)/self.N;f=self.out_freq
   a=-2*z[:,0,f[1:]].imag;b=2*z[:,1,f].real;c=2*z[:,2,f].real
   b[:,0]*=.5;c[:,0]*=.5
   return np.concatenate((a,b,c),axis=-1)
  def constraint_weight_field(self,w):
   M,N=self.out_modes,self.N;z=np.zeros((len(w),3,N//2+1),complex)
   z[:,0,self.out_freq[1:]]=-1j*N*w[:,:M]
   z[:,1,self.out_freq]=N*w[:,M:2*M+1]
   z[:,2,self.out_freq]=N*w[:,2*M+1:]
   return np.fft.irfft(z,n=N,axis=-1)

 class GramLocal:
  def __init__(self,F,Y,U,a,rho,chunk=32):
   self.F=F;self.a=np.asarray(a);self.rho=rho;self.chunk=chunk;self.size=len(Y)
   self.d=np.empty((self.size,3,F.N));self.V=np.empty_like(self.d)
   for start in range(0,self.size,chunk):
    sl=slice(start,min(start+chunk,self.size));_,self.d[sl]=F.first_jet(Y[sl]);self.V[sl]=F.synthesize(U[sl])
  def residual(self):
   out=np.empty((self.size,self.F.out_n))
   for start in range(0,self.size,self.chunk):
    sl=slice(start,min(start+self.chunk,self.size));d,V=self.d[sl],self.V[sl];a=self.a[sl,None]
    r=np.empty((len(d),3,self.F.N));r[:,0]=np.sum(V*d,axis=1)/a
    r[:,1]=np.sum(d*d,axis=1)/(a*a)-self.rho[None,:]**2
    r[:,2]=np.sum(V*V,axis=1)-1;out[sl]=self.F.project_constraints(r)
   return out
  def jvp(self,dY,dU,drho):
   F=self.F;out=np.empty((self.size,F.out_n))
   for start in range(0,self.size,self.chunk):
    sl=slice(start,min(start+self.chunk,self.size));_,dd=F.first_jet(dY[sl]);dv=F.synthesize(dU[sl])
    d,V=self.d[sl],self.V[sl];a=self.a[sl,None];r=np.empty((len(d),3,F.N))
    r[:,0]=np.sum(dv*d+V*dd,axis=1)/a
    r[:,1]=2*np.sum(d*dd,axis=1)/(a*a)-2*self.rho[None,:]*drho[None,:]
    r[:,2]=2*np.sum(V*dv,axis=1);out[sl]=F.project_constraints(r)
   return out
  def jtv(self,w):
   F=self.F;gy=np.empty((self.size,F.n));gu=np.empty_like(gy);core_beta=np.zeros(F.N)
   for start in range(0,self.size,self.chunk):
    sl=slice(start,min(start+self.chunk,self.size));eta=F.constraint_weight_field(w[sl])
    d,V=self.d[sl],self.V[sl];a=self.a[sl,None,None]
    flux=eta[:,0,None,:]*V/a+2*eta[:,1,None,:]*d/(a*a)
    force=eta[:,0,None,:]*d/a+2*eta[:,2,None,:]*V
    gy[sl]=F.adjoint_pack(-F.angle_derivative_spec(F.vector_spec(flux)))
    gu[sl]=F.adjoint_pack(F.vector_spec(force))
    core_beta+=np.sum(-2*self.rho[None,:]*eta[:,1],axis=0)
   return gy,gu,core_beta

 class GramComplete:
  def __init__(self,P,Y,U,chunk=32):
   self.P=P;self.F=GramFourier(P.M,P.N);self.rho=self.F.rho(Y[0])
   self.node=GramLocal(self.F,Y,U,P.scalar_nodes[:,0],self.rho,chunk)
   ym,um=P.midpoint(Y,U);self.middle=GramLocal(self.F,ym,um,P.scalar_mid[:,0],self.rho,chunk)
   self.variables=2*P.m*P.n;self.rows=(2*P.m-1)*self.F.out_n+P.n
   self.shape=(self.rows,self.variables);self.dtype=np.dtype(float);self.matvec_count=0;self.rmatvec_count=0
   self.bc=P.boundary(Y)
  def residual(self):
   nodes=self.node.residual();middle=self.middle.residual();bc=self.bc.copy()
   cost=float(np.sum(nodes*nodes)+np.sum(middle*middle)+np.sum(bc*bc))
   return dict(nodes=nodes,middle=middle,boundary=bc,cost=cost,
    finite=bool(np.isfinite(nodes).all()and np.isfinite(middle).all()and np.isfinite(bc).all()and np.isfinite(cost)))
  def matvec(self,v):
   P=self.P;v=np.asarray(v).reshape(-1);dY=v[:P.m*P.n].reshape(P.m,P.n);dU=v[P.m*P.n:].reshape(P.m,P.n)
   drho=self.F.rho(dY[0],constant=0.);ym,um=P.midpoint(dY,dU);self.matvec_count+=1
   return np.r_[self.node.jvp(dY,dU,drho).ravel(),self.middle.jvp(ym,um,drho).ravel(),P.BA@dY[0]+P.BB@dY[-1]]
  def rmatvec(self,w):
   P=self.P;nout=self.F.out_n;w=np.asarray(w).reshape(-1)
   wn=w[:P.m*nout].reshape(P.m,nout);wm=w[P.m*nout:-P.n].reshape(P.m-1,nout);wb=w[-P.n:]
   gY,gU,beta_n=self.node.jtv(wn);a,b,beta_m=self.middle.jtv(wm);h=P.h[:,None]
   gY[:-1]+=.5*a-1.5*b/h;gY[1:]+=.5*a+1.5*b/h
   gU[:-1]+=h*a/8-.25*b;gU[1:]+=-h*a/8-.25*b
   gY[0]+=P.BA.T@wb;gY[-1]+=P.BB.T@wb
   gY[0,1:P.M+1]+=self.F.rho_transpose(beta_n+beta_m)
   self.rmatvec_count+=1;return np.r_[gY.ravel(),gU.ravel()]
 return GramComplete

def independent_direction(P,F,dY,dU,eps=1e-25):
 # Published non-batched complex physical jets, without the new FFT derivative.
 yc=P.Y.astype(complex)+1j*eps*dY;uc=P.U.astype(complex)+1j*eps*dU
 rho=1+np.cos(P.q.angle[:,None]*P.q.freq[None,1:])@((1-P.q.freq[1:]**2)*yc[0,1:P.M+1])
 ym,um=P.midpoint(yc,uc);groups=[]
 for ys,us,aa in ((yc,uc,P.scalar_nodes[:,0]),(ym,um,P.scalar_mid[:,0])):
  group=np.empty((len(ys),F.out_n))
  for i,(y,u,a)in enumerate(zip(ys,us,aa)):
   _,d,_=P.q.jet(y);V=P.q.jet(u)[0]
   point=np.c_[np.sum(V*d,axis=1)/a,np.sum(d*d,axis=1)/(a*a)-rho*rho,np.sum(V*V,axis=1)-1]
   group[i]=F.project_constraints((point.imag/eps).T[None,:,:])[0]
  groups.append(group.ravel())
 return np.r_[*groups,P.boundary(yc).imag/eps]

def main(a):
 start=time.perf_counter()
 if sha(a.matrix_source)!=MATRIX_SHA:raise ValueError('Original matrix source changed')
 base=load(a.matrix_source,'direct_gram_original_matrix');p,P,identities=base.initialize(a)
 identities[str(a.matrix_source)]=MATRIX_SHA;identities[str(Path(__file__))]=sha(__file__)
 Gram=factory(base);J=Gram(P,P.Y,P.U);R=J.residual()
 nu=np.r_[P.q.freq,P.q.freq[1:],P.q.freq];idx=np.arange(P.n)
 phase=P.x[:,None]*(1+idx%7)[None,:]+.37*idx[None,:]
 dY=1e-4*np.cos(phase)/(1+nu[None,:]**2);dU=1e-4*np.sin(phase+.23)/(1+nu[None,:])
 delta=np.r_[dY.ravel(),dU.ravel()];idx=np.arange(J.rows);w=np.sin(.731*idx)+.21*np.cos(.217*idx)
 tick=time.perf_counter();jv=J.matvec(delta);forward=time.perf_counter()-tick
 tick=time.perf_counter();jtw=J.rmatvec(w);transpose=time.perf_counter()-tick
 reference=independent_direction(P,J.F,dY,dU);difference=jv-reference;lhs=base.inner(jv,w);rhs=base.inner(delta,jtw)
 # Isolate the global target derivative: a weight in a far-node angular row
 # contributes to Y0_R, even though that node's local geometry is independent.
 remote_mode=7;remote=np.zeros(J.rows);remote[(P.m-1)*J.F.out_n+2*P.M+remote_mode]=1.
 remote_grad=J.rmatvec(remote);remote_core=remote_grad[:P.n]
 beta=-4*J.rho*np.cos(2*remote_mode*P.q.angle)
 direct_core=(1-P.q.freq[1:]**2)*(np.cos(P.q.angle[:,None]*P.q.freq[None,1:]).T@beta/P.N)
 p.assert_sources(identities)
 out=dict(scope=__doc__,source_sha256=sha(__file__),identities=identities,
  shape=list(J.shape),M=P.M,N=P.N,nodes=P.m,full_scalar_dimension=J.F.out_n,
  polynomial_rows='v.d/a, d.d/a^2-rho(core)^2, v.v-1',
  rho_definition='1+sum_(j=1..M)(1-(2j)^2)*Y0_Rj*cos(2j*phi); constant1 fixed',
  variable_core_global_jacobian_included=True,original_BC_rows_preserved=True,
  new_mirror_velocity_constraints_enforced=False,
  raw_polynomial_Gram_SSE=R['cost'],node_max=maximum(R['nodes']),midpoint_max=maximum(R['middle']),BC_max=maximum(R['boundary']),
  node_group_max=[maximum(R['nodes'][:,sl])for sl in (slice(0,2*P.M),slice(2*P.M,4*P.M+1),slice(4*P.M+1,None))],
  midpoint_group_max=[maximum(R['middle'][:,sl])for sl in (slice(0,2*P.M),slice(2*P.M,4*P.M+1),slice(4*P.M+1,None))],
  full_Jv_complex_step_relative_L2=float(np.linalg.norm(difference)/np.linalg.norm(reference)),
  full_Jv_complex_step_max=maximum(difference),
  full_adjoint=dict(left=float(lhs),right=float(rhs),absolute=float(abs(lhs-rhs)),
   relative_to_inner_products=float(abs(lhs-rhs)/max(abs(lhs),abs(rhs),np.finfo(float).tiny))),
  remote_angular_row_core_gradient_max=maximum(remote_core[1:P.M+1]),
  remote_core_gradient_direct_cosine_sum_max_difference=maximum(remote_core[1:P.M+1]-direct_core),
  cached_first_jet_bytes=sum(z.nbytes for loc in (J.node,J.middle)for z in (loc.d,loc.V)),
  Jv_seconds=forward,Jtw_seconds=transpose,seconds=time.perf_counter()-start,
  maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
  linear_solve_executed=False,nonlinear_solve_executed=False,accepted_parent=False,
  continuous_metric_certified=False,arithmetic='Ordinary binary64 FFT and complex-step checks, not an interval certificate.')
 a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
 print(json.dumps(dict(report=str(a.out),sha256=sha(a.out),**out)),flush=True)

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','out'):a.add_argument('--'+key,type=Path,required=True)
 main(a.parse_args())
