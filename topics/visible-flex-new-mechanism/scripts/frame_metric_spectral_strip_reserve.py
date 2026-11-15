#!/usr/bin/env python3
"""Positive linear proposal reserve for the two normalized strip rows only.

No actual gate, physical field, value grid, curvature floor, shared budget,
physical step cost, growth rule, or SOC scaling changes in this module.
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
from frame_metric_spectral_trust_growth import (
    GrowingTrustSpectralMetricObjective,configuration as growth_configuration,
    implementation_hashes as growth_hashes,next_growth_trust,
    growth_definition,adaptive_definition)
from frame_metric_spectral_physical_penalty import (
    evaluated_penalty,penalty_definition,REFERENCE_WEIGHT,PHYSICAL_WEIGHT)
from frame_metric_spectral_curvature_reserve import (
    CURVATURE_GROUPS,_floor,floor_definition,floor_diagnostics)
from frame_metric_spectral_adaptive import trial_quality
from frame_metric_budget_recovery import (
    require_public_research_environment,EvaluationBudgetReached,
    compact,parabolic_candidate,curvature_arc_slack_bound)

POLICY='spectral-metric-normalized-strip-proposal-reserve-v1'
STRIP_FLOOR='1/10000000'
STRIP_GROUPS=(4,5)


def implementation_hashes():
    result=growth_hashes();p=Path(__file__)
    result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def configuration(base):
    cfg=growth_configuration(base)
    cfg.update(strip_proposal_floor_policy=POLICY,
        strip_proposal_floor_exact=STRIP_FLOOR,
        strip_proposal_floor_group_indices=list(STRIP_GROUPS),
        strip_proposal_floor_does_not_change_actual_strip_or_tolerance=True,
        new_strip_stage_inherits_restored_actual_controller_state=True)
    return cfg


def strip_floor_definition(cfg):
    if (cfg.get('strip_proposal_floor_policy')!=POLICY
            or cfg.get('strip_proposal_floor_group_indices')!=list(STRIP_GROUPS)
            or Q(cfg['strip_proposal_floor_exact'])!=Q(STRIP_FLOOR)):
        raise ValueError('explicit exact strip-only proposal reserve required')
    p=Q(cfg['hard_strip_half_width_exact'])
    if p<=0:raise ValueError('positive existing strip half-width required')
    return {'schema':POLICY+'-definition','floor_exact':STRIP_FLOOR,
        'groups':list(STRIP_GROUPS),'row_functions':['1-X_y/p','1+X_y/p'],
        'units':'dimensionless original normalized strip row, not absolute y',
        'existing_strip_half_width_exact':str(p),
        'linear_inward_length_equivalent_exact':str(p*Q(STRIP_FLOOR)),
        'primary_target':'max(original target, strip floor); RHS=min(original RHS, base-floor)',
        'SOC_target':'max(original retained base target, strip floor); RHS=actual_y-target',
        'SOC_step_is_correction_w_from_the_already_evaluated_y':True,
        'base_below_floor_is_allowed_for_proposal_restoration':True,
        'all_non_strip_rows_and_all_LP_objectives_bounds_and_scalings_unchanged':True,
        'actual_strip_tolerance_unchanged':cfg['shape_constraint_tolerance'],
        'independent_linear_residual_limit_unchanged':cfg['linear_model_residual_limit'],
        'LP_success_is_not_a_claim_of_strict_floor_satisfaction':True,
        'all_original_actual_two_grid_gates_and_strict_eta_descent_unchanged':True,
        'original_growth_shrink_mintrust_and_shared_budgets_unchanged':True,
        'not_a_nonlinear_error_bound_or_continuous_shape_certificate':True}


def _strip_floor(cfg):
    strip_floor_definition(cfg);return float(Q(STRIP_FLOOR))


def strip_diagnostics(base,at_point,old_target,new_target,groups,cfg,*,linear=None):
    """Original row units; no successful LP is promoted to a strict floor."""
    base,at_point,old_target,new_target,groups=[
        np.asarray(x) for x in (base,at_point,old_target,new_target,groups)]
    f=_strip_floor(cfg);p=float(Q(cfg['hard_strip_half_width_exact']));records=[]
    for g in STRIP_GROUPS:
        ids=np.flatnonzero(groups==g)
        if not len(ids):continue
        record={'group':g,'selected_count':int(len(ids)),
            'base_minimum':float(np.min(base[ids])),
            'actual_point_minimum':float(np.min(at_point[ids])),
            'old_target_minimum':float(np.min(old_target[ids])),
            'new_target_minimum':float(np.min(new_target[ids])),
            'floor_active_count':int(np.sum(old_target[ids]<f)),
            'largest_RHS_tightening':float(np.max(new_target[ids]-old_target[ids])),
            'linear_achieved_minimum':None,
            'linear_old_target_margin_minimum':None,
            'linear_new_target_margin_minimum':None,
            'maximum_linear_floor_shortfall':None,
            'linear_inward_length_minimum':None}
        if linear is not None:
            values=np.asarray(linear)[ids]
            record.update(linear_achieved_minimum=float(np.min(values)),
                linear_old_target_margin_minimum=float(np.min(values-old_target[ids])),
                linear_new_target_margin_minimum=float(np.min(values-new_target[ids])),
                maximum_linear_floor_shortfall=max(0.,float(np.max(f-values))),
                linear_inward_length_minimum=p*float(np.min(values)))
        records.append(record)
    return {'definition':strip_floor_definition(cfg),'group_statistics':records,
        'selected_stack':'all current coarse selected rows then current fine selected rows',
        'no_actual_shape_gate_is_inferred_from_these_linear_statistics':True}


class StripReserveSpectralMetricObjective(GrowingTrustSpectralMetricObjective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs);strip_floor_definition(self.cfg)
        self.evaluation_definition.update(strip_proposal_floor=strip_floor_definition(self.cfg),
            strip_reserve_controller_source_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)

    def snapshot(self):
        result=super().snapshot()
        result['strip_proposal_floor']=strip_floor_definition(self.cfg);return result


def compact_with_strip_gate(decision):
    """Retain actual failure reasons already calculated, with no geometry call."""
    out=compact(decision)
    for key in ['hard_strip_pass','hard_ball_pass','signed_height_pass',
            'independent_direct_curvature_pass','curvature_scaled_PSD_row_pass',
            'mirror_polynomial_pass','independent_direct_mirror_radius_pass',
            'shape_constraint_tolerance','hard_strip_half_width_exact']:
        if key in decision:out[key]=copy.deepcopy(decision[key])
    p=decision.get('hard_strip_half_width_exact');y=decision.get('maximum_absolute_y')
    if p is not None and y is not None:
        out['normalized_strip_row_minimum']=1-float(y)/float(Q(p))
    return out


def _reserve_primary_proposal(values,J,groups,tolerances,state,lower,upper,cap_row,cap_margin,trust,cfg):
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
    target_before_strip=values-b[:m]
    strip=np.isin(groups,STRIP_GROUPS)
    b[:m][strip]=np.minimum(b[:m][strip],values[strip]-_strip_floor(cfg))
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
    report['strip_proposal_diagnostics']=strip_diagnostics(values,values,target_before_strip,target,groups,cfg)
    if r.x is None or not np.all(np.isfinite(r.x)):return None,report
    x=np.asarray(r.x); p=scale*x[:n]; violation=max(0.,float(np.max(A@x-b)))
    bv=max(0.,float(np.max(lo-x[:n])),float(np.max(x[:n]-hi)),-float(x[n]),-float(x[n+1]),float(x[n+1]-1))
    report.update(predicted_metric_slack=float(x[n]),predicted_slack_improvement=rho0-float(x[n]),
        normalized_step_norm=float(x[n+1]),maximum_linear_row_violation=violation,maximum_linear_bound_violation=bv,
        maximum_absolute_physical_step=float(np.max(abs(p))),physical_step_l2=float(np.linalg.norm(p)))
    report['curvature_proposal_diagnostics']=floor_diagnostics(values,values,legacy_target,target,groups,cfg,
        linear=values+J@p)
    report['strip_proposal_diagnostics']=strip_diagnostics(values,values,target_before_strip,target,groups,cfg,
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
    report['strip_proposal_diagnostics']=strip_diagnostics(base,trial,target_before_strip,target,groups,cfg,
        linear=trial+J@w)
    if not r.success or max(violation,bv)>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='SOC LP status or linear residual';return None,report
    return w,report


def primary_proposal(values,J,groups,tolerances,state,lower,upper,cap_row,cap_margin,trust,cfg):
    penalty=evaluated_penalty(cfg,trust)
    local=dict(cfg,linear_step_norm_weight_exact=penalty['effective_normalized_weight_exact'])
    # Exactly the published physical norm cost; only strip RHS has a new floor.
    p,report=_reserve_primary_proposal(values,J,groups,tolerances,state,lower,upper,cap_row,cap_margin,trust,local)
    if report.get('normalized_step_norm') is not None:
        z=report['normalized_step_norm'];rho=report['predicted_metric_slack']
        cost=penalty['effective_normalized_weight_evaluated']*z
        penalty.update(returned_LP_norm_auxiliary=z,returned_primary_step_cost=cost,
            old_constant_normalized_cost_at_the_same_returned_auxiliary=float(Q(REFERENCE_WEIGHT))*z,
            returned_weighted_objective=rho+cost,
            returned_predicted_metric_slack=rho,
            predicted_metric_slack_improvement=report['predicted_slack_improvement'])
    if p is not None:
        width=np.asarray(upper,float)-np.asarray(lower,float)
        physical_norm=float(np.max(abs(p)/width))
        penalty.update(actual_physical_box_normalized_step_norm=physical_norm,
            actual_trust_normalized_step_norm=physical_norm/float(trust),
            physical_norm_cost_evaluated=float(Q(PHYSICAL_WEIGHT))*physical_norm)
    report['primary_step_cost_diagnostic']=penalty
    return p,report


def controller_continuation(cfg,value,*,artificial=False):
    """A separate evaluated controller state, never a physical coefficient."""
    if value is None:
        if not artificial:raise ValueError('actual restored controller continuation required')
        value={'schema':'restored-growth-controller-continuation-v1',
            'trust_binary64_exact':str(Q.from_float(float(Q(cfg['initial_trust_box_fraction_exact'])))),
            'success_streak':0,'origin':'artificial no-prefix seed only'}
    if value.get('schema')!='restored-growth-controller-continuation-v1':
        raise ValueError('explicit restored controller continuation schema required')
    q=Q(value['trust_binary64_exact']);radius=float(q);streak=value['success_streak']
    if (not np.isfinite(radius) or radius<=0 or Q.from_float(radius)!=q
            or radius>float(Q(cfg['trust_growth_maximum_box_fraction_exact']))
            or type(streak) is not int or not 0<=streak<cfg['trust_growth_required_consecutive_models']):
        raise ValueError('finite exact binary64 inherited radius and bounded integer streak required')
    return radius,streak,copy.deepcopy(value)


def run_strip_reserve_recovery(objective,initial,*,known_metric_locations=(),continuation_state=None,artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,StripReserveSpectralMetricObjective):
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
        accepted=objective.accepted_point(current,cd,fd,{'kind':'temporary-restored-growth-two-grid-success-strip-start'})
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
            def assess(candidate,kind,alpha,need_fine=False,curve=None,prediction=None):
                nonlocal current,accepted,succeeded,relearned
                record={'kind':kind,'alpha_exact':alpha,'accepted_as_next_iterate':False,
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started'}
                if curve is not None:record['parabolic_curve']=copy.deepcopy(curve)
                model['trials'].append(record)
                rv=objective.evaluate(objective.vector(candidate)); c=rv['decision']
                record.update(attempt_status='coarse-value-call-complete',
                    coarse_physical_evaluation=rv['physical_geometry_evaluation'],coarse_decision=compact_with_strip_gate(c))
                possible=c['direct_max_eta']<old_eta and (
                    old_eta-c['direct_max_eta']>=drop or c['single_grid_new_target_qualified'])
                f=None
                if c.get('regularity_screen_pass',False) and (need_fine or (possible and c['single_grid_admissible_recovery_point'])):
                    f=objective.fine_decision(candidate)
                    record.update(fine_value_evaluation=objective.fine_evaluations,fine_decision=compact_with_strip_gate(f),
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
    """Only the new proposal rows, diagnostics and unchanged real-gate wiring."""
    from types import SimpleNamespace
    from unittest.mock import patch
    import sys
    import frame_metric_spectral_curvature_reserve as old_reserve
    import frame_metric_spectral_physical_penalty as old_physical
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    cfg=configuration(recovery_configuration(start_configuration(),target='1/100',curvature_cap='3'))
    cfg.update(max_linear_models=1,max_seconds=20.,radial_Jacobian_batch_owned_rows=2,
        fine_Jacobian_owned_radial_rows=2)
    groups=np.array([0,1,2,3,4,5,6,7,8,9,10,4,5])
    base=np.array([-.01,-.009,.1,.2,-2e-10,2e-7,.1,.57,8.4e-8,.66,.09,.3,.4])
    n=3;m=len(base);J=np.arange(m*n,dtype=float).reshape(m,n)*1e-4
    J[0]=[1.,0.,0.];J[1]=[.5,0.,0.]
    state=np.zeros(n);lo=np.full(n,-1.);hi=np.ones(n)
    cap=np.array([0.,1.,0.]);tol=np.full(m,1e-9);radius=float(Q('1/64000'))
    original=[v.copy() for v in (base,J,groups,state,lo,hi,cap,tol)]
    def capture(module,call):
        calls=[]
        def stopped(c,**kwargs):
            calls.append({'c':np.asarray(c).copy(),'A':np.asarray(kwargs['A_ub']).copy(),
                'b':np.asarray(kwargs['b_ub']).copy(),'bounds':copy.deepcopy(kwargs['bounds']),
                'method':kwargs['method'],'options':copy.deepcopy(kwargs['options'])})
            return SimpleNamespace(success=False,status=2,message='artificial capture: no solve',nit=0,x=None)
        with patch.object(module,'linprog',side_effect=stopped):
            result=call()
        if len(calls)!=1:raise AssertionError('exactly one requested LP capture')
        return calls[0],result[1]
    args=(base,J,groups,tol,state,lo,hi,cap,.1,radius,cfg)
    oldp,old_report=capture(old_reserve,lambda:old_physical.primary_proposal(*args))
    newp,new_report=capture(sys.modules[__name__],lambda:primary_proposal(*args))
    selected=np.isin(groups,STRIP_GROUPS);not_selected=np.r_[~selected,np.ones(1+2*n,dtype=bool)]
    expected=oldp['b'].copy()
    expected[:m][selected]=np.minimum(expected[:m][selected],base[selected]-float(Q(STRIP_FLOOR)))
    primary_rhs=bool(np.array_equal(newp['b'],expected) and np.array_equal(newp['b'][not_selected],oldp['b'][not_selected]))
    primary_other=bool(np.array_equal(newp['A'],oldp['A']) and np.array_equal(newp['c'],oldp['c'])
        and newp['bounds']==oldp['bounds'] and newp['options']==oldp['options'] and newp['method']==oldp['method'])
    step=np.array([.001,.0001,0.]);trial=base+J@step
    trial[:2]-=.0002;trial[4]=-1.1e-9;trial[5]=-8e-10
    socargs=(base,trial,J,groups,state,step,lo,hi,cap,.1+float(cap@step),cfg)
    olds,old_soc=capture(old_reserve,lambda:old_reserve.correction_proposal(*socargs))
    news,new_soc=capture(sys.modules[__name__],lambda:correction_proposal(*socargs))
    expected=olds['b'].copy()
    old_targets=trial-olds['b'][:m]
    expected[:m][selected]=trial[selected]-np.maximum(old_targets[selected],float(Q(STRIP_FLOOR)))
    SOC_rhs=bool(np.array_equal(news['b'],expected) and np.array_equal(news['b'][not_selected],olds['b'][not_selected]))
    SOC_other=bool(np.array_equal(news['A'],olds['A']) and np.array_equal(news['c'],olds['c'])
        and news['bounds']==olds['bounds'] and news['options']==olds['options'])
    actual_y=bool(news['b'][m]==.1+float(cap@step)
        and np.array_equal(news['b'][:m][groups<2],trial[groups<2]+new_soc['metric_slack_budget']))
    unchanged_curvature=bool(old_report['curvature_proposal_diagnostics']==new_report['curvature_proposal_diagnostics']
        and old_soc['curvature_proposal_diagnostics']==new_soc['curvature_proposal_diagnostics'])
    immutable=all(np.array_equal(a,b) for a,b in zip(original,(base,J,groups,state,lo,hi,cap,tol)))
    # One small real array LP checks the implemented RHS through HiGHS.
    small_groups=np.array([0,1,4,5,8])
    small_base=np.array([-.01,-.009,-2e-10,.1,.01])
    small_J=np.array([[1.,0.],[.5,0.],[0.,1.],[0.,-1.],[0.,0.]])
    p,solved=primary_proposal(small_base,small_J,small_groups,np.full(5,1e-9),
        np.zeros(2),np.full(2,-1.),np.ones(2),np.zeros(2),.1,.01,cfg)
    tiny_solve=bool(p is not None and solved['success']
        and solved['maximum_linear_row_violation']<=cfg['linear_model_residual_limit']
        and small_base[2]+small_J[2]@p>=float(Q(STRIP_FLOOR))-1e-8)
    # Artificial successful primal with a residual below the unchanged limit:
    # its positive floor shortfall MUST remain visible rather than called strict.
    labels=np.array([0,1,4,5,8]);values=np.array([-.01,-.009,9.8e-8,.1,.01])
    zeroJ=np.zeros((5,1))
    def approximate_primal(*args,**kwargs):
        return SimpleNamespace(success=True,status=0,message='injected approximate LP primal',nit=1,
            x=np.array([0.,.01,0.]))
    with patch.object(sys.modules[__name__],'linprog',side_effect=approximate_primal):
        unused,approx=primary_proposal(values,zeroJ,labels,np.full(5,1e-9),np.zeros(1),
            np.array([-1.]),np.array([1.]),np.zeros(1),.1,radius,cfg)
    group4=next(r for r in approx['strip_proposal_diagnostics']['group_statistics'] if r['group']==4)
    honest_residual=bool(unused is not None and approx['maximum_linear_row_violation']>0
        and group4['maximum_linear_floor_shortfall']>0
        and group4['linear_new_target_margin_minimum']<0)
    pstrip=float(Q(cfg['hard_strip_half_width_exact']));epsilon=cfg['shape_constraint_tolerance']
    normalized_gate=bool(1-(pstrip+pstrip*epsilon/2)/pstrip>=-epsilon
        and 1-(pstrip+2*pstrip*epsilon)/pstrip < -epsilon)
    # No old growth solve: compare all actual rows for one artificial array state.
    problem=_CurvatureArrayProblem();x=np.array([.3,.6,.6])
    radial=np.array([0.,.2,.4,.7,1.]);theta=np.arange(12)*2*np.pi/12
    args=(problem,HeightAffineGate.from_artificial_array_problem(problem),radial,theta,3,
        np.array([-.8,-1.,-1.]),np.array([2.,1.,1.]))
    old=GrowingTrustSpectralMetricObjective(*args,cfg=cfg)
    new=StripReserveSpectralMetricObjective(*args,cfg=cfg)
    actual_rows=bool(np.array_equal(old.all_rows(old.vector(x)),new.all_rows(new.vector(x)))
        and problem.identity(x)==new.problem.identity(x))
    reason_source={'single_grid_hard_gate_pass':False,'hard_strip_pass':False,
        'hard_strip_half_width_exact':'38999/100000','maximum_absolute_y':.38999000045}
    reason=compact_with_strip_gate(reason_source)
    reasons=bool(reason['hard_strip_pass'] is False and reason['normalized_strip_row_minimum'] < -1e-9)
    inherited={'schema':'restored-growth-controller-continuation-v1',
        'trust_binary64_exact':str(Q.from_float(float(Q('1/32000')))),
        'success_streak':1,'origin':'artificial partial model'}
    inherited_before=copy.deepcopy(inherited)
    ir,ist,idef=controller_continuation(cfg,inherited,artificial=True)
    continuation_ok=bool(ir==float(Q('1/32000')) and ist==1
        and inherited==inherited_before and idef==inherited)
    try:controller_continuation(cfg,None,artificial=False);missing_continuation_rejected=False
    except ValueError:missing_continuation_rejected=True
    checks={'inherited_actual_radius_and_streak_not_reset':continuation_ok,
        'real_continuation_cannot_silently_use_seed':missing_continuation_rejected,
        'primary_only_4_5_RHS_strengthened':primary_rhs,
        'primary_matrix_objective_cap_box_scaling_unchanged':primary_other,
        'SOC_only_4_5_RHS_strengthened':SOC_rhs,
        'SOC_matrix_objective_box_scaling_unchanged':SOC_other,
        'SOC_uses_same_actual_y_without_double_primary_step':actual_y,
        'old_curvature_floor_diagnostics_unchanged':unchanged_curvature,
        'input_arrays_not_mutated':immutable,'one_tiny_real_array_LP_passed':tiny_solve,
        'approximate_primal_floor_shortfall_not_hidden':honest_residual,
        'actual_strip_gate_keeps_original_normalized_tolerance':normalized_gate,
        'all_actual_geometry_rows_and_physical_identity_unchanged':actual_rows,
        'trial_compact_preserves_existing_strip_failure':reasons}
    return {'schema':POLICY+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,
        'old_growth_development_or_actual_not_repeated':True,'checks':checks,
        'tiny_primary_status':solved['status'],'tiny_primary_max_linear_residual':solved.get('maximum_linear_row_violation'),
        'tiny_strip_diagnostics':solved['strip_proposal_diagnostics'],
        'injected_approximate_primal_strip_floor_shortfall':group4['maximum_linear_floor_shortfall'],
        'passed':bool(all(checks.values()))}
