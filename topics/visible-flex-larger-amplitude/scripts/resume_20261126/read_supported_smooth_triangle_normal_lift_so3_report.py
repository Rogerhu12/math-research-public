#!/usr/bin/env python3
"""Bind the complete supported-smooth-triangle-reference common-normal-plane SO3 report.

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


DRIVER_SHA = 'fd95d91abe9525cbfa34d55bd576be7dfba1fe25fcafb73bdaaea40e003ad65f'
REPORT_SCHEMA = 'complete-supported-smooth-triangle-reference-fixed-normal-plane-SO3-QP-v1'


OPERATOR_SCHEMA = 'complete-supported-smooth-triangle-reference-SO3-fixed-normal-plane-six-control-zero-layer-v1'
ROOT_SNAPSHOT_SCHEMA = 'actual-fixed-normal-plane-current-point-snapshot-v1'
ROOT_SNAPSHOT_KEYS = ('current_full_point_sha256',
 'endpoint_root_policy',
 'normal_stage_count',
 'exact_normal_step_nodes',
 'actual_normal_step_carriers_binary64_hex',
 'common_partition_for_all_angles_and_free_points',
 'per_angle_adaptive_normal_partition',
 'current_cached_angle_roots',
 'current_all_grid_angle_roots_available',
 'current_all_grid_second_angular_jets_available',
 'current_maximum_endpoint_residual',
 'current_maximum_dimensionless_control_norm',
 'current_maximum_physical_z_norm',
 'current_maximum_gamma_axis_norm',
 'current_maximum_first_angular_endpoint_residual',
 'current_maximum_second_angular_endpoint_residual',
 'endpoint_counts',
 'actual_normal_counts',
 'last_root_failure',
 'normal_lift_last_summary',
 'numerical_Newton_iterations_differentiated',
 'complete_uniform_IFT_conditions_verified',
 'complete_continuous_root_branch_certified',
 'endpoint_root_error_enclosed',
 'stationary_KKT_selection_used',
 'continuous_horizontal_ODE_solution_claimed',
 'final_implicit_J_uses_all_normal_stage_equations',
 'previous_normal_frame_full_parameter_chain_retained',
 'original_zero_control_target_full_parameter_chain_retained',
 'implicit_control_dimension',
 'normal_increment_dimension',
 'implicit_dimension_per_stage',
 'complete_first_angular_implicit_dimension',
 'complete_second_angular_implicit_dimension')

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


def normal_dimensions(value, model=None):
    """Pure exact-node and dimensional contract; no normal root is evaluated."""
    count = value.get('normal_stage_count')
    words = value.get('exact_normal_step_nodes')
    if (not isinstance(count,int) or isinstance(count,bool) or count < 1
            or not isinstance(words,list) or len(words) != count+1
            or any(not isinstance(word,str) for word in words)):
        raise ValueError('Keep every exact common normal-stage node')
    nodes = [Fraction(word) for word in words]
    if (any(str(node) != word for node,word in zip(nodes,words))
            or nodes[0] != 0 or nodes[-1] != 1
            or any(a >= b for a,b in zip(nodes,nodes[1:]))):
        raise ValueError('Use one canonical exact increasing partition from zero to one')
    if (value.get('implicit_control_dimension') != 6
            or value.get('normal_increment_dimension') != 3
            or value.get('implicit_dimension_per_stage') != 9
            or value.get('complete_first_angular_implicit_dimension') != 6*count
            or value.get('complete_second_angular_implicit_dimension') != 9*count):
        raise ValueError('Retain the complete 6m/9m finite-chain implicit system')
    carriers = value.get('actual_normal_step_carriers_binary64_hex')
    if carriers is not None and carriers != [float(node).hex() for node in nodes]:
        raise ValueError('The numerical common-node carriers changed their exact declared parameters')
    if model is not None and (words != model['exact_normal_step_nodes']
            or count != model['normal_stage_count']):
        raise ValueError('This snapshot/working record belongs to a different selected normal-chain field')
    return count,nodes


def endpoint_roots(value):
    """This actual point only; no old KKT snapshot or other point is substituted."""
    if value is None:
        return None
    if value.get('schema') not in (ROOT_SNAPSHOT_SCHEMA,OPERATOR_SCHEMA):
        raise ValueError('Bind the explicit complete normal-chain snapshot contract')
    missing = [key for key in ROOT_SNAPSHOT_KEYS if key not in value]
    if missing:
        raise ValueError('The actual normal-chain snapshot lacks declared fields: '+repr(missing))
    normal_dimensions(value)
    for key in ('numerical_Newton_iterations_differentiated',
            'complete_uniform_IFT_conditions_verified','complete_continuous_root_branch_certified',
            'endpoint_root_error_enclosed','stationary_KKT_selection_used',
            'continuous_horizontal_ODE_solution_claimed','per_angle_adaptive_normal_partition'):
        if value[key] is not False:
            raise ValueError('The numerical normal-chain record cannot assert '+key)
    for key in ('common_partition_for_all_angles_and_free_points',
            'final_implicit_J_uses_all_normal_stage_equations',
            'previous_normal_frame_full_parameter_chain_retained',
            'original_zero_control_target_full_parameter_chain_retained'):
        if value[key] is not True:
            raise ValueError('The complete finite-chain derivative must retain '+key)
    result = {key:value[key] for key in ROOT_SNAPSHOT_KEYS}
    result.update(actual_snapshot_schema=value['schema'],
        all_grid_roots_available_is_a_numerical_cache_statement_only=True,
        missing_point_values_replaced_from_latest_metadata=False,
        final_endpoint_only_equation_determines_six_control_derivative=False,
        first_and_second_angular_endpoint_residuals_are_physical_length_units=True)
    return result

def bind_snapshots(value, model, roles):
    """Bind every stored short readout to this exact operator/model, without filling gaps."""
    count = 0
    if isinstance(value, dict):
        if value.get('schema') == ROOT_SNAPSHOT_SCHEMA:
            if (value.get('operator_schema') != OPERATOR_SCHEMA
                    or value.get('operator_source_sha256') != roles['endpoint']
                    or value.get('model_identity_sha256') != canonical(model)):
                raise ValueError('A stored normal-chain snapshot belongs to another actual operator/model')
            normal_dimensions(value,model)
            if value['endpoint_root_policy'] != model['root_normal_policy']:
                raise ValueError('A stored snapshot uses another complete normal-root policy')
            endpoint_roots(value)
            count += 1
        for key,child in value.items():
            if key in ('endpoint_roots','initial_endpoint_roots') and child is not None:
                if not isinstance(child,dict) or child.get('schema') != ROOT_SNAPSHOT_SCHEMA:
                    raise ValueError('Every actual point-read snapshot must use its complete NEW declared contract')
            count += bind_snapshots(child,model,roles)
    elif isinstance(value,list):
        count += sum(bind_snapshots(child,model,roles) for child in value)
    return count


def bind_literal_input(topic, report, model, roles, profile):
    """Pure binding of this supported reference, its WHOLE seed and 18 literal words."""
    value = report['frozen_moment_Q_input']
    if (report.get('moment_input_binding_mode') != 'supported-smooth-triangle-reference'
            or value.get('schema') != 'supported-smooth-triangle-reference-literal-zero-endpoint-Q-input-v1'
            or value.get('definition', {}).get('schema')
                != 'supported-smooth-triangle-reference-literal-two-bubble-endpoint-Q-v1'
            or model.get('new_reference_input_binding_source_sha256') != roles['new_moment_input']
            or report['frozen_moment_Q_input_record'].get('same_mathematical_g_claimed') is not False
            or report['frozen_moment_Q_input_record'].get('current_moment_inverse_property_claimed') is not False
            or report['frozen_moment_Q_input_record'].get('no_moment_or_inverse_recomputed') is not True
            or report['frozen_moment_Q_input_record'].get('old_reference_or_initial_point_binding_inherited') is not False):
        raise ValueError('This complete supported-reference field uses its new twelve-key pure binder only')
    path = topic/'scripts/resume_20261126/supported_smooth_triangle_literal_zero_moment_input.py'
    if sha(path) != roles['new_moment_input']:
        raise ValueError('The complete supported-reference pure input binder differs')
    spec = importlib.util.spec_from_file_location('_pure_supported_seed_Q_'+roles['new_moment_input'], path)
    binder = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = binder
    spec.loader.exec_module(binder)
    identity = binder.bind_to_base(value,
        base_model=model['base_complete_model'],
        initial_reference_bundle_sha256=report['bundle_sha256'],
        fixed_scalar_metric_identity_sha256=profile,
        initial_full_point_sha256=report['actual_reference_initial_full_point_sha256'],
        bubble_nodes=model['exact_relative_bubble_nodes'])
    if (model.get('literal_Q_input_schema') != value['schema']
            or model.get('historical_reference_same_mathematical_g_claimed') is not False):
        raise ValueError('Do not inherit an older current reference, root or target identity from parameter provenance')
    return value, identity


def supported_seed_binding(report, model, roles, frozen_input, profile):
    """Check one complete seed identity through report, normal layer, base and input."""
    base = model['base_complete_model']
    reference = base['complete_axisymmetric_reference_model']
    seed = base.get('fixed_supported_unit_seed_model')
    if not isinstance(seed, dict):
        raise ValueError('Retain the complete fixed supported-smooth-triangle seed definition')
    identity = canonical(seed)
    if (base.get('schema') != 'complete-supported-smooth-triangle-reference-so3-meridian-with-core-lift-v1'
            or seed.get('schema') != 'complete-supported-smooth-triangle-meridian-seed-reference-v1'
            or seed.get('source_sha256') != roles['seed_reference']
            or seed.get('original_reference_source_sha256') != roles['reference']
            or seed.get('mean_kernel_source_sha256') != roles['seed_mean']
            or seed.get('complete_axisymmetric_reference_model') != reference
            or seed.get('initial_reference_model_identity_sha256') != canonical(reference)
            or seed.get('initial_reference_bundle_sha256') != report['bundle_sha256']
            or seed.get('fixed_scalar_metric_identity_sha256') != profile
            or seed.get('fixed_scalar_profile_definition') != reference['fixed_scalar_profile_definition']
            or seed.get('fixed_chart_core_sha256') != base['fixed_chart_core_sha256']
            or base.get('reference_meridian_kernel_sha256') != roles['seed_reference']
            or base.get('original_axisymmetric_reference_source_sha256') != roles['reference']
            or base.get('fixed_supported_unit_seed_source_sha256') != roles['seed_reference']
            or base.get('fixed_supported_unit_seed_mean_kernel_sha256') != roles['seed_mean']
            or base.get('fixed_supported_unit_seed_identity_sha256') != identity
            or base.get('fixed_supported_unit_seed_working_definition') != seed['working_definition']
            or model.get('fixed_supported_unit_seed_identity_sha256') != identity
            or model.get('fixed_supported_unit_seed_model') != seed
            or report.get('supported_unit_seed_identity_sha256') != identity
            or report.get('supported_unit_seed_definition') != seed
            or frozen_input['definition'].get('fixed_supported_unit_seed_identity_sha256') != identity
            or frozen_input['definition'].get('fixed_supported_unit_seed_model') != seed):
        raise ValueError('The complete fixed supported seed, actual reference or fixed scalar target differs')
    for container, names in (
            (seed, ('seed_is_frozen_from_original_initial_point',
                    'outer_current_core_height_and_all_rotation_variables_retained')),
            (base, ('fixed_reference_not_recomputed_from_current_omega',
                    'all_original_outer_free_variables_and_norm_layout_unchanged')),
            (model, ('fixed_supported_unit_reference_not_rebuilt_from_current_outer_point',
                     'supported_seed_mean_inverse_not_inherited_as_normal_control_inverse')),
            (report, ('supported_unit_seed_is_frozen_from_original_core_and_height',
                      'supported_unit_seed_does_not_replace_current_outer_omega',
                      'supported_unit_mean_Jacobian_is_not_a_normal_control_inverse_certificate',
                      'original_complete_reference_and_fixed_scalar_retained'))):
        for name in names:
            if container.get(name) is not True:
                raise ValueError('The new fixed seed cannot remove or relabel the complete outer field: '+name)
    context = report.get('independent_reference_context')
    binding = report.get('supported_unit_seed_binding')
    if not isinstance(context, dict) or not isinstance(binding, dict):
        raise ValueError('Retain both actual original-reference and supported-seed bindings')
    if (context.get('schema') != reference['schema']
            or context.get('source_sha256') != roles['reference']
            or context.get('definition') != reference
            or context.get('model_identity_sha256') != canonical(reference)
            or context.get('fixed_scalar_metric_identity_sha256') != profile
            or binding.get('schema') != seed['schema']
            or binding.get('source_sha256') != roles['seed_reference']
            or binding.get('reference_model_identity_sha256') != canonical(reference)
            or binding.get('supported_unit_seed_model_identity_sha256') != identity
            or binding.get('fixed_scalar_metric_identity_sha256') != profile
            or binding.get('original_reference_source_sha256') != roles['reference']
            or binding.get('mean_kernel_source_sha256') != roles['seed_mean']
            or binding.get('complete_original_reference_input_records') != context.get('input_records')
            or binding.get('original_optimized_q_field_used') is not False
            or binding.get('seed_core_and_H_frozen_but_outer_free_variables_unchanged') is not True):
        raise ValueError('Keep actual source and byte bindings distinct from a new physical seed definition')
    records = context['input_records']
    expected = dict(reference_bundle=report['bundle_sha256'],
        carrier=report['observation_carrier_sha256'],
        node_report=report['exact_tail_node_report_sha256'],
        scalar_input=report['exact_tail_scalar_input_sha256'],
        preparation_report=report['independent_preparation_report']['sha256'])
    for role, digest in expected.items():
        if records[role]['sha256'] != digest:
            raise ValueError('A complete original input byte identity changed: '+role)
        if role != 'preparation_report' and report['independent_reference_binding']['actual_input_records'][role]['sha256'] != digest:
            raise ValueError('The actual prepared input and supported seed disagree: '+role)
    if binding.get('reference_bundle') != records['reference_bundle']:
        raise ValueError('The actual seed reference bundle record changed')
    if report.get('direct_base_seed') is not None:
        raise ValueError('This entry forbids relabeling a previous independent-base checkpoint as the supported reference')
    return dict(definition=seed, identity_sha256=identity, binding=binding)


def supported_seed_metadata(value, model, roles, supported):
    """Read actual frozen-reference work; do not promote it to current normal roots."""
    base = value['base_complete_metadata']
    seed = supported['definition']
    identity = supported['identity_sha256']
    actual = base.get('fixed_supported_unit_seed')
    if (not isinstance(actual, dict)
            or base.get('fixed_supported_unit_seed_identity_sha256') != identity
            or base.get('axisymmetric_reference_binding') != supported['binding']
            or base.get('seed_mean_Jacobian_not_a_certificate_for_current_closure_control_Jacobian') is not True
            or actual.get('schema') != seed['schema']
            or actual.get('source_sha256') != roles['seed_reference']
            or actual.get('model') != seed
            or actual.get('model_identity_sha256') != identity
            or actual.get('binding') != supported['binding']
            or actual.get('working_definition') != seed['working_definition']):
        raise ValueError('The actual provider metadata belongs to another frozen supported seed')
    for name in ('exact_seed_global_existence_hypotheses_certified',
                 'seed_physical_field_or_normal_control_rank_inherited',
                 'continuous_metric_geometry_or_full_phase_certificate'):
        if actual.get(name) is not False:
            raise ValueError('A working seed evaluation is not its accurate continuous certificate: '+name)
    plan = actual.get('radial_plan')
    if plan is not None:
        if (plan.get('schema') != 'complete-supported-smooth-triangle-seed-radial-plan-v1'
                or plan.get('source_sha256') != roles['seed_reference']
                or plan.get('seed_model_identity_sha256') != identity
                or plan.get('complete_domain') is not True
                or plan.get('complete_infinite_scalar_tail_in_complement') is not True
                or plan.get('no_scalar_tail_or_radial_piece_dropped') is not True
                or plan.get('central_profile_integral_is_separate') is not True
                or plan.get('numerical_integral_error_enclosed') is not False
                or plan.get('scalar_errors_are_not_normalization_or_integration_errors') is not True):
            raise ValueError('The actual seed radial plan must retain all pieces and its unpaid numerical fees')
    batches = actual['mean_batch_records']
    if not isinstance(batches, list):
        raise ValueError('Keep every actual completed seed-mean batch record')
    completed = []
    for batch in batches:
        metadata = batch['metadata']
        angles = batch['literal_angle_hex']
        if (batch.get('seed_model_identity_sha256') != identity
                or batch.get('fixed_original_core_H_used') is not True
                or batch.get('current_outer_free_point_not_used') is not True
                or metadata.get('schema') != 'complete-supported-smooth-triangle-seed-working-newton-mean-and-angular-jets-v1'
                or metadata.get('source_sha256') != roles['seed_mean']
                or metadata.get('complete') is not True
                or metadata.get('actual_successful_angle_count') != len(angles)):
            raise ValueError('A completed seed batch must keep its actual angle count, original point and whole kernel source')
        for word in angles:
            if not isinstance(word, str):
                raise ValueError('The fixed seed cache uses exact literal binary64 angle words')
            angle = float.fromhex(word)
            if not math.isfinite(angle) or angle.hex() != word:
                raise ValueError('A recorded fixed-seed angle word is not canonical and finite')
        for name in ('mean_root_complete','central_amplitude_root_complete',
                     'all_three_mean_components_used','all_twelve_profile_pieces_used',
                     'all_input_angles_retained','reference_angle_jets_only'):
            if metadata.get(name) is not True:
                raise ValueError('A partial mean or angular jet is not a complete seed batch: '+name)
        for name in ('continuous_contraction_verified','exact_root_or_angle_jet_errors_enclosed',
                     'quadrature_and_floating_errors_enclosed','geometry_certificate',
                     'metric_certificate','current_free_parameter_J_claimed',
                     'accurate_global_branch_association_verified'):
            if metadata.get(name) is not False:
                raise ValueError('Keep the actual seed-mean result within its numerical scope: '+name)
        completed.extend(angles)
    if len(completed) != len(set(completed)):
        raise ValueError('A completed fixed-reference batch cannot repeat a previously recorded literal angle')
    # The actual provider stores arrays and increments counters before writing
    # its runner files and appending a complete batch record. A real interrupted
    # cache write may therefore leave fewer complete records than cached values.
    # Keep those actual scopes separate, including in an initial-failure report.
    completed_cache = actual['completed_literal_angle_count']
    completed_counter = actual['counts']['completed_mean_angles']
    for number in (completed_cache, completed_counter):
        if isinstance(number, bool) or not isinstance(number, int) or number < 0:
            raise ValueError('Keep actual nonnegative integer seed cache/count readouts')
    accounting_matches = completed_cache == completed_counter == len(completed)
    failure = actual.get('last_failure')
    if failure is not None and (failure.get('schema') != seed['schema']
            or failure.get('source_sha256') != roles['seed_reference']
            or failure.get('seed_model_identity_sha256') != identity
            or failure.get('fixed_scalar_metric_identity_sha256') != model['fixed_scalar_metric_identity_sha256']
            or failure.get('complete') is not False
            or failure.get('continuous_certificate') is not False):
        raise ValueError('The recorded seed failure belongs to another source, fixed input or scientific scope')
    return dict(schema='actual-fixed-supported-smooth-triangle-reference-working-readout-v1',
        source_sha256=roles['seed_reference'], mean_kernel_source_sha256=roles['seed_mean'],
        fixed_supported_unit_seed_identity_sha256=identity,
        actual_counts=actual['counts'],
        completed_literal_angle_count=completed_cache, mean_successful_batch_count=len(batches),
        complete_batch_recorded_angle_count=len(completed),
        complete_batch_records_match_cached_angle_count=accounting_matches,
        completed_batch_literal_angle_hex=completed,
        complete_radial_plan_available=plan is not None, radial_plan=plan,
        mean_batch_records=batches,
        last_recorded_seed_failure=failure,
        last_seed_failure_phase=None if failure is None else failure['failure_phase'],
        last_seed_failure_reason=None if failure is None else failure['reason'],
        maximum_original_scalar_carrier_errors=actual['maximum_original_scalar_carrier_errors'],
        frozen_reference_cache_is_not_current_normal_root_availability=True,
        seed_mean_inverse_is_not_normal_control_inverse_certificate=True,
        fixed_seed_changed_the_original_scalar_target=False,
        exact_seed_global_existence_hypotheses_certified=False,
        seed_root_or_angle_jet_error_enclosed=False,
        seed_quadrature_or_normalization_error_enclosed=False,
        seed_continuous_metric_or_geometry_certified=False)

def endpoint_metadata(value, model, source_by_role, working_evaluation, supported):
    """Actual current/all-attempted scopes and the FULL selected finite-chain model."""
    if not value:
        return None
    if (value.get('model') != model or value.get('model_identity_sha256') != canonical(model)
            or value.get('source_sha256') != source_by_role['endpoint']
            or value.get('schema') != model['schema']
            or value.get('base_source_sha256') != source_by_role['meridian']
            or value.get('endpoint_root_policy') != working_evaluation['endpoint_root_policy']
            or value.get('endpoint_root_policy') != model['root_normal_policy']):
        raise ValueError('The actual normal-chain metadata changed its complete model/source/root policy')
    if (value.get('frozen_moment_Q_definition') != model['frozen_moment_Q_definition']
            or value.get('frozen_moment_Q_definition_identity_sha256')
                != model['frozen_moment_Q_definition_identity_sha256']
            or value.get('Q_input_recomputed_at_current_point') is not False
            or value.get('actual_working_moment_inverse_is_not_a_continuous_certificate') is not True):
        raise ValueError('The actual complete fixed literal control input changed')
    count,nodes = normal_dimensions(value,model)
    if (value.get('exact_relative_gamma_nodes') != model['exact_relative_gamma_nodes']
            or value.get('maximum_required_mixed_exponential_derivative_order') != 4
            or value.get('literal_Q_input_schema') != model['literal_Q_input_schema']
            or value.get('new_reference_input_binding_source_sha256')
                != model['new_reference_input_binding_source_sha256']):
        raise ValueError('Keep all six controls, source-bound Q modes and complete mixed derivatives')
    base = value['base_complete_metadata']
    if (base.get('model') != model['base_complete_model']
            or base.get('model_identity_sha256') != model['base_model_identity_sha256']
            or base.get('source_sha256') != source_by_role['meridian']):
        raise ValueError('The actual full independent reference metadata differs')
    for key in ('numerical_Newton_iterations_differentiated',
            'second_parameter_derivatives_supported_by_surrogate','finite_difference_J',
            'fixed_target_recomputed_from_current_field','numerical_radial_Gram_row_omitted',
            'integration_error_enclosed','symbolic_mesh_carrier_rounding_error_enclosed',
            'endpoint_root_error_enclosed','complete_uniform_IFT_conditions_verified',
            'angular_root_jets_outward_enclosed','complete_continuous_root_branch_certified',
            'old_metric_or_geometry_certificates_inherited','closed_exact_isometry_certified',
            'numerical_stage_iterations_differentiated','auxiliary_parameter_is_physical_t',
            'actual_plane_matrix_singular_values_computed'):
        if value.get(key) is not False:
            raise ValueError('No unsupported numerical-to-continuous promotion: '+key)
    for key in ('all_metric_mean_and_cross_rows_retained','radial_metric_identity_in_exact_definition',
            'cached_first_angular_branch_preserved_on_upgrade','cached_forward_stage_words_anchored_in_active_graph',
            'changing_normal_partition_changes_selected_field_definition'):
        if value.get(key) is not True:
            raise ValueError('Keep the complete actual field contract: '+key)
    summary = value['normal_lift_last_summary']
    if summary is not None and (summary['current_full_point_sha256'] != value['current_full_point_sha256']
            or summary['normal_stage_count'] != count
            or summary['exact_normal_step_nodes'] != model['exact_normal_step_nodes']
            or summary['auxiliary_nodes_are_README_physical_flex'] is not False
            or summary['complete_continuous_branch_certified'] is not False):
        raise ValueError('The normal-stage summary belongs to another point, partition or claim')
    current = endpoint_roots(value)
    seed_actual = supported_seed_metadata(value, model, source_by_role, supported)
    names = ('all_attempted_fields_maximum_successful_endpoint_residual',
        'all_attempted_fields_maximum_successful_dimensionless_control_norm',
        'all_attempted_fields_maximum_core_inverse_residual',
        'all_attempted_fields_minimum_core_inverse_sample_rho')
    return dict(current=current,all_attempted={key:value[key] for key in names},
        fixed_supported_unit_seed=seed_actual,
        actual_normal_counts=value['actual_normal_counts'],
        normal_counts_scope=value['normal_count_scope'],
        last_normal_summary=summary,complete_last_normal_batch=value['normal_lift_last_batch'],
        normal_stage_count=count,exact_normal_step_nodes=[str(v) for v in nodes],
        implicit_control_dimension=6,normal_increment_dimension=3,implicit_dimension_per_stage=9,
        complete_first_angular_implicit_dimension=6*count,complete_second_angular_implicit_dimension=9*count,
        final_implicit_J_uses_all_normal_stage_equations=True,
        previous_normal_frame_full_parameter_chain_retained=True,
        original_zero_control_target_full_parameter_chain_retained=True,
        maximum_required_mixed_exponential_derivative_order=4,
        stationary_KKT_selection_used=False,continuous_horizontal_ODE_solution_claimed=False,
        actual_field_counts=value['actual_field_counts'],endpoint_counts=value['endpoint_counts'],
        base_actual_operator_counts=base.get('actual_counts'),
        base_core_inverse_path_used=base['base_core_inverse_path_used'],
        base_actual_counts_scope=base['actual_counts_scope'],base_metadata_scope=base['metadata_scope'],
        base_reference_maximum_requested_norm_deviation=base.get('maximum_requested_reference_norm_deviation'),
        free_variables=value['free_variables'],free_core_variables=value['free_core_variables'],
        free_rotation_variables=value['free_rotation_variables'],all_free_height_variables=value['all_free_height_variables'],
        J_method=value['J_method'],Jtranspose_method=value['Jtranspose_method'],core_inverse_J=value['core_inverse_J'],
        first_parameter_implicit_derivatives_only=True,second_parameter_derivatives_supported_by_surrogate=False,
        numerical_Newton_iterations_differentiated=False,numerical_radial_Gram_row_omitted=False,
        current_root_availability_is_continuous_branch_certificate=False,
        complete_uniform_IFT_conditions_verified=False,complete_continuous_root_branch_certified=False,
        endpoint_root_error_enclosed=False,integration_error_enclosed=False,angular_root_jets_outward_enclosed=False)

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


def read_report(repo, report_path, *, verify_final_bundle=False):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    driver = topic/'scripts/resume_20261126/fullclosed_supported_smooth_triangle_normal_lift_so3_qp.py'
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
    frozen_input, moment_identity = bind_literal_input(topic,report,model,roles,profile)
    supported = supported_seed_binding(report,model,roles,frozen_input,profile)
    if (model.get('schema') != 'complete-supported-smooth-triangle-reference-SO3-fixed-normal-plane-six-control-zero-layer-v1'
            or model.get('frozen_moment_Q_definition') != frozen_input['definition']
            or model.get('frozen_moment_Q_definition_identity_sha256') != moment_identity
            or report.get('frozen_moment_Q_definition_identity_sha256') != moment_identity
            or model.get('moment_Q_recomputed_from_current_field') is not False
            or model.get('moment_Q_is_an_exact_integral_inverse_claimed') is not False
            or report.get('moment_Q_recomputed_from_current_free_point') is not False
            or report.get('old_zero_field_or_root_certificate_inherited') is not False
            or model.get('historical_original_three_root_algorithm_source_sha256') != roles['moment_original_endpoint']):
        raise ValueError('Do not replace, recompute or relabel the fixed moment-Q mathematical control input')
    working = report['working_evaluation']
    if (working.get('fixed_moment_Q_definition_identity_sha256') != moment_identity
            or working.get('old_endpoint_coordinate_ball_certificate_inherited') is not False):
        raise ValueError('The new coordinate ball has its own declared scope and no inherited old certificate')
    count,nodes = normal_dimensions(model)
    normal_dimensions(report,model)
    normal_dimensions(working,model)
    if (working['exact_relative_bubble_nodes'] != model['exact_relative_bubble_nodes']
            or working['exact_relative_gamma_nodes'] != model['exact_relative_gamma_nodes']
            or working['endpoint_root_policy'] != model['root_normal_policy']
            or float(working['endpoint_root_policy']['control_radius']).hex() != model['root_control_radius_hex']
            or working.get('quadrature_error_enclosed') is not False
            or working.get('root_error_enclosed') is not False
            or working.get('evaluation_refinement_changes_exact_target') is not False):
        raise ValueError('The actual numerical normal-root/evaluation policy is not an error enclosure')
    for container in (model,report):
        for key in ('stationary_KKT_selection_used','continuous_horizontal_ODE_solution_claimed',
                    'per_angle_adaptive_normal_partition'):
            if container.get(key) is not False:
                raise ValueError('This fixed-plane numerical field cannot claim '+key)
        if container.get('common_partition_for_all_angles_and_free_points') is not True:
            raise ValueError('Every actual angle/candidate must use the SAME complete exact partition')
        if any(key in container for key in ('KKT_dimension','selected_KKT_stationary_branch','implicit_control_cost')):
            raise ValueError('A normal-plane field cannot retain a stationary-KKT dimension or cost label')
    if (model.get('normal_partition_is_part_of_selected_field_definition') is not True
            or model.get('fixed_finite_normal_planes_are_distinct_selection') is not True
            or report.get('normal_auxiliary_nodes_are_physical_flex') is not False
            or report.get('normal_selection_changes_fixed_g') is not False
            or report.get('numerical_normal_stage_iterations_differentiated') is not False
            or report.get('final_implicit_J_uses_all_normal_stage_equations') is not True
            or report.get('previous_normal_frame_full_parameter_chain_retained') is not True
            or report.get('original_zero_control_target_full_parameter_chain_retained') is not True):
        raise ValueError('Keep the common finite selection and its COMPLETE upstream implicit derivative chain')
    if report.get('final_original_physical_closure_is_separately_checked') is not True:
        raise ValueError('A normalized plane residual cannot replace the final original physical closure tolerance')
    snapshot_count = bind_snapshots(report,model,roles)
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
    endpoint = endpoint_metadata(metadata, model, roles, working, supported)
    failed_initial = report.get('actual_initial_read_error') is not None
    if failed_initial and (report.get('complete') is True
            or report.get('initial_failed_candidate_is_not_an_accepted_field') is not True
            or metrics or restoration or report.get('final_bundle_sha256') is not None):
        raise ValueError('An initial endpoint/field-read failure is not a completed or accepted candidate')
    if report.get('complete') is True and endpoint is None:
        raise ValueError('A complete zero-closure budget needs its actual endpoint diagnostics')
    return dict(schema='actual-complete-supported-smooth-triangle-fixed-normal-plane-SO3-scalar-readout-v1',
        reader_sha256=sha(__file__), report_path=str(Path(report_path).resolve()),
        report_sha256=sha(report_path), report_bytes=Path(report_path).stat().st_size,
        actual_driver_sha256=DRIVER_SHA, actual_source_commit=report['source_commit'],
        workflow_trigger_commit=report.get('workflow_trigger_commit'),
        github_run_id=report.get('github_run_id'), complete=report.get('complete') is True,
        initial_reference_bundle_sha256=report['bundle_sha256'],
        model_identity_sha256=report['model_identity_sha256'],
        base_model_identity_sha256=model['base_model_identity_sha256'],
        supported_unit_seed_definition=supported['definition'],
        supported_unit_seed_identity_sha256=supported['identity_sha256'],
        supported_unit_seed_binding=supported['binding'],
        seed_diagnostics=None if endpoint is None else endpoint['fixed_supported_unit_seed'],
        seed_mean_inverse_is_not_current_normal_control_inverse_certificate=True,
        old_independent_base_checkpoint_relabelled=False,
        actual_endpoint_source_sha256=roles['endpoint'],
        actual_base_source_sha256=roles['meridian'],
        moment_input_binding_mode=report['moment_input_binding_mode'],
        actual_reference_initial_full_point_sha256=report['actual_reference_initial_full_point_sha256'],
        actual_bound_current_point_snapshot_count=snapshot_count,
        snapshot_values_backfilled_from_other_points=False,
        implicit_control_dimension=6,normal_increment_dimension=3,implicit_dimension_per_stage=9,
        normal_stage_count=count,exact_normal_step_nodes=[str(v) for v in nodes],
        complete_first_angular_implicit_dimension=6*count,complete_second_angular_implicit_dimension=9*count,
        exact_relative_gamma_nodes=model['exact_relative_gamma_nodes'],
        stationary_KKT_selection_used=False,continuous_horizontal_ODE_solution_claimed=False,
        common_partition_for_all_angles_and_free_points=True,per_angle_adaptive_normal_partition=False,
        final_implicit_J_uses_all_normal_stage_equations=True,
        direct_base_seed=seed,
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
