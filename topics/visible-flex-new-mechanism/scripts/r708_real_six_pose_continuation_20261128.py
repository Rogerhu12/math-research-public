#!/usr/bin/env python3
"""Continue the actual finite central R693/R697 target using all six R704 controls."""
import argparse
import json
import time
import numpy as np
from r688_actual_r664_window_collars import require_public
from r708_developable_shoulder_rod import D, UNIT, Rod, about_x, phase_center
from r708_developable_material_bounds import certificate, physical_output


def emit(kind, **fields):
    def encode(x):
        if isinstance(x,np.ndarray):
            return x.tolist()
        if isinstance(x,np.generic):
            return x.item()
        raise TypeError(type(x).__name__)
    print(json.dumps(dict(kind=kind,**fields),sort_keys=True,default=encode,allow_nan=False),flush=True)


def norm(v):
    return float(np.linalg.norm(v))


def retarget(rod,old,delta,newphase,sigma):
    # Left equivariance of the space-frame ODE around the original upper-seat axis.
    R=about_x(delta)
    end=old['end']@R.T
    end[0]+=D*UNIT[2]-R@(D*UNIT[2])
    jac=np.einsum('ij,tjk->tik',R,old['J'].reshape(4,3,6)).reshape(12,6)
    near,target=rod.endpoints(newphase,sigma)
    return dict(end=end,target=target,near=near,J=jac,residual=(end-target).ravel())


def snapshot(s):
    return {k:s[k] for k in ('end','target','near','J','residual')}


def main():
    require_public()
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-seconds',type=int,required=True)
    args=ap.parse_args()
    start=time.monotonic()
    elapsed=lambda: time.monotonic()-start
    rod=Rod()
    phase=0.;sigma=0.;q=np.zeros(6);answered=[];attempts=0;pending=None
    quick=None;physical=None
    try:
        h0,a0=phase_center(0.,True,rod.count)
        quick=rod.integrate(0.,sigma,q,columns=True,dense=True)
        gs=certificate(rod,q)
        if not gs['pass_strip'] or norm(quick['residual'])>2.e-11:
            raise ArithmeticError('The native six-column source did not reproduce the actual R704 arc.')
        independent=[]
        for idx in range(6):
            d=np.zeros(6);d[idx]=2.e-7
            plus=rod.integrate(0.,sigma,q+d,columns=False)['residual']
            minus=rod.integrate(0.,sigma,q-d,columns=False)['residual']
            independent.append(norm((plus-minus)/(2*d[idx])-quick['J'][:,idx])/norm(quick['J'][:,idx]))
        physical=physical_output(rod,phase,q,quick,h0)
        emit('actual_source',parameters=q,phase=phase,sigma=sigma,native_bump_integrals=rod.norm,
             separate_bump_integrals=rod.norm_check,source_read=snapshot(quick),
             source_singular_values=np.linalg.svd(quick['J'],compute_uv=False),all_six_central_difference_errors=independent,
             material_strip=gs,position_and_labels=physical,counts=dict(rod.count),seconds=elapsed())
        if max(independent)>2.e-5 or physical['maximum_join_jet_error']>2.e-10:
            raise ArithmeticError('One of the six spatial endpoint variations did not pass its independent source read.')
        step=.002
        why='full_phase'
        while phase<1.:
            if elapsed()>args.max_seconds-30:
                why='scientific_budget';break
            step=min(step,1.-phase)
            if step<2.e-10:
                why='next_requested_phase_increment_below_resolution';break
            attempts+=1
            aim=phase+step
            pending=dict(attempt=attempts,source_phase=phase,source_parameters=q.copy(),target_phase=aim,sigma=sigma)
            x=q.copy()
            state=retarget(rod,quick,step,aim,sigma)
            initial=norm(state['residual'])
            tol=max(2.e-13,min(1.e-10,step*2.e-5,initial*.0005))
            reason='newton_iteration_limit'
            ok=False
            for iteration in range(11):
                error=norm(state['residual'])
                pending.update(iteration=iteration,parameters=x.copy(),end_read=snapshot(state),residual_norm=error)
                if elapsed()>args.max_seconds-30:
                    reason='scientific_budget';break
                if error<tol and error<initial*.002:
                    material=certificate(rod,x)
                    pending['material_strip']=material
                    if not material['pass_strip']:
                        reason=material['reason'];break
                    fine=rod.integrate(aim,sigma,x,tight=True,columns=True,dense=True)
                    audit=norm(fine['residual'])
                    det=np.linalg.det(fine['end'][1:])
                    gram=norm(fine['end'][1:]@fine['end'][1:].T-np.eye(3))
                    variation=norm(fine['J']-state['J'])/max(norm(fine['J']),1.e-30)
                    pending.update(refined_residual_norm=audit,independent_full_J_relative=variation,
                                   refined_frame_determinant=det,refined_frame_Gram_defect=gram)
                    if audit>tol or gram>5.e-11 or det<=0 or variation>5.e-9:
                        reason='independent_end_pose_or_frame_difference';break
                    placed=physical_output(rod,aim,x,fine,h0)
                    if (max(placed['centerline_angle_checks'])>5.e-10 or
                            placed['centroid_independent_difference']>3.e-11 or placed['maximum_join_jet_error']>3.e-9):
                        reason='original_centerline_pose_disagreement';break
                    item=dict(phase=aim,sigma=sigma,controls=x.tolist(),end_residual=audit,
                              strip_curvature_upper=material['curvature_upper'],
                              material_jacobian_lower=material['minimum_jacobian_lower'],
                              strip_normal_ball_lower=material['all_pairs_strip_normal_ball_lower'])
                    answered.append(item)
                    phase,q,quick,physical=aim,x.copy(),fine,placed
                    emit('accepted_finite_central_pose',**item,attempt=attempts,material_strip=material,
                         actual_full_J_and_absolute_relative_end=snapshot(fine),native_labels_and_world_pose=placed,
                         six_singular_values=np.linalg.svd(fine['J'],compute_uv=False),
                         independent_full_J_relative=variation,counts=dict(rod.count),seconds=elapsed())
                    pending=None;ok=True
                    step=min(.1,step*1.65)
                    break
                U,s,Vh=np.linalg.svd(state['J'],full_matrices=False)
                if s[-1]<=0:
                    reason='singular_full_six_pose';break
                dx=-Vh.T@((U.T@state['residual'])/s)
                rod.count['all_six_newton_directions']+=1
                entered=False
                for bt in range(13):
                    trial=x+2.**(-bt)*dx
                    trial_read=rod.integrate(aim,sigma,trial,columns=False)
                    rod.count['value_only_end_trials']+=1
                    if norm(trial_read['residual'])<(1.-1.e-4*2.**(-bt))*error:
                        x=trial
                        state=rod.integrate(aim,sigma,x,columns=True)
                        rod.count['accepted_inner_Newton_trials']+=1
                        entered=True;break
                    rod.count['rejected_inner_Newton_trials']+=1
                if not entered:
                    reason='no_full_end_residual_descent';break
            if not ok:
                pending['reason']=reason
                emit('unaccepted_physical_phase',**pending,counts=dict(rod.count),seconds=elapsed())
                if reason=='scientific_budget':
                    why=reason;break
                step*=.40
        emit('terminal',status=why,last_accepted_phase=phase,last_parameters=q,sigma=sigma,
             accepted_phase_path=answered,next_phase_increment=step,tried_targets=attempts,
             last_accepted_actual_end=snapshot(quick),last_accepted_world_pose_and_labels=physical,
             pending_or_last_failed_target=pending,counts=dict(rod.count),scientific_seconds=elapsed(),
             global_fixed_metric_surface_verified=False,all_time_reach_verified=False,README_completion_claim=False)
    except Exception as exc:
        emit('incomplete',exception=type(exc).__name__,reason=str(exc),
             last_accepted_phase=phase,last_parameters=q,accepted_phase_path=answered,current_target=pending,
             last_base=None if quick is None else snapshot(quick),counts=dict(rod.count),seconds=elapsed())
        raise


if __name__=='__main__':
    main()
