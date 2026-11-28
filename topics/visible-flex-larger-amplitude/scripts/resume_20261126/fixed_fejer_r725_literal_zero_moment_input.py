#!/usr/bin/env python3
"""Bind eighteen fixed Q words to one complete R725 paired-halfwave reference seed.

This is a separate complete input type.  The old 05dc definition and its
actual trace are parameter origins, never identities of the current base,
reference, scalar target, chart or initial point.  No moment, inverse,
endpoint root, F, J, Jtranspose or scientific array is read or computed.
The caller first constructs and validates its complete actual reference and
fixed paired-halfwave provider.  This pure binder then binds both complete JSON
models and supplied actual byte identities.  Old same-reference and ea94
new-reference validators remain unchanged.  The complete provider, mean-jet
kernel and base operator are independently pinned by their exact source bytes.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path


SCHEMA = 'fixed-fejer-r725-reference-literal-zero-endpoint-Q-input-v1'
DEFINITION_SCHEMA = 'fixed-fejer-r725-reference-literal-two-bubble-endpoint-Q-v1'
ORIGIN_SCHEMA = 'frozen-zero-endpoint-moment-Q-input-v1'
ORIGIN_DEFINITION_SCHEMA = 'literal-two-bubble-endpoint-Q-v1'
ORIGIN_DEFINITION_SHA = '05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e'
ORIGIN_PARAMETER_FILE_SHA = 'df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c'
ORIGIN_PARAMETER_FILE_BYTES = 3618
ORIGIN_PARAMETER_PATH = 'topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json'
ORIGIN_TRACE_REPORT_SHA = '26b094fef8baf6ff2ecdda5d1a0f5a8be7383e5171733320be959a22d83cb47e'
ORIGIN_TRACE_SOURCE_SHA = '73193414b094c05c9d8ce1dd033aab6a18446a88a5d7c4a6f352fcbcd966fb54'
BASE_SCHEMA = 'complete-fixed-fejer-r725-so3-meridian-with-core-lift-v1'
BASE_SOURCE_SHA = 'b5bea4d00c5e88978cebc56e4a9ebebabd1a4776aa19fc38d769f1fa078db792'
SEED_SCHEMA = 'complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1'
SEED_PROVIDER_SOURCE_SHA = '1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f'
SEED_MEAN_KERNEL_SOURCE_SHA = 'f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917'
PARENT_COMPLETE_BINDER_SOURCE_SHA = 'ea94cff11a975b44a6f91d46d3d08423ce386225b6eb8154bfb3f834706c9e39'
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
    'fixed_supported_unit_seed_model', 'fixed_supported_unit_seed_identity_sha256',
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


def _positive_exact_fraction(value, name):
    if not isinstance(value, str):
        raise ValueError('Keep an exact canonical Fraction string for '+name)
    try:
        number = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError('Invalid exact Fraction for '+name) from error
    if number <= 0 or str(number) != value:
        raise ValueError('Keep a positive canonical exact Fraction for '+name)
    return number


def _paired_halfwave_definition(central, profile_delta):
    """Exact complete radial profile; no numerical mean or field evaluation."""
    central = tuple(tuple(Fraction(v) for v in pair) for pair in central)
    delta = Fraction(profile_delta)
    if (len(central) != 2 or any(len(pair) != 2 for pair in central)
            or not Fraction(0) < delta < Fraction(1, 8)
            or not Fraction(0) < central[0][1]-central[0][0]
            or central[0][1]-central[0][0] != central[1][1]-central[1][0]):
        raise ValueError("The paired halfwaves require two complete equal positive central intervals")
    edges = (Fraction(0), 2*delta, Fraction(1,2)-2*delta, Fraction(1,2),
             Fraction(1,2)+2*delta, Fraction(1)-2*delta, Fraction(1))
    if any(a >= b for a, b in zip(edges, edges[1:])):
        raise ValueError("Every one of the six exact halfwave pieces is required")
    return dict(schema="complete-equal-central-intervals-paired-halfwave-profile-v1",
        auxiliary_profile="the original complete R711 h_delta on [0,1]",
        auxiliary_mean_kernel_source_sha256=SEED_MEAN_KERNEL_SOURCE_SHA,
        auxiliary_mean_rule_piece_count=12,
        physical_central_interval_count=2, physical_piece_count_per_interval=6,
        complete_physical_pair_piece_count=12,
        exact_profile_delta=str(delta),
        exact_normalized_piece_edges=[str(v) for v in edges],
        exact_relative_central_intervals=[[str(v) for v in pair] for pair in central],
        exact_relative_central_each_length=str(central[0][1]-central[0][0]),
        exact_relative_physical_piece_edges=[
            [str(a+(b-a)*v) for v in edges] for a,b in central],
        signs_in_radial_discovery_order=[1,-1],
        physical_profile="sign[index]*h_delta(t/2); t=(s-a)/(b-a)",
        radial_derivative_chain_factor="1/2",
        combined_cosine_mean="Lc*A_delta(lambda)*d",
        combined_transverse_mean="zero by equal complete central lengths and opposite signs",
        transverse_mean_zero_in_each_individual_interval=False,
        old_per_interval_odd_physical_profile_inherited=False)


BOUNDARY_CUTOFF_EPSILON = "1/8"
BOUNDARY_CUTOFF_SCHEMA = "complete-fixed-width-three-piece-C3-boundary-cutoff-v1"


def _flat_cutoff_polynomial_jets(t, epsilon):
    """Exact arithmetic for Fraction inputs; working arithmetic for float inputs."""
    zero, one = t*0, t*0+1
    if t <= zero:
        return zero, zero, zero, zero
    if t >= one:
        return one, zero, zero, zero
    denominator = one-epsilon
    if epsilon <= t <= one-epsilon:
        return (t-epsilon/2)/denominator, one/denominator, zero, zero
    reflected = t > one-epsilon
    u = (one-t)/epsilon if reflected else t/epsilon
    G = (u*u*u*u)*(5+u*(-6+2*u))/2
    S = u*u*u*(10+u*(-15+6*u))
    S1 = 30*u*u*(one-u)*(one-u)
    S2 = 60*u*(one-u)*(one-2*u)
    value = epsilon*G/denominator
    first = S/denominator
    second = S1/(epsilon*denominator)
    third = S2/(epsilon*epsilon*denominator)
    if reflected:
        return one-value, first, -second, third
    return value, first, second, third


def _boundary_cutoff_exact_jets(t):
    """R725 value and first three normalized-coordinate derivatives, all exact."""
    if not isinstance(t, (str, Fraction)):
        raise ValueError("Use an exact Fraction boundary cutoff coordinate")
    t = Fraction(t)
    return _flat_cutoff_polynomial_jets(t, Fraction(BOUNDARY_CUTOFF_EPSILON))


def _boundary_cutoff_definition(support, central):
    """Complete fixed-rational three-piece law and every exact physical cut."""
    epsilon = Fraction(BOUNDARY_CUTOFF_EPSILON)
    support = tuple(tuple(Fraction(v) for v in pair) for pair in support)
    central = tuple(tuple(Fraction(v) for v in pair) for pair in central)
    if (epsilon != Fraction(1,8) or len(support) != 2 or len(central) != 2
            or any(len(pair) != 2 for pair in support+central)):
        raise ValueError("This source fixes the complete R725 cutoff at epsilon=1/8")
    edges = (Fraction(0), epsilon, Fraction(1)-epsilon, Fraction(1))
    layers = []
    for index, ((left, right), (ca, cb)) in enumerate(zip(support, central)):
        if not left < ca < cb < right:
            raise ValueError("Every complete original boundary and central interval is required")
        for side, a, b, orientation in (("left", left, ca, 1), ("right", cb, right, -1)):
            physical = tuple(a+(b-a)*v for v in edges)
            layers.append(dict(support_index=index, side=side,
                exact_relative_interval=[str(a),str(b)],
                exact_relative_piece_edges=[str(v) for v in physical],
                exact_relative_internal_cuts=[str(v) for v in physical[1:-1]],
                original_interval_normalized_piece_edges=[str(v) for v in edges],
                cutoff_coordinate="t" if orientation == 1 else "1-t",
                odd_material_derivative_orientation=orientation,
                physical_piece_count=3,
                branches_in_increasing_material_order=(
                    ["left-polynomial","affine","right-reflection"] if orientation == 1 else
                    ["right-reflection","affine","left-polynomial"])))
    return dict(schema=BOUNDARY_CUTOFF_SCHEMA, proof_result="R725",
        exact_epsilon=str(epsilon), epsilon_is_a_fixed_source_parameter=True,
        epsilon_depends_on_angle_mean_direction_or_outer_point=False,
        accurate_law="C=epsilon*G(t/epsilon)/(1-epsilon); (t-epsilon/2)/(1-epsilon); 1-epsilon*G((1-t)/epsilon)/(1-epsilon)",
        exact_G_ascending_coefficients=["0","0","0","0","5/2","-3","1"],
        exact_velocity_S5_ascending_coefficients=["0","0","0","10","-15","6"],
        exact_normalized_piece_edges=[str(v) for v in edges],
        constant_extension_outside_unit_interval=True,
        piecewise_polynomial_degree=[6,1,6],
        matching_material_derivative_order=3,
        fourth_material_derivative_continuity_claimed=False,
        exact_cut_values_and_first_three_normalized_jets=[
            [str(v) for v in _boundary_cutoff_exact_jets(t)] for t in edges],
        exact_first_derivative_peak=str(Fraction(1)/(1-epsilon)),
        exact_derivative_integral="1", exact_value_integral="1/2",
        four_boundary_layers=layers, complete_physical_boundary_piece_count=12,
        complete_new_internal_boundary_cut_count=8,
        original_central_halfwave_profile_changed=False,
        original_bubble_gamma_and_raw_defect_lift_changed=False,
        working_arithmetic="binary64 evaluation of this complete exact-rational law",
        working_rounding_or_integration_error_enclosed=False)


def _supported_seed(seed_model, *, reference, reference_id,
                    initial_reference_bundle_sha256,
                    fixed_scalar_metric_identity_sha256,
                    profile, fixed_chart_core_sha256, bubble_nodes):
    """Check the full frozen seed JSON; no seed root or field is evaluated."""
    for value, name in (
            (SEED_PROVIDER_SOURCE_SHA, 'locked complete supported seed provider'),
            (SEED_MEAN_KERNEL_SOURCE_SHA, 'locked complete supported seed mean kernel')):
        require_digest(value, name)
    if not isinstance(seed_model, dict):
        raise ValueError('Retain the entire fixed supported-smooth-triangle seed model')
    seed = json_copy(seed_model)
    if (seed.get('schema') != SEED_SCHEMA
            or seed.get('source_sha256') != SEED_PROVIDER_SOURCE_SHA
            or seed.get('original_reference_source_sha256') != REFERENCE_SOURCE_SHA
            or seed.get('mean_kernel_source_sha256') != SEED_MEAN_KERNEL_SOURCE_SHA
            or seed.get('initial_reference_bundle_sha256') != initial_reference_bundle_sha256
            or seed.get('initial_reference_model_identity_sha256') != reference_id
            or seed.get('complete_axisymmetric_reference_model') != reference
            or seed.get('fixed_scalar_metric_identity_sha256') != fixed_scalar_metric_identity_sha256
            or seed.get('fixed_scalar_profile_definition') != profile
            or seed.get('fixed_chart_core_sha256') != fixed_chart_core_sha256):
        raise ValueError('Bind the actual complete supported seed to this same full reference, chart and fixed scalar target')
    word = seed.get('initial_height_hex')
    if not isinstance(word, str):
        raise ValueError('The fixed seed must record its actual initial height word')
    try:
        height = float.fromhex(word)
    except ValueError as error:
        raise ValueError('Invalid fixed seed initial height word') from error
    if not math.isfinite(height) or height.hex() != word:
        raise ValueError('Keep the finite canonical fixed seed initial height word')
    nodes = _nodes(bubble_nodes)
    expected_support = [[row[0], row[2]] for row in nodes]
    if seed.get('exact_relative_support_intervals') != expected_support:
        raise ValueError('The fixed seed uses exactly the two declared wide bubble supports; gamma is not a third interval')
    boundary = _positive_exact_fraction(seed.get('exact_relative_boundary_total_length'),
        'fixed seed boundary total length')
    support = tuple(tuple(Fraction(v) for v in pair) for pair in expected_support)
    if boundary >= 2*min(b-a for a,b in support):
        raise ValueError('Keep positive boundary layers and both complete central intervals')
    end_width = boundary/4
    central = tuple((a+end_width,b-end_width) for a,b in support)
    profile_delta = _positive_exact_fraction(seed.get('exact_profile_delta'), 'fixed seed smooth-triangle profile delta')
    paired = _paired_halfwave_definition(central, profile_delta)
    if (profile_delta >= Fraction(1, 8)
            or seed.get('mathematical_profile_piece_count') != 6
            or seed.get('mathematical_profile_piece_count_scope') != 'one physical central interval'
            or seed.get('auxiliary_mean_profile_piece_count') != 12
            or seed.get('complete_physical_pair_piece_count') != 12
            or seed.get('paired_halfwave_definition') != paired
            or seed.get('exact_relative_central_intervals') != paired['exact_relative_central_intervals']
            or seed.get('exact_relative_boundary_each_end_length') != str(end_width)
            or seed.get('mathematical_amplitude_interval') != '(0,pi)'
            or seed.get('old_five_piece_working_cache_or_geometry_inherited') is not False):
        raise ValueError('Bind both complete opposite halfwaves and the original full R711 amplitude rule')
    cutoff = _boundary_cutoff_definition(support, central)
    if (seed.get('exact_boundary_cutoff_epsilon') != BOUNDARY_CUTOFF_EPSILON
            or seed.get('boundary_cutoff_definition') != cutoff):
        raise ValueError('Bind the full R725 law, all four boundary layers, all eight internal cuts and exact endpoint jets')
    working = seed.get('working_definition')
    if (not isinstance(working, dict)
            or working.get('schema') != 'paired-halfwave-flat-cutoff-reference-working-definition-v1'
            or working.get('physical_central_profile_definition') != paired
            or working.get('physical_boundary_cutoff_definition') != cutoff
            or working.get('exact_boundary_cutoff_epsilon') != BOUNDARY_CUTOFF_EPSILON
            or working.get('old_boundary_quadrature_mean_root_or_cache_inherited') is not False
            or working.get('original_outer_whole_cell_Gauss_and_partial_rule_is_separate') is not True
            or working.get('auxiliary_mean_metadata_describes_original_full_R711_rule') is not True
            or working.get('physical_profile_is_not_the_auxiliary_full_period_on_each_interval') is not True
            or working.get('actual_field_quadrature_or_closure_words_inherited_from_original_seed') is not False):
        raise ValueError('Retain the complete paired physical profile and distinct auxiliary mean rule')
    # Root/positivity/capacity conditions belong to the real complete provider.
    # Canonical positive parameters are not a contraction or field certificate.
    json_copy(working)
    return seed, canonical(seed)


def _current_binding(*, base_model, initial_reference_bundle_sha256,
                     fixed_scalar_metric_identity_sha256, initial_full_point_sha256,
                     bubble_nodes):
    """Check the complete actual JSON reference, without evaluating its arrays."""
    require_digest(initial_reference_bundle_sha256, 'current initial reference bundle')
    require_digest(fixed_scalar_metric_identity_sha256, 'current fixed scalar metric')
    require_digest(initial_full_point_sha256, 'current complete base initial point')
    if not isinstance(base_model, dict):
        raise ValueError('Supply the complete actual base model, not a replacement digest')
    require_digest(BASE_SOURCE_SHA, 'locked complete supported-smooth-triangle base source')
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
        raise ValueError('Bind this actual complete supported-smooth-triangle base/4e/e091 target, without old physical-source identity substitution')
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
    seed, seed_identity = _supported_seed(base.get('fixed_supported_unit_seed_model'),
        reference=reference, reference_id=reference_id,
        initial_reference_bundle_sha256=initial_reference_bundle_sha256,
        fixed_scalar_metric_identity_sha256=fixed_scalar_metric_identity_sha256,
        profile=profile, fixed_chart_core_sha256=base['fixed_chart_core_sha256'],
        bubble_nodes=bubble_nodes)
    if (base.get('fixed_supported_unit_seed_identity_sha256') != seed_identity
            or base.get('fixed_supported_unit_seed_source_sha256') != SEED_PROVIDER_SOURCE_SHA
            or base.get('fixed_supported_unit_seed_mean_kernel_sha256') != SEED_MEAN_KERNEL_SOURCE_SHA
            or base.get('fixed_supported_unit_seed_working_definition') != seed['working_definition']):
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
        fixed_supported_unit_seed_model=seed,
        fixed_supported_unit_seed_identity_sha256=seed_identity)


def validate_definition(definition, expected_identity=None):
    if not isinstance(definition, dict) or set(definition) != DEFINITION_KEYS:
        raise ValueError('Keep exactly the twelve declared complete supported-smooth-triangle input fields')
    if definition.get('schema') != DEFINITION_SCHEMA:
        raise ValueError('Use the independent complete supported-smooth-triangle mathematical control type')
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
    seed_model = definition['fixed_supported_unit_seed_model']
    if not isinstance(seed_model, dict):
        raise ValueError('Keep the whole actual supported seed in the fixed input')
    reference = seed_model.get('complete_axisymmetric_reference_model')
    if (not isinstance(reference, dict)
            or reference.get('schema') != REFERENCE_SCHEMA
            or reference.get('source_sha256') != REFERENCE_SOURCE_SHA
            or canonical(reference) != definition['initial_reference_model_identity_sha256']
            or reference.get('fixed_scalar_profile_definition') != profile
            or reference.get('fixed_scalar_metric_identity_sha256') != definition['fixed_scalar_metric_identity_sha256']
            or reference.get('fixed_chart_core_sha256') != definition['fixed_chart_core_sha256']):
        raise ValueError('The seed must retain this whole actual 4e reference and exact fixed target/chart')
    seed, seed_identity = _supported_seed(seed_model, reference=reference,
        reference_id=definition['initial_reference_model_identity_sha256'],
        initial_reference_bundle_sha256=definition['initial_reference_bundle_sha256'],
        fixed_scalar_metric_identity_sha256=definition['fixed_scalar_metric_identity_sha256'],
        profile=profile, fixed_chart_core_sha256=definition['fixed_chart_core_sha256'],
        bubble_nodes=definition['exact_relative_bubble_nodes'])
    require_digest(definition['fixed_supported_unit_seed_identity_sha256'], 'complete fixed supported-smooth-triangle seed')
    if definition['fixed_supported_unit_seed_identity_sha256'] != seed_identity:
        raise ValueError('The whole supported seed definition changed')
    identity = canonical(definition)
    if expected_identity is not None:
        require_digest(expected_identity, 'explicit current input definition')
        if identity != expected_identity:
            raise ValueError('The explicitly fixed complete supported-smooth-triangle input changed')
    return identity


def _validate_outer(value):
    if (not isinstance(value, dict) or set(value) != OUTER_KEYS
            or value.get('schema') != SCHEMA):
        raise ValueError('Use the separate complete supported-smooth-triangle literal-Q input type')
    identity = validate_definition(value['definition'], value.get('definition_identity_sha256'))
    if value.get('definition_identity_sha256') != identity:
        raise ValueError('The complete supported-smooth-triangle definition identity is missing or altered')
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
            or p.get('supported_unit_seed_is_frozen_before_current_free_point') is not True
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
            current_binding='This complete supported-smooth-triangle base, whole frozen seed, original reference, fixed scalar/chart and base.initial identity',
            parent_complete_binder_source_sha256=PARENT_COMPLETE_BINDER_SOURCE_SHA,
            supported_unit_seed_is_frozen_before_current_free_point=True,
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
