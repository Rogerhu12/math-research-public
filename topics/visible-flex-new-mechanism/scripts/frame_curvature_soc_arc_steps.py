#!/usr/bin/env python3
"""Reuse a failed full SOC correction on a parabolic backtracking path.

The old primary LP, correction LP, two-grid objective and all gates are imported
unchanged. Only post-SOC backtracking uses x+alpha*p+(alpha/alpha0)^2*w.
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
from frame_height_affine_gate import EvaluationBudgetReached, require_public_research_environment
from frame_curvature_feasible_steps import linear_proposal, compact_decision
from frame_curvature_soc_steps import correction_proposal, implementation_hashes as old_hashes

POLICY='same-LPs-two-grid-SOC-parabolic-backtracking-v1'


def implementation_hashes():
    result=old_hashes(); path=Path(__file__)
    result[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def configuration(base):
    cfg=copy.deepcopy(base)
    cfg.update(SOC_parabolic_backtracking_policy=POLICY,
        mixed_grid_policy=POLICY,target_ladder_policy=POLICY,
        SOC_backtracking_path='x+alpha*p+(alpha/alpha0)^2*w; alpha0 is the actual corrected primary fraction',
        failed_full_SOC_correction_not_discarded_before_backtracking=True,
        parabolic_backtracking_uses_no_additional_LP=True,
        old_successful_SOC_controller_and_all_original_gates_unchanged=False,
        old_primary_and_correction_LPs_and_all_original_gates_unchanged=True,
        only_failed_SOC_backtracking_curve_changed=True)
    return cfg


def parabolic_candidate(state,primary,correction,alpha_exact,reference_alpha_exact):
    """Exact rational fractions, floating evaluation of one saved model curve."""
    a,r=Q(alpha_exact),Q(reference_alpha_exact)
    if not 0<a<=r<=1:raise ValueError('backtrack fraction must lie in (0, reference_alpha] <= 1')
    x,p,w=[np.asarray(v,float) for v in (state,primary,correction)]
    if x.ndim!=1 or p.shape!=x.shape or w.shape!=x.shape or not all(np.all(np.isfinite(v)) for v in (x,p,w)):
        raise ValueError('three finite same-layout model vectors are required')
    t=a/r; weight=t*t
    z=x+float(a)*p+float(weight)*w
    return z,{'reference_primary_alpha_exact':str(r),'curve_fraction_exact':str(t),
        'correction_weight_exact':str(weight),'convex_weights_exact':[str(1-t),str(t-weight),str(weight)],
        'same_reference_accepted_point_and_saved_primary_and_correction':True,
        'finite_arithmetic_formula_not_exact_binary64_polynomial_identity':True}


def curvature_arc_slack_bound(initial,primary,corrected,fraction):
    t=float(fraction)
    if not 0<=t<=1 or not all(np.isfinite(v) and v>=0 for v in (initial,primary,corrected)):
        raise ValueError('finite nonnegative endpoint slacks and fraction in [0,1] required')
    return float((1-t)*initial+(t-t*t)*primary+t*t*corrected)


def run_soc_arc_steps(objective,initial,*,known_metric_locations=(),artificial_inputs_only=False,evaluate_only=False):
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
    """Only the new path, real-residual acceptance and shared-budget branches."""
    from types import SimpleNamespace
    from frame_curvature_soc_steps import configuration as old_configuration
    from frame_curvature_target_ladder import TargetLadderObjective
    from frame_curvature_feasible_steps import FeasibleStepObjective
    cap=np.array([0.,1.])
    class Toy:
        active_target_exact=TargetLadderObjective.active_target_exact
        active_target=TargetLadderObjective.active_target
        set_stage=TargetLadderObjective.set_stage
        record_stage=TargetLadderObjective.record_stage
        accepted_point=FeasibleStepObjective.accepted_point
        def __init__(self,budget=40,fail_correction_fine=False,missing_fine_row=False):
            self.cfg=configuration(old_configuration()); self.cfg.update(fixed_curvature_target_exact='14/5',
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
            v=float(s[1]*(1-s[0])-(1.02 if fine else 1)*s[0]**2)
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
            return np.array([s[1]*(1-s[0])-s[0]**2,vector[-1]-3+s[0]])
        def fine_rows(self,state):
            self.fine_decision(state); rows=np.ones((7,1,1)); rows[0,0,0]=state[1]*(1-state[0])-1.02*state[0]**2
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
            a,b=vector[:2]; jac=np.array([[-b-2*a,1-a],[1.,0.],[-b-2.04*a,1-a]])
            return values,jac,np.array([0,7,0]),np.full(3,1e-9)
        def snapshot(self):
            return {'selected_two_grid_physical_point':copy.deepcopy(self.accepted_iterates[-1] if self.accepted_iterates else None),
                'accepted_iterates':copy.deepcopy(self.accepted_iterates),'stage_events':copy.deepcopy(self.stage_events),
                'physical_geometry_evaluations':self.geometry_evaluations,'doubled_angle_full_value_evaluations':self.fine_evaluations,
                'total_full_value_physical_evaluations':self.full_value_evaluations}

    x=np.array([0.,.001])
    toy=Toy(); result=run_soc_arc_steps(toy,x,artificial_inputs_only=True)
    solver=result['solver']; points=result['checkpoint']['accepted_iterates']; models=solver['models']
    all_trials=[t for m in models for t in m['trials']]
    arcs=[t for t in all_trials if t['kind']=='SOC-parabolic-backtrack']
    accepted=[t for t in arcs if t['accepted_as_next_iterate']]
    curve_pass=bool(len(points)==2 and accepted and solver['primary_LP_invocation_count']==1
        and solver['correction_LP_invocation_count']==1 and solver['linear_program_invocation_count']==2)
    endpoint_rejected=bool(any(t['kind']=='SOC-corrected-short-step' and not t['accepted_as_next_iterate'] for t in all_trials))
    arc=accepted[0] if accepted else {}; curve=arc.get('parabolic_curve',{})
    exact_weights=bool(curve and sum(Q(q) for q in curve['convex_weights_exact'])==1
        and all(Q(q)>=0 for q in curve['convex_weights_exact'])
        and Q(curve['correction_weight_exact'])==Q(curve['curve_fraction_exact'])**2)
    if accepted:
        point=np.asarray([float(Q(v)) for v in arc['exact_binary64_physical_coefficients']])
        p=np.asarray([float(Q(v)) for v in models[0]['exact_binary64_proposed_step']])
        alpha=float(Q(arc['alpha_exact'])); straight=x+alpha*p
        straight_coarse=toy._decision(straight,False)
        lost_correction_would_fail=not straight_coarse['eligible_under_fixed_metric_and_physical_gates']
        actual_both=toy._decision(point,False)['eligible_under_fixed_metric_and_physical_gates'] and toy._decision(point,True)['eligible_under_fixed_metric_and_physical_gates']
    else:lost_correction_would_fail=False; actual_both=False
    # A correction computed after an already reduced primary uses alpha/alpha0,
    # never alpha alone. This is the exact source-parameterization identity.
    z,sub=parabolic_candidate(np.array([1.,2.]),np.array([.3,-.2]),np.array([.02,.04]),'1/8','1/2')
    reference=np.array([1.,2.])+np.array([.3,-.2])/8+np.array([.02,.04])/16
    scaled_reference=bool(np.array_equal(z,reference) and sub['correction_weight_exact']=='1/16')
    rejected_alpha=False
    try:parabolic_candidate(np.zeros(2),np.ones(2),np.ones(2),'1/2','1/4')
    except ValueError:rejected_alpha=True
    # At the accepted arc point the fine call is a new state and consumes the
    # same physical cap. Failure there cannot promote a coarse-only point.
    bad=Toy(fail_correction_fine=True); failed=run_soc_arc_steps(bad,x,artificial_inputs_only=True)
    failure_kept=bool(failed['status']=='SOC-step-error' and len(failed['checkpoint']['accepted_iterates'])==1)
    baseline_calls=toy.full_value_evaluations
    tiny=Toy(budget=max(2,baseline_calls-1)); limited=run_soc_arc_steps(tiny,x,artificial_inputs_only=True)
    budget_kept=bool(limited['status']=='shared-SOC-value-time-or-pool-budget-exit'
        and tiny.full_value_evaluations==tiny.cfg['max_physical_evaluations']
        and len(limited['checkpoint']['accepted_iterates'])==1)
    no_extra_clock=toy.clock_starts==1 and solver['linear_program_invocation_count']==2
    rho=curvature_arc_slack_bound(.1,.04,.07,.5)
    slack_bound=bool(abs(rho-.0775)<1e-15 and rho<=.1-.5*(1-.5/2)*(.1-.04)+1e-15)
    passed=bool(curve_pass and endpoint_rejected and exact_weights and lost_correction_would_fail and actual_both
        and scaled_reference and rejected_alpha and failure_kept and budget_kept and no_extra_clock and slack_bound)
    return {'schema':'SOC-parabolic-path-real-curved-boundary-artificial-v1','artificial_inputs_only':True,
        'research_candidate_geometry_evaluated_or_optimized':False,'same_one_primary_and_one_correction_LP':curve_pass,
        'full_SOC_endpoint_is_rejected_before_curve_backtracking':endpoint_rejected,
        'same_alpha_unmodified_primary_would_still_fail':lost_correction_would_fail,
        'accepted_curve_point_passes_both_actual_toy_grids':actual_both,
        'exact_curve_weights_are_nonnegative_and_sum_one':exact_weights,
        'already_reduced_primary_uses_correct_alpha_ratio':scaled_reference,'invalid_curve_fraction_rejected':rejected_alpha,
        'injected_arc_fine_failure_keeps_old_accepted':failure_kept,
        'shared_value_budget_before_arc_fine_keeps_old_accepted':budget_kept,
        'one_active_clock_and_no_extra_LP':no_extra_clock,'convex_linear_curvature_slack_bound':slack_bound,
        'toy_status':result['status'],'toy_error':result.get('error'),
        'toy_counts':{k:v for k,v in solver.items() if k.endswith('invocation_count')},
        'toy_value_calls':baseline_calls,'toy_models':models,'passed':passed}
