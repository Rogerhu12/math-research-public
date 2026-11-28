#!/usr/bin/env python3
"""Complete same-invocation detached J3/J6/J9 normal-stage matrix reuse.

Only the returned-value J3 after an ORIGINAL successful stage root and the
complete detached J6/J9 loop are served.  The ORIGINAL _solve_stage and its
Newton matrices remain untouched.  Every stage still evaluates its own
equations, domain, angular solves and final endpoint residual.  The active
implicit chain retains its complete residual graph and every upstream edge.

The first value is obtained from the entire original Jacobian method.  A
later request may clone that value only at the same complete batch/data,
point, layout and binary64 previous/frame/increment words.  Tau is checked
against the current fixed stage but is absent from the equality key: the
bound original constraint subtracts (1-tau)*zero independently of eta.

This is a new, explicitly declared working numerical policy.  It makes no
claim that an unexecuted fresh selected-matrix evaluation would produce the same bits,
that a matrix is nonsingular, or that a scientific field has succeeded.
All scientific operations require the public repository Actions runner.

This independent revision replaces only repeated full-point copies inside a
matrix scope by a strict immutable-bytes-owner binding.  Scope entry retains
both the original full-word read and canonical array SHA check.  Scope exit
rereads every point word.  All per-stage model/data/control/carrier guards
and all original scientific matrix methods remain in force.
"""
import ast
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
import torch


SCHEMA = 'complete-immutable-point-bound-same-call-detached-normal-stage-matrix-reuse-v1'
ANALYTIC_STAGE_SOURCE_SHA256 = '617550e0df01b853a3239b20833076671334f840c0b48c3b64b3f0503b82a247'
TORCH_VERSION = '2.5.1'
FRAME_C1_SOURCE_SHA256 = 'edbf2018efbe09f14902a4e1833db736f3467317f87cb6ebae2561ab31a0056b'
ORIGINAL_C1_OPERATOR_SOURCE_SHA256 = 'a62c24570eef2ef253c0960c387bac8d68452ef4a277e41ae77ec8adc6faebfd'
BASE_SOURCE_SHA256 = 'b1df4f8f0b0d777337bbc8d7a6893fb44001edb5601439e027b7153fef2935a6'
PHASES = ('returned_value_J3', 'complete_angular_J6_J9')
NORMAL_COUNTER_KEYS = ('stage_equation_angle_evaluations',
    'closure_jet_angle_evaluations', 'stage_matrix_angle_evaluations',
    'stage_angular_matrix_angle_evaluations', 'actual_implicit_matrix_angle_rows')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific detached stage matrices require public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),
        allow_nan=False).encode()).hexdigest()


def definition():
    return dict(schema=SCHEMA,source_sha256=sha(__file__),
        original_complete_C1_operator_source_sha256=ORIGINAL_C1_OPERATOR_SOURCE_SHA256,
        complete_frame_C1_source_sha256=FRAME_C1_SOURCE_SHA256,
        complete_base_source_sha256=BASE_SOURCE_SHA256,
        complete_analytic_stage_source_sha256=ANALYTIC_STAGE_SOURCE_SHA256,
        local_scalar_matrix_policy='actual selected analytic working Rodrigues J3, with explicit complete AD fallback',
        phases=list(PHASES),
        original_complete_stage_matrix_source_sha256='7aabf3ef5857dbdbbf9832b8bb4ca378faa7e06514a21b48f83649d6df7cb0d7',
        point_guard_policy='whole words and canonical array SHA at entry; same hard immutable bytes owner at every stage; whole words again at exit',
        point_owner='plain native-float64 non-owning readonly contiguous one-dimensional ndarray directly backed by full immutable bytes',
        point_array_shape_stride_owner_length_and_selected_object_rechecked_each_stage=True,
        selected_point_object_identity_and_point_SHA_rechecked_each_stage=True,
        entry_and_exit_complete_point_words_retained=True,
        per_stage_full_point_word_copy_performed=False,
        point_owner_checks_and_whole_word_reads_counted_separately=True,
        point_guard_costs_are_closed_scope_totals=True,
        scope_exit_binding_failure_is_not_a_successful_scope=True,
        original_all_other_stage_guards_unchanged=True,
        scope='one original returned-value root chain OR one detached full angular-matrix loop',
        matrix_source='first complete selected _stage_jacobian or original _stage_jet_jacobian evaluation',
        key='whole ordered batch; full previous/frame/increment binary64 words and layouts; kind/order',
        current_point_data_object_versions_and_integral_carriers_bound=True,
        complete_three_angular_control_and_frame_jets_in_every_key=True,
        full_increment_jets_in_angular_key=True,
        signed_zero_words_distinguished=True,
        near_equal_words_accepted=False,
        matrices_shared_between_calls_or_points_or_batches=False,
        matrices_shared_between_orders_or_kinds=False,
        active_input_graphs_accepted=False,
        matrix_value_detached=True,
        tau_omitted_only_from_eta_partial_equivalence_key=True,
        each_tau_checked_against_the_actual_fixed_partition=True,
        complete_original_zero_target_bound=True,
        original_Newton_matrix_evaluations_unchanged=True,
        original_stage_equations_domain_solves_and_trace_retained=True,
        original_active_residual_and_full_upstream_parameter_chain_retained=True,
        original_nine_frame_helper_method_guards_unchanged=False,
        complete_current_frame_wrapper_guard_and_eight_original_method_guards_retained=True,
        first_matrix_not_reassembled_or_cropped_from_another_kind=True,
        optional_cache_key_copy_or_storage_failure_uses_original_formula=True,
        original_counters_count_only_actual_original_method_calls=True,
        logical_requests_and_reuses_counted_separately=True,
        fresh_unexecuted_AD_words_claimed_equal=False,
        speedup_or_hit_rate_claimed=False,
        quadrature_rounding_root_or_geometry_error_enclosed=False)


def _new_counts():
    return dict(logical_matrix_requests=0,logical_scalar_requests=0,
        logical_angular_requests=0,logical_angle_blocks=0,logical_angle_rows=0,
        completed_matrix_requests=0,original_matrix_attempts=0,
        original_matrix_returns=0,original_matrix_failures=0,
        original_scalar_attempts=0,original_angular_attempts=0,
        cache_hits=0,cache_scalar_hits=0,cache_angular_hits=0,
        cache_key_failures=0,cache_value_digest_failures=0,cache_copy_or_store_failures=0,
        bypassed_after_optional_failure=0,saved_matrices=0,
        peak_cached_matrix_bytes=0,
        actual_stage_equation_angle_evaluations=0,
        actual_closure_jet_angle_evaluations=0,
        actual_stage_matrix_angle_evaluations=0,
        actual_stage_angular_matrix_angle_evaluations=0,
        actual_implicit_matrix_angle_rows=0,
        actual_implicit_jacobian_blocks=0,
        point_owner_entry_checks=0,point_owner_entry_failures=0,
        point_owner_stage_checks=0,point_owner_stage_failures=0,
        point_owner_exit_checks=0,point_owner_exit_failures=0,
        whole_point_entry_reads=0,whole_point_entry_read_failures=0,
        whole_point_exit_reads=0,whole_point_exit_read_failures=0,
        whole_point_entry_array_sha_checks=0,whole_point_entry_array_sha_failures=0)


def _plain_copy(value):
    return json.loads(json.dumps(value,allow_nan=False))


def _valid_digest(value):
    return (isinstance(value,str) and len(value) == 64
        and all(character in '0123456789abcdef' for character in value))


def _finite_nonnegative(value):
    return (not isinstance(value,bool) and isinstance(value,(int,float))
        and math.isfinite(value) and value >= 0)


def _validated_counts(value):
    if (not isinstance(value,dict) or set(value) != set(_new_counts())
            or any(type(item) is not int or item < 0 for item in value.values())):
        raise ValueError('Keep all actual matrix-cache counters; missing values are not zero')
    if (value['logical_matrix_requests'] != value['logical_scalar_requests']+value['logical_angular_requests']
            or value['cache_hits'] != value['cache_scalar_hits']+value['cache_angular_hits']
            or value['original_matrix_attempts'] != value['original_scalar_attempts']+value['original_angular_attempts']
            or value['original_matrix_attempts'] != value['original_matrix_returns']+value['original_matrix_failures']
            or value['completed_matrix_requests'] > value['original_matrix_returns']+value['cache_hits']
            or value['original_matrix_attempts']+value['cache_hits'] > value['logical_matrix_requests']
            or value['saved_matrices'] > value['original_matrix_returns']):
        raise ValueError('Logical requests, actual original calls and returned cache values must stay distinct')
    for phase in ('entry','stage','exit'):
        if value['point_owner_'+phase+'_failures'] > value['point_owner_'+phase+'_checks']:
            raise ValueError('Immutable point binding failures exceed actual attempts')
    for phase in ('entry','exit'):
        if value['whole_point_'+phase+'_read_failures'] > value['whole_point_'+phase+'_reads']:
            raise ValueError('Complete point read failures exceed actual attempts')
    if (value['whole_point_entry_array_sha_failures'] > value['whole_point_entry_array_sha_checks']
            or value['point_owner_stage_checks'] < value['logical_matrix_requests']):
        raise ValueError('Every actual matrix request retains its own immutable point check')
    return dict(value)


def validate_metadata(value, *, model, source_by_role, current_full_point_sha256):
    """Pure stdlib attribution; the reader extracts this exact source-bound body.

    No field, array, root, matrix, NumPy or Torch operation is used here.
    A last scope retains its OWN point.  A partial scope never establishes
    root/field completion, and absent actual counters are never backfilled.
    """
    expected = definition()
    model_identity = canonical(model)
    if (not isinstance(value,dict) or value.get('schema') != SCHEMA
            or value.get('source_sha256') != source_by_role['stage_matrices']
            or expected['source_sha256'] != source_by_role['stage_matrices']
            or value.get('definition') != expected
            or model.get('detached_stage_matrix_reuse') != expected
            or value.get('actual_operator_source_sha256') != source_by_role['endpoint']
            or value.get('actual_calibration_source_sha256') != source_by_role['reference_calibration']
            or value.get('actual_model_identity_sha256') != model_identity):
        raise ValueError('The detached matrix metadata belongs to another complete source or field')
    total = _validated_counts(value.get('actual_counts'))
    for key in ('scopes_started','scopes_closed'):
        if type(value.get(key)) is not int or value[key] < 0:
            raise ValueError('Keep the actual nonnegative scope counters')
    if value['scopes_closed'] > value['scopes_started']:
        raise ValueError('More matrix scopes cannot close than have started')
    for key in ('scope_seconds','original_method_seconds','point_owner_binding_seconds',
            'complete_point_word_read_seconds','complete_point_array_sha_seconds'):
        if not _finite_nonnegative(value.get(key)):
            raise ValueError('Keep actual finite matrix-scope timing with its stated scope')
    for key in ('matrices_or_input_graphs_stored_in_kernel',
            'normal_Newton_matrices_served_by_this_cache',
            'original_equations_and_stage_solves_executed_by_this_cache',
            'matrix_singularity_or_field_success_inferred',
            'measured_acceleration_or_repeat_rate_claimed','arithmetic_errors_enclosed'):
        if value.get(key) is not False:
            raise ValueError('An unsupported cache/field/performance claim was recorded: '+key)
    if (value.get('original_equations_and_stage_solves_still_required_in_caller') is not True
            or value.get('scope_seconds_include_owning_stage_chain') is not True):
        raise ValueError('The original whole stage chain and timing scope remain explicit')
    closed = value['scopes_closed']
    if (any(total[key] != closed for key in ('point_owner_entry_checks',
                'whole_point_entry_reads','whole_point_entry_array_sha_checks',
                'point_owner_exit_checks','whole_point_exit_reads'))
            or any(total[key] != 0 for key in ('point_owner_entry_failures',
                'whole_point_entry_read_failures','whole_point_entry_array_sha_failures'))
            or value.get('point_guard_costs_count_only_closed_scopes') is not True
            or value.get('per_stage_complete_point_word_copy_performed') is not False):
        raise ValueError('Closed scopes retain full entry/exit reads without inventing per-stage word reads')
    last = value.get('last_scope')
    summary = None
    if last is not None:
        if not isinstance(last,dict) or not isinstance(last.get('binding'),dict):
            raise ValueError('Retain the actual complete last scope or null')
        binding = last['binding']
        count = binding.get('literal_angle_count')
        order = binding.get('angular_order')
        stages = model.get('normal_stage_count')
        if (type(count) is not int or count < 1 or order not in (1,2)
                or type(stages) is not int or stages < 1
                or binding.get('phase') not in PHASES
                or type(binding.get('scope_serial')) is not int
                or not 1 <= binding['scope_serial'] <= value['scopes_started']
                or binding.get('actual_operator_source_sha256') != source_by_role['endpoint']
                or binding.get('actual_calibration_source_sha256') != source_by_role['reference_calibration']
                or binding.get('actual_model_identity_sha256') != model_identity
                or binding.get('normal_stage_count') != stages
                or binding.get('exact_normal_step_nodes') != model['exact_normal_step_nodes']
                or binding.get('actual_normal_step_carriers_binary64_hex')
                    != model['actual_normal_step_carriers_binary64_hex']
                or binding.get('complete_previous_shape') != [count,3,6]
                or binding.get('complete_frame_shape') != [count,3,3,6]
                or binding.get('detached_data_objects_versions_and_layouts_bound') is not True
                or binding.get('all_tau_values_still_used_by_the_original_stage_equations') is not True
                or binding.get('active_parameter_graph_accepted') is not False):
            raise ValueError('The complete own-batch matrix binding and unchanged stage partition differ')
        point_words = binding.get('complete_free_point_word_count')
        expected_words = (model['M']-len(model['fixed_core_first3'])
            +(3*model['J']-3)*(3*model['M']+2)+1)
        if (type(point_words) is not int or point_words != expected_words
                or binding.get('complete_free_point_shape') != [point_words]
                or binding.get('complete_free_point_stride_bytes') != [8]
                or binding.get('immutable_point_owner_bytes') != 8*point_words
                or binding.get('point_dtype') != 'float64'
                or binding.get('point_owner_kind') != 'immutable built-in bytes'
                or binding.get('point_array_is_plain_native_contiguous_readonly_nonowning') is not True
                or binding.get('entry_canonical_array_sha_checked') is not True
                or binding.get('per_stage_complete_point_word_copy_performed') is not False):
            raise ValueError('Keep the entire immutable point layout and original entry SHA check')
        keys = binding.get('literal_phi_hex')
        if (not isinstance(keys,list) or len(keys) != count
                or any(not isinstance(key,str) or not math.isfinite(float.fromhex(key))
                    or float.fromhex(key).hex() != key for key in keys)
                or binding.get('literal_phi_words_sha256') != canonical(keys)):
            raise ValueError('Keep the complete ordered literal angle batch')
        for key in ('actual_full_free_point_sha256','complete_free_point_words_sha256',
                'mesh_words_sha256','gauss_weight_words_sha256'):
            if not _valid_digest(binding.get(key)):
                raise ValueError('Keep every complete point/carrier byte identity: '+key)
        if (type(binding.get('J')) is not int or binding['J'] != model['J']
                or type(binding.get('integration_order')) is not int or binding['integration_order'] < 1
                or not isinstance(binding.get('current_S_hex'),str)
                or not math.isfinite(float.fromhex(binding['current_S_hex']))
                or float.fromhex(binding['current_S_hex']) <= 0
                or float.fromhex(binding['current_S_hex']).hex() != binding['current_S_hex']):
            raise ValueError('Keep the actual complete positive integral carrier')
        current = _validated_counts(last.get('actual_counts'))
        if any(item > total[key] for key,item in current.items()):
            raise ValueError('A last scope cannot exceed the cumulative actual costs')
        if (any(current[key] != 1 for key in ('point_owner_entry_checks',
                    'whole_point_entry_reads','whole_point_entry_array_sha_checks',
                    'point_owner_exit_checks','whole_point_exit_reads'))
                or any(current[key] != 0 for key in ('point_owner_entry_failures',
                    'whole_point_entry_read_failures','whole_point_entry_array_sha_failures'))):
            raise ValueError('Every closed scope must retain its actual complete entry and exit checks')
        exit_check = last.get('point_scope_exit_check')
        if (not isinstance(exit_check,dict) or exit_check.get('attempted') is not True
                or type(exit_check.get('immutable_binding_valid')) is not bool
                or exit_check.get('immutable_binding_valid') is not (current['point_owner_exit_failures'] == 0)
                or exit_check.get('complete_point_words_equal') not in (True,False,None)
                or not isinstance(exit_check.get('failures'),list)
                or any(not isinstance(item,dict) or not isinstance(item.get('operation'),str)
                    or not isinstance(item.get('exception_type'),str) or not isinstance(item.get('reason'),str)
                    for item in exit_check['failures'])
                or (current['whole_point_exit_read_failures'] != 0
                    and exit_check['complete_point_words_equal'] is not None)
                or (current['whole_point_exit_read_failures'] == 0
                    and type(exit_check['complete_point_words_equal']) is not bool)):
            raise ValueError('An exit guard must retain its actual failed or successful own-point evidence')
        point_complete = (exit_check['immutable_binding_valid'] is True
            and exit_check['complete_point_words_equal'] is True
            and not exit_check['failures'] and current['point_owner_stage_failures']==0)
        if (last.get('scope_point_binding_complete') is not point_complete
                or (not point_complete and not exit_check['failures']
                    and current['point_owner_stage_failures']==0)):
            raise ValueError('A failed scope-exit binding is never reported as a complete point binding')
        attempted = last.get('stage_requests_attempted')
        records = last.get('matrix_request_records')
        if (type(attempted) is not int or not 0 <= attempted <= stages
                or attempted != current['logical_matrix_requests']
                or not isinstance(records,list) or len(records) != attempted
                or last.get('all_declared_stage_matrix_requests_completed') is not (
                    attempted == stages and current['completed_matrix_requests'] == stages)
                or last.get('scientific_field_success_inferred') is not False
                or last.get('active_parameter_graph_borrowed') is not False
                or last.get('original_Newton_matrices_unchanged') is not True
                or last.get('original_phase_source') != binding['phase']):
            raise ValueError('Keep the actual partial/full matrix sequence without inferring scientific completion')
        if attempted and not _valid_digest(binding.get('zero_target_words_sha256')):
            raise ValueError('Every actual request must bind the original complete zero target')
        for key in ('scope_seconds','original_method_seconds','point_owner_binding_seconds',
            'complete_point_word_read_seconds','complete_point_array_sha_seconds'):
            if not _finite_nonnegative(last.get(key)):
                raise ValueError('Keep actual own-scope timing')
        completed = originals = failures = hits = 0
        deltas = {name:0 for name in NORMAL_COUNTER_KEYS}
        block_delta = 0
        expected_kind = 'scalar' if binding['phase'] == PHASES[0] else 'angular'
        size = 3 if expected_kind == 'scalar' else 3*(order+1)
        for index,record in enumerate(records):
            if (not isinstance(record,dict) or record.get('request_index') != index
                    or record.get('normal_stage_index') != index+1
                    or record.get('exact_auxiliary_node') != model['exact_normal_step_nodes'][index+1]
                    or record.get('actual_auxiliary_node_hex') != model['actual_normal_step_carriers_binary64_hex'][index+1]
                    or record.get('kind') != expected_kind or record.get('angular_order') != order
                    or record.get('matrix_shape') != [count,size,size]
                    or type(record.get('completed')) is not bool
                    or type(record.get('original_method_executed')) is not bool
                    or record.get('own_stage_equation_or_root_success_inferred') is not False):
                raise ValueError('A logical matrix request changed point/order/stage or inferred a root')
            key_digest = record.get('complete_input_key_sha256')
            if key_digest is not None and not _valid_digest(key_digest):
                raise ValueError('Keep the full equality-key digest or an explicit optional allocation failure')
            originals += int(record['original_method_executed'])
            completed += int(record['completed'])
            failures += int('original_matrix_failure' in record)
            if record['original_method_executed'] or record.get('reused_previous_original_matrix_value') is True:
                current_deltas = record.get('actual_normal_counter_delta')
                block = record.get('actual_implicit_jacobian_blocks_delta')
                if (not isinstance(current_deltas,dict) or set(current_deltas) != set(NORMAL_COUNTER_KEYS)
                        or any(type(v) is not int or v < 0 for v in current_deltas.values())
                        or type(block) is not int or block < 0):
                    raise ValueError('Actual original-counter increments cannot be filled from logical requests')
                for name,item in current_deltas.items():
                    deltas[name] += item
                block_delta += block
            if not record['completed']:
                continue
            origin = record.get('numerical_value_origin')
            if (not isinstance(origin,dict) or origin.get('scope_serial') != binding['scope_serial']
                    or origin.get('complete_input_key_sha256') != key_digest
                    or type(origin.get('request_index')) is not int
                    or not 0 <= origin['request_index'] <= index
                    or origin.get('normal_stage_index') != origin['request_index']+1):
                raise ValueError('Keep the actual same-scope origin of every returned complete matrix')
            digest = origin.get('actual_matrix_words_sha256')
            if digest is not None and not _valid_digest(digest):
                raise ValueError('Keep the complete matrix-value identity or its recorded optional digest failure')
            if record.get('reused_previous_original_matrix_value') is True:
                source = records[origin['request_index']]
                if (record['original_method_executed'] or origin['request_index'] >= index
                        or source.get('completed') is not True
                        or source.get('original_method_executed') is not True
                        or source.get('reused_previous_original_matrix_value') is not False
                        or source.get('complete_input_key_sha256') != key_digest
                        or source.get('numerical_value_origin') != origin
                        or not _valid_digest(digest)
                        or record.get('unexecuted_fresh_AD_words_claimed_equal') is not False
                        or any(record['actual_normal_counter_delta'].values())
                        or record['actual_implicit_jacobian_blocks_delta'] != 0):
                    raise ValueError('A cache hit must name its same-input original return, not a fresh AD or another stage root')
                hits += 1
            elif (record.get('reused_previous_original_matrix_value') is not False
                    or not record['original_method_executed'] or origin['request_index'] != index):
                raise ValueError('A new matrix return must come from this actual complete original evaluation')
        if (completed != current['completed_matrix_requests']
                or originals != current['original_matrix_attempts']
                or failures != current['original_matrix_failures']
                or hits != current['cache_hits']
                or current['logical_angle_blocks'] != attempted*count
                or current['logical_angle_rows'] != attempted*count*size
                or any(current[key if key.startswith('actual_') else 'actual_'+key] != val for key,val in deltas.items())
                or current['actual_implicit_jacobian_blocks'] != block_delta):
            raise ValueError('The complete last-scope records must account for actual and logical costs')
        summary = dict(binding=_plain_copy(binding),actual_counts=current,
            stage_requests_attempted=attempted,
            all_declared_stage_matrix_requests_completed=last['all_declared_stage_matrix_requests_completed'],
            scope_seconds=last['scope_seconds'],original_method_seconds=last['original_method_seconds'],
            point_owner_binding_seconds=last['point_owner_binding_seconds'],
            complete_point_word_read_seconds=last['complete_point_word_read_seconds'],
            complete_point_array_sha_seconds=last['complete_point_array_sha_seconds'],
            point_scope_exit_check=_plain_copy(exit_check),
            scope_point_binding_complete=point_complete,
            matrix_request_records=_plain_copy(records),
            optional_cache_failures=_plain_copy(last.get('optional_cache_failures')),
            point_is_current_metadata_point=binding['actual_full_free_point_sha256']==current_full_point_sha256,
            own_point_not_backfilled_from_current_metadata=True,scientific_field_success_inferred=False)
    elif value['scopes_closed'] != 0:
        raise ValueError('A completed scope cannot disappear from actual matrix provenance')
    return dict(source_sha256=source_by_role['stage_matrices'],definition=expected,
        actual_counts=total,scopes_started=value['scopes_started'],scopes_closed=value['scopes_closed'],
        scope_seconds=value['scope_seconds'],original_method_seconds=value['original_method_seconds'],
        point_owner_binding_seconds=value['point_owner_binding_seconds'],
        complete_point_word_read_seconds=value['complete_point_word_read_seconds'],
        complete_point_array_sha_seconds=value['complete_point_array_sha_seconds'],
        point_guard_costs_count_only_closed_scopes=True,
        per_stage_complete_point_word_copy_performed=False,
        last_scope=summary,all_original_stage_equations_and_active_residuals_retained=True,
        numerical_matrix_origin_is_distinct_from_current_stage_root=True,
        mathematical_rank_or_field_or_acceleration_certificate=False)


def _tensor_layout(value, shape):
    if (not isinstance(value,torch.Tensor) or value.layout != torch.strided
            or value.device.type != 'cpu' or value.dtype != torch.float64
            or tuple(value.shape) != tuple(shape)
            or value.requires_grad or value.grad_fn is not None):
        raise ValueError('Keep complete detached CPU float64 inputs with the exact declared shape')
    return (tuple(value.shape),str(value.dtype),str(value.device),str(value.layout),
        tuple(value.stride()),int(value.storage_offset()))


def _numpy_layout(value, shape):
    if (not isinstance(value,np.ndarray) or value.dtype != np.dtype('float64')
            or value.shape != tuple(shape) or not np.isfinite(value).all()):
        raise ValueError('Bind the entire actual binary64 integral carrier without conversion')
    return (id(value),tuple(value.shape),str(value.dtype),tuple(value.strides),
        bool(value.flags.c_contiguous),bool(value.flags.f_contiguous),value.tobytes(order='C'))


def _immutable_point_owner(value, shape, expected_owner=None):
    """Read only fixed-size array metadata; never copy or scan full point words."""
    if type(value) is not np.ndarray:
        raise ValueError('The selected complete point must be a plain ndarray')
    owner=value.base
    if (type(owner) is not bytes or value.dtype!=np.dtype('float64')
            or not value.dtype.isnative or value.shape!=shape
            or value.strides!=(np.dtype('float64').itemsize,)
            or value.ndim!=1 or not value.flags.c_contiguous
            or value.flags.writeable or value.flags.owndata
            or value.nbytes!=8*shape[0] or len(owner)!=value.nbytes
            or (expected_owner is not None and owner is not expected_owner)):
        raise ValueError('Bind the entire readonly point directly to its exact immutable bytes owner')
    # The exact-length contiguous array covers the whole bytes allocation;
    # a nonzero slice offset would require bytes beyond the bound owner.
    return owner


class CompleteDetachedStageMatrices:
    """Source-bound factory.  It retains scalar records, never a cached matrix."""
    def __init__(self, q, *, frame_c1_module):
        require_actions()
        if torch.__version__.split('+')[0] != TORCH_VERSION:
            raise ValueError('Use the declared CPU PyTorch version for this working policy')
        required_helpers = ('definition','_ast_value','_array_words','_tensor_identity',
            '_data_identity','_all_data_detached','NormalFrameC1Kernel')
        if (frame_c1_module is None or sha(frame_c1_module.__file__) != FRAME_C1_SOURCE_SHA256
                or any(not hasattr(frame_c1_module,name) for name in required_helpers)):
            raise ValueError('Bind the complete unchanged C1 helper, not a replacement identity utility')
        for name in required_helpers:
            value = getattr(frame_c1_module,name)
            function = value.__init__ if isinstance(value,type) else value
            if sha(function.__code__.co_filename) != FRAME_C1_SOURCE_SHA256:
                raise ValueError('C1 helper method source differs: '+name)
        self.q,self.frame_module = q,frame_c1_module
        self.definition = definition()
        if (q.model.get('detached_stage_matrix_reuse') != self.definition
                or canonical(q.model) != q.identity
                or q.model.get('normal_frame_C1_reuse') != frame_c1_module.definition()
                or not isinstance(q.frame_c1,frame_c1_module.NormalFrameC1Kernel)
                or q.frame_c1.q is not q
                or q.frame_c1.model_identity_sha256 != q.identity
                or q.frame_c1.definition != q.model['normal_frame_C1_reuse']
                or q.model.get('base_source_sha256') != BASE_SOURCE_SHA256
                or q.model.get('base_complete_model') != q.base.model
                or canonical(q.base.model) != q.base.identity
                or q.model.get('implicit_control_dimension') != 6
                or q.model.get('normal_increment_dimension') != 3
                or q.model.get('normal_stage_count') != q.normal_stage_count
                or q.model.get('complete_first_angular_implicit_dimension') != 6*q.normal_stage_count
                or q.model.get('complete_second_angular_implicit_dimension') != 9*q.normal_stage_count
                or q.model.get('common_partition_for_all_angles_and_free_points') is not True
                or q.model.get('per_angle_adaptive_normal_partition') is not False
                or q.model.get('stationary_KKT_selection_used') is not False):
            raise ValueError('Bind the complete actual model, original free variables and every normal stage')
        nodes = tuple(q.normal_step_nodes)
        if (len(nodes) != q.normal_stage_count+1 or any(not isinstance(v,Fraction) for v in nodes)
                or nodes[0] != 0 or nodes[-1] != 1
                or any(a >= b for a,b in zip(nodes,nodes[1:]))
                or [str(v) for v in nodes] != q.model.get('exact_normal_step_nodes')
                or tuple(float(v).hex() for v in nodes)
                    != tuple(float(v).hex() for v in q.normal_step_carriers)
                or [float(v).hex() for v in q.normal_step_carriers]
                    != q.model.get('actual_normal_step_carriers_binary64_hex')):
            raise ValueError('Use one complete source-declared common partition and its actual carriers')
        methods = {name:getattr(q,name) for name in frame_c1_module.complete_method_ast()}
        if any(getattr(method,'__self__',None) is not q for method in methods.values()):
            raise ValueError('The nine original complete methods must remain bound to this operator')
        path = Path(methods['_stage_jacobian'].__func__.__code__.co_filename).resolve()
        source = path.read_bytes()
        digest = hashlib.sha256(source).hexdigest()
        if (digest != q.model.get('source_sha256')
                or digest != q.frame_c1.actual_operator_source_sha256):
            raise ValueError('The complete actual operator source and declared model differ')
        classes = [node for node in ast.parse(source).body
            if isinstance(node,ast.ClassDef) and node.name == 'ZeroClosureOperator']
        if len(classes) != 1:
            raise ValueError('Read the complete original-plus-explicit-hooks operator body')
        nodes_by_name = {node.name:node for node in classes[0].body
            if isinstance(node,ast.FunctionDef)}
        for name,method in methods.items():
            function = method.__func__
            if (Path(function.__code__.co_filename).resolve() != path
                    or function is not q.frame_c1.methods[name]
                    or function.__globals__.get('SCHEMA') != q.model.get('schema')
                    or function.__globals__.get('FRAME_C1_SOURCE_SHA256') != FRAME_C1_SOURCE_SHA256
                    or function.__globals__.get('STAGE_MATRIX_SOURCE_SHA256') != sha(__file__)
                    or function.__globals__.get('ANALYTIC_STAGE_SOURCE_SHA256') != ANALYTIC_STAGE_SOURCE_SHA256
                    or name not in nodes_by_name
                    or canonical(frame_c1_module._ast_value(nodes_by_name[name]))
                        != frame_c1_module.complete_method_ast()[name]):
                raise ValueError('Changed original complete method or explicit source pin: '+name)
        calibration = q.reference_calibration
        cal_function = calibration.bind_field.__func__
        calibration_sha = sha(cal_function.__code__.co_filename)
        if (calibration.definition != q.model.get('reference_centering_definition')
                or methods['_total'].__func__.__globals__.get('REFERENCE_CENTERING_SOURCE_SHA256')
                    != calibration_sha):
            raise ValueError('Keep the complete independently bound current calibration source')
        self.methods = {name:method.__func__ for name,method in methods.items()}
        self.model_identity_sha256 = q.identity
        self.actual_operator_source_sha256 = digest
        self.actual_calibration_source_sha256 = calibration_sha
        self.model_object,self.base_model_object = q.model,q.base.model
        self.partition = tuple(str(v) for v in nodes)
        self.partition_carriers = tuple(float(v).hex() for v in q.normal_step_carriers)
        self.scopes_started = 0
        self.scopes_closed = 0
        self.counts = _new_counts()
        self.scope_seconds = 0.
        self.original_method_seconds = 0.
        self.last_scope = None
        self.point_owner_binding_seconds = 0.
        self.complete_point_word_read_seconds = 0.
        self.complete_point_array_sha_seconds = 0.

    def scope(self, data, literal_phi_hex_keys, order, phase):
        require_actions()
        self.scopes_started += 1
        return CompleteDetachedStageMatrixScope(self,data,literal_phi_hex_keys,
            order,phase,self.scopes_started)

    def _finish(self, record):
        self.scopes_closed += 1
        for key,value in record['actual_counts'].items():
            if key.startswith('peak_'):
                self.counts[key] = max(self.counts[key],value)
            else:
                self.counts[key] += value
        self.scope_seconds += record['scope_seconds']
        self.original_method_seconds += record['original_method_seconds']
        self.point_owner_binding_seconds += record['point_owner_binding_seconds']
        self.complete_point_word_read_seconds += record['complete_point_word_read_seconds']
        self.complete_point_array_sha_seconds += record['complete_point_array_sha_seconds']
        self.last_scope = record

    def metadata(self):
        return dict(schema=SCHEMA,source_sha256=sha(__file__),definition=_plain_copy(self.definition),
            actual_operator_source_sha256=self.actual_operator_source_sha256,
            actual_calibration_source_sha256=self.actual_calibration_source_sha256,
            actual_model_identity_sha256=self.model_identity_sha256,
            scopes_started=self.scopes_started,scopes_closed=self.scopes_closed,
            actual_counts=dict(self.counts),scope_seconds=self.scope_seconds,
            original_method_seconds=self.original_method_seconds,
            last_scope=_plain_copy(self.last_scope),
            point_owner_binding_seconds=self.point_owner_binding_seconds,
            complete_point_word_read_seconds=self.complete_point_word_read_seconds,
            complete_point_array_sha_seconds=self.complete_point_array_sha_seconds,
            point_guard_costs_count_only_closed_scopes=True,
            per_stage_complete_point_word_copy_performed=False,
            matrices_or_input_graphs_stored_in_kernel=False,
            normal_Newton_matrices_served_by_this_cache=False,
            original_equations_and_stage_solves_executed_by_this_cache=False,
            original_equations_and_stage_solves_still_required_in_caller=True,
            matrix_singularity_or_field_success_inferred=False,
            scope_seconds_include_owning_stage_chain=True,
            measured_acceleration_or_repeat_rate_claimed=False,
            arithmetic_errors_enclosed=False)


class CompleteDetachedStageMatrixScope:
    """One complete actual detached subset, with an independent numerical cache."""
    def __init__(self, kernel, data, keys, order, phase, serial):
        require_actions()
        self.kernel,self.q,self.module = kernel,kernel.q,kernel.frame_module
        if (phase not in PHASES or type(order) is not int or order not in (1,2)
                or not isinstance(data,dict) or int(data.get('order',-1)) != order
                or not self.module._all_data_detached(data)):
            raise ValueError('Use one complete detached root/linearization batch of a declared angular order')
        keys = tuple(keys)
        if (not keys or len(keys) != len(data['core'][0])
                or any(not isinstance(key,str) or not math.isfinite(float.fromhex(key))
                    or float.fromhex(key).hex() != key for key in keys)):
            raise ValueError('Keep every ordered canonical literal angle of the actual batch')
        self.data,self.keys,self.order,self.phase = data,keys,order,phase
        self.count,self.serial = len(keys),serial
        self.data_identity = self.module._data_identity(data)
        self.counts = _new_counts()
        self.point_owner_binding_seconds = 0.
        self.complete_point_word_read_seconds = 0.
        self.complete_point_array_sha_seconds = 0.
        self.point_object = self.q._current_x
        self.point_identity = self.q._current_point_sha256
        self.point_owner = None
        self.point_owner = self._point_binding('entry')
        self.point_words = self._read_complete_point_words('entry')
        self.counts['whole_point_entry_array_sha_checks'] += 1
        point_sha_started = time.monotonic()
        try:
            current_sha = self.kernel.methods['_stage_jacobian'].__globals__['array_sha'](self.point_object)
            if (not isinstance(self.point_identity,str) or current_sha != self.point_identity
                    or canonical(self.q.model) != kernel.model_identity_sha256):
                raise ValueError('Use the actual complete selected free point and current model')
        except Exception:
            self.counts['whole_point_entry_array_sha_failures'] += 1
            raise
        finally:
            self.complete_point_array_sha_seconds += time.monotonic()-point_sha_started
        self.carrier = self._carrier_identity()
        self.cache,self.blocked = {},set()
        self.cache_bytes = 0
        self.zero_object = None
        self.zero_identity = None
        self.zero_words = None
        self.next_stage = 0
        self.closed = False
        self.started = time.monotonic()
        self.original_seconds = 0.
        self.records,self.optional_failures = [],[]
        self.last_request_record = None
        self.binding = dict(scope_serial=serial,phase=phase,
            actual_operator_source_sha256=kernel.actual_operator_source_sha256,
            actual_calibration_source_sha256=kernel.actual_calibration_source_sha256,
            actual_model_identity_sha256=kernel.model_identity_sha256,
            actual_full_free_point_sha256=self.point_identity,
            complete_free_point_words_sha256=hashlib.sha256(self.point_words).hexdigest(),
            complete_free_point_word_count=int(self.q.free_size),
            complete_free_point_shape=[int(self.q.free_size)],
            complete_free_point_stride_bytes=[8],
            immutable_point_owner_bytes=len(self.point_owner),
            point_dtype='float64',point_owner_kind='immutable built-in bytes',
            point_array_is_plain_native_contiguous_readonly_nonowning=True,
            entry_canonical_array_sha_checked=True,
            per_stage_complete_point_word_copy_performed=False,
            literal_phi_hex=list(keys),literal_phi_words_sha256=canonical(keys),
            literal_angle_count=self.count,angular_order=order,
            normal_stage_count=self.q.normal_stage_count,
            exact_normal_step_nodes=list(kernel.partition),
            actual_normal_step_carriers_binary64_hex=list(kernel.partition_carriers),
            complete_previous_shape=[self.count,3,6],
            complete_frame_shape=[self.count,3,3,6],
            detached_data_objects_versions_and_layouts_bound=True,
            current_S_hex=float(self.q.S).hex(),J=int(self.q.J),
            integration_order=int(self.q.integration_order),
            mesh_words_sha256=hashlib.sha256(self.carrier[3][-1]).hexdigest(),
            gauss_weight_words_sha256=hashlib.sha256(self.carrier[4][-1]).hexdigest(),
            all_tau_values_still_used_by_the_original_stage_equations=True,
            zero_target_words_sha256=None,
            active_parameter_graph_accepted=False)

    def _point_binding(self, phase):
        self.counts['point_owner_'+phase+'_checks'] += 1
        started = time.monotonic()
        try:
            owner = _immutable_point_owner(self.point_object,(self.q.free_size,),self.point_owner)
            if (self.q._current_x is not self.point_object
                    or self.q._current_point_sha256 != self.point_identity):
                raise ValueError('Do not replace the actual selected point object or its complete identity inside a scope')
            return owner
        except Exception:
            self.counts['point_owner_'+phase+'_failures'] += 1
            raise
        finally:
            self.point_owner_binding_seconds += time.monotonic()-started

    def _read_complete_point_words(self, phase):
        self.counts['whole_point_'+phase+'_reads'] += 1
        started = time.monotonic()
        try:
            return self.module._array_words(self.point_object,(self.q.free_size,))[0]
        except Exception:
            self.counts['whole_point_'+phase+'_read_failures'] += 1
            raise
        finally:
            self.complete_point_word_read_seconds += time.monotonic()-started

    def _carrier_identity(self):
        if (type(self.q.J) not in (int,np.int64,np.int32) or self.q.J < 2
                or type(self.q.integration_order) not in (int,np.int64,np.int32)
                or self.q.integration_order < 1
                or not math.isfinite(float(self.q.S)) or self.q.S <= 0):
            raise ValueError('Bind the positive original total-integral carrier and dimensions')
        return (float(self.q.S).hex(),int(self.q.J),int(self.q.integration_order),
            _numpy_layout(self.q.mesh,(self.q.J,)),
            _numpy_layout(self.q.gauss_w,(self.q.integration_order,)))

    def _validate(self, previous, frame, zero, tau, stage_index):
        self._point_binding('stage')
        if (self.closed or type(stage_index) is not int or stage_index != self.next_stage
                or not 0 <= stage_index < self.q.normal_stage_count
                or not math.isfinite(float(tau))
                or float(tau).hex() != self.kernel.partition_carriers[stage_index+1]
                or tuple(str(v) for v in self.q.normal_step_nodes) != self.kernel.partition
                or tuple(float(v).hex() for v in self.q.normal_step_carriers)
                    != self.kernel.partition_carriers
                or self.q.model is not self.kernel.model_object
                or self.q.base.model is not self.kernel.base_model_object
                or self.q.identity != self.kernel.model_identity_sha256
                or canonical(self.q.model) != self.kernel.model_identity_sha256
                or self.q._current_x is not self.point_object
                or self.q._current_point_sha256 != self.point_identity
                or not self.module._all_data_detached(self.data)
                or self.module._data_identity(self.data) != self.data_identity
                or self._carrier_identity() != self.carrier
                or any(getattr(self.q,name).__func__ is not function
                    for name,function in self.kernel.methods.items())):
            raise ValueError('Do not cross a point, batch, layout, graph, source, carrier, order or fixed stage')
        previous_layout = _tensor_layout(previous,(self.count,3,6))
        frame_layout = _tensor_layout(frame,(self.count,3,3,6))
        _tensor_layout(zero,(self.count,3,3))
        zero_identity = self.module._tensor_identity(zero)
        zero_words,_ = self.module._array_words(zero,(self.count,3,3))
        if self.zero_object is None:
            self.zero_object,self.zero_identity,self.zero_words = zero,zero_identity,zero_words
            self.binding['zero_target_words_sha256'] = hashlib.sha256(zero_words).hexdigest()
        elif (zero is not self.zero_object or zero_identity != self.zero_identity
                or zero_words != self.zero_words):
            raise ValueError('Bind the complete original zero target; never substitute a stage-specific target')
        return previous_layout,frame_layout

    def scalar(self, eta, previous, frame, zero, tau, stage_index):
        if self.phase != PHASES[0]:
            raise ValueError('Returned-value J3 and full angular J6/J9 use separate scopes')
        return self._request('scalar',eta,previous,frame,zero,tau,stage_index)

    def angular(self, increments, previous, frame, zero, tau, stage_index, order):
        if self.phase != PHASES[1] or type(order) is not int or order != self.order:
            raise ValueError('Keep each complete angular order in its separate exact scope')
        return self._request('angular',increments,previous,frame,zero,tau,stage_index)

    def _request(self, kind, increments, previous, frame, zero, tau, stage_index):
        previous_layout,frame_layout = self._validate(previous,frame,zero,tau,stage_index)
        increment_shape = (self.count,3) if kind == 'scalar' else (self.count,3,3)
        increment_layout = _tensor_layout(increments,increment_shape)
        size = 3 if kind == 'scalar' else 3*(self.order+1)
        self.next_stage += 1
        self.counts['logical_matrix_requests'] += 1
        self.counts['logical_'+kind+'_requests'] += 1
        self.counts['logical_angle_blocks'] += self.count
        self.counts['logical_angle_rows'] += size*self.count
        record = dict(request_index=len(self.records),normal_stage_index=stage_index+1,
            exact_auxiliary_node=self.kernel.partition[stage_index+1],
            actual_auxiliary_node_hex=float(tau).hex(),kind=kind,angular_order=self.order,
            matrix_shape=[self.count,size,size],complete_input_key_sha256=None,
            completed=False,numerical_value_origin=None,original_method_executed=False,
            own_stage_equation_or_root_success_inferred=False)
        self.records.append(record)
        self.last_request_record = record
        key = None
        try:
            previous_words,_ = self.module._array_words(previous,(self.count,3,6))
            frame_words,_ = self.module._array_words(frame,(self.count,3,3,6))
            increment_words,_ = self.module._array_words(increments,increment_shape)
            key = (kind,self.order,previous_layout,frame_layout,increment_layout,
                previous_words,frame_words,increment_words)
            record['complete_input_key_sha256'] = canonical(dict(kind=kind,order=self.order,
                previous_layout=previous_layout,frame_layout=frame_layout,
                increment_layout=increment_layout,
                previous_words_sha256=hashlib.sha256(previous_words).hexdigest(),
                frame_words_sha256=hashlib.sha256(frame_words).hexdigest(),
                increment_words_sha256=hashlib.sha256(increment_words).hexdigest()))
        except (MemoryError,RuntimeError) as error:
            self.counts['cache_key_failures'] += 1
            self._optional_failure(record,'construct complete equality key',error)
        if key is not None and key in self.cache:
            entry = self.cache[key]
            try:
                result = entry['value'].clone()
            except (MemoryError,RuntimeError) as error:
                self._discard(key)
                self.blocked.add(key)
                self.counts['cache_copy_or_store_failures'] += 1
                self._optional_failure(record,'clone previously returned original matrix',error)
            else:
                self.counts['cache_hits'] += 1
                self.counts['cache_'+kind+'_hits'] += 1
                record.update(numerical_value_origin=dict(scope_serial=self.serial,
                    request_index=entry['request_index'],normal_stage_index=entry['stage_index']+1,
                    complete_input_key_sha256=record['complete_input_key_sha256'],
                    actual_matrix_words_sha256=entry['matrix_sha256']),
                    reused_previous_original_matrix_value=True,
                    unexecuted_fresh_AD_words_claimed_equal=False,
                    actual_normal_counter_delta={name:0 for name in NORMAL_COUNTER_KEYS},
                    actual_implicit_jacobian_blocks_delta=0)
                self._complete(record)
                return result
        result = self._original_value(kind,increments,previous,frame,zero,tau,size,record)
        try:
            matrix_words,_ = self.module._array_words(result,(self.count,size,size))
            matrix_sha = hashlib.sha256(matrix_words).hexdigest()
        except (MemoryError,RuntimeError) as error:
            self.counts['cache_value_digest_failures'] += 1
            self._optional_failure(record,'record complete returned matrix words',error)
            # The original scientific return is already available.  Do not
            # turn an optional digest allocation into a different root result.
            matrix_sha = None
            key = None
        record.update(numerical_value_origin=dict(scope_serial=self.serial,
            request_index=record['request_index'],normal_stage_index=stage_index+1,
            complete_input_key_sha256=record['complete_input_key_sha256'],
            actual_matrix_words_sha256=matrix_sha),reused_previous_original_matrix_value=False)
        if key is not None and key not in self.blocked:
            try:
                saved = result.detach().clone()
                self.cache[key] = dict(value=saved,request_index=record['request_index'],
                    stage_index=stage_index,matrix_sha256=matrix_sha)
            except (MemoryError,RuntimeError) as error:
                self._discard(key)
                self.blocked.add(key)
                self.counts['cache_copy_or_store_failures'] += 1
                self._optional_failure(record,'save a clone of the complete original matrix',error)
            else:
                self.cache_bytes += result.numel()*result.element_size()
                self.counts['saved_matrices'] += 1
                self.counts['peak_cached_matrix_bytes'] = max(
                    self.counts['peak_cached_matrix_bytes'],self.cache_bytes)
        elif key is not None:
            self.counts['bypassed_after_optional_failure'] += 1
        self._complete(record)
        return result

    def _original_value(self, kind, increments, previous, frame, zero, tau, size, record):
        self.counts['original_matrix_attempts'] += 1
        self.counts['original_'+kind+'_attempts'] += 1
        record['original_method_executed'] = True
        before = {name:self.q.normal_counts[name] for name in NORMAL_COUNTER_KEYS}
        before_blocks = self.q.endpoint_counts['implicit_jacobian_blocks']
        started = time.monotonic()
        try:
            if kind == 'scalar':
                result = self.q._stage_jacobian(increments,self.data,previous,frame,zero,tau)
            else:
                result = self.q._stage_jet_jacobian(increments,self.data,previous,frame,
                    zero,tau,self.order)
            _tensor_layout(result,(self.count,size,size))
            if not bool(torch.isfinite(result).all()):
                raise ValueError('Never memoize a nonfinite original stage matrix')
        except Exception as error:
            self.counts['original_matrix_failures'] += 1
            record['original_matrix_failure'] = dict(exception_type=type(error).__name__,reason=str(error))
            raise
        finally:
            elapsed = time.monotonic()-started
            self.original_seconds += elapsed
            record['original_method_seconds'] = elapsed
            deltas = {name:self.q.normal_counts[name]-before[name] for name in NORMAL_COUNTER_KEYS}
            block_delta = self.q.endpoint_counts['implicit_jacobian_blocks']-before_blocks
            if any(type(value) is not int or value < 0 for value in (*deltas.values(),block_delta)):
                raise ValueError('Original matrix counters must remain actual nonnegative increments')
            for name,value in deltas.items():
                self.counts[name if name.startswith('actual_') else 'actual_'+name] += value
            self.counts['actual_implicit_jacobian_blocks'] += block_delta
            record['actual_normal_counter_delta'] = deltas
            record['actual_implicit_jacobian_blocks_delta'] = block_delta
        self.counts['original_matrix_returns'] += 1
        return result

    def _complete(self, record):
        self.counts['completed_matrix_requests'] += 1
        record['completed'] = True

    def _discard(self, key):
        entry = self.cache.pop(key,None)
        if entry is not None:
            self.cache_bytes -= entry['value'].numel()*entry['value'].element_size()

    def _optional_failure(self, record, operation, error):
        item = dict(request_index=record['request_index'],normal_stage_index=record['normal_stage_index'],
            kind=record['kind'],complete_input_key_sha256=record['complete_input_key_sha256'],
            operation=operation,exception_type=type(error).__name__,reason=str(error),
            fallback='original complete matrix method, or its already computed complete return')
        self.optional_failures.append(item)
        record.setdefault('optional_cache_failures',[]).append(item)
        error.__traceback__ = None

    def close(self):
        if self.closed:
            return
        exit_check = dict(attempted=True,immutable_binding_valid=False,
            complete_point_words_equal=None,failures=[])
        try:
            self._point_binding('exit')
        except Exception as error:
            exit_check['failures'].append(dict(operation='immutable point binding at scope exit',
                exception_type=type(error).__name__,reason=str(error)))
        else:
            exit_check['immutable_binding_valid'] = True
        try:
            words = self._read_complete_point_words('exit')
        except Exception as error:
            exit_check['failures'].append(dict(operation='complete point word read at scope exit',
                exception_type=type(error).__name__,reason=str(error)))
        else:
            exit_check['complete_point_words_equal'] = words == self.point_words
            if not exit_check['complete_point_words_equal']:
                exit_check['failures'].append(dict(operation='complete point word equality at scope exit',
                    exception_type='ValueError',reason='The complete selected point words changed inside a matrix scope'))
        point_complete = (exit_check['immutable_binding_valid'] is True
            and exit_check['complete_point_words_equal'] is True and not exit_check['failures']
            and self.counts['point_owner_stage_failures']==0)
        record = dict(binding=self.binding,actual_counts=dict(self.counts),
            scope_seconds=time.monotonic()-self.started,
            original_method_seconds=self.original_seconds,
            point_owner_binding_seconds=self.point_owner_binding_seconds,
            complete_point_word_read_seconds=self.complete_point_word_read_seconds,
            complete_point_array_sha_seconds=self.complete_point_array_sha_seconds,
            point_scope_exit_check=exit_check,scope_point_binding_complete=point_complete,
            stage_requests_attempted=self.next_stage,
            all_declared_stage_matrix_requests_completed=(
                self.next_stage == self.q.normal_stage_count
                and self.counts['completed_matrix_requests'] == self.q.normal_stage_count),
            matrix_request_records=self.records,optional_cache_failures=self.optional_failures,
            active_parameter_graph_borrowed=False,
            original_Newton_matrices_unchanged=True,
            original_phase_source=self.phase,
            scientific_field_success_inferred=False)
        self.closed = True
        self.cache.clear()
        self.blocked.clear()
        self.cache_bytes = 0
        self.data = None
        self.zero_object = None
        self.point_object = None
        self.point_owner = None
        self.point_words = None
        self.zero_words = None
        self.carrier = None
        self.data_identity = None
        self.zero_identity = None
        self.kernel._finish(record)
        if not point_complete:
            raise ValueError('Complete matrix scope point binding failed: '+json.dumps(dict(exit_check=exit_check,stage_binding_failures=self.counts['point_owner_stage_failures'])))

    def __enter__(self):
        return self

    def __exit__(self, error_type, error, traceback):
        try:
            self.close()
        except Exception:
            if error_type is None:
                raise
            # Preserve the original body exception.  The failed exit guard
            # has already been retained in the closed own-scope record.
        return False
