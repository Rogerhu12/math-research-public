#!/usr/bin/env python3
"""One original1662 Pr direction with the frozen invertible T coordinates.

All variables, compatibility defects,580328 raw rows and original BC remain.
Only the right coordinates/column scale and hence the damped step norm change.
Reuses ef81/7aff preparation. No moments/column-norm recalculation or nonlinear
loop. --execute-direction is required for the single damp1/maxiter128 solve.
"""
import argparse,hashlib,importlib.util,inspect,json,resource,time
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator,lsmr
MATRIX_SHA='ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4'
COORDINATE_SHA='ef81da0b0de7200501d34d6702f92ae0131a953e9038ad8302d2e1edb61cd3d8'
PREPARED_SHA='7affbce1eac7e61b94a03ca8b463c35ea1c4e28dfc3f02e74f1847670923965e'
PREPARATION_SHA='c69c2325a979af1757904ff37ba7ad7a3e7ef4f1e2f1f003d63cf985e875ec8f'
RAY_SHA='e67f7d1bf021fd88646e1a77057b4557418ff77ebd5032461d8a46dd7f6498fc'
BASELINE_SHA='5629db05e0cc7b014c6eb4375badb35ea1d408f40d8cdbccef88122e6150798e'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def maximum(z):return float(np.max(np.abs(z)))
def norm(z):return float(np.linalg.norm(z))
def write(p,d):p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
def emit(**d):print(json.dumps(d,allow_nan=False),flush=True)

def main(a):
 start=time.perf_counter();required={a.matrix_source:MATRIX_SHA,a.coordinate_source:COORDINATE_SHA,
  a.prepared:PREPARED_SHA,a.preparation_report:PREPARATION_SHA,a.ray_source:RAY_SHA,a.baseline_direction:BASELINE_SHA}
 for file,expected in required.items():
  if sha(file)!=expected:raise ValueError('Frozen source/input changed: '+str(file))
 mf=load(a.matrix_source,'T_direction_matrix');coord=load(a.coordinate_source,'T_direction_coordinates');ray=load(a.ray_source,'T_direction_ray')
 p,P,identities=mf.initialize(a);identities.update({str(file):value for file,value in required.items()})
 identities[str(Path(__file__))]=sha(__file__);ls_source=Path(inspect.getsourcefile(lsmr));identities[str(ls_source)]=sha(ls_source)
 prep=json.loads(a.preparation_report.read_text())
 if prep['original_warm_sha256']!=p.WARM_SHA or prep['prepared_sha256']!=PREPARED_SHA:raise ValueError('Wrong original1662 preparation')
 with np.load(a.prepared,allow_pickle=False)as data:S=data['scale'].copy()
 T=coord.IntegratedCoordinates(P);B=coord.IntegratedBoundary(P,T,S);n=P.m*P.n
 if T.size!=2*n:raise ValueError('Dropped original variables/compatibility defects')
 with np.load(a.baseline_direction,allow_pickle=False)as data:
  if not np.array_equal(data['Y'],P.Y)or not np.array_equal(data['U'],P.U):raise ValueError('Baseline is at a different base')
  baseline_delta=np.r_[data['dY'].ravel(),data['dU'].ravel()]
 preparation=dict(schema='one-integrated-coordinate-Pr-direction-preparation-v1',scope=__doc__,identities=identities,
  M=P.M,N=P.N,nodes=P.m,variables=2*n,rows=2*n,coordinate_order=prep['coordinate_order'],
  all_compatibility_defects_retained=True,original_base_YU_sha256=p.binary_sha(P.Y,P.U),
  prepared_arrays_reused_sha256=PREPARED_SHA,original_boundary_sha256=p.binary_sha(P.BA,P.BB,P.target),
  policy=dict(damp=1.,maxiter=128,atol=1e-8,btol=1e-8,conlim=1e6,actual_alpha=1.,
   objective='||r+J*d0+J*T*S*Pi*z||_2^2+||z||_2^2',direction='d0+T*S*Pi*z',
   changed_step_norm=True,changed_raw_residual_weights=False,changed_equations=False,new_direction_solves=1,nonlinear_iterations=0),
  linear_solve_executed=False,accepted_parent=False,source_sha256=sha(__file__))
 p.assert_sources(identities);write(a.out.with_suffix('.preparation.json'),preparation)
 emit(event='integrated_direction_prepared',report=str(a.out.with_suffix('.preparation.json')),sha256=sha(a.out.with_suffix('.preparation.json')))
 if not a.execute_direction:return
 r=P.residual(P.Y,P.U);raw=mf.flatten(r);J=mf.CompleteLinear(P,P.Y,P.U);d0=B.affine(r['boundary']);b=-(raw+J.matvec(d0))
 physical_gradient_before=J.rmatvec(raw);calls=[0,0];in_solve=True
 def mv(z):
  calls[0]+=1;value=J.matvec(B.lift(z))
  if in_solve and calls[0]%16==0:emit(event='integrated_LSMR_progress',matvecs=calls[0],rmatvecs=calls[1],seconds=time.perf_counter()-start)
  return value
 def rmv(w):calls[1]+=1;return B.pullback(J.rmatvec(w))
 A=LinearOperator(J.shape,matvec=mv,rmatvec=rmv,dtype=float);tick=time.perf_counter()
 sol=lsmr(A,b,damp=1.,atol=1e-8,btol=1e-8,conlim=1e6,maxiter=128,show=False)
 solve_seconds=time.perf_counter()-tick;in_solve=False;solve_counts=calls.copy();z=sol[0]
 if not np.isfinite(z).all()or not all(np.isfinite(sol[i])for i in range(3,8)):raise FloatingPointError('Nonfinite single-budget LSMR output')
 delta=d0+B.lift(z);dY=delta[:n].reshape(P.m,P.n);dU=delta[n:].reshape(P.m,P.n)
 if not np.isfinite(delta).all():raise FloatingPointError('Nonfinite physical direction')
 linear=raw+J.matvec(delta);physical_gradient_after=J.rmatvec(linear)
 normal=B.pullback(physical_gradient_after)+z;normal_denom=max(norm(A.rmatvec(b)),np.finfo(float).tiny)
 baseline_linear=raw+J.matvec(baseline_delta);baseline_gradient=J.rmatvec(baseline_linear)
 predicted=r['cost']-float(mf.inner(linear,linear));Y=P.Y+dY;U=P.U+dU
 actual=P.residual(Y,U);ratio=(r['cost']-actual['cost'])/predicted if actual['finite']and predicted>0 else None
 if ratio is not None and not np.isfinite(ratio):ratio=None
 original_BC_linear=r['boundary']+P.BA@dY[0]+P.BB@dY[-1]
 file=a.out.with_suffix('.direction.npz');np.savez_compressed(file,Y=P.Y,U=P.U,dY=dY,dU=dU,z=z)
 audit=None
 if actual['finite']:audit=P.physical_samples(Y,U)
 ray_report=ray.analyze(P,P.Y,P.U,dY,dU,alphas=(1.,));ray_path=a.out.with_suffix('.ray.json');write(ray_path,ray_report)
 raw_merit=bool(ratio is not None and ratio>=1e-4 and actual['cost']<r['cost']and maximum(actual['boundary'])<=p.BC_TOL)
 sampled_feasible=bool(audit and audit.get('finite')and audit.get('all_sampled_domain_and_branch_positive'))
 result=dict(preparation=preparation,source_sha256=sha(__file__),linear_solve_executed=True,nonlinear_solve_executed=False,
  lsmr_return=dict(istop=int(sol[1]),iterations=int(sol[2]),normr=float(sol[3]),normar=float(sol[4]),norma=float(sol[5]),conda=float(sol[6]),normx=float(sol[7])),
  solve_seconds=solve_seconds,LSMR_action_counts=solve_counts,initial_residual=P.summary(r),actual_trial_residual=P.summary(actual),
  actual_linear_model_SSE=float(mf.inner(linear,linear)),regularization_penalty=float(mf.inner(z,z)),predicted_reduction=predicted,actual_to_predicted_ratio=ratio,
  explicit_coordinate_normal_residual_L2=norm(normal),explicit_coordinate_normal_residual_relative=norm(normal)/normal_denom,
  comparable_original_YU_coefficient_diagnostics=dict(
   definition='Euclidean original (Y,U) coefficients: J^T r and J^T(r+J delta); twice these are gradients of raw SSE. Raw vectors include constrained-normal components and are NOT alone equality-constrained stationarity tests.',
   JT_r_L2=norm(physical_gradient_before),JT_r_max=maximum(physical_gradient_before),
   JT_new_linear_residual_L2=norm(physical_gradient_after),JT_new_linear_residual_max=maximum(physical_gradient_after),
   new_relative_to_initial=norm(physical_gradient_after)/max(norm(physical_gradient_before),np.finfo(float).tiny),
   previous_S_only_direction_sha256=BASELINE_SHA,previous_S_only_linear_SSE=float(mf.inner(baseline_linear,baseline_linear)),
   JT_previous_S_only_linear_residual_L2=norm(baseline_gradient),JT_previous_S_only_linear_residual_max=maximum(baseline_gradient),
   previous_relative_to_initial=norm(baseline_gradient)/max(norm(physical_gradient_before),np.finfo(float).tiny),
   previous_direction_only_read=True,previous_LSMR_not_repeated=True),
  original_BC_linear_remaining_max=maximum(original_BC_linear),delta_Y_max=maximum(dY),delta_U_max=maximum(dU),
  direction_path=str(file),direction_file_sha256=sha(file),direction_binary_sha256=p.binary_sha(dY,dU),candidate_YU_sha256=p.binary_sha(Y,U),
  physical_sample_audit=audit,raw_merit_rule_passed=raw_merit,sampled_physical_branch_passed=sampled_feasible,
  admissible_single_trial_after_audit=raw_merit and sampled_feasible,accepted_parent=False,continuous_geometry_certified=False,
  ray_report_path=str(ray_path),ray_report_sha256=sha(ray_path),seconds=time.perf_counter()-start,maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 p.assert_sources(identities);write(a.out,result);emit(event='integrated_direction_complete',report=str(a.out),sha256=sha(a.out),
  lsmr=result['lsmr_return'],raw_SSE=actual['cost'],ratio=ratio,coordinate_normal_relative=result['explicit_coordinate_normal_residual_relative'],
  physical=result['physical_sample_audit'],seconds=result['seconds'],accepted_parent=False)

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','coordinate-source','prepared','preparation-report','ray-source','baseline-direction','out'):a.add_argument('--'+key,type=Path,required=True)
 a.add_argument('--execute-direction',action='store_true');main(a.parse_args())
