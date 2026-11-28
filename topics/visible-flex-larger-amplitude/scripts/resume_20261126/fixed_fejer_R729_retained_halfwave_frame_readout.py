#!/usr/bin/env python3
"""The complete original run28 frame readout, retained without numerical changes.

This pure-only source holds the original full function and canonical serializer.
It imports no scientific library and never evaluates a field, root or derivative.
"""
import hashlib
import json
import math
from pathlib import Path

def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


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




def source_record():
    raw=Path(__file__).read_bytes()
    return dict(schema='complete-R729-retained-original-halfwave-frame-readout-v1',
        path=str(Path(__file__).resolve()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
        original_complete_reader_sha256="8631ae6ba1b20480465b96d2c4b71c419253a736e24ecba9cae967d01cb955d2",
        complete_original_function_sha256="ed7afb7e4c04bd441628e176176faf69ac2e9f6793894899cec524895d6b0a26",
        complete_original_canonical_sha256="7fe46a84349eee09a783ece5decbd3c61a223dae764beba80f48925fe2b5621f",
        both_function_texts_retained_byte_for_byte=True,
        every_original_counter_scope_point_and_error_check_retained=True,
        source_bound_pure_relocation_only=True,field_root_or_J_evaluations=0)
