#!/usr/bin/env python3
"""Bounded second-order feasibility corrections for the same physical family.

The correction LP uses real residuals at the trial on BOTH value grids and the
already computed Jacobian at the last accepted point. It is only a proposal;
the corrected point must pass both complete original value gates.
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
from frame_height_affine_gate import EvaluationBudgetReached, require_public_research_environment
from frame_curvature_epigraph_exchange import GROUPS
from frame_curvature_feasible_steps import linear_proposal, compact_decision
from frame_curvature_target_ladder import (TargetLadderObjective, configuration as old_configuration,
    implementation_hashes as old_hashes)

POLICY='two-grid-real-residual-bounded-SOC-shared-budget-v1'
TARGETS=('60','55','50','45','40','35','30','25','20','16')


def implementation_hashes():
    hashes=old_hashes(); path=Path(__file__)
    hashes[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def configuration(base=None):
    cfg=old_configuration(base)
    cfg.update(fixed_curvature_target_exact=TARGETS[0],curvature_target_schedule_exact=list(TARGETS),
        target_ladder_policy=POLICY,mixed_grid_policy=POLICY,SOC_policy=POLICY,
        SOC_physical_margin_retention_exact='1/4',SOC_predicted_descent_retention_exact='1/2',
        SOC_maximum_correction_relative_to_proposed_step_exact='1/2',
        SOC_correction_objective='box-width-normalized L1 norm inside a hard infinity radius',
        maximum_SOC_LPs_per_primary_model=1,
        all_primary_and_correction_LPs_share_the_original_limit=True,
        SOC_requires_both_grid_actual_residuals_at_the_same_primary_trial=True,
        any_new_omitted_row_restarts_from_last_accepted_point_before_SOC=True,
        all_corrected_points_require_both_original_complete_value_grids=True,
        accepted_value_cache_restoration_does_not_count_as_new_geometry=True)
    return cfg


def correction_proposal(base_rows, trial_rows, jacobian, groups, state, primary_step,
                        lower, upper, cap_row, trial_cap_margin, cfg):
    """Minimize ||w/box_width||_1 inside a hard infinity radius.

    Physical direction: c(y)+J(x)w >= gamma*max(c(x),0).
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
    target=gamma*np.maximum(base,0.)
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
    if not result.success or max(linear_violation,bound_violation)>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='LP status or independent linear residual'
        return None,report
    return w,report


class SOCObjective(TargetLadderObjective):
    """Keep the ordinary/Jacobian cache of the last accepted point for rollback."""
    def __init__(self,*args,**kwargs):
        self.accepted_cache=None; self.accepted_coarse_cache_restores=0; self.accepted_fine_cache_restores=0
        self.maximum_accepted_cache_array_bytes=0
        super().__init__(*args,**kwargs)
        self.evaluation_definition.update(SOC_policy=POLICY,implementation_source_sha256=implementation_hashes(),
            last_accepted_value_cache_retained_with_exact_state_and_original_evaluation_number=True)
        self.evaluation_sha256=digest(self.evaluation_definition)
    def physical_geometry(self,state):
        saved=self.accepted_cache
        if (saved is not None and np.array_equal(state,saved['state'])
                and (self.geometry_cache is None or not np.array_equal(state,self.geometry_cache['state']))):
            self.assert_context(state); self._wall()
            self.geometry_cache=saved['coarse']
            d=saved.get('coarse_derivatives')
            self.derivative_cache=d if d is not None and d['pool_version']==self.pool_version else None
            self.accepted_coarse_cache_restores+=1
        return super().physical_geometry(state)
    def fine_decision(self,state):
        saved=self.accepted_cache
        if (saved is not None and np.array_equal(state,saved['state'])
                and (self.fine_cache is None or not np.array_equal(state,self.fine_cache['state']))):
            self.assert_context(state); self._wall(); self.fine_cache=saved['fine']
            d=saved.get('fine_derivatives')
            self.fine_derivative_cache=d if d is not None and d['pool_version']==self.fine_pool_version else None
            self.accepted_fine_cache_restores+=1
        return super().fine_decision(state)
    def accepted_point(self,state,coarse,fine,reason):
        if (self.geometry_cache is None or not np.array_equal(state,self.geometry_cache['state'])
                or self.fine_cache is None or not np.array_equal(state,self.fine_cache['state'])):
            raise ArithmeticError('a newly accepted state must own both actual complete value caches')
        point=super().accepted_point(state,coarse,fine,reason)
        dc=self.derivative_cache; df=self.fine_derivative_cache
        self.accepted_cache={'state':np.asarray(state).copy(),'coarse':self.geometry_cache,'fine':self.fine_cache,
            'coarse_derivatives':dc if dc is not None and np.array_equal(state,dc['state']) else None,
            'fine_derivatives':df if df is not None and np.array_equal(state,df['state']) else None}
        self._cache_size()
        return point
    def _cache_size(self):
        seen=set()
        def size(value):
            if id(value) in seen:return 0
            seen.add(id(value))
            if isinstance(value,np.ndarray):return value.nbytes
            if isinstance(value,dict):return sum(size(x) for x in value.values())
            return 0
        self.maximum_accepted_cache_array_bytes=max(self.maximum_accepted_cache_array_bytes,size(self.accepted_cache))
    def linear_rows(self,vector):
        result=super().linear_rows(vector)
        if self.accepted_cache is not None and np.array_equal(vector[:-1],self.accepted_cache['state']):
            self.accepted_cache.update(coarse_derivatives=self.derivative_cache,fine_derivatives=self.fine_derivative_cache)
            self._cache_size()
        return result
    def snapshot(self):
        result=super().snapshot()
        result.update(SOC_policy=POLICY,accepted_coarse_cache_restores_without_new_geometry=self.accepted_coarse_cache_restores,
            accepted_fine_cache_restores_without_new_geometry=self.accepted_fine_cache_restores,
            maximum_retained_accepted_cache_array_bytes=self.maximum_accepted_cache_array_bytes)
        return result


def run_soc_steps(objective,initial,*,known_metric_locations=(),artificial_inputs_only=False,evaluate_only=False):
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
        'evaluate_only':bool(evaluate_only),'models':[],'no_budget_reset_between_stages_or_corrections':True}
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
            old_max=accepted['maximum_curvature_on_both_grids']; succeeded=False; relearned=False; soc_used=False

            def assess(candidate,kind,alpha,need_fine_for_SOC=False):
                nonlocal current,accepted,succeeded,relearned
                record={'kind':kind,'alpha_exact':alpha,'stage_index':objective.active_stage_index,
                    'target_exact':objective.active_target_exact,'accepted_as_next_iterate':False,
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started'}
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
                alpha=2.**(-backtrack); step=alpha*p; y=current+step
                may_SOC=not soc_used and metadata['linear_program_invocation_count']<cfg['max_linear_models']
                cd,fd,trial=assess(y,'primary-short-step',str(Q(1,2**backtrack)),may_SOC)
                if succeeded:
                    model['result']='accepted-primary-two-grid-step'; break
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
    from types import SimpleNamespace
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_curvature_feasible_steps import FeasibleStepObjective

    cfg=configuration(); cfg.update(linear_program_seconds=2.)
    x=np.array([0.,1e-6]); p=np.array([.2,0.]); lo=np.full(2,-2.); hi=-lo
    base=np.array([x[1],-.2,x[1]])
    J=np.array([[0.,1.],[1.,0.],[0.,1.]])
    y=x+p; trial=np.array([y[1]-y[0]**2,0.,y[1]-2*y[0]**2])
    groups=np.array([0,7,0]); cap=np.array([0.,1.])
    w,report=correction_proposal(base,trial,J,groups,x,p,lo,hi,cap,y[1],cfg)
    z=y+w
    true_values=np.array([z[1]-z[0]**2,z[1]-2*z[0]**2])
    curved_pass=bool(np.min(true_values)>=0 and z[0]>x[0] and report['LP_invoked'])
    keep_half=report['corrected_predicted_slack_improvement']>=.5*report['primary_predicted_slack_improvement']-1e-8
    radius_pass=report['correction_box_normalized_infinity_norm']<=report['maximum_box_normalized_correction_infinity_norm']+1e-12
    badtrial=trial.copy(); badtrial[2]=trial[0]
    wrong,wrong_report=correction_proposal(base,badtrial,J,groups,x,p,lo,hi,cap,y[1],cfg)
    wrong_z=y+wrong; wrong_fine=float(wrong_z[1]-2*wrong_z[0]**2)
    stale_fine_fails=wrong_fine<0

    class Array(_CurvatureArrayProblem):
        def geometry(self,state,radial,theta,order,jacobian=False,full_two_jet_jacobian=False):
            d=super().geometry(state,radial,theta,order,jacobian,full_two_jet_jacobian)
            d['height']={'b':np.full(len(radial),.5*state[1]+.25*state[2]),
                'b_s':np.zeros(len(radial)),'b_ss':np.zeros(len(radial))}
            return d
    ap=Array(); state=np.array([.3,.6,.6]); radial=np.array([0.,.2,.6,1.]); theta=np.arange(8)*np.pi/4
    acfg=configuration(); acfg.update(fixed_metric_budget_exact='1/5',curvature_scale_exact='3',mirror_target_exact='1/1000',
        radial_Jacobian_batch_owned_rows=2,fine_Jacobian_owned_radial_rows=2,max_physical_evaluations=80)
    agate=HeightAffineGate.from_artificial_array_problem(ap)
    obj=SOCObjective(ap,agate,radial,theta,3,np.array([-.8,-1.,-1.]),np.array([2.,1.,1.]),cfg=acfg)
    c=obj.evaluate(np.r_[state,20.])['decision']; f=obj.fine_decision(state)
    # The array family supplies finite jets and tests the cache mechanism. Its
    # artificial physical thresholds are not a claim about any research field.
    if not(c['eligible_under_fixed_metric_and_physical_gates'] and f['eligible_under_fixed_metric_and_physical_gates']):
        raise ArithmeticError('artificial cache baseline must satisfy its own declared gates')
    obj.accepted_point(state,c,f,{'kind':'artificial-cache-baseline'})
    coarse_original=obj.geometry_cache; fine_original=obj.fine_cache
    other=state+np.array([.001,0.,0.])
    obj.evaluate(np.r_[other,20.]); obj.fine_decision(other)
    calls=ap.calls; count=obj.full_value_evaluations
    obj.evaluate(np.r_[state,20.]); obj.fine_decision(state)
    cache_pass=bool(ap.calls==calls and obj.full_value_evaluations==count
        and obj.geometry_cache is coarse_original and obj.fine_cache is fine_original
        and obj.accepted_coarse_cache_restores==1 and obj.accepted_fine_cache_restores==1)

    class Toy:
        active_target_exact=TargetLadderObjective.active_target_exact
        active_target=TargetLadderObjective.active_target
        set_stage=TargetLadderObjective.set_stage
        record_stage=TargetLadderObjective.record_stage
        accepted_point=FeasibleStepObjective.accepted_point
        def __init__(self,budget=40,fail_correction_fine=False,missing_fine_row=False):
            self.cfg=configuration(); self.cfg.update(fixed_curvature_target_exact='14/5',
                curvature_target_schedule_exact=['14/5','13/5'],curvature_scale_exact='1',
                initial_trust_box_fraction_exact='1/4',max_linear_models=2,max_physical_evaluations=budget,
                max_seconds=10.,minimum_accepted_curvature_decrease_exact='1/1000000')
            self.n=2; self.targets=('14/5','13/5'); self.active_stage_index=0; self.stage_events=[]
            self.lower=np.full(2,-2.); self.upper=-self.lower
            self.gate=SimpleNamespace(kind='artificial-array',row=cap.copy(),intercept=0.,target=0.)
            self.problem=SimpleNamespace(identity=lambda s:np.asarray(s).tolist())
            self.pool=np.array([0,7]); self.fine_pool=np.array([0]); self.pool_version=1; self.fine_pool_version=1
            self.checkpoint=None; self.geometry_evaluations=0; self.fine_evaluations=0; self.optimization_started=None
            self.accepted_iterates=[]; self.cstate=None; self.fstate=None; self.ccache=None; self.fcache=None
            self.fail_correction_fine=fail_correction_fine; self.clock_starts=0; self.fine_states=[]
            self.missing_fine_row=missing_fine_row; self.new_fine_learned=False
        @property
        def full_value_evaluations(self):return self.geometry_evaluations+self.fine_evaluations
        def _wall(self):
            if self.optimization_started is not None and time.monotonic()-self.optimization_started>=self.cfg['max_seconds']:
                raise EvaluationBudgetReached('toy active clock')
        def begin_optimization(self):
            self.clock_starts+=1; self.optimization_started=time.monotonic()
        def _decision(self,s,fine):
            v=float(s[1]-(2 if fine else 1)*s[0]**2)
            return {'eligible_under_fixed_metric_and_physical_gates':bool(v>=-1e-9 and np.all(s>=self.lower) and np.all(s<=self.upper)),
                'regularity_screen_pass':True,'direct_maximum_absolute_principal_curvature':3-float(s[0]),
                'direct_max_eta':max(0.,-v)}
        def evaluate(self,vector):
            self._wall(); state=np.asarray(vector[:-1],float)
            if self.cstate is None or not np.array_equal(state,self.cstate):
                if self.full_value_evaluations>=self.cfg['max_physical_evaluations']:
                    raise EvaluationBudgetReached('toy shared actual value cap')
                self.geometry_evaluations+=1; self.cstate=state.copy(); self.ccache=self._decision(state,False)
            return {'decision':copy.deepcopy(self.ccache),'physical_geometry_evaluation':self.geometry_evaluations}
        def fine_decision(self,state):
            self._wall(); state=np.asarray(state,float)
            if self.fstate is None or not np.array_equal(state,self.fstate):
                if self.full_value_evaluations>=self.cfg['max_physical_evaluations']:
                    raise EvaluationBudgetReached('toy shared actual value cap')
                self.fine_evaluations+=1; self.fine_states.append(state.tolist())
                if self.fail_correction_fine and self.fine_evaluations==3:
                    raise FloatingPointError('injected corrected-trial fine evaluation failure')
                self.fstate=state.copy(); self.fcache=self._decision(state,True)
            return copy.deepcopy(self.fcache)
        def constraint_fun(self,vector):
            self.evaluate(vector); s=vector[:-1]
            return np.array([s[1]-s[0]**2,vector[-1]-3+s[0]])
        def fine_rows(self,state):
            self.fine_decision(state); rows=np.ones((7,1,1)); rows[0,0,0]=state[1]-2*state[0]**2
            return rows
        def initialize_pool(self,vector):raise AssertionError('toy pool is already complete')
        def initialize_fine_pool(self,state,known_metric_locations=()):return None
        def expand_pool(self,vector,reason):return None,{'omitted_violating_count':0}
        def learn_fine_violations(self,state,reason):
            if self.missing_fine_row and not self.new_fine_learned and state[0]!=0:
                self.new_fine_learned=True; self.fine_pool_version+=1
                return {'added_row_indices':[1]}, {'omitted_violating_count':1,'group_counts':{'metric_minus':1}}
            return None,{'omitted_violating_count':0,'group_counts':{}}
        def linear_rows(self,vector):
            values=np.r_[self.constraint_fun(vector),self.fine_rows(vector[:-1]).ravel()[0]]
            a=vector[0]; jac=np.array([[-2*a,1.],[1.,0.],[-4*a,1.]])
            return values,jac,np.array([0,7,0]),np.full(3,1e-9)
        def snapshot(self):
            return {'selected_two_grid_physical_point':copy.deepcopy(self.accepted_iterates[-1] if self.accepted_iterates else None),
                'accepted_iterates':copy.deepcopy(self.accepted_iterates),'stage_events':copy.deepcopy(self.stage_events),
                'physical_geometry_evaluations':self.geometry_evaluations,'doubled_angle_full_value_evaluations':self.fine_evaluations,
                'total_full_value_physical_evaluations':self.full_value_evaluations}

    toy=Toy(); result=run_soc_steps(toy,x,artificial_inputs_only=True)
    solver=result['solver']; points=result['checkpoint']['accepted_iterates']
    restored=bool(len(points)==2 and solver['primary_LP_invocation_count']==1 and solver['correction_LP_invocation_count']==1
        and solver['linear_program_invocation_count']==2 and points[-1]['reason']['kind']=='SOC-corrected-short-step')
    shared=toy.clock_starts==1 and toy.full_value_evaluations==6
    distinct_fine=len(toy.fine_states)==3 and toy.fine_states[1]!=toy.fine_states[0] and toy.fine_states[2]!=toy.fine_states[1]
    tiny=Toy(budget=5); limited=run_soc_steps(tiny,x,artificial_inputs_only=True)
    budget_pass=(limited['status']=='shared-SOC-value-time-or-pool-budget-exit' and tiny.full_value_evaluations==5
        and len(limited['checkpoint']['accepted_iterates'])==1)
    bad=Toy(fail_correction_fine=True); failure=run_soc_steps(bad,x,artificial_inputs_only=True)
    error_pass=failure['status']=='SOC-step-error' and len(failure['checkpoint']['accepted_iterates'])==1
    missing=Toy(missing_fine_row=True)
    missed=run_soc_steps(missing,x,artificial_inputs_only=True)
    omitted_pass=bool(missing.new_fine_learned and missed['solver']['correction_LP_invocation_count']==0
        and len(missed['checkpoint']['accepted_iterates'])==1
        and missed['solver']['models'][0]['result']=='observed-new-rows-return-to-last-accepted-before-correction')
    passed=bool(curved_pass and keep_half and radius_pass and stale_fine_fails and cache_pass
        and restored and shared and distinct_fine and budget_pass and error_pass and omitted_pass)
    return {'schema':'SOC-curved-boundary-and-shared-budget-artificial-check-v1','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,
        'actual_coarse_and_fine_curved_boundaries_restored':curved_pass,'actual_corrected_boundaries':true_values.tolist(),
        'linear_curvature_descent_retains_declared_half':keep_half,'correction_respects_actual_primary_norm_cap':radius_pass,
        'substituting_coarse_residual_for_unread_fine_would_fail':stale_fine_fails,
        'wrong_fine_substitution_actual_residual':wrong_fine,
        'real_array_accepted_cache_restore_preserves_values_identity_and_counts':cache_pass,
        'one_primary_plus_one_SOC_LP_reaches_a_true_two_grid_improvement':restored,
        'all_LPs_and_values_and_active_clock_share_one_budget':shared,
        'fine_residuals_are_evaluated_at_initial_primary_and_corrected_states':distinct_fine,
        'budget_exit_before_corrected_fine_keeps_old_accepted_state':budget_pass,
        'injected_corrected_fine_error_keeps_old_accepted_state':error_pass,
        'newly_violated_omitted_fine_row_preempts_SOC_at_rejected_state':omitted_pass,
        'toy_status':result['status'],'toy_error':result.get('error'),
        'toy_solver_counts':{k:v for k,v in solver.items() if k.endswith('invocation_count')},
        'toy_total_values':toy.full_value_evaluations,'correction_LP_report':report,'passed':passed}
