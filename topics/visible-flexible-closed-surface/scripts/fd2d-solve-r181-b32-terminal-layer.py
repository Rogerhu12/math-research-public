#!/usr/bin/env python3
"""Optional terminal-resolved B32 finite-amplitude solve, with explicit new g.

This source adds a declared terminal P1 mesh and finite initializer to the
published recovery driver. It was saved during the executor outage and
has not been executed; it does not claim the analytic screen is this field.

Full angular node/Gauss-point rows come from the new physical-point
objective. A local normal is accumulated without a tall whole Jacobian.
Only its block-tridiagonal field part and small parameter Schur system
are solved. All trial fields are re-evaluated at the same full finite
objective. A finite result is not an exact immersion or strong certificate.
"""
from __future__ import annotations
import os
for _thread_name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_thread_name]='1'
import argparse,itertools,json,time,traceback
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.sparse.linalg import splu
from scipy.optimize import minimize,LinearConstraint,Bounds
from fd2d_gc_archive_arrays import identity
from fd2d_gc_r181_b_round_raw_recovery import (
    R181BRecoveryRoundRawBumpDAE,checkpoint_arrays,DEFAULT_CANDIDATE,REPRESENTATION)
from fd2d_gc_r181_b_point_objective_recovery import (
    RoundB32PointObjective,small_gap_parameter_certificate)
from fd2d_gc_r181_b_finite_seed_recovery import restore_gap_on_first_mode
from fd2d_gc_r181_b_terminal_layer_seed import (
    create_layer_resolved_problem,finite_terminal_layer_seed)


def jsonable(value):
    if isinstance(value,np.ndarray):return value.tolist()
    if isinstance(value,np.generic):return value.item()
    if isinstance(value,Path):return str(value)
    if isinstance(value,Fraction):return str(value)
    if isinstance(value,dict):return {str(k):jsonable(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [jsonable(v) for v in value]
    return value


def write_json_atomic(path,value):
    path=Path(path);temporary=path.with_name('.'+path.name+'.tmp')
    raw=(json.dumps(jsonable(value),sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
    with temporary.open('wb') as out:
        out.write(raw);out.flush();os.fsync(out.fileno())
    os.replace(temporary,path)


def save_field(path,problem,z):
    path=Path(path)
    if path.exists():raise FileExistsError(path)
    temporary=path.with_name('.'+path.name+'.tmp')
    with temporary.open('wb') as out:
        np.savez_compressed(out,**checkpoint_arrays(problem,z))
        out.flush();os.fsync(out.fileno())
    os.replace(temporary,path)
    return identity(path)


def parameter_constraints(problem,p,scale,*,profile_box=.08):
    P=problem.parameter_count;matrices=[];lower=[];upper=[]
    # All sign rows express the continuous sufficient central l1 domain.
    signs=np.asarray(list(itertools.product((-1.,1.),repeat=problem.K)))
    block=np.zeros((len(signs),P));block[:,problem.central_slice]=signs*scale[problem.central_slice]
    cap=float((Fraction(200,201)-Fraction(1,10))/2)
    matrices.append(block);lower.extend([-np.inf]*len(signs))
    upper.extend(cap-signs@p[problem.central_slice])
    tail=problem.tail_control_box.linear_constraints(p[problem.tail_slice])
    block=np.zeros((len(tail['lower']),P))
    block[:,problem.tail_slice]=tail['matrix']*scale[problem.tail_slice]
    matrices.append(block);lower.extend(tail['lower']);upper.extend(tail['upper'])
    dom=problem.profile_domain
    block=np.zeros((len(dom['lower']),P))
    block[:,problem.profile_slice]=dom['matrix']*scale[problem.profile_slice]
    matrices.append(block)
    lower.extend(dom['lower']-dom['matrix']@p[problem.profile_slice])
    upper.extend([np.inf]*len(dom['lower']))
    A=np.vstack(matrices)
    constraints=[LinearConstraint(A,np.asarray(lower),np.asarray(upper))]
    _,axes=problem.core(p[problem.central_slice])
    gap=np.zeros(P);gap[problem.central_slice]=np.asarray(axes['gap_jacobian'],float)*scale[problem.central_slice]
    rhs=problem.gap-float(axes['gap'])
    constraints.append(LinearConstraint(gap[None,:],[rhs],[rhs]))
    # These are explicit finite trust boxes; the actual domain is checked
    # exactly after forming every new physical parameter vector.
    trust=np.r_[np.full(problem.K,.05),np.full(16,.1),np.full(problem.J,.003)]
    low=-trust;high=trust
    section=problem.profile_slice
    low[section]=np.maximum(low[section],-float(profile_box)-p[section])
    high[section]=np.minimum(high[section],float(profile_box)-p[section])
    return constraints,Bounds(low/scale,high/scale),dict(
        central_l1_cap=cap,tail_rows=len(tail['lower']),
        profile_rows=len(dom['lower']),linear_gap_right_side=rhs,
        physical_step_trust=trust.tolist(),absolute_profile_box=float(profile_box))


def normal_direction(problem,z,normal,damping,*,profile_box=.08):
    _,p=problem.unpack(z);scaled=normal.scaled(damping)
    factor=splu(scaled['hff'])
    rhs=np.c_[scaled['gf'],scaled['hfp']]
    solved=factor.solve(rhs)
    ig,ic=solved[:,0],solved[:,1:]
    S=scaled['hpp']-scaled['hfp'].T@ic
    S=(S+S.T)/2
    g=scaled['gp']-scaled['hfp'].T@ig
    eigen=np.linalg.eigvalsh(S)
    extra=max(0.,1e-12-float(eigen[0]))
    if extra:S=S+np.eye(len(g))*extra
    constraints,bounds,domain=parameter_constraints(problem,p,scaled['parameter_scale'],
        profile_box=profile_box)
    f=lambda q:.5*float(q@(S@q))+float(g@q)
    jac=lambda q:S@q+g
    answer=minimize(f,np.zeros(problem.parameter_count),jac=jac,method='SLSQP',
        constraints=constraints,bounds=bounds,
        options=dict(ftol=1e-11,maxiter=300,disp=False))
    if not np.all(np.isfinite(answer.x)):raise FloatingPointError('Nonfinite small parameter direction')
    vp=scaled['parameter_scale']*answer.x
    vf=scaled['field_scale']*(-ig-ic@answer.x)
    direction=normal.mapping.expand(vf,vp)
    # The scalar gap is re-solved explicitly at each trial below, so this
    # optional whole-direction scaling does not silently lose its target.
    rawmax=float(np.max(abs(direction[:problem.N*problem.q]),initial=0.))
    trust_scale=min(1.,2/max(rawmax,np.finfo(float).tiny))
    direction*=trust_scale
    reduced_f=direction[normal.mapping.free]
    reduced_p=direction[normal.mapping.total:]
    gradient=float(normal.gf@reduced_f+normal.gp@reduced_p)
    return direction,dict(qp_success=bool(answer.success),qp_status=int(answer.status),
        qp_message=str(answer.message),qp_iterations=int(answer.nit),
        parameter_schur_min_eigen_before_shift=float(eigen[0]),
        parameter_schur_extra_diagonal=extra,damping=float(damping),
        direction_maximum=float(np.max(abs(direction))),raw_trust_scale=trust_scale,
        actual_linear_gradient=gradient,parameter_constraints=domain,
        parameter_direction=direction[-problem.parameter_count:].tolist(),
        field_factor_dimension=int(scaled['hff'].shape[0]),
        tall_whole_J_constructed=False)


def read_restart(problem,path):
    with np.load(path,allow_pickle=False) as source:
        if str(source['representation_kind'])!=REPRESENTATION:
            raise ValueError('A previous new recovery representation is required')
        if int(source['modes'])!=problem.K or int(source['tail_parameter_count'])!=16:
            raise ValueError('Explicit new angular/tail layout mismatch')
        if not np.array_equal(source['mesh'],problem.x):
            raise ValueError('Do not silently remesh a restart')
        if not np.array_equal(source['profile_supports'],problem.profile.supports):
            raise ValueError('Actual new physical supports differ')
        z=np.r_[source['corrections'].ravel(),source['parameters']]
    return problem.impose_linear_boundary_values(z)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--candidate',type=Path,default=DEFAULT_CANDIDATE)
    ap.add_argument('--restart',type=Path)
    ap.add_argument('--modes',type=int,default=7)
    ap.add_argument('--gap',type=float,default=.05)
    ap.add_argument('--gap-scale',type=float,default=.64)
    ap.add_argument('--max-step',type=float,default=.04)
    ap.add_argument('--accepted-limit',type=int,default=4)
    ap.add_argument('--attempts',type=int,default=12)
    ap.add_argument('--damping',type=float,default=1e-4)
    ap.add_argument('--profile-box',type=float,default=.08)
    ap.add_argument('--tail-amplitude',type=float)
    ap.add_argument('--terminal-layer-width',type=float,default=.002)
    ap.add_argument('--finite-tolerance',type=float,default=1e-6)
    args=ap.parse_args()
    if not 1<=args.modes<=7:
        raise ValueError('This initial bounded solve explicitly limits the all-sign central QP to K<=7')
    if args.accepted_limit<1 or args.attempts<1 or args.gap<=0:
        raise ValueError('Specify a nonzero finite gap and a real short batch')
    prefix=args.out_prefix;prefix.parent.mkdir(parents=True,exist_ok=True)
    report_path=Path(str(prefix)+'-report.json')
    if report_path.exists():raise FileExistsError(report_path)
    started=time.perf_counter()
    problem=create_layer_resolved_problem(args.candidate,modes=args.modes,
        gap=args.gap,gap_scale=args.gap_scale,max_step=args.max_step,base_kind='circle',
        terminal_layer_width=args.terminal_layer_width)
    objective=RoundB32PointObjective(problem,order=2,point_batch=8)
    if args.restart:
        z=read_restart(problem,args.restart)
        yy,pp=problem.unpack(z)
        pp[:],seed_info=restore_gap_on_first_mode(problem,pp,problem.gap)
        z=problem.impose_linear_boundary_values(z)
        seed_info=dict(restart=identity(args.restart),finite_gap_restore=seed_info)
    else:z,seed_info=finite_terminal_layer_seed(problem,tail_amplitude=args.tail_amplitude)
    domain=small_gap_parameter_certificate(problem,z,profile_box=args.profile_box)
    if not domain['passed']:raise ValueError('Initial actual field parameters violate the exact domain')
    initial_path=Path(str(prefix)+'-initial.npz')
    initial_identity=save_field(initial_path,problem,z)
    value,_=objective.consume(z,jacobian=False)
    history=[];accepted=[];damping=args.damping;finite_success=False
    report=dict(schema='fd2d-R181-B32-terminal-layer-actual-finite-short-solve-v1',
        source=identity(__file__),candidate=identity(args.candidate),
        arguments=vars(args),representation=problem.definition(),
        objective=objective.definition(),initializer=seed_info,
        initial=initial_identity,initial_value=value,history=history,accepted=accepted,
        whole_body_run=False,exact_C2_immersion_or_reach_claimed=False,
        nonround_branch_existence_assumed=False)
    write_json_atomic(report_path,dict(report,state='running',seconds=time.perf_counter()-started))
    print(json.dumps(dict(event='initial',norm=value['norm'],gap=value['actual_gap'],
        full_G=value['full_finite_Gauss_maximum'],full_C=value['full_finite_Codazzi_maximum'],
        node_count=problem.N,parameters=problem.parameter_count)),flush=True)
    try:
        for attempt in range(1,args.attempts+1):
            if (value['norm']<=args.finite_tolerance and
                    value['full_finite_Gauss_maximum']<=20*args.finite_tolerance and
                    value['full_finite_Codazzi_maximum']<=20*args.finite_tolerance and
                    abs(value['actual_gap']-problem.gap)<=args.finite_tolerance):
                finite_success=True;break
            before,normal=objective.consume(z,jacobian=True)
            mismatch=abs(before['residual_squared']-value['residual_squared'])
            if mismatch>1e-10*max(1.,value['residual_squared']):
                raise ArithmeticError('Actual no-J and same finite normal values differ')
            direction,choice=normal_direction(problem,z,normal,damping,profile_box=args.profile_box)
            record=dict(attempt=attempt,before=before,direction=choice,trials=[])
            taken=False
            for power in range(12):
                alpha=2.**(-power);trial=z+alpha*direction
                y,p=problem.unpack(trial)
                try:
                    repaired=None
                    if not problem.tail_control_box.certificate(p[problem.tail_slice])['passed']:
                        result=problem.tail_control_box.repair_toward_constant(p[problem.tail_slice])
                        p[problem.tail_slice]=result['controls'];repaired=result['info']
                    p[:],gap_restore=restore_gap_on_first_mode(problem,p,problem.gap)
                    trial=problem.impose_linear_boundary_values(trial)
                    certificate=small_gap_parameter_certificate(problem,trial,profile_box=args.profile_box)
                    if not certificate['passed']:
                        record['trials'].append(dict(alpha=alpha,domain_passed=False,
                            certificate=certificate,tail_projection=repaired,gap_restore=gap_restore))
                        continue
                    actual,_=objective.consume(trial,jacobian=False)
                    difference=trial-z
                    gradient=float(normal.gf@difference[normal.mapping.free]+normal.gp@difference[normal.mapping.total:])
                    threshold=value['residual_squared']+2e-4*min(0.,gradient)
                    accept=(actual['residual_squared']<value['residual_squared']
                        and actual['residual_squared']<=threshold)
                    row=dict(alpha=alpha,domain_passed=True,value=actual,
                        actual_projected_gradient=gradient,accepted=accept,
                        tail_projection=repaired,gap_restore=gap_restore)
                    record['trials'].append(row)
                    if accept:
                        z=trial;value=actual;taken=True
                        path=Path(str(prefix)+f'-accepted-{len(accepted)+1:04d}.npz')
                        ident=save_field(path,problem,z)
                        accepted.append(dict(field=ident,value=value,domain_certificate=certificate,
                            alpha=alpha,tail_projection=repaired,gap_restore=gap_restore))
                        damping=max(1e-9,damping*.4)
                        print(json.dumps(dict(event='accepted',number=len(accepted),attempt=attempt,
                            norm=value['norm'],gap=value['actual_gap'],
                            full_G=value['full_finite_Gauss_maximum'],
                            full_C=value['full_finite_Codazzi_maximum'],
                            formal_kappa=value['formal_curvature_samples_maximum'],
                            field_sha256=ident['sha256'])),flush=True)
                        break
                except (ValueError,FloatingPointError,OverflowError) as error:
                    record['trials'].append(dict(alpha=alpha,rejected_exception=type(error).__name__,message=str(error)))
            history.append(record)
            if not taken:damping=min(1e8,damping*10)
            write_json_atomic(report_path,dict(report,state='running',current=value,
                current_damping=damping,seconds=time.perf_counter()-started))
            if len(accepted)>=args.accepted_limit:break
        final_path=Path(str(prefix)+'-final.npz')
        final_identity=save_field(final_path,problem,z)
        report.update(state='natural_batch_end',current=value,final=final_identity,
            current_damping=damping,finite_convergence=finite_success,
            continuous_solution_claimed=False,accepted_count=len(accepted),
            seconds=time.perf_counter()-started)
        write_json_atomic(report_path,report)
        print(json.dumps(dict(event='natural_batch_end',accepted=len(accepted),
            norm=value['norm'],finite_convergence=finite_success,
            final_sha256=final_identity['sha256'],report=str(report_path))),flush=True)
    except BaseException as error:
        report.update(state='exception',current=value,exception=type(error).__name__,
            message=str(error),traceback=traceback.format_exc(),seconds=time.perf_counter()-started)
        write_json_atomic(report_path,report)
        raise


if __name__=='__main__':main()
