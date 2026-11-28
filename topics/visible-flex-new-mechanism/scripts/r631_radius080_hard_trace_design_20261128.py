#!/usr/bin/env python3
"""R=.8 complete static design with prescribed TOTAL core and free H/W/E.

This is a new design model, not a continuation under the old target86da.
It keeps every new-factory old/compact column, adds the complete extra
compact and genuine rapid-flat tail dictionaries, and eliminates both core
traces.  H remains a free mean-height control.  The actual turning-derived
E and its full derivative change with static design.  A selected candidate
can later define its own fixed metric for refinement.
"""
from collections import defaultdict
from dataclasses import replace
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
FACTORY_SHA = 'b2ec6744c47992c08407652488d5a7bb593902b7adce15f610330d8925e7c8e5'
HEIGHT_FORMULAS_SHA = '87fdb14d80d12836c6328d3adf83abfc020300e468da43b3ebfffe4bdc6409e2'
COUNTS = defaultdict(int)
JET_KEYS = ('f', 'fr', 'frr', 'ft', 'ftt', 'frt')


def _load(name, filename, digest):
    path = HERE / filename
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise RuntimeError('source-bound new-radius component changed: '+filename)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


formulas = _load('r631_parameterized_R618_paper_formulas',
    'r618_growing_post_fixed_metric_height_20261127.py', HEIGHT_FORMULAS_SHA)


def _sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def _readonly(value):
    out = np.asarray(value, dtype=float).copy()
    out.flags.writeable = False
    return out


def _pad(value, size):
    out = np.zeros(size)
    if len(value) > size:
        raise ValueError('an original core mode would be lost')
    out[:len(value)] = value
    return out


def _separable_block(radial, coefficients, modes, theta):
    co, si = np.cos(modes[:, None]*theta), np.sin(modes[:, None]*theta)
    a = co.T@coefficients
    at = -si.T@(modes[:, None]*coefficients)
    att = -co.T@(modes[:, None]**2*coefficients)
    v, vr, vrr = radial.T
    return dict(zip(JET_KEYS, (v[:, None, None]*a, vr[:, None, None]*a,
        vrr[:, None, None]*a, v[:, None, None]*at, v[:, None, None]*att, vr[:, None, None]*at)))


def default_policy():
    return {'maximum_independent_mode': 48, 'core_points': 512,
        'root_steps': 80, 'root_tolerance': 1e-13,
        'core_lift_cutoff_left': .6, 'core_lift_cutoff_right': .78,
        'core_lift_epsabs': 1e-12, 'core_lift_epsrel': 2e-11, 'quadrature_limit': 96,
        'tail_degrees': [0, 1, 2, 3], 'tail_gaussian_denominator': 1.,
        'tail_cutoff_left': .30, 'tail_cutoff_right': .50}


class Radius080HardTraceDesign:
    def __init__(self, actual_factory, policy, *, prescribed_pc=None, trace_input_provenance=None):
        formulas.chain.public_only()
        module = sys.modules.get(type(actual_factory).__module__)
        path = HERE/'r631_radius080_design_factory_20261128.py'
        if (module is None or Path(module.__file__).resolve() != path.resolve()
                or type(actual_factory) is not module.Radius080Design
                or hashlib.sha256(path.read_bytes()).hexdigest() != FACTORY_SHA):
            raise ValueError('the actual reconstructed R=.8 factory object is required')
        self.factory = actual_factory
        self.factory_provenance = actual_factory.guard()
        self.driver, self.old = actual_factory.driver, actual_factory.field
        self.base, self.compact = self.driver.base, self.driver.compact
        self.par, self.args, self.deadline = self.old.par, self.old.args, self.old.deadline
        self.amplitude = actual_factory.amplitude
        self.policy = json.loads(json.dumps(policy, allow_nan=False))
        self.J = self.policy['maximum_independent_mode']
        if (type(self.J) is not int or self.J < 32 or self.J % 2
                or int(self.policy['core_points']) <= 4*self.J):
            raise ValueError('complete original mode32 and full2J core quadrature required')
        self.modes = np.arange(2, self.J+1, 2, dtype=int)
        self.core_modes = np.arange(2, 2*self.J+1, 2, dtype=int)
        self.extra_compact_modes = np.arange(34, self.J+1, 2, dtype=int)
        self.tail_degrees = np.asarray(self.policy['tail_degrees'], dtype=int)
        if not np.array_equal(self.tail_degrees, np.arange(len(self.tail_degrees))):
            raise ValueError('the full consecutive tail degree dictionary is required')
        self.tail_left, self.tail_right = self.policy['tail_cutoff_left'], self.policy['tail_cutoff_right']
        self.tail_denominator = self.policy['tail_gaussian_denominator']
        self.core_lift_left, self.core_lift_right = self.policy['core_lift_cutoff_left'], self.policy['core_lift_cutoff_right']
        if (not self.base.R0 <= self.tail_left < self.tail_right <= self.driver.complete.CORE_LEFT
                or not 0 < self.tail_denominator <= 40
                or not self.par.core_start < self.core_lift_left < self.driver.complete.CORE_LEFT
                or not self.core_lift_left < self.core_lift_right < self.par.R):
            raise ValueError('true-tail and actual overlapping core-lift supports are invalid')
        self.old_count = self.old.nq
        self.compact_start = self.old_count
        self.compact_count = len(self.extra_compact_modes)*self.compact.COMPACT_NB
        self.tail_start = self.compact_start+self.compact_count
        self.tail_count = len(self.modes)*len(self.tail_degrees)
        self.j2_germ_index = self.tail_start+self.tail_count
        self.nq = self.j2_germ_index+1
        self.seed_q = np.zeros(self.nq)
        self.seed_q[:self.old_count] = actual_factory.initial_q
        self.seed_q = _readonly(self.seed_q)
        self.seed_old_q = _readonly(actual_factory.initial_q)
        self.core_theta = 2*np.pi*np.arange(int(self.policy['core_points']))/int(self.policy['core_points'])
        self.core_cos = np.cos(self.modes[:, None]*self.core_theta)
        self.core_sin = np.sin(self.modes[:, None]*self.core_theta)
        self.core_all_cos = np.cos(self.core_modes[:, None]*self.core_theta)
        source_trace = self.old.core_trace(self.seed_old_q, self.amplitude)
        self.seed_pc = _readonly(_pad(source_trace['pc'], len(self.modes)))
        self.seed_target = self._core_target(self.seed_pc)
        self.seed_source_P1 = _readonly(_pad(source_trace['target_coeff'], len(self.core_modes)))
        self.seed_core_rectification = _readonly(self.seed_target['target']-self.seed_source_P1)
        # This is a newly reconstructed design seed, not a previously
        # accepted field.  The tiny rule/roundoff difference between the
        # old sampled core projection and complete Laurent target is made
        # an explicit actual B-height term before any new solve.
        self.prescribed_pc = _readonly(self.seed_pc if prescribed_pc is None else prescribed_pc)
        if self.prescribed_pc.shape != self.seed_pc.shape or not np.all(np.isfinite(self.prescribed_pc)):
            raise ValueError('all prescribed total core coefficients are required')
        self.target = self.seed_target if np.array_equal(self.prescribed_pc, self.seed_pc) else self._core_target(self.prescribed_pc)
        if prescribed_pc is None:
            self.trace_input_provenance = {'kind': 'actual_new_R080_reconstructed_seed',
                'old_accepted_core_or_old_fixed_metric_claimed': False}
        else:
            if not isinstance(trace_input_provenance, dict) or not trace_input_provenance:
                raise ValueError('an external total P needs its actual mathematical input provenance')
            self.trace_input_provenance = dict(trace_input_provenance)
        self.B0, self.B1 = self._linear_core_traces()
        self.radial_lift_cache, self.cache = {}, {}
        self.frozen_finite_profile = replace(self.par, gain_height=float(self.seed_old_q[0]))
        self.work_radii, self.fine_radii = actual_factory.work_radii, actual_factory.fine_radii
        self.definition = {'schema': 'new-R080-hard-total-P-variable-E-static-design-v1',
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'actual_factory_definition': actual_factory.definition,
            'parameterized_core_lift_tail_formula_source_sha256': HEIGHT_FORMULAS_SHA,
            'policy': self.policy, 'prescribed_total_P0': self.prescribed_pc.tolist(),
            'trace_input_provenance': self.trace_input_provenance,
            'seed_core_rule_difference_definition': 'same exact T(Pseed), evaluated by complete Laurent coefficients and source projection; numerical difference is an observation',
            'height_definition': 'new_seed_corrected_to_T(Pseed)+L_dx+A*(P-Pseed-B0_dx)+B*(T(P)-T(Pseed)-B1_dx)',
            'core_lift_W_definition': 'new seed W fixed in A; current H changes only mean W; gain vanishes near core',
            'all_free_parameters': self.nq, 'free_H_coordinate': 0,
            'true_new_R080_F2_post_germ_coordinate': self.j2_germ_index,
            'extra_j2_zero_initial_value_embeds_previous_new_seed_exactly': True,
            'amplitude_is_a_numerical_unit_actual_j2_tail_amplitude_is_free': True,
            'new_metric_allowed_to_change_in_static_design': True,
            'old_target86da_used': False, 'no_connection_or_README_claim': True}
        self.design_model_sha256 = _sha(self.definition)
        COUNTS['new_radius_hard_trace_models'] += 1

    def __getattr__(self, name):
        return getattr(self.old, name)

    def guard(self):
        if (type(self) is not Radius080HardTraceDesign
                or self.factory.guard() != self.factory_provenance
                or self.design_model_sha256 != _sha(self.definition)
                or self.prescribed_pc.tolist() != self.definition['prescribed_total_P0']):
            raise ValueError('the actual new-radius hard-trace field changed')
        return {'design_model_sha256': self.design_model_sha256, 'definition': self.definition,
            'all_old_free_columns_and_free_H_retained': True, 'old_fixed_E_provenance_claimed': False}

    def _check_q(self, q):
        value = np.asarray(q, dtype=float)
        if value.shape != (self.nq,) or not np.all(np.isfinite(value)):
            raise ValueError('complete finite new-radius design parameters required')
        self.driver.check(self.deadline)
        return value

    def initial_response(self):
        return self.seed_q.copy()

    def _core_target(self, pc):
        return formulas.GrowingPostFixedMetricHeight._core_target(self, pc)

    def _W_at_core_delta(self, delta):
        return formulas.GrowingPostFixedMetricHeight._W_at_core_delta(self, delta)

    def _linear_core_traces(self):
        B0 = np.zeros((len(self.modes), self.nq))
        B1 = np.zeros((len(self.core_modes), self.nq))
        c = self.par.alpha/(1+self.par.alpha)
        for index in range(1, self.old.nm):
            j = int(self.driver.MODES[index])
            B0[j//2-1, index] = -(j*j-1)/self.par.R*self.amplitude
            B1[j//2-1, index] = -c/self.par.R*j*j*B0[j//2-1, index]
        for index in range(self.old.nm, self.compact.OLD_NQ):
            mode, basis = divmod(index-self.old.nm, self.old.nb)
            B1[mode, index] = self.amplitude*self.old.core_k*(self.par.alpha+2)/self.old.bulk_scale*self.old.core_B[basis]
        B0[0, self.j2_germ_index] = -3/self.par.R*self.amplitude
        B1[0, self.j2_germ_index] = -c/self.par.R*4*B0[0, self.j2_germ_index]
        return _readonly(B0), _readonly(B1)

    def prepare(self, r, ntheta, *, grid_role=None):
        self.guard()
        r = np.asarray(r, dtype=float)
        if ntheta % 4 or ntheta <= 4*self.J:
            raise ValueError('every full2J angular mode needs the complete declared output grid')
        if grid_role is None:
            grid_role = 'work' if ntheta < 512 else 'fine'
        if grid_role not in ('work', 'fine'):
            raise ValueError('actual work or fine grid role required')
        required = self.work_radii if grid_role == 'work' else self.fine_radii
        if not np.all(np.isin(required, r)):
            raise ValueError('all declared new-radius work/fine points must be retained')
        key = (r.tobytes(), int(ntheta))
        if key in self.cache:
            return self.cache[key]
        data = dict(self.old.prepare(r, ntheta))
        first = self.compact.OLD_NQ-1
        data['compact_radial_dictionary'] = data['new_columns'][:, first:first+self.compact.COMPACT_NB, :]
        dh = self.seed_old_q[0]-self.par.gain_height
        W, Wr = data['w0']+dh*data['gain_w'], data['wr0']+dh*data['gain_wr']
        data['new_core_lift'], data['new_core_lift_quad_error_observation'] = formulas.GrowingPostFixedMetricHeight._core_lift(self, r, W, Wr)
        data['analytic_tail_columns'] = formulas.GrowingPostFixedMetricHeight._tail_columns(self, r)
        odd = np.arange(1, ntheta//2, 2, dtype=int)
        data['all_position_odd_modes'] = odd
        data['position_projection'] = self.driver.position.projection(data['theta'], odd)
        data['design_model_sha256'] = self.design_model_sha256
        self.cache[key] = data
        return data

    def _bare_increment(self, dq, data):
        out = dict(zip(JET_KEYS, self.old.delta_jets(dq[:self.old_count], self.amplitude, data)))
        for start, count, modes, radial in (
                (self.compact_start, self.compact_count, self.extra_compact_modes, data['compact_radial_dictionary']),
                (self.tail_start, self.tail_count, self.modes, data['analytic_tail_columns'])):
            if count:
                c = self.amplitude*dq[start:start+count].reshape(len(modes), radial.shape[1])
                f = np.einsum('rbk,jb->rjk', radial, c)
                co, si = np.cos(modes[:, None]*data['theta']), np.sin(modes[:, None]*data['theta'])
                values = (f[:, :, 0]@co, f[:, :, 1]@co, f[:, :, 2]@co,
                    -(f[:, :, 0]*modes)@si, -(f[:, :, 0]*modes*modes)@co, -(f[:, :, 1]*modes)@si)
                for name, value in zip(JET_KEYS, values):
                    out[name] += value
        germ = formulas._separable(data['fields'][:, 0, :],
            np.asarray([self.amplitude*dq[self.j2_germ_index]]), np.asarray([2]), data['theta'])
        for name in JET_KEYS:
            out[name] += germ[name]
        return out

    def height_jets(self, q, amplitude, data):
        q = self._check_q(q)
        if amplitude != self.amplitude:
            raise ValueError('design normalization amplitude is an explicit fixed input')
        if 'new_R080_reference_six_jets' not in data:
            data['new_R080_reference_six_jets'] = dict(zip(JET_KEYS,
                self.old.height_jets(self.seed_old_q, self.amplitude, data)))
        seed = data['new_R080_reference_six_jets']
        dq = q-self.seed_q
        out = self._bare_increment(dq, data)
        ac = self.prescribed_pc-self.seed_pc-self.B0@dq
        bc = self.target['target']-self.seed_source_P1-self.B1@dq
        A = formulas._separable(data['new_core_lift'], ac, self.modes, data['theta'])
        B = formulas._separable(data['core_radial'], bc, self.core_modes, data['theta'])
        for name in JET_KEYS:
            out[name] += seed[name]+A[name]+B[name]
        COUNTS['new_radius_hard_trace_six_jet_points'] += int(out['f'].size)
        return tuple(out[name] for name in JET_KEYS)

    def height_direction(self, indices, data):
        indices = np.asarray(indices, dtype=int)
        if np.any(indices < 0) or np.any(indices >= self.nq):
            raise ValueError('actual new-radius free column indices required')
        nr, nt, nc = len(data['r']), len(data['theta']), len(indices)
        out = {name: np.zeros((nr, nt, nc)) for name in JET_KEYS}
        dw, dwr = np.zeros((nr, 1, nc)), np.zeros((nr, 1, nc))
        for local, index in enumerate(indices):
            if index == 0:
                dw[:, 0, local], dwr[:, 0, local] = data['gain_w'], data['gain_wr']
                continue
            if index == self.j2_germ_index:
                radial = self.amplitude*data['fields'][:, 0, :]
                mode = 2
            elif index < self.old_count:
                radial = self.amplitude*data['new_columns'][:, index-1, :]
                mode = self.old.column_modes[index-1]
            elif index < self.tail_start:
                which, basis = divmod(index-self.compact_start, self.compact.COMPACT_NB)
                radial = self.amplitude*data['compact_radial_dictionary'][:, basis, :]
                mode = self.extra_compact_modes[which]
            else:
                which, basis = divmod(index-self.tail_start, len(self.tail_degrees))
                radial = self.amplitude*data['analytic_tail_columns'][:, basis, :]
                mode = self.modes[which]
            co, si = np.cos(mode*data['theta']), np.sin(mode*data['theta'])
            values = (radial[:, 0, None]*co, radial[:, 1, None]*co, radial[:, 2, None]*co,
                -mode*radial[:, 0, None]*si, -mode*mode*radial[:, 0, None]*co, -mode*radial[:, 1, None]*si)
            for name, value in zip(JET_KEYS, values):
                out[name][:, :, local] = value
        A = _separable_block(data['new_core_lift'], -self.B0[:, indices], self.modes, data['theta'])
        B = _separable_block(data['core_radial'], -self.B1[:, indices], self.core_modes, data['theta'])
        for name in JET_KEYS:
            out[name] += A[name]+B[name]
        return out, dw, dwr

    def combined_height_direction(self, direction, data):
        direction = self._check_q(direction)
        jets = self._bare_increment(direction, data)
        A = formulas._separable(data['new_core_lift'], -(self.B0@direction), self.modes, data['theta'])
        B = formulas._separable(data['core_radial'], -(self.B1@direction), self.core_modes, data['theta'])
        for name in JET_KEYS:
            jets[name] += A[name]+B[name]
        return jets, data['gain_w'][:, None]*direction[0], data['gain_wr'][:, None]*direction[0]

    def core_trace(self, q, amplitude=None):
        q = self._check_q(q)
        if amplitude is not None and amplitude != self.amplitude:
            raise ValueError('the same declared design amplitude is required')
        dq = q-self.seed_q
        return {**self.target, 'pc': self.prescribed_pc.copy(),
            'P1_coeff': self.target['target'].copy(),
            'correction_delta': self.target['target']-self.seed_source_P1-self.B1@dq,
            'lift_coefficients': self.prescribed_pc-self.seed_pc-self.B0@dq,
            'total_P0_and_full_P1_hard_prescribed': True,
            'H_and_free_parameters_do_not_change_prescribed_total_core': True,
            'actual_new_factory_design_seed_not_old_accepted_state': True}

    def core_state(self, q, amplitude, theta):
        self._check_q(q)
        pc = self.prescribed_pc
        co, si = np.cos(self.modes[:, None]*theta), np.sin(self.modes[:, None]*theta)
        P, Pt, Ptt = pc@co, -(pc*self.modes)@si, -(pc*self.modes*self.modes)@co
        P1 = self.target['target']@np.cos(self.core_modes[:, None]*theta)
        e = self.target['e']; u = np.sqrt(e+2*P)
        c = self.par.alpha/(1+self.par.alpha)
        At = -self.par.R*P1+c*(e+2*P)*Ptt-Pt*Pt
        er = -2*(np.mean(P1/u**3)+np.mean(Ptt/u)/(self.par.R*(1+self.par.alpha)))/np.mean(u**-3)
        D = At-self.par.R*er/2
        return {'P': P, 'Pt': Pt, 'Ptt': Ptt, 'Pr': P1, 'e': e, 'u': u, 'At': At,
            'er': er, 'D': D, 'pc': pc.copy(), 'target_coeff': self.target['target'].copy(),
            'turning_error': float(np.mean(1/u)-1),
            'complete_core_D_observation': float(np.max(abs(D))),
            'total_P0_and_full_P1_hard_prescribed': True, 'H_does_not_change_prescribed_P0': True,
            'all_2J_dependent_modes_retained': True, 'core_error_certified': False}

    def geometry(self, q, amplitude, data, *, details=False):
        return self.base.HeightDesign.geometry(self, q, amplitude, data, details=details)

    def evaluate(self, q, data):
        self.guard(); q = self._check_q(q)
        if data.get('design_model_sha256') != self.design_model_sha256:
            raise ValueError('same actual new-radius prepared dictionary required')
        state = self.driver.complete.CompletedCoreHeight.evaluate(self, q, self.amplitude, data)
        state['original_complete_At_M_rows'] = state['residual']
        cache = self.driver.position.prepare(state, data)
        state['position_cache'] = cache
        state['residual'] = self.driver.position.residual(cache, data['position_projection'],
            data['position_radial_units'], self.amplitude)
        state['design_model_sha256'] = self.design_model_sha256
        state['static_design_E_is_trial_dependent'] = True
        COUNTS['new_radius_hard_trace_complete_design_evaluations'] += 1
        return state

    def _field_direction(self, data, state, jets, dw, dwr):
        r = data['r'][:, None, None]
        g = state['g']
        p, b, N, u, E, e = [g[k][:, :, None] for k in ('p', 'b', 'N', 'u', 'E', 'e')]
        w, wr, fr, frr, ft, ftt, B, M, At = [state[k][:, :, None] for k in
            ('w', 'wr', 'fr', 'frr', 'ft', 'ftt', 'B', 'M', 'At')]
        dfr, dfrr, dft, dftt, dfrt = [jets[k] for k in ('fr', 'frr', 'ft', 'ftt', 'frt')]
        denominator = np.mean(N/u**3, axis=1, keepdims=True)
        dp = -dw+dfr
        dN = r*ft*dft/b**3+r*r*(ftt*dp+p*dftt)/b**3+3*r*r*p*ftt*ft*dft/b**5
        dshift = (-2*dw*fr-2*w*dfr+2*fr*dfr+2*p*dp*ft*ft/b**2
            +2*p*p*ft*dft/b**2+2*p*p*ft**3*dft/b**4)
        de = (2*np.mean(dN/u, axis=1, keepdims=True)
            +np.mean(N*dshift/u**3, axis=1, keepdims=True))/denominator
        dE = 2*w*dw+de
        dM = ftt*dp+p*dftt-2*ft*dft/r
        dB = dfrt-dft/r
        dAt = (-r*(dw*frr+w*dfrr)-r*(dwr*fr+wr*dfr)
            -de*wr*ftt-e*dwr*ftt-e*wr*dftt
            +dE*frr*ftt+E*dfrr*ftt+E*frr*dftt
            -(dw*wr+w*dwr)*fr*ftt-w*wr*dfr*ftt-w*wr*fr*dftt
            -dE*B*B-2*E*B*dB+r*(dfr*frr+fr*dfrr)
            +(dw*wr+w*dwr)*ft*ft/r+2*w*wr*ft*dft/r)
        dG = dAt/M-At*dM/M**2
        du, db = (de-dshift)/(2*u), -ft*dft/b
        dS = self.driver.position.derivative(state['position_cache'], dN, du, dE, db, dG)
        return dS, {'implicit_turning_e': de, 'actual_design_E': dE,
            'complete_off_solution_position_terms_retained': True}

    def jacobian(self, q, data, state, block_columns=16):
        self.guard(); q = self._check_q(q)
        if (state.get('design_model_sha256') != self.design_model_sha256
                or not np.array_equal(q, state['q'])):
            raise ValueError('same actual full new-radius state required')
        rows = 2*len(data['all_position_odd_modes'])*len(data['r'])
        J = np.empty((rows, self.nq))
        for first in range(0, self.nq, block_columns):
            self.driver.check(self.deadline)
            indices = np.arange(first, min(self.nq, first+block_columns))
            jets, dw, dwr = self.height_direction(indices, data)
            dS, _ = self._field_direction(data, state, jets, dw, dwr)
            J[:, indices] = self.driver.position.projected_derivative(dS,
                data['position_projection'], data['position_radial_units'], self.amplitude)
            COUNTS['new_radius_hard_trace_complete_analytic_columns'] += len(indices)
        if not np.all(np.isfinite(J)):
            raise ArithmeticError('nonfinite actual H/core/turning/full-position design Jacobian')
        COUNTS['new_radius_hard_trace_complete_Jacobians'] += 1
        return J

    def external_trace_field_direction(self, q, data, state, pc_direction):
        q = self._check_q(q)
        if not np.array_equal(q, state['q']) or state.get('design_model_sha256') != self.design_model_sha256:
            raise ValueError('same actual new-radius design state required')
        pc_direction = np.asarray(pc_direction, dtype=float)
        if pc_direction.shape != self.prescribed_pc.shape or not np.all(np.isfinite(pc_direction)):
            raise ValueError('all actual external trace directions required')
        A = formulas._separable(data['new_core_lift'], pc_direction, self.modes, data['theta'])
        B = formulas._separable(data['core_radial'], self.target['target_jac_pc']@pc_direction,
            self.core_modes, data['theta'])
        jets = {name: (A[name]+B[name])[:, :, None] for name in JET_KEYS}
        zero = np.zeros((len(data['r']), 1, 1))
        dS, receipt = self._field_direction(data, state, jets, zero, zero)
        result = self.driver.position.projected_derivative(dS,
            data['position_projection'], data['position_radial_units'], self.amplitude)
        return {'residual_direction': result[:, 0], 'six_height_jets': jets, **receipt,
            'same_root_full_2J_core_direction': self.target['target_jac_pc']@pc_direction,
            'design_direction_changes_E_and_is_not_a_fixed_g_isometry': True}

    def coefficient_fields(self, q, data, state=None):
        q = self._check_q(q)
        V, oldL, old_modes = self.driver.majorant.coefficient_fields(self.old, self.seed_old_q, self.amplitude, data)
        L = np.zeros((len(data['r']), len(self.core_modes), 3))
        for index, mode in enumerate(old_modes):
            L[:, mode//2-1, :] += oldL[:, index, :]
        dq = q-self.seed_q
        for index, mode in enumerate(self.old.column_modes):
            L[:, mode//2-1, :] += self.amplitude*dq[index+1]*data['new_columns'][:, index, :]
        for start, count, modes, radial in (
                (self.compact_start, self.compact_count, self.extra_compact_modes, data['compact_radial_dictionary']),
                (self.tail_start, self.tail_count, self.modes, data['analytic_tail_columns'])):
            if count:
                c = self.amplitude*dq[start:start+count].reshape(len(modes), radial.shape[1])
                values = np.einsum('rbk,jb->rjk', radial, c)
                for index, mode in enumerate(modes):
                    L[:, mode//2-1, :] += values[:, index, :]
        L[:, 0, :] += self.amplitude*dq[self.j2_germ_index]*data['fields'][:, 0, :]
        ac = self.prescribed_pc-self.seed_pc-self.B0@dq
        bc = self.target['target']-self.seed_source_P1-self.B1@dq
        for index, mode in enumerate(self.modes):
            L[:, mode//2-1, :] += ac[index]*data['new_core_lift']
        L += data['core_radial'][:, None, :]*bc[None, :, None]
        return {'design_model_sha256': self.design_model_sha256,
            'pre_tanh_threejet_coefficients': V, 'all_post_tanh_threejet_coefficients': L,
            'all_post_modes': self.core_modes.copy(), 'free_H_changes_actual_turning_E': True,
            'all_2J_terms_combined_before_norms': True,
            'source_root_mean_angular_and_roundoff_errors_enclosed': False}

    def candidate_metric_definition(self, q, *, candidate_provenance):
        q = self._check_q(q)
        if not isinstance(candidate_provenance, dict) or not candidate_provenance:
            raise ValueError('the actual selected static design provenance is required')
        definition = {'schema': 'new-R080-hard-total-P-selected-fixed-metric-v1',
            'new_design_definition': self.definition, 'selected_complete_q': q.tolist(),
            'selected_complete_q_sha256': _sha(q.tolist()),
            'candidate_provenance': candidate_provenance,
            'metric_definition': 'same complete selected height and W; continuous turning mean fixes E_star(r); g=E_star dr^2+r^2 dtheta^2',
            'all_P0_P1_H_and_dictionaries_frozen_for_subsequent_refinement': True,
            'old_R085_target_or_old_accepted_state_used': False,
            'continuous_source_and_geometric_errors_certified': False}
        return {'new_target_sha256': _sha(definition), 'mathematical_metric_definition': definition}

    def cumulative_cost_receipt(self):
        return {'actual_new_factory_costs': self.factory.cumulative_cost_receipt(),
            'new_hard_trace_counts': dict(COUNTS), 'parameterized_formula_counts': dict(formulas.COUNTS),
            'actual_hard_trace_definition': self.definition,
            'seed_core_rule_difference_observation': self.seed_core_rectification.tolist(),
            'seed_rule_roundoff_difference_is_not_a_frozen_new_mathematical_parameter': True,
            'new_design_metric_not_the_old_fixed_E': True}
