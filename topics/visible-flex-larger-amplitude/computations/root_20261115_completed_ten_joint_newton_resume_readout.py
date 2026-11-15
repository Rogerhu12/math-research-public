#!/usr/bin/env python3
"""Request183 necessary original conclusion; no scientific recomputation.

The whole temporary status and every original trial/FD record are read.
Return all128 planned direction rows, initial/final ten words, all original
FD level maxima/errors and original final gates. Large direction/J/QR and
per-trial vectors are identified, not encoded or split for transport.
"""
from __future__ import annotations
import argparse
from collections import Counter
from decimal import Decimal, InvalidOperation
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import traceback

HERE=Path(__file__).resolve().parent
ENTRY='root_20261115_completed_ten_joint_newton_resume_readout.py'
PRODUCER='geometry_20261115_completed_ten_joint_newton_resume.py'
PRODUCER_SHA='57569d4734ec10f64db71416ab2e61a37db2b724addad64413938c16d803f1d6'
PRODUCER_SCHEMA='R259-completed-ten-persistent-scaled-Newton-continuation-v1'
STATUS_NAME='completed-ten-joint-newton-resume-status.json'
SCHEMA='request183-complete-ten-continuation-necessary-readback-v1'
BASE='root_20261115_fixed_power_ten_joint_newton_scalar_readout.py'
BASE_SHA='728ac09e7f008f06396bf578822b1107fa9cfcdb806a64e01d0cc130c303d3ef'
LIMIT=90000


def encoded(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=True,allow_nan=False,
        separators=(',',':')).encode('ascii')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(value):
    raw=encoded(value)
    return dict(canonical_bytes=len(raw),canonical_sha256=digest(raw))


def file_identity(path):
    raw=Path(path).read_bytes()
    return dict(file=Path(path).name,bytes=len(raw),sha256=digest(raw))


def load_reader():
    if digest((HERE/BASE).read_bytes())!=BASE_SHA:
        raise ValueError('The frozen original ten-FD metadata reader differs')
    spec=importlib.util.spec_from_file_location('_request183_original_metadata_reader',HERE/BASE)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def selected_extrema(rows):
    """Order existing finite Decimal word values; do not form any new scientific scalar."""
    low=None;high=None;nonfinite=[]
    for global_index,trial in rows:
        value=trial.get('actual_merit')
        if value is None:
            continue
        try:
            word=Decimal(str(value))
        except (InvalidOperation,ValueError) as error:
            nonfinite.append(dict(direction=global_index,trial=trial.get('trial'),
                original_value=value,metadata_parse_error=repr(error)))
            continue
        if not word.is_finite():
            nonfinite.append(dict(direction=global_index,trial=trial.get('trial'),
                original_value=value))
            continue
        item=(word,global_index,trial)
        if low is None or word<low[0]:low=item
        if high is None or word>high[0]:high=item
    def original(item):
        if item is None:return None
        _,global_index,trial=item
        return dict(direction=global_index,**{key:trial[key] for key in (
            'trial','alpha','accepted','actual_merit','actual_unit_equations',
            'original_Armijo_bound','reason') if key in trial})
    return dict(minimum_recorded_finite_merit=original(low),
        maximum_recorded_finite_merit=original(high),
        original_nonfinite_or_malformed_merit_records=nonfinite,
        only_ordering_of_original_values_not_norms_differences_or_recomputed_merit=True)


def description(base,reader,value,path,binary64=False):
    result=reader.description(value,path,binary64)
    if not isinstance(value,dict):return result
    matrix_key='three_by_ten_parameter_jacobian' if binary64 else 'complete_three_by_ten_forward_response'
    matrix=result.pop(matrix_key,None)
    result[matrix_key+'_identity']=identity(matrix)
    result['complete_matrix_words_transported']=False
    # The whole original description was already checked; these large diagnostics
    # do not define the required compact restart or original final-gate claims.
    for key in ('low_mode_trajectory_max_by_mode','low_two_by_two_right_condition_max_by_mode'):
        if key in result:result[key+'_identity']=identity(result.pop(key))
    return result


def build(status,raw,directory,rules,compute_outcome):
    base=load_reader()
    reader=base.Readback()
    if status.get('schema')!=PRODUCER_SCHEMA or status.get('source_sha256')!=PRODUCER_SHA:
        raise ValueError('Do not relabel an old eight-direction or nine-coordinate producer')
    sources=status.get('consumed_source_sha256',{})
    if len(sources)!=46 or sources.get(PRODUCER)!=PRODUCER_SHA:
        raise ValueError('The complete current46 consumed-source closure differs')
    fields=['phase','run_id','source_commit','actual_origin','parameter_recipe',
        'continuation_contract','input_sha256','initial_ten_parameter_words',
        'fixed_scale_original_actual157_words','fixed_scale_origin','original_parent_radius',
        'parent_radius_not_used_as_new_shape_scale','decimal_digits','rounding',
        'original_mesh_nodes','field_and_tail_modes','selected_catalogue_index',
        'catalogue_reselection_performed','all_ten_parameters_can_change',
        'fixed_physical_scales','fixed_scales_computed_once_from_actual157_words',
        'scaled_trust_radius','shape_frozen_for_all_ten_forward_FD_trials_and_final_consumers',
        'accepted_point_count','attempted_outer_directions','original_trial_records',
        'current_accepted_ten_parameter_words','unvisited_outer_indices','unvisited_block_indices',
        'old_nine_parameters_relabelled_as_new','new_shape_parameter_index',
        'input_tables_not_reformed_in_high_precision',
        'source_bound_original112_terminal_and699_chain_retained',
        'full_ten_QR_or_Cauchy_is_a_proposal_not_an_accuracy_or_rank_gate',
        'high_mode_Schur_elimination_or_current_nonlinear_native_performed',
        'native_nonlinear_solver_called','nonzero_field_completed','success',
        'diagnostic_completed','resource_partial','stop_reason','exception','traceback',
        'scientific_failure_not_inferred','actual_initial_merit',
        'original_Armijo_coefficient_exact_binary64_lift','final_ten_parameter_words',
        'final_selected_shape_coefficient','final_original_three_merit',
        'high_precision_original_unit_stopping_tolerance_met',
        'high_precision_full112_linear_right_tolerance_met',
        'binary64_projection_original_unit_stopping_tolerance_met',
        'binary64_projection_full112_linear_right_tolerance_met',
        'initial_final_complete_ten_axis_three_step_Decimal_and_binary64_FD_attempted',
        'final_continuous_scalar_and453_circle_consumers_at_explicit_projection_only',
        'high_precision_complete_interval_domain_or_exact_derivative_accuracy_certified',
        'independent_ten_model_call_counts','fresh_original_nine_model_call_counts',
        'complete_original_event_ledger','elapsed_wall_seconds',
        'zero_extension_not_evaluated_in_nonzero_ten_resume',
        'no_previous_parent_state_J_merit_or_FD_used_as_current',
        'old_nine_model_role','fresh_initial_parent_word_comparison']
    out=dict(schema=SCHEMA,producer_schema=PRODUCER_SCHEMA,producer_sha256=PRODUCER_SHA,
        original_status=dict(file=STATUS_NAME,bytes=len(raw),sha256=digest(raw)),
        readout_source=file_identity(__file__),base_metadata_reader=file_identity(HERE/BASE),
        **base.pick(status,fields),actual_compute_outcome=compute_outcome,
        complete_current_source_closure_count=len(sources),
        complete_current_source_closure_identity=identity(sources),
        actual_rule_sync=base.compact_rules(rules),
        original_policy_identity=identity(status.get('policy')),
        fixed_shape_definition_identity=identity(status.get('fixed_shape_definition')),
        fixed_shape_evidence_identity=identity(status.get('fixed_shape_evidence')),
        no_scientific_evaluation_or_matrix_norm_FD_recalculation=True,
        one_small_conclusion_not_a_data_reconstruction_protocol=True,
        raw_Git_Release_or_artifact_retention=False)
    for name in ('original_nine_literal_binding','new_ten_literal_binding'):
        value=status.get(name)
        if value is not None:
            out[name]=dict(identity=identity(value),original=base.pick(value,[
                'schema','source','canonical_binding_sha256','parameter_dimension','parameter_order',
                'decimal_digits','rounding','original_mesh_nodes','field_and_tail_modes',
                'complete_original_tail_J_consumed',
                'new_control_table_words_are_binary64_source_samples_then_exact_lifts',
                'new_shape_table_formation_recomputed_in_Decimal',
                'no_discrete_rounding_derivative_or_interval_accuracy_certificate',
                'frozen_original_native_anchor_J_is_not_a_new_g_nonlinear_tail_response']))
    for name,binary in (('initial',False),('final',False),
            ('initial_binary64_projection',True),('final_binary64_projection',True)):
        out[name]=description(base,reader,status.get(name),name,binary)
    for name in ('initial_projection_contract','final_projection_contract'):
        if name in status:
            out[name]=dict(identity=identity(status[name]),
                original_scalar_flags=base.scalar_fields(status[name]),
                actual_failures_and_exceptions=base.exceptions_in(status[name],name))
    steps=status.get('outer_steps',[])
    if not isinstance(steps,list) or len(steps)>128:
        raise ValueError('The original continuation direction list is malformed')
    columns=['direction','started','accepted','accepted_alpha','merit_before',
        'merit_after','formed_full3_slope','real_trial_count','unvisited_real_trial_indices',
        'original_stop_reason','complete_original_record_sha256']
    rows=[];trial_items=[];trial_reasons=Counter();domain_counts=Counter()
    direction_errors=[];trial_errors=[];accepted_count=0
    for i,row in enumerate(steps):
        path='outer_steps['+str(i)+']'
        reader.required(row,['global_direction','block_index','direction','parameters_before',
            'original_full3_residual','original_full3_merit_before','direction_model',
            'trials','accepted','unvisited_real_trial_indices'],path)
        if (row.get('global_direction'),row.get('block_index'),row.get('direction'))!=(i,i//8,i%8):
            reader.metadata_errors.append(dict(path=path,reason='global/block/local direction order differs'))
        reader.vector(row.get('parameters_before'),10,path+'.parameters_before')
        reader.vector(row.get('original_full3_residual'),3,path+'.original_full3_residual')
        if 'current_complete_three_by_ten_J' in row:
            reader.matrix(row['current_complete_three_by_ten_J'],3,10,path+'.current_complete_three_by_ten_J')
        if 'actual_ten_direction' in row:
            reader.vector(row['actual_ten_direction'],10,path+'.actual_ten_direction')
            reader.vector(row.get('original_complete_three_directional_response'),3,
                path+'.original_complete_three_directional_response')
        dm=row.get('direction_model',{})
        direction_errors.extend(base.exceptions_in(dm,path+'.direction_model'))
        trials=row.get('trials',[])
        if not isinstance(trials,list) or len(trials)>20:
            raise ValueError('The original twenty-trial list is malformed')
        actual_accepted=[]
        for j,trial in enumerate(trials):
            tpath=path+'.trials['+str(j)+']'
            reader.required(trial,['trial','alpha','seed_parameters','original_Armijo_bound',
                'original_full3_slope','accepted'],tpath)
            if trial.get('trial')!=j:
                reader.metadata_errors.append(dict(path=tpath,reason='original trial order differs'))
            reader.vector(trial.get('seed_parameters'),10,tpath+'.seed_parameters')
            if trial.get('all_original_finite_primal_domain_guards_passed') is True:
                reader.required(trial,['actual_merit','actual_parameters','actual_unit_equations',
                    'actual_full112_right'],tpath)
                reader.vector(trial.get('actual_parameters'),10,tpath+'.actual_parameters')
                reader.vector(trial.get('actual_unit_equations'),3,tpath+'.actual_unit_equations')
                reader.vector(trial.get('actual_full112_right'),112,tpath+'.actual_full112_right')
            if trial.get('accepted') is True:actual_accepted.append(j)
            domain_counts[str(trial.get('all_original_finite_primal_domain_guards_passed'))]+=1
            trial_reasons[str(trial.get('reason'))]+=1
            trial_items.append((i,trial))
            trial_errors.extend(base.exceptions_in(trial,tpath))
        if row.get('unvisited_real_trial_indices')!=list(range(len(trials),20)):
            reader.metadata_errors.append(dict(path=path,reason='actual unvisited trial suffix differs'))
        if row.get('accepted') is True:
            accepted_count+=1
            reader.vector(row.get('accepted_ten_parameter_words'),10,path+'.accepted_ten_parameter_words')
            if actual_accepted!=[len(trials)-1]:
                reader.metadata_errors.append(dict(path=path,reason='accepted outer and original accepted trial differ'))
        elif actual_accepted:
            reader.metadata_errors.append(dict(path=path,reason='accepted trial absent from outer acceptance'))
        rows.append([i,True,row.get('accepted'),row.get('accepted_alpha'),
            row.get('original_full3_merit_before'),row.get('original_actual_merit_after'),
            row.get('original_full3_slope'),len(trials),row.get('unvisited_real_trial_indices'),
            row.get('stop_reason'),identity(row)['canonical_sha256']])
    for i in range(len(steps),128):
        rows.append([i,False,None,None,None,None,None,0,list(range(20)),
            status.get('stop_reason',status.get('phase')),None])
    out['direction_columns']=columns
    out['all128_planned_direction_rows']=rows
    out['all_original_direction_records_identity']=identity(steps)
    out['trial_conclusion']=dict(original_count=len(trial_items),
        accepted_count=sum(t.get('accepted') is True for _,t in trial_items),
        reason_counts=dict(sorted(trial_reasons.items())),
        original_primal_domain_flag_counts=dict(sorted(domain_counts.items())),
        original_complete_trial_lists_identity=identity([row.get('trials',[]) for row in steps]),
        extrema=selected_extrema(trial_items),
        all_original_trial_failures_and_exceptions=trial_errors,
        complete_trial_parameter_F_full112_vectors_read_in_Actions_but_not_transported=True)
    out['all_original_direction_failures_and_exceptions']=direction_errors
    blocks=status.get('continuation_blocks',[])
    if not isinstance(blocks,list) or len(blocks)>16:
        raise ValueError('The explicit sixteen-block metadata differs')
    bcols=['block','started','original_eight_search_completed','directions',
        'accepted_count','trial_count','original_stop_reason','continued','first_J_source',
        'fresh_first_forward_equation_words_equal_owner']
    brows=[]
    for i in range(16):
        b=blocks[i] if i<len(blocks) else {}
        brows.append([i,i<len(blocks),b.get('original_eight_search_completed',False),
            b.get('attempted_outer_directions',0),b.get('accepted_point_count',0),
            b.get('original_trial_records',0),b.get('stop_reason',status.get('stop_reason')),
            b.get('continued',False),b.get('first_J_source'),
            b.get('first_forward_equation_words_equal_owned_primal')])
    out['block_columns']=bcols;out['all16_planned_block_rows']=brows
    out['complete_original_block_metadata_identity']=identity(blocks)
    domain=status.get('complete_scalar_domain_at_binary64_projection')
    if domain is not None:
        out['complete_scalar_domain_at_binary64_projection']=dict(identity=identity(domain),
            original=base.pick(domain,['schema','covered_interval','bits','maximum_depth',
                'leaf_count','split_cells','unresolved_leaf_count',
                'complete_declared_real_expression_domain_certified','fresh_new_ten_control_identity',
                'old_scalar_domain_certificate_reused',
                'exact_prefix_scalar_and_complete_stored_finite_Gauss_expression',
                'exact_scalar_derivative_compatibility_or_C2_interface_certificate',
                'literal_binary64_evaluation_roundoff_enclosed',
                'returned_ap_identified_with_derivative_of_finite_Gauss_a','source_returned_ap_used',
                'source_circle_R_and_full_Frenet_domain_covered_by_this_scalar_bound']),
            actual_failures_and_exceptions=base.exceptions_in(domain,'complete_scalar_domain'))
    circle=status.get('original_complete_circle_check_at_binary64_projection')
    if circle is not None:
        dom=circle.get('actual_domain',{})
        square=circle.get('frozen_seven_added_shapes_square_check')
        out['original_complete_circle_check_at_binary64_projection']=dict(identity=identity(circle),
            original=base.pick(circle,['original_full_reference_finite','reference_is_not_a_nonzero_parent',
                'reference_sha256','scalar_family_sha256']),
            frozen_seven_added_shapes_square_check=dict(identity=identity(square),
                scalar_flags=base.scalar_fields(square),actual_failures_and_exceptions=base.exceptions_in(square)),
            actual_domain={**base.scalar_fields(dom),
                'original_RMS_query_checks':dom.get('original_RMS_query_checks'),
                'full_original_domain_identity':identity(dom)},
            actual_failures_and_exceptions=base.exceptions_in(circle,'original_complete_circle'),
            complete_original_FFT_checks_identity=identity(circle.get('original_full_FFT_tangent_checks')))
    for name in ('fresh_extended_scalar_family','original_projection_call_trace',
            'source_bound_family_views','source_bound_decimal_views'):
        if name in status:out[name+'_identity']=identity(status[name])
    if status.get('diagnostic_completed'):
        reader.required(status,['initial','final','initial_binary64_projection','final_binary64_projection',
            'complete_scalar_domain_at_binary64_projection','original_complete_circle_check_at_binary64_projection',
            'fixed_physical_scales','fixed_shape_definition','selected_shape',
            'outer_steps','complete_planned_outer_rows','complete_planned_block_rows','stop_reason'],
            'completed_status')
        if (reader.fd_levels,reader.fd_checks)!=(12,120):
            reader.metadata_errors.append(dict(path='completed_initial_final_FD',
                expected_levels=12,actual_levels=reader.fd_levels,
                expected_checks=120,actual_checks=reader.fd_checks))
    if status.get('accepted_point_count')!=accepted_count:
        reader.metadata_errors.append(dict(path='accepted_point_count',
            recorded=status.get('accepted_point_count'),actual_outer_flags=accepted_count))
    out['original_readback_coverage']=dict(
        planned_directions=128,started_directions=len(steps),planned_blocks=16,started_blocks=len(blocks),
        complete_original_trial_count=len(trial_items),
        original_FD_levels=reader.fd_levels,original_FD_column_checks=reader.fd_checks,
        original_FD_failures_and_exceptions_count=len(reader.fd_failures),
        original_FD_failures_and_exceptions_identity=identity(reader.fd_failures),
        original_FD_failures_returned_in_each_description=True,
        required_available_recorded_fields_complete=not reader.metadata_errors,
        metadata_errors=reader.metadata_errors,
        complete128_direction_rows_and_full_unvisited_suffix_returned=True,
        all_actual_direction_and_trial_records_read_before_necessary_selection=True,
        original_d_J_actions_QR_and_per_trial_vector_values_not_transported=True,
        downstream_recipient_has_not_independently_read_all_large_arrays=True,
        extrema_are_only_selections_of_original_values_not_recomputed_scientific_quantities=True,
        no_accuracy_or_rank_certificate_from_FD_or_formed_slope=True)
    return out,not reader.metadata_errors


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rules-directory',type=Path)
    p.add_argument('--compute-outcome',default='not-recorded')
    args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    path=args.directory/STATUS_NAME;complete=False
    try:
        if not path.is_file():
            out=dict(schema=SCHEMA,producer_schema=PRODUCER_SCHEMA,
                original_status_present=False,readout_source=file_identity(__file__),
                diagnostic_completed=False,complete_original_status_not_available=True,
                actual_compute_outcome=args.compute_outcome,scientific_failure_not_inferred=True)
        else:
            raw=path.read_bytes()
            out,complete=build(json.loads(raw),raw,args.directory,args.rules_directory,args.compute_outcome)
    except Exception as error:
        out=dict(schema='request183-readback-exception-v1',exception=repr(error),
            traceback=traceback.format_exc(),readout_source=file_identity(__file__),
            original_status=file_identity(path) if path.is_file() else None,
            complete_original_readback_not_claimed=True,scientific_failure_not_inferred=True)
    raw=encoded(out);sections={name:len(encoded(value)) for name,value in out.items()}
    original_identity=dict(bytes=len(raw),sha256=digest(raw))
    print(encoded(dict(event='request183-necessary-section-byte-counts',total=len(raw),
        section_UTF8_bytes=sections,hard_bound=LIMIT,
        complete_original_status_not_recomputed=True)).decode(),flush=True)
    if len(raw)>LIMIT:
        out=dict(schema='request183-necessary-summary-over-budget-v1',
            original_summary_identity=original_identity,section_UTF8_byte_counts=sections,
            original_status=out.get('original_status'),phase=out.get('phase'),
            accepted_point_count=out.get('accepted_point_count'),stop_reason=out.get('stop_reason'),
            complete_original_readback_not_transported=True,
            scientific_failure_not_inferred_from_summary_size=True)
        raw=encoded(out);complete=False
    (args.out/'compact-summary.json').write_bytes(raw)
    receipt=dict(bytes=len(raw),sha256=digest(raw),metadata_complete=complete,
        complete_original_status_identity=out.get('original_status'),
        no_raw_array_reconstruction_protocol=True)
    (args.out/'compact-summary-receipt.json').write_bytes(encoded(receipt)+b'\n')
    print('BEGIN_VISIBLE183_COMPACT_SUMMARY',flush=True)
    print(raw.decode('ascii'),flush=True)
    print('END_VISIBLE183_COMPACT_SUMMARY',flush=True)
    print(encoded(dict(event='request183-necessary-summary-identity',**receipt,
        hash_scope='ASCII JSON bytes excluding log separator LF')).decode(),flush=True)
    return 0 if complete else 70


if __name__=='__main__':
    raise SystemExit(main())
