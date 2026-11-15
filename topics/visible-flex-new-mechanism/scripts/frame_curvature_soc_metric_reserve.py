#!/usr/bin/env python3
"""Keep the SOC arc controller; reserve 1e-6 only in metric-row proposal RHS.

No physical gate, curvature prediction, box, height row, parameter or budget is
relaxed. The independently copied controller calls the new correction function;
no published module or process-global function is patched.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import inspect
from pathlib import Path
import time
import numpy as np
import scipy
from scipy.optimize import linprog
from frame_collar_residual_audit import digest
from frame_height_affine_gate import EvaluationBudgetReached, require_public_research_environment
from frame_curvature_epigraph_exchange import GROUPS
from frame_curvature_feasible_steps import linear_proposal, compact_decision
from frame_curvature_soc_arc_steps import (parabolic_candidate,curvature_arc_slack_bound,
    implementation_hashes as old_hashes,configuration as arc_configuration,
    run_soc_arc_steps as old_arc_controller,POLICY)
from frame_curvature_soc_steps import correction_proposal as old_correction_proposal

RESERVE_POLICY='same-budget-SOC-metric-row-reserve-v1'
FLOOR='1/1000000'


def implementation_hashes():
    result=old_hashes(); path=Path(__file__)
    result[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def configuration(base):
    cfg=arc_configuration(base)
    cfg.update(SOC_metric_row_reserve_policy=RESERVE_POLICY,SOC_metric_row_floor_exact=FLOOR,
        SOC_metric_reserve_group_indices=[0,1],SOC_metric_reserve_group_names=list(GROUPS[:2]),
        SOC_metric_reserve_is_not_an_eta_tolerance=True,
        SOC_other_physical_rows_and_curvature_retention_unchanged=True,
        old_primary_and_correction_LPs_and_all_original_gates_unchanged=False,
        only_failed_SOC_backtracking_curve_changed=False,
        original_primary_LP_and_arc_controller_and_actual_gates_unchanged=True,
        only_SOC_metric_proposal_RHS_changed=True)
    return cfg


def physical_margin_targets(base_rows,groups,cfg):
    """Return row-unit proposal targets; no change to real row evaluations."""
    base=np.asarray(base_rows,float); group=np.asarray(groups,int)
    gamma=float(Q(cfg['SOC_physical_margin_retention_exact']))
    floor=Q(cfg['SOC_metric_row_floor_exact'])
    if (base.ndim!=1 or group.shape!=base.shape or not np.all(np.isfinite(base))
            or np.any(group<0) or np.any(group>=len(GROUPS)) or not 0<=gamma<=1 or floor!=Q(FLOOR)):
        raise ValueError('finite original groups, margin fraction, and exact metric row floor 1/1000000 required')
    old=gamma*np.maximum(base,0.); target=old.copy(); metric=(group==0)|(group==1)
    target[metric]=np.maximum(old[metric],float(floor))
    lifted=metric&(target>old)
    return target,{'policy':RESERVE_POLICY,'floor_exact':FLOOR,'floor_units':'original metric Schur row c_plus/c_minus',
        'only_group_indices':[0,1],'only_group_names':list(GROUPS[:2]),
        'metric_selected_row_count':int(np.count_nonzero(metric)),
        'metric_selected_rows_lifted_to_floor':int(np.count_nonzero(lifted)),
        'lifted_selected_row_positions_sha256':digest(np.flatnonzero(lifted).tolist()),
        'minimum_metric_target_evaluated':float(np.min(target[metric])) if np.any(metric) else None,
        'maximum_metric_target_increment_evaluated':float(np.max(target[metric]-old[metric])) if np.any(metric) else 0.,
        'other_physical_row_targets_unchanged':bool(np.array_equal(target[(group>=2)&(group<7)],old[(group>=2)&(group<7)])),
        'actual_same_trial_residuals_not_shifted_or_relabelled':True,
        'actual_metric_budget_and_tolerances_unchanged':True,
        'not_a_claim_of_actual_metric_improvement_or_feasibility':True}


def correction_proposal(base_rows, trial_rows, jacobian, groups, state, primary_step,
                        lower, upper, cap_row, trial_cap_margin, cfg):
    """Minimize ||w/box_width||_1 inside a hard infinity radius.

    Physical direction: c(y)+J(x)w >= gamma*max(c(x),0), except
    metric groups 0/1 have the additional exact row target 1/1000000.
    Curvature direction: c(x)+J(x)(p+w)+rho_budget >= 0,
      rho_budget = initial_slack - r*(initial_slack - primary_predicted_slack).
    No tolerance is added to either physical right hand side. Final nonlinear
    acceptance uses the original (unchanged) tolerances and actual curvatures.
    """
    base,trial=np.asarray(base_rows,float),np.asarray(trial_rows,float)
    J,groups=np.asarray(jacobian,float),np.asarray(groups,int)
    state,p,lower,upper,cap_row=[np.asarray(x,float) for x in (state,primary_step,lower,upper,cap_row)]
    n=len(state); m=len(base)
    if (state.ndim!=1 or any(x.shape!=state.shape for x in (p,lower,upper,cap_row))
            or base.ndim!=1 or trial.shape!=base.shape or groups.shape!=base.shape or J.shape!=(m,n)
            or np.any(lower>upper) or np.any(groups<0) or np.any(groups>=len(GROUPS))
            or not all(np.all(np.isfinite(x)) for x in (state,p,lower,upper,cap_row,base,trial,J))
            or not np.isfinite(trial_cap_margin)):
        raise ValueError('finite same-layout base/trial rows, fixed Jacobian, box and actual affine cap are required')
    physical=groups<7; curved=~physical
    if not np.any(curved):
        raise ValueError('the primary fixed-target curvature rows must remain present')
    width=upper-lower; scale=np.where(width>0,width,1.)
    primary_norm=float(np.max(abs(p)/scale))
    relative=float(Q(cfg['SOC_maximum_correction_relative_to_proposed_step_exact']))
    gamma=float(Q(cfg['SOC_physical_margin_retention_exact']))
    retained=float(Q(cfg['SOC_predicted_descent_retention_exact']))
    if not(0<relative<=1 and 0<=gamma<=1 and 0<retained<=1):
        raise ValueError('declared correction radius/margin/descent fractions are invalid')
    initial=max(0.,float(np.max(-base[curved])))
    primary_linear=base+J@p
    predicted=max(0.,float(np.max(-primary_linear[curved])))
    improvement=initial-predicted
    report={'method':'bounded second-order correction LP using actual two-grid trial residuals',
        'initial_curvature_slack':initial,'primary_predicted_curvature_slack':predicted,
        'primary_predicted_slack_improvement':improvement,
        'primary_box_normalized_step_infinity_norm':primary_norm,
        'physical_rows_count':int(np.count_nonzero(physical)),'curvature_rows_count':int(np.count_nonzero(curved)),
        'Jacobian_reference':'last both-grid physically accepted point x',
        'physical_residual_reference':'actual same primary trial y=x+p on both complete value grids',
        'no_physical_tolerance_or_elastic_slack_added':True,
        'cap_and_box_use_trial_plus_correction_not_the_old_point':True}
    if primary_norm==0 or improvement<=cfg['linear_model_improvement_floor']:
        report['proposal_rejected_before_LP']='no nonzero primary step with predicted curvature descent'
        return None,report
    radius=relative*primary_norm
    rho_budget=initial-retained*improvement
    target,reserve=physical_margin_targets(base,groups,cfg)
    report['metric_row_reserve']=reserve
    A=np.zeros((m+1+2*n,2*n)); b=np.empty(m+1+2*n)
    A[:m,:n]=-J*scale[None,:]
    b[:m][physical]=trial[physical]-target[physical]
    b[:m][curved]=primary_linear[curved]+rho_budget
    A[m,:n]=-cap_row*scale; b[m]=trial_cap_margin
    for j in range(n):
        A[m+1+j,j]=1.; A[m+1+j,n+j]=-1.
        A[m+1+n+j,j]=-1.; A[m+1+n+j,n+j]=-1.
    b[m+1:]=0.
    y=state+p
    lo=np.maximum(-radius,(lower-y)/scale); hi=np.minimum(radius,(upper-y)/scale)
    report.update(curvature_slack_budget=rho_budget,retained_fraction_of_primary_predicted_descent=retained,
        maximum_box_normalized_correction_infinity_norm=radius,
        selected_physical_linearization_error_minimum=float(np.min(trial[physical]-primary_linear[physical])) if np.any(physical) else None,
        rows=len(b),variables=2*n,matrix_bytes=int(A.nbytes),
        objective='sum_j abs(w_j / original_parameter_box_width_j)',
        correction_objective_does_not_reward_unused_tangential_displacements=True)
    if np.any(lo>hi):
        report['proposal_rejected_before_LP']='no correction inside both radius and unchanged parameter box'
        return None,report
    objective=np.r_[np.zeros(n),np.ones(n)]
    before=time.monotonic()
    result=linprog(objective,A_ub=A,b_ub=b,bounds=list(zip(lo,hi))+[(0.,radius)]*n,method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
                 'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],
                 'time_limit':float(cfg['linear_program_seconds'])})
    report.update(LP_invoked=True,success=bool(result.success),status=int(result.status),message=str(result.message),
        nit=int(result.nit),elapsed_seconds=time.monotonic()-before)
    if result.x is None or not np.all(np.isfinite(result.x)):
        return None,report
    solution=np.asarray(result.x,float); w=scale*solution[:n]
    linear_violation=float(np.max(A@solution-b))
    bound_violation=max(float(np.max(lo-solution[:n])),float(np.max(solution[:n]-hi)),
        float(np.max(-solution[n:])),float(np.max(solution[n:]-radius)))
    corrected_curvature_slack=max(0.,float(np.max(-(primary_linear+J@w)[curved])))
    report.update(maximum_linear_row_violation=max(0.,linear_violation),maximum_linear_bound_violation=max(0.,bound_violation),
        correction_box_normalized_infinity_norm=float(np.max(abs(w)/scale)),
        correction_box_normalized_l1_norm=float(np.sum(abs(w)/scale)),
        maximum_absolute_correction=float(np.max(abs(w))),correction_l2=float(np.linalg.norm(w)),
        corrected_predicted_curvature_slack=corrected_curvature_slack,
        corrected_predicted_slack_improvement=initial-corrected_curvature_slack,
        corrected_affine_cap_margin=float(trial_cap_margin+cap_row@w))
    metric_mask=(groups==0)|(groups==1)
    if np.any(metric_mask):
        linear_metric=(trial+J@w)[metric_mask]
        report['metric_row_reserve'].update(
            minimum_corrected_linear_metric_margin=float(np.min(linear_metric)),
            minimum_corrected_linear_metric_margin_minus_floor=float(np.min(linear_metric)-float(Q(FLOOR))),
            actual_nonlinear_metric_not_evaluated_by_this_LP=True)
    if not result.success or max(linear_violation,bound_violation)>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='LP status or independent linear residual'
        return None,report
    return w,report


def run_soc_metric_reserve_steps(objective,initial,*,known_metric_locations=(),artificial_inputs_only=False,evaluate_only=False):
    if not artificial_inputs_only:
        require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear checks require the declared artificial array family')
    cfg=objective.cfg; scale=float(Q(cfg['curvature_scale_exact']))
    metadata={'method':POLICY,'target_schedule_exact':list(objective.targets),'nonlinear_minimize_invocation_count':0,
        'linear_program_invocation_count':0,'primary_LP_invocation_count':0,'correction_LP_invocation_count':0,
        'max_linear_programs_total':cfg['max_linear_models'],'shared_max_physical_evaluations':cfg['max_physical_evaluations'],
        'shared_optimization_seconds':cfg['max_seconds'],'artificial_inputs_only':bool(artificial_inputs_only),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__,
        'evaluate_only':bool(evaluate_only),'models':[],'no_budget_reset_between_stages_or_corrections':True,
        'SOC_parabolic_backtracking_policy':POLICY,'no_extra_correction_LP_for_backtracking':True}
    metadata.update(SOC_metric_row_reserve_policy=RESERVE_POLICY,
        SOC_metric_row_floor_exact=cfg['SOC_metric_row_floor_exact'],
        floor_changes_only_the_proposal_RHS_not_any_actual_gate=True)
    def finish(status,error=None,budget=None):
        point=objective.accepted_iterates[-1] if objective.accepted_iterates else None
        done=any(r['kind']=='stage-complete' and r['stage_index']==objective.active_stage_index for r in objective.stage_events)
        if (point and not done and point['maximum_curvature_on_both_grids']<=objective.active_target+cfg['direct_curvature_tolerance']):
            objective.record_stage('stage-complete',np.asarray(point['physical_parameter_coefficients_binary64']),
                point['coarse'],point['fine'],total_LPs_so_far=metadata['linear_program_invocation_count'],
                derived_from_saved_two_grid_acceptance_without_another_value_call=True)
        snap=objective.snapshot()
        if objective.checkpoint:objective.checkpoint(snap)
        return {'status':status,'error':error,'budget_message':budget,'solver':metadata,'checkpoint':snap,
            'completed_targets_exact':[x['target_exact'] for x in objective.stage_events if x['kind']=='stage-complete'],
            'active_stage_target_exact':objective.active_target_exact,
            'all_ladder_targets_reached':bool(point and point['maximum_curvature_on_both_grids']
                <=float(Q(objective.targets[-1]))+cfg['direct_curvature_tolerance']),
            'correction_prediction_does_not_replace_two_grid_physical_acceptance':True}
    try:
        current=np.asarray(initial,float).copy(); target=objective.active_target; zeta=target/scale
        vector=np.r_[current,zeta]
        coarse=objective.evaluate(vector)['decision']; fine=objective.fine_decision(current)
        if not(coarse['eligible_under_fixed_metric_and_physical_gates'] and fine['eligible_under_fixed_metric_and_physical_gates']):
            return finish('initial-SOC-two-grid-physical-gate-failed')
        accepted=objective.accepted_point(current,coarse,fine,{'kind':'saved-d1ca5f-both-grid-accepted-SOC-start'})
        if not len(objective.pool):objective.initialize_pool(vector)
        objective.expand_pool(vector,'initial-SOC-target-coarse-violations')
        objective.initialize_fine_pool(current,known_metric_locations=known_metric_locations)
        objective.record_stage('stage-start',current,coarse,fine,total_LPs_so_far=0)
        if evaluate_only:return finish('evaluation-only-SOC-initial-state')
        objective.linear_rows(vector); objective.begin_optimization()
        trust=float(Q(cfg['initial_trust_box_fraction_exact']))
        minimum_trust=float(Q(cfg['minimum_trust_box_fraction_exact']))
        minimum_drop=float(Q(cfg['minimum_accepted_curvature_decrease_exact']))
        while metadata['linear_program_invocation_count']<cfg['max_linear_models']:
            objective._wall()
            while accepted['maximum_curvature_on_both_grids']<=objective.active_target+cfg['direct_curvature_tolerance']:
                vector=np.r_[current,objective.active_target/scale]
                coarse=objective.evaluate(vector)['decision']; fine=objective.fine_decision(current)
                objective.record_stage('stage-complete',current,coarse,fine,total_LPs_so_far=metadata['linear_program_invocation_count'])
                if objective.active_stage_index==len(objective.targets)-1:
                    return finish('all-declared-SOC-targets-reached-on-both-grids')
                objective.set_stage(objective.active_stage_index+1)
                vector=np.r_[current,objective.active_target/scale]
                coarse=objective.evaluate(vector)['decision']; fine=objective.fine_decision(current)
                objective.expand_pool(vector,'next-SOC-stage-coarse-curvature-violations')
                objective.record_stage('stage-start',current,coarse,fine,total_LPs_so_far=metadata['linear_program_invocation_count'])
            target=objective.active_target; zeta=target/scale; vector=np.r_[current,zeta]
            base,J,groups,tols=objective.linear_rows(vector)
            pool_versions=(objective.pool_version,objective.fine_pool_version)
            remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
            local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
            p,lp=linear_proposal(base,J,groups,tols,current,objective.lower,objective.upper,objective.gate.row,
                objective.gate.intercept+float(objective.gate.row@current)-objective.gate.target,trust,local)
            metadata['linear_program_invocation_count']+=1; metadata['primary_LP_invocation_count']+=1
            model={'number':len(metadata['models'])+1,'stage_index':objective.active_stage_index,
                'fixed_stage_target_exact':objective.active_target_exact,'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'coarse_pool_rows':len(objective.pool),'fine_pool_rows':len(objective.fine_pool),
                'linear_program':lp,'trials':[],'corrections':[]}
            metadata['models'].append(model); objective._wall()
            if p is None:
                trust*=.5; model['result']='primary-LP-failed-trust-shrunk'
                if trust<minimum_trust:return finish('minimum-trust-after-primary-LP-failure')
                continue
            if lp['predicted_slack_improvement']<=cfg['linear_model_improvement_floor'] or np.max(abs(p))==0:
                model['result']='no-primary-predicted-descent'; return finish('SOC-primary-model-stalled')
            model['exact_binary64_proposed_step']=[str(Q.from_float(float(x))) for x in p]
            old_max=accepted['maximum_curvature_on_both_grids']; succeeded=False; relearned=False; soc_used=False; arc=None

            def assess(candidate,kind,alpha,need_fine_for_SOC=False,curve=None):
                nonlocal current,accepted,succeeded,relearned
                record={'kind':kind,'alpha_exact':alpha,'stage_index':objective.active_stage_index,
                    'target_exact':objective.active_target_exact,'accepted_as_next_iterate':False,
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started'}
                if curve is not None:record['parabolic_curve']=copy.deepcopy(curve)
                model['trials'].append(record)
                rv=objective.evaluate(np.r_[candidate,zeta]); cd=rv['decision']
                record.update(attempt_status='coarse-value-call-complete',coarse_physical_evaluation=rv['physical_geometry_evaluation'],
                    coarse_decision=compact_decision(cd))
                possible=(cd['direct_maximum_absolute_principal_curvature']<=target+cfg['direct_curvature_tolerance']
                    or old_max-cd['direct_maximum_absolute_principal_curvature']>=minimum_drop)
                fd=None
                if possible and cd.get('regularity_screen_pass',True) and (
                        cd['eligible_under_fixed_metric_and_physical_gates'] or need_fine_for_SOC):
                    fd=objective.fine_decision(candidate)
                    record.update(fine_value_evaluation=objective.fine_evaluations,fine_decision=compact_decision(fd),
                        actual_fine_residual_was_evaluated_even_if_coarse_ineligible=not cd['eligible_under_fixed_metric_and_physical_gates'])
                    maximum=max(cd['direct_maximum_absolute_principal_curvature'],fd['direct_maximum_absolute_principal_curvature'])
                    if (cd['eligible_under_fixed_metric_and_physical_gates'] and fd['eligible_under_fixed_metric_and_physical_gates']
                            and maximum<old_max and (maximum<=target+cfg['direct_curvature_tolerance'] or old_max-maximum>=minimum_drop)):
                        accepted=objective.accepted_point(candidate,cd,fd,{'kind':kind,'model':model['number'],
                            'stage_index':objective.active_stage_index,'target_exact':objective.active_target_exact,
                            'alpha_exact':alpha,'previous_maximum_curvature':old_max})
                        current=candidate.copy(); succeeded=True
                        record.update(accepted_as_next_iterate=True,accepted_index=accepted['accepted_index'])
                added,detail=objective.expand_pool(np.r_[candidate,zeta],'SOC-observed-coarse-trial-violations')
                record.update(coarse_omitted_rows=detail['omitted_violating_count'],
                    new_coarse_rows=len(added['added_row_indices']) if added else 0)
                if detail.get('pool_capacity_would_be_exceeded'):raise EvaluationBudgetReached('coarse pool capacity; last accepted retained')
                relearned=relearned or bool(added)
                if fd is not None:
                    added_fine,fd_detail=objective.learn_fine_violations(candidate,'SOC-observed-fine-trial-violations')
                    record.update(fine_omitted_rows=fd_detail['omitted_violating_count'],fine_violation_groups=fd_detail['group_counts'],
                        new_fine_rows=len(added_fine['added_row_indices']) if added_fine else 0)
                    if fd_detail.get('pool_capacity_would_be_exceeded'):raise EvaluationBudgetReached('fine pool capacity; last accepted retained')
                    relearned=relearned or bool(added_fine)
                return cd,fd,record

            for backtrack in range(int(cfg['maximum_backtracks_per_model'])):
                alpha_exact=str(Q(1,2**backtrack)); alpha=float(Q(alpha_exact)); step=alpha*p
                may_SOC=arc is None and not soc_used and metadata['linear_program_invocation_count']<cfg['max_linear_models']
                if arc is None:
                    y=current+step; kind='primary-short-step'; curve=None
                else:
                    y,curve=parabolic_candidate(current,p,arc['w'],alpha_exact,arc['reference_alpha_exact'])
                    curve.update(correction_index=arc['correction_index'],
                        primary_trial_index=arc['primary_trial_index'],
                        linear_curvature_slack_upper_bound=curvature_arc_slack_bound(
                            arc['initial_slack'],arc['primary_slack'],arc['corrected_slack'],
                            float(Q(curve['curve_fraction_exact']))),
                        curve_geometry_must_still_pass_both_original_grids=True)
                    kind='SOC-parabolic-backtrack'
                cd,fd,trial=assess(y,kind,alpha_exact,may_SOC,curve)
                if succeeded:
                    model['result']=('accepted-SOC-parabolic-two-grid-step' if arc is not None
                        else 'accepted-primary-two-grid-step'); break
                if relearned:
                    model['result']='observed-new-rows-return-to-last-accepted-before-correction'; break
                if may_SOC and fd is not None and cd.get('regularity_screen_pass',True) and fd.get('regularity_screen_pass',True):
                    soc_used=True
                    if pool_versions!=(objective.pool_version,objective.fine_pool_version):
                        raise ArithmeticError('SOC cannot use the old Jacobian after a pool layout change')
                    # Both residual blocks below belong to this exact y. No fine
                    # residual from x or from a previous trial is substituted.
                    trial_rows=np.r_[objective.constraint_fun(np.r_[y,zeta]),
                        objective.fine_rows(y).reshape(-1)[objective.fine_pool]]
                    remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
                    local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
                    w,soc=correction_proposal(base,trial_rows,J,groups,current,step,objective.lower,objective.upper,
                        objective.gate.row,objective.gate.intercept+float(objective.gate.row@y)-objective.gate.target,local)
                    if soc.get('LP_invoked'):
                        metadata['linear_program_invocation_count']+=1; metadata['correction_LP_invocation_count']+=1
                    correction={'primary_trial_index':len(model['trials'])-1,'primary_trial_physical_sha256':digest(objective.problem.identity(y)),
                        'coarse_residual_evaluation':trial['coarse_physical_evaluation'],'fine_residual_evaluation':trial['fine_value_evaluation'],
                        'coarse_pool_version':pool_versions[0],'fine_pool_version':pool_versions[1],'linear_program':soc}
                    model['corrections'].append(correction); objective._wall()
                    if w is not None:
                        correction['exact_binary64_correction']=[str(Q.from_float(float(x))) for x in w]
                        arc={'w':w.copy(),'reference_alpha_exact':alpha_exact,
                            'correction_index':len(model['corrections'])-1,
                            'primary_trial_index':correction['primary_trial_index'],
                            'initial_slack':soc['initial_curvature_slack'],
                            'primary_slack':soc['primary_predicted_curvature_slack'],
                            'corrected_slack':soc['corrected_predicted_curvature_slack']}
                        correction['reused_on_later_backtracks_without_another_LP']=True
                        correction['reference_primary_alpha_exact']=alpha_exact
                        z=y+w
                        assess(z,'SOC-corrected-short-step',str(Q(1,2**backtrack)),False)
                        if succeeded:
                            model['result']='accepted-SOC-corrected-two-grid-step'; break
                        if relearned:
                            model['result']='corrected-point-revealed-new-rows-return-to-last-accepted'; break
            if not succeeded and not relearned:
                trust*=.5; model['result']='all-actual-proposals-rejected-last-accepted-preserved'
                if trust<minimum_trust:return finish('minimum-trust-after-SOC-and-backtracking')
            if objective.checkpoint:objective.checkpoint(objective.snapshot())
        return finish('shared-primary-plus-correction-LP-budget-exit')
    except EvaluationBudgetReached as error:
        return finish('shared-SOC-value-time-or-pool-budget-exit',budget=str(error))
    except Exception as error:
        return finish('SOC-step-error',error={'type':type(error).__name__,'message':str(error)})



def developer_check():
    """New RHS/LP branch and copy-equivalence only; no research geometry."""
    from frame_curvature_soc_steps import configuration as initial_configuration
    cfg=configuration(initial_configuration())
    base=np.array([-2e-9,4e-5,0.,2e-8,4e-4,-1e-9,0.,-.1])
    groups=np.array([0,1,2,3,4,5,6,7])
    target,meta=physical_margin_targets(base,groups,cfg)
    expected=np.maximum(base,0.)/4; expected[:2]=np.maximum(expected[:2],1e-6)
    mask_only=bool(np.array_equal(target,expected) and meta['metric_selected_rows_lifted_to_floor']==1
        and meta['other_physical_row_targets_unchanged'] and target[2]==0. and target[3]==5e-9)
    unchanged={k:cfg[k]==initial_configuration()[k] for k in [
        'fixed_metric_budget_exact','metric_row_tolerance','direct_eta_tolerance',
        'shape_constraint_tolerance','mirror_polynomial_tolerance','mirror_radius_tolerance',
        'height_tolerance','box_tolerance','linear_model_residual_limit',
        'SOC_predicted_descent_retention_exact','SOC_maximum_correction_relative_to_proposed_step_exact']}
    base=np.array([2e-8,4e-5,.001,-.2]); trial=np.array([-1e-5,3e-5,.001,-.1])
    J=np.array([[0.,1.],[0.,.5],[0.,1.],[1.,0.]])
    groups=np.array([0,1,2,7]); x=np.array([0.,.001]); p=np.array([.1,0.])
    lo=np.array([-2.,-2.]); hi=-lo; cap=np.array([0.,1.])
    w,report=correction_proposal(base,trial,J,groups,x,p,lo,hi,cap,.001,cfg)
    old_w,old_report=old_correction_proposal(base,trial,J,groups,x,p,lo,hi,cap,.001,cfg)
    wanted=np.array([0.,1.1e-5])
    actual_error=max(abs(w-wanted)) if w is not None else None
    lp_valid=bool(w is not None and report['success'] and actual_error<1e-10
        and report['metric_row_reserve']['minimum_corrected_linear_metric_margin_minus_floor']>=-1e-12)
    old_comparison=bool(old_w is not None and np.max(abs(w-old_w-np.array([0.,9.95e-7])))<1e-10
        and report['curvature_slack_budget']==old_report['curvature_slack_budget']
        and report['selected_physical_linearization_error_minimum']==old_report['selected_physical_linearization_error_minimum'])
    rejected=False
    try:physical_margin_targets(base,groups,dict(cfg,SOC_metric_row_floor_exact='0'))
    except ValueError:rejected=True
    # Exact source comparison is confined to the copied controller: it has the
    # original branch/count/cache/gate behavior and a new local corrector binding.
    old=inspect.getsource(old_arc_controller)
    new=inspect.getsource(run_soc_metric_reserve_steps).replace('def run_soc_metric_reserve_steps(', 'def run_soc_arc_steps(',1)
    addition="""    metadata.update(SOC_metric_row_reserve_policy=RESERVE_POLICY,
        SOC_metric_row_floor_exact=cfg['SOC_metric_row_floor_exact'],
        floor_changes_only_the_proposal_RHS_not_any_actual_gate=True)
"""
    controller_same=new.replace(addition,'',1)==old
    # Row-floor units are not eta units. This is an algebraic scalar fixture,
    # not a stored candidate or any new surface evaluation.
    e,f,bar=.1,.2,float(Q('167/625'))
    eta=(abs(e)+np.sqrt(e*e+4*f*f))/2
    row=bar-abs(e)-f*f/bar
    identity_error=abs(row-(bar-eta)*(bar+eta-abs(e))/bar)
    passed=bool(mask_only and all(unchanged.values()) and lp_valid and old_comparison and rejected
        and controller_same and identity_error<1e-15)
    return {'schema':'SOC-metric-row-reserve-targeted-artificial-v1','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,'target_only_metric_groups':mask_only,
        'unchanged_gate_and_retention_fields':unchanged,'new_LP_analytic_correction':wanted.tolist(),
        'new_LP_actual_correction':None if w is None else w.tolist(),'new_LP_error':actual_error,
        'old_LP_actual_correction':None if old_w is None else old_w.tolist(),
        'old_and_new_only_expected_RHS_effect':old_comparison,'new_LP_respects_metric_floor':lp_valid,
        'original_trial_linearization_error_not_relabelled':old_comparison,
        'invalid_reserve_definition_rejected':rejected,
        'copied_controller_equal_except_new_name_and_metadata':controller_same,
        'metric_row_to_eta_identity_error':identity_error,'toy_correction_report':report,'passed':passed}
