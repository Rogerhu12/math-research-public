#!/usr/bin/env python3
"""One frozen full-Pr LM direction from the original 1662 warm, not a BVP.

All 580328 residual rows remain. Build the complete J column norms once,
including four actual Hermite blocks and BC, then solve ONE equality-feasible
scaled damped least-squares problem: damp=1, maxiter=128. No damping scan,
nonlinear iteration, changed g, trial-state parent, or accepted geometry.
"""
import argparse,hashlib,importlib.util,inspect,json,math,resource,sys,time
from fractions import Fraction
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import solve_triangular
from scipy.sparse.linalg import LinearOperator,lsmr

MATRIX_SHA='ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4'
RAY_SHA='e67f7d1bf021fd88646e1a77057b4557418ff77ebd5032461d8a46dd7f6498fc'
DAMP=1.;MAXITER=128;ATOL=1e-8;BTOL=1e-8;CONLIM=1e6
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def emit(**k):print(json.dumps(k,allow_nan=False),flush=True)
def maximum(x):return float(np.max(np.abs(x)))
def norm(x):return float(np.linalg.norm(x))
def sqcols(x):return np.sum(x*x,axis=0)
def write(p,d):p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')

def column_diagonal(P):
 """Actual full J^T J diagonal; no dropped cross terms or global assembly."""
 t=time.perf_counter();a=np.zeros_like(P.Y);b=np.zeros_like(P.U)
 for i in range(P.m):
  cy,cu=P.operator.jacobians(P.Y[i],P.U[i],P.k[i]);a[i]+=sqcols(cy);b[i]+=sqcols(cu)
  if i%64==63 or i==P.m-1:emit(event='LM_node_column_norms',completed=i+1,total=P.m,seconds=time.perf_counter()-t)
 ym,um=P.midpoint(P.Y,P.U)
 for i,h in enumerate(P.h):
  cy,cu=P.operator.jacobians(ym[i],um[i],P.km[i])
  a[i]+=sqcols(.5*cy-1.5*cu/h);a[i+1]+=sqcols(.5*cy+1.5*cu/h)
  b[i]+=sqcols(h*cy/8-.25*cu);b[i+1]+=sqcols(-h*cy/8-.25*cu)
  if i%64==63 or i==P.m-2:emit(event='LM_midpoint_column_norms',completed=i+1,total=P.m-1,seconds=time.perf_counter()-t)
 a[0]+=sqcols(P.BA);a[-1]+=sqcols(P.BB)
 d=np.r_[a.ravel(),b.ravel()]
 if not np.isfinite(d).all()or np.min(d)<=0:raise ValueError('Every full column norm must be finite and positive; no arbitrary floor is permitted')
 return d,time.perf_counter()-t

def exact_right_row_rank(B):
 """Integer proof ||BB^T-I||_infinity < 1 for literal binary64 B."""
 ratios=[float(x).as_integer_ratio()for x in B.ravel()];exponent=max(q.bit_length()-1 for p,q in ratios)
 integers=np.array([p<<(exponent-(q.bit_length()-1))for p,q in ratios],dtype=object).reshape(B.shape)
 gram=integers@integers.T;denominator=1<<(2*exponent)
 for i in range(len(B)):gram[i,i]-=denominator
 error=max(sum(abs(v)for v in row)for row in gram)
 if not error<denominator:raise ValueError('Exact original BB row-rank certificate failed')
 return dict(rows=len(B),binary_denominator_exponent=exponent,Gram_error_infinity_numerator=str(error),
  Gram_error_infinity_denominator_exponent=2*exponent,
  strict_upper_float=math.nextafter(float(Fraction(error,denominator)),math.inf),
  exact_integer_less_than_one=True,method='Common power-of-two integer scaling, object-integer products/sums; no floating Gram in this rank proof.')

class BoundaryCoordinates:
 """D=d0+S Pi z; Pi is the SAME scaled-coordinate endpoint projector."""
 def __init__(self,P,S,bc):
  self.P,self.S=P,S;self.q=[];self.indices=[];self.audit=[];v0=np.zeros(len(S))
  n=P.n;count=P.m*n
  for name,B,index,r in (('left',P.BA[:P.nl],slice(0,n),bc[:P.nl]),
                         ('right',P.BB[P.nl:],slice(count-n,count),bc[P.nl:])):
   scale=S[index];C=B*scale[None,:];row_norm=np.linalg.norm(C,axis=1)
   if not np.isfinite(row_norm).all()or np.min(row_norm)<=0:raise ValueError('Bad scaled boundary rows')
   Cn=C/row_norm[:,None];Q,R=np.linalg.qr(Cn.T,mode='reduced')
   if not np.isfinite(R).all()or np.min(np.abs(np.diag(R)))<=0:raise ValueError('Bad complete boundary QR')
   coeff=solve_triangular(R.T,-r/row_norm,lower=True,check_finite=True);v0[index]=Q@coeff
   self.q.append(Q);self.indices.append(index)
   singular=np.linalg.svd(Cn,compute_uv=False)
   self.audit.append(dict(end=name,rows=len(B),row_normalized_scaled_sigma_min=float(singular[-1]),
    row_normalized_scaled_sigma_max=float(singular[0]),row_normalized_scaled_condition=float(singular[0]/singular[-1]),
    computed_Q_orthogonality_max=maximum(Q.T@Q-np.eye(len(B))),
    scaled_C_projector_defect_max=maximum(C-(C@Q)@Q.T)))
  self.d0=S*v0
 def project(self,z):
  z=np.asarray(z).reshape(-1).copy()
  for Q,index in zip(self.q,self.indices):z[index]-=Q@(Q.T@z[index])
  return z
 def lift(self,z):return self.S*self.project(z)
 def pullback(self,z):return self.project(self.S*z)

def main(a):
 begin=time.perf_counter()
 if sha(a.matrix_source)!=MATRIX_SHA or sha(a.ray_source)!=RAY_SHA:raise ValueError('Frozen matrix/ray source changed')
 mf=load(a.matrix_source,'lm_complete_matrix');ray=load(a.ray_source,'lm_complete_ray');p,P,identities=mf.initialize(a)
 identities.update({str(a.matrix_source):MATRIX_SHA,str(a.ray_source):RAY_SHA,str(Path(__file__)):sha(__file__)})
 lsmr_source=Path(inspect.getsourcefile(lsmr));identities[str(lsmr_source)]=sha(lsmr_source);p.assert_sources(identities)
 r=P.residual(P.Y,P.U);raw=mf.flatten(r);diag,diag_seconds=column_diagonal(P);S=1/np.sqrt(diag)
 rank=exact_right_row_rank(P.BB[P.nl:]);bc=BoundaryCoordinates(P,S,r['boundary'])
 n=P.m*P.n;d0y=bc.d0[:n].reshape(P.m,P.n)
 bc0=r['boundary']+P.BA@d0y[0]+P.BB@d0y[-1]
 J=mf.CompleteLinear(P,P.Y,P.U);b=-(raw+J.matvec(bc.d0));phase='preparation'
 def mv(z):
  out=J.matvec(bc.lift(z))
  if phase=='LSMR'and J.matvec_count%16==0:emit(event='LM_linear_progress',matvecs=J.matvec_count,rmatvecs=J.rmatvec_count,seconds=time.perf_counter()-begin)
  return out
 def rmv(w):return bc.pullback(J.rmatvec(w))
 A=LinearOperator(J.shape,matvec=mv,rmatvec=rmv,dtype=float)
 idx=np.arange(J.shape[0]);ztest=np.sin(.731*idx);wtest=np.cos(.217*idx)+.13*np.sin(.319*idx)
 f=A.matvec(ztest);g=A.rmatvec(wtest);left=mf.inner(f,wtest);right=mf.inner(ztest,g)
 relative=float(abs(left-right)/(norm(f)*norm(wtest)+norm(ztest)*norm(g)))
 if not math.isfinite(relative)or relative>1e-10:raise ValueError('New scaled/projected full-adjoint check failed')
 arrays=a.out.with_suffix('.prepared.npz')
 np.savez_compressed(arrays,diagonal=diag,scale=S,d0=bc.d0,Q_left=bc.q[0],Q_right=bc.q[1])
 preparation=dict(schema='complete-Pr-one-LM-direction-preparation-v1',scope=__doc__,identities=identities,
  M=P.M,N=P.N,nodes=P.m,unknowns=J.shape[1],residual_rows=J.shape[0],node_rows=P.m*P.n,
  midpoint_rows=(P.m-1)*P.n,boundary_rows=P.n,left_count=P.nl,right_count=P.n-P.nl,
  original_base_YU_sha256=p.binary_sha(P.Y,P.U),mesh_scalar_boundary_sha256=p.binary_sha(P.x,P.k,P.km,P.BA,P.BB,P.target),
  initial_residual=P.summary(r),prepared_arrays_path=str(arrays),prepared_arrays_sha256=sha(arrays),
  diagonal_sha256=p.binary_sha(diag),diagonal_min=float(diag.min()),diagonal_max=float(diag.max()),
  scale_min=float(S.min()),scale_max=float(S.max()),column_diagonal_seconds=diag_seconds,
  column_diagonal_definition='Node CY/CU squares plus all four formed midpoint blocks .5CY+-1.5CU/h, +-hCY/8-.25CU, plus complete original BA/BB; form blocks BEFORE squares.',
  exact_right_boundary_rank=rank,left_boundary_rank='Exact unit triangular pivots: fixed R0/first3 R, all T in support equations, all Z; rank325.',
  numerical_boundary_projectors=bc.audit,affine_direction_max=maximum(bc.d0),affine_remaining_original_BC_max=maximum(bc0),
  scaled_projected_adjoint=dict(left=float(left),right=float(right),relative_to_norm_products=relative),
  policy=dict(damp=DAMP,maxiter=MAXITER,atol=ATOL,btol=BTOL,conlim=CONLIM,
   linear_objective='||r+J*d0+J*S*Pi*z||_2^2 + damp^2||z||_2^2',
   raw_residual_row_weights_changed=False,frozen_g=True,full_direction_D='d0+S*Pi*z',
   one_linear_solve_only=True,nonlinear_iteration_count=0,actual_ray_alphas=[1.,.5,.25]),
  prepared=True,linear_solve_executed=False,nonlinear_solve_executed=False,accepted_parent=False,
  numpy_version=np.__version__,scipy_version=scipy.__version__,seconds=time.perf_counter()-begin,
  maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 p.assert_sources(identities);write(a.out.with_suffix('.preparation.json'),preparation)
 emit(event='LM_preparation_frozen',file=str(a.out.with_suffix('.preparation.json')),sha256=sha(a.out.with_suffix('.preparation.json')),
  exact_BB_Gram_upper=rank['strict_upper_float'],column_diagonal_seconds=diag_seconds,scaled_adjoint_error=relative,
  affine_BC_max=maximum(bc0),maximum_RSS_kib=preparation['maximum_RSS_kib'])
 if not a.execute_direction:return
 phase='LSMR';start_counts=(J.matvec_count,J.rmatvec_count);solve_start=time.perf_counter()
 result=lsmr(A,b,damp=DAMP,atol=ATOL,btol=BTOL,conlim=CONLIM,maxiter=MAXITER,show=False)
 solve_seconds=time.perf_counter()-solve_start;solve_end_counts=(J.matvec_count,J.rmatvec_count);phase='audit';z=result[0]
 if not np.isfinite(z).all():raise FloatingPointError('Nonfinite one-budget LSMR output')
 delta=bc.d0+bc.lift(z);dY=delta[:n].reshape(P.m,P.n);dU=delta[n:].reshape(P.m,P.n)
 current_j=J.matvec(delta);linear=raw+current_j;scaled_residual=A.matvec(z)-b
 normal=A.rmatvec(scaled_residual)+DAMP**2*z
 new_bc=r['boundary']+P.BA@dY[0]+P.BB@dY[-1]
 direction_path=a.out.with_suffix('.direction.npz');np.savez_compressed(direction_path,Y=P.Y,U=P.U,dY=dY,dU=dU,z=z)
 ray_report=ray.analyze(P,P.Y,P.U,dY,dU,alphas=(1.,.5,.25))
 ray_path=a.out.with_suffix('.ray.json');write(ray_path,ray_report)
 normal_denominator=max(norm(A.rmatvec(b)),np.finfo(float).tiny)
 output=dict(preparation=preparation,linear_solve_executed=True,nonlinear_solve_executed=False,
  solve_seconds=solve_seconds,lsmr_return=dict(istop=int(result[1]),iterations=int(result[2]),normr=float(result[3]),normar=float(result[4]),
   norma=float(result[5]),conda=float(result[6]),normx=float(result[7])),
  complete_matrix_action_counts=dict(before_LSMR=list(start_counts),after_LSMR=list(solve_end_counts),after_audit=[J.matvec_count,J.rmatvec_count]),
  actual_linear_residual_L2=norm(linear),actual_linear_residual_max=maximum(linear),
  actual_linear_model_SSE=float(mf.inner(linear,linear)),regularization_penalty=float(DAMP**2*mf.inner(z,z)),
  full_regularized_objective=float(mf.inner(linear,linear)+DAMP**2*mf.inner(z,z)),
  explicit_regularized_normal_residual_L2=norm(normal),
  explicit_regularized_normal_residual_relative=norm(normal)/normal_denominator,
  scaled_model_vs_original_linear_max=maximum(scaled_residual-linear),actual_remaining_original_BC_max=maximum(new_bc),
  delta_Y_max=maximum(dY),delta_U_max=maximum(dU),direction_path=str(direction_path),direction_file_sha256=sha(direction_path),
  ray_report_path=str(ray_path),ray_report_sha256=sha(ray_path),actual_ray=ray_report['direct_vector_checks'],
  direction_is_exact_Newton=False,accepted_parent=False,physical_solution_certified=False,
  source_sha256=sha(__file__),seconds=time.perf_counter()-begin,maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 p.assert_sources(identities);write(a.out,output)
 emit(event='LM_one_direction_complete',file=str(a.out),sha256=sha(a.out),lsmr=output['lsmr_return'],
  normal_relative=output['explicit_regularized_normal_residual_relative'],BC_max=output['actual_remaining_original_BC_max'],
  linear_SSE=output['actual_linear_model_SSE'],solve_seconds=solve_seconds,total_seconds=output['seconds'],
  maximum_RSS_kib=output['maximum_RSS_kib'],actual_ray=output['actual_ray'])

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','ray-source','out'):a.add_argument('--'+key,type=Path,required=True)
 a.add_argument('--execute-direction',action='store_true');main(a.parse_args())
