#!/usr/bin/env python3
"""Actual R080 full-position static design along the canonical R631 core.

Reconstruct the new field, solve its own base, and automatically continue
mu toward one. H, W, E and the true F2 germ amplitude are design variables.
This is not an isometric motion under an inherited R085 metric. Every
complete J row, all columns and all singular directions enter QR/SVD.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time

import numpy as np

HERE = Path(__file__).resolve().parent
SCHEMA = 'new-R080-full-position-R631-adaptive-core-design-v1'
BINDINGS = {
    'factory': ('r631_radius080_design_factory_20261128.py', 'b2ec6744c47992c08407652488d5a7bb593902b7adce15f610330d8925e7c8e5'),
    'model': ('r631_radius080_hard_trace_design_20261128.py', '5fc7b6cb112e9ef659b0a61e3adb8a7981a8c0f50ec2d8d38e208edb49b9efcb'),
    'path': ('r631_radius080_convex_core_input_path_20261128.py', '574e1f6a1d0865a3d871ecd5999ac79dc367375708fa07a2f8f31b86393fdf8a'),
    'factor': ('r631_complete_two_rhs_qr_svd_20261128.py', 'c45559d99fbcaa7220e50d2907210549e8f2f74202420a0a16184e4d34f3bda3'),
    'consumers': ('r631_radius080_design_consumers_20261128.py', '48a447963870ac0a1fc8f156e5e8b56a3f3bbc6a382faaf4903da19ef013fcad'),
}
COUNTS, REJECTIONS = defaultdict(int), defaultdict(int)


def sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def emit(tag, value):
    print('R631_DESIGN_'+tag+' '+json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False), flush=True)


def load(label):
    filename, expected = BINDINGS[label]
    path = HERE/filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError('source-bound actual design component differs: '+filename)
    name = 'r631_actual_'+label
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class RuleChange(Exception):
    pass


class SolverReserve(Exception):
    pass


class Rules:
    def __init__(self, request_path, deadline):
        path = Path(request_path)
        self.request = json.loads(path.read_text())
        runner = HERE/'run_inverse_state_stdin_20261126.py'
        relative = str(runner.relative_to(Path.cwd()))
        if hashlib.sha256(runner.read_bytes()).hexdigest() != self.request['source_sha256'][relative]:
            raise ValueError('the published actual-pull implementation differs')
        spec = importlib.util.spec_from_file_location('r631_actual_rule_pull', runner)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.source = os.environ['GITHUB_SHA']
        self.last, self.deadline = time.monotonic(), deadline
        self.receipts = []

    def check(self):
        now = time.monotonic()
        if now-self.last < 3300:
            return
        row = {'before_elapsed_since_previous_check': now-self.last,
            'actual_public_pull_and_both_README_exact_differences': True,
            'private_hourly_pull_owned_by_active_parent_session': self.request['queue_session']}
        self.receipts.append(row)
        try:
            row['after_pull_commit'] = self.module.public_pull(Path.cwd(), self.request, self.source)
            self.module.git(Path.cwd(), 'checkout', '--detach', self.source)
            row['same_scientific_source_restored_after_rule_comparison'] = True
            row['status'] = 'unchanged_rules_continue_same_declared_source'
            self.last = time.monotonic()
        except Exception as exc:
            row['status'] = 'rule_difference_or_pull_failure_stop_old_scope_with_actual_state'
            row['failure_type'] = type(exc).__name__
            raise RuleChange('hourly public pull / README check failed; preserve state and apply printed differences') from exc
        emit('HOURLY_RULES', row)


def embed_response(old_model, old_q, new_model):
    """Exact old dictionary inclusion; no old coordinate is discarded."""
    q = new_model.initial_response()
    q[:old_model.old_count] = old_q[:old_model.old_count]
    if new_model.J < old_model.J:
        raise ValueError('a declared old mode would be discarded')
    for index, mode in enumerate(old_model.extra_compact_modes):
        j = int(np.nonzero(new_model.extra_compact_modes == mode)[0][0])
        n = old_model.compact.COMPACT_NB
        q[new_model.compact_start+j*n:new_model.compact_start+(j+1)*n] = old_q[old_model.compact_start+index*n:old_model.compact_start+(index+1)*n]
    for index, mode in enumerate(old_model.modes):
        j = int(np.nonzero(new_model.modes == mode)[0][0])
        n = len(old_model.tail_degrees)
        q[new_model.tail_start+j*n:new_model.tail_start+(j+1)*n] = old_q[old_model.tail_start+index*n:old_model.tail_start+(index+1)*n]
    q[new_model.j2_germ_index] = old_q[old_model.j2_germ_index]
    return q


def function_changes(model, q_direction, data, state, external=None):
    jets, dw, _ = model.combined_height_direction(q_direction, data)
    if external is not None:
        for key in jets:
            jets[key] = jets[key]+external['six_height_jets'][key][:, :, 0]
    r, g = data['r'][:, None], state['g']
    p, b, N, u = [g[key] for key in ('p', 'b', 'N', 'u')]
    w, fr, ft, ftt = [state[key] for key in ('w', 'fr', 'ft', 'ftt')]
    dfr, dft, dftt = [jets[key] for key in ('fr', 'ft', 'ftt')]
    dp = -dw+dfr
    dN = r*ft*dft/b**3+r*r*(ftt*dp+p*dftt)/b**3+3*r*r*p*ftt*ft*dft/b**5
    dshift = -2*dw*fr-2*w*dfr+2*fr*dfr+2*p*dp*ft*ft/b**2+2*p*p*ft*dft/b**2+2*p*p*ft**3*dft/b**4
    de = (2*np.mean(dN/u, axis=1, keepdims=True)+np.mean(N*dshift/u**3, axis=1, keepdims=True))/np.mean(N/u**3, axis=1, keepdims=True)
    du, db = (de-dshift)/(2*u), -ft*dft/b
    dz = jets['f']+q_direction[0]*data['gain_height'][:, None]
    changes = {'relative_b': float(np.max(abs(db)/b)), 'relative_u': float(np.max(abs(du)/u)),
        'relative_N': float(np.max(abs(dN)/N)), 'relative_positive_Z': float(np.max(abs(dz)/g['Z'])),
        'height_theta_over_r': float(np.max(abs(dft)/r)),
        'height_r_over_one_plus_W': float(np.max(abs(dfr)/(1+abs(w)))),
        'W_over_one_plus_W': float(np.max(abs(dw)/(1+abs(w))))}
    maximum = max(changes.values())
    if not np.isfinite(maximum):
        raise ArithmeticError('nonfinite actual complete physical direction')
    COUNTS['actual_combined_function_direction_limits'] += 1
    return maximum, {'actual_six_jet_and_implicit_turning_changes': changes,
        'external_total_P_derivative_included': external is not None,
        'H_W_and_E_derivatives_retained': True, 'nonlinear_or_continuous_domain_certificate': False}


def radial_view(value, first, last, original_rows, *, key=''):
    if isinstance(value, np.ndarray):
        if value.ndim and value.shape[0] == original_rows and key not in ('q', 'theta', 'primitive', 'derivative', 'second_derivative'):
            return value[first:last]
        return value
    if isinstance(value, dict):
        if key in ('core', 'paid_height_cache'):
            return value
        return {name: radial_view(item, first, last, original_rows, key=name) for name, item in value.items()}
    return value


class DesignRun:
    def __init__(self, incoming, args, modules, started):
        self.input, self.args, self.modules, self.started = incoming, args, modules, started
        self.deadline = started+args.maximum_seconds
        self.solver_deadline = self.deadline-args.final_reserve_seconds
        self.rules = Rules(args.request_path, self.deadline)
        self.factory = self.path = self.seed_model = None
        self.attempts = []
        self.current = self.completed = self.pending = self.last_trial = None
        self.current_record = self.completed_record = None
        self.history, self.failure_history = [], []
        self.readout = None
        self.damping = incoming['solver']['initial_damping']
        self.accepted_steps = 0
        self.last_spectrum = None

    def check(self, solver=False):
        self.rules.check()
        if self.factory is not None:
            self.factory.driver.check(self.deadline)
        elif time.monotonic() >= self.deadline:
            raise SolverReserve('declared clock before new-radius factory completed')
        if solver and time.monotonic() >= self.solver_deadline:
            raise SolverReserve('declared reserve for complete fine and actual-position readout')

    def checkpoint(self, label):
        model, q, data, state, core_input, mu, fine = self.current
        observation = self.modules['consumers'].complete_observation(model, q, data, state)
        record = {'status': label, 'mu_literal': str(mu), 'maximum_independent_mode': model.J,
            'fine_grid_active': fine, 'actual_complete_q': q.tolist(), 'actual_q_sha256': sha(q.tolist()),
            'actual_prescribed_total_P0': model.prescribed_pc.tolist(),
            'actual_core_input': {k: v for k, v in core_input.items() if k != 'continuous_function_definition'},
            'actual_next_damping': self.damping, 'accepted_Newton_steps': self.accepted_steps,
            'observation': observation, 'elapsed_seconds': time.monotonic()-self.started,
            'metric_is_this_actual_trial_E_not_old_fixed_g': True}
        self.current_record = record
        emit('CHECKPOINT', record)
        return observation

    def enforce_sampled_ball(self, model, data, state):
        """Actual nonlinear design budget, never a global ball certificate."""
        g = state['g']
        body = float(np.max(np.sqrt(np.sum(g['Y']**2, axis=2)+g['Z']**2)))
        key = len(data['theta'])
        cache = getattr(model, 'new_design_core_ball_observations', {})
        if key not in cache:
            core = model.core_state(state['q'], model.amplitude, data['theta'])
            phi = data['theta']+(1/core['u']-1)@data['primitive'].T
            tangent = np.stack([-np.sin(phi), np.cos(phi)], axis=1)
            Y = np.stack([(model.par.R*tangent[:, k])@data['primitive'].T for k in range(2)], axis=1)
            cache[key] = float(np.max(np.sqrt(np.sum(Y**2, axis=1)+model.par.core_height**2)))
            model.new_design_core_ball_observations = cache
            COUNTS['actual_finite_core_ball_grid_evaluations'] += 1
        COUNTS['actual_nonlinear_body_ball_budget_observations'] += 1
        if max(body, cache[key]) > model.par.ball_budget:
            raise model.driver.base.DomainError('actual sampled new-design body/core ball exceeds R631 budget')
        return {'sampled_body_ball': body, 'sampled_core_ball': cache[key],
            'declared_new_ball_budget': model.par.ball_budget, 'continuous_ball_certificate': False}

    def build_input(self, mu, minimum_J):
        levels = self.input['solver']['independent_mode_levels']
        for J in levels:
            if J < minimum_J:
                continue
            self.check(solver=True)
            value = self.path.input(str(mu), maximum_mode=J,
                angular_points=max(self.input['path_angular_points'], 8*J))
            error = value['fine_observations']['sampled_J_projection_error']
            if error <= self.input['solver']['core_projection_observation_target'] or J == levels[-1]:
                break
        value['finite_projection_observation_target_met'] = error <= self.input['solver']['core_projection_observation_target']
        # The entire continuous R631 function is unchanged when J increases.
        # The actual finite P and its own turning root remain explicit.
        return value

    def make_current(self, mu, core_input, source_model, source_q, *, fine=False):
        policy = dict(self.input['model_policy'])
        policy['maximum_independent_mode'] = core_input['maximum_independent_mode']
        policy['core_points'] = max(policy['core_points'], 8*policy['maximum_independent_mode'])
        model = self.modules['model'].Radius080HardTraceDesign(self.factory, policy,
            prescribed_pc=core_input['P0_coefficients'], trace_input_provenance={
                'continuous_input_definition_sha256': core_input['continuous_function_definition_sha256'],
                'mu_literal': str(mu), 'finite_J': policy['maximum_independent_mode'],
                'actual_finite_P0_sha256': sha(core_input['P0_coefficients']),
                'finite_projection_is_not_exact_R631_support': True})
        model.radial_lift_cache = self.seed_model.radial_lift_cache
        q = embed_response(source_model, source_q, model)
        ntheta = 256
        while ntheta <= 4*model.J:
            ntheta *= 2
        if fine:
            ntheta = max(512, ntheta)
        radii = self.factory.fine_radii if fine else self.factory.work_radii
        data = model.prepare(radii, ntheta, grid_role='fine' if fine else 'work')
        self.pending = {'status': 'new_design_input_not_yet_validated', 'mu_literal': str(mu),
            'maximum_independent_mode': model.J, 'actual_q': q.tolist(),
            'actual_prescribed_P': model.prescribed_pc.tolist(), 'fine_grid': fine}
        state = model.evaluate(q, data)
        self.enforce_sampled_ball(model, data, state)
        self.current = (model, q, data, state, core_input, mu, fine)
        self.pending = None
        self.checkpoint('actual_new_input_domain_valid_before_connection_solve')

    def full_factor(self, external):
        model, q, data, state, _, _, _ = self.current
        residual, derivative = state['residual'], external['residual_direction']
        F = self.modules['factor'].CompleteTwoRHSFactor
        batch_rows = max(4096, model.nq+2)
        self.check(solver=True)
        if len(residual)*model.nq <= self.input['solver']['maximum_materialized_J_entries']:
            J = model.jacobian(q, data, state)
            COUNTS['logical_complete_J_analytic_passes'] += 1
            self.check(solver=True)
            factor = F(J, residual, derivative, batch_rows=batch_rows, deadline_check=lambda: self.check(solver=True))
            del J
        else:
            rows_per_radius = 2*len(data['all_position_odd_modes'])
            radial_block = max(1, batch_rows//rows_per_radius)
            nr = len(data['r'])
            def blocks(pass_number):
                for first in range(0, nr, radial_block):
                    self.check(solver=True)
                    last = min(nr, first+radial_block)
                    dv, sv = radial_view(data, first, last, nr), radial_view(state, first, last, nr)
                    Jblock = model.jacobian(q, dv, sv)
                    a, b = first*rows_per_radius, last*rows_per_radius
                    yield a, Jblock, residual[a:b], derivative[a:b]
                    del Jblock
                COUNTS['logical_complete_J_analytic_passes'] += 1
            factor = F.from_complete_row_passes(len(residual), model.nq, blocks,
                batch_rows=batch_rows, deadline_check=lambda: self.check(solver=True))
        self.last_spectrum = factor.spectrum()
        emit('COMPLETE_FACTOR', {'mu_literal': str(self.current[5]), 'spectrum': self.last_spectrum,
            'two_rhs_are_actual_Newton_and_actual_same_path_derivative': True,
            'all_original_rows_and_every_current_column_retained': True,
            'streaming_recomputations_charged_as_real_complete_J_passes': True})
        self.check(solver=True)
        return factor

    def solve_stage(self):
        """Actual full nonlinear solve; never just an initial-J diagnostic."""
        solver = self.input['solver']
        for iteration in range(solver['maximum_Newton_iterations_per_stage_attempt']):
            self.check(solver=True)
            model, q, data, state, core_input, mu, fine = self.current
            target = solver['final_eta_target'] if fine else solver['design_stage_eta_target']
            eta = float(np.max(state['g']['eta']))
            external = model.external_trace_field_direction(q, data, state,
                core_input['P0_path_derivative_coefficients'])
            # The first base/full J is a necessary predictor computation,
            # including when the small initial seed already meets eta.
            factor = self.full_factor(external)
            if eta <= target:
                predictor = factor.direction(self.damping, rhs=1)
                maximum, measures = function_changes(model, predictor, data, state, external)
                predictor_receipt = {'mu_literal': str(mu), 'same_complete_factor_used': True,
                    'actual_linearized_path_residual_norm': factor.residual_norm_after_direction(predictor, rhs=1),
                    'function_changes': measures, 'maximum_relative_function_change_per_unit_mu': maximum}
                emit('PATH_PREDICTOR', predictor_receipt)
                return {'status': 'actual_finite_stage_target_met', 'predictor': predictor,
                    'predictor_change': maximum, 'predictor_receipt': predictor_receipt, 'iterations': iteration}
            objective = float(state['residual']@state['residual']/2)
            accepted = False
            for trial in range(solver['damping_trials']):
                self.check(solver=True)
                lam = self.damping*10.**trial
                direction = factor.direction(lam, rhs=0)
                maximum, measures = function_changes(model, direction, data, state)
                physical_fraction = min(1., solver['maximum_relative_function_step']/maximum) if maximum else 1.
                direction *= physical_fraction
                for cut in range(solver['line_search_cuts']):
                    self.check(solver=True)
                    fraction = 2.**(-cut)
                    predicted = factor.predicted_decrease(direction, fraction)
                    COUNTS['line_search_algebraic_trials'] += 1
                    if not np.isfinite(predicted) or predicted <= 0:
                        REJECTIONS['nonpositive_full_row_prediction'] += 1
                        continue
                    proposed = q+fraction*direction
                    self.pending = {'status': 'actual_Newton_trial_not_accepted', 'mu_literal': str(mu),
                        'actual_complete_q': proposed.tolist(), 'trial': trial, 'fraction': fraction,
                        'predicted_decrease': predicted, 'lambda_used': lam}
                    COUNTS['actual_complete_nonlinear_trials_attempted'] += 1
                    try:
                        candidate = model.evaluate(proposed, data)
                        ball = self.enforce_sampled_ball(model, data, candidate)
                        candidate_objective = float(candidate['residual']@candidate['residual']/2)
                        if not np.isfinite(candidate_objective):
                            raise ArithmeticError('nonfinite complete nonlinear trial merit')
                        actual = objective-candidate_objective
                        ratio = actual/predicted
                        if not np.isfinite(ratio):
                            raise ArithmeticError('nonfinite actual versus full-row predicted decrease')
                        okay = (np.isfinite(candidate_objective) and np.isfinite(ratio)
                            and actual > max(32*np.finfo(float).eps*objective, 1e-30) and ratio > .01)
                        reason = 'no_resolvable_complete_position_decrease'
                        self.last_trial = {'actual_q_sha256': sha(proposed.tolist()), 'actual_decrease': actual,
                            'predicted_decrease': predicted, 'actual_over_predicted': ratio,
                            'accepted': bool(okay), 'mu_literal': str(mu), 'candidate_merit': candidate_objective,
                            'actual_nonlinear_geometry_budget_observation': ball}
                    except (model.driver.base.DomainError, ArithmeticError, ValueError, FloatingPointError) as exc:
                        okay, reason = False, type(exc).__name__+':'+str(exc)
                        self.last_trial = {'actual_q_sha256': sha(proposed.tolist()), 'failure': reason,
                            'accepted': False, 'mu_literal': str(mu)}
                    self.pending = None
                    if okay:
                        self.damping = max(1e-14, lam/3)
                        self.accepted_steps += 1
                        COUNTS['actual_Newton_steps_accepted'] += 1
                        self.current = (model, proposed, data, candidate, core_input, mu, fine)
                        emit('ACCEPTANCE', {'trial': trial, 'fraction': fraction,
                            'physical_fraction': physical_fraction, 'function_changes': measures,
                            'actual_next_damping': self.damping, **self.last_trial})
                        self.checkpoint('actual_complete_position_decrease_accepted')
                        self.check(solver=True)
                        accepted = True
                        break
                    COUNTS['actual_complete_nonlinear_trials_rejected'] += 1
                    REJECTIONS[reason] += 1
                if accepted:
                    break
            if not accepted:
                return {'status': 'finite_full_family_no_resolvable_step', 'iterations': iteration,
                    'full_spectrum': self.last_spectrum, 'not_an_impossibility_certificate': True}
        return {'status': 'stage_iteration_allocation_used_with_actual_progress',
            'iterations': solver['maximum_Newton_iterations_per_stage_attempt']}

    def execute(self):
        f, m, p = [self.modules[key] for key in ('factory', 'model', 'path')]
        self.factory = f.build_radius080_design(paid_reconstruction_json=self.input['R_independent_paid_reconstruction_JSON'],
            paid_reconstruction_sha256=self.input['R_independent_paid_reconstruction_sha256'],
            profile_input=self.input['new_mathematical_profile'], numerical_input=self.input['new_numerical_settings'],
            amplitude=self.input['amplitude'], deadline=self.deadline, attempts=self.attempts,
            force_normalization=self.input['new_force_normalization'])
        self.seed_model = m.Radius080HardTraceDesign(self.factory, self.input['model_policy'])
        self.path = p.Radius080ConvexCoreInputPath(self.seed_model, **self.input['path_settings'])
        emit('ACTUAL_NEW_DESIGN', {'factory': self.factory.guard(), 'seed_model': self.seed_model.guard(),
            'same_continuous_path_definition': self.path.definition, 'grid_receipt': self.factory.grid_receipt})
        core_input = self.build_input(Fraction(0), self.seed_model.J)
        self.make_current(Fraction(0), core_input, self.seed_model, self.seed_model.initial_response())
        step = Fraction(self.input['solver']['initial_mu_step'])
        maximum_step = Fraction(self.input['solver']['maximum_mu_step'])
        while True:
            self.check(solver=True)
            before_count = self.accepted_steps
            outcome = self.solve_stage()
            model, q, data, state, core_input, mu, fine = self.current
            if outcome['status'] == 'actual_finite_stage_target_met':
                self.completed = self.current
                self.checkpoint('actual_finite_stage_complete_connection_target_observed')
                self.completed_record = dict(self.current_record)
                self.history.append({'mu_literal': str(mu), 'J': model.J, 'fine_grid': fine,
                    'actual_q_sha256': self.current_record['actual_q_sha256'],
                    'eta_observation': self.current_record['observation']['eta_max_identity'],
                    'accepted_Newton_steps': self.accepted_steps,
                    'projection_target_met': core_input['finite_projection_observation_target_met']})
                if mu == 1:
                    if fine:
                        return 'actual_mu_one_full_fine_finite_connection_target_met'
                    self.make_current(mu, core_input, model, q, fine=True)
                    continue
                maximum = outcome['predictor_change']
                physical = self.input['solver']['maximum_relative_predictor_step']/maximum if maximum else float(maximum_step)
                proposed_step = min(maximum_step, step if len(self.history) == 1 else step*2, 1-mu)
                while float(proposed_step) > physical:
                    proposed_step /= 2
                # A dyadic rational records the actual mathematical input;
                # failure halves this step and consumes the actual state.
                while True:
                    self.check(solver=True)
                    next_mu = mu+proposed_step
                    next_input = self.build_input(next_mu, model.J)
                    prediction = q+float(proposed_step)*outcome['predictor']
                    try:
                        self.make_current(next_mu, next_input, model, prediction)
                        step = proposed_step
                        break
                    except (model.driver.base.DomainError, ArithmeticError, ValueError, FloatingPointError) as exc:
                        self.failure_history.append({'mu_literal': str(next_mu), 'attempt': 'actual_path_prediction_domain',
                            'failure': type(exc).__name__+':'+str(exc), 'source_mu_literal': str(mu),
                            'actual_trial_q_sha256': sha(prediction.tolist()), 'all_costs_retained': True})
                        REJECTIONS['path_prediction_domain'] += 1
                        proposed_step /= 2
                        if float(proposed_step) == 0 or float(next_mu) == float(mu):
                            raise ArithmeticError('actual continuation step reached floating resolution') from exc
                continue
            if outcome['status'] == 'stage_iteration_allocation_used_with_actual_progress':
                # This is an allocation boundary, never a small-mu stopping
                # criterion. Continue from the actual new accepted state.
                continue
            self.failure_history.append({'mu_literal': str(mu), 'J': model.J, **outcome,
                'actual_q_sha256': sha(q.tolist()), 'all_previous_work_retained': True})
            levels = self.input['solver']['independent_mode_levels']
            higher = [value for value in levels if value > model.J]
            if higher:
                next_input = self.build_input(mu, higher[0])
                self.make_current(mu, next_input, model, q, fine=fine)
                continue
            if self.completed is None or mu == self.completed[5]:
                return 'declared_maximum_full_dictionary_no_resolvable_step_actual_new_input_exhausted'
            previous = self.completed
            step = (mu-previous[5])/2
            self.current = previous
            # The last completed field is an actual starting value, not a
            # fabricated saved Jacobian/predictor. The new intermediate
            # input is then fully solved with fresh paid J computations.
            next_mu = previous[5]+step
            next_input = self.build_input(next_mu, model.J)
            self.make_current(next_mu, next_input, previous[0], previous[1])

    def complete_readout(self):
        if self.current is None:
            return None
        self.check()
        model, q, current_data, current_state, core_input, mu, current_is_fine = self.current
        ntheta = 512
        while ntheta <= 4*model.J:
            ntheta *= 2
        if (current_is_fine and np.array_equal(current_data['r'], self.factory.fine_radii)
                and len(current_data['theta']) == ntheta
                and np.array_equal(current_state['q'], q)
                and current_state['design_model_sha256'] == model.design_model_sha256):
            data, state = current_data, current_state
            COUNTS['already_paid_complete_current_fine_states_reused'] += 1
            reused_current_fine = True
        else:
            data = model.prepare(self.factory.fine_radii, ntheta, grid_role='fine')
            state = model.evaluate(q, data)
            reused_current_fine = False
        self.readout = {'status': 'fine_geometry_completed_direct_position_pending',
            'mu_literal': str(mu), 'actual_q_sha256': sha(q.tolist()),
            'fine': self.modules['consumers'].complete_observation(model, q, data, state),
            'same_complete_current_fine_field_reused_without_duplicate_evaluation': reused_current_fine,
            'full_original_fine_and_all_positive_odd_modes_retained': True}
        emit('FINE', self.readout)
        coefficients = model.coefficient_fields(q, data, state)
        self.readout['coefficient_observation'] = {
            'all_post_modes': coefficients['all_post_modes'].tolist(),
            'maximum_abs_pre_tanh_threejet_coefficients': np.max(abs(coefficients['pre_tanh_threejet_coefficients']), axis=(0, 1)).tolist(),
            'maximum_abs_post_tanh_threejet_coefficients': np.max(abs(coefficients['all_post_tanh_threejet_coefficients']), axis=(0, 1)).tolist(),
            'all_2J_terms_combined_before_norms': True, 'source_or_continuous_error_bound': False}
        self.check()
        self.readout['actual_position_two_stencils'] = self.modules['consumers'].two_direct_position_stencils(model, q, data, state)
        self.readout['status'] = 'complete_fine_and_both_direct_position_stencils_completed'
        if mu == 1 and self.readout['fine']['eta_max_identity'] <= self.input['solver']['final_eta_target']:
            self.readout['selected_new_metric_definition'] = model.candidate_metric_definition(q,
                candidate_provenance={'source_commit': os.environ['GITHUB_SHA'],
                    'run_id': os.environ['GITHUB_RUN_ID'], 'mu_literal': str(mu),
                    'actual_q_sha256': sha(q.tolist()),
                    'numerical_candidate_only_continuous_and_global_errors_unresolved': True})
        emit('COMPLETE_READOUT', self.readout)
        return self.readout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-state-json', required=True)
    parser.add_argument('--source-state-sha256', required=True)
    parser.add_argument('--request-path', required=True)
    parser.add_argument('--maximum-seconds', type=float, default=18000.)
    parser.add_argument('--final-reserve-seconds', type=float, default=1800.)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('all new-radius scientific calculations require this public Actions scope')
    raw = sys.stdin.buffer.read() if args.source_state_json == '@stdin' else args.source_state_json.encode()
    if hashlib.sha256(raw).hexdigest() != args.source_state_sha256:
        raise ValueError('the actual new-radius input bytes differ')
    incoming = json.loads(raw)
    if incoming['schema'] != SCHEMA or not 0 < args.final_reserve_seconds < args.maximum_seconds <= 19800:
        raise ValueError('the complete declared new-radius input or scientific budget differs')
    modules = {key: load(key) for key in BINDINGS}
    started = time.monotonic()
    run = DesignRun(incoming, args, modules, started)
    emit('DEFINITION', {'schema': SCHEMA, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256': args.source_state_sha256, 'complete_scientific_input': incoming,
        'source_bound_components': BINDINGS, 'actual_initial_accepted_steps': 0,
        'automatic_path_target_mu': 1, 'private_hourly_rules_pull_owned_by_active_parent': True,
        'actual_public_pull_and_both_README_diffs_every_55_minutes': True,
        'all_old_1450_columns_plus_true_F2_free_column_retained_at_J48': True,
        'H_W_and_E_can_change_in_static_design_only': True,
        'old_fixed_E_old_accepted_q_or_R085_connection_values_used': False,
        'continuous_metric_global_reach_and_README_certificate': False,
        'arguments': {k: v for k, v in vars(args).items() if k != 'source_state_json'}})
    failure, status = None, 'new_radius_factory_not_yet_complete'
    try:
        status = run.execute()
    except SolverReserve as exc:
        status = 'declared_solver_reserve_actual_state_retained'
        failure = {'type': type(exc).__name__, 'message': str(exc)}
    except Exception as exc:
        status = 'actual_design_clock_rule_or_numerical_failure_retained'
        failure = {'type': type(exc).__name__, 'message': str(exc)}
        emit('FAILURE', failure)
    # No new numerical readout may run under changed instructions.
    if run.current is not None and (failure is None or failure['type'] != 'RuleChange'):
        try:
            run.complete_readout()
        except Exception as exc:
            run.failure_history.append({'attempt': 'complete_original_fine_and_direct_readout',
                'failure': type(exc).__name__+':'+str(exc), 'all_partial_work_retained': True})
    # The unchanged formula modules remain available even when the new
    # factory failed midway. Preserve their actual partial costs as well.
    driver = modules['factory']._driver()
    old_counts = {}
    for label in ('base', 'paid', 'complete', 'compact', 'full', 'high', 'parent', 'resume', 'position', 'majorant'):
        module = getattr(driver, label)
        old_counts[label] = {name: dict(getattr(module, name))
            for name in ('COUNTS', 'NEW', 'NEW_COUNTS') if hasattr(module, name)}
    source = json.loads(incoming['R_independent_paid_reconstruction_JSON'])
    final = {'schema': SCHEMA, 'status': status, 'failure': failure,
        'elapsed_seconds': time.monotonic()-started,
        'actual_current_checkpoint': run.current_record,
        'last_completed_finite_stage_checkpoint': run.completed_record,
        'pending_actual_trial_not_accepted': run.pending, 'last_actual_trial': run.last_trial,
        'actual_next_damping': run.damping, 'actual_accepted_Newton_steps': run.accepted_steps,
        'completed_finite_stages': run.history, 'failed_attempts_and_partial_readouts': run.failure_history,
        'complete_or_partial_final_readout': run.readout, 'last_actual_full_spectrum': run.last_spectrum,
        'actual_model_costs': None if run.current is None else run.current[0].cumulative_cost_receipt(),
        'factory_counts_including_incomplete_construction': dict(modules['factory'].COUNTS),
        'factory_attempts_including_incomplete_construction': list(modules['factory'].ATTEMPTS),
        'high_mode_reconstruction_attempts': driver.full.attempt_receipts(run.attempts),
        'original_module_costs_including_incomplete_construction': old_counts,
        'hard_trace_costs_including_incomplete_construction': dict(modules['model'].COUNTS),
        'core_lift_and_tail_costs_including_incomplete_construction': dict(modules['model'].formulas.COUNTS),
        'new_scope_counts': dict(COUNTS), 'complete_QR_SVD_cost_counts': dict(modules['factor'].COUNTS),
        'canonical_path_counts': dict(modules['path'].path_formulas.COUNTS),
        'consumers_including_partial_work': dict(modules['consumers'].COUNTS),
        'rejections': dict(REJECTIONS), 'hourly_public_rule_pull_receipts': run.rules.receipts,
        'prior_R_independent_source_cost_ledger_not_counted_as_new': source['source_cost_ledger'],
        'prior_cost_ledgers_not_counted_as_new': source['prior_cost_ledgers'],
        'overlapping_counts_are_not_disjoint_costs': True,
        'same_continuous_target_used_for_mu_J_and_N_refinement': True,
        'finite_P_projection_does_not_consume_R631_support_budgets_without_error': True,
        'static_design_is_not_a_final_fixed_g_isometric_motion': True,
        'source_ODE_tail_mean_primitive_roundoff_global_geometry_errors_unresolved': True,
        'raw_array_artifacts_releases_or_git_writes': False,
        'continuous_metric_C2_embedding_reach_and_README_certified': False}
    literal = json.dumps(final, sort_keys=True, separators=(',', ':'), allow_nan=False)
    print('R631_DESIGN_FINAL '+literal, flush=True)
    emit('FINAL_IDENTITY', {'JSON_bytes': len(literal.encode()), 'sha256': hashlib.sha256(literal.encode()).hexdigest()})


if __name__ == '__main__':
    main()
