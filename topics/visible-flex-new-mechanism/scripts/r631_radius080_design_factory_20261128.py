#!/usr/bin/env python3
"""A genuinely new R=.8 static-design factory using only R-independent germs.

Every connector/core propagation, forced j4 solution, basis normalization,
spline endpoint, canonical field and grid is rebuilt at the new radius.
The old q/accepted count/eta/metric target are never inherited.  H and the
actual turning-derived E may vary during static design.  Selecting a later
complete candidate for fixed-g refinement is a separate explicit snapshot.
Scientific work runs only in the public repository's Actions environment.
"""
from collections import defaultdict
from dataclasses import asdict
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
from types import SimpleNamespace

import numpy as np

HERE = Path(__file__).resolve().parent
DRIVER_SHA = '6850c9e7f561aadfbc749536b181e1e5e32ff6fddfa6ea3b2de9d08d91b2cfb0'
COUNTS = defaultdict(int)
ATTEMPTS = []


def public_only():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('new-radius science requires this public repository Actions scope')


def _sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def _driver():
    path = HERE / 'r613_full_position_height_20261127.py'
    if hashlib.sha256(path.read_bytes()).hexdigest() != DRIVER_SHA:
        raise RuntimeError('declared complete variable-E position source changed')
    name = 'r631_new_radius_unmodified_position_formulas'
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def mathematical_profile(*, gain_height=.5188903877153482):
    """Explicit design input.  This H is a starting value, never an old result."""
    return {'R': .8, 'log_suppression': 6., 'gain_height': float(gain_height),
        'core_scale': .5, 'drop_end': .34, 'gain_start': .37,
        'gain_peak': .48, 'gain_end': .61, 'core_start': .55,
        'alpha': .55, 'beta': 1.1, 'core_height': .04,
        'ball_budget': 1.032, 'reach_budget': .062, 'target_core_support': 1.}


def numerical_settings(*, M=25, rtol=2e-11, atol=2e-13, height_saturation=.15):
    return {'M': M, 'rtol': float(rtol), 'atol': float(atol),
            'height_saturation': float(height_saturation)}


class Radius080Design:
    """Own the actual new field; its metric is allowed to change in design."""
    def __init__(self, driver, field, initial_q, amplitude, definition, reconstruction):
        self.driver, self.field = driver, field
        self.initial_q = np.asarray(initial_q, dtype=float).copy()
        self.amplitude = float(amplitude)
        self.definition = definition
        self.design_model_sha256 = _sha(definition)
        self.high_mode_objects = list(reconstruction['high_mode_objects'])
        self.reconstruction_receipt = {key: value for key, value in reconstruction.items()
            if key != 'high_mode_objects'}
        self.initial_q.flags.writeable = False
        self.accepted_steps = 0
        self.work_radii = driver.compact.radial_grid(field, 1)
        self.fine_radii = driver.compact.radial_grid(field, 2)
        if (np.any(self.work_radii >= .8) or np.any(self.fine_radii >= .8)
                or np.any(np.diff(self.work_radii) <= 0) or np.any(np.diff(self.fine_radii) <= 0)):
            raise ValueError('the actual new-radius domain/grid is inconsistent')
        self.grid_receipt = {'work_points': int(len(self.work_radii)),
            'fine_points': int(len(self.fine_radii)),
            'work_sha256': _sha(self.work_radii.tolist()), 'fine_sha256': _sha(self.fine_radii.tolist()),
            'new_profile_new_spline_spans_and_all_compact_spans_included': True,
            'old_R085_radii_or_accepted_eta_transferred': False}

    def __getattr__(self, name):
        return getattr(self.field, name)

    def guard(self):
        if (type(self) is not Radius080Design or self.field.par.R != .8
                or self.design_model_sha256 != _sha(self.definition)
                or asdict(self.field.par) != self.definition['new_profile']
                or self.initial_q.tolist() != self.definition['design_initial_response']
                or self.amplitude != self.definition['amplitude']
                or self.field.paidq.tolist() != self.definition['new_frozen_pre_tanh_and_force_coefficients']
                or self.field.bs.t.tolist() != self.definition['new_complete_B_spline_knots']):
            raise ValueError('actual new-radius design field changed its declared definition')
        return {'design_model_sha256': self.design_model_sha256,
            'mathematical_definition': self.definition,
            'new_radius': .8, 'metric_is_trial_dependent_during_design': True,
            'old_86da_target_or_old_acceptance_claimed': False}

    def _q(self, q):
        q = np.asarray(q, dtype=float)
        if q.shape != (self.field.nq,) or not np.all(np.isfinite(q)):
            raise ValueError('complete finite actual design coordinates are required')
        self.driver.check(self.deadline)
        return q

    def evaluate_design(self, q, data):
        """Actual variable-E turning geometry with H a genuine design control."""
        self.guard()
        q = self._q(q)
        state = self.field.evaluate(q, self.amplitude, data)
        state['new_radius_design_identity'] = self.design_model_sha256
        state['actual_design_q'] = q.copy()
        state['actual_design_amplitude'] = self.amplitude
        state['metric_allowed_to_change_with_static_design'] = True
        state['design_parameter_is_not_final_isometry_time'] = True
        COUNTS['new_radius_complete_variable_E_design_evaluations'] += 1
        return state

    def jacobian_design(self, q, data, state):
        q = self._q(q)
        if (state.get('new_radius_design_identity') != self.design_model_sha256
                or not np.array_equal(q, state.get('actual_design_q'))):
            raise ValueError('the actual same new-radius design state is required')
        result = self.field.jacobian(q, self.amplitude, data, state)
        COUNTS['new_radius_complete_variable_E_design_jacobians'] += 1
        return result

    def actual_core_seed(self, q):
        """The reconstructed new core, with no old accepted-state label."""
        q = self._q(q)
        trace = self.field.core_trace(q, self.amplitude)
        return {'new_radius': .8, 'design_model_sha256': self.design_model_sha256,
            'actual_design_q': q.tolist(), 'actual_design_q_sha256': _sha(q.tolist()),
            'actual_total_P0_coefficients': np.asarray(trace['pc']).tolist(),
            'actual_P0_modes': self.driver.MODES.tolist(),
            'actual_core_e_observation': float(trace['e']),
            'actual_full_P1_coefficients': np.asarray(trace['target_coeff']).tolist(),
            'actual_P1_modes': self.driver.CORE_MODES.tolist(),
            'old_core_normalizations_or_old_q_reused': False,
            'this_source_is_a_design_seed_not_an_accepted_connection_root': True,
            'core_root_source_and_roundoff_errors_enclosed': False}

    def candidate_metric_definition(self, q, *, candidate_provenance):
        """Complete function definition to freeze AFTER selecting an actual design.

        This does not qualify the candidate.  It separates design freedom
        from a later fixed-g refinement and keeps all unresolved errors.
        """
        q = self._q(q)
        if not isinstance(candidate_provenance, dict) or not candidate_provenance:
            raise ValueError('the selected actual static design provenance is required')
        definition = {'schema': 'new-R080-actual-selected-static-metric-function-v1',
            'source_design_mathematical_definition': self.definition,
            'selected_actual_q': q.tolist(), 'selected_actual_q_sha256': _sha(q.tolist()),
            'selected_amplitude': self.amplitude,
            'candidate_provenance': candidate_provenance,
            'metric_definition': 'E_star(r)=W_selected(r)^2+e_selected(r); mean_theta(N/sqrt(e-shift))=1; g=E_star dr^2+r^2 dtheta^2',
            'reference_height_includes_complete_canonical_tanh_post_and_all_core_corrections': True,
            'inner_germ_definition': self.definition['true_inner_germ_definition'],
            'fixed_during_future_refinement': ['all_selected_q', 'amplitude', 'R',
                'all_profile_parameters', 'all_complete_basis_definitions', 'all_final_isometry_time_range'],
            'old_R085_target_identity_or_old_acceptance_transferred': False,
            'unresolved_errors': self.definition['unresolved_errors'],
            'complete_connection_or_README_criteria_asserted': False}
        return {'mathematical_metric_definition': definition,
            'new_target_sha256': _sha(definition),
            'actual_radial_E_arrays_not_substituted_for_the_full_function': True}

    def cumulative_cost_receipt(self):
        d = self.driver
        return {'new_factory_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'design_model_sha256': self.design_model_sha256,
            'new_radius_reconstruction': self.reconstruction_receipt,
            'new_radius_grid_receipt': self.grid_receipt,
            'new_factory_counts': dict(COUNTS), 'attempts': list(ATTEMPTS),
            'original_base_counts': dict(d.base.COUNTS),
            'forced_counts': dict(d.paid.NEW_COUNTS), 'complete_height_counts': dict(d.complete.COUNTS),
            'compact_counts': dict(d.compact.NEW), 'full_spectrum_counts': dict(d.full.NEW),
            'high_mode_attempts': d.full.attempt_receipts(self.high_mode_objects),
            'old_inner_germ_costs_are_inherited_inputs_not_new_work': True,
            'overlapping_counters_are_not_disjoint_costs': True}


def build_radius080_design(*, paid_reconstruction_json, paid_reconstruction_sha256,
        profile_input, numerical_input, amplitude, deadline, attempts,
        pre_tanh_and_force_initial=None, complete_design_initial=None,
        force_normalization=1.):
    """Rebuild the actual field at R=.8; never calls an old restore_model."""
    public_only()
    if hashlib.sha256(paid_reconstruction_json.encode()).hexdigest() != paid_reconstruction_sha256:
        raise ValueError('literal R-independent paid inner data source differs')
    source = json.loads(paid_reconstruction_json)
    d = _driver()
    profile_input = json.loads(json.dumps(profile_input, allow_nan=False))
    numerical_input = json.loads(json.dumps(numerical_input, allow_nan=False))
    if (profile_input.get('R') != .8 or numerical_input.get('M') != 25
            or numerical_input.get('height_saturation') != .15
            or not np.isfinite(amplitude) or amplitude <= 0
            or not np.isfinite(force_normalization) or force_normalization <= 0):
        raise ValueError('explicit actual R=.8 design profile and finite normalization inputs required')
    if (set(numerical_input) != {'M', 'rtol', 'atol', 'height_saturation'}
            or not all(np.isfinite(numerical_input[key]) and numerical_input[key] > 0
                       for key in ('rtol', 'atol', 'height_saturation'))):
        raise ValueError('complete declared positive reconstruction accuracy inputs are required')
    args = SimpleNamespace(**numerical_input)
    profile = d.base.gain.Profile(**profile_input)
    d.check(deadline)
    COUNTS['new_radius_factory_attempts'] += 1
    outer_receipts, flat_sources = [], {}
    low_flats = []
    for j in d.base.MODES:
        d.check(deadline)
        row = {'kind': 'R_independent_low_dense_field', 'mode': int(j), 'status': 'started'}
        ATTEMPTS.append(row)
        flat_sources[str(int(j))] = dict(d.parent.PAID_SEEDS[str(int(j))])
        before = dict(d.base.COUNTS)
        flat = d.parent.PaidFlatSeed(int(j), args)
        row.update(status='completed', new_dense_seed_RHS=int(d.base.COUNTS['seed_RHS']-before['seed_RHS']))
        low_flats.append(flat)
    all_flats = list(low_flats)
    for j in (10, 12, 14, 16):
        d.check(deadline)
        record = source['paid_modes_10_through_16'][str(j)]
        flat_sources[str(j)] = record['finite_inner_data']
        flat = d.resume.ReusedHigherFlat(j, args, record)
        all_flats.append(flat)
    minimum = max(value.minimum_radius for value in all_flats)
    high_objects = []
    for j in (18, 20, 22):
        d.check(deadline)
        record = source['paid_modes_18_through_22'][str(j)]
        flat_sources[str(j)] = record['finite_inner_data']
        flat = d.full.PaidFactoredFlat.__new__(d.full.PaidFactoredFlat)
        attempts.append(flat); high_objects.append(flat)
        flat.__init__(j, args, record, deadline, minimum)
        all_flats.append(flat)
    modes = []
    for flat in all_flats:
        d.check(deadline)
        row = {'kind': 'new_R080_connector_core', 'mode': int(flat.mode), 'status': 'started'}
        ATTEMPTS.append(row)
        connector_before = d.base.COUNTS['connector_RHS']
        core_before = d.base.COUNTS['core_basis_RHS']
        mode = d.base.AdmissibleMode(flat, profile, args)
        row.update(status='completed', connector_RHS=int(d.base.COUNTS['connector_RHS']-connector_before),
            core_RHS=int(d.base.COUNTS['core_basis_RHS']-core_before))
        modes.append(mode)
        outer_receipts.append({'mode': int(flat.mode), 'new_R': .8,
            'actual_rebuilt_core_and_match': mode.receipt(),
            'old_R085_core_A_or_C_used': False})
    # Only the old knot topology is a design template.  It has new physical
    # coordinates above .65 and a new exact endpoint .8; no old q is mapped.
    template = np.asarray(json.loads(d.weak.RAW_KNOT_JSON), dtype=float)
    knots = np.where(template <= .65, template,
        .65+(template-.65)*(.8-.65)/(.85-.65))
    knots[template == .85] = .8
    if np.any(knots > .8) or len(knots) != 67:
        raise ValueError('new endpoint knot dictionary is incomplete')
    base_height = d.base.HeightDesign(profile, modes[:4], knots[6:-6], args)
    local, _ = d.parent.enrich_same_state(base_height, np.zeros(base_height.nq))
    d.check(deadline)
    force_row = {'kind': 'new_R080_forced_j4', 'status': 'started'}
    ATTEMPTS.append(force_row)
    force = d.paid.BodyForcedFour(low_flats[1], modes[0], profile, args, deadline)
    force.scale = float(force_normalization)
    force_row.update(status='completed', new_declared_normalization=float(force_normalization))
    # The source supplies an explicit subclass constructor pattern.  This
    # transfers only this freshly created R=.8 object's dictionary, never an
    # old accepted model or a field with a frozen R=.85 identity.
    forced = d.paid.ForcedHeightDesign.__new__(d.paid.ForcedHeightDesign)
    forced.__dict__.update(local.__dict__)
    forced.cache = {}
    forced.forced, forced.original_nq, forced.nq = force, local.nq, local.nq+1
    if pre_tanh_and_force_initial is None:
        paidq = np.zeros(forced.nq); paidq[0] = profile.gain_height
    else:
        paidq = np.asarray(pre_tanh_and_force_initial, dtype=float).copy()
    if paidq.shape != (forced.nq,) or not np.all(np.isfinite(paidq)):
        raise ValueError('all new pre-tanh/local/force design coefficients are required')
    skeleton = SimpleNamespace(old=forced, paidq=paidq, modes=modes, minimum=minimum)
    field = d.FullPositionHeight(skeleton, modes, args, deadline)
    if field.nq != 1130 or field.nb != 61 or field.par.R != .8:
        raise ValueError('the full new-radius dictionary has unexpected dimensions')
    if complete_design_initial is None:
        q = np.zeros(field.nq); q[0] = profile.gain_height
    else:
        q = np.asarray(complete_design_initial, dtype=float).copy()
    if q.shape != (field.nq,) or not np.all(np.isfinite(q)):
        raise ValueError('all actual new static design coordinates are required')
    field.actual_checkpoint = field.pending_trial = field.last_trial = None
    force_receipt = {'background_profile': asdict(profile), 'scale': force.scale,
        'actual_raw_A_core': float(force.Acore), 'actual_tail_multiplier': float(force.tail_multiplier),
        'actual_raw_combined_C_core': float(force.raw_Ccore_after_combination),
        'backward_switch_difference_observation': force.backward_switch_difference,
        'old_forced_solution_or_paid_force_normalization_used': False}
    definition = {'schema': 'new-R080-static-design-variable-E-complete-position-v1',
        'factory_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'unchanged_formula_source_sha256': DRIVER_SHA,
        'new_profile': asdict(profile), 'amplitude': float(amplitude),
        'new_complete_B_spline_knots': field.bs.t.tolist(),
        'new_frozen_pre_tanh_and_force_coefficients': paidq.tolist(),
        'design_initial_response': q.tolist(), 'forced_normalization': float(force_normalization),
        'force_background_is_new_profile_at_construction_not_later_trial_H': True,
        'all_original_positive_modes_and_complete_position_rows_retained': True,
        'compact_dictionary': [patch.tolist() for patch in d.compact.PATCH_KNOTS],
        'core_completion_cutoff': [float(d.complete.CORE_LEFT), float(d.complete.CORE_RIGHT)],
        'R_independent_inner_data_source_sha256': paid_reconstruction_sha256,
        'R_independent_inner_data_sha256': _sha(flat_sources),
        'true_inner_germ_definition': {'rc': '11/50', 'ell': '1/5', 'A': '4/5',
            'u': 'ell/(r-rc)', 'W': 'A*exp(-u*(2-sin(u)))', 'phase': 0,
            'all_even_germs': list(range(2, 23, 2)),
            'germ_choice': 'same projective infinite-DtN limit; paid finite-M mouths only approximate it',
            'outer_normalization': 'NEW R=.8 exact connector/core ODE and NEW Acore normalization',
            'zero_continuation_below_any_numerical_mouth': False},
        'static_design_H_W_and_turning_E_may_change': True,
        'hard_total_P_extension_must_eliminate_total_traces_not_only_new_core_columns': True,
        'first_frozen_metric_must_be_a_new_selected_actual_design_definition': True,
        'old_R085_q_eta_accepted_count_or_target_hash_inherited': False,
        'initial_accepted_steps': 0,
        'unresolved_errors': ['old_infinite_DtN_finite_M_and_Cauchy_input',
            'new_dense_inner_reconstruction_error', 'new_R080_connector_and_core_ODE_error',
            'new_mode_and_force_normalization_roundoff', 'canonical_mean_and_turning_root_error',
            'angular_primitive_and_radial_readout_error', 'complete_connection_embedding_and_cross_piece_reach']}
    reconstruction = {'actual_new_mode_receipts': outer_receipts, 'actual_new_force_receipt': force_receipt,
        'numerical_settings': numerical_input, 'R_independent_reused_germs': flat_sources,
        'high_mode_objects': high_objects,
        'all_old_R085_connector_core_and_normalization_values_discarded': True,
        'no_new_inner_DtN_slope_or_old_diagnostic_gate': True}
    COUNTS['new_radius_factories_completed'] += 1
    return Radius080Design(d, field, q, amplitude, definition, reconstruction)
