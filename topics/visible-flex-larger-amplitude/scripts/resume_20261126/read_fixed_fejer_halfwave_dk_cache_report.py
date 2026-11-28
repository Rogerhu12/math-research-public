#!/usr/bin/env python3
"""Pure complete R715 reference-centred R711 normal-chain attribution.

All original normal snapshots, Phase I, full geometry/metric/history and
source/model guards remain. Raw quadrature closure and the centred root
equation have separate own-point records. A complete physical sixjet lift is
mandatory; working radial identity is never asserted. No F/J, root, integral
or scientific array is recomputed by this pure reader.
"""
import argparse
import ast
import hashlib
from fractions import Fraction
import importlib.util
import sys
import textwrap
import json
import math
from pathlib import Path


DRIVER_SHA = "7883d9fac2422509e5577fada1ed58f7a0d83f76031d00f3abf9aa41d5159910"
REPORT_SCHEMA = "complete-fixed-fejer-paired-halfwave-dk-cache-SO3-QP-v1"


OPERATOR_SCHEMA = "complete-fixed-fejer-paired-halfwave-detached-meridian-normal-layer-v1"
ROOT_SNAPSHOT_SCHEMA = "actual-fixed-fejer-immutable-point-current-point-snapshot-v1"
ROOT_SNAPSHOT_KEYS = ('current_full_point_sha256', 'endpoint_root_policy', 'normal_stage_count', 'exact_normal_step_nodes', 'actual_normal_step_carriers_binary64_hex', 'common_partition_for_all_angles_and_free_points', 'per_angle_adaptive_normal_partition', 'current_cached_angle_roots', 'current_all_grid_angle_roots_available', 'current_all_grid_second_angular_jets_available', 'current_maximum_endpoint_residual', 'current_maximum_dimensionless_control_norm', 'current_maximum_physical_z_norm', 'current_maximum_gamma_axis_norm', 'current_maximum_first_angular_endpoint_residual', 'current_maximum_second_angular_endpoint_residual', 'endpoint_counts', 'actual_normal_counts', 'last_root_failure', 'normal_lift_last_summary', 'numerical_Newton_iterations_differentiated', 'complete_uniform_IFT_conditions_verified', 'complete_continuous_root_branch_certified', 'endpoint_root_error_enclosed', 'stationary_KKT_selection_used', 'continuous_horizontal_ODE_solution_claimed', 'final_implicit_J_uses_all_normal_stage_equations', 'previous_normal_frame_full_parameter_chain_retained', 'original_zero_control_target_full_parameter_chain_retained', 'implicit_control_dimension', 'normal_increment_dimension', 'implicit_dimension_per_stage', 'complete_first_angular_implicit_dimension', 'complete_second_angular_implicit_dimension', 'current_reference_calibration', 'analytic_stage_jacobian', 'analytic_normal_frame', 'detached_closure_value_reuse')

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




def read_frame_reuse_policy(path):
    """Evaluate the complete explicitly source-bound pure C1 policy and AST overrides."""
    tree = ast.parse(Path(path).read_text())
    names = {'SCHEMA','ORIGINAL_CENTERED_SOURCE','METHOD_AST','ANALYTIC_STAGE_SOURCE_SHA256',
        'METHOD_SOURCE_OVERRIDES','CLOSURE_VALUE_SOURCE_SHA256'}
    functions = {'sha','definition','_new_counts','canonical','_ast_value','complete_method_ast'}
    body = []
    seen_names,seen_functions = set(),set()
    for node in tree.body:
        if isinstance(node,ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0],ast.Name):
            name = node.targets[0].id
            if name in names:
                ast.literal_eval(node.value)
                body.append(node)
                seen_names.add(name)
        if isinstance(node,ast.FunctionDef) and node.name in functions:
            body.append(node)
            seen_functions.add(node.name)
    if seen_names != names or seen_functions != functions:
        raise ValueError('The complete source-bound C1 policy is not independently readable')
    namespace = dict(Path=Path,hashlib=hashlib,json=json,math=math,ast=ast,textwrap=textwrap,__file__=str(path))
    exec(compile(ast.Module(body=body,type_ignores=[]),'<bound pure C1 policy>','exec'),namespace)
    return namespace['definition'](),set(namespace['_new_counts']())


def frame_reuse_binding(report,model,roles,helper_path):
    if sha(helper_path) != roles['frame_C1']:
        raise ValueError('Bind the complete independent C1 helper bytes')
    expected,count_keys = read_frame_reuse_policy(helper_path)
    if (model.get('normal_frame_C1_reuse') != expected
            or report.get('normal_frame_C1_reuse_definition') != expected
            or report.get('normal_frame_C1_source',{}).get('sha256') != roles['frame_C1']
            or expected['source_sha256'] != roles['frame_C1']
            or expected['minimum_generic_full_batch_repetitions'] != 8
            or expected['complete_zero_control_jet_analytic_template_enabled'] is not True):
        raise ValueError('Keep the complete declared same-graph/zero-template policy and source')
    if (report.get('all_normal_stage_equations_and_matrices_retained_with_frame_reuse') is not True
            or report.get('frame_reuse_speedup_or_rounding_certified') is not False):
        raise ValueError('A frame cache may not delete stage equations or claim unobserved performance')
    return dict(definition=expected,definition_identity_sha256=canonical(expected),
        source_sha256=roles['frame_C1'],counter_keys=sorted(count_keys),
        all_original_outer_variables_and_all_normal_stages_retained=True,
        no_prior_plain_centred_scientific_run_required=True,
        actual_speedup_or_rounding_certificate=False)


def frame_reuse_metadata(value,model,roles,binding):
    actual = value.get('normal_frame_C1_reuse')
    if (not isinstance(actual,dict)
            or actual.get('schema') != binding['definition']['schema']
            or actual.get('source_sha256') != roles['frame_C1']
            or actual.get('definition') != binding['definition']
            or actual.get('actual_operator_source_sha256') != roles['endpoint']
            or actual.get('actual_model_identity_sha256') != canonical(model)):
        raise ValueError('The recorded C1 counters belong to another complete field or source')
    counter_keys = set(binding['counter_keys'])
    def counts(record):
        if (not isinstance(record,dict) or set(record) != counter_keys
                or any(type(v) is not int or v < 0 for v in record.values())):
            raise ValueError('Keep every actual nonnegative C1 counter, without missing-zero backfills')
        return dict(record)
    total = counts(actual.get('actual_counts'))
    for name in ('scopes_started','scopes_closed','value_scopes_started','value_scopes_closed'):
        if type(actual.get(name)) is not int or actual[name] < 0:
            raise ValueError('Keep actual integer scope counts')
    if (actual['scopes_closed'] > actual['scopes_started']
            or actual['value_scopes_closed'] > actual['value_scopes_started']):
        raise ValueError('More scopes cannot finish than were actually started')
    seconds = actual.get('scope_seconds')
    if (isinstance(seconds,bool) or not isinstance(seconds,(int,float))
            or not math.isfinite(seconds) or seconds < 0):
        raise ValueError('Keep actual finite elapsed time, not an assumed saving')
    for key in ('active_graphs_stored_in_kernel','duplicate_rate_or_acceleration_claimed',
            'complete_parameter_Hessian_supported','arithmetic_errors_enclosed'):
        if actual.get(key) is not False:
            raise ValueError('No stronger caching or numerical claim is authorized: '+key)
    for key in ('scope_seconds_include_the_owning_stage_chain',
            'scope_seconds_exclude_later_external_backward'):
        if actual.get(key) is not True:
            raise ValueError('Do not relabel the actual timing scope: '+key)
    summaries = {}
    for name,started in (('last_scope','scopes_started'),('last_value_scope','value_scopes_started')):
        record = actual.get(name)
        if record is None:
            summaries[name] = None
            continue
        if not isinstance(record,dict) or not isinstance(record.get('binding'),dict):
            raise ValueError('Keep the actual own-scope complete record or null')
        b = record['binding']
        if (b.get('actual_model_identity_sha256') != canonical(model)
                or b.get('normal_stage_count') != model['normal_stage_count']
                or b.get('angular_order') not in (1,2)
                or type(b.get('literal_angle_count')) is not int or b['literal_angle_count'] < 1
                or b.get('complete_control_jet_shape') != [b['literal_angle_count'],3,6]
                or type(b.get('scope_serial')) is not int
                or not 1 <= b['scope_serial'] <= actual[started]):
            raise ValueError('The full cached scope/shape/partition changed')
        for key in ('actual_full_free_point_sha256','literal_phi_words_sha256'):
            word = b.get(key)
            if not isinstance(word,str) or len(word) != 64 or any(c not in '0123456789abcdef' for c in word):
                raise ValueError('Keep the complete actual point/angle digest')
        current = counts(record.get('counts'))
        if any(v > total[k] for k,v in current.items()):
            raise ValueError('A recorded scope cannot exceed its cumulative actual counters')
        completed = record.get('stage_requests_completed')
        if (type(completed) is not int or not 0 <= completed <= model['normal_stage_count']
                or record.get('all_stage_frame_requests_completed') is not (completed == model['normal_stage_count'])
                or record.get('scientific_success_inferred') is not False):
            raise ValueError('A partial frame scope cannot imply a complete physical field')
        elapsed = record.get('scope_seconds')
        if (isinstance(elapsed,bool) or not isinstance(elapsed,(int,float))
                or not math.isfinite(elapsed) or elapsed < 0):
            raise ValueError('Keep the actual own-scope elapsed time')
        if name == 'last_scope':
            if (b.get('same_invocation_graph_only') is not True
                    or b.get('working_frames_anchored_by_original_stage') is not True
                    or record.get('graph_released_from_scope') is not True
                    or record.get('numerical_template_or_AD_rounding_enclosed') is not False):
                raise ValueError('The active C1 scope lost its full upstream/rounding contract')
        else:
            if (b.get('all_stage_roots_matrices_residual_rereads_and_trace_retained') is not True
                    or b.get('outer_parameter_derivatives_obtained_from_this_cache') is not False
                    or record.get('derivative_graph_borrowed_by_active_scope') is not False
                    or record.get('unexecuted_AD_reread_words_claimed_equal') is not False):
                raise ValueError('Detached numerical values cannot replace the active derivative chain')
        summaries[name] = dict(binding=b,counts=current,stage_requests_completed=completed,
            all_stage_frame_requests_completed=record['all_stage_frame_requests_completed'],
            scope_seconds=elapsed,
            point_is_current_metadata_point=b['actual_full_free_point_sha256']==value['current_full_point_sha256'],
            own_point_values_backfilled_from_current_point=False,
            optional_failures=record.get('template_failures',record.get('optional_cache_failures',[])))
    return dict(source_sha256=roles['frame_C1'],definition=binding['definition'],
        actual_counts=total,scopes_started=actual['scopes_started'],scopes_closed=actual['scopes_closed'],
        value_scopes_started=actual['value_scopes_started'],value_scopes_closed=actual['value_scopes_closed'],
        scope_seconds=seconds,**summaries,
        costs_include_failed_or_rejected_attempts=True,scope_records_keep_their_own_point=True,
        later_outer_backward_is_not_included_in_scope_timer=True,
        actual_speedup_or_rounding_certified=False,outer_parameter_Hessian_supported=False)



def read_detached_matrix_policy(path):
    """Read the whole pinned helper's explicitly selected pure stdlib interface."""
    tree = ast.parse(Path(path).read_text())
    names = {'SCHEMA','FRAME_C1_SOURCE_SHA256','ORIGINAL_C1_OPERATOR_SOURCE_SHA256',
        'BASE_SOURCE_SHA256','PHASES','NORMAL_COUNTER_KEYS','ANALYTIC_STAGE_SOURCE_SHA256'}
    wanted = {'sha','canonical','definition','_new_counts','_plain_copy','_valid_digest',
        '_finite_nonnegative','_validated_counts','validate_metadata'}
    body,seen_names,seen_functions = [],set(),set()
    for node in tree.body:
        if isinstance(node,ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0],ast.Name):
            name = node.targets[0].id
            if name in names:
                ast.literal_eval(node.value)
                body.append(node)
                seen_names.add(name)
        if isinstance(node,ast.FunctionDef) and node.name in wanted:
            body.append(node)
            seen_functions.add(node.name)
    if seen_names != names or seen_functions != wanted:
        raise ValueError('Keep the complete source-bound detached-matrix pure policy and validator')
    namespace = dict(Path=Path,hashlib=hashlib,json=json,math=math,__file__=str(path))
    exec(compile(ast.Module(body=body,type_ignores=[]),'<bound pure detached-matrix metadata>','exec'),namespace)
    return namespace['definition'](),namespace['validate_metadata']


def detached_matrix_binding(report,model,roles,path):
    if sha(path) != roles['stage_matrices']:
        raise ValueError('Bind the entire independently published detached-matrix helper')
    expected,validator = read_detached_matrix_policy(path)
    if (model.get('detached_stage_matrix_reuse') != expected
            or report.get('detached_stage_matrix_reuse_definition') != expected
            or report.get('detached_stage_matrix_source',{}).get('sha256') != roles['stage_matrices']
            or report.get('all_original_Newton_stage_equations_and_full_implicit_chain_retained') is not True
            or report.get('stage_matrix_cache_acceleration_or_rounding_certified') is not False):
        raise ValueError('Numerical matrix reuse must preserve the complete original stage and field contract')
    binding = dict(definition=expected,definition_identity_sha256=canonical(expected),
        source_sha256=roles['stage_matrices'],all_original_free_variables_and_stages_retained=True,
        selected_local_matrices_unchanged_by_cache=True,prior_uncached_run_required=False,
        numerical_matrix_origin_is_distinct_from_current_stage_root=True,
        acceleration_or_error_certificate=False)
    def read_metadata(value):
        if value is None or value == {}:
            return None
        if not isinstance(value,dict):
            raise ValueError('Keep the actual complete operator metadata or absence')
        return validator(value.get('detached_stage_matrix_reuse'),model=model,
            source_by_role=roles,current_full_point_sha256=value.get('current_full_point_sha256'))
    return binding,read_metadata


def read_adjacent_frame_policy(path):
    """Read only the complete pinned helper's pure standard-library interface."""
    tree=ast.parse(Path(path).read_text())
    names={'SCHEMA','FRAME_C1_SOURCE_SHA256','STAGE_MATRIX_SOURCE_SHA256',
        'PARENT_OPERATOR_SOURCE_SHA256','BASE_SOURCE_SHA256','COUNTER_KEYS','ANALYTIC_STAGE_SOURCE_SHA256'}
    wanted={'sha','canonical','definition','_copy','_digest','validate_metadata'}
    body=[];seen_names=set();seen_functions=set()
    for node in tree.body:
        if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
            name=node.targets[0].id
            if name in names:
                ast.literal_eval(node.value);body.append(node);seen_names.add(name)
        if isinstance(node,ast.FunctionDef) and node.name in wanted:
            body.append(node);seen_functions.add(node.name)
    if seen_names!=names or seen_functions!=wanted:
        raise ValueError('Retain the entire source-bound adjacent-frame pure contract')
    namespace=dict(Path=Path,hashlib=hashlib,json=json,math=math,__file__=str(path))
    exec(compile(ast.Module(body=body,type_ignores=[]),'<bound adjacent-frame metadata>','exec'),namespace)
    return namespace['definition'](),namespace['validate_metadata']


def adjacent_frame_binding(report,model,roles,path):
    if sha(path)!=roles['adjacent_matrices']:
        raise ValueError('Bind the whole actual adjacent-frame producer source')
    expected,validator=read_adjacent_frame_policy(path)
    if (model.get('adjacent_normal_frame_matrices')!=expected
            or report.get('adjacent_normal_frame_matrix_definition')!=expected
            or report.get('adjacent_normal_frame_matrix_source',{}).get('sha256')!=roles['adjacent_matrices']
            or report.get('adjacent_matrix_rounding_is_independent') is not True
            or report.get('adjacent_matrix_acceleration_or_error_certified') is not False):
        raise ValueError('Keep the independent working products and original complete root/field responsibilities')
    binding=dict(definition=expected,definition_identity_sha256=canonical(expected),
        source_sha256=roles['adjacent_matrices'],selected_local_J3_and_original_root_active_chain_retained=True,
        old_higher_order_roots_not_discarded=True,prior_plain_run_required=False,
        actual_matrix_origin_separate_from_root_success=True,acceleration_or_error_certificate=False)
    def read_metadata(value):
        if value is None or value=={}:return None
        if not isinstance(value,dict):raise ValueError('Keep actual complete operator metadata or absence')
        answer=validator(value.get('adjacent_normal_frame_matrices'),
            model_identity=canonical(model),operator_source_sha256=roles['endpoint'],
            expected_definition=expected)
        last=answer.get('last_call')
        answer['last_call_point_matches_latest_operator_point']=(None if last is None else
            last['current_full_point_sha256']==value.get('current_full_point_sha256'))
        return answer
    return binding,read_metadata


def transferred_envelope_binding(topic,report,model,roles,driver):
    relative,expected = load_pins(driver)['envelope_transfer']
    path = topic/relative
    if (sha(path) != expected or roles['envelope_transfer'] != expected
            or report.get('material_envelope_transfer_source',{}).get('sha256') != expected):
        raise ValueError('Keep the complete independent address/type transfer source')
    name = '_actual_complete_envelope_transfer_'+expected
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    for function in (module.definition,module.validate_metadata,module.validate_seed_metadata):
        if sha(function.__code__.co_filename) != expected:
            raise ValueError('Use the complete source-bound pure transfer policy and validator')
    if report.get('material_envelope_transfer_definition') != module.definition():
        raise ValueError('The actual transfer policy is not the complete declared source policy')
    transfer = module.validate_metadata(report.get('material_envelope_transfer'),model=model,
        envelope=report['material_envelope'],caller_source_sha256=DRIVER_SHA,
        carrier_sha256=report['observation_carrier_sha256'])
    raw_transfer=report['material_envelope_transfer']
    if raw_transfer.get('current_invocation_memory_mode')=='explicit-independent-branch':
        original=model['reference_centering_definition']['original_reference_point_sha256']
        if (report.get('initial_full_variable_point_sha256')!=original
                or report.get('actual_reference_initial_full_point_sha256')!=original
                or report.get('prior_envelope_final_variable_seed') is not None):
            raise ValueError('The independent branch must really start from its complete original reference point')
    seed = module.validate_seed_metadata(report.get('prior_envelope_final_variable_seed'),
        report=report,model=model,transfer=report['material_envelope_transfer'])
    return transfer,seed


def material_envelope_binding(topic, report, roles, driver):
    """Bind the new finite responsibility and working-row policy without scientific recomputation."""
    actual_source=report.get('material_envelope_source',{}).get('sha256')
    candidates=[role for role in ('envelope_memory','independent_envelope_memory')
        if roles.get(role)==actual_source]
    if len(candidates)!=1:
        raise ValueError('Bind one explicit complete original or current-restorer memory source')
    role=candidates[0]
    relative, expected_source = load_pins(driver)[role]
    path = topic/relative
    if sha(path) != expected_source or roles.get(role) != expected_source:
        raise ValueError('Keep the complete independent material-envelope memory source')
    name = '_actual_complete_material_envelope_reader_'+expected_source
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    for function in (module.definition,module.validate_report_metadata,module.validate_scan_metadata):
        if sha(function.__code__.co_filename) != expected_source:
            raise ValueError('Use the actual whole-source pure envelope validators')
    cap = report.get('material_envelope_near_active_rows')
    if type(cap) is not int or cap < 1:
        raise ValueError('The independently declared near-active candidate cap must be positive')
    expected = module.definition(near_active_rows=cap)
    actual = report.get('material_envelope')
    if (not isinstance(actual,dict) or actual.get('definition') != expected
            or report.get('material_envelope_definition') != expected
            or report.get('material_envelope_source',{}).get('sha256') != expected_source
            or report.get('material_envelope_rows_source',{}).get('sha256') != roles['envelope_rows']
            or report.get('material_envelope_new_working_set_policy') is not True
            or report.get('unknown_historical_protected_labels_reconstructed') is not False
            or report.get('old_protected_required_priority_equivalence_claimed') is not False
            or report.get('full_material_envelope_nonlinear_responsibility') is not True):
        raise ValueError('Do not call the new complete envelope an unchanged old protected-row policy')
    validated = module.validate_report_metadata(actual,
        model_identity=report['model_identity_sha256'],
        carrier_sha256=report['observation_carrier_sha256'])
    if not isinstance(validated,dict):
        raise ValueError('The complete pure envelope attribution must return its actual validated summary')
    binding = dict(definition=expected,definition_identity_sha256=canonical(expected),
        source_sha256=expected_source,rows_source_sha256=roles['envelope_rows'],
        actual_metadata=validated,old_unknown_protected_tags_reconstructed=False,
        old_required_row_priority_equivalence_claimed=False,
        nonlinear_responsibility_is_complete_permanent_envelope=True,
        continuous_geometry_or_metric_certificate=False)
    def validate_scan(value):
        checked = module.validate_scan_metadata(value,model_identity=report['model_identity_sha256'],
            carrier_sha256=report['observation_carrier_sha256'])
        if checked.get('definition') != expected or checked.get('definition_identity_sha256') != canonical(expected):
            raise ValueError('Every actual scan must retain this report exact same complete envelope policy')
        return checked
    def validate_rows(rows, starting_geometry):
        if not isinstance(rows,dict) or not isinstance(starting_geometry,dict):
            raise ValueError('Every completed direction has its own complete row preparation and starting scan')
        checked_scan = validate_scan(starting_geometry.get('material_envelope'))
        prefix = rows.get('known_geometry_and_amplitude_prefix_rows')
        total = rows.get('selected_rows')
        columns = rows.get('coordinate_size')
        added = rows.get('appended_envelope_rows')
        if (any(type(v) is not int or v < 0 for v in (prefix,total,columns,added))
                or columns < 1 or columns != report['original_variables']):
            raise ValueError('Use actual nonnegative row counts and every positive full coordinate column')
        before = rows.get('known_prefix_sha256')
        if (not isinstance(before,str) or len(before) != 64
                or any(c not in '0123456789abcdef' for c in before)
                or rows.get('known_prefix_after_append_sha256') != before
                or rows.get('known_prefix_bytes') != prefix*columns*8
                or rows.get('row_cache_bytes') != total*columns*8
                or rows.get('known_prefix_rewritten') is not False
                or rows.get('envelope_rows_start_index') != prefix
                or rows.get('current_full_point_sha256') != starting_geometry.get('current_full_point_sha256')
                or checked_scan.get('complete') is not True):
            raise ValueError('The measured original prefix and complete current coordinate cache must be retained')
        typed = rows.get('material_envelope_rows',{})
        selection = typed.get('selection',{})
        if (typed.get('source_sha256') != roles['envelope_rows']
                or typed.get('current_full_point_sha256') != rows['current_full_point_sha256']
                or typed.get('actual_model_identity_sha256') != report['model_identity_sha256']
                or typed.get('policy_identity_sha256') != canonical(expected)
                or typed.get('actual_appended_typed_count') != added
                or typed.get('actual_new_rows_sha256') != canonical(rows['rows'][prefix:])
                or typed.get('permanent_typed_rows_not_capped') is not True
                or typed.get('all_original_free_coordinates_retained') is not True
                or typed.get('original_common_slack_includes_all_appended_rows') is not True
                or typed.get('original_nonlinear_thresholds_unchanged') is not True
                or typed.get('continuous_geometry_certified') is not False
                or selection.get('new_near_active_row_cap') != cap
                or selection.get('active_band') != report.get('material_envelope_active_band')):
            raise ValueError('The complete appended typed rows need their own actual policy/source/point and full pullback')
        memory = module.validate_report_metadata(rows.get('material_envelope'),
            model_identity=report['model_identity_sha256'],carrier_sha256=report['observation_carrier_sha256'])
        if (memory.get('definition_identity_sha256') != canonical(expected)
                or typed.get('actual_permanent_typed_count') != memory['actual_separation_memory_count']):
            raise ValueError('The actual appended-row snapshot must retain the complete uncapped separation memory')
        return dict(source_sha256=roles['envelope_rows'],policy_identity_sha256=canonical(expected),
            current_full_point_sha256=rows['current_full_point_sha256'],
            measured_prefix_sha256=before,measured_prefix_unchanged=True,
            actual_appended_typed_count=added,
            actual_permanent_typed_count=typed['actual_permanent_typed_count'],
            actual_new_rows_sha256=typed['actual_new_rows_sha256'],
            actual_envelope_row_seconds=typed.get('elapsed_seconds'),
            selection=typed.get('selection'),continuous_geometry_certified=False)
    return binding,validate_scan,validate_rows

def calibration_snapshot(value, point=None, definition=None):
    """Only own-point recorded raw/centred maxima; missing values stay missing."""
    keys = {'reference_point_sha256','current_full_point_sha256','raw_value_max',
        'raw_phi_max','raw_phiphi_max','centered_value_max','centered_phi_max',
        'centered_phiphi_max','working_radial_identity','complete_raw_defect_lift',
        'equation_scope'}
    if not isinstance(value,dict) or set(value) != keys:
        raise ValueError('Keep the complete explicit current reference-calibration readout')
    for name in ('reference_point_sha256','current_full_point_sha256'):
        word = value[name]
        if word is None and name == 'current_full_point_sha256':
            continue
        if not isinstance(word,str) or len(word) != 64 or any(c not in '0123456789abcdef' for c in word):
            raise ValueError('The actual full point digest is not a complete SHA256')
    if point != value['current_full_point_sha256']:
        raise ValueError('Do not backfill another current point calibration')
    if definition is not None and value['reference_point_sha256'] != definition['original_reference_point_sha256']:
        raise ValueError('The frozen ORIGINAL reference point changed')
    for name in ('raw_value_max','raw_phi_max','raw_phiphi_max',
                 'centered_value_max','centered_phi_max','centered_phiphi_max'):
        number = value[name]
        if number is not None and (isinstance(number,bool) or not isinstance(number,(int,float))
                or not math.isfinite(number) or number < 0):
            raise ValueError('Keep actual finite nonnegative recorded norms or null')
    if (value['working_radial_identity'] is not False or value['complete_raw_defect_lift'] is not True
            or value['equation_scope'] != 'reference-centred complete equation; distinct raw quadrature defect'):
        raise ValueError('A centred root cannot remove the full physical raw-defect lift')
    return dict(value)


def centering_binding(report, model, roles):
    """Pure source/model/original-point binding; no reference integral is recomputed."""
    value = model.get('reference_centering_definition')
    base = model['base_complete_model']
    seed = base['fixed_supported_unit_seed_model']
    if (not isinstance(value,dict)
            or value.get('schema') != 'R715-fixed-reference-centred-working-normal-definition-v1'
            or value.get('source_sha256') != roles['reference_calibration']
            or value.get('endpoint_source_sha256') != roles['endpoint']
            or value.get('original_complete_normal_source_sha256') !=
                '66e81e439a2545134549b4527e68a2480a9d8010679dcf9cfa23ca5e48c15d68'
            or value.get('original_reference_point_sha256') != report['actual_reference_initial_full_point_sha256']
            or value.get('original_reference_point_sha256') != report.get('frozen_original_reference_point_sha256')
            or value.get('original_height_hex') != seed['initial_height_hex']
            or value.get('base_model_identity_sha256') != model['base_model_identity_sha256']
            or value.get('fixed_supported_reference_identity_sha256') != canonical(seed)
            or value.get('mesh_sha256') != model['mesh_sha256']
            or value.get('integration_order') != report['working_evaluation']['integration_order']
            or report.get('reference_centering_definition') != value
            or report.get('reference_centering_source',{}).get('sha256') != roles['reference_calibration']):
        raise ValueError('The fixed centering definition must bind this complete original reference and exact working rule')
    for name in ('nodewise_difference_before_original_complete_cumsum',
                 'exact_equality_to_original_closure_requires_exact_reference_closure',
                 'all_normal_stages_and_full_upstream_parameter_jets_retained'):
        if value.get(name) is not True:
            raise ValueError('Keep the full reference-centred mathematical/numerical contract: '+name)
    for name in ('numerical_current_raw_closure_defect_omitted',
                 'numerical_radial_Gram_error_identically_zero'):
        if value.get(name) is not False:
            raise ValueError('A numerical defect cannot be promoted to an identity: '+name)
    for name in ('gauss_nodes_sha256','gauss_weights_sha256'):
        word = value.get(name)
        if not isinstance(word,str) or len(word) != 64 or any(c not in '0123456789abcdef' for c in word):
            raise ValueError('Retain the actual complete fixed integration-carrier digest')
    for name in ('complete_current_raw_closure_lift_and_all_sixjet_derivatives_retained',
                 'raw_quadrature_defect_is_not_the_centred_root_residual',
                 'all_normal_stages_retained_at_literal_reference_zero',
                 'final_reference_centred_closure_is_separately_checked',
                 'raw_physical_closure_is_retained_in_complete_lift'):
        if report.get(name) is not True:
            raise ValueError('The current complete field omits a centering/lift responsibility: '+name)
    if report.get('final_original_physical_closure_is_separately_checked') is not False:
        raise ValueError('The root tolerance applies to the centred equation, not a separately zero raw quadrature defect')
    return dict(definition=value,definition_identity_sha256=canonical(value),
        source_sha256=roles['reference_calibration'],
        original_reference_point_sha256=value['original_reference_point_sha256'],
        raw_physical_closure_and_centred_root_residual_are_distinct=True,
        exact_reference_and_working_fees_certified=False)


def calibration_metadata(value, model, roles):
    """Bind actual frozen batches and own-point lift statistics without raw recomputation."""
    definition = model['reference_centering_definition']
    actual = value.get('reference_centering')
    if (not isinstance(actual,dict)
            or actual.get('schema') != 'complete-R715-frozen-reference-working-calibration-v1'
            or actual.get('source_sha256') != roles['reference_calibration']
            or actual.get('definition') != definition
            or actual.get('model_identity_sha256') != canonical(model)
            or actual.get('reference_point_sha256') != definition['original_reference_point_sha256']):
        raise ValueError('The actual reference calibration belongs to another complete field')
    for name in ('physical_field_uses_complete_current_raw_defect_lift',
                 'lift_includes_all_current_parameter_and_angular_derivatives'):
        if actual.get(name) is not True:
            raise ValueError('The current physical lift must remain complete: '+name)
    for name in ('baseline_reselected_from_current_outer_point','raw_reference_defect_forced_to_zero',
                 'numerical_radial_Gram_identity_claimed','accurate_reference_or_quadrature_or_geometry_certified'):
        if actual.get(name) is not False:
            raise ValueError('The actual calibration may not assert '+name)
    current = calibration_snapshot(actual.get('current'),value['current_full_point_sha256'],definition)
    if value.get('current_reference_calibration') != current:
        raise ValueError('Keep the SAME current-point raw/centred calibration in metadata and snapshots')
    records = actual.get('actual_reference_records')
    if not isinstance(records,list) or actual.get('fixed_endpoint_angle_batches') != len(records):
        raise ValueError('Keep every actual completed frozen-reference angle batch')
    angles = 0
    for record in records:
        count = record.get('angle_count')
        if (isinstance(count,bool) or not isinstance(count,int) or count < 1
                or not isinstance(record.get('path'),str)
                or not isinstance(record.get('bytes'),int) or record['bytes'] <= 0
                or set(record.get('arrays_sha256',{})) != {'phi','core','cap','delta'}):
            raise ValueError('The actual frozen-reference batch record is incomplete')
        for word in [record.get('angle_list_sha256'),record.get('sha256'),*record['arrays_sha256'].values()]:
            if not isinstance(word,str) or len(word) != 64 or any(c not in '0123456789abcdef' for c in word):
                raise ValueError('Keep complete actual calibration array/file identities')
        numbers = record.get('maximum_defect_norms')
        if not isinstance(numbers,list) or len(numbers) != 3 or any(
                isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v < 0 for v in numbers):
            raise ValueError('The complete fixed-reference defect has all three angular readouts')
        angles += count
    maxima = actual.get('maximum_fixed_reference_defect_norms')
    if maxima != [max((r['maximum_defect_norms'][j] for r in records),default=None) for j in range(3)]:
        raise ValueError('The reported calibration maxima must match their actual completed batch records')
    if (value.get('working_radial_Gram_error_identically_zero') is not False
            or value.get('complete_current_raw_defect_lift_in_physical_sixjets') is not True
            or value.get('endpoint_residual_scope') != 'centred equation; raw quadrature closure defect is reported separately'):
        raise ValueError('The actual operator must distinguish the raw physical lift from centred roots')
    return dict(source_sha256=roles['reference_calibration'],
        definition_identity_sha256=canonical(definition),
        original_reference_point_sha256=definition['original_reference_point_sha256'],
        completed_fixed_reference_angle_batches=len(records),
        recorded_angle_occurrences_across_batches=angles,
        reference_batch_records_sha256=canonical(records),
        fixed_defect_value_max=maxima[0],fixed_defect_phi_max=maxima[1],fixed_defect_phiphi_max=maxima[2],
        current=current,physical_sixjet_raw_lift_complete=True,
        working_radial_identity=False,raw_reference_files_recomputed=False,
        continuous_reference_root_quadrature_or_geometry_certified=False)


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
    calibration_snapshot(value['current_reference_calibration'],value['current_full_point_sha256'])
    result = {key:value[key] for key in ROOT_SNAPSHOT_KEYS}
    result.update(actual_snapshot_schema=value['schema'],
        all_grid_roots_available_is_a_numerical_cache_statement_only=True,
        missing_point_values_replaced_from_latest_metadata=False,
        final_endpoint_only_equation_determines_six_control_derivative=False,
        first_and_second_angular_endpoint_residuals_are_physical_length_units=True,
        those_endpoint_residuals_are_the_centred_equation=True,
        raw_quadrature_closure_is_separately_in_the_complete_physical_lift=True)
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
            calibration_snapshot(value['current_reference_calibration'],value['current_full_point_sha256'],
                model['reference_centering_definition'])
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
            or value.get('schema') != 'fixed-fejer-paired-halfwave-reference-literal-zero-endpoint-Q-input-v1'
            or value.get('definition', {}).get('schema')
                != 'fixed-fejer-paired-halfwave-reference-literal-two-bubble-endpoint-Q-v1'
            or model.get('new_reference_input_binding_source_sha256') != roles['new_moment_input']
            or report['frozen_moment_Q_input_record'].get('same_mathematical_g_claimed') is not False
            or report['frozen_moment_Q_input_record'].get('current_moment_inverse_property_claimed') is not False
            or report['frozen_moment_Q_input_record'].get('no_moment_or_inverse_recomputed') is not True
            or report['frozen_moment_Q_input_record'].get('old_reference_or_initial_point_binding_inherited') is not False):
        raise ValueError('This complete supported-reference field uses its new twelve-key pure binder only')
    path = topic/'scripts/resume_20261126/fixed_fejer_paired_halfwave_literal_zero_moment_input.py'
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
    if (base.get('schema') != 'complete-fixed-fejer-paired-halfwave-so3-meridian-with-core-lift-v1'
            or seed.get('schema') != 'complete-fixed-fejer-paired-halfwave-meridian-seed-reference-v1'
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
        if (plan.get('schema') != 'complete-paired-halfwave-seed-radial-plan-v1'
                or plan.get('source_sha256') != roles['seed_reference']
                or plan.get('paired_halfwave_definition') != seed['paired_halfwave_definition']
                or plan.get('every_physical_halfwave_breakpoint_in_complete_partition') is not True
                or plan.get('complete_physical_pair_piece_count') != 12
                or plan.get('auxiliary_mean_rule_piece_count') != 12
                or plan.get('physical_sine_cancellation_scope') != 'both equal complete central intervals together'
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

def endpoint_metadata(value, model, source_by_role, working_evaluation, supported, frame_binding):
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
    calibrated = calibration_metadata(value,model,source_by_role)
    seed_actual = supported_seed_metadata(value, model, source_by_role, supported)
    names = ('all_attempted_fields_maximum_successful_endpoint_residual',
        'all_attempted_fields_maximum_successful_dimensionless_control_norm',
        'all_attempted_fields_maximum_core_inverse_residual',
        'all_attempted_fields_minimum_core_inverse_sample_rho')
    return dict(current=current,all_attempted={key:value[key] for key in names},
        fixed_supported_unit_seed=seed_actual,reference_calibration=calibrated,
        normal_frame_C1_reuse=frame_reuse_metadata(value,model,source_by_role,frame_binding),
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


def geometric(value, *, envelope_check):
    if value is None:
        return None
    complete = value.get('complete') is True
    scope = value.get('material_envelope')
    checked_scope = envelope_check(scope)
    if complete and (not isinstance(scope,dict) or scope.get('complete') is not True
            or scope.get('current_full_point_sha256') != value.get('current_full_point_sha256')):
        raise ValueError('A complete current scan needs its own complete material-envelope read')
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
    result['material_envelope'] = checked_scope
    result['missing_angle_batches'] = envelope_check.full_geometry_check(value)
    return result


def direction(value, profile, *, envelope_check, envelope_row_check):
    phase = value['phase']
    if phase not in ('metric', 'restoration'):
        raise ValueError('The complete report used an undeclared scientific phase')
    rows = value['complete_selected_inequalities']
    checked_rows = envelope_row_check(rows,value.get('starting_geometry'))
    if (rows.get('no_original_row_removed') is not True
            or rows['original_prefix_rows']+rows['appended_amplitude_rows']+rows['appended_envelope_rows'] != rows['selected_rows']
            or rows.get('known_geometry_and_amplitude_prefix_rows') != rows['original_prefix_rows']+rows['appended_amplitude_rows']
            or rows.get('envelope_rows_start_index') != rows['known_geometry_and_amplitude_prefix_rows']
            or rows.get('known_prefix_rewritten') is not False
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
        material_envelope_rows=checked_rows,
        original_geometry_rows=rows['original_prefix_rows'],
        amplitude_rows=rows['appended_amplitude_rows'], envelope_rows=rows['appended_envelope_rows'],
        known_geometry_and_amplitude_prefix_rows=rows['known_geometry_and_amplitude_prefix_rows'],
        known_prefix_bytes=rows['known_prefix_bytes'],known_prefix_rewritten=False,
        total_rows=rows['selected_rows'],
        row_cache_bytes=rows['row_cache_bytes'],
        duplicate_prefix_cache_bytes=rows.get('duplicate_prefix_cache_bytes'),
        actual_QP_seconds=value.get('actual_QP_seconds'),
        actual_complete_direction_seconds=value['seconds'],
        actual_QP_operator_counts=value.get('actual_QP_operator_counts'),
        actual_complete_direction_operator_counts=value.get('actual_complete_direction_operator_counts'),
        starting_statistics=statistic(value['starting_statistics'],profile),
        starting_geometry=geometric(value['starting_geometry'], envelope_check=envelope_check),
        accepted_statistics=statistic(value.get('accepted_statistics'),profile),
        accepted_geometry=geometric(value.get('accepted_geometry'), envelope_check=envelope_check),
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
                or not geometric(trial.get('full_geometry'), envelope_check=envelope_check)['true_finite_geometry_feasible']):
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
            full_geometry=geometric(trial.get('full_geometry'), envelope_check=envelope_check),
            endpoint_roots=endpoint_roots(trial.get('endpoint_roots')),
            actual_seconds=trial.get('actual_seconds'), actual_read_error=trial.get('actual_read_error')))
    result['trials'] = trials
    return result





def extra_bindings(report,topic,driver,envelope_binding):
    answer={}
    for role,function in (('analytic_J3_binding','read_actual'),('root_packets','validate_entry_report'),
                          ('batched_geometry_binding','bind_report')):
        relative,expected=load_pins(driver)[role];path=topic/relative
        if sha(path)!=expected:raise ValueError('Changed complete entry helper: '+role)
        spec=importlib.util.spec_from_file_location('_entry_pure_'+expected,path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        fn=getattr(module,function)
        if role=='analytic_J3_binding':
            chart=module.independent_chart_binding
            if sha(chart.__code__.co_filename)!=expected:raise ValueError('Changed complete chart binding')
            answer['independent_fixed_target']=chart(report,envelope_binding)
        if sha(fn.__code__.co_filename)!=expected:raise ValueError('Changed actual pure entry function')
        if role=='batched_geometry_binding':
            answer[role],answer['full_geometry_check']=fn(report,
                source_by_role=report['source_sha256_by_role'],
                geometry_source=topic/load_pins(driver)['geometry'][0])
            continue
        answer[role]=(fn(report,roles=report['source_sha256_by_role'],source_directory=path.parent)
            if role=='analytic_J3_binding' else fn(report,reread_packets=True,reread_arrays=True))
    return answer


def mathematical_progress_binding(report,topic,driver):
    relative,expected=load_pins(driver)['scalar_progress']
    path=topic/relative
    if sha(path)!=expected or report.get('mathematical_progress_source',{}).get('sha256')!=expected:
        raise ValueError('Keep the whole explicitly declared standard-library scalar observer')
    name='_pure_fixed_fejer_mathematical_progress_'+expected[:16]
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module.validate_report_progress(report,source_sha256=expected,driver_sha256=DRIVER_SHA)


def read_report(repo, report_path, *, verify_final_bundle=False):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    driver = topic/'scripts/resume_20261126/fullclosed_fixed_fejer_halfwave_dk_cache_qp.py'
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
    frame_binding = frame_reuse_binding(report,model,roles,topic/load_pins(driver)['frame_C1'][0])
    matrix_binding,matrix_read = detached_matrix_binding(report,model,roles,topic/load_pins(driver)['stage_matrices'][0])
    adjacent_binding,adjacent_read = adjacent_frame_binding(report,model,roles,topic/load_pins(driver)['adjacent_matrices'][0])
    envelope_binding,envelope_check,envelope_row_check = material_envelope_binding(topic,report,roles,driver)
    transfer_binding,prior_final_seed = transferred_envelope_binding(topic,report,model,roles,driver)
    extra=extra_bindings(report,topic,driver,envelope_binding)
    envelope_check.full_geometry_check=extra['full_geometry_check']
    independent_target=extra['independent_fixed_target']
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
            or model.get('radial_Gram_error_identically_zero') is not False
            or model.get('accurate_zero_root_radial_Gram_error_identically_zero') is not True
            or model.get('mathematical_field_definition_requires_exact_implicit_root') is not True
            or model.get('implicit_root_is_not_a_new_independent_free_field') is not True
            or model.get('all_current_free_core_coefficients_retained') is not True
            or model.get('all_original_rotation_variables_retained') is not True
            or model.get('current_height_free') is not True
            or report.get('radial_metric_error_identically_zero') is not False
            or report.get('accurate_zero_root_radial_metric_identity') is not True
            or report.get('radial_Gram_uses_complete_hprime_Delta') is not True
            or report.get('numerical_radial_Gram_row_retained') is not True
            or report.get('endpoint_implicit_J_separate_from_Newton') is not True):
        raise ValueError('Keep the exact fixed target and full WORKING physical lift in every numerical Gram row')
    centered_binding = centering_binding(report,model,roles)
    frozen_input, moment_identity = bind_literal_input(topic,report,model,roles,profile)
    supported = supported_seed_binding(report,model,roles,frozen_input,profile)
    if (model.get('schema') != OPERATOR_SCHEMA
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
    if report.get('final_reference_centred_closure_is_separately_checked') is not True:
        raise ValueError('A normalized stage residual cannot replace the final complete centred closure tolerance')
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
    metrics = [direction(value,profile, envelope_check=envelope_check, envelope_row_check=envelope_row_check) for value in report.get('metric_directions', [])]
    restoration = [direction(value,profile, envelope_check=envelope_check, envelope_row_check=envelope_row_check) for value in report.get('restoration_directions', [])]
    final_geometry = geometric(report.get('final_geometry'), envelope_check=envelope_check)
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
    endpoint = endpoint_metadata(metadata, model, roles, working, supported, frame_binding)
    failed_initial = report.get('actual_initial_read_error') is not None
    if failed_initial and (report.get('complete') is True
            or report.get('initial_failed_candidate_is_not_an_accepted_field') is not True
            or metrics or restoration or report.get('final_bundle_sha256') is not None):
        raise ValueError('An initial endpoint/field-read failure is not a completed or accepted candidate')
    if report.get('complete') is True and endpoint is None:
        raise ValueError('A complete zero-closure budget needs its actual endpoint diagnostics')
    return dict(schema='actual-fixed-fejer-halfwave-dk-cache-observed-SO3-readout-v1',
        mathematical_observation=mathematical_progress_binding(report,topic,driver),
        reader_sha256=sha(__file__), report_path=str(Path(report_path).resolve()),
        report_sha256=sha(report_path), report_bytes=Path(report_path).stat().st_size,
        actual_driver_sha256=DRIVER_SHA, actual_source_commit=report['source_commit'],
        workflow_trigger_commit=report.get('workflow_trigger_commit'),
        github_run_id=report.get('github_run_id'), complete=report.get('complete') is True,
        initial_reference_bundle_sha256=report['bundle_sha256'],
        model_identity_sha256=report['model_identity_sha256'],
        reference_centering=centered_binding,analytic_stage_jacobian=extra['analytic_J3_binding'],
        analytic_normal_frame=extra['analytic_J3_binding']['analytic_normal_frame'],
        detached_closure_value_reuse=extra['analytic_J3_binding']['detached_closure_value_reuse'],
        detached_meridian_value_reuse=extra['analytic_J3_binding']['detached_meridian_value_reuse'],
        mutable_evaluation_progress_not_used_as_scientific_input=True,
        normal_root_packets=extra['root_packets'],
        normal_frame_C1_binding=frame_binding,
        detached_stage_matrix_binding=matrix_binding,
        detached_stage_matrix_diagnostics=matrix_read(metadata),
        adjacent_normal_frame_matrix_binding=adjacent_binding,
        adjacent_normal_frame_matrix_diagnostics=adjacent_read(metadata),
        material_envelope_binding=envelope_binding,
        batched_geometry_binding=extra['batched_geometry_binding'],
        independent_fixed_target_binding=independent_target,
        actual_fixed_reference_input_binding=independent_target['actual_fixed_recipe_input_binding'],
        predeclared_mathematical_target_identity_sha256=independent_target['mathematical_target_identity_sha256'],
        predeclared_new_fixed_fejer_target=True,
        historical_literal_requests_reinterpreted_not_same_physical_points=True,
        previous_target_completion_or_unknown_typed_history_reconstructed=False,
        material_envelope_transfer=transfer_binding,
        prior_envelope_final_variable_seed=prior_final_seed,
        initial_full_variable_point_sha256=report['initial_full_variable_point_sha256'],
        material_envelope_diagnostics=envelope_binding['actual_metadata'],
        normal_frame_C1_diagnostics=None if endpoint is None else endpoint['normal_frame_C1_reuse'],
        reference_calibration_diagnostics=None if endpoint is None else endpoint['reference_calibration'],
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
        initial_geometry=geometric(report.get('initial_geometry'), envelope_check=envelope_check), final_geometry=final_geometry,
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
        radial_Gram_uses_complete_hprime_Delta=True,
        working_radial_metric_error_identically_zero=False,
        exact_radial_identity_requires_exact_reference_and_final_implicit_roots=True,
        raw_quadrature_defect_is_not_the_centred_root_residual=True,
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
