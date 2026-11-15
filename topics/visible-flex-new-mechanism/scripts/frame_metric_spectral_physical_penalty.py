#!/usr/bin/env python3
"""Same two-grid spectral recovery with a trust-independent physical step cost.

Only the primary LP objective coefficient changes. The existing curvature
proposal floor, SOC constraints/controller, true gates and budgets remain.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time
import numpy as np
import scipy

from frame_collar_residual_audit import digest
from frame_metric_spectral_curvature_reserve import (
    CurvatureReserveSpectralMetricObjective,configuration as reserve_configuration,
    implementation_hashes as reserve_hashes,primary_proposal as reserve_primary,
    correction_proposal,floor_definition)
from frame_metric_spectral_adaptive import adaptive_definition,trial_quality,next_trust
from frame_metric_budget_recovery import (require_public_research_environment,
    EvaluationBudgetReached,compact,parabolic_candidate,curvature_arc_slack_bound)

POLICY='spectral-metric-trust-independent-physical-step-cost-v1'
REFERENCE_TRUST='1/1000'
REFERENCE_WEIGHT='1/1000000'
PHYSICAL_WEIGHT='1/1000'


def implementation_hashes():
    result=reserve_hashes();p=Path(__file__)
    result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def configuration(base):
    cfg=reserve_configuration(base)
    cfg.pop('initial_trust_is_last_accepted_adaptive_primary_scale',None)
    cfg.update(primary_physical_step_cost_policy=POLICY,
        step_cost_reference_trust_exact=REFERENCE_TRUST,
        step_cost_reference_normalized_weight_exact=REFERENCE_WEIGHT,
        step_cost_physical_box_norm_coefficient_exact=PHYSICAL_WEIGHT,
        initial_trust_box_fraction_exact='1/64000',
        initial_trust_is_last_accepted_curvature_reserve_primary_scale=True,
        linear_step_norm_weight_is_reference_only_primary_uses_runtime_physical_penalty=True,
        primary_step_cost_is_not_a_geometric_tolerance=True,
        curvature_floor_SOC_actual_gates_and_all_budgets_unchanged=True)
    return cfg


def penalty_definition(cfg):
    if (cfg.get('primary_physical_step_cost_policy')!=POLICY
            or Q(cfg['step_cost_reference_trust_exact'])!=Q(REFERENCE_TRUST)
            or Q(cfg['step_cost_reference_normalized_weight_exact'])!=Q(REFERENCE_WEIGHT)
            or Q(cfg['step_cost_physical_box_norm_coefficient_exact'])!=Q(PHYSICAL_WEIGHT)):
        raise ValueError('explicit calibrated physical-step cost required')
    return {'schema':POLICY+'-definition','reference_trust_exact':REFERENCE_TRUST,
        'reference_normalized_weight_exact':REFERENCE_WEIGHT,
        'physical_box_norm_coefficient_exact':PHYSICAL_WEIGHT,
        'primary_objective':'rho + (reference_weight*trust/reference_trust)*z; |p/(trust*box_width)|<=z<=1',
        'equivalent_positive_weight_optimal_objective':'rho + physical_weight*max_j|p_j/box_width_j|',
        'same_reference_radius_cost_as_the_original_controller':True,
        'rho_bias_bound_given_exact_weighted_LP_optimality':'0<=rho_returned-rho_min_only<=effective_weight',
        'floating_HiGHS_status_and_residuals_do_not_certify_exact_LP_optimality':True,
        'no_second_LP_or_changed_constraint_or_acceptance_threshold':True,
        'physical_model_and_all_SOC_rows_and_objective_unchanged':True}


def evaluated_penalty(cfg,trust):
    definition=penalty_definition(cfg)
    if not np.isfinite(trust) or trust<=0:raise ValueError('finite positive current trust required')
    radius=Q.from_float(float(trust))
    weight=Q(REFERENCE_WEIGHT)*radius/Q(REFERENCE_TRUST)
    return {'definition':definition,'current_trust_binary64_exact':str(radius),
        'current_trust_evaluated':float(trust),'effective_normalized_weight_exact':str(weight),
        'effective_normalized_weight_evaluated':float(weight),
        'physical_box_norm_coefficient_evaluated':float(Q(PHYSICAL_WEIGHT)),
        'rho_bias_bound_if_exact_weighted_optimum_evaluated':float(weight),
        'old_implied_physical_norm_coefficient_evaluated':float(Q(REFERENCE_WEIGHT))/float(trust)}


class PhysicalPenaltySpectralMetricObjective(CurvatureReserveSpectralMetricObjective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.evaluation_definition.update(primary_physical_step_cost=penalty_definition(self.cfg),
            physical_penalty_controller_source_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)

    def snapshot(self):
        result=super().snapshot()
        result['primary_physical_step_cost']=penalty_definition(self.cfg)
        return result


def primary_proposal(values,J,groups,tolerances,state,lower,upper,cap_row,cap_margin,trust,cfg):
    penalty=evaluated_penalty(cfg,trust)
    local=dict(cfg,linear_step_norm_weight_exact=penalty['effective_normalized_weight_exact'])
    # Existing library constructs every row/RHS/bound and runs the only LP.
    # Its independent residual tests and all curvature-floor diagnostics remain.
    p,report=reserve_primary(values,J,groups,tolerances,state,lower,upper,cap_row,cap_margin,trust,local)
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


def run_physical_penalty_recovery(objective,initial,*,known_metric_locations=(),artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,PhysicalPenaltySpectralMetricObjective):
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
            'primary_physical_step_cost':penalty_definition(objective.cfg),
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
    """New objective coefficient and its call path, using artificial data only."""
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    cfg=configuration(recovery_configuration(start_configuration(),target='1/100',curvature_cap='3'))
    cfg.update(max_linear_models=2,max_seconds=20.,radial_Jacobian_batch_owned_rows=2,
        fine_Jacobian_owned_radial_rows=2)
    groups=np.array([0,1,8]);values=np.array([-.01,-.009,.001])
    J=np.array([[.02],[.02],[0.]])
    state=np.zeros(1);lower=np.array([-1.]);upper=np.array([1.]);cap=np.zeros(1)
    tol=np.full(3,1e-9);radius=1e-5
    old_p,old_report=reserve_primary(values,J,groups,tol,state,lower,upper,cap,.1,radius,cfg)
    new_p,new_report=primary_proposal(values,J,groups,tol,state,lower,upper,cap,.1,radius,cfg)
    analytic_rho_min=.01-.02*(2*radius)
    old_stops_new_moves=bool(old_p is not None and new_p is not None and abs(old_p[0])<1e-12
        and abs(new_p[0]-2*radius)<1e-12
        and new_report['predicted_metric_slack']<old_report['predicted_metric_slack'])
    gap=new_report['predicted_metric_slack']-analytic_rho_min
    bound=new_report['primary_step_cost_diagnostic']['rho_bias_bound_if_exact_weighted_optimum_evaluated']
    bias_matches_known_toy=bool(-1e-12<=gap<=bound+1e-12)
    reference=float(Q(REFERENCE_TRUST))
    rp,rr=reserve_primary(values,J,groups,tol,state,lower,upper,cap,.1,reference,cfg)
    np_,nr=primary_proposal(values,J,groups,tol,state,lower,upper,cap,.1,reference,cfg)
    reference_match=bool(rp is not None and np_ is not None and np.array_equal(rp,np_)
        and rr['predicted_metric_slack']==nr['predicted_metric_slack']
        and nr['primary_step_cost_diagnostic']['effective_normalized_weight_evaluated']==float(Q(REFERENCE_WEIGHT)))
    fixed_physical_norm=Q(1,2000000)
    exact_costs=[]
    for radius_exact in [Q(1,32000),Q(1,64000),Q(1,100000)]:
        z=fixed_physical_norm/radius_exact
        exact_costs.append(Q(REFERENCE_WEIGHT)*radius_exact/Q(REFERENCE_TRUST)*z)
    invariant=all(c==Q(PHYSICAL_WEIGHT)*fixed_physical_norm for c in exact_costs)
    # One selected curvature row is below the proposal floor but within the
    # original true gate. Its restoration and SOC are the unchanged library.
    groups2=np.array([0,1,2,7,8,9,10]);base=np.array([-.01,-.009,.1,.57,8.4634e-8,.66,.09])
    J2=np.array([[1.,0.],[.5,0.],[0.,.1],[0.,0.],[-1e-4,1e-3],[0.,0.],[0.,0.]])
    state2=np.zeros(2);lo=np.full(2,-1.);hi=np.full(2,1.);cap2=np.array([0.,1.]);tol2=np.full(7,1e-9)
    p,primary=primary_proposal(base,J2,groups2,tol2,state2,lo,hi,cap2,.1,1/64000,cfg)
    g8=primary['curvature_proposal_diagnostics']['group8_selected_rows']['rows'][0]
    floor_preserved=bool(p is not None and g8[4]>=1e-7-1e-18 and g8[7]>=-cfg['linear_model_residual_limit'])
    pp=np.array([.01,.001]);actual=base+J2@pp;actual[:2]-=.0005;actual[4]=-1.8792e-8
    w,correction=correction_proposal(base,actual,J2,groups2,state2,pp,lo,hi,cap2,.1,cfg)
    soc_preserved=bool(w is not None and correction['residual_source']=='actual same y on both full grids'
        and correction['corrected_actual_trial_linear_metric_slack']<=correction['metric_slack_budget']+1e-10)
    problem=_CurvatureArrayProblem();x=np.array([.3,.6,.6])
    radial=np.array([0.,.2,.4,.7,1.]);theta=np.arange(12)*2*np.pi/12
    args=(problem,HeightAffineGate.from_artificial_array_problem(problem),radial,theta,3,
        np.array([-.8,-1.,-1.]),np.array([2.,1.,1.]))
    old=CurvatureReserveSpectralMetricObjective(*args,cfg=cfg)
    new=PhysicalPenaltySpectralMetricObjective(*args,cfg=cfg)
    unchanged=bool(np.array_equal(old.all_rows(old.vector(x)),new.all_rows(new.vector(x)))
        and old.problem.identity(x)==new.problem.identity(x))
    result=run_physical_penalty_recovery(new,x,artificial_inputs_only=True)
    accepted=result['checkpoint']['accepted_iterates']
    valid=bool(accepted and all(v['coarse']['single_grid_admissible_recovery_point']
        and v['fine']['single_grid_admissible_recovery_point'] for v in accepted))
    no_extra_LP=bool(result['solver']['linear_program_invocation_count']
        ==result['solver']['primary_LP_invocation_count']+result['solver']['correction_LP_invocation_count']
        <=cfg['max_linear_models'])
    return {'schema':POLICY+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,
        'reference_radius_same_primary_solution':reference_match,
        'small_radius_old_stops_new_moves_in_known_one_variable_LP':old_stops_new_moves,
        'known_pure_metric_LP_optimum':analytic_rho_min,'new_returned_rho_gap':gap,
        'conditional_exact_optimality_bound_evaluated':bound,
        'conditional_gap_matches_known_artificial_optimum':bias_matches_known_toy,
        'exact_fixed_physical_norm_cost_independent_of_trust':invariant,
        'unchanged_proposal_curvature_floor':floor_preserved,'unchanged_SOC_actual_residual_path':soc_preserved,
        'same_actual_rows_and_physical_field':unchanged,'tiny_actual_gates_preserved':valid,
        'tiny_total_LPs_equal_primary_plus_SOC':no_extra_LP,'tiny_status':result['status'],
        'tiny_accepted_eta':[v['maximum_eta_on_both_grids'] for v in accepted],
        'old_small_radius_primary':old_report,'new_small_radius_primary':new_report,
        'primary':primary,'correction':correction,
        'passed':bool(reference_match and old_stops_new_moves and bias_matches_known_toy and invariant
            and floor_preserved and soc_preserved and unchanged and valid and no_extra_LP)}

