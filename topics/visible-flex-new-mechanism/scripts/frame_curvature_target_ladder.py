#!/usr/bin/env python3
"""A finite target ladder, sharing one physical model, row pools and budget.

A target decreases only after the last accepted physical state passes both
complete value grids and that target. No target is optimized as a coefficient.
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
from frame_curvature_epigraph_exchange import candidate_decision, curvature_forms
from frame_curvature_feasible_steps import linear_proposal, compact_decision
from frame_curvature_mixed_grid_steps import (
    MixedGridStepObjective, configuration as previous_configuration,
    implementation_hashes as previous_hashes)

POLICY = 'two-grid-accepted-fixed-target-ladder-shared-budget-v1'
TARGETS = ('65', '60', '55', '50', '45', '40', '35', '30', '25', '20', '16')


def implementation_hashes():
    result = previous_hashes()
    path = Path(__file__)
    result[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def configuration(base=None):
    cfg = previous_configuration(base)
    cfg.update(fixed_curvature_target_exact=TARGETS[0], curvature_target_schedule_exact=list(TARGETS),
        mixed_grid_policy=POLICY, target_ladder_policy=POLICY,
        optimizer_objective='fixed-stage LP curvature slack and small step norm; no free curvature auxiliary',
        target_changes_only_after_both_grid_actual_success=True,
        budgets_and_row_pools_shared_across_all_targets=True,
        target_change_reuses_same_state_geometry_and_parameter_Jacobians=True,
        final_ladder_target_does_not_certify_continuous_curvature_or_whole_reach=True)
    return cfg


class TargetLadderObjective(MixedGridStepObjective):
    def __init__(self, *args, **kwargs):
        self.active_stage_index = 0
        self.stage_events = []
        self.cached_fine_target_rescorings = 0
        super().__init__(*args, **kwargs)
        self.targets = tuple(self.cfg['curvature_target_schedule_exact'])
        exact = [Q(x) for x in self.targets]
        if (not exact or min(exact) <= 0 or any(b >= a for a, b in zip(exact, exact[1:]))
                or self.cfg['fixed_curvature_target_exact'] != self.targets[0]):
            raise ValueError('a positive strictly decreasing exact schedule matching the first target is required')
        self.evaluation_definition.update(target_ladder_policy=POLICY,
            mixed_grid_policy=POLICY, curvature_target_schedule_exact=list(self.targets),
            stage_target_is_a_recorded_auxiliary_not_a_physical_state_coordinate=True,
            one_initialization_and_one_shared_active_clock_for_all_stages=True,
            fixed_metric_b0_and_height_mean_not_changed_by_target_switch=True,
            implementation_source_sha256=implementation_hashes())
        self.evaluation_sha256 = digest(self.evaluation_definition)

    @property
    def active_target_exact(self):
        return self.targets[self.active_stage_index]

    @property
    def active_target(self):
        return float(Q(self.active_target_exact))

    def set_stage(self, index):
        if type(index) is not int or index not in [self.active_stage_index, self.active_stage_index+1] or index >= len(self.targets):
            raise ValueError('stage indices may only stay or advance once within the declared ladder')
        self.active_stage_index = index

    def _capture_coarse(self):
        cached = self.epigraph_cache
        if cached is None:
            return
        record = cached['record']; number = record['physical_geometry_evaluation']
        if number in self.saved_coarse_trials:
            return
        state = cached['vector'][:-1]
        self.saved_coarse_trials[number] = {
            'coarse_physical_evaluation':number, 'epigraph_evaluation':record['epigraph_evaluation'],
            'physical_state_sha256':digest(self.problem.identity(state)),
            'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
            'physical_parameter_coefficients_binary64':state.tolist(),
            'stage_index':self.active_stage_index,
            'fixed_stage_target_lambda':float(cached['vector'][-1])*float(Q(self.cfg['curvature_scale_exact'])),
            'decision':copy.deepcopy(record['decision']),
        }

    def fine_decision(self, state):
        before = self.fine_evaluations
        try:
            super().fine_decision(state)
        finally:
            # The inherited method owns the physical-value budget and errors.
            # Retag/rescore only an existing complete cache for this same state;
            # this does not construct another curve or increment a value count.
            cache = self.fine_cache
            if cache is not None and np.array_equal(state, cache['state']):
                if cache.get('stage_target_exact') != self.active_target_exact:
                    if 'curvature_forms' not in cache:
                        cache['curvature_forms'] = curvature_forms(cache['data'], self.cfg)
                    zeta = self.active_target/float(Q(self.cfg['curvature_scale_exact']))
                    decision = candidate_decision(self.problem, self.gate, state, zeta, cache['data'],
                        self.lower, self.upper, self.cfg, forms=cache['curvature_forms'])
                    cache['decision'] = copy.deepcopy(decision)
                    cache['stage_target_exact'] = self.active_target_exact
                    self.cached_fine_target_rescorings += 1
                if self.fine_evaluations > before and self.saved_fine_trials[-1].get('status') == 'complete-doubled-angle-value-call':
                    self.saved_fine_trials[-1].update(decision=copy.deepcopy(cache['decision']),
                        stage_index=self.active_stage_index, stage_target_exact=self.active_target_exact)
        return self.fine_cache['decision']

    def record_stage(self, kind, state, coarse, fine, **extra):
        event = {'kind':kind, 'stage_index':self.active_stage_index,
            'target_exact':self.active_target_exact, 'physical_state_sha256':digest(self.problem.identity(state)),
            'coarse':compact_decision(coarse), 'fine':compact_decision(fine),
            'combined_value_evaluations':self.full_value_evaluations,
            'optimization_elapsed_seconds':None if self.optimization_started is None else time.monotonic()-self.optimization_started}
        event.update(extra); self.stage_events.append(event)
        return event

    def snapshot(self):
        result = super().snapshot()
        result.pop('fixed_target_lambda_exact', None)
        result.update(target_ladder_policy=POLICY, mixed_grid_policy=POLICY,
            curvature_target_schedule_exact=list(self.targets), active_stage_index=self.active_stage_index,
            active_stage_target_exact=self.active_target_exact,
            stage_events=copy.deepcopy(self.stage_events),
            cached_fine_target_rescorings_without_geometry=self.cached_fine_target_rescorings,
            no_clock_counter_or_pool_reset_at_target_changes=True)
        return result


def run_ladder(objective, initial, *, known_metric_locations=(), artificial_inputs_only=False, evaluate_only=False):
    if not artificial_inputs_only:
        require_public_research_environment()
    elif objective.gate.kind != 'artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear ladder checks require the declared artificial array family')
    cfg = objective.cfg
    scale = float(Q(cfg['curvature_scale_exact']))
    metadata = {'method':POLICY, 'target_schedule_exact':list(objective.targets),
        'nonlinear_minimize_invocation_count':0, 'linear_program_invocation_count':0,
        'max_linear_models_total':cfg['max_linear_models'],
        'shared_max_physical_evaluations_coarse_plus_fine':cfg['max_physical_evaluations'],
        'shared_optimization_seconds':cfg['max_seconds'], 'models':[],
        'artificial_inputs_only':bool(artificial_inputs_only), 'evaluate_only':bool(evaluate_only),
        'numpy_version':np.__version__, 'scipy_version':scipy.__version__,
        'target_is_fixed_inside_each_model_and_backtracking_sequence':True,
        'stages_do_not_restart_budget_or_initialization':True}
    def finish(status, error=None, budget=None):
        # Completion is a fact of a stored two-grid accepted state. Preserve it
        # even if the clock expires immediately after that acceptance; no new
        # geometry call is needed merely to record the successful target.
        point = objective.accepted_iterates[-1] if objective.accepted_iterates else None
        already = any(r['kind'] == 'stage-complete' and r['stage_index'] == objective.active_stage_index
                      for r in objective.stage_events)
        if (point and not already and point['maximum_curvature_on_both_grids']
                <= objective.active_target+cfg['direct_curvature_tolerance']):
            state = np.asarray(point['physical_parameter_coefficients_binary64'], float)
            objective.record_stage('stage-complete', state, point['coarse'], point['fine'],
                total_models_so_far=metadata['linear_program_invocation_count'],
                derived_from_saved_two_grid_acceptance_without_another_value_call=True)
        snap = objective.snapshot()
        if objective.checkpoint:
            objective.checkpoint(snap)
        point = snap.get('selected_two_grid_physical_point')
        completed = [r['target_exact'] for r in objective.stage_events if r['kind'] == 'stage-complete']
        final_target = float(Q(objective.targets[-1]))
        return {'status':status, 'error':error, 'budget_message':budget, 'solver':metadata, 'checkpoint':snap,
            'completed_targets_exact':completed, 'active_stage_target_exact':objective.active_target_exact,
            'final_schedule_target_exact':objective.targets[-1],
            'all_ladder_targets_reached':bool(point and point['maximum_curvature_on_both_grids']
                <= final_target+cfg['direct_curvature_tolerance']),
            'last_selected_point_is_two_grid_physically_eligible':point is not None,
            'physical_metric_height_reference_and_space_unchanged':True,
            'sampled_target_success_not_whole_surface_reach':True}

    try:
        current = np.asarray(initial, float).copy()
        target = objective.active_target; zeta = target/scale
        vector = np.r_[current, zeta]
        coarse = objective.evaluate(vector)['decision']; fine = objective.fine_decision(current)
        if not (coarse['eligible_under_fixed_metric_and_physical_gates'] and fine['eligible_under_fixed_metric_and_physical_gates']):
            return finish('initial-ladder-two-grid-physical-gate-failed')
        accepted = objective.accepted_point(current, coarse, fine,
            {'kind':'published-d0d635-two-grid-accepted-ladder-start', 'target_exact':objective.active_target_exact})
        if not len(objective.pool):
            objective.initialize_pool(vector)
        objective.expand_pool(vector, 'initial-ladder-target-coarse-violations')
        objective.initialize_fine_pool(current, known_metric_locations=known_metric_locations)
        objective.record_stage('stage-start', current, coarse, fine, total_models_so_far=0)
        if evaluate_only:
            return finish('evaluation-only-ladder-initial-state')
        # Once only: the initial ordinary/Jacobian construction is explicitly
        # outside the shared active clock. Later stage changes never repeat it.
        objective.linear_rows(vector)
        objective.begin_optimization()
        trust = float(Q(cfg['initial_trust_box_fraction_exact']))
        minimum_trust = float(Q(cfg['minimum_trust_box_fraction_exact']))
        minimum_drop = float(Q(cfg['minimum_accepted_curvature_decrease_exact']))
        for number in range(int(cfg['max_linear_models'])):
            objective._wall()
            # An already attained stage may be skipped without any physical
            # evaluation or LP, but its value decisions are explicitly rescored.
            while accepted['maximum_curvature_on_both_grids'] <= objective.active_target+cfg['direct_curvature_tolerance']:
                vector = np.r_[current, objective.active_target/scale]
                coarse = objective.evaluate(vector)['decision']; fine = objective.fine_decision(current)
                if not (coarse['eligible_under_fixed_metric_and_physical_gates'] and fine['eligible_under_fixed_metric_and_physical_gates']):
                    raise ArithmeticError('cached same-state target change lost physical eligibility')
                objective.record_stage('stage-complete', current, coarse, fine, total_models_so_far=number)
                if objective.active_stage_index == len(objective.targets)-1:
                    return finish('all-declared-curvature-targets-reached-on-both-grids')
                objective.set_stage(objective.active_stage_index+1)
                vector = np.r_[current, objective.active_target/scale]
                coarse = objective.evaluate(vector)['decision']; fine = objective.fine_decision(current)
                objective.expand_pool(vector, 'next-fixed-stage-coarse-curvature-violations')
                objective.record_stage('stage-start', current, coarse, fine, total_models_so_far=number)
                if objective.checkpoint:
                    objective.checkpoint(objective.snapshot())
            target = objective.active_target; zeta = target/scale
            vector = np.r_[current, zeta]
            rows, J, groups, tolerances = objective.linear_rows(vector)
            remaining = cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
            local = dict(cfg, linear_program_seconds=min(cfg['linear_program_seconds'], max(.001, remaining)))
            step, lp = linear_proposal(rows, J, groups, tolerances, current, objective.lower, objective.upper,
                objective.gate.row, objective.gate.intercept+float(objective.gate.row@current)-objective.gate.target,
                trust, local)
            metadata['linear_program_invocation_count'] += 1
            model = {'number':number+1, 'stage_index':objective.active_stage_index,
                'fixed_stage_target_exact':objective.active_target_exact,
                'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'coarse_pool_rows':len(objective.pool), 'fine_pool_rows':len(objective.fine_pool),
                'linear_program':lp, 'trials':[]}
            metadata['models'].append(model); objective._wall()
            if step is None:
                trust *= .5; model['result'] = 'linear-proposal-failed-trust-shrunk'
                if trust < minimum_trust:
                    return finish('minimum-trust-after-linear-proposal-failure')
                continue
            if lp['predicted_slack_improvement'] <= cfg['linear_model_improvement_floor'] or np.max(abs(step)) == 0:
                model['result'] = 'no-current-target-linear-improvement'
                return finish('current-stage-linear-model-stalled')
            model['exact_binary64_proposed_step'] = [str(Q.from_float(float(x))) for x in step]
            old_max = accepted['maximum_curvature_on_both_grids']
            succeeded, relearned = False, False
            for k in range(int(cfg['maximum_backtracks_per_model'])):
                candidate = current+2.**(-k)*step
                trial = {'alpha_exact':str(Q(1, 2**k)), 'accepted_as_next_iterate':False,
                    'stage_index':objective.active_stage_index, 'target_exact':objective.active_target_exact,
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started'}
                model['trials'].append(trial)
                record = objective.evaluate(np.r_[candidate, zeta]); decision = record['decision']
                trial.update(attempt_status='coarse-value-call-complete',
                    coarse_physical_evaluation=record['physical_geometry_evaluation'],
                    coarse_decision=compact_decision(decision))
                coarse_k = decision['direct_maximum_absolute_principal_curvature']
                possible = coarse_k <= target+cfg['direct_curvature_tolerance'] or old_max-coarse_k >= minimum_drop
                fine_dec = None
                if decision['eligible_under_fixed_metric_and_physical_gates'] and possible:
                    fine_dec = objective.fine_decision(candidate)
                    trial.update(fine_decision=compact_decision(fine_dec), fine_value_evaluation=objective.fine_evaluations)
                    new_k = max(coarse_k, fine_dec['direct_maximum_absolute_principal_curvature'])
                    if (fine_dec['eligible_under_fixed_metric_and_physical_gates'] and new_k < old_max
                            and (new_k <= target+cfg['direct_curvature_tolerance'] or old_max-new_k >= minimum_drop)):
                        accepted = objective.accepted_point(candidate, decision, fine_dec,
                            {'kind':'target-ladder-two-grid-physical-step', 'model':number+1,
                             'stage_index':objective.active_stage_index, 'target_exact':objective.active_target_exact,
                             'alpha_exact':str(Q(1, 2**k)), 'previous_maximum_curvature':old_max})
                        current = candidate.copy(); succeeded = True
                        trial.update(accepted_as_next_iterate=True, accepted_index=accepted['accepted_index'])
                added, detail = objective.expand_pool(np.r_[candidate, zeta], 'ladder-trial-coarse-violations')
                trial.update(coarse_omitted_rows=detail['omitted_violating_count'],
                    new_coarse_rows=len(added['added_row_indices']) if added else 0)
                if detail.get('pool_capacity_would_be_exceeded'):
                    return finish('coarse-pool-capacity-preserved-last-accepted-state')
                if fine_dec is not None:
                    added_fine, fine_detail = objective.learn_fine_violations(candidate, 'ladder-trial-fine-violations')
                    trial.update(fine_omitted_rows=fine_detail['omitted_violating_count'],
                        fine_violation_groups=fine_detail['group_counts'],
                        new_fine_rows=len(added_fine['added_row_indices']) if added_fine else 0)
                    if fine_detail.get('pool_capacity_would_be_exceeded'):
                        return finish('fine-pool-capacity-preserved-last-accepted-state')
                    relearned = bool(added_fine)
                if succeeded:
                    model['result'] = 'accepted-two-grid-physical-ladder-step'
                    break
                if relearned:
                    model['result'] = 'new-fine-rows-relinearize-at-last-accepted-state'
                    break
            if not succeeded and not relearned:
                trust *= .5; model['result'] = 'backtracking-rejected-last-two-grid-state-preserved'
                if trust < minimum_trust:
                    return finish('minimum-trust-after-two-grid-backtracking')
            if objective.checkpoint:
                objective.checkpoint(objective.snapshot())
        return finish('shared-ladder-linear-model-budget-exit')
    except EvaluationBudgetReached as error:
        return finish('shared-ladder-value-or-time-budget-exit', budget=str(error))
    except Exception as error:
        return finish('target-ladder-error', error={'type':type(error).__name__, 'message':str(error)})


def developer_check():
    """New stage/cache/budget branches only; no research candidate is evaluated."""
    from types import SimpleNamespace
    from frame_height_affine_gate import HeightAffineGate
    from frame_curvature_epigraph_exchange import _CurvatureArrayProblem
    from frame_curvature_feasible_steps import _StepToy

    class Array(_CurvatureArrayProblem):
        def geometry(self, state, radial, theta, order, jacobian=False, full_two_jet_jacobian=False):
            data = super().geometry(state, radial, theta, order, jacobian, full_two_jet_jacobian)
            r = np.asarray(radial)
            data['height'] = {'b':np.full(len(r), .5*state[1]+.25*state[2]),
                'b_s':np.zeros(len(r)), 'b_ss':np.zeros(len(r))}
            return data

    p = Array(); state = np.array([.3,.6,.6])
    radial = np.array([0., .2, .6, 1.]); theta = np.arange(8)*np.pi/4
    cfg = configuration(); cfg.update(fixed_metric_budget_exact='1/5', curvature_scale_exact='3',
        mirror_target_exact='1/1000', radial_Jacobian_batch_owned_rows=2,
        fine_Jacobian_owned_radial_rows=2, max_physical_evaluations=80)
    obj = TargetLadderObjective(p, HeightAffineGate.from_artificial_array_problem(p), radial, theta, 3,
        np.array([-.8,-1.,-1.]), np.array([2.,1.,1.]), cfg=cfg)
    obj.evaluate(np.r_[state,obj.active_target/3]); obj.fine_decision(state)
    physical = p.identity(state); calls = p.calls; counts = obj.full_value_evaluations
    obj.set_stage(1)
    cd = obj.evaluate(np.r_[state,obj.active_target/3])['decision']; fd = obj.fine_decision(state)
    cached = calls == p.calls and counts == obj.full_value_evaluations
    correct_target = cd['curvature_auxiliary_lambda'] == 60. and fd['curvature_auxiliary_lambda'] == 60.
    fine_target = obj.fine_cache['stage_target_exact'] == '60'
    unchanged = p.identity(state) == physical
    try:
        obj.set_stage(3); bad_skip = False
    except ValueError:
        bad_skip = True

    class Toy(_StepToy):
        active_target_exact = TargetLadderObjective.active_target_exact
        active_target = TargetLadderObjective.active_target
        full_value_evaluations = property(lambda self:self.geometry_evaluations+self.fine_evaluations)
        set_stage = TargetLadderObjective.set_stage
        record_stage = TargetLadderObjective.record_stage
        def __init__(self, *, fine_limit=.85, budget=40, failure=False, models=12):
            super().__init__(target=2.8, fine_limit=fine_limit, inject_fine_failure=failure)
            self.cfg = configuration(self.cfg)
            self.targets = ('14/5','13/5','12/5')
            self.cfg.update(fixed_curvature_target_exact=self.targets[0], curvature_target_schedule_exact=list(self.targets),
                curvature_scale_exact='1', max_seconds=10., max_physical_evaluations=budget,
                max_linear_models=models, initial_trust_box_fraction_exact='1/4',
                minimum_accepted_curvature_decrease_exact='1/1000000')
            self.problem = SimpleNamespace(identity=lambda x:np.asarray(x).tolist())
            self.active_stage_index=0; self.stage_events=[]; self.fine_pool=np.array([0],int)
            self.fine_pool_history=[]; self.pool_history=[]; self.start_count=0
            self.fine_state=None; self.fine_result=None; self.value_state=None
        def begin_optimization(self):
            self.start_count+=1
            return super().begin_optimization()
        def rows(self, vector):
            rows=super().rows(vector); rows.flat[6]=.95-vector[0]
            return rows
        def evaluate(self, vector):
            vector=np.asarray(vector,float); self._wall()
            if self.last is not None and np.array_equal(vector,self.last):
                return self.record
            hit=self.value_state is not None and np.array_equal(vector[:-1],self.value_state)
            if not hit:
                if self.full_value_evaluations>=self.cfg['max_physical_evaluations']:
                    raise EvaluationBudgetReached('toy shared ladder budget')
                self.geometry_evaluations+=1; self.value_state=vector[:-1].copy()
            x=float(vector[0]); good=bool(-2<=x<=2 and 1-x*x>=-1e-9 and .95-x>=-1e-9)
            d={'eligible_under_fixed_metric_and_physical_gates':good,
                'direct_maximum_absolute_principal_curvature':3-x}
            self.record={'physical_geometry_evaluation':self.geometry_evaluations,'decision':d}
            self.last=vector.copy(); self.coarse_records.append({'vector':vector.tolist(),'decision':copy.deepcopy(d)})
            return self.record
        def fine_decision(self,state):
            if self.fine_state is not None and np.array_equal(state,self.fine_state):
                return self.fine_result
            result=super().fine_decision(state)
            self.fine_state=np.asarray(state).copy(); self.fine_result=result
            return result
        def initialize_fine_pool(self,state,known_metric_locations=()):
            return None
        def linear_rows(self, vector):
            values=self.constraint_fun(vector); jac=self.constraint_jac(vector)[:,:1]; groups=self.pool//2
            if 1 in self.fine_pool:
                values=np.r_[values,self.fine_limit-vector[0]]
                jac=np.r_[jac,[[-1.]]]; groups=np.r_[groups,0]
            return values,jac,groups,self.row_tolerances()[groups]
        def learn_fine_violations(self,state,reason):
            bad=state[0]>self.fine_limit+1e-9 and 1 not in self.fine_pool
            if not bad:
                return None,{'omitted_violating_count':0,'group_counts':{}}
            self.fine_pool=np.array([0,1]); self.fine_pool_history.append({'reason':reason})
            return {'added_row_indices':[1]},{'omitted_violating_count':1,'group_counts':{}}
        def snapshot(self):
            return dict(super().snapshot(), stage_events=copy.deepcopy(self.stage_events),
                fine_physical_row_pool_history=copy.deepcopy(self.fine_pool_history),
                active_stage_index=self.active_stage_index, active_stage_target_exact=self.active_target_exact)

    good=Toy(); result=run_ladder(good,np.zeros(1),artificial_inputs_only=True)
    complete=result['all_ladder_targets_reached'] and result['completed_targets_exact']==list(good.targets)
    one_clock=good.start_count==1
    counts=[r['combined_value_evaluations'] for r in good.stage_events]
    increasing=all(b>=a for a,b in zip(counts,counts[1:]))
    switches=[r for r in good.stage_events if r['kind']=='stage-start'][1:]
    finishes=[r for r in good.stage_events if r['kind']=='stage-complete']
    same_at_switch=all(a['combined_value_evaluations']==b['combined_value_evaluations'] for a,b in zip(finishes,switches))
    fine_blocked=Toy(fine_limit=.25,models=4)
    blocked=run_ladder(fine_blocked,np.zeros(1),artificial_inputs_only=True)
    no_bad_advance=(blocked['completed_targets_exact']==['14/5'] and fine_blocked.active_stage_index==1
        and all(p['physical_parameter_coefficients_binary64'][0]<=.25+1e-9 for p in fine_blocked.accepted_iterates))
    budgeted=Toy(budget=4)
    limited=run_ladder(budgeted,np.zeros(1),artificial_inputs_only=True)
    shared_budget=(budgeted.full_value_evaluations==4 and limited['status']=='shared-ladder-value-or-time-budget-exit'
        and limited['completed_targets_exact']==['14/5'] and budgeted.start_count==1)
    bad=Toy(failure=True)
    failed=run_ladder(bad,np.zeros(1),artificial_inputs_only=True)
    kept=failed['status']=='target-ladder-error' and len(bad.accepted_iterates)==1
    one=Toy(models=1)
    last=run_ladder(one,np.zeros(1),artificial_inputs_only=True)
    last_success=last['completed_targets_exact']==['14/5'] and last['solver']['linear_program_invocation_count']==1
    passed=bool(cached and correct_target and fine_target and unchanged and bad_skip and complete and one_clock
        and increasing and same_at_switch and no_bad_advance and shared_budget and kept and last_success)
    return {'schema':'curvature-target-ladder-new-branches-artificial-check-v1', 'artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,
        'actual_array_target_switch_reuses_coarse_and_fine_geometry':cached,
        'both_actual_array_curvature_decisions_use_new_target':correct_target and fine_target,
        'physical_state_unchanged_by_target_switch':unchanged, 'skipping_a_target_is_rejected':bad_skip,
        'three_toy_targets_completed_only_after_two_grid_success':complete,
        'one_active_clock_for_all_stages':one_clock, 'total_value_count_never_resets':increasing,
        'same_state_target_switch_consumes_no_extra_geometry':same_at_switch,
        'fine_gate_failure_cannot_advance_to_next_target':no_bad_advance,
        'shared_value_budget_not_restarted_at_next_target':shared_budget,
        'injected_fine_failure_keeps_last_accepted_state':kept,
        'last_allowed_model_success_recorded_without_another_call':last_success,
        'toy_success_status':result['status'], 'toy_success_error':result.get('error'),
        'toy_success_LP_count':result['solver']['linear_program_invocation_count'],
        'toy_success_total_values':good.full_value_evaluations,
        'toy_fine_gate_status':blocked['status'], 'toy_budget_status':limited['status'],
        'toy_failure_status':failed['status'], 'passed':passed}
