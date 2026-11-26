#!/usr/bin/env python3
"""Bind the actual complete optional-initial-height frozen moment-Q zero SO3 report.

Only stdlib JSON/source/byte attribution is performed. No F/J or scientific
arrays are recomputed. Common-slack values and real nonlinear violations
remain separate. An incomplete or failed actual budget is never promoted
to a complete direction, a feasible field, or fixed-g refinement success.
The exact-definition radial identity is distinct from ordinary numerical
Gram, endpoint-root and quadrature errors. Current-field root records and
all-attempted-field counters retain their separate actual scopes. This
reader neither solves a root nor verifies a continuous implicit branch.
"""
import argparse
import ast
import hashlib
from fractions import Fraction
import importlib.util
import sys
import json
import math
from pathlib import Path


DRIVER_SHA = '34c9273aad6ccc3299c8b64ac250a37b3ae758eec34945ef00a4b14a3acaf1b3'
REPORT_SCHEMA = 'complete-independent-axisymmetric-fixed-deep-frozen-moment-Q-zero-SO3-explicit-height-QP-v1'


HEIGHT_ENTRY_DERIVATION = dict(
    schema='complete-fixed-moment-zero-SO3-explicit-height-source-derivation-v1',
    parent_driver_sha256='ff500abfa24de27c22f8a8993b9104cc265c5c96289a927c18755d318fbf0766',
    parent_launcher_sha256='082bb92e0e9f01067cf1bd8ecaae65cb559e38bba90dd79b97bf492c11d758f4',
    parent_reader_sha256='c942aa60db84698215e53dd2427a19c693ca73e6c3c8553ef0b73fa75edf295a',
    original_driver_suffix_from_save_report_sha256='9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee',
    scientific_loop_suffix_byte_identical=True,
    scientific_source_registry_unchanged=True,
    original_endpoint_and_geometry_sources_unchanged=True,
    explicit_height_changes_only_new_initial_free_point=True)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def load_pins(path):
    values = [ast.literal_eval(node.value) for node in ast.parse(path.read_text()).body
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SOURCE_PINS'
            for t in node.targets)]
    if len(values) != 1:
        raise ValueError('One complete literal source registry is required')
    return values[0]


def endpoint_roots(value):
    """Read only the actual diagnostic record, never construct an implicit root."""
    if value is None:
        return None
    for key in ('numerical_Newton_iterations_differentiated',
                'complete_uniform_IFT_conditions_verified',
                'complete_continuous_root_branch_certified',
                'endpoint_root_error_enclosed'):
        if value.get(key) is not False:
            raise ValueError('The bound numerical root record cannot certify '+key)
    names = ('current_full_point_sha256', 'endpoint_root_policy',
        'current_cached_angle_roots', 'current_all_grid_angle_roots_available',
        'current_maximum_endpoint_residual', 'current_maximum_endpoint_correction_norm',
        'current_minimum_endpoint_sample_singular_value',
        'current_maximum_first_angular_root_residual',
        'current_maximum_second_angular_root_residual',
        'endpoint_counts', 'last_root_failure')
    result = {key: value[key] for key in names}
    result.update(numerical_Newton_iterations_differentiated=False,
        complete_uniform_IFT_conditions_verified=False,
        complete_continuous_root_branch_certified=False,
        endpoint_root_error_enclosed=False,
        all_grid_roots_available_is_a_numerical_cache_statement_only=True)
    return result


def endpoint_metadata(value, model, source_by_role, working_evaluation):
    """Retain actual current and all-attempted scopes, with exact source binding."""
    if not value:
        return None
    if (value.get('model') != model
            or value.get('model_identity_sha256') != canonical(model)
            or value.get('source_sha256') != source_by_role['endpoint']
            or value.get('schema') != model['schema']
            or value.get('base_source_sha256') != source_by_role['meridian']
            or value.get('endpoint_root_policy') != working_evaluation['endpoint_root_policy']):
        raise ValueError('The actual endpoint metadata belongs to a different model or root policy')
    if (value.get('frozen_moment_Q_definition') != model['frozen_moment_Q_definition']
            or value.get('frozen_moment_Q_definition_identity_sha256') != model['frozen_moment_Q_definition_identity_sha256']
            or value.get('Q_input_recomputed_at_current_point') is not False
            or value.get('actual_working_moment_inverse_is_not_a_continuous_certificate') is not True):
        raise ValueError('The actual endpoint metadata changed its complete frozen literal control input')
    base = value['base_complete_metadata']
    if (base.get('model') != model['base_complete_model']
            or base.get('model_identity_sha256') != model['base_model_identity_sha256']
            or base.get('source_sha256') != source_by_role['meridian']):
        raise ValueError('The actual complete base metadata differs from the independent base source')
    for key in ('numerical_Newton_iterations_differentiated',
                'second_parameter_derivatives_supported_by_surrogate',
                'finite_difference_J', 'fixed_target_recomputed_from_current_field',
                'numerical_radial_Gram_row_omitted', 'integration_error_enclosed',
                'symbolic_mesh_carrier_rounding_error_enclosed', 'endpoint_root_error_enclosed',
                'complete_uniform_IFT_conditions_verified', 'angular_root_jets_outward_enclosed',
                'complete_continuous_root_branch_certified',
                'old_metric_or_geometry_certificates_inherited', 'closed_exact_isometry_certified'):
        if value.get(key) is not False:
            raise ValueError('No unsupported numerical-to-continuous promotion: '+key)
    if (value.get('all_metric_mean_and_cross_rows_retained') is not True
            or value.get('radial_metric_identity_in_exact_definition') is not True):
        raise ValueError('Keep the exact radial identity and every numerical Gram row distinct')
    current = endpoint_roots(value)
    names = ('all_attempted_fields_maximum_successful_endpoint_residual',
        'all_attempted_fields_maximum_successful_correction_norm',
        'all_attempted_fields_minimum_sample_endpoint_singular_value',
        'all_attempted_fields_maximum_core_inverse_residual',
        'all_attempted_fields_minimum_core_inverse_sample_rho')
    return dict(current=current, all_attempted={key: value[key] for key in names},
        actual_field_counts=value['actual_field_counts'], endpoint_counts=value['endpoint_counts'],
        base_actual_operator_counts=base.get('actual_counts'),
        base_core_inverse_path_used=base['base_core_inverse_path_used'],
        base_actual_counts_scope=base['actual_counts_scope'],
        base_metadata_scope=base['metadata_scope'],
        base_reference_maximum_requested_norm_deviation=base.get('maximum_requested_reference_norm_deviation'),
        free_variables=value['free_variables'], free_core_variables=value['free_core_variables'],
        free_rotation_variables=value['free_rotation_variables'],
        all_free_height_variables=value['all_free_height_variables'],
        J_method=value['J_method'], Jtranspose_method=value['Jtranspose_method'],
        core_inverse_J=value['core_inverse_J'],
        first_parameter_implicit_derivatives_only=True,
        second_parameter_derivatives_supported_by_surrogate=False,
        numerical_Newton_iterations_differentiated=False,
        numerical_radial_Gram_row_omitted=False,
        current_root_availability_is_continuous_branch_certificate=False,
        complete_uniform_IFT_conditions_verified=False,
        complete_continuous_root_branch_certified=False,
        endpoint_root_error_enclosed=False, integration_error_enclosed=False,
        angular_root_jets_outward_enclosed=False)


def statistic(value, profile):
    if value is None:
        return None
    if value.get('fixed_scalar_metric_identity_sha256') != profile:
        raise ValueError('A statistics record belongs to another actual target')
    spectrum = value['spectral']
    return dict(max_relative_gram=value['max_relative_gram'],
        legacy_max_relative_gram=value.get('legacy_max_relative_gram'),
        Phi=spectrum['centered_phi_normalized'], uncentered_Phi=spectrum['phi_normalized'],
        p=spectrum['p'], epsilon=spectrum['epsilon'], scale=spectrum['scale'],
        normalization=spectrum['normalization'],
        min_relative_E=value['min_relative_E'],
        min_relative_determinant=value['min_relative_determinant'],
        domain=value.get('domain'), endpoint_roots=endpoint_roots(value.get('endpoint_roots')))


def geometric(value):
    if value is None:
        return None
    complete = value.get('complete') is True
    g = value.get('maximum_physical_g')
    real_feasible = bool(complete and isinstance(g, (int, float))
        and math.isfinite(g) and g <= 0 and value.get('passed') is True)
    result = dict(complete=complete, true_finite_geometry_feasible=real_feasible,
        maximum_physical_g=g, necessary_reach_product=value.get('necessary_reach_product'),
        maximum_absolute_principal_curvature=value.get('maximum_absolute_principal_curvature'),
        diameter_point_lower=value.get('diameter_point_lower'), current_height=value.get('current_height'),
        current_witness_radius=value.get('current_witness_radius'),
        permanent_unique_locations_read=value.get('permanent_unique_locations_read'),
        permanent_curvature_locations=value.get('permanent_curvature_locations'),
        permanent_radius_locations=value.get('permanent_radius_locations'),
        all_permanent_locations_read=value.get('all_permanent_curvature_and_radius_locations_read', False),
        both_witness_signs_read=value.get('both_witness_signs_read_at_every_point', False),
        continuous_geometry_certified=False)
    amplitude = value.get('amplitude')
    if amplitude is not None:
        result['amplitude_g'] = {key: amplitude[key] for key in
            ('body_diameter', 'distance_plus', 'distance_minus', 'cap_diameter', 'height_floor')}
    for key in ('error_type', 'error'):
        if key in value:
            result[key] = value[key]
    return result


def direction(value, profile):
    phase = value['phase']
    if phase not in ('metric', 'restoration'):
        raise ValueError('The complete report used an undeclared scientific phase')
    rows = value['complete_selected_inequalities']
    if (rows.get('no_original_row_removed') is not True
            or rows['original_prefix_rows']+rows['appended_amplitude_rows'] != rows['selected_rows']
            or len(rows['rows']) != rows['selected_rows']):
        raise ValueError('A full selected geometry/amplitude prefix was dropped or miscounted')
    if phase == 'restoration':
        quadratic = value['quadratic_model']
        if (quadratic.get('all_original_rows_retained') is not True
                or quadratic.get('physical_feasibility_inferred_from_slack') is not False
                or quadratic['original_rows'] != rows['selected_rows']):
            raise ValueError('Do not drop any typed row or interpret slack as physical feasibility')
    qp = value['qp']
    result = dict(index=value['index'], serial=value['serial'], phase=phase,
        accepted=value['accepted'], accepted_alpha=value.get('accepted_alpha'),
        damping=value['actual_damping'], damping_after=value.get('damping_after_direction'),
        qp_status=qp['status'], actual_advances=qp['advances'],
        final_face_projected_gradient_norm=qp.get('final_face_projected_gradient_norm'),
        qp_tolerance=qp.get('gradient_tolerance'),
        active_face_rows=qp.get('active_face', {}).get('active_rows'),
        active_face_indices=qp.get('active_face', {}).get('active_indices'),
        actual_operator_products=qp.get('operator_products'),
        maximum_linear_violation=qp.get('maximum_linear_violation'),
        original_geometry_rows=rows['original_prefix_rows'],
        amplitude_rows=rows['appended_amplitude_rows'], total_rows=rows['selected_rows'],
        row_cache_bytes=rows['row_cache_bytes'],
        duplicate_prefix_cache_bytes=rows.get('duplicate_prefix_cache_bytes'),
        actual_QP_seconds=value.get('actual_QP_seconds'),
        actual_complete_direction_seconds=value['seconds'],
        actual_QP_operator_counts=value.get('actual_QP_operator_counts'),
        actual_complete_direction_operator_counts=value.get('actual_complete_direction_operator_counts'),
        starting_statistics=statistic(value['starting_statistics'],profile),
        starting_geometry=geometric(value['starting_geometry']),
        accepted_statistics=statistic(value.get('accepted_statistics'),profile),
        accepted_geometry=geometric(value.get('accepted_geometry')),
        maximum_selected_linear_physical_g=value.get('maximum_selected_linear_physical_g'),
        old_actual_positive_physical_g=value['old_actual_maximum_positive_physical_g'],
        computed_common_slack=value.get('computed_common_slack'),
        common_slack_is_true_feasibility=False,
        trial_count=len(value['trials']))
    if value.get('accepted_bundle') is not None:
        result['accepted_bundle_sha256'] = value['accepted_bundle']['sha256']
    trials = []
    for trial in value['trials']:
        if trial.get('accepted') and trial.get('full_true_geometry_read') is not True:
            raise ValueError('No numerical trial may be accepted without its complete true-field geometry')
        if phase == 'metric' and trial.get('accepted') and (
                trial.get('actual_Phi_descent') is not True
                or not geometric(trial.get('full_geometry'))['true_finite_geometry_feasible']):
            raise ValueError('A metric direction must have actual same-objective descent and true geometry')
        if phase == 'restoration' and trial.get('accepted') and not (
                isinstance(trial.get('actual_positive_physical_g'), (int, float))
                and trial['actual_positive_physical_g'] < value['old_actual_maximum_positive_physical_g']):
            raise ValueError('A restored trial needs real physical violation decrease, independently of tau')
        trials.append(dict(index=trial['index'], alpha=trial['alpha'], accepted=trial['accepted'],
            actual_Phi_descent=trial.get('actual_Phi_descent'),
            actual_positive_physical_g=trial.get('actual_positive_physical_g'),
            full_true_geometry_read=trial.get('full_true_geometry_read'),
            true_finite_geometry_feasible=trial.get('physically_feasible'),
            domain_feasible=trial.get('domain_feasible'),
            statistics=statistic(trial.get('statistics'),profile),
            full_geometry=geometric(trial.get('full_geometry')),
            endpoint_roots=endpoint_roots(trial.get('endpoint_roots')),
            actual_seconds=trial.get('actual_seconds'), actual_read_error=trial.get('actual_read_error')))
    result['trials'] = trials
    return result


def finite_initial_height(literal):
    """Parse one explicit finite binary64 seed word; no feasibility is asserted."""
    if not isinstance(literal, str) or not literal.strip():
        raise ValueError('Declare a nonempty explicit initial-height literal')
    stripped = literal.strip()
    value = (float.fromhex(stripped) if stripped.lower().lstrip('+-').startswith('0x')
             else float(stripped))
    if not math.isfinite(value):
        raise ValueError('The explicit initial height must be finite')
    return value


def digest_word(value, name):
    if not isinstance(value, str) or len(value) != 64 or any(c not in '0123456789abcdef' for c in value):
        raise ValueError('Use the complete recorded SHA256 for '+name)
    return value


def exact_height_word(word, exact, name):
    if not isinstance(word, str) or not isinstance(exact, str):
        raise ValueError('Keep the exact binary64 and rational height words for '+name)
    value = float.fromhex(word)
    if (not math.isfinite(value) or value.hex() != word
            or str(Fraction.from_float(value)) != exact):
        raise ValueError('The recorded finite height words disagree for '+name)
    return value


def read_initial_height_input(report, model, frozen_input, profile, moment_identity):
    """Pure source/JSON identity audit; no full point or field is recomputed."""
    if report.get('initial_height_entry_source_derivation') != HEIGHT_ENTRY_DERIVATION:
        raise ValueError('The independent initial-height entry lost its exact full-body derivation')
    initial = report.get('initial_free_point')
    if not isinstance(initial, dict) or initial.get('schema') != 'actual-full-zero-SO3-initial-free-point-v1':
        raise ValueError('Retain the actual complete initial free-point identity before any root read')
    size = report['original_variables']
    if not isinstance(size, int) or isinstance(size, bool) or size < 1:
        raise ValueError('Use the actual complete original free dimension')
    point_sha = digest_word(initial.get('full_point_sha256'), 'actual initial free point')
    prefix_sha = digest_word(initial.get('nonheight_coordinates_sha256'), 'initial nonheight prefix')
    initial_height = exact_height_word(initial.get('height_binary64_hex'),
        initial.get('height_exact'), 'actual initial free point')
    if (initial.get('dtype') != 'float64' or initial.get('shape') != [size]
            or initial.get('free_variables') != size
            or initial.get('height_coordinate_index') != size-1
            or initial.get('model_identity_sha256') != report['model_identity_sha256']
            or initial.get('fixed_scalar_metric_identity_sha256') != profile
            or initial.get('frozen_moment_Q_definition_identity_sha256') != moment_identity
            or initial.get('field_or_root_read_required_before_acceptance') is not True
            or initial.get('recorded_before_initial_field_read') is not True
            or initial.get('scientific_field_evaluated_by_this_record') is not False):
        raise ValueError('The initial point identity is not the complete same-model free point')
    restart, seed = report.get('restart'), report.get('direct_base_seed')
    if restart is not None and seed is not None:
        raise ValueError('A report cannot combine a true restart and a direct-base seed')
    if 'initial_height_input' not in report:
        raise ValueError('The new entry must state explicitly whether a height override was used')
    changed = report['initial_height_input']
    expected_mode = ('same-source-restart' if restart is not None else
        'complete-direct-base-seed' if seed is not None else
        'explicit-height-new-reference-seed' if changed is not None else 'original-reference-seed')
    if initial.get('source_mode') != expected_mode:
        raise ValueError('The complete initial point came from a different seed path')
    if changed is not None:
        if (not isinstance(changed, dict)
                or changed.get('schema') != 'explicit-new-reference-free-height-input-v1'
                or restart is not None or seed is not None):
            raise ValueError('An explicit height is allowed only on a new original reference seed')
        original_point = digest_word(changed.get('original_full_point_sha256'), 'original trace reference point')
        requested = finite_initial_height(changed.get('requested_literal'))
        original_height = exact_height_word(changed.get('original_height_binary64_hex'),
            changed.get('original_height_exact'), 'unchanged reference initial height')
        actual_height = exact_height_word(changed.get('actual_initial_height_binary64_hex'),
            changed.get('actual_initial_height_exact'), 'overridden initial height')
        exact_height_word(changed.get('requested_binary64_hex'),
            changed.get('requested_exact'), 'requested initial height')
        if (original_point != frozen_input['definition']['trace_initial_full_point_sha256']
                or changed.get('actual_initial_full_point_sha256') != point_sha
                or changed.get('requested_binary64_hex') != requested.hex()
                or actual_height.hex() != requested.hex()
                or actual_height.hex() != initial_height.hex()
                or changed.get('original_nonheight_coordinates_sha256') != prefix_sha
                or changed.get('actual_nonheight_coordinates_sha256') != prefix_sha
                or changed.get('changed_coordinate_index') != size-1
                or changed.get('full_free_size') != size
                or changed.get('original_array_dtype') != 'float64'
                or changed.get('actual_array_dtype') != 'float64'
                or changed.get('original_array_shape') != [size]
                or changed.get('actual_array_shape') != [size]
                or changed.get('model_identity_before_sha256') != report['model_identity_sha256']
                or changed.get('model_identity_after_sha256') != report['model_identity_sha256']
                or changed.get('base_model_identity_sha256') != model['base_model_identity_sha256']
                or changed.get('fixed_scalar_metric_identity_sha256') != profile
                or changed.get('frozen_moment_Q_definition_identity_sha256') != moment_identity
                or changed.get('initial_reference_bundle_sha256') != report['bundle_sha256']):
            raise ValueError('Do not relabel an old initial point, target, reference, or frozen Q as a new height seed')
        word_changed = original_height.hex() != actual_height.hex()
        if (changed.get('height_word_changed') is not word_changed
                or (point_sha != original_point) != word_changed):
            raise ValueError('The point digest and exact height-change flag disagree')
        for name in ('all_nonheight_coordinates_byte_identical',
                'original_reference_point_verified_before_override',
                'height_remains_an_original_free_variable'):
            if changed.get(name) is not True:
                raise ValueError('The explicit height path must preserve '+name)
        for name in ('reference_context_or_bundle_modified', 'model_or_target_modified',
                'frozen_Q_recomputed', 'restart_or_direct_base_seed_used',
                'previous_Phi_or_root_or_geometry_certificate_inherited',
                'height_input_implies_field_acceptance'):
            if changed.get(name) is not False:
                raise ValueError('A seed height choice cannot assert '+name)
    elif expected_mode == 'original-reference-seed' and (
            point_sha != frozen_input['definition']['trace_initial_full_point_sha256']):
        raise ValueError('An unmodified reference seed must retain the actual original trace point identity')
    stats = report.get('initial')
    if stats is not None:
        roots = stats.get('endpoint_roots')
        if not isinstance(roots, dict) or roots.get('current_full_point_sha256') != point_sha:
            raise ValueError('The initial true endpoint/field read belongs to a different free point')
        domain = stats.get('domain')
        if not isinstance(domain, dict) or float(domain['H']).hex() != initial_height.hex():
            raise ValueError('The actual initial full-field domain read used another height')
    failure_roots = report.get('initial_endpoint_roots')
    if failure_roots is not None and failure_roots.get('current_full_point_sha256') != point_sha:
        raise ValueError('Do not attribute a failed initial root read to a different point')
    if report.get('actual_initial_read_error') is not None and failure_roots is None:
        raise ValueError('An actual initial field failure must retain its current-point root diagnostics')
    return initial, changed


def read_report(repo, report_path, *, verify_final_bundle=False):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    driver = topic/'scripts/resume_20261126/fullclosed_zero_moment_height_so3_qp.py'
    if sha(driver) != DRIVER_SHA:
        raise ValueError('The complete actual driver body differs from the bound source')
    report = json.loads(Path(report_path).read_text())
    if report.get('schema') != REPORT_SCHEMA or report.get('source_sha256') != DRIVER_SHA:
        raise ValueError('This reader accepts only its complete actual SO3 report; no old schema relabeling')
    for role, (relative, expected) in load_pins(driver).items():
        if report['source_sha256_by_role'].get(role) != expected or sha(topic/relative) != expected:
            raise ValueError('The actual complete source role changed: '+role)
    model = report['representation']
    fixed = report['fixed_scalar_metric']
    base_model = model['base_complete_model']
    reference = base_model['complete_axisymmetric_reference_model']
    profile = reference['fixed_scalar_metric_identity_sha256']
    roles = report['source_sha256_by_role']
    if (canonical(model) != report['model_identity_sha256']
            or canonical(base_model) != model['base_model_identity_sha256']
            or model['source_sha256'] != roles['endpoint']
            or model['base_source_sha256'] != roles['meridian']
            or base_model['source_sha256'] != roles['meridian']
            or model['base_schema'] != base_model['schema']
            or base_model['initial_reference_bundle_sha256'] != report['bundle_sha256']
            or canonical(reference) != base_model['initial_reference_model_identity_sha256']
            or canonical(reference['fixed_scalar_profile_definition']) != profile
            or fixed['exact_profile_definition'] != reference['fixed_scalar_profile_definition']
            or model['fixed_scalar_profile_definition'] != reference['fixed_scalar_profile_definition']
            or base_model['fixed_scalar_profile_definition'] != reference['fixed_scalar_profile_definition']
            or report['independent_reference_binding']['reference_model_identity_sha256'] != canonical(reference)
            or report['independent_reference_binding']['fixed_scalar_metric_identity_sha256'] != profile
            or reference['source_sha256'] != roles['reference']
            or fixed['identity_sha256'] != profile
            or canonical(fixed['exact_profile_definition']) != profile
            or fixed.get('target_fixed_before_first_direction') is not True
            or fixed.get('target_recomputed_from_current_field') is not False
            or fixed.get('moving_mean_projection') is not False
            or fixed.get('all_metric_mean_constraints_retained') is not True
            or model['fixed_scalar_metric_identity_sha256'] != profile
            or base_model['fixed_scalar_metric_identity_sha256'] != profile
            or model.get('radial_Gram_error_identically_zero') is not True
            or model.get('mathematical_field_definition_requires_exact_implicit_root') is not True
            or model.get('implicit_root_is_not_a_new_independent_free_field') is not True
            or model.get('all_current_free_core_coefficients_retained') is not True
            or model.get('all_original_rotation_variables_retained') is not True
            or model.get('current_height_free') is not True
            or report.get('radial_metric_error_identically_zero') is not True
            or report.get('radial_Gram_uses_complete_hprime_Delta') is not False
            or report.get('numerical_radial_Gram_row_retained') is not True
            or report.get('endpoint_implicit_J_separate_from_Newton') is not True):
        raise ValueError('Keep the exact zero-closure definition, same fixed target, and complete numerical Gram')
    binder_path = topic/'scripts/resume_20261126/frozen_zero_moment_input.py'
    if sha(binder_path) != roles['frozen_moment_input']:
        raise ValueError('The whole pure fixed input binder changed')
    spec = importlib.util.spec_from_file_location('_pure_actual_fixed_moment_input',binder_path)
    binder = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = binder
    spec.loader.exec_module(binder)
    frozen_input = report['frozen_moment_Q_input']
    moment_identity = binder.bind_to_base(frozen_input, base_model=base_model,
        initial_reference_bundle_sha256=report['bundle_sha256'],
        fixed_scalar_metric_identity_sha256=profile,
        bubble_nodes=model['exact_relative_bubble_nodes'])
    if (model.get('schema') != 'complete-direct-R690-SO3-frozen-moment-Q-zero-endpoint-layer-v1'
            or model.get('frozen_moment_Q_definition') != frozen_input['definition']
            or model.get('frozen_moment_Q_definition_identity_sha256') != moment_identity
            or report.get('frozen_moment_Q_definition_identity_sha256') != moment_identity
            or model.get('moment_Q_recomputed_from_current_field') is not False
            or model.get('moment_Q_is_an_exact_integral_inverse_claimed') is not False
            or report.get('moment_Q_recomputed_from_current_free_point') is not False
            or report.get('old_zero_field_or_root_certificate_inherited') is not False
            or model.get('original_implicit_root_algorithm_source_sha256') != roles['moment_original_endpoint']):
        raise ValueError('Do not replace, recompute or relabel the fixed moment-Q mathematical control input')
    initial_free_point, initial_height_input = read_initial_height_input(
        report, model, frozen_input, profile, moment_identity)
    working = report['working_evaluation']
    if (working.get('fixed_moment_Q_definition_identity_sha256') != moment_identity
            or working.get('old_endpoint_coordinate_ball_certificate_inherited') is not False):
        raise ValueError('The new coordinate ball has its own declared scope and no inherited old certificate')
    if (working['exact_relative_bubble_nodes'] != model['exact_relative_bubble_nodes']
            or float(working['endpoint_root_policy']['branch_radius']).hex() != model['root_branch_radius_hex']
            or working.get('quadrature_error_enclosed') is not False
            or working.get('root_error_enclosed') is not False
            or working.get('evaluation_refinement_changes_exact_target') is not False):
        raise ValueError('Do not mistake the actual numerical root/evaluation policy for an error enclosure')
    seed = report.get('direct_base_seed')
    if seed is not None and (seed.get('actual_base_model_identity_sha256') != canonical(base_model)
            or seed.get('all_original_variables_copied') is not True
            or seed.get('old_Phi_or_certificates_inherited') is not False):
        raise ValueError('An original-variable seed changes the physical field and needs a fresh baseline')
    norm = report['coordinate_norm']
    if canonical({key: value for key, value in norm.items() if key != 'norm_identity_sha256'}) != norm['norm_identity_sha256']:
        raise ValueError('The actual full new coordinate norm identity changed')
    initial, final = statistic(report.get('initial'),profile), statistic(report.get('final_statistics'),profile)
    if initial is not None and final is not None:
        for key in ('p', 'epsilon', 'scale', 'normalization'):
            if initial[key] != final[key]:
                raise ValueError('Never subtract Phi from different target definitions or positive measures')
    metrics = [direction(value,profile) for value in report.get('metric_directions', [])]
    restoration = [direction(value,profile) for value in report.get('restoration_directions', [])]
    final_geometry = geometric(report.get('final_geometry'))
    if report.get('complete') is True:
        if final is None or final_geometry is None:
            raise ValueError('A complete actual budget needs the final full field read')
        if bool(report.get('final_true_sampled_geometry_feasible')) != final_geometry['true_finite_geometry_feasible']:
            raise ValueError('A common slack or partial screen was mistaken for final physical feasibility')
        if report['actual_metric_directions'] != len(metrics) or report['actual_restoration_directions'] != len(restoration):
            raise ValueError('Only actual complete recorded directions count')
        if verify_final_bundle:
            path = Path(report['final_bundle'])
            if sha(path) != report['final_bundle_sha256']:
                raise ValueError('The actual returned full SO3 bundle differs from the source report')
    metadata = report.get('latest_operator_metadata', {})
    endpoint = endpoint_metadata(metadata, model, roles, working)
    failed_initial = report.get('actual_initial_read_error') is not None
    if failed_initial and (report.get('complete') is True
            or report.get('initial_failed_candidate_is_not_an_accepted_field') is not True
            or metrics or restoration or report.get('final_bundle_sha256') is not None):
        raise ValueError('An initial endpoint/field-read failure is not a completed or accepted candidate')
    if report.get('complete') is True and endpoint is None:
        raise ValueError('A complete zero-closure budget needs its actual endpoint diagnostics')
    return dict(schema='actual-complete-independent-frozen-moment-Q-zero-SO3-explicit-height-readout-v1',
        reader_sha256=sha(__file__), report_path=str(Path(report_path).resolve()),
        report_sha256=sha(report_path), report_bytes=Path(report_path).stat().st_size,
        actual_driver_sha256=DRIVER_SHA, actual_source_commit=report['source_commit'],
        workflow_trigger_commit=report.get('workflow_trigger_commit'),
        github_run_id=report.get('github_run_id'), complete=report.get('complete') is True,
        initial_reference_bundle_sha256=report['bundle_sha256'],
        model_identity_sha256=report['model_identity_sha256'],
        base_model_identity_sha256=model['base_model_identity_sha256'],
        actual_endpoint_source_sha256=roles['endpoint'],
        actual_base_source_sha256=roles['meridian'],
        direct_base_seed=seed,
        initial_height_entry_source_derivation=report['initial_height_entry_source_derivation'],
        initial_free_point=initial_free_point, initial_height_input=initial_height_input,
        explicit_initial_height_used=initial_height_input is not None,
        actual_initial_full_point_sha256=initial_free_point['full_point_sha256'],
        actual_initial_height_binary64_hex=initial_free_point['height_binary64_hex'],
        actual_initial_height_exact=initial_free_point['height_exact'],
        actual_initial_point_source_mode=initial_free_point['source_mode'],
        initial_height_changes_target_or_model=False,
        initial_point_digest_recomputed_from_arrays_by_reader=False,
        frozen_moment_Q_definition=frozen_input['definition'],
        frozen_moment_Q_definition_identity_sha256=moment_identity,
        frozen_moment_Q_input_provenance=frozen_input['provenance'],
        frozen_moment_Q_input_record=report['frozen_moment_Q_input_record'],
        moment_Q_recomputed_from_current_free_point=False,
        old_zero_field_or_root_certificate_inherited=False,
        old_endpoint_coordinate_ball_certificate_inherited=False,
        new_zero_closure_seed_changes_physical_field=report['new_zero_closure_seed_changes_physical_field'],
        fixed_scalar_metric_identity_sha256=profile,
        independent_reference_binding=report['independent_reference_binding'],
        actual_new_initial_bundle_sha256=report.get('initial_new_bundle', {}).get('sha256'),
        actual_final_bundle_sha256=report.get('final_bundle_sha256'),
        initial=initial, final=final,
        initial_Phi=None if initial is None else initial['Phi'],
        final_Phi=None if final is None else final['Phi'],
        initial_max_relative_gram=None if initial is None else initial['max_relative_gram'],
        final_max_relative_gram=None if final is None else final['max_relative_gram'],
        initial_maximum_physical_g=(report.get('initial_geometry') or {}).get('maximum_physical_g'),
        final_maximum_physical_g=(report.get('final_geometry') or {}).get('maximum_physical_g'),
        final_finite_geometry_passed=None if final_geometry is None else final_geometry['true_finite_geometry_feasible'],
        actual_same_objective_change=None if initial is None or final is None else final['Phi']-initial['Phi'],
        old_parent_Phi_subtracted_from_new_field=False,
        initial_geometry=geometric(report.get('initial_geometry')), final_geometry=final_geometry,
        actual_metric_directions=metrics, actual_restoration_directions=restoration,
        actual_metric_direction_count=len(metrics), actual_restoration_direction_count=len(restoration),
        actual_accepted_metric_direction_count=sum(bool(v['accepted']) for v in metrics),
        actual_accepted_restoration_direction_count=sum(bool(v['accepted']) for v in restoration),
        final_damping=report.get('final_damping'), final_restoration_damping=report.get('final_restoration_damping'),
        coordinate_norm=norm, working_evaluation=working,
        endpoint_diagnostics=endpoint,
        actual_operator_counts=metadata.get('actual_field_counts'),
        actual_endpoint_counts=metadata.get('endpoint_counts'),
        actual_initial_read_error=report.get('actual_initial_read_error'),
        initial_endpoint_roots=endpoint_roots(report.get('initial_endpoint_roots')),
        initial_failed_candidate_is_not_an_accepted_field=report.get('initial_failed_candidate_is_not_an_accepted_field'),
        current_statistics=statistic(report.get('current'),profile),
        radial_metric_error_identically_zero_in_exact_definition=True,
        radial_identity_scope=report['radial_identity_scope'],
        numerical_radial_Gram_row_retained=True,
        radial_Gram_uses_complete_hprime_Delta=False,
        endpoint_implicit_J_separate_from_Newton=True,
        initial_position_counts=report['initial_permanent_position_counts'],
        final_position_counts=report.get('final_permanent_position_counts'),
        history=report['history'], stop_reason=report.get('stop_reason'),
        total_actual_seconds=report.get('total_actual_seconds'),
        initial_actual_setup_and_full_read_seconds=report.get('initial_actual_setup_and_full_read_seconds'),
        peak_rss_KiB=report.get('peak_rss_KiB'),
        sample_target_reached=report.get('sample_target_reached'),
        raw_scientific_arrays_recomputed=False, J_calls_by_reader=0, Jtranspose_calls_by_reader=0,
        continuous_metric_or_geometry_certified=False,
        complete_uniform_IFT_conditions_verified=False,
        complete_continuous_root_branch_certified=False,
        endpoint_root_error_enclosed=False, integration_error_enclosed=False,
        angular_root_jets_outward_enclosed=False,
        global_nonexistence_inferred_from_numerical_root_failure=False,
        refinement_convergence_claimed=False, closed_isometry_accepted=False,
        common_slack_residual_is_geometric_feasibility=False,
        quadrature_normalization_inverse_root_errors_certified=False,
        limitations=report.get('limitations', 'Actual incomplete numerical budget; no scientific success inferred'))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--report', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--verify-final-bundle', action='store_true')
    a = p.parse_args()
    result = read_report(a.repo, a.report, verify_final_bundle=a.verify_final_bundle)
    if a.output.exists():
        raise FileExistsError('Do not overwrite an actual previously bound readout')
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(result, separators=(',', ':'), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
