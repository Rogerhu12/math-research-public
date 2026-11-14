#!/usr/bin/env python3
"""Fixed-curvature-target short steps with independent whole-grid acceptance.

The linear program proposes a step. Only a physical state passing both angular
value grids and decreasing the actual maximum curvature becomes a new iterate.
Rejected states teach omitted rows but are never used as physical warm starts.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np
import scipy
from scipy.optimize import linprog

from frame_collar_residual_audit import digest
from frame_height_affine_gate import EvaluationBudgetReached, require_public_research_environment
from frame_curvature_epigraph_exchange import (
    CurvatureExchangeObjective as PreviousObjective, GROUPS, POSITION_JETS,
    candidate_decision, configuration as previous_configuration,
    implementation_hashes as previous_hashes,
)

POLICY = 'fixed-lambda-linear-proposals-two-grid-physical-acceptance-v1'


def implementation_hashes():
    result = previous_hashes()
    path = Path(__file__)
    result[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def configuration(base=None):
    cfg = previous_configuration() if base is None else copy.deepcopy(base)
    cfg.update(
        fixed_curvature_target_exact='70',
        curvature_auxiliary_is_fixed_not_minimized=True,
        short_step_policy=POLICY,
        max_linear_models=12,
        max_physical_evaluations=40,
        max_seconds=120.,
        maximum_backtracks_per_model=6,
        initial_trust_box_fraction_exact='1/100',
        minimum_trust_box_fraction_exact='1/102400',
        linear_fraction_to_boundary_exact='1/2',
        linear_step_norm_weight_exact='1/1000000',
        minimum_accepted_curvature_decrease_exact='1/1000',
        linear_model_improvement_floor=1e-10,
        linear_model_residual_limit=1e-7,
        linear_program_primal_tolerance=1e-9,
        linear_program_dual_tolerance=1e-9,
        linear_program_seconds=10.,
        every_trial_full_coefficients_preserved=True,
        accepted_iterate_requires_both_angular_value_grids=True,
        doubled_grid_value_evaluations_consume_shared_physical_budget=True,
        no_rejected_trial_becomes_next_physical_iterate=True,
        no_symmetry_row_compression_in_this_stage=True,
    )
    return cfg


def linear_proposal(values, jacobian, groups, tolerances, state, lower, upper,
                    cap_row, cap_margin, trust_fraction, cfg):
    """A bounded linear model in normalized step y, curvature slack rho, norm t.

    Physical rows use J d >= -gamma*(c+original_tolerance).
    Curvature rows at the one fixed target use c+J d+rho >= 0.
    Bounds and the original affine cap row are not elastic.
    """
    state, lower, upper = [np.asarray(x, float) for x in (state, lower, upper)]
    values, J = np.asarray(values, float), np.asarray(jacobian, float)
    groups, tolerances = np.asarray(groups, int), np.asarray(tolerances, float)
    n = len(state)
    if (state.ndim != 1 or lower.shape != state.shape or upper.shape != state.shape
            or J.shape != (len(values), n) or groups.shape != values.shape
            or tolerances.shape != values.shape or np.any(lower > upper)
            or not all(np.all(np.isfinite(x)) for x in (state, lower, upper, values, J, tolerances))
            or not np.isfinite(trust_fraction) or trust_fraction <= 0):
        raise ValueError('finite matching linear model and positive trust fraction required')
    if np.any(groups < 0) or np.any(groups >= len(GROUPS)):
        raise ValueError('known eleven-group indices required')
    physical = groups < 7
    if np.any(values[physical] < -tolerances[physical]):
        raise ValueError('a linear short step must start at a physical-row-feasible state')
    width = upper-lower
    scale = np.where(width > 0, float(trust_fraction)*width, 1.)
    JD = J*scale[None, :]
    gamma = float(Q(cfg['linear_fraction_to_boundary_exact']))
    m = len(values)
    A = np.zeros((m+1+2*n, n+2), float)
    b = np.empty(m+1+2*n, float)
    A[:m, :n] = -JD
    b[:m] = values
    b[:m][physical] = gamma*(values[physical]+tolerances[physical])
    A[:m, n][~physical] = -1.
    cap_row = np.asarray(cap_row, float)
    if cap_row.shape != state.shape or not np.all(np.isfinite(cap_row)) or not np.isfinite(cap_margin):
        raise ValueError('finite original affine cap data required')
    A[m, :n] = -cap_row*scale
    b[m] = float(cap_margin)
    for j in range(n):
        A[m+1+j, j] = 1.; A[m+1+j, n+1] = -1.
        A[m+1+n+j, j] = -1.; A[m+1+n+j, n+1] = -1.
    b[m+1:] = 0.
    lo = np.maximum(-1., (lower-state)/scale)
    hi = np.minimum(1., (upper-state)/scale)
    if np.any(lo > hi):
        raise ValueError('accepted state is outside its unchanged physical box')
    objective = np.zeros(n+2)
    objective[n] = 1.
    objective[n+1] = float(Q(cfg['linear_step_norm_weight_exact']))
    bounds = list(zip(lo, hi)) + [(0., None), (0., 1.)]
    before = time.monotonic()
    result = linprog(objective, A_ub=A, b_ub=b, bounds=bounds, method='highs',
        options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
                 'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],
                 'time_limit':float(cfg['linear_program_seconds'])})
    initial_slack = max(0., float(np.max(-values[~physical]))) if np.any(~physical) else 0.
    report = {
        'method':'scipy.optimize.linprog(method=highs)',
        'success':bool(result.success), 'status':int(result.status), 'message':str(result.message),
        'nit':int(result.nit), 'elapsed_seconds':time.monotonic()-before,
        'rows':len(b), 'variables':n+2, 'matrix_bytes':int(A.nbytes),
        'trust_fraction':float(trust_fraction), 'initial_curvature_slack':initial_slack,
        'curvature_target_not_an_optimization_variable':True,
        'physical_rows_and_cap_not_given_elastic_slack':True,
    }
    if result.x is None or not np.all(np.isfinite(result.x)):
        return None, report
    x = np.asarray(result.x, float)
    residual = float(np.max(A@x-b))
    bound_residual = max(float(np.max(lo-x[:n])), float(np.max(x[:n]-hi)),
                         -float(x[n]), -float(x[n+1]), float(x[n+1]-1))
    step = scale*x[:n]
    report.update(
        predicted_curvature_slack=float(x[n]), normalized_step_norm=float(x[n+1]),
        linear_objective=float(result.fun), maximum_linear_row_violation=max(0., residual),
        maximum_linear_bound_violation=max(0., bound_residual),
        maximum_absolute_physical_step=float(np.max(abs(step))),
        physical_step_l2=float(np.linalg.norm(step)),
        predicted_slack_improvement=initial_slack-float(x[n]),
    )
    if (not result.success or max(residual, bound_residual) > cfg['linear_model_residual_limit']):
        report['proposal_rejected_before_geometry'] = 'LP return or independent linear residual'
        return None, report
    return step, report


def compact_decision(d):
    keys = ['eligible_under_fixed_metric_and_physical_gates',
        'physical_gate_pass_excluding_fixed_metric', 'fixed_metric_budget_pass',
        'direct_max_eta', 'direct_max_eta_location',
        'direct_maximum_absolute_principal_curvature', 'direct_max_curvature_location',
        'curvature_auxiliary_lambda', 'direct_curvature_minus_lambda',
        'curvature_lambda_bound_pass', 'minimum_signed_height',
        'ball_radius_squared_normalized_max', 'maximum_absolute_y',
        'inner_strip_absolute_margin', 'direct_mirror_radius_min_finite',
        'regularity_screen_pass', 'cap_and_box']
    return {k:copy.deepcopy(d[k]) for k in keys if k in d}


class FeasibleStepObjective(PreviousObjective):
    def __init__(self, *args, **kwargs):
        self.fine_evaluations = 0
        self.fine_value_seconds = 0.
        self.fine_cache = None
        self.saved_coarse_trials = {}
        self.saved_fine_trials = []
        self.accepted_iterates = []
        super().__init__(*args, **kwargs)
        self.evaluation_definition.update(
            short_step_policy=POLICY,
            fixed_curvature_target_exact=self.cfg['fixed_curvature_target_exact'],
            fine_value_grid={'angular_nodes':2*len(self.theta),
                             'radial_nodes_unchanged':True,'no_Jacobian_requested':True},
            shared_physical_budget_counts='coarse plus doubled-angle full value geometry calls',
            implementation_source_sha256=implementation_hashes())
        self.evaluation_sha256 = digest(self.evaluation_definition)

    @property
    def full_value_evaluations(self):
        return self.geometry_evaluations+self.fine_evaluations

    def physical_geometry(self, state):
        hit = self.geometry_cache is not None and np.array_equal(state, self.geometry_cache['state'])
        if not hit and self.full_value_evaluations >= self.cfg['max_physical_evaluations']:
            raise EvaluationBudgetReached('shared coarse plus fine full-value physical budget reached')
        return super().physical_geometry(state)

    def _capture_coarse(self):
        cached = self.epigraph_cache
        if cached is None:
            return
        record = cached['record']
        number = record['physical_geometry_evaluation']
        if number in self.saved_coarse_trials:
            return
        state = cached['vector'][:-1]
        self.saved_coarse_trials[number] = {
            'coarse_physical_evaluation':number,
            'epigraph_evaluation':record['epigraph_evaluation'],
            'physical_state_sha256':digest(self.problem.identity(state)),
            'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
            'physical_parameter_coefficients_binary64':state.tolist(),
            'fixed_target_lambda':float(Q(self.cfg['fixed_curvature_target_exact'])),
            'decision':copy.deepcopy(record['decision']),
        }

    def evaluate(self, vector):
        try:
            return super().evaluate(vector)
        finally:
            self._capture_coarse()

    def fine_decision(self, state):
        state = np.asarray(state, float)
        self.assert_context(state)
        self._wall()
        if self.fine_cache is not None and np.array_equal(state, self.fine_cache['state']):
            return self.fine_cache['decision']
        if self.full_value_evaluations >= self.cfg['max_physical_evaluations']:
            raise EvaluationBudgetReached('shared coarse plus fine full-value physical budget reached')
        before = time.monotonic()
        self.fine_evaluations += 1
        saved = {
            'fine_value_evaluation':self.fine_evaluations,
            'combined_value_evaluation':self.full_value_evaluations,
            'physical_state_sha256':digest(self.problem.identity(state)),
            'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
            'status':'doubled-angle-value-call-started',
            'no_parameter_step_or_Jacobian_in_this_fine_evaluation':True,
        }
        self.saved_fine_trials.append(saved)
        try:
            theta = np.arange(2*len(self.theta))*np.pi/len(self.theta)
            data = self.problem.geometry(state, self.radial, theta, self.order, jacobian=False)
            expected = (len(self.radial), len(theta), 3)
            for key in POSITION_JETS:
                if np.asarray(data[key]).shape != expected or not np.all(np.isfinite(data[key])):
                    raise FloatingPointError('finite doubled-angle ordinary jets required: '+key)
            zeta = float(Q(self.cfg['fixed_curvature_target_exact']))/float(Q(self.cfg['curvature_scale_exact']))
            decision = candidate_decision(self.problem, self.gate, state, zeta, data,
                                          self.lower, self.upper, self.cfg)
            self.fine_cache = {'state':state.copy(), 'data':data, 'decision':copy.deepcopy(decision)}
            saved.update(status='complete-doubled-angle-value-call', decision=copy.deepcopy(decision))
        except Exception as error:
            saved.update(status='failed-doubled-angle-value-call',
                error={'type':type(error).__name__, 'message':str(error)})
            raise
        finally:
            saved['elapsed_seconds'] = time.monotonic()-before
            self.fine_value_seconds += saved['elapsed_seconds']
        self._wall()
        return decision

    def accepted_point(self, state, coarse, fine, reason):
        state = np.asarray(state, float)
        if not (coarse['eligible_under_fixed_metric_and_physical_gates']
                and fine['eligible_under_fixed_metric_and_physical_gates']):
            raise ValueError('only both-grid physically eligible states can become iterates')
        point = {
            'accepted_index':len(self.accepted_iterates),
            'physical_state_sha256':digest(self.problem.identity(state)),
            'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
            'physical_parameter_coefficients_binary64':state.tolist(),
            'coarse':compact_decision(coarse), 'fine':compact_decision(fine),
            'maximum_curvature_on_both_grids':max(
                coarse['direct_maximum_absolute_principal_curvature'],
                fine['direct_maximum_absolute_principal_curvature']),
            'reason':copy.deepcopy(reason),
        }
        self.accepted_iterates.append(point)
        return point

    def snapshot(self):
        self._capture_coarse()
        snap = super().snapshot()
        snap.update(
            short_step_policy=POLICY,
            fixed_target_lambda_exact=self.cfg['fixed_curvature_target_exact'],
            doubled_angle_full_value_evaluations=self.fine_evaluations,
            total_full_value_physical_evaluations=self.full_value_evaluations,
            doubled_angle_value_seconds=self.fine_value_seconds,
            saved_coarse_trials=list(self.saved_coarse_trials.values()),
            saved_fine_trials=copy.deepcopy(self.saved_fine_trials),
            accepted_iterates=copy.deepcopy(self.accepted_iterates),
            selected_two_grid_physical_point=copy.deepcopy(
                self.accepted_iterates[-1] if self.accepted_iterates else None),
            coarse_only_best_is_not_the_final_two_grid_selection=True)
        return snap


def run_feasible_steps(objective, initial, *, artificial_inputs_only=False, evaluate_only=False):
    if not artificial_inputs_only:
        require_public_research_environment()
    elif objective.gate.kind != 'artificial-array' and not evaluate_only:
        raise ValueError('local nonlinear evaluation requires the declared artificial array family')
    cfg = objective.cfg
    target = float(Q(cfg['fixed_curvature_target_exact']))
    scale = float(Q(cfg['curvature_scale_exact']))
    zeta = target/scale
    metadata = {
        'method':'fixed target linear proposals with two-grid true physical acceptance',
        'fixed_target_lambda_exact':cfg['fixed_curvature_target_exact'],
        'nonlinear_minimize_invocation_count':0,
        'linear_program_invocation_count':0,
        'max_linear_models':cfg['max_linear_models'],
        'shared_max_physical_evaluations_coarse_plus_fine':cfg['max_physical_evaluations'],
        'shared_optimization_seconds':cfg['max_seconds'],
        'artificial_inputs_only':bool(artificial_inputs_only),
        'evaluate_only':bool(evaluate_only),
        'numpy_version':np.__version__, 'scipy_version':scipy.__version__,
        'models':[], 'acceptance_uses_original_physical_tolerances_on_both_grids':True,
        'LP_slack_and_step_norm_are_not_physical_parameters':True,
        'rejected_trial_is_never_the_next_linearization_state':True,
    }
    def finish(status, error=None, budget=None):
        snap = objective.snapshot()
        if objective.checkpoint:
            objective.checkpoint(snap)
        selected = snap.get('selected_two_grid_physical_point')
        return {
            'status':status, 'error':error, 'budget_message':budget,
            'solver':metadata, 'checkpoint':snap,
            'selected_point':'last accepted both-grid physical state with monotone true maximum curvature',
            'fixed_target_reached':bool(selected is not None and
                selected['maximum_curvature_on_both_grids'] <= target+cfg['direct_curvature_tolerance']),
            'target_70_and_actual_progress_are_distinct':True,
            'no_metric_parameter_or_height_reference_change':True,
        }
    try:
        current = np.asarray(initial, float).copy()
        vector = np.r_[current, zeta]
        first = objective.evaluate(vector)['decision']
        if not first['eligible_under_fixed_metric_and_physical_gates']:
            return finish('initial-coarse-physical-gate-failed')
        fine = objective.fine_decision(current)
        if not fine['eligible_under_fixed_metric_and_physical_gates']:
            return finish('initial-fine-physical-gate-failed')
        accepted = objective.accepted_point(current, first, fine, {'kind':'original-accepted-e407-baseline'})
        if not len(objective.pool):
            objective.initialize_pool(vector)
        objective.expand_pool(vector, 'fixed-target-initial-known-violations')
        if evaluate_only:
            return finish('evaluation-only-two-grid-fixed-target-physical-baseline')
        if accepted['maximum_curvature_on_both_grids'] <= target+cfg['direct_curvature_tolerance']:
            return finish('fixed-target-already-reached-on-both-grids')
        objective.active_derivatives(vector)
        objective.begin_optimization()
        trust = float(Q(cfg['initial_trust_box_fraction_exact']))
        minimum_trust = float(Q(cfg['minimum_trust_box_fraction_exact']))
        minimum_drop = float(Q(cfg['minimum_accepted_curvature_decrease_exact']))
        for number in range(int(cfg['max_linear_models'])):
            objective._wall()
            vector = np.r_[current, zeta]
            coarse = objective.evaluate(vector)['decision']
            if not coarse['eligible_under_fixed_metric_and_physical_gates']:
                raise ArithmeticError('accepted coarse state lost its unchanged physical identity or gates')
            rows = objective.constraint_fun(vector)
            J = objective.constraint_jac(vector)[:, :objective.n]
            group = objective.pool//(len(objective.radial)*len(objective.theta))
            remaining = cfg['max_seconds']-(time.monotonic()-objective.optimization_started)
            local_cfg = dict(cfg, linear_program_seconds=min(cfg['linear_program_seconds'], max(.001, remaining)))
            step, lp = linear_proposal(rows, J, group, objective.row_tolerances()[group],
                current, objective.lower, objective.upper, objective.gate.row,
                objective.gate.intercept+float(objective.gate.row@current)-objective.gate.target,
                trust, local_cfg)
            metadata['linear_program_invocation_count'] += 1
            model = {'number':number+1, 'linearized_at_accepted_index':accepted['accepted_index'],
                'linearized_at_physical_sha256':accepted['physical_state_sha256'],
                'pool_rows':len(objective.pool), 'linear_program':lp, 'trials':[]}
            metadata['models'].append(model)
            objective._wall()
            if step is None:
                trust *= .5
                model['result'] = 'linear-proposal-rejected-trust-shrunk'
                if trust < minimum_trust:
                    return finish('minimum-trust-after-linear-proposal-failure')
                continue
            if (lp['predicted_slack_improvement'] <= cfg['linear_model_improvement_floor']
                    or np.max(abs(step)) == 0):
                model['result'] = 'no-fixed-target-linear-improvement'
                return finish('fixed-target-linear-model-stalled')
            model['exact_binary64_proposed_step'] = [str(Q.from_float(float(x))) for x in step]
            old_maximum = accepted['maximum_curvature_on_both_grids']
            succeeded = False
            for k in range(int(cfg['maximum_backtracks_per_model'])):
                alpha = 2.**(-k)
                candidate = current+alpha*step
                trial = {'alpha_exact':str(Q(1,2**k)),
                    'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in candidate],
                    'attempt_status':'coarse-value-call-started', 'accepted_as_next_iterate':False}
                model['trials'].append(trial)
                record = objective.evaluate(np.r_[candidate, zeta])
                decision = record['decision']
                trial.update(attempt_status='coarse-value-call-complete', **{
                    'coarse_physical_evaluation':record['physical_geometry_evaluation'],
                    'coarse_decision':compact_decision(decision),
                })
                good = decision['eligible_under_fixed_metric_and_physical_gates']
                coarse_k = decision['direct_maximum_absolute_principal_curvature']
                potentially_better = coarse_k <= target+cfg['direct_curvature_tolerance'] or old_maximum-coarse_k >= minimum_drop
                fine_dec = None
                if good and potentially_better:
                    fine_dec = objective.fine_decision(candidate)
                    trial['fine_decision'] = compact_decision(fine_dec)
                    trial['fine_value_evaluation'] = objective.fine_evaluations
                    new_k = max(coarse_k, fine_dec['direct_maximum_absolute_principal_curvature'])
                    reached = new_k <= target+cfg['direct_curvature_tolerance']
                    if (fine_dec['eligible_under_fixed_metric_and_physical_gates']
                            and new_k < old_maximum
                            and (reached or old_maximum-new_k >= minimum_drop)):
                        accepted = objective.accepted_point(candidate, decision, fine_dec,
                            {'kind':'two-grid-accepted-fixed-target-short-step','model':number+1,
                             'alpha_exact':str(Q(1,2**k)), 'previous_maximum_curvature':old_maximum})
                        current = candidate.copy()
                        trial['accepted_as_next_iterate'] = True
                        trial['accepted_index'] = accepted['accepted_index']
                        succeeded = True
                addition, detail = objective.expand_pool(np.r_[candidate, zeta],
                    'whole-grid-observed-rows-from-trial-not-an-infeasible-warm-start')
                trial['omitted_rows_observed'] = detail['omitted_violating_count']
                trial['pool_after_learning'] = len(objective.pool)
                trial['new_rows_learned'] = len(addition['added_row_indices']) if addition else 0
                if detail.get('pool_capacity_would_be_exceeded'):
                    return finish('row-capacity-preserved-last-two-grid-accepted-state')
                if succeeded:
                    model['result'] = 'accepted-true-physical-short-step'
                    if objective.checkpoint:
                        objective.checkpoint(objective.snapshot())
                    if accepted['maximum_curvature_on_both_grids'] <= target+cfg['direct_curvature_tolerance']:
                        return finish('fixed-curvature-target-reached-on-both-value-grids')
                    break
            if not succeeded:
                trust *= .5
                model['result'] = 'all-backtracks-rejected-last-feasible-state-preserved'
                if trust < minimum_trust:
                    return finish('minimum-trust-after-full-grid-backtracking')
            if objective.checkpoint:
                objective.checkpoint(objective.snapshot())
        return finish('fixed-target-linear-model-budget-exit')
    except EvaluationBudgetReached as error:
        return finish('shared-fixed-target-short-step-budget-exit', budget=str(error))
    except Exception as error:
        return finish('fixed-target-short-step-error',
            error={'type':type(error).__name__, 'message':str(error)})


class _StepToy:
    """One scalar, exact artificial rows, and an intentionally stricter fine grid."""
    def __init__(self, target=2.8, fine_limit=.3, inject_fine_failure=False):
        self.n=1; self.lower=np.array([-2.]); self.upper=np.array([2.])
        self.radial=np.array([0.]); self.theta=np.array([0., np.pi])
        self.cfg=configuration(); self.cfg.update(curvature_scale_exact='1',
            fixed_curvature_target_exact=str(target), max_seconds=10.,
            initial_trust_box_fraction_exact='1/4', minimum_accepted_curvature_decrease_exact='1/1000000')
        self.gate=SimpleNamespace(kind='artificial-array', row=np.zeros(1), intercept=1., target=0.)
        self.pool=np.array([0,16],int); self.checkpoint=None; self.pool_version=1
        self.started=time.monotonic(); self.optimization_started=None
        self.geometry_evaluations=0; self.fine_evaluations=0; self.last=None; self.record=None
        self.accepted_iterates=[]; self.coarse_records=[]; self.fine_records=[]
        self.fine_limit=fine_limit; self.inject_fine_failure=inject_fine_failure
    def _wall(self):
        if self.optimization_started is not None and time.monotonic()-self.optimization_started>10:
            raise EvaluationBudgetReached('artificial clock')
    def begin_optimization(self):
        self.optimization_started=time.monotonic()
    def rows(self, vector):
        x, lam=vector
        a=np.ones((11,1,2)); a.flat[0]=1-x*x; a.flat[6]=.4-x; a.flat[16]=lam-(3-x)
        return a
    def row_tolerances(self):
        return np.full(11,1e-9)
    def evaluate(self, vector):
        vector=np.asarray(vector,float)
        if self.last is not None and np.array_equal(vector,self.last): return self.record
        if self.geometry_evaluations+self.fine_evaluations>=self.cfg['max_physical_evaluations']:
            raise EvaluationBudgetReached('artificial shared coarse/fine budget')
        self._wall(); self.geometry_evaluations+=1
        x=float(vector[0]); good=bool(-2<=x<=2 and 1-x*x>=-1e-9 and .4-x>=-1e-9)
        decision={'eligible_under_fixed_metric_and_physical_gates':good,
            'direct_maximum_absolute_principal_curvature':3-x}
        self.record={'physical_geometry_evaluation':self.geometry_evaluations,'decision':decision}
        self.last=vector.copy(); self.coarse_records.append({'vector':vector.tolist(),'decision':copy.deepcopy(decision)})
        return self.record
    def fine_decision(self,state):
        if self.geometry_evaluations+self.fine_evaluations>=self.cfg['max_physical_evaluations']:
            raise EvaluationBudgetReached('artificial shared coarse/fine budget')
        if self.inject_fine_failure and self.fine_evaluations:
            raise FloatingPointError('injected artificial fine failure')
        self.fine_evaluations+=1; x=float(state[0])
        d={'eligible_under_fixed_metric_and_physical_gates':bool(-2<=x<=self.fine_limit+1e-9),
           'direct_maximum_absolute_principal_curvature':3-x}
        self.fine_records.append({'state':[x],'decision':copy.deepcopy(d)})
        return d
    def accepted_point(self,state,coarse,fine,reason):
        if not(coarse['eligible_under_fixed_metric_and_physical_gates']
               and fine['eligible_under_fixed_metric_and_physical_gates']): raise ValueError('toy acceptance')
        p={'accepted_index':len(self.accepted_iterates),'physical_state_sha256':digest(np.asarray(state).tolist()),
            'exact_binary64_physical_coefficients':[str(Q.from_float(float(x))) for x in state],
            'physical_parameter_coefficients_binary64':np.asarray(state).tolist(),
            'maximum_curvature_on_both_grids':max(coarse['direct_maximum_absolute_principal_curvature'],
                                                fine['direct_maximum_absolute_principal_curvature']),
            'coarse':coarse,'fine':fine,'reason':reason}
        self.accepted_iterates.append(copy.deepcopy(p)); return p
    def initialize_pool(self,vector):
        raise AssertionError('toy starts with its deliberate sparse pool')
    def expand_pool(self,vector,reason):
        self.evaluate(vector); rows=self.rows(vector); missing=rows<-1e-9; missing.flat[self.pool]=False
        ids=np.flatnonzero(missing); detail={'omitted_violating_count':len(ids)}
        if not len(ids): return None,detail
        self.pool=np.unique(np.r_[self.pool,ids]); self.pool_version+=1
        return {'added_row_indices':ids.tolist(),'reason':reason},detail
    def active_derivatives(self,vector):
        return self.constraint_jac(vector)
    def constraint_fun(self,vector):
        self.evaluate(vector); return self.rows(vector).reshape(-1)[self.pool]
    def constraint_jac(self,vector):
        self.evaluate(vector); J=np.zeros((22,2))
        J[0,0]=-2*vector[0]; J[6,0]=-1.; J[16]=[1.,1.]
        return J[self.pool]
    def snapshot(self):
        return {'selected_two_grid_physical_point':copy.deepcopy(self.accepted_iterates[-1] if self.accepted_iterates else None),
            'accepted_iterates':copy.deepcopy(self.accepted_iterates),
            'saved_coarse_trials':copy.deepcopy(self.coarse_records),
            'saved_fine_trials':copy.deepcopy(self.fine_records),
            'physical_geometry_evaluations':self.geometry_evaluations,
            'doubled_angle_full_value_evaluations':self.fine_evaluations,
            'total_full_value_physical_evaluations':self.geometry_evaluations+self.fine_evaluations}


def developer_check():
    initial=np.array([0.])
    attainable=_StepToy()
    one=run_feasible_steps(attainable,initial,artificial_inputs_only=True)
    limited=_StepToy(target=2.5)
    two=run_feasible_steps(limited,initial,artificial_inputs_only=True)
    failed=_StepToy(inject_fine_failure=True)
    three=run_feasible_steps(failed,initial,artificial_inputs_only=True)
    accepted=two['checkpoint']['accepted_iterates']
    monotone=all(accepted[i+1]['maximum_curvature_on_both_grids']<accepted[i]['maximum_curvature_on_both_grids']
                 for i in range(len(accepted)-1))
    reject_fine=any(not r['decision']['eligible_under_fixed_metric_and_physical_gates']
                    for r in two['checkpoint']['saved_fine_trials'])
    preserved=all(p['physical_parameter_coefficients_binary64'][0]<=.3+1e-9 for p in accepted)
    all_targets=all(abs(r['vector'][-1]-2.5)<1e-15 for r in two['checkpoint']['saved_coarse_trials'])
    last=two['checkpoint']['selected_two_grid_physical_point']
    failure_kept=three['status']=='fixed-target-short-step-error' and len(three['checkpoint']['accepted_iterates'])==1
    learned=any(t.get('new_rows_learned',0)>0 for m in two['solver']['models'] for t in m['trials'])
    passed=bool(one['fixed_target_reached'] and not two['fixed_target_reached'] and monotone and reject_fine
        and preserved and all_targets and failure_kept and learned and last['maximum_curvature_on_both_grids']<3)
    return {'schema':'fixed-target-short-step-artificial-check-v1','artificial_inputs_only':True,
        'research_geometry_evaluated_or_optimized':False,'no_Actions_environment_is_forged':True,
        'attainable_target_status':one['status'],'attainable_target_pass':one['fixed_target_reached'],
        'fine_blocked_target_status':two['status'],'unreached_target_not_claimed':not two['fixed_target_reached'],
        'accepted_curvature_monotone':monotone,'fine_failing_candidates_rejected':reject_fine and preserved,
        'all_target_values_fixed':all_targets,'failed_fine_call_preserves_original':failure_kept,
        'rejected_trial_teaches_missing_rows':learned,
        'fine_calls_count_toward_physical_budget':two['checkpoint']['total_full_value_physical_evaluations']
            ==two['checkpoint']['physical_geometry_evaluations']+two['checkpoint']['doubled_angle_full_value_evaluations'],
        'last_artificial_accepted_point':last,'passed':passed}

