#!/usr/bin/env python3
"""Compact actual Request174 metadata; no numerical source is imported.

Read the complete temporary status, retain scientifically useful original
scalars and small matrices, and identify the larger original arrays/FD
perturbation tables by canonical bytes.  One summary only: no raw-array
encoding, dictionary packing, or structural splitting for transport.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import traceback

ENTRY='root_20261115_local_odd_signsum_ten_control_scalar_readout.py'
PRODUCER='geometry_20261115_local_odd_signsum_ten_control_recipe.py'
PRODUCER_SHA='975bb25f1dd879bd88dc1a3b1df451836cadceca1695820050bfe3842efd949f'
PRODUCER_SCHEMA='R259-all-station-fixed-odd-signsum-ten-control-one-real-full3-direction-v1'
STATUS_NAME='local-odd-signsum-ten-control-status.json'
SCHEMA='request174-fixed-all-station-odd-signsum-original-compact-word-reference-v2'
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


def pick(value,keys):
    if not isinstance(value,dict):
        return {}
    return {key:value[key] for key in keys if key in value}


def scalar_fields(value):
    return {key:item for key,item in value.items()
            if item is None or isinstance(item,(str,bool,int,float))} if isinstance(value,dict) else {}


def exceptions_in(value,path='$'):
    found=[]
    if isinstance(value,dict):
        for key,item in value.items():
            here=path+'.'+key
            if ((key in ('exception','original_exception','traceback','complete_traceback')
                    and item is not None) or (key=='error' and isinstance(item,(str,dict)))):
                found.append(dict(path=here,original=item))
            elif key=='valid' and item is False:
                found.append(dict(path=here,original=False))
            elif isinstance(item,(dict,list)):
                found.extend(exceptions_in(item,here))
    elif isinstance(value,list):
        for i,item in enumerate(value):
            found.extend(exceptions_in(item,path+'['+str(i)+']'))
    return found


class Readback:
    def __init__(self):
        self.metadata_errors=[]
        self.fd_checks=0
        self.fd_levels=0
        self.fd_failures=[]

    def required(self,value,keys,path):
        if not isinstance(value,dict):
            self.metadata_errors.append(dict(path=path,reason='expected object'))
            return
        for key in keys:
            if key not in value:
                self.metadata_errors.append(dict(path=path+'.'+key,reason='required original field absent'))

    def matrix(self,value,rows,columns,path):
        good=isinstance(value,list) and len(value)==rows and all(isinstance(row,list) and len(row)==columns for row in value)
        if not good:
            self.metadata_errors.append(dict(path=path,reason='actual recorded matrix shape differs',
                expected=[rows,columns]))
        return value

    def vector(self,value,size,path):
        if not isinstance(value,list) or len(value)!=size:
            self.metadata_errors.append(dict(path=path,reason='actual recorded vector length differs',expected=size))
        return value

    def fd(self,levels,path):
        if levels is None:
            return dict(present=False)
        if not isinstance(levels,list) or len(levels)!=3:
            self.metadata_errors.append(dict(path=path,reason='expected all three original FD levels'))
            return dict(present=True,identity=identity(levels),metadata_incomplete=True)
        result=[]
        for i,level in enumerate(levels):
            self.required(level,['step','valid','maximum_relative_error','checks_by_parameter'],path+'['+str(i)+']')
            checks=level.get('checks_by_parameter',[])
            if not isinstance(checks,list):
                self.metadata_errors.append(dict(path=path,reason='FD checks are not a list'))
                checks=[]
            columns=[row.get('column') for row in checks]
            if columns!=list(range(10)):
                self.metadata_errors.append(dict(path=path,reason='all ten original FD columns not present in declared order',actual_columns=columns))
            failures=exceptions_in(checks,path+'['+str(i)+'].checks_by_parameter')
            self.fd_checks+=len(checks);self.fd_levels+=1
            self.fd_failures.extend(failures)
            result.append(dict(**pick(level,['step','valid','maximum_relative_error',
                'all_ten_columns_attempted','all_ten_columns_checked']),
                all_ten_column_indices_checked_in_order=columns==list(range(10)),
                complete_check_count=len(checks),
                complete_original_checks_identity=identity(checks),
                actual_failures_and_exceptions=failures,
                all_perturbed_parameter_and_equation_tables_transported=False))
        return result

    def description(self,value,path,binary64=False):
        if value is None:
            return dict(present=False)
        keys=['parameters','parameter_encoding','unweighted_full3_merit','low_equations_used',
            'unit_diagonal_defects','high_right_leak_max',
            'low_mode_trajectory_max_by_mode','scalar_node_and_mid_minimum_radius',
            'source_circle_node_and_mid_minimum_radius','source_circle_node_and_mid_minimum_beta2',
            'radius_cell_denominator_minimum_absolute','high_free_core_Schur_elimination_computed',
            'high_mode_nonresonance_proved','same_literal_coefficient_model_not_reformed_continuous_metric',
            'raw_original_table_accuracy_not_certified','derivative_accuracy_or_exact_rank_not_certified',
            'forward_primal_equation_words_equal_to_real_state','response_shape',
            'singular_values','first_three_column_singular_values','original_nine_column_singular_values',
            'numerical_parameter_condition','numerical_singular_values_are_not_a_transversality_proof',
            'actual_circle_R_minus_supplied_a_node_max','low_original_collocation_tangent_residual_max',
            'low_two_by_two_right_condition_max_by_mode','zero_tail_slope_J',
            'added_function_independence_does_not_assert_response_rank','new_g_family_not_a_relabelled_old_fixed_metric',
            'scalar_and_circle_queries_are_not_whole_interval_bounds']
        result=dict(present=True,**pick(value,keys))
        self.required(value,['parameters','low_equations_used','complete_first_order_right_residual'],path)
        self.vector(value.get('parameters'),10,path+'.parameters')
        self.vector(value.get('low_equations_used'),3,path+'.low_equations_used')
        full=value.get('complete_first_order_right_residual')
        self.vector(full,112,path+'.complete_first_order_right_residual')
        result['complete112_right_identity']=identity(full)
        if isinstance(full,list):
            result['first_three_actual_full112_right_rows']=full[:3]
        matrix_key='three_by_ten_parameter_jacobian' if binary64 else 'complete_three_by_ten_forward_response'
        self.required(value,[matrix_key],path)
        result[matrix_key]=self.matrix(value.get(matrix_key),3,10,path+'.'+matrix_key)
        fd_key='independent_real_parameter_difference_checks' if binary64 else 'independent_high_precision_real_parameter_difference_checks'
        self.required(value,[fd_key],path)
        result['original_three_step_complete_ten_axis_FD']=self.fd(value.get(fd_key),path+'.'+fd_key)
        response=value.get('forward_response_report')
        if response is not None:
            result['forward_response_report_identity']=identity(response)
            result['complete112_forward_identity']=pick(response,['complete112_response_canonical_sha256','forward_column_count'])
            if 'complete112_response' in response:
                self.matrix(response['complete112_response'],112,10,path+'.forward_response_report.complete112_response')
                result['complete112_forward_payload_identity']=identity(response['complete112_response'])
        result['full_original_description_identity']=identity(value)
        if 'terminal_Robin_terms' in value:
            result['terminal_Robin_terms_identity']=identity(value['terminal_Robin_terms'])
        return result

    def station_catalogue(self,value):
        if value is None:
            return dict(present=False)
        result=dict(present=True,complete_original_catalogue_report_identity=identity(value),
            original=pick(value,['schema','source','complete','stage','failure',
                'original_node_count','original_midpoint_count','actual_occurrence_grouping_complete',
                'visited_logical_occurrences','unvisited_node_indices','unvisited_midpoint_indices',
                'grouped_logical_occurrence_count','unique_physical_positions',
                'grouped_position_records_so_far','repeated_position_groups',
                'processed_unique_position_groups','unvisited_unique_group_ids',
                'allowed_candidate_count','skipped_group_count','response_error_count',
                'formed_finite_response_count','formed_nonzero_merit_action_count',
                'all_finite_formed_actions_zero','original_supports',
                'exact_position_and_occurrence_layout_sha256','complete_candidate_catalogue_sha256',
                'complete_skipped_groups_sha256','formed_weights_and_scores_not_exact_derivative_sign_or_rank_certificates',
                'same_position_general_value_jet_span_not_claimed','duplicate_occurrence_scope',
                'elapsed_wall_seconds']),
            complete_binding_identity=identity(value.get('binding')),
            candidate_and_weight_tables_transported=False)
        if value.get('complete'):
            self.required(value,['allowed_candidate_count','response_error_count',
                'unvisited_unique_group_ids','complete_candidate_catalogue_sha256'],'station_catalogue')
            if value.get('original_node_count')!=699 or value.get('original_midpoint_count')!=698:
                self.metadata_errors.append(dict(path='station_catalogue',reason='actual original699/698 occurrence coverage differs'))
        return result

    def combined_response(self,value):
        if value is None:
            return dict(present=False)
        result=dict(present=True,complete_original_response_identity=identity(value),
            original=pick(value,['schema','complete','adjoint_complete_three_response',
                'formed_local_forward_complete_three_response','actual_adjoint_minus_formed_forward',
                'complete112_response_canonical_sha256','complete_forward_cells',
                'direct_terminal_q_action','direct_terminal_three_contribution',
                'actual_full3_merit_directional_action','actual_full3_merit_directional_action_from_local_forward',
                'new_trial_or_acceptance_performed','action_sign_or_smallest_singular_value_certified']),
            complete_shape_binding_identity=identity(value.get('shape_binding')))
        for key in ('adjoint_complete_three_response','formed_local_forward_complete_three_response',
                    'actual_adjoint_minus_formed_forward'):
            self.vector(value.get(key),3,'combined_sampled_response.'+key)
        self.vector(value.get('complete112_formed_local_forward_response'),112,
            'combined_sampled_response.complete112_formed_local_forward_response')
        return result

    def original_nine(self,value):
        if value is None:
            return dict(present=False)
        compare=value.get('existing_original_forward_comparison',{})
        out=dict(present=True,complete_original_report_identity=identity(value),
            **pick(value,['schema','complete','original_nine_columns_attempted',
                'original_parameters_unchanged','no_new_control_basis_or_rank_claim']))
        key='complete_three_by_nine_adjoint_response'
        out[key]=self.matrix(value.get(key),3,9,'original_nine_adjoint_comparison.'+key)
        out['existing_original_forward_comparison']=pick(compare,[
            'provided','original_forward_recomputed_here','reference_canonical_sha256',
            'existing_reference_report_canonical_sha256','complete_original_three_by_nine_response',
            'actual_adjoint_minus_original_forward','complete112_original_response_canonical_sha256',
            'independent_full112_original_response_words_not_supplied',
            'discrepancy_is_not_a_new_acceptance_or_accuracy_gate'])
        if compare.get('provided'):
            for key in ('complete_original_three_by_nine_response','actual_adjoint_minus_original_forward'):
                self.matrix(compare.get(key),3,9,'existing_original_forward_comparison.'+key)
        full=value.get('complete112_by_nine_formed_local_forward_response')
        self.matrix(full,112,9,'original_nine_adjoint_comparison.complete112_by_nine_formed_local_forward_response')
        out['complete112_by_nine_formed_local_forward_identity']=identity(full)
        return out

    def trials(self,rows,original_nine_words):
        result=[]
        for i,row in enumerate(rows):
            path='trials['+str(i)+']'
            self.required(row,['trial','alpha','seed_parameters','original_Armijo_bound',
                'original_full3_slope','accepted'],path)
            self.vector(row.get('seed_parameters'),10,path+'.seed_parameters')
            out=pick(row,['trial','alpha','original_Armijo_bound','original_full3_slope',
                'accepted','actual_merit','actual_unit_equations',
                'actual_scalar_node_and_mid_minimum_radius','actual_circle_node_and_mid_minimum_beta2',
                'all_original_finite_primal_domain_guards_passed','reason','exception'])
            for key in ('seed_parameters','actual_parameters'):
                if key not in row:
                    continue
                words=row[key]
                self.vector(words,10,path+'.'+key)
                same=isinstance(words,list) and len(words)==10 and words[:9]==original_nine_words
                out[key+'_old_nine_words_equal_recorded_initial']=same
                out[key+'_new_shape_coefficient']=words[9] if isinstance(words,list) and len(words)==10 else None
                if not same:
                    # Preserve every unexpected value; compactness never hides a changed old coordinate.
                    out[key+'_complete_unexpected_words']=words
                    self.metadata_errors.append(dict(path=path+'.'+key,
                        reason='original nine words differ from the explicitly recorded fixed coordinates'))
            if 'actual_full112_right' in row:
                self.vector(row['actual_full112_right'],112,path+'.actual_full112_right')
                out['complete112_right_identity']=identity(row['actual_full112_right'])
            result.append(out)
        return result

    def zero_extension(self,value,path):
        if not isinstance(value,dict):
            self.metadata_errors.append(dict(path=path,reason='expected original zero-extension object'))
            return dict(present=False,original_identity=identity(value))
        key='fields' if 'fields' in value else 'array_readback'
        flag='encoded_words_equal' if key=='fields' else 'byte_identical'
        rows=value.get(key,[])
        if not isinstance(rows,list):
            self.metadata_errors.append(dict(path=path+'.'+key,reason='expected original comparison rows'))
            rows=[]
        failed=[row for row in rows if not isinstance(row,dict) or row.get(flag) is not True]
        return dict(present=True,original_identity=identity(value),
            original_scalar_flags=scalar_fields(value),
            comparison_rows=len(rows),comparison_rows_identity=identity(rows),
            all_recorded_rows_true=all(isinstance(row,dict) and row.get(flag) is True for row in rows),
            actual_nontrue_or_malformed_comparison_rows=failed,
            matching_array_descriptors_and_repeated_parameter_words_transported=False)


def compact_rules(directory):
    rows=[]
    if directory is not None and directory.is_dir():
        paths=sorted(directory.glob('sync-*-completed.json'))
        if (directory/'runner-result.json').is_file():
            paths.append(directory/'runner-result.json')
        for path in paths:
            value=json.loads(path.read_bytes())
            rows.append(dict(identity=file_identity(path),
                original=pick(value,['phase','status','returncode','return_code','exit_code',
                    'rules_changed','exception','traceback','source_commit','current_head','head',
                    'started','completed','elapsed_seconds','changed_paths','readme_blobs',
                    'latest_readme_blobs','period_seconds']),
                full_original_metadata_identity=identity(value)))
    return rows


def build(status,raw,directory,rules,compute_outcome):
    reader=Readback()
    if status.get('schema')!=PRODUCER_SCHEMA or status.get('source_sha256')!=PRODUCER_SHA:
        raise ValueError('Bind the independent actual174 producer, not a relabelled old-nine status')
    sources=status.get('consumed_source_sha256',{})
    if len(sources)!=46 or sources.get(PRODUCER)!=PRODUCER_SHA:
        raise ValueError('The full current46 producer source closure differs')
    fields=['phase','run_id','source_commit','actual_origin','parameter_recipe','policy',
        'input_sha256','original_nine_parameter_words','original_parent_radius',
        'parent_radius_not_used_as_new_shape_scale','decimal_digits','rounding',
        'original_mesh_nodes','field_and_tail_modes','frozen_shape_selected',
        'fixed_shape_selection','frozen_shape_summary','complete_fixed_shape_ledger','unvisited_real_trial_indices',
        'accepted_point_count','old_nine_parameters_relabelled_as_new','new_shape_parameter_index',
        'input_tables_not_reformed_in_high_precision','source_bound_original112_terminal_and699_chain_retained',
        'adjoint_comparison_is_diagnostic_not_new_gate',
        'high_mode_Schur_elimination_or_current_nonlinear_native_performed',
        'native_nonlinear_solver_called','nonzero_field_completed','success','diagnostic_completed',
        'resource_partial','stop_reason','exception','traceback','scientific_failure_not_inferred',
        'complete_final_consumers_not_reached','no_new_family_point_adopted',
        'actual_initial_merit','original_Armijo_coefficient_exact_binary64_lift',
        'actual_direction','final_ten_parameter_words','final_selected_shape_coefficient',
        'final_original_three_merit','high_precision_original_unit_stopping_tolerance_met',
        'high_precision_full112_linear_right_tolerance_met',
        'binary64_projection_original_unit_stopping_tolerance_met',
        'binary64_projection_full112_linear_right_tolerance_met',
        'initial_final_complete_ten_axis_three_step_Decimal_and_binary64_FD_attempted',
        'final_continuous_scalar_and453_circle_consumers_at_explicit_projection_only',
        'high_precision_complete_interval_domain_or_exact_derivative_accuracy_certified',
        'independent_ten_model_call_counts','fresh_original_nine_model_call_counts',
        'complete_original_event_ledger','elapsed_wall_seconds']
    out=dict(schema=SCHEMA,producer_schema=PRODUCER_SCHEMA,
        original_status=dict(bytes=len(raw),sha256=digest(raw),file=STATUS_NAME),
        readout_source=file_identity(__file__),producer_sha256=PRODUCER_SHA,
        **pick(status,fields),actual_compute_outcome=compute_outcome,
        complete_current_source_closure_count=len(sources),
        complete_current_source_closure_identity=identity(sources),
        actual_rule_sync=compact_rules(rules),
        readout_is_original_JSON_and_byte_operations_only=True,
        matrix_norm_FD_or_scientific_evaluation_recomputed_by_reader=False,
        raw_array_payloads_or_complete_FD_perturbation_tables_transported=False,
        one_compact_conclusion_not_a_raw_data_reconstruction=True,
        raw_Git_Release_or_artifact_retention=False,
        numerical_acceptance_not_changed_by_readback_checks=True)
    for name in ('original_nine_literal_binding','new_ten_literal_binding'):
        value=status.get(name)
        if value is not None:
            out[name]=dict(identity=identity(value),
                original=pick(value,['schema','source','base_primal_source_sha256','canonical_binding_sha256',
                    'parameter_dimension','parameter_order','old_parameter_columns','new_shape_column',
                    'decimal_digits','rounding','original_mesh_nodes','field_and_tail_modes',
                    'complete_original_tail_J_consumed',
                    'new_control_table_words_are_binary64_source_samples_then_exact_lifts',
                    'new_shape_table_formation_recomputed_in_Decimal',
                    'no_discrete_rounding_derivative_or_interval_accuracy_certificate',
                    'frozen_original_native_anchor_J_is_not_a_new_g_nonlinear_tail_response']))
    fresh=status.get('fresh_original_nine')
    if fresh is not None:
        out['fresh_original_nine']=pick(fresh,['parameters','equation','merit',
            'complete_three_by_nine_forward','original_primal_and_forward_equation_words_equal'])
        out['fresh_original_nine']['complete112_right_identity']=identity(fresh.get('full112_right'))
    for name in ('adjoint_build','adjoint_final_report'):
        value=status.get(name)
        if value is not None:
            out[name]=dict(identity=identity(value),original_scalars=scalar_fields(value),
                binding_identity=identity(value.get('binding')),
                selected_original_fields=pick(value,['counts','local_unvisited_suffix','reverse_unvisited_prefix',
                    'local_primal_word_mismatch_cells','terminal_original_equation_word_comparison',
                    'terminal_original_full112_word_comparison']))
    out['original_nine_adjoint_comparison']=reader.original_nine(status.get('original_nine_adjoint_comparison'))
    out['station_catalogue']=reader.station_catalogue(status.get('station_catalogue'))
    out['combined_sampled_response']=reader.combined_response(status.get('combined_sampled_response'))
    for name in ('zero_extension_literal_readback','zero_extension_binary64_readback'):
        if name in status:
            out[name]=reader.zero_extension(status[name],name)
    for name in ('selected_shape_actual_new_model_comparison','initial_projection_contract','final_projection_contract'):
        if name in status:
            out[name]=status[name]
    if 'selected_shape' in status:
        shape=status['selected_shape']
        out['selected_shape']=dict(identity=identity(shape),
            original=pick(shape,['schema','parameter_order','selected_shape','extra_shape',
                'parameter_count','parameter_dimension','new_shape_parameter_index',
                'base_family_source_sha256','source']))
    out['initial']=reader.description(status.get('initial'),'initial')
    out['final']=reader.description(status.get('final'),'final')
    out['initial_binary64_projection']=reader.description(status.get('initial_binary64_projection'),'initial_binary64_projection',True)
    out['final_binary64_projection']=reader.description(status.get('final_binary64_projection'),'final_binary64_projection',True)
    out['all_original_real_trials']=reader.trials(status.get('trials',[]),status.get('original_nine_parameter_words'))
    out['complete_planned_real_trial_rows']=[
        dict(index=i,visited=i<len(status.get('trials',[])),
             actual_trial=status['trials'][i].get('trial') if i<len(status.get('trials',[])) else None,
             unvisited_reason=None if i<len(status.get('trials',[])) else
                ('stopped after actual acceptance' if status.get('accepted_point_count') else status.get('stop_reason',status.get('phase'))))
        for i in range(20)]
    domain=status.get('complete_scalar_domain_at_binary64_projection')
    if domain is not None:
        out['complete_scalar_domain_at_binary64_projection']=dict(identity=identity(domain),
            original=pick(domain,['schema','covered_interval','bits','maximum_depth','leaf_count','split_cells',
                'unresolved_leaf_count','complete_declared_real_expression_domain_certified',
                'fresh_new_ten_control_identity','old_scalar_domain_certificate_reused',
                'exact_prefix_scalar_and_complete_stored_finite_Gauss_expression',
                'exact_scalar_derivative_compatibility_or_C2_interface_certificate',
                'literal_binary64_evaluation_roundoff_enclosed',
                'returned_ap_identified_with_derivative_of_finite_Gauss_a','source_returned_ap_used',
                'source_circle_R_and_full_Frenet_domain_covered_by_this_scalar_bound']),
            actual_failures_and_exceptions=exceptions_in(domain))
    circle=status.get('original_complete_circle_check_at_binary64_projection')
    if circle is not None:
        domain=circle.get('actual_domain',{})
        out['original_complete_circle_check_at_binary64_projection']=dict(identity=identity(circle),
            original=pick(circle,['original_full_reference_finite','reference_is_not_a_nonzero_parent',
                'reference_sha256','scalar_family_sha256','frozen_seven_added_shapes_square_check']),
            actual_domain={**scalar_fields(domain),
                'original_RMS_query_checks':domain.get('original_RMS_query_checks'),
                'full_original_domain_identity':identity(domain)},
            actual_failures_and_exceptions=exceptions_in(circle),
            complete_original_FFT_checks_identity=identity(circle.get('original_full_FFT_tangent_checks')))
    for name in ('fresh_extended_scalar_family','original_projection_call_trace',
                 'source_bound_family_views','source_bound_decimal_views'):
        if name in status:
            out[name+'_identity']=identity(status[name])
    if status.get('diagnostic_completed'):
        reader.required(status,['initial','final','initial_binary64_projection','final_binary64_projection',
            'complete_scalar_domain_at_binary64_projection','original_complete_circle_check_at_binary64_projection',
            'actual_direction','selected_shape_actual_new_model_comparison'],'completed_status')
        # No direction is a legitimate numerical outcome, not a missing scientific field.
        if 'actual_direction' not in status and status.get('stop_reason')=='Selected actual ten-model column supplies no finite nonzero strict merit slope':
            reader.metadata_errors=[row for row in reader.metadata_errors if row.get('path')!='completed_status.actual_direction']
        if reader.fd_checks!=120 or reader.fd_levels!=12:
            reader.metadata_errors.append(dict(path='complete_initial_final_ten_axis_FD',
                expected_checks=120,actual_checks=reader.fd_checks,expected_levels=12,actual_levels=reader.fd_levels))
        reader.required(status,['station_catalogue','fixed_shape_selection','frozen_shape_summary',
            'complete_fixed_shape_ledger','combined_sampled_response'],'completed_status')
        if not (status.get('station_catalogue') or {}).get('complete') or not status.get('frozen_shape_selected'):
            reader.metadata_errors.append(dict(path='station_catalogue',reason='completed experiment needs the complete fixed-function selection provenance'))
    out['original_readback_coverage']=dict(allowed_station_candidates=(status.get('station_catalogue') or {}).get('allowed_candidate_count'),
        complete_station_catalogue_report_present=status.get('station_catalogue') is not None,
        original_real_trial_rows=len(status.get('trials',[])),planned_real_trial_rows=20,
        fd_original_levels=reader.fd_levels,fd_original_column_checks=reader.fd_checks,
        fd_actual_failures_and_exceptions_count=len(reader.fd_failures),
        fd_actual_failures_and_exceptions_identity=identity(reader.fd_failures),
        fd_failures_full_original_details_location='each description / original_three_step_complete_ten_axis_FD / actual_failures_and_exceptions',
        metadata_errors=reader.metadata_errors,
        required_available_recorded_fields_complete=not reader.metadata_errors,
        large_original_tables_identified_but_not_transported=True,
        canonical_identity_scope='original JSON values; metadata-only serialization, no scientific recomputation',
        omitted_payload_categories=['matching zero-extension array descriptors',
            'repeated trial old-nine words', 'full station catalogue, weights, scores and defining piece table',
            'combined local-state and ratio-action tables',
            'terminal Robin detail tables', 'complete literal-binding array descriptor lists',
            'adjoint start/terminal weight matrices', 'complete FD perturbation tables'],
        full_scientific_tables_not_independently_read_by_downstream_recipient=True,
        no_accuracy_certificate_from_metadata_or_FD=True)
    reference_actual_repeated_words(out,status)
    return out,not reader.metadata_errors


def reference_actual_repeated_words(out,status):
    """Reference only canonical-byte-identical values already kept in this summary."""
    used=[]
    coverage=out.get('original_readback_coverage',{})
    complete_fd_coverage=(coverage.get('fd_original_column_checks')==120
                          and coverage.get('fd_original_levels')==12)
    out['actual_repeated_word_references']=dict(
        locations=used,
        complete_original_status_and_all_available_FD_checks_processed_first=True,
        all120_original_FD_checks_and12_levels_present=complete_fd_coverage,
        differing_or_exception_bearing_values_retained_in_full=True,
        no_scientific_value_or_gate_changed=True)
    if not complete_fd_coverage:
        return
    initial=status.get('initial')
    full=initial.get('complete_three_by_ten_forward_response') if isinstance(initial,dict) else None
    if (isinstance(full,list) and len(full)==3 and
            all(isinstance(row,list) and len(row)==10 for row in full)):
        left_nine=[row[:9] for row in full]
        locations=[(out.get('fresh_original_nine'),
                    'complete_three_by_nine_forward',
                    '#/fresh_original_nine/complete_three_by_nine_forward'),
                   ((out.get('original_nine_adjoint_comparison') or {}).get('existing_original_forward_comparison'),
                    'complete_original_three_by_nine_response',
                    '#/original_nine_adjoint_comparison/existing_original_forward_comparison/complete_original_three_by_nine_response')]
        for container,key,location in locations:
            if not isinstance(container,dict) or key not in container:
                continue
            actual=container[key]
            if encoded(actual)==encoded(left_nine):
                container[key]=dict(
                    schema='same-summary-byte-identical-reference-v1',
                    reference='#/initial/complete_three_by_ten_forward_response',
                    selection=dict(rows='all',column_start=0,column_stop_exclusive=9),
                    original_value_identity=identity(actual),
                    canonical_bytes_compared_equal=True)
                used.append(location)
    for final_name,initial_name in (('final','initial'),
                                    ('final_binary64_projection','initial_binary64_projection')):
        actual=status.get(final_name);reference=status.get(initial_name)
        # Complete originals, all FD columns and all exceptions were read first.
        # Keep any exception-bearing description fully expanded even if repeated.
        if (isinstance(actual,dict) and isinstance(reference,dict)
                and not exceptions_in(actual)
                and encoded(actual)==encoded(reference)):
            compact=out[final_name]
            out[final_name]=dict(present=True,
                schema='same-summary-byte-identical-reference-v1',
                reference='#/'+initial_name,
                complete_original_description_identity=identity(actual),
                compact_description_identity=identity(compact),
                canonical_complete_original_bytes_compared_equal=True,
                all_original_FD_columns_and_exceptions_counted_before_reference=True)
            used.append('#/'+final_name)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rules-directory',type=Path)
    p.add_argument('--compute-outcome',default='not-recorded')
    args=p.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    path=args.directory/STATUS_NAME
    complete=False
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
        out=dict(schema='request174-readback-exception-v1',exception=repr(error),
            traceback=traceback.format_exc(),readout_source=file_identity(__file__),
            original_status=file_identity(path) if path.is_file() else None,
            complete_original_readback_not_claimed=True,scientific_failure_not_inferred=True)
    raw=encoded(out)
    sections={name:len(encoded(value)) for name,value in out.items()}
    original_identity=dict(bytes=len(raw),sha256=digest(raw))
    print(encoded(dict(event='request174-compact-section-byte-counts',total=len(raw),
        section_UTF8_bytes=sections,hard_bound=LIMIT,complete_original_status_not_recomputed=True)).decode(),flush=True)
    if len(raw)>LIMIT:
        out=dict(schema='request174-compact-summary-over-budget-v1',
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
    print('BEGIN_VISIBLE174_COMPACT_SUMMARY',flush=True)
    print(raw.decode('ascii'),flush=True)
    print('END_VISIBLE174_COMPACT_SUMMARY',flush=True)
    print(encoded(dict(event='request174-compact-summary-identity',**receipt,
        hash_scope='ASCII JSON bytes excluding log separator LF')).decode(),flush=True)
    return 0 if complete else 70


if __name__=='__main__':
    raise SystemExit(main())
