#!/usr/bin/env python3
"""Spectral metric recovery with recorded actual-model trust feedback.

Only the controller scale policy changes. The physical family, spectral rows,
complete coarse/fine Jacobians, all actual gates and shared budgets are kept.
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
from frame_metric_spectral_recovery import (SpectralMetricRecoveryObjective,
    implementation_hashes as spectral_hashes, configuration as spectral_configuration)
from frame_metric_budget_recovery import (require_public_research_environment,
    EvaluationBudgetReached, primary_proposal, correction_proposal, compact,
    parabolic_candidate, curvature_arc_slack_bound)

POLICY='fixed-curvature-two-grid-spectral-adaptive-scale-v1'


def implementation_hashes():
    result=spectral_hashes();p=Path(__file__)
    result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def configuration(base):
    cfg=spectral_configuration(base)
    cfg.update(adaptive_scale_policy=POLICY,initial_trust_box_fraction_exact='1/4000',
        adaptive_eta_model_ratio_threshold_exact='1/4',adaptive_trust_shrink_factor_exact='1/2',
        adaptive_trust_never_increases=True,
        adaptive_initial_scale_is_a_new_proposal_choice_not_a_physical_change=True,
        curvature_feedback_uses_original_direct_gate_tolerance=True,
        extra_fine_values_for_feedback_are_not_requested=True)
    return cfg


def adaptive_definition(cfg):
    return {'schema':POLICY+'-definition','initial_trust_box_fraction_exact':cfg['initial_trust_box_fraction_exact'],
        'ratio_threshold_exact':cfg['adaptive_eta_model_ratio_threshold_exact'],
        'shrink_factor_exact':cfg['adaptive_trust_shrink_factor_exact'],
        'ratio_uses_complete_actual_coarse_and_fine_max_eta':True,
        'missing_fine_uses_only_a_proven_coarse_upper_bound_on_the_ratio':True,
        'primary_prediction':'old selected rows plus J step',
        'SOC_prediction':'same actual y selected rows plus J correction',
        'arc_prediction':'declared parabolic basepoint linear bound; undefined ratio if no predicted drop',
        'curvature_failure_on_either_evaluated_grid_triggers_shrink':True,
        'pool_learning_does_not_cancel_feedback':True,'one_shrink_per_model_not_per_failed_trial':True,
        'never_increase_and_never_double_shrink_after_original_rejection':True,
        'feedback_does_not_change_acceptance_or_request_unrecorded_fine_values':True}


def trial_quality(old_eta,coarse,fine,prediction,kind,cfg):
    """A diagnosis from already evaluated decisions; never fills a missing fine value."""
    target=float(Q(cfg['fixed_metric_budget_exact']))
    predicted=None if prediction is None else prediction.get('predicted_slack')
    before=max(0.,float(old_eta)-target)
    improvement=None if predicted is None else before-float(predicted)
    full=fine is not None
    actual=None if not full else float(old_eta)-max(float(coarse['direct_max_eta']),float(fine['direct_max_eta']))
    usable=improvement is not None and improvement>cfg['linear_model_improvement_floor']
    ratio=None if not full or not usable else actual/improvement
    upper=None if not usable else (float(old_eta)-float(coarse['direct_max_eta']))/improvement
    cap=float(Q(cfg['fixed_hard_curvature_cap_exact']))
    tolerance=float(cfg['direct_curvature_tolerance'])
    failures=[name for name,d in [('coarse',coarse),('fine',fine)] if d is not None
        and float(d['direct_maximum_absolute_principal_curvature'])>cap+tolerance]
    threshold=float(Q(cfg['adaptive_eta_model_ratio_threshold_exact']))
    poor=ratio is not None and ratio<threshold
    poor_upper=not full and upper is not None and upper<threshold
    return {'kind':kind,'prediction':copy.deepcopy(prediction),
        'base_true_maximum_eta':float(old_eta),'base_true_eta_excess':before,
        'predicted_metric_improvement':improvement,'full_two_grid_actual_available':full,
        'actual_two_grid_eta_improvement':actual,'actual_to_predicted_ratio':ratio,
        'ratio_denominator_usable':bool(usable),
        'coarse_only_upper_bound_on_actual_two_grid_ratio':upper,
        'poor_complete_two_grid_ratio':bool(poor),'poor_coarse_upper_bound_without_fine':bool(poor_upper),
        'actual_curvature_failure_grids':failures,
        'actual_curvature_cap_and_tolerance':[cap,tolerance],
        'request_shrink':bool(poor or poor_upper or failures),
        'ratio_is_model_quality_not_an_acceptance_gate':True,
        'missing_fine_is_not_estimated_or_reused_from_another_state':True}


def next_trust(model_trust,current_trust,qualities,cfg):
    """At most one extra cap at half the model's scale; preserve prior shrinking."""
    before=float(model_trust);current=float(current_trust)
    if not(0<current<=before and np.isfinite(before) and np.isfinite(current)):
        raise ValueError('finite positive model scale and nonincreased current scale required')
    trigger=[i for i,q in enumerate(qualities) if q['request_shrink']]
    cap=before*float(Q(cfg['adaptive_trust_shrink_factor_exact']))
    after=min(current,cap) if trigger else current
    return after,{'model_trust':before,'trust_after_original_controller':current,'next_trust':after,
        'trigger_trial_indices':trigger,'one_half_model_scale_cap':cap if trigger else None,
        'original_rejection_shrink_not_applied_twice':bool(trigger and current<=cap),
        'same_physical_gates_and_LP_value_time_budgets':True}


class AdaptiveSpectralMetricObjective(SpectralMetricRecoveryObjective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if self.cfg.get('adaptive_scale_policy')!=POLICY:raise ValueError('explicit adaptive scale identity required')
        self.trust_updates=[]
        self.evaluation_definition.update(adaptive_trust_policy=adaptive_definition(self.cfg),
            adaptive_controller_source_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)

    def snapshot(self):
        result=super().snapshot()
        result.update(adaptive_trust_policy=adaptive_definition(self.cfg),
            trust_scale_updates=copy.deepcopy(self.trust_updates))
        return result


def run_adaptive_recovery(objective,initial,*,known_metric_locations=(),artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,AdaptiveSpectralMetricObjective):
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
    """New scale events plus a small artificial controller; no research geometry."""
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    cfg=configuration(recovery_configuration(start_configuration(),target='1/100',curvature_cap='3'))
    cfg.update(max_linear_models=2,max_seconds=20.,radial_Jacobian_batch_owned_rows=2,
        fine_Jacobian_owned_radial_rows=2)
    def decision(eta,k=2.):
        return {'direct_max_eta':eta,'direct_maximum_absolute_principal_curvature':k}
    pred={'predicted_slack':.010,'model_kind':'basepoint-plus-J-step'}
    # The base eta .03 has excess .02; predicted improvement .01.
    fixtures=[
        ('new-rows-early-return-without-fine',decision(.031),None,pred,True),
        ('accepted-low-quality',decision(.029),decision(.029),pred,True),
        ('accepted-good-quality',decision(.020),decision(.021),pred,False),
        ('curvature-failure-even-if-eta-good',decision(.020,3.1),decision(.021),pred,True),
        ('SOC-actual-y-denominator',decision(.029),decision(.029),
            {'predicted_slack':.018,'model_kind':'same-actual-y-rows-plus-J-correction'},False),
        ('undefined-nonpositive-denominator',decision(.031),decision(.031),
            {'predicted_slack':.021,'model_kind':'parabolic-basepoint-linear-bound'},False),
        ('missing-fine-upper-bound-insufficient',decision(.020),None,pred,False)]
    events=[];ok=True
    for name,c,f,p,expect in fixtures:
        q=trial_quality(.03,c,f,p,name,cfg)
        next_value,update=next_trust(.00025,.00025,[q,q],cfg)
        once=next_value==(.000125 if expect else .00025)
        already,unchanged=next_trust(.00025,.000125,[q,q],cfg)
        nodouble=already==.000125
        event={'name':name,'quality':q,'update':update,
            'expected_request_shrink':expect,'at_most_once':once,'original_halving_not_repeated':nodouble}
        events.append(event);ok=ok and q['request_shrink']==expect and once and nodouble
    old=[{'state':'unchanged'}];previous_history=copy.deepcopy(old)
    next_trust(.00025,.00025,[events[0]['quality']],cfg)
    history_ok=old==previous_history
    p=_CurvatureArrayProblem();x=np.array([.3,.6,.6])
    r=np.array([0.,.2,.4,.7,1.]);theta=np.arange(12)*2*np.pi/12
    low=np.array([-.8,-1.,-1.]);up=np.array([2.,1.,1.])
    def make(cls=AdaptiveSpectralMetricObjective):
        return cls(p,HeightAffineGate.from_artificial_array_problem(p),r,theta,3,low,up,cfg=cfg)
    obj=make();result=run_adaptive_recovery(obj,x,artificial_inputs_only=True)
    points=result['checkpoint'].get('accepted_iterates',[])
    decrease=len(points)>1 and all(b['maximum_eta_on_both_grids']<a['maximum_eta_on_both_grids']
        for a,b in zip(points,points[1:]))
    genuine=all(v['coarse']['single_grid_hard_gate_pass'] and v['fine']['single_grid_hard_gate_pass']
        and v['coarse']['previous_metric_budget_pass'] and v['fine']['previous_metric_budget_pass'] for v in points)
    trust_values=[m['trust_before_model'] for m in result['solver']['models']]
    monotone=bool(trust_values and trust_values[0]==float(Q('1/4000'))
        and all(b<=a for a,b in zip(trust_values,trust_values[1:])))
    class FailNewState(AdaptiveSpectralMetricObjective):
        def evaluate(self,vector):
            if getattr(self,'accepted_iterates',[]) and not np.array_equal(np.asarray(vector)[:-1],x):
                raise FloatingPointError('artificial injected trial failure')
            return super().evaluate(vector)
    bad=run_adaptive_recovery(make(FailNewState),x,artificial_inputs_only=True)
    retained=bad['status']=='metric-recovery-error' and bad['checkpoint']['selected_two_grid_physical_point'][
        'physical_parameter_coefficients_binary64']==x.tolist()
    models=result['solver']['models']
    qualities=all(m.get('scale_feedback_trials') and all(q['prediction']['model_kind']=='basepoint-plus-J-step'
        for q in m['scale_feedback_trials']) for m in models)
    return {'schema':POLICY+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,
        'new_event_fixtures':events,'early_return_is_only_coarse_ratio_upper_bound':events[0]['quality']['actual_to_predicted_ratio'] is None,
        'SOC_actual_y_denominator_ratio':events[4]['quality']['actual_to_predicted_ratio'],
        'nonpositive_denominator_unavailable':events[5]['quality']['actual_to_predicted_ratio'] is None,
        'pure_feedback_does_not_mutate_history':history_ok,
        'tiny_status':result['status'],'tiny_error':result['error'],
        'tiny_accepted_eta':[v['maximum_eta_on_both_grids'] for v in points],
        'tiny_all_true_two_grid_gates':genuine,'tiny_actual_eta_strictly_decreases':decrease,
        'tiny_trust_values':trust_values,'tiny_trust_never_increases':monotone,
        'tiny_actual_prediction_semantics_recorded':qualities,
        'injected_trial_failure_preserves_initial_qualified_state':retained,
        'shared_counts':{'LP':result['solver']['linear_program_invocation_count'],
            'values':result['checkpoint']['total_full_value_physical_evaluations']},
        'passed':bool(ok and history_ok and decrease and genuine and monotone and qualities and retained)}
