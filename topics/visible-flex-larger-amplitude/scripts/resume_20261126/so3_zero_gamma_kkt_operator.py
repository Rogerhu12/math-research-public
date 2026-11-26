#!/usr/bin/env python3
"""Complete added-gamma six-control, nine-KKT zero-closure SO3 field.

The same fixed scalar, frozen chart, literal Q matrices and ALL original
core/omega/H variables remain. A genuinely independent C2 gamma shape inside
the original support adds three WORLD axial controls. The selected numerical
KKT stationary branch has six dimensionless controls and three multipliers;
its angular second-jet implicit system is 27 dimensional, not the old nine.
The full first parameter J/J* retains every multiplier and mixed fourth
derivative. Numerical continuation is detached and is not a physical flex.

Stationarity, numerical closure and numerical small-matrix singular values
are not SOSC, global-minimum, continuous-branch, metric or geometry proofs.
All scientific calls require the public repository Actions environment.
"""
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np
import torch


SCHEMA = 'complete-direct-R690-SO3-added-gamma-six-control-KKT-zero-layer-v1'
CONTINUATION_DERIVED_FROM_SHA256 = '44ac53f1fcecceae55ed3b3230e1925292ce76ced85dc75f08e15ff0b70f5e4e'
FROZEN_MOMENT_INPUT_SCHEMA = 'frozen-zero-endpoint-moment-Q-input-v1'
FROZEN_MOMENT_DEFINITION_SCHEMA = 'literal-two-bubble-endpoint-Q-v1'
ORIGINAL_COMPLETE_ENDPOINT_SOURCE_SHA256 = '5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46'
ACTUAL_TRACE_REPORT_SHA256 = '26b094fef8baf6ff2ecdda5d1a0f5a8be7383e5171733320be959a22d83cb47e'
ACTUAL_TRACE_SOURCE_SHA256 = '73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54'
ACTUAL_TRACE_ORIGINAL_MODEL_IDENTITY_SHA256 = '29f540c6fc265b977a388813dcd0d3faddfd48fd06d40c7f6c4bcae5c848281b'
ACTUAL_TRACE_INITIAL_FULL_POINT_SHA256 = 'cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3'
TORCH_VERSION = '2.5.1'
GAMMA_KKT_DERIVED_FROM_CONTINUATION_SHA256 = '3f37789f1624b97cb7f83b1795ac5fe96be3b3026d4078115078f12e8fd4e34a'
CONTROL_DIMENSION = 6
KKT_DIMENSION = 9
NEW_REFERENCE_INPUT_SCHEMA = 'new-reference-literal-zero-endpoint-Q-input-v1'
NEW_REFERENCE_INPUT_BINDER_SHA256 = 'ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39'
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
    """Explicit disjoint input modes; no old current-reference guard is relaxed."""
    if isinstance(value, dict) and value.get('schema') == FROZEN_MOMENT_INPUT_SCHEMA:
        if new_input_binder is not None:
            raise ValueError('The strict original same-reference input uses its original validator')
        return validate_frozen_moment_input(value, base, bubble_nodes)
    if not isinstance(value, dict) or value.get('schema') != NEW_REFERENCE_INPUT_SCHEMA:
        raise ValueError('Declare either the original same-reference input or the explicit NEW-reference literal input')
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
    kkt_tolerance: float = 2.e-12
    maximum_iterations: int = 24
    maximum_backtracks: int = 18
    armijo: float = 1.e-4
    control_radius: float = 2.
    multiplier_radius: float = 64.

    def __post_init__(self):
        for name in ('endpoint_tolerance', 'kkt_tolerance', 'armijo',
                     'control_radius', 'multiplier_radius'):
            value = float(getattr(self, name))
            if not math.isfinite(value) or value <= 0:
                raise ValueError('Use explicit finite positive KKT numerical parameters: '+name)
            object.__setattr__(self, name, value)
        if self.armijo >= 1:
            raise ValueError('The numerical KKT residual decrease factor must be below one')
        for name in ('maximum_iterations', 'maximum_backtracks'):
            value = int(getattr(self, name))
            if value != getattr(self, name) or value < 1:
                raise ValueError('Use an explicit positive KKT stage budget: '+name)
            object.__setattr__(self, name, value)

    def metadata(self):
        return dict(schema='complete-six-control-nine-KKT-numerical-policy-v1',
            endpoint_tolerance=self.endpoint_tolerance,
            kkt_tolerance=self.kkt_tolerance,
            maximum_iterations=self.maximum_iterations,
            maximum_backtracks=self.maximum_backtracks, armijo=self.armijo,
            control_radius=self.control_radius, multiplier_radius=self.multiplier_radius,
            control='u=(z/S,v); six dimensionless entries, including every new gamma axis',
            multiplier='ell: three dimensionless equality multipliers',
            merit='Euclidean norm of all nine dimensionless KKT equations',
            stage_tolerance='min(kkt_tolerance, endpoint_tolerance / actual S carrier)',
            final_acceptance='fresh ORIGINAL KKT norm <= kkt_tolerance AND physical closure norm <= endpoint_tolerance AND both declared open domains',
            domains='|u| < control_radius and |ell| < multiplier_radius; independent new algorithmic domains',
            old_three_coordinate_radius_or_IFT_ball_inherited=False,
            initial_root='literal u=ell=0 independently for every new angle/full point at continuation_parameter=0',
            actual_root_failure='reject this candidate; no failed root or multiplier is replaced by zero',
            selected_KKT_stationary_branch=True, SOSC_verified=False,
            global_minimum_verified=False, continuous_branch_certified=False,
            root_iteration_graph_differentiated=False)


@dataclass(frozen=True)
class EndpointContinuationPolicy:
    initial_step: float = .25
    minimum_step: float = 1./65536
    growth: float = 1.5
    shrink: float = .5
    maximum_stage_attempts: int = 64
    predictor: bool = True

    def __post_init__(self):
        for name in ('initial_step', 'minimum_step', 'growth', 'shrink'):
            value = float(getattr(self, name))
            if not math.isfinite(value):
                raise ValueError('Finite continuation parameter required: '+name)
            object.__setattr__(self, name, value)
        if not (0 < self.minimum_step <= self.initial_step <= 1
                and self.growth >= 1 and 0 < self.shrink < 1):
            raise ValueError('Use a positive bounded continuation step and honest growth/shrink policy')
        count = int(self.maximum_stage_attempts)
        if count != self.maximum_stage_attempts or count < 1:
            raise ValueError('Use a positive complete per-angle continuation stage-attempt budget')
        object.__setattr__(self, 'maximum_stage_attempts', count)
        if not isinstance(self.predictor, bool):
            raise TypeError('Continuation predictor policy must be an explicit boolean')

    def metadata(self):
        return dict(schema='fixed-final-nine-KKT-residual-continuation-policy-v1',
            initial_step=self.initial_step, minimum_step=self.minimum_step,
            growth=self.growth, shrink=self.shrink,
            maximum_stage_attempts=self.maximum_stage_attempts, predictor=self.predictor,
            equation='R(Y; x,phi) - (1-continuation_parameter)*(0_6,f(x,0,phi)) = 0',
            origin='continuation_parameter=0,u=ell=0 at the SAME x,phi,Q,gamma',
            target='continuation_parameter=1 and a fresh ORIGINAL KKT plus physical closure read',
            rejected_stage='restore the exact last accepted full Y=(u,ell) and continuation_parameter, then shrink its step',
            corrector='complete nine-KKT residual and Hessian/Jacobian with declared Newton/Armijo/control/multiplier domains',
            auxiliary_parameter_is_physical_t=False,
            target_metric_changed=False, current_free_point_changed_by_continuation=False,
            numerical_stage_trajectory_differentiated=False,
            implicit_derivatives_use_final_original_equation=True,
            final_angular_implicit_dimension=27, auxiliary_parameter_is_README_physical_flex=False,
            exact_branch_existence_or_uniqueness_certified=False)


class EndpointRootFailure(ValueError):
    pass


class ZeroClosureOperator:
    """Compose the actual complete direct-reference base with a new field.

    The caller pins BOTH complete sources and the exact base schema. This
    module does not forge a direct-reference label on a different source.
    A new independent driver must record these same source pins.
    """
    def __init__(self, base, *, expected_base_source_sha256, expected_base_schema,
                 bubble_nodes, frozen_moment_input, gamma_nodes=('1/16', '1/8', '3/16'),
                 endpoint_policy=None, continuation_policy=None, new_input_binder=None):
        require_actions()
        if torch.__version__.split('+')[0] != TORCH_VERSION:
            raise ValueError('Use declared CPU PyTorch '+TORCH_VERSION)
        if (not isinstance(expected_base_source_sha256, str)
                or len(expected_base_source_sha256) != 64
                or any(c not in '0123456789abcdef' for c in expected_base_source_sha256)):
            raise ValueError('Pin the actual complete direct R690 base source')
        self.base = base
        if (base.model.get('schema') != expected_base_schema
                or base.model.get('source_sha256') != expected_base_source_sha256
                or canonical(base.model) != base.identity):
            raise ValueError('The actual complete base model/source identity differs')
        for name in ('_unpack_torch', '_angular_nodes', '_radial', '_meridians',
                     '_integrate', 'prepare', 'unpack', 'make_query', '_parent_tensor'):
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
        self.kkt_counts = dict(KKT_angle_evaluations=0, KKT_matrix_angle_evaluations=0,
            closure_jet_angle_evaluations=0, stationarity_reverse_angle_products=0,
            jet_constraint_angle_evaluations=0, nine_dimensional_linear_solve_angle_attempts=0,
            actual_implicit_matrix_rows=0)
        self.maximum_kkt_root_residual = 0.
        self.maximum_multiplier_norm = 0.
        self.policy = EndpointPolicy() if endpoint_policy is None else endpoint_policy
        if not isinstance(self.policy, EndpointPolicy):
            raise TypeError('Use one explicit immutable EndpointPolicy')
        self.continuation_policy = (EndpointContinuationPolicy() if continuation_policy is None
                                    else continuation_policy)
        if not isinstance(self.continuation_policy, EndpointContinuationPolicy):
            raise TypeError('Use one explicit immutable EndpointContinuationPolicy')
        self.endpoint_continuation_counts = dict(batches=0, equation_angle_evaluations=0,
            jacobian_angle_evaluations=0, stage_attempt_angle_count=0,
            accepted_stage_angle_count=0, rejected_stage_angle_count=0,
            predictor_angle_count=0, predictor_fallback_angle_count=0,
            corrector_newton_updates=0, backtrack_angle_evaluations=0)
        self._last_continuation_batch = None
        self.base_source_sha256 = expected_base_source_sha256
        self.base_schema = expected_base_schema
        self._bubble_query_cache = {}
        self._point_queries = {}
        self._current_x = None
        self._current_point_sha256 = None
        self._root_cache = {}
        self._residual_cache = None
        self._last_root_failure = None
        self.endpoint_counts = dict(root_angles_solved=0, root_iterations=0,
            root_line_search_evaluations=0, root_failures=0, jet_upgrades=0,
            implicit_jacobian_blocks=0, cached_root_angles_used=0)
        self.maximum_endpoint_root_residual = 0.
        self.maximum_endpoint_correction_norm = 0.
        self.minimum_endpoint_sample_singular_value = math.inf
        self.maximum_core_inverse_residual = 0.
        self.minimum_core_inverse_sample_rho = math.inf
        self.model = dict(schema=SCHEMA, source_sha256=sha(__file__),
            base_source_sha256=expected_base_source_sha256,
            base_schema=expected_base_schema, base_model_identity_sha256=base.identity,
            base_complete_model=base.model,
            fixed_scalar_metric_identity_sha256=base.context.scalar_identity,
            fixed_scalar_profile_definition=base.context.scalar_definition,
            field='Pcap + integral_S^s Exp((S W zeta(phi0)+gamma v(phi0)) cross) Exp(omega cross) T0; full nine-KKT selects controls',
            endpoint_equation='Gamma_current-Pcap+integral_0^S corrected_T=0',
            correction_side='left multiplication in WORLD coordinates',
            correction_dimension=6, original_shared_control_dimension=3,
            added_gamma_axis_control_dimension=3,
            implicit_control_dimension=CONTROL_DIMENSION, KKT_dimension=KKT_DIMENSION,
            complete_second_angular_implicit_dimension=27,
            exact_relative_gamma_nodes=[str(value) for value in self.gamma_nodes],
            gamma='independent C2 S5 rise/fall shape strictly inside an original support; zero outside',
            implicit_control_cost='(|z/S|^2+|v|^2)/2',
            dimensionless_controls='u=(z/S,v); actual world rotation is [S W,gamma I] u',
            dimensionless_constraint='f=(Gamma-Pcap+integral corrected_T)/S',
            KKT_residual='(u+f_u^T ell,f)',
            KKT_jacobian='[[I+sum ell_i f_i,uu, f_u^T],[f_u,0]]',
            selected_KKT_stationary_branch=True, SOSC_verified=False,
            global_minimum_verified=False,
            old_admissible_control_family_included_at_v_zero=True,
            old_selected_root_or_field_inherited=False,
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
            literal_Q_parameter_origin='eighteen adopted words from a historical working-moment proposal; no current inverse property assumed',
            historical_original_three_root_algorithm_source_sha256=ORIGINAL_COMPLETE_ENDPOINT_SOURCE_SHA256,
            root_numerical_method='detached per-angle residual continuation to the full final nine-KKT stationary system and physical closure',
            root_continuation_policy=self.continuation_policy.metadata(),
            continuation_derived_from_complete_moment_source_sha256=CONTINUATION_DERIVED_FROM_SHA256,
            root_branch='same-seed per-angle continuation_parameter in [0,1] with explicit NEW control/multiplier domains; exact branch and cross-angle association unproved',
            root_control_radius_hex=float(self.policy.control_radius).hex(),
            root_multiplier_radius_hex=float(self.policy.multiplier_radius).hex(),
            root_KKT_policy=self.policy.metadata(),
            new_KKT_implementation_derived_from_continuation_sha256=GAMMA_KKT_DERIVED_FROM_CONTINUATION_SHA256,
            physical_S='same exact S and affine physical nodes as the complete fixed scalar base; mesh/S are numerical carriers',
            M=int(base.M), J=int(base.J), mesh_sha256=array_sha(base.mesh),
            radius_hex=float(base.R).hex(),
            fixed_core_first3=[float(v).hex() for v in base.parent_core[:3]],
            frozen_material_chart='theta0(phi0)=Theta_fixed_base_chart(phi0)',
            all_current_free_core_coefficients_retained=True, current_height_free=True,
            all_original_rotation_variables_retained=True,
            radial_Gram_error_identically_zero=True,
            radial_identity_scope='exact unit-rotation/integral definition; ordinary evaluation errors are unpaid',
            mathematical_field_definition_requires_exact_implicit_root=True,
            implicit_root_is_not_a_new_independent_free_field=True,
            numerical_integration_or_root_tolerance_part_of_fixed_metric=False)
        self.identity = canonical(self.model)

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
            self._current_x = value.copy()
            self._current_point_sha256 = array_sha(value)
            self._root_cache = {}
            self._residual_cache = None
            self._last_root_failure = None

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
        return dict(meridians={key: value.detach() for key, value in data['meridians'].items()},
            core=tuple(value.detach() for value in data['core']),
            cap=tuple(value.detach() for value in data['cap']),
            W={key: value.detach() for key, value in data['W'].items()},
            order=int(data['order']))

    @staticmethod
    def _subset_data(data, indices):
        index = torch.as_tensor(indices, dtype=torch.long)
        return dict(meridians={key: value[:, index] for key, value in data['meridians'].items()},
            core=tuple(value[index] for value in data['core']),
            cap=tuple(value[index] for value in data['cap']),
            W={key: value[:, index] for key, value in data['W'].items()},
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
        corrected = self._corrected_jets(data['meridians'], data['W'], controls, order)
        names = ('T', 'Tp', 'Tpp')
        self.kkt_counts['closure_jet_angle_evaluations'] += len(controls)
        return torch.stack(tuple((data['core'][j]-data['cap'][j]
            +self._total(corrected[names[j]]))/self.S
            for j in range(order+1)), dim=1)


    def _constraints(self, Yjets, data, order):
        """All nine KKT equations and their COMPLETE total angular jets.

        If g_j is the j-th physical closure jet, d g_j / d u0 is the
        j-th total angular derivative of f_u, with u1/u2 independent.
        Its graph MUST retain the original parameter and multiplier chains.
        The enclosing numerical solve may detach the returned VALUES only.
        """
        if (order not in (0, 1, 2) or Yjets.ndim != 3
                or Yjets.shape[-1] != KKT_DIMENSION or Yjets.shape[1] < order+1):
            raise ValueError('Use complete nine-component KKT jets of the declared order')
        outer_grad_enabled = torch.is_grad_enabled()
        with torch.enable_grad():
            controls = Yjets[:, :order+1, :CONTROL_DIMENSION]
            if not controls.requires_grad:
                # A local independent control leaf is needed to EVALUATE
                # f_u even during no-grad Newton. It never detaches data/y.
                controls = controls.detach().clone().requires_grad_(True)
            multipliers = Yjets[:, :order+1, CONTROL_DIMENSION:]
            closure = self._closure_jets(controls, data, order)
            residuals = []
            for j in range(order+1):
                scalar = sum(math.comb(j, k)*(closure[:, j-k]*multipliers[:, k]).sum()
                             for k in range(j+1))
                gradient, = torch.autograd.grad(scalar, controls,
                    create_graph=True, retain_graph=True, allow_unused=False)
                stationarity = controls[:, j]+gradient[:, 0]
                residuals.append(torch.cat((stationarity, closure[:, j]), dim=-1))
                self.kkt_counts['stationarity_reverse_angle_products'] += len(Yjets)
            result = torch.stack(residuals, dim=1)
        self.kkt_counts['jet_constraint_angle_evaluations'] += len(Yjets)
        return result if outer_grad_enabled else result.detach()

    def _K0(self, state, data):
        self.kkt_counts['KKT_angle_evaluations'] += len(state)
        return self._constraints(state[:, None, :], data, 0)[:, 0]

    def _inside_domain(self, state):
        return (torch.isfinite(state).all(-1)
            &(torch.linalg.vector_norm(state[:, :CONTROL_DIMENSION], dim=-1)<self.policy.control_radius)
            &(torch.linalg.vector_norm(state[:, CONTROL_DIMENSION:], dim=-1)<self.policy.multiplier_radius))

    def _stage_tolerance(self):
        return min(self.policy.kkt_tolerance, self.policy.endpoint_tolerance/self.S)


    def _K0_jacobian(self, state, data):
        with torch.enable_grad():
            local = state.detach().clone().requires_grad_(True)
            value = self._K0(local, data)
            rows = [torch.autograd.grad(value[:, j].sum(), local,
                retain_graph=j < KKT_DIMENSION-1, create_graph=False)[0]
                for j in range(KKT_DIMENSION)]
            result = torch.stack(rows, dim=1).detach()
        self.kkt_counts['KKT_matrix_angle_evaluations'] += len(state)
        self.kkt_counts['actual_implicit_matrix_rows'] += KKT_DIMENSION*len(state)
        if not bool(torch.isfinite(result).all()):
            raise EndpointRootFailure('Nonfinite complete nine-dimensional KKT Hessian/Jacobian')
        return result


    def _jet_jacobian(self, Yjets, data, order):
        size = KKT_DIMENSION*(order+1)
        with torch.enable_grad():
            local = Yjets[:, :order+1].detach().clone().requires_grad_(True)
            value = self._constraints(local, data, order).reshape(len(local), size)
            rows = [torch.autograd.grad(value[:, j].sum(), local,
                retain_graph=j < size-1, create_graph=False)[0].reshape(len(local), size)
                for j in range(size)]
            result = torch.stack(rows, dim=1).detach()
        if not bool(torch.isfinite(result).all()):
            raise EndpointRootFailure('Nonfinite COMPLETE 9/18/27 KKT angular-jet Jacobian')
        self.endpoint_counts['implicit_jacobian_blocks'] += len(Yjets)
        self.kkt_counts['actual_implicit_matrix_rows'] += size*len(Yjets)
        return result


    def _fail(self, reason, *, residual=None, state=None, angles=None, physical_endpoint=None):
        self.endpoint_counts['root_failures'] += 1
        finite = lambda value: float(value) if math.isfinite(float(value)) else None
        record = dict(schema='actual-added-gamma-nine-KKT-root-failure-v1',
            reason=str(reason), current_full_point_sha256=self._current_point_sha256,
            root_policy=self.policy.metadata(),
            continuation_policy=self.continuation_policy.metadata(),
            continuation_summary=self._continuation_summary(),
            implicit_control_dimension=CONTROL_DIMENSION, KKT_dimension=KKT_DIMENSION,
            failed_candidate_is_not_an_accepted_field=True,
            failed_root_replaced_by_zero=False,
            SOSC_verified=False, global_minimum_verified=False,
            uniform_IFT_failure_or_nonexistence_claimed=False)
        if residual is not None:
            record['maximum_actual_dimensionless_KKT_residual'] = finite(residual)
        if physical_endpoint is not None:
            record['maximum_actual_physical_endpoint_residual'] = finite(physical_endpoint)
        if state is not None:
            value = state.detach().cpu().numpy() if isinstance(state, torch.Tensor) else np.asarray(state)
            if value.ndim != 2 or value.shape[1] != KKT_DIMENSION:
                raise ValueError('Failure records must retain every control and multiplier')
            record['actual_states'] = [[finite(v) for v in row] for row in value]
            record['actual_states_binary64_hex'] = [
                [float(v).hex() if math.isfinite(float(v)) else None for v in row] for row in value]
            record['state_component_order'] = ['zeta_x','zeta_y','zeta_z',
                'v_x','v_y','v_z','ell_x','ell_y','ell_z']
        if angles is not None:
            record['failed_angle_indices'] = [int(v) for v in angles]
            record['failed_angle_count'] = len(angles)
        self._last_root_failure = record
        raise EndpointRootFailure(json.dumps(record, sort_keys=True, separators=(',', ':'),
                                             allow_nan=False))

    def _continuation_value(self, z, data):
        self.endpoint_continuation_counts['equation_angle_evaluations'] += len(z)
        return self._K0(z, data)

    def _continuation_jacobian(self, z, data):
        self.endpoint_continuation_counts['jacobian_angle_evaluations'] += len(z)
        return self._K0_jacobian(z, data)

    def _continuation_summary(self):
        record = self._last_continuation_batch
        if record is None:
            return None
        result = {key: record[key] for key in (
            'schema', 'current_full_point_sha256', 'angle_count', 'material_angles_binary64_hex',
            'initial_endpoint_residual_norms', 'final_parameters',
            'stage_attempts_by_angle', 'accepted_stages_by_angle',
            'rejected_stages_by_angle', 'corrector_updates_by_angle',
            'all_final_parameters_reached_one', 'final_original_equation_checked',
            'auxiliary_parameter_is_not_physical_t',
            'complete_continuous_branch_certified')}
        result.update(minimum_completed_parameter=min(record['final_parameters'], default=None),
            maximum_completed_parameter=max(record['final_parameters'], default=None),
            actual_total_stage_attempts=sum(record['stage_attempts_by_angle']),
            actual_total_accepted_stages=sum(record['accepted_stages_by_angle']),
            actual_total_rejected_stages=sum(record['rejected_stages_by_angle']),
            actual_total_corrector_updates=sum(record['corrector_updates_by_angle']),
            actual_batch_stage_count=len(record['stages']))
        return result

    def _continuation_corrector(self, data, anchor, start, target, needed):
        """Complete original nine-KKT equations with only the endpoint residual offset.

        A rejected stage never changes the accepted (state,continuation_parameter) pair. Every
        accepted numerical update remains in the declared control and multiplier domains.
        Values are detached; only the final original endpoint equation is
        subsequently used by the complete new 9/18/27 KKT implicit derivative chain.
        """
        count = len(start)
        state = start.detach().clone()
        success = ~needed
        failed = torch.zeros(count, dtype=torch.bool)
        advances = np.zeros(count, dtype=np.int64)
        reasons = ['not requested' if not bool(needed[j]) else 'unresolved'
                   for j in range(count)]
        last_alpha = [None]*count
        last_trial_norm = [None]*count
        last_candidate_norm = [None]*count
        last_norm = [None]*count
        last_matrix_record = [None]*count
        offset = (1-target)[:, None]*anchor
        for iteration in range(self.policy.maximum_iterations+1):
            value = self._continuation_value(state, data)-offset
            norms = torch.linalg.vector_norm(value, dim=-1)
            active = needed & ~success & ~failed
            finite = torch.isfinite(value).all(-1) & torch.isfinite(norms)
            for j in torch.nonzero(active).flatten().tolist():
                last_norm[j] = float(norms[j]) if bool(finite[j]) else None
            bad = active & ~finite
            for j in torch.nonzero(bad).flatten().tolist():
                reasons[j] = 'nonfinite complete continuation residual'
            failed |= bad
            done = active & finite & (norms <= self._stage_tolerance())
            success |= done
            for j in torch.nonzero(done).flatten().tolist():
                reasons[j] = 'complete continuation residual tolerance met'
            active = needed & ~success & ~failed
            if not bool(active.any()):
                break
            if iteration == self.policy.maximum_iterations:
                for j in torch.nonzero(active).flatten().tolist():
                    reasons[j] = 'declared per-stage Newton budget exhausted'
                failed |= active
                break
            try:
                matrix = self._continuation_jacobian(state, data)
            except EndpointRootFailure as error:
                for j in torch.nonzero(active).flatten().tolist():
                    reasons[j] = 'complete continuation Jacobian unavailable: '+str(error)
                failed |= active
                break
            for j in torch.nonzero(active).flatten().tolist():
                last_matrix_record[j] = dict(
                    scope='already evaluated ORIGINAL nine-KKT Jacobian at its explicitly recorded state; not a matrix at an unlabelled later state',
                    current_full_point_sha256=self._current_point_sha256,
                    local_angle_index=j, newton_iteration=iteration,
                    continuation_parameter_target=float(target[j]),
                    state_values=[float(v) for v in state[j]],
                    shifted_stage_residual_values=[float(v) for v in value[j]],
                    matrix_values=[[float(v) for v in row] for row in matrix[j]],
                    extra_field_or_J_evaluations=0, extra_SVD_evaluations=0)
            direction = torch.zeros_like(state)
            work = active.clone()
            for j in torch.nonzero(active).flatten().tolist():
                try:
                    self.kkt_counts['nine_dimensional_linear_solve_angle_attempts'] += 1
                    direction[j] = torch.linalg.solve(matrix[j], value[j, :, None])[:, 0]
                except RuntimeError as error:
                    work[j] = False
                    failed[j] = True
                    reasons[j] = 'actual stage linear solve failed: '+str(error)
                if bool(work[j]) and not bool(torch.isfinite(direction[j]).all()):
                    work[j] = False
                    failed[j] = True
                    reasons[j] = 'nonfinite actual stage Newton direction'
            if not bool(work.any()):
                continue
            accepted = ~work
            next_z = state.clone()
            alpha = torch.ones(count, dtype=torch.float64)
            for _ in range(self.policy.maximum_backtracks):
                candidate = state-alpha[:, None]*direction
                candidate_norm = torch.linalg.vector_norm(candidate, dim=-1)
                admissible = self._inside_domain(candidate)
                pending = work & ~accepted
                use_candidate = pending & admissible
                # Unusable or already resolved rows are evaluated at the
                # unchanged current point; the true complete batch count is paid.
                trial = torch.where(use_candidate[:, None], candidate, state)
                trial_value = self._continuation_value(trial, data)-offset
                trial_norm = torch.linalg.vector_norm(trial_value, dim=-1)
                for j in torch.nonzero(pending).flatten().tolist():
                    last_alpha[j] = float(alpha[j])
                    last_candidate_norm[j] = (float(candidate_norm[j])
                        if bool(torch.isfinite(candidate_norm[j])) else None)
                    last_trial_norm[j] = (float(trial_norm[j])
                        if bool(torch.isfinite(trial_norm[j])) else None)
                good = (pending & admissible & torch.isfinite(trial_norm)
                    & ((trial_norm <= self._stage_tolerance())
                       | (trial_norm < (1-self.policy.armijo*alpha)*norms)))
                next_z[good] = candidate[good]
                accepted |= good
                self.endpoint_counts['root_line_search_evaluations'] += count
                self.endpoint_continuation_counts['backtrack_angle_evaluations'] += count
                if bool(accepted.all()):
                    break
                alpha[work & ~accepted] *= .5
            bad = work & ~accepted
            for j in torch.nonzero(bad).flatten().tolist():
                reasons[j] = 'no same-stage complete residual Armijo decrease inside the new control/multiplier domains'
            failed |= bad
            advanced = work & accepted
            advances[advanced.cpu().numpy()] += 1
            state = next_z
        # Every claimed stage success is checked again at its returned state.
        final = self._continuation_value(state, data)-offset
        norm = torch.linalg.vector_norm(final, dim=-1)
        inside = self._inside_domain(state)
        valid = torch.isfinite(final).all(-1) & torch.isfinite(norm) & inside & (norm <= self._stage_tolerance())
        success = needed & success & valid
        for j in torch.nonzero(needed & ~success).flatten().tolist():
            if reasons[j] == 'complete continuation residual tolerance met':
                reasons[j] = 'returned same-stage residual or new control/multiplier domains check failed'
        records = [dict(angle_index=j, requested=bool(needed[j]),
            parameter_target=float(target[j]), successful=bool(success[j]),
            actual_newton_updates=int(advances[j]), reason=reasons[j],
            last_evaluated_KKT_matrix=(None if bool(success[j]) else last_matrix_record[j]),
            final_stage_residual_norm=(float(norm[j]) if bool(torch.isfinite(norm[j])) else None),
            dimensionless_state_norm=(float(torch.linalg.vector_norm(state[j]))
                if bool(torch.isfinite(state[j]).all()) else None),
            last_newton_residual_norm=last_norm[j], last_alpha=last_alpha[j],
            last_trial_residual_norm=last_trial_norm[j],
            last_candidate_state_norm=last_candidate_norm[j],
            dimensionless_control_norm=(float(torch.linalg.vector_norm(state[j, :CONTROL_DIMENSION]))
                if bool(torch.isfinite(state[j]).all()) else None),
            multiplier_norm=(float(torch.linalg.vector_norm(state[j, CONTROL_DIMENSION:]))
                if bool(torch.isfinite(state[j]).all()) else None),
            stationarity_norm=(float(torch.linalg.vector_norm(final[j, :CONTROL_DIMENSION]))
                if bool(torch.isfinite(final[j]).all()) else None),
            physical_auxiliary_endpoint_norm=(float(self.S*torch.linalg.vector_norm(final[j, CONTROL_DIMENSION:]))
                if bool(torch.isfinite(final[j]).all()) else None),
            state_values=[float(v) if math.isfinite(float(v)) else None for v in state[j]],
            nine_KKT_values=[float(v) if math.isfinite(float(v)) else None for v in final[j]])
            for j in range(count) if bool(needed[j])]
        return state.detach(), success, advances, records

    def _solve_roots(self, data, *, literal_phi_hex):
        """Detached residual continuation, ending at the original NINE KKT equations.

        The auxiliary continuation_parameter is neither the README physical flex nor a changed
        target metric. Its successful finite stages are numerical trajectory
        records only; no existence, uniqueness or cross-angle branch theorem
        is inferred from them.
        """
        count = len(data['core'][0])
        if len(literal_phi_hex) != count or any(float.fromhex(v).hex() != v for v in literal_phi_hex):
            raise ValueError('Continuation roots need every original literal material angle')
        self.endpoint_continuation_counts['batches'] += 1
        self._last_continuation_batch = dict(
            schema='actual-added-gamma-nine-KKT-residual-continuation-batch-v1',
            current_full_point_sha256=self._current_point_sha256,
            angle_count=count, material_angles_binary64_hex=list(literal_phi_hex),
            initial_endpoint_residual_norms=[],
            final_parameters=[0.]*count, stage_attempts_by_angle=[0]*count,
            accepted_stages_by_angle=[0]*count, rejected_stages_by_angle=[0]*count,
            corrector_updates_by_angle=[0]*count, stages=[],
            all_final_parameters_reached_one=False,
            final_original_equation_checked=False,
            auxiliary_parameter_is_not_physical_t=True,
            complete_continuous_branch_certified=False)
        log = self._last_continuation_batch
        policy = self.continuation_policy
        with torch.no_grad():
            state = torch.zeros((count, KKT_DIMENSION), dtype=torch.float64)
            anchor = self._continuation_value(state, data).detach()
            if bool((anchor[:, :CONTROL_DIMENSION] != 0).any()):
                self._fail('The zero-control/zero-multiplier KKT origin has nonzero stationarity', state=state)
            norm0 = torch.linalg.vector_norm(anchor, dim=-1)
            log['initial_endpoint_residual_norms'] = [
                float(self.S*torch.linalg.vector_norm(anchor[j, CONTROL_DIMENSION:]))
                if bool(torch.isfinite(anchor[j]).all()) else None for j in range(count)]
            log['initial_dimensionless_KKT_residual_norms'] = [
                float(norm0[j]) if bool(torch.isfinite(norm0[j])) else None for j in range(count)]
            if not bool(torch.isfinite(anchor).all()) or not bool(torch.isfinite(norm0).all()):
                self._fail('Nonfinite original endpoint residual at continuation origin')
            parameter = torch.zeros(count, dtype=torch.float64)
            # An already accurate original root needs no auxiliary stages.
            parameter[norm0 <= self._stage_tolerance()] = 1.
            step = torch.full((count,), policy.initial_step, dtype=torch.float64)
            attempts = np.zeros(count, dtype=np.int64)
            accepted_stages = np.zeros(count, dtype=np.int64)
            rejected_stages = np.zeros(count, dtype=np.int64)
            updates = np.zeros(count, dtype=np.int64)
            while bool((parameter < 1).any()):
                needed = parameter < 1
                exhausted = needed.cpu().numpy() & (attempts >= policy.maximum_stage_attempts)
                if bool(exhausted.any()):
                    log.update(final_parameters=parameter.tolist(),
                        stage_attempts_by_angle=attempts.tolist(),
                        accepted_stages_by_angle=accepted_stages.tolist(),
                        rejected_stages_by_angle=rejected_stages.tolist(),
                        corrector_updates_by_angle=updates.tolist())
                    self._fail('Declared continuation stage-attempt budget exhausted before continuation_parameter=1',
                        residual=float(torch.linalg.vector_norm(self._continuation_value(state, data), dim=-1).max()),
                        state=state,
                        angles=np.flatnonzero(exhausted).tolist())
                before = parameter.clone()
                target = torch.minimum(torch.ones_like(parameter), parameter+step)
                target[~needed] = 1.
                delta = target-parameter
                stalled = needed & (delta <= 0)
                if bool(stalled.any()):
                    self._fail('No positive representable continuation parameter step',
                        angles=torch.nonzero(stalled).flatten().tolist())
                start = state.clone()
                predictor_used = torch.zeros(count, dtype=torch.bool)
                predictor_reason = ['not requested']*count
                if policy.predictor:
                    try:
                        matrix = self._continuation_jacobian(state, data)
                    except EndpointRootFailure as error:
                        matrix = None
                        for j in torch.nonzero(needed).flatten().tolist():
                            predictor_reason[j] = 'Jacobian unavailable; last accepted state retained: '+str(error)
                    if matrix is not None:
                        for j in torch.nonzero(needed).flatten().tolist():
                            try:
                                self.kkt_counts['nine_dimensional_linear_solve_angle_attempts'] += 1
                                tangent = torch.linalg.solve(matrix[j], -anchor[j, :, None])[:, 0]
                                candidate = state[j]+delta[j]*tangent
                                if (bool(torch.isfinite(candidate).all())
                                        and bool(self._inside_domain(candidate[None])[0])):
                                    start[j] = candidate
                                    predictor_used[j] = True
                                    predictor_reason[j] = 'same-equation tangent predictor used'
                                else:
                                    predictor_reason[j] = 'predictor outside new control/multiplier domains or nonfinite; last accepted state retained'
                            except RuntimeError as error:
                                predictor_reason[j] = 'predictor linear solve failed; last accepted state retained: '+str(error)
                else:
                    for j in torch.nonzero(needed).flatten().tolist():
                        predictor_reason[j] = 'predictor explicitly disabled; last accepted state retained'
                attempts[needed.cpu().numpy()] += 1
                self.endpoint_continuation_counts['stage_attempt_angle_count'] += int(needed.sum())
                self.endpoint_continuation_counts['predictor_angle_count'] += int(predictor_used.sum())
                self.endpoint_continuation_counts['predictor_fallback_angle_count'] += int((needed & ~predictor_used).sum())
                corrected, success, stage_updates, stage_records = self._continuation_corrector(
                    data, anchor, start, target, needed)
                updates += stage_updates
                self.endpoint_counts['root_iterations'] += int(stage_updates.sum())
                self.endpoint_continuation_counts['corrector_newton_updates'] += int(stage_updates.sum())
                failed = needed & ~success
                state[success] = corrected[success]
                parameter[success] = target[success]
                accepted_stages[success.cpu().numpy()] += 1
                rejected_stages[failed.cpu().numpy()] += 1
                self.endpoint_continuation_counts['accepted_stage_angle_count'] += int(success.sum())
                self.endpoint_continuation_counts['rejected_stage_angle_count'] += int(failed.sum())
                for item in stage_records:
                    j = item['angle_index']
                    item.update(parameter_before=float(before[j]), actual_parameter_increment=float(delta[j]),
                        predictor_used=bool(predictor_used[j]), predictor_reason=predictor_reason[j],
                        accepted_parameter_after=float(parameter[j]),
                        rejected_stage_did_not_change_accepted_z_or_parameter=not bool(success[j]))
                log['stages'].append(dict(batch_stage=len(log['stages']),
                    angle_records=stage_records))
                log.update(final_parameters=parameter.tolist(),
                    stage_attempts_by_angle=attempts.tolist(),
                    accepted_stages_by_angle=accepted_stages.tolist(),
                    rejected_stages_by_angle=rejected_stages.tolist(),
                    corrector_updates_by_angle=updates.tolist())
                # Increase only after a complete successful correction; every
                # rejected stage returns to exactly the prior accepted pair.
                step[success] = torch.minimum(torch.ones_like(step[success]), delta[success]*policy.growth)
                step[failed] = delta[failed]*policy.shrink
                too_small = failed & (step < policy.minimum_step)
                if bool(too_small.any()):
                    self._fail('Continuation step exhausted before the original endpoint equation was reached',
                        residual=float(torch.linalg.vector_norm(self._continuation_value(state, data), dim=-1).max()),
                        state=state,
                        angles=torch.nonzero(too_small).flatten().tolist())
            log.update(final_parameters=parameter.tolist(),
                stage_attempts_by_angle=attempts.tolist(),
                accepted_stages_by_angle=accepted_stages.tolist(),
                rejected_stages_by_angle=rejected_stages.tolist(),
                corrector_updates_by_angle=updates.tolist())
            log['all_final_parameters_reached_one'] = bool((parameter == 1).all())
            # The final acceptance reads original C, with no homotopy offset.
            final_value = self._continuation_value(state, data)
            final_norm = torch.linalg.vector_norm(final_value, dim=-1)
            inside = self._inside_domain(state)
        physical_norm = self.S*torch.linalg.vector_norm(final_value[:, CONTROL_DIMENSION:], dim=-1)
        stationarity_norm = torch.linalg.vector_norm(final_value[:, :CONTROL_DIMENSION], dim=-1)
        if (not log['all_final_parameters_reached_one']
                or not bool(torch.isfinite(final_norm).all())
                or not bool(torch.isfinite(physical_norm).all())
                or bool((final_norm > self.policy.kkt_tolerance).any())
                or bool((physical_norm > self.policy.endpoint_tolerance).any())
                or not bool(inside.all())):
            self._fail('Returned continuation candidate has unpaid ORIGINAL KKT, physical closure or declared domain',
                residual=float(final_norm.max()), state=state,
                physical_endpoint=float(physical_norm.max()))
        log['final_original_equation_checked'] = True
        try:
            K = self._continuation_jacobian(state, data)
            singular = torch.linalg.svdvals(K)[..., -1]
        except (RuntimeError, EndpointRootFailure) as error:
            self._fail('Actual final COMPLETE nine-KKT matrix read failed: '+str(error), state=state)
        if not bool(torch.isfinite(singular).all()):
            self._fail('Nonfinite actual complete KKT singular-value diagnostic', state=state)
        controls = torch.linalg.vector_norm(state[:, :CONTROL_DIMENSION], dim=-1)
        multipliers = torch.linalg.vector_norm(state[:, CONTROL_DIMENSION:], dim=-1)
        self.endpoint_counts['root_angles_solved'] += count
        self.maximum_endpoint_root_residual = max(self.maximum_endpoint_root_residual,
                                                   float(physical_norm.max()))
        self.maximum_kkt_root_residual = max(self.maximum_kkt_root_residual, float(final_norm.max()))
        self.maximum_endpoint_correction_norm = max(self.maximum_endpoint_correction_norm,
                                                     float(controls.max()))
        self.maximum_multiplier_norm = max(self.maximum_multiplier_norm, float(multipliers.max()))
        self.minimum_endpoint_sample_singular_value = min(self.minimum_endpoint_sample_singular_value,
                                                           float(singular.min()))
        records = [dict(numerical_endpoint_residual_norm=float(physical_norm[j]),
            numerical_KKT_residual_norm=float(final_norm[j]),
            numerical_stationarity_residual_norm=float(stationarity_norm[j]),
            numerical_normalized_endpoint_residual_norm=float(physical_norm[j]/self.S),
            dimensionless_control_norm=float(controls[j]), multiplier_norm=float(multipliers[j]),
            physical_z_norm=float(self.S*torch.linalg.vector_norm(state[j, :3])),
            gamma_axis_norm=float(torch.linalg.vector_norm(state[j, 3:6])),
            numerical_iterations=int(updates[j]),
            actual_KKT_smallest_singular_value=float(singular[j]),
            continuation_final_parameter=float(parameter[j]),
            continuation_stage_attempts=int(attempts[j]),
            continuation_accepted_stages=int(accepted_stages[j]),
            continuation_rejected_stages=int(rejected_stages[j]),
            numerical_root_tolerances_met=True,
            selected_KKT_stationary_branch=True, SOSC_verified=False,
            global_minimum_verified=False, uniform_IFT_conditions_verified=False,
            exact_continuous_root_certified=False) for j in range(count)]
        return state.detach(), K.detach(), records


    def _finish_jets(self, data, state, K, order, existing=None):
        with torch.no_grad():
            Yjets = torch.zeros((len(state), 3, KKT_DIMENSION), dtype=torch.float64)
            Yjets[:, 0] = state
            if existing is not None:
                Yjets[:, 1] = existing[:, 1]
            else:
                first = self._constraints(Yjets, data, 1)[:, 1]
                try:
                    self.kkt_counts['nine_dimensional_linear_solve_angle_attempts'] += len(state)
                    Yjets[:, 1] = torch.linalg.solve(K, -first[..., None])[..., 0]
                except RuntimeError as error:
                    self._fail('Actual complete first angular KKT-jet solve failed: '+str(error), state=state)
            if order == 2:
                second = self._constraints(Yjets, data, 2)[:, 2]
                try:
                    self.kkt_counts['nine_dimensional_linear_solve_angle_attempts'] += len(state)
                    Yjets[:, 2] = torch.linalg.solve(K, -second[..., None])[..., 0]
                except RuntimeError as error:
                    self._fail('Actual complete second angular KKT-jet solve failed: '+str(error), state=state)
            if not bool(torch.isfinite(Yjets).all()):
                self._fail('Nonfinite COMPLETE control/multiplier angular jets', state=state)
            residual = self._constraints(Yjets, data, order)
            if not bool(torch.isfinite(residual).all()):
                self._fail('Nonfinite complete angular KKT residual', state=state)
            norms = torch.linalg.vector_norm(residual, dim=-1)
        # Every residual here has all six stationarity and three endpoint
        # components. A numerical jet residual is never a continuous proof.
        return Yjets.detach(), norms.detach()

    def _get_roots(self, data, phi, order, *, need_linearization):
        keys = [float(value).hex() for value in phi]
        detached = self._detach_data(data)
        missing = [i for i, key in enumerate(keys) if key not in self._root_cache]
        if missing:
            subset = self._subset_data(detached, missing)
            z, A, records = self._solve_roots(subset, literal_phi_hex=[keys[i] for i in missing])
            Zjets, residuals = self._finish_jets(subset, z, A, order)
            for local, original in enumerate(missing):
                self._root_cache[keys[original]] = dict(
                    Z=Zjets[local].cpu().numpy().copy(),
                    A=A[local].cpu().numpy().copy(), order=order,
                    record=dict(records[local],
                        angular_jet_residual_norms=[float(v) for v in residuals[local]]),
                    jacobian=None, jacobian_order=0)
        upgrades = [i for i, key in enumerate(keys) if self._root_cache[key]['order'] < order]
        if upgrades:
            subset = self._subset_data(detached, upgrades)
            prior = tensor(np.stack([self._root_cache[keys[i]]['Z'] for i in upgrades]))
            A = tensor(np.stack([self._root_cache[keys[i]]['A'] for i in upgrades]))
            Zjets, residuals = self._finish_jets(subset, prior[:, 0], A, order, existing=prior)
            for local, original in enumerate(upgrades):
                item = self._root_cache[keys[original]]
                item['Z'], item['order'] = Zjets[local].cpu().numpy().copy(), order
                item['record']['angular_jet_residual_norms'] = [float(v) for v in residuals[local]]
            self.endpoint_counts['jet_upgrades'] += len(upgrades)
        Zhat = tensor(np.stack([self._root_cache[key]['Z'] for key in keys]))
        self.endpoint_counts['cached_root_angles_used'] += len(keys)-len(missing)
        if not need_linearization:
            return Zhat, None
        unfactored = [i for i, key in enumerate(keys)
                      if self._root_cache[key]['jacobian_order'] < order]
        if unfactored:
            subset = self._subset_data(detached, unfactored)
            current = Zhat[torch.as_tensor(unfactored, dtype=torch.long)]
            matrix = self._jet_jacobian(current, subset, order)
            for local, original in enumerate(unfactored):
                item = self._root_cache[keys[original]]
                item['jacobian'] = matrix[local].cpu().numpy().copy()
                item['jacobian_order'] = order
        size = KKT_DIMENSION*(order+1)
        RZ = tensor(np.stack([self._root_cache[key]['jacobian'][:size, :size] for key in keys]))
        return Zhat, RZ

    def _implicit_jet_value(self, data, phi, order, x):
        active = bool(torch.is_grad_enabled() and x.requires_grad)
        Zhat, RZ = self._get_roots(data, phi, order, need_linearization=active)
        if not active:
            return Zhat
        # This is a value-preserving FIRST-PARAMETER implicit linearization.
        # Its forward value is exactly Zhat. RZ is the complete current
        # 18x18 or 27x27 KKT jet Jacobian at fixed original y, including ALL multipliers.
        # No Newton iteration contributes an autograd edge.
        residual = self._constraints(Zhat, data, order)
        zero_value_full_derivative = residual-residual.detach()
        try:
            correction = torch.linalg.solve(RZ,
                zero_value_full_derivative.reshape(len(phi), -1, 1))[..., 0]
        except RuntimeError as error:
            self._fail('Actual complete implicit endpoint-jet linearization failed: '+str(error))
        Zused = Zhat[:, :order+1]-correction.reshape(len(phi), order+1, KKT_DIMENSION)
        if order == 1:
            Zused = torch.cat((Zused, Zhat[:, 2:3]), dim=1)
        return Zused

    def _meridian_data(self, x, query, phi, curvature, query_label):
        core, jets, height = self.base._unpack_torch(x)
        nodes = self.base._angular_nodes(jets, phi, 0)
        nodes_p = self.base._angular_nodes(jets, phi, 1)
        nodes_pp = self.base._angular_nodes(jets, phi, 2) if curvature else None
        integration = self.base._meridians(nodes, nodes_p, nodes_pp,
            self.integration_query, phi, 'integration', curvature)
        direct = self.base._meridians(nodes, nodes_p, nodes_pp, query, phi,
            query_label, curvature)
        core_jets, cap_jets, rho0 = self._core_and_cap(core, height, phi)
        for values in (integration, direct):
            if any(not bool(torch.isfinite(value.detach()).all()) for value in values.values()):
                self._fail('Nonfinite actual direct-reference meridian jets')
        order = 2 if curvature else 1
        data = dict(meridians=integration, core=core_jets, cap=cap_jets,
                    W=self._W(self.integration_query, phi), order=order)
        return data, direct, self._W(query, phi), rho0

    def fields_torch(self, x, query, phi, *, curvature=True, query_label='arbitrary'):
        require_actions()
        self._select_point(x)
        phi = np.asarray(phi, dtype=float)
        if phi.ndim != 1 or not len(phi) or not np.isfinite(phi).all():
            raise ValueError('Use an actual finite one-dimensional material-chart angle list')
        data, direct, Wdirect, rho0 = self._meridian_data(x, query, phi, curvature, query_label)
        order = 2 if curvature else 1
        Zjets = self._implicit_jet_value(data, phi, order, x)
        controls = Zjets[:, :, :CONTROL_DIMENSION]
        integrated = self._corrected_jets(data['meridians'], data['W'], controls, order)
        requested = self._corrected_jets(direct, Wdirect, controls, order, need_s=curvature)
        result = {}
        names = ('T', 'Tp', 'Tpp')
        outputs = ('F', 'Fphi', 'Fphiphi')
        totals = []
        for j in range(order+1):
            integral, total = self.base._integrate(integrated[names[j]], query)
            result[outputs[j]] = data['cap'][j][None]+integral-total[None]
            totals.append(total)
        result['Fs'] = requested['T']
        if curvature:
            result['Fss'], result['Fsphi'] = requested['Ts'], requested['Tp']
        result['rho0'] = rho0
        result['closure_delta'] = data['core'][0]-data['cap'][0]+totals[0]
        if any(not bool(torch.isfinite(value.detach()).all()) for value in result.values()):
            self._fail('Nonfinite complete zero-closure physical field')
        self.counts['evaluated_field_points'] += len(query['cells'])*len(phi)
        return result

    def _raw_block(self, x, begin, end):
        fields = self.fields_torch(x, self.grid_query, self.phi[begin:end],
                                  curvature=False, query_label='grid')
        V, W = fields['Fs'], fields['Fphi']
        denominator = tensor(self.a)[:, None]*fields['rho0'][None]
        e = (V*V).sum(-1)-1
        f = (V*W).sum(-1)/denominator
        c = (W*W).sum(-1)/(denominator*denominator)-1
        # Keep ALL original Gram rows, including the numerical evaluation
        # of the structurally zero radial error. The fixed g is unchanged.
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
        finite_or_none = lambda value: float(value) if math.isfinite(value) else None
        grid_keys = {float(value).hex() for value in self.phi}
        base_metadata = self.base.metadata()
        # This wrapper never calls the base's finite-Newton core path.
        # Its untouched +inf minimum is an unused diagnostic, not a read.
        # Keep the actual base definition/source and report absence as null;
        # do not copy the wrapper's successful values into another source.
        base_metadata.update(base_core_inverse_path_used=False,
            maximum_actual_inverse_chart_residual=None,
            minimum_actual_inverse_root_rho=None,
            metadata_scope='actual base definition and provider metadata; base hDelta/core/J field paths are not used',
            actual_counts_scope='shared low-level counter dictionary; wrapper updates included, no per-source count separation claimed')
        return dict(schema=SCHEMA, source_sha256=sha(__file__),
            model=self.model, model_identity_sha256=self.identity,
            base_source_sha256=self.base_source_sha256,
            base_complete_metadata=base_metadata,
            frozen_moment_Q_definition_identity_sha256=self.frozen_moment_identity,
            frozen_moment_Q_definition=self.frozen_moment_definition,
            literal_Q_input_schema=self.literal_Q_input_schema,
            new_reference_input_binding_source_sha256=self.new_reference_input_binding_source_sha256,
            historical_reference_same_mathematical_g_claimed=False,
            Q_input_recomputed_at_current_point=False,
            actual_working_moment_inverse_is_not_a_continuous_certificate=True,
            historical_original_three_root_algorithm_source_sha256=ORIGINAL_COMPLETE_ENDPOINT_SOURCE_SHA256,
            free_variables=int(self.free_size), free_core_variables=int(self.core_size),
            free_rotation_variables=int(self.rotation_size), all_free_height_variables=1,
            current_full_point_sha256=self._current_point_sha256,
            working_integration_order=int(self.integration_order),
            endpoint_root_policy=self.policy.metadata(),
            endpoint_continuation_policy=self.continuation_policy.metadata(),
            endpoint_continuation_counts=dict(self.endpoint_continuation_counts),
            endpoint_continuation_last_summary=self._continuation_summary(),
            endpoint_continuation_last_batch=self._last_continuation_batch,
            continuation_counts_scope='actual complete-batch nine-KKT evaluations and separate full K matrices (including their internal retained constraint-Hessian graphs); Newton updates include subsequently rejected continuation stages',
            continuation_trajectory_differentiated=False,
            final_implicit_J_uses_original_KKT_equation=True,
            auxiliary_parameter_is_physical_t=False,
            current_cached_angle_roots=len(self._root_cache),
            current_all_grid_angle_roots_available=grid_keys.issubset(self._root_cache),
            current_maximum_endpoint_residual=max((v['numerical_endpoint_residual_norm'] for v in records), default=None),
            current_maximum_dimensionless_control_norm=max((v['dimensionless_control_norm'] for v in records), default=None),
            current_maximum_multiplier_norm=max((v['multiplier_norm'] for v in records), default=None),
            current_maximum_KKT_residual=max((v['numerical_KKT_residual_norm'] for v in records), default=None),
            current_maximum_stationarity_residual=max((v['numerical_stationarity_residual_norm'] for v in records), default=None),
            current_maximum_physical_z_norm=max((v['physical_z_norm'] for v in records), default=None),
            current_maximum_gamma_axis_norm=max((v['gamma_axis_norm'] for v in records), default=None),
            current_minimum_KKT_sample_singular_value=min((v['actual_KKT_smallest_singular_value'] for v in records), default=None),
            current_maximum_first_angular_root_residual=max(
                (v['angular_jet_residual_norms'][1] for v in records), default=None),
            current_maximum_second_angular_root_residual=max(
                (v['angular_jet_residual_norms'][2] for v in records
                 if len(v['angular_jet_residual_norms']) == 3), default=None),
            all_attempted_fields_maximum_successful_endpoint_residual=(self.maximum_endpoint_root_residual if self.endpoint_counts['root_angles_solved'] else None),
            all_attempted_fields_maximum_successful_dimensionless_control_norm=(self.maximum_endpoint_correction_norm if self.endpoint_counts['root_angles_solved'] else None),
            all_attempted_fields_maximum_successful_KKT_residual=(self.maximum_kkt_root_residual if self.endpoint_counts['root_angles_solved'] else None),
            all_attempted_fields_maximum_successful_multiplier_norm=(self.maximum_multiplier_norm if self.endpoint_counts['root_angles_solved'] else None),
            all_attempted_fields_minimum_sample_KKT_singular_value=finite_or_none(
                self.minimum_endpoint_sample_singular_value),
            all_attempted_fields_maximum_core_inverse_residual=self.maximum_core_inverse_residual,
            all_attempted_fields_minimum_core_inverse_sample_rho=finite_or_none(self.minimum_core_inverse_sample_rho),
            endpoint_counts=dict(self.endpoint_counts), actual_field_counts=dict(self.counts),
            last_root_failure=self._last_root_failure,
            J_method='complete first-parameter implicit 18x18 metric / 27x27 six-jet KKT system; all multipliers and constraint-Hessian derivatives retained',
            implicit_control_dimension=CONTROL_DIMENSION, KKT_dimension=KKT_DIMENSION,
            complete_second_angular_implicit_dimension=27,
            exact_relative_gamma_nodes=[str(value) for value in self.gamma_nodes],
            implicit_control_cost='(|z/S|^2+|v|^2)/2',
            selected_KKT_stationary_branch=True, SOSC_verified=False,
            global_minimum_verified=False, actual_KKT_counts=dict(self.kkt_counts),
            actual_KKT_counter_scope='angle-equation and retained-graph reverse products; every attempted nine-dimensional solve counts before success, including rejected stages and failures; implicit matrix rows count all angle rows assembled',
            old_selected_root_or_field_inherited=False,
            maximum_required_mixed_exponential_derivative_order=4,
            rotation_coefficient_source_sha256=self.base_source_sha256,
            rotation_small_branch='z=|w|^2 < 1/4; same degree-12 A/B polynomials and their exact first/second polynomial derivatives; further mixed derivatives use their retained graph',
            unused_large_rotation_branch='same source clamps scalar z to >=1/4 before sqrt/division; no zero denominator',
            rotation_truncation_branch_seam_or_rounding_error_enclosed=False,
            Jtranspose_method='autograd transpose of the SAME complete first-parameter implicit graph',
            core_inverse_J='value-preserving -Theta_c,c/rho_c implicit derivative at actual numerical root',
            numerical_Newton_iterations_differentiated=False,
            second_parameter_derivatives_supported_by_surrogate=False,
            finite_difference_J=False, all_metric_mean_and_cross_rows_retained=True,
            fixed_target_recomputed_from_current_field=False,
            radial_metric_identity_in_exact_definition=True,
            numerical_radial_Gram_row_omitted=False,
            integration_error_enclosed=False, symbolic_mesh_carrier_rounding_error_enclosed=False,
            endpoint_root_error_enclosed=False, complete_uniform_IFT_conditions_verified=False,
            angular_root_jets_outward_enclosed=False,
            complete_continuous_root_branch_certified=False,
            old_metric_or_geometry_certificates_inherited=False,
            closed_exact_isometry_certified=False,
            scope='Actual finite NEW added-gamma six-control nine-KKT stationary candidate with complete 27-jet implicit first derivatives; continuous branch/quad/SOSC/geometry/refinement remain')
