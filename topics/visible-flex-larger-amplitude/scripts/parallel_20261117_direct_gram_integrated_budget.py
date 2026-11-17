#!/usr/bin/env python3
"""One full-spectrum polynomial-Gram LM budget, distinct from the Pr run.

Same original1662 g/mesh/Y and later U, with the prepared exact U0=ez model.
All1158250 rows, all580328 variables and all964 joint boundary rows remain.
Cached513 direction0 used256 iterations; every NEW direction uses at most512.
Maximum24 logical directions including0 and20 accepted steps. Reuse70c scale.
New terminal gates: full Gram coefficients1e-10, oldBC1e-11, literalU0=ez,
and the complete8192 node+midpoint sampled relative Gram at most5e-7.
No old Pr residual or C_U inverse is used to define the objective or jets.
"""
import argparse,gzip,hashlib,importlib.util,inspect,json,math,os,resource,time
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator,lsmr

MATRIX_SHA='ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4'
COORDINATE_SHA='ef81da0b0de7200501d34d6702f92ae0131a953e9038ad8302d2e1edb61cd3d8'
PREP_SOURCE_SHA='85c726146641e26e09039cfd56e431b56ab503eb2c7801a7ae29d68ea02a0151'
GRAM_SOURCE_SHA='5b5ebf5276ab73109859fc03cade7716ca3a6941bb5a5f19890673447db735e6'
PREPARED_SHA='70c6a7cb4f8886d96daba9dacda11d7c82d08342ef4d0283cf3a93c795a58390'
PREPARATION_SHA='b1c03602bd19049361e5268a3cfa39eb0d23fce30805cab814965e45c7c79ea4'
DIRECTION_SHA='11550c74cc98c95864625b499d90aa136b56961452f266f314672cf3dea51447'
FIRST_REPORT_SHA='81c8d13152a5b31229395c148d8d115ab3d071b421b92cf1e31f8acd04b884b4'
FIRST_SOURCE_SHA='513aa782ee2da6bc61acb3c7e5df2c2585e4f3e917b76836946284394253306d'
GRAM_TOL=1e-10;PHYSICAL_GRAM_TOL=5e-7
MAX_DIRECTIONS=24;MAX_ACCEPTED=20;MAXITER=512;ATOL=1e-8;BTOL=1e-8;CONLIM=1e6;ETA=1e-4
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def maximum(z):return float(np.max(np.abs(z)))
def norm(z):return float(np.linalg.norm(z))
def write_bytes(p,data):
 p=Path(p);tmp=p.with_name(p.name+'.tmp')
 with tmp.open('wb')as f:f.write(data);f.flush();os.fsync(f.fileno())
 tmp.replace(p)
def write(p,d):write_bytes(p,(json.dumps(d,indent=2,allow_nan=False)+'\n').encode())
def save_npz(p,**arrays):
 p=Path(p);tmp=p.with_name(p.name+'.tmp')
 with tmp.open('wb')as f:np.savez_compressed(f,**arrays);f.flush();os.fsync(f.fileno())
 tmp.replace(p)
def emit(**d):print(json.dumps(d,allow_nan=False),flush=True)
def rss():return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
def clean_info(sol):
 d=dict(istop=int(sol[1]),iterations=int(sol[2]),normr=float(sol[3]),normar=float(sol[4]),norma=float(sol[5]),conda=float(sol[6]),normx=float(sol[7]))
 return {k:(v if isinstance(v,int)or math.isfinite(v)else None)for k,v in d.items()}

def main(a):
 start=time.perf_counter();source_sha=sha(__file__);invocation=str(time.time_ns())
 required={a.matrix_source:MATRIX_SHA,a.coordinate_source:COORDINATE_SHA,a.prepared:PREPARED_SHA,
  a.preparation_report:PREPARATION_SHA,a.first_direction:DIRECTION_SHA,a.first_report:FIRST_REPORT_SHA,
  a.preparation_source:PREP_SOURCE_SHA,a.gram_source:GRAM_SOURCE_SHA}
 for file,expected in required.items():
  if sha(file)!=expected:raise ValueError('Frozen input changed: '+str(file))
 mf=load(a.matrix_source,'full_Gram_budget_matrix');coord=load(a.coordinate_source,'full_Gram_budget_coordinates')
 pr=load(a.preparation_source,'full_Gram_budget_preparation');gm=load(a.gram_source,'full_Gram_budget_operator')
 p,P,identities=mf.initialize(a);identities.update({str(f):h for f,h in required.items()});identities[str(Path(__file__))]=source_sha
 ls_source=Path(inspect.getsourcefile(lsmr));identities[str(ls_source)]=sha(ls_source);p.assert_sources(identities)
 if (P.M,P.N,P.m,P.n,P.nl,p.PR_TOL,p.BC_TOL)!=(160,2048,602,482,325,1e-8,1e-11):raise ValueError('Original finite problem changed')
 for loc in (a.work,a.out):
  if a.topic.resolve()==loc.resolve()or a.topic.resolve()in loc.resolve().parents:raise ValueError('Raw archives must remain outside topic')
 a.work.mkdir(parents=True,exist_ok=True);a.out.parent.mkdir(parents=True,exist_ok=True)
 prep=read(a.preparation_report);first=read(a.first_report)
 if prep['original_warm_sha256']!=p.WARM_SHA or prep['prepared_sha256']!=PREPARED_SHA:raise ValueError('Wrong complete Gram preparation')
 with np.load(a.prepared,allow_pickle=False)as data:S=data['scale'].copy();baseY=data['Y'].copy();baseU=data['U'].copy()
 if not np.array_equal(baseY,P.Y)or not np.array_equal(baseU[1:],P.U[1:])or not np.array_equal(baseU[0],pr.core_target(P)):raise ValueError('New initialization changed more than U0=ez')
 if p.binary_sha(baseY,baseU)!=prep['initialization']['new_YU_sha256']:raise ValueError('Wrong prepared full initial state')
 P.Y=baseY;P.U=baseU
 if first['source_sha256']!=FIRST_SOURCE_SHA or first['initial_YU_sha256']!=p.binary_sha(P.Y,P.U):raise ValueError('Wrong cached full-Gram direction')
 if prep['original_BC_sha256']!=p.binary_sha(P.BA,P.BB,P.target):raise ValueError('Original BC bytes changed')
 if (first['policy']['rows'],first['policy']['variables'])!=(1158250,580328):raise ValueError('Cached model omits full Gram rows/variables')
 T=coord.IntegratedCoordinates(P);bc=pr.CoreBoundary(P,T,S);Aug=pr.augmented_factory(gm.factory(mf));n=P.m*P.n
 if T.size!=2*n:raise ValueError('Dropped compatibility variables')
 gram_counts=dict(residual_evaluations=0,node_constraint_points=0,midpoint_constraint_points=0)
 def evaluate(yy,uu):
  operator=Aug(P,yy,uu)
  if operator.shape!=(1158250,580328):raise ValueError('Changed complete Gram row/variable count')
  r=operator.residual();del operator
  gram_counts['residual_evaluations']+=1;gram_counts['node_constraint_points']+=P.m;gram_counts['midpoint_constraint_points']+=P.m-1
  return r
 def summary(r):
  return pr.summary(r,P.M)if r['finite']else dict(finite=False,raw_SSE=None)
 def algebraic_converged(r,uu):
  return bool(r['finite']and maximum(r['nodes'])<=GRAM_TOL and maximum(r['middle'])<=GRAM_TOL and maximum(r['boundary'])<=p.BC_TOL and maximum(r['core_velocity'])==0. and np.array_equal(uu[0],pr.core_target(P)))
 def converged():
  if not algebraic_converged(R,U):return False
  audit=next(h['physical']for h in reversed(history)if h.get('accepted'))
  return bool(audit.get('finite')and audit.get('all_sampled_domain_and_branch_positive')and audit['actual_common_cubic_Gram_max']['value']<=PHYSICAL_GRAM_TOL)
 policy=dict(max_directions_including_cached_zero=MAX_DIRECTIONS,max_accepted_steps=MAX_ACCEPTED,
  cached_zero_LSMR_maxiter=256,new_LSMR_maxiter=MAXITER,LSMR_atol=ATOL,LSMR_btol=BTOL,LSMR_conlim=CONLIM,
  full_Gram_coefficient_tol=GRAM_TOL,sampled_relative_Gram_tol=PHYSICAL_GRAM_TOL,bc_tol=p.BC_TOL,literal_U0_ez_required=True,ratio_threshold=ETA,alpha=1.,
  predicted_reduction='full_Gram_raw_SSE - ||r+J*delta||_2^2 over all1158250 rows',
  acceptance='finite full Gram residual, pred>0, ratio>=1e-4, actual rawSSE decrease, originalBC<=1e-11 and literalU0=ez, then finite positive rho/Q/W/H/normal at every8192 node+actual cubic-mid sample',
  damping='initial cached damp1; accepted ratio>.75: /2, ratio<.25: *2, otherwise unchanged; rejected: same point *2',
  coordinates='C then all U then all trapezoidal defects D; all retained',direction='d0+T*S*Pi*z',
  regularized_objective='||r+J*d0+J*T*S*Pi*z||^2+damp^2*||z||^2',changed_step_norm_from_original_S_only=True,
  fixed_initial_T_scale=True,fixed_original_mesh=True,all_rows_retained=True,changed_raw_row_weights=False,
  total_rows=1158250,physical_Fourier_rows=1157286,joint_boundary_rows=964,all_full_quadratic_Gram_modes=True,
  original_T_Pr_budget_changed=False,old_Pr_rows_used_in_objective=False,old_Pr_CU_used_for_acceleration=False,
  no_intermediate_Gram_monotonicity_requirement=True,no_moments_or_cached_LSMR_or_cached_physical_repetition=True,
  finite_LSMR_stop_not_automatically_converged=True,all_directions_saved=True,
  resume='same source/policy/base hashes; consume durable completed direction/evaluation; restart only unfinished call at same index/damp, record partial work')
 checkpoint_path=a.out.with_suffix('.checkpoint.json');active_path=a.out.with_suffix('.active.json')
 source_base=p.binary_sha(P.Y,P.U);partial_runs=[];history=[];failure=None;J=None;A=None
 active={};state_file=None;state_sha=None
 def activate(stage,**kw):
  nonlocal active
  active=dict(schema='complete-full-Gram-integrated-LM-active-call-v1',source_sha256=source_sha,invocation=invocation,
   stage=stage,unix_time=time.time(),elapsed_current_invocation=time.perf_counter()-start,**kw)
  write(active_path,active)
 def state_archive():
  nonlocal state_file,state_sha
  state_file=a.work/f'accepted-{accepted:03d}.npz'
  if state_file.exists():
   with np.load(state_file,allow_pickle=False)as d:
    if not np.array_equal(d['Y'],Y)or not np.array_equal(d['U'],U):raise ValueError('Immutable accepted archive collision')
  else:save_npz(state_file,Y=Y,U=U)
  state_sha=sha(state_file)
 def checkpoint():
  data=dict(schema='complete-full-Gram-integrated-LM-checkpoint-v1',source_sha256=source_sha,identities=identities,
   original_warm_sha256=p.WARM_SHA,policy=policy,accepted_parent=False,accepted_algebraic_steps=accepted,
   directions_used=directions,damp_next=damp,history=history,partial_runs=partial_runs,failure=failure,
   state_archive=str(state_file),state_archive_sha256=state_sha,state_YU_sha256=p.binary_sha(Y,U),
   residual_summary=summary(R),mesh_sha256=p.binary_sha(P.x),elapsed_current_invocation=time.perf_counter()-start,
   current_invocation=invocation,active_path=str(active_path))
  write(checkpoint_path,data)
 def bound_record(record,index,base_sha):
  if record.get('source_sha256')!=source_sha or record.get('direction_index')!=index or record.get('base_YU_sha256')!=base_sha or record.get('damp')!=damp:
   raise ValueError('Stored direction/evaluation identity mismatch')
  if record.get('base_state_archive_sha256')!=state_sha:raise ValueError('Stored direction has another accepted base archive')
  f=record.get('direction_file')
  if f and sha(f)!=record['direction_file_sha256']:raise ValueError('Stored direction bytes changed')
 def get_delta(record):
  with np.load(record['direction_file'],allow_pickle=False)as d:
   z=d['z'].copy()
   if record.get('physical_direction_defined')is False:
    if z.shape!=(2*n,):raise ValueError('Wrong saved LSMR direction shape')
    return z,None,None
   dY=d['dY'].copy();dU=d['dU'].copy()
  if z.shape!=(2*n,)or dY.shape!=Y.shape or dU.shape!=U.shape:raise ValueError('Wrong saved complete direction shapes')
  if p.binary_sha(dY,dU)!=record['direction_binary_sha256']:raise ValueError('Saved physical direction identity changed')
  return z,dY,dU

 if a.resume:
  if a.prepare_only:raise ValueError('prepare-only cannot resume')
  saved=read(checkpoint_path)
  if saved.get('source_sha256')!=source_sha or saved.get('identities')!=identities or saved.get('policy')!=policy or saved.get('original_warm_sha256')!=p.WARM_SHA:raise ValueError('Resume source/policy/identities changed')
  if saved['mesh_sha256']!=p.binary_sha(P.x):raise ValueError('Resume mesh changed')
  state_file=Path(saved['state_archive']);state_sha=saved['state_archive_sha256']
  if sha(state_file)!=state_sha:raise ValueError('Resume accepted archive changed')
  with np.load(state_file,allow_pickle=False)as d:Y=d['Y'].copy();U=d['U'].copy()
  if p.binary_sha(Y,U)!=saved['state_YU_sha256']:raise ValueError('Resume Y/U identity mismatch')
  R=evaluate(Y,U)
  if summary(R)!=saved['residual_summary']:raise ValueError('Resume raw residual changed')
  history=saved['history'];accepted=saved['accepted_algebraic_steps'];directions=saved['directions_used'];damp=saved['damp_next'];failure=saved['failure'];partial_runs=saved['partial_runs']
  if len(history)!=directions or sum(bool(h.get('accepted'))for h in history)!=accepted or [h['direction_index']for h in history]!=list(range(directions)):
   raise ValueError('Resume completed logical budget is inconsistent')
  if not(1<=accepted<=MAX_ACCEPTED and accepted<=directions<=MAX_DIRECTIONS):raise ValueError('Resume budget outside original limits')
  for record in history:
   if record.get('direction_file'):
    if sha(record['direction_file'])!=record['direction_file_sha256']:raise ValueError('Completed direction bytes changed')
   elif not record.get('failure'):raise ValueError('Completed direction lacks saved arrays or explicit failure')
  if active_path.exists():
   old=read(active_path)
   if old.get('source_sha256')!=source_sha:raise ValueError('Active source changed')
   idx=old.get('direction_index');ready=a.work/f'direction-{directions:03d}.ready.json';evaluation=a.work/f'direction-{directions:03d}.evaluation.json'
   if idx==directions and old.get('stage')not in ('idle','terminal_complete'):
    partial_runs.append(dict(prior_active=old,restarted_direction_index=directions,
     completed_direction_reused=ready.exists(),completed_evaluation_reused=evaluation.exists(),
     unfinished_LSMR_may_repeat=not ready.exists()and not evaluation.exists(),
     known_action_counts_are_lower_bounds=True,reason='explicit same-budget executor recovery; no mathematical failure inferred'))
  checkpoint();emit(event='full_Gram_LM_resume',directions_completed=directions,accepted_steps=accepted,damp_next=damp,
   raw_SSE=R['cost'],partial_runs=len(partial_runs),source_sha256=source_sha)
 else:
  if checkpoint_path.exists()or a.out.exists()or any(a.work.glob('accepted-*.npz')):raise ValueError('Existing budget state; use --resume, do not refresh limits')
  with np.load(a.first_direction,allow_pickle=False)as d:
   if not np.array_equal(d['Y'],P.Y)or not np.array_equal(d['U'],P.U):raise ValueError('Cached direction0 not original1662')
   Y=P.Y+d['dY'];U=P.U+d['dU']
  if p.binary_sha(Y,U)!=first['candidate_YU_sha256']:raise ValueError('Cached audit is for another candidate')
  R=evaluate(Y,U)
  if summary(R)!=first['actual_trial_full_Gram']:raise ValueError('Cached complete residual changed')
  initial=first['initial_full_Gram'];cost0=initial['raw_SSE'];pred0=cost0-first['linear_model_SSE'];ratio0=(cost0-R['cost'])/pred0
  physical0=first['full_physical_sample_audit']
  if not(R['finite']and pred0>0 and ratio0>=ETA and R['cost']<cost0 and maximum(R['boundary'])<=p.BC_TOL and np.array_equal(U[0],pr.core_target(P))and maximum(R['core_velocity'])==0. and physical0['finite']and physical0['all_sampled_domain_and_branch_positive']):raise ValueError('Cached zero fails original acceptance rule')
  if (physical0['angles'],physical0['node_count'],physical0['midpoint_count'])!=(8192,602,601):raise ValueError('Incomplete cached branch audit')
  history=[dict(source_sha256=source_sha,direction_index=0,cached=True,accepted=True,base_YU_sha256=source_base,
   candidate_YU_sha256=p.binary_sha(Y,U),damp=1.,predicted_reduction=pred0,actual_reduction=cost0-R['cost'],ratio=ratio0,
   residual_before=initial,residual_after=summary(R),lsmr_return=first['LSMR'],
   explicit_regularized_normal_residual_L2=first['explicit_regularized_normal_L2'],
   explicit_regularized_normal_residual_relative=first['explicit_regularized_normal_relative'],
   direction_file=str(a.first_direction),direction_file_sha256=DIRECTION_SHA,physical=physical0,cached_report_sha256=FIRST_REPORT_SHA)]
  accepted=1;directions=1;damp=.5 if ratio0>.75 else(2. if ratio0<.25 else 1.)
  preparation=dict(schema='integrated-full-Gram-LM-budget-preparation-v1',source_sha256=source_sha,identities=identities,policy=policy,
   original_base_YU_sha256=source_base,cached_candidate_YU_sha256=p.binary_sha(Y,U),cached_zero_raw_SSE=R['cost'],
   cached_zero_accepted_by_original_rules=True,cached_direction_recomputed=False,cached_physical_audit_recomputed=False,
   prepared_moments_recomputed=False,new_LSMR_executed=False,accepted_parent=False,seconds=time.perf_counter()-start)
  write(a.out.with_suffix('.preparation.json'),preparation)
  emit(event='full_Gram_LM_prepared',source_sha256=source_sha,preparation=str(a.out.with_suffix('.preparation.json')),
   preparation_sha256=sha(a.out.with_suffix('.preparation.json')),policy=policy)
  if a.prepare_only:return
  state_archive();checkpoint();activate('idle',directions_completed=directions,accepted_steps=accepted)
  emit(event='full_Gram_LM_start_cached_zero',accepted=accepted,directions=directions,damp_next=damp,raw_SSE=R['cost'],
   cached_report_sha256=FIRST_REPORT_SHA,candidate_YU_sha256=p.binary_sha(Y,U))

 while failure is None and directions<MAX_DIRECTIONS and accepted<MAX_ACCEPTED and not converged():
  p.assert_sources(identities);index=directions;base_sha=p.binary_sha(Y,U);attempt_start=time.perf_counter()
  direction_file=a.work/f'direction-{index:03d}.npz';ready_path=a.work/f'direction-{index:03d}.ready.json';evaluation_path=a.work/f'direction-{index:03d}.evaluation.json'
  call_id=invocation+':'+str(index)
  def phase(stage,**kw):activate(stage,direction_index=index,base_YU_sha256=base_sha,base_state_archive_sha256=state_sha,
   damp=damp,call_id=call_id,attempt_seconds=time.perf_counter()-attempt_start,**kw)
  record=None
  if evaluation_path.exists():
   record=read(evaluation_path);bound_record(record,index,base_sha)
   emit(event='full_Gram_LM_reuse_completed_evaluation',direction_index=index,evaluation_sha256=sha(evaluation_path))
  else:
   if ready_path.exists():
    record=read(ready_path);bound_record(record,index,base_sha);z,dY,dU=get_delta(record)
    emit(event='full_Gram_LM_reuse_completed_LSMR',direction_index=index,direction_file_sha256=record['direction_file_sha256'])
   else:
    phase('linear_setup')
    if J is None:J=Aug(P,Y,U)
    raw=pr.flatten(R);d0=bc.affine(R['boundary'],R['core_velocity']);b=-(raw+J.matvec(d0));calls=[0,0];in_solve=True
    def mv(z):
     calls[0]+=1;value=J.matvec(bc.lift(z))
     if in_solve and calls[0]%16==0:
      phase('LSMR',matvecs=calls[0],rmatvecs=calls[1]);emit(event='full_Gram_LM_linear_progress',direction_index=index,damp=damp,
       matvecs=calls[0],rmatvecs=calls[1],seconds=time.perf_counter()-attempt_start)
     return value
    def rmv(w):calls[1]+=1;return bc.pullback(J.rmatvec(w))
    A=LinearOperator(J.shape,matvec=mv,rmatvec=rmv,dtype=float);phase('LSMR',matvecs=0,rmatvecs=0)
    try:sol=lsmr(A,b,damp=damp,atol=ATOL,btol=BTOL,conlim=CONLIM,maxiter=MAXITER,show=False)
    except Exception as exc:
     failure=dict(direction_index=index,stage='LSMR',type=type(exc).__name__,message=str(exc))
     record=dict(source_sha256=source_sha,direction_index=index,accepted=False,damp=damp,base_YU_sha256=base_sha,
      base_state_archive_sha256=state_sha,failure=failure,LSMR_action_counts=calls.copy(),residual_before=summary(R),seconds=time.perf_counter()-attempt_start)
     write(evaluation_path,record)
    else:
     in_solve=False;z=sol[0];solve_calls=calls.copy();phase('LSMR_returned_arrays_pending',matvecs=calls[0],rmatvecs=calls[1],lsmr_return=clean_info(sol))
     dY=None;dU=None;lift_error=None
     if np.isfinite(z).all():
      try:
       with np.errstate(over='ignore',invalid='ignore'):delta=d0+bc.lift(z)
       dY=delta[:n].reshape(P.m,P.n);dU=delta[n:].reshape(P.m,P.n)
      except (ValueError,FloatingPointError)as exc:lift_error=dict(type=type(exc).__name__,message=str(exc))
     if dY is None:save_npz(direction_file,z=z)
     else:save_npz(direction_file,dY=dY,dU=dU,z=z)
     record=dict(source_sha256=source_sha,direction_index=index,cached=False,base_YU_sha256=base_sha,
      base_state_archive=str(state_file),base_state_archive_sha256=state_sha,damp=damp,lsmr_return=clean_info(sol),
      LSMR_action_counts=solve_calls,residual_before=summary(R),direction_file=str(direction_file),direction_file_sha256=sha(direction_file),
      physical_direction_defined=dY is not None,lift_error=lift_error,direction_binary_sha256=p.binary_sha(dY,dU)if dY is not None else None,
      delta_Y_max=maximum(dY)if dY is not None and np.isfinite(dY).all()else None,
      delta_U_max=maximum(dU)if dU is not None and np.isfinite(dU).all()else None,LSMR_and_save_seconds=time.perf_counter()-attempt_start)
     write(ready_path,record);phase('direction_saved',ready_sha256=sha(ready_path),direction_sha256=record['direction_file_sha256'])
   if failure is None:
    # A ready record is durable before any merit/physical evaluation. Reusing
    # it never repeats its LSMR; J reconstruction is only a linearization cache.
    rejection=None
    if not np.isfinite(z).all():rejection='nonfinite_LSMR_direction'
    elif dY is None:rejection='undefined_lifted_direction'
    elif not(np.isfinite(dY).all()and np.isfinite(dU).all()):rejection='nonfinite_lifted_direction'
    if rejection is None:
     if J is None:J=Aug(P,Y,U)
     raw=pr.flatten(R);d0=bc.affine(R['boundary'],R['core_velocity']);b=-(raw+J.matvec(d0));delta=np.r_[dY.ravel(),dU.ravel()]
     linear=raw+J.matvec(delta);linear_SSE=float(mf.inner(linear,linear));pred=R['cost']-linear_SSE
     if not np.isfinite(linear).all()or not math.isfinite(linear_SSE):rejection='nonfinite_linear_model'
     else:
      normal=bc.pullback(J.rmatvec(linear))+damp*damp*z;normal_denom=max(norm(bc.pullback(J.rmatvec(b))),np.finfo(float).tiny)
      if not np.isfinite(normal).all()or not math.isfinite(normal_denom):rejection='nonfinite_regularized_normal_residual'
      else:record.update(linear_model_SSE=linear_SSE,predicted_reduction=pred,regularization_penalty=float(damp*damp*mf.inner(z,z)),
       explicit_regularized_normal_residual_L2=norm(normal),explicit_regularized_normal_residual_relative=norm(normal)/normal_denom,
       original_BC_linear_residual_max=maximum(linear[-2*P.n:-P.n]),core_U0_linear_residual_max=maximum(linear[-P.n:]))
    if rejection is not None:record.update(accepted=False,rejection=rejection,seconds=time.perf_counter()-attempt_start)
    else:
     phase('actual_full_residual');yn=Y+dY;un=U+dU;rn=evaluate(yn,un)
     finite=rn['finite']and math.isfinite(pred);ratio=(R['cost']-rn['cost'])/pred if finite and pred>0 else None
     if ratio is not None and not math.isfinite(ratio):ratio=None
     merit=bool(finite and pred>0 and ratio is not None and ratio>=ETA and rn['cost']<R['cost']and maximum(rn['boundary'])<=p.BC_TOL and maximum(rn['core_velocity'])==0. and np.array_equal(un[0],pr.core_target(P)))
     physical=None;ok=False
     if merit:
      phase('physical8192',candidate_YU_sha256=p.binary_sha(yn,un));physical=P.physical_samples(yn,un)
      ok=bool(physical.get('finite')and physical.get('all_sampled_domain_and_branch_positive'))
     record.update(accepted=ok,ratio=ratio,residual_trial=summary(rn),candidate_YU_sha256=p.binary_sha(yn,un),physical=physical,
      rejection=None if ok else('physical_branch_gate'if merit else'full_Gram_merit_or_joint_BC_gate'),seconds=time.perf_counter()-attempt_start)
    write(evaluation_path,record);phase('evaluation_saved',evaluation_sha256=sha(evaluation_path))
  # This commit is identical for new work or a recovered durable evaluation.
  if record.get('failure'):failure=record['failure']
  history.append(record);directions+=1
  if record.get('accepted'):
   z,dY,dU=get_delta(record);Y=Y+dY;U=U+dU
   if p.binary_sha(Y,U)!=record['candidate_YU_sha256']:raise ValueError('Accepted update bytes changed')
   R=evaluate(Y,U)
   if summary(R)!=record['residual_trial']:raise ValueError('Accepted complete residual changed')
   accepted+=1;ratio=record['ratio']
   if ratio>.75:damp/=2
   elif ratio<.25:damp*=2
   J=None;A=None;state_archive()
  elif failure is None:damp*=2
  checkpoint();activate('idle',directions_completed=directions,accepted_steps=accepted)
  if record.get('accepted'):
   physical=record['physical'];emit(event='full_Gram_LM_accept',direction_index=index,accepted_steps=accepted,directions_used=directions,
    damp_next=damp,raw_SSE=R['cost'],ratio=record['ratio'],node_max=maximum(R['nodes']),midpoint_max=maximum(R['middle']),BC_max=maximum(R['boundary']),
    physical_H_min=physical['domain_minima']['H']['value'],physical_normal_min=physical['domain_minima']['positive_branch_normal_velocity']['value'],
    actual_cubic_Gram=physical['actual_common_cubic_Gram_max'],lsmr=record['lsmr_return'],normal_relative=record['explicit_regularized_normal_residual_relative'],seconds=record['seconds'])
  else:emit(event='full_Gram_LM_reject_or_failure',direction_index=index,directions_used=directions,damp_next=damp,
   reason=record.get('rejection'),failure=record.get('failure'),trial=record.get('residual_trial'),lsmr=record.get('lsmr_return'))

 if failure is not None:reason='linear_exception_retained_previous_accepted_state'
 elif converged():reason='full_Gram_joint_BC_and_sampled_metric_gates_met'
 elif accepted>=MAX_ACCEPTED:reason='fixed20accepted_budget'
 else:reason='fixed24direction_budget'
 J=None;A=None;p.assert_sources(identities)
 last_accepted=next(r for r in reversed(history)if r.get('accepted'))
 if last_accepted['candidate_YU_sha256']!=p.binary_sha(Y,U):raise ValueError('Final audit is not the final accepted state')
 physical=last_accepted['physical'];p.assert_sources(identities)
 result=dict(schema='independent-YU-full-polynomial-Gram-finite-attempt-v1',scope=__doc__,source_sha256=source_sha,identities=identities,
  M=P.M,N=P.N,dimension_Y=P.n,dimension_U=P.n,nodes=P.m,mesh=P.x.tolist(),states=Y.tolist(),independent_velocities=U.tolist(),
  full_Gram_scalar_dimension=6*P.M+2,nodes_full_Gram_coefficients=R['nodes'].tolist(),midpoint_full_Gram_coefficients=R['middle'].tolist(),
  original_position_boundary_residual=R['boundary'].tolist(),core_velocity_residual=R['core_velocity'].tolist(),residual_summary=summary(R),
  finite_algebraic_converged=algebraic_converged(R,U),all_frozen_terminal_gates_met=converged(),termination=reason,failure=failure,original_explicit_BVP_accepted=False,accepted_parent=False,
  full_Newton_executed=False,full_LM_executed=True,integrated_T_coordinates=True,policy=policy,accepted_algebraic_steps=accepted,
  directions_used=directions,damp_next=damp,partial_runs=partial_runs,terminal_physical_audit_reused_from_direction=last_accepted['direction_index'],
  unchanged_boundary=dict(left_count=P.nl,right_count=P.n-P.nl,rows=P.BB[P.nl:].tolist(),target=P.target[P.nl:].tolist(),arrays_sha256=p.binary_sha(P.BA,P.BB,P.target)),
  fixed_scalar_profile=P.metadata['fixed_scalar_profile'],analytic_extension_origin=P.metadata['analytic_extension_origin'],hold_scalar_profile=P.metadata['hold_scalar_profile'],hold_profile_sha256=p.HOLD_SHA,
  scalar_nodes=dict(a=P.scalar_nodes[:,0].tolist(),ap=P.scalar_nodes[:,1].tolist(),app=P.scalar_nodes[:,2].tolist(),k=P.k.tolist(),k_prime=P.kprime.tolist()),
  core=dict(coefficients=Y[0,1:P.M+1].tolist(),fixed_first_three=P.metadata['fixed_core_first_three'],axis_support_gap=float(2*np.sum(Y[0,1:P.M+1:2])),
   U0_literal_ez=bool(np.array_equal(U[0],pr.core_target(P))),position_Z_nonzero=int(np.count_nonzero(Y[0,2*P.M+1:])),position_Z_max=maximum(Y[0,2*P.M+1:])),
  history=history,physical_sample_audit=physical,full_Gram_counts_current_invocation=gram_counts,
  physical_reader_ancillary_Pr_fields_not_used_in_objective=True,common_C2_reconstruction_paid=False,
  old_Pr_CU_acceleration_not_defined=True,continuous_geometry_certified=False,
  cubic_solver_field_regularity='C1 and piecewise cubic; no automatic C2 assertion',old_cut_jets_not_fabricated=True,
  seconds=time.perf_counter()-start,seconds_scope='current invocation only; completed per-direction times and partial-run evidence retained separately',maximum_RSS_kib=rss())
 field=a.out.with_suffix('.field.json.gz');write_bytes(field,gzip.compress((json.dumps(result,allow_nan=False)+'\n').encode(),mtime=0))
 report={k:v for k,v in result.items()if k not in ('mesh','states','independent_velocities','nodes_full_Gram_coefficients','midpoint_full_Gram_coefficients','original_position_boundary_residual','core_velocity_residual','fixed_scalar_profile','scalar_nodes','unchanged_boundary','core')}
 report.update(field_path=str(field),field_sha256=sha(field),core={k:v for k,v in result['core'].items()if k!='coefficients'})
 write(a.out,report);activate('terminal_complete',directions_completed=directions,accepted_steps=accepted,report_sha256=sha(a.out),field_sha256=sha(field))
 emit(event='full_Gram_LM_terminal',report=str(a.out),report_sha256=sha(a.out),field=str(field),field_sha256=sha(field),
  termination=reason,accepted_steps=accepted,directions=directions,**summary(R),physical=physical,all_frozen_terminal_gates_met=converged(),seconds=report['seconds'],maximum_RSS_kib=rss())

if __name__=='__main__':
 a=argparse.ArgumentParser(description=__doc__)
 for key in ('topic','problem-source','warm','polynomial-source','matrix-source','coordinate-source','gram-source','preparation-source','prepared','preparation-report','first-direction','first-report','work','out'):a.add_argument('--'+key,type=Path,required=True)
 a.add_argument('--prepare-only',action='store_true');a.add_argument('--resume',action='store_true');main(a.parse_args())
