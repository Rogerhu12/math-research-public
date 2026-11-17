#!/usr/bin/env python3
"""Prepare the complete polynomial Gram model with T and exact core velocity.

Original1662 Y/U, except explicitly initialize U0=ez. All original position
BC, all962 quadratic Fourier rows at all602 nodes/601 actual cubic midpoints,
and all482 new core velocity rows remain. This is one preparation, no solve.
New moments include the global core-rho cross terms; old Pr moments are not
reused. Completed per-location moments are saved outside Git for exact reuse.
"""
import argparse,hashlib,importlib.util,json,os,resource,time
from pathlib import Path
import numpy as np
from scipy.linalg import cho_factor,cho_solve

MATRIX_SHA='ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4'
GRAM_SHA='5b5ebf5276ab73109859fc03cade7716ca3a6941bb5a5f19890673447db735e6'
COORDINATE_SHA='ef81da0b0de7200501d34d6702f92ae0131a953e9038ad8302d2e1edb61cd3d8'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def maximum(a):return float(np.max(np.abs(a)))
def columns(a):return np.asarray(np.sum(a*a,axis=0,dtype=np.longdouble),float)
def cross_columns(a,b):return np.asarray(np.sum(a*b,axis=0,dtype=np.longdouble),float)
def save_npz(p,**data):
 p=Path(p);tmp=p.with_name(p.name+'.tmp')
 with tmp.open('wb')as f:np.savez_compressed(f,**data);f.flush();os.fsync(f.fileno())
 tmp.replace(p)
def write(p,data):
 p=Path(p);tmp=p.with_name(p.name+'.tmp')
 with tmp.open('w')as f:json.dump(data,f,indent=2,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
 tmp.replace(p)
def core_target(P):
 z=np.zeros(P.n);z[2*P.M+1]=1.;return z
def flatten(r):return np.r_[r['nodes'].ravel(),r['middle'].ravel(),r['boundary'],r['core_velocity']]
def summary(r,M):
 groups=(slice(0,2*M),slice(2*M,4*M+1),slice(4*M+1,None))
 return dict(raw_SSE=r['cost'],finite=r['finite'],node_max=maximum(r['nodes']),midpoint_max=maximum(r['middle']),
  old_BC_max=maximum(r['boundary']),core_velocity_max=maximum(r['core_velocity']),
  node_group_max=[maximum(r['nodes'][:,s])for s in groups],midpoint_group_max=[maximum(r['middle'][:,s])for s in groups],
  core_all962_Gram_rows_max=maximum(r['nodes'][0]))

def augmented_factory(Gram):
 class AugmentedGram(Gram):
  def __init__(self,P,Y,U,chunk=32):
   super().__init__(P,Y,U,chunk);self.core_bc=U[0]-core_target(P)
   self.rows+=P.n;self.shape=(self.rows,self.variables)
  def residual(self):
   r=super().residual();r['core_velocity']=self.core_bc.copy()
   r['cost']+=float(np.sum(self.core_bc*self.core_bc));r['finite']=bool(r['finite']and np.isfinite(self.core_bc).all()and np.isfinite(r['cost']))
   return r
  def matvec(self,v):
   v=np.asarray(v).reshape(-1);k=self.P.m*self.P.n
   return np.r_[super().matvec(v),v[k:k+self.P.n]]
  def rmatvec(self,w):
   w=np.asarray(w).reshape(-1);g=super().rmatvec(w[:-self.P.n]);k=self.P.m*self.P.n
   g[k:k+self.P.n]+=w[-self.P.n:];return g
 return AugmentedGram

def density_matrix(P,F):
 """Exact coefficient formula DG-T2, including the single constant term."""
 M=P.M;G=np.zeros((F.out_n,P.n));q=1-(2*np.arange(M+1))**2;r=q[1:]*P.Y[0,1:M+1]
 for j in range(1,M+1):
  G[2*M+j,j]=-2*q[j]
  for k in range(1,M+1):
   G[2*M+k+j,j]-=q[j]*r[k-1];G[2*M+abs(k-j),j]-=q[j]*r[k-1]
 return G

def local_matrices(F,d,V,a,vbasis,dbasis):
 raw=np.zeros((F.n,3,F.N))
 raw[:,0]=np.einsum('cn,jcn->jn',V,dbasis,optimize=False)/a
 raw[:,1]=2*np.einsum('cn,jcn->jn',d,dbasis,optimize=False)/(a*a)
 L=F.project_constraints(raw).T
 raw.fill(0.)
 raw[:,0]=np.einsum('cn,jcn->jn',d,vbasis,optimize=False)/a
 raw[:,2]=2*np.einsum('cn,jcn->jn',V,vbasis,optimize=False)
 U=F.project_constraints(raw).T
 return L,U

def complete_diagonal(P,T,J,work,binding):
 F=J.F;G=density_matrix(P,F);vbasis,dbasis=F.first_jet(np.eye(P.n))
 node=np.empty((P.m,3,P.n));mid=np.empty((P.m-1,3,P.n));coupled=np.zeros(P.n,dtype=np.longdouble)
 count_new=0;count_reused=0;begin=time.perf_counter()
 for label,loc,aa,moments in (('node',J.node,P.scalar_nodes[:,0],node),('midpoint',J.middle,P.scalar_mid[:,0],mid)):
  for i,a in enumerate(aa):
   file=work/f'moments-{label}-{i:04d}.npz'
   if file.exists():
    with np.load(file,allow_pickle=False)as z:
     if str(z['binding'].item())!=binding or str(z['group'].item())!=label or int(z['index'])!=i:raise ValueError('Moment checkpoint identity differs')
     vals=z['moments'].copy();dc=z['coupled_C'].copy()
    count_reused+=1
   else:
    write(work/'active-moment.json',dict(binding=binding,group=label,index=i,completed_new=count_new,completed_reused=count_reused))
    L,U=local_matrices(F,loc.d[i],loc.V[i],a,vbasis,dbasis)
    vals=np.array([columns(L),columns(U),cross_columns(L,U)]);dc=columns(L+G)
    save_npz(file,binding=np.array(binding),group=np.array(label),index=np.array(i),moments=vals,coupled_C=dc)
    count_new+=1
   if vals.shape!=(3,P.n)or dc.shape!=(P.n,)or not np.isfinite(vals).all()or not np.isfinite(dc).all():raise ValueError('Invalid complete local moments')
   moments[i]=vals;coupled+=dc.astype(np.longdouble)
   if (i+1)%100==0:print(json.dumps(dict(event='Gram_T_complete_moments',group=label,completed=i+1,total=len(aa),new=count_new,reused=count_reused,seconds=time.perf_counter()-begin)),flush=True)
 an,bn,en=node[:,0],node[:,1],node[:,2];am,bm,em=mid[:,0],mid[:,1],mid[:,2]
 sn=np.zeros_like(an);sn[:-1]=np.cumsum(an[:0:-1],axis=0)[::-1]
 sm=np.zeros_like(am);sm[:-1]=np.cumsum(am[:0:-1],axis=0)[::-1]
 bb=columns(P.BB);dc=np.asarray(coupled,float)+columns(P.BA+P.BB)
 dd=T.h[:,None]**2*(sn[:-1]+sm+bb)+T.h[:,None]**2*am/4+1.5*T.h[:,None]*em+2.25*bm
 du=np.empty_like(an)
 for k in range(P.m):
  hp=T.h[k-1]if k else 0.;hn=T.h[k]if k<P.m-1 else 0.;ak=hp/2;om=T.omega[k]
  far=sn[k]+(sm[k]if k<P.m-1 else 0.)+bb
  value=ak*ak*an[k]+2*ak*en[k]+bn[k]+om*om*far
  if k:
   yy=hp/8;value+=yy*yy*am[k-1]+yy*em[k-1]+.25*bm[k-1]
  if k<P.m-1:
   yy=hp/2+3*hn/8;value+=yy*yy*am[k]+yy*em[k]+.25*bm[k]
  du[k]=value
 du[0]+=1. # The complete new U0-ez residual rows remain in the column norms.
 diag=np.r_[dc,du.ravel(),dd.ravel()]
 if not np.isfinite(diag).all()or np.min(diag)<=0:raise ValueError('All exact-formula diagonal entries must be positive; no floor is permitted')
 return diag,node,mid,G,dict(new=count_new,reused=count_reused,total=count_new+count_reused,seconds=time.perf_counter()-begin)

class CoreBoundary:
 """Joint old position BC and U0=ez, via one mask and a482-order Gram."""
 def __init__(self,P,T,S):
  self.P,self.T,self.S=P,T,np.asarray(S)
  if len(S)!=T.size or not np.isfinite(S).all()or np.min(S)<=0:raise ValueError('Bad positive scale')
  sc,su,sd=T.unpack(S);C=P.BA+P.BB
  tail=np.sum((T.omega[1:,None]*su[1:])**2,axis=0)+np.sum((T.h[:,None]*sd)**2,axis=0)
  G=(C*(sc*sc))@C.T+(P.BB*tail)@P.BB.T
  self.row_norm=np.sqrt(np.diag(G));self.normalized_gram=G/self.row_norm[:,None]/self.row_norm[None,:]
  self.factor=cho_factor(self.normalized_gram,lower=True,check_finite=True)
 def mask(self,z):
  z=np.asarray(z).reshape(-1).copy();z[self.P.n:2*self.P.n]=0.;return z
 def apply(self,z):return self.T.boundary(self.S*z)
 def transpose(self,w):return self.S*self.T.boundary_transpose(w)
 def normal_solve(self,w):return cho_solve(self.factor,w/self.row_norm,check_finite=True)/self.row_norm
 def project(self,z):
  z=self.mask(z);return z-self.mask(self.transpose(self.normal_solve(self.apply(z))))
 def lift(self,z):return self.T.lift(self.S*self.project(z))
 def pullback(self,g):return self.project(self.S*self.T.pullback(g))
 def affine(self,position_residual,velocity_residual):
  w=np.zeros(self.T.size);w[self.P.n:2*self.P.n]=-velocity_residual/self.S[self.P.n:2*self.P.n]
  w-=self.mask(self.transpose(self.normal_solve(position_residual+self.apply(w))))
  return self.T.lift(self.S*w)

def main(a):
 begin=time.perf_counter();source=sha(__file__)
 required={a.matrix_source:MATRIX_SHA,a.gram_source:GRAM_SHA,a.coordinate_source:COORDINATE_SHA}
 for f,s in required.items():
  if sha(f)!=s:raise ValueError('Frozen source changed: '+str(f))
 base=load(a.matrix_source,'gram_T_base');gm=load(a.gram_source,'gram_T_gram');coord=load(a.coordinate_source,'gram_T_coordinates')
 p,P,identities=base.initialize(a);identities.update({str(k):v for k,v in required.items()});identities[str(Path(__file__))]=source
 if (P.M,P.N,P.m,P.n,P.nl)!=(160,2048,602,482,325):raise ValueError('Original full model changed')
 for loc in (a.out,a.work):
  if a.topic.resolve()==loc.resolve()or a.topic.resolve()in loc.resolve().parents:raise ValueError('Raw results must stay outside the topic')
 a.work.mkdir(parents=True,exist_ok=True);a.out.parent.mkdir(parents=True,exist_ok=True)
 if a.out.exists()or a.out.with_suffix('.prepared.npz').exists():raise ValueError('This complete preparation already exists; consume it instead of recomputing')
 original_U0=P.U[0].copy();original_binary=p.binary_sha(P.Y,P.U)
 if np.any(P.Y[0,2*P.M+1:]):raise ValueError('Original literal core Z must remain zero')
 P.U=P.U.copy();P.U[0]=core_target(P);initial_binary=p.binary_sha(P.Y,P.U)
 initialization=dict(original_YU_sha256=original_binary,new_YU_sha256=initial_binary,old_U0_minus_ez_max=maximum(original_U0-core_target(P)),
  old_U0_minus_ez_nonzero=int(np.count_nonzero(original_U0-core_target(P))),new_U0_literal_ez=True,original_Y_unchanged=True,old_warm_file_modified=False,
  definition='Explicit new model initialization sets only the482 U0 slots to ez; all original Y and later U remain.')
 T=coord.IntegratedCoordinates(P);Aug=augmented_factory(gm.factory(base));J=Aug(P,P.Y,P.U);r=J.residual()
 if J.shape!=(1158250,580328):raise ValueError('A complete physical or boundary row was omitted')
 binding=hashlib.sha256((source+'\n'+initial_binary+'\n'+json.dumps(identities,sort_keys=True)).encode()).hexdigest()
 diag,nmom,mmom,G,account=complete_diagonal(P,T,J,a.work,binding);S=1/np.sqrt(diag)
 prepared=a.out.with_suffix('.prepared.npz');save_npz(prepared,scale=S,diagonal=diag,node_moments=nmom,midpoint_moments=mmom,density_matrix=G,
  Y=P.Y,U=P.U,initial_YU_sha256=np.array(initial_binary),binding=np.array(binding),source_sha256=np.array(source))
 print(json.dumps(dict(event='Gram_T_prepared_arrays',path=str(prepared),sha256=sha(prepared),moments=account)),flush=True)
 B=CoreBoundary(P,T,S);checks=[]
 selected=[1,P.M+3,2*P.M+6,P.n+3,P.n+529*P.n+P.M+7,P.n+601*P.n+2*P.M+9,(P.m+1)*P.n+5,(P.m+1)*P.n+573*P.n+P.M+11,(P.m+1)*P.n+600*P.n+2*P.M+13]
 for i in selected:
  z=np.zeros(T.size);z[i]=1.;col=J.matvec(T.lift(z));actual=float(base.inner(col,col));expected=float(diag[i])
  checks.append(dict(index=i,formula=expected,full_column_squared=actual,relative_difference=abs(actual-expected)/max(actual,expected)))
 # One full independent physical-jet derivative with a nonzero core-rho variation.
 nu=np.r_[P.q.freq,P.q.freq[1:],P.q.freq];idx=np.arange(P.n);phase=P.x[:,None]*(1+idx%7)[None,:]+.37*idx[None,:]
 dY=1e-4*np.cos(phase)/(1+nu[None,:]**2);dU=1e-4*np.sin(phase+.23)/(1+nu[None,:]);delta=np.r_[dY.ravel(),dU.ravel()]
 actual=J.matvec(delta);reference=np.r_[gm.independent_direction(P,J.F,dY,dU),dU[0]];diff=actual-reference
 # All new joint constraints, their affine RHS and the complete adjoint.
 idx=np.arange(T.size);z=1e-5*(np.sin(.173*idx)+.17*np.cos(.271*idx));pz=B.project(z);lift=B.lift(z)
 old_hom=P.BA@lift[:P.n]+P.BB@lift[(P.m-1)*P.n:P.m*P.n];new_hom=lift[P.m*P.n:(P.m+1)*P.n]
 d0=B.affine(r['boundary'],r['core_velocity']);old_aff=P.BA@d0[:P.n]+P.BB@d0[(P.m-1)*P.n:P.m*P.n]+r['boundary'];new_aff=d0[P.m*P.n:(P.m+1)*P.n]+r['core_velocity']
 w=np.sin(.019*np.arange(J.rows));forward=J.matvec(lift);backward=B.pullback(J.rmatvec(w));left=base.inner(forward,w);right=base.inner(z,backward)
 # DG-T2 is checked once against the full original Fourier coefficient rule.
 raw=np.zeros((P.M,3,P.N));raw[:,1]=-2*J.rho[None,:]*(1-P.q.freq[1:,None]**2)*np.cos(P.q.freq[1:,None]*P.q.angle[None,:])
 Gfft=J.F.project_constraints(raw).T;Gdiff=G[:,1:P.M+1]-Gfft
 p.assert_sources(identities)
 out=dict(scope=__doc__,source_sha256=source,identities=identities,initialization=initialization,original_warm_sha256=p.WARM_SHA,
  original_BC_sha256=p.binary_sha(P.BA,P.BB,P.target),M=P.M,N=P.N,nodes=P.m,shape=list(J.shape),original_position_rows=482,new_core_velocity_rows=482,
  initial_full_polynomial_Gram=summary(r,P.M),all_quadratic_Fourier_modes_retained=True,global_rho_chain_in_C_columns=True,
  prepared_path=str(prepared),prepared_sha256=sha(prepared),moment_account=account,
  diagonal_min=float(diag.min()),diagonal_max=float(diag.max()),scale_min=float(S.min()),scale_max=float(S.max()),
  full_column_checks=checks,density_matrix_full_Fourier_max_difference=maximum(Gdiff),density_matrix_relative_L2=float(np.linalg.norm(Gdiff)/np.linalg.norm(Gfft)),
  full_augmented_Jv_complex_step_max=maximum(diff),full_augmented_Jv_complex_step_relative_L2=float(np.linalg.norm(diff)/np.linalg.norm(reference)),
  normalized_joint_boundary_Gram_condition_2=float(np.linalg.cond(B.normalized_gram)),projected_old_BC_max=maximum(old_hom),projected_U0_max=maximum(new_hom),
  affine_old_BC_residual_max=maximum(old_aff),affine_U0_residual_max=maximum(new_aff),projection_idempotence_max=maximum(B.project(pz)-pz),
  full_projected_adjoint=dict(left=float(left),right=float(right),absolute=float(abs(left-right)),relative_to_inner_products=float(abs(left-right)/max(abs(left),abs(right),np.finfo(float).tiny))),
  seconds=time.perf_counter()-begin,maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,linear_solve_executed=False,nonlinear_solve_executed=False,
  accepted_parent=False,continuous_geometry_certified=False,old_T_Pr_budget_changed=False,
  arithmetic='Ordinary binary64 FFT and moment sums with long-double reductions. Exact-real formulas, no interval conditioning claim.',
  boundary_scope='U0 is literal ez by initialization/mask. Floating position-BC projection is audited, not claimed an exact support identity.',
  objective_scope='New full polynomial Gram objective, including all old BC and new U0 residual rows. Its raw SSE is not a Pr improvement claim.')
 write(a.out,out);print(json.dumps(dict(report=str(a.out),sha256=sha(a.out),**out)),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','gram-source','coordinate-source','work','out'):p.add_argument('--'+key,type=Path,required=True)
 main(p.parse_args())
