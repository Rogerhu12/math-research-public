#!/usr/bin/env python3
"""One full-spectrum Gram direction after the completed85c T preparation.

All1158250 rows, original1662, exact U0=ez mask, same fixed g and original
position BC. One damp1/max256 LSMR and exactly one alpha1 actual trial.
Prepared70c moments are reused. No nonlinear loop or follow-up alpha scan.
"""
import argparse,hashlib,importlib.util,inspect,json,resource,time
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator,lsmr

PREP_SOURCE='85c726146641e26e09039cfd56e431b56ab503eb2c7801a7ae29d68ea02a0151'
PREPARED='70c6a7cb4f8886d96daba9dacda11d7c82d08342ef4d0283cf3a93c795a58390'
REPORT='b1c03602bd19049361e5268a3cfa39eb0d23fce30805cab814965e45c7c79ea4'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def maximum(a):return float(np.max(np.abs(a)))

def quadratic(F,P,dY,dU):
 """Full Gram q; the p1 target contributes -(delta-rho)^2 everywhere."""
 drho=F.rho(dY[0],constant=0.);ym,um=P.midpoint(dY,dU);parts=[]
 for yy,vv,aa in ((dY,dU,P.scalar_nodes[:,0]),(ym,um,P.scalar_mid[:,0])):
  out=np.empty((len(yy),F.out_n))
  for i in range(0,len(yy),32):
   sl=slice(i,min(i+32,len(yy)));_,dd=F.first_jet(yy[sl]);dv=F.synthesize(vv[sl]);a=aa[sl,None]
   r=np.empty((len(dd),3,F.N));r[:,0]=np.sum(dv*dd,axis=1)/a
   r[:,1]=np.sum(dd*dd,axis=1)/(a*a)-drho[None,:]**2;r[:,2]=np.sum(dv*dv,axis=1)
   out[sl]=F.project_constraints(r)
  parts.append(out.ravel())
 return np.r_[*parts,np.zeros(2*P.n)]

def main(a):
 begin=time.perf_counter();source=sha(__file__)
 required={a.preparation_source:PREP_SOURCE,a.prepared:PREPARED,a.preparation_report:REPORT}
 for f,h in required.items():
  if sha(f)!=h:raise ValueError('Complete fixed preparation identity changed: '+str(f))
 pr=load(a.preparation_source,'one_Gram_T_preparation');base=load(a.matrix_source,'one_Gram_T_matrix')
 gm=load(a.gram_source,'one_Gram_T_Gram');coord=load(a.coordinate_source,'one_Gram_T_coordinate')
 for f,h in ((a.matrix_source,pr.MATRIX_SHA),(a.gram_source,pr.GRAM_SHA),(a.coordinate_source,pr.COORDINATE_SHA)):
  if sha(f)!=h:raise ValueError('Frozen mathematical source changed')
 p,P,identities=base.initialize(a);prep=json.loads(a.preparation_report.read_text())
 with np.load(a.prepared,allow_pickle=False)as z:S=z['scale'].copy();Y=z['Y'].copy();U=z['U'].copy()
 if p.binary_sha(Y,U)!=prep['initialization']['new_YU_sha256']or not np.array_equal(Y,P.Y):raise ValueError('Wrong complete initial state')
 if not np.array_equal(U[1:],P.U[1:])or not np.array_equal(U[0],pr.core_target(P)):raise ValueError('Unexpected initial velocity change')
 if p.binary_sha(P.BA,P.BB,P.target)!=prep['original_BC_sha256']:raise ValueError('Original position boundary changed')
 P.Y=Y;P.U=U
 identities.update({str(k):v for k,v in required.items()});identities[str(a.gram_source)]=pr.GRAM_SHA
 identities[str(a.coordinate_source)]=pr.COORDINATE_SHA;identities[str(a.matrix_source)]=pr.MATRIX_SHA;identities[str(Path(__file__))]=source
 scipy_source=Path(inspect.getsourcefile(lsmr));identities[str(scipy_source)]=sha(scipy_source);p.assert_sources(identities)
 if a.topic.resolve()==a.out.resolve()or a.topic.resolve()in a.out.resolve().parents:raise ValueError('Raw results stay outside Git')
 if a.out.exists()or a.out.with_suffix('.direction.npz').exists():raise ValueError('This one direction already exists; do not repeat it')
 T=coord.IntegratedCoordinates(P);B=pr.CoreBoundary(P,T,S);Aug=pr.augmented_factory(gm.factory(base));J=Aug(P,Y,U)
 r=J.residual();raw=pr.flatten(r);n=P.m*P.n;d0=B.affine(r['boundary'],r['core_velocity']);b=-(raw+J.matvec(d0));calls=[0,0]
 policy=dict(damp=1.,maxiter=256,atol=1e-8,btol=1e-8,conlim=1e6,alpha=1.,linear_solves=1,actual_trial_count=1,
  rows=1158250,variables=580328,old_position_boundary_rows=482,new_core_velocity_rows=482,
  all_full_quadratic_Fourier_modes=True,all_original_cubic_midpoints=True,initial_T_scale_fixed=True,
  prepared_moments_recomputed=False,regularization='new projected scaled T coordinates',raw_row_weights_changed=False,
  old_T_Pr_budget_changed=False,nonlinear_budget_started=False)
 def progress(stage,**kw):
  record=dict(source_sha256=source,stage=stage,policy=policy,initial_YU_sha256=p.binary_sha(Y,U),seconds=time.perf_counter()-begin,**kw)
  pr.write(a.out.with_suffix('.active.json'),record)
 def mv(z):
  calls[0]+=1;v=J.matvec(B.lift(z))
  if calls[0]%16==0:
   progress('LSMR',matvecs=calls[0],rmatvecs=calls[1]);print(json.dumps(dict(event='one_Gram_T_LSMR',matvecs=calls[0],rmatvecs=calls[1],seconds=time.perf_counter()-begin)),flush=True)
  return v
 def rmv(w):calls[1]+=1;return B.pullback(J.rmatvec(w))
 A=LinearOperator(J.shape,matvec=mv,rmatvec=rmv,dtype=float);progress('LSMR',matvecs=0,rmatvecs=0)
 tick=time.perf_counter();sol=lsmr(A,b,damp=1.,atol=1e-8,btol=1e-8,conlim=1e6,maxiter=256,show=False);solve_seconds=time.perf_counter()-tick
 z=sol[0];solve_calls=calls.copy()
 if not np.isfinite(z).all():raise FloatingPointError('Nonfinite one-shot LSMR result; no further direction authorized by this source')
 delta=d0+B.lift(z);dY=delta[:n].reshape(P.m,P.n);dU=delta[n:].reshape(P.m,P.n)
 direction=a.out.with_suffix('.direction.npz');pr.save_npz(direction,Y=Y,U=U,dY=dY,dU=dU,z=z)
 info=dict(istop=int(sol[1]),iterations=int(sol[2]),normr=float(sol[3]),normar=float(sol[4]),norma=float(sol[5]),conda=float(sol[6]),normx=float(sol[7]))
 progress('direction_saved',direction_path=str(direction),direction_sha256=sha(direction),LSMR=info)
 linear=raw+J.matvec(delta);linear_SSE=float(base.inner(linear,linear));pred=r['cost']-linear_SSE
 normal=B.pullback(J.rmatvec(linear))+z;denom=np.linalg.norm(B.pullback(J.rmatvec(b)))
 q=quadratic(J.F,P,dY,dU);ray=raw+J.matvec(delta)+q
 yn=Y+dY;un=U+dU
 if not np.array_equal(un[0],pr.core_target(P)):raise ValueError('Joint masked direction failed to preserve literal U0=ez')
 progress('full_alpha1_residual')
 trial_operator=Aug(P,yn,un);rn=trial_operator.residual();actual=pr.flatten(rn);difference=actual-ray;del trial_operator
 candidate=a.out.with_suffix('.candidate.npz');pr.save_npz(candidate,Y=yn,U=un,mesh=P.x,source_sha256=np.array(source),candidate_YU_sha256=np.array(p.binary_sha(yn,un)))
 ratio=(r['cost']-rn['cost'])/pred if pred>0 else None
 progress('full_alpha1_physical8192',candidate_path=str(candidate),candidate_sha256=sha(candidate))
 physical=P.physical_samples(yn,un)
 merit=bool(rn['finite']and pred>0 and ratio is not None and ratio>=1e-4 and rn['cost']<r['cost']and maximum(rn['boundary'])<=p.BC_TOL and maximum(rn['core_velocity'])==0.)
 feasible=bool(merit and physical.get('finite')and physical.get('all_sampled_domain_and_branch_positive'))
 p.assert_sources(identities)
 result=dict(scope=__doc__,source_sha256=source,identities=identities,policy=policy,original_warm_sha256=p.WARM_SHA,
  prepared_sha256=PREPARED,preparation_report_sha256=REPORT,initial_YU_sha256=p.binary_sha(Y,U),candidate_YU_sha256=p.binary_sha(yn,un),
  initial_full_Gram=pr.summary(r,P.M),actual_trial_full_Gram=pr.summary(rn,P.M),linear_model_SSE=linear_SSE,predicted_reduction=pred,actual_reduction=r['cost']-rn['cost'],ratio=ratio,
  LSMR=info,LSMR_action_counts=solve_calls,LSMR_seconds=solve_seconds,coordinate_regularization_penalty=float(base.inner(z,z)),
  explicit_regularized_normal_L2=float(np.linalg.norm(normal)),explicit_regularized_normal_relative=float(np.linalg.norm(normal)/max(denom,np.finfo(float).tiny)),
  delta_Y_max=maximum(dY),delta_U_max=maximum(dU),linear_old_BC_max=maximum(linear[-2*P.n:-P.n]),linear_new_U0_max=maximum(linear[-P.n:]),
  quadratic_full_Gram_norm_squared=float(base.inner(q,q)),actual_minus_quadratic_ray_max=maximum(difference),
  ray_components_max=dict(nodes=maximum(difference[:P.m*J.F.out_n]),midpoints=maximum(difference[P.m*J.F.out_n:-2*P.n]),position_BC=maximum(difference[-2*P.n:-P.n]),core_velocity=maximum(difference[-P.n:])),
  candidate_core_Z_nonzero=int(np.count_nonzero(yn[0,2*P.M+1:])),candidate_core_Z_max=maximum(yn[0,2*P.M+1:]),candidate_U0_literal_ez=True,
  full_physical_sample_audit=physical,raw_merit_and_position_BC_pass=merit,single_direction_branch_feasible=feasible,
  direction_path=str(direction),direction_sha256=sha(direction),candidate_path=str(candidate),candidate_sha256=sha(candidate),
  accepted_parent=False,finite_nonlinear_solution_claimed=False,continuous_geometry_certified=False,common_C2_reconstruction_paid=False,
  seconds=time.perf_counter()-begin,maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
  scope_limit='One actual complete-direction trial only. Positive branch samples, lower raw Gram SSE, and an LSMR stop are not a closed C2 solution or a continuous metric certificate.')
 pr.write(a.out,result);progress('complete',report_path=str(a.out),report_sha256=sha(a.out))
 print(json.dumps(dict(report=str(a.out),sha256=sha(a.out),**result)),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','gram-source','coordinate-source','preparation-source','prepared','preparation-report','out'):p.add_argument('--'+key,type=Path,required=True)
 main(p.parse_args())
