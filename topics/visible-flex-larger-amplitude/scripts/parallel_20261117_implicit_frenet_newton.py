#!/usr/bin/env python3
"""One fixed-602-node Newton budget for the full polynomial Frenet system.

Preparation is the default. --execute enables the separately authorized
finite attempt: 20 iterations, at most 8 fresh Jacobians, 17 Armijo trials.
All 482 Y and 482 U slots per node, all node/midpoint constraints, and the
original 325/157 separated boundary rows are retained. This new projected
polynomial system is not the original projected explicit positive-root RHS.
Its algebraic convergence never certifies physical acceptance or C2 geometry.
"""
import argparse,gzip,hashlib,importlib.util,json,math,resource,shutil,sys,tempfile,time,warnings
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import lu_factor,lu_solve,LinAlgWarning
from scipy.linalg.lapack import dgecon

WARM_SHA='1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057'
POLYNOMIAL_SHA='ba0b17fc85af8510c7c45b22a8facecd59061f53b3f7fd4adb48d3380c74e1a2'
QR_SHA='c76bde190ff67a9e148d230c8e5e7d7a7899324c055e67faac6679b8fba10e39'
FRENET_SHA='7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831'
HOLD_SHA='ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'
PROFILE_SHA='08b1894ca407a0c49b0de80427c669cafe702ab5878b1abf7b346994138d79b3'
INWARD_SHA='1816ba9f5c9d1c207ba5e502ed5fa37a2f28807c54067cde766ae313df40e3e0'
PR_TOL=1e-8
BC_TOL=1e-11
MAX_ITER=20
MAX_JAC=8
BACKTRACKS=17

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def binary_sha(*arrays):
 h=hashlib.sha256()
 for a in arrays:h.update(np.asarray(a,dtype='<f8',order='C').tobytes(order='C'))
 return h.hexdigest()
def load(p,name):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def emit(**values):print(json.dumps(values,allow_nan=False),flush=True)
def rss():return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
def maxabs(a):return float(np.max(np.abs(a)))
def assert_sources(identities):
 for path,expected in identities.items():
  if sha(path)!=expected:raise ValueError('Frozen problem/source changed: '+str(path))
def write_json(path,data):path.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')

class Problem:
 def __init__(self,d,fs,hp,polynomial):
  self.M,self.N,self.n,self.m,self.nl=160,2048,482,602,325
  if (d.get('M'),d.get('N'),d.get('left_count'),d.get('right_count'))!=(160,2048,325,157)or not d.get('preparation_only')or not d.get('prepared'):raise ValueError('Wrong original complete prepared warm')
  self.x=np.asarray(d['mesh'],dtype=float);self.Y=np.asarray(d['states'],dtype=float);self.U=np.asarray(d['full_ode_rhs_at_nodes'],dtype=float)
  if self.x.shape!=(self.m,)or not np.isfinite(self.x).all()or not(np.diff(self.x)>0).all()or self.x[0]!=0. or self.x[-1]!=1.03:raise ValueError('Fixed original 602-node mesh required')
  if any(a.shape!=(self.m,self.n)or not np.isfinite(a).all()for a in (self.Y,self.U)):raise ValueError('Bad full Y/U arrays')
  self.h=np.diff(self.x);self.mid=self.x[:-1]+self.h/2
  self.profile=hp.HoldProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'])
  if self.profile.spec()!=d['hold_scalar_profile']:raise ValueError('Different fixed scalar evaluator')
  self.q=fs.Frenet(self.M,self.N);self.operator=polynomial.PolynomialFrenet(self.q);self.fs=fs
  self.scalar_nodes=np.array([self.profile(float(s))for s in self.x]);self.scalar_mid=np.array([self.profile(float(s))for s in self.mid])
  if not np.isfinite(self.scalar_nodes).all()or not np.isfinite(self.scalar_mid).all()or min(self.scalar_nodes[:,0].min(),self.scalar_mid[:,0].min())<=0:raise ValueError('Bad fixed scalar samples')
  self.k=self.scalar_nodes[:,1]/self.scalar_nodes[:,0];self.km=self.scalar_mid[:,1]/self.scalar_mid[:,0]
  self.kprime=self.scalar_nodes[:,2]/self.scalar_nodes[:,0]-self.k*self.k
  self.BA=np.zeros((self.n,self.n));self.BB=np.zeros_like(self.BA);self.target=np.zeros(self.n)
  self.BA[0,0]=1.;self.target[0]=1.
  fixed=np.asarray(d['fixed_core_first_three'],dtype=float)
  if fixed.shape!=(3,)or not np.isfinite(fixed).all():raise ValueError('Wrong fixed core data')
  for j in range(3):self.BA[1+j,1+j]=1.;self.target[1+j]=fixed[j]
  for j in range(self.M):self.BA[4+j,1+j]=self.q.freq[j+1];self.BA[4+j,self.M+1+j]=1.
  self.BA[4+self.M:self.nl,2*self.M+1:]=np.eye(self.M+1)
  self.BB[self.nl:]=np.asarray(d['terminal_rows'],dtype=float);self.target[self.nl:]=np.asarray(d['terminal_target'],dtype=float)
  if not np.isfinite(self.BB).all()or not np.isfinite(self.target).all()or np.any(self.BA[self.nl:])or np.any(self.BB[:self.nl]):raise ValueError('Bad original separated boundary')
  self.metadata={k:d[k]for k in ('schema','source_sha256','parent_sha256','interface_sha256','fixed_scalar_profile','analytic_extension_origin','hold_scalar_profile','hold_profile_sha256','fixed_core_first_three','terminal_reference','warm_definition')}
  self.counts=dict(residual_evaluations=0,node_constraint_points=0,midpoint_constraint_points=0,fresh_jacobians=0,node_jacobian_points=0,midpoint_jacobian_points=0,terminal_jet_jacobian_points=0)
 def midpoint(self,Y,U):
  h=self.h[:,None]
  return (Y[:-1]+Y[1:])/2+h*(U[:-1]-U[1:])/8,1.5*(Y[1:]-Y[:-1])/h-.25*(U[:-1]+U[1:])
 def boundary(self,Y):return self.BA@Y[0]+self.BB@Y[-1]-self.target
 def residual(self,Y,U):
  self.counts['residual_evaluations']+=1;self.counts['node_constraint_points']+=self.m;self.counts['midpoint_constraint_points']+=self.m-1
  ym,um=self.midpoint(Y,U);nodes=np.empty_like(Y);middle=np.empty_like(ym)
  with np.errstate(over='ignore',invalid='ignore',divide='ignore'):
   for i in range(self.m):nodes[i]=self.operator.residual(Y[i],U[i],self.k[i])
   for i in range(self.m-1):middle[i]=self.operator.residual(ym[i],um[i],self.km[i])
   boundary=self.boundary(Y)
   cost=float(np.sum(nodes*nodes)+np.sum(middle*middle)+np.sum(boundary*boundary))
  finite=bool(np.isfinite(nodes).all()and np.isfinite(middle).all()and np.isfinite(boundary).all()and math.isfinite(cost))
  return dict(nodes=nodes,middle=middle,boundary=boundary,cost=cost,finite=finite)
 def summary(self,R):
  if not R['finite']:return dict(finite=False,raw_residual_square_sum=None)
  groups=(slice(0,self.M),slice(self.M,2*self.M+1),slice(2*self.M+1,None))
  return dict(finite=True,raw_residual_square_sum=R['cost'],all_residual_rms=math.sqrt(R['cost']/(2*self.m*self.n)),node_max=maxabs(R['nodes']),midpoint_max=maxabs(R['middle']),boundary_max=maxabs(R['boundary']),node_block_max=[maxabs(R['nodes'][:,g])for g in groups],midpoint_block_max=[maxabs(R['middle'][:,g])for g in groups])
 def converged(self,R):return bool(R['finite']and maxabs(R['nodes'])<=PR_TOL and maxabs(R['middle'])<=PR_TOL and maxabs(R['boundary'])<=BC_TOL)
 def physical_samples(self,Y,U):
  """Numerical audit only: all original nodes and actual cubic midpoints."""
  reader=self.fs.Frenet(self.M,8192);rho=1+np.cos(reader.angle[:,None]*reader.freq[None,1:])@((1-reader.freq[1:]**2)*Y[0,1:self.M+1])
  ym,um=self.midpoint(Y,U);limits={k:dict(value=float('inf'))for k in ('Q','W','H','positive_branch_normal_velocity')};metric=dict(value=0.);raw=np.zeros(3);omitted=np.zeros(3)
  for label,times,ys,us,ks,scalars in (('node',self.x,Y,U,self.k,self.scalar_nodes),('midpoint',self.mid,ym,um,self.km,self.scalar_mid)):
   for i,(s,y,u,k,scalar)in enumerate(zip(times,ys,us,ks,scalars)):
    _,d,e=reader.jet(y);V=reader.jet(u)[0];Q=np.sum(d*d,axis=1);C=np.cross(d,e);W=np.sum(C*C,axis=1);H=W-k*k*Q**3;branch=np.sum(C*V,axis=1)
    for name,value in zip(limits,(Q,W,H,branch)):
     j=int(np.argmin(value))
     if value[j]<limits[name]['value']:limits[name]=dict(value=float(value[j]),kind=label,index=i,s=float(s),angle=float(reader.angle[j]))
    point=np.c_[np.sum(V*d,axis=1),np.sum(V*e,axis=1)+k*Q,np.sum(V*V,axis=1)-1]
    if not all(np.isfinite(z).all()for z in (Q,W,H,branch,point)):return dict(finite=False,angles=8192,physical_solution_accepted=False,failure=dict(kind=label,index=i,reason='nonfinite physical quantities'))
    raw=np.maximum(raw,np.max(np.abs(point),axis=0));spectrum=np.fft.rfft(point,axis=0)/reader.N;f=2*np.arange(self.M+1,2*self.M+1)
    omitted=np.maximum(omitted,np.array([maxabs(-2*spectrum[f,0].imag),maxabs(2*spectrum[f,1].real),maxabs(2*spectrum[f,2].real)]))
    with np.errstate(over='ignore',divide='ignore',invalid='ignore'):
     er=point[:,2];fr=point[:,0]/(scalar[0]*rho);gr=Q/(scalar[0]*rho)**2-1
     op=(np.abs(er+gr)+np.sqrt((er-gr)**2+4*fr*fr))/2
    if not np.isfinite(op).all():return dict(finite=False,definition='Actual common cubic node/midpoint samples; no continuous certificate',angles=8192,rho_min=float(rho.min()),failure=dict(kind=label,index=i))
    j=int(np.argmax(op))
    if op[j]>metric['value']:metric=dict(value=float(op[j]),kind=label,index=i,s=float(s),angle=float(reader.angle[j]))
  return dict(finite=True,angles=8192,node_count=self.m,midpoint_count=self.m-1,rho_min=float(rho.min()),domain_minima=limits,raw_point_constraint_max_by_row=raw.tolist(),unretained_quadratic_coefficient_max_by_row=omitted.tolist(),unretained_mode_indices=[self.M+1,2*self.M],unretained_row_count=3*self.M,actual_common_cubic_Gram_max=metric,all_sampled_domain_and_branch_positive=bool(rho.min()>0 and all(z['value']>0 for z in limits.values())),continuous_metric_certified=False,physical_solution_accepted=False,definition='All original nodes and actual common-cubic midpoints, using the frozen ordinary scalar evaluator; whole-angle/whole-radius exact-g metric remains unpaid.')
 def terminal_common_jets(self,Y,U):
  """Define literal common second jets; do not reinterpret nonzero C as zero."""
  acceleration=[];rcond=[];linear_errors=[];conditions=[];missing=[]
  for i in range(self.m):
   try:
    fy,fv=self.operator.jacobians(Y[i],U[i],self.k[i]);self.counts['terminal_jet_jacobian_points']+=1
    with warnings.catch_warnings():
     warnings.simplefilter('error',LinAlgWarning);lu,piv=lu_factor(fv,check_finite=False)
    rc,info=dgecon(lu,float(np.linalg.norm(fv,1)),norm='1')
    if info or not math.isfinite(rc)or rc<=0:raise np.linalg.LinAlgError('Unpaid terminal C_U inverse')
    _,d,_=self.q.jet(Y[i]);ck_point=np.zeros((self.N,3));ck_point[:,1]=np.sum(d*d,axis=1);ck=self.operator.project(ck_point)
    rhs=-(fy@U[i]+ck*self.kprime[i]);a=lu_solve((lu,piv),rhs,check_finite=False)
    if not np.isfinite(a).all():raise np.linalg.LinAlgError('Nonfinite common acceleration')
    acceleration.append(a.tolist());rcond.append(float(rc));conditions.append(float(1/rc));linear_errors.append(maxabs(fv@a-rhs))
   except (RuntimeError,ValueError,LinAlgWarning,np.linalg.LinAlgError)as exc:
    acceleration.append(None);rcond.append(None);conditions.append(None);linear_errors.append(None);missing.append(dict(node=i,message=str(exc)))
  conversion=None
  if not missing:
   h=self.h[:,None];dy=Y[1:]-Y[:-1];ac0=6*dy/(h*h)-(4*U[:-1]+2*U[1:])/h;ac1=-6*dy/(h*h)+(2*U[:-1]+4*U[1:])/h
   aa=np.asarray(acceleration);delta_sum=np.sum(np.abs(aa[:-1]-ac0),axis=1)+np.sum(np.abs(aa[1:]-ac1),axis=1)
   conversion=dict(cubic_to_quintic_velocity_l1_bound_by_cell=(2*self.h*delta_sum/9).tolist(),cubic_to_quintic_position_l1_bound_by_cell=(54*self.h*self.h*delta_sum/3125).tolist(),ordinary_floating_evaluation=True,interval_certified=False,definition='R227 h2 endpoint-acceleration correction; this does not replace an actual whole-quintic Gram readout.')
  return dict(common_accelerations=acceleration,cubic_to_quintic_diagnostic=conversion,C_U_reciprocal_condition_estimate_1norm=rcond,C_U_condition_estimate_1norm=conditions,acceleration_linear_residual_max_by_node=linear_errors,missing_acceleration_nodes=missing,definition='a_i=-C_U^{-1}(C_Y U_i+C_k kprime_i). For nonzero c_i=C(Y_i,U_i;k_i), this is a tangent acceleration to the local level set C=c_i, not a derivative along C=0. These literal doubles can define a NEW common C2 quintic; its interior derivatives must be read from that quintic, not the solver cubic.')

class CondensedFactor:
 def __init__(self,P,Y,U,qr_module,work,jac_number):
  self.P=P;self.root=Path(tempfile.mkdtemp(prefix='implicit-602-',dir=work));self.nodes=self.root/'nodes';self.middle=self.root/'middle';self.nodes.mkdir();self.middle.mkdir();self.qr=None;self.jac_number=jac_number
  self.state_sha256=binary_sha(Y,U);begin=time.perf_counter();self.rcond=[]
  n=P.n;m=P.m
  try:
   for i in range(m):
    fy,fv=P.operator.jacobians(Y[i],U[i],P.k[i]);P.counts['node_jacobian_points']+=1
    if not np.isfinite(fy).all()or not np.isfinite(fv).all():raise np.linalg.LinAlgError('Nonfinite full node Jacobian')
    with warnings.catch_warnings():
     warnings.simplefilter('error',LinAlgWarning);lu,piv=lu_factor(fv,check_finite=False)
    rc,info=dgecon(lu,float(np.linalg.norm(fv,1)),norm='1')
    if info or not math.isfinite(rc)or rc<=0:raise np.linalg.LinAlgError('Singular node C_U in complete elimination')
    A=-lu_solve((lu,piv),fy,check_finite=False)
    if not np.isfinite(A).all():raise np.linalg.LinAlgError('Nonfinite full node elimination')
    np.savez(self.nodes/f'{i:04d}.npz',A=A,LU=lu,piv=piv,Fy=fy,Fv=fv)
    self.rcond.append(float(rc))
    if i%32==31 or i==m-1:emit(event='implicit_node_elimination',fresh_jacobian=jac_number,completed=i+1,total=m,minimum_rcond1=min(self.rcond),maximum_RSS_kib=rss())
   ym,um=P.midpoint(Y,U);self.qr=qr_module.DiskQRFactor(n,m,P.BA,P.BB,P.nl,self.root,verify_residual=True)
   with np.load(self.nodes/'0000.npz')as z:A0=z['A']
   for i in range(m-1):
    fy,fv=P.operator.jacobians(ym[i],um[i],P.km[i]);P.counts['midpoint_jacobian_points']+=1
    with np.load(self.nodes/f'{i+1:04d}.npz')as z:A1=z['A']
    h=P.h[i]
    # Complete condensed blocks, algebraically the probe's unexpanded form.
    left=.5*fy-1.5*fv/h+(h*fy/8-.25*fv)@A0
    right=.5*fy+1.5*fv/h+(-h*fy/8-.25*fv)@A1
    if not all(np.isfinite(z).all()for z in (fy,fv,left,right)):raise np.linalg.LinAlgError('Nonfinite complete midpoint block')
    np.savez(self.middle/f'{i:04d}.npz',Fy=fy,Fv=fv)
    self.qr.append(i,left,right);A0=A1
    if i%32==31 or i==m-2:emit(event='implicit_midpoint_condensation',fresh_jacobian=jac_number,completed=i+1,total=m-1,maximum_RSS_kib=rss())
   self.qr.finish();emit(event='implicit_complete_factor',fresh_jacobian=jac_number,nodes=m,node_rows=m*n,midpoint_rows=(m-1)*n,boundary_rows=n,state_sha256=self.state_sha256,minimum_node_rcond1=min(self.rcond),seconds=time.perf_counter()-begin,maximum_RSS_kib=rss())
  except Exception:
   self.close();raise
 def solve(self,R):
  """Solve J delta=-R, recomputing every b_i for this current residual."""
  P=self.P;n=P.n;m=P.m;b=np.empty((m,n))
  for i in range(m):
   with np.load(self.nodes/f'{i:04d}.npz')as z:b[i]=-lu_solve((z['LU'],z['piv']),R['nodes'][i],check_finite=False)
  rhs=np.empty((m-1,n))
  for i in range(m-1):
   with np.load(self.middle/f'{i:04d}.npz')as z:
    rhs[i]=-R['middle'][i]-z['Fy']@(P.h[i]*(b[i]-b[i+1])/8)+z['Fv']@(.25*(b[i]+b[i+1]))
  dy=self.qr.solve(np.r_[rhs.ravel(),-R['boundary']]).reshape((m,n));du=np.empty_like(dy);node_error=0.;mid_error=0.
  for i in range(m):
   with np.load(self.nodes/f'{i:04d}.npz')as z:
    du[i]=b[i]+z['A']@dy[i]
    error=R['nodes'][i]+z['Fy']@dy[i]+z['Fv']@du[i]
    if not np.isfinite(error).all():raise np.linalg.LinAlgError('Nonfinite complete node linear residual')
    node_error=max(node_error,maxabs(error))
  for i in range(m-1):
   dym=(dy[i]+dy[i+1])/2+P.h[i]*(du[i]-du[i+1])/8
   dum=1.5*(dy[i+1]-dy[i])/P.h[i]-.25*(du[i]+du[i+1])
   with np.load(self.middle/f'{i:04d}.npz')as z:error=R['middle'][i]+z['Fy']@dym+z['Fv']@dum
   if not np.isfinite(error).all():raise np.linalg.LinAlgError('Nonfinite complete midpoint linear residual')
   mid_error=max(mid_error,maxabs(error))
  bc_error=maxabs(R['boundary']+P.BA@dy[0]+P.BB@dy[-1]);scale=max(maxabs(R['nodes']),maxabs(R['middle']),maxabs(R['boundary']))
  detail=dict(node_linear_residual_max=node_error,midpoint_linear_residual_max=mid_error,boundary_linear_residual_max=bc_error,full_linear_relative_residual=max(node_error,mid_error,bc_error)/max(scale,np.finfo(float).tiny),delta_Y_max=maxabs(dy),delta_U_max=maxabs(du),factor_state_sha256=self.state_sha256)
  if not np.isfinite(dy).all()or not np.isfinite(du).all()or not all(math.isfinite(v)for k,v in detail.items()if k!='factor_state_sha256'):raise np.linalg.LinAlgError('Nonfinite complete reconstructed Newton step')
  emit(event='implicit_full_linear_solve',fresh_jacobian=self.jac_number,**detail)
  return dy,du,detail
 def close(self):
  if getattr(self,'qr',None)is not None:self.qr.close();self.qr=None
  if getattr(self,'root',None)is not None:shutil.rmtree(self.root,ignore_errors=True);self.root=None
 def __del__(self):self.close()

def storage_budget(P):
 n,m,k=P.n,P.m,P.n-P.nl
 node=4*m*n*n*8;middle=2*(m-1)*n*n*8;diskqr=4*(m-1)*n*n*8
 return dict(unknowns=2*m*n,node_constraints=m*n,midpoint_constraints=(m-1)*n,boundary_constraints=n,condensed_unknowns=m*n,
  QR_U_bytes=m*n*k*8,QR_transport_bytes=(m-1)*k*k*8,state_YU_bytes=2*m*n*8,node_A_LU_Fy_Fv_bytes=node,midpoint_Fy_Fv_bytes=middle,QR_L_R_LU_T_bytes=diskqr,
  dominant_cache_bytes=node+middle+diskqr,preflight_free_bytes_required=int((node+middle+diskqr)*1.15)+1024**3,
  explanation='Disk estimate excludes small pivots/ZIP headers. RAM dominant arrays are original DiskQR U and transport (~483 MB decimal), plus live blocks/FFT work/state. Only one fresh factor is retained; old own temporary caches are closed before rebuilding. This is an array-count estimate, not a measured execution RSS.')

def checkpoint(path,P,Y,U,R,history,source_sha,identities):
 record=dict(schema='independent-YU-polynomial-Frenet-checkpoint-v1',accepted_parent=False,original_explicit_BVP_accepted=False,source_sha256=source_sha,identities=identities,M=P.M,N=P.N,mesh=P.x.tolist(),states=Y.tolist(),independent_velocities=U.tolist(),residual_summary=P.summary(R),history=history)
 path.write_bytes(gzip.compress((json.dumps(record,allow_nan=False)+'\n').encode(),mtime=0))

def run(P,qr,work,out,source_sha,identities,initial):
 Y=P.Y.copy();U=P.U.copy();R=initial;factor=None;fresh=True;njev=0;history=[];reason='iteration_budget';failure=None
 try:
  for iteration in range(MAX_ITER):
   if P.converged(R):reason='finite_polynomial_tolerances_met';break
   if not R['finite']:reason='nonfinite_current_polynomial_residual';break
   if fresh:
    if njev>=MAX_JAC:reason='fresh_jacobian_budget';break
    if factor is not None:factor.close();factor=None
    assert_sources(identities);njev+=1;P.counts['fresh_jacobians']=njev
    checkpoint(out.with_suffix('.checkpoint.json.gz'),P,Y,U,R,history,source_sha,identities)
    factor=CondensedFactor(P,Y,U,qr,work,njev)
   dy,du,linear=factor.solve(R);accepted=False
   for trial in range(BACKTRACKS):
    alpha=2.**(-trial);yn=Y+alpha*dy;un=U+alpha*du;rn=P.residual(yn,un)
    accepted=bool(rn['finite']and (rn['cost']<(1-.4*alpha)*R['cost']or rn['cost']==R['cost']==0.))
    emit(event='implicit_armijo_trial',iteration=iteration,fresh_jacobian=njev,factor_fresh=fresh,trial=trial,alpha=alpha,accepted=accepted,**P.summary(rn))
    if accepted:break
   record=dict(iteration=iteration,fresh_jacobian=njev,factor_fresh=fresh,accepted=accepted,trials=trial+1,alpha=alpha if accepted else None,linear=linear,residual_before=P.summary(R),residual_after=P.summary(rn))
   history.append(record)
   if not accepted:
    if not fresh:
     if njev<MAX_JAC:fresh=True;emit(event='implicit_stale_factor_refresh_same_iterate',iteration=iteration);continue
     reason='stale_factor_no_descent_fresh_budget_exhausted';break
    reason='fresh_factor_no_descending_trial_old_iterate_retained';break
   Y,U,R=yn,un,rn;checkpoint(out.with_suffix('.checkpoint.json.gz'),P,Y,U,R,history,source_sha,identities)
   if P.converged(R):reason='finite_polynomial_tolerances_met';break
   # Eight fresh factors do not forbid further full-step reuse.
   # Stop only if the next iteration actually requests a ninth fresh J.
   fresh=alpha!=1.
 except Exception as exc:
  reason='finite_attempt_exception_old_iterate_retained';failure=dict(type=type(exc).__name__,message=str(exc))
 finally:
  if factor is not None:factor.close()
 return Y,U,R,history,reason,failure

def main(a):
 started=time.perf_counter();source_sha=sha(__file__);scripts=a.topic/'scripts';sys.path.insert(0,str(scripts))
 identities={str(a.warm):WARM_SHA,str(a.implicit_source):POLYNOMIAL_SHA,str(a.qr_source):QR_SHA,str(a.hold_source):HOLD_SHA,str(scripts/'parallel_20261117_frenet_symbol.py'):FRENET_SHA,str(scripts/'parallel_20261117_profile.py'):PROFILE_SHA,str(scripts/'parallel_20261117_inward_profile.py'):INWARD_SHA,str(Path(__file__)):source_sha}
 assert_sources(identities)
 fs=load(scripts/'parallel_20261117_frenet_symbol.py','independent_YU_fs');hp=load(a.hold_source,'independent_YU_hold');poly=load(a.implicit_source,'independent_YU_polynomial');qr=load(a.qr_source,'independent_YU_original_diskqr')
 raw=json.loads(gzip.decompress(a.warm.read_bytes()));P=Problem(raw,fs,hp,poly);del raw
 budget=storage_budget(P);initial=P.residual(P.Y,P.U)
 if not initial['finite']:raise ValueError('Original complete polynomial initial residual is nonfinite')
 a.out.parent.mkdir(parents=True,exist_ok=True);a.work.mkdir(parents=True,exist_ok=True)
 if a.topic.resolve()in a.work.resolve().parents or a.work.resolve()==a.topic.resolve():raise ValueError('Regenerable linear caches must remain outside the topic repository')
 preparation=dict(schema='independent-YU-polynomial-Frenet-preparation-v1',scope=__doc__,source_sha256=source_sha,identities=identities,mode='execute'if a.execute else'preparation_only',M=P.M,N=P.N,nodes=P.m,start=float(P.x[0]),end=float(P.x[-1]),left_count=325,right_count=157,mesh_sha256=binary_sha(P.x),initial_YU_sha256=binary_sha(P.Y,P.U),boundary_arrays_sha256=binary_sha(P.BA,P.BB,P.target),scalar_nodes_sha256=binary_sha(P.scalar_nodes),scalar_midpoints_sha256=binary_sha(P.scalar_mid),budget=budget,free_scratch_bytes=shutil.disk_usage(a.work).free,policy=dict(Pr_tol=PR_TOL,bc_tol=BC_TOL,max_iterations=MAX_ITER,max_fresh_jacobians=MAX_JAC,backtracking_trials=BACKTRACKS,alphas=[2.**(-j)for j in range(BACKTRACKS)],armijo_coefficient=.4,merit='sum of squares of EVERY node, midpoint and boundary raw scalar residual',H_guard_in_algebraic_line_search=False,fixed_original_mesh=True),initial_residual=P.summary(initial),initial_actual_cubic_audit=P.physical_samples(P.Y,P.U),counts=dict(P.counts),numpy_version=np.__version__,scipy_version=scipy.__version__,maximum_RSS_kib=rss(),seconds=time.perf_counter()-started,full_Newton_executed=False,original_explicit_BVP_accepted=False,continuous_geometry_certified=False)
 assert_sources(identities);write_json(a.out,preparation);emit(event='complete_implicit_preparation',report=str(a.out),sha256=sha(a.out),**preparation['initial_residual'],maximum_RSS_kib=rss(),seconds=preparation['seconds'])
 if not a.execute:return
 if shutil.disk_usage(a.work).free<budget['preflight_free_bytes_required']:raise RuntimeError('Insufficient scratch for the fixed complete cached factor')
 Y,U,R,history,reason,failure=run(P,qr,a.work,a.out,source_sha,identities,initial)
 physical=P.physical_samples(Y,U);jets=P.terminal_common_jets(Y,U);assert_sources(identities)
 result=dict(schema='independent-YU-polynomial-Frenet-finite-attempt-v1',scope=__doc__,source_sha256=source_sha,identities=identities,M=P.M,N=P.N,dimension_Y=P.n,dimension_U=P.n,nodes=P.m,mesh=P.x.tolist(),states=Y.tolist(),independent_velocities=U.tolist(),nodes_raw_constraints=R['nodes'].tolist(),midpoint_raw_constraints=R['middle'].tolist(),boundary_residual=R['boundary'].tolist(),residual_summary=P.summary(R),finite_algebraic_converged=P.converged(R),termination=reason,failure=failure,original_explicit_BVP_accepted=False,accepted_parent=False,full_Newton_executed=True,policy=preparation['policy'],unchanged_boundary=dict(left_count=P.nl,right_count=P.n-P.nl,rows=P.BB[P.nl:].tolist(),target=P.target[P.nl:].tolist(),arrays_sha256=binary_sha(P.BA,P.BB,P.target)),
  fixed_scalar_profile=P.metadata['fixed_scalar_profile'],analytic_extension_origin=P.metadata['analytic_extension_origin'],hold_scalar_profile=P.metadata['hold_scalar_profile'],hold_profile_sha256=HOLD_SHA,scalar_nodes=dict(a=P.scalar_nodes[:,0].tolist(),ap=P.scalar_nodes[:,1].tolist(),app=P.scalar_nodes[:,2].tolist(),k=P.k.tolist(),k_prime=P.kprime.tolist()),core=dict(coefficients=Y[0,1:P.M+1].tolist(),fixed_first_three=P.metadata['fixed_core_first_three'],axis_support_gap=float(2*np.sum(Y[0,1:P.M+1:2]))),history=history,physical_sample_audit=physical,counts=P.counts,common_accelerations=jets['common_accelerations'],common_jet_readout={k:v for k,v in jets.items()if k!='common_accelerations'},continuous_geometry_certified=False,cubic_solver_field_regularity='C1 and piecewise cubic; no automatic C2 assertion',old_cut_jets_not_fabricated=True,seconds=time.perf_counter()-started,maximum_RSS_kib=rss())
 field=a.out.with_suffix('.field.json.gz');field.write_bytes(gzip.compress((json.dumps(result,allow_nan=False)+'\n').encode(),mtime=0))
 report={k:v for k,v in result.items()if k not in ('mesh','states','independent_velocities','nodes_raw_constraints','midpoint_raw_constraints','boundary_residual','fixed_scalar_profile','scalar_nodes','unchanged_boundary','common_accelerations','common_jet_readout','core')}
 report.update(field_path=str(field),field_sha256=sha(field),common_jet_readout_summary=dict(missing_acceleration_nodes=jets['missing_acceleration_nodes'],max_condition_estimate_1norm=max((v for v in jets['C_U_condition_estimate_1norm']if v is not None),default=None),max_linear_residual=max((v for v in jets['acceleration_linear_residual_max_by_node']if v is not None),default=None)),core={k:v for k,v in result['core'].items()if k!='coefficients'})
 write_json(a.out,report);emit(event='complete_implicit_finite_terminal',report=str(a.out),sha256=sha(a.out),termination=reason,finite_algebraic_converged=P.converged(R),**P.summary(R),seconds=report['seconds'])

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','warm','implicit-source','qr-source','hold-source','out','work'):parser.add_argument('--'+key,type=Path,required=True)
 parser.add_argument('--execute',action='store_true',help='Run the separately authorized single fixed-mesh 17/8J/20-step budget; default is preparation only.')
 main(parser.parse_args())
