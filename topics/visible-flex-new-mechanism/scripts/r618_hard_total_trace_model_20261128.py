#!/usr/bin/env python3
"""Actual fixed-E height with prescribed TOTAL core trace and all free columns.

The external P is taken from an actual hard-tau1 accepted source unless an
explicit new trace input is supplied.  All old, compact and true-tail free
columns remain; both core traces are eliminated algebraically.  The first
input is evaluated by the unchanged source field itself.  No source or
numerical error becomes a certificate through this representation.
Scientific arithmetic runs only in this public repository's Actions.
"""
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import quad_vec

HERE = Path(__file__).resolve().parent
CENTERED_SHA = 'fe1d8a07343152bc981a94cd00c311b826fc283afa1c6b020e9b7de59c04bda3'
COUNTS = defaultdict(int)


def _load(name, filename, digest):
    path = HERE / filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('source-bound hard-trace component differs: ' + filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


centered = _load('r618_hard_total_trace_centered_source',
    'r618_fourier_centered_model_20261128.py', CENTERED_SHA)
height, chain = centered.height, centered.chain
JET_KEYS = height.JET_KEYS


def _sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def _readonly(value):
    result = np.asarray(value, dtype=float).copy()
    result.flags.writeable = False
    return result


def _copied_trace(trace):
    return {key: _readonly(value) if isinstance(value, np.ndarray) else value
            for key, value in trace.items()}


def _separable_block(radial, coefficients, modes, theta):
    """All six spatial jets for a matrix of cosine coefficients."""
    co, si = np.cos(modes[:, None] * theta), np.sin(modes[:, None] * theta)
    a = co.T @ coefficients
    at = -si.T @ (modes[:, None] * coefficients)
    att = -co.T @ (modes[:, None] ** 2 * coefficients)
    v, vr, vrr = radial.T
    values = (v[:, None, None] * a, vr[:, None, None] * a,
        vrr[:, None, None] * a, v[:, None, None] * at,
        v[:, None, None] * att, vr[:, None, None] * at)
    return dict(zip(JET_KEYS, values))


class HardTotalTraceHeight:
    """Composition with an unchanged centered source; not an old-class alias."""
    @staticmethod
    def policy_descriptor():
        return {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'unchanged_centered_source_sha256': CENTERED_SHA,
            'height_definition': 'f_seed+L_dx+A*(P-P_seed-B0_dx)+B*(T(P)-T(P_seed)-B1_dx)',
            'total_P0_prescribed': True, 'total_P1_equals_full_T_of_P': True,
            'all_old_compact_and_true_tail_free_columns_retained': True,
            'A_lift_contains_all_modes_including_j2': True,
            'first_seed_function_and_six_jets_reused_exactly': True,
            'free_direction': 'L_dx-A*B0_dx-B*B1_dx',
            'external_trace_direction': 'A*Pdot+B*DT(P)*Pdot',
            'literal_zero_free_vector_is_not_the_frozen_reference': True,
            'fixed_target_mean_roots_and_full_position_rows_retained': True,
            'tail_anchor_transfer_requires_exact_support_identity': True,
            'core_and_whole_surface_error_certification': False}

    @classmethod
    def restore_from_frozen_reference(cls, original_driver, actual_q_json, amplitude,
            frozen_identity, maximum_independent_mode, policy, *, deadline, attempts,
            accepted_seed_response, accepted_source, prescribed_pc=None,
            trace_input_provenance=None):
        chain.public_only()
        if policy.get('hard_total_trace_adapter') != cls.policy_descriptor():
            raise ValueError('hard-trace source policy must precede source restoration')
        owned = centered.FourierCenteredHeight.restore_from_frozen_reference(
            original_driver, actual_q_json, amplitude, frozen_identity,
            maximum_independent_mode, policy, deadline=deadline, attempts=attempts)
        return cls(owned, accepted_seed_response, accepted_source,
            prescribed_pc=prescribed_pc, trace_input_provenance=trace_input_provenance)

    def __init__(self, owned, accepted_seed_response, accepted_source, *,
            prescribed_pc=None, trace_input_provenance=None):
        chain.public_only()
        if type(owned) is not centered.FourierCenteredHeight:
            raise TypeError('the actual complete centered model is required')
        owned.guard()
        if owned.policy.get('hard_total_trace_adapter') != self.policy_descriptor():
            raise ValueError('hard-trace definition must be in the original restoration policy')
        seed = owned._check_response(accepted_seed_response).copy()
        if seed[owned.tau_index] != 1.:
            raise ValueError('an actual accepted hard-tau1 source is required')
        source = json.loads(json.dumps(accepted_source, allow_nan=False))
        if (not isinstance(source, dict) or source.get('target_sha256') != owned.identity.target_sha256
                or source.get('accepted_response_sha256') != _sha(seed.tolist())):
            raise ValueError('literal accepted source response and unchanged target are required')
        for key in ('source_commit', 'run_id', 'job_id', 'final_json_sha256', 'response_model_sha256'):
            if not source.get(key):
                raise ValueError('actual accepted source provenance is missing: ' + key)
        self.owned, self.original = owned, owned.original
        self.split_chain = owned.split_chain
        self.nq = int(owned.core_start)
        self.seed_response = _readonly(seed)
        self.seed_x = _readonly(seed[:self.nq])
        self.accepted_source = source
        self.seed_trace = _copied_trace(owned.core_trace(seed))
        self.seed_pc = _readonly(self.seed_trace['pc'])
        B0, B1, dtau = owned._core_linear_directions(np.arange(self.nq))
        if np.any(dtau):
            raise ValueError('free dictionary unexpectedly contains tau')
        self.B0, self.B1 = _readonly(B0), _readonly(B1)
        self.seed_lift_coefficients = np.zeros(len(self.modes))
        for column, mode in enumerate(self.core_free_modes):
            self.seed_lift_coefficients[mode // 2 - 1] = self.amplitude * seed[self.core_start + column]
        self.seed_lift_coefficients = _readonly(self.seed_lift_coefficients)
        pc = self.seed_pc if prescribed_pc is None else np.asarray(prescribed_pc, dtype=float)
        if pc.shape != self.seed_pc.shape or not np.all(np.isfinite(pc)):
            raise ValueError('all finite independent total-trace coefficients are required')
        self.prescribed_pc = _readonly(pc)
        self.same_seed_trace = bool(np.array_equal(self.prescribed_pc, self.seed_pc))
        if self.same_seed_trace:
            target = self.seed_trace
            provenance = {'kind': 'actual_accepted_source_total_trace',
                'accepted_response_sha256': source['accepted_response_sha256'],
                'external_trace_change': False}
        else:
            if not isinstance(trace_input_provenance, dict) or not trace_input_provenance:
                raise ValueError('a changed external trace needs its actual mathematical input provenance')
            target = self.original._core_target(self.prescribed_pc)
            provenance = dict(trace_input_provenance)
        self.trace_input_provenance = provenance
        self.target_trace = _copied_trace(target)
        self._core_geometry = self._prescribed_core_geometry()
        self.definition = {'adapter': self.policy_descriptor(),
            'same_frozen_target_sha256': self.identity.target_sha256,
            'owned_centered_response_model_sha256': owned.response_model_sha256,
            'accepted_source': source, 'accepted_seed_x_sha256': _sha(self.seed_x.tolist()),
            'seed_total_P0': self.seed_pc.tolist(), 'prescribed_total_P0': self.prescribed_pc.tolist(),
            'trace_input_provenance': provenance, 'free_parameter_count': self.nq,
            'B0_sha256': _sha(self.B0.tolist()), 'B1_sha256': _sha(self.B1.tolist())}
        self.response_model_sha256 = _sha(self.definition)
        self._owned_model_sha256 = owned.response_model_sha256
        self._definition_sha256 = _sha(self.definition)
        self.cache = {}
        self.last_trace_key, self.last_trace = None, None
        COUNTS['actual_prescribed_total_trace_models'] += 1

    def __getattr__(self, name):
        return getattr(self.owned, name)

    def guard(self):
        base = self.owned.guard()
        if (type(self) is not HardTotalTraceHeight or self.original is not self.owned.original
                or self.owned.response_model_sha256 != self._owned_model_sha256
                or self.definition['adapter'] != self.policy_descriptor()
                or _sha(self.definition) != self._definition_sha256
                or self.response_model_sha256 != self._definition_sha256
                or not np.array_equal(self.prescribed_pc, self.definition['prescribed_total_P0'])
                or _sha(self.seed_response.tolist()) != self.accepted_source['accepted_response_sha256']
                or _sha(self.B0.tolist()) != self.definition['B0_sha256']
                or _sha(self.B1.tolist()) != self.definition['B1_sha256']):
            raise ValueError('actual hard-trace field inputs changed')
        return {'response_model_sha256': self.response_model_sha256,
            'hard_total_trace_definition': self.definition,
            'owned_centered_provenance': base,
            'original_classes_or_loaded_functions_patched': False}

    def _check_response(self, response):
        value = np.asarray(response, dtype=float)
        if value.shape != (self.nq,) or not np.all(np.isfinite(value)):
            raise ValueError('all finite old/compact/true-tail free parameters are required')
        self.driver.check(self.deadline)
        return value

    def initial_response(self):
        return self.seed_x.copy()

    def _field_identity(self, response, data, *, include_angles=True):
        return height.GrowingPostFixedMetricHeight._field_identity(
            self, self._check_response(response), data, include_angles=include_angles)

    def _require_same_state(self, response, data, state):
        return height.GrowingPostFixedMetricHeight._require_same_state(self, response, data, state)

    def prepare(self, r, ntheta):
        self.guard()
        key = (np.asarray(r, dtype=float).tobytes(), int(ntheta))
        if key not in self.cache:
            source = self.owned.prepare(r, ntheta)
            data = dict(source)
            data['fixed_mean_data'] = dict(source['fixed_mean_data'])
            data['response_model_sha256'] = self.response_model_sha256
            data['owned_radial_dictionary_model_sha256'] = self.owned.response_model_sha256
            self.cache[key] = data
        return self.cache[key]

    def original_data_view(self, data):
        """Explicit original-basis view for the equal inner-tail function only."""
        result = dict(data)
        result['response_model_sha256'] = self.owned.response_model_sha256
        return result

    def _prescribed_core_geometry(self):
        if self.same_seed_trace:
            return _copied_trace(self.seed_trace)
        target = self.target_trace
        P1_coeff = target['target']
        P1 = P1_coeff @ self.core_all_cos
        u, Ptt, Pt = [target[key] for key in ('u', 'Ptt', 'Pt')]
        er = -2 * (np.mean(P1 / u ** 3)
            + np.mean(Ptt / u) / (self.par.R * (1 + self.par.alpha))) / np.mean(u ** -3)
        c = self.par.alpha / (1 + self.par.alpha)
        D = -self.par.R * P1 + c * u * u * Ptt - Pt * Pt - self.par.R * er / 2
        return {**target, 'tau': 1., 'P1_coeff': P1_coeff, 'P1': P1,
            'zeta': (target['e'] - self.frozen_core_e) / 2,
            'zeta_r': (er - self.frozen_core_er) / 2, 'effective_e_r': float(er), 'D': D,
            'fixed_e': self.frozen_core_e, 'fixed_e_r': self.frozen_core_er,
            'full_tau_core_identity_difference_observation': float(np.max(abs(D))),
            'complete_core_D_observation': float(np.max(abs(D))),
            'original_j2_core_amplitude_unchanged': bool(self.prescribed_pc[0] == self.pc_reference[0]),
            'tau_equals_one_target_core_map_selected': True,
            'all_2J_dependent_modes_in_actual_height': True}

    def core_trace(self, response):
        response = self._check_response(response)
        key = response.tobytes()
        if key == self.last_trace_key:
            return self.last_trace
        dx = response - self.seed_x
        dP = self.prescribed_pc - self.seed_pc
        dT = self.target_trace['target'] - self.seed_trace['target']
        result = dict(self._core_geometry)
        result.update(correction_delta=self.seed_trace['correction_delta'] + dT - self.B1 @ dx,
            lift_coefficients=self.seed_lift_coefficients + dP - self.B0 @ dx,
            prescribed_total_trace=True, independent_total_trace_coefficients=self.prescribed_pc.copy(),
            complete_free_parameter_count=self.nq,
            total_trace_does_not_change_with_free_response=True)
        self.last_trace_key, self.last_trace = key, result
        COUNTS['actual_hard_trace_affine_trace_assemblies'] += 1
        return result

    def core_direction(self, trace, indices):
        indices = np.asarray(indices, dtype=int)
        if indices.ndim != 1 or np.any(indices < 0) or np.any(indices >= self.nq):
            raise ValueError('actual complete free column indices required')
        n = len(indices)
        zero = np.zeros((len(self.core_theta), n))
        return {'correction_delta': -self.B1[:, indices],
            'lift_coefficients': -self.B0[:, indices],
            'P': zero.copy(), 'Pt': zero.copy(), 'Ptt': zero.copy(), 'P1': zero.copy(),
            'e': np.zeros(n), 'zeta': np.zeros(n), 'zeta_r': np.zeros(n),
            'effective_e_r': np.zeros(n), 'D': zero.copy(),
            'fixed_e': np.zeros(n), 'fixed_e_r': np.zeros(n),
            'total_trace_fixed_by_exact_elimination': True,
            'all_tau_and_implicit_core_root_terms_retained': True}

    def _bare_increment(self, direction, data):
        direction = self._check_response(direction)
        plain = self.old.delta_jets(np.r_[0., direction[:self.old_count]], self.amplitude, data)
        answer = {key: value.copy() for key, value in zip(JET_KEYS, plain)}
        for start, count, modes, radial in (
                (self.compact_start, self.compact_count, self.extra_compact_modes, data['compact_radial_dictionary']),
                (self.tail_start, self.tail_count, self.modes, data['analytic_tail_columns'])):
            if not count:
                continue
            coefficients = self.amplitude * direction[start:start + count].reshape(len(modes), radial.shape[1])
            fields = np.einsum('rbk,jb->rjk', radial, coefficients)
            co, si = np.cos(modes[:, None] * data['theta']), np.sin(modes[:, None] * data['theta'])
            extra = (fields[:, :, 0] @ co, fields[:, :, 1] @ co, fields[:, :, 2] @ co,
                -(fields[:, :, 0] * modes) @ si, -(fields[:, :, 0] * modes * modes) @ co,
                -(fields[:, :, 1] * modes) @ si)
            for name, value in zip(JET_KEYS, extra):
                answer[name] += value
        return answer

    def height_jets(self, response, data, trace=None):
        response = self._check_response(response)
        if trace is None:
            trace = self.core_trace(response)
        seed = self.owned.height_jets(self.seed_response, data, self.seed_trace)
        dx = response - self.seed_x
        if self.same_seed_trace and np.all(dx == 0):
            COUNTS['literal_accepted_seed_six_jets_reused'] += 1
            return seed
        answer = self._bare_increment(dx, data)
        dP = self.prescribed_pc - self.seed_pc - self.B0 @ dx
        dT = self.target_trace['target'] - self.seed_trace['target'] - self.B1 @ dx
        A = height._separable(data['new_core_lift'], dP, self.modes, data['theta'])
        B = height._separable(data['core_radial'], dT, self.core_modes, data['theta'])
        for name in JET_KEYS:
            answer[name] += seed[name] + A[name] + B[name]
        COUNTS['actual_hard_trace_six_jet_points'] += int(answer['f'].size)
        return answer

    def height_direction(self, trace, indices, data, core_block=None):
        indices = np.asarray(indices, dtype=int)
        core = self.core_direction(trace, indices) if core_block is None else core_block
        answer, _ = self.original.height_direction(trace, indices, data,
            {'correction_delta': core['correction_delta']})
        lift = _separable_block(data['new_core_lift'], core['lift_coefficients'], self.modes, data['theta'])
        for name in JET_KEYS:
            answer[name] += lift[name]
        COUNTS['actual_hard_trace_direction_columns_at_radii'] += len(data['r']) * len(indices)
        return answer, core

    def combined_height_direction(self, direction, data):
        direction = self._check_response(direction)
        answer = self._bare_increment(direction, data)
        A = height._separable(data['new_core_lift'], -(self.B0 @ direction), self.modes, data['theta'])
        B = height._separable(data['core_radial'], -(self.B1 @ direction), self.core_modes, data['theta'])
        for name in JET_KEYS:
            answer[name] += A[name] + B[name]
        return answer

    def external_trace_direction(self, pc_direction, data):
        pc_direction = np.asarray(pc_direction, dtype=float)
        if pc_direction.shape != self.prescribed_pc.shape or not np.all(np.isfinite(pc_direction)):
            raise ValueError('all independent external trace directions are required')
        A = height._separable(data['new_core_lift'], pc_direction, self.modes, data['theta'])
        dT = self.target_trace['target_jac_pc'] @ pc_direction
        B = height._separable(data['core_radial'], dT, self.core_modes, data['theta'])
        return {name: A[name] + B[name] for name in JET_KEYS}

    def external_core_direction(self, pc_direction):
        """Full same-root core derivative for an external P-path direction."""
        direction = np.asarray(pc_direction, dtype=float)
        if direction.shape != self.prescribed_pc.shape or not np.all(np.isfinite(direction)):
            raise ValueError('all independent external trace directions are required')
        trace = self._core_geometry
        dP = direction @ self.core_cos
        dPt = -(direction * self.modes) @ self.core_sin
        dPtt = -(direction * self.modes ** 2) @ self.core_cos
        de = float(self.target_trace['de_pc'] @ direction)
        dT = self.target_trace['target_jac_pc'] @ direction
        dP1 = dT @ self.core_all_cos
        u, P1, Ptt = [trace[name] for name in ('u', 'P1', 'Ptt')]
        du = (de + 2 * dP) / (2 * u)
        den = np.mean(u ** -3)
        dden = np.mean(-3 * du / u ** 4)
        dnum = (np.mean(dP1 / u ** 3 - 3 * P1 * du / u ** 4)
            + np.mean(dPtt / u - Ptt * du / u ** 2) / (self.par.R * (1 + self.par.alpha)))
        der = -2 * dnum / den - trace['effective_e_r'] * dden / den
        c = self.par.alpha / (1 + self.par.alpha)
        dD = (-self.par.R * dP1 + c * ((de + 2 * dP) * Ptt + u * u * dPtt)
            - 2 * trace['Pt'] * dPt - self.par.R * der / 2)
        return {'P': dP, 'Pt': dPt, 'Ptt': dPtt, 'P1': dP1,
            'e': de, 'zeta': de / 2, 'effective_e_r': float(der), 'zeta_r': float(der / 2),
            'D': dD, 'correction_delta': dT, 'lift_coefficients': direction.copy(),
            'same_implicit_core_root_and_all_2J_terms': True}

    def external_field_direction(self, response, data, state, pc_direction):
        """Complete implicit-mean and position derivative on every actual row."""
        self._require_same_state(response, data, state)
        mean_jets = self.external_trace_direction(pc_direction, data['fixed_mean_data'])
        output_jets = self.external_trace_direction(pc_direction, data)
        co, si = data['complete_position_projection']
        projected = np.empty((len(data['r']), 2, len(data['all_position_odd_modes'])))
        mean_s, mean_sr = np.empty(len(data['r'])), np.empty(len(data['r']))
        position_directions = []
        for radial_index in range(len(data['r'])):
            self.driver.check(self.deadline)
            dm = self.split_chain.mean_direction(state['mean_states'][radial_index],
                {name: value[radial_index, :, None] for name, value in mean_jets.items()})
            ds = self.split_chain.output_direction(state['output_states'][radial_index],
                {name: value[radial_index, :, None] for name, value in output_jets.items()}, dm)
            dS = chain.position_direction(state['output_states'][radial_index],
                state['positions'][radial_index], ds)
            projected[radial_index, 0] = (co @ dS[:, 0, :])[:, 0]
            projected[radial_index, 1] = (si @ dS[:, 1, :])[:, 0]
            mean_s[radial_index], mean_sr[radial_index] = dm['s'][0], dm['s_r'][0]
            position_directions.append(dS[:, :, 0])
        residual = (projected * data['position_radial_units'][:, None, None] / self.amplitude).ravel()
        COUNTS['complete_external_trace_field_directions'] += 1
        return {'height_jets': output_jets, 'mean_height_jets': mean_jets,
            'mean_s': mean_s, 'mean_s_r': mean_sr, 'position_S_direction': position_directions,
            'residual_direction': residual, 'core': self.external_core_direction(pc_direction),
            'all_original_position_rows_retained': True, 'same_fixed_reference_E': True,
            'continuous_error_certified': False}

    def _target(self, data, index):
        return self.owned._target(data, index)

    def _mean_state(self, target, jets, seed=0., literal_zero=False):
        # The free vector zero is a genuine hard-P field, not reference tau0.
        return self.owned._mean_state(target, jets, seed=seed, literal_zero=False)

    def evaluate(self, response, data, accepted_mean_seed=None):
        return centered.FourierCenteredHeight.evaluate(self, response, data, accepted_mean_seed)

    def jacobian(self, response, data, state, block_columns=16):
        return centered.FourierCenteredHeight.jacobian(self, response, data, state, block_columns)

    def _mean_point_query(self, response, r, trace, indices):
        return centered.FourierCenteredHeight._mean_point_query(self, response, r, trace, indices)

    def geometry_with_mean_height(self, response, data, state, mean_height):
        return height.GrowingPostFixedMetricHeight.geometry_with_mean_height(self, response, data, state, mean_height)

    def coefficient_fields(self, response, data, state=None):
        self.guard()
        response = self._check_response(response)
        identity = self._field_identity(response, data)
        if state is not None:
            self._require_same_state(response, data, state)
        source = self.original.coefficient_fields(self.seed_response, self.original_data_view(data))
        dx = response - self.seed_x
        fields = source['all_post_tanh_threejet_coefficients'].copy()
        for column, mode in enumerate(self.old.column_modes):
            fields[:, mode // 2 - 1, :] += self.amplitude * dx[column] * data['new_columns'][:, column, :]
        for start, count, modes, radial in (
                (self.compact_start, self.compact_count, self.extra_compact_modes, data['compact_radial_dictionary']),
                (self.tail_start, self.tail_count, self.modes, data['analytic_tail_columns'])):
            if count:
                coefficients = self.amplitude * dx[start:start + count].reshape(len(modes), radial.shape[1])
                part = np.einsum('rbk,jb->rjk', radial, coefficients)
                for column, mode in enumerate(modes):
                    fields[:, mode // 2 - 1, :] += part[:, column, :]
        dP = self.prescribed_pc - self.seed_pc - self.B0 @ dx
        dT = self.target_trace['target'] - self.seed_trace['target'] - self.B1 @ dx
        for column, mode in enumerate(self.modes):
            fields[:, mode // 2 - 1, :] += dP[column] * data['new_core_lift']
        fields += data['core_radial'][:, None, :] * dT[None, :, None]
        result = {**source, **identity, 'all_post_tanh_threejet_coefficients': fields,
            'actual_hard_total_trace_definition': self.definition,
            'seed_relative_complete_coefficient_assembly': True}
        if state is not None:
            W, Wr = data['frozen_W'], data['frozen_Wr']
            s = np.asarray([value['s'] for value in state['mean_states']])
            sr = np.asarray([value['s_r'] for value in state['mean_states']])
            e = np.asarray([value['target']['e'] for value in state['mean_states']])
            er = np.asarray([value['target']['e_r'] for value in state['mean_states']])
            result.update(effective_mean_W=W-s, effective_mean_Wr=Wr-sr,
                effective_split_e=e+2*W*s-s*s,
                effective_split_er=er+2*Wr*s+2*(W-s)*sr,
                effective_split_formed_without_E_minus_large_W_squared=True)
        return result

    def inner_equivalent_response(self, response):
        """This original response has exactly the SAME height on the true tail.

        Outside the common zero-support interval it is generally different.
        It is used only by the unchanged cap-to-mouth interval producer.
        """
        response = self._check_response(response)
        result = self.seed_response.copy()
        result[:self.nq] = response
        return result

    def tail_support_identity(self, response, data, parameter_indices):
        response = self._check_response(response)
        mouth = float(data['r'][0])
        support = min(float(self.driver.complete.CORE_LEFT), float(self.core_lift_left))
        if not self.base.RC < mouth < support:
            raise ValueError('tail is not entirely below both exact core-cutoff supports')
        indices = [int(index) for index in parameter_indices]
        if len(set(indices)) != len(indices) or any(index < 0 or index >= self.nq for index in indices):
            raise ValueError('distinct actual free columns are required')
        return {'lemma': 'A=B=0 with all six jets on cap_to_mouth; Lx and frozen reference identical',
            'interval': [float(self.base.RC), mouth], 'core_support_left': support,
            'hard_trace_field_identity': self._field_identity(response, data, include_angles=False),
            'original_inner_equivalent_response_sha256': _sha(self.inner_equivalent_response(response).tolist()),
            'same_reference_E_and_branch': True, 'parameter_indices': indices,
            'all_free_direction_tail_jets_identical': True,
            'outside_this_interval_fields_claimed_identical': False,
            'original_source_errors_remain_unresolved_if_unresolved': True}

    def cumulative_cost_receipt(self):
        result = self.owned.cumulative_cost_receipt()
        result['hard_total_trace_provenance'] = self.guard()
        result['hard_total_trace_counts'] = dict(COUNTS)
        result['all_original_and_failed_scope_costs_retained'] = True
        return result

    def integrate_mean_height(self,response,data,tail_anchor,indices=()):
        """Actual Z mean and optional parameter derivative, anchored at rc.

        The mathematical function is h-h_ref=integral_rc^r s(t)dt. The
        unchanged finite-DtN evaluator does not evaluate below its mouth,
        so its true cap-to-first-node integral/error must be supplied with
        explicit provenance. There is NO default zero continuation. The zero free vector is not the reference tau0 field; every response
        therefore requires its actual tail anchor.

        scipy's reported quadrature errors are retained as observations,
        never silently upgraded to rigorous enclosures. Endpoint values
        also return the common translation of the central column and the
        reflection center needed to keep the chosen inner held cap fixed.
        """
        chain.public_only()
        response = self._check_response(response)
        indices = np.asarray(indices,dtype=int)
        if (indices.ndim != 1 or np.any(indices < 0) or np.any(indices >= self.nq)
                or len(set(indices.tolist())) != len(indices)):
            raise ValueError('distinct actual parameter directions required')
        field_identity = self._field_identity(response,data,include_angles=False)
        response_sha = field_identity['response_sha256']
        r = np.asarray(data['r'])
        if not isinstance(tail_anchor,dict):
            raise ValueError('actual true cap-to-first-node mean integral and provenance required')
        expected = {'target_sha256':self.identity.target_sha256,'response_sha256':response_sha,
            'response_model_sha256':self.response_model_sha256,
            'cap_radius':self.base.RC,'mouth_radius':float(r[0]),'parameter_indices':indices.tolist()}
        for key,value in expected.items():
            if tail_anchor.get(key) != value:
                raise ValueError('true mean-height tail anchor differs: '+key)
        if not tail_anchor.get('true_tail_evidence') or 'unresolved_errors' not in tail_anchor:
            raise ValueError('true infinite-tail provenance and unresolved errors cannot be omitted')
        start = np.asarray(tail_anchor['integral_and_directions'],dtype=float)
        error = np.asarray(tail_anchor['absolute_error_bounds_or_unresolved_radii'],dtype=float)
        if start.shape != (1+len(indices),) or error.shape != start.shape or np.any(error < 0):
            raise ValueError('complete mean and parameter tail integrals/errors required')
        trace = self.core_trace(response)
        values = np.empty((len(r),len(start)));values[0] = start
        cumulative = start.copy();quad_error = 0.
        endpoints = np.r_[r,self.par.R]
        for interval,(left,right) in enumerate(zip(endpoints[:-1],endpoints[1:])):
            self.driver.check(self.deadline)
            value,estimate = quad_vec(lambda t:self._mean_point_query(response,float(t),trace,indices),
                float(left),float(right),epsabs=float(self.policy['mean_height_epsabs']),
                epsrel=float(self.policy['mean_height_epsrel']),
                limit=int(self.policy['quadrature_limit']),norm='max')
            cumulative += value;quad_error += float(estimate)
            if interval+1 < len(r):
                values[interval+1] = cumulative
            COUNTS['new_mean_height_radial_integral_intervals'] += 1
        return {**field_identity,'mean_height_offset':values[:,0],
            'mean_height_parameter_directions':values[:,1:],
            'parameter_indices':indices.copy(),
            'central_column_translation_and_reflection_center_offset':float(cumulative[0]),
            'central_column_translation_parameter_directions':cumulative[1:],
            'tail_anchor_value_and_errors':tail_anchor,
            'quad_error_estimate_observation':quad_error,
            'mean_root_and_quadrature_errors_rigorously_enclosed':False,
            'same_frozen_target_sha256':self.identity.target_sha256,
            'physical_definition_is_true_cap_anchored_integral_not_finite_mouth_zero':True,
            'all_geometric_errors_certified':False}
