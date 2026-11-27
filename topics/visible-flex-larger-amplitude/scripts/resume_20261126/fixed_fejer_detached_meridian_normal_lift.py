#!/usr/bin/env python3
"""Complete R715 reference-centred R711 normal-plane field.

All original variables, 32-stage default, full implicit chains and true Gram
rows remain. Every closure/target angular jet subtracts the SAME frozen
reference. Physical sixjets include the complete CURRENT closure lift.
The accurate unit-speed equivalence is conditional on exact reference and
normal roots; the working lifted radial Gram is always really evaluated.
All scientific execution remains public Actions only.
"""
from dataclasses import dataclass
from contextlib import nullcontext
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np
import torch


SCHEMA = 'complete-fixed-fejer-detached-meridian-values-normal-layer-v1'
ANALYTIC_STAGE_SOURCE_SHA256 = '223afb992e0e9904c30ab20387a92569dc2979dbfde84f75f04e3402b9c5e811'
ANALYTIC_FRAME_SOURCE_SHA256 = 'd3cf01067c0c3cd348560a74d1845b02f859bbd0a41f2938ec544034d2a63bcd'
FROZEN_MOMENT_INPUT_SCHEMA = 'frozen-zero-endpoint-moment-Q-input-v1'
FROZEN_MOMENT_DEFINITION_SCHEMA = 'literal-two-bubble-endpoint-Q-v1'
ORIGINAL_COMPLETE_ENDPOINT_SOURCE_SHA256 = '5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46'
ACTUAL_TRACE_REPORT_SHA256 = '26b094fef8baf6ff2ecdda5d1a0f5a8be7383e5171733320be959a22d83cb47e'
ACTUAL_TRACE_SOURCE_SHA256 = '73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54'
ACTUAL_TRACE_ORIGINAL_MODEL_IDENTITY_SHA256 = '29f540c6fc265b977a388813dcd0d3faddfd48fd06d40c7f6c4bcae5c848281b'
ACTUAL_TRACE_INITIAL_FULL_POINT_SHA256 = 'cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3'
TORCH_VERSION = '2.5.1'
DETACHED_CLOSURE_SOURCE_SHA256 = '2889fef0d09a32c3f609f9a4e100efb1b136070dad77c8104204b552a867c4e0'
NORMAL_DERIVED_FROM_SHA256 = 'b712a24a0c0223356b4a53e6aa1fa78ba9cea66e4be39c7ee39931be99cb782a'
MERIDIAN_VALUE_SOURCE_SHA256 = '7aa760baa30a46484d90bc5e327849ab5229cca708e6ba4289b12da253a5facd'
CONTROL_DIMENSION = 6
REFERENCE_CENTRED_FROM_SHA256 = '66e81e439a2545134549b4527e68a2480a9d8010679dcf9cfa23ca5e48c15d68'
REFERENCE_CENTERING_SOURCE_SHA256 = 'aa40b224da667b5e01b207a431f771e2bf11177fabaebb075ca6218bbb130de3'
NEW_REFERENCE_INPUT_SCHEMA = 'fixed-fejer-supported-reference-literal-zero-endpoint-Q-input-v1'
NEW_REFERENCE_INPUT_BINDER_SHA256 = 'ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3'
SUPPORTED_BASE_SCHEMA = 'complete-fixed-fejer-supported-smooth-triangle-so3-meridian-with-core-lift-v1'
SUPPORTED_BASE_SOURCE_SHA256 = '552f75dd138b81217f88155dab61446416a54510d3d947cc2bb1b3fde5b800b3'
SUPPORTED_SEED_SOURCE_SHA256 = 'ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a'
SUPPORTED_MEAN_SOURCE_SHA256 = 'f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917'
DERIVED_FROM_COMPLETE_NORMAL_SOURCE_SHA256 = '42ea8ec5920e3815b99c83c41448efb38ee37860f4d9362ddea6bce2418d39fe'
FRAME_C1_SOURCE_SHA256 = 'c97749c8fae14981a1f86e45845d152134a62039d88b7cfaccfb69fb0665e246'
STAGE_MATRIX_SOURCE_SHA256 = 'f98bf270265f9d41c9c297dd23c2db7da9ea91a039663c1785966e9135795791'
ADJACENT_FRAME_SOURCE_SHA256 = 'bd65734da69f3e5bc560ec81df03f8555593257560455b56adfa353e025c4564'
JET_KEYS = ('F', 'Fs', 'Fphi', 'Fss', 'Fsphi', 'Fphiphi')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific zero-closure SO3 fields require public repository Actions')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    digest = hashlib.sha256(str(value.dtype).encode())
    digest.update(json.dumps(list(value.shape)).encode())
    digest.update(value.tobytes())
    return digest.hexdigest()


def tensor(value):
    return torch.as_tensor(np.array(value, dtype=np.float64, copy=True),
                           dtype=torch.float64, device='cpu')


def hat(value):
    x, y, z = value.unbind(-1)
    zero = torch.zeros_like(x)
    return torch.stack((zero, -z, y, z, zero, -x, -y, x, zero), -1).reshape(
        value.shape[:-1]+(3, 3))


def cross(left, right):
    return torch.cross(left, right, dim=-1)



def validate_frozen_moment_input(value, base, bubble_nodes):
    """Validate the exact literal input and its same-reference provenance.

    The independently source-pinned outer input binder reads the ACTUAL
    26b report and verifies each of these eighteen hex words. Here the
    complete mathematical definition is checked again against this base.
    No numerical integral or inverse is evaluated or selected here.
    """
    if not isinstance(value, dict) or value.get('schema') != FROZEN_MOMENT_INPUT_SCHEMA:
        raise ValueError('Supply one complete independently bound literal moment-Q input')
    definition = json.loads(json.dumps(value.get('definition'), allow_nan=False))
    keys = {'schema', 'Q0_binary64_hex', 'exact_relative_bubble_nodes',
        'fixed_scalar_metric_identity_sha256', 'initial_reference_bundle_sha256',
        'base_model_identity_sha256', 'trace_report_sha256', 'trace_source_sha256',
        'trace_original_model_identity_sha256', 'trace_initial_full_point_sha256'}
    if (not isinstance(definition, dict) or set(definition) != keys
            or definition.get('schema') != FROZEN_MOMENT_DEFINITION_SCHEMA
            or canonical(definition) != value.get('definition_identity_sha256')):
        raise ValueError('Keep the complete exact frozen-Q definition and canonical identity')
    expected = dict(fixed_scalar_metric_identity_sha256=base.context.scalar_identity,
        initial_reference_bundle_sha256=base.model['initial_reference_bundle_sha256'],
        base_model_identity_sha256=base.identity,
        trace_report_sha256=ACTUAL_TRACE_REPORT_SHA256,
        trace_source_sha256=ACTUAL_TRACE_SOURCE_SHA256,
        trace_original_model_identity_sha256=ACTUAL_TRACE_ORIGINAL_MODEL_IDENTITY_SHA256,
        trace_initial_full_point_sha256=ACTUAL_TRACE_INITIAL_FULL_POINT_SHA256)
    for name, wanted in expected.items():
        if definition[name] != wanted:
            raise ValueError('The frozen moment input changed its complete actual binding: '+name)
    if array_sha(base.initial()) != ACTUAL_TRACE_INITIAL_FULL_POINT_SHA256:
        raise ValueError('The reference initial point differs from the actual working-moment input')
    relative = [[str(v) for v in row] for row in bubble_nodes]
    if definition['exact_relative_bubble_nodes'] != relative:
        raise ValueError('The literal matrices belong to these same complete wide bubble supports')
    words = definition['Q0_binary64_hex']
    if (not isinstance(words, list) or len(words) != 2
            or any(not isinstance(matrix, list) or len(matrix) != 3 for matrix in words)
            or any(not isinstance(row, list) or len(row) != 3
                   for matrix in words for row in matrix)):
        raise ValueError('Keep all eighteen literal two-by-three-by-three matrix words')
    matrices = np.empty((2, 3, 3), dtype=np.float64)
    for i in range(2):
        for j in range(3):
            for k in range(3):
                word = words[i][j][k]
                if not isinstance(word, str):
                    raise ValueError('Every frozen matrix entry must have an exact binary64 hex word')
                number = float.fromhex(word)
                if not math.isfinite(number) or number.hex() != word:
                    raise ValueError('Use each canonical finite binary64 matrix word without rounding')
                matrices[i,j,k] = number
    # The actual phi=0 axisymmetric construction has one tangential
    # input/output index in every allowed nonzero entry. This exact sparse
    # pattern proves reflection/half-turn covariance after Rz conjugation.
    # Do not replace a small nonzero entry by zero to pass the guard.
    forbidden = ((0,0), (0,2), (1,1), (2,0), (2,2))
    if any(matrices[i,j,k] != 0 for i in range(2) for j,k in forbidden):
        raise ValueError('The actual literal input does not preserve the declared full-circle parity')
    matrices.setflags(write=False)
    return definition, canonical(definition), matrices




def validate_control_input(value, base, bubble_nodes, new_input_binder):
    """Only the independent complete supported-seed input is accepted here."""
    if not isinstance(value, dict) or value.get('schema') != NEW_REFERENCE_INPUT_SCHEMA:
        raise ValueError('Use the complete supported-smooth-triangle seed literal input; original same-reference and ea94 types are not this field')
    if new_input_binder is None:
        raise ValueError('A NEW-reference input needs its actual independently pinned complete binder')
    if sha(Path(new_input_binder.__file__).resolve()) != NEW_REFERENCE_INPUT_BINDER_SHA256:
        raise ValueError('The complete NEW-reference input binder source differs')
    for name in ('bind_to_base', 'parse_literal_Q'):
        method = getattr(new_input_binder, name)
        if sha(Path(method.__code__.co_filename).resolve()) != NEW_REFERENCE_INPUT_BINDER_SHA256:
            raise ValueError('The actual NEW-reference input validation method differs: '+name)
    identity = new_input_binder.bind_to_base(value,
        base_model=base.model,
        initial_reference_bundle_sha256=base.model['initial_reference_bundle_sha256'],
        fixed_scalar_metric_identity_sha256=base.context.scalar_identity,
        initial_full_point_sha256=array_sha(base.initial()),
        bubble_nodes=[[str(v) for v in row] for row in bubble_nodes])
    words, parsed = new_input_binder.parse_literal_Q(value)
    definition = json.loads(json.dumps(value['definition'], allow_nan=False))
    if (canonical(definition) != identity
            or identity != value.get('definition_identity_sha256')
            or definition.get('Q0_binary64_hex') != words):
        raise ValueError('The NEW-reference exact definition or eighteen literal words changed')
    matrices = np.asarray(parsed, dtype=np.float64)
    if matrices.shape != (2,3,3) or not np.isfinite(matrices).all():
        raise ValueError('The actual adopted parameter matrices must contain all eighteen finite entries')
    if any(float(matrices[i,j,k]).hex() != words[i][j][k]
            for i in range(2) for j in range(3) for k in range(3)):
        raise ValueError('The actual parameter conversion changed a canonical binary64 word')
    forbidden = ((0,0), (0,2), (1,1), (2,0), (2,2))
    if any(matrices[i,j,k] != 0 for i in range(2) for j,k in forbidden):
        raise ValueError('The adopted literal constants must retain the proved full-circle sparse parity')
    matrices.setflags(write=False)
    return definition, identity, matrices


@dataclass(frozen=True)
class EndpointPolicy:
    endpoint_tolerance: float = 2.e-12
    maximum_iterations: int = 24
    maximum_backtracks: int = 18
    armijo: float = 1.e-4
    control_radius: float = 2.

    def __post_init__(self):
        for name in ('endpoint_tolerance', 'armijo', 'control_radius'):
            value = float(getattr(self, name))
            if not math.isfinite(value) or value <= 0:
                raise ValueError('Use finite positive normal-plane numerical parameters: '+name)
            object.__setattr__(self, name, value)
        if self.armijo >= 1:
            raise ValueError('The original residual decrease factor must be below one')
        for name in ('maximum_iterations', 'maximum_backtracks'):
            value = int(getattr(self, name))
            if value != getattr(self, name) or value < 1:
                raise ValueError('Use an explicit positive per-plane root budget: '+name)
            object.__setattr__(self, name, value)

    def metadata(self):
        return dict(schema='fixed-normal-plane-six-control-root-policy-v1',
            endpoint_tolerance=self.endpoint_tolerance,
            maximum_iterations=self.maximum_iterations,
            maximum_backtracks=self.maximum_backtracks, armijo=self.armijo,
            control_radius=self.control_radius,
            control='u=(z/S,v); every original and added gamma control',
            normal_increment='eta in R3; u_i=u_previous+A_previous^T eta',
            merit='Euclidean norm of the three dimensionless current-plane equations',
            stage_tolerance='endpoint_tolerance / actual S carrier',
            final_acceptance='fresh centred closure norm <= endpoint_tolerance and all declared open control domains',
            domain='|u_i| < control_radius at every stage and accepted Newton trial',
            normal_increment_radius_imposed=False,
            initial_root='literal eta=0 in each fixed normal plane, with the actual preceding control retained',
            failure='reject the candidate; no failed stage or jet is replaced by zero',
            stationary_KKT_selection_used=False,
            continuous_branch_certified=False, root_iteration_graph_differentiated=False)


class EndpointRootFailure(ValueError):
    pass


class ZeroClosureOperator:
    def __init__(self, base, *, expected_base_source_sha256, expected_base_schema,
                 bubble_nodes, frozen_moment_input, gamma_nodes=('1/16', '1/8', '3/16'),
                 endpoint_policy=None, normal_step_nodes=None, new_input_binder=None, reference_centering_module=None, frame_c1_module=None, stage_matrix_module=None, adjacent_matrix_module=None, analytic_stage_module=None, analytic_frame_module=None, closure_value_module=None, meridian_value_module=None, evaluation_progress_path=None):
        require_actions()
        if torch.__version__.split('+')[0] != TORCH_VERSION:
            raise ValueError('Use declared CPU PyTorch '+TORCH_VERSION)
        if (not isinstance(expected_base_source_sha256, str)
                or len(expected_base_source_sha256) != 64
                or any(c not in '0123456789abcdef' for c in expected_base_source_sha256)):
            raise ValueError('Pin the actual complete direct R690 base source')
        self.base = base
        if (expected_base_source_sha256 != SUPPORTED_BASE_SOURCE_SHA256
                or expected_base_schema != SUPPORTED_BASE_SCHEMA):
            raise ValueError('This complete normal layer binds its actual independent supported-smooth-triangle base source')
        seed = base.model.get('fixed_supported_unit_seed_model')
        if (not isinstance(seed, dict)
                or seed.get('schema') != 'complete-fixed-fejer-supported-smooth-triangle-meridian-seed-reference-v1'
                or seed.get('source_sha256') != SUPPORTED_SEED_SOURCE_SHA256
                or seed.get('mean_kernel_source_sha256') != SUPPORTED_MEAN_SOURCE_SHA256
                or canonical(seed) != base.model.get('fixed_supported_unit_seed_identity_sha256')
                or seed != base.parent_jet.model
                or base.parent_jet.model_identity != canonical(seed)):
            raise ValueError('The complete fixed supported seed and its numerical source differ')
        if (base.model.get('schema') != expected_base_schema
                or base.model.get('source_sha256') != expected_base_source_sha256
                or canonical(base.model) != base.identity):
            raise ValueError('The actual complete base model/source identity differs')
        for name in ('_unpack_torch', '_angular_nodes', '_radial', '_meridians',
                     '_integrate', 'prepare', 'unpack', 'make_query', '_parent_tensor', 'initial'):
            method = getattr(base, name)
            if sha(Path(method.__code__.co_filename).resolve()) != expected_base_source_sha256:
                raise ValueError('The direct base method differs from its actual source: '+name)
        rotation = base._meridians.__func__.__globals__['rotated_jets']
        self.rotation_coefficients = rotation.__globals__['rotation_coefficients']
        for function in (rotation, self.rotation_coefficients):
            if sha(Path(function.__code__.co_filename).resolve()) != expected_base_source_sha256:
                raise ValueError('Bind the actual complete base rotation evaluation')
        if (base.K != 3 or base.core_size != base.M-3
                or base.free_size != base.core_size+base.rotation_size+1
                or base.model.get('all_current_free_core_coefficients_retained') is not True
                or base.model.get('current_height_free') is not True):
            raise ValueError('Retain every original free core, full omega and final H coordinate')
        if (base.model.get('fixed_scalar_metric_identity_sha256')
                != base.context.scalar_identity
                or base.model.get('fixed_scalar_profile_definition')
                != base.context.scalar_definition
                or canonical(base.context.scalar_definition) != base.context.scalar_identity):
            raise ValueError('The new field must retain the SAME exact fixed R690 metric')
        if len(bubble_nodes) != 2 or any(len(row) != 3 for row in bubble_nodes):
            raise ValueError('Specify two full exact relative (left,middle,right) bubble triples')
        self.bubble_nodes = tuple(tuple(Fraction(value) for value in row) for row in bubble_nodes)
        for row in self.bubble_nodes:
            if not 0 < row[0] < row[1] < row[2] < 1:
                raise ValueError('Each C2 bubble must stay strictly inside the same exact radial domain')
        if self.bubble_nodes[0][2] >= self.bubble_nodes[1][0]:
            raise ValueError('The two declared frozen-moment bubbles must have disjoint supports')
        (self.frozen_moment_definition, self.frozen_moment_identity,
         frozen_matrices) = validate_control_input(frozen_moment_input, base, self.bubble_nodes, new_input_binder)
        self.literal_Q_input_schema = frozen_moment_input['schema']
        self.new_reference_input_binding_source_sha256 = (NEW_REFERENCE_INPUT_BINDER_SHA256
            if self.literal_Q_input_schema == NEW_REFERENCE_INPUT_SCHEMA else None)
        self._frozen_Q0 = tensor(frozen_matrices)
        self.gamma_nodes = tuple(Fraction(value) for value in gamma_nodes)
        if (len(self.gamma_nodes) != 3
                or not 0 < self.gamma_nodes[0] < self.gamma_nodes[1] < self.gamma_nodes[2] < 1):
            raise ValueError('Specify a complete strictly ordered exact relative gamma triple')
        if not any(row[0] < self.gamma_nodes[0] < self.gamma_nodes[2] < row[2]
                   for row in self.bubble_nodes):
            raise ValueError('The complete gamma support must lie strictly inside one original support')
        self._gamma_query_cache = {}
        if normal_step_nodes is None:
            normal_step_nodes = tuple(Fraction(i,32) for i in range(33))
        self.normal_step_nodes = tuple(Fraction(value) for value in normal_step_nodes)
        if (len(self.normal_step_nodes) < 2 or self.normal_step_nodes[0] != 0
                or self.normal_step_nodes[-1] != 1
                or any(a >= b for a,b in zip(self.normal_step_nodes, self.normal_step_nodes[1:]))):
            raise ValueError('Use one fixed common exact increasing normal-plane partition from zero to one')
        self.normal_stage_count = len(self.normal_step_nodes)-1
        carriers = tuple(float(value) for value in self.normal_step_nodes)
        if (any(not math.isfinite(v) for v in carriers)
                or any(a >= b for a,b in zip(carriers,carriers[1:]))):
            raise ValueError('The working node carriers must retain every declared normal stage distinctly')
        self.normal_step_carriers = carriers
        self.policy = EndpointPolicy() if endpoint_policy is None else endpoint_policy
        if not isinstance(self.policy, EndpointPolicy):
            raise TypeError('Use the independent immutable normal-plane EndpointPolicy')
        self.normal_counts = dict(closure_jet_angle_evaluations=0,
            frame_reverse_angle_products=0, stage_equation_angle_evaluations=0,
            stage_matrix_angle_evaluations=0, stage_angular_matrix_angle_evaluations=0,
            three_dimensional_solve_angle_attempts=0, implicit_solve_angle_attempts=0,
            actual_implicit_matrix_angle_rows=0, stage_root_angle_attempts=0,
            stage_root_angle_successes=0, stage_newton_angle_updates=0,
            stage_backtrack_angle_evaluations=0, failed_stage_angle_count=0,
            first_angular_solve_angle_attempts=0, second_angular_solve_angle_attempts=0)
        if (reference_centering_module is None
                or sha(reference_centering_module.__file__) != REFERENCE_CENTERING_SOURCE_SHA256
                or sha(reference_centering_module.FrozenReferenceCalibration.__init__.__code__.co_filename)
                    != REFERENCE_CENTERING_SOURCE_SHA256):
            raise ValueError('Bind the complete independent frozen-reference calibration helper')
        if (frame_c1_module is None or sha(frame_c1_module.__file__) != FRAME_C1_SOURCE_SHA256
                or sha(frame_c1_module.definition.__code__.co_filename) != FRAME_C1_SOURCE_SHA256
                or sha(frame_c1_module.NormalFrameC1Kernel.__init__.__code__.co_filename) != FRAME_C1_SOURCE_SHA256):
            raise ValueError('Bind the entire same-graph C1/frame-value helper source')
        if (stage_matrix_module is None
                or sha(stage_matrix_module.__file__) != STAGE_MATRIX_SOURCE_SHA256
                or sha(stage_matrix_module.definition.__code__.co_filename) != STAGE_MATRIX_SOURCE_SHA256
                or sha(stage_matrix_module.CompleteDetachedStageMatrices.__init__.__code__.co_filename)
                    != STAGE_MATRIX_SOURCE_SHA256):
            raise ValueError('Bind the complete independent detached stage-matrix helper')
        if (adjacent_matrix_module is None or sha(adjacent_matrix_module.__file__) != ADJACENT_FRAME_SOURCE_SHA256
                or sha(adjacent_matrix_module.AdjacentNormalFrameMatrices.__init__.__code__.co_filename)
                    != ADJACENT_FRAME_SOURCE_SHA256):
            raise ValueError('Bind the entire independent adjacent total-frame matrix producer')
        if (analytic_stage_module is None
                or sha(analytic_stage_module.__file__) != ANALYTIC_STAGE_SOURCE_SHA256
                or sha(analytic_stage_module.definition.__code__.co_filename) != ANALYTIC_STAGE_SOURCE_SHA256
                or sha(analytic_stage_module.AnalyticNormalStageJacobian.__init__.__code__.co_filename)
                    != ANALYTIC_STAGE_SOURCE_SHA256):
            raise ValueError('Bind the complete independent local analytic J3 producer')
        if (analytic_frame_module is None
                or sha(analytic_frame_module.__file__) != ANALYTIC_FRAME_SOURCE_SHA256
                or sha(analytic_frame_module.definition.__code__.co_filename) != ANALYTIC_FRAME_SOURCE_SHA256
                or sha(analytic_frame_module.AnalyticNormalFrame.__init__.__code__.co_filename)
                    != ANALYTIC_FRAME_SOURCE_SHA256):
            raise ValueError('Bind the complete six-control analytic frame and original full AD fallback')
        if (closure_value_module is None or sha(closure_value_module.__file__) != DETACHED_CLOSURE_SOURCE_SHA256
                or sha(closure_value_module.CompleteDetachedClosureValues.__init__.__code__.co_filename)
                    != DETACHED_CLOSURE_SOURCE_SHA256
                or sha(closure_value_module.definition.__code__.co_filename) != DETACHED_CLOSURE_SOURCE_SHA256):
            raise ValueError('Bind the complete same-chain closure value producer')
        if (meridian_value_module is None
                or sha(meridian_value_module.__file__) != MERIDIAN_VALUE_SOURCE_SHA256
                or sha(meridian_value_module.DetachedMeridianValues.__init__.__code__.co_filename)
                    != MERIDIAN_VALUE_SOURCE_SHA256
                or sha(meridian_value_module.definition.__code__.co_filename) != MERIDIAN_VALUE_SOURCE_SHA256):
            raise ValueError('Bind the complete plain-detached meridian-value helper')
        self.reference_calibration = reference_centering_module.FrozenReferenceCalibration(
            base,self._core_and_cap,self._total,endpoint_source_sha256=sha(__file__))
        self.reference_point_sha256 = self.reference_calibration.reference_point_sha256
        self.base_source_sha256 = expected_base_source_sha256
        self.base_schema = expected_base_schema
        self._bubble_query_cache = {}
        self._point_queries = {}
        self._current_x = None
        self._current_point_sha256 = None
        self._root_cache = {}
        self._residual_cache = None
        self._last_root_failure = None
        self._last_normal_batch = None
        self.endpoint_counts = dict(root_angles_solved=0, root_iterations=0,
            root_line_search_evaluations=0, root_failures=0, jet_upgrades=0,
            implicit_jacobian_blocks=0, cached_root_angles_used=0)
        self.maximum_endpoint_root_residual = 0.
        self.maximum_endpoint_correction_norm = 0.
        self.minimum_endpoint_sample_singular_value = math.inf
        self.maximum_core_inverse_residual = 0.
        self.minimum_core_inverse_sample_rho = math.inf
        self.model = dict(schema=SCHEMA, source_sha256=sha(__file__),
            normal_frame_C1_reuse=frame_c1_module.definition(),
            detached_stage_matrix_reuse=stage_matrix_module.definition(),
            adjacent_normal_frame_matrices=adjacent_matrix_module.definition(),
            analytic_stage_jacobian=analytic_stage_module.definition(),
            analytic_normal_frame=analytic_frame_module.definition(),
            detached_closure_value_reuse=closure_value_module.definition(),
            detached_meridian_value_reuse=meridian_value_module.definition(),
            base_source_sha256=expected_base_source_sha256,
            base_schema=expected_base_schema, base_model_identity_sha256=base.identity,
            base_complete_model=base.model,
            fixed_supported_unit_seed_identity_sha256=base.parent_jet.model_identity,
            fixed_supported_unit_seed_model=base.parent_jet.model,
            fixed_supported_unit_reference_not_rebuilt_from_current_outer_point=True,
            supported_seed_mean_inverse_not_inherited_as_normal_control_inverse=True,
            supported_unit_implementation_derived_from_normal_source_sha256=DERIVED_FROM_COMPLETE_NORMAL_SOURCE_SHA256,
            previous_supported_seed_normal_source_sha256="5297192216356970140585eb9e56c521d9f35453211fb5a76086b713350eaa67",
            normal_frame_create_graph_matches_outer_grad_enabled=True,
            active_full_parameter_J_and_transpose_graph_retained=True,
            fixed_scalar_metric_identity_sha256=base.context.scalar_identity,
            fixed_scalar_profile_definition=base.context.scalar_definition,
            field='complete hDelta lift of CURRENT corrected T, with reference-centred normal-plane roots',
            endpoint_equation='(Gamma-Gamma0)-(P-P0)+integral_0^S(corrected_T-Tref)=0',
            reference_centering_definition=self.reference_calibration.definition,
            correction_side='left multiplication in WORLD coordinates',
            correction_dimension=6, original_shared_control_dimension=3,
            added_gamma_axis_control_dimension=3, implicit_control_dimension=6,
            normal_increment_dimension=3, implicit_dimension_per_stage=9,
            complete_first_angular_implicit_dimension=6*self.normal_stage_count,
            complete_second_angular_implicit_dimension=9*self.normal_stage_count,
            normal_stage_count=self.normal_stage_count,
            exact_normal_step_nodes=[str(value) for value in self.normal_step_nodes],
            actual_normal_step_carriers_binary64_hex=[value.hex() for value in carriers],
            normal_step_carrier_rounding_enclosed=False,
            common_partition_for_all_angles_and_free_points=True,
            per_angle_adaptive_normal_partition=False,
            normal_partition_is_part_of_selected_field_definition=True,
            selection='u0=0; Aprev=f_u(x,phi,uprev); ui=uprev+Aprev^T eta_i; f(ui)=(1-tau_i)f(0)',
            dimensionless_controls='u=(z/S,v); actual world rotation is [S W,gamma I] u',
            dimensionless_constraint='f=((Gamma-Gamma0)-(P-P0)+integral(corrected_T-Tref))/S',
            control_metric='Euclidean metric in all six dimensionless u=(z/S,v) coordinates',
            normal_plane_jacobian='f_u(ui) f_u(uprev)^T; not assumed symmetric or nonsingular',
            stationary_KKT_selection_used=False,
            continuous_horizontal_ODE_solution_claimed=False,
            fixed_finite_normal_planes_are_distinct_selection=True,
            old_admissible_control_family_included_at_v_zero=True,
            old_selected_root_or_field_inherited=False,
            exact_relative_gamma_nodes=[str(value) for value in self.gamma_nodes],
            gamma='independent C2 S5 rise/fall shape strictly inside an original support; zero outside',
            gamma_support_does_not_enlarge_original_support_union=True,
            exact_relative_bubble_nodes=[[str(value) for value in row] for row in self.bubble_nodes],
            bubble='C2 shared-quintic S5 rise and 1-S5 fall, zero outside two disjoint supports',
            frozen_moment_Q_definition=self.frozen_moment_definition,
            literal_Q_input_schema=self.literal_Q_input_schema,
            new_reference_input_binding_source_sha256=self.new_reference_input_binding_source_sha256,
            historical_reference_same_mathematical_g_claimed=False,
            frozen_moment_Q_definition_identity_sha256=self.frozen_moment_identity,
            correction_matrix='B=[S*sum_i beta_i(s) Rz(theta0) Q_i0 Rz(theta0)^T, gamma(s)*I3]',
            Q_i0='the eighteen exact binary64 words in the complete frozen input definition',
            moment_Q_recomputed_from_current_field=False,
            moment_Q_is_an_exact_integral_inverse_claimed=False,
            moment_Q_sparse_parity='only er-et, et-er, et-ez, ez-et entries at theta0=0',
            literal_Q_parameter_origin='eighteen adopted historical working words; no current inverse property assumed',
            historical_original_three_root_algorithm_source_sha256=ORIGINAL_COMPLETE_ENDPOINT_SOURCE_SHA256,
            normal_implementation_derived_from_gamma_source_sha256=NORMAL_DERIVED_FROM_SHA256,
            root_numerical_method='detached Newton/Armijo in each declared fixed normal plane; every preceding frame retained in final implicit differentiation',
            root_branch='same literal eta-zero seed at each common stage; actual cross-angle association and uniqueness unproved',
            root_control_radius_hex=float(self.policy.control_radius).hex(),
            root_normal_policy=self.policy.metadata(),
            physical_S='same exact S and affine physical nodes as the fixed scalar base; mesh/S are numerical carriers',
            M=int(base.M), J=int(base.J), mesh_sha256=array_sha(base.mesh),
            radius_hex=float(base.R).hex(),
            fixed_core_first3=[float(v).hex() for v in base.parent_core[:3]],
            frozen_material_chart='theta0(phi0)=Theta_fixed_base_chart(phi0)',
            all_current_free_core_coefficients_retained=True, current_height_free=True,
            all_original_rotation_variables_retained=True,
            radial_Gram_error_identically_zero=False,
            accurate_zero_root_radial_Gram_error_identically_zero=True,
            radial_identity_scope='only exact reference and final implicit roots; working complete-lift Gram is actually read',
            mathematical_field_definition_requires_exact_implicit_root=True,
            implicit_root_is_not_a_new_independent_free_field=True,
            numerical_integration_or_root_tolerance_part_of_fixed_metric=False)
        self.identity = canonical(self.model)
        self.reference_calibration.bind_field(self.model,self.identity)
        self.detached_closure_values = closure_value_module.CompleteDetachedClosureValues(
            self,progress_path=evaluation_progress_path)
        self.analytic_stage_jacobian = analytic_stage_module.AnalyticNormalStageJacobian(self)
        self.analytic_normal_frame = analytic_frame_module.AnalyticNormalFrame(self)
        self.frame_c1 = frame_c1_module.NormalFrameC1Kernel(self)
        self.stage_matrices = stage_matrix_module.CompleteDetachedStageMatrices(self,frame_c1_module=frame_c1_module)
        self.adjacent_frames = adjacent_matrix_module.AdjacentNormalFrameMatrices(self,
            frame_c1_module=frame_c1_module,stage_matrix_module=stage_matrix_module)
        self.detached_meridian_values = meridian_value_module.DetachedMeridianValues(
            self,closure_value_module=closure_value_module)

    def __getattr__(self, name):
        base = self.__dict__.get('base')
        if base is None:
            raise AttributeError(name)
        return getattr(base, name)

    def _select_point(self, x):
        value = (x.detach().cpu().numpy() if isinstance(x, torch.Tensor) else np.asarray(x))
        value = np.asarray(value, dtype=float)
        if value.shape != (self.free_size,) or not np.isfinite(value).all():
            raise ValueError('Use the actual complete finite original free point')
        if self._current_x is None or not np.array_equal(value, self._current_x):
            self._current_x = np.frombuffer(value.tobytes(order='C'), dtype=np.float64)
            self._current_point_sha256 = array_sha(value)
            self._root_cache = {}
            self._residual_cache = None
            self._last_root_failure = None
            self._last_normal_batch = None
            self.reference_calibration.select_point(self._current_point_sha256)

    def initial(self):
        return self.base.initial()

    def unpack(self, x):
        return self.base.unpack(x)

    def prepare(self, x):
        self._select_point(x)
        return self.base.prepare(x)

    def domain(self, x):
        self._select_point(x)
        result = self.base.domain(x)
        result.update(endpoint_source_sha256=sha(__file__),
            zero_closure_model_identity_sha256=self.identity,
            continuous_endpoint_root_domain_certified=False)
        return result

    def _chart(self, phi):
        p = tensor(np.asarray(phi, dtype=float))
        nu, core = tensor(self.freq), tensor(self.parent_core)
        qfreq = 1-nu*nu
        phase = p[:, None]*nu[None]
        theta = p+(torch.sin(phase)*(qfreq/nu)*core).sum(-1)
        rho = 1+(torch.cos(phase)*qfreq*core).sum(-1)
        rhop = -(torch.sin(phase)*nu*qfreq*core).sum(-1)
        zero = torch.zeros_like(theta)
        er = torch.stack((torch.cos(theta), torch.sin(theta), zero), -1)
        et = torch.stack((-torch.sin(theta), torch.cos(theta), zero), -1)
        return theta, rho, rhop, er, et

    def _core_and_cap(self, core, height, phi):
        theta0, rho0, rhop0, er0, et0 = self._chart(phi)
        nu, qfreq = tensor(self.freq), tensor(self.qfreq)
        with torch.no_grad():
            pc0 = tensor(np.asarray(phi, dtype=float))
            cc = core.detach()
            for _ in range(self.root_iterations):
                phase = pc0[:, None]*nu[None]
                value = pc0+(torch.sin(phase)*(qfreq/nu)*cc).sum(-1)-theta0
                rho = 1+(torch.cos(phase)*qfreq*cc).sum(-1)
                pc0 = pc0-value/rho
            phase = pc0[:, None]*nu[None]
            observed = pc0+(torch.sin(phase)*(qfreq/nu)*cc).sum(-1)-theta0
            rho_detached = 1+(torch.cos(phase)*qfreq*cc).sum(-1)
            error = float(observed.abs().max())
            minimum = float(rho_detached.min())
        if (not math.isfinite(error) or error > self.root_tolerance
                or not math.isfinite(minimum) or minimum <= 0
                or not bool(torch.isfinite(pc0).all())):
            raise EndpointRootFailure('The actual full-core inverse chart failed in its positive numerical domain')
        self.maximum_core_inverse_residual = max(self.maximum_core_inverse_residual, error)
        self.minimum_core_inverse_sample_rho = min(self.minimum_core_inverse_sample_rho, minimum)
        self.counts['inverse_chart_solves'] += len(phi)
        if torch.is_grad_enabled() and core.requires_grad:
            phase0 = pc0[:, None]*nu[None]
            equation = pc0+(torch.sin(phase0)*(qfreq/nu)*core).sum(-1)-theta0
            # Forward is exactly pc0. The first parameter derivative is the
            # full implicit -Theta_c,c/rho_c, not the finite Newton graph.
            pc = pc0-(equation-equation.detach())/rho_detached
        else:
            pc = pc0
        phase = pc[:, None]*nu[None]
        zero = torch.zeros_like(pc)
        er = torch.stack((torch.cos(pc), torch.sin(pc), zero), -1)
        et = torch.stack((-torch.sin(pc), torch.cos(pc), zero), -1)
        support = 1+(torch.cos(phase)*core).sum(-1)
        support_p = -(torch.sin(phase)*nu*core).sum(-1)
        rho = 1+(torch.cos(phase)*qfreq*core).sum(-1)
        Gamma = support[:, None]*er+support_p[:, None]*et
        Gamma_p = rho0[:, None]*et
        Gamma_pp = rhop0[:, None]*et-(rho0*rho0/rho)[:, None]*er
        ez = tensor([0., 0., 1.])
        P = self.R*er0+height*ez
        Pp = self.R*rho0[:, None]*et0
        Ppp = self.R*(rhop0[:, None]*et0-rho0[:, None]**2*er0)
        return (Gamma, Gamma_p, Gamma_pp), (P, Pp, Ppp), rho0

    def _bubble_values(self, query):
        key = array_sha(np.asarray(query['s']))
        if key not in self._bubble_query_cache:
            s = np.asarray(query['s'], dtype=float)
            values, derivatives, masses = [], [], []
            for alpha, gamma, beta in self.bubble_nodes:
                a, c, b = [float(value)*self.S for value in (alpha, gamma, beta)]
                if not 0 < a < c < b < self.S:
                    raise ValueError('The actual bubble carrier loses its strict order')
                v, d = np.zeros_like(s), np.zeros_like(s)
                for left, right, rising in ((a, c, True), (c, b, False)):
                    mask = (s >= left) & (s <= right)
                    u = (s[mask]-left)/(right-left)
                    S5 = 10*u**3-15*u**4+6*u**5
                    D5 = (30*u*u-60*u**3+30*u**4)/(right-left)
                    v[mask] = S5 if rising else 1-S5
                    d[mask] = D5 if rising else -D5
                values.append(v)
                derivatives.append(d)
                masses.append((b-a)/2)
            self._bubble_query_cache[key] = (
                tensor(np.stack(values)), tensor(np.stack(derivatives)), tuple(masses))
        return self._bubble_query_cache[key]

    def _gamma_values(self, query):
        key = array_sha(np.asarray(query['s']))
        if key not in self._gamma_query_cache:
            s = np.asarray(query['s'], dtype=float)
            a, c, b = [float(value)*self.S for value in self.gamma_nodes]
            if not 0 < a < c < b < self.S:
                raise ValueError('The actual gamma carrier loses its complete strict order')
            value, derivative = np.zeros_like(s), np.zeros_like(s)
            for left, right, rising in ((a, c, True), (c, b, False)):
                mask = (s >= left)&(s <= right)
                u = (s[mask]-left)/(right-left)
                S5 = 10*u**3-15*u**4+6*u**5
                D5 = (30*u*u-60*u**3+30*u**4)/(right-left)
                value[mask] = S5 if rising else 1-S5
                derivative[mask] = D5 if rising else -D5
            self._gamma_query_cache[key] = (tensor(value), tensor(derivative))
        return self._gamma_query_cache[key]

    def _W(self, query, phi):
        theta, rho, rhop, er, et = self._chart(phi)
        bubbles, slopes, _ = self._bubble_values(query)
        zero = torch.zeros_like(theta)
        ez = torch.stack((zero, zero, torch.ones_like(theta)), -1)
        frame = torch.stack((er, et, ez), dim=-1)
        Q = torch.stack(tuple(frame@self._frozen_Q0[i]@frame.transpose(-1, -2)
                              for i in range(2)))
        old = sum(bubbles[i, :, None, None, None]*Q[i][None] for i in range(2))
        old_s = sum(slopes[i, :, None, None, None]*Q[i][None] for i in range(2))
        Z = hat(tensor([0., 0., 1.]))
        commutator = Z@old-old@Z
        old_p = rho[None, :, None, None]*commutator
        old_pp = (rhop[None, :, None, None]*commutator
            +rho[None, :, None, None]**2*(Z@commutator-commutator@Z))
        gamma, gamma_s = self._gamma_values(query)
        eye = torch.eye(3, dtype=torch.float64)
        g = (gamma[:, None, None, None]*eye[None, None]).expand(-1, len(phi), -1, -1)
        gs = (gamma_s[:, None, None, None]*eye[None, None]).expand(-1, len(phi), -1, -1)
        zeros = torch.zeros_like(g)
        # Existing W keys retain their physical-jet meaning; each value is
        # now the complete 3x6 B matrix for u=(z/S,v), not an old 3x3 W.
        return dict(W=torch.cat((self.S*old, g), dim=-1),
            Ws=torch.cat((self.S*old_s, gs), dim=-1),
            Wp=torch.cat((self.S*old_p, zeros), dim=-1),
            Wpp=torch.cat((self.S*old_pp, zeros), dim=-1))

    def _total(self, value):
        block = value.reshape(self.J-1, self.integration_order, value.shape[-2], 3)
        widths = tensor(np.diff(self.mesh))
        cell_total = (block*tensor(self.gauss_w)[None, :, None, None]).sum(1)*widths[:, None, None]
        # Same actual reduction order as base._integrate's total.
        return torch.cumsum(cell_total, 0)[-1]

    @staticmethod
    def _detach_data(data):
        return dict(meridians={k:v.detach() for k,v in data['meridians'].items()},
            core=tuple(v.detach() for v in data['core']),
            cap=tuple(v.detach() for v in data['cap']),
            W={k:v.detach() for k,v in data['W'].items()},
            reference={k:v.detach() for k,v in data['reference'].items()},
            reference_core=tuple(v.detach() for v in data['reference_core']),
            reference_cap=tuple(v.detach() for v in data['reference_cap']),
            order=int(data['order']))

    @staticmethod
    def _subset_data(data, indices):
        index = torch.as_tensor(indices,dtype=torch.long)
        return dict(meridians={k:v[:,index] for k,v in data['meridians'].items()},
            core=tuple(v[index] for v in data['core']),
            cap=tuple(v[index] for v in data['cap']),
            W={k:v[:,index] for k,v in data['W'].items()},
            reference={k:v[:,index] for k,v in data['reference'].items()},
            reference_core=tuple(v[index] for v in data['reference_core']),
            reference_cap=tuple(v[index] for v in data['reference_cap']),
            order=int(data['order']))

    def _rotate(self, w, V):
        q = (w*w).sum(-1)
        A, B, _, _, _, _ = self.rotation_coefficients(q)
        first = cross(w, V)
        return V+A[..., None]*first+B[..., None]*cross(w, first)

    def _corrected_jets(self, meridians, W, Zjets, order, *, need_s=False):
        apply = lambda matrix, vector: torch.einsum('paij,aj->pai', matrix, vector)
        w = apply(W['W'], Zjets[:, 0])
        V = meridians['T']
        q = (w*w).sum(-1)
        A, B, Az, Bz, Azz, Bzz = self.rotation_coefficients(q)
        expand = lambda value: value[..., None]
        first, second = cross(w, V), None
        second = cross(w, first)
        answer = {'T': V+expand(A)*first+expand(B)*second}
        if order >= 1:
            wp = apply(W['Wp'], Zjets[:, 0])+apply(W['W'], Zjets[:, 1])
            Vp = meridians['Tp']
            qp = 2*(w*wp).sum(-1)
            first_p = cross(wp, V)+cross(w, Vp)
            second_p = cross(wp, first)+cross(w, first_p)
            answer['Tp'] = (Vp+expand(Az*qp)*first+expand(A)*first_p
                            +expand(Bz*qp)*second+expand(B)*second_p)
        if order >= 2:
            wpp = (apply(W['Wpp'], Zjets[:, 0])+2*apply(W['Wp'], Zjets[:, 1])
                   +apply(W['W'], Zjets[:, 2]))
            Vpp = meridians['Tpp']
            qpp = 2*((wp*wp).sum(-1)+(w*wpp).sum(-1))
            first_pp = cross(wpp, V)+2*cross(wp, Vp)+cross(w, Vpp)
            second_pp = cross(wpp, first)+2*cross(wp, first_p)+cross(w, first_pp)
            answer['Tpp'] = (Vpp+expand(Azz*qp*qp+Az*qpp)*first
                +2*expand(Az*qp)*first_p+expand(A)*first_pp
                +expand(Bzz*qp*qp+Bz*qpp)*second
                +2*expand(Bz*qp)*second_p+expand(B)*second_pp)
        if need_s:
            ws, Vs = apply(W['Ws'], Zjets[:, 0]), meridians['Ts']
            qs = 2*(w*ws).sum(-1)
            first_s = cross(ws, V)+cross(w, Vs)
            second_s = cross(ws, first)+cross(w, first_s)
            answer['Ts'] = (Vs+expand(Az*qs)*first+expand(A)*first_s
                            +expand(Bz*qs)*second+expand(B)*second_s)
        return answer

    def _closure_jets(self, controls, data, order):
        return self.detached_closure_values.value(controls, data, order)

    def _closure_jets_original(self, controls, data, order):
        corrected = self._corrected_jets(data['meridians'],data['W'],controls,order)
        names = ('T','Tp','Tpp')
        self.normal_counts['closure_jet_angle_evaluations'] += len(controls)
        return torch.stack(tuple(((data['core'][j]-data['reference_core'][j])
            -(data['cap'][j]-data['reference_cap'][j])
            +self._total(corrected[names[j]]-data['reference'][names[j]]))/self.S
            for j in range(order+1)),dim=1)

    def _normal_frame_jets(self, previous, data, order):
        return self.analytic_normal_frame.frame(previous, data, order)

    def _stage_control_jets(self, previous, frame, increments, order):
        if (previous.shape[1] < order+1 or frame.shape[1] < order+1
                or increments.shape[1] < order+1 or previous.shape[-1] != 6
                or frame.shape[-2:] != (3,6) or increments.shape[-1] != 3):
            raise ValueError('Use complete previous controls, normal-frame jets and three increments')
        rows = [previous[:,j]+sum(math.comb(j,k)*torch.einsum(
            'aij,ai->aj',frame[:,j-k],increments[:,k]) for k in range(j+1))
            for j in range(order+1)]
        return torch.stack(rows,dim=1)

    def _stage_constraints(self, increments, data, previous, frame, zero, tau, order):
        controls = self._stage_control_jets(previous,frame,increments,order)
        result = self._closure_jets(controls,data,order)-(1-float(tau))*zero[:,:order+1]
        self.normal_counts['stage_equation_angle_evaluations'] += len(increments)
        return result

    def _inside_domain(self, controls):
        return (torch.isfinite(controls).all(-1)
            & (torch.linalg.vector_norm(controls,dim=-1) < self.policy.control_radius))

    def _stage_tolerance(self):
        return self.policy.endpoint_tolerance/self.S

    def _stage_jacobian(self, eta, data, previous, frame, zero, tau):
        return self.analytic_stage_jacobian.matrix(eta, data, previous, frame, zero, tau)

    def _stage_jet_jacobian(self, increments, data, previous, frame, zero, tau, order):
        size = 3*(order+1)
        with torch.enable_grad():
            local = increments[:,:order+1].detach().clone().requires_grad_(True)
            value = self._stage_constraints(local,data,previous,frame,zero,tau,order).reshape(len(local),size)
            rows = [torch.autograd.grad(value[:,j].sum(),local,
                retain_graph=j < size-1,create_graph=False)[0].reshape(len(local),size)
                for j in range(size)]
            result = torch.stack(rows,dim=1).detach()
        self.normal_counts['stage_angular_matrix_angle_evaluations'] += len(increments)
        self.normal_counts['actual_implicit_matrix_angle_rows'] += size*len(increments)
        self.endpoint_counts['implicit_jacobian_blocks'] += len(increments)
        if not bool(torch.isfinite(result).all()):
            raise EndpointRootFailure('Nonfinite complete 6/9 dimensional current normal-stage jet Jacobian')
        return result

    def _fail(self, reason, *, normal_stage_index=None, angles=None,
              physical_endpoint=None, state=None, incremental_state=None):
        self.endpoint_counts['root_failures'] += 1
        finite = lambda value: float(value) if math.isfinite(float(value)) else None
        record = dict(schema='actual-fixed-normal-plane-endpoint-failure-v1',reason=str(reason),
            current_full_point_sha256=self._current_point_sha256,
            normal_stage_index=normal_stage_index, normal_stage_count=self.normal_stage_count,
            normal_summary=self._normal_summary(),root_policy=self.policy.metadata(),
            implicit_control_dimension=6,normal_increment_dimension=3,
            complete_second_angular_implicit_dimension=9*self.normal_stage_count,
            stationary_KKT_selection_used=False,failed_candidate_is_not_an_accepted_field=True,
            failed_root_replaced_by_zero=False,uniform_IFT_failure_or_nonexistence_claimed=False)
        if physical_endpoint is not None:
            record['maximum_actual_physical_endpoint_residual'] = finite(physical_endpoint)
        if state is not None:
            value = state.detach().cpu().numpy() if isinstance(state,torch.Tensor) else np.asarray(state)
            if value.ndim != 2 or value.shape[1] != 6:
                raise ValueError('Retain every actual six-dimensional control in a failure record')
            record['actual_controls'] = [[finite(v) for v in row] for row in value]
            record['actual_controls_binary64_hex'] = [
                [float(v).hex() if math.isfinite(float(v)) else None for v in row] for row in value]
        if incremental_state is not None:
            value = (incremental_state.detach().cpu().numpy()
                if isinstance(incremental_state,torch.Tensor) else np.asarray(incremental_state))
            if value.ndim != 2 or value.shape[1] != 3:
                raise ValueError('Retain each actual three-dimensional normal increment')
            record['actual_normal_increments'] = [[finite(v) for v in row] for row in value]
        if angles is not None:
            record['failed_angle_indices'] = [int(v) for v in angles]
            record['failed_angle_count'] = len(angles)
        self._last_root_failure = record
        raise EndpointRootFailure(json.dumps(record,sort_keys=True,separators=(',',':'),allow_nan=False))

    def _normal_summary(self):
        record = self._last_normal_batch
        if record is None:
            return None
        keys = ('schema','current_full_point_sha256','angle_count','material_angles_binary64_hex',
            'requested_angular_order','same_branch_jet_upgrade','normal_stage_count',
            'exact_normal_step_nodes','completed_stage_count','all_original_endpoint_equations_checked',
            'auxiliary_nodes_are_README_physical_flex','complete_continuous_branch_certified')
        answer = {key:record[key] for key in keys}
        answer['actual_recorded_stage_count'] = len(record['stages'])
        answer['final_original_endpoint_maximum'] = record.get('final_original_endpoint_maximum')
        answer['all_original_endpoint_equations_passed'] = record.get('all_original_endpoint_equations_passed')
        return answer

    def _solve_stage(self, data, previous, frame, zero, tau, stage_index):
        """Detached Newton only in THIS fixed three-dimensional normal plane."""
        count = len(previous)
        eta = torch.zeros((count,3),dtype=torch.float64)
        success = torch.zeros(count,dtype=torch.bool)
        failed = torch.zeros(count,dtype=torch.bool)
        updates = np.zeros(count,dtype=np.int64)
        reasons = ['unresolved']*count
        last_matrix = [None]*count
        last_alpha = [None]*count
        last_candidate_control_norm = [None]*count
        last_trial_norm = [None]*count
        self.normal_counts['stage_root_angle_attempts'] += count
        with torch.no_grad():
            for iteration in range(self.policy.maximum_iterations+1):
                value = self._stage_constraints(eta[:,None],data,previous,frame,zero,tau,0)[:,0]
                norms = torch.linalg.vector_norm(value,dim=-1)
                control = self._stage_control_jets(previous,frame,eta[:,None],0)[:,0]
                finite = torch.isfinite(value).all(-1) & torch.isfinite(norms) & self._inside_domain(control)
                active = ~success & ~failed
                bad = active & ~finite
                for j in torch.nonzero(bad).flatten().tolist():
                    reasons[j] = 'nonfinite current-plane residual or actual control domain failed'
                failed |= bad
                done = active & finite & (norms <= self._stage_tolerance())
                success |= done
                for j in torch.nonzero(done).flatten().tolist():
                    reasons[j] = 'complete current-plane original residual tolerance met'
                active = ~success & ~failed
                if not bool(active.any()):
                    break
                if iteration == self.policy.maximum_iterations:
                    for j in torch.nonzero(active).flatten().tolist():
                        reasons[j] = 'declared fixed-plane Newton budget exhausted'
                    failed |= active
                    break
                try:
                    matrix = self._stage_jacobian(eta,data,previous,frame,zero,tau)
                except (EndpointRootFailure,RuntimeError) as error:
                    for j in torch.nonzero(active).flatten().tolist():
                        reasons[j] = 'actual complete normal-plane Jacobian unavailable: '+str(error)
                    failed |= active
                    break
                direction = torch.zeros_like(eta)
                work = active.clone()
                for j in torch.nonzero(active).flatten().tolist():
                    last_matrix[j] = dict(
                        scope='already evaluated current-plane Jacobian at its own recorded eta/control/residual',
                        current_full_point_sha256=self._current_point_sha256,
                        normal_stage_index=stage_index,local_angle_index=j,newton_iteration=iteration,
                        exact_auxiliary_node=str(self.normal_step_nodes[stage_index]),
                        actual_auxiliary_node_hex=float(tau).hex(),
                        actual_normal_increment=[float(v) for v in eta[j]],
                        actual_previous_controls=[float(v) for v in previous[j,0]],
                        actual_controls=[float(v) for v in control[j]],
                        actual_residual=[float(v) for v in value[j]],
                        actual_previous_frame=[[float(v) for v in row] for row in frame[j,0]],
                        matrix_values=[[float(v) for v in row] for row in matrix[j]],
                        extra_field_or_J_evaluations=0,extra_SVD_evaluations=0)
                    try:
                        self.normal_counts['three_dimensional_solve_angle_attempts'] += 1
                        direction[j] = torch.linalg.solve(matrix[j],value[j,:,None])[:,0]
                    except RuntimeError as error:
                        work[j] = False
                        failed[j] = True
                        reasons[j] = 'actual three-dimensional normal-plane solve failed: '+str(error)
                    if bool(work[j]) and not bool(torch.isfinite(direction[j]).all()):
                        work[j] = False
                        failed[j] = True
                        reasons[j] = 'nonfinite actual normal-plane Newton direction'
                if not bool(work.any()):
                    continue
                accepted = ~work
                next_eta = eta.clone()
                alpha = torch.ones(count,dtype=torch.float64)
                for _ in range(self.policy.maximum_backtracks):
                    candidate = eta-alpha[:,None]*direction
                    candidate_controls = self._stage_control_jets(previous,frame,candidate[:,None],0)[:,0]
                    admissible = torch.isfinite(candidate).all(-1) & self._inside_domain(candidate_controls)
                    pending = work & ~accepted
                    trial = torch.where((pending & admissible)[:,None],candidate,eta)
                    trial_value = self._stage_constraints(trial[:,None],data,previous,frame,zero,tau,0)[:,0]
                    trial_norm = torch.linalg.vector_norm(trial_value,dim=-1)
                    for j in torch.nonzero(pending).flatten().tolist():
                        last_alpha[j] = float(alpha[j])
                        cn = torch.linalg.vector_norm(candidate_controls[j])
                        last_candidate_control_norm[j] = float(cn) if bool(torch.isfinite(cn)) else None
                        last_trial_norm[j] = float(trial_norm[j]) if bool(torch.isfinite(trial_norm[j])) else None
                    good = (pending & admissible & torch.isfinite(trial_norm)
                        & ((trial_norm <= self._stage_tolerance())
                            | (trial_norm < (1-self.policy.armijo*alpha)*norms)))
                    next_eta[good] = candidate[good]
                    accepted |= good
                    self.endpoint_counts['root_line_search_evaluations'] += count
                    self.normal_counts['stage_backtrack_angle_evaluations'] += count
                    if bool(accepted.all()):
                        break
                    alpha[work & ~accepted] *= .5
                bad = work & ~accepted
                for j in torch.nonzero(bad).flatten().tolist():
                    reasons[j] = 'no same-plane residual Armijo decrease inside the actual six-control domain'
                failed |= bad
                advanced = work & accepted
                updates[advanced.cpu().numpy()] += 1
                self.endpoint_counts['root_iterations'] += int(advanced.sum())
                self.normal_counts['stage_newton_angle_updates'] += int(advanced.sum())
                eta = next_eta
            final = self._stage_constraints(eta[:,None],data,previous,frame,zero,tau,0)[:,0]
            norms = torch.linalg.vector_norm(final,dim=-1)
            controls = self._stage_control_jets(previous,frame,eta[:,None],0)[:,0]
            success &= (torch.isfinite(final).all(-1) & torch.isfinite(norms)
                & self._inside_domain(controls) & (norms <= self._stage_tolerance()))
            for j in torch.nonzero(~success).flatten().tolist():
                if reasons[j] == 'complete current-plane original residual tolerance met':
                    reasons[j] = 'returned original current-plane residual or control-domain check failed'
        finite = lambda v: float(v) if math.isfinite(float(v)) else None
        records = [dict(local_angle_index=j,successful=bool(success[j]),
            actual_newton_updates=int(updates[j]),reason=reasons[j],
            actual_normal_increment=[finite(v) for v in eta[j]],
            actual_control=[finite(v) for v in controls[j]],
            final_dimensionless_stage_residual_norm=finite(norms[j]),
            physical_stage_residual_norm=finite(self.S*norms[j]),
            dimensionless_control_norm=finite(torch.linalg.vector_norm(controls[j])),
            last_alpha=last_alpha[j],last_trial_residual_norm=last_trial_norm[j],
            last_candidate_control_norm=last_candidate_control_norm[j],
            last_evaluated_plane_matrix=(None if bool(success[j]) else last_matrix[j]))
            for j in range(count)]
        self.normal_counts['stage_root_angle_successes'] += int(success.sum())
        self.normal_counts['failed_stage_angle_count'] += int((~success).sum())
        return eta.detach(),success,records

    def _finish_stage_jets(self, data, previous, frame, zero, tau, eta, matrix, order, existing=None):
        with torch.no_grad():
            jets = torch.zeros((len(eta),3,3),dtype=torch.float64)
            jets[:,0] = eta
            if existing is not None:
                if order != 2:
                    raise ValueError('A cached first-jet branch is upgraded only to the full second jet')
                jets[:,:2] = existing[:,:2]
            else:
                first = self._stage_constraints(jets,data,previous,frame,zero,tau,1)[:,1]
                try:
                    self.normal_counts['first_angular_solve_angle_attempts'] += len(eta)
                    self.normal_counts['three_dimensional_solve_angle_attempts'] += len(eta)
                    jets[:,1] = torch.linalg.solve(matrix,-first[...,None])[...,0]
                except RuntimeError as error:
                    self._fail('Actual same-plane first angular root-jet solve failed: '+str(error),
                        incremental_state=eta)
            if order == 2:
                second = self._stage_constraints(jets,data,previous,frame,zero,tau,2)[:,2]
                try:
                    self.normal_counts['second_angular_solve_angle_attempts'] += len(eta)
                    self.normal_counts['three_dimensional_solve_angle_attempts'] += len(eta)
                    jets[:,2] = torch.linalg.solve(matrix,-second[...,None])[...,0]
                except RuntimeError as error:
                    self._fail('Actual same-plane second angular root-jet solve failed: '+str(error),
                        incremental_state=eta)
            if not bool(torch.isfinite(jets).all()):
                self._fail('Nonfinite complete normal-increment angular jets',incremental_state=eta)
            residual = self._stage_constraints(jets,data,previous,frame,zero,tau,order)
            if not bool(torch.isfinite(residual).all()):
                self._fail('Nonfinite complete current-plane angular constraint jets',incremental_state=eta)
            norms = torch.linalg.vector_norm(residual,dim=-1)
        return jets.detach(),norms.detach()

    def _run_chain(self, data, keys, order, existing=None):
        """One common finite chain; an order-two upgrade keeps every old value/first jet."""
        if order not in (1,2) or len(keys) != len(data['core'][0]):
            raise ValueError('Use every actual angle and the complete requested angular order')
        if existing is not None and (order != 2 or len(existing) != len(keys)
                or any(item['order'] != 1 for item in existing)):
            raise ValueError('Only an actual cached first-jet branch may be upgraded')
        entry_environment = self.detached_closure_values.entry_environment()
        count = len(keys)
        self._last_normal_batch = dict(schema='actual-complete-fixed-normal-plane-batch-v1',
            current_full_point_sha256=self._current_point_sha256,angle_count=count,
            material_angles_binary64_hex=list(keys),requested_angular_order=order,
            same_branch_jet_upgrade=existing is not None,
            normal_stage_count=self.normal_stage_count,
            exact_normal_step_nodes=[str(v) for v in self.normal_step_nodes],
            completed_stage_count=0,all_original_endpoint_equations_checked=False,
            auxiliary_nodes_are_README_physical_flex=False,
            complete_continuous_branch_certified=False,stages=[])
        log = self._last_normal_batch
        all_stages = []
        frame_context = self.adjacent_frames.frame_context(data,keys,order)
        with torch.no_grad(), self.detached_closure_values.scope(
                data, keys, order, entry_environment) as closure_values, (
                self.frame_c1.value_scope(data,keys,order)) as frame_values, (
                self.stage_matrices.scope(data,keys,order,'returned_value_J3')
                if existing is None else nullcontext()) as stage_matrices:
            previous = torch.zeros((count,3,CONTROL_DIMENSION),dtype=torch.float64)
            zero = torch.zeros((count,3,3),dtype=torch.float64)
            zero[:,:order+1] = self._closure_jets(previous,data,order)
            if existing is not None:
                zero[:,:2] = tensor(np.stack([item['zero'][:2] for item in existing]))
            if not bool(torch.isfinite(zero).all()):
                self._fail('Nonfinite original zero-control closure jets')
            for index in range(1,self.normal_stage_count+1):
                tau = self.normal_step_carriers[index]
                closure_values.progress("normal_stage_frame", stage_index=index)
                frame = torch.zeros((count,3,3,CONTROL_DIMENSION),dtype=torch.float64)
                frame[:,:order+1] = frame_values.frame(previous,index-1)
                old_stage = None if existing is None else [item['stages'][index-1] for item in existing]
                if old_stage is not None:
                    frame[:,:2] = tensor(np.stack([item['frame'][:2] for item in old_stage]))
                if not bool(torch.isfinite(frame).all()):
                    self._fail('Nonfinite complete preceding normal frame',
                        normal_stage_index=index,state=previous[:,0])
                frame_provenance = self.adjacent_frames.capture_frame_inputs(
                    frame_context,previous,frame,index-1,old_stages=old_stage)
                closure_values.progress("normal_stage_root", stage_index=index)
                if old_stage is None:
                    eta,success,records = self._solve_stage(data,previous,frame,zero,tau,index)
                else:
                    eta = tensor(np.stack([item['eta'][0] for item in old_stage]))
                    success = torch.ones(count,dtype=torch.bool)
                    records = [dict(local_angle_index=j,successful=True,
                        reused_original_value_and_first_jet=True,
                        original_stage_record=old_stage[j]['record']) for j in range(count)]
                stage_record = dict(normal_stage_index=index,
                    exact_auxiliary_node=str(self.normal_step_nodes[index]),
                    actual_auxiliary_node_hex=float(tau).hex(),
                    same_branch_jet_upgrade=old_stage is not None,angle_records=records)
                log['stages'].append(stage_record)
                if not bool(success.all()):
                    control = self._stage_control_jets(previous,frame,eta[:,None],0)[:,0]
                    self._fail('A declared fixed normal plane did not return every original stage equation',
                        normal_stage_index=index,angles=torch.nonzero(~success).flatten().tolist(),
                        state=control,incremental_state=eta)
                if old_stage is None:
                    try:
                        matrix = stage_matrices.scalar(eta,previous,frame,zero,tau,index-1)
                        stage_record['returned_value_matrix_origin'] = json.loads(json.dumps(
                            stage_matrices.last_request_record,allow_nan=False))
                    except (EndpointRootFailure,RuntimeError) as error:
                        stage_record['returned_value_matrix_failure'] = str(error)
                        self._fail('Actual normal-plane angular-jet matrix unavailable: '+str(error),
                            normal_stage_index=index,incremental_state=eta)
                    prior_eta = None
                else:
                    matrix = tensor(np.stack([item['J'] for item in old_stage]))
                    prior_eta = tensor(np.stack([item['eta'] for item in old_stage]))
                closure_values.progress("normal_stage_angular_jets", stage_index=index)
                eta_jets,residuals = self._finish_stage_jets(data,previous,frame,zero,tau,
                    eta,matrix,order,existing=prior_eta)
                controls = torch.zeros((count,3,CONTROL_DIMENSION),dtype=torch.float64)
                controls[:,:order+1] = self._stage_control_jets(previous,frame,eta_jets,order)
                if old_stage is not None:
                    controls[:,:2] = tensor(np.stack([item['controls'][:2] for item in old_stage]))
                    if (eta_jets[:,:2].cpu().numpy().tobytes()
                            != np.stack([item['eta'][:2] for item in old_stage]).tobytes()
                            or controls[:,:2].cpu().numpy().tobytes()
                            != np.stack([item['controls'][:2] for item in old_stage]).tobytes()):
                        raise AssertionError('An angular upgrade changed the already selected root branch words')
                # Re-read the actual original plane with these actual cached/extended
                # controls. A cache upgrade never silently repairs a failed old value.
                actual = closure_values.force_value(controls,data,order,
                    reason='original_stage_residual_reread')-(1-tau)*zero[:,:order+1]
                norms = torch.linalg.vector_norm(actual,dim=-1)
                valid = (torch.isfinite(actual).all(-1).all(-1)
                    & self._inside_domain(controls[:,0])
                    & (self.S*norms[:,0] <= self.policy.endpoint_tolerance))
                for j,record in enumerate(records):
                    record.update(actual_control_jet_residual_norms=[float(v) if math.isfinite(float(v))
                        else None for v in norms[j]],original_stage_reread_passed=bool(valid[j]),
                        lower_jets_byte_preserved_on_upgrade=old_stage is not None,
                        dimensionless_control_norm=(float(torch.linalg.vector_norm(controls[j,0]))
                            if bool(torch.isfinite(controls[j,0]).all()) else None))
                if not bool(valid.all()):
                    self._fail('The actual original normal-plane equation failed after its complete angular-jet read',
                        normal_stage_index=index,angles=torch.nonzero(~valid).flatten().tolist(),
                        state=controls[:,0],incremental_state=eta,
                        physical_endpoint=float(torch.max(self.S*norms[:,0])))
                all_stages.append(dict(eta=eta_jets.detach().cpu().numpy().copy(),
                    frame=frame.detach().cpu().numpy().copy(),
                    controls=controls.detach().cpu().numpy().copy(),
                    J=matrix.detach().cpu().numpy().copy(),records=records,frame_provenance=frame_provenance))
                previous = controls.detach()
                log['completed_stage_count'] = index
                closure_values.stage_complete(index)
            closure_values.progress('normal_final_endpoint_reread')
            final = self.S*closure_values.force_value(previous,data,order,
                reason='original_final_endpoint_reread')
            final_norms = torch.linalg.vector_norm(final,dim=-1)
            log['all_original_endpoint_equations_checked'] = True
            finite_final = torch.isfinite(final).all(-1).all(-1)
            log['final_original_endpoint_maximum'] = (
                float(final_norms[:,0].max()) if bool(finite_final.all()) else None)
            valid = finite_final & self._inside_domain(previous[:,0]) & (
                final_norms[:,0] <= self.policy.endpoint_tolerance)
            log['all_original_endpoint_equations_passed'] = bool(valid.all())
            if not bool(valid.all()):
                self._fail('The final ORIGINAL physical endpoint equation failed after the full normal chain',
                    normal_stage_index=self.normal_stage_count,
                    angles=torch.nonzero(~valid).flatten().tolist(),state=previous[:,0],
                    physical_endpoint=log['final_original_endpoint_maximum'])
        if existing is None:
            self.endpoint_counts['root_angles_solved'] += count
        else:
            self.endpoint_counts['jet_upgrades'] += count
        self.maximum_endpoint_root_residual = max(self.maximum_endpoint_root_residual,
            float(final_norms[:,0].max()))
        self.maximum_endpoint_correction_norm = max(self.maximum_endpoint_correction_norm,
            float(torch.linalg.vector_norm(previous[:,0],dim=-1).max()))
        frozen = lambda value: np.array(value,dtype=np.float64,copy=True)
        result = []
        for j in range(count):
            stages = [dict(eta=frozen(item['eta'][j]),frame=frozen(item['frame'][j]),
                controls=frozen(item['controls'][j]),J=frozen(item['J'][j]),
                record=item['records'][j],frame_provenance=item['frame_provenance'][j],
                jacobian=None,jacobian_order=0) for item in all_stages]
            record = dict(numerical_endpoint_residual_norm=float(final_norms[j,0]),
                physical_angular_endpoint_residual_norms=[float(v) for v in final_norms[j]],
                dimensionless_control_norm=float(torch.linalg.vector_norm(previous[j,0])),
                physical_z_norm=float(self.S*torch.linalg.vector_norm(previous[j,0,:3])),
                gamma_axis_norm=float(torch.linalg.vector_norm(previous[j,0,3:])),
                all_normal_stages_returned=True,normal_stage_count=self.normal_stage_count,
                exact_normal_step_nodes=[str(v) for v in self.normal_step_nodes],
                same_branch_jet_upgrade=existing is not None,
                original_value_and_first_jet_preserved=existing is not None,
                final_original_physical_endpoint_equation_checked=True,
                stationary_KKT_selection_used=False,continuous_branch_certified=False)
            item = dict(Z=frozen(previous[j].cpu().numpy()),zero=frozen(zero[j].cpu().numpy()),
                stages=stages,order=order,record=record)
            for key in ('Z','zero'):
                item[key].setflags(write=False)
            for stage in stages:
                for key in ('eta','frame','controls','J'):
                    stage[key].setflags(write=False)
            result.append(item)
        return result

    def _get_roots(self, data, phi, order, *, need_linearization):
        keys = [float(value).hex() for value in phi]
        detached = self._detach_data(data)
        first = {}
        for i,key in enumerate(keys):
            first.setdefault(key,i)
        missing = [i for key,i in first.items() if key not in self._root_cache]
        if missing:
            subset = self._subset_data(detached,missing)
            returned = self._run_chain(subset,[keys[i] for i in missing],order)
            for original,item in zip(missing,returned):
                self._root_cache[keys[original]] = item
        upgrades = [i for key,i in first.items() if self._root_cache[key]['order'] < order]
        if upgrades:
            subset = self._subset_data(detached,upgrades)
            existing = [self._root_cache[keys[i]] for i in upgrades]
            returned = self._run_chain(subset,[keys[i] for i in upgrades],order,existing=existing)
            for original,item in zip(upgrades,returned):
                self._root_cache[keys[original]] = item
        items = [self._root_cache[key] for key in keys]
        self.endpoint_counts['cached_root_angles_used'] += len(keys)-len(missing)
        if need_linearization:
            needed = [i for key,i in first.items()
                if any(stage['jacobian_order'] < order for stage in self._root_cache[key]['stages'])]
            if needed:
                subset = self._subset_data(detached,needed)
                selected = [self._root_cache[keys[i]] for i in needed]
                self.adjacent_frames.populate(subset,[keys[i] for i in needed],selected,order)
        return items


    def _implicit_jet_value(self, data, phi, order, x):
        active = bool(torch.is_grad_enabled() and x.requires_grad)
        items = self._get_roots(data,phi,order,need_linearization=active)
        if not active:
            return tensor(np.stack([item['Z'] for item in items]))
        # The stage increments have a block-lower-triangular global 9m jet
        # system. Sequential value-preserving implicit solves implement ALL
        # its blocks; every upstream u/A/zero-target graph is kept.
        previous = torch.zeros((len(phi),3,CONTROL_DIMENSION),dtype=torch.float64)
        zero_computed = self._closure_jets(previous,data,order)
        zero_hat = tensor(np.stack([item['zero'][:order+1] for item in items]))
        zero = zero_hat+(zero_computed-zero_computed.detach())
        size = 3*(order+1)
        with self.frame_c1.scope(x,data,phi,order,items) as frame_scope:
            for index in range(self.normal_stage_count):
                stages = [item['stages'][index] for item in items]
                frame_computed = frame_scope.frame(previous,index)
                frame_hat = tensor(np.stack([item['frame'][:order+1] for item in stages]))
                frame = frame_hat+(frame_computed-frame_computed.detach())
                eta_hat = tensor(np.stack([item['eta'] for item in stages]))
                matrix = tensor(np.stack([item['jacobian'][:size,:size] for item in stages]))
                residual = self._stage_constraints(eta_hat,data,previous,frame,zero,
                    self.normal_step_carriers[index+1],order)
                zero_value_full_derivative = residual-residual.detach()
                try:
                    self.normal_counts['implicit_solve_angle_attempts'] += len(phi)
                    correction = torch.linalg.solve(matrix,
                        zero_value_full_derivative.reshape(len(phi),size,1))[...,0]
                except RuntimeError as error:
                    self._fail('Actual same-chain full implicit angular linearization failed: '+str(error),
                        normal_stage_index=index+1,incremental_state=eta_hat[:,0])
                eta_used = eta_hat[:,:order+1]-correction.reshape(len(phi),order+1,3)
                computed = self._stage_control_jets(previous,frame,eta_used,order)
                control_hat = tensor(np.stack([item['controls'][:order+1] for item in stages]))
                # Grad/no-grad and batch arithmetic may differ in their working
                # frames. Anchor VALUES to the selected cached stage words while
                # retaining the complete partial derivative of the same formula.
                used = control_hat+(computed-computed.detach())
                previous = (torch.cat((used,tensor(np.stack(
                    [item['controls'][2:3] for item in stages]))),dim=1)
                    if order == 1 else used)
        return previous

    def _reference_data(self, phi):
        return self.reference_calibration.reference_data(phi)

    def _meridian_data(self, x, query, phi, curvature, query_label):
        return self.detached_meridian_values.meridian_data(x,query,phi,curvature,query_label)

    def fields_torch(self, x, query, phi, *, curvature=True, query_label='arbitrary'):
        return self.detached_meridian_values.fields_torch(x,query,phi,
            curvature=curvature,query_label=query_label)

    def _raw_block(self, x, begin, end):
        fields = self.fields_torch(x, self.grid_query, self.phi[begin:end],
                                  curvature=False, query_label='grid')
        V, W = fields['Fs'], fields['Fphi']
        denominator = tensor(self.a)[:, None]*fields['rho0'][None]
        e = (V*V).sum(-1)-1
        f = (V*W).sum(-1)/denominator
        c = (W*W).sum(-1)/(denominator*denominator)-1
        # Keep ALL original Gram rows, including the numerical evaluation
        # of the actual non-unit WORKING lifted Fs. The exact fixed g is unchanged.
        return torch.stack((e, f, c), -1)*tensor(self.sqrt_multiplicity[begin:end])[None, :, None]

    def _blocks(self):
        for begin in range(0, self.N, self.angle_block):
            yield begin, min(begin+self.angle_block, self.N)

    def residual(self, x):
        require_actions()
        self.counts['residual_calls'] += 1
        self.domain(x)
        x = np.asarray(x, dtype=float)
        if self._residual_cache is not None and np.array_equal(x, self._residual_cache[0]):
            return self._residual_cache[1].copy()
        result = np.empty((self.P, self.N, 3))
        with torch.no_grad():
            xt = tensor(x)
            for begin, end in self._blocks():
                result[:, begin:end] = self._raw_block(xt, begin, end).cpu().numpy()
        if not np.isfinite(result).all():
            raise FloatingPointError('Nonfinite complete zero-closure fixed-metric residual')
        self._residual_cache = (x.copy(), result.copy())
        return result

    def unweight(self, native):
        return np.asarray(native).reshape(self.P, self.N, 3)/self.sqrt_multiplicity[None, :, None]

    def jvp(self, x, direction):
        require_actions()
        self.counts['J_calls'] += 1
        self.domain(x)
        direction = np.asarray(direction, dtype=float)
        if direction.shape != (self.free_size,) or not np.isfinite(direction).all():
            raise ValueError('Use every finite original free coordinate in the full J direction')
        result = np.empty((self.P, self.N, 3))
        xt, dt = tensor(x), tensor(direction)
        for begin, end in self._blocks():
            _, value = torch.autograd.functional.jvp(
                lambda point: self._raw_block(point, begin, end), xt, dt,
                create_graph=False, strict=False)
            result[:, begin:end] = value.detach().cpu().numpy()
        if not np.isfinite(result).all():
            raise FloatingPointError('Nonfinite full implicit zero-closure J product')
        return result

    def vjp(self, x, cotangent):
        require_actions()
        self.counts['Jtranspose_calls'] += 1
        self.domain(x)
        cotangent = np.asarray(cotangent, dtype=float).reshape(self.P, self.N, 3)
        if not np.isfinite(cotangent).all():
            raise ValueError('A full metric covector must be finite')
        result = np.zeros(self.free_size)
        for begin, end in self._blocks():
            xt = tensor(x).requires_grad_(True)
            value = self._raw_block(xt, begin, end)
            gradient, = torch.autograd.grad(value, xt, tensor(cotangent[:, begin:end]),
                                           create_graph=False, retain_graph=False)
            result += gradient.detach().cpu().numpy()
        if not np.isfinite(result).all():
            raise FloatingPointError('Nonfinite complete implicit zero-closure transpose')
        return result

    def grid_fields(self, x):
        require_actions()
        self.domain(x)
        with torch.no_grad():
            xt = tensor(x)
            for begin, end in self._blocks():
                values = self.fields_torch(xt, self.grid_query, self.phi[begin:end],
                                          curvature=True, query_label='grid')
                yield begin, end, {name: value.cpu().numpy() for name, value in values.items()}

    def _point_query(self, cell, u):
        key = int(cell), float(u).hex()
        if key not in self._point_queries:
            self._point_queries[key] = self.base.make_query([int(cell)], [float(u)])
        return self._point_queries[key]

    def point_fields(self, x, cell, u, phi):
        require_actions()
        self.domain(x)
        with torch.no_grad():
            result = self.fields_torch(tensor(x), self._point_query(cell, u), [float(phi)],
                                       curvature=True, query_label='arbitrary')
            return {name: result[name][0, 0].cpu().numpy() for name in JET_KEYS}

    def point_vjp(self, x, cell, u, phi, cotangent):
        require_actions()
        self.counts['point_covectors'] += 1
        self.domain(x)
        if set(cotangent) != set(JET_KEYS):
            raise ValueError('Keep all six explicit physical cotangent slots')
        for name in JET_KEYS:
            value = np.asarray(cotangent[name], dtype=float)
            if value.shape != (3,) or not np.isfinite(value).all():
                raise ValueError('Invalid complete physical point covector: '+name)
        xt = tensor(x).requires_grad_(True)
        fields = self.fields_torch(xt, self._point_query(cell, u), [float(phi)],
                                   curvature=True, query_label='arbitrary')
        loss = sum((fields[name][0, 0]*tensor(cotangent[name])).sum() for name in JET_KEYS)
        gradient, = torch.autograd.grad(loss, xt, create_graph=False, retain_graph=False)
        result = gradient.detach().cpu().numpy()
        if result.shape != (self.free_size,) or not np.isfinite(result).all():
            raise FloatingPointError('Nonfinite complete zero-closure point transpose')
        return result

    def mixed_stage_weights(self, fraction):
        return self.base.mixed_stage_weights(fraction)

    def save(self, path, x):
        require_actions()
        self._select_point(x)
        core, jets, height = self.unpack(x)
        np.savez(path, schema=np.array(SCHEMA), omega_jets=jets, core=core, Hcap=np.array(height),
            mesh=self.mesh, fixed_parent_core=self.parent_core,
            zero_closure_model_json=np.array(json.dumps(self.model, sort_keys=True, separators=(',', ':'))),
            zero_closure_model_identity_sha256=np.array(self.identity),
            base_so3_model_identity_sha256=np.array(self.base.identity),
            fixed_scalar_metric_identity_sha256=np.array(self.context.scalar_identity),
            endpoint_root_policy_json=np.array(json.dumps(self.policy.metadata(), sort_keys=True,
                                                          separators=(',', ':'))),
            working_integration_order=np.array(self.integration_order),
            working_full_angles=np.array(self.full_N))

    def load_checkpoint(self, path):
        require_actions()
        with np.load(path, allow_pickle=False) as data:
            if (str(data['schema'].item()) != SCHEMA
                    or str(data['zero_closure_model_identity_sha256'].item()) != self.identity
                    or json.loads(str(data['zero_closure_model_json'].item())) != self.model
                    or str(data['base_so3_model_identity_sha256'].item()) != self.base.identity
                    or str(data['fixed_scalar_metric_identity_sha256'].item()) != self.context.scalar_identity
                    or not np.array_equal(data['mesh'], self.mesh)
                    or not np.array_equal(data['fixed_parent_core'], self.parent_core)
                    or not np.array_equal(data['core'][:self.K], self.parent_core[:self.K])
                    or data['omega_jets'].shape != (self.J, 3, self.n)):
                raise ValueError('Only the identical complete zero-closure field model may continue')
            jets = np.array(data['omega_jets'], copy=True).reshape(3*self.J, self.n)
            if np.any(jets[[0, 3*(self.J-1), 3*(self.J-1)+1]] != 0):
                raise ValueError('The structural core/cap omega slots changed')
            result = np.r_[data['core'][self.K:], jets[self.radial_free].ravel(), float(data['Hcap'])]
        self.unpack(result)
        self._select_point(result)
        return result

    def clear_base(self):
        self._residual_cache = None

    def metadata(self):
        records = [item['record'] for item in self._root_cache.values()]
        grid_keys = {float(value).hex() for value in self.phi}
        finite_or_none = lambda v: float(v) if math.isfinite(float(v)) else None
        base_metadata = self.base.metadata()
        base_metadata.update(base_core_inverse_path_used=False,
            maximum_actual_inverse_chart_residual=None,minimum_actual_inverse_root_rho=None,
            metadata_scope='actual base definition and provider metadata; base hDelta/core/J field paths are not used',
            actual_counts_scope='shared low-level counters; wrapper updates included without per-source cost separation')
        return dict(schema=SCHEMA,source_sha256=sha(__file__),model=self.model,
            model_identity_sha256=self.identity,base_source_sha256=self.base_source_sha256,
            base_complete_metadata=base_metadata,
            reference_centering=self.reference_calibration.metadata(),
            normal_frame_C1_reuse=self.frame_c1.metadata(),
            detached_stage_matrix_reuse=self.stage_matrices.metadata(),
            adjacent_normal_frame_matrices=self.adjacent_frames.metadata(),
            analytic_stage_jacobian=self.analytic_stage_jacobian.metadata(),
            analytic_normal_frame=self.analytic_normal_frame.metadata(),
            detached_closure_value_reuse=self.detached_closure_values.metadata(),
            detached_meridian_value_reuse=self.detached_meridian_values.metadata(),
            current_reference_calibration=self.reference_calibration.current_record(),
            frozen_moment_Q_definition_identity_sha256=self.frozen_moment_identity,
            frozen_moment_Q_definition=self.frozen_moment_definition,
            literal_Q_input_schema=self.literal_Q_input_schema,
            new_reference_input_binding_source_sha256=self.new_reference_input_binding_source_sha256,
            historical_reference_same_mathematical_g_claimed=False,
            Q_input_recomputed_at_current_point=False,
            actual_working_moment_inverse_is_not_a_continuous_certificate=True,
            historical_original_three_root_algorithm_source_sha256=ORIGINAL_COMPLETE_ENDPOINT_SOURCE_SHA256,
            normal_implementation_derived_from_gamma_source_sha256=NORMAL_DERIVED_FROM_SHA256,
            free_variables=int(self.free_size),free_core_variables=int(self.core_size),
            free_rotation_variables=int(self.rotation_size),all_free_height_variables=1,
            current_full_point_sha256=self._current_point_sha256,
            working_integration_order=int(self.integration_order),endpoint_root_policy=self.policy.metadata(),
            normal_stage_count=self.normal_stage_count,
            exact_normal_step_nodes=[str(v) for v in self.normal_step_nodes],
            actual_normal_step_carriers_binary64_hex=[v.hex() for v in self.normal_step_carriers],
            common_partition_for_all_angles_and_free_points=True,per_angle_adaptive_normal_partition=False,
            actual_normal_counts=dict(self.normal_counts),
            normal_lift_last_summary=self._normal_summary(),
            normal_lift_last_batch=self._last_normal_batch,
            normal_frame_create_graph_matches_outer_grad_enabled=True,
            active_full_parameter_J_and_transpose_graph_retained=True,
            normal_count_scope='actual original closure integrals only; logical closure requests and cached returns are separately recorded; all attempted complete batch values, frame reverse products with create_graph matching outer grad mode, stage matrix rows and linear solves; rejected stages and failed candidates included',
            numerical_stage_iterations_differentiated=False,
            final_implicit_J_uses_all_normal_stage_equations=True,
            previous_normal_frame_full_parameter_chain_retained=True,
            original_zero_control_target_full_parameter_chain_retained=True,
            stationary_KKT_selection_used=False,continuous_horizontal_ODE_solution_claimed=False,
            auxiliary_parameter_is_physical_t=False,
            current_cached_angle_roots=len(self._root_cache),
            current_all_grid_angle_roots_available=grid_keys.issubset(self._root_cache),
            current_all_grid_second_angular_jets_available=all(key in self._root_cache
                and self._root_cache[key]['order'] >= 2 for key in grid_keys),
            current_maximum_endpoint_residual=max((v['numerical_endpoint_residual_norm'] for v in records),default=None),
            current_maximum_dimensionless_control_norm=max((v['dimensionless_control_norm'] for v in records),default=None),
            current_maximum_physical_z_norm=max((v['physical_z_norm'] for v in records),default=None),
            current_maximum_gamma_axis_norm=max((v['gamma_axis_norm'] for v in records),default=None),
            current_maximum_first_angular_endpoint_residual=max(
                (v['physical_angular_endpoint_residual_norms'][1] for v in records),default=None),
            current_maximum_second_angular_endpoint_residual=max(
                (v['physical_angular_endpoint_residual_norms'][2] for v in records
                    if len(v['physical_angular_endpoint_residual_norms']) == 3),default=None),
            actual_plane_matrix_singular_values_computed=False,
            all_attempted_fields_maximum_successful_endpoint_residual=(
                self.maximum_endpoint_root_residual if self.endpoint_counts['root_angles_solved'] else None),
            all_attempted_fields_maximum_successful_dimensionless_control_norm=(
                self.maximum_endpoint_correction_norm if self.endpoint_counts['root_angles_solved'] else None),
            all_attempted_fields_maximum_core_inverse_residual=self.maximum_core_inverse_residual,
            all_attempted_fields_minimum_core_inverse_sample_rho=finite_or_none(self.minimum_core_inverse_sample_rho),
            endpoint_counts=dict(self.endpoint_counts),actual_field_counts=dict(self.counts),
            last_root_failure=self._last_root_failure,
            J_method='complete first-parameter implicit finite chain; 6 per stage for metric and 9 per stage for sixjets; every previous A/u and zero-control target edge retained',
            Jtranspose_method='autograd transpose of the SAME complete block-lower-triangular finite-chain implicit graph',
            implicit_control_dimension=6,normal_increment_dimension=3,implicit_dimension_per_stage=9,
            complete_first_angular_implicit_dimension=6*self.normal_stage_count,
            complete_second_angular_implicit_dimension=9*self.normal_stage_count,
            exact_relative_gamma_nodes=[str(v) for v in self.gamma_nodes],
            control_metric='Euclidean in u=(z/S,v); same six-control admissible family, distinct fixed-plane selection',
            cached_first_angular_branch_preserved_on_upgrade=True,
            cached_forward_stage_words_anchored_in_active_graph=True,
            changing_normal_partition_changes_selected_field_definition=True,
            old_selected_root_or_field_inherited=False,
            maximum_required_mixed_exponential_derivative_order=4,
            rotation_coefficient_source_sha256=self.base_source_sha256,
            rotation_small_branch='same degree-12 A/B polynomials in |w|^2<1/4 and all retained graph derivatives',
            unused_large_rotation_branch='same source clamps |w|^2 to >=1/4 before sqrt/division',
            rotation_truncation_branch_seam_or_rounding_error_enclosed=False,
            core_inverse_J='value-preserving -Theta_c,c/rho_c implicit derivative at actual numerical root',
            numerical_Newton_iterations_differentiated=False,
            second_parameter_derivatives_supported_by_surrogate=False,finite_difference_J=False,
            all_metric_mean_and_cross_rows_retained=True,fixed_target_recomputed_from_current_field=False,
            radial_metric_identity_in_exact_definition=True,numerical_radial_Gram_row_omitted=False,
            working_radial_Gram_error_identically_zero=False,
            endpoint_residual_scope='centred equation; raw quadrature closure defect is reported separately',
            complete_current_raw_defect_lift_in_physical_sixjets=True,
            integration_error_enclosed=False,symbolic_mesh_carrier_rounding_error_enclosed=False,
            endpoint_root_error_enclosed=False,complete_uniform_IFT_conditions_verified=False,
            angular_root_jets_outward_enclosed=False,complete_continuous_root_branch_certified=False,
            old_metric_or_geometry_certificates_inherited=False,closed_exact_isometry_certified=False,
            scope='Actual fixed-common-partition six-control candidate; every normal-plane root and angular jet is numerical, with continuous branch/integral/geometry/refinement responsibilities retained')
