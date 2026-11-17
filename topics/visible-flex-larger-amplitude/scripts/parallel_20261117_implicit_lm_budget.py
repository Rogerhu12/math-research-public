#!/usr/bin/env python3
"""One full finite LM budget, reusing the already measured original step zero.

Original 1662 problem, fixed S/mesh/scalar/all Pr rows and original 325/157 BC.
At most24 directions INCLUDING cached direction0, at most20 accepted steps.
Every NEW LSMR has maxiter128, atol=btol1e-8, conlim1e6. Full-step actual raw
merit and the existing 8192 node/midpoint physical branch audit govern acceptance.
This is not a physical accepted parent or a continuous C2 metric certificate.
"""
import argparse,gzip,hashlib,importlib.util,inspect,json,math,resource,time
from pathlib import Path
import numpy as np
from scipy.linalg import lu_factor,lu_solve
from scipy.sparse.linalg import LinearOperator,lsmr

MATRIX_SHA='ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4'
PREPARED_SHA='d742521c362b0f680bf53a329784a516416da83fbfd226a23f3a4cb051c7a36c'
PREPARATION_SHA='f691e4e31d53d04a10a4c16be6c23bf15fa0c7aaed56d2338c214b40e2618224'
DIRECTION_SHA='5629db05e0cc7b014c6eb4375badb35ea1d408f40d8cdbccef88122e6150798e'
FIRST_REPORT_SHA='5ac4371a2ff1b7be659a21a507e62d9974c75878308610d095389cefda1b1a7f'
FIRST_PHYSICAL_SHA='ebb364fee7e9a8d5fdfb587a1d89c440f4159862c8453105edf07dcf06c6fd84'
MAX_DIRECTIONS=24;MAX_ACCEPTED=20;MAXITER=128;ATOL=1e-8;BTOL=1e-8;CONLIM=1e6;ETA=1e-4
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def maximum(z):return float(np.max(np.abs(z)))
def norm(z):return float(np.linalg.norm(z))
def write(p,d):p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
def emit(**d):print(json.dumps(d,allow_nan=False),flush=True)
def rss():return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

class FixedBoundary:
 def __init__(self,P,S,Qs):
  self.P,self.S,self.Qs=P,S,Qs;n=P.n;count=P.m*n
  self.indices=(slice(0,n),slice(count-n,count));self.rows=(P.BA[:P.nl],P.BB[P.nl:]);self.norms=[];self.factors=[]
  for B,Q,index in zip(self.rows,Qs,self.indices):
   C=B*S[index][None,:];rn=np.linalg.norm(C,axis=1);CQ=(C@Q)/rn[:,None]
   if not np.isfinite(CQ).all()or np.min(rn)<=0:raise ValueError('Invalid frozen boundary coordinates')
   self.norms.append(rn);self.factors.append(lu_factor(CQ,check_finite=True))
 def project(self,z):
  z=np.asarray(z).reshape(-1).copy()
  for Q,index in zip(self.Qs,self.indices):z[index]-=Q@(Q.T@z[index])
  return z
 def lift(self,z):return self.S*self.project(z)
 def pullback(self,z):return self.project(self.S*z)
 def affine(self,residual):
  z=np.zeros_like(self.S)
  for Q,index,rn,fac,r in zip(self.Qs,self.indices,self.norms,self.factors,(residual[:self.P.nl],residual[self.P.nl:])):
   z[index]=self.S[index]*(Q@lu_solve(fac,-r/rn,check_finite=True))
  return z

def main(a):
 start=time.perf_counter();source_sha=sha(__file__)
 required={a.matrix_source:MATRIX_SHA,a.prepared:PREPARED_SHA,a.preparation_report:PREPARATION_SHA,
  a.first_direction:DIRECTION_SHA,a.first_report:FIRST_REPORT_SHA,a.first_physical:FIRST_PHYSICAL_SHA}
 for file,expected in required.items():
  if sha(file)!=expected:raise ValueError('Frozen cached input changed: '+str(file))
 mf=load(a.matrix_source,'lm_budget_matrix');p,P,identities=mf.initialize(a)
 identities.update({str(file):value for file,value in required.items()});identities[str(Path(__file__))]=source_sha
 ls_source=Path(inspect.getsourcefile(lsmr));identities[str(ls_source)]=sha(ls_source);p.assert_sources(identities)
 if a.topic.resolve()==a.work.resolve()or a.topic.resolve()in a.work.resolve().parents:raise ValueError('All regenerable state/direction archives must remain outside the topic')
 a.work.mkdir(parents=True,exist_ok=True);a.out.parent.mkdir(parents=True,exist_ok=True)
 prep=read(a.preparation_report);first=read(a.first_report);first_physical=read(a.first_physical)
 if not prep['exact_right_boundary_rank']['exact_integer_less_than_one']:raise ValueError('Missing original exact BB rank certificate')
 if prep['original_base_YU_sha256']!=p.binary_sha(P.Y,P.U):raise ValueError('Wrong original warm base')
 with np.load(a.prepared,allow_pickle=False)as data:
  S=data['scale'].copy();Qs=(data['Q_left'].copy(),data['Q_right'].copy())
 if len(S)!=2*P.m*P.n or not np.isfinite(S).all()or np.min(S)<=0:raise ValueError('Bad frozen positive diagonal scale')
 bc=FixedBoundary(P,S,Qs);n=P.m*P.n
 with np.load(a.first_direction,allow_pickle=False)as d:
  if not np.array_equal(d['Y'],P.Y)or not np.array_equal(d['U'],P.U):raise ValueError('Cached step zero did not start at original1662')
  Y=P.Y+d['dY'];U=P.U+d['dU']
 if p.binary_sha(Y,U)!=first_physical['candidate_YU_sha256']:raise ValueError('Cached physical audit is for another trial')
 R=P.residual(Y,U)
 if R['cost']!=first_physical['complete_residual']['raw_residual_square_sum']:raise ValueError('Cached raw cost changed')
 cost0=prep['initial_residual']['raw_residual_square_sum'];pred0=cost0-first['actual_linear_model_SSE'];ratio0=(cost0-R['cost'])/pred0
 physical0=first_physical['physical']
 if not(R['finite']and pred0>0 and ratio0>=ETA and R['cost']<cost0 and maximum(R['boundary'])<=p.BC_TOL and physical0['finite']and physical0['all_sampled_domain_and_branch_positive']):raise ValueError('Cached step zero does not pass the frozen acceptance rule')
 policy=dict(max_directions_including_cached_zero=MAX_DIRECTIONS,max_accepted_steps=MAX_ACCEPTED,
  LSMR_maxiter=MAXITER,LSMR_atol=ATOL,LSMR_btol=BTOL,LSMR_conlim=CONLIM,
  Pr_tol=p.PR_TOL,bc_tol=p.BC_TOL,ratio_threshold=ETA,alpha=1.,
  predicted_reduction='raw_SSE - ||r+J*delta||_2^2 over all580328 rows',
  acceptance='finite full residual, pred>0, ratio>=1e-4, actual rawSSE decrease, originalBC<=1e-11, then finite positive rho/Q/W/H/normal at every8192 node+actual cubic-mid sample',
  damping='initial cached damp1; accepted ratio>.75: /2, ratio<.25: *2, otherwise unchanged; rejected: same point *2',
  fixed_initial_S=True,fixed_original_mesh=True,all_rows_retained=True,changed_raw_row_weights=False,
  no_intermediate_Gram_monotonicity_requirement=True,no_initial_diagonal_or_cached_LSMR_or_cached_physical_repetition=True,
  finite_LSMR_stop_not_automatically_converged=True,all_directions_saved=True)
 history=[dict(direction_index=0,cached=True,accepted=True,base_YU_sha256=prep['original_base_YU_sha256'],
  candidate_YU_sha256=p.binary_sha(Y,U),damp=1.,predicted_reduction=pred0,actual_reduction=cost0-R['cost'],ratio=ratio0,
  residual_before=prep['initial_residual'],residual_after=P.summary(R),lsmr_return=first['lsmr_return'],
  explicit_regularized_normal_residual_L2=first['explicit_regularized_normal_residual_L2'],
  explicit_regularized_normal_residual_relative=first['explicit_regularized_normal_residual_relative'],
  direction_file=str(a.first_direction),direction_file_sha256=DIRECTION_SHA,physical=physical0)]
 accepted=1;directions=1;damp=.5 if ratio0>.75 else(2. if ratio0<.25 else 1.);J=None;failure=None
 state_file=None;state_sha=None
 def save_state():
  nonlocal state_file,state_sha
  state_file=a.work/f'accepted-{accepted:03d}.npz';np.savez_compressed(state_file,Y=Y,U=U);state_sha=sha(state_file)
  checkpoint=dict(schema='complete-Pr-LM-checkpoint-v1',source_sha256=source_sha,identities=identities,
   original_warm_sha256=p.WARM_SHA,accepted_parent=False,accepted_algebraic_steps=accepted,directions_used=directions,
   damp_next=damp,M=P.M,N=P.N,mesh=P.x.tolist(),states=Y.tolist(),independent_velocities=U.tolist(),
   residual_summary=P.summary(R),history=history,policy=policy,state_archive=str(state_file),state_archive_sha256=state_sha)
  a.out.with_suffix('.checkpoint.json.gz').write_bytes(gzip.compress((json.dumps(checkpoint,allow_nan=False)+'\n').encode(),mtime=0))
 save_state();emit(event='LM_budget_start_cached_zero',policy=policy,source_sha256=source_sha,accepted=accepted,directions=directions,damp_next=damp,
  ratio=ratio0,raw_SSE=R['cost'],candidate_YU_sha256=p.binary_sha(Y,U),physical_audit_reused_sha256=FIRST_PHYSICAL_SHA)
 while directions<MAX_DIRECTIONS and accepted<MAX_ACCEPTED and not P.converged(R):
  p.assert_sources(identities);index=directions;directions+=1;attempt_start=time.perf_counter();base_sha=p.binary_sha(Y,U)
  if J is None:J=mf.CompleteLinear(P,Y,U)
  raw=mf.flatten(R);d0=bc.affine(R['boundary']);b=-(raw+J.matvec(d0));calls=[0,0];in_solve=True
  def mv(z):
   calls[0]+=1;out=J.matvec(bc.lift(z))
   if in_solve and calls[0]%16==0:emit(event='LM_budget_linear_progress',direction_index=index,damp=damp,matvecs=calls[0],rmatvecs=calls[1],seconds=time.perf_counter()-attempt_start)
   return out
  def rmv(w):calls[1]+=1;return bc.pullback(J.rmatvec(w))
  A=LinearOperator(J.shape,matvec=mv,rmatvec=rmv,dtype=float)
  try:sol=lsmr(A,b,damp=damp,atol=ATOL,btol=BTOL,conlim=CONLIM,maxiter=MAXITER,show=False)
  except Exception as exc:
   failure=dict(direction_index=index,stage='LSMR',type=type(exc).__name__,message=str(exc));history.append(dict(direction_index=index,accepted=False,damp=damp,failure=failure));break
  in_solve=False;solve_calls=calls.copy();z=sol[0]
  info=dict(istop=int(sol[1]),iterations=int(sol[2]),normr=float(sol[3]),normar=float(sol[4]),norma=float(sol[5]),conda=float(sol[6]),normx=float(sol[7]))
  record=dict(direction_index=index,cached=False,base_YU_sha256=base_sha,base_state_archive=str(state_file),base_state_archive_sha256=state_sha,
   damp=damp,lsmr_return={k:(v if isinstance(v,int)or math.isfinite(v)else None)for k,v in info.items()},LSMR_action_counts=solve_calls,residual_before=P.summary(R))
  if not np.isfinite(z).all():
   record.update(accepted=False,rejection='nonfinite_LSMR_direction',seconds=time.perf_counter()-attempt_start);history.append(record);damp*=2
   emit(event='LM_budget_reject',**record,damp_next=damp);continue
  delta=d0+bc.lift(z);dY=delta[:n].reshape(P.m,P.n);dU=delta[n:].reshape(P.m,P.n)
  direction_file=a.work/f'direction-{index:03d}.npz';np.savez_compressed(direction_file,dY=dY,dU=dU,z=z)
  record.update(direction_file=str(direction_file),direction_file_sha256=sha(direction_file),direction_binary_sha256=p.binary_sha(dY,dU),
   delta_Y_max=maximum(dY)if np.isfinite(dY).all()else None,delta_U_max=maximum(dU)if np.isfinite(dU).all()else None)
  if not np.isfinite(delta).all():
   record.update(accepted=False,rejection='nonfinite_lifted_direction',seconds=time.perf_counter()-attempt_start);history.append(record);damp*=2
   emit(event='LM_budget_reject',**record,damp_next=damp);continue
  jdelta=J.matvec(delta);linear=raw+jdelta;linear_SSE=float(mf.inner(linear,linear));pred=R['cost']-linear_SSE
  if not np.isfinite(linear).all()or not math.isfinite(linear_SSE):
   record.update(accepted=False,rejection='nonfinite_linear_model',seconds=time.perf_counter()-attempt_start);history.append(record);damp*=2
   emit(event='LM_budget_reject',**record,damp_next=damp);continue
  normal=A.rmatvec(linear)+damp*damp*z;normal_denom=max(norm(A.rmatvec(b)),np.finfo(float).tiny)
  if not np.isfinite(normal).all()or not math.isfinite(normal_denom):
   record.update(accepted=False,rejection='nonfinite_regularized_normal_residual',seconds=time.perf_counter()-attempt_start);history.append(record);damp*=2
   emit(event='LM_budget_reject',**record,damp_next=damp);continue
  record.update(linear_model_SSE=linear_SSE,predicted_reduction=pred,regularization_penalty=float(damp*damp*mf.inner(z,z)),
   explicit_regularized_normal_residual_L2=norm(normal),explicit_regularized_normal_residual_relative=norm(normal)/normal_denom,
   original_BC_linear_residual_max=maximum(linear[-P.n:]))
  yn=Y+dY;un=U+dU;rn=P.residual(yn,un)
  finite=rn['finite']and math.isfinite(pred);ratio=(R['cost']-rn['cost'])/pred if finite and pred>0 else None
  if ratio is not None and not math.isfinite(ratio):ratio=None
  merit=bool(finite and pred>0 and ratio is not None and ratio>=ETA and rn['cost']<R['cost']and maximum(rn['boundary'])<=p.BC_TOL)
  physical=None;ok=False
  if merit:
   physical=P.physical_samples(yn,un);ok=bool(physical.get('finite')and physical.get('all_sampled_domain_and_branch_positive'))
  record.update(accepted=ok,ratio=ratio,residual_trial=P.summary(rn),physical=physical,
   rejection=None if ok else('physical_branch_gate'if merit else'raw_merit_or_original_BC_gate'),seconds=time.perf_counter()-attempt_start)
  history.append(record)
  if ok:
   Y,U,R=yn,un,rn;accepted+=1
   if ratio>.75:damp/=2
   elif ratio<.25:damp*=2
   J=None;A=None;save_state()
   emit(event='LM_budget_accept',direction_index=index,accepted_steps=accepted,directions_used=directions,damp_next=damp,
    raw_SSE=R['cost'],ratio=ratio,node_max=maximum(R['nodes']),midpoint_max=maximum(R['middle']),BC_max=maximum(R['boundary']),
    physical_H_min=physical['domain_minima']['H']['value'],physical_normal_min=physical['domain_minima']['positive_branch_normal_velocity']['value'],
    actual_cubic_Gram=physical['actual_common_cubic_Gram_max'],lsmr=record['lsmr_return'],normal_relative=record['explicit_regularized_normal_residual_relative'],seconds=record['seconds'])
  else:
   damp*=2;emit(event='LM_budget_reject',direction_index=index,directions_used=directions,damp_next=damp,ratio=ratio,
    reason=record['rejection'],trial=P.summary(rn),physical=physical,lsmr=record['lsmr_return'],seconds=record['seconds'])
 if failure is not None:reason='linear_exception_retained_previous_accepted_state'
 elif P.converged(R):reason='full_Pr_and_BC_tolerances_met'
 elif accepted>=MAX_ACCEPTED:reason='fixed20accepted_budget'
 else:reason='fixed24direction_budget'
 J=None;A=None;p.assert_sources(identities);physical=P.physical_samples(Y,U);jets=P.terminal_common_jets(Y,U);p.assert_sources(identities)
 result=dict(schema='independent-YU-polynomial-Frenet-finite-attempt-v1',scope=__doc__,source_sha256=source_sha,identities=identities,
  M=P.M,N=P.N,dimension_Y=P.n,dimension_U=P.n,nodes=P.m,mesh=P.x.tolist(),states=Y.tolist(),independent_velocities=U.tolist(),
  nodes_raw_constraints=R['nodes'].tolist(),midpoint_raw_constraints=R['middle'].tolist(),boundary_residual=R['boundary'].tolist(),residual_summary=P.summary(R),
  finite_algebraic_converged=P.converged(R),termination=reason,failure=failure,original_explicit_BVP_accepted=False,accepted_parent=False,
  full_Newton_executed=False,full_LM_executed=True,policy=policy,accepted_algebraic_steps=accepted,directions_used=directions,damp_next=damp,
  unchanged_boundary=dict(left_count=P.nl,right_count=P.n-P.nl,rows=P.BB[P.nl:].tolist(),target=P.target[P.nl:].tolist(),arrays_sha256=p.binary_sha(P.BA,P.BB,P.target)),
  fixed_scalar_profile=P.metadata['fixed_scalar_profile'],analytic_extension_origin=P.metadata['analytic_extension_origin'],hold_scalar_profile=P.metadata['hold_scalar_profile'],hold_profile_sha256=p.HOLD_SHA,
  scalar_nodes=dict(a=P.scalar_nodes[:,0].tolist(),ap=P.scalar_nodes[:,1].tolist(),app=P.scalar_nodes[:,2].tolist(),k=P.k.tolist(),k_prime=P.kprime.tolist()),
  core=dict(coefficients=Y[0,1:P.M+1].tolist(),fixed_first_three=P.metadata['fixed_core_first_three'],axis_support_gap=float(2*np.sum(Y[0,1:P.M+1:2]))),
  history=history,physical_sample_audit=physical,counts=P.counts,common_accelerations=jets['common_accelerations'],
  common_jet_readout={k:v for k,v in jets.items()if k!='common_accelerations'},continuous_geometry_certified=False,
  cubic_solver_field_regularity='C1 and piecewise cubic; no automatic C2 assertion',old_cut_jets_not_fabricated=True,
  seconds=time.perf_counter()-start,maximum_RSS_kib=rss())
 field=a.out.with_suffix('.field.json.gz');field.write_bytes(gzip.compress((json.dumps(result,allow_nan=False)+'\n').encode(),mtime=0))
 report={k:v for k,v in result.items()if k not in ('mesh','states','independent_velocities','nodes_raw_constraints','midpoint_raw_constraints','boundary_residual','fixed_scalar_profile','scalar_nodes','unchanged_boundary','common_accelerations','common_jet_readout','core')}
 report.update(field_path=str(field),field_sha256=sha(field),common_jet_readout_summary=dict(missing_acceleration_nodes=jets['missing_acceleration_nodes'],
  max_condition_estimate_1norm=max((v for v in jets['C_U_condition_estimate_1norm']if v is not None),default=None),
  max_linear_residual=max((v for v in jets['acceleration_linear_residual_max_by_node']if v is not None),default=None)),core={k:v for k,v in result['core'].items()if k!='coefficients'})
 write(a.out,report);emit(event='LM_budget_terminal',report=str(a.out),report_sha256=sha(a.out),field=str(field),field_sha256=sha(field),
  termination=reason,accepted_steps=accepted,directions=directions,**P.summary(R),physical=physical,common_jet_summary=report['common_jet_readout_summary'],seconds=report['seconds'],maximum_RSS_kib=rss())

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','prepared','preparation-report','first-direction','first-report','first-physical','work','out'):a.add_argument('--'+key,type=Path,required=True)
 main(a.parse_args())
