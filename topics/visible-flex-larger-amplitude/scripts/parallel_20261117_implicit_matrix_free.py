#!/usr/bin/env python3
"""Complete finite Pr Jacobian actions and Euclidean adjoints by batched FFT.

The fixed 602-node problem, all 580328 rows, Fourier slots, actual Hermite
midpoints and original boundary rows are unchanged. No C_U inverse, global
Jacobian assembly, nonlinear solve, or accepted geometry is asserted here.
"""
import argparse,gzip,hashlib,importlib.util,json,resource,sys,time
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator

PROBLEM_SHA='5b965b9c4f9979a5b8dcc38661de027570d04d55aceb86de0dc7b1217fb03aac'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def maximum(a):return float(np.max(np.abs(a)))
def inner(a,b):return np.sum(np.asarray(a,dtype=np.longdouble)*np.asarray(b,dtype=np.longdouble),dtype=np.longdouble)
def flatten(r):return np.r_[r['nodes'].ravel(),r['middle'].ravel(),r['boundary']]

class FourierBatch:
 def __init__(self,M,N):
  if N<=8*M:raise ValueError('All physical quadratic frequencies must fit below Nyquist')
  self.M,self.N,self.n=M,N,3*M+2;self.freq=2*np.arange(M+1)
  self.imul=1j*np.arange(N//2+1)[None,None,:]
 def state_spec(self,y):
  M,N=self.M,self.N;y=np.asarray(y);z=np.zeros((len(y),3,N//2+1),complex)
  z[:,0,self.freq]=N/2*y[:,:M+1];z[:,1,self.freq[1:]]=-1j*N/2*y[:,M+1:2*M+1]
  z[:,2,self.freq]=N/2*y[:,2*M+1:];z[:,0,0]*=2;z[:,2,0]*=2
  return z
 def jet(self,y):
  z=self.state_spec(y);v=np.fft.irfft(z,n=self.N,axis=-1)
  d=np.fft.irfft(z*self.imul,n=self.N,axis=-1);e=np.fft.irfft(z*self.imul**2,n=self.N,axis=-1)
  e[:,0]-=2*d[:,1]+v[:,0];e[:,1]+=2*d[:,0]-v[:,1]
  d[:,0]-=v[:,1];d[:,1]+=v[:,0]
  return v,d,e
 def synthesize(self,y):return np.fft.irfft(self.state_spec(y),n=self.N,axis=-1)
 def project_constraints(self,r):
  z=np.fft.rfft(r,axis=-1)/self.N;M=self.M
  a=-2*z[:,0,self.freq[1:]].imag;b=2*z[:,1,self.freq].real;c=2*z[:,2,self.freq].real
  b[:,0]*=.5;c[:,0]*=.5
  return np.concatenate((a,b,c),axis=-1)
 def constraint_weight_field(self,w):
  # This is S_C D_C w, not P_C^T w. The missing factor 1/N
  # cancels exactly against S_Y^T when returning coefficient gradients.
  M,N=self.M,self.N;z=np.zeros((len(w),3,N//2+1),complex)
  z[:,0,self.freq[1:]]=-1j*N*w[:,:M]
  z[:,1,self.freq]=N*w[:,M:2*M+1]
  z[:,2,self.freq]=N*w[:,2*M+1:]
  return np.fft.irfft(z,n=N,axis=-1)
 def vector_spec(self,v):return (np.fft.rfft(v,axis=-1)/self.N)[:,:,self.freq]
 def angle_derivative_spec(self,z):
  # Apply the true rotating-frame derivative, including its skew connection.
  a=z*(1j*self.freq)[None,None,:];a[:,0]-=z[:,1];a[:,1]+=z[:,0]
  return a
 def adjoint_pack(self,z):
  # D_Y^{-1} P_Y: all cosine entries take Re, all sine entries -Im.
  # The zero cosine coefficient and nonzero coefficients have different
  # P_Y and D_Y factors which cancel to this same expression.
  return np.concatenate((z[:,0].real,-z[:,1,1:].imag,z[:,2].real),axis=-1)

class LocalLinear:
 def __init__(self,F,Y,U,k,chunk=32):
  self.F=F;self.k=np.asarray(k);self.chunk=chunk;self.size=len(Y)
  shape=(self.size,3,F.N);self.d=np.empty(shape);self.e=np.empty(shape);self.V=np.empty(shape)
  for start in range(0,self.size,chunk):
   sl=slice(start,min(start+chunk,self.size));_,self.d[sl],self.e[sl]=F.jet(Y[sl]);self.V[sl]=F.synthesize(U[sl])
 def jvp(self,dY,dU):
  F=self.F;out=np.empty_like(dY)
  for start in range(0,self.size,self.chunk):
   sl=slice(start,min(start+self.chunk,self.size));_,dd,de=F.jet(dY[sl]);dv=F.synthesize(dU[sl])
   d,e,V=self.d[sl],self.e[sl],self.V[sl];r=np.empty((len(d),3,F.N))
   r[:,0]=np.sum(dv*d+V*dd,axis=1)
   r[:,1]=np.sum(dv*e+V*de+2*self.k[sl,None,None]*d*dd,axis=1)
   r[:,2]=2*np.sum(V*dv,axis=1);out[sl]=F.project_constraints(r)
  return out
 def jtv(self,w):
  F=self.F;gy=np.empty_like(w);gu=np.empty_like(w)
  for start in range(0,self.size,self.chunk):
   sl=slice(start,min(start+self.chunk,self.size));eta=F.constraint_weight_field(w[sl])
   d,e,V=self.d[sl],self.e[sl],self.V[sl];a=eta[:,0,None,:]*V+2*self.k[sl,None,None]*eta[:,1,None,:]*d
   b=eta[:,1,None,:]*V
   # Multiply first at full N; then transform the full products. The constant
   # connection and angular derivative do not couple Fourier frequencies,
   # so selecting retained output frequencies after this FFT is exact.
   ah=F.vector_spec(a);bh=F.vector_spec(b)
   gy[sl]=F.adjoint_pack(-F.angle_derivative_spec(ah)+F.angle_derivative_spec(F.angle_derivative_spec(bh)))
   gu[sl]=F.adjoint_pack(F.vector_spec(eta[:,0,None,:]*d+eta[:,1,None,:]*e+2*eta[:,2,None,:]*V))
  return gy,gu

class CompleteLinear:
 def __init__(self,P,Y,U,chunk=32):
  self.P=P;self.F=FourierBatch(P.M,P.N);self.node=LocalLinear(self.F,Y,U,P.k,chunk)
  ym,um=P.midpoint(Y,U);self.middle=LocalLinear(self.F,ym,um,P.km,chunk)
  self.variables=2*P.m*P.n;self.shape=(self.variables,self.variables);self.dtype=np.dtype(float)
  self.matvec_count=0;self.rmatvec_count=0
 def matvec(self,v):
  P=self.P;v=np.asarray(v).reshape(-1);dY=v[:P.m*P.n].reshape(P.m,P.n);dU=v[P.m*P.n:].reshape(P.m,P.n)
  ym,um=P.midpoint(dY,dU);self.matvec_count+=1
  return np.r_[self.node.jvp(dY,dU).ravel(),self.middle.jvp(ym,um).ravel(),P.BA@dY[0]+P.BB@dY[-1]]
 def rmatvec(self,w):
  P=self.P;w=np.asarray(w).reshape(-1);wn=w[:P.m*P.n].reshape(P.m,P.n)
  wm=w[P.m*P.n:-P.n].reshape(P.m-1,P.n);wb=w[-P.n:];gY,gU=self.node.jtv(wn);a,b=self.middle.jtv(wm)
  h=P.h[:,None];gY[:-1]+=.5*a-1.5*b/h;gY[1:]+=.5*a+1.5*b/h
  gU[:-1]+=h*a/8-.25*b;gU[1:]+=-h*a/8-.25*b
  gY[0]+=P.BA.T@wb;gY[-1]+=P.BB.T@wb;self.rmatvec_count+=1
  return np.r_[gY.ravel(),gU.ravel()]
 def operator(self):return LinearOperator(self.shape,matvec=self.matvec,rmatvec=self.rmatvec,dtype=float)

def initialize(a):
 if sha(a.problem_source)!=PROBLEM_SHA:raise ValueError('Not the frozen complete Problem')
 p=load(a.problem_source,'matrix_free_problem');scripts=a.topic/'scripts';sys.path.insert(0,str(scripts))
 hp=scripts/'parallel_20261117_negative_hold_profile_ivp.py';fs=scripts/'parallel_20261117_frenet_symbol.py'
 identities={str(a.problem_source):PROBLEM_SHA,str(a.warm):p.WARM_SHA,str(a.polynomial_source):p.POLYNOMIAL_SHA,
  str(hp):p.HOLD_SHA,str(fs):p.FRENET_SHA,str(scripts/'parallel_20261117_profile.py'):p.PROFILE_SHA,
  str(scripts/'parallel_20261117_inward_profile.py'):p.INWARD_SHA,str(Path(__file__)):sha(__file__)}
 p.assert_sources(identities);d=json.loads(gzip.decompress(a.warm.read_bytes()))
 P=p.Problem(d,load(fs,'matrix_free_fs'),load(hp,'matrix_free_hp'),load(a.polynomial_source,'matrix_free_poly'))
 return p,P,identities

def main(a):
 started=time.perf_counter();p,P,identities=initialize(a)
 if sha(a.ray_source)!=a.ray_sha256:raise ValueError('The independent forward-action source changed')
 identities[str(a.ray_source)]=a.ray_sha256;ray=load(a.ray_source,'matrix_free_reference_ray')
 begin=time.perf_counter();J=CompleteLinear(P,P.Y,P.U);build=time.perf_counter()-begin
 nu=np.r_[P.q.freq,P.q.freq[1:],P.q.freq];j=np.arange(P.n)
 phase=P.x[:,None]*(1+j%7)[None,:]+.37*j[None,:]
 dY=1e-4*np.cos(phase)/(1+nu[None,:]**2);dU=1e-4*np.sin(phase+.23)/(1+nu[None,:])
 delta=np.r_[dY.ravel(),dU.ravel()];idx=np.arange(J.shape[0]);w=np.sin(.731*idx)+.21*np.cos(.217*idx)
 begin=time.perf_counter();jv=J.matvec(delta);forward=time.perf_counter()-begin
 begin=time.perf_counter();jtw=J.rmatvec(w);transpose=time.perf_counter()-begin
 ref,_=ray.terms(P,P.Y,P.U,dY,dU);reference=flatten(ref);difference=jv-reference
 lhs,rhs=inner(jv,w),inner(delta,jtw)
 adjoint=dict(left=float(lhs),right=float(rhs),absolute=float(abs(lhs-rhs)),
  relative_to_inner_products=float(abs(lhs-rhs)/max(abs(lhs),abs(rhs),np.finfo(float).tiny)),
  relative_to_norm_products=float(abs(lhs-rhs)/(np.linalg.norm(jv)*np.linalg.norm(w)+np.linalg.norm(delta)*np.linalg.norm(jtw))))
 dense=[]
 for i in (0,528,581,601):
  fy,fu=P.operator.jacobians(P.Y[i],P.U[i],P.k[i]);ww=w[i*P.n:(i+1)*P.n][None,:]
  loc=LocalLinear(J.F,P.Y[i:i+1],P.U[i:i+1],P.k[i:i+1]);ay,au=loc.jtv(ww)
  gy,gu=fy.T@ww[0],fu.T@ww[0];err=np.r_[ay[0]-gy,au[0]-gu];expected=np.r_[gy,gu]
  dense.append(dict(node=i,s=float(P.x[i]),adjoint_absolute_max=maximum(err),adjoint_relative_L2=float(np.linalg.norm(err)/np.linalg.norm(expected))))
 p.assert_sources(identities)
 n=P.m*P.n;out=dict(scope=__doc__,source_sha256=sha(__file__),identities=identities,
  shape=list(J.shape),node_rows=n,midpoint_rows=(P.m-1)*P.n,boundary_rows=P.n,
  variable_order='all Y nodes followed by all independent U nodes',row_order='all node constraints, all actual cubic midpoint constraints, all original BC',
  actual_core_and_scalar_unchanged=True,complete_forward_reference=dict(source_sha256=a.ray_sha256,
   node_absolute_max=maximum(difference[:n]),midpoint_absolute_max=maximum(difference[n:-P.n]),boundary_absolute_max=maximum(difference[-P.n:]),
   relative_L2=float(np.linalg.norm(difference)/np.linalg.norm(reference))),
  full_adjoint_dot_product=adjoint,dense_complete_local_adjoint_comparisons=dense,
  cached_actual_local_values_bytes=sum(z.nbytes for loc in (J.node,J.middle)for z in (loc.d,loc.e,loc.V)),
  build_seconds=build,matvec_seconds=forward,rmatvec_seconds=transpose,seconds=time.perf_counter()-started,
  maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
  nonlinear_solve_executed=False,linear_system_solved=False,accepted_parent=False,continuous_geometry_certified=False,
  arithmetic='Ordinary binary64 FFTs; long-double dot accumulation. These numerical checks do not bound all rounding errors.')
 a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
 print(json.dumps(dict(report=str(a.out),report_sha256=sha(a.out),**out),allow_nan=False),flush=True)

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','ray-source','out'):a.add_argument('--'+key,type=Path,required=True)
 a.add_argument('--ray-sha256',required=True);main(a.parse_args())
