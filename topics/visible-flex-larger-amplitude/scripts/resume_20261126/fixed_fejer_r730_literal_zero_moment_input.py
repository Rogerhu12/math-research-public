#!/usr/bin/env python3
"""Bind eighteen fixed Q words to one complete R730 safe-cone length seed.

This is a separate complete input type.  The old 05dc definition and its
actual trace are parameter origins, never identities of the current base,
reference, scalar target, chart or initial point.  No moment, inverse,
endpoint root, F, J, Jtranspose or scientific array is read or computed.
The caller first constructs and validates its complete actual reference and
fixed global safe-cone provider.  This pure binder then binds both complete JSON
models and supplied actual byte identities.  Old same-reference and ea94
new-reference validators remain unchanged.  The complete provider, length/inverse-arclength
kernel and base operator are independently pinned by their exact source bytes.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


SCHEMA = 'fixed-fejer-r730-reference-literal-zero-endpoint-Q-input-v1'
DEFINITION_SCHEMA = 'fixed-fejer-r730-reference-literal-two-bubble-endpoint-Q-v1'
ORIGIN_SCHEMA = 'frozen-zero-endpoint-moment-Q-input-v1'
ORIGIN_DEFINITION_SCHEMA = 'literal-two-bubble-endpoint-Q-v1'
ORIGIN_DEFINITION_SHA = '05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e'
ORIGIN_PARAMETER_FILE_SHA = 'df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c'
ORIGIN_PARAMETER_FILE_BYTES = 3618
ORIGIN_PARAMETER_PATH = 'topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json'
ORIGIN_TRACE_REPORT_SHA = '26b094fef8baf6ff2ecdda5d1a0f5a8be7383e5171733320be959a22d83cb47e'
ORIGIN_TRACE_SOURCE_SHA = '73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54'
BASE_SCHEMA = 'complete-fixed-fejer-r730-so3-meridian-with-core-lift-v1'
BASE_SOURCE_SHA = 'b9c787340021b5736f2796f2b84a1c25cb4b0ce96333eb98f543b1e8923ce267'
SEED_SCHEMA = 'complete-fixed-fejer-R730-safe-cone-arclength-reference-v1'
SEED_PROVIDER_SOURCE_SHA = '53ebce095394a833d95a65b834ae889b4cb9554e06ef839fcb626bddcb8864b8'
LENGTH_KERNEL_SOURCE_SHA = '87be2efa7381f50bd419c0d91a3b0c5b1a762f9f1eb7d1f2f7a053f8bc93cfc2'
PULSE_FLATNESS = 6
LENGTH_DEFINITION_SCHEMA = 'R730-global-single-pulse-contracted-Bezier-physical-definition-v1'
PARENT_COMPLETE_BINDER_SOURCE_SHA = '872dca4cf1e15c419aad68d31c053fc4f3465357a3e162413a19002f5b70e43d'
REFERENCE_SCHEMA = 'R690-fixed-fejer-axisymmetric-SO3-reference-input-v1'
REFERENCE_SOURCE_SHA = 'e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb'
SCALAR_SCHEMA = 'fullhold-deep-valley-flat-tail-input-v1'
SCALAR_SOURCE_SHA = 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
EXACT_BUBBLE_NODES = (('1/32', '1/4', '15/32'), ('17/32', '3/4', '31/32'))
LITERAL_Q_WORDS = (
    (('0x0.0p+0', '-0x1.f54b784ca956ap-1', '0x0.0p+0'),
     ('0x1.972524c4f8e87p+0', '0x0.0p+0', '-0x1.e6c4f7d8b8182p+0'),
     ('0x0.0p+0', '0x1.956cca02ca83bp-3', '0x0.0p+0')),
    (('0x0.0p+0', '-0x1.7be87d3213c4cp-1', '0x0.0p+0'),
     ('0x1.03bb57b63d53dp-1', '0x0.0p+0', '0x1.41266339b41f3p+1'),
     ('0x0.0p+0', '-0x1.3dc38eaa8f3a4p-1', '0x0.0p+0')),
)
DEFINITION_KEYS = {
    'schema', 'Q0_binary64_hex', 'exact_relative_bubble_nodes',
    'fixed_scalar_metric_identity_sha256', 'fixed_scalar_profile_definition',
    'initial_reference_bundle_sha256', 'initial_reference_model_identity_sha256',
    'base_model_identity_sha256', 'initial_full_point_sha256',
    'fixed_chart_core_sha256',
    'fixed_safe_cone_unit_seed_model', 'fixed_safe_cone_unit_seed_identity_sha256',
}
OUTER_KEYS = {'schema', 'definition', 'definition_identity_sha256', 'provenance'}


def sha(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            result.update(block)
    return result.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def json_copy(value):
    return json.loads(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False))


def is_digest(value):
    return isinstance(value, str) and len(value) == 64 and all(c in '0123456789abcdef' for c in value)


def require_digest(value, name):
    if not is_digest(value):
        raise ValueError('Use a complete actual SHA256 for '+name)
    return value


def _nodes(value):
    if (not isinstance(value, (list, tuple)) or len(value) != 2
            or any(not isinstance(row, (list, tuple)) or len(row) != 3 for row in value)):
        raise ValueError('Keep both complete exact relative bubble triples')
    # Fraction strings and actual Fraction objects are exact.  Float input
    # is rejected even if its rounded value looks like a desired endpoint.
    if any(not isinstance(v, (str, Fraction)) for row in value for v in row):
        raise ValueError('Bubble endpoints must be exact Fraction strings or Fraction values')
    result = [[str(Fraction(v)) for v in row] for row in value]
    if result != [list(row) for row in EXACT_BUBBLE_NODES]:
        raise ValueError('This complete literal input uses the declared wide disjoint supports')
    return result


def _words(value):
    if (not isinstance(value, list) or len(value) != 2
            or any(not isinstance(matrix, list) or len(matrix) != 3 for matrix in value)
            or any(not isinstance(row, list) or len(row) != 3 for matrix in value for row in matrix)):
        raise ValueError('Keep exactly eighteen literal binary64 words of shape (2,3,3)')
    result = []
    for matrix in value:
        rows = []
        for i, row in enumerate(matrix):
            numbers = []
            for j, word in enumerate(row):
                if not isinstance(word, str):
                    raise ValueError('Every Q parameter must remain a canonical binary64 hex word')
                number = float.fromhex(word)
                if not math.isfinite(number) or number.hex() != word:
                    raise ValueError('Do not round, normalize or replace any literal finite Q word')
                if not ((i == 1) != (j == 1)) and number != 0:
                    raise ValueError('The fixed matrices must retain exact polar-to-axial reflection parity')
                numbers.append(number)
            rows.append(numbers)
        result.append(rows)
    if value != [[list(row) for row in matrix] for matrix in LITERAL_Q_WORDS]:
        raise ValueError('This input adopts all eighteen published words, without a new fitted inverse')
    return result


def _validate_origin(value):
    if not isinstance(value, dict) or value.get('schema') != ORIGIN_SCHEMA:
        raise ValueError('Use the complete already published original fixed-Q parameter input')
    definition = value.get('definition')
    if (not isinstance(definition, dict)
            or definition.get('schema') != ORIGIN_DEFINITION_SCHEMA
            or canonical(definition) != ORIGIN_DEFINITION_SHA
            or value.get('definition_identity_sha256') != ORIGIN_DEFINITION_SHA
            or definition.get('trace_report_sha256') != ORIGIN_TRACE_REPORT_SHA
            or definition.get('trace_source_sha256') != ORIGIN_TRACE_SOURCE_SHA):
        raise ValueError('The old complete 05dc input is a fixed parameter origin, not a current target')
    _words(definition['Q0_binary64_hex'])
    if definition['exact_relative_bubble_nodes'] != _nodes(definition['exact_relative_bubble_nodes']):
        raise ValueError('The original complete support strings must remain canonical')
    provenance = value.get('provenance')
    if (not isinstance(provenance, dict)
            or provenance.get('actual_trace_report', {}).get('sha256') != ORIGIN_TRACE_REPORT_SHA
            or provenance.get('new_control_parameters') != 18
            or provenance.get('current_free_variables_never_recompute_Q') is not True
            or provenance.get('working_matrix_is_exact_true_endpoint_right_inverse_claimed') is not False):
        raise ValueError('Retain the actual origin and its numerical-moment limitations')
    return json_copy(definition)


def _canonical_positive_word(value,name,*,upper=None):
    if not isinstance(value,str):
        raise ValueError("Keep a canonical binary64 hex word for "+name)
    try:number=float.fromhex(value)
    except ValueError as error:raise ValueError("Invalid "+name) from error
    if (not math.isfinite(number) or number.hex()!=value or number<=0
            or (upper is not None and number>=upper)):
        raise ValueError("Keep the complete finite positive "+name)
    return number


def _length_definition(value):
    """Pure reconstruction of the complete 87be physical/working declaration."""
    if not isinstance(value,dict):
        raise ValueError("Retain the complete new length/inverse-arclength definition")
    orders=value.get("declared_original_orders");budgets=value.get("complete_root_budgets")
    if (not isinstance(orders,dict)
            or set(orders)!={"radial_quadrature_order","profile_quadrature_order"}
            or not isinstance(budgets,dict)
            or set(budgets)!={"mean_maxiter","scalar_iterations","mean_backtracks"}):
        raise ValueError("Retain all original declared orders and every complete scalar-root budget")
    ints=dict(orders,**budgets)
    if any(type(v) is not int or v<1 for v in ints.values()):
        raise ValueError("Keep all five positive complete integer rule parameters")
    if min(ints["radial_quadrature_order"],ints["profile_quadrature_order"])<4:
        raise ValueError("Keep both complete positive Gauss orders at least four")
    tolerance=_canonical_positive_word(value.get("root_tolerance_hex"),"length root tolerance")
    armijo=_canonical_positive_word(value.get("armijo_hex"),"length Armijo coefficient",upper=1)
    eta,maximum=Fraction("1/32"),Fraction("3/4")
    expected = dict(schema=LENGTH_DEFINITION_SCHEMA,proof_result="R730",
        exact_handle_length=str(eta),exact_maximum_contraction=str(maximum),
        pulse_flatness=PULSE_FLATNESS,pulse="(1-(2*t-1)^12)^7",
        pulse_is_one_global_polynomial=True,polynomial_degree=84,
        internal_formula_cuts=[],endpoint_vanishing_derivatives=list(range(7)),
        controls=["Gamma","Gamma+eta*ez",
            "Gamma+2*eta*ez+(5/4)*kappa0*eta^2*er(Theta)",
            "(R+2*eta)*er(Theta)+H0*ez","(R+eta)*er(Theta)+H0*ez","R*er(Theta)+H0*ez"],
        baseline="sum_{j=0}^5 binom(5,j)t^j(1-t)^(5-j)P_j",
        z_depends_on_phi=False,
        contracted_curve="G_xi=((1-xi*psi)*baseline_xy,baseline_z)",
        accurate_length_equation="integral_0^1 |d_t G_xi| dt = S",
        accurate_root_range="0 < xi(phi) < 3/4",
        accurate_inverse_equation="integral_0^t |d_u G_xi(phi)| du = s",
        accurate_field="F(s,phi)=G_xi(phi)(t(s,phi),phi)",
        accurate_unit_reference="T0=F_s",
        complete_domain="all s in [0,S] and every original fixed-chart angle",
        original_fixed_scalar_chart_and_target_unchanged=True,
        old_support_complement_boundary_width_and_profile_delta_used=False,
        old_R709_R722_R726_R727_mean_or_branch_certificate_inherited=False,
        working_full_cell_rule="all original normalized material mesh cells; full positive Gauss",
        working_order=max(ints["radial_quadrature_order"],ints["profile_quadrature_order"]),
        declared_original_orders={n:ints[n] for n in (
            "radial_quadrature_order","profile_quadrature_order")},
        working_inverse_rule=(
            "full positive prefix table and same positive Gauss rule on each required "
            "partial cell; target (s/S)*actual_total_length"),
        working_angle_chain=(
            "two implicit length-root jets and two inverse-arclength jets of the "
            "accurate expressions, evaluated with complete working quadratures"),
        complete_root_budgets={n:ints[n] for n in (
            "mean_maxiter","scalar_iterations","mean_backtracks")},
        root_tolerance_hex=tolerance.hex(),armijo_hex=armijo.hex(),
        working_partial_integral_monotonicity_or_exact_discrete_derivatives_claimed=False,
        quadrature_root_inverse_trigonometry_and_rounding_errors_enclosed=False,
        original_outer_whole_cell_integration_and_normal32_are_separate=True)

    if value!=expected:
        raise ValueError("The whole exact R730 recipe, working rule or unpaid-error scope changed")
    return expected


def _safe_cone_seed(seed_model, *, reference, reference_id,
                    initial_reference_bundle_sha256,
                    fixed_scalar_metric_identity_sha256,
                    profile, fixed_chart_core_sha256, bubble_nodes):
    """Full new seed JSON; no length root, inverse, array, field or old mean."""
    for value,name in ((SEED_PROVIDER_SOURCE_SHA,"complete R730 provider"),
                       (LENGTH_KERNEL_SOURCE_SHA,"complete R730 length kernel")):
        require_digest(value,name)
    if not isinstance(seed_model,dict):
        raise ValueError("Retain the entire R730 frozen seed model")
    seed=json_copy(seed_model)
    length=_length_definition(seed.get("complete_safe_cone_definition"))
    _nodes(bubble_nodes)
    height_word=seed.get("initial_height_hex")
    _canonical_positive_word(height_word,"fixed seed height")
    radius_word=seed.get("radius_carrier_hex")
    _canonical_positive_word(radius_word,"fixed R690 radius")
    if radius_word!=reference.get("radius_carrier_hex"):
        raise ValueError("The new reference must use the same complete R690 radius")
    raw_kappa=seed.get("exact_core_radial_curvature")
    if not isinstance(raw_kappa,str):
        raise ValueError("Keep the actual original exact core-curvature Fraction")
    try:kappa=Fraction(raw_kappa)
    except (ValueError,ZeroDivisionError) as error:
        raise ValueError("Invalid exact original core-curvature parameter") from error
    if str(kappa)!=raw_kappa:
        raise ValueError("Keep canonical original exact kappa0; no new fitted curvature")
    working=seed.get("working_definition")
    if not isinstance(working,dict):
        raise ValueError("Retain the complete R730 working definition")
    S_word=working.get("physical_S_carrier_hex")
    _canonical_positive_word(S_word,"same original physical S carrier")
    S_definition=working.get("exact_S_definition")
    if not isinstance(S_definition,dict) or not S_definition:
        raise ValueError("Retain the complete original exact S enclosure record")
    json_copy(S_definition)
    nodes=working.get("original_material_affine_nodes")
    if (not isinstance(nodes,list) or len(nodes)!=923
            or any(not isinstance(row,list) or len(row)!=2 for row in nodes)
            or any(not isinstance(v,str) for row in nodes for v in row)):
        raise ValueError("Retain all 923 original exact-affine material nodes")
    try:normalized=[[str(Fraction(v)) for v in row] for row in nodes]
    except (ValueError,ZeroDivisionError) as error:
        raise ValueError("Invalid exact original affine material address") from error
    if normalized!=nodes or nodes[0]!=["0","0"] or nodes[-1]!=["1","0"]:
        raise ValueError("Keep the complete canonical affine source domain including 0 and S")
    expected_working=dict(
        schema="complete-R730-safe-cone-reference-working-definition-v1",
        length_kernel_source_sha256=LENGTH_KERNEL_SOURCE_SHA,
        complete_length_definition=length,
        exact_S_definition=S_definition,
        physical_S_carrier_hex=S_word,
        original_material_affine_nodes=nodes,
        full_original_material_cells=922,
        working_quadrature_partition=(
            "every original increasing material mesh carrier divided by the same S "
            "carrier; this complete partition is a working rule, not a new target"),
        root_identity_includes_literal_angle_and_full_frozen_model=True,
        inverse_queries_use_original_affine_material_addresses=True,
        original_bubbles_raw_defect_lift_outer_full_cell_Gauss_and_normal32_are_separate=True,
        working_inverse_normalizes_actual_total_length_to_full_S=True,
        working_primitive_equals_integral_of_returned_unit_T0_claimed=False,
        working_errors_enclosed=False)
    if working!=expected_working:
        raise ValueError("Keep the entire actual reference partition, both inverse chains and unpaid working defects")
    expected_seed=dict(schema=SEED_SCHEMA,source_sha256=SEED_PROVIDER_SOURCE_SHA,
        original_reference_source_sha256=REFERENCE_SOURCE_SHA,
        length_kernel_source_sha256=LENGTH_KERNEL_SOURCE_SHA,
        complete_axisymmetric_reference_model=reference,
        initial_reference_model_identity_sha256=reference_id,
        initial_reference_bundle_sha256=initial_reference_bundle_sha256,
        fixed_scalar_metric_identity_sha256=fixed_scalar_metric_identity_sha256,
        fixed_scalar_profile_definition=profile,
        fixed_chart_core_sha256=fixed_chart_core_sha256,
        initial_height_hex=height_word,radius_carrier_hex=radius_word,
        exact_core_radial_curvature=raw_kappa,exact_physical_handle_length="1/32",
        exact_maximum_contraction="3/4",
        complete_safe_cone_definition=length,
        core_cap_control_jets="R730 complete six controls, original kappa0 and fixed Gamma/Theta",
        reference_height_is_declared_working_word_not_exact_scalar_integral=True,
        accurate_S_R_chart_from_complete_original_definition=True,
        scalar_and_S_carriers_not_promoted_to_exact_values=True,
        seed_is_frozen_from_original_initial_point=True,
        current_outer_core_H_and_all_rotation_variables_are_not_seed_inputs=True,
        original_scalar_reference_outside_old_supports_retained=False,
        old_mean_v_d_w_lambda_arrays_or_roots_inherited=False,
        accurate_reference="G(xi(phi),t(s,phi),phi), complete scalar length and inverse equations",
        accurate_T0="the arclength unit tangent of that same complete G",
        working_definition=expected_working)
    if seed!=expected_seed:
        raise ValueError("Bind all and only the complete actual R730 model and its original fixed input")
    return seed,canonical(seed)


def _current_binding(*, base_model, initial_reference_bundle_sha256,
                     fixed_scalar_metric_identity_sha256, initial_full_point_sha256,
                     bubble_nodes):
    """Check the complete actual JSON reference, without evaluating its arrays."""
    require_digest(initial_reference_bundle_sha256, 'current initial reference bundle')
    require_digest(fixed_scalar_metric_identity_sha256, 'current fixed scalar metric')
    require_digest(initial_full_point_sha256, 'current complete base initial point')
    if not isinstance(base_model, dict):
        raise ValueError('Supply the complete actual base model, not a replacement digest')
    require_digest(BASE_SOURCE_SHA, 'locked complete R730 safe-cone base source')
    base = json_copy(base_model)
    reference = base.get('complete_axisymmetric_reference_model')
    if not isinstance(reference, dict):
        raise ValueError('The current complete base must retain the whole independent reference model')
    profile = reference.get('fixed_scalar_profile_definition')
    if not isinstance(profile, dict):
        raise ValueError('Retain the complete current fixed scalar profile definition')
    reference_id = canonical(reference)
    if (reference.get('predeclared_fixed_chart_from_rational_recipe') is not True
            or reference.get('warm_or_BVP_core_consumed') is not False
            or reference.get('same_previous_target_claimed') is not False
            or canonical(reference.get('mathematical_target_recipe'))!=reference.get('mathematical_target_identity_sha256')):
        raise ValueError('Bind the predeclared Fejer target without an old optimized chart identity')
    if (base.get('schema') != BASE_SCHEMA or base.get('source_sha256') != BASE_SOURCE_SHA
            or base.get('reference_meridian_kernel_sha256') != SEED_PROVIDER_SOURCE_SHA
            or base.get('original_axisymmetric_reference_source_sha256') != REFERENCE_SOURCE_SHA
            or reference.get('schema') != REFERENCE_SCHEMA
            or reference.get('source_sha256') != REFERENCE_SOURCE_SHA
            or profile.get('schema') != SCALAR_SCHEMA
            or profile.get('source_sha256') != SCALAR_SOURCE_SHA
            or canonical(profile) != fixed_scalar_metric_identity_sha256
            or base.get('fixed_scalar_metric_identity_sha256') != fixed_scalar_metric_identity_sha256
            or reference.get('fixed_scalar_metric_identity_sha256') != fixed_scalar_metric_identity_sha256
            or base.get('fixed_scalar_profile_definition') != profile
            or base.get('initial_reference_bundle_sha256') != initial_reference_bundle_sha256
            or base.get('initial_reference_model_identity_sha256') != reference_id):
        raise ValueError('Bind this actual complete R730 safe-cone base/4e/e091 target, without old physical-source identity substitution')
    for key in ('fixed_chart_core_sha256', 'mesh_sha256'):
        require_digest(base.get(key), 'base '+key)
        if base.get(key) != reference.get(key):
            raise ValueError('The actual full base/reference disagree on '+key)
    if (base.get('M') != 160 or base.get('J') != 923
            or reference.get('M') != 160 or reference.get('J') != 923
            or base.get('fixed_core_first3') != reference.get('fixed_core_first3')
            or base.get('radius_hex') != reference.get('radius_carrier_hex')
            or base.get('all_current_free_core_coefficients_retained') is not True
            or base.get('current_height_free') is not True
            or reference.get('all_original_free_core_coefficients_retained') is not True
            or reference.get('old_optimized_q_field_required') is not False
            or reference.get('old_nonlinear_directions_required') is not False):
        raise ValueError('Retain the whole current finite trial space, all free core/H, chart and full reference')
    first = reference.get('fixed_core_first3')
    if not isinstance(first, list) or len(first) != 3:
        raise ValueError('The current reference must retain its exact first three core words')
    for word in first+[reference.get('radius_carrier_hex')]:
        if not isinstance(word, str):
            raise ValueError('Actual fixed core/radius words must remain explicit')
        number = float.fromhex(word)
        if not math.isfinite(number) or number.hex() != word:
            raise ValueError('The current base/reference contains a noncanonical carrier word')
    for key in ('scalar_input_sha256', 'original_scalar_parameters_identity_sha256',
                'symbolic_node_report_sha256', 'fixed_input_bundle_sha256',
                'observation_carrier_sha256', 'a_observations_sha256'):
        require_digest(reference.get(key), 'current reference '+key)
    seed, seed_identity = _safe_cone_seed(base.get('fixed_safe_cone_unit_seed_model'),
        reference=reference, reference_id=reference_id,
        initial_reference_bundle_sha256=initial_reference_bundle_sha256,
        fixed_scalar_metric_identity_sha256=fixed_scalar_metric_identity_sha256,
        profile=profile, fixed_chart_core_sha256=base['fixed_chart_core_sha256'],
        bubble_nodes=bubble_nodes)
    if (base.get('fixed_safe_cone_unit_seed_identity_sha256') != seed_identity
            or base.get('fixed_safe_cone_unit_seed_source_sha256') != SEED_PROVIDER_SOURCE_SHA
            or base.get('fixed_safe_cone_unit_seed_length_kernel_sha256') != LENGTH_KERNEL_SOURCE_SHA
            or base.get('fixed_safe_cone_unit_seed_working_definition') != seed['working_definition']):
        raise ValueError('The complete new base must retain the same frozen seed identity, both real sources and full working rule')
    return dict(schema=DEFINITION_SCHEMA,
        Q0_binary64_hex=[[list(row) for row in matrix] for matrix in LITERAL_Q_WORDS],
        exact_relative_bubble_nodes=_nodes(bubble_nodes),
        fixed_scalar_metric_identity_sha256=fixed_scalar_metric_identity_sha256,
        fixed_scalar_profile_definition=profile,
        initial_reference_bundle_sha256=initial_reference_bundle_sha256,
        initial_reference_model_identity_sha256=reference_id,
        base_model_identity_sha256=canonical(base),
        initial_full_point_sha256=initial_full_point_sha256,
        fixed_chart_core_sha256=base['fixed_chart_core_sha256'],
        fixed_safe_cone_unit_seed_model=seed,
        fixed_safe_cone_unit_seed_identity_sha256=seed_identity)


def validate_definition(definition, expected_identity=None):
    if not isinstance(definition, dict) or set(definition) != DEFINITION_KEYS:
        raise ValueError('Keep exactly the declared complete R730 safe-cone input fields')
    if definition.get('schema') != DEFINITION_SCHEMA:
        raise ValueError('Use the independent complete R730 safe-cone mathematical control type')
    _words(definition['Q0_binary64_hex'])
    if definition['exact_relative_bubble_nodes'] != _nodes(definition['exact_relative_bubble_nodes']):
        raise ValueError('Keep the exact canonical complete bubble support strings')
    for key in ('fixed_scalar_metric_identity_sha256', 'initial_reference_bundle_sha256',
                'initial_reference_model_identity_sha256', 'base_model_identity_sha256',
                'initial_full_point_sha256', 'fixed_chart_core_sha256'):
        require_digest(definition[key], key)
    profile = definition['fixed_scalar_profile_definition']
    if (not isinstance(profile, dict) or profile.get('schema') != SCALAR_SCHEMA
            or profile.get('source_sha256') != SCALAR_SOURCE_SHA
            or canonical(profile) != definition['fixed_scalar_metric_identity_sha256']):
        raise ValueError('The new complete input must retain and identify its actual fixed scalar law')
    seed_model = definition['fixed_safe_cone_unit_seed_model']
    if not isinstance(seed_model, dict):
        raise ValueError('Keep the whole actual safe-cone seed in the fixed input')
    reference = seed_model.get('complete_axisymmetric_reference_model')
    if (not isinstance(reference, dict)
            or reference.get('schema') != REFERENCE_SCHEMA
            or reference.get('source_sha256') != REFERENCE_SOURCE_SHA
            or canonical(reference) != definition['initial_reference_model_identity_sha256']
            or reference.get('fixed_scalar_profile_definition') != profile
            or reference.get('fixed_scalar_metric_identity_sha256') != definition['fixed_scalar_metric_identity_sha256']
            or reference.get('fixed_chart_core_sha256') != definition['fixed_chart_core_sha256']):
        raise ValueError('The seed must retain this whole actual 4e reference and exact fixed target/chart')
    seed, seed_identity = _safe_cone_seed(seed_model, reference=reference,
        reference_id=definition['initial_reference_model_identity_sha256'],
        initial_reference_bundle_sha256=definition['initial_reference_bundle_sha256'],
        fixed_scalar_metric_identity_sha256=definition['fixed_scalar_metric_identity_sha256'],
        profile=profile, fixed_chart_core_sha256=definition['fixed_chart_core_sha256'],
        bubble_nodes=definition['exact_relative_bubble_nodes'])
    require_digest(definition['fixed_safe_cone_unit_seed_identity_sha256'], 'complete fixed R730 safe-cone seed')
    if definition['fixed_safe_cone_unit_seed_identity_sha256'] != seed_identity:
        raise ValueError('The whole safe-cone seed definition changed')
    identity = canonical(definition)
    if expected_identity is not None:
        require_digest(expected_identity, 'explicit current input definition')
        if identity != expected_identity:
            raise ValueError('The explicitly fixed complete R730 safe-cone input changed')
    return identity


def _validate_outer(value):
    if (not isinstance(value, dict) or set(value) != OUTER_KEYS
            or value.get('schema') != SCHEMA):
        raise ValueError('Use the separate complete R730 safe-cone literal-Q input type')
    identity = validate_definition(value['definition'], value.get('definition_identity_sha256'))
    if value.get('definition_identity_sha256') != identity:
        raise ValueError('The complete R730 safe-cone definition identity is missing or altered')
    p = value['provenance']
    if (not isinstance(p, dict)
            or p.get('binding_source_sha256') != sha(__file__)
            or p.get('origin_definition_identity_sha256') != ORIGIN_DEFINITION_SHA
            or p.get('origin_trace_report_sha256') != ORIGIN_TRACE_REPORT_SHA
            or p.get('origin_trace_source_sha256') != ORIGIN_TRACE_SOURCE_SHA
            or p.get('new_control_parameters') != 18
            or p.get('current_free_variables_never_recompute_Q') is not True
            or p.get('same_mathematical_g_claimed') is not False
            or p.get('current_working_moment_inverse_claimed') is not False
            or p.get('current_exact_endpoint_right_inverse_claimed') is not False
            or p.get('origin_current_model_or_reference_identity_inherited') is not False
            or p.get('original_root_or_field_success_inherited') is not False
            or p.get('true_moment_error_or_uniform_IFT_certified') is not False
            or p.get('complete_current_field_validated_by_this_pure_binder') is not False
            or p.get('safe_cone_unit_seed_is_frozen_before_current_free_point') is not True
            or p.get('fixed_scalar_target_rechosen_by_this_binder') is not False
            or p.get('permanent_location_or_constraint_history_removed_by_this_binder') is not False):
        raise ValueError('Keep old parameter provenance separate from every current scientific claim')
    origin = p.get('complete_origin_definition')
    if not isinstance(origin, dict) or canonical(origin) != ORIGIN_DEFINITION_SHA:
        raise ValueError('Retain the complete published parameter-origin definition as provenance only')
    if origin.get('Q0_binary64_hex') != value['definition']['Q0_binary64_hex']:
        raise ValueError('All eighteen selected literal parameters must agree with the recorded origin')
    return identity


def bind_new_input(origin_value, *, base_model, initial_reference_bundle_sha256,
                   fixed_scalar_metric_identity_sha256, initial_full_point_sha256,
                   bubble_nodes):
    origin = _validate_origin(origin_value)
    definition = _current_binding(base_model=base_model,
        initial_reference_bundle_sha256=initial_reference_bundle_sha256,
        fixed_scalar_metric_identity_sha256=fixed_scalar_metric_identity_sha256,
        initial_full_point_sha256=initial_full_point_sha256, bubble_nodes=bubble_nodes)
    value = dict(schema=SCHEMA, definition=definition,
        definition_identity_sha256=validate_definition(definition),
        provenance=dict(binding_source_sha256=sha(__file__),
            origin_definition_identity_sha256=ORIGIN_DEFINITION_SHA,
            complete_origin_definition=origin,
            origin_trace_report_sha256=ORIGIN_TRACE_REPORT_SHA,
            origin_trace_source_sha256=ORIGIN_TRACE_SOURCE_SHA,
            published_origin_parameter_file=dict(repo_relative_path=ORIGIN_PARAMETER_PATH,
                sha256=ORIGIN_PARAMETER_FILE_SHA, bytes=ORIGIN_PARAMETER_FILE_BYTES),
            origin_parameter_file_bytes_reread_by_this_call=False,
            input_selection='Adopt the same eighteen published binary64 words as new fixed control parameters',
            current_binding='This complete R730 safe-cone base, whole frozen seed, original reference, fixed scalar/chart and base.initial identity',
            parent_complete_binder_source_sha256=PARENT_COMPLETE_BINDER_SOURCE_SHA,
            safe_cone_unit_seed_is_frozen_before_current_free_point=True,
            fixed_scalar_target_rechosen_by_this_binder=False,
            fixed_seed_change_does_not_assert_a_changed_mathematical_metric=True,
            old_binding_scope='Only a historical origin for eighteen scalar parameters; no current-source, target, point or reference identity',
            current_free_variables_never_recompute_Q=True,
            new_control_parameters=18,
            same_mathematical_g_claimed=False,
            current_working_moment_inverse_claimed=False,
            current_exact_endpoint_right_inverse_claimed=False,
            origin_current_model_or_reference_identity_inherited=False,
            original_root_or_field_success_inherited=False,
            true_moment_error_or_uniform_IFT_certified=False,
            complete_current_field_validated_by_this_pure_binder=False,
            current_base_array_and_source_validation_remains_callers_responsibility=True,
            permanent_location_or_constraint_history_removed_by_this_binder=False,
            raw_scientific_arrays_read=False, field_calls=0, endpoint_root_calls=0,
            J_calls=0, Jtranspose_calls=0))
    _validate_outer(value)
    return value


def bind_to_base(value, *, base_model, initial_reference_bundle_sha256,
                 fixed_scalar_metric_identity_sha256, initial_full_point_sha256,
                 bubble_nodes):
    identity = _validate_outer(value)
    expected = _current_binding(base_model=base_model,
        initial_reference_bundle_sha256=initial_reference_bundle_sha256,
        fixed_scalar_metric_identity_sha256=fixed_scalar_metric_identity_sha256,
        initial_full_point_sha256=initial_full_point_sha256, bubble_nodes=bubble_nodes)
    if value['definition'] != expected or identity != canonical(expected):
        raise ValueError('The complete literal-Q input belongs to another actual current base/target/chart/initial point')
    return identity


def parse_literal_Q(value):
    """Return fresh (complete hex words, numeric 2x3x3 lists), never fit Q."""
    _validate_outer(value)
    words = json_copy(value['definition']['Q0_binary64_hex'])
    return words, _words(words)


def from_parameter_file(path, *, input_sha256, base_model,
                        initial_reference_bundle_sha256,
                        fixed_scalar_metric_identity_sha256,
                        initial_full_point_sha256, bubble_nodes):
    path = Path(path)
    before = sha(path)
    if (input_sha256 != ORIGIN_PARAMETER_FILE_SHA or before != input_sha256
            or path.stat().st_size != ORIGIN_PARAMETER_FILE_BYTES):
        raise ValueError('Read the complete published df11 small parameter origin by actual bytes')
    origin = json.loads(path.read_text())
    result = bind_new_input(origin, base_model=base_model,
        initial_reference_bundle_sha256=initial_reference_bundle_sha256,
        fixed_scalar_metric_identity_sha256=fixed_scalar_metric_identity_sha256,
        initial_full_point_sha256=initial_full_point_sha256, bubble_nodes=bubble_nodes)
    if sha(path) != before:
        raise ValueError('The complete published small parameter file changed while being read')
    result['provenance']['origin_parameter_file_bytes_reread_by_this_call'] = True
    result['provenance']['actual_origin_parameter_file'] = dict(
        path=str(path.resolve()), sha256=before, bytes=path.stat().st_size)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--origin-parameter-file', type=Path, required=True)
    p.add_argument('--origin-parameter-file-sha256', required=True)
    p.add_argument('--current-binding-json', type=Path, required=True)
    p.add_argument('--current-binding-json-sha256', required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    before = sha(args.current_binding_json)
    if before != require_digest(args.current_binding_json_sha256, 'actual current binding JSON'):
        raise ValueError('Read the actual complete current binding JSON by exact bytes')
    current = json.loads(args.current_binding_json.read_text())
    required = {'base_model', 'initial_reference_bundle_sha256',
        'fixed_scalar_metric_identity_sha256', 'initial_full_point_sha256', 'bubble_nodes'}
    if not isinstance(current, dict) or set(current) != required:
        raise ValueError('The pure entry takes exactly the complete declared current binding arguments')
    value = from_parameter_file(args.origin_parameter_file,
        input_sha256=args.origin_parameter_file_sha256, **current)
    bind_to_base(value, **current)
    if sha(args.current_binding_json) != before:
        raise ValueError('The actual current binding JSON changed during this pure read')
    value['provenance']['actual_current_binding_json'] = dict(
        path=str(args.current_binding_json.resolve()), sha256=before,
        bytes=args.current_binding_json.stat().st_size)
    if args.output.exists():
        raise FileExistsError('Never overwrite a previously declared complete fixed input')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(schema=SCHEMA, source_sha256=sha(__file__),
        definition_identity_sha256=value['definition_identity_sha256'],
        fixed_scalar_metric_identity_sha256=value['definition']['fixed_scalar_metric_identity_sha256'],
        same_mathematical_g_claimed=False, current_working_moment_inverse_claimed=False,
        scientific_arrays_read=False, field_or_J_or_root_evaluations=0), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
