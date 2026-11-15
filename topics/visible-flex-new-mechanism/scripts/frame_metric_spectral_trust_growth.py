#!/usr/bin/env python3
"""Conservative next-model trust growth after complete successful full steps.

The published physical primary cost, SOC and all actual two-grid gates stay.
Only the next proposal radius may grow under an explicit new policy.
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
from frame_metric_spectral_physical_penalty import (
    PhysicalPenaltySpectralMetricObjective, configuration as physical_configuration,
    implementation_hashes as physical_hashes, primary_proposal,
    correction_proposal, penalty_definition, floor_definition)
from frame_metric_spectral_adaptive import (adaptive_definition as shrink_definition,
    trial_quality, next_trust as shrink_next_trust)
from frame_metric_budget_recovery import (require_public_research_environment,
    EvaluationBudgetReached, compact, parabolic_candidate, curvature_arc_slack_bound)

POLICY='two-grid-spectral-conservative-next-model-trust-growth-v1'


def implementation_hashes():
    result=physical_hashes();p=Path(__file__)
    result[p.name]=hashlib.sha256(p.read_bytes()).hexdigest();return result


def configuration(base):
    cfg=physical_configuration(base)
    cfg.pop('initial_trust_is_last_accepted_curvature_reserve_primary_scale',None)
    cfg.update(trust_growth_policy=POLICY, adaptive_trust_never_increases=False,
        initial_trust_box_fraction_exact='1/64000',
        initial_trust_inherits_last_physical_penalty_scale_but_streak_starts_zero=True,
        trust_growth_required_consecutive_models=2,
        trust_growth_minimum_complete_ratio_exact='3/4',
        trust_growth_minimum_actual_norm_fraction_exact='9/10',
        trust_growth_factor_exact='2',trust_growth_maximum_box_fraction_exact='1/1000',
        trust_growth_cap_is_a_new_explicit_proposal_parameter=True,
        trust_growth_requires_no_new_rows_and_first_full_primary_only=True,
        trust_growth_is_not_an_acceptance_or_convergence_claim=True)
    return cfg


def growth_definition(cfg):
    if cfg.get('trust_growth_policy')!=POLICY:raise ValueError('explicit conservative growth identity required')
    for key,value in [('initial_trust_box_fraction_exact','1/64000'),
            ('trust_growth_minimum_complete_ratio_exact','3/4'),
            ('trust_growth_minimum_actual_norm_fraction_exact','9/10'),
            ('trust_growth_factor_exact','2'),('trust_growth_maximum_box_fraction_exact','1/1000')]:
        if Q(cfg[key])!=Q(value):raise ValueError('the declared growth constants must not drift: '+key)
    if cfg.get('trust_growth_required_consecutive_models')!=2:
        raise ValueError('two consecutive qualifying models required')
    return {'schema':POLICY+'-definition','initial_radius_exact':'1/64000',
        'initial_success_streak':0,'consecutive_models_required':2,
        'minimum_full_two_grid_actual_to_predicted_ratio_exact':'3/4',
        'minimum_actual_step_box_norm_over_current_radius_exact':'9/10',
        'growth_factor_exact':'2','new_maximum_proposal_radius_exact':'1/1000',
        'maximum_is_new_not_an_existing_old_controller_field':True,
        'only_first_alpha1_primary_accepted_without_SOC_or_backtrack':True,
        'all_model_added_soft_or_hard_coarse_or_fine_rows_reset_streak':True,
        'missing_fine_or_invalid_ratio_or_failed_trial_resets_streak':True,
        'old_one_shrink_per_model_rule_has_priority':True,
        'same_radius_consecutive_successes_only':True,
        'growth_or_shrink_at_most_once_after_each_model':True,
        'all_original_actual_gates_and_acceptance_and_shared_budgets_unchanged':True,
        'fixed_physical_primary_cost_unchanged_as_radius_changes':True,
        'no_additional_actual_evaluation_for_feedback':True,
        'proposal_policy_and_streak_not_physical_parameters':True}


def adaptive_definition(cfg):
    result=shrink_definition(cfg)
    result.pop('never_increase_and_never_double_shrink_after_original_rejection',None)
    result.update(schema=POLICY+'-adaptive-definition',
        original_shrink_subpolicy_schema=shrink_definition(cfg)['schema'],
        original_rejection_shrink_not_applied_twice=True,
        next_model_growth=growth_definition(cfg))
    return result


class GrowingTrustSpectralMetricObjective(PhysicalPenaltySpectralMetricObjective):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.evaluation_definition.update(adaptive_trust_policy=adaptive_definition(self.cfg),
            conservative_trust_growth=growth_definition(self.cfg),
            trust_growth_controller_source_sha256=implementation_hashes())
        self.evaluation_sha256=digest(self.evaluation_definition)

    def snapshot(self):
        result=super().snapshot()
        result.update(adaptive_trust_policy=adaptive_definition(self.cfg),
            conservative_trust_growth=growth_definition(self.cfg))
        return result


def next_growth_trust(model,current_trust,streak,cfg):
    """Pure decision from saved model records; never changes a trial or gate."""
    growth_definition(cfg)
    if type(streak) is not int or not 0<=streak<cfg['trust_growth_required_consecutive_models']:
        raise ValueError('bounded integer success streak required')
    before=float(model['trust_before_model'])
    after,old=shrink_next_trust(before,current_trust,model.get('scale_feedback_trials',[]),cfg)
    trials=model.get('trials',[]);trial=trials[0] if len(trials)==1 else {}
    quality=trial.get('scale_feedback',{})
    ratio=quality.get('actual_to_predicted_ratio')
    norm=model.get('linear_program',{}).get('primary_step_cost_diagnostic',{}).get('actual_trust_normalized_step_norm')
    coarse=trial.get('coarse_decision',{});fine=trial.get('fine_decision',{})
    added_coarse=sum(int(t.get('new_coarse_rows',0)) for t in trials)
    added_fine=sum(int(t.get('new_fine_rows',0)) for t in trials)
    checks={
        'first_only_full_primary_accepted':bool(len(trials)==1
            and trial.get('kind')=='primary-metric-short-step'
            and trial.get('alpha_exact')=='1' and trial.get('accepted_as_next_iterate') is True
            and model.get('result')=='accepted-two-grid-true-metric-descent'),
        'no_SOC_or_backtrack':bool(not model.get('corrections') and len(trials)==1),
        'complete_actual_two_grid_gates':bool(quality.get('full_two_grid_actual_available')
            and coarse.get('single_grid_admissible_recovery_point')
            and fine.get('single_grid_admissible_recovery_point')),
        'valid_high_complete_ratio':bool(quality.get('ratio_denominator_usable')
            and ratio is not None and np.isfinite(ratio)
            and ratio>=float(Q(cfg['trust_growth_minimum_complete_ratio_exact']))),
        'actual_step_uses_radius':bool(norm is not None and np.isfinite(norm)
            and norm>=float(Q(cfg['trust_growth_minimum_actual_norm_fraction_exact']))),
        'no_new_coarse_or_fine_rows':bool(trials and all(
            t.get('new_coarse_rows')==0 and t.get('new_fine_rows')==0 for t in trials)),
        'old_shrink_not_requested_or_applied':bool(after==before and current_trust==before
            and not old['trigger_trial_indices'])}
    qualified=all(checks.values());count=streak+1 if qualified else 0
    cap=float(Q(cfg['trust_growth_maximum_box_fraction_exact']))
    grew=False;at_cap=False;next_radius=after
    if count==cfg['trust_growth_required_consecutive_models']:
        next_radius=min(after*float(Q(cfg['trust_growth_factor_exact'])),cap)
        if next_radius<after:raise ValueError('current proposal scale exceeds the explicit cap')
        grew=next_radius>after;at_cap=not grew;count=0
    report=copy.deepcopy(old)
    report.update(next_trust=next_radius,trust_after_unchanged_shrink_rule=after,
        conservative_growth={'streak_before':streak,'streak_after':count,
            'qualifying_model':qualified,'checks':checks,
            'failed_conditions':[k for k,v in checks.items() if not v],
            'complete_ratio':ratio,'actual_step_norm_over_radius':norm,
            'new_coarse_rows':added_coarse,'new_fine_rows':added_fine,
            'grew_for_next_model':grew,'qualified_pair_at_cap':at_cap,
            'new_explicit_cap_evaluated':cap,
            'old_shrink_has_priority':True,'input_model_and_trials_not_modified':True})
    return next_radius,count,report


def run_growing_trust_recovery(objective,initial,*,known_metric_locations=(),artificial_inputs_only=False,evaluate_only=False):
    if not isinstance(objective,GrowingTrustSpectralMetricObjective):
        raise ValueError('the explicit adaptive spectral objective is required')
    if objective.cfg.get('artificial_large_metric_budget_for_IO_only') and not (artificial_inputs_only and evaluate_only):
        raise ValueError('the loose predecessor fixture budget is only for artificial IO without LPs')
    if not artificial_inputs_only:require_public_research_environment()
    elif objective.gate.kind!='artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear steps require the explicit artificial array family')
    cfg=objective.cfg;growth_streak=0
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
            'conservative_trust_growth':growth_definition(objective.cfg),
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
        accepted=objective.accepted_point(current,cd,fd,{'kind':'saved-physical-penalty-two-grid-success-growth-start'})
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
    """Only artificial records/models; no saved research coefficients are read."""
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_soc_steps import configuration as start_configuration
    from frame_metric_budget_recovery import configuration as recovery_configuration
    cfg=configuration(recovery_configuration(start_configuration(),target='1/100',curvature_cap='3'))
    cfg.update(max_linear_models=2,max_seconds=20.,radial_Jacobian_batch_owned_rows=2,
        fine_Jacobian_owned_radial_rows=2)
    radius=float(Q('1/64000'))
    def good_model(r=radius):
        q={'ratio_denominator_usable':True,'full_two_grid_actual_available':True,
            'actual_to_predicted_ratio':.8,'request_shrink':False}
        d={'single_grid_admissible_recovery_point':True}
        t={'kind':'primary-metric-short-step','alpha_exact':'1','accepted_as_next_iterate':True,
            'coarse_decision':copy.deepcopy(d),'fine_decision':copy.deepcopy(d),
            'scale_feedback':copy.deepcopy(q),'new_coarse_rows':0,'new_fine_rows':0}
        return {'trust_before_model':r,'scale_feedback_trials':[q],'trials':[t],'corrections':[],
            'result':'accepted-two-grid-true-metric-descent',
            'linear_program':{'primary_step_cost_diagnostic':{'actual_trust_normalized_step_norm':1.}}}
    model=good_model();original=copy.deepcopy(model)
    r1,n1,d1=next_growth_trust(model,radius,0,cfg)
    r2,n2,d2=next_growth_trust(model,r1,n1,cfg)
    pair=bool(r1==radius and n1==1 and r2==2*radius and n2==0
        and d2['conservative_growth']['grew_for_next_model'])
    rejections={}
    cases={}
    for key in ['coarse_new','fine_new','missing_fine','low_ratio','invalid_ratio','low_norm',
            'failed_trial','SOC','backtrack','multiple_trials','new_rows_without_fine_record']:
        m=good_model()
        if key=='coarse_new':m['trials'][0]['new_coarse_rows']=1
        elif key=='fine_new':m['trials'][0]['new_fine_rows']=1
        elif key=='missing_fine':
            m['trials'][0].pop('fine_decision');m['trials'][0]['scale_feedback']['full_two_grid_actual_available']=False
        elif key=='low_ratio':m['trials'][0]['scale_feedback']['actual_to_predicted_ratio']=.749
        elif key=='invalid_ratio':m['trials'][0]['scale_feedback']['ratio_denominator_usable']=False
        elif key=='low_norm':m['linear_program']['primary_step_cost_diagnostic']['actual_trust_normalized_step_norm']=.899
        elif key=='failed_trial':m['trials'][0]['accepted_as_next_iterate']=False
        elif key=='SOC':m['corrections']=[{'LP_invoked':True}]
        elif key=='backtrack':m['trials'][0]['alpha_exact']='1/2'
        elif key=='multiple_trials':m['trials'].append(copy.deepcopy(m['trials'][0]))
        else:m['trials'][0].pop('new_fine_rows')
        r,n,d=next_growth_trust(m,radius,1,cfg)
        rejections[key]=bool(r==radius and n==0 and not d['conservative_growth']['grew_for_next_model'])
        cases[key]=d
    m=good_model();m['scale_feedback_trials'][0]['request_shrink']=True
    r,n,d=next_growth_trust(m,radius,1,cfg)
    shrink_priority=bool(r==radius/2 and n==0 and not d['conservative_growth']['grew_for_next_model'])
    r,n,d=next_growth_trust(m,radius/2,1,cfg)
    no_double=bool(r==radius/2 and n==0 and d['original_rejection_shrink_not_applied_twice'])
    m=good_model();m['result']='primary-LP-failed-trust-shrunk';m['trials']=[];m['scale_feedback_trials']=[]
    r,n,d=next_growth_trust(m,radius/2,1,cfg)
    failed_primary=bool(r==radius/2 and n==0)
    cap=float(Q('1/1000'));m=good_model(3*cap/4)
    r,n,d=next_growth_trust(m,3*cap/4,1,cfg)
    capped=bool(r==cap and n==0 and d['conservative_growth']['grew_for_next_model'])
    m=good_model(cap);r,n,d=next_growth_trust(m,cap,1,cfg)
    capped &= bool(r==cap and n==0 and d['conservative_growth']['qualified_pair_at_cap'])
    boundary=good_model();boundary['trials'][0]['scale_feedback']['actual_to_predicted_ratio']=.75
    boundary['linear_program']['primary_step_cost_diagnostic']['actual_trust_normalized_step_norm']=.9
    r,n,d=next_growth_trust(boundary,radius,1,cfg)
    thresholds=bool(r==2*radius and n==0)
    immutable=model==original
    problem=_CurvatureArrayProblem();x=np.array([.3,.6,.6])
    radial=np.array([0.,.2,.4,.7,1.]);theta=np.arange(12)*2*np.pi/12
    args=(problem,HeightAffineGate.from_artificial_array_problem(problem),radial,theta,3,
        np.array([-.8,-1.,-1.]),np.array([2.,1.,1.]))
    old=PhysicalPenaltySpectralMetricObjective(*args,cfg=cfg)
    new=GrowingTrustSpectralMetricObjective(*args,cfg=cfg)
    same=bool(np.array_equal(old.all_rows(old.vector(x)),new.all_rows(new.vector(x)))
        and old.problem.identity(x)==new.problem.identity(x))
    result=run_growing_trust_recovery(new,x,artificial_inputs_only=True)
    accepted=result['checkpoint']['accepted_iterates'];models=result['solver']['models']
    valid=bool(accepted and all(v['coarse']['single_grid_admissible_recovery_point']
        and v['fine']['single_grid_admissible_recovery_point'] for v in accepted))
    counted=bool(result['solver']['linear_program_invocation_count']
        ==result['solver']['primary_LP_invocation_count']+result['solver']['correction_LP_invocation_count']
        <=cfg['max_linear_models'])
    recorded=all('conservative_growth' in m['scale_feedback_update'] for m in models if 'scale_feedback_update' in m)
    # Source functions are reused, rather than separately reimplemented here.
    from frame_metric_spectral_physical_penalty import primary_proposal as published_primary, correction_proposal as published_SOC
    unchanged=primary_proposal is published_primary and correction_proposal is published_SOC
    # Existing LP record schema, generated on tiny arrays only, is used by
    # the new compact-output stress test; it is not a repeated scientific run.
    groups=np.array([0,1,2,7,8,9,10]);values=np.array([-.01,-.009,.1,.57,8.4e-8,.66,.09])
    matrix=np.array([[1.,0.],[.5,0.],[0.,.1],[0.,0.],[-1e-4,1e-3],[0.,0.],[0.,0.]])
    lo=np.full(2,-1.);hi=np.full(2,1.);caprow=np.array([0.,1.]);state=np.zeros(2)
    unused,primary=primary_proposal(values,matrix,groups,np.full(7,1e-9),state,lo,hi,caprow,.1,radius,cfg)
    step=np.array([.01,.001]);trial=values+matrix@step;trial[:2]-=.0005;trial[4]=-1e-8
    unused,correction=correction_proposal(values,trial,matrix,groups,state,step,lo,hi,caprow,.1,cfg)
    passed=bool(pair and all(rejections.values()) and shrink_priority and no_double and failed_primary
        and capped and thresholds and immutable and same and valid and counted and recorded and unchanged)
    return {'schema':POLICY+'-artificial-check','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,
        'first_success_does_not_grow_second_doubles':pair,'rejection_conditions_reset_streak':rejections,
        'old_actual_feedback_shrink_has_priority':shrink_priority,'old_rejection_not_double_shrunk':no_double,
        'failed_primary_resets_successes':failed_primary,'explicit_new_cap_preserved':capped,
        'exact_thresholds_inclusive':thresholds,'saved_models_and_history_unchanged':immutable,
        'all_actual_rows_and_physical_model_unchanged':same,'published_primary_and_SOC_objects_reused':unchanged,
        'tiny_actual_acceptance_gates_preserved':valid,'tiny_LP_shared_count_preserved':counted,
        'tiny_update_records_complete':recorded,'tiny_status':result['status'],
        'tiny_solver':result['solver'],'first_feedback':d1,'second_feedback':d2,
        'representative_reset_diagnostics':cases,
        'primary':primary,'correction':correction,'passed':passed}
