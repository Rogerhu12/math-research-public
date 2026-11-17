#!/usr/bin/env python3
"""Invertible integrated coordinates and all-row column norms for fixed Pr.

C=Y0, all original U, and all trapezoidal compatibility defects remain free.
This does not replace the cubic field or discard defects. The original LM run
is unchanged; this is one preparation/probe, not a new linear/nonlinear solve.
"""
import argparse,hashlib,importlib.util,json,resource,time
from pathlib import Path
import numpy as np
from scipy.linalg import cho_factor,cho_solve

MATRIX_SHA='ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def maximum(z):return float(np.max(np.abs(z)))
def columns(a):return np.asarray(np.sum(a*a,axis=0,dtype=np.longdouble),float)
def cross_columns(a,b):return np.asarray(np.sum(a*b,axis=0,dtype=np.longdouble),float)

class IntegratedCoordinates:
 def __init__(self,P):
  self.P=P;self.m=P.m;self.n=P.n;self.h=P.h.copy();self.omega=np.zeros(P.m)
  self.omega[:-1]+=self.h/2;self.omega[1:]+=self.h/2
  self.size=2*self.m*self.n
 def unpack(self,z):
  z=np.asarray(z).reshape(-1);n,m=self.n,self.m
  if len(z)!=self.size:raise ValueError('Wrong integrated coordinate size')
  return z[:n],z[n:(m+1)*n].reshape(m,n),z[(m+1)*n:].reshape(m-1,n)
 def lift(self,z):
  C,U,D=self.unpack(z);increments=self.h[:,None]*(.5*(U[:-1]+U[1:])+D)
  Y=np.empty_like(U);Y[0]=C;Y[1:]=C+np.cumsum(increments,axis=0)
  return np.r_[Y.ravel(),U.ravel()]
 def inverse(self,x):
  x=np.asarray(x).reshape(-1);n,m=self.n,self.m;Y=x[:m*n].reshape(m,n);U=x[m*n:].reshape(m,n)
  D=np.diff(Y,axis=0)/self.h[:,None]-.5*(U[:-1]+U[1:])
  return np.r_[Y[0],U.ravel(),D.ravel()]
 def pullback(self,g):
  g=np.asarray(g).reshape(-1);m,n=self.m,self.n;gY=g[:m*n].reshape(m,n);gU=g[m*n:].reshape(m,n).copy()
  suffix=np.cumsum(gY[:0:-1],axis=0)[::-1];w=self.h[:,None]*suffix
  gU[:-1]+=.5*w;gU[1:]+=.5*w
  return np.r_[np.sum(gY,axis=0),gU.ravel(),w.ravel()]
 def boundary(self,z):
  C,U,D=self.unpack(z);end=C+self.omega@U+self.h@D
  return self.P.BA@C+self.P.BB@end
 def boundary_transpose(self,w):
  u=self.P.BB.T@w;c=self.P.BA.T@w+u
  return np.r_[c,(self.omega[:,None]*u).ravel(),(self.h[:,None]*u).ravel()]

def complete_column_diagonal(P,T):
 """Exact real-arithmetic diagonal formula; floating local moments retained."""
 node=np.empty((P.m,3,P.n));mid=np.empty((P.m-1,3,P.n));ym,um=P.midpoint(P.Y,P.U)
 start=time.perf_counter()
 for name,ys,us,ks,moments in (('node',P.Y,P.U,P.k,node),('midpoint',ym,um,P.km,mid)):
  for i,(y,u,k)in enumerate(zip(ys,us,ks)):
   fy,fu=P.operator.jacobians(y,u,k)
   moments[i,0]=columns(fy);moments[i,1]=columns(fu);moments[i,2]=cross_columns(fy,fu)
   if (i+1)%100==0:print(json.dumps(dict(event='integrated_column_moments',group=name,completed=i+1,total=len(ys),seconds=time.perf_counter()-start)),flush=True)
 an,bn,cn=node[:,0],node[:,1],node[:,2];am,bm,cm=mid[:,0],mid[:,1],mid[:,2]
 # Each suffix at k contains only rows strictly after k.
 sn=np.zeros_like(an);sn[:-1]=np.cumsum(an[:0:-1],axis=0)[::-1]
 sm=np.zeros_like(am);sm[:-1]=np.cumsum(am[:0:-1],axis=0)[::-1]
 bb=columns(P.BB);dc=np.sum(an,axis=0)+np.sum(am,axis=0)+columns(P.BA+P.BB)
 dd=T.h[:,None]**2*(sn[:-1]+sm+bb)
 dd+=T.h[:,None]**2/4*am+1.5*T.h[:,None]*cm+2.25*bm
 du=np.empty_like(an)
 for k in range(P.m):
  hp=T.h[k-1]if k else 0.;hn=T.h[k]if k<P.m-1 else 0.;ak=hp/2;om=T.omega[k]
  far=sn[k]+(sm[k]if k<P.m-1 else 0.)+bb
  value=ak*ak*an[k]+2*ak*cn[k]+bn[k]+om*om*far
  if k:
   yy=hp/8;value+=yy*yy*am[k-1]+yy*cm[k-1]+.25*bm[k-1]
  if k<P.m-1:
   yy=hp/2+3*hn/8;value+=yy*yy*am[k]+yy*cm[k]+.25*bm[k]
  du[k]=value
 diag=np.r_[dc,du.ravel(),dd.ravel()]
 if not np.isfinite(diag).all()or np.min(diag)<=0:raise ValueError('Nonpositive/nonfinite integrated diagonal')
 return diag,node,mid

class IntegratedBoundary:
 """C=B T S, its exact small Gram, and row-normalized affine projector."""
 def __init__(self,P,T,S):
  self.P,self.T,self.S=P,T,np.asarray(S)
  if len(self.S)!=T.size or not np.isfinite(self.S).all()or np.min(self.S)<=0:raise ValueError('Bad positive integrated scale')
  sc,su,sd=T.unpack(self.S);A=P.BA+P.BB
  tail=np.sum((T.omega[:,None]*su)**2,axis=0)+np.sum((T.h[:,None]*sd)**2,axis=0)
  G=(A*(sc*sc))@A.T+(P.BB*tail)@P.BB.T
  self.row_norm=np.sqrt(np.diag(G));self.normalized_gram=G/self.row_norm[:,None]/self.row_norm[None,:]
  self.factor=cho_factor(self.normalized_gram,lower=True,check_finite=True)
 def apply(self,z):return self.T.boundary(self.S*z)
 def transpose(self,w):return self.S*self.T.boundary_transpose(w)
 def normal_solve(self,w):return cho_solve(self.factor,w/self.row_norm,check_finite=True)/self.row_norm
 def project(self,z):
  z=np.asarray(z).reshape(-1);return z-self.transpose(self.normal_solve(self.apply(z)))
 def lift(self,z):return self.T.lift(self.S*self.project(z))
 def pullback(self,g):return self.project(self.S*self.T.pullback(g))
 def affine(self,residual):return self.T.lift(self.S*self.transpose(self.normal_solve(-residual)))

def main(a):
 start=time.perf_counter()
 if sha(a.matrix_source)!=MATRIX_SHA:raise ValueError('Original matrix source changed')
 base=load(a.matrix_source,'integrated_matrix');p,P,identities=base.initialize(a)
 identities[str(a.matrix_source)]=MATRIX_SHA;identities[str(Path(__file__))]=sha(__file__)
 T=IntegratedCoordinates(P);x=np.r_[P.Y.ravel(),P.U.ravel()];zin=T.inverse(x);roundtrip=T.lift(zin)-x
 tick=time.perf_counter();diagonal,nmom,mmom=complete_column_diagonal(P,T);moment_seconds=time.perf_counter()-tick
 S=1/np.sqrt(diagonal)
 prepared=a.out.with_suffix('.prepared.npz');np.savez_compressed(prepared,scale=S,diagonal=diagonal,node_moments=nmom,midpoint_moments=mmom)
 print(json.dumps(dict(event='integrated_column_diagonal_complete',prepared=str(prepared),sha256=sha(prepared))),flush=True)
 B=IntegratedBoundary(P,T,S);J=base.CompleteLinear(P,P.Y,P.U)
 # These complete columns test both radial endpoints, both local midpoint
 # blocks, far-node sums, all Fourier blocks, and all original BC rows.
 checks=[]
 selected=[0,P.M+3,2*P.M+6,P.n+3,P.n+529*P.n+P.M+7,P.n+601*P.n+2*P.M+9,(P.m+1)*P.n+5,(P.m+1)*P.n+573*P.n+P.M+11,(P.m+1)*P.n+600*P.n+2*P.M+13]
 for index in selected:
  z=np.zeros(T.size);z[index]=1.;col=J.matvec(T.lift(z));actual=float(base.inner(col,col));expected=float(diagonal[index])
  checks.append(dict(index=index,formula=expected,complete_column_norm_squared=actual,relative_difference=abs(actual-expected)/max(actual,expected)))
 j=np.arange(T.size);z=1e-5*(np.sin(.173*j)+.17*np.cos(.271*j));g=np.cos(.137*j)+.31*np.sin(.319*j)
 left=base.inner(T.lift(z),g);right=base.inner(z,T.pullback(g))
 w=np.sin(.321*np.arange(P.n));c_left=base.inner(B.apply(z),w);c_right=base.inner(z,B.transpose(w))
 projected=B.project(z);d0=B.affine(P.boundary(P.Y));affine_B=P.BA@d0[:P.n]+P.BB@d0[(P.m-1)*P.n:P.m*P.n]
 q=np.sin(.019*np.arange(J.shape[0]));forward=J.matvec(B.lift(z));backward=B.pullback(J.rmatvec(q));jl=base.inner(forward,q);jr=base.inner(z,backward)
 p.assert_sources(identities)
 out=dict(scope=__doc__,source_sha256=sha(__file__),identities=identities,prepared_path=str(prepared),prepared_sha256=sha(prepared),
  original_warm_sha256=p.WARM_SHA,M=P.M,N=P.N,nodes=P.m,variables=T.size,rows=J.shape[0],
  coordinate_order='C then all original U then all trapezoidal defects D',all_compatibility_defects_retained=True,
  exact_arithmetic_cubic_unchanged=True,physical_roundtrip_max=maximum(roundtrip),
  all_row_diagonal_formula_includes_cross_terms=True,diagonal_min=float(diagonal.min()),diagonal_max=float(diagonal.max()),
  scale_min=float(S.min()),scale_max=float(S.max()),all_column_moments_seconds=moment_seconds,full_column_checks=checks,
  coordinate_adjoint=dict(left=float(left),right=float(right),absolute=float(abs(left-right))),
  scaled_BTS_adjoint=dict(left=float(c_left),right=float(c_right),absolute=float(abs(c_left-c_right))),
  normalized_boundary_Gram_condition_2=float(np.linalg.cond(B.normalized_gram)),
  projected_boundary_max=maximum(B.apply(projected)),projection_idempotence_max=maximum(B.project(projected)-projected),
  affine_boundary_residual_max=maximum(affine_B+P.boundary(P.Y)),
  complete_scaled_projected_adjoint=dict(left=float(jl),right=float(jr),absolute=float(abs(jl-jr)),relative_to_inner_products=float(abs(jl-jr)/max(abs(jl),abs(jr),np.finfo(float).tiny))),
  seconds=time.perf_counter()-start,maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
  linear_solve_executed=False,nonlinear_solve_executed=False,original_LM_algorithm_changed=False,
  accepted_parent=False,continuous_geometry_certified=False,
  penalty_scope='An ordinary lsmr damp on these coordinates would define a different step norm. Preserving another LM penalty requires its full transformed lower operator block.',
  arithmetic='Exact formulas implemented in ordinary binary64; local column moments use long-double sums. No full interval conditioning certificate.')
 a.out.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n');print(json.dumps(dict(report=str(a.out),sha256=sha(a.out),**out)),flush=True)

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','out'):a.add_argument('--'+key,type=Path,required=True)
 main(a.parse_args())
