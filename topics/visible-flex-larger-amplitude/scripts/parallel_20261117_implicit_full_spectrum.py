#!/usr/bin/env python3
"""All quadratic angular coefficients of the complete fixed implicit problem.

The Y/U space remains M160; each node and actual Hermite midpoint now exposes
every sine/cosine coefficient through scalar mode2M. This rectangular operator
does not solve a BVP or change the currently running retained-Pr LM budget.
"""
import argparse,hashlib,importlib.util,json,resource,time
from pathlib import Path
import numpy as np

MATRIX_SHA='ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4'
PREPARATION_SHA='63c9bcd28fb25d22f7e56f874c210e597850b106e563d4e8567872e6321aa0ff'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def maximum(v):return float(np.max(np.abs(v)))

def factory(base):
 class FullSpectrumBatch(base.FourierBatch):
  def __init__(self,M,N):
   super().__init__(M,N)
   if N<=12*M:raise ValueError('The complete adjoint products must fit below Nyquist')
   self.out_modes=2*M;self.out_n=6*M+2;self.out_freq=2*np.arange(2*M+1)
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

 class FullLocalLinear(base.LocalLinear):
  def jvp(self,dY,dU):
   F=self.F;out=np.empty((len(dY),F.out_n))
   for start in range(0,self.size,self.chunk):
    sl=slice(start,min(start+self.chunk,self.size));_,dd,de=F.jet(dY[sl]);dv=F.synthesize(dU[sl])
    d,e,V=self.d[sl],self.e[sl],self.V[sl];r=np.empty((len(d),3,F.N))
    r[:,0]=np.sum(dv*d+V*dd,axis=1)
    r[:,1]=np.sum(dv*e+V*de+2*self.k[sl,None,None]*d*dd,axis=1)
    r[:,2]=2*np.sum(V*dv,axis=1);out[sl]=F.project_constraints(r)
   return out
  def jtv(self,w):
   F=self.F;gy=np.empty((len(w),F.n));gu=np.empty_like(gy)
   for start in range(0,self.size,self.chunk):
    sl=slice(start,min(start+self.chunk,self.size));eta=F.constraint_weight_field(w[sl])
    d,e,V=self.d[sl],self.e[sl],self.V[sl]
    a=eta[:,0,None,:]*V+2*self.k[sl,None,None]*eta[:,1,None,:]*d;b=eta[:,1,None,:]*V
    ah=F.vector_spec(a);bh=F.vector_spec(b)
    gy[sl]=F.adjoint_pack(-F.angle_derivative_spec(ah)+F.angle_derivative_spec(F.angle_derivative_spec(bh)))
    gu[sl]=F.adjoint_pack(F.vector_spec(eta[:,0,None,:]*d+eta[:,1,None,:]*e+2*eta[:,2,None,:]*V))
   return gy,gu
  def residual(self):
   out=np.empty((self.size,self.F.out_n))
   for start in range(0,self.size,self.chunk):
    sl=slice(start,min(start+self.chunk,self.size));d,e,V=self.d[sl],self.e[sl],self.V[sl]
    r=np.empty((len(d),3,self.F.N));r[:,0]=np.sum(V*d,axis=1)
    r[:,1]=np.sum(V*e,axis=1)+self.k[sl,None]*np.sum(d*d,axis=1)
    r[:,2]=np.sum(V*V,axis=1)-1;out[sl]=self.F.project_constraints(r)
   return out

 class FullLinear(base.CompleteLinear):
  def __init__(self,P,Y,U,chunk=32):
   self.P=P;self.F=FullSpectrumBatch(P.M,P.N);self.node=FullLocalLinear(self.F,Y,U,P.k,chunk)
   ym,um=P.midpoint(Y,U);self.middle=FullLocalLinear(self.F,ym,um,P.km,chunk)
   self.variables=2*P.m*P.n;self.rows=(2*P.m-1)*self.F.out_n+P.n
   self.shape=(self.rows,self.variables);self.dtype=np.dtype(float);self.matvec_count=0;self.rmatvec_count=0
   self.boundary_residual=P.boundary(Y)
  def rmatvec(self,w):
   P=self.P;nout=self.F.out_n;w=np.asarray(w).reshape(-1)
   wn=w[:P.m*nout].reshape(P.m,nout);wm=w[P.m*nout:-P.n].reshape(P.m-1,nout);wb=w[-P.n:]
   gY,gU=self.node.jtv(wn);a,b=self.middle.jtv(wm);h=P.h[:,None]
   gY[:-1]+=.5*a-1.5*b/h;gY[1:]+=.5*a+1.5*b/h
   gU[:-1]+=h*a/8-.25*b;gU[1:]+=-h*a/8-.25*b
   gY[0]+=P.BA.T@wb;gY[-1]+=P.BB.T@wb;self.rmatvec_count+=1
   return np.r_[gY.ravel(),gU.ravel()]
  def residual(self):
   nodes=self.node.residual();middle=self.middle.residual();bc=self.boundary_residual.copy()
   cost=float(np.sum(nodes*nodes)+np.sum(middle*middle)+np.sum(bc*bc))
   return dict(nodes=nodes,middle=middle,boundary=bc,cost=cost,
    finite=bool(np.isfinite(nodes).all()and np.isfinite(middle).all()and np.isfinite(bc).all()and np.isfinite(cost)))
 return FullLinear

def complex_direction(P,F,dY,dU,eps=1e-25):
 # Independent physical evaluation using the published non-batched complex jet.
 yc=P.Y.astype(complex)+1j*eps*dY;uc=P.U.astype(complex)+1j*eps*dU
 ym,um=P.midpoint(yc,uc);groups=[]
 for ys,us,ks in ((yc,uc,P.k),(ym,um,P.km)):
  group=np.empty((len(ys),F.out_n))
  for i,(y,u,k)in enumerate(zip(ys,us,ks)):
   point=P.operator.point_residual(y,u,k).imag/eps
   group[i]=F.project_constraints(point.T[None,:,:])[0]
  groups.append(group.ravel())
 return np.r_[*groups,P.boundary(yc).imag/eps]

def main(a):
 start=time.perf_counter()
 if sha(a.matrix_source)!=MATRIX_SHA or sha(a.original_preparation)!=PREPARATION_SHA:raise ValueError('Frozen reference changed')
 base=load(a.matrix_source,'all_quadratic_matrix');p,P,identities=base.initialize(a)
 identities.update({str(a.matrix_source):MATRIX_SHA,str(a.original_preparation):PREPARATION_SHA,str(Path(__file__)):sha(__file__)})
 FullLinear=factory(base);J=FullLinear(P,P.Y,P.U);R=J.residual();M=P.M
 keep=np.r_[np.arange(M),2*M+np.arange(M+1),4*M+1+np.arange(M+1)]
 omitted=np.setdiff1d(np.arange(J.F.out_n),keep)
 retained_cost=float(np.sum(np.ascontiguousarray(R['nodes'][:,keep])**2)+np.sum(np.ascontiguousarray(R['middle'][:,keep])**2)+np.sum(R['boundary']**2))
 omitted_cost=float(np.sum(R['nodes'][:,omitted]**2)+np.sum(R['middle'][:,omitted]**2))
 prior=json.loads(a.original_preparation.read_text());old_cost=prior['initial_residual']['raw_residual_square_sum']
 nu=np.r_[P.q.freq,P.q.freq[1:],P.q.freq];idx=np.arange(P.n);phase=P.x[:,None]*(1+idx%7)[None,:]+.37*idx[None,:]
 dY=1e-4*np.cos(phase)/(1+nu[None,:]**2);dU=1e-4*np.sin(phase+.23)/(1+nu[None,:]);delta=np.r_[dY.ravel(),dU.ravel()]
 idx=np.arange(J.rows);w=np.sin(.731*idx)+.21*np.cos(.217*idx)
 tick=time.perf_counter();jv=J.matvec(delta);jv_seconds=time.perf_counter()-tick
 tick=time.perf_counter();jtw=J.rmatvec(w);jtw_seconds=time.perf_counter()-tick
 reference=complex_direction(P,J.F,dY,dU);difference=jv-reference;lhs=base.inner(jv,w);rhs=base.inner(delta,jtw)
 groups=[]
 for name in ('nodes','middle'):
  for row,offset,length in ((0,0,2*M),(1,2*M,2*M+1),(2,4*M+1,2*M+1)):
   z=R[name][:,offset:offset+length];cut=M if row==0 else M+1
   groups.append(dict(group=name,row=row,full_scalar_rows=z.size,
    retained_SSE=float(base.inner(z[:,:cut],z[:,:cut])),omitted_SSE=float(base.inner(z[:,cut:],z[:,cut:])),
    full_max=maximum(z),omitted_max=maximum(z[:,cut:])))
 p.assert_sources(identities)
 out=dict(scope=__doc__,source_sha256=sha(__file__),identities=identities,M=P.M,N=P.N,nodes=P.m,
  state_dimension=P.n,full_scalar_dimension=J.F.out_n,shape=list(J.shape),node_rows=P.m*J.F.out_n,
  midpoint_rows=(P.m-1)*J.F.out_n,boundary_rows=P.n,extra_rows=(2*P.m-1)*3*P.M,
  all_quadratic_modes_included=True,retained_selection=keep.tolist(),unretained_selection=omitted.tolist(),
  original_retained_raw_SSE=old_cost,reselected_retained_raw_SSE=retained_cost,retained_cost_difference=retained_cost-old_cost,
  added_quadratic_mode_SSE=omitted_cost,full_quadratic_raw_SSE=R['cost'],full_SSE_minus_parts=R['cost']-retained_cost-omitted_cost,
  per_group=groups,full_direction_complex_step_relative_L2=float(np.linalg.norm(difference)/np.linalg.norm(reference)),
  full_direction_complex_step_max=maximum(difference),full_adjoint=dict(left=float(lhs),right=float(rhs),
   absolute=float(abs(lhs-rhs)),relative_to_inner_products=float(abs(lhs-rhs)/max(abs(lhs),abs(rhs),np.finfo(float).tiny)),
   relative_to_norm_products=float(abs(lhs-rhs)/(np.linalg.norm(jv)*np.linalg.norm(w)+np.linalg.norm(delta)*np.linalg.norm(jtw)))),
  complete_Jv_seconds=jv_seconds,complete_Jtw_seconds=jtw_seconds,
  cached_local_geometry_bytes=sum(z.nbytes for loc in (J.node,J.middle)for z in (loc.d,loc.e,loc.V)),
  maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,seconds=time.perf_counter()-start,
  nonlinear_solve_executed=False,linear_solve_executed=False,accepted_parent=False,continuous_metric_certified=False,
  interpretation='This all-quadratic-coefficient least-squares objective differs from retained Pr. No exact finite noncircular zero or actual BVP solution is asserted.',
  arithmetic='Ordinary binary64 FFTs and long-double dot accumulation; no interval rounding certificate.')
 a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ('retained_selection','unretained_selection')}),flush=True)
 print(json.dumps(dict(report=str(a.out),sha256=sha(a.out))),flush=True)

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','original-preparation','out'):a.add_argument('--'+key,type=Path,required=True)
 main(a.parse_args())
