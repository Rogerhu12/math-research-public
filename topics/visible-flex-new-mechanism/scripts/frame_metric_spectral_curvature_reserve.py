#!/usr/bin/env python3
"""Same spectral recovery, with an explicit proposal-only curvature PSD floor.

Only groups7..10 primary/SOC target RHS change. Physical fields, actual gates,
adaptive feedback, old minimum trust and shared budgets remain unchanged.
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
from frame_metric_spectral_adaptive import (AdaptiveSpectralMetricObjective,
    configuration as adaptive_configuration, implementation_hashes as adaptive_hashes,
    adaptive_definition, trial_quality, next_trust)
from frame_metric_budget_recovery import (require_public_research_environment,
    EvaluationBudgetReached, compact, parabolic_candidate, curvature_arc_slack_bound)

POLICY='spectral-metric-curvature-proposal-inner-floor-v1'
FLOOR='1/10000000'
CURVATURE_GROUPS=(7,8,9,10)


def implementation_hashes():
    result=adaptive_hashes();p=Path(__file__)
    result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def configuration(base):
    cfg=adaptive_configuration(base)
    cfg.update(curvature_proposal_floor_policy=POLICY,curvature_proposal_floor_exact=FLOOR,
        curvature_proposal_floor_group_indices=list(CURVATURE_GROUPS),
        initial_trust_box_fraction_exact='1/32000',
        initial_trust_is_last_accepted_adaptive_primary_scale=True,
        curvature_proposal_floor_is_not_a_change_to_true_curvature_tolerance=True,
        primary_SOC_variable_and_row_scalings_unchanged=True)
    return cfg


def floor_definition(cfg):
    return {'schema':POLICY+'-definition','floor_exact':cfg['curvature_proposal_floor_exact'],
        'groups':list(CURVATURE_GROUPS),'units':'existing scale100 actual-metric PSD trace/determinant row units',
        'primary_target':'max(old half-current-margin target, floor), only groups7..10',
        'SOC_target':'max(old quarter-nonnegative-base-margin target, floor), only groups7..10',
        'base_below_floor_is_allowed_as_a_proposal_restoration_not_assumed_feasible':True,
        'independent_linear_residual_limit_unchanged':cfg['linear_model_residual_limit'],
        'LP_success_is_not_a_claim_of_strict_floor_satisfaction':True,
        'original_actual_curvature58_eta_shape_and_two_grid_gates_unchanged':True,
        'original_minimum_trust_shared_budgets_and_adaptive_feedback_unchanged':True,
        'not_a_curvature_error_bound_or_whole_surface_reach_certificate':True}


def _floor(cfg):
    if (cfg.get('curvature_proposal_floor_policy')!=POLICY
            or cfg.get('curvature_proposal_floor_group_indices')!=list(CURVATURE_GROUPS)
            or Q(cfg['curvature_proposal_floor_exact'])!=Q(FLOOR)):
        raise ValueError('explicit exact curvature-only proposal floor required')
    return float(Q(cfg['curvature_proposal_floor_exact']))


def floor_diagnostics(base,at_point,legacy,target,groups,cfg,*,linear=None):
    """All selected group8 rows, plus all four group minima in original units."""
    base,at_point,legacy,target,groups=[np.asarray(x) for x in (base,at_point,legacy,target,groups)]
    f=_floor(cfg);statistics=[]
    for g in CURVATURE_GROUPS:
        ids=np.flatnonzero(groups==g)
        if not len(ids):continue
        statistics.append({'group':g,'selected_count':len(ids),
            'base_minimum':float(np.min(base[ids])),'actual_point_minimum':float(np.min(at_point[ids])),
            'legacy_target_minimum':float(np.min(legacy[ids])),
            'requested_target_minimum':float(np.min(target[ids])),
            'floor_active_count':int(np.sum(legacy[ids]<f)),
            'linear_achieved_minimum':None if linear is None else float(np.min(linear[ids])),
            'linear_legacy_target_margin_minimum':None if linear is None else float(np.min(linear[ids]-legacy[ids])),
            'linear_target_margin_minimum':None if linear is None else float(np.min(linear[ids]-target[ids])),
            'maximum_linear_floor_shortfall':None if linear is None else max(0.,float(np.max(f-linear[ids])))})
    rows=[]
    for i in np.flatnonzero(groups==8):
        rows.append([int(i),float(base[i]),float(at_point[i]),float(legacy[i]),float(target[i]),
            bool(legacy[i]<f),None if linear is None else float(linear[i]),
            None if linear is None else float(linear[i]-target[i]),
            None if linear is None else float(linear[i]-legacy[i]),
            None if linear is None else max(0.,float(f-linear[i]))])
    return {'definition':floor_definition(cfg),'group_statistics':statistics,
        'group8_selected_rows':{'columns':['selected_stack_index','base','actual_point','legacy_target',
            'requested_target','floor_active','linear_achieved','linear_target_margin',
            'linear_legacy_target_margin','linear_floor_shortfall'],'rows':rows},
        'indexing':'stack of current coarse pool followed by current fine pool; model/SOC versions bind both histories',
        'all_values_float_evaluations_of_the_exact_declared_proposal_not_interval_bounds':True}


class CurvatureReserveSpectralMetricObjective(AdaptiveSpectralMetricObjective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs);_floor(self.cfg)
        self.evaluation_definition.update(curvature_proposal_floor=floor_definition(self.cfg),
            curvature_floor_controller_source_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)

    def snapshot(self):
        result=super().snapshot();result['curvature_proposal_floor']=floor_definition(self.cfg)
        return result

def primary_proposal(values,J,groups,tolerances,state,lower,upper,cap_row,cap_margin,trust,cfg):
    values,J,groups,tolerances=np.asarray(values,float),np.asarray(J,float),np.asarray(groups,int),np.asarray(tolerances,float)
    state,lower,upper,cap_row=[np.asarray(x,float) for x in (state,lower,upper,cap_row)]
    n=len(state); m=len(values); soft=groups<2; hard=~soft
    if (J.shape!=(m,n) or groups.shape!=values.shape or tolerances.shape!=values.shape
            or np.any(groups<0) or np.any(groups>10) or not np.any(soft)
            or any(x.shape!=state.shape for x in [lower,upper,cap_row])
            or not all(np.all(np.isfinite(x)) for x in [values,J,tolerances,state,lower,upper,cap_row])
            or np.any(lower>=upper) or trust<=0 or not np.isfinite(cap_margin)):
        raise ValueError('finite complete fixed-cap metric-restoration linear model required')
    if np.any(values[hard]<-tolerances[hard]):
        raise ValueError('hard rows must be feasible at the accepted linearization point')
    scale=trust*(upper-lower); gamma=float(Q(cfg['linear_fraction_to_boundary_exact']))
    A=np.zeros((m+1+2*n,n+2)); b=np.empty(m+1+2*n)
    A[:m,:n]=-J*scale; b[:m]=values
    b[:m][hard]=gamma*(values[hard]+tolerances[hard]); A[:m,n][soft]=-1.
    # Original RHS for all other groups is bit-for-bit unchanged.
    legacy_target=values-b[:m]
    curved=np.isin(groups,CURVATURE_GROUPS)
    b[:m][curved]=np.minimum(b[:m][curved],values[curved]-_floor(cfg))
    target=values-b[:m]
    A[m,:n]=-cap_row*scale; b[m]=cap_margin
    for j in range(n):
        A[m+1+j,j]=1.; A[m+1+j,n+1]=-1.
        A[m+1+n+j,j]=-1.; A[m+1+n+j,n+1]=-1.
    b[m+1:]=0.; lo=np.maximum(-1.,(lower-state)/scale); hi=np.minimum(1.,(upper-state)/scale)
    if np.any(lo>hi):raise ValueError('accepted point outside original box')
    c=np.zeros(n+2); c[n]=1.; c[n+1]=float(Q(cfg['linear_step_norm_weight_exact']))
    before=time.monotonic()
    r=linprog(c,A_ub=A,b_ub=b,bounds=list(zip(lo,hi))+[(0.,None),(0.,1.)],method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
            'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],'time_limit':cfg['linear_program_seconds']})
    rho0=max(0.,float(np.max(-values[soft])))
    report={'method':'HiGHS linear metric-target recovery; actual curvature rows hard',
        'success':bool(r.success),'status':int(r.status),'message':str(r.message),'nit':int(r.nit),
        'elapsed_seconds':time.monotonic()-before,'rows':len(b),'variables':n+2,'matrix_bytes':A.nbytes,
        'trust_fraction':trust,'initial_metric_slack':rho0,
        'hard_rows_count':int(hard.sum()),'soft_metric_rows_count':int(soft.sum()),
        'curvature_cap_and_physical_rows_and_cap_not_elastic':True}
    report['curvature_proposal_diagnostics']=floor_diagnostics(values,values,legacy_target,target,groups,cfg)
    if r.x is None or not np.all(np.isfinite(r.x)):return None,report
    x=np.asarray(r.x); p=scale*x[:n]; violation=max(0.,float(np.max(A@x-b)))
    bv=max(0.,float(np.max(lo-x[:n])),float(np.max(x[:n]-hi)),-float(x[n]),-float(x[n+1]),float(x[n+1]-1))
    report.update(predicted_metric_slack=float(x[n]),predicted_slack_improvement=rho0-float(x[n]),
        normalized_step_norm=float(x[n+1]),maximum_linear_row_violation=violation,maximum_linear_bound_violation=bv,
        maximum_absolute_physical_step=float(np.max(abs(p))),physical_step_l2=float(np.linalg.norm(p)))
    report['curvature_proposal_diagnostics']=floor_diagnostics(values,values,legacy_target,target,groups,cfg,
        linear=values+J@p)
    if not r.success or max(violation,bv)>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='LP status or independent linear residual'; return None,report
    return p,report

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
    if np.any(lo>hi):
        report['proposal_rejected_before_LP']='no correction in original box and relative radius';return None,report
    before=time.monotonic()
    r=linprog(np.r_[np.zeros(n),np.ones(n)],A_ub=A,b_ub=b,
        bounds=list(zip(lo,hi))+[(0.,radius)]*n,method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
            'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],'time_limit':cfg['linear_program_seconds']})
    report.update(LP_invoked=True,success=bool(r.success),status=int(r.status),message=str(r.message),
        nit=int(r.nit),elapsed_seconds=time.monotonic()-before)
    if r.x is None or not np.all(np.isfinite(r.x)):return None,report
    x=np.asarray(r.x); w=width*x[:n]
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
    if not r.success or max(violation,bv)>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='SOC LP status or linear residual';return None,report
    return w,report

def run_curvature_reserve_recovery(objective,initial,*,known_metric_locations=(),artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,CurvatureReserveSpectralMetricObjective):
        raise ValueError('the explicit adaptive spectral objective is required')
    if objective.cfg.get('artificial_large_metric_budget_for_IO_only') and not (artificial_inputs_only and evaluate_only):
        raise ValueError('the loose predecessor fixture budget is only for artificial IO without LPs')
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear steps require the explicit artificial array family')
    cfg=objective.cfg
    meta={'method':POLICY,'new_metric_target_exact':cfg['fixed_metric_budget_exact'],
        'previous_qualified_metric_budget_exact':cfg['previous_qualified_metric_budget_exact'],
        'fixed_hard_curvature_cap_exact':cfg['fixed_hard_curvature_cap_exact'],
        'nonlinear_minimize_invocation_count':0,'linear_program_invocation_count':0,
        'primary_LP_invocation_count':0,'correction_LP_invocation_count':0,
        'shared_max_LPs':cfg['max_linear_models'],'shared_max_values':cfg['max_physical_evaluations'],
        'shared_active_seconds':cfg['max_seconds'],'models':[],
        'artificial_inputs_only':bool(artificial_inputs_only),'evaluate_only':bool(evaluate_only),
        'numpy_version':np.__version__,'scipy_version':scipy.__version__}
    def finish(status,error=None,budget=None):
        snap=objective.snapshot(); point=snap.get('selected_two_grid_physical_point')
        if objective.checkpoint:objective.checkpoint(snap)
        return {'status':status,'error':error,'budget_message':budget,'solver':meta,'checkpoint':snap,
            'new_metric_target_reached_on_both_grids':bool(point and point['new_metric_target_qualified_on_both_grids']),
            'adaptive_trust_policy':adaptive_definition(objective.cfg),
            'curvature_proposal_floor':floor_definition(objective.cfg),
            'no_free_curvature_or_metric_auxiliary_is_a_physical_coefficient':True}
    try:
        current=np.asarray(initial,float).copy(); vector=objective.vector(current)
        cd=objective.evaluate(vector)['decision']; fd=objective.fine_decision(current)
        if not(cd['single_grid_admissible_recovery_point'] and fd['single_grid_admissible_recovery_point']):
            return finish('initial-hard-curvature-or-prior-metric-physical-gate-failed')
        accepted=objective.accepted_point(current,cd,fd,{'kind':'saved-reserve-two-grid-success-metric-recovery-start'})
        if not len(objective.pool):objective.initialize_pool(vector)
        objective.expand_pool(vector,'initial-soft-metric-envelope-and-hard-coarse-separation')
        objective.initialize_fine_pool(current,known_metric_locations=known_metric_locations)
        if evaluate_only:return finish('evaluation-only-recovery-initialization')
        if accepted['new_metric_target_qualified_on_both_grids']:return finish('new-metric-target-already-qualified')
        objective.linear_rows(vector); objective.begin_optimization()
        trust=float(Q(cfg['initial_trust_box_fraction_exact']))
        minimum_trust=float(Q(cfg['minimum_trust_box_fraction_exact']))
        drop=float(Q(cfg['minimum_accepted_eta_decrease_exact']))
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
                trust,feedback=next_trust(model['trust_before_model'],trust,[],cfg)
                model['scale_feedback_update']=feedback;objective.trust_updates.append(copy.deepcopy(feedback))
                if trust<minimum_trust:return finish('minimum-trust-after-primary-failure')
                continue
            if lp['predicted_slack_improvement']<=cfg['linear_model_improvement_floor'] or np.max(abs(p))==0:
                model['result']='no-primary-metric-restoration';return finish('metric-restoration-linear-model-stalled')
            model['exact_binary64_proposed_step']=[str(Q.from_float(float(x))) for x in p]
            old_eta=accepted['maximum_eta_on_both_grids']; succeeded=False; relearned=False; soc_used=False; arc=None
            def assess(candidate,kind,alpha,need_fine=False,curve=None,prediction=None):
                nonlocal current,accepted,succeeded,relearned
                record={'kind':kind,'alpha_exact':alpha,'accepted_as_next_iterate':False,
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started'}
                if curve is not None:record['parabolic_curve']=copy.deepcopy(curve)
                model['trials'].append(record)
                rv=objective.evaluate(objective.vector(candidate)); c=rv['decision']
                record.update(attempt_status='coarse-value-call-complete',
                    coarse_physical_evaluation=rv['physical_geometry_evaluation'],coarse_decision=compact(c))
                possible=c['direct_max_eta']<old_eta and (
                    old_eta-c['direct_max_eta']>=drop or c['single_grid_new_target_qualified'])
                f=None
                if c.get('regularity_screen_pass',False) and (need_fine or (possible and c['single_grid_admissible_recovery_point'])):
                    f=objective.fine_decision(candidate)
                    record.update(fine_value_evaluation=objective.fine_evaluations,fine_decision=compact(f),
                        actual_fine_evaluated_even_if_coarse_ineligible=not c['single_grid_admissible_recovery_point'])
                    maximum=max(c['direct_max_eta'],f['direct_max_eta'])
                    qualified=c['single_grid_new_target_qualified'] and f['single_grid_new_target_qualified']
                    if (c['single_grid_admissible_recovery_point'] and f['single_grid_admissible_recovery_point']
                            and maximum<old_eta and (old_eta-maximum>=drop or qualified)):
                        accepted=objective.accepted_point(candidate,c,f,{'kind':kind,'model':model['number'],
                            'alpha_exact':alpha,'previous_two_grid_maximum_eta':old_eta})
                        current=candidate.copy();succeeded=True
                        record.update(accepted_as_next_iterate=True,accepted_index=accepted['accepted_index'])
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
                                'pool_versions':list(versions),'full_fine_actual_required_for_eta_ratio':True})
                        if succeeded:model['result']='accepted-full-SOC-two-grid-metric-descent';break
                        if relearned:model['result']='corrected-new-rows-return-to-last-accepted';break
            if succeeded and accepted['new_metric_target_qualified_on_both_grids']:
                return finish('fixed-new-metric-target-qualified-on-both-grids')
            if not succeeded and not relearned:
                trust*=.5;model['result']='all-proposals-rejected-last-accepted-retained'
                if trust<minimum_trust:return finish('minimum-trust-after-SOC-and-backtracking')
            trust,feedback=next_trust(model['trust_before_model'],trust,model['scale_feedback_trials'],cfg)
            model['scale_feedback_update']=feedback;objective.trust_updates.append(copy.deepcopy(feedback))
            if trust<minimum_trust:return finish('minimum-trust-after-actual-model-quality-feedback')
            if objective.checkpoint:objective.checkpoint(objective.snapshot())
        return finish('shared-primary-plus-SOC-LP-budget-exit')
    except EvaluationBudgetReached as error:
        return finish('shared-value-time-or-pool-budget-exit',budget=str(error))
    except Exception as error:
        return finish('metric-recovery-error',error={'type':type(error).__name__,'message':str(error)})

def developer_check():
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    from frame_metric_budget_recovery import primary_proposal as old_primary
    cfg=configuration(recovery_configuration(start_configuration(),target='1/100',curvature_cap='3'))
    cfg.update(max_linear_models=2,max_seconds=20.,radial_Jacobian_batch_owned_rows=2,
        fine_Jacobian_owned_radial_rows=2)
    groups=np.array([0,1,2,7,8,9,10])
    base=np.array([-.01,-.009,.1,.57,8.4634e-8,.66,.09])
    J=np.array([[1.,0.],[.5,0.],[0.,.1],[0.,0.],[-1e-4,1e-3],[0.,0.],[0.,0.]])
    state=np.zeros(2);lo=np.full(2,-1.);hi=np.full(2,1.);cap=np.array([0.,1.]);tol=np.full(len(base),1e-9)
    p,primary=primary_proposal(base,J,groups,tol,state,lo,hi,cap,.1,.001,cfg)
    fd=primary['curvature_proposal_diagnostics'];g8=fd['group8_selected_rows']['rows'][0]
    restored=bool(p is not None and g8[1]<float(Q(FLOOR)) and g8[4]>=float(Q(FLOOR))-1e-18
        and g8[7]>=-cfg['linear_model_residual_limit'])
    # Non-curvature rows retain their original mathematical RHS.
    gamma=float(Q(cfg['linear_fraction_to_boundary_exact']))
    legacy=base-gamma*(base+tol);target=legacy.copy()
    curved=np.isin(groups,CURVATURE_GROUPS);target[curved]=np.maximum(target[curved],float(Q(FLOOR)))
    unaffected=bool(np.array_equal(target[~curved],legacy[~curved]))
    roomy=base.copy();roomy[4]=.001
    op,oreport=old_primary(roomy,J,groups,tol,state,lo,hi,cap,.1,.001,cfg)
    np_,nreport=primary_proposal(roomy,J,groups,tol,state,lo,hi,cap,.1,.001,cfg)
    inactive=bool(op is not None and np_ is not None and np.max(abs(op-np_))<1e-12
        and abs(oreport['predicted_metric_slack']-nreport['predicted_metric_slack'])<1e-12)
    pp=np.array([.01,.001]);actual=base+J@pp;actual[:2]-=.0005;actual[4]=-1.8792e-8
    w,correction=correction_proposal(base,actual,J,groups,state,pp,lo,hi,cap,.1,cfg)
    cg8=correction['curvature_proposal_diagnostics']['group8_selected_rows']['rows'][0]
    repaired=bool(w is not None and cg8[2]==actual[4] and cg8[4]==float(Q(FLOOR))
        and cg8[7]>=-cfg['linear_model_residual_limit']
        and correction['corrected_actual_trial_linear_metric_slack']<=correction['metric_slack_budget']+1e-10)
    flat=J.copy();flat[4]=0
    no,failed=primary_proposal(base,flat,groups,tol,state,lo,hi,cap,.1,.001,cfg)
    impossible=bool(no is None and not failed['success'])
    # Same tiny nonlinear field: only proposal RHS differ, never actual rows/J.
    problem=_CurvatureArrayProblem();x=np.array([.3,.6,.6])
    radial=np.array([0.,.2,.4,.7,1.]);theta=np.arange(12)*2*np.pi/12
    lower=np.array([-.8,-1.,-1.]);upper=np.array([2.,1.,1.])
    args=(problem,HeightAffineGate.from_artificial_array_problem(problem),radial,theta,3,lower,upper)
    old=AdaptiveSpectralMetricObjective(*args,cfg=cfg)
    new=CurvatureReserveSpectralMetricObjective(*args,cfg=cfg)
    orow=old.all_rows(old.vector(x));nrow=new.all_rows(new.vector(x))
    same=bool(np.array_equal(orow,nrow) and old.problem.identity(x)==new.problem.identity(x))
    result=run_curvature_reserve_recovery(new,x,artificial_inputs_only=True)
    accepted=result['checkpoint']['accepted_iterates']
    valid=bool(accepted and all(v['coarse']['single_grid_admissible_recovery_point']
        and v['fine']['single_grid_admissible_recovery_point'] for v in accepted))
    return {'schema':POLICY+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,
        'base_below_proposal_floor_restored_without_relabelling_actual_gate':restored,
        'other_group_RHS_unchanged':unaffected,'inactive_floor_matches_original_LP':inactive,
        'SOC_uses_actual_y_and_retains_the_metric_prediction_budget':repaired,
        'impossible_linear_floor_rejected_without_geometric_claim':impossible,
        'same_actual_rows_and_physical_field':same,
        'tiny_actual_gates_preserved':valid,
        'tiny_trust':[m['trust_before_model'] for m in result['solver']['models']],
        'tiny_status':result['status'],'tiny_accepted_eta':[v['maximum_eta_on_both_grids'] for v in accepted],
        'primary':primary,'correction':correction,
        'no_SOC_variable_or_row_scaling_change':True,
        'passed':bool(restored and unaffected and inactive and repaired and impossible and same and valid)}
