#!/usr/bin/env python3
"""Same strip-reserve controller with an equivalent scaled SOC linear program.

Only the second-order-correction LP representation changes. Primary proposals,
all targets/floors, growth/shrink rules, budgets, full-grid actual gates and
accepted-state policy remain the frozen strip-reserve definitions.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time
import numpy as np
import scipy
from scipy.optimize import linprog

from frame_collar_residual_audit import digest
from frame_second_order_correction_scaling import scale_correction_lp
from frame_metric_spectral_strip_reserve import (
    StripReserveSpectralMetricObjective,configuration as strip_configuration,
    implementation_hashes as strip_hashes,controller_continuation,
    primary_proposal,strip_floor_definition,strip_diagnostics,
    STRIP_GROUPS,_strip_floor,compact_with_strip_gate)
from frame_metric_spectral_trust_growth import (
    next_growth_trust,growth_definition,adaptive_definition)
from frame_metric_spectral_physical_penalty import penalty_definition
from frame_metric_spectral_curvature_reserve import (
    CURVATURE_GROUPS,_floor,floor_definition,floor_diagnostics)
from frame_metric_spectral_adaptive import trial_quality
from frame_metric_budget_recovery import (
    require_public_research_environment,EvaluationBudgetReached,
    parabolic_candidate,curvature_arc_slack_bound)

POLICY='spectral-metric-equivalent-SOC-LP-scaling-v1'


def implementation_hashes():
    result=strip_hashes()
    for name in ['frame_second_order_correction_scaling.py',Path(__file__).name]:
        p=Path(__file__).with_name(name);result[name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def configuration(base):
    cfg=strip_configuration(base)
    cfg.update(second_order_correction_LP_scaling_policy=POLICY,
        primary_SOC_variable_and_row_scalings_unchanged=False,
        primary_variable_and_row_scalings_unchanged=True,
        SOC_only_equivalent_positive_reparameterization=True,
        actual_gate_and_original_unit_LP_residuals_unchanged=True)
    return cfg


def scaling_definition(cfg):
    if cfg.get('second_order_correction_LP_scaling_policy')!=POLICY:
        raise ValueError('explicit equivalent SOC-only scaling policy required')
    return {'schema':POLICY+'-definition',
        'change':'v=r_c z; h_aux=r_c t; divide each affine row by a positive power of two',
        'old_variables':'v=D^-1 w and 0<=h_aux<=r_c with h_aux>=|v|',
        'old_objective_equals_positive_r_c_times_new_objective':True,
        'old_r_c_exact_rule':cfg['SOC_maximum_correction_relative_to_proposed_step_exact']+' times ||D^-1 p||_infinity',
        'old_targets_including_strip_and_curvature_floors_unchanged':True,
        'old_primary_LP_and_every_controller_branch_unchanged':True,
        'old_original_unit_residual_limit':cfg['linear_model_residual_limit'],
        'old_HiGHS_time_limit_and_shared_budgets_unchanged':True,
        'numeric_solver_tolerances_act_on_new_units_and_may_change_the_trajectory':True,
        'no_increase_in_feasible_LP_set_or_actual_geometry_gate':True,
        'not_a_claim_of_solver_conditioning_or_geometric_progress':True}


class SOCScaledSpectralMetricObjective(StripReserveSpectralMetricObjective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.evaluation_definition['SOC_reversible_scaling']=scaling_definition(self.cfg)
        self.evaluation_definition['SOC_scaled_controller_source_sha256']=implementation_hashes()
        self.evaluation_sha256=digest(self.evaluation_definition)

    def snapshot(self):
        result=super().snapshot()
        result['SOC_reversible_scaling']=scaling_definition(self.cfg)
        return result


ACTUAL_GATES=('regularity_screen_pass','previous_metric_budget_pass',
    'single_grid_hard_gate_pass','hard_ball_pass','hard_strip_pass','outer_strip_pass',
    'signed_height_pass','mirror_polynomial_pass','independent_direct_mirror_radius_pass',
    'curvature_lambda_bound_pass','curvature_scaled_PSD_row_pass','independent_direct_curvature_pass',
    'single_grid_admissible_recovery_point')


def compact_with_all_actual_gates(decision):
    out=compact_with_strip_gate(decision)
    out['actual_gate_booleans']={key:decision.get(key) for key in ACTUAL_GATES}
    out['actual_gate_booleans']['cap_and_box_eligible']=decision.get('cap_and_box',{}).get(
        'eligible_under_declared_numerical_gate_tolerances')
    out['new_metric_target_qualified']=decision.get('single_grid_new_target_qualified')
    return out


def curvature_trial_diagnostics(objective,state,reference_values,J,groups,reference_state,reference_kind,*,fine_present):
    """Read only already evaluated arrays; never call geometry or a value oracle."""
    state=np.asarray(state,float);reference_values=np.asarray(reference_values,float)
    J=np.asarray(J,float);groups=np.asarray(groups,int)
    if J.shape!=(len(reference_values),len(state)) or groups.shape!=reference_values.shape:
        raise ValueError('the same selected-row stack and original accepted-state Jacobian are required')
    count=len(objective.pool)
    if len(reference_values)!=count+len(objective.fine_pool):
        raise ValueError('defect diagnostics must precede pool growth')
    prediction=reference_values+J@(state-np.asarray(reference_state,float))
    if not np.array_equal(objective.epigraph_cache['vector'][:-1],state):
        raise ValueError('coarse diagnostic cache must match the actual trial')
    if not np.array_equal(objective.geometry_cache['state'],state):
        raise ValueError('coarse ordinary geometry cache must match the actual trial')
    specs=[('coarse',objective.epigraph_cache['rows'],objective.geometry_cache,objective.pool,0)]
    if fine_present:
        if not np.array_equal(objective.fine_cache['state'],state):
            raise ValueError('fine diagnostic cache must match the actual trial')
        specs.append(('fine',objective.fine_cache['rows'],objective.fine_cache['data'],objective.fine_pool,count))
    out={'reference_kind':reference_kind,
        'scope':'original scaled PSD units, selected same-point rows only; whole-grid decisions remain independent',
        'same_cached_state_no_additional_geometry_or_value_call':True,
        'fine_actual_available':bool(fine_present),'grids':{}}
    scale=float(Q(objective.cfg['curvature_scale_exact']))
    lam=float(objective.fixed_zeta)*scale
    for name,rows,data,pool,offset in specs:
        rows=np.asarray(rows,float);pool=np.asarray(pool,int)
        actual=rows.reshape(-1)[pool]; pred=prediction[offset:offset+len(pool)]
        labels=groups[offset:offset+len(pool)]
        if rows.ndim!=3 or rows.shape[0]!=11:
            raise ValueError('the actual public group-major eleven-row layout is required')
        nr,nt=rows.shape[1:]; point_count=nr*nt
        if not np.array_equal(labels,pool//point_count):
            raise ValueError('coarse/fine flattened eleven-group index mapping changed')
        forms=data['curvature']
        statistics=[]
        for group in CURVATURE_GROUPS:
            ids=np.flatnonzero(labels==group)
            if not len(ids):continue
            k=ids[np.argmin(actual[ids])]; flat=int(pool[k]); point=flat%point_count
            ir,it=divmod(point,nt); q=float(forms['q'][ir,it])
            kappas=np.asarray(forms['principal'][ir,it],float)
            critical={'flat_row_id':flat,'radial_index':ir,'angular_index':it,
                't':float(data['radial'][ir]),'theta':float(data['theta'][it]),
                'actual_row':float(actual[k]),'predicted_row':float(pred[k]),
                'actual_minus_predicted':float(actual[k]-pred[k]),'q':q,
                'principal_curvatures':kappas.tolist()}
            if group in (8,10):
                sign=1 if group==8 else -1
                spectral=q**4/scale**2*float(np.prod(lam+sign*kappas))
                critical.update(exact_determinant_identity='q^4/scale^2*(lambda+sign*kappa1)*(lambda+sign*kappa2)',
                    determinant_from_same_point_spectral_factors=spectral,
                    floating_identity_difference=float(actual[k]-spectral))
            statistics.append({'group':group,'selected_count':len(ids),
                'selected_predicted_minimum':float(np.min(pred[ids])),
                'selected_actual_minimum':float(np.min(actual[ids])),
                'minimum_actual_minus_prediction':float(np.min(actual[ids]-pred[ids])),
                'maximum_absolute_actual_minus_prediction':float(np.max(abs(actual[ids]-pred[ids]))),
                'actual_minimum_selected_row':critical})
        out['grids'][name]={'groups':statistics}
    return out


def correction_proposal(base,trial,J,groups,state,p,lower,upper,cap_row,cap_y,cfg):
    base,trial,J,groups=np.asarray(base,float),np.asarray(trial,float),np.asarray(J,float),np.asarray(groups,int)
    state,p,lower,upper,cap_row=[np.asarray(x,float) for x in (state,p,lower,upper,cap_row)]
    n=len(state); m=len(base); soft=groups<2; hard=~soft
    if (trial.shape!=base.shape or groups.shape!=base.shape or J.shape!=(m,n)
            or any(x.shape!=state.shape for x in [p,lower,upper,cap_row]) or not np.any(soft)
            or np.any(groups<0) or np.any(groups>10) or np.any(lower>=upper)
            or not all(np.all(np.isfinite(x)) for x in [base,trial,J,state,p,lower,upper,cap_row])
            or not np.isfinite(cap_y)):
        raise ValueError('same actual two-grid trial residuals and fixed accepted-state Jacobian required')
    width=upper-lower; norm=float(np.max(abs(p)/width)); linear=base+J@p
    rho0=max(0.,float(np.max(-base[soft]))); rho1=max(0.,float(np.max(-linear[soft])))
    gain=rho0-rho1; report={'initial_metric_slack':rho0,'primary_predicted_metric_slack':rho1,
        'primary_predicted_slack_improvement':gain,'primary_box_normalized_step_infinity_norm':norm,
        'residual_source':'actual same y on both full grids','Jacobian_source':'last accepted x',
        'hard_curvature_is_not_given_slack':True,'cap_and_box_use_y_plus_w':True}
    if norm==0 or gain<=cfg['linear_model_improvement_floor']:
        report['proposal_rejected_before_LP']='no primary predicted metric restoration'; return None,report
    gamma=float(Q(cfg['SOC_physical_margin_retention_exact']))
    retained=float(Q(cfg['SOC_predicted_descent_retention_exact']))
    radius=float(Q(cfg['SOC_maximum_correction_relative_to_proposed_step_exact']))*norm
    budget=rho0-retained*gain; target=gamma*np.maximum(base,0.)
    legacy_target=target.copy()
    curved=np.isin(groups,CURVATURE_GROUPS)
    target[curved]=np.maximum(target[curved],_floor(cfg))
    target_before_strip=target.copy()
    strip=np.isin(groups,STRIP_GROUPS)
    target[strip]=np.maximum(target[strip],_strip_floor(cfg))
    A=np.zeros((m+1+2*n,2*n)); b=np.empty(m+1+2*n); A[:m,:n]=-J*width
    # The retained budget comes from the primary prediction, but BOTH actual
    # residual blocks are now taken at the same y. This corrects nonlinear
    # metric curvature as well as the hard constraints.
    b[:m][hard]=trial[hard]-target[hard]; b[:m][soft]=trial[soft]+budget
    A[m,:n]=-cap_row*width; b[m]=cap_y
    for j in range(n):
        A[m+1+j,j]=1.; A[m+1+j,n+j]=-1.
        A[m+1+n+j,j]=-1.; A[m+1+n+j,n+j]=-1.
    b[m+1:]=0.; y=state+p
    lo=np.maximum(-radius,(lower-y)/width); hi=np.minimum(radius,(upper-y)/width)
    report.update(metric_slack_budget=budget,maximum_box_normalized_correction_infinity_norm=radius,
        hard_margin_retention=gamma,rows=len(b),variables=2*n,matrix_bytes=A.nbytes,
        metric_budget_applied_to_actual_trial_rows_plus_old_Jacobian_correction=True,
        selected_metric_actual_minus_primary_linear_minimum=float(np.min(trial[soft]-linear[soft])))
    report['curvature_proposal_diagnostics']=floor_diagnostics(base,trial,legacy_target,target,groups,cfg)
    report['strip_proposal_diagnostics']=strip_diagnostics(base,trial,target_before_strip,target,groups,cfg)
    if np.any(lo>hi):
        report['proposal_rejected_before_LP']='no correction in original box and relative radius';return None,report
    # This is a bijective representation of the already assembled old LP.
    scaling_started=time.monotonic()
    scaled=scale_correction_lp(A,b,np.r_[lo,np.zeros(n)],np.r_[hi,np.full(n,radius)],radius)
    report['SOC_reversible_scaling']=scaled.definition()
    report['SOC_scaling_prepare_seconds']=time.monotonic()-scaling_started
    report['SOC_solver_tolerances_are_in_scaled_units_not_original_residual_units']=True
    before=time.monotonic()
    r=linprog(scaled.objective,A_ub=scaled.A,b_ub=scaled.b,
        bounds=list(zip(scaled.lower,scaled.upper)),method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
            'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],'time_limit':cfg['linear_program_seconds']})
    report.update(LP_invoked=True,success=bool(r.success),status=int(r.status),message=str(r.message),
        nit=int(r.nit),elapsed_seconds=time.monotonic()-before)
    report['SOC_solver_returned_finite_primal']=bool(r.x is not None
        and np.asarray(r.x).shape==scaled.objective.shape and np.all(np.isfinite(r.x)))
    report['SOC_original_unit_dual_diagnostics']=scaled.original_dual_diagnostics(
        r,np.r_[groups,-1,np.full(2*n,-2)])
    if not report['SOC_solver_returned_finite_primal']:return None,report
    x=scaled.to_original(r.x); w=width*x[:n]
    report['SOC_original_and_scaled_residuals']=scaled.original_residuals(r.x)
    violation=max(0.,float(np.max(A@x-b)))
    bv=max(0.,float(np.max(lo-x[:n])),float(np.max(x[:n]-hi)),float(np.max(-x[n:])),float(np.max(x[n:]-radius)))
    report.update(maximum_linear_row_violation=violation,maximum_linear_bound_violation=bv,
        maximum_absolute_correction=float(np.max(abs(w))),correction_l2=float(np.linalg.norm(w)),
        correction_box_normalized_infinity_norm=float(np.max(abs(w)/width)),
        correction_box_normalized_l1_norm=float(np.sum(abs(w)/width)),
        corrected_predicted_metric_slack=max(0.,float(np.max(-(linear+J@w)[soft]))),
        corrected_actual_trial_linear_metric_slack=max(0.,float(np.max(-(trial+J@w)[soft]))),
        basepoint_prediction_slack_is_only_for_parabolic_linear_bookkeeping=True,
        minimum_corrected_linear_hard_margin=float(np.min(trial[hard]+J[hard]@w)) if np.any(hard) else None,
        corrected_affine_cap_margin=float(cap_y+cap_row@w))
    report['curvature_proposal_diagnostics']=floor_diagnostics(base,trial,legacy_target,target,groups,cfg,
        linear=trial+J@w)
    report['strip_proposal_diagnostics']=strip_diagnostics(base,trial,target_before_strip,target,groups,cfg,
        linear=trial+J@w)
    if not r.success or max(violation,bv)>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='SOC LP status or linear residual';return None,report
    return w,report



def run_soc_scaled_recovery(objective,initial,*,known_metric_locations=(),continuation_state=None,artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,SOCScaledSpectralMetricObjective):
        raise ValueError('the explicit adaptive spectral objective is required')
    if objective.cfg.get('artificial_large_metric_budget_for_IO_only') and not (artificial_inputs_only and evaluate_only):
        raise ValueError('the loose predecessor fixture budget is only for artificial IO without LPs')
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear steps require the explicit artificial array family')
    cfg=objective.cfg
    inherited_trust,growth_streak,continuation=controller_continuation(cfg,continuation_state,artificial=artificial_inputs_only)
    objective.evaluation_definition['restored_controller_continuation']=continuation
    objective.evaluation_sha256=digest(objective.evaluation_definition)
    meta={'method':POLICY,'new_metric_target_exact':cfg['fixed_metric_budget_exact'],
        'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
        'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
        'nonlinear_minimize_invocation_count':0,'linear_program_invocation_count':0,
        'primary_LP_invocation_count':0,'correction_LP_invocation_count':0,
        'shared_max_LPs':cfg['max_linear_models'],'shared_max_values':cfg['max_physical_evaluations'],
        'shared_active_seconds':cfg['max_seconds'],'models':[],
        'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'restored_controller_continuation':continuation,
        'numpy_version':np.__version__,'scipy_version':scipy.__version__}
    def finish(status,error=None,budget=None):
        snap=objective.snapshot(); point=snap.get('selected_two_grid_physical_point')
        if objective.checkpoint:objective.checkpoint(snap)
        return {'status':status,'error':error,'budget_message':budget,'solver':meta,'checkpoint':snap,
            'new_metric_target_reached_on_both_grids':bool(point and point['new_metric_target_qualified_on_both_grids']),
            'adaptive_trust_policy':adaptive_definition(objective.cfg),
            'curvature_proposal_floor':floor_definition(objective.cfg),
            'primary_physical_step_cost':penalty_definition(objective.cfg),
            'conservative_trust_growth':growth_definition(objective.cfg),
            'strip_proposal_floor':strip_floor_definition(objective.cfg),
            'SOC_reversible_scaling':scaling_definition(objective.cfg),
            'final_consecutive_growth_qualifying_models':growth_streak,
            'no_free_curvature_or_metric_auxiliary_is_a_physical_coefficient':True}
    def update_model_scale(model,proposed):
        nonlocal growth_streak
        radius,growth_streak,feedback=next_growth_trust(model,proposed,growth_streak,cfg)
        model['scale_feedback_update']=feedback
        objective.trust_updates.append(copy.deepcopy(feedback))
        return radius
    try:
        current=np.asarray(initial,float).copy(); vector=objective.vector(current)
        cd=objective.evaluate(vector)['decision']; fd=objective.fine_decision(current)
        if not(cd['single_grid_admissible_recovery_point'] and fd['single_grid_admissible_recovery_point']):
            return finish('initial-hard-curvature-or-prior-metric-physical-gate-failed')
        accepted=objective.accepted_point(current,cd,fd,{'kind':'temporary-restored-strip-two-grid-success-SOC-scaling-start'})
        if not len(objective.pool):objective.initialize_pool(vector)
        objective.expand_pool(vector,'initial-soft-metric-envelope-and-hard-coarse-separation')
        objective.initialize_fine_pool(current,known_metric_locations=known_metric_locations)
        if evaluate_only:return finish('evaluation-only-recovery-initialization')
        if accepted['new_metric_target_qualified_on_both_grids']:return finish('new-metric-target-already-qualified')
        objective.linear_rows(vector); objective.begin_optimization()
        trust=inherited_trust
        minimum_trust=float(Q(cfg['minimum_trust_box_fraction_exact']))
        drop=float(Q(cfg['minimum_accepted_eta_decrease_exact']))
        if trust<minimum_trust:return finish('restored-controller-below-original-minimum-trust')
        while meta['linear_program_invocation_count']<cfg['max_linear_models']:
            objective._wall(); vector=objective.vector(current)
            base,J,groups,tols=objective.linear_rows(vector)
            versions=(objective.pool_version,objective.fine_pool_version)
            remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
            local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
            p,lp=primary_proposal(base,J,groups,tols,current,objective.lower,objective.upper,objective.gate.row,
                objective.gate.intercept+float(objective.gate.row@current)-objective.gate.target,trust,local)
            meta['linear_program_invocation_count']+=1; meta['primary_LP_invocation_count']+=1
            model={'number':len(meta['models'])+1,'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'coarse_pool_rows':len(objective.pool),'fine_pool_rows':len(objective.fine_pool),
                'coarse_pool_version':versions[0],'fine_pool_version':versions[1],
                'trust_before_model':trust,'scale_feedback_trials':[],
                'linear_program':lp,'trials':[],'corrections':[]}; meta['models'].append(model);objective._wall()
            if p is None:
                trust*=.5;model['result']='primary-LP-failed-trust-shrunk'
                trust=update_model_scale(model,trust)
                if trust<minimum_trust:return finish('minimum-trust-after-primary-failure')
                continue
            if lp['predicted_slack_improvement']<=cfg['linear_model_improvement_floor'] or np.max(abs(p))==0:
                model['result']='no-primary-metric-restoration';return finish('metric-restoration-linear-model-stalled')
            model['exact_binary64_proposed_step']=[str(Q.from_float(float(x))) for x in p]
            old_eta=accepted['maximum_eta_on_both_grids']; succeeded=False; relearned=False; soc_used=False; arc=None
            def assess(candidate,kind,alpha,need_fine=False,curve=None,prediction=None,curvature_reference=None):
                nonlocal current,accepted,succeeded,relearned
                record={'kind':kind,'alpha_exact':alpha,'accepted_as_next_iterate':False,
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started'}
                if curve is not None:record['parabolic_curve']=copy.deepcopy(curve)
                model['trials'].append(record)
                rv=objective.evaluate(objective.vector(candidate)); c=rv['decision']
                record.update(attempt_status='coarse-value-call-complete',
                    coarse_physical_evaluation=rv['physical_geometry_evaluation'],coarse_decision=compact_with_all_actual_gates(c))
                possible=c['direct_max_eta']<old_eta and (
                    old_eta-c['direct_max_eta']>=drop or c['single_grid_new_target_qualified'])
                f=None
                if c.get('regularity_screen_pass',False) and (need_fine or (possible and c['single_grid_admissible_recovery_point'])):
                    f=objective.fine_decision(candidate)
                    record.update(fine_value_evaluation=objective.fine_evaluations,fine_decision=compact_with_all_actual_gates(f),
                        actual_fine_evaluated_even_if_coarse_ineligible=not c['single_grid_admissible_recovery_point'])
                    maximum=max(c['direct_max_eta'],f['direct_max_eta'])
                    qualified=c['single_grid_new_target_qualified'] and f['single_grid_new_target_qualified']
                    if (c['single_grid_admissible_recovery_point'] and f['single_grid_admissible_recovery_point']
                            and maximum<old_eta and (old_eta-maximum>=drop or qualified)):
                        accepted=objective.accepted_point(candidate,c,f,{'kind':kind,'model':model['number'],
                            'alpha_exact':alpha,'previous_two_grid_maximum_eta':old_eta})
                        current=candidate.copy();succeeded=True
                        record.update(accepted_as_next_iterate=True,accepted_index=accepted['accepted_index'])
                # Values and forms are already cached at this exact candidate.
                # Capture before any learned row changes the pool indexing.
                reference=(base,vector[:-1],'accepted-basepoint-plus-J-total-step') if curvature_reference is None else curvature_reference
                record['curvature_nonlinear_defect_diagnostic']=curvature_trial_diagnostics(
                    objective,candidate,reference[0],J,groups,reference[1],reference[2],fine_present=f is not None)
                added,detail=objective.expand_pool(objective.vector(candidate),'recovery-coarse-actual-hard-and-soft-envelope')
                record.update(coarse_omitted_rows=detail['omitted_violating_count'],
                    coarse_omitted_hard_rows=detail['omitted_hard_violating_count'],
                    new_coarse_rows=len(added['added_row_indices']) if added else 0)
                if detail.get('pool_capacity_would_be_exceeded'):
                    raise EvaluationBudgetReached('coarse row capacity; last accepted metric point retained')
                relearned=relearned or bool(added)
                if f is not None:
                    addf,detailf=objective.learn_fine_violations(candidate,'recovery-fine-hard-and-soft-envelope')
                    record.update(fine_omitted_rows=detailf['omitted_violating_count'],
                        fine_omitted_hard_rows=detailf['omitted_hard_violating_count'],
                        fine_violation_groups=detailf['group_counts'],
                        new_fine_rows=len(addf['added_row_indices']) if addf else 0)
                    if detailf.get('pool_capacity_would_be_exceeded'):
                        raise EvaluationBudgetReached('fine row capacity; last accepted metric point retained')
                    relearned=relearned or bool(addf)
                quality=trial_quality(old_eta,c,f,prediction,kind,cfg)
                record['scale_feedback']=quality;model['scale_feedback_trials'].append(quality)
                return c,f,record
            for bi in range(int(cfg['maximum_backtracks_per_model'])):
                alpha=str(Q(1,2**bi)); step=float(Q(alpha))*p
                may_soc=arc is None and not soc_used and meta['linear_program_invocation_count']<cfg['max_linear_models']
                if arc is None:y=current+step;kind='primary-metric-short-step';curve=None
                else:
                    y,curve=parabolic_candidate(current,p,arc['w'],alpha,arc['reference_alpha_exact'])
                    curve.update(correction_index=arc['correction_index'],
                        linear_metric_slack_upper_bound=curvature_arc_slack_bound(
                            arc['initial'],arc['primary'],arc['corrected'],float(Q(curve['curve_fraction_exact']))))
                    kind='metric-SOC-parabolic-backtrack'
                predicted=(max(0.,float(np.max(-(base+J@step)[groups<2]))) if arc is None
                    else curve['linear_metric_slack_upper_bound'])
                prediction={'predicted_slack':predicted,
                    'model_kind':'basepoint-plus-J-step' if arc is None else 'parabolic-basepoint-linear-bound',
                    'pool_versions':list(versions),'full_fine_actual_required_for_eta_ratio':True}
                c,f,trial=assess(y,kind,alpha,may_soc,curve,prediction)
                if succeeded:model['result']='accepted-two-grid-true-metric-descent';break
                if relearned:model['result']='new-rows-return-to-last-accepted-before-SOC';break
                if may_soc and f is not None and c.get('regularity_screen_pass',False) and f.get('regularity_screen_pass',False):
                    soc_used=True
                    if versions!=(objective.pool_version,objective.fine_pool_version):
                        raise ArithmeticError('SOC old Jacobian cannot survive pool layout change')
                    trial_rows=np.r_[objective.constraint_fun(objective.vector(y)),
                        objective.fine_rows(y).reshape(-1)[objective.fine_pool]]
                    remaining=cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
                    local=dict(cfg,linear_program_seconds=min(cfg['linear_program_seconds'],max(.001,remaining)))
                    w,soc=correction_proposal(base,trial_rows,J,groups,current,step,objective.lower,objective.upper,
                        objective.gate.row,objective.gate.intercept+float(objective.gate.row@y)-objective.gate.target,local)
                    if soc.get('LP_invoked'):
                        meta['linear_program_invocation_count']+=1;meta['correction_LP_invocation_count']+=1
                    correction={'primary_trial_index':len(model['trials'])-1,
                        'primary_trial_physical_sha256':digest(objective.problem.identity(y)),
                        'coarse_residual_evaluation':trial['coarse_physical_evaluation'],
                        'fine_residual_evaluation':trial['fine_value_evaluation'],
                        'coarse_pool_version':versions[0],'fine_pool_version':versions[1],'linear_program':soc}
                    model['corrections'].append(correction);objective._wall()
                    if w is not None:
                        correction['exact_binary64_correction']=[str(Q.from_float(float(x))) for x in w]
                        arc={'w':w.copy(),'reference_alpha_exact':alpha,'correction_index':len(model['corrections'])-1,
                            'initial':soc['initial_metric_slack'],'primary':soc['primary_predicted_metric_slack'],
                            'corrected':soc['corrected_predicted_metric_slack']}
                        assess(y+w,'metric-SOC-corrected-short-step',alpha,
                            prediction={'predicted_slack':soc['corrected_actual_trial_linear_metric_slack'],
                                'model_kind':'same-actual-y-rows-plus-J-correction',
                                'pool_versions':list(versions),'full_fine_actual_required_for_eta_ratio':True},
                            curvature_reference=(trial_rows,y.copy(),'same-primary-y-actual-rows-plus-old-J-correction'))
                        if succeeded:model['result']='accepted-full-SOC-two-grid-metric-descent';break
                        if relearned:model['result']='corrected-new-rows-return-to-last-accepted';break
            if succeeded and accepted['new_metric_target_qualified_on_both_grids']:
                return finish('fixed-new-metric-target-qualified-on-both-grids')
            original_minimum_reached=False
            if not succeeded and not relearned:
                trust*=.5;model['result']='all-proposals-rejected-last-accepted-retained'
                original_minimum_reached=trust<minimum_trust
            trust=update_model_scale(model,trust)
            if trust<minimum_trust:return finish('minimum-trust-after-SOC-and-backtracking' if original_minimum_reached
                else 'minimum-trust-after-actual-model-quality-feedback')
            if objective.checkpoint:objective.checkpoint(objective.snapshot())
        return finish('shared-primary-plus-SOC-LP-budget-exit')
    except EvaluationBudgetReached as error:
        return finish('shared-value-time-or-pool-budget-exit',budget=str(error))
    except Exception as error:
        return finish('metric-recovery-error',error={'type':type(error).__name__,'message':str(error)})

def developer_check():
    """Exercise only the new SOC representation, mapping and cached diagnostics."""
    from types import SimpleNamespace
    from unittest.mock import patch
    import sys
    import frame_metric_spectral_strip_reserve as old_strip
    from frame_second_order_correction_scaling import developer_check as scaling_check
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    from frame_curvature_epigraph_exchange import curvature_rows
    from frame_curvature_psd import curvature_values,independent_principal_curvatures
    helper=scaling_check()
    cfg=configuration(recovery_configuration(start_configuration(),target='1/100',curvature_cap='3'))
    groups=np.arange(11)
    base=np.array([-.01,-.009,1.,1.,2e-7,2e-7,1.,1.,1e-7,1.,1.])
    J=np.zeros((11,2));J[0,0]=J[1,0]=1.;J[4,1]=1.;J[5,1]=-1.;J[8,1]=100.
    state=np.zeros(2);p=np.array([.001,0.]);lo=np.full(2,-8.);hi=np.full(2,8.)
    trial=base+J@p;trial[:2]-=.0002;trial[4]=.9e-7;trial[5]=1.1e-7;trial[8]=-1e-8
    cap=np.zeros(2)
    args=(base,trial,J,groups,state,p,lo,hi,cap,0.,cfg)
    def capture(module,call):
        records=[]
        def stop(c,**kwargs):
            records.append({'c':np.array(c),'A':np.array(kwargs['A_ub']),'b':np.array(kwargs['b_ub']),
                'bounds':copy.deepcopy(kwargs['bounds']),'options':copy.deepcopy(kwargs['options']),
                'method':kwargs['method']})
            return SimpleNamespace(success=False,status=2,message='artificial assembly capture only',nit=0,x=None)
        with patch.object(module,'linprog',side_effect=stop):
            answer=call()
        if len(records)!=1:raise AssertionError('one requested SOC LP assembly')
        return records[0],answer
    before=[x.copy() for x in (base,trial,J,groups,state,p,lo,hi,cap)]
    old_data,old_answer=capture(old_strip,lambda:old_strip.correction_proposal(*args))
    new_data,new_answer=capture(sys.modules[__name__],lambda:correction_proposal(*args))
    radius=old_answer[1]['maximum_box_normalized_correction_infinity_norm']
    oldbounds=np.asarray(old_data['bounds'])
    expected=scale_correction_lp(old_data['A'],old_data['b'],oldbounds[:,0],oldbounds[:,1],radius)
    assembly=bool(np.array_equal(new_data['A'],expected.A)
        and np.array_equal(new_data['b'],expected.b) and np.array_equal(new_data['c'],expected.objective)
        and new_data['bounds']==list(zip(expected.lower,expected.upper))
        and new_data['options']==old_data['options'] and new_data['method']==old_data['method'])
    targets_same=(new_answer[1]['curvature_proposal_diagnostics']==old_answer[1]['curvature_proposal_diagnostics']
        and new_answer[1]['strip_proposal_diagnostics']==old_answer[1]['strip_proposal_diagnostics']
        and new_answer[1]['metric_slack_budget']==old_answer[1]['metric_slack_budget'])
    old_w,old_lp=old_strip.correction_proposal(*args)
    new_w,new_lp=correction_proposal(*args)
    solved=bool(old_w is not None and new_w is not None and old_lp['success'] and new_lp['success']
        and np.max(abs(old_w-new_w))<1e-10
        and new_lp['maximum_linear_row_violation']<=cfg['linear_model_residual_limit']
        and new_lp['SOC_original_unit_dual_diagnostics']['available'])
    rejected_primal={}
    for label,bad_x in [('nonfinite',np.full(4,np.nan)),('wrong-shape',np.zeros(5))]:
        bad_result=SimpleNamespace(success=False,status=4,message='artificial malformed primal',nit=0,x=bad_x)
        with patch.object(sys.modules[__name__],'linprog',return_value=bad_result):
            bad_w,bad_report=correction_proposal(*args)
        rejected_primal[label]=bool(bad_w is None
            and not bad_report['SOC_solver_returned_finite_primal']
            and bad_report['SOC_original_unit_dual_diagnostics']['available'] is False)

    # Actual row/cache indexing and same-point spectral units: artificial jets only.
    def make_data(nt):
        nr=2; shape=(nr,nt,3);data={}
        data['radial']=np.array([0.,1.]);data['theta']=2*np.pi*np.arange(nt)/nt
        data['Xs']=np.broadcast_to(np.array([.9,0.,0.]),shape).copy()
        data['Xt']=np.broadcast_to(np.array([0.,1.,0.]),shape).copy()
        data['Xss']=np.zeros(shape);data['Xss'][...,2]=-1.62*(1+.01*np.arange(nt))
        data['Xst']=np.zeros(shape);data['Xtt']=np.zeros(shape);data['Xtt'][...,2]=1.
        forms=curvature_values(data,np.ones((nr,1)),.01)
        forms['principal']=independent_principal_curvatures(forms);data['curvature']=forms
        rows=np.zeros((11,nr,nt));rows[7:]=np.moveaxis(curvature_rows(forms,.03,100.)[0],-1,0)
        ids=np.array([g*nr*nt+i for g in CURVATURE_GROUPS for i in range(nr*nt)],int)
        return data,rows,ids
    dc,rc,pc=make_data(4);df,rf,pf=make_data(8)
    toy=SimpleNamespace(pool=pc,fine_pool=pf,cfg={'curvature_scale_exact':'100'},
        fixed_zeta=.03,epigraph_cache={'vector':np.array([0.,.03]),'rows':rc},
        geometry_cache=dict(dc,state=np.array([0.])),
        fine_cache={'state':np.array([0.]),'data':df,'rows':rf})
    observed=np.r_[rc.reshape(-1)[pc],rf.reshape(-1)[pf]]
    refs=observed+1e-4; JJ=np.zeros((len(refs),1)); labels=np.r_[pc//8,pf//16]
    diag=curvature_trial_diagnostics(toy,np.array([0.]),refs,JJ,labels,np.array([0.]),
        'artificial basepoint',fine_present=True)
    only_coarse=curvature_trial_diagnostics(toy,np.array([0.]),refs,JJ,labels,np.array([0.]),
        'artificial incomplete fine',fine_present=False)
    identity_error=max(abs(g['actual_minimum_selected_row'].get('floating_identity_difference',0.))
        for v in diag['grids'].values() for g in v['groups'])
    defect_error=max(abs(g['minimum_actual_minus_prediction']+1e-4)
        for v in diag['grids'].values() for g in v['groups'])
    flag_source={key:True for key in ACTUAL_GATES}
    flag_source.update(hard_strip_pass=False,independent_direct_curvature_pass=False,
        cap_and_box={'eligible_under_declared_numerical_gate_tolerances':True})
    flags=compact_with_all_actual_gates(flag_source)
    # Use the genuine existing objective/cache API on a tiny artificial family,
    # rather than relying only on a self-invented cache layout.
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    problem=_CurvatureArrayProblem();xx=np.array([.3,.6,.6])
    radial=np.array([0.,.2,.4,.7,1.]);theta=np.arange(12)*2*np.pi/12
    obj=SOCScaledSpectralMetricObjective(problem,HeightAffineGate.from_artificial_array_problem(problem),
        radial,theta,3,np.array([-.8,-1.,-1.]),np.array([2.,1.,1.]),cfg=cfg)
    obj.evaluate(obj.vector(xx));obj.fine_decision(xx)
    obj.initialize_pool(obj.vector(xx));obj.initialize_fine_pool(xx)
    obj.evaluate(obj.vector(xx));obj.fine_decision(xx)
    vv=np.r_[obj.epigraph_cache['rows'].reshape(-1)[obj.pool],obj.fine_cache['rows'].reshape(-1)[obj.fine_pool]]
    gg=np.r_[obj.pool//(len(radial)*len(theta)),obj.fine_pool//(2*len(radial)*len(theta))]
    counts=(obj.geometry_evaluations,obj.fine_evaluations)
    real_cache_diag=curvature_trial_diagnostics(obj,xx,vv,np.zeros((len(vv),len(xx))),gg,xx,
        'genuine artificial objective same-state caches',fine_present=True)
    actual_cache_zero=max(abs(v['minimum_actual_minus_prediction'])
        for d in real_cache_diag['grids'].values() for v in d['groups'])
    checks={
        'pure_scaling_helper':helper['passed'],
        'bad_primal_diagnostics_do_not_turn_proposal_rejection_into_stage_error':all(rejected_primal.values()),
        'all_SOC_original_rows_and_bounds_transform_without_target_change':assembly,
        'unchanged_actual_y_targets_cap_and_metric_budget':targets_same,
        'same_LP_time_limit_and_solver_tolerance_numbers':new_data['options']==old_data['options'],
        'new_numeric_tolerance_units_explicit':new_answer[1]['SOC_solver_tolerances_are_in_scaled_units_not_original_residual_units'],
        'no_primal_not_filled_by_zero':new_answer[0] is None and not new_answer[1]['SOC_solver_returned_finite_primal']
            and not new_answer[1]['SOC_original_unit_dual_diagnostics']['available'],
        'small_new_and_old_artificial_SOC_solve_same_original_optimum':solved,
        'old_primary_callable_is_unmodified':primary_proposal is old_strip.primary_proposal,
        'old_actual_coarse_and_fine_gate_methods_unmodified':
            SOCScaledSpectralMetricObjective.evaluate is old_strip.StripReserveSpectralMetricObjective.evaluate
            and SOCScaledSpectralMetricObjective.fine_decision is old_strip.StripReserveSpectralMetricObjective.fine_decision,
        'assembly_inputs_unmodified':all(np.array_equal(x,y) for x,y in zip(before,(base,trial,J,groups,state,p,lo,hi,cap))),
        'cached_same_point_curvature_determinant_units':identity_error<1e-14,
        'actual_minus_prediction_uses_the_same_rows':defect_error<1e-14,
        'genuine_artificial_objective_group_major_cache_API':actual_cache_zero==0.
            and counts==(obj.geometry_evaluations,obj.fine_evaluations),
        'missing_fine_not_fabricated':not only_coarse['fine_actual_available'] and set(only_coarse['grids'])=={'coarse'},
        'full_failure_booleans_preserved':flags['actual_gate_booleans']['hard_strip_pass'] is False
            and flags['actual_gate_booleans']['independent_direct_curvature_pass'] is False
            and flags['actual_gate_booleans']['hard_ball_pass'] is True,
        'no_research_candidate_evaluated_or_optimized':True,
        'no_old_growth_or_strip_development_suite_repeated':True}
    result={'schema':POLICY+'-artificial-check','passed':all(checks.values()),'checks':checks,
        'helper':helper,'old_original_unit_array_SOC':old_lp,'new_scaled_array_SOC':new_lp,
        'maximum_same_point_determinant_identity_difference':identity_error,
        'maximum_known_nonlinear_defect_difference':defect_error,
        'source_files_sha256':implementation_hashes()}
    if not result['passed']:raise AssertionError(str(result))
    return result




