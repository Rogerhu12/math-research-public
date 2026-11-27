#!/usr/bin/env python3
"""Complete R715 reference-centred field geometry and original full rows.

All original world sixjet scans, both witness signs, permanent positions,
full 192-prefix selection and complete parameter transposes are retained.
The new physical field includes its complete current raw closure lift.
Working Fs is not labelled unit. No previous-field certificate is inherited.
"""
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib.util
import json
import math
import mmap
import os
from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np
import torch

MATERIAL_ENVELOPE_MEMORY_SHA256 = 'c79c7f7ec1febf0ab6dca30d28a91b1566745972342c7336a3a9a106f56b3152'
CURRENT_MATERIAL_ENVELOPE_MEMORY_SHA256 = "f1c6629fc52e17ad8cc74d1fd2431e3e7ee132e9da2b46ed4cf63a14e99d38ba"
MATERIAL_ENVELOPE_ROWS_SHA256 = '729910dc27b0dc4fb5b1b019635f8dc606dcb2965fcbd3c47dc380b7a028c8d7'


SCHEMA = 'complete-run10-M320-immutable-point-envelope-world-geometry-v1'
ANALYTIC_STAGE_SOURCE_SHA256 = '3f351c6b0aa80ff025e5714f8dcbf67cba870e5e9c45b9ad80b61198e5fa00ed'
OPERATOR_SCHEMA = "complete-R711-reference-centred-frequency-refined-immutable-point-closure-analytic-frame-J3-normal-layer-v1"
PURE_GEOMETRY_SHA256 = 'a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854'
SELECTOR_SHA256 = 'e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8'
ENDPOINT_SOURCE_SHA256 = 'a53b2ad03c1c5ba81a0392c6fe7bd08076f6e8f3f11e64f7e997f8319bedc8aa'
STAGE_MATRIX_SOURCE_SHA256 = '93944b0a344e9d155477b874dc215cc104e616e74bcee536609484e1cddc8168'
ADJACENT_FRAME_SOURCE_SHA256 = '2331d3a43188b39eeb3522094af1351ca8df46fe0820cf65597cb04b8d19c40c'
BASE_OPERATOR_SCHEMA = 'complete-R711-frequency-refined-frozen-reference-so3-meridian-with-core-lift-v1'
BASE_SOURCE_SHA256 = '41c865d9a505f4b7ac3b0b9c2b89a027235e78968b1f62cf7840bc119179efb2'
SEED_PROVIDER_SHA256 = '0d09ca45500e85c2cdada0155c79a8db71b92d84600743a90db88889ac58662b'
SEED_MEAN_SHA256 = 'f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917'
SUPPORTED_INPUT_BINDER_SHA256 = 'bde3fd4cab72c6296472928cd9760ad88063462ac5872c2c88addd75958d2971'
DERIVED_FROM_COMPLETE_GEOMETRY_SHA256 = '255760e188d13f22ffef86c029f35f5d1629384411d2e32f03f75df60f4ab71c'
REFERENCE_CENTERING_SOURCE_SHA256 = '61ad9a9e782c0fd67bf83887d8414968946e8543baac773dcc628419f0248992'
CLOSURE_VALUE_SOURCE_SHA256 = 'e87044f0b0a51c9552f3f4028617a433c661e73b6a4507a6edb5ddbab7a877fb'
KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')
MARKER_HEIGHT_EXACT = Fraction(1, 1000)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific SO3 geometry requires the public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    h = hashlib.sha256(str(value.dtype).encode())
    h.update(json.dumps(list(value.shape)).encode())
    h.update(value.tobytes())
    return h.hexdigest()


def load_source(path, expected):
    path = Path(path).resolve()
    if sha(path) != expected:
        raise ValueError('The complete reused source differs: '+str(path))
    name = 'so3_geometry_dependency_'+expected
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _round_fraction(value, *, upward):
    rounded = float(value)
    exact = Fraction.from_float(rounded)
    if (upward and exact < value) or (not upward and exact > value):
        rounded = math.nextafter(rounded, math.inf if upward else -math.inf)
    return rounded


@dataclass(frozen=True)
class Budgets:
    """Immutable marked/body/held budgets for the actual NEW physical field.

    Scalar roundings are directed, but field evaluations remain numerical.
    R is this same frozen deep scalar profile's terminal radius carrier.
    """
    marked_diameter_budget: float
    witness_lower_budget: float
    cap_radius: float
    height_floor: float

    def __post_init__(self):
        for name in ('marked_diameter_budget', 'witness_lower_budget',
                     'cap_radius', 'height_floor'):
            value = float(getattr(self, name))
            if not math.isfinite(value):
                raise ValueError('All fixed amplitude budgets must be finite')
            object.__setattr__(self, name, value)
        D, L, R, H = (Fraction.from_float(getattr(self, name)) for name in
            ('marked_diameter_budget', 'witness_lower_budget', 'cap_radius', 'height_floor'))
        if not 2*MARKER_HEIGHT_EXACT < D <= Fraction(9, 2):
            raise ValueError('Need 2h < marked D <= 4.5 for the fixed diameter-0.9 grip')
        if L <= 0 or 5*L < D:
            raise ValueError('The held-witness lower budget must be at least marked D/5')
        if R <= Fraction(9, 20):
            raise ValueError('The fixed same-profile cap must contain the radius-0.45 grip')
        if H <= 1:
            raise ValueError('An explicit fixed height floor greater than 1 is required')

    @property
    def body_diameter_budget(self):
        return _round_fraction(Fraction.from_float(self.marked_diameter_budget)
                               - 2*MARKER_HEIGHT_EXACT, upward=False)

    @property
    def amplitude_height_floor(self):
        return _round_fraction(Fraction.from_float(self.witness_lower_budget)
                               + MARKER_HEIGHT_EXACT, upward=True)

    @property
    def effective_height_floor(self):
        return max(self.height_floor, self.amplitude_height_floor)

    def metadata(self):
        return dict(marked_diameter_budget=self.marked_diameter_budget,
            body_diameter_budget=self.body_diameter_budget,
            witness_lower_budget=self.witness_lower_budget,
            cap_radius=self.cap_radius, cap_radius_carrier_hex=self.cap_radius.hex(),
            height_floor=self.height_floor,
            amplitude_height_floor=self.amplitude_height_floor,
            effective_height_floor=self.effective_height_floor,
            marker_height_exact='1/1000', fixed_grip_diameter=0.9,
            body_budget_rounding='downward from exact binary64 marked D minus 2/1000',
            amplitude_height_rounding='upward from exact binary64 L plus 1/1000',
            fixed_during_direction_and_all_trial_reads=True,
            cap_radius_scope='same frozen deep-profile terminal radius; no free R variable',
            scope='Design constraints for the chosen whole-image witness; finite values are not continuous certificates')


def _key(location):
    return (int(location['cell']), float(location['u']).hex(), float(location['phi']).hex())


def _discard(matrix):
    if (isinstance(matrix, np.memmap) and hasattr(matrix._mmap, 'madvise')
            and hasattr(mmap, 'MADV_DONTNEED')):
        matrix._mmap.madvise(mmap.MADV_DONTNEED)


class GeometryScreen:
    def __init__(self, problem, repo, budgets, *, reach_ratio=.03,
                 reach_safety_factor=.992, amplitude_top_radius=2,
                 amplitude_top_distance=4, envelope=None):
        require_actions()
        self.q = problem
        self.repo = Path(repo).resolve()
        self.budgets = budgets
        self.envelope_memory_source_sha256=(None if envelope is None else sha(type(envelope).__init__.__code__.co_filename))
        if self.envelope_memory_source_sha256 != CURRENT_MATERIAL_ENVELOPE_MEMORY_SHA256:
            raise ValueError('The complete actual envelope consumer is required')
        if envelope.model_identity != problem.identity:
            raise ValueError('The envelope belongs to another full physical model')
        self.envelope = envelope
        self.envelope_rows = load_source(Path(__file__).with_name('complete_material_envelope_rows.py'),
            MATERIAL_ENVELOPE_ROWS_SHA256)
        self._extra_grid = None
        self._extra_complete = False
        if not isinstance(budgets, Budgets):
            raise TypeError('Use one immutable Budgets instance for the whole continuation')
        if float(problem.R).hex() != budgets.cap_radius.hex():
            raise ValueError('Amplitude R must be the actual unchanged scalar-profile R')
        self.reach_ratio = float(reach_ratio)
        self.safety = float(reach_safety_factor)
        if not (0 < self.reach_ratio < 1 and 0 < self.safety < 1):
            raise ValueError('Use explicit positive reach ratio and numerical safety below one')
        self.amplitude_top_radius = int(amplitude_top_radius)
        self.amplitude_top_distance = int(amplitude_top_distance)
        if (self.amplitude_top_radius != amplitude_top_radius
                or self.amplitude_top_distance != amplitude_top_distance
                or not 1 <= self.amplitude_top_radius <= 2
                or not 1 <= self.amplitude_top_distance <= 4):
            raise ValueError('Use at most two radius and four paired-distance working locations')
        model = problem.model
        if (model.get('schema') != OPERATOR_SCHEMA
                or model.get('source_sha256') != ENDPOINT_SOURCE_SHA256
                or model.get('base_schema') != BASE_OPERATOR_SCHEMA
                or model.get('all_current_free_core_coefficients_retained') is not True
                or model.get('all_original_rotation_variables_retained') is not True
                or model.get('current_height_free') is not True
                or model.get('radial_Gram_error_identically_zero') is not False
                or model.get('accurate_zero_root_radial_Gram_error_identically_zero') is not True
                or model.get('mathematical_field_definition_requires_exact_implicit_root') is not True
                or model.get('moment_Q_recomputed_from_current_field') is not False
                or model.get('moment_Q_is_an_exact_integral_inverse_claimed') is not False
                or model.get('correction_side') != 'left multiplication in WORLD coordinates'):
            raise ValueError('Use the complete independent normal-lift field and all of its sequential implicit derivatives')
        local_matrix = problem.analytic_stage_jacobian
        if (local_matrix.q is not problem
                or local_matrix.definition != model.get('analytic_stage_jacobian')
                or local_matrix.definition.get('source_sha256') != ANALYTIC_STAGE_SOURCE_SHA256
                or sha(type(local_matrix).__init__.__code__.co_filename) != ANALYTIC_STAGE_SOURCE_SHA256
                or local_matrix.model_identity != problem.identity):
            raise ValueError('Bind the entire selected local J3 producer without changing the physical sixjets')
        closure=problem.detached_closure_values
        closure_policy=model.get('detached_closure_value_reuse')
        if (closure.q is not problem or closure.identity!=problem.identity
                or closure.operator_source!=ENDPOINT_SOURCE_SHA256
                or closure_policy!=closure.definition
                or closure_policy.get('source_sha256')!=CLOSURE_VALUE_SOURCE_SHA256
                or closure_policy.get('active_parameter_J_and_transpose_use_original') is not True
                or closure_policy.get('all_32_or_declared_stages_tau_targets_domains_residuals_and_trace_retained') is not True
                or closure_policy.get('every_stage_final_closure_reread_forces_original') is not True
                or closure_policy.get('final_endpoint_closure_reread_forces_original') is not True
                or closure_policy.get('exact_normal_partition_or_root_selection_changed') is not False
                or closure_policy.get('cache_lifetime_ends_at_the_same_chain_return_or_exception') is not True):
            raise ValueError('Only complete detached closure values may be reused inside one unchanged chain')
        for name in ('__init__','value','scope','metadata','progress'):
            method=getattr(closure,name)
            if sha(method.__func__.__code__.co_filename)!=CLOSURE_VALUE_SOURCE_SHA256:
                raise ValueError('The complete closure-value helper method differs: '+name)
        calibration = problem.reference_calibration
        definition = model.get('reference_centering_definition')
        if (not isinstance(definition,dict) or definition != calibration.definition
                or definition.get('schema') != 'R715-fixed-reference-centred-working-normal-definition-v1'
                or definition.get('source_sha256') != REFERENCE_CENTERING_SOURCE_SHA256
                or definition.get('endpoint_source_sha256') != ENDPOINT_SOURCE_SHA256
                or definition.get('original_reference_point_sha256') != array_sha(problem.base.initial())
                or definition.get('base_model_identity_sha256') != problem.base.identity
                or definition.get('fixed_supported_reference_identity_sha256') != problem.base.parent_jet.model_identity
                or definition.get('nodewise_difference_before_original_complete_cumsum') is not True
                or definition.get('all_normal_stages_and_full_upstream_parameter_jets_retained') is not True
                or definition.get('numerical_current_raw_closure_defect_omitted') is not False
                or definition.get('numerical_radial_Gram_error_identically_zero') is not False
                or calibration.field_identity != problem.identity):
            raise ValueError('Bind the complete SAME frozen-reference calibration and physical raw-defect lift')
        for name in ('reference_data','observe_field','current_record'):
            if sha(getattr(calibration,name).__func__.__code__.co_filename) != REFERENCE_CENTERING_SOURCE_SHA256:
                raise ValueError('The actual complete calibration helper changed: '+name)
        normal_nodes = tuple(Fraction(value) for value in problem.normal_step_nodes)
        normal_words = [str(value) for value in normal_nodes]
        normal_steps = len(normal_nodes)-1
        if (normal_steps < 1 or normal_nodes[0] != 0 or normal_nodes[-1] != 1
                or any(a >= b for a, b in zip(normal_nodes, normal_nodes[1:]))
                or model.get('exact_normal_step_nodes') != normal_words):
            raise ValueError('Bind one complete fixed exact normal partition shared by every angle and full free point')
        if (model.get('implicit_control_dimension') != 6
                or model.get('normal_increment_dimension') != 3
                or model.get('implicit_dimension_per_stage') != 9
                or model.get('complete_first_angular_implicit_dimension') != 6*normal_steps
                or model.get('complete_second_angular_implicit_dimension') != 9*normal_steps
                or model.get('common_partition_for_all_angles_and_free_points') is not True
                or model.get('per_angle_adaptive_normal_partition') is not False
                or model.get('normal_partition_is_part_of_selected_field_definition') is not True
                or model.get('stationary_KKT_selection_used') is not False):
            raise ValueError('Keep every full normal-step root/jet and its interstage parameter derivative; no KKT selection is relabelled')
        gamma_nodes = tuple(Fraction(value) for value in problem.gamma_nodes)
        gamma_words = [str(value) for value in gamma_nodes]
        if (len(gamma_nodes) != 3 or not 0 < gamma_nodes[0] < gamma_nodes[1] < gamma_nodes[2] < 1
                or model.get('exact_relative_gamma_nodes') != gamma_words):
            raise ValueError('The actual fixed relative gamma input differs from the complete mathematical model')
        frozen = model.get('frozen_moment_Q_definition')
        if (not isinstance(frozen, dict)
                or frozen.get('schema') != 'frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
                or canonical(frozen) != model.get('frozen_moment_Q_definition_identity_sha256')
                or frozen != problem.frozen_moment_definition
                or model['frozen_moment_Q_definition_identity_sha256'] != problem.frozen_moment_identity):
            raise ValueError('Keep this same explicitly frozen full literal moment-Q input')
        base = model['base_complete_model']
        if (base != problem.base.model or canonical(base) != model['base_model_identity_sha256']
                or base.get('schema') != BASE_OPERATOR_SCHEMA
                or base.get('source_sha256') != model['base_source_sha256']
                or model['fixed_scalar_metric_identity_sha256'] != problem.context.scalar_identity
                or model['fixed_scalar_profile_definition'] != problem.context.scalar_definition
                or base['fixed_scalar_metric_identity_sha256'] != problem.context.scalar_identity):
            raise ValueError('The actual complete direct reference/base/fixed scalar differs')
        new_literal_input = frozen['schema'] == 'frequency-refined-supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
        literal_input_schema = model.get('literal_Q_input_schema')
        literal_binder_sha = model.get('new_reference_input_binding_source_sha256')
        if new_literal_input:
            if (literal_input_schema != 'frequency-refined-supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'
                    or literal_binder_sha != SUPPORTED_INPUT_BINDER_SHA256
                    or not isinstance(literal_binder_sha, str) or len(literal_binder_sha) != 64
                    or any(ch not in '0123456789abcdef' for ch in literal_binder_sha)):
                raise ValueError('The new-reference literal input must declare its actual independently bound producer source')
            expected_keys = {'schema', 'Q0_binary64_hex', 'exact_relative_bubble_nodes',
                'fixed_scalar_metric_identity_sha256', 'fixed_scalar_profile_definition',
                'initial_reference_bundle_sha256', 'initial_reference_model_identity_sha256',
                'base_model_identity_sha256', 'initial_full_point_sha256', 'fixed_chart_core_sha256',
                'fixed_supported_unit_seed_model', 'fixed_supported_unit_seed_identity_sha256'}
            if (set(frozen) != expected_keys
                    or frozen['fixed_scalar_metric_identity_sha256'] != problem.context.scalar_identity
                    or frozen['fixed_scalar_profile_definition'] != problem.context.scalar_definition
                    or canonical(frozen['fixed_scalar_profile_definition']) != problem.context.scalar_identity
                    or frozen['base_model_identity_sha256'] != problem.base.identity
                    or frozen['initial_reference_bundle_sha256'] != base['initial_reference_bundle_sha256']
                    or frozen['initial_reference_bundle_sha256'] != problem.context.input_records['reference_bundle']['sha256']
                    or frozen['initial_reference_model_identity_sha256'] != base['initial_reference_model_identity_sha256']
                    or frozen['initial_reference_model_identity_sha256'] != problem.context.identity
                    or frozen['fixed_chart_core_sha256'] != base['fixed_chart_core_sha256']
                    or frozen['fixed_chart_core_sha256'] != array_sha(problem.parent_core)
                    or frozen['initial_full_point_sha256'] != array_sha(problem.base.initial())
                    or frozen['exact_relative_bubble_nodes'] != [[str(Fraction(v)) for v in row]
                                                                for row in problem.bubble_nodes]):
                raise ValueError('The new literal Q must bind this actual complete reference, profile, chart and original full initial point')
        elif (literal_input_schema != 'frozen-zero-endpoint-moment-Q-input-v1'
                or literal_binder_sha is not None):
            raise ValueError('The original actual-moment input must retain its own exact schema and binding path')
        seed = base.get('fixed_supported_unit_seed_model')
        if (base.get('source_sha256') != BASE_SOURCE_SHA256
                or not isinstance(seed, dict)
                or seed.get('schema') != 'complete-supported-smooth-triangle-meridian-seed-reference-v1'
                or seed.get('source_sha256') != SEED_PROVIDER_SHA256
                or seed.get('mean_kernel_source_sha256') != SEED_MEAN_SHA256
                or canonical(seed) != base.get('fixed_supported_unit_seed_identity_sha256')
                or seed != problem.base.parent_jet.model
                or seed != frozen.get('fixed_supported_unit_seed_model')
                or canonical(seed) != frozen.get('fixed_supported_unit_seed_identity_sha256')
                or seed != model.get('fixed_supported_unit_seed_model')
                or canonical(seed) != model.get('fixed_supported_unit_seed_identity_sha256')
                or seed['complete_axisymmetric_reference_model'] != problem.context.model
                or seed['initial_reference_bundle_sha256'] != base['initial_reference_bundle_sha256']
                or seed['fixed_chart_core_sha256'] != array_sha(problem.parent_core)
                or seed['fixed_scalar_profile_definition'] != problem.context.scalar_definition
                or seed['fixed_scalar_metric_identity_sha256'] != problem.context.scalar_identity
                or base['fixed_supported_unit_seed_working_definition'] != seed['working_definition']
                or seed['exact_relative_support_intervals'] !=
                    [[str(row[0]), str(row[2])] for row in problem.bubble_nodes]
                or model.get('fixed_supported_unit_reference_not_rebuilt_from_current_outer_point') is not True
                or model.get('supported_seed_mean_inverse_not_inherited_as_normal_control_inverse') is not True):
            raise ValueError('Bind the complete fixed supported reference, its original input, full working rule and actual current normal map')
        policy = model.get('normal_frame_C1_reuse')
        if (not isinstance(policy,dict) or policy != problem.frame_c1.definition
                or policy.get('source_sha256') != 'fbe2f08578c6ea21c1e481e8f37b9ff973838e841329e20d87fa53753def96aa'
                or policy.get('original_normal_stages_and_implicit_matrices_retained') is not True
                or policy.get('original_stage_primal_frame_anchors_required') is not True
                or policy.get('complete_second_outer_parameter_derivative_supported') is not False):
            raise ValueError('The C1 cache must retain all stages, anchors and original free-point transposes')
        matrices = problem.stage_matrices
        matrix_policy = model.get('detached_stage_matrix_reuse')
        if (not isinstance(matrix_policy,dict) or matrix_policy != matrices.definition
                or matrix_policy.get('source_sha256') != STAGE_MATRIX_SOURCE_SHA256
                or sha(matrices.__init__.__func__.__code__.co_filename) != STAGE_MATRIX_SOURCE_SHA256
                or matrices.q is not problem or matrices.model_identity_sha256 != problem.identity
                or matrices.actual_operator_source_sha256 != ENDPOINT_SOURCE_SHA256
                or matrices.actual_calibration_source_sha256 != REFERENCE_CENTERING_SOURCE_SHA256
                or matrix_policy.get('original_Newton_matrix_evaluations_unchanged') is not True
                or matrix_policy.get('original_stage_equations_domain_solves_and_trace_retained') is not True
                or matrix_policy.get('original_active_residual_and_full_upstream_parameter_chain_retained') is not True
                or matrix_policy.get('matrices_shared_between_calls_or_points_or_batches') is not False
                or matrix_policy.get('active_input_graphs_accepted') is not False):
            raise ValueError('Detached matrix reuse cannot replace original stages or the complete active field chain')
        adjacent=problem.adjacent_frames
        if (adjacent.q is not problem or adjacent.model_identity!=problem.identity
                or adjacent.operator_source!=ENDPOINT_SOURCE_SHA256
                or model.get('adjacent_normal_frame_matrices')!=adjacent.definition
                or adjacent.definition.get('source_sha256')!=ADJACENT_FRAME_SOURCE_SHA256
                or sha(adjacent.__init__.__func__.__code__.co_filename)!=ADJACENT_FRAME_SOURCE_SHA256
                or adjacent.definition.get('all_selected_stage_equations_roots_Newton_J3_and_angular_solves_retained') is not True
                or adjacent.definition.get('original_active_residual_and_all_upstream_parameter_edges_retained') is not True):
            raise ValueError('The adjacent-frame producer cannot replace roots, stages or the active field chain')
        self.operator_sha256 = model['source_sha256']
        if sha(problem.base.make_query.__code__.co_filename) != BASE_SOURCE_SHA256:
            raise ValueError('Historical grid queries require the actual complete base query maker')
        for name in ('grid_fields', 'point_fields', 'point_vjp', 'prepare', 'domain', 'fields_torch'):
            method = getattr(problem, name)
            path = Path(method.__code__.co_filename).resolve()
            if sha(path) != self.operator_sha256:
                raise ValueError('Actual new-field entry differs from its bound model: '+name)
        if canonical(model) != problem.identity:
            raise ValueError('The actual complete SO3 model identity differs')
        if (int(problem.K) != 3 or int(problem.core_size) != int(problem.M)-3
                or int(problem.free_size) != int(problem.core_size)+int(problem.rotation_size)+1):
            raise ValueError('Keep every free core coefficient, every rotation coordinate and final H')
        scripts = self.repo/'topics/visible-flex-larger-amplitude/scripts'
        self.pure = load_source(scripts/'resume_20261120_curvature_qp.py',
                                PURE_GEOMETRY_SHA256)
        self.selector = load_source(scripts/'resume_20261120/fullclosed_point_inequalities_v2.py',
                                    SELECTOR_SHA256)
        # The old selector's observed_module is passed only to our new point
        # shim. Its original physical field/point functions are never called.
        self.observed_marker = SimpleNamespace(
            schema='actual-new-SO3-world-point-shim-v1',
            operator_source_sha256=self.operator_sha256)
        self._curvature_memory = {}
        self._radius_memory = {}
        self._x = None
        self._prepared = None
        self._token = None
        self._field_cache = {}
        self._grid = None
        self._extra_grid = None
        self._extra_complete = False
        self._last_scan = None
        self._radial_index = {}
        for i, (cell, u) in enumerate(zip(problem.observation_cells, problem.observation_u)):
            self._radial_index.setdefault((int(cell), float(u).hex()), int(i))
        self._angle_index = {float(phi).hex(): int(i) for i, phi in enumerate(problem.phi)}
        if len(self._angle_index) != int(problem.N):
            raise ValueError('The actual angular observation carrier has duplicate literal angles')
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            material_envelope_memory_source_sha256=self.envelope_memory_source_sha256,
            material_envelope_rows_source_sha256=MATERIAL_ENVELOPE_ROWS_SHA256,
            material_envelope_definition_identity_sha256=self.envelope.identity,
            complete_old_current_grid_union=True,unknown_historical_protected_order_reconstructed=False,
            operator_source_sha256=self.operator_sha256,
            detached_closure_value_source_sha256=CLOSURE_VALUE_SOURCE_SHA256,
            detached_closure_value_definition=closure_policy,
            all_stage_final_and_chain_final_closures_reintegrated=True,
            active_parameter_derivatives_bypass_closure_value_cache=True,
            reference_centering_source_sha256=REFERENCE_CENTERING_SOURCE_SHA256,
            reference_centering_definition=definition,
            complete_current_raw_closure_lift_and_all_derivatives_read=True,
            working_radial_Gram_identity_claimed=False,
            fixed_supported_unit_seed_identity_sha256=canonical(seed),
            fixed_supported_unit_seed_source_sha256=SEED_PROVIDER_SHA256,
            fixed_supported_unit_seed_mean_kernel_sha256=SEED_MEAN_SHA256,
            seed_mean_Jacobian_not_a_normal_control_inverse_certificate=True,
            frozen_moment_Q_definition_identity_sha256=problem.frozen_moment_identity,
            frozen_moment_Q_definition_schema=frozen['schema'],
            literal_Q_input_schema=literal_input_schema,
            new_reference_input_binding_source_sha256=literal_binder_sha,
            frozen_Q_binding_kind=('explicit-literal-parameters-for-new-reference' if new_literal_input
                                   else 'actual-historical-working-moment-input'),
            frozen_moment_Q_trace_report_sha256=(None if new_literal_input else frozen['trace_report_sha256']),
            current_reference_Q_is_newly_bound_literal_input=new_literal_input,
            new_reference_same_mathematical_g_claimed=(False if new_literal_input else None),
            current_working_moment_inverse_claimed=False,
            historical_trace_is_only_provenance_for_new_literal_input=new_literal_input,
            exact_relative_gamma_nodes=gamma_words,
            implicit_control_dimension=6, normal_increment_dimension=3,
            implicit_dimension_per_stage=9,
            complete_first_angular_implicit_dimension=6*normal_steps,
            complete_second_angular_implicit_dimension=9*normal_steps,
            exact_normal_step_nodes=normal_words, normal_stage_count=normal_steps,
            normal_partition_shared_by_all_angles_and_current_points=True,
            internal_normal_step_roots_are_not_added_to_outer_free_point=True,
            all_original_free_point_coordinates_retained=True,
            stationary_KKT_selection_used=False,
            complete_interstage_parameter_and_second_angular_derivatives_required=True,
            rank_of_each_endpoint_A_is_not_by_itself_a_finite_step_inverse_certificate=True,
            numerical_moment_inverse_not_a_continuous_root_certificate=True,
            endpoint_root_and_quadrature_errors_certified=False,
            exact_implicit_branch_existence_certified=False,
            base_complete_model_identity_sha256=model['base_model_identity_sha256'],
            derived_from_complete_geometry_sha256=DERIVED_FROM_COMPLETE_GEOMETRY_SHA256,
            actual_model_identity_sha256=problem.identity,
            pure_curvature_source_sha256=PURE_GEOMETRY_SHA256,
            unchanged_original_selector_sha256=SELECTOR_SHA256,
            physical_pullback='actual new normal-lift SO3 point_vjp in world coordinates, through every sequential root/angle-jet and preceding normal-plane derivative',
            old_R671_point_pullback_used=False, old_geometry_certificate_inherited=False,
            budgets=budgets.metadata(), reach_ratio=self.reach_ratio,
            numerical_reach_safety_factor=self.safety,
            quarter_completion='declared polar-z/axial-v literal-Q/gamma reflection and half-turn covariance; each fixed normal stage must select the corresponding consistent branch and axis jets, both witness signs are actually read',
            lower_half_completion='z reflection; absolute curvature, radius and distances to the equatorial witness are invariant',
            scientific_evaluation_environment='public repository Actions',
            coordinate_semantics='cell/u on the unchanged symbolic radial mesh; phi is the NEW fixed-parent chart coordinate phi0',
            historical_angle_reinterpretation='every literal legacy normal-angle value is read as new phi0; no claim of the same physical point across representations',
            historical_physical_values_or_certificates_transferred=False,
            current_normal_angle='operator solves Theta_current(phi_c)=Theta_frozen_parent(phi0); all free core derivatives retained, root errors not certified')

    def _set_x(self, x):
        require_actions()
        x = np.asarray(x, dtype=float)
        if x.shape != (self.q.free_size,) or not np.isfinite(x).all():
            raise ValueError('Use the actual finite complete new-field point')
        if self._x is not None and np.array_equal(x, self._x):
            return
        prepared = self.q.prepare(x)
        if (np.asarray(prepared.core).shape != (self.q.M,)
                or not np.array_equal(prepared.core[self.q.K:], x[:self.q.core_size])
                or float(prepared.height) != float(x[-1])):
            raise ValueError('Current core and H do not match the complete new-field point')
        self._x = x.copy()
        self._prepared = prepared
        self._token = array_sha(x)
        self._field_cache = {}
        self._grid = None
        self._extra_grid = None
        self._extra_complete = False
        self._last_scan = None

    def _location(self, value):
        if 'cell' in value:
            cell, u, phi = int(value['cell']), float(value['u']), float(value['phi'])
        else:
            stage, angle = int(value['stage']), int(value['angle'])
            if not 0 <= stage < self.q.P or not 0 <= angle < self.q.N:
                raise ValueError('A requested grid location is outside the actual observation carrier')
            cell, u = int(self.q.observation_cells[stage]), float(self.q.observation_u[stage])
            phi = float(self.q.phi[angle])
        if (not 0 <= cell < self.q.J-1 or not 0 <= u <= 1
                or not math.isfinite(u) or not math.isfinite(phi)):
            raise ValueError('Use an actual same-mesh literal binary64 location')
        return dict(cell=cell, u=u, phi=phi, protected=bool(value.get('protected', False)))

    def _remember(self, values, memory):
        for value in values:
            item = self._location(value)
            key = _key(item)
            if key in memory:
                memory[key]['protected'] = bool(memory[key].get('protected', False)
                                                or item.get('protected', False))
            else:
                memory[key] = item

    def _grid_location(self, stage, angle, **metadata):
        result = self._location(dict(stage=int(stage), angle=int(angle)))
        result.update(stage=int(stage), angle=int(angle),
                      s=float(self.q.times[int(stage)]))
        result.update(metadata)
        return result

    def _validate_fields(self, fields, shape):
        if (not set(KEYS).issubset(fields)
                or set(fields)-set(KEYS)-{'rho0', 'closure_delta', 'centered_closure_residual'}):
            raise ValueError('Every new world field query must return the complete six jets')
        # grid_fields also reports its true chart and closure diagnostics.
        # They are checked, but are not mistaken for physical six-jet slots.
        for name in set(fields)-set(KEYS):
            extra = np.asarray(fields[name], dtype=float)
            expected = ((shape[-2],) if name == 'rho0' else (shape[-2], 3))
            if len(shape) != 3 or extra.shape != expected or not np.isfinite(extra).all():
                raise FloatingPointError('Invalid complete-field diagnostic: '+name)
        result = {}
        for name in KEYS:
            value = np.asarray(fields[name], dtype=float)
            if value.shape != shape or not np.isfinite(value).all():
                raise FloatingPointError('Nonfinite or incomplete actual world six-jet: '+name)
            result[name] = value
        return result

    def _point(self, location):
        item = self._location(location)
        key = _key(item)
        if key not in self._field_cache:
            fields = self.q.point_fields(self._x, item['cell'], item['u'], item['phi'])
            fields = self._validate_fields(fields, (3,))
            self._field_cache[key] = {name: value.copy() for name, value in fields.items()}
        return self._field_cache[key]

    def _point_geometry(self, fields):
        V, W = fields['Fs'], fields['Fphi']
        area = float(np.linalg.norm(np.cross(V, W)))
        if not math.isfinite(area) or area <= 0:
            raise FloatingPointError('An actually requested point has nonpositive tangent area')
        values = [self.pure.curvature_cotangent(fields, branch)[0] for branch in (0, 1)]
        radius = float(np.linalg.norm(fields['F']))
        if not np.isfinite(values).all() or not math.isfinite(radius):
            raise FloatingPointError('Nonfinite actual point curvature or radius')
        return values, radius, area

    def _amplitude_values(self, fields):
        F = fields['F']
        B, L = self.budgets.body_diameter_budget, self.budgets.witness_lower_budget
        r0 = 1.+np.sum(self._prepared.core)
        if not np.isfinite(r0):
            raise FloatingPointError('The complete current witness radius is not finite')
        squared = np.sum(F*F, axis=-1)
        result = {'body_diameter': 4*squared/(B*B)-1}
        for sign, name in ((1, 'distance_plus'), (-1, 'distance_minus')):
            delta = np.array(F, copy=True)
            delta[..., 1] -= sign*r0
            result[name] = 1-np.sum(delta*delta, axis=-1)/(L*L)
        if any(not np.isfinite(value).all() for value in result.values()):
            raise FloatingPointError('Nonfinite true same-field amplitude values')
        return result

    def _scalar_values(self):
        H = float(self._prepared.height)
        B, L = self.budgets.body_diameter_budget, self.budgets.witness_lower_budget
        result = dict(cap_diameter=4*(self.q.R*self.q.R+H*H)/(B*B)-1,
                      height_floor=(self.budgets.effective_height_floor-H)/L)
        if not np.isfinite(list(result.values())).all():
            raise FloatingPointError('Nonfinite same-field scalar amplitude values')
        return result

    @staticmethod
    def _offer(pool, location, score, count, **data):
        key = _key(location)
        item = dict(location=location, score=float(score), **data)
        if key not in pool or item['score'] > pool[key]['score']:
            pool[key] = item
        if len(pool) > count:
            kept = sorted(pool, key=lambda k: pool[k]['score'], reverse=True)[:count]
            for old in tuple(pool):
                if old not in kept:
                    del pool[old]

    def _block_candidates(self, values, begin, count):
        # All values have already participated in the full finite maximum.
        # Adaptive top selection affects only the bounded linear working set.
        flat = np.asarray(values).ravel()
        take = min(len(flat), max(64, 8*count))
        while True:
            indices = np.argpartition(flat, len(flat)-take)[-take:]
            indices = indices[np.argsort(flat[indices])[::-1]]
            output, keys = [], set()
            for index in indices:
                stage, local_angle = np.unravel_index(int(index), values.shape)
                location = self._grid_location(stage, begin+local_angle)
                key = _key(location)
                if key not in keys:
                    keys.add(key)
                    output.append((location, float(flat[index]), int(stage), int(local_angle)))
                    if len(output) == count:
                        return output
            if take == len(flat):
                return output
            take = min(len(flat), 2*take)

    def _envelope_extra_fields(self):
        q = self.q
        if not self.envelope.extra_cells:
            return
        query = q.base.make_query(self.envelope.extra_cells,self.envelope.extra_u)
        with torch.no_grad():
            xt = torch.as_tensor(self._x,dtype=torch.float64,device='cpu')
            for begin,end in q._blocks():
                values = q.fields_torch(xt,query,q.phi[begin:end],curvature=True,
                    query_label='complete_historical_material_envelope')
                yield begin,end,{key:value.cpu().numpy() for key,value in values.items()}

    def _envelope_location(self, radial, angle, historical=False, **metadata):
        if not historical:
            return self._grid_location(radial,angle,**metadata)
        result = dict(cell=int(self.envelope.extra_cells[radial]),
            u=float(self.envelope.extra_u[radial]),phi=float(self.q.phi[angle]),
            protected=False,historical_envelope_grid=True)
        result.update(metadata)
        return result

    def _collect_complete_grid(self,cells,local,iterator,*,historical):
        q = self.q
        count = len(cells)
        if count == 0:
            raise ValueError('Empty grids are handled explicitly without fabricated extrema')
        kappas,radii = np.empty((count,q.N,2)),np.empty((count,q.N))
        covered = np.zeros(q.N,dtype=bool)
        radius_pool,distance_pool = {},{}
        maxima = {key:-math.inf for key in ('body_diameter','distance_plus','distance_minus')}
        worst_by_family = {}
        minimum_area = math.inf
        radial_index = {}
        for index,(cell,u) in enumerate(zip(cells,local)):
            radial_index.setdefault((int(cell),float(u).hex()),index)
        needed = {}
        for item in list(self._curvature_memory.values())+list(self._radius_memory.values()):
            radial = radial_index.get((item['cell'],float(item['u']).hex()))
            angle = self._angle_index.get(float(item['phi']).hex())
            if radial is not None and angle is not None:
                needed.setdefault(angle,[]).append((radial,_key(item)))
        blocks = 0
        for begin,end,supplied in iterator:
            begin,end = int(begin),int(end)
            if not 0 <= begin < end <= q.N or np.any(covered[begin:end]):
                raise ValueError('An actual complete material angular block overlaps or is invalid')
            z = self._validate_fields(supplied,(count,end-begin,3))
            V,W = z['Fs'],z['Fphi']
            cross = np.cross(V,W)
            area = np.sqrt(np.sum(cross*cross,axis=-1))
            if not np.isfinite(area).all() or np.any(area<=0):
                raise FloatingPointError('A material envelope point has nonpositive or nonfinite tangent area')
            minimum_area = min(minimum_area,float(np.min(area)))
            normal = cross/area[...,None]
            E,F,G = np.sum(V*V,axis=-1),np.sum(V*W,axis=-1),np.sum(W*W,axis=-1)
            e = np.sum(normal*z['Fss'],axis=-1)
            f = np.sum(normal*z['Fsphi'],axis=-1)
            g = np.sum(normal*z['Fphiphi'],axis=-1)
            determinant = area*area
            trace = (e*G+g*E-2*f*F)/determinant
            gauss = (e*g-f*f)/determinant
            gap = np.sqrt(np.maximum(0.,trace*trace-4*gauss))
            block_k = np.stack(((trace-gap)/2,(trace+gap)/2),axis=-1)
            block_r = np.sqrt(np.sum(z['F']*z['F'],axis=-1))
            if not np.isfinite(block_k).all() or not np.isfinite(block_r).all():
                raise FloatingPointError('A complete envelope curvature/radius is nonfinite')
            kappas[:,begin:end] = block_k
            radii[:,begin:end] = block_r
            amplitude = self._amplitude_values(z)
            for family in maxima:
                values = amplitude[family]
                radial,angle = tuple(int(v) for v in np.unravel_index(np.argmax(values),values.shape))
                maximum = float(values[radial,angle])
                if maximum > maxima[family]:
                    maxima[family] = maximum
                    loc = self._envelope_location(radial,begin+angle,historical)
                    worst_by_family[family] = dict(location=loc,physical_g=maximum)
                    self._field_cache[_key(loc)] = {name:value[radial,angle].copy() for name,value in z.items()}
            paired = np.maximum(amplitude['distance_plus'],amplitude['distance_minus'])
            for family,values,keep,pool in (
                    ('body_diameter',amplitude['body_diameter'],self.amplitude_top_radius,radius_pool),
                    ('witness_distance',paired,self.amplitude_top_distance,distance_pool)):
                flat = np.asarray(values).ravel()
                take = min(len(flat),max(64,8*keep))
                while True:
                    indices = np.argpartition(flat,len(flat)-take)[-take:]
                    indices = indices[np.argsort(flat[indices])[::-1]]
                    chosen,keys = [],set()
                    for index in indices:
                        radial,angle = tuple(int(v) for v in np.unravel_index(int(index),values.shape))
                        loc = self._envelope_location(radial,begin+angle,historical)
                        key = _key(loc)
                        if key not in keys:
                            keys.add(key)
                            chosen.append((loc,float(flat[index]),radial,angle))
                            if len(chosen)==keep:
                                break
                    if len(chosen)==keep or take==len(flat):
                        break
                    take = min(len(flat),2*take)
                for loc,score,radial,angle in chosen:
                    self._offer(pool,loc,score,keep,kind=family)
                    self._field_cache[_key(loc)] = {name:value[radial,angle].copy() for name,value in z.items()}
            for angle in range(begin,end):
                for radial,key in needed.get(angle,()):
                    self._field_cache[key] = {name:value[radial,angle-begin].copy() for name,value in z.items()}
            covered[begin:end] = True
            blocks += 1
        if not covered.all():
            raise ValueError('The complete material envelope angular coverage is incomplete')
        worst = tuple(int(v) for v in np.unravel_index(np.argmax(np.abs(kappas)),kappas.shape))
        farthest = tuple(int(v) for v in np.unravel_index(np.argmax(radii),radii.shape))
        K,radius = float(abs(kappas[worst])),float(radii[farthest])
        diameter = max(2.,2*abs(float(self._prepared.height)),2*radius)
        summary = dict(complete=True,maximum_absolute_principal_curvature=K,maximum_radius=radius,
            diameter_point_lower=diameter,necessary_reach_product=self.reach_ratio*diameter*K,
            min_area=minimum_area,worst=self._envelope_location(*worst[:2],historical,branch=worst[2]),
            farthest=self._envelope_location(*farthest,historical),point_count=count*q.N,
            observed_stages=count,angular_orbits=q.N,angular_blocks=blocks,
            every_requested_grid_point_read=True,angular_coverage_complete=True,
            historical_extra_grid=historical,continuous_geometry_certified=False)
        return dict(kappas=kappas,radii=radii,summary=summary,radius_pool=radius_pool,
            distance_pool=distance_pool,maximum_body_g=maxima['body_diameter'],
            maximum_plus_g=maxima['distance_plus'],maximum_minus_g=maxima['distance_minus'],
            worst_by_family=worst_by_family)

    def _ensure_grid(self):
        if self._grid is None:
            domain = self.q.domain(self._x)
            self._grid = self._collect_complete_grid(self.q.observation_cells,self.q.observation_u,
                self.q.grid_fields(self._x),historical=False)
            self._grid['summary']['domain'] = domain
        if self._extra_grid is None and self.envelope.extra_cells:
            self._extra_grid = self._collect_complete_grid(self.envelope.extra_cells,self.envelope.extra_u,
                self._envelope_extra_fields(),historical=True)
        self._extra_complete = self._extra_grid is not None or not self.envelope.extra_cells

    def envelope_grids(self):
        if self._grid is None or not self._extra_complete:
            raise ValueError('Every actual grid must be complete before row selection')
        result = [(self.q.observation_cells,self._grid['kappas'],
            lambda radial,angle:self._envelope_location(radial,angle,False))]
        if self._extra_grid is not None:
            result.append((self.envelope.extra_cells,self._extra_grid['kappas'],
                lambda radial,angle:self._envelope_location(radial,angle,True)))
        return result

    def _new_locations(self, supplied, memory):
        keys = {_key(self._location(value)) for value in supplied}
        # Also return protected upgrades, with no rounding or memory eviction.
        old_protected = {_key(self._location(value)) for value in supplied if value.get('protected', False)}
        return [dict(value) for key, value in memory.items()
                if key not in keys or (value.get('protected', False) and key not in old_protected)]

    def scan(self,x,witnesses=(),radius_witnesses=()):
        require_actions()
        witnesses,radius_witnesses = list(witnesses),list(radius_witnesses)
        self.envelope.admit_explicit(witnesses+radius_witnesses)
        self._remember(witnesses,self._curvature_memory)
        self._remember(radius_witnesses,self._radius_memory)
        current_complete=extra_complete=explicit_complete=False
        attempted=np.asarray(x,dtype=float)
        attempted_token=(array_sha(attempted) if attempted.shape==(self.q.free_size,)
            and np.isfinite(attempted).all() else None)
        try:
            self._set_x(x)
            self._ensure_grid()
            current_complete = self._grid is not None
            extra_complete = self._extra_complete
            grids = [(self._grid,False)]
            if self._extra_grid is not None:
                grids.append((self._extra_grid,True))
            K=radius=-math.inf
            minimum_area=math.inf
            worst=farthest=None
            maxima={key:-math.inf for key in ('body_diameter','distance_plus','distance_minus')}
            worst_by_family={}
            radius_pool,distance_pool={},{}
            for grid,historical in grids:
                curv=self.pure.pick_extremes(grid['kappas'],16,branches=True)
                radii=self.pure.pick_extremes(grid['radii'],2)
                self._remember([self._envelope_location(s,a,historical) for s,a,_ in curv]
                    +[grid['summary']['worst']],self._curvature_memory)
                self._remember([self._envelope_location(s,a,historical) for s,a in radii]
                    +[grid['summary']['farthest']],self._radius_memory)
                if grid['summary']['maximum_absolute_principal_curvature']>K:
                    K=float(grid['summary']['maximum_absolute_principal_curvature'])
                    worst=grid['summary']['worst']
                if grid['summary']['maximum_radius']>radius:
                    radius=float(grid['summary']['maximum_radius'])
                    farthest=grid['summary']['farthest']
                minimum_area=min(minimum_area,float(grid['summary']['min_area']))
                for family in maxima:
                    item=grid['worst_by_family'][family]
                    if item['physical_g']>maxima[family]:
                        maxima[family]=float(item['physical_g'])
                        worst_by_family[family]=dict(item)
                for pool,key,count in ((radius_pool,'radius_pool',self.amplitude_top_radius),
                                        (distance_pool,'distance_pool',self.amplitude_top_distance)):
                    for item in grid[key].values():
                        self._offer(pool,item['location'],item['score'],count,kind=item['kind'])
            self._remember([v['location'] for v in radius_pool.values()]
                +[v['location'] for v in distance_pool.values()]
                +[v['location'] for v in worst_by_family.values()],self._radius_memory)
            union=dict(self._curvature_memory)
            union.update(self._radius_memory)
            point_records=[]
            for location in union.values():
                if not self.envelope.contains(location):
                    raise ValueError('A physical location escaped its complete declared envelope')
                fields=self._point(location)
                values,point_radius,area=self._point_geometry(fields)
                branch=int(np.argmax(np.abs(values)))
                value=abs(float(values[branch]))
                if value>K:
                    K,worst=value,dict(location,branch=branch)
                if point_radius>radius:
                    radius,farthest=point_radius,dict(location)
                minimum_area=min(minimum_area,area)
                av=self._amplitude_values(fields)
                for family in maxima:
                    if float(av[family])>maxima[family]:
                        maxima[family]=float(av[family])
                        worst_by_family[family]=dict(location=dict(location),physical_g=float(av[family]))
                self._offer(radius_pool,location,av['body_diameter'],self.amplitude_top_radius,kind='body_diameter')
                self._offer(distance_pool,location,max(av['distance_plus'],av['distance_minus']),
                    self.amplitude_top_distance,kind='witness_distance')
                point_records.append(dict(location=location,signed_principal_curvatures=[float(v) for v in values],
                    radius=point_radius,area=area,amplitude={key:float(v) for key,v in av.items()}))
            explicit_complete=True
            self._remember([worst],self._curvature_memory)
            self._remember([farthest]+[v['location'] for v in radius_pool.values()]
                +[v['location'] for v in distance_pool.values()]
                +[v['location'] for v in worst_by_family.values()],self._radius_memory)
            diameter=max(2.,2*abs(float(self._prepared.height)),2*radius)
            product=self.reach_ratio*diameter*K
            scalar=self._scalar_values()
            maximum_g=max(product-self.safety,*maxima.values(),*scalar.values())
            if not math.isfinite(maximum_g):
                raise FloatingPointError('Nonfinite complete envelope inequality maximum')
            result=dict(schema=SCHEMA,complete=True,passed=bool(maximum_g<=0),
                current_full_point_sha256=self._token,actual_model_identity_sha256=self.q.identity,
                maximum_physical_g=float(maximum_g),maximum_absolute_principal_curvature=K,
                maximum_radius=radius,diameter_point_lower=diameter,necessary_reach_product=product,
                reach_physical_g=product-self.safety,min_area=minimum_area,worst=worst,farthest=farthest,
                current_height=float(self._prepared.height),current_witness_radius=float(1.+np.sum(self._prepared.core)),
                grid=self._grid['summary'],
                historical_extra_grid=None if self._extra_grid is None else self._extra_grid['summary'],
                permanent_unique_locations_read=len(union),permanent_curvature_locations=len(self._curvature_memory),
                permanent_radius_locations=len(self._radius_memory),
                all_permanent_curvature_and_radius_locations_read=True,all_six_world_jets_read=True,
                both_witness_signs_read_at_every_point=True,
                amplitude=dict(complete=True,**maxima,**scalar,worst_by_family=worst_by_family,
                    radius_working_candidates=sorted(radius_pool.values(),key=lambda v:-v['score']),
                    distance_working_candidates=sorted(distance_pool.values(),key=lambda v:-v['score']),
                    budgets=self.budgets.metadata()),
                new_curvature_locations=self._new_locations(witnesses,self._curvature_memory),
                new_radius_locations=self._new_locations(radius_witnesses,self._radius_memory),
                continuous_geometry_certified=False,continuous_metric_certified=False,
                rigorous_quadrature_or_root_errors_paid=False,old_continuous_certificates_inherited=False,
                source_binding=self.binding,permanent_point_records=point_records)
            result['material_envelope']=self.envelope.observe_scan(result,
                extra_complete=extra_complete,explicit_complete=explicit_complete,
                full_current_complete=current_complete)
            self._last_scan=result
            return result
        except (ValueError,ArithmeticError,OverflowError,np.linalg.LinAlgError) as error:
            current_complete=bool(self._grid is not None and self._token==attempted_token)
            extra_complete=bool(current_complete and self._extra_complete)
            self._grid=None
            self._extra_grid=None
            self._extra_complete=False
            self._last_scan=None
            result=dict(schema=SCHEMA,complete=False,passed=False,current_full_point_sha256=attempted_token,
                actual_model_identity_sha256=self.q.identity,maximum_physical_g=None,
                error_type=type(error).__name__,error=str(error),
                new_curvature_locations=self._new_locations(witnesses,self._curvature_memory),
                new_radius_locations=self._new_locations(radius_witnesses,self._radius_memory),
                all_permanent_curvature_and_radius_locations_read=False,
                continuous_geometry_certified=False,old_continuous_certificates_inherited=False)
            result['material_envelope']=self.envelope.observe_scan(result,
                extra_complete=extra_complete,explicit_complete=explicit_complete,
                full_current_complete=current_complete)
            return result

    # ----- Explicit NEW physical shims for the unchanged original selector.
    def scan_geometry(self, problem, x, *, top_curvature=16, top_radius=2):
        if problem is not self.q:
            raise ValueError('Original selector received a different physical problem')
        self._set_x(x)
        self._ensure_grid()
        return (dict(self._grid['summary']),
            self.pure.pick_extremes(self._grid['kappas'], top_curvature, branches=True),
            self.pure.pick_extremes(self._grid['radii'], top_radius))

    def single_fields(self, problem, prepared, stage, angle):
        self._check_prepared(problem, prepared)
        return self._point(self._grid_location(stage, angle))

    def curvature_cotangent(self, fields, branch):
        return self.pure.curvature_cotangent(fields, branch)

    def _check_prepared(self, problem, prepared):
        if problem is not self.q or not np.array_equal(prepared.x, self._x):
            raise ValueError('A point query or covector crossed the actual same-parent boundary')

    def fields_at(self, problem, prepared, cell, u, phi, observed_module):
        self._check_prepared(problem, prepared)
        if observed_module is not self.observed_marker:
            raise ValueError('Use the explicit new world-point shim')
        return self._point(dict(cell=cell, u=u, phi=phi))

    def pullback(self, problem, prepared, stage, angle, cotangent):
        self._check_prepared(problem, prepared)
        location = self._grid_location(stage, angle)
        return self._pullback(location, cotangent)

    def pullback_at(self, problem, prepared, cell, u, phi, cotangent, observed_module):
        self._check_prepared(problem, prepared)
        if observed_module is not self.observed_marker:
            raise ValueError('Use the explicit new world-point shim')
        return self._pullback(dict(cell=cell, u=u, phi=phi), cotangent)

    def _pullback(self, location, cotangent):
        item = self._location(location)
        cotangent = self._validate_fields(cotangent, (3,))
        gradient = np.asarray(self.q.point_vjp(self._x, item['cell'], item['u'], item['phi'],
                                             cotangent), dtype=float)
        if gradient.shape != (self.q.free_size,) or not np.isfinite(gradient).all():
            raise FloatingPointError('The new world pullback omitted a free variable or is nonfinite')
        return gradient

    def _amplitude_row(self, kind, location=None, sign=None):
        gradient = np.zeros(self.q.free_size)
        B, L = self.budgets.body_diameter_budget, self.budgets.witness_lower_budget
        if kind in ('cap_diameter', 'height_floor'):
            value = self._scalar_values()[kind]
            gradient[-1] = (8*self._prepared.height/(B*B) if kind == 'cap_diameter' else -1/L)
            return float(value), gradient, dict(kind=kind, only_final_height_coordinate=True,
                fixed_cap_radius_has_no_free_derivative=True)
        location = self._location(location)
        fields = self._point(location)
        F = fields['F']
        cot = {name: np.zeros(3) for name in KEYS}
        values = self._amplitude_values(fields)
        if kind == 'body_diameter':
            value = float(values[kind])
            cot['F'] = 8*F/(B*B)
            gradient = self._pullback(location, cot)
        elif kind == 'witness_distance':
            if sign not in (-1, 1):
                raise ValueError('A distance derivative must keep its actual witness sign')
            w = F.copy()
            w[1] -= sign*(1.+np.sum(self._prepared.core))
            value = float(values['distance_plus' if sign == 1 else 'distance_minus'])
            cot['F'] = -2*w/(L*L)
            gradient = self._pullback(location, cot)
            # p=(0,1+sum ALL current core coefficients,0) in WORLD coordinates.
            # Every original FREE core entry changes p_y by one. This term is
            # added before the full H2 coordinate transpose, never after it.
            gradient[:self.q.core_size] += 2*sign*w[1]/(L*L)
        else:
            raise ValueError('Unknown actual amplitude inequality')
        return value, gradient, dict(kind=kind, location=location, sign=sign,
            witness_formula='p=(0,1+sum_all_current_core,0)',
            full_free_core_witness_derivative_added=(kind == 'witness_distance'),
            witness_derivative_added_before_coordinate_transpose=True)

    def build_rows(self, x, transpose, coordinate_size, *, witnesses=(),
                   radius_witnesses=(), current_geometry=None, matrix_workdir=None,
                   max_rows=192, active_band=.025, block_columns=32768):
        require_actions()
        if int(coordinate_size) != coordinate_size or coordinate_size != self.q.free_size:
            raise ValueError('Retain all full SO3 H2 coordinates in every selected row')
        if int(max_rows) != 192:
            raise ValueError('The complete original selector must keep its declared 192-row cap')
        if not math.isfinite(float(active_band)) or active_band <= 0:
            raise ValueError('Use a positive declared linear working-set activity band')
        if int(block_columns) != block_columns or block_columns <= 0:
            raise ValueError('Use a positive streamed column block size')
        self._set_x(x)
        if current_geometry is not None:
            if (current_geometry.get('current_full_point_sha256') != self._token
                    or current_geometry.get('actual_model_identity_sha256') != self.q.identity):
                raise ValueError('The supplied true scan belongs to a different complete parent')
        actual = self.scan(x, witnesses, radius_witnesses)
        if not actual['complete']:
            raise ValueError('A singular or incomplete current world field cannot define rows: '
                             +actual.get('error', 'unknown actual failure'))
        if matrix_workdir is None:
            raise ValueError('An explicit outside-repository runner scratch cache is required')
        directory = Path(matrix_workdir).resolve()
        if directory == self.repo or self.repo in directory.parents:
            raise ValueError('Scientific row caches must stay outside the repository')
        directory.mkdir(parents=True, exist_ok=False)
        original, bounds, prefix = self.selector.build_inequality_rows(
            self.q, self._x, self, self, transpose, coordinate_size,
            reach_ratio=self.reach_ratio, safety=self.safety, active_band=active_band,
            max_rows=192, top_curvature=16, top_radius=2,
            witnesses=list(self._curvature_memory.values()),
            radius_witnesses=list(self._radius_memory.values()),
            observed_module=self.observed_marker,
            matrix_workdir=directory/'original-192', block_columns=block_columns)
        prefix_rows = int(original.shape[0])
        selections = []
        for kind, key in (('body_diameter', 'radius_working_candidates'),
                          ('witness_distance', 'distance_working_candidates')):
            for index, item in enumerate(actual['amplitude'][key]):
                if index and item['score'] < -active_band:
                    continue
                if kind == 'body_diameter':
                    selections.append((kind, item['location'], None))
                else:
                    # The selected physical location always carries BOTH
                    # reflection branches, irrespective of which is active.
                    selections.extend((kind, item['location'], sign) for sign in (-1, 1))
        selections.extend((kind, None, None) for kind in ('cap_diameter', 'height_floor'))
        if len(selections) > 12:
            raise ValueError('The declared bounded amplitude working set unexpectedly expanded')
        total = prefix_rows+len(selections)
        path = Path(prefix['row_cache'])
        prefix_bytes = prefix_rows*coordinate_size*np.dtype(np.float64).itemsize
        if isinstance(original, np.memmap):
            original.flush()
            original._mmap.close()
        del original
        if prefix_rows and (not path.exists() or path.stat().st_size != prefix_bytes):
            raise ValueError('The complete original selected-row prefix byte length changed')
        # Extend the SAME cache. No prefix row is rewritten, no second 2GB
        # cache is created, and no scientific row is moved into git.
        with path.open('r+b' if path.exists() else 'w+b') as stream:
            stream.truncate(total*coordinate_size*np.dtype(np.float64).itemsize)
        matrix = np.memmap(path, dtype=np.float64, mode='r+', shape=(total, coordinate_size))
        result_bounds = np.empty(total)
        result_bounds[:prefix_rows] = bounds
        row_metadata = []
        for old in prefix['rows']:
            row = dict(old)
            row.update(kind='necessary_reach_product',
                physical_g=float(old['current_product'])-self.safety,
                upper_bound=self.safety,
                physical_current_value=float(old['current_product']),
                row_normalization_scale=float(old['gradient_coordinate_norm']),
                original_prefix_row=True)
            row_metadata.append(row)
        for offset, (kind, location, sign) in enumerate(selections):
            value, free_gradient, extra = self._amplitude_row(kind, location, sign)
            coordinate_gradient = np.asarray(transpose(free_gradient), dtype=float)
            if coordinate_gradient.shape != (coordinate_size,) or not np.isfinite(coordinate_gradient).all():
                raise FloatingPointError('The full H2 coordinate transpose is incomplete or nonfinite')
            norm = float(np.linalg.norm(coordinate_gradient))
            if not math.isfinite(norm):
                raise FloatingPointError('Nonfinite full-coordinate amplitude gradient norm')
            scale = norm if norm > 0 else 1.
            index = prefix_rows+offset
            matrix[index] = coordinate_gradient/scale
            result_bounds[index] = -value/scale
            row_metadata.append(dict(index=index, **extra, physical_g=value,
                physical_current_value=value, upper_bound=0.,
                current_product=None, gradient_coordinate_norm=norm,
                row_normalization_scale=scale, zero_gradient_row_retained=bool(norm == 0),
                normalized_bound=float(result_bounds[index]), original_prefix_row=False))
            matrix.flush()
            _discard(matrix)
        if len(row_metadata) != total or not np.isfinite(result_bounds).all():
            raise FloatingPointError('The complete typed selected-row metadata is inconsistent')
        matrix.flush()
        _discard(matrix)
        metadata = dict(schema=SCHEMA, source_binding=self.binding,
            selected_rows=total, original_prefix_rows=prefix_rows,
            appended_amplitude_rows=len(selections), no_original_row_removed=True,
            original_prefix_rewritten=False, original_selector_source_sha256=SELECTOR_SHA256,
            original_selection_metadata=prefix, rows=row_metadata,
            row_cache=str(path), row_cache_bytes=total*coordinate_size*8,
            row_cache_allocated_bytes=int(path.stat().st_blocks*512),
            original_prefix_bytes=prefix_bytes, duplicate_prefix_cache_bytes=0,
            shared_cache_extended_in_place=True, block_columns=int(block_columns),
            original_variables=int(self.q.free_size), coordinate_size=int(coordinate_size),
            physical_g_formula='current physical value minus its own upper bound',
            normalized_row_formula='C=dg[T]/positive_scale; b=-physical_g/positive_scale',
            common_slack_formula='dg[Tz]-delta_tau <= tau0-physical_g for EVERY typed row',
            zero_gradient_amplitude_rows_retained=True,
            all_original_field_variables_retained=True,
            current_full_point_sha256=self._token,
            current_geometry=actual, numerical_reach_safety_factor=self.safety,
            permanent_curvature_locations=len(self._curvature_memory),
            permanent_radius_locations=len(self._radius_memory),
            nonlinear_memory_has_no_eviction_or_working_row_cap=True,
            no_feasibility_inferred_from_linear_model=True,
            continuous_geometry_certified=False,
            scope='Full finite NEW-field world geometry, unchanged original 192 selection, plus bounded actual amplitude rows; true whole-grid/permanent-point scans decide nonlinear acceptance')
        return self.envelope_rows.append_rows(self,matrix,result_bounds,metadata,transpose,coordinate_size,
            active_band=active_band,block_columns=block_columns)
