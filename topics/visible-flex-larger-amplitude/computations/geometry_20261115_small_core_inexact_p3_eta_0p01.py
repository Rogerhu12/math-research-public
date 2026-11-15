#!/usr/bin/env python3
"""Independent fixed-eta=0.01 inexact p3 restoration from actual97.

The complete mathematical functions are retained byte-for-byte from the
frozen ce93 producer. Its fixed-eta=0.1 entry is not executed or modified.
This distinct entry fixes eta=0.01 and binds the genuine actual97 parent
or a completed output of this exact new producer and its full closure.

This independent candidate strategy uses the unchanged original R259 three
unit equations and full parameter Jacobian. Its linear direction retains the
actual nonzero third residual through a normal p3 correction. Bounded scalar
restoration still seeks the original 1e-8 unit threshold, but its last finite
original point with a finite nonzero J33 may enter the original complete-three
merit/actual full-J slope/.2 Armijo test even when that threshold was not met.
Neither an approximate inner root nor an implicit-function curve is assumed.
The actual restoration displacement is recorded separately from alpha*v.
Original final unit/full112, FD, scalar Arb and zero-core circle diagnostics
remain unchanged, separate from original BVP/native acceptance.

Scientific operations run only in Rogerhu12/math-research-public Actions.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
ENTRY_NAME = 'geometry_20261115_small_core_inexact_p3_eta_0p01.py'
SCHEMA = 'R278-original-three-equation-inexact-p3-restoration-LM-eta0p01-v1'
ORIGINAL_NAME = 'geometry_20261114_small_core_resonance.py'
ORIGINAL_SHA256 = '3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5'
RESUME_NAME = 'geometry_20261115_small_core_damped_resume.py'
PREVIOUS_NAME = 'geometry_20261115_small_core_p3_inner_root_search.py'
BASELINE_NAME = 'geometry_20261115_small_core_inexact_p3_restoration.py'
BASELINE_SCHEMA = 'R278-original-three-equation-inexact-p3-restoration-LM-v1'
BASELINE_SHA256 = 'ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e'
ACTUAL97_STATUS_SHA256 = 'd55b5338880cabaae44bd7575db9a10bcba22fad4ae1fce0225f1ef38064f331'
ACTUAL97_STATUS_BYTES = 233256
FROZEN = {
    BASELINE_NAME: BASELINE_SHA256,
    PREVIOUS_NAME: '3b48efd71eb696fef66acbe7fbd163bb8dc8ca63287bfa8c4e873a2600fbf9d9',
    RESUME_NAME: 'ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a',
    'geometry_20261115_small_core_damped_search.py': '1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728',
    ORIGINAL_NAME: ORIGINAL_SHA256,
    'geometry_20261114_constrained_trust_warm.py': '5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2',
    'geometry_20261114_constrained_collocation.py': '70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8',
    'geometry_20261114_full_dn_augmented.py': 'f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e',
    'geometry_20261114_full_dn_boundary.py': '4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2',
    'geometry_20261114_physical_test_boundary.py': '3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681',
    'geometry_20261114_lifted_modes_profile.py': '13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5',
    'geometry_20261114_full_prefix_operator.py': 'a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703',
    'geometry_20261114_direct_operator_cell.py': '1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce',
}
ORIGINAL_INPUTS = {
    'accepted': 'b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff',
    'prepared': '0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714',
    'tail_anchor': 'e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51',
    'tail_config': '01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5',
}
STATUS_NAME = 'inexact-p3-restoration-status.json'


def file_sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b''):
            digest.update(chunk)
    return digest.hexdigest()


def clean(value):
    """Keep nonfinite diagnostic values explicit, including their original bits."""
    if isinstance(value, dict):
        return {str(key): clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(item) for item in value]
    if hasattr(value, 'tolist'):
        return clean(value.tolist())
    if isinstance(value, float) and not math.isfinite(value):
        return dict(nonfinite_class=('NaN' if math.isnan(value) else
            ('positive-infinity' if value > 0 else 'negative-infinity')),
            binary64_big_endian_hex=struct.pack('>d', value).hex())
    return value


def write_json(path, value):
    path = Path(path)
    raw = (json.dumps(clean(value), ensure_ascii=False, allow_nan=False,
                      sort_keys=True, indent=2)+'\n').encode()
    if path.suffix == '.gz':
        raw = gzip.compress(raw, mtime=0)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_bytes(raw)
    temporary.replace(path)


def descriptor(path, root):
    return dict(file=str(Path(path).relative_to(root)), bytes=Path(path).stat().st_size,
                sha256=file_sha(path))


def checked_sources():
    for name, digest in FROZEN.items():
        if file_sha(HERE/name) != digest:
            raise ValueError('Retain the frozen original source: '+name)
    return {**FROZEN, ENTRY_NAME: file_sha(__file__)}


def checked_parent(path, expected_sha256, sources):
    if (len(expected_sha256) != 64
            or any(c not in '0123456789abcdef' for c in expected_sha256)):
        raise ValueError('Declare the actual complete parent file SHA256')
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError('The supplied original parent bytes do not match the CLI digest')
    compressed = raw.startswith(b'\x1f\x8b')
    decoded = gzip.decompress(raw) if compressed else raw
    decoded_sha = hashlib.sha256(decoded).hexdigest()
    parent = json.loads(decoded)
    if (not isinstance(parent, dict) or parent.get('phase') != 'diagnostic-completed'
            or parent.get('diagnostic_completed') is not True or parent.get('success') is not False
            or parent.get('native_nonlinear_solver_called') is not False
            or parent.get('full_nonlinear_nonzero_lambda_solution_computed') is not False
            or parent.get('original_diagnostic_source_sha256') != ORIGINAL_SHA256
            or parent.get('input_sha256') != ORIGINAL_INPUTS):
        raise ValueError('The parent must be a completed original-equation candidate diagnostic')
    if parent.get('schema') == BASELINE_SCHEMA:
        if len(decoded) != ACTUAL97_STATUS_BYTES or decoded_sha != ACTUAL97_STATUS_SHA256:
            raise ValueError('The first parent is the complete genuine actual97 ce93 final status')
        expected_sources = FROZEN
        expected_producer = BASELINE_SHA256
        origin = 'actual97 completed ce93 eta0.1 final accepted candidate; new producer fixes eta0.01'
        if parent.get('last_accepted_point_semantics') != 'original-three-merit-accepted-candidate-or-fresh-parent':
            raise ValueError('The genuine actual97 parent retains its declared final-point semantics')
    elif parent.get('schema') == SCHEMA:
        expected_sources = sources
        expected_producer = sources[ENTRY_NAME]
        origin = 'completed output of this exact independent inexact-restoration producer'
        if parent.get('last_accepted_point_semantics') != 'original-three-merit-accepted-candidate-or-fresh-parent':
            raise ValueError('An own-schema parent must retain the declared final-point semantics')
    else:
        raise ValueError('Unsupported parent schema; no old result is relabelled')
    if (parent.get('source_sha256') != expected_producer
            or parent.get('consumed_source_sha256') != expected_sources):
        raise ValueError('Parent producer and full source closure must match exactly')
    parameters = parent.get('final', {}).get('parameters')
    if (not isinstance(parameters, list) or len(parameters) != 3
            or any(isinstance(v, bool) or not isinstance(v, (int, float))
                   or not math.isfinite(v) for v in parameters)):
        raise ValueError('Use all three finite literal final parameters of the real parent')
    receipt = dict(file='parent-status.json'+('.gz' if compressed else ''),
        bytes=len(raw), sha256=expected_sha256, decoded_bytes=len(decoded), decoded_sha256=decoded_sha,
        encoding='gzip-json' if compressed else 'json', schema=parent['schema'],
        producer_sha256=expected_producer, origin=origin, parameters_field='final.parameters',
        literal_parameters=parameters, parent_damping_cli_text=parent.get('damping_cli_text'),
        parent_damping_binary64=parent.get('damping_binary64'),
        only_literal_parameters_reused=True, saved_parent_J_merit_state_or_FD_reused=False,
        parent_is_not_a_native_nonzero_or_BVP_solution=True)
    return raw, parent, receipt


def original_module():
    path = HERE/ORIGINAL_NAME
    specification = importlib.util.spec_from_file_location('actual_R259_original_for_R278_inner_root', path)
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


def original_merit(np, state):
    residual = state['equation']
    if residual.shape != (3,) or not np.all(np.isfinite(residual)):
        raise FloatingPointError('All three original unit residuals must be finite')
    return .5*float(residual@residual)


def state_record(np, state):
    """Read returned arrays only; this does not evaluate the model again."""
    return dict(parameters=state['parameters'].tolist(), low_equations_used=state['equation'].tolist(),
        unit_diagonal_defects=state['unit_diagonal_defect'].tolist(),
        original_three_equation_merit=.5*float(state['equation']@state['equation']),
        complete_first_order_right_residual=state['full_right'].tolist(),
        full_first_order_native_height=state['native_first_order_height'].tolist(),
        original_real_domain_evaluation_returned=True,
        scalar_node_and_mid_minimum_radius=float(min(np.min(state['scalar_nodes'][:, 0]),
            np.min(state['scalar_middle'][:, 0]))),
        scalar_node_and_mid_maximum_absolute_returned_ap=float(max(np.max(abs(state['scalar_nodes'][:, 1])),
            np.max(abs(state['scalar_middle'][:, 1])))),
        source_circle_node_and_mid_minimum_radius=float(min(np.min(state['radius']), np.min(state['radius_mid']))),
        source_circle_node_and_mid_minimum_beta2=float(min(np.min(state['margin']), np.min(state['margin_mid']))),
        radius_cell_denominator_minimum_absolute=float(np.min(abs(state['radius_right']))),
        query_domain_is_not_an_interval_certificate=True, native_nonlinear_solve_performed=False)


class EvaluationTrace:
    """An observer of original calls, including their unmodified exceptions."""
    def __init__(self, output):
        self.output = Path(output)
        self.path = self.output/'large-arrays'/'original-model-evaluations.jsonl'
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = self.path.open('w', encoding='utf-8')
        self.label = 'setup'
        self.events = 0
        self.counts = dict(evaluation_attempts=0, real_evaluation_attempts=0,
            complex_evaluation_attempts=0, evaluation_returns=0, evaluation_exceptions=0,
            jacobian_attempts=0, jacobian_returns=0, description_attempts=0)
        self.observer_errors = []

    @contextmanager
    def context(self, label):
        previous = self.label
        self.label = label
        try:
            yield
        finally:
            self.label = previous

    def emit(self, event):
        self.events += 1
        event = dict(event_number=self.events, context=self.label,
                     this_event_does_not_accept_an_outer_candidate=True, **event)
        try:
            self.handle.write(json.dumps(clean(event), ensure_ascii=False, allow_nan=False,
                                         separators=(',', ':'))+'\n')
            self.handle.flush()
        except (OSError, ValueError) as error:
            self.observer_errors.append(dict(event_number=self.events, exception=repr(error)))

    def close(self):
        try:
            self.handle.close()
        except OSError as error:
            self.observer_errors.append(dict(context='close', exception=repr(error)))

    def report(self):
        result = dict(counts=dict(self.counts), events=self.events, observer_errors=self.observer_errors,
            original_model_methods_or_acceptance_returns_modified=False,
            all_evaluation_and_jacobian_events_requested=True,
            observer_is_not_an_acceptance_gate=True)
        if self.path.is_file():
            result['file'] = descriptor(self.path, self.output)
        return result


def observed_model_class(base, trace):
    np = base.np
    class ObservedCircleReference(base.CircleReference):
        def evaluate(self, parameters):
            values = np.asarray(parameters)
            real = bool(np.isrealobj(values))
            trace.counts['evaluation_attempts'] += 1
            trace.counts['real_evaluation_attempts' if real else 'complex_evaluation_attempts'] += 1
            index = trace.counts['evaluation_attempts']
            point = (dict(parameters=values.tolist()) if real else
                     dict(parameters_real=values.real.tolist(), parameters_imag=values.imag.tolist()))
            started = time.monotonic()
            try:
                answer = super().evaluate(parameters)
            except Exception as error:
                trace.counts['evaluation_exceptions'] += 1
                trace.emit(dict(kind='original_evaluate_exception', evaluation_index=index,
                    real_parameters=real, **point, exception=repr(error),
                    original_exception_class=type(error).__name__, seconds=time.monotonic()-started))
                raise
            trace.counts['evaluation_returns'] += 1
            if real:
                try:
                    payload = state_record(np, answer)
                except Exception as error:
                    # Observation must not change an original evaluate return.
                    payload = dict(observer_error=repr(error), original_evaluate_return_preserved=True)
                    trace.observer_errors.append(dict(evaluation_index=index, exception=repr(error)))
            else:
                payload = dict(equation_real=answer['equation'].real.tolist(),
                    equation_imag=answer['equation'].imag.tolist(),
                    original_complex_step_path=True,
                    original_real_domain_guard_is_not_applied_to_complex_probe=True)
            trace.emit(dict(kind='original_evaluate_return', evaluation_index=index,
                real_parameters=real, **point, returned=payload, seconds=time.monotonic()-started))
            return answer

        def jacobian(self, parameters):
            trace.counts['jacobian_attempts'] += 1
            index = trace.counts['jacobian_attempts']
            started = time.monotonic()
            try:
                answer = super().jacobian(parameters)
            except Exception as error:
                trace.emit(dict(kind='original_jacobian_exception', jacobian_index=index,
                    parameters=np.asarray(parameters).tolist(), exception=repr(error),
                    seconds=time.monotonic()-started))
                raise
            trace.counts['jacobian_returns'] += 1
            trace.emit(dict(kind='original_jacobian_return', jacobian_index=index,
                parameters=np.asarray(parameters).tolist(), original_full_three_by_three_jacobian=answer.tolist(),
                original_complex_step=1e-25, seconds=time.monotonic()-started))
            return answer

        def description(self, state):
            trace.counts['description_attempts'] += 1
            return super().description(state)
    return ObservedCircleReference


class P3RestorationSearch:
    def __init__(self, np, model, trace, output, tolerance, newton_steps, backtracks):
        self.np, self.model, self.trace = np, model, trace
        self.output, self.tolerance = Path(output), tolerance
        self.newton_steps, self.backtracks = newton_steps, backtracks
        self.calls = 0
        self.receipts = []

    def solve(self, seed_parameters, label, seed_state=None):
        """Finite scalar Newton probes, without changing either p1 or p2.

        Scalar probes still seek the original |d3| <= tolerance. A last finite
        real point with its actual finite full J and nonzero J33 is eligible for
        the outer merit test even when that inner target was not met. This does
        not call it a root, accept it, or modify any original residual/threshold.
        """
        np, model = self.np, self.model
        self.calls += 1
        index = self.calls
        parameters = np.asarray(seed_parameters, float).copy()
        fixed = parameters[:2].copy()
        start_counts = dict(self.trace.counts)
        started = time.monotonic()
        state = None
        derivative = None
        derivative_parameters = None
        report = dict(schema='R278-actual-inexact-p3-restoration-probes-v1', inner_call=index,
            label=label, seed_parameters=parameters.tolist(), fixed_first_two_parameters=fixed.tolist(),
            unit_third_residual_tolerance=self.tolerance, maximum_newton_updates=self.newton_steps,
            maximum_backtracks_per_update=self.backtracks,
            inner_acceptance='actual abs(original d3) strictly decreases; this is not outer acceptance',
            original_all_three_equations_saved=True,
            original_full_J_recomputed_for_every_inner_Newton_or_root_validation=True,
            intermediate_points_are_probes_only=True, exact_IFT_or_exact_root_claimed=False,
            original_third_residual_never_overwritten=True, steps=[], usable_inner_root=False,
            usable_restoration_point=False, inner_threshold_is_not_an_outer_eligibility_gate=True,
            residual_tolerance_met=False, original_full_J_finite=False,
            original_J33_finite_nonzero=False, accepted_outer_state=False)
        answer = dict(usable=False, state=None, derivative=None)
        reason = None
        try:
            with self.trace.context(label+'/seed'):
                if seed_state is None:
                    state = model.evaluate(parameters)
                else:
                    if not np.array_equal(seed_state['parameters'], parameters):
                        raise ValueError('A reused freshly evaluated seed must have the exact same parameters')
                    state = seed_state
            report['initial'] = state_record(np, state)
            report['seed_is_reused_fresh_state'] = seed_state is not None
            for iteration in range(self.newton_steps+1):
                residual = state['equation']
                original_merit(np, state)
                met = bool(abs(residual[2]) <= self.tolerance)
                report['residual_tolerance_met'] = met
                if iteration == self.newton_steps and not met:
                    reason = 'inner Newton update budget exhausted with the actual d3 still outside tolerance'
                    break
                with self.trace.context(label+'/inner-'+str(iteration)+'/original-full-J'):
                    derivative = model.jacobian(parameters)
                    derivative_parameters = parameters.copy()
                current = dict(iteration=iteration, point=state_record(np, state),
                    original_full_three_by_three_jacobian=derivative.tolist(),
                    original_J33=float(derivative[2, 2]), trials=[], inner_step_accepted=False)
                report['steps'].append(current)
                finite = bool(derivative.shape == (3, 3) and np.all(np.isfinite(derivative)))
                partial_ok = bool(np.isfinite(derivative[2, 2]) and derivative[2, 2] != 0)
                report['original_full_J_finite'] = finite
                report['original_J33_finite_nonzero'] = partial_ok
                current.update(original_full_J_finite=finite, original_J33_finite_nonzero=partial_ok)
                if not finite or not partial_ok:
                    reason = 'original full J is nonfinite or the original p3 partial J33 is zero'
                    current['stop_reason'] = reason
                    break
                if met:
                    report['usable_inner_root'] = True
                    reason = 'actual third unit residual meets tolerance with finite nonzero original J33'
                    answer.update(usable=True, state=state, derivative=derivative)
                    break
                step = -residual[2]/derivative[2, 2]
                current['p3_newton_direction'] = float(step)
                current['scalar_d3_squared_half_model_slope'] = float(residual[2]*(derivative[2, 2]*step))
                if not np.isfinite(step) or step == 0:
                    reason = 'p3 Newton direction is nonfinite or exactly zero before reaching tolerance'
                    current['stop_reason'] = reason
                    break
                before = float(abs(residual[2]))
                for trial in range(self.backtracks):
                    alpha = 2.**(-trial)
                    trial_parameters = parameters.copy()
                    trial_parameters[2] += alpha*step
                    item = dict(trial=trial, alpha=alpha, parameters=trial_parameters.tolist(),
                        inner_step_accepted=False, outer_candidate_accepted=False,
                        absolute_third_unit_residual_before=before)
                    current['trials'].append(item)
                    try:
                        with self.trace.context(label+'/inner-'+str(iteration)+'/trial-'+str(trial)):
                            trial_state = model.evaluate(trial_parameters)
                        item['point'] = state_record(np, trial_state)
                        original_merit(np, trial_state)
                        after = float(abs(trial_state['equation'][2]))
                        item['absolute_third_unit_residual_after'] = after
                        if after < before:
                            if not np.array_equal(trial_parameters[:2], fixed):
                                raise AssertionError('Inner Newton must not change either exterior coordinate')
                            parameters, state = trial_parameters, trial_state
                            item['inner_step_accepted'] = current['inner_step_accepted'] = True
                            break
                    except (FloatingPointError, np.linalg.LinAlgError) as error:
                        item['domain_or_cell_error'] = repr(error)
                if not current['inner_step_accepted']:
                    reason = 'all inner backtracks failed original domain or strict actual abs(d3) decrease'
                    break
        except (FloatingPointError, np.linalg.LinAlgError) as error:
            reason = 'inner seed or current original evaluation/J failed: '+repr(error)
            report['domain_or_cell_error'] = repr(error)
        finally:
            report['stop_reason'] = reason
            if state is not None:
                report['last_probe'] = state_record(np, state)
                report['residual_tolerance_met'] = bool(abs(state['equation'][2]) <= self.tolerance)
                try:
                    original_merit(np, state)
                    same_point_J = (derivative is not None and derivative_parameters is not None
                        and np.array_equal(derivative_parameters, state['parameters']))
                    if not same_point_J:
                        with self.trace.context(label+'/last-actual-point-original-full-J'):
                            derivative = model.jacobian(state['parameters'])
                        derivative_parameters = state['parameters'].copy()
                    finite = bool(derivative.shape == (3, 3) and np.all(np.isfinite(derivative)))
                    partial_ok = bool(finite and derivative[2, 2] != 0)
                    report.update(original_full_J_finite=finite,
                        original_J33_finite_nonzero=partial_ok,
                        final_original_full_three_by_three_jacobian=derivative.tolist(),
                        final_J_parameter_identity=derivative_parameters.tolist(),
                        original_final_J_reused_only_at_exact_same_fresh_point=same_point_J,
                        usable_restoration_point=bool(finite and partial_ok),
                        usable_inner_root=bool(finite and partial_ok and report['residual_tolerance_met']))
                    if finite and partial_ok:
                        answer.update(usable=True, state=state, derivative=derivative)
                    else:
                        answer.update(usable=False, state=None, derivative=None)
                except (FloatingPointError, np.linalg.LinAlgError) as error:
                    report['last_point_J_validation_error'] = repr(error)
                    report['usable_restoration_point'] = False
                    report['usable_inner_root'] = False
                    answer.update(usable=False, state=None, derivative=None)
            report['seconds'] = time.monotonic()-started
            report['original_call_cost'] = {key: value-start_counts[key] for key, value in self.trace.counts.items()}
            path = self.output/'inner-solves'/('inner-%04d.json.gz' % index)
            write_json(path, report)
            receipt = dict(**descriptor(path, self.output), label=label, inner_call=index,
                usable_inner_root=report['usable_inner_root'],
                usable_restoration_point=report['usable_restoration_point'],
                inner_threshold_is_not_an_outer_eligibility_gate=True,
                residual_tolerance_met=report['residual_tolerance_met'],
                original_full_J_finite=report['original_full_J_finite'],
                original_J33_finite_nonzero=report['original_J33_finite_nonzero'], stop_reason=reason,
                seconds=report['seconds'], original_call_cost=report['original_call_cost'],
                last_probe=report.get('last_probe'))
            self.receipts.append(receipt)
            answer['receipt'] = receipt
        return answer


def schur_damped_direction(np, derivative, residual, damping, tolerance):
    """Linear Schur elimination with the actual nonzero third residual retained."""
    if derivative.shape != (3, 3) or residual.shape != (3,):
        raise ValueError('Use the original complete three-equation parameter system')
    if not np.all(np.isfinite(derivative)) or not np.all(np.isfinite(residual)):
        raise FloatingPointError('The actual original small system is nonfinite')
    if derivative[2, 2] == 0:
        raise FloatingPointError('Linear elimination requires finite nonzero original J33')
    normal_p3 = -residual[2]/derivative[2, 2]
    p3_tangent = -derivative[2, :2]/derivative[2, 2]
    schur = derivative[:2, :2]+derivative[:2, 2:3]*p3_tangent[None, :]
    effective_residual = residual[:2]+derivative[:2, 2]*normal_p3
    column_norms = np.hypot.reduce(np.abs(schur), axis=0)
    zero_columns = column_norms == 0
    scale = np.where(zero_columns, 1., column_norms)
    scaled = schur/scale[None, :]
    augmented = np.vstack((scaled, damping*np.eye(2)))
    rhs = np.r_[-effective_residual, np.zeros(2)]
    if not (np.isfinite(normal_p3) and np.all(np.isfinite(effective_residual))
            and np.all(np.isfinite(p3_tangent)) and np.all(np.isfinite(augmented))
            and np.all(np.isfinite(scale))):
        raise FloatingPointError('The explicitly formed two-coordinate damped model is nonfinite')
    z, lstsq_residuals, rank, singular_values = np.linalg.lstsq(augmented, rhs, rcond=None)
    exterior = z/scale
    direction = np.r_[exterior, normal_p3+p3_tangent@exterior]
    action = derivative@direction
    if not np.all(np.isfinite(z)) or not np.all(np.isfinite(direction)) or not np.all(np.isfinite(action)):
        raise FloatingPointError('The actual lifted original-parameter direction is nonfinite')
    diagnostic = dict(schema='R278-full-residual-linear-Schur-restoration-LM-direction-v1',
        original_residual=residual.tolist(), original_full_three_by_three_jacobian=derivative.tolist(),
        actual_original_third_unit_residual=float(residual[2]), original_J33=float(derivative[2, 2]),
        normal_p3_correction=float(normal_p3),
        effective_first_two_residual_after_normal_correction=effective_residual.tolist(),
        actual_third_unit_threshold_met=bool(abs(residual[2]) <= tolerance),
        near_root_is_not_required_for_this_linear_elimination=True,
        p3_tangent_by_first_two_parameters=p3_tangent.tolist(), schur_matrix=schur.tolist(),
        schur_is_finite_linear_elimination_not_an_exact_IFT_derivative=True,
        column_norms=column_norms.tolist(), coordinate_scale=scale.tolist(),
        exactly_zero_columns=np.flatnonzero(zero_columns).tolist(),
        zero_column_scale_policy='Use one for an exactly zero column; keep both exterior coordinates',
        positive_damping=float(damping), scaled_schur_matrix=scaled.tolist(),
        augmented_matrix=augmented.tolist(), augmented_rhs=rhs.tolist(),
        augmented_lstsq_rank=int(rank), augmented_lstsq_singular_values=singular_values.tolist(),
        augmented_lstsq_returned_residuals=lstsq_residuals.tolist(), lstsq_rcond_argument=None,
        scaled_two_coordinate_direction=z.tolist(), first_two_parameter_direction=exterior.tolist(),
        lifted_original_three_parameter_direction=direction.tolist(),
        original_full_J_times_direction=action.tolist(),
        original_full_three_merit_model_slope=float(residual@action),
        original_full_Jd_third_component=float(action[2]),
        full_linear_residual_after_direction=(residual+action).tolist(),
        third_linear_residual_not_overwritten=float((residual+action)[2]),
        actual_third_residual_is_not_set_to_zero=True,
        damping_penalty_not_added_to_nonlinear_merit=True)
    try:
        left_vectors, local_singular_values, right_vectors_transposed = np.linalg.svd(scaled, full_matrices=False)
        projected_residual = left_vectors.T@effective_residual
        denominator = local_singular_values*local_singular_values+damping*damping
        removal = local_singular_values*local_singular_values/denominator
        retention = (damping*damping)/denominator
        diagnostic['same_model_spectrum'] = dict(
            completed=True, left_singular_vectors=left_vectors.tolist(),
            singular_values=local_singular_values.tolist(),
            right_singular_vectors_transposed=right_vectors_transposed.tolist(),
            effective_first_two_residual_projected_coordinates=projected_residual.tolist(),
            damping=float(damping), linear_residual_removal_fraction=removal.tolist(),
            linear_residual_retention_fraction=retention.tolist(),
            ideal_filtered_residual_coordinates=(retention*projected_residual).tolist(),
            spectrum_of='the actual scaled 2x2 linear Schur matrix with its normal-corrected residual',
            original_third_residual_retained_in_normal_correction=float(residual[2]),
            extra_nonlinear_candidate_or_new_acceptance_gate=False)
    except (FloatingPointError, np.linalg.LinAlgError) as error:
        diagnostic['same_model_spectrum'] = dict(completed=False, observer_error=repr(error),
            original_direction_and_original_merit_tests_preserved=True,
            extra_nonlinear_candidate_or_new_acceptance_gate=False)
    return direction, diagnostic


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('accepted', 'prepared', 'tail-anchor', 'tail-config', 'parent-status', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--parent-status-sha256', type=str, required=True)
    parser.add_argument('--damping', type=str, required=True)
    parser.add_argument('--candidate-steps', type=int, default=8)
    parser.add_argument('--backtracks', type=int, default=20)
    parser.add_argument('--inner-newton-steps', type=int, default=12)
    parser.add_argument('--inner-backtracks', type=int, default=20)
    parser.add_argument('--candidate-resonance-tolerance', type=float, default=1e-8)
    parser.add_argument('--interval-bits', type=int, default=160)
    parser.add_argument('--interval-depth', type=int, default=14)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError("All numerical work belongs to the public repository's own Actions")
    damping = float(args.damping)
    if not math.isfinite(damping) or damping != .01:
        raise ValueError('This independent producer declares the single positive outer damping 0.01')
    if (not 0 <= args.candidate_steps <= 8 or not 1 <= args.backtracks <= 20
            or not 1 <= args.inner_newton_steps <= 12 or not 1 <= args.inner_backtracks <= 20):
        raise ValueError('Keep the explicit 8/20 outer and 12/20 inner budget ceilings')
    if args.candidate_resonance_tolerance != 1e-8 or args.interval_bits != 160 or args.interval_depth != 14:
        raise ValueError('Retain the original unit threshold and final Arb budgets')
    if Path(__file__).name != ENTRY_NAME:
        raise ValueError('Retain this independent producer basename')
    sources = checked_sources()
    parent_raw, parent, parent_receipt = checked_parent(args.parent_status, args.parent_status_sha256, sources)
    for name, digest in ORIGINAL_INPUTS.items():
        if file_sha(getattr(args, name)) != digest:
            raise ValueError('Retain the complete original actual input: '+name)
    # No numerical package or mathematical source is imported before the Actions gate.
    base = original_module()
    np, original = base.np, base.original
    if base.EXPECTED != ORIGINAL_INPUTS:
        raise ValueError('The frozen original setup input dictionary must remain identical')
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError('Use a fresh independent inexact-p3-restoration output directory')
    (args.out/parent_receipt['file']).write_bytes(parent_raw)
    trace = EvaluationTrace(args.out)
    inner = None
    status = dict(schema=SCHEMA, scope=__doc__, phase='starting', source_sha256=sources[ENTRY_NAME],
        original_diagnostic_source_sha256=ORIGINAL_SHA256, consumed_source_sha256=sources,
        source_roles=dict(original_equations=ORIGINAL_NAME,
            immutable_parent_provenance_only=[BASELINE_NAME, PREVIOUS_NAME, RESUME_NAME, 'geometry_20261115_small_core_damped_search.py'],
            new_algorithm=ENTRY_NAME),
        algorithm_baseline_source_sha256=BASELINE_SHA256,
        mathematical_function_bodies_unchanged_from_baseline=True,
        baseline_producer_not_imported_or_executed=True,
        independent_fixed_damping_producer_not_an_unchanged_old_entry=True,
        input_sha256=ORIGINAL_INPUTS, parent_status=parent_receipt,
        parent_parameters_are_initial_guess_not_completed_field=True,
        initial_model_evaluation_and_description_are_fresh=True,
        parent_model_values_are_not_relabelled_as_current_values=True,
        candidate_algorithm='actual bounded p3 restoration and full-residual linear normal-plus-Schur LM directions',
        damping_cli_text=args.damping, damping_binary64=damping,
        candidate_iteration_budget=args.candidate_steps, original_backtrack_budget=args.backtracks,
        inner_newton_update_budget=args.inner_newton_steps, inner_backtrack_budget=args.inner_backtracks,
        original_armijo_coefficient=.2, candidate_resonance_tolerance=args.candidate_resonance_tolerance,
        scalar_interval_bits=args.interval_bits, scalar_interval_maximum_depth=args.interval_depth,
        initial_parent_not_projected_or_replaced_before_outer_search=True,
        inner_threshold_is_not_an_outer_eligibility_gate=True,
        all_inner_points_are_probes_not_outer_accepted_states=True,
        actual_third_unit_residual_never_overwritten=True,
        approximate_inner_root_is_not_an_exact_root_or_IFT_proof=True,
        original_equation_and_jacobian_functions_reused=True,
        unweighted_original_merit_and_domain_functions_reused=True,
        same_complete_original_scalar_formula_and_three_supports=True,
        design_parameters_are_varied_not_claimed_one_fixed_metric_during_search=True,
        complete_zero_slope_J_retained=True, low_modes_diagnosed=[1, 2, 3],
        native_nonlinear_solver_called=False, original_Gauss_app_used_as_a_derivative=False,
        original_full_BVP_or_large_amplitude_acceptance_claimed=False,
        straight_homotopy_only=True, weighted_lambda_j_homotopies_not_excluded=True,
        last_accepted_point_semantics='original-three-merit-accepted-candidate-or-fresh-parent',
        searches=[], success=False)
    start = time.monotonic()
    try:
        source, accepted, anchor = [original.read(path) for path in (args.prepared, args.accepted, args.tail_anchor)]
        profile, flow, boundary = base.setup(accepted, source, anchor, 4096, 1)
        true_J = np.asarray(anchor['heightJetJacobian']).reshape(3*flow.M+2, flow.M)[:flow.M]
        target = np.asarray(accepted['core']['coefficients'])[:3]
        model_class = observed_model_class(base, trace)
        model = model_class(profile, source['mesh'], true_J, target, boundary.eh, boundary.cut_scale)
        status.update(original_mesh_nodes=len(model.x), field_and_tail_modes=flow.M)
        parameters = np.asarray(parent['final']['parameters'], float)
        with trace.context('fresh-parent-state'):
            state = model.evaluate(parameters)
        with trace.context('fresh-parent-original-description-FD'):
            status['initial'] = model.description(state)
        status['initial_original_three_equation_merit'] = original_merit(np, state)
        status['phase'] = 'outer-candidate-search'
        write_json(args.out/STATUS_NAME, status)
        if not model.exactly_diagonal or np.any(target == 0):
            raise ValueError('This unit-equation search cannot discard true offdiagonal J or zero-target expansion')
        inner = P3RestorationSearch(np, model, trace, args.out, args.candidate_resonance_tolerance,
                                   args.inner_newton_steps, args.inner_backtracks)
        derivative = np.asarray(status['initial']['three_by_three_parameter_jacobian'])
        status['initial_J_source'] = 'fresh original initial description at exactly the fresh parent'
        status['initial_projection'] = dict(performed=False,
            reason='normal correction retains actual d3; no prior root or projection is required',
            fresh_original_parent_retained=True)
        for iteration in range(args.candidate_steps):
            residual = state['equation']
            if np.max(abs(residual)) <= args.candidate_resonance_tolerance:
                status['search_stop_reason'] = 'all original unit equations meet their original stopping tolerance'
                break
            before = original_merit(np, state)
            row = dict(iteration=iteration, parameters=parameters.tolist(), residual=residual.tolist(),
                actual_third_unit_residual=float(residual[2]), derivative=derivative.tolist(),
                derivative_source='full original J evaluated at exactly the actual current point, not a presumed root',
                merit_before=before, trials=[], accepted=False)
            status['searches'].append(row)
            try:
                direction, direction_report = schur_damped_direction(np, derivative, residual, damping,
                                                                     args.candidate_resonance_tolerance)
            except (FloatingPointError, np.linalg.LinAlgError) as error:
                row['direction_model_error'] = repr(error)
                status['search_stop_reason'] = 'the actual full-residual linear elimination direction model failed'
                break
            slope = float(residual@(derivative@direction))
            row.update(direction_model=direction_report, true_model_merit_slope=slope)
            if not np.isfinite(slope) or slope >= 0:
                row['reason'] = 'No finite strict descent of the actual complete three-equation merit'
                status['search_stop_reason'] = row['reason']
                break
            for trial in range(args.backtracks):
                alpha = 2.**(-trial)
                seed = parameters+alpha*direction
                trial_root = inner.solve(seed, 'outer-'+str(iteration)+'/trial-'+str(trial))
                item = dict(trial=trial, alpha=alpha, predicted_seed_parameters=seed.tolist(),
                    inner=trial_root['receipt'], accepted=False,
                    merit_before=before, original_Armijo_bound=before+.2*alpha*slope,
                    inner_threshold_is_not_an_outer_eligibility_gate=True,
                    finite_actual_restoration_point_and_own_full_J_required=True)
                row['trials'].append(item)
                if trial_root['usable']:
                    candidate = trial_root['state']
                    merit = original_merit(np, candidate)
                    item.update(actual_merit=merit, actual_projected_point=state_record(np, candidate),
                        full_merit_model_slope_used=slope,
                        true_third_unit_residual_preserved=float(candidate['equation'][2]),
                        actual_total_parameter_displacement=(candidate['parameters']-parameters).tolist(),
                        actual_restoration_displacement_from_seed=(candidate['parameters']-seed).tolist(),
                        original_seed_direction_not_relabelled_as_actual_restoration_displacement=True,
                        inner_unit_threshold_met=trial_root['receipt']['residual_tolerance_met'])
                    if np.isfinite(merit) and merit <= before+.2*alpha*slope:
                        parameters, state = candidate['parameters'].copy(), candidate
                        derivative = trial_root['derivative']
                        item['accepted'] = row['accepted'] = True
                        item['reason'] = 'actual restored candidate passes the original complete-three-merit Armijo test'
                    else:
                        item['reason'] = 'actual restored candidate fails the original complete-three-merit Armijo test'
                else:
                    item['reason'] = 'no finite actual restoration point with its finite nonzero original J33; probes not adopted'
                write_json(args.out/STATUS_NAME, status)
                if row['accepted']:
                    break
            if not row['accepted']:
                status['search_stop_reason'] = 'all original outer backtracks exhausted without an accepted complete-three-merit candidate'
                break
        else:
            status['search_stop_reason'] = 'explicit outer direction budget completed'
        status['phase'] = 'original-final-diagnostics'
        status['last_accepted_parameters'] = parameters.tolist()
        status['final_original_three_equation_merit'] = original_merit(np, state)
        with trace.context('final-original-description-FD'):
            status['final'] = model.description(state)
        specification = base.scalar_spec(profile, source['complete_scalar_profile']['complete_original_port'],
                                         parameters, ORIGINAL_INPUTS['accepted'])
        status['complete_scalar_domain'] = base.scalar_domain(profile, specification, args.out,
                                                               args.interval_bits, args.interval_depth)
        status['original_complete_circle_check'] = base.complete_reference_check(model, state, profile, flow,
            boundary, args.out, source, ORIGINAL_INPUTS['prepared'])
        small = bool(np.max(abs(state['full_right'])) <= args.candidate_resonance_tolerance)
        status.update(phase='diagnostic-completed', diagnostic_completed=True,
            low_mode_candidate_has_small_full_recorded_right_residual=small,
            original_unit_stopping_tolerance_met=bool(np.max(abs(state['equation'])) <= args.candidate_resonance_tolerance),
            this_candidate_threshold_is_not_an_original_BVP_acceptance_gate=True,
            full_nonlinear_nonzero_lambda_solution_computed=False,
            high_mode_nonresonance_or_interval_transversality_proved=False,
            exact_p3_elimination_or_implicit_function_theorem_proved=False,
            original_circle_reference_schema_retained=True)
        return 0
    except Exception as error:
        status.update(phase='exception', exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        trace.close()
        status['original_call_trace'] = trace.report()
        if inner is not None:
            status['inner_call_count'] = inner.calls
            status['inner_reports'] = inner.receipts
        status['seconds'] = time.monotonic()-start
        write_json(args.out/STATUS_NAME, status)


if __name__ == '__main__':
    raise SystemExit(main())
